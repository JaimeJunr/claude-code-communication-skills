"""Tests for the compatibility patches applied by scripts/sync.py.

    python3 -m unittest discover -s tests
"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("sync", ROOT / "scripts" / "sync.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

SKILL = """---
name: review-animations
description: Reviews animation code.
disable-model-invocation: true
---

Run `python3 scripts/search.py "x"` then `node scripts/tokens.cjs --dir src/`.
"""


class ApplyPatchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.skill_md = Path(self.tmp.name) / "SKILL.md"
        self.skill_md.write_text(SKILL)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_drop_keys_removes_frontmatter_key_and_keeps_the_rest(self) -> None:
        sync.apply_patch(self.skill_md, {"drop_keys": ["disable-model-invocation"]})
        text = self.skill_md.read_text()
        self.assertNotIn("disable-model-invocation", text)
        self.assertTrue(text.startswith("---\nname: review-animations\ndescription: Reviews animation code.\n---\n"))

    def test_drop_keys_fails_when_key_is_missing_upstream(self) -> None:
        with self.assertRaises(SystemExit):
            sync.apply_patch(self.skill_md, {"drop_keys": ["user-invocable"]})

    def test_replace_rewrites_body_only(self) -> None:
        sync.apply_patch(self.skill_md, {"replace": [{
            "pattern": r"\b(python3?|node) (scripts/[\w./-]+)",
            "with": r'\1 "${CLAUDE_SKILL_DIR}/\2"',
        }]})
        text = self.skill_md.read_text()
        self.assertIn('python3 "${CLAUDE_SKILL_DIR}/scripts/search.py" "x"', text)
        self.assertIn('node "${CLAUDE_SKILL_DIR}/scripts/tokens.cjs" --dir src/', text)
        self.assertIn("name: review-animations\n", text)

    def test_replace_fails_when_pattern_matches_nothing(self) -> None:
        with self.assertRaises(SystemExit):
            sync.apply_patch(self.skill_md, {"replace": [{"pattern": "ruby scripts/", "with": "x"}]})

    def test_description_and_drop_keys_combine(self) -> None:
        sync.apply_patch(self.skill_md, {
            "description": "Use ONLY when asked.",
            "drop_keys": ["disable-model-invocation"],
        })
        text = self.skill_md.read_text()
        self.assertIn('description: "Use ONLY when asked."\n', text)
        self.assertNotIn("disable-model-invocation", text)

    def test_block_description_preserves_following_metadata(self) -> None:
        self.skill_md.write_text('---\nname: caveman\ndescription: >\n  Broad trigger.\n  Whole session.\nlicense: MIT\nmetadata:\n  version: "1"\n---\n\nBody.\n')
        sync.apply_patch(self.skill_md, {"description": "Explicit current task."})
        text = self.skill_md.read_text()
        self.assertIn('description: "Explicit current task."\nlicense: MIT\nmetadata:\n  version: "1"', text)
        self.assertNotIn("Whole session", text)
        self.assertTrue(text.endswith("\nBody.\n"))

    def test_frontmatter_patch_sets_scalar_keys(self) -> None:
        sync.apply_patch(self.skill_md, {"frontmatter": {"disable-model-invocation": True, "user-invocable": True}})
        metadata = sync.frontmatter(self.skill_md.read_text())
        self.assertEqual(metadata["disable-model-invocation"], "true")
        self.assertEqual(metadata["user-invocable"], "true")
        self.assertEqual(self.skill_md.read_text().count("disable-model-invocation:"), 1)

    def test_model_invocable_patch_removes_upstream_restriction(self) -> None:
        sync.apply_patch(self.skill_md, {"model_invocable": True})
        self.assertEqual(self.skill_md.read_text(), SKILL.replace("disable-model-invocation: true\n", ""))
        # Reapplying also works when the upstream no longer contains the restriction.
        sync.apply_patch(self.skill_md, {"model_invocable": True})
        self.assertEqual(self.skill_md.read_text(), SKILL.replace("disable-model-invocation: true\n", ""))

    def test_replacement_rejects_changed_match_count(self) -> None:
        self.skill_md.write_text(SKILL + "Repeated rule.\nRepeated rule.\n")
        original = self.skill_md.read_bytes()
        with self.assertRaises(SystemExit):
            sync.apply_patch(self.skill_md, {"replace": [{"pattern": "Repeated rule.", "with": "Scoped rule.", "count": 1}]})
        self.assertEqual(self.skill_md.read_bytes(), original)


class FetchTest(unittest.TestCase):
    def test_local_source_uses_clone_without_network(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            local = root / "owner_repo"
            local.mkdir()
            with patch.object(sync, "run") as run:
                self.assertEqual(sync.fetch("owner/repo", "main", root, {}, root / "tmp"), local)
                run.assert_not_called()

    def test_missing_local_source_fails_without_network(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(sync, "run") as run:
                with self.assertRaises(SystemExit):
                    sync.fetch("owner/missing", "main", root, {}, root / "tmp")
                run.assert_not_called()


class SyncTreeTest(unittest.TestCase):
    def test_reference_sync_preserves_owned_files_and_is_reproducible(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sources = root / "clones"
            upstream = sources / "owner_recipe"
            reference = sources / "owner_reference"
            upstream.mkdir(parents=True)
            reference.mkdir()
            (upstream / "SKILL.md").write_text(SKILL)
            (upstream / "LICENSE").write_text("MIT recipe license\n")
            (reference / "prompt.md").write_text("Reference prompt.\n")
            (reference / "LICENSE").write_text("MIT reference license\n")
            plugins = root / "plugins"
            owned = plugins / "communication-stack"
            (owned / "output-styles").mkdir(parents=True)
            style = owned / "output-styles" / "eli5.md"
            style.write_text("Owned ELI5 must survive.\n")
            manifest = owned / ".claude-plugin" / "plugin.json"
            manifest.parent.mkdir()
            manifest.write_text('{"name": "communication-stack", "author": {"name": "Jaime Basso"}}\n')
            previous = plugins / "recipe" / "skills" / "stale" / "SKILL.md"
            previous.parent.mkdir(parents=True)
            previous.write_text("Stale skill.\n")
            stack = {
                "marketplace": {"name": "communication-stack", "owner": {"name": "Jaime Basso"},
                                "repository": "https://example.com/stack", "description": "Communication."},
                "local_plugins": [{"plugin": "communication-stack", "description": "Router.", "category": "productivity"}],
                "sources": [
                    {"id": "recipe", "repo": "owner/recipe", "ref": "main", "plugin": "recipe", "author": "Owner",
                     "license": "MIT", "license_files": ["LICENSE"], "description": "Recipe.", "category": "productivity",
                     "copy": [{"from": "SKILL.md", "to": "skills/recipe/SKILL.md"},
                              {"from": "LICENSE", "to": "skills/communication-stack/references/upstream/recipe/LICENSE",
                               "plugin": "communication-stack"}]},
                    {"id": "reference", "repo": "owner/reference", "ref": "main", "plugin": "communication-stack",
                     "author": "Reference owner", "license": "MIT", "license_files": ["LICENSE"],
                     "reference_only": True, "license_dir": "skills/communication-stack/references/upstream/reference",
                     "description": "Reference.", "category": "productivity",
                     "copy": [{"from": "prompt.md", "to": "skills/communication-stack/references/upstream/reference/prompt.md"}]}
                ]
            }
            with patch.multiple(sync, ROOT=root, PLUGINS=plugins, STACK=stack, LOCK_PATH=root / "UPSTREAM.lock"), \
                    patch.object(sync, "run", return_value="a" * 40):
                sync.sync(sources)
                first = {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob("*") if path.is_file()}
                sync.sync(sources)
                second = {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            self.assertEqual(first, second)
            self.assertEqual(style.read_text(), "Owned ELI5 must survive.\n")
            self.assertEqual(json.loads(manifest.read_text())["author"]["name"], "Jaime Basso")
            self.assertFalse(previous.exists())
            self.assertEqual((owned / stack["sources"][1]["copy"][0]["to"]).read_text(), "Reference prompt.\n")
            self.assertEqual((owned / stack["sources"][1]["license_dir"] / "LICENSE").read_text(), "MIT reference license\n")
            self.assertEqual((owned / "skills/communication-stack/references/upstream/recipe/LICENSE").read_text(), "MIT recipe license\n")
            self.assertFalse((plugins / "recipe" / "skills/communication-stack").exists())
            market = json.loads((root / ".claude-plugin" / "marketplace.json").read_text())
            self.assertEqual([entry["name"] for entry in market["plugins"]], ["communication-stack", "recipe"])
            lock = json.loads((root / "UPSTREAM.lock").read_text())
            self.assertEqual(len(lock), 2)
            self.assertEqual(lock["recipe"]["license"], "MIT")
            self.assertEqual(len(lock["recipe"]["files"]["SKILL.md"]), 64)


if __name__ == "__main__":
    unittest.main()
