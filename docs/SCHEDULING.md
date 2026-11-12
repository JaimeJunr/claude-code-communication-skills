# Scheduling kinds in Claude Code

Reference behind the "Pick the kind by need" lines of Stack Focus. Researched
2026-11-12 from the official docs, Anthropic posts, and community reports.
Claims marked (community) are single or weak sources, not confirmed by Anthropic.

## The five kinds

| Kind | Runs where | Survives closing the session / PC off | Sees local files | Minimum interval |
|---|---|---|---|---|
| `/loop`, reminder (CronCreate), Monitor | this session, this machine | No. Recurring tasks expire in 7 days | yes | 1 minute |
| Desktop scheduled task | your machine, new session per run | Only with the app open and the PC awake; a missed run is recovered once | yes | 1 hour in the forms |
| Cloud task (`/schedule`, formerly routines) | Anthropic servers | Yes | no: fresh repo clone, no local MCP | 1 hour, cron in UTC |
| GitHub Actions `schedule` | GitHub runner | Yes | only the checkout | GitHub rules |
| Other session (`--bg`, `/fork`, subagent, `--cloud`) | varies | varies | varies | does not schedule, only runs in parallel |

Sources: [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks.md),
[desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks.md),
[routines](https://code.claude.com/docs/en/routines.md),
[github-actions](https://code.claude.com/docs/en/github-actions.md),
[agent-view](https://code.claude.com/docs/en/agent-view.md).
`claude -p` run by the system cron is not covered by the docs.

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
