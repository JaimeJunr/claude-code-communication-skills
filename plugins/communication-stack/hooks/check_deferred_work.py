"""Hook Stop: barra o fim do turno que adia trabalho sem deixar registro.

A regra "Deferred work" do Stack Focus sozinha não bastou: só 6% dos adiamentos tinham registro
(docs/GOALS.md, G6), e no Sussurro (2026-11-20) seis achados de revisão ficaram numa seção
"Fica para depois" da descrição do PR. O hook lê o turno atual no transcript e, se o texto
adia algo sem issue, ticket ou backlog no mesmo turno, devolve "block" uma única vez.
Qualquer falha de leitura sai sem bloquear: o hook nunca pode travar a sessão.
"""
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

DEFERRAL = re.compile(
    r"\b(?:"
    r"fica(?:m)?\s+(?:para|pra)\s+depois|deix(?:o|a|amos|ar)\s+(?:isso\s+|isto\s+)?(?:para|pra)\s+depois"
    r"|(?:para|pra|num|em)\s+(?:um\s+)?(?:próximo|proximo|outro)\s+PR|PR\s+(?:separado|à\s+parte|futuro)"
    r"|fora\s+do\s+escopo"
    r"|follow-?up\s+PR|next\s+PR|separate\s+PR|future\s+PR|out\s+of\s+scope"
    r"|(?:do|fix|handle|address|tackle)\s+(?:this|these|that|them|it)\s+later|for\s+later|left\s+for\s+later"
    r")\b",
    re.IGNORECASE,
)
RECORD_LINK = re.compile(
    r"github\.com/[^/\s]+/[^/\s]+/issues/\d+|gitlab\.[^\s]*/-/issues/\d+"
    r"|atlassian\.net/browse/[A-Z][A-Z0-9]+-\d+|linear\.app/[^\s]*/issue/",
)
RECORD_COMMAND = re.compile(r"\b(?:gh|glab)\s+issue\s+create\b|\bjira\s+issue\s+create\b")
RECORD_TOOL = re.compile(r"create.?(?:jira)?.?issue|issue.?create|add_list_record", re.IGNORECASE)
BACKLOG_FILE = re.compile(r"(?:backlog|todo)[^/]*\.md$", re.IGNORECASE)
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.DOTALL)

REASON = (
    "Deferred work without a record: this turn sets work aside ({phrase!r}) but created no issue, "
    "ticket or backlog entry. A list in a PR description, a commit, a code comment or this report "
    "is not a record: it is gone once the PR closes. Record each item now in the project's tracker "
    "(gh issue create, Jira, Linear; in your own repo, create it) and cite the links in the report. "
    "If the tracker is shared or unclear, show the ready-to-create title and body and name that "
    "pending creation in the closing line. No tracker: add it to a backlog file in the repo. If "
    "nothing was actually set aside, finish as is."
)


def is_real_prompt(entry: dict[str, Any]) -> bool:
    if entry.get("type") != "user" or entry.get("isSidechain"):
        return False
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return True
    return isinstance(content, list) and any(block.get("type") == "text" for block in content)


def current_turn(lines: Iterable[str]) -> list[dict[str, Any]]:
    turn: list[dict[str, Any]] = []
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if is_real_prompt(entry):
            turn = []
        elif entry.get("type") == "assistant" and not entry.get("isSidechain"):
            turn.append(entry)
    return turn


def blocks_of(turn: list[dict[str, Any]]) -> Iterable[dict[str, Any]]:
    for entry in turn:
        yield from (entry.get("message") or {}).get("content") or []


def tool_records(block: dict[str, Any]) -> bool:
    name = block.get("name", "")
    tool_input = block.get("input") or {}
    if RECORD_TOOL.search(name):
        return True
    if name in ("Write", "Edit", "MultiEdit") and BACKLOG_FILE.search(str(tool_input.get("file_path", ""))):
        return True
    return bool(RECORD_COMMAND.search(json.dumps(tool_input)))


def turn_records(turn: list[dict[str, Any]], text: str) -> bool:
    if RECORD_LINK.search(text):
        return True
    return any(block.get("type") == "tool_use" and tool_records(block) for block in blocks_of(turn))


def read_turn(payload: dict[str, Any]) -> tuple[list[dict[str, Any]], str]:
    try:
        lines = Path(payload["transcript_path"]).read_text(encoding="utf-8").splitlines()
    except (KeyError, OSError, TypeError):
        return [], str(payload.get("last_assistant_message") or "")
    turn = current_turn(lines)
    text = "\n".join(block.get("text", "") for block in blocks_of(turn) if block.get("type") == "text")
    return turn, text


def decide(payload: dict[str, Any]) -> dict[str, str] | None:
    # stop_hook_active: o hook já barrou uma vez neste fim de turno; barrar de novo vira loop.
    if payload.get("stop_hook_active"):
        return None
    turn, text = read_turn(payload)
    found = DEFERRAL.search(CODE.sub(" ", text))
    if not found or turn_records(turn, text):
        return None
    return {"decision": "block", "reason": REASON.format(phrase=found.group(0))}


def main() -> None:
    try:
        payload = json.loads(sys.stdin.read())
        decision = decide(payload) if isinstance(payload, dict) else None
    except Exception:  # o hook nunca pode quebrar a sessão
        return
    if decision:
        print(json.dumps(decision))


if __name__ == "__main__":
    main()
