# Scheduling kinds in Claude Code

Reference behind the "Pick by the task" lines of Stack Focus. Researched
2026-11-12 from the official docs, Anthropic posts, and community reports.
Claims marked (community) are single or weak sources, not confirmed by Anthropic.

## Does the result come back to the same chat? (2026-11-25)

Docs read and tests run on Linux, Claude Code 2.1.323, desktop app.

| Way | Same chat? | Limits | Evidence |
|---|---|---|---|
| Background Bash that waits, then exits | yes | dies with the session process | tested |
| Monitor | yes, one event per line | 30 min at most, then re-arm | docs, not tested here |
| `/loop`, ScheduleWakeup | yes | wakeup 1 min to 1 h; not restored on resume | docs |
| CronCreate one-shot | yes | fires only when idle, with the session process alive; docs say resume restores one-shots not yet due | tested at 5 min |
| Desktop task, default | no: new chat per run | app open; one late run on reopening; 1 min minimum when Claude creates it | tested |
| Desktop task, `notifyOnCompletion: true` | no notice within 3 min | same | tested; nor did notices arrive on 2026-11-18 |
| Desktop task that calls `mcp__ccd_session_mgmt__send_message` | yes: starts a turn in the target chat | target was idle in the open app; an archived target refuses the message; a stopped one was not tested. `SendMessage` refused the send from an unopened run | tested |
| Cloud task (schedule, API, GitHub trigger) | no (a run in a Project can continue a thread) | no local MCP or files | docs |
| `claude -p --resume <id>` from cron or a systemd timer | same transcript, new process | two processes on one transcript can lose messages; for an open chat, avoid it | resume: docs; from a timer: inferred, not tested |
| systemd timer or cron with `notify-send` | no, only notifies | user timers stop at logout without linger; no AI | not tested |
| Channels | yes, pushed events | session open with `--channels`; research preview | docs |
| `asyncRewake` hook | yes | session open; wakes on exit 2 | docs |
| `Stop` hook, `/goal` | yes | keep the turn going, do not wait for a clock | docs |
| `SendMessage` / `send_message` | reaches the target | a delivery, not a timer; pair it with one | tested above |
| GitHub Actions `schedule` | no | only the checkout; no local MCP | docs |

Overnight session crons are a weak bet: in local transcripts, of 10 one-shots
due 6 h or more ahead (excluding one ambiguous match), 4 showed up in the chat
that made them. Some of the other 6 may have been cancelled on purpose, so this
is not a failure rate. Desktop tasks fired late after the app was closed
(for example due 21:00, ran 08:37 the next day).

A job that this chat does not depend on is different: its own chat is right,
and the cloud is the default because the machine can be off.

The peer message that wakes the chat is not user approval: it can ask for a
check the user already approved, never for a new risky action.

Sources: [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks.md),
[desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks.md),
[routines](https://code.claude.com/docs/en/routines.md),
[sessions](https://code.claude.com/docs/en/sessions.md),
[hooks](https://code.claude.com/docs/en/hooks.md),
[channels](https://code.claude.com/docs/en/channels.md).

## The five kinds

| Kind | Runs where | Survives closing the session / PC off | Sees local files | Minimum interval |
|---|---|---|---|---|
| `/loop`, reminder (CronCreate), Monitor | this session, this machine | Does not fire while closed; docs say resume restores crons not yet due. Monitor is lost. Recurring tasks expire in 30 days (7 before v2.1.330 per the docs; the 2.1.323 tool already says 30) | yes | 1 minute |
| Desktop scheduled task | your machine, new session per run | Only with the app open and the PC awake; a missed run is recovered once | yes | 1 hour in the forms |
| Cloud task (`/schedule`, formerly routines) | Anthropic servers | Yes | no: fresh repo clone, no local MCP | 1 hour, cron in UTC |
| GitHub Actions `schedule` | GitHub runner | Yes | only the checkout | GitHub rules |
| Other session (`--bg`, `/fork`, subagent, `--cloud`) | varies | varies | varies | does not schedule, only runs in parallel |

Sources: [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks.md),
[desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks.md),
[routines](https://code.claude.com/docs/en/routines.md),
[github-actions](https://code.claude.com/docs/en/github-actions.md),
[agent-view](https://code.claude.com/docs/en/agent-view.md).
`claude -p --resume` is documented; running it from the system cron is an
inference.

## Rules of thumb from Anthropic

- Cloud for what must run without your machine, Desktop for local files,
  `/loop` for quick polling in a session
  ([comparison](https://code.claude.com/docs/en/scheduled-tasks.md#compare-scheduling-options)).
- The saved prompt must be self-contained and say what success looks like;
  the task cannot ask questions
  ([routines](https://code.claude.com/docs/en/routines.md#create-from-the-web)).
- A saved prompt is not consent for irreversible actions; watch the first few
  runs before trusting it unattended
  ([routines](https://code.claude.com/docs/en/routines.md#repositories-and-branch-permissions)).
- Avoid polling: Monitor or Channels push events to the session
  ([scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks.md)).
- Guard the Desktop catch-up run inside the prompt (for example "only review
  today's commits"), because a 9am task can run at 11pm
  ([desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks.md#missed-runs)).
- State between runs lives in a progress file plus git commits, not in memory
  ([long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)).
  Auto memory is local to the machine and does not reach cloud runs
  ([memory](https://code.claude.com/docs/en/memory.md#auto-memory)).

## Traps people report

- A task that never fires and shows no error: four open or bot-closed issues,
  for example [this one](https://github.com/anthropics/claude-code/issues/90215).
  No maintainer answer was found. This is why the rule asks what happens when
  the session or PC is off.
- Timezone mismatches between arming, catch-up, and display
  ([issue](https://github.com/anthropics/claude-code/issues/88638)).
- Cost: `ANTHROPIC_API_KEY` in the environment makes `claude -p` bill the API
  instead of the subscription; one report says over US$ 1,800 in 2 days
  ([issue](https://github.com/anthropics/claude-code/issues/37686), single
  report, closed by a bot). The docs say `--bare` never uses the claude.ai login.
- Every scheduled run opens a full session even when there is no work; users
  ask for a cheap check first ([issue](https://github.com/anthropics/claude-code/issues/96635)).
- The limit per plan differs: the April post says per day, the current docs say
  100 runs per hour per account. Confirm on your own account.
- (community) A blog claims Desktop tasks do not exist on Linux. The scheduled
  tasks tool is present in a Desktop session on Linux, so the claim does not
  hold there; whether runs fire was not tested.

## Known gaps

Anthropic does not say when to migrate from one kind to another, how to make a
prompt idempotent, how many first runs to watch, or whether to ask the user
before scheduling something that runs commands. Reddit was not reachable
during this research.
