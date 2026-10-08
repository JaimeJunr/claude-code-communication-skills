"""Repository contracts for the communication stack, including non-empty scans."""
import importlib.util
import json
import hashlib
import re
import unittest
from pathlib import Path

import tiktoken
import yaml

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("stack_token_budget", ROOT / "scripts" / "token_budget.py")
token_budget = importlib.util.module_from_spec(spec)
spec.loader.exec_module(token_budget)

STYLE_FILES = {"clear.md", "eli5.md", "adhd.md", "caveman-lite.md", "focus.md"}
PLUGIN_NAMES = {"communication-stack", "caveman", "i-have-adhd", "humanizer", "no-ai-slop", "eli5-ste"}


def styles():
    return sorted((ROOT / "plugins").glob("*/output-styles/*.md"))


class StackContractTest(unittest.TestCase):
    def test_every_output_style_keeps_coding_and_never_forces_selection(self):
        candidates = styles()
        self.assertTrue(candidates, "scanned 0 output styles; expected 5")
        for path in candidates:
            with self.subTest(file=str(path.relative_to(ROOT))):
                text = path.read_text()
                self.assertTrue(text.startswith("---\n"), "missing leading frontmatter")
                blocks = text.split("---\n", 2)
                self.assertEqual(len(blocks), 3, "missing closing frontmatter")
                metadata = yaml.safe_load(blocks[1])
                self.assertIsInstance(metadata, dict)
                self.assertTrue(metadata.get("name"))
                self.assertTrue(metadata.get("description"))
                self.assertIs(metadata.get("keep-coding-instructions"), True)
                self.assertIs(metadata.get("force-for-plugin"), False)

    def test_exactly_five_output_styles_exist(self):
        candidates = styles()
        self.assertEqual(len(candidates), 5, f"scanned {len(candidates)} output styles; expected 5")
        self.assertEqual({path.name for path in candidates}, STYLE_FILES)
        self.assertEqual({path.parent.parent.name for path in candidates}, {"communication-stack"})

    def test_focus_style_is_named_stack_focus(self):
        path = ROOT / "plugins" / "communication-stack" / "output-styles" / "focus.md"
        self.assertTrue(path.is_file(), f"{path}: missing")
        metadata = yaml.safe_load(path.read_text().split("---\n", 2)[1])
        self.assertEqual(metadata.get("name"), "Stack Focus")

    def test_no_plugin_ships_hooks(self):
        plugins = sorted(path for path in (ROOT / "plugins").glob("*") if path.is_dir())
        self.assertEqual({path.name for path in plugins}, PLUGIN_NAMES,
                         f"scanned {len(plugins)} plugin directories; expected 6")
        for plugin in plugins:
            with self.subTest(plugin=plugin.name):
                hooks = [path for path in plugin.rglob("*") if path.is_dir() and path.name == "hooks"]
                self.assertEqual(hooks, [])
                manifest = plugin / ".claude-plugin" / "plugin.json"
                self.assertTrue(manifest.is_file(), f"{manifest}: missing manifest")
                self.assertNotIn("hooks", json.loads(manifest.read_text()))

    def test_caveman_contains_only_the_base_skill(self):
        plugin = ROOT / "plugins" / "caveman"
        skills = sorted(plugin.rglob("SKILL.md"))
        self.assertEqual([path.relative_to(plugin).as_posix() for path in skills],
                         ["skills/caveman/SKILL.md"],
                         f"scanned {len(skills)} caveman skills; expected only the base skill")

    def test_every_source_license_and_notice_exists_after_sync(self):
        stack = json.loads((ROOT / "stack.json").read_text())
        self.assertEqual(len(stack["sources"]), 6)
        for source in stack["sources"]:
            with self.subTest(source=source["id"]):
                self.assertTrue(source.get("license"))
                self.assertTrue(source.get("license_files"))
                target = ROOT / "plugins" / source["plugin"] / source.get("license_dir", "")
                for name in source["license_files"]:
                    path = target / Path(name).name
                    self.assertTrue(path.is_file(), f"{source['id']}: missing {path.relative_to(ROOT)}")
                    self.assertGreater(path.stat().st_size, 0)

    def test_hand_written_plugin_token_budget(self):
        plugin = ROOT / "plugins" / "communication-stack"
        router = plugin / "skills" / "communication-stack" / "SKILL.md"
        self.assertTrue(router.is_file(), "scanned 0 routers; expected communication-stack/SKILL.md")
        self.assertGreater(router.stat().st_size, 0)
        candidates = token_budget.budgeted_files(plugin)
        self.assertEqual(len(candidates), 6, f"scanned {len(candidates)} budgeted files; expected router + 5 styles")
        encoding = tiktoken.get_encoding("o200k_base")
        self.assertEqual(token_budget.over_budget(
            [plugin], lambda text: len(encoding.encode(text)), token_budget.LIMITS), [])

    def test_no_skill_disables_model_invocation(self):
        candidates = sorted((ROOT / "plugins").rglob("SKILL.md"))
        self.assertEqual(len(candidates), 7, f"scanned {len(candidates)} skills; expected 7")
        violations = [path.relative_to(ROOT).as_posix() for path in candidates
                      if "disable-model-invocation" in path.read_text()]
        self.assertEqual(violations, [], f"scanned {len(candidates)} skills; violations: {violations}")

    def test_patches_do_not_disable_model_invocation(self):
        stack = json.loads((ROOT / "stack.json").read_text())
        candidates = [(source["id"], patch) for source in stack["sources"]
                      for patch in source.get("patches", [])]
        self.assertEqual(len(candidates), 7, f"scanned {len(candidates)} patches; expected 7")
        violations = [source for source, patch in candidates
                      if "disable-model-invocation" in json.dumps(patch)]
        self.assertEqual(violations, [], f"scanned {len(candidates)} patches; violations: {violations}")

    def test_router_invokes_one_namespaced_skill_without_install_path_discovery(self):
        router = ROOT / "plugins/communication-stack/skills/communication-stack/SKILL.md"
        self.assertTrue(router.is_file(), "scanned 0 routers; expected 1")
        text = router.read_text()
        forbidden = ("installed_plugins.json", "installPath", "claude plugin list")
        violations = [term for term in forbidden if term in text]
        self.assertEqual(violations, [], f"scanned 1 router for {len(forbidden)} terms; violations: {violations}")
        self.assertIn("Invoke the chosen skill via the Skill tool", text)
        self.assertIn("namespaced name", text)
        self.assertIn("Never invoke more than one editor per task", text)
        self.assertIn("/plugin install <name>@communication-stack", text)

    def test_leaf_descriptions_require_explicit_request_or_router_selection(self):
        candidates = sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md"))
        leaves = [path for path in candidates if path.parent.name != "communication-stack"]
        self.assertEqual(len(leaves), 6, f"scanned {len(leaves)} leaf descriptions; expected 6")
        for path in leaves:
            with self.subTest(file=str(path.relative_to(ROOT))):
                metadata = yaml.safe_load(path.read_text().split("---\n", 2)[1])
                self.assertIn("Load only on explicit request or when the communication-stack router selects it.",
                              metadata["description"])

    def test_owned_eli5_is_exactly_the_fixed_design_version(self):
        design = (ROOT / "docs/research/DESIGN.md").read_text()
        section = design.split("### Our hand-written ELI5 output style", 1)[1].split("### Router and manual recipes", 1)[0]
        expected = re.search(r"~~~markdown\n(.*?)\n~~~", section, re.S).group(1) + "\n"
        path = ROOT / "plugins/communication-stack/output-styles/eli5.md"
        self.assertEqual(path.read_text(), expected)

    def test_lock_covers_sources_and_verbatim_copies(self):
        stack = json.loads((ROOT / "stack.json").read_text())
        lock = json.loads((ROOT / "UPSTREAM.lock").read_text())
        self.assertEqual(len(stack["sources"]), 6)
        self.assertEqual(set(lock), {source["id"] for source in stack["sources"]})
        checked = 0
        for source in stack["sources"]:
            info = lock[source["id"]]
            self.assertRegex(info["commit"], r"^[0-9a-f]{40}$")
            self.assertEqual(info["ref"], "main")
            self.assertEqual(info["license"], source["license"])
            expected = {item["from"] for item in source["copy"]} | set(source["license_files"])
            self.assertEqual(set(info["files"]), expected)
            patched = {patch["file"] for patch in source.get("patches", [])}
            copies = [(ROOT / "plugins" / item.get("plugin", source["plugin"]) / item["to"], item["from"])
                      for item in source["copy"] if item["to"] not in patched]
            copies += [(ROOT / "plugins" / source["plugin"] / source.get("license_dir", "") / Path(name).name, name)
                       for name in source["license_files"]]
            for path, origin in copies:
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), info["files"][origin])
                checked += 1
        self.assertGreaterEqual(checked, 11, f"scanned {checked} verbatim copies; expected at least 11")


if __name__ == "__main__":
    unittest.main()
