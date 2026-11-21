"""To-do do projeto: um arquivo por projeto em ~/.claude/projects/<pasta>/memory/todo.md.

Fica na pasta de memória do projeto porque é a única parte de ~/.claude onde o Claude Code grava
sem pedir permissão (o resto é "arquivo sensível", e nem um hook PreToolUse "allow" libera: testado
em 2026-11-20). Por isso o arquivo tem frontmatter de memória e um link no MEMORY.md. Fica fora do
repositório (não suja o git status) e é o mesmo para todas as worktrees e subpastas do projeto.
Uso: o que só precisa ser lembrado no projeto vai sempre para cá; tarefa vai para o tracker
(issue, Jira) e só vem para cá quando o projeto não tem tracker.
No SessionStart, imprime onde fica o arquivo e os itens abertos. Qualquer falha sai calada.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

MAX_LISTED = 10
OPEN_ITEM = re.compile(r"^\s*- \[ \] ")

USAGE = (
    "Project to-do: {path} ({status}). Use it for work set aside for later in this project: "
    "a reminder that is not a task always goes here; a task goes to the project's tracker "
    "(GitHub issue, Jira ticket) and comes here only when there is none. One line per item: "
    "`- [ ] YYYY-MM-DD <what is left> (from <PR, session or file>)`. When an item is done, "
    "change it to `- [x]` and append `done YYYY-MM-DD`; never delete it."
)
CREATE = (
    "To create it, start the file with this frontmatter: `---`, `name: project-todo`, "
    "`description: Work set aside for later in this project; open items are shown at session start`, "
    "`metadata:`, `  type: project`, `---`; then add `- [Project to-do](todo.md) — work set aside for "
    "later in this project` to MEMORY.md in the same folder."
)


def project_root(cwd: Path) -> Path:
    """Pasta principal do repositório (a mesma para worktrees); fora do git, a própria pasta."""
    try:
        common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                                cwd=cwd, capture_output=True, text=True, timeout=5)
    except (OSError, subprocess.SubprocessError):
        return cwd
    if common.returncode != 0 or not common.stdout.strip():
        return cwd
    git_dir = Path(common.stdout.strip())
    return git_dir.parent if git_dir.name == ".git" else git_dir


def todo_path(cwd: Path) -> Path:
    # Mesmo nome de pasta que o Claude Code usa para a memória do projeto.
    encoded = re.sub(r"[^A-Za-z0-9]", "-", str(project_root(cwd)))
    config = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")
    return config / "projects" / encoded / "memory" / "todo.md"


def session_context(cwd: Path) -> str:
    path = todo_path(cwd)
    try:
        items = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if OPEN_ITEM.match(line)]
    except FileNotFoundError:
        return USAGE.format(path=path, status="no file yet; create it with the first item") + " " + CREATE
    listed = items[:MAX_LISTED]
    more = [f"+{len(items) - MAX_LISTED} more in the file"] if len(items) > MAX_LISTED else []
    return "\n".join([USAGE.format(path=path, status=f"{len(items)} open")] + listed + more)


def main() -> None:
    try:
        payload: dict[str, Any] = json.loads(sys.stdin.read())
        cwd = Path(payload["cwd"])
        if not cwd.is_dir():
            return
        context = session_context(cwd)
    except Exception:  # o hook nunca pode quebrar a sessão
        return
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}))


if __name__ == "__main__":
    main()
