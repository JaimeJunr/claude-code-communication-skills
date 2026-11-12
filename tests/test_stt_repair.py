"""Contract for the optional stt-repair plugin (speech-to-text repair)."""
import json
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_DIR = ROOT / "plugins" / "stt-repair"
SKILL_DIR = PLUGIN_DIR / "skills" / "stt-repair"


def skill_text() -> str:
    return " ".join((SKILL_DIR / "SKILL.md").read_text().split())


class SttRepairSkillTest(unittest.TestCase):
    def test_skill_lives_in_its_own_plugin_and_the_model_may_invoke_it(self) -> None:
        raw = (SKILL_DIR / "SKILL.md").read_text()
        metadata = yaml.safe_load(raw.split("---\n", 2)[1])
        self.assertEqual(metadata["name"], "stt-repair")
        self.assertTrue(metadata["description"])
        self.assertNotIn("disable-model-invocation", metadata)

    def test_description_names_the_triggers_the_user_described(self) -> None:
        raw = (SKILL_DIR / "SKILL.md").read_text()
        description = yaml.safe_load(raw.split("---\n", 2)[1])["description"]
        for trigger in ("speech-to-text", "/stt-repair", "Ambima 5"):
            with self.subTest(trigger=trigger):
                self.assertIn(trigger, description)

    def test_rules_that_prevent_over_correction_and_silent_guesses(self) -> None:
        text = skill_text()
        for rule in ("never guess silently", "never invent a name", "ask even if you are fairly sure",
                     "at most three spans", "read the glossary only now"):
            with self.subTest(rule=rule):
                self.assertIn(rule, text.lower())

    def test_glossary_is_a_file_read_on_demand_with_an_example(self) -> None:
        example = (SKILL_DIR / "glossary.example.md").read_text()
        self.assertIn("| Meant | Heard as | Note |", example)
        self.assertIn("~/.claude/stt-glossary.md", skill_text())

    def test_research_notes_cite_papers_with_links(self) -> None:
        research = (SKILL_DIR / "references" / "research.md").read_text()
        for arxiv_id in ("2309.15701", "2506.10779", "2508.20700", "2601.15397",
                         "2212.07769", "2410.13788", "2311.09469"):
            if arxiv_id == "2309.15701":
                continue  # HyPoradise is cited through its NeurIPS proceedings link
            with self.subTest(paper=arxiv_id):
                self.assertIn(arxiv_id, research)
        self.assertIn("proceedings.neurips.cc", research)

    def test_skill_is_an_optional_plugin_outside_the_core(self) -> None:
        core = ROOT / "plugins" / "communication-stack"
        self.assertFalse((core / "skills").exists(), "the core plugin must ship no skill")
        core_manifest = json.loads((core / ".claude-plugin" / "plugin.json").read_text())
        self.assertNotIn("stt-repair", core_manifest["description"])
        manifest = json.loads((PLUGIN_DIR / ".claude-plugin" / "plugin.json").read_text())
        self.assertEqual(manifest["name"], "stt-repair")
        self.assertIn("Optional", manifest["description"])
        self.assertTrue((PLUGIN_DIR / "LICENSE").is_file())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = {p["name"]: p for p in market["plugins"]}
        self.assertNotIn("stt-repair", entries["communication-stack"]["description"])
        self.assertIn("Optional", entries["stt-repair"]["description"])
        for readme in ("README.md", "README.pt-BR.md"):
            with self.subTest(readme=readme):
                text = (ROOT / readme).read_text()
                self.assertIn("| `stt-repair` | `stt-repair` | 1 |", text)
                self.assertIn("/plugin install stt-repair@communication-stack", text)

if __name__ == "__main__":
    unittest.main()
