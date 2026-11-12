"""Repository contracts for the communication stack, including non-empty scans."""
import importlib.util
import json
import os
import subprocess
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

STYLE_FILES = {"focus.md"}
PLUGIN_NAMES = {"communication-stack", "communication-router", "caveman", "i-have-adhd", "humanizer", "no-ai-slop", "eli5-ste"}


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

    def test_exactly_one_output_style_exists(self):
        candidates = styles()
        self.assertEqual(len(candidates), 1, f"scanned {len(candidates)} output styles; expected 1")
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
                         f"scanned {len(plugins)} plugin directories; expected 7")
        # Hooks de estilo dos upstreams (caveman, ADHD...) reinjetariam o output style; só o
        # communication-stack pode ter hook, e só o de data/hora (testado abaixo).
        for plugin in plugins:
            with self.subTest(plugin=plugin.name):
                hooks = [path for path in plugin.rglob("*") if path.is_dir() and path.name == "hooks"]
                expected = [plugin / "hooks"] if plugin.name == "communication-stack" else []
                self.assertEqual(hooks, expected)
                manifest = plugin / ".claude-plugin" / "plugin.json"
                self.assertTrue(manifest.is_file(), f"{manifest}: missing manifest")
                self.assertNotIn("hooks", json.loads(manifest.read_text()))

    def test_stack_ships_only_the_context_hooks(self):
        hooks_dir = ROOT / "plugins" / "communication-stack" / "hooks"
        self.assertEqual(sorted(path.name for path in hooks_dir.iterdir()),
                         ["hooks.json", "inject-datetime.sh", "inject-environment.sh"])
        config = json.loads((hooks_dir / "hooks.json").read_text())["hooks"]
        commands = {event: [hook["command"] for entry in entries for hook in entry["hooks"]]
                    for event, entries in config.items()}
        datetime_cmd = 'bash "${CLAUDE_PLUGIN_ROOT}/hooks/inject-datetime.sh"'
        environment_cmd = 'bash "${CLAUDE_PLUGIN_ROOT}/hooks/inject-environment.sh"'
        self.assertEqual(commands, {"SessionStart": [environment_cmd],
                                    "UserPromptSubmit": [datetime_cmd, environment_cmd]})

    def test_datetime_hook_injects_only_the_current_time(self):
        script = ROOT / "plugins" / "communication-stack" / "hooks" / "inject-datetime.sh"
        env = {"PATH": os.environ["PATH"], "TZ": "America/Sao_Paulo"}
        result = subprocess.run(["bash", str(script)], input="{}", capture_output=True, text=True, env=env, check=True)
        output = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], "UserPromptSubmit")
        self.assertRegex(output["additionalContext"],
                         r"^Now: (Mon|Tue|Wed|Thu|Fri|Sat|Sun) \d{4}-\d{2}-\d{2} \d{2}:\d{2} -0300$")

    def test_datetime_hook_ignores_the_user_locale(self):
        script = ROOT / "plugins" / "communication-stack" / "hooks" / "inject-datetime.sh"
        env = {"PATH": os.environ["PATH"], "TZ": "UTC", "LC_ALL": "pt_BR.UTF-8", "LANG": "pt_BR.UTF-8"}
        result = subprocess.run(["bash", str(script)], input="{}", capture_output=True, text=True, env=env, check=True)
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        self.assertRegex(context, r"^Now: (Mon|Tue|Wed|Thu|Fri|Sat|Sun) .* \+0000$")

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
        plugin = ROOT / "plugins" / "communication-router"
        router = plugin / "skills" / "communication-stack" / "SKILL.md"
        self.assertTrue(router.is_file(), "scanned 0 routers; expected communication-stack/SKILL.md")
        self.assertGreater(router.stat().st_size, 0)
        candidates = token_budget.budgeted_files(plugin)
        self.assertEqual(len(candidates), 1, f"scanned {len(candidates)} budgeted files; expected the router")
        style_plugin = ROOT / "plugins" / "communication-stack"
        self.assertEqual(len(token_budget.budgeted_files(style_plugin)), 2, "expected 1 style and the stt-repair skill")
        encoding = tiktoken.get_encoding("o200k_base")
        self.assertEqual(token_budget.over_budget(
            [plugin, style_plugin], lambda text: len(encoding.encode(text)), token_budget.LIMITS), [])

    def test_no_skill_disables_model_invocation(self):
        candidates = sorted((ROOT / "plugins").rglob("SKILL.md"))
        self.assertEqual(len(candidates), 8, f"scanned {len(candidates)} skills; expected 8")
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

    def test_router_invokes_namespaced_skills_without_install_path_discovery(self):
        router = ROOT / "plugins/communication-router/skills/communication-stack/SKILL.md"
        self.assertTrue(router.is_file(), "scanned 0 routers; expected 1")
        text = router.read_text()
        forbidden = ("installed_plugins.json", "installPath", "claude plugin list")
        violations = [term for term in forbidden if term in text]
        self.assertEqual(violations, [], f"scanned 1 router for {len(forbidden)} terms; violations: {violations}")
        self.assertIn("Invoke each listed skill via the Skill tool", " ".join(text.split()))
        self.assertIn("namespaced name", text)
        self.assertIn("Only one editor rewrites", " ".join(text.split()))
        self.assertIn("/plugin install <name>@communication-stack", text)

    def test_leaf_descriptions_require_explicit_request_or_router_selection(self):
        candidates = sorted((ROOT / "plugins").glob("*/skills/*/SKILL.md"))
        # stt-repair is the one skill that is always installed and model-invoked; it is exempt here.
        leaves = [path for path in candidates if path.parent.name not in {"communication-stack", "stt-repair"}]
        self.assertEqual(len(leaves), 6, f"scanned {len(leaves)} leaf descriptions; expected 6")
        for path in leaves:
            with self.subTest(file=str(path.relative_to(ROOT))):
                metadata = yaml.safe_load(path.read_text().split("---\n", 2)[1])
                self.assertIn("Load only on explicit request or when the communication-stack router selects it.",
                              metadata["description"])

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




class StateRoutingAndFocusRulesTest(unittest.TestCase):
    ROUTER = ROOT / "plugins" / "communication-router" / "skills" / "communication-stack" / "SKILL.md"
    FOCUS = ROOT / "plugins" / "communication-stack" / "output-styles" / "focus.md"

    def router_parts(self):
        text = self.ROUTER.read_text()
        metadata = yaml.safe_load(text.split("---\n", 2)[1])
        return metadata["description"], text

    def test_router_description_triggers_on_reader_states(self):
        description, _ = self.router_parts()
        for cue in ("confused", "tired", "lost context", "hurry", "stuck", "frustrated",
                    "small screen", "depth"):
            with self.subTest(cue=cue):
                self.assertIn(cue, description)

    def section(self, title):
        _, text = self.router_parts()
        self.assertIn(f"## {title}", text)
        return text.split(f"## {title}", 1)[1].split("\n## ", 1)[0]

    def table_rows(self, title):
        rows = [line for line in self.section(title).splitlines()
                if line.startswith("| ") and "---" not in line][1:]
        return {row.split("|")[1].strip(): row.split("|")[2].strip() for row in rows}

    def test_reply_layers_are_one_skill_each(self):
        layers = self.table_rows("Reply layers")
        self.assertEqual(set(layers), {"Words", "Structure", "Length"})
        self.assertIn("`eli5-ste:eli5`", layers["Words"])
        self.assertIn("`i-have-adhd:i-have-adhd`", layers["Structure"])
        self.assertIn("`caveman:caveman`", layers["Length"])
        self.assertIn("correctness, then understanding", " ".join(self.section("Reply layers").split()))

    def test_reader_states_map_to_layer_combinations(self):
        states = self.table_rows("Reader state")
        self.assertGreaterEqual(len(states), 10, f"scanned {len(states)} states; expected at least 10")
        allowed = {"`eli5-ste:eli5`", "`i-have-adhd:i-have-adhd`", "`caveman:caveman`"}

        def skills(prefix):
            [row] = [v for k, v in states.items() if k.startswith(prefix)]
            return {token for token in allowed if token in row}

        self.assertEqual(skills("Confused (\""), {"`eli5-ste:eli5`"})
        self.assertEqual(skills("Tired"), allowed)
        self.assertEqual(skills("Confused and tired"), {"`eli5-ste:eli5`", "`i-have-adhd:i-have-adhd`"})
        self.assertEqual(skills("In a hurry"), {"`caveman:caveman`"})
        self.assertEqual(skills("Back to normal"), set())

    def test_reader_state_has_persistence_and_signal_rules(self):
        text = " ".join(self.section("Reader state").split())
        for rule in ("Lost context first", "needs two in a row", "Never guess a state",
                     "until the reader says otherwise", "Do not announce the layers"):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)

    def test_drafts_pick_editors_by_destination(self):
        editors = self.table_rows("Edit a draft")
        self.assertGreaterEqual(len(editors), 4, f"scanned {len(editors)} destinations; expected at least 4")

        def row(prefix):
            [value] = [v for k, v in editors.items() if k.startswith(prefix)]
            return value

        site = row("Site")
        self.assertIn("`no-ai-slop:no-ai-slop`", site)
        self.assertNotIn("`humanizer:humanizer`", site)
        email = row("Email")
        self.assertLess(email.index("`no-ai-slop:no-ai-slop` detect"), email.index("`humanizer:humanizer`"),
                        "email: no-ai-slop must detect before humanizer rewrites")
        text = " ".join(self.section("Edit a draft").split())
        self.assertIn("Only one editor rewrites", text)
        self.assertIn("ask once", text)

    def test_focus_style_carries_the_round_two_rules(self):
        text = " ".join(self.FOCUS.read_text().split())
        for rule in ("No label stamps", "Resumo:", "unless the user already used it",
                     "list exactly that many", "list problems first", "3 most important points",
                     "one short sentence"):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)

    def test_focus_style_records_deferred_work_in_a_tracker(self):
        text = " ".join(self.FOCUS.read_text().split())
        for rule in ("Deferred work:", "same turn", "tracker the project uses",
                     "ready-to-create title and body",
                     "pending creation in the closing line"):
            with self.subTest(rule=rule):
                self.assertIn(rule, text)


ENVIRONMENT_HOOK = ROOT / "plugins" / "communication-stack" / "hooks" / "inject-environment.sh"


class EnvironmentHookTest(unittest.TestCase):
    def run_hook(self, cwd, event, session="s1"):
        env = {"PATH": os.environ["PATH"], "TMPDIR": str(self.tmp), "HOME": str(self.tmp)}
        payload = json.dumps({"session_id": session, "hook_event_name": event, "cwd": str(cwd)})
        result = subprocess.run(["bash", str(ENVIRONMENT_HOOK)], input=payload, capture_output=True,
                                text=True, env=env, cwd=cwd, check=True)
        if not result.stdout.strip():
            return None
        output = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual(output["hookEventName"], event)
        return output["additionalContext"]

    def setUp(self):
        import tempfile
        self._dir = tempfile.TemporaryDirectory()
        self.tmp = Path(self._dir.name)
        self.repo = self.tmp / "demo-repo"
        self.repo.mkdir()
        git = ["git", "-C", str(self.repo), "-c", "user.name=t", "-c", "user.email=t@t"]
        subprocess.run(git + ["init", "-q", "-b", "feature-x"], check=True)
        (self.repo / "a.txt").write_text("a")
        subprocess.run(git + ["add", "."], check=True)
        subprocess.run(git + ["commit", "-qm", "init"], check=True)
        (self.repo / "b.txt").write_text("b")

    def tearDown(self):
        self._dir.cleanup()

    def test_reports_repo_branch_and_changed_files_without_emoji(self):
        context = self.run_hook(self.repo, "SessionStart")
        self.assertIn("Repo: demo-repo | Branch: feature-x | Uncommitted files: 1", context)
        self.assertFalse(re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", context), context)

    def test_outside_git_reports_machine_only(self):
        outside = self.tmp / "plain"
        outside.mkdir()
        context = self.run_hook(outside, "SessionStart")
        self.assertNotIn("Repo:", context or "")

    def test_reports_machine_load_and_memory_on_linux(self):
        if not Path("/proc/meminfo").is_file():
            self.skipTest("machine stats read /proc (Linux only)")
        context = self.run_hook(self.repo, "SessionStart")
        self.assertRegex(context, r"Machine: load [\d.]+/\d+ cores \| RAM free \d+% \(\d+ GiB\)")
        self.assertNotIn("heavy-run", context)
        self.assertNotIn("note2", context)

    def test_prompt_updates_are_throttled_per_session(self):
        self.assertIsNotNone(self.run_hook(self.repo, "UserPromptSubmit"))
        self.assertIsNone(self.run_hook(self.repo, "UserPromptSubmit"))
        self.assertIsNotNone(self.run_hook(self.repo, "UserPromptSubmit", session="s2"))

    def test_first_prompt_after_session_start_does_not_repeat(self):
        self.assertIsNotNone(self.run_hook(self.repo, "SessionStart"))
        self.assertIsNone(self.run_hook(self.repo, "UserPromptSubmit"))

    def test_session_start_always_reports(self):
        self.assertIsNotNone(self.run_hook(self.repo, "UserPromptSubmit"))
        self.assertIsNotNone(self.run_hook(self.repo, "SessionStart"))


if __name__ == "__main__":
    unittest.main()
