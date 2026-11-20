"""Contract for the optional project-todo plugin: the project's to-do file and the deferred-work check."""
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_DIR = ROOT / "plugins" / "project-todo"
HOOKS = PLUGIN_DIR / "hooks"
TODO_HOOK = HOOKS / "inject-todo.sh"


def encoded(path):
    # Mesmo nome de pasta que o Claude Code usa em ~/.claude/projects (memória do projeto).
    return "".join(char if char.isalnum() else "-" for char in str(path))


class ProjectTodoPluginTest(unittest.TestCase):
    def test_plugin_ships_the_todo_and_deferred_work_hooks(self):
        self.assertEqual(sorted(path.name for path in HOOKS.iterdir() if path.name != "__pycache__"),
                         ["check-deferred-work.sh", "check_deferred_work.py", "hooks.json",
                          "inject-todo.sh", "project_todo.py"])
        config = json.loads((HOOKS / "hooks.json").read_text())["hooks"]
        commands = {event: [hook["command"] for entry in entries for hook in entry["hooks"]]
                    for event, entries in config.items()}
        self.assertEqual(commands, {
            "SessionStart": ['bash "${CLAUDE_PLUGIN_ROOT}/hooks/inject-todo.sh"'],
            "Stop": ['bash "${CLAUDE_PLUGIN_ROOT}/hooks/check-deferred-work.sh"']})
        manifest = json.loads((PLUGIN_DIR / ".claude-plugin" / "plugin.json").read_text())
        self.assertEqual(manifest["name"], "project-todo")
        self.assertNotIn("hooks", manifest)

    def test_core_plugin_no_longer_ships_the_deferred_work_check(self):
        core = ROOT / "plugins" / "communication-stack"
        self.assertFalse((core / "hooks" / "check-deferred-work.sh").exists())
        self.assertNotIn("Stop", json.loads((core / "hooks" / "hooks.json").read_text())["hooks"])


class TodoInjectionTest(unittest.TestCase):
    """No início da sessão o agente vê onde fica o to-do do projeto e os itens abertos."""

    def setUp(self):
        self.tmp = Path(self.enterContext(tempfile.TemporaryDirectory())).resolve()
        self.home = self.tmp / "home"
        self.repo = self.tmp / "my.repo"
        self.repo.mkdir(parents=True)
        git = {"cwd": self.repo, "check": True, "capture_output": True}
        subprocess.run(["git", "init", "-q", "-b", "main"], **git)
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q",
                        "--allow-empty", "-m", "init"], **git)

    def todo_file(self):
        return self.home / ".claude" / "projects" / encoded(self.repo) / "memory" / "todo.md"

    def run_hook(self, cwd, raw=None):
        payload = raw if raw is not None else json.dumps({"hook_event_name": "SessionStart", "cwd": str(cwd)})
        env = {"PATH": os.environ["PATH"], "HOME": str(self.home)}
        result = subprocess.run(["bash", str(TODO_HOOK)], input=payload, capture_output=True,
                                text=True, env=env, check=True)
        return json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"] if result.stdout.strip() else None

    def test_without_a_file_says_where_to_create_it_and_the_routing(self):
        context = self.run_hook(self.repo)
        self.assertIn(str(self.todo_file()), context)
        self.assertIn("no file yet", context)
        # Na pasta memory/ o Claude Code grava sem pedir permissão (o resto de ~/.claude é "sensível");
        # o frontmatter e o link no MEMORY.md fazem o arquivo passar no formato de memória.
        for rule in ("a reminder that is not a task", "tracker", "only when there is none", "- [ ]", "- [x]",
                     "name: project-todo", "type: project", "MEMORY.md"):
            with self.subTest(rule=rule):
                self.assertIn(rule, context)

    def test_lists_only_open_items_capped_at_ten(self):
        self.todo_file().parent.mkdir(parents=True)
        lines = [f"- [ ] 2026-11-20 item {n}" for n in range(12)] + ["- [x] 2026-11-19 old done 2026-11-20"]
        self.todo_file().write_text("---\nname: project-todo\n---\n" + "\n".join(lines) + "\n")
        context = self.run_hook(self.repo)
        self.assertIn("12 open", context)
        self.assertIn("item 9", context)
        self.assertNotIn("item 10", context)
        self.assertIn("+2 more", context)
        self.assertNotIn("old done", context)
        self.assertNotIn("no file yet", context)

    def test_worktrees_and_subfolders_share_the_project_file(self):
        subprocess.run(["git", "worktree", "add", "-q", str(self.tmp / "wt"), "-b", "wt"],
                       cwd=self.repo, check=True, capture_output=True)
        (self.repo / "sub").mkdir()
        for cwd in (self.tmp / "wt", self.repo / "sub"):
            with self.subTest(cwd=cwd.name):
                self.assertIn(str(self.todo_file()), self.run_hook(cwd))

    def test_outside_git_uses_the_folder_itself(self):
        plain = self.tmp / "plain"
        plain.mkdir()
        expected = self.home / ".claude" / "projects" / encoded(plain) / "memory" / "todo.md"
        self.assertIn(str(expected), self.run_hook(plain))

    def test_bad_input_never_breaks_the_session(self):
        for raw in ("not json", "{}", json.dumps({"cwd": str(self.tmp / "missing")})):
            with self.subTest(raw=raw):
                result = subprocess.run(["bash", str(TODO_HOOK)], input=raw, capture_output=True, text=True,
                                        env={"PATH": os.environ["PATH"], "HOME": str(self.home)})
                self.assertEqual((result.returncode, result.stdout), (0, ""))


DEFERRED_HOOK = HOOKS / "check-deferred-work.sh"


def user_prompt(text):
    return {"type": "user", "message": {"role": "user", "content": text}}


def assistant_text(text):
    return {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": text}]}}


def assistant_tool(name, tool_input):
    return {"type": "assistant", "message": {"role": "assistant", "content": [
        {"type": "tool_use", "id": "t1", "name": name, "input": tool_input}]}}


def tool_result(text, is_error=False):
    return {"type": "user", "message": {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "t1", "content": text, "is_error": is_error}]}}


def meta_notice(text):
    return {"type": "user", "isMeta": True, "message": {"role": "user", "content": [{"type": "text", "text": text}]}}


# Caso real que originou o hook (Sussurro, 2026-11-20): seis achados da revisão listados numa
# seção "Fica para depois" da descrição do PR, sem issue nenhuma.
SUSSURRO_REPORT = (
    "I opened the PR. The review's six suggestions are listed under \"Fica para depois\", "
    "so they don't get lost.\n\n**Fica para depois**\n- Tests for `capture.rs`\n- A `FocusGuard`")


class DeferredWorkHookTest(unittest.TestCase):
    """O hook Stop barra o fim do turno que adia trabalho sem deixar registro (issue, ticket, to-do)."""

    def setUp(self):
        self.tmp = Path(self.enterContext(tempfile.TemporaryDirectory()))

    def run_hook(self, entries, stop_hook_active=False, **extra):
        transcript = self.tmp / "t.jsonl"
        transcript.write_text("".join(json.dumps(entry) + "\n" for entry in entries))
        payload = {"session_id": "s1", "hook_event_name": "Stop", "transcript_path": str(transcript),
                   "stop_hook_active": stop_hook_active, **extra}
        result = subprocess.run(["bash", str(DEFERRED_HOOK)], input=json.dumps(payload),
                                capture_output=True, text=True, env={"PATH": os.environ["PATH"]}, check=True)
        return json.loads(result.stdout) if result.stdout.strip() else None

    def assertBlocks(self, decision):
        self.assertIsNotNone(decision)
        self.assertEqual(decision["decision"], "block")
        self.assertIn("not a record", decision["reason"])

    def test_blocks_the_sussurro_case(self):
        self.assertBlocks(self.run_hook([user_prompt("Open with gh"),
                                         assistant_tool("Bash", {"command": "gh pr create --body x"}),
                                         tool_result("https://github.com/o/r/pull/8"),
                                         assistant_text(SUSSURRO_REPORT)]))

    def test_blocks_english_deferral(self):
        for phrase in ("We can handle these in a follow-up PR.", "That is out of scope; next PR.",
                       "I'll fix them later.", "Deixo isso para um próximo PR.", "Fica fora do escopo."):
            with self.subTest(phrase=phrase):
                self.assertBlocks(self.run_hook([user_prompt("go"), assistant_text(phrase)]))

    def test_passes_when_an_issue_was_created_in_the_turn(self):
        self.assertIsNone(self.run_hook([user_prompt("go"),
                                         assistant_tool("Bash", {"command": "gh issue create --title x"}),
                                         tool_result("https://github.com/o/r/issues/9"),
                                         assistant_text(SUSSURRO_REPORT)]))

    def test_passes_when_the_report_links_an_issue(self):
        text = SUSSURRO_REPORT + "\nRecorded in https://github.com/o/r/issues/9 and https://x.atlassian.net/browse/CAP-1"
        self.assertIsNone(self.run_hook([user_prompt("go"), assistant_text(text)]))

    def test_passes_when_a_tracker_tool_or_backlog_file_was_used(self):
        for name, tool_input in (("mcp__atlassian__createJiraIssue", {"summary": "x"}),
                                 ("Edit", {"file_path": "/repo/BACKLOG.md", "old_string": "a", "new_string": "b"}),
                                 ("Write", {"file_path": "/repo/docs/backlog.md", "content": "x"})):
            with self.subTest(tool=name):
                self.assertIsNone(self.run_hook([user_prompt("go"), assistant_tool(name, tool_input),
                                                 tool_result("ok"), assistant_text(SUSSURRO_REPORT)]))

    def test_passes_when_a_todo_app_was_used(self):
        for name in ("mcp__todoist__add_task", "mcp__microsoft-todo__create_task", "mcp__trello__add_card"):
            with self.subTest(tool=name):
                self.assertIsNone(self.run_hook([user_prompt("go"), assistant_tool(name, {"content": "x"}),
                                                 tool_result("ok"), assistant_text(SUSSURRO_REPORT)]))

    def test_passes_when_the_report_links_a_todo_item(self):
        for link in ("https://app.todoist.com/app/task/abc-123", "https://trello.com/c/AbC123/9-x"):
            with self.subTest(link=link):
                self.assertIsNone(self.run_hook([user_prompt("go"), assistant_text(SUSSURRO_REPORT + "\n" + link)]))

    def test_the_agents_own_task_list_is_not_a_record(self):
        # Lista de tarefas da sessão e card de sessão somem com a sessão: o usuário não vê depois.
        for name in ("TodoWrite", "TaskCreate", "mcp__ccd_turn__update_plan", "mcp__ccd_session__start_session"):
            with self.subTest(tool=name):
                self.assertBlocks(self.run_hook([user_prompt("go"), assistant_tool(name, {"items": []}),
                                                 tool_result("ok"), assistant_text(SUSSURRO_REPORT)]))

    def test_a_failed_record_write_is_not_a_record(self):
        # Apontado pelo Codex no PR 17: tool_use com tool_result is_error não criou nada.
        for name, tool_input in (("Write", {"file_path": "/repo/BACKLOG.md", "content": "x"}),
                                 ("Bash", {"command": "gh issue create --title x"})):
            with self.subTest(tool=name):
                self.assertBlocks(self.run_hook([user_prompt("go"), assistant_tool(name, tool_input),
                                                 tool_result("permission denied", is_error=True),
                                                 assistant_text("I will fix them later; the record failed.")]))

    def test_blocks_deferral_written_only_in_the_pr_body(self):
        # Apontado pelo Codex no PR 17: o caso B9 com a lista só no corpo do PR e a resposta só com o link.
        body = "## What\nx\n\n## Fica para depois\n- testes do capture.rs"
        for name, tool_input in (("mcp__github__create_pull_request", {"title": "x", "body": body}),
                                 ("Bash", {"command": f"gh pr create --title x --body-file - <<'EOF'\n{body}\nEOF"})):
            with self.subTest(tool=name):
                self.assertBlocks(self.run_hook([user_prompt("open the PR"), assistant_tool(name, tool_input),
                                                 tool_result("https://github.com/o/r/pull/8"),
                                                 assistant_text("Opened https://github.com/o/r/pull/8.")]))

    def test_injected_meta_entries_do_not_reset_the_turn(self):
        # Apontado pelo Codex no PR 17: aviso injetado (isMeta) no meio do turno apagava o registro feito antes.
        self.assertIsNone(self.run_hook([user_prompt("go"),
                                         assistant_tool("Edit", {"file_path": "/repo/BACKLOG.md"}),
                                         tool_result("ok"), meta_notice("<system-reminder>x</system-reminder>"),
                                         assistant_text("Tests are left for later and recorded in BACKLOG.md.")]))

    def test_passes_without_deferral(self):
        self.assertIsNone(self.run_hook([user_prompt("go"), assistant_text("Done. Tests pass.")]))

    def test_ignores_deferrals_from_previous_turns(self):
        self.assertIsNone(self.run_hook([user_prompt("a"), assistant_text("Fica para depois: X"),
                                         user_prompt("b"), assistant_text("Done.")]))

    def test_ignores_phrases_inside_code(self):
        text = "Done.\n```\n# TODO: fix later\n```\nThe flag is `--later`."
        self.assertIsNone(self.run_hook([user_prompt("go"), assistant_text(text)]))

    def test_does_not_block_twice(self):
        # stop_hook_active: já barrou uma vez; barrar de novo prende o agente em loop.
        self.assertIsNone(self.run_hook([user_prompt("go"), assistant_text(SUSSURRO_REPORT)],
                                        stop_hook_active=True))

    def test_missing_transcript_falls_back_to_last_message(self):
        payload = {"hook_event_name": "Stop", "transcript_path": str(self.tmp / "missing.jsonl"),
                   "last_assistant_message": SUSSURRO_REPORT}
        result = subprocess.run(["bash", str(DEFERRED_HOOK)], input=json.dumps(payload),
                                capture_output=True, text=True, check=True)
        self.assertBlocks(json.loads(result.stdout))

    def test_reads_the_final_message_not_yet_in_the_transcript(self):
        # Visto no /verify: no Stop, o transcript às vezes ainda não tem a resposta final gravada;
        # o payload traz ela em last_assistant_message.
        self.assertBlocks(self.run_hook([user_prompt("go"), assistant_tool("Write", {"file_path": "/r/hello.py"}),
                                         tool_result("ok")],
                                        last_assistant_message="Tests are out of scope and stay for a next PR."))

    def test_bad_input_never_breaks_the_session(self):
        result = subprocess.run(["bash", str(DEFERRED_HOOK)], input="not json",
                                capture_output=True, text=True)
        self.assertEqual((result.returncode, result.stdout), (0, ""))

    def test_reason_routes_tasks_to_the_tracker_and_reminders_to_the_project_todo(self):
        repo = self.tmp / "repo"
        repo.mkdir()
        decision = self.run_hook([user_prompt("go"), assistant_text(SUSSURRO_REPORT)], cwd=str(repo))
        self.assertBlocks(decision)
        self.assertIn(f"/.claude/projects/{encoded(repo)}/memory/todo.md", decision["reason"])
        for rule in ("tracker", "a reminder that is not a task"):
            with self.subTest(rule=rule):
                self.assertIn(rule, decision["reason"])

    def test_writing_the_project_todo_is_a_record(self):
        todo = f"/home/u/.claude/projects/{encoded(self.tmp)}/memory/todo.md"
        self.assertIsNone(self.run_hook([user_prompt("go"), assistant_tool("Edit", {"file_path": todo}),
                                         tool_result("ok"), assistant_text(SUSSURRO_REPORT)]))


if __name__ == "__main__":
    unittest.main()
