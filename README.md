# Claude Code Communication Skills

**Objective, short, clear replies, with no topic drift.** One marketplace curates
existing communication recipes, reconciles their conflicting rules, and offers
four optional output styles. It preserves meaning, author voice, exact technical
payload, and engineering rigor.

[Português](README.pt-BR.md)

## Why this exists

A brevity recipe can drop grammar; a simplifier can lose caveats; an editor can
overwrite personal voice. Stacking them also adds competing instructions and
input cost. This stack selects one recipe per task, distinguishes chat from
publishable prose and machine text, and keeps every runtime hook out.

The research and source evidence live in [DESIGN.md](docs/research/DESIGN.md)
and [ANALYSIS.md](docs/research/ANALYSIS.md). This repository uses the simpler
per-upstream plugin layout of the sibling frontend marketplace.

## What's included, and why

- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman):
  only the base `caveman` skill, for a requested brevity pass. Readable grammar,
  real uncertainty, and task scope replace its persistent-mode defaults.
  Apache-2.0; `LICENSE`, `NOTICE`, `LICENSE-MIT`, and `LICENSING.md` are retained.
- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd):
  action-first formatting, bounded steps, useful progress, and complete coverage.
  Only its canonical skill is copied; no always-on hook. MIT.
- [blader/humanizer](https://github.com/blader/humanizer):
  substantial cleanup of supplied prose, preserving supported claims and the
  writer's sample. Its full recipe loads only for the selected task. MIT.
- [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop):
  the default for minimum effective draft edits and detect-only pattern audits.
  Its required `eval.md` stays beside the skill. MIT.
- [rahulj51/eli5](https://github.com/rahulj51/eli5):
  task-specific executive/plain-language explanations and explicitly requested
  Simplified Technical English, packaged as `eli5-ste`. MIT.
- [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal):
  the compact prompt is adapted into Stack Clear. Both original prompts and the
  MIT license are reference-only copies inside the owned plugin. No installer
  or talk-normal skill is registered.

The owned **communication-stack** plugin contains the router, precedence rules,
conflict rulings, and four styles. The **ELI5 output style is the user's own
hand-written style**, exactly the fixed version in DESIGN.md section B. It is
distinct from Rahul's `eli5-ste:eli5` recipe.

<!-- SKILLS:START -->
| Plugin | Skills | Count |
|---|---|---|
| `communication-stack` | `communication-stack` | 1 |
| `caveman` | `caveman` | 1 |
| `i-have-adhd` | `i-have-adhd` | 1 |
| `humanizer` | `humanizer` | 1 |
| `no-ai-slop` | `no-ai-slop` | 1 |
| `eli5-ste` | `eli5`, `ste` | 2 |
| **Total** | | **7** |
<!-- SKILLS:END -->

## Install

Once this repository is published, run in Claude Code:

```text
/plugin marketplace add JaimeJunr/claude-code-communication-skills
/plugin install communication-stack@communication-stack
/plugin install caveman@communication-stack
/plugin install i-have-adhd@communication-stack
/plugin install humanizer@communication-stack
/plugin install no-ai-slop@communication-stack
/plugin install eli5-ste@communication-stack
```

Each plugin is independent. Installing only `communication-stack` provides the
four styles. Install the upstream plugins needed by the router; if its chosen
source is unavailable, the router names it instead of silently switching editors.

If you already installed an original upstream plugin, remove the duplicate copy.
Check separately installed caveman/ADHD hooks, forced output styles, and old
talk-normal blocks in AGENTS.md once during migration. This marketplace does not
inspect or modify those other installations automatically.

### For a team project

Put this in `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "communication-stack": {
      "source": {
        "source": "github",
        "repo": "JaimeJunr/claude-code-communication-skills"
      }
    }
  },
  "enabledPlugins": {
    "communication-stack@communication-stack": true,
    "caveman@communication-stack": true,
    "i-have-adhd@communication-stack": true,
    "humanizer@communication-stack": true,
    "no-ai-slop@communication-stack": true,
    "eli5-ste@communication-stack": true
  }
}
```

Enabled is not installed. Each machine needs its own installation:

```bash
for p in communication-stack caveman i-have-adhd humanizer no-ai-slop eli5-ste; do
  claude plugin install "$p@communication-stack" --scope project
done
claude plugin list
```

Start a new session after installation.

## Pick one output style

Run `/output-style` to list styles, or `/config` and choose **Output style**:

- **Stack Clear**: ordinary chat; direct answers, useful context, no redundant
  endings. Recommended starting point.
- **ELI5**: small words, short answers, inline definitions, unchanged engineering
  rigor. Work-report slots apply to work reports; broader requests override its
  two-option preference.
- **Stack ADHD**: action-first answers, bounded numbered steps, useful progress,
  and small visible groups without losing requested items.
- **Stack Caveman Lite**: experimental brevity with complete, readable grammar.
  This is our adaptation name; upstream's current lite/full aliases both use
  the base caveman skill.

All four keep `keep-coding-instructions: true` and `force-for-plugin: false`.
Enabling the plugin respects the existing selection. Styles use the default
`output-styles/` scan, so the manifest omits `outputStyles`, which would replace
that scan. See the [output-style docs](https://code.claude.com/docs/en/output-styles)
and [plugin manifest reference](https://code.claude.com/docs/en/plugins-reference).

If you also keep `~/.claude/output-styles/eli5.md` with the name **ELI5**, rename
one style's frontmatter `name` to avoid ambiguous selection.

## How to use the recipes

Ask for a transformation; the router picks one primary recipe:

| Request | Recipe |
|---|---|
| Edit my supplied draft while keeping my voice | `no-ai-slop:no-ai-slop` |
| Substantially rewrite AI-sounding prose | `humanizer:humanizer` |
| Audit patterns without rewriting | `no-ai-slop:no-ai-slop`, detect mode |
| Plain-language/executive version of specified content | `eli5-ste:eli5` |
| Explicit Simplified Technical English | `eli5-ste:ste` |
| Action-first formatting for this task | `i-have-adhd:i-have-adhd` |
| Brevity pass for this task | `caveman:caveman` |

Or invoke a leaf directly, such as `/no-ai-slop:no-ai-slop`,
`/humanizer:humanizer`, or `/eli5-ste:eli5`. A named source wins over the default.

All six leaf skills remain model-invocable with narrow descriptions: load only
on explicit request or when the communication-stack router selects one.
The router invokes the chosen namespaced skill through the Skill tool, loading
only that recipe. Never invoke more than one editor per task. If its plugin is
not installed, report that and give `/plugin install <name>@communication-stack`.

Recipes apply to the current task or artifact only. They do not change the
selected style or govern later unrelated tasks. No editor runs on routine chat,
code review, or engineering work merely because it produces prose.

## Conflict rulings

The router holds three precedence ladders:

- **Chat:** current user request/language/output contract → current-task recipe
  → selected output style → generic brevity.
- **Publishable prose:** brief/audience/output contract → writer sample and
  existing voice → one editor → editor defaults.
- **Machine text:** schema/project syntax/verbatim contract → project conventions
  for new content. Style changes surrounding prose only.

The ten rulings require: answer first; readable grammar; substance over caps;
same-goal endings; changed-state progress; complete real lists; preserved author
voice and intentional asides; contextual pattern tests; final text once unless
notes are requested; and exact machine payload. Meaningful caveats and contrasts
survive. Detect mode returns findings without guessing authorship.

See [conflicts.md](plugins/communication-stack/skills/communication-stack/references/conflicts.md)
for all ten, and [DESIGN.md section C](docs/research/DESIGN.md#complete-register-of-all-44-audited-conflicts)
for the full 44-conflict register.

## What's excluded, and why

- **hardikpandya/stop-slop:** duplicates the two editors; categorical adverb,
  actor, passive-voice, punctuation, and item-count bans need extensive repair.
- **obra/the-elements-of-style:** no repository license covering the modern
  wrapper. Historical Strunk text being public domain does not resolve that.
- **Kyaa-A/eli5:** simplicity-over-precision, withheld caveats, and a five-sentence
  ceiling conflict with complete, accurate answers.
- **fcakyon ADHD:** forced style selection and mandatory Insight blocks conflict
  with optional profiles, short replies, and bare artifacts.
- **smixs/awesome-claude-output-styles:** a derivative packaging reference;
  direct sources avoid a second upstream layer and overlapping presets.
- **Caveman's other 21 skills:** no `ultracave`, `megacave`, `caveman-compress`,
  `caveman-commit`, `caveman-review`, `cavecrew`, `caveman-discover`,
  `caveman-evidence-review`, `caveman-explore`, `caveman-help`, `caveman-learn`,
  `caveman-manage`, `caveman-optimize`, `caveman-setup`, `caveman-stats`,
  `investigate-first`, `lean-build`, `migration`, `safe-refactor`,
  `surgical-patch`, or `verify-and-stop`. They strip grammar, switch language,
  modify memory, or add artifact/coding/delegation/Cloud policy outside this scope.
- **All hooks, installers, and runtime machinery:** no startup injection,
  always-on flags, automatic rewriting, statusline offers, or AGENTS.md edits.

## Keeping up with upstream

[stack.json](stack.json) allowlists every source at `ref: main`, copy path,
license file, and reviewed patch. [scripts/sync.py](scripts/sync.py) regenerates
the five upstream plugins, talk-normal references, marketplace, notices, lock,
and inventory tables. Other files in `communication-stack` are owned and survive
sync, including the exact ELI5 style. The three adapted styles are maintained by
hand and reviewed against their sources after updates.

The small `reference_only` option copies talk-normal directly into the router's
references. It preserves owned files and creates no extra marketplace entry.
Keeping source prompts with their adapter makes the installed plugin
self-contained and avoids an empty talk-normal plugin.

Cross-plugin `copy` entries also keep caveman and ADHD license/notice texts in
the owned plugin's references, so its styles retain those grants when installed
alone. These managed reference copies are the only additional sync destinations.

[UPSTREAM.lock](UPSTREAM.lock) records all six full HEAD commits, licenses, and
SHA-256 hashes of the copied source files before patches. Raw recipe versions
remain inspectable at those commits rather than in a duplicate vendor tree.
Each patch records its reviewed base commit, reason, and conflict IDs; context
or match-count changes fail sync. License/notice changes are flagged for review.

```bash
python scripts/sync.py
python scripts/sync.py --src .cache/upstream
python scripts/sync.py --check
```

`--src` uses clones named `<owner>_<repo>` at their existing HEAD without fetching.
A missing clone fails instead of falling back to the network. Repeating it with
the same six clean clones reproduces the generated bytes, including lock dates.

The weekly Action runs Mondays at 09:00 UTC and opens an upstream-sync PR.
`SYNC_TOKEN` should grant Contents and Pull requests write access. PRs opened
with the default `GITHUB_TOKEN` do not trigger the validation workflow; use
`SYNC_TOKEN` when requiring that check before merge.

## Evaluation TODO

The structural tests validate packaging; behavioral evaluation is **not run**.
Implement [DESIGN.md section E](docs/research/DESIGN.md#e-biggest-risk-and-cheap-evaluation):

- [ ] Freeze **20 cases**: 6 short chat, 4 fixed multi-turn conversations,
  4 explanations, 3 publishable prose, and 3 machine-text cases. Specify expected
  facts, protected spans, and required coverage before scoring. Include a later
  unrelated task after a recipe loads to test scope leakage.
- [ ] Compare Default, built-in Concise, Stack Clear, and owned ELI5 under the
  same model/settings/tools/turn budget: **80 case runs**. Add **5 matched cases
  each** for Stack ADHD and Stack Caveman Lite: **90 initial case runs** total,
  plus the prescribed extra conversation turns. Repeat ambiguous results only.
- [ ] Record chat/artifact median and longest word counts, answer-first,
  same-goal endings, completeness/accuracy, byte-exact protected spans,
  final-only contracts, selected recipe, and blind paired human voice/readability
  review. Record actual input/output tokens, later context, cache effects,
  latency, and routing/source-loading costs.
- [ ] Target at least 90% answer-first and 95% no drift; zero required-content,
  unsupported-fact, protected-payload, or artifact-contract failures. Fewer chat
  words than Default; compare Concise separately. Match Concise readability,
  preserve writer voice, and prevent recipe collisions or mode leakage.
- [ ] Run two small engineering smoke tasks using their existing project
  instructions and verification requirements before a release. Revise or drop
  a profile that loses meaning, exactness, or readability.

These are small-suite acceptance targets, not measured general success rates.
No token-savings claim follows from fewer output words alone.

## Contributing and licenses

See [CONTRIBUTING.md](CONTRIBUTING.md). Original router, owned ELI5 style,
scripts, and docs are MIT, copyright Jaime Basso. Upstream recipes, reference
prompts, and adapted styles retain their own grants. Sources, preserved notices,
and every modification are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
