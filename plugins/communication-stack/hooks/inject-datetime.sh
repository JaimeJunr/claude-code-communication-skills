#!/usr/bin/env bash
# Injeta a data/hora local em cada prompt: o modelo não sabe "agora" sozinho e erra prazos
# relativos ("amanhã", "há 2 dias"). Locale C e ISO para a saída não depender do idioma do sistema.
# Depois de uma pausa de 1h+ na mesma sessão, diz quanto tempo passou: sem isso o modelo trata a
# mensagem do dia seguinte como continuação imediata (CI, branch e contexto podem ter mudado).
set -u
MIN_GAP_S=3600

payload=$(cat)
session=$(printf '%s' "$payload" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' \
  | tr -c 'A-Za-z0-9_-' '_')
stamp="${TMPDIR:-/tmp}/communication-stack-time-${session:-default}.stamp"
now=$(date +%s)
last=$(cat "$stamp" 2>/dev/null || echo "$now")
case "$last" in ""|*[!0-9]*) last=$now ;; esac
echo "$now" > "$stamp"

gap=""
elapsed=$((now - last))
if [ "$elapsed" -ge "$MIN_GAP_S" ]; then
  days=$((elapsed / 86400)); hours=$((elapsed % 86400 / 3600))
  if [ "$days" -gt 0 ]; then gap="${days}d ${hours}h"; else gap="${hours}h"; fi
  gap=" | ${gap} since the previous message"
fi

printf '{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"Now: %s%s"}}\n' \
  "$(LC_ALL=C date '+%a %Y-%m-%d %H:%M %z')" "$gap"
