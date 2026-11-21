"""To-do do projeto: um arquivo por repo em ~/.local/share/claude-project-todo/<pasta>/todo.md.

Fica fora de qualquer pasta versionada: a memory/ do projeto em ~/.claude/projects às vezes é
versionada com o time (repos *-context), e o to-do é pessoal. É o mesmo arquivo para todas as
worktrees e subpastas do repo. Fora da pasta de trabalho o Claude Code pede permissão para ler e
gravar; o hook PreToolUse (modo "allow") libera só o to-do do projeto da sessão. Em ~/.claude isso
não funciona: lá o arquivo é "sensível" e nem o "allow" passa (testado em 2026-11-20).
Uso: o que só precisa ser lembrado no projeto vai sempre para cá; tarefa vai para o tracker
(issue, Jira) e só vem para cá quando o projeto não tem tracker.
SessionStart: imprime onde fica o arquivo e os itens abertos. Qualquer falha sai calada.
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
    "change it to `- [x]` and append `done YYYY-MM-DD`; never delete it. Use Read, Write and Edit "
    "on this file (no permission prompt), not Bash."
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
    # Mesmo nome de pasta que o Claude Code usa em ~/.claude/projects para o projeto.
    encoded = re.sub(r"[^A-Za-z0-9]", "-", str(project_root(cwd)))
    data = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share")
    return data / "claude-project-todo" / encoded / "todo.md"


def session_context(cwd: Path) -> str:
    path = todo_path(cwd)
    try:
        items = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if OPEN_ITEM.match(line)]
    except FileNotFoundError:
        return USAGE.format(path=path, status="no file yet; create it with the first item")
    listed = items[:MAX_LISTED]
    more = [f"+{len(items) - MAX_LISTED} more in the file"] if len(items) > MAX_LISTED else []
    return "\n".join([USAGE.format(path=path, status=f"{len(items)} open")] + listed + more)


FILE_TOOLS = ("Read", "Write", "Edit", "MultiEdit")


def allows(payload: dict[str, Any]) -> bool:
    """PreToolUse: libera ler e gravar só o to-do do projeto desta sessão, caminho normalizado."""
    if payload.get("tool_name") not in FILE_TOOLS:
        return False
    target = (payload.get("tool_input") or {}).get("file_path")
    if not target:
        return False
    expected = todo_path(Path(payload["cwd"]))
    return os.path.normpath(os.path.expanduser(str(target))) == os.path.normpath(str(expected))


def respond(mode: str, payload: dict[str, Any]) -> dict[str, Any] | None:
    if mode == "allow":
        if not allows(payload):
            return None
        return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "allow",
                                       "permissionDecisionReason": "project to-do (project-todo plugin)"}}
    cwd = Path(payload["cwd"])
    if not cwd.is_dir():
        return None
    return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": session_context(cwd)}}


def main() -> None:
    try:
        payload: dict[str, Any] = json.loads(sys.stdin.read())
        decision = respond(sys.argv[1] if len(sys.argv) > 1 else "session", payload)
    except Exception:  # o hook nunca pode quebrar a sessão
        return
    if decision:
        print(json.dumps(decision))


if __name__ == "__main__":
    main()
