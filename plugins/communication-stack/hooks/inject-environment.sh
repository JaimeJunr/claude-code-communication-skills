#!/usr/bin/env bash
# Injeta repo/branch e carga da máquina: no início da sessão sempre e, nos prompts, no máximo
# 1x a cada 5 min por sessão, pra o modelo não supor branch errada nem rodar build pesado com a
# máquina no limite sem gastar token em toda mensagem. Parte de máquina só em Linux (/proc).
set -u
MIN_INTERVAL_S=300

payload=$(cat)
field() { printf '%s' "$payload" | sed -n "s/.*\"$1\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p"; }
event=$(field hook_event_name)
event=${event:-UserPromptSubmit}
session=$(field session_id | tr -c 'A-Za-z0-9_-' '_')

stamp="${TMPDIR:-/tmp}/communication-stack-env-${session:-default}.stamp"
now=$(date +%s)
if [ "$event" = "UserPromptSubmit" ]; then
  last=$(cat "$stamp" 2>/dev/null || echo 0)
  [ $((now - last)) -ge "$MIN_INTERVAL_S" ] || exit 0
fi
echo "$now" > "$stamp"

repo_line() {
  top=$(git rev-parse --show-toplevel 2>/dev/null) || return 0
  branch=$(git branch --show-current 2>/dev/null)
  changed=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  printf 'Repo: %s | Branch: %s | Uncommitted files: %s' "$(basename "$top")" "${branch:-detached}" "$changed"
}

machine_line() {
  [ -r /proc/meminfo ] && [ -r /proc/loadavg ] || return 0
  read -r load1 _ < /proc/loadavg
  mem_total=$(awk '/^MemTotal:/ {print $2}' /proc/meminfo)
  mem_avail=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
  swap_used=$(awk '/^SwapTotal:/ {t=$2} /^SwapFree:/ {f=$2} END {print t-f}' /proc/meminfo)
  pct=$(( mem_avail * 100 / mem_total ))
  line=$(printf 'Machine: load %s/%s cores | RAM free %s%% (%s GiB) | swap used %s GiB' \
    "$load1" "$(nproc)" "$pct" "$((mem_avail / 1048576))" "$((swap_used / 1048576))")
  psi=$(awk -F'avg10=' '/^some/ {split($2,a," "); print a[1]}' /proc/pressure/memory 2>/dev/null)
  [ -n "$psi" ] && line="$line | memory pressure ${psi}%"
  # Maior leitura entre os sensores disponíveis; o nome do sensor muda por máquina.
  temp=$(cat /sys/class/thermal/thermal_zone*/temp /sys/class/hwmon/hwmon*/temp*_input 2>/dev/null \
    | awk '$1 > max {max = $1} END {if (max > 0) print int(max / 1000)}')
  [ -n "$temp" ] && line="$line | max temp ${temp} C"
  if [ "$pct" -lt 15 ] || [ "${psi%.*}" -ge 20 ] 2>/dev/null || [ "${temp:-0}" -ge 85 ]; then
    line="$line | overloaded: avoid heavy local builds or test suites now"
  fi
  printf '%s' "$line"
}

context=$(printf '%s\n%s' "$(repo_line)" "$(machine_line)" | sed '/^$/d; s/\\/\\\\/g; s/"/\\"/g' | paste -sd '\t' - | sed 's/\t/\\n/g')
[ -n "$context" ] || exit 0
printf '{"hookSpecificOutput":{"hookEventName":"%s","additionalContext":"%s"}}\n' "$event" "$context"
