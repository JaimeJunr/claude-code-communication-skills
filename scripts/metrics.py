#!/usr/bin/env python3
"""Measure the Stack Focus style from real Claude Code transcripts.

Reads ~/.claude/projects/*/*.jsonl locally and prints aggregates only: no
message text leaves the machine or reaches the output. Sessions are grouped by
the output style recorded in the transcript, so sessions from before the style
existed form the baseline. Every metric is a proxy; docs/GOALS.md says which.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

FOCUS_STYLE = "communication-stack:Stack Focus"
WIDGET_TOOLS = {"mcp__visualize__show_widget"}
SCHEDULE_TOOLS = {"CronCreate", "ScheduleWakeup", "mcp__scheduled-tasks__create_scheduled_task"}
TRACKER_TOOLS = {"mcp__atlassian__createJiraIssue"}
TRACKER_BASH = re.compile(r"gh\s+issue\s+create")
# Phrases that park work without recording it. A proxy: it also matches
# harmless uses, so read the rate as a trend, not an exact count.
DEFERRAL = re.compile(
    r"(deixa(r|mos)?\s+(isso\s+)?(pra|para)\s+depois|fica(r)?\s+(pra|para)\s+depois|"
    r"vamos\s+deixar|mais\s+tarde|pr[óo]ximo\s+PR|fora\s+do\s+escopo|"
    r"out\s+of\s+scope|\blater\b|next\s+PR)",
    re.IGNORECASE,
)


def is_real_prompt(entry: dict[str, Any]) -> bool:
    """A user entry typed by the person, not a tool result or injected meta."""
    if entry.get("type") != "user" or entry.get("isMeta") or entry.get("isSidechain"):
        return False
    content = entry["message"]["content"]
    if isinstance(content, str):
        return True
    return any(block.get("type") in ("text", "image") for block in content)


def tool_flags(block: dict[str, Any]) -> dict[str, bool]:
    name = block.get("name", "")
    command = str(block.get("input", {}).get("command", "")) if name == "Bash" else ""
    return {
        "widget": name in WIDGET_TOOLS,
        "schedule": name in SCHEDULE_TOOLS,
        "record": name in TRACKER_TOOLS or bool(TRACKER_BASH.search(command)),
    }


def new_turn() -> dict[str, Any]:
    return {"text": "", "style": None, "week": "",
            "widget": False, "schedule": False, "record": False}


def absorb_assistant(turn: dict[str, Any], entry: dict[str, Any], style: str) -> None:
    """Fold one assistant message into the turn.

    Style and week are fixed by the turn's first assistant message. Text blocks
    of one message are joined; a later message replaces an earlier one, which
    drops progress lines and keeps the final message.
    """
    blocks = entry["message"]["content"]
    texts = [b["text"] for b in blocks if b.get("type") == "text" and b.get("text", "").strip()]
    if texts:
        turn["text"] = "\n".join(texts)
    for block in blocks:
        if block.get("type") == "tool_use":
            for key, hit in tool_flags(block).items():
                turn[key] = turn[key] or hit
    if turn["style"] is None:
        turn["style"] = style
        turn["week"] = iso_week(entry.get("timestamp", ""))


def finish_turn(turn: dict[str, Any]) -> dict[str, Any] | None:
    """Reduce a turn to numbers; a turn with no final text is skipped."""
    if not turn["text"]:
        return None
    return {
        "style": turn["style"],
        "week": turn["week"],
        "words": len(turn["text"].split()),
        "widget": turn["widget"],
        "schedule": turn["schedule"],
        "deferred": bool(DEFERRAL.search(turn["text"])),
        "record": turn["record"],
    }


def iter_entries(lines: Iterable[str]) -> Iterable[dict[str, Any]]:
    for line in lines:
        if '"type":"assistant"' not in line and '"type":"user"' not in line \
                and "output_style_instructions" not in line:
            continue
        try:
            yield json.loads(line)
        except json.JSONDecodeError:
            continue


def analyze_session(lines: Iterable[str]) -> dict[str, Any]:
    """Return {"turns"} for one transcript; each turn carries its own style and week."""
    style, turns, turn = "none", [], None
    for entry in iter_entries(lines):
        kind = entry.get("type")
        if kind == "attachment" and entry["attachment"].get("type") == "output_style_instructions":
            style = (entry["attachment"].get("style") or {}).get("name") or style
        elif kind == "assistant" and not entry.get("isSidechain") and turn is not None:
            absorb_assistant(turn, entry, style)
        elif is_real_prompt(entry):
            done = finish_turn(turn) if turn else None
            turns.extend([done] if done else [])
            turn = new_turn()
    done = finish_turn(turn) if turn else None
    turns.extend([done] if done else [])
    return {"turns": turns}


def iso_week(timestamp: str) -> str:
    try:
        year, week, _ = datetime.fromisoformat(timestamp.replace("Z", "+00:00")).isocalendar()
    except ValueError:
        return ""
    return f"{year}-W{week:02d}"


def summarize(turns: list[dict[str, Any]]) -> dict[str, float]:
    words = sorted(t["words"] for t in turns)
    deferred = [t for t in turns if t["deferred"]]
    per100 = lambda key: 100 * sum(t[key] for t in turns) / len(turns)
    return {
        "turns": len(turns),
        "median_words": statistics.median(words),
        "p90_words": words[int(0.9 * (len(words) - 1))],
        "widget_per_100": per100("widget"),
        "schedule_per_100": per100("schedule"),
        "deferred_pct": 100 * len(deferred) / len(turns),
        "deferred_recorded_pct": (100 * sum(t["record"] for t in deferred) / len(deferred))
        if deferred else float("nan"),
    }


def group_key(turn: dict[str, Any], by: str) -> str:
    focus = "Stack Focus" if turn["style"] == FOCUS_STYLE else "other styles"
    return focus if by == "style" else f"{focus} {turn['week']}"


def collect(projects: Path, since: str) -> list[dict[str, Any]]:
    """All turns from every transcript whose own week is at or after `since`."""
    turns: list[dict[str, Any]] = []
    for path in projects.glob("*/*.jsonl"):
        with path.open(errors="ignore") as handle:
            turns.extend(t for t in analyze_session(handle)["turns"] if t["week"] >= since)
    return turns


def render(turns: list[dict[str, Any]], by: str, min_turns: int) -> str:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for turn in turns:
        groups[group_key(turn, by)].append(turn)
    header = ("| Group | Turns | Median words | P90 words | Visuals /100 | "
              "Schedules /100 | Deferral phrase % | Deferrals recorded % |\n"
              "|---|---|---|---|---|---|---|---|")
    rows = []
    for name in sorted(groups):
        if len(groups[name]) < min_turns:
            continue
        s = summarize(groups[name])
        rows.append(f"| {name} | {s['turns']} | {s['median_words']:.0f} | {s['p90_words']} | "
                    f"{s['widget_per_100']:.1f} | {s['schedule_per_100']:.1f} | "
                    f"{s['deferred_pct']:.1f} | {s['deferred_recorded_pct']:.0f} |")
    return "\n".join([header, *rows])


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--projects", type=Path, default=Path.home() / ".claude" / "projects")
    parser.add_argument("--by", choices=("style", "week"), default="style")
    parser.add_argument("--since", default="", help="ISO week, e.g. 2026-W40")
    parser.add_argument("--min-turns", type=int, default=20)
    args = parser.parse_args(argv)
    if not args.projects.is_dir():
        print(f"metrics: {args.projects} is not a directory", file=sys.stderr)
        return 2
    print(render(collect(args.projects, args.since), args.by, args.min_turns))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
