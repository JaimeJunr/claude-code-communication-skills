#!/usr/bin/env bash
# Hook PreToolUse: libera ler e gravar o to-do do projeto sem pedir permissão (lógica em project_todo.py).
# Sem python3 o hook sai calado: o Claude Code volta a pedir permissão, nada quebra.
command -v python3 >/dev/null 2>&1 || exit 0
exec python3 -I -B "$(dirname "$0")/project_todo.py" allow
