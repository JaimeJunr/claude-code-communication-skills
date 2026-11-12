#!/usr/bin/env bash
# Injeta a data/hora local em cada prompt: o modelo não sabe "agora" sozinho e erra prazos
# relativos ("amanhã", "há 2 dias"). Locale C e ISO para a saída não depender do idioma do sistema.
printf '{"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":"Now: %s"}}\n' \
  "$(LC_ALL=C date '+%a %Y-%m-%d %H:%M %z')"
