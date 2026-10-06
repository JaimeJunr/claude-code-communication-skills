# communication-stack: plugin marketplace design

Status: proposed design, not an implemented plugin. This document incorporates the user's supplied hand-written ELI5 style and the source audit in [ANALYSIS.md](./ANALYSIS.md), dated 2026-10-06. Source instructions were reviewed as material, not activated. Only this design file is being written; upstream repositories, hooks, settings, and output styles are unchanged.

Recommendation: one marketplace entry containing one plugin, four selectable output styles, one automatically selectable router, six manual recipe commands, and no runtime hooks. Curate existing instructions, preserve their provenance, and reconcile them with a small, explicit precedence layer.

The goal is objective, short, clear, readable replies that begin and end on the requested point. Shortness must preserve the answer, necessary qualifications, and engineering rigor.

## A) INCLUDE / EXCLUDE

### Source decisions

| Source | Decision | Reason and audit evidence |
|---|---|---|
| JuliusBrussee/caveman — Apache-2.0 | INCLUDE exactly skills/caveman/SKILL.md; EXCLUDE every other skill, all hooks, installers, runtime, and mode machinery. | The base skill provides answer-first brevity and exact technical payload protection. The full plugin also changes workflows and injects session rules. ANALYSIS.md:6–54. |
| ayghri/i-have-adhd — MIT | INCLUDE skills/i-have-adhd/SKILL.md only, with task-scope and progress patches. | Useful actionable steps and topic control; its opt-in always-on hook would duplicate the selected output style. ANALYSIS.md:57–69. |
| blader/humanizer — MIT | INCLUDE root SKILL.md on demand. | Use for substantial cleanup of AI-sounding prose while preserving claims and writer samples; keep its 5,219-word body out of ordinary chat. ANALYSIS.md:72–83, 1330. |
| petergyang/no-ai-slop — MIT | INCLUDE skills/no-ai-slop/SKILL.md and its required eval.md. | Default editor for supplied drafts: minimum effective edits and personal voice preservation. ANALYSIS.md:97–108. |
| hexiecs/talk-normal — MIT | INCLUDE prompt-chatgpt.md and prompt.md as reference text; EXCLUDE installer skills and install.sh. | The compact prompt supplies the ordinary chat foundation; the full prompt is supporting reference. Do not append another always-on block to AGENTS.md. ANALYSIS.md:123–137, 1324–1325. |
| rahulj51/eli5 — MIT | INCLUDE skills/eli5/SKILL.md and skills/ste/SKILL.md as on-demand recipes. | Accuracy-conscious executive simplification and explicitly requested controlled English. Rahul's eli5 is not the source of our hand-written ELI5 output style. ANALYSIS.md:299–312. |
| hardikpandya/stop-slop — MIT | EXCLUDE from the runtime bundle. | Duplicates the two editors; absolute adverb, human-subject, passive-voice, and item-count bans require too much repair for a minimal-patch bundle. ANALYSIS.md:85–96, 563–595, 808–875. |
| obra/the-elements-of-style | EXCLUDE pending licensing clarification. | Strunk's historical text is public domain, but the repository has no license file covering its modern wrapper. The manifest's “Public Domain” label does not establish an unambiguous repository-wide grant. Do not relabel it MIT, CC0, or Unlicense. ANALYSIS.md:110–122. |
| Kyaa-A/eli5 — MIT | EXCLUDE. | Prioritizes simplicity over precision, withholds caveats, and imposes a five-sentence ceiling; repairing these central rules would substantially change the skill. ANALYSIS.md:284–298, 473–525. |
| smixs/awesome-claude-output-styles — MIT | EXCLUDE from runtime; use as a packaging/guardrail reference. | Its styles are derivative adaptations. Prefer direct sources rather than maintaining a second upstream layer or shipping 20 overlapping presets. ANALYSIS.md:138–141, 282. |
| fcakyon/claude-codex-settings ADHD plugin — Apache-2.0 | EXCLUDE. | Its forced output style and mandatory Insight blocks conflict with optional selection, short replies, and bare artifacts. ANALYSIS.md:313–327, 685–708. |
| User's hand-written ELI5 style — owned content | INCLUDE as output-styles/eli5.md, with keep-coding-instructions: true and force-for-plugin: false. | Its explicit promise is small words and short answers with identical engineering rigor. The original file was absent during the audit; this design uses the content supplied by the user, not an inferred repository equivalent. ANALYSIS.md:3, 328–329; subsequent user-provided content. |

Preserve upstream license texts and notices. Current caveman is Apache-2.0; its historical MIT file is not the blanket license for the current source. Retain LICENSE-MIT as attribution because caveman's current NOTICE and LICENSING.md reference historical contributions. ANALYSIS.md:9; JuliusBrussee_caveman/LICENSING.md:11–18, 31–41.

New router, precedence glue, and the owned ELI5 style may use the marketplace repository's own license. Preserve the separate upstream grants; do not label the entire vendored tree as solely MIT.

### Exact caveman skill boundary

INCLUDE only:

- skills/caveman/SKILL.md.

EXCLUDE these five other communication/artifact skills:

| Skill | Reason |
|---|---|
| ultracave | Required grammar stripping undermines readability. |
| megacave | Classical Chinese persona changes the reply language. |
| caveman-compress | Rewrites persisted context files; this bundle controls communication, not memory-file compression. |
| caveman-commit | Adds a specialized commit-writing contract; existing engineering/project conventions should govern commits. |
| caveman-review | Adds code-review workflow and finding-format rules outside this bundle's communication scope. |

EXCLUDE the remaining sixteen skills:

- cavecrew
- caveman-discover
- caveman-evidence-review
- caveman-explore
- caveman-help
- caveman-learn
- caveman-manage
- caveman-optimize
- caveman-setup
- caveman-stats
- investigate-first
- lean-build
- migration
- safe-refactor
- surgical-patch
- verify-and-stop

These add delegation, installation/help, telemetry, Cloud operations, optimization, or coding workflow policy. All 22 root skills are inventoried in ANALYSIS.md:21–43. Do not import the root plugin or distribution mirrors wholesale.

## B) Architecture, activation, ownership, and sync

### One selected output style; one recipe per task

Ship exactly four output styles:

| Frontmatter name | File | Purpose and source |
|---|---|---|
| Stack Clear | output-styles/clear.md | Recommended ordinary chat profile: adapt the compact talk-normal prompt, with the common context and accuracy boundaries. |
| ELI5 | output-styles/eli5.md | Our own hand-written style: small words, short answers, and unchanged engineering rigor. |
| Stack ADHD | output-styles/adhd.md | Adapt ayghri's canonical skill for action ordering, bounded steps, useful progress, and small visible groups. |
| Stack Caveman Lite | output-styles/caveman-lite.md | Experimental brevity profile from base caveman; preserve readable grammar and all necessary substance. |

“Caveman Lite” is the stack's adaptation name. Upstream's current lite/full aliases both resolve to caveman; this is not a claim that upstream ships a distinct lite skill. ANALYSIS.md:45–49.

All four styles declare keep-coding-instructions: true and force-for-plugin: false. No style forces itself on plugin enablement. The user selects one through Claude Code's output-style selector; enabling the plugin alone respects the existing selection.

A selected output style supplies session-wide communication guidance. It is not combined with the bodies of the other three styles. Each generated/adapted profile contains the same short essential boundaries: preserve meaning and protected text, respect the requested output contract, distinguish chat from artifacts, and yield presentation defaults to necessary coverage.

Claude Code's documented default for keep-coding-instructions is false: a custom style otherwise omits built-in software engineering instructions. A forced plugin style overrides the user's outputStyle setting; if multiple plugins force styles, the first loaded wins. See [output-style documentation](https://code.claude.com/docs/en/output-styles).

### Our hand-written ELI5 output style

Ship this as an owned file, not an upstream-synced file:

~~~markdown
---
name: ELI5
description: "Talk to me like I'm 5 — small words, short answers, same engineering rigor"
keep-coding-instructions: true
force-for-plugin: false
---

Use small words, short sentences, and short paragraphs.
Explain big words right after using them.

Return only what is necessary:
- What you did.
- Did it work?
- What to do now.

For a decision, give at most two options and say which you would pick.

Keep paths, commands, code, and file names exact.
Keep engineering work identical. Only the talking changes.

Apply the work-report slots when reporting work. For a question, give its answer.
The option limit and length preferences yield to an explicit request for more
coverage. Keep necessary facts, conditions, risks, and honest uncertainty.

Apply this voice to chat. For a requested draft, follow its audience and brief.
Style alone must never rewrite machine text or quoted material.
End on the requested point; give a next action only when one is needed.
~~~

The last paragraph and coverage exceptions are the stack's reconciliation layer. They prevent the original “what you did / did it work / what now” preference from forcing irrelevant status slots into a conceptual answer, and prevent the two-option default from deleting requested alternatives.

Preserve the supplied frontmatter name ELI5. Avoid installing a duplicate user-level copy with the same display name alongside the plugin copy. If both copies are deliberately retained, disambiguate their names rather than relying on ambiguous selection.

### Router and manual recipes

The communication-router is the only automatically selectable skill in this plugin. It handles explicit prose editing, AI-pattern cleanup, and simplification requests. It does not load for every routine answer; the selected output style already governs ordinary chat.

Select one primary upstream recipe per task:

| Request | Recipe |
|---|---|
| Edit my supplied draft while keeping my voice | no-ai-slop |
| Substantially rewrite AI-sounding prose | humanizer |
| Audit writing patterns without rewriting | no-ai-slop detect mode |
| Give a plain-language/executive version of specified content | rahul eli5 |
| Use Simplified Technical English / ASD-STE100-style writing | ste |
| Explicit action-first formatting for this task | i-have-adhd |
| Explicit brevity pass for this task | caveman |

A requested source wins over a default router choice. Do not automatically chain no-ai-slop, Humanizer, and another style audit over the same draft. The selected recipe performs its own supported review/check.

Six model-invocable leaf skills remain available: caveman, i-have-adhd, humanizer, no-ai-slop, eli5, and ste. Their narrowed descriptions permit loading only on explicit request or when the communication-stack router selects one. Invoke the chosen namespaced skill through the Skill tool, loading only that recipe. Never invoke more than one editor per task. If it is not installed, say so and give `/plugin install <name>@communication-stack`.

Recipe activation is current-task/current-artifact only. It does not establish a session-wide mode. A loaded skill can remain in conversation context after use; its instructions must explicitly stop governing later unrelated tasks. This is a scope rule, not a claim that Claude erases the loaded text.

### No runtime hooks in v1

Do not ship:

- Caveman's SessionStart or UserPromptSubmit hooks.
- ADHD's opt-in always-on hook or flag mechanism.
- Smixs's reminder hook or style-picker installer.
- Talk-normal's AGENTS.md installer.
- Kyaa's update-check hook.
- Automatic output rewriting, unsolicited statusline setup, or startup offers.

There is no need to re-inject a selected output style at SessionStart or on every prompt. No hook is needed to install, select, or reinforce these four profiles.

The plugin cannot cancel another plugin's hook injections or old AGENTS.md blocks. Document a one-time migration check for separately installed caveman/ADHD hooks, forced styles, and persisted talk-normal blocks. Report findings through an explicitly invoked diagnostic command if such a command is added later; do not silently modify other installations or add startup chatter.

The audit documents full-rule stacking, ADHD reactivation after compact/resume, duplicate reminders, and persisted blocks in ANALYSIS.md:1309–1315. Caveman's statusline setup offer also conflicts with its own no-offer rule: ANALYSIS.md:1161–1178.

### Repository layout

~~~text
communication-stack/
  .claude-plugin/marketplace.json
  stack.json
  sources.lock.json
  patches/
  scripts/sync-upstream
  plugins/communication-stack/
    .claude-plugin/plugin.json
    output-styles/
      clear.md
      eli5.md
      adhd.md
      caveman-lite.md
    skills/
      communication-router/SKILL.md
      caveman/SKILL.md
      i-have-adhd/SKILL.md
      humanizer/SKILL.md
      no-ai-slop/SKILL.md
      eli5/SKILL.md
      ste/SKILL.md
    references/
      conflicts.md
      recipes/
    vendor/
      caveman/
      adhd/
      humanizer/
      no-ai-slop/
      talk-normal/
      rahul-eli5/
~~~

The root marketplace has one communication-stack entry pointing to ./plugins/communication-stack. The plugin loads its own skills/ and output-styles/ directories. vendor/ and references/ are resource directories, not additional registered skill roots. Do not register vendor/ in the plugin's skills field.

Output styles live at the plugin root's supported output-styles/ location. Keep every runtime reference inside that plugin root so cached installations remain self-contained. A plugin-root CLAUDE.md is not an always-on substitute. See [plugin manifest documentation](https://code.claude.com/docs/en/plugins-reference).

The router and manual wrappers consume generated patched recipes in references/recipes/. Keep no-ai-slop's eval.md beside its compiled recipe so its relative reference remains valid. The owned ELI5 style is edited directly; the other three output styles are generated adapters of their source bodies plus the relevant reconciliation rules.

### Exact proposed stack.json copy map

The following is a proposed schema for the maintainer's sync script, not a claim that Claude Code itself reads stack.json:

- repo is the upstream GitHub repository URL.
- ref is main for every included upstream, as requested.
- copy lists exact upstream-root-relative from paths and marketplace-root-relative to paths.
- license_files uses the same from/to mapping shape for exact notice destinations.
- Sources are allowlisted files, not whole repositories.
- Source bodies are copied unchanged into vendor/. Patches generate runtime recipes/adapters from those copies; the raw vendor copies stay inspectable.
- The owned ELI5 file is intentionally absent from upstream sources and must never be overwritten by sync.

~~~json
{
  "schema_version": 1,
  "owned_files": [
    "plugins/communication-stack/output-styles/eli5.md",
    "plugins/communication-stack/skills/communication-router/SKILL.md",
    "plugins/communication-stack/references/conflicts.md"
  ],
  "sources": [
    {
      "id": "caveman",
      "repo": "https://github.com/JuliusBrussee/caveman",
      "ref": "main",
      "license": "Apache-2.0",
      "copy": [
        {
          "from": "skills/caveman/SKILL.md",
          "to": "plugins/communication-stack/vendor/caveman/skills/caveman/SKILL.md"
        },
        {
          "from": "LICENSING.md",
          "to": "plugins/communication-stack/vendor/caveman/LICENSING.md"
        }
      ],
      "license_files": [
        {
          "from": "LICENSE",
          "to": "plugins/communication-stack/vendor/caveman/LICENSE"
        },
        {
          "from": "NOTICE",
          "to": "plugins/communication-stack/vendor/caveman/NOTICE"
        },
        {
          "from": "LICENSE-MIT",
          "to": "plugins/communication-stack/vendor/caveman/LICENSE-MIT"
        }
      ]
    },
    {
      "id": "adhd",
      "repo": "https://github.com/ayghri/i-have-adhd",
      "ref": "main",
      "license": "MIT",
      "copy": [
        {
          "from": "skills/i-have-adhd/SKILL.md",
          "to": "plugins/communication-stack/vendor/adhd/skills/i-have-adhd/SKILL.md"
        }
      ],
      "license_files": [
        {
          "from": "LICENSE",
          "to": "plugins/communication-stack/vendor/adhd/LICENSE"
        }
      ]
    },
    {
      "id": "humanizer",
      "repo": "https://github.com/blader/humanizer",
      "ref": "main",
      "license": "MIT",
      "copy": [
        {
          "from": "SKILL.md",
          "to": "plugins/communication-stack/vendor/humanizer/SKILL.md"
        }
      ],
      "license_files": [
        {
          "from": "LICENSE",
          "to": "plugins/communication-stack/vendor/humanizer/LICENSE"
        }
      ]
    },
    {
      "id": "no-ai-slop",
      "repo": "https://github.com/petergyang/no-ai-slop",
      "ref": "main",
      "license": "MIT",
      "copy": [
        {
          "from": "skills/no-ai-slop/SKILL.md",
          "to": "plugins/communication-stack/vendor/no-ai-slop/skills/no-ai-slop/SKILL.md"
        },
        {
          "from": "skills/no-ai-slop/eval.md",
          "to": "plugins/communication-stack/vendor/no-ai-slop/skills/no-ai-slop/eval.md"
        }
      ],
      "license_files": [
        {
          "from": "LICENSE",
          "to": "plugins/communication-stack/vendor/no-ai-slop/LICENSE"
        }
      ]
    },
    {
      "id": "talk-normal",
      "repo": "https://github.com/hexiecs/talk-normal",
      "ref": "main",
      "license": "MIT",
      "copy": [
        {
          "from": "prompt-chatgpt.md",
          "to": "plugins/communication-stack/vendor/talk-normal/prompt-chatgpt.md"
        },
        {
          "from": "prompt.md",
          "to": "plugins/communication-stack/vendor/talk-normal/prompt.md"
        }
      ],
      "license_files": [
        {
          "from": "LICENSE",
          "to": "plugins/communication-stack/vendor/talk-normal/LICENSE"
        }
      ]
    },
    {
      "id": "rahul-eli5",
      "repo": "https://github.com/rahulj51/eli5",
      "ref": "main",
      "license": "MIT",
      "copy": [
        {
          "from": "skills/eli5/SKILL.md",
          "to": "plugins/communication-stack/vendor/rahul-eli5/skills/eli5/SKILL.md"
        },
        {
          "from": "skills/ste/SKILL.md",
          "to": "plugins/communication-stack/vendor/rahul-eli5/skills/ste/SKILL.md"
        }
      ],
      "license_files": [
        {
          "from": "LICENSE",
          "to": "plugins/communication-stack/vendor/rahul-eli5/LICENSE"
        }
      ]
    }
  ]
}
~~~

All from paths above exist in the checked-out sources. Local origin/main points to the audited commit for each included repository. No live fetch was run; these are checked-out snapshot facts, not a claim about the current remote branch.

Seed the lock file with these observed commits; maintainers resolve main to a full SHA before future syncing:

| Source id | Audited commit |
|---|---|
| caveman | 99aafe151a1be72be783e662858e8a0955add59f |
| adhd | 839872f9d1cd634fed642b4589ce7226199cc15f |
| humanizer | 225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8 |
| no-ai-slop | 000650b156983f5159695b441477f4e63b25dc85 |
| talk-normal | d89cf329e775e640181427fae071652198264c7e |
| rahul-eli5 | 43055a43a94f5508b74eb3ce31a103c55369aaf2 |

The same audit commits are recorded at ANALYSIS.md:2697–2709. The lock file also records each copied file's SHA-256 and the source license.

Sync must:

1. Resolve main to a commit and copy only the declared files and notices.
2. Preserve original source content in vendor/.
3. Apply named, reviewed patches to generated runtime copies; fail if patch context no longer matches.
4. Generate the three upstream-derived output styles and compiled recipes, preserving required helper-file relationships.
5. Verify that the owned ELI5 file, router, and conflicts.md were not overwritten.
6. Check that no upstream hooks, installers, manifests, or extra skills entered the plugin.
7. Validate the plugin manifest and run the cheap evaluation before releasing an update.

Do not fetch upstream or apply updates during a user's session. Sync is a maintainer operation, not a hook. Flag license/NOTICE changes for review rather than automatically assuming the previous grant still applies.

## C) Precedence ladder and conflict rulings

### Three contexts

Apply these ladders within Claude Code's normal instruction hierarchy. Accuracy, required content, and exactness contracts are constraints, not optional stylistic preferences.

| Context | Precedence |
|---|---|
| Chat replies to the user | Current user request, language, and output contract → selected current-task recipe → selected output style → generic brevity defaults. |
| Prose the user will publish | User brief, audience, and output contract → supplied writer sample / existing author voice → one selected editor → that editor's defaults. Chat persona rules do not control the artifact. |
| Machine text | Required schema, project syntax, and verbatim contract → project conventions for new content. Style rules govern surrounding prose only. |

For machine text, an existing code block, commit message, path, command, error, identifier, data value, or quoted string stays exact under a communication-only transformation. An explicit engineering request may authorize changing code or creating a new commit message; those changes follow the task and project rules, not a speaking style. Preserve protected spans inside prose artifacts as well.

A requested summary may omit details outside its required scope; every retained protected value remains exact. Do not turn that permission into dropping facts from a complete rewrite or an explicit “keep every value” request.

### Top ten rulings

| # | Context / topic | Winner → ruling and reason | Audit lines |
|---|---|---|---|
| T1 | Chat: opening order | Talk-normal/Rahul answer-first. Give the answer, decision, or requested action before background or an optional analogy. Include any condition needed to interpret that first answer safely. | 436–471 |
| T2 | Chat: readable grammar | Rahul's complete sentences plus caveman's clarity principle. Retain articles and grammatical relationships; concise headings/labels are fine, ambiguous telegraph speech is not. | 354–409 |
| T3 | All: caps versus substance | Rahul accuracy and ADHD's task-wins exception. Necessary facts, risks, uncertainty, and requested depth outrank sentence, word, option, and reading-time targets. | 473–546, 1053–1064 |
| T4 | Chat: ending and topic drift | Talk-normal and conditional ADHD next action. End on a fact, consequence, or needed action within the requested goal. No compulsory recap, new topic, or hypothetical offer. “Same point” means same goal, not repeating the opening. | 611–683, 768–783 |
| T5 | Chat: repeated state | Context-aware progress wins. Report changed state; in selected ADHD mode allow one useful step indicator during ongoing work or reader reorientation. Suppress unchanged background and completed-task recaps. | 411–434, 914–932 |
| T6 | Chat / prose: list count | ADHD completeness and Humanizer's genuine-item exception. Keep real three-step procedures and all requested items. Group long lists; do not truncate or destroy meaningful hierarchy. | 563–609 |
| T7 | Publishable prose: voice and detours | No-ai-slop minimum edits and Humanizer sample matching. Preserve intentional rhythm, humor, asides, and meaningful detours belonging to the requested piece. Chat topic control is not authority to erase the author's voice. | 742–783 |
| T8 | Prose: categorical bans | Humanizer's contextual tests. Preserve useful qualifiers, technical actors, passive voice, meaningful contrasts, and sample-matched punctuation. Remove empty formulae, not grammatical categories. | 785–875, 1066–1079 |
| T9 | Prose: return contract | Requested artifact plus Humanizer embedded mode. Return final text once; add critique, intermediate drafts, or What changed only when requested. A detect-only request returns findings, not a rewrite. | 961–979 |
| T10 | Machine text: exactness | Caveman payload protection and STE verbatim protection. Never alter protected payload to satisfy punctuation, word, language, grammar, or formatting preferences. Do not add code comments during a communication-only rewrite. | 527–561, 1003–1017, 1081–1108 |

### Complete register of all 44 audited conflicts

This register covers every conflict heading in ANALYSIS.md. It records scope and the winning rule, including cases resolved by not shipping the conflicting component. “Compatible” entries are not converted into fabricated contradictions.

| Audit # | Topic | Context | Ruling | ANALYSIS.md lines |
|---|---|---|---|---|
| 1 | Dropped grammar vs complete sentences | Chat | Whole readable sentences win; no ultra profile. Allow ordinary short labels, not omitted grammar that makes an explanation harder to read. | 354–373 |
| 2 | Removing articles in persisted context | Prose / machine | Do not ship caveman-compress. Preserve meaningful grammar and source structure; no automatic context-file rewrites. | 375–391 |
| 3 | Twenty-word ceiling vs natural rhythm | Chat / prose | Chat prefers short sentences without a universal hard ceiling. In authored prose, clear natural rhythm wins. Explicit STE has its own scoped rules. | 393–409 |
| 4 | Restate state vs say each fact once | Chat | One useful progress indicator during ongoing ADHD work; otherwise report changed state and avoid duplicate recap. | 411–434 |
| 5 | Action-first vs mandatory grounding | Chat | Give the requested answer/action first. Brief grounding follows when needed; do not require a reset on every turn. | 436–453 |
| 6 | Analogy-first vs answer-first | Chat | Answer first. An analogy is optional explanatory support, not a mandatory opening. | 455–471 |
| 7 | Five-sentence ceiling vs full walkthrough | Chat | Give the requested depth now. Sentence targets cannot force another turn to finish an authorized answer. | 473–489 |
| 8 | Simplicity vs precision/completeness | All | Preserve substance and precision. Simplify wording rather than deleting material facts; Kyaa's contrary contract is excluded. | 491–507 |
| 9 | Caveats only if asked | All | Include caveats that change the answer or action, concisely. Do not require the user to discover them through follow-up questions. | 509–525 |
| 10 | Dropping names/numbers vs exact payload | All | Selective omission is allowed only by the requested summary scope. Retain every required value exactly; complete technical rewrites cannot discard them. | 527–546 |
| 11 | Inline comments vs protected code | Machine | Explain around unchanged code. Add comments only when the engineering task explicitly calls for an edited/annotated version. | 548–561 |
| 12 | Numbered steps vs three-item suppression | Chat / prose | Keep the real number of steps/items. Three real items are valid; avoid artificial triads, not the number three. | 563–576 |
| 13 | Five-item display cap vs completeness | Chat | Group and rank items. Show all relevant items when completeness is requested or necessary. Five is a presentation preference. | 578–595 |
| 14 | Flat lists vs preserved nesting | Prose | Prefer flat chat lists, but keep hierarchy when it carries meaning or is part of the requested artifact structure. | 597–609 |
| 15 | Mandatory closing action vs done | Chat | Give a next action only if work remains or the answer calls for one. Finished answers stop. | 611–625 |
| 16 | Follow-up offers vs no offers | Chat / prose | No hypothetical unlock menus or unsolicited “want more?” endings. Necessary clarification and real coordination remain legitimate. | 627–642 |
| 17 | Three explanation levels vs say once | Chat | Give one explanation at the requested level. Re-explain when requested; do not ship a mandatory ladder profile. | 644–661 |
| 18 | Takeaway/aphorism vs redundant kicker | Chat / prose | End with useful content. A new consequence is allowed; a compulsory repeated lesson or decorative aphorism is not. | 663–683 |
| 19 | Insight wrappers vs bounded chatter | Chat / machine | No compulsory before/after teaching blocks. Explain when requested or necessary; respect artifact-only contracts. | 685–708 |
| 20 | Fixed bold labels vs content-led formatting | Chat / prose | Use headings, labels, and lists when they help the content or are requested. No compulsory What/Why/Fix or Why it matters template. | 710–740 |
| 21 | Author voice vs compression/persona | Prose | Writer sample and meaningful existing voice win. Chat profiles do not impose a persona on the published artifact. | 742–766 |
| 22 | Personal detours vs no tangents | Chat / prose | Chat stays on the user's requested goal. An intentional aside in the requested draft may be part of the task and should survive. | 768–783 |
| 23 | Absolute dash ban vs writer sample | Prose | Writer sample and useful punctuation win; otherwise use plain punctuation and avoid dash clusters. Protected strings are always exempt. | 785–806 |
| 24 | No adverbs/hedges vs real uncertainty | All | Preserve qualifiers that carry uncertainty, scope, emphasis, or author voice. Cut only empty padding. | 808–834 |
| 25 | Human subject / active-only vs real actors | Prose / chat | Use the actual actor, including a server or process. Useful passive voice is allowed; never invent a human actor. | 836–853 |
| 26 | Negative contrast ban vs real correction | Prose / chat | Humanizer's meaningful-correction exception wins. Retain both sides when they convey information or correct an actual belief; cut theatrical invented alternatives. | 855–875 |
| 27 | Literal action vs mandatory image | Chat | Prefer literal actions for work. An analogy may help an explanation, but no image is compulsory. | 877–899 |
| 28 | Technical actors vs personification | Chat / prose | Do not introduce fictitious agency into factual explanations. Explicitly requested fiction or metaphor follows its brief; no bedtime-story profile is shipped. | 901–912 |
| 29 | Rebuild known context vs thread reply | Chat / prose | Use the reader's actual context. Lead with the decision and new information; give reorientation when the reader needs it. | 914–932 |
| 30 | Sentence-end emphasis vs answer-first | Chat / prose | Compatible: the first answer sentence may put its strongest word at its end. No precedence patch is needed. | 934–941 |
| 31 | Parallel form vs deliberate irregularity | Prose | Use parallel form for genuinely coordinate ideas. Vary rhythm where it helps; do not manufacture irregularity merely to look human. | 943–959 |
| 32 | Draft plus explanation vs final-only | Prose | The requested output contract wins. Final text once by default; requested audit or change commentary is separate. | 961–979 |
| 33 | Exact terms vs renamed concepts | Chat / machine | Keep real names and identifiers. Define unfamiliar terms inline; avoid long invented replacements that obscure the term. | 981–1001 |
| 34 | Source quotation vs punctuation cleanup | All | Reproduce quotations as written. Word/punctuation bans apply only to editable original prose, never to evidence or protected strings. | 1003–1017 |
| 35 | Session persistence vs one-task ELI5 | Chat | Selected output styles are session-wide. Manual/routed recipes are task-bound and do not change the selected style. No shared natural-language mode tracker. | 1019–1036 |
| 36 | Reply language vs Wenyan/English-only | Chat / prose | The user's requested language wins. STE is English only when specifically requested. No Wenyan profile; Rahul's generic English-only wording is scoped accordingly. | 1038–1051 |
| 37 | Requested options vs one recommendation | Chat | Include the requested alternatives and, when useful, one recommendation. Owned ELI5 defaults to at most two options, but explicit broader coverage overrides that preference. | 1053–1064; owned style |
| 38 | Banned words vs technical vocabulary | All | Exact terms, proper names, quotations, and necessary technical senses survive word bans. “harness” and technical “robust” cannot be deleted mechanically. | 1066–1079 |
| 39 | Commit/review conventions vs full sentences | Machine / prose | Project artifact conventions win. New commit subjects may be intentional fragments; existing commit payload remains exact under style-only transformation. No generic emoji/grammar rule rewrites it. | 1081–1108 |
| 40 | Expository transitions vs no restatement | Prose | Meaningful exposition follows the brief. Cut redundant chat recap, but allow a transition or deliberate restatement that develops the requested long-form piece. | 1110–1128 |
| 41 | Rhetorical setups vs genuine questions | Chat / prose | Cut staged self-answered questions. Keep actual questions needed for clarification, coordination, or requested teaching; no blanket Wh-word ban. | 1130–1146 |
| 42 | Parentheses vs replacement bans | Prose | Parentheses, commas, colons, or sentence rewrites are allowed when clear and brief-appropriate. No universal punctuation replacement ban. | 1148–1159 |
| 43 | Startup setup offer vs no offers | Chat / hooks | Exclude the statusline/setup hooks. Do not inject an unsolicited setup task into the user's first reply. | 1161–1178 |
| 44 | Examples contradict their own rules | All | Explicit scope, exceptions, and the stack's rulings outrank illustrative examples. Do not learn a new mandate from a conflicting example. Keep real coordination distinct from chatbot boilerplate. | 1180–1200 |

## D) Exact description and body patches

### Registration patches

The router selects one model-invocable leaf skill. Each leaf description requires an explicit request or selection by the communication-stack router. Remove inherited invocation restrictions during sync.

Use these exact descriptions in generated registration frontmatter:

| Skill name | Description |
|---|---|
| communication-router | Use when asked to edit publishable prose, remove AI writing patterns, or simplify a specific explanation. Select one vendored recipe for the current task. |
| caveman | Explicit brevity pass for the current chat task. Preserve readable grammar, necessary substance, and exact technical payload. Load only on explicit request or when the communication-stack router selects it. |
| i-have-adhd | Explicit action-first formatting for the current task: bounded numbered steps and useful visible progress. Load only on explicit request or when the communication-stack router selects it. |
| humanizer | Substantial cleanup of supplied prose for AI writing patterns, preserving supported claims and the writer's voice. Load only on explicit request or when the communication-stack router selects it. |
| no-ai-slop | Minimum effective edits or a requested pattern audit of a supplied draft, preserving the writer's personal voice. Load only on explicit request or when the communication-stack router selects it. |
| eli5 | Plain-language or executive version of specified content for the current task. Preserve necessary facts and qualifications. Load only on explicit request or when the communication-stack router selects it. |
| ste | Explicitly requested Simplified Technical English for specified technical content. Load only on explicit request or when the communication-stack router selects it. |

Remove “be brief,” “less tokens,” “eli5 anywhere,” generic “any prose,” and session-mode claims from exposed descriptions. Remove or narrow any additional when_to_use or metadata.trigger text that reintroduces those meanings. A heading or quote containing eli5/caveman is not a request to change modes.

The existing ayghri skill disables model invocation upstream; remove that restriction in the generated leaf skill. Output-style descriptions are selector labels, not automatic skill triggers. Do not treat four style descriptions as four auto-selectable skills. Collision evidence: ANALYSIS.md:1202–1308.

Rename neither Rahul's upstream vendor path nor its canonical source identity. The namespaced skill eli5-ste:eli5 uses Rahul's recipe; the selected output style named ELI5 is our owned hand-written style. They have different activation paths and scopes.

### Shared context patch

Embed this essential contract in each adapted output style and compiled recipe, expressed for its context:

~~~text
Preserve required facts, conditions, risks, and genuine uncertainty.
Keep protected code, commands, paths, identifiers, data, errors, and quotations exact.
An explicit task may authorize changing engineering artifacts; speaking style cannot.
Follow the requested language, audience, structure, and output contract.
Presentation limits yield to requested coverage and necessary substance.
Chat profiles do not override the voice or conventions of a requested artifact.
Start with the requested answer. End on the same requested goal.
Give a next action only when one is needed; omit redundant recap and hypothetical offers.
~~~

For compiled recipe bodies, add this scope sentence:

~~~text
These instructions apply only to the current requested transformation or artifact.
They do not establish a session-wide mode or govern later unrelated tasks.
~~~

This is a compact reconciliation layer drawn from the retained sources and the user's goal. Do not add a new writing framework, a second global persona, or engineering workflow policy.

### Caveman patch

Source: skills/caveman/SKILL.md.

- Replace the Persistence section's whole-session claim with the shared current-task scope for the manual/routed recipe. In the output-style adapter, persistence is controlled solely by the selected output style.
- Remove the ultra/wenyan/status aliases and hook-dependent mode reporting. The stack does not ship their implementations.
- Replace article dropping/fragments as an ordinary explanation rule with: “Use complete, readable sentences. Short labels are fine. Keep articles and grammatical relationships when they help a single-pass reading.”
- Replace the absolute hedge ban with: “Cut ceremonial hedging and empty qualifiers. Keep genuine uncertainty, limits, and conditions.”
- Replace the universal 20-word/ASD-STE100 floor with: “Prefer short sentences and one clear idea per sentence. Clarity and necessary precision outrank a sentence-length target. Do not claim STE compliance from this brevity rule.”
- Scope “answer, reason, next step” so a next step appears only when relevant.
- Keep payload protection, explicit reply-language precedence, negations, units, and clarity exceptions.
- Retain the rule that harness instructions decide when to speak; do not let a brevity profile suppress required progress, warnings, or verification.
- Remove the caveman-compress exception because that skill is not included.

Evidence: ANALYSIS.md:8–19, 45–49, 354–409, 808–834, 1019–1051; canonical SKILL.md:15–19, 32, 39, 45–58, 60–81.

### ADHD patch

Source: skills/i-have-adhd/SKILL.md.

- Replace whole-session persistence and “normal mode” exit handling with current-task scope for the recipe. The selected ADHD output style retains its normal selected-style lifetime.
- Replace unconditional “restate state every turn” with: “During ongoing multi-step work, show one short step indicator when it helps orientation. Report changed state; otherwise avoid repeating background or completed-task recaps.”
- Preserve the existing “if anything is left open” condition on the final action; do not manufacture an action after completion.
- Preserve numbered bounded steps and grouping; keep the explicit completeness exception. Five items is a visible-group preference, not a search, analysis, or answer limit.
- Replace offering a second issue with: “Finish the requested issue. Include a secondary issue only when it affects the requested outcome; otherwise omit it unless requested.”
- Give time estimates only when supportable, and mark estimates as estimates. Do not invent precise durations to satisfy the formatting preference.
- Preserve full-walkthrough and task-wins exceptions, literal actions, and genuine uncertainty.

Evidence: ANALYSIS.md:60–69, 411–434, 563–595, 611–642, 768–783; canonical SKILL.md:57–94, 103–140.

### Humanizer patch

Source: root SKILL.md.

- Narrow the exposed description to substantial editing of supplied prose. Do not register it as ordinary reply-style guidance.
- Replace pasted-text default output (draft + remaining patterns + final rewrite) with: “Return the final text once. Include critique, intermediate drafts, or a change summary only when requested.”
- Keep file mode's prose-only boundary, exact protected spans, and embedded-mode artifact-only behavior. When file mode changes a named artifact, give only the concise completion information required by the task.
- Add the shared current-task scope.
- Preserve all supported-claim checks, writer-sample precedence, meaningful-contrast exceptions, useful passive voice, and source-quotation exceptions.
- Do not tighten its already contextual pattern tests into blanket word, dash, rhythm, or list bans.

Evidence: ANALYSIS.md:74–83, 742–875, 961–1017; canonical SKILL.md:34–53.

### No-ai-slop patch

Source: skills/no-ai-slop/SKILL.md, with eval.md preserved.

- Narrow the exposed description to a supplied-draft edit or requested pattern audit.
- Replace the default and workflow's compulsory What changed section with: “Return the edited draft once. Add What changed only if the user asks for edit notes.”
- Keep detect mode limited to evidence-based findings; remove its compulsory offer to edit afterward. Do not guess whether AI authored the draft.
- Add exemptions to the banned-word list for exact payload, names, quotations, and necessary technical senses.
- Replace the literal “never let inanimate things do human verbs” rule with: “Use the actual actor and concrete action. Technical systems can perform their actual operations; avoid invented agency.”
- Preserve author voice, meaningful uncertainty, complete supported claims, and minimum effective edits.
- Preserve its eval.md review, but interpret style checks through the shared meaning/voice/exactness contract. Do not add unrelated tests or publish its internal evaluation by default.
- Ask for missing audience/goal information only when the answer materially depends on it and the existing context does not supply it; do not require an interview for an otherwise clear edit.

Evidence: ANALYSIS.md:98–108, 742–853, 961–979, 1066–1079; canonical SKILL.md:10–22, 24–50, 90–97.

### Talk-normal patch

Sources: prompt-chatgpt.md for Stack Clear; prompt.md as supporting reference. Apply equivalent corrections wherever both copies state the same rule.

- Replace the absolute negation-based contrast prohibition with: “Cut staged contrasts against an alternative nobody claimed. Keep a contrast when both sides convey information or it corrects a real misunderstanding.”
- Replace fixed yes/no reasoning and explanation ceilings with short default targets that yield to complexity, requested depth, and material caveats.
- Replace fixed pros/cons item caps with: “Prioritize and group comparisons; retain all requested or decision-relevant alternatives and facts.”
- Make the compact prompt's unconditional final recommendation conditional: “End with useful content. Give a recommendation or next step only when relevant; otherwise stop.”
- Scope the code-plus-usage-example rule to requests that need an example; do not add extra text to exact or artifact-only output.
- Add protected-text, reply-language, and chat/artifact boundaries.
- Preserve answer-first, no empty preamble, no redundant rewording block, content-led formatting, and no hypothetical follow-up menus.
- Do not import either installer skill, AGENTS.md installation, or performance claims into runtime descriptions.

Evidence: ANALYSIS.md:123–137, 455–489, 611–642, 855–875; compact prompt:4, 12–24; full prompt:5, 21–34.

### Rahul eli5 patch

Source: skills/eli5/SKILL.md.

- Remove “eli5 anywhere” and broad implicit activation from the exposed description and When this applies section. Scope it to an explicit current-task simplification/executive-summary request.
- Replace generic English-only wording with the requested reply language. English remains the default when the request/context supplies no different language.
- Make single-level lists and under-one-minute reading presentation defaults; preserve meaningful hierarchy and requested depth.
- Qualify dropping names/numbers: “In a requested summary, omit only details outside its required scope. Preserve every required fact and retained protected value exactly.”
- Keep complete sentences, inline definitions, answer-first, decision-relevant risks/costs/deadlines, and the accuracy exception.
- Add current-task scope and the requested output contract.
- Do not use this recipe as the owner or upstream source of our ELI5 output-style file.

Evidence: ANALYSIS.md:299–312, 527–546, 597–609, 1038–1051.

### STE patch

Source: skills/ste/SKILL.md.

- Expose only an explicit STE/controlled-English invocation; keep it off for ordinary “simple words” requests.
- Preserve the recipe's English scope, meaning protection, procedural/descriptive distinctions, dictionary requirements, and exact technical spans.
- Add current-task scope and the shared protected-text/output-contract boundary.
- Preserve the qualification that a formal ASD-STE100 compliance claim requires an actual requested check against the relevant official standard and dictionary. Do not claim formal compliance from the skill text alone.
- Do not mix caveman fragments, automatic metaphors, or general prose word bans into STE.
- Any external standard retrieval follows the explicit task and normal engineering rigor; do not install or embed an unlicensed controlled dictionary as an incidental dependency.

Evidence: ANALYSIS.md:312, 548–559, 1038–1051; canonical SKILL.md:8–18, 22–74.

### Owned ELI5 patch

This file is owned, not an upstream patch target.

- Add keep-coding-instructions: true.
- Set force-for-plugin: false explicitly.
- Preserve the user's name, description, small-word/short-paragraph preferences, inline definitions, work-report slots, two-option preference, exact paths/commands/code/file names, and unchanged-engineering promise.
- Add only the coverage, work-report context, artifact scope, genuine-uncertainty, and same-goal ending exceptions shown in section B.
- Never overwrite it during upstream sync.

### Patch discipline

Keep raw upstream copies unchanged. Store each adaptation as a small named patch with source path, upstream SHA, reason, and relevant conflict ids. Generated runtime files should identify their source and modifications. Changes to descriptions alone cannot fix contradictory body instructions.

Avoid silently splitting Humanizer into independently rewritten subskills or rebuilding every source into a novel “master communication skill.” Keep complete recipes on demand; keep the router and shared contract small. If an upstream change requires a large patch, reconsider inclusion instead of maintaining a divergent fork.

## E) Biggest risk and cheap evaluation

The biggest risk is a reply that looks concise while losing the answer, necessary qualification, author voice, or engineering behavior. The original custom-style default for keep-coding-instructions makes that last risk concrete.

The supplied independent caveman evidence supports testing, not a savings promise: the JetBrains result covers 86 coding tasks and reports 8.5% fewer output tokens without a quality change; another small benchmark reported higher total tokens due to injected instructions. Full caveman's readability criticism supports keeping the lite adaptation opt-in. These are user-supplied external findings, not measurements from ANALYSIS.md or this design session.

The audit's word counts are not billable token counts. Humanizer and long injected profiles can erase output savings through input/context costs. ANALYSIS.md:1316–1330.

### Fixed prompt set

Use twenty fixed cases with the same prompts, model, model settings, tool availability, and turn budget:

| Group | Count | Examples |
|---|---:|---|
| Short chat | 6 | Yes/no with a material condition; direct factual answer; decision; requested three-or-more options; seven-item complete list; reply in Portuguese. |
| Multi-turn work | 4 | Changed progress; unchanged progress; task completion with no next action; unrelated issue that must not hijack the requested goal. |
| Explanations | 4 | Unfamiliar technical term; important caveat; full walkthrough; re-explanation explicitly requested after confusion. |
| Publishable prose | 3 | Voice-rich draft with an intentional aside; writer sample with dashes/uncertainty; AI-sounding draft requested as final-only text. |
| Machine text | 3 | Exact code/command/path copying; error strings and technical words also present in ban lists; exact existing commit/data payload. |

The four multi-turn cases are short fixed conversations, not merely isolated last messages. Include a later unrelated task after recipe loading to catch instruction leakage. Provide expected facts, protected spans, and requested coverage before scoring.

Compare Default, built-in Concise, Stack Clear, and the owned ELI5 style. This is 80 short case runs, with extra turns only for the fixed multi-turn cases. First run one sample per case; repeat only ambiguous results. Then run five matched cases each for Stack ADHD and Stack Caveman Lite.

For the baseline conditions, do not load stack source recipes automatically. For stack conditions, allow the intended router behavior and record which recipe it selects. Use the same task/tool budgets; include routing and recipe input costs in the stack's measured total.

### Measurements

| Metric | Definition |
|---|---|
| Words | Whitespace word count, reporting median and longest answers separately for chat and artifacts. Do not count fewer words from omitted requirements as a win. |
| Answer-first | First substantive sentence contains the requested answer, decision, or actionable result, including any necessary condition. |
| Drift | Each sentence serves the requested goal; the last substantive sentence remains on that goal. A necessary caveat is not drift. |
| Completeness / accuracy | Every required fact, caveat, condition, and requested alternative survives. No invented claims or unsupported certainty. |
| Exactness | Required protected spans compare byte-for-byte; style-only transformations leave existing machine payload unchanged. |
| Artifact contract | Final-only requests contain the artifact once, without compulsory intermediate drafts, change notes, or closing offers. |
| Voice / readability | Blind paired review by one human: easy to understand on one reading; supplied voice remains recognizable. |
| Routing | Exactly one intended primary recipe; no editing recipe on routine chat/code review merely because of broad descriptions. |
| Cost | Actual input and output tokens, including source loading and later context; report cache effects and latency separately. |

A simple word counter and exact-span comparison handle the mechanical checks. A short human pass scores answer-first, drift, completeness, and readability against the predefined expected facts. Do not use an AI-authorship detector or claim stylistic patterns prove authorship.

Initial acceptance targets:

- At least 90% answer-first.
- At least 95% no drift.
- Zero required-content, unsupported-fact, protected-payload, or artifact-contract failures.
- Fewer chat words than Default; compare against Concise separately.
- Readability at least matching Concise. Beating Concise on word count is not required if a necessary qualification makes the answer clearer.
- No regression in requested author voice.
- No automatic source-recipe collisions or session-mode leakage in the fixed suite.
- Report total-token results honestly; do not advertise token savings based only on output reduction.

These percentages describe this small fixed suite, not a statistically established general success rate.

Before plugin release or a sync update, verify all four style frontmatters retain keep-coding-instructions: true, none forces selection, only the router is automatically selectable, all license/helper mappings resolve, and no runtime hooks or extra caveman skills are present. A couple of small engineering smoke tasks should still follow their existing project instructions, verification requirements, and artifact conventions; the communication stack should change only how those results are explained.

If a profile loses meaning, fails exactness, or harms readability, revise or drop that profile before expanding the bundle. Keep the evaluation focused on answering the same requested point more clearly with less unnecessary text.
