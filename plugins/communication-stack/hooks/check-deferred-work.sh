#!/usr/bin/env bash
# Hook Stop: barra o fim do turno que adia trabalho sem registro (lógica em check_deferred_work.py).
# Sem python3 o hook sai calado: melhor perder a checagem do que quebrar a sessão.
command -v python3 >/dev/null 2>&1 || exit 0
exec python3 -I "$(dirname "$0")/check_deferred_work.py"
