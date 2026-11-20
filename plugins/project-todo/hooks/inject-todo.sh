#!/usr/bin/env bash
# Hook SessionStart: mostra onde fica o to-do do projeto e os itens abertos (lógica em project_todo.py).
# Sem python3 o hook sai calado: melhor perder o lembrete do que quebrar a sessão.
command -v python3 >/dev/null 2>&1 || exit 0
exec python3 -I -B "$(dirname "$0")/project_todo.py"
