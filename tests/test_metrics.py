"""Tests for scripts/metrics.py.

    python3 -m unittest discover -s tests
"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("metrics", ROOT / "scripts" / "metrics.py")
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)

STAMP = "2026-11-08T14:00:00.000Z"


def dump(entry: dict) -> str:
    """Compact like the real transcripts, which the reader's pre-filter relies on."""
    return json.dumps(entry, separators=(",", ":"))


def prompt(text: str = "oi") -> str:
    return dump({"type": "user", "message": {"role": "user", "content": text}})


def tool_result() -> str:
    block = {"type": "tool_result", "content": "ok"}
    return dump({"type": "user", "message": {"role": "user", "content": [block]}})


def reply(*blocks: dict, sidechain: bool = False, stamp: str = STAMP) -> str:
    return dump({"type": "assistant", "isSidechain": sidechain, "timestamp": stamp,
                       "message": {"role": "assistant", "content": list(blocks)}})


def text(words: str) -> dict:
    return {"type": "text", "text": words}


def tool(name: str, **tool_input: str) -> dict:
    return {"type": "tool_use", "name": name, "input": tool_input}


def style(name: str) -> str:
    return dump({"type": "attachment", "attachment": {
        "type": "output_style_instructions", "style": {"name": name}}})


class AnalyzeSessionTest(unittest.TestCase):
    def test_final_text_of_each_turn_is_counted_not_the_progress_lines(self) -> None:
        lines = [prompt(), reply(text("vou ler o arquivo agora")), tool_result(),
                 reply(text("pronto, dois arquivos mudaram"))]
        turns = metrics.analyze_session(lines)["turns"]
        self.assertEqual([t["words"] for t in turns], [4])

    def test_tool_results_do_not_open_a_new_turn(self) -> None:
        lines = [prompt(), reply(tool("Read")), tool_result(), reply(text("a b c")),
                 prompt(), reply(text("d e"))]
        self.assertEqual([t["words"] for t in metrics.analyze_session(lines)["turns"]], [3, 2])

    def test_subagent_messages_are_ignored(self) -> None:
        lines = [prompt(), reply(text("resposta do sub"), sidechain=True), reply(text("a b"))]
        self.assertEqual(metrics.analyze_session(lines)["turns"][0]["words"], 2)

    def test_style_comes_from_the_attachment_and_defaults_to_none(self) -> None:
        self.assertEqual(metrics.analyze_session([prompt(), reply(text("a"))])["turns"][0]["style"], "none")
        lines = [style(metrics.FOCUS_STYLE), prompt(), reply(text("a"))]
        self.assertEqual(metrics.analyze_session(lines)["turns"][0]["style"], metrics.FOCUS_STYLE)

    def test_style_attachment_without_a_style_is_ignored(self) -> None:
        empty = dump({"type": "attachment", "attachment": {
            "type": "output_style_instructions", "style": None}})
        lines = [style(metrics.FOCUS_STYLE), empty, prompt(), reply(text("a"))]
        self.assertEqual(metrics.analyze_session(lines)["turns"][0]["style"], metrics.FOCUS_STYLE)

    def test_each_turn_keeps_the_style_active_when_it_happened(self) -> None:
        lines = [prompt(), reply(text("a")), style(metrics.FOCUS_STYLE), prompt(), reply(text("b"))]
        turns = metrics.analyze_session(lines)["turns"]
        self.assertEqual([t["style"] for t in turns], ["none", metrics.FOCUS_STYLE])

    def test_each_turn_keeps_its_own_week(self) -> None:
        lines = [prompt(), reply(text("a")), prompt(), reply(text("b"), stamp="2026-11-15T10:00:00.000Z")]
        turns = metrics.analyze_session(lines)["turns"]
        self.assertEqual([t["week"] for t in turns], ["2026-W45", "2026-W46"])

    def test_all_text_blocks_of_the_final_message_are_counted(self) -> None:
        lines = [prompt(), reply(text("We will fix this later."), text("Tests passed."))]
        turn = metrics.analyze_session(lines)["turns"][0]
        self.assertEqual(turn["words"], 7)
        self.assertTrue(turn["deferred"])

    def test_visual_and_schedule_tools_are_flagged(self) -> None:
        lines = [prompt(), reply(tool("mcp__visualize__show_widget"), tool("CronCreate"),
                                 text("feito"))]
        turn = metrics.analyze_session(lines)["turns"][0]
        self.assertTrue(turn["widget"] and turn["schedule"])

    def test_deferral_without_record_is_flagged_and_with_record_is_not_lost(self) -> None:
        bare = [prompt(), reply(text("isso a gente faz mais tarde"))]
        kept = [prompt(), reply(tool("Bash", command="gh issue create -t x"),
                                text("isso fica pra depois, issue criada"))]
        self.assertEqual(metrics.analyze_session(bare)["turns"][0]["record"], False)
        turn = metrics.analyze_session(kept)["turns"][0]
        self.assertTrue(turn["deferred"] and turn["record"])

    def test_turn_without_final_text_is_skipped(self) -> None:
        self.assertEqual(metrics.analyze_session([prompt(), reply(tool("Read"))])["turns"], [])

    def test_week_label_comes_from_the_first_assistant_timestamp(self) -> None:
        self.assertEqual(metrics.analyze_session([prompt(), reply(text("a"))])["turns"][0]["week"], "2026-W45")


class SummarizeTest(unittest.TestCase):
    def turns(self) -> list:
        base = {"widget": False, "schedule": False, "deferred": False, "record": False}
        return [dict(base, words=10), dict(base, words=20, widget=True),
                dict(base, words=30, deferred=True, record=True),
                dict(base, words=40, deferred=True)]

    def test_rates_are_per_turn(self) -> None:
        s = metrics.summarize(self.turns())
        self.assertEqual((s["median_words"], s["widget_per_100"], s["deferred_pct"]), (25, 25, 50))
        self.assertEqual(s["deferred_recorded_pct"], 50)

    def test_no_deferrals_gives_nan_not_a_crash(self) -> None:
        s = metrics.summarize([dict(words=5, widget=False, schedule=False, deferred=False,
                                    record=False)])
        self.assertNotEqual(s["deferred_recorded_pct"], s["deferred_recorded_pct"])


class RenderTest(unittest.TestCase):
    def test_groups_by_style_and_hides_small_groups(self) -> None:
        turn = dict(words=5, widget=False, schedule=False, deferred=False, record=False,
                    week="2026-W45")
        turns = [dict(turn, style=metrics.FOCUS_STYLE)] * 3 + [dict(turn, style="none")]
        table = metrics.render(turns, "style", min_turns=2)
        self.assertIn("| Stack Focus | 3 |", table)
        self.assertNotIn("other styles", table)


class CollectTest(unittest.TestCase):
    def test_since_filters_turns_not_whole_sessions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "project"
            folder.mkdir()
            lines = [prompt(), reply(text("old")), prompt(),
                     reply(text("new"), stamp="2026-11-15T10:00:00.000Z")]
            (folder / "s.jsonl").write_text("\n".join(lines))
            turns = metrics.collect(Path(tmp), since="2026-W46")
        self.assertEqual([t["words"] for t in turns], [1])


if __name__ == "__main__":
    unittest.main()
