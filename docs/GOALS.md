# Goals and benchmarks

The Stack Focus style keeps getting better only if each rule has a target and a
check. This file is the scoreboard. Two kinds of check exist: automatic
metrics from your own transcripts (below, already measured) and frozen
benchmark cases (not run yet).

## Automatic metrics

`python scripts/metrics.py` reads `~/.claude/projects/*/*.jsonl` locally and
prints aggregates only, never message text. It groups sessions by the output
style stored in the transcript, so sessions from before the style form the
baseline. Use `--by week --since 2026-W40` for the trend. Rerun it after each
style change and add a row to the run log.

These are proxies, not verdicts. Task mix differs between groups, a "deferral
phrase" also matches harmless uses, and "recorded" only means a ticket or
`gh issue create` call happened in the same turn. Read the direction over
weeks, not one number.

| Metric | What it approximates | Goal |
|---|---|---|
| Median / P90 words of the final message | G7, concise answers | median down, P90 flat or down |
| Visuals per 100 turns | G3, builds a visual on its own | up |
| Schedules per 100 turns | G5, schedules later work | up |
| Deferral phrase % | how often work is parked | down or flat |
| Deferrals recorded % | G6, parked work gets a record | up, target >= 90 |

## Goals

| # | Behavior | Target | Baseline |
|---|----------|--------|----------|
| G1 | Answer first: line 1 is the verdict or answer | >= 90% of cases | not run |
| G2 | The last message ends with the conclusion and what the user must do | >= 95% | not run |
| G3 | Builds a visual on its own when the visual-check cases apply, and never offers it | >= 80% when it applies, 0 offers | 0.8 visuals per 100 turns (proxy) |
| G4 | Does not build a visual when it only restates the text | 0 decorative visuals | not run |
| G5 | Schedules later work on its own (reminder) or proposes it with task and time (runs commands) | >= 80% when it applies | 0.4 schedules per 100 turns (proxy) |
| G6 | Deferred work gets a tracker record with a link in the same turn, never a bare "later" | >= 90% when work is set aside | 6% of deferral phrases had a record (proxy; rule added after) |
| G7 | Fewer chat words than Default, with no required content lost | yes | median 99 words in W45, down from 151 in W42 |

## Benchmark cases for the newer rules

Freeze these before scoring and add them to the 20-case suite in the README
section "Evaluation TODO". Each case lists the expected behavior.

- **B1, deferred review finding.** A review reports two findings outside the PR.
  Expected: a tracker record for each (or one ready-to-create body when the
  tracker is shared), with a link or text in the report. Fail: "we do these later".
- **B2, known gap while implementing.** The agent notices a missing edge case it
  will not handle now. Expected: a record in the tracker or a backlog file.
  Fail: a sentence only.
- **B3, no tracker found.** A repo with no issue tracker. Expected: a backlog
  file entry, and one line saying where it lives.
- **B4, "I did not understand".** The user says they did not understand a flow
  with two or more quantities. Expected: an interactive visual in the same reply.
- **B5, plain status question.** Expected: text only, no visual, no tracker record.
- **B6, work that waits two hours for a deploy.** Expected: a scheduled check
  (created, or proposed with task and time if it runs commands).
- **B7, "tomorrow at 9am, my PC will be off".** Expected: a cloud task (or the
  conflict named if the job needs local files), never a session-only reminder.
  The line says what happens if the PC or session is off. Fail: a session
  reminder presented as done.
- **B8, watching a CI run.** Expected: Monitor, a channel or a trigger instead of
  a polling loop; a polling loop is acceptable only with the reason.

## Improvement loop

1. When a session shows a miss (a bare "later", a skipped visual, a buried
   conclusion), add it as a new benchmark case with the expected behavior.
2. Change the rule in `plugins/communication-stack/output-styles/focus.md`
   and add or extend the matching test in `tests/test_stack.py`.
3. Check the size: the style must stay under the output-style limit in
   `scripts/token_budget.py` (2000 tokens).
4. Rerun the cases, fill the baseline column, and note the date and model.
5. A rule that no case exercises, or that no session ever needed, is a
   candidate to cut.

## Run log

| Date | Scope | Cases | G1 | G3 (Focus vs other) | G4 | G5 (Focus vs other) | G6 (Focus vs other) | G7 |
|------|-------|-------|----|----|----|----|----|----|
| 2026-11-08 (metrics.py) | all transcripts, 21,307 turns | n/a | n/a | 0.8 vs 0.2 per 100 | n/a | 0.5 vs 0.8 per 100 | 6% vs 3% | median 111 vs 106 words overall; 99 in W45 |

Reading of the first run: over the whole history Stack Focus is not shorter
than the other sessions (111 vs 106 median words), but the weekly trend is
clearly down (151 in W42 to 99 in W45) and visuals rose from 0 to about 1 per
100 turns. Parked work was rarely recorded (6%); the new deferred-work
rule targets exactly that, so the next run should show it rise.
