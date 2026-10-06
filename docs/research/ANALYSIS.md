# AI communication sources: evidence audit
Snapshot: 2026-10-06. This report describes the checked-out files, not current upstream releases. All paths are relative to this directory unless absolute. `file:line` quotations preserve source text; ranges identify contiguous lines. Source instructions were treated as audit material, not activated. No installers, hooks, network checks, builds, or repo tests were run.
**Coverage limitation:** `/home/jaime/.claude/output-styles/eli5.md` does not exist. `/home/jaime/.claude/output-styles` also does not exist. One requested user-style file was checked; zero user-style files were readable. Its description, rules, word count, license, trigger, overlaps, and conflicts are unknown. It is not assumed identical to either ELI5 repository. All 11 requested repository directories are present.
**Counting method:** words = Python `len(text.split())`, including headings, examples, frontmatter, and code. Body words exclude a leading closed YAML frontmatter block. These are whitespace counts, not linguistic word counts or model tokens. Inventory counts list each selected physical file once; mirrors are counted separately. License text is reproduced in Appendix B. Missing package artifacts are explicit below; absence is based on recursive file enumeration excluding `.git`.
## 1. Per-source findings
### C — JuliusBrussee_caveman
Claude Code plugin: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` exist. Plugin manifest registers **SessionStart** and **UserPromptSubmit** command hooks. `JuliusBrussee_caveman/.claude-plugin/plugin.json:9-34` Marketplace uses repo root `"source": "./"` `JuliusBrussee_caveman/.claude-plugin/marketplace.json:13`. Root `skills/*/SKILL.md` is discovered wholesale; this includes coding and Cloud workflows, not just prose. `JuliusBrussee_caveman/CLAUDE.md:136-147`
Trigger: base caveman is model-invocable on “be brief”/“less tokens”, and persists for the session. Ultracave and megacave explicitly disable model invocation. Installation as a plugin activates the configured default at SessionStart; default resolves to `caveman`, with env → repository config → user config precedence. `off` and `manual` suppress rule activation. `JuliusBrussee_caveman/skills/caveman/SKILL.md:3-19` `JuliusBrussee_caveman/src/hooks/caveman-config.js:14-50` `JuliusBrussee_caveman/src/hooks/caveman-activate.js:295-327`
License: current whole repo **Apache-2.0**, root `LICENSE`; historical `LICENSE-MIT` is **MIT**, not the current blanket license. `JuliusBrussee_caveman/LICENSING.md:3-18` `JuliusBrussee_caveman/LICENSING.md:31-41`. Both full texts appear in Appendix B. No claim about third-party SDK/font licenses is needed for this communication audit.
- Answer, reason, next step. `JuliusBrussee_caveman/skills/caveman/SKILL.md:30-35`
- Remove greeting, hedging, recap, and closer. `JuliusBrussee_caveman/skills/caveman/SKILL.md:37-39`
- Use short common words; keep standard acronyms; no invented abbreviations or arrows. `JuliusBrussee_caveman/skills/caveman/SKILL.md:41-43`
- Articles optional; fragments allowed; preserve negations, numbers, and units. `JuliusBrussee_caveman/skills/caveman/SKILL.md:45-50`
- One idea per sentence; maximum 20 words; clarity outranks compression. `JuliusBrussee_caveman/skills/caveman/SKILL.md:52-54`
- Keep code, commands, paths, API names, and errors verbatim. `JuliusBrussee_caveman/skills/caveman/SKILL.md:56-58`
- Bound tool status to start, phase changes, and result. `JuliusBrussee_caveman/skills/caveman/SKILL.md:60-62`
- Keep the user’s language and grammatical particles. `JuliusBrussee_caveman/skills/caveman/SKILL.md:64-66`
- No caveman performance, decorative tables, or emoji. `JuliusBrussee_caveman/skills/caveman/SKILL.md:68-70`
- Use plain prose for risk, ambiguity, confused users, harness requirements, and persisted artifacts; `/caveman-compress` is exempt. `JuliusBrussee_caveman/skills/caveman/SKILL.md:72-81`

#### All root skills (22 candidates; all 22 listed)
- `JuliusBrussee_caveman/skills/cavecrew/SKILL.md` — **coding workflow / delegation with compressed agent output**; 544 words; description at `JuliusBrussee_caveman/skills/cavecrew/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/caveman/SKILL.md` — **communication / persistent reply voice**; 628 words; description at `JuliusBrussee_caveman/skills/caveman/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/caveman-commit/SKILL.md` — **communication / commit artifact, not general reply style**; 358 words; description at `JuliusBrussee_caveman/skills/caveman-commit/SKILL.md:3-5`.
- `JuliusBrussee_caveman/skills/caveman-compress/SKILL.md` — **communication / persisted context-file rewrite, not general reply style**; 703 words; description at `JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:3-5`.
- `JuliusBrussee_caveman/skills/caveman-discover/SKILL.md` — **Cloud setup / workflow spend labels**; 804 words; description at `JuliusBrussee_caveman/skills/caveman-discover/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/caveman-evidence-review/SKILL.md` — **Cloud stats / read-only evidence review**; 557 words; description at `JuliusBrussee_caveman/skills/caveman-evidence-review/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/caveman-explore/SKILL.md` — **coding workflow / localization**; 317 words; description at `JuliusBrussee_caveman/skills/caveman-explore/SKILL.md:3-5`.
- `JuliusBrussee_caveman/skills/caveman-help/SKILL.md` — **help / one-shot reference card**; 386 words; description at `JuliusBrussee_caveman/skills/caveman-help/SKILL.md:3-5`.
- `JuliusBrussee_caveman/skills/caveman-learn/SKILL.md` — **optimization workflow / consent-gated token-cost edits**; 1864 words; description at `JuliusBrussee_caveman/skills/caveman-learn/SKILL.md:3-3`.
- `JuliusBrussee_caveman/skills/caveman-manage/SKILL.md` — **Cloud workflow / experiment lifecycle control**; 549 words; description at `JuliusBrussee_caveman/skills/caveman-manage/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/caveman-optimize/SKILL.md` — **Cloud workflow / paired optimization evaluation**; 672 words; description at `JuliusBrussee_caveman/skills/caveman-optimize/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/caveman-review/SKILL.md` — **communication / PR review artifact, not general reply style**; 412 words; description at `JuliusBrussee_caveman/skills/caveman-review/SKILL.md:3-5`.
- `JuliusBrussee_caveman/skills/caveman-setup/SKILL.md` — **setup / gateway integration**; 1427 words; description at `JuliusBrussee_caveman/skills/caveman-setup/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/caveman-stats/SKILL.md` — **stats / usage reporting**; 281 words; description at `JuliusBrussee_caveman/skills/caveman-stats/SKILL.md:3-6`.
- `JuliusBrussee_caveman/skills/investigate-first/SKILL.md` — **coding workflow / diagnosis**; 92 words; description at `JuliusBrussee_caveman/skills/investigate-first/SKILL.md:3-3`.
- `JuliusBrussee_caveman/skills/lean-build/SKILL.md` — **coding workflow / narrow feature delivery**; 152 words; description at `JuliusBrussee_caveman/skills/lean-build/SKILL.md:3-3`.
- `JuliusBrussee_caveman/skills/megacave/SKILL.md` — **communication / persistent reply language and voice**; 320 words; description at `JuliusBrussee_caveman/skills/megacave/SKILL.md:3-7`.
- `JuliusBrussee_caveman/skills/migration/SKILL.md` — **migration workflow**; 104 words; description at `JuliusBrussee_caveman/skills/migration/SKILL.md:3-3`.
- `JuliusBrussee_caveman/skills/safe-refactor/SKILL.md` — **coding workflow / behavior-preserving refactor**; 92 words; description at `JuliusBrussee_caveman/skills/safe-refactor/SKILL.md:3-3`.
- `JuliusBrussee_caveman/skills/surgical-patch/SKILL.md` — **coding workflow / bounded fix**; 93 words; description at `JuliusBrussee_caveman/skills/surgical-patch/SKILL.md:3-3`.
- `JuliusBrussee_caveman/skills/ultracave/SKILL.md` — **communication / persistent reply voice**; 340 words; description at `JuliusBrussee_caveman/skills/ultracave/SKILL.md:3-7`.
- `JuliusBrussee_caveman/skills/verify-and-stop/SKILL.md` — **coding workflow / verification stop condition**; 98 words; description at `JuliusBrussee_caveman/skills/verify-and-stop/SKILL.md:3-3`.
The six `plugins/caveman/skills/*/SKILL.md` distribution copies are inventoried separately below. They are not six additional root skills. The stats copy differs from the root source; equality is checked in the verification section.
#### Modes: current behavior versus old names
- **lite / full:** both now map to `caveman`; no separate active lite-versus-full grammar rule exists. It drops ceremony and optionally articles, retains meaningful grammar. `JuliusBrussee_caveman/src/hooks/caveman-config.js:43-51` `JuliusBrussee_caveman/skills/caveman/SKILL.md:13` `JuliusBrussee_caveman/skills/caveman/SKILL.md:45-54`
- **ultra / ultracave:** drops articles, copulas, and connectives when order remains clear; each fact once; no summary after a list. `JuliusBrussee_caveman/skills/ultracave/SKILL.md:14-40`
- **megacave / wenyan / wenyan-lite / wenyan-full / wenyan-ultra:** all Wenyan aliases map to `megacave`. Uses Classical Chinese, omits recoverable subjects, replaces connective phrases with particles; keeps identifiers in original script. No distinct Wenyan intensity levels remain. `JuliusBrussee_caveman/src/hooks/caveman-config.js:47-51` `JuliusBrussee_caveman/skills/megacave/SKILL.md:14-28`
- **off / manual:** startup policy suppresses the full ruleset; `manual` is a default policy, not a stored selectable mode. **commit / review / compress:** independent one-shot skills, then restore the displaced prose mode. `JuliusBrussee_caveman/src/hooks/caveman-config.js:34-41` `JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js:287-325` `JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js:342-358`
#### Hooks and commands
- `src/hooks/caveman-activate.js`: resolves and persists per-session mode, loads the complete active skill body without frontmatter, emits it plus banner and switch line; preserves a stored mode on continuation events. Can append a one-time statusline setup/repair instruction. `JuliusBrussee_caveman/src/hooks/caveman-activate.js:295-393` `JuliusBrussee_caveman/src/hooks/caveman-activate.js:534-555`
- `src/hooks/caveman-mode-tracker.js`: parses mode commands and natural language, records transitions, stores durable off, restores one-shot modes, emits per-turn scope/style reinforcement and a full body on mode changes; intercepts `/caveman-stats`. `JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js:191-215` `JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js:287-388`
- `src/hooks/caveman-config.js` and `caveman-parse.js`: support state/configuration and parsing; not additional independently registered hooks. `cavecrew-model-overrides.js` is invoked by activation to apply agent model overrides. `JuliusBrussee_caveman/src/hooks/caveman-activate.js:185-190`
- `src/hooks/caveman-stats.js`: invoked for stats, not automatic full-rule injection. `caveman-statusline.sh` / `.ps1`: render mode badge and optional savings suffix. `install.sh` / `uninstall.sh`: install/remove registrations and files; not event hooks themselves. `JuliusBrussee_caveman/src/hooks/README.md:49-62` `JuliusBrussee_caveman/src/hooks/README.md:180-182`
- Repo-local Codex hook: `.codex/hooks.json` calls `.codex/codex-sessionstart.js` on startup/resume. It loads configured rules; the general installer does not copy `.codex/`. `JuliusBrussee_caveman/.codex/hooks.json:3-12` `JuliusBrussee_caveman/CLAUDE.md:121`
- Root Claude slash command file: `commands/caveman-init.md`; all root skills can provide skill invocations. Seven root `.toml` command stubs serve other hosts, not Claude’s Markdown command discovery. Eight OpenCode Markdown command files live in `src/plugins/opencode/commands/`; native plugin `src/plugins/opencode/plugin.js` handles mode state and reminders. `JuliusBrussee_caveman/CLAUDE.md:133-134` `JuliusBrussee_caveman/CLAUDE.md:166-174`
### A — ayghri_i-have-adhd
Claude plugin and marketplace present; Codex plugin/marketplace and Cursor mirror also present. Canonical skill `skills/i-have-adhd/SKILL.md`; same body in `.cursor/skills/i-have-adhd/SKILL.md`. License **MIT**, root `LICENSE`. Skill has `disable-model-invocation: true`: explicit `/i-have-adhd`, then session persistence; not ordinary automatic description activation. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:1-19`
Always-on is **opt-in**, via `$CLAUDE_CONFIG_DIR/.i-have-adhd-always` (default `~/.claude`). `hooks/hooks.json` fires on `startup|resume|clear|compact` and launches `hooks/always-on.mjs`; absent flag exits without injecting anything. Full body, with frontmatter stripped, is printed when opted in. POSIX `always-on.sh` and PowerShell `always-on.ps1` are fallback implementations, not three simultaneous default registrations. `ayghri_i-have-adhd/hooks/hooks.json:3-12` `ayghri_i-have-adhd/hooks/always-on.mjs:16-40`
- Lead with the actionable command, path, snippet, or answer. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:33-40`
- Number multi-step work; each step is one bounded action. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:42-46`
- If work remains, end with one action doable in under two minutes. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:57-62`
- Finish the first issue before offering another; surface unresolved questions once at the end. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:64-71`
- Restate state every turn; a harness checklist can do this without duplicate prose. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:73-80`
- Give specific time estimates and make completed work visible. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:82-94`
- Errors: cause and fix, without alarmed language. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:96-101`
- Aim for five visible items per group, but never omit relevant items when completeness matters. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:103-107`
- No preamble, completed-task recap, or closing pleasantries. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:109-117`
- Walkthroughs can be full length; task and harness constraints win; retain real uncertainty and use literal actions. `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:119-140`

OpenCode `.opencode/command/i-have-adhd.md` is an explicit slash command; `.opencode/plugins/i-have-adhd.mjs` registers it and injects the full body **every turn** if its separate OpenCode flag exists. `ayghri_i-have-adhd/.opencode/plugins/i-have-adhd.mjs:36-51` `ayghri_i-have-adhd/.opencode/plugins/i-have-adhd.mjs:74-97`. Pi/OMP `extensions/i-have-adhd.ts` has an `--adhd` flag, toggle command, state restore, and context-aware once-only rule injection. `ayghri_i-have-adhd/extensions/i-have-adhd.ts:130-151` `ayghri_i-have-adhd/extensions/i-have-adhd.ts:181-202` `ayghri_i-have-adhd/extensions/i-have-adhd.ts:237`. Root `plugin.json`, Gemini/Qwen/Kimi manifests are adapters, not extra Claude SessionStart registrations.
### H — blader_humanizer
Claude plugin/marketplace present; plugin skill path is `["./"]`, loading root `SKILL.md`. Cursor plugin and `agents/openai.yaml` exist. No hook registration or command-directory file exists. Description-driven prose editing/review; no session persistence directive. MIT root license. `blader_humanizer/.claude-plugin/plugin.json:12-14` `blader_humanizer/SKILL.md:3-7`
- Preserve supported claims; invent no facts, names, numbers, dates, quotes, or citations. `blader_humanizer/SKILL.md:15-38`
- Match a supplied writer sample; it overrides patterns, including dash rate. `blader_humanizer/SKILL.md:41-45`
- Cut empty contrasts and redundant one-line closers; merge dramatic fragments. `blader_humanizer/SKILL.md:59-79`
- Remove staged openers, fake objections, and forced triads; retain informative contrasts and three real items. `blader_humanizer/SKILL.md:110-142`
- Default final rewrite has no em/en dashes; protect code, paths, commands, and URLs. `blader_humanizer/SKILL.md:160-163`
- Keep genuine uncertainty; use active voice when it clarifies the actor. `blader_humanizer/SKILL.md:169-189`
- Replace inflated significance, sales language, and borrowed authority with supported concrete facts. `blader_humanizer/SKILL.md:208-268`
- Formatting follows meaning; avoid decorative bold, headings, emoji, and arrows. `blader_humanizer/SKILL.md:278-307`
- Strip chatbot residue and redundant context in thread replies. `blader_humanizer/SKILL.md:317-373`
- Output varies: pasted text returns draft + remaining patterns + final; file mode changes prose only; embedded PR/commit/doc mode returns final text only. `blader_humanizer/SKILL.md:47-53`

### S — hardikpandya_stop-slop
Root standalone `SKILL.md` plus three `references/*.md`; no `.claude-plugin/plugin.json`, marketplace, hooks, output-style file, or command file. Description-driven drafting/editing/review of prose. No persistence directive. MIT root license. `hardikpandya_stop-slop/SKILL.md:1-7`
- Delete filler and all adverbs. `hardikpandya_stop-slop/SKILL.md:13-15`
- Avoid formulaic contrasts, negative listing, dramatic fragments, and rhetorical setup. `hardikpandya_stop-slop/SKILL.md:17-17`
- Require a human subject and active voice; no passive constructions. `hardikpandya_stop-slop/SKILL.md:19-19`
- Name specific things and avoid vague extremes. `hardikpandya_stop-slop/SKILL.md:21-21`
- Address the reader rather than narrating from a distance. `hardikpandya_stop-slop/SKILL.md:23-23`
- Vary sentence/paragraph rhythm; prefer two items over three; ban em dashes. `hardikpandya_stop-slop/SKILL.md:25-25`
- State facts directly; skip hand-holding. `hardikpandya_stop-slop/SKILL.md:27-27`
- Rewrite quotable mic-drop lines; score five dimensions and revise below 35/50. `hardikpandya_stop-slop/SKILL.md:29-60`

References sharpen the constraints: `structures.md:122` says three-item lists become two or one; `phrases.md:55` says no softeners or hedges. These are stronger than merely “avoid unnecessary lists”.
### N — petergyang_no-ai-slop
Canonical `skills/no-ai-slop/SKILL.md`, required `eval.md`, root and skill `agents/openai.yaml`, Codex plugin present. **No checked-in Claude plugin/marketplace**, hooks, command file, or output-style file. A build script is not a checked-in Claude package. On-demand edit/detect via description; no session persistence. MIT root license. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:3` `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:10-22`
- Preserve personal vocabulary, cadence, bluntness, humor, uncertainty, digressions, and polish. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:24-27`
- Make minimum effective edits; front-load only when clarity improves. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:27-29`
- Keep meaning, nuance, and precision; invent nothing. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:30-31`
- Keep genuine qualifiers, clear spoken fragments, and characteristic long sentences. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:33-34`
- Use concrete facts, direct verbs, and the portability test. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:35-39`
- Preserve edge and structure unless they harm the piece. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:40-42`
- Ban named AI words; cut often-empty adverbs/phrases conditionally. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:44-50`
- Cut synthetic contrasts, faux insight, recap endings, and formatting slop. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:52-86`
- Dashes: none in short copy; one or two allowed in longer drafts if useful. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:88-88`
- Edit returns full draft + What changed; detect quotes patterns without rewriting, scoring, or guessing AI authorship. `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:10-14`

### E — obra_the-elements-of-style
Claude plugin/marketplace, Codex/Cursor/Devin/Kimi manifests, and other host adapters present. One canonical skill and `elements-of-style.md` reference. No SessionStart or UserPromptSubmit style injection; Codex manifest has `"hooks": {}`. OpenCode and Pi adapters register skill paths, not full prose rules each turn. `obra_the-elements-of-style/.codex-plugin/plugin.json:19-20` `obra_the-elements-of-style/.opencode/plugins/elements-of-style.js:13-20` `obra_the-elements-of-style/.pi/extensions/elements-of-style.ts:12-15`
Trigger is unusually broad: ANY prose humans read, including documentation, commits, errors, UI, comments, reports, and explanations. On-demand/model-selected, not an always-on hook. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:3` `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:14-24`. **LICENSE file absent**. Manifest says `Public Domain`; book says public-domain Strunk text. This literal label is not a canonical SPDX identifier; no CC0 or Unlicense grant is present, so neither is substituted. `obra_the-elements-of-style/.claude-plugin/plugin.json:9` `obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:3`. Reference is 12,154 whitespace words; skill warns “~12,000 tokens”, an upstream estimate rather than a measured count. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:12`
- Use ordinary punctuation and grammatical subjects. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:35-43`
- One paragraph per topic; topic sentence near the beginning. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:44-46`
- Prefer active voice. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:47-47`
- Prefer positive statements and concrete language. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:48-49`
- Omit needless words, not necessary detail. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:50-50`
- Avoid runs of loose sentences; use parallel form for coordinate ideas. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:51-52`
- Keep related words together and one tense in summaries. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:53-54`
- Put emphatic words at the sentence end. `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:55-55`

The reference has material exceptions: warranted fragments (`elements-of-style.md:218-222`), passive voice (`:351`), transition sentences (`:305`), restatement (`:307`), and negative/positive antithesis (`:409-413`). The short skill’s headlines must not be read as absolute bans.
### T — hexiecs_talk-normal
No Claude plugin manifest, marketplace, SessionStart/UserPromptSubmit hook, output-style directory, or slash-command directory. Two **installer skills**: `skill/SKILL.md` for OpenClaw and `skill-hermes/SKILL.md` for Hermes, both named `talk-normal`. Actual rules in root `prompt.md` and the two skill prompt copies; shorter `prompt-chatgpt.md` for custom instructions. Each bundle has `install.sh`; root and both bundle installers have the same implementation. MIT root license. `hexiecs_talk-normal/skill/SKILL.md:15-39` `hexiecs_talk-normal/skill-hermes/SKILL.md:17-37`
Trigger: invoke installer once, then **persisted always-on context**, not a per-turn workflow invocation. Installer checks `.`, `$HOME`, `$OPENCLAW_WORKSPACE`; within each, prefers `.hermes.md` → `HERMES.md` → `AGENTS.md`; creates `./AGENTS.md` if none exists, appends/replaces marker block, and removes it on uninstall. Markers prevent duplicate installation; they do not solve semantic rule conflicts. `hexiecs_talk-normal/install.sh:34-48` `hexiecs_talk-normal/install.sh:85-108`
- Answer first; add useful context only. `hexiecs_talk-normal/prompt.md:21-21`
- Ban negative contrast framing in any language/order; formal necessary/sufficient conditions have a narrow exception. `hexiecs_talk-normal/prompt.md:5-22`
- End with relevant concrete recommendation/step; no summary stamps or pleasantries. `hexiecs_talk-normal/prompt.md:23-23`
- Kill filler and never repeat the question. `hexiecs_talk-normal/prompt.md:24-25`
- Yes/no: answer plus one reasoning sentence; comparisons: recommendation with brief reason. `hexiecs_talk-normal/prompt.md:26-27`
- Code plus usage example when nontrivial. `hexiecs_talk-normal/prompt.md:28-28`
- Concept explanations: maximum three to five sentences; depth still matches complexity. `hexiecs_talk-normal/prompt.md:29-31`
- Use lists only for natural sequences/parallel content; comparisons max three to four points per side. `hexiecs_talk-normal/prompt.md:30-34`
- No conditional follow-up offers or unlock menus. `hexiecs_talk-normal/prompt.md:32-32`
- Say a point once; no second plain-language rewording block. `hexiecs_talk-normal/prompt.md:33-33`

All skills under either skill bundle: exactly the two SKILL.md paths above; both are communication installers, no unrelated coding/stats/setup skill beyond their own installation procedure. No lite/full/ultra/Wenyan modes. ChatGPT prompt has no frontmatter and no hook; it lacks the root prompt’s explicit formal-logic exception. Its recommendation-ending rule is unconditional (`prompt-chatgpt.md:23`) where root says “when relevant”.
### M — smixs_awesome-claude-output-styles
Collection of **20 selectable Claude output styles**, one `skills/style-maker/SKILL.md`, one slash command `commands/style.md`, optional `hooks/style-reminder.sh`, installer `install.sh`. No Claude plugin or marketplace JSON. Every style has `keep-coding-instructions: true`; body specifies rules when selected. Installing all styles does not activate all 20. Installing exactly one activates its frontmatter name in settings. `smixs_awesome-claude-output-styles/install.sh:22-27` `smixs_awesome-claude-output-styles/install.sh:153-160` `smixs_awesome-claude-output-styles/install.sh:188-195`
Trigger: a selected output style applies throughout the session/system prompt; descriptions label styles, not 20 independently auto-triggered skills. `style-maker` is description-triggered customization. `/style` has `disable-model-invocation: true` and changes the selected style for the next session. Optional `--enforce` registers UserPromptSubmit; it emits the **name-only reminder**, not the full body, and skips default/built-in styles. `smixs_awesome-claude-output-styles/commands/style.md:1-6` `smixs_awesome-claude-output-styles/commands/style.md:81-84` `smixs_awesome-claude-output-styles/hooks/style-reminder.sh:14-32`. Hook reads global settings only; picker can activate a project style in project settings, so enforcement can name a different style. `smixs_awesome-claude-output-styles/commands/style.md:60-62`
License **MIT** with explicit upstream notices in `LICENSE:5-15`; not evidence that current caveman is MIT. Styles are adaptations, not exact current upstream copies. Full description and word count of each style appears in Appendix A.
#### caveman
- Answer, reason, next step. `smixs_awesome-claude-output-styles/output-styles/caveman.md:13-14`
- Drop articles, hedging, preamble, and recap; fragments allowed. `smixs_awesome-claude-output-styles/output-styles/caveman.md:15-15`
- Keep precise terms; do not invent abbreviations. `smixs_awesome-claude-output-styles/output-styles/caveman.md:16-19`
- Use scan-friendly bullets/tables only when useful. `smixs_awesome-claude-output-styles/output-styles/caveman.md:20-20`
- Depth requests keep every fact; artifacts use normal language and ship bare. `smixs_awesome-claude-output-styles/output-styles/caveman.md:21-27`

#### adhd
- Action first; numbered multi-step work. `smixs_awesome-claude-output-styles/output-styles/adhd.md:13-16`
- Five-item lists; offer the rest on request. `smixs_awesome-claude-output-styles/output-styles/adhd.md:17-18`
- Restate state; estimate minutes; show wins without error drama. `smixs_awesome-claude-output-styles/output-styles/adhd.md:19-23`
- One topic; park tangents in a conditional offer. `smixs_awesome-claude-output-styles/output-styles/adhd.md:24-26`
- Depth cancels budgets; requested artifacts ship bare. `smixs_awesome-claude-output-styles/output-styles/adhd.md:27-33`

#### no-slop
- Concrete is/has claims; generic-sentence test. `smixs_awesome-claude-output-styles/output-styles/no-slop.md:13-18`
- Ordinary team vocabulary; one term per concept. `smixs_awesome-claude-output-styles/output-styles/no-slop.md:19-29`
- Useful positive claims and checkable insight. `smixs_awesome-claude-output-styles/output-styles/no-slop.md:22-27`
- Emotion tied to fact; teaching metaphor must be clear. `smixs_awesome-claude-output-styles/output-styles/no-slop.md:30-33`
- Full depth when asked; artifact alone. `smixs_awesome-claude-output-styles/output-styles/no-slop.md:34-40`

#### no-ai-slop
- Minimum words; portability test. `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:13-17`
- Recommend one thing with evidence. `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:18-23`
- Active plain verbs; explain mechanism precisely. `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:24-27`
- Stop on content; depth cancels budget. `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:28-32`
- Requested artifact alone. `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:33-35`

#### unslop
- Periods/commas, straight quotes; zero own em dashes. `smixs_awesome-claude-output-styles/output-styles/unslop.md:13-17`
- Plain words; protect defined technical nouns. `smixs_awesome-claude-output-styles/output-styles/unslop.md:18-25`
- Mechanism and evidence; honest uncertainty survives. `smixs_awesome-claude-output-styles/output-styles/unslop.md:26-34`
- Vary rhythm; real opinion; content-first open/close. `smixs_awesome-claude-output-styles/output-styles/unslop.md:35-45`
- Quiet formatting; natural item count; all depth and bare artifacts. `smixs_awesome-claude-output-styles/output-styles/unslop.md:46-58`

#### eli15
- Core max 150 words; answer first. `smixs_awesome-claude-output-styles/output-styles/eli15.md:13-13`
- Exactly one everyday analogy and its breaking point. `smixs_awesome-claude-output-styles/output-styles/eli15.md:14-17`
- Define jargon inline; memorable takeaway. `smixs_awesome-claude-output-styles/output-styles/eli15.md:18-20`
- Adapt to fluency; avoid just/simply. `smixs_awesome-claude-output-styles/output-styles/eli15.md:21-22`
- Depth cancels cap; artifact has no analogy/takeaway. `smixs_awesome-claude-output-styles/output-styles/eli15.md:23-28`

#### plain-english
- Maximum 20 words per sentence; one fact/action. `smixs_awesome-claude-output-styles/output-styles/plain-english.md:13-13`
- One word per meaning; active/simple verbs. `smixs_awesome-claude-output-styles/output-styles/plain-english.md:14-19`
- Condition before command; retain articles and that. `smixs_awesome-claude-output-styles/output-styles/plain-english.md:20-23`
- Define technical words inline. `smixs_awesome-claude-output-styles/output-styles/plain-english.md:24-25`
- Full-depth short sentences; artifact alone. `smixs_awesome-claude-output-styles/output-styles/plain-english.md:26-30`

#### executive
- Complete answer first. `smixs_awesome-claude-output-styles/output-styles/executive.md:13-15`
- Up to three full-sentence reasons. `smixs_awesome-claude-output-styles/output-styles/executive.md:16-18`
- Evidence underneath, offered on request. `smixs_awesome-claude-output-styles/output-styles/executive.md:19-20`
- Missing context permits two opening sentences; claim headings and exact numbers. `smixs_awesome-claude-output-styles/output-styles/executive.md:21-31`
- Depth outranks pyramid; artifact bare. `smixs_awesome-claude-output-styles/output-styles/executive.md:32-38`

#### smart-brevity
- Bold headline max six words. `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:13-15`
- One big new fact. `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:17-18`
- Literal Why it matters label; impact not background. `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:20-21`
- Optional Go deeper section with three to five one-line bullets. `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:23-25`
- Human sentences; around 200 words; no closing recap; depth drops template; artifact bare. `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:27-38`

#### analogy-engine
- One familiar domain throughout. `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:13-15`
- Explicit mapping of every moving part. `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:16-19`
- State where the analogy fails. `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:20-21`
- Land real answer in one or two sentences after analogy. `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:22-23`
- Depth expands mechanism; no analogy in requested artifact. `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:24-30`

#### feynman
- One concept, plain words, defined terms, concrete example. `smixs_awesome-claude-output-styles/output-styles/feynman.md:13-15`
- Name the hard part explicitly. `smixs_awesome-claude-output-styles/output-styles/feynman.md:16-19`
- Ask one or two check questions; wait without answering them. `smixs_awesome-claude-output-styles/output-styles/feynman.md:20-22`
- Calibrate to reader’s response. `smixs_awesome-claude-output-styles/output-styles/feynman.md:23-25`
- Depth expands all concepts; artifact bare without teaching/check. `smixs_awesome-claude-output-styles/output-styles/feynman.md:26-32`

#### thing-explainer
- Use very common words. `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:13-15`
- Explain things by function. `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:16-18`
- Keep real names exact and explain them. `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:19-21`
- Short sentences; mark unavoidable hard word. `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:22-25`
- Full depth in common words; artifacts use normal language. `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:26-31`

#### ladder
- Explain at three labeled levels. `smixs_awesome-claude-output-styles/output-styles/ladder.md:11-14`
- Five-year-old rung: two/three sentences with everyday picture. `smixs_awesome-claude-output-styles/output-styles/ladder.md:13-14`
- Teen rung: defined terms and at most one bounded analogy. `smixs_awesome-claude-output-styles/output-styles/ladder.md:16-17`
- Pro rung: precise, compact tradeoffs and edge cases. `smixs_awesome-claude-output-styles/output-styles/ladder.md:19-26`
- Trivial lookups get one rung; depth expands pro rung; artifact bare. `smixs_awesome-claude-output-styles/output-styles/ladder.md:28-37`

#### wait-what
- Open with current context/state. `smixs_awesome-claude-output-styles/output-styles/wait-what.md:13-16`
- Max 20-word sentences; active voice; one meaning per term. `smixs_awesome-claude-output-styles/output-styles/wait-what.md:17-19`
- Use project vocabulary and define new terms. `smixs_awesome-claude-output-styles/output-styles/wait-what.md:20-23`
- Re-pitch lost reader in simpler words. `smixs_awesome-claude-output-styles/output-styles/wait-what.md:24-25`
- Depth keeps all facts; artifact has no grounding wrapper. `smixs_awesome-claude-output-styles/output-styles/wait-what.md:26-33`

#### coach
- Lead with one outcome-changing point. `smixs_awesome-claude-output-styles/output-styles/coach.md:13-14`
- Short active sentences; spoken voice. `smixs_awesome-claude-output-styles/output-styles/coach.md:15-18`
- One vivid image per answer. `smixs_awesome-claude-output-styles/output-styles/coach.md:19-21`
- Truth and fix; no maybe/it seems hedges. `smixs_awesome-claude-output-styles/output-styles/coach.md:22-25`
- End with action; depth includes all facts; artifact bare. `smixs_awesome-claude-output-styles/output-styles/coach.md:26-33`

#### street
- Current slang/profanity, no costume. `smixs_awesome-claude-output-styles/output-styles/street.md:13-16`
- Claims need evidence; criticism needs fix. `smixs_awesome-claude-output-styles/output-styles/street.md:17-22`
- One/two slang hits per paragraph. `smixs_awesome-claude-output-styles/output-styles/street.md:23-24`
- Profanity never targets user; distinguish jokes/facts. `smixs_awesome-claude-output-styles/output-styles/street.md:25-28`
- Depth keeps voice; artifacts professional; lite drops profanity. `smixs_awesome-claude-output-styles/output-styles/street.md:29-41`

#### gen-z
- Use specified slang correctly. `smixs_awesome-claude-output-styles/output-styles/gen-z.md:13-20`
- One slang hit per sentence, two per paragraph. `smixs_awesome-claude-output-styles/output-styles/gen-z.md:21-22`
- Short energetic sentences; claim survives slang removal. `smixs_awesome-claude-output-styles/output-styles/gen-z.md:23-25`
- Depth cancels length, not slang limits. `smixs_awesome-claude-output-styles/output-styles/gen-z.md:26-28`
- Artifacts professional; lite/ultra/off variants. `smixs_awesome-claude-output-styles/output-styles/gen-z.md:29-38`

#### sportscaster
- Lean play-by-play. `smixs_awesome-claude-output-styles/output-styles/sportscaster.md:13-15`
- Reset state repeatedly. `smixs_awesome-claude-output-styles/output-styles/sportscaster.md:16-18`
- Explain importance and key actor. `smixs_awesome-claude-output-styles/output-styles/sportscaster.md:19-21`
- Setup, tension, climax, celebration; analyst beat for mechanism. `smixs_awesome-claude-output-styles/output-styles/sportscaster.md:22-30`
- Full depth cuts commentary before facts; artifacts professional. `smixs_awesome-claude-output-styles/output-styles/sportscaster.md:31-37`

#### yoda
- Plain mechanism first. `smixs_awesome-claude-output-styles/output-styles/yoda.md:13-15`
- One inverted final lesson. `smixs_awesome-claude-output-styles/output-styles/yoda.md:16-19`
- Short aphorisms, occasional Hmm/Mmm. `smixs_awesome-claude-output-styles/output-styles/yoda.md:20-24`
- At most one learner question; facts outrank gag. `smixs_awesome-claude-output-styles/output-styles/yoda.md:25-28`
- Depth uninverted except landing; artifact professional. `smixs_awesome-claude-output-styles/output-styles/yoda.md:29-35`

#### bedtime-story
- Five-sentence microstory, longer only on request. `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:13-15`
- Concept protagonist; calm rhythm. `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:16-19`
- Every story beat maps to real mechanism. `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:20-21`
- End with remember-this line; lookup answer first. `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:22-25`
- Depth ends story; artifact professional. `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:26-32`

**Common guardrails:** all 20 styles contain byte-exact code/commands/errors/paths/identifiers/numbers, scoped-condition and numeric-preservation rules, and full treatment of depth requests. Persona styles step out of character for risky/order-sensitive actions and persisted artifacts. Exact locations are each style’s `Guardrails` block (inventory and conflict evidence below). This is a scan of 20 style files, not an inference from one example.
`style-maker` core rules: interview once (~10 questions), turn preferences into countable directives, mine samples, include technical/risk guardrails, show draft/demo for approval, then install and activate; offer optional enforcement. `smixs_awesome-claude-output-styles/skills/style-maker/SKILL.md:19-43` `smixs_awesome-claude-output-styles/skills/style-maker/SKILL.md:45-94` `smixs_awesome-claude-output-styles/skills/style-maker/SKILL.md:96-116`. `/style` core rules: discover user/project styles, deduplicate by name with project precedence, choose target, update only proper settings, report in two lines. `smixs_awesome-claude-output-styles/commands/style.md:13-84`
### K — Kyaa-A_eli5
Claude plugin/marketplace and Codex plugin/marketplace present. One skill, no Markdown command directory or output-style file. MIT root license. Model-invocable on `/eli5`, “simplify”, “too complex”, and plain-language explanation of code/errors/concepts. Applies to current explanation/task, then exits unless asked to persist. `Kyaa-A_eli5/skills/eli5/SKILL.md:3` `Kyaa-A_eli5/skills/eli5/SKILL.md:46-52`
SessionStart hook exists, but **checks version only**: `hooks/hooks.json` → `scripts/check-update.mjs`. Startup matcher, five-second hook timeout, HTTPS latest-version fetch, 24-hour cache, update message when newer. It never reads/injects `SKILL.md`. Disabled by `ELI5_UPDATE_CHECK=0`. `Kyaa-A_eli5/hooks/hooks.json:3-12` `Kyaa-A_eli5/scripts/check-update.mjs:24-26` `Kyaa-A_eli5/scripts/check-update.mjs:109-133`
- One core idea; numbered single-sentence items if multiple. `Kyaa-A_eli5/skills/eli5/SKILL.md:12-12`
- No jargon; define unavoidable terms inline. `Kyaa-A_eli5/skills/eli5/SKILL.md:13-13`
- Use everyday analogies. `Kyaa-A_eli5/skills/eli5/SKILL.md:14-14`
- Max five sentences; ask whether reader wants more. `Kyaa-A_eli5/skills/eli5/SKILL.md:15-15`
- Explain code through short inline comments. `Kyaa-A_eli5/skills/eli5/SKILL.md:16-16`
- No preamble. `Kyaa-A_eli5/skills/eli5/SKILL.md:17-17`
- Simple version first; caveats only if asked. `Kyaa-A_eli5/skills/eli5/SKILL.md:18-18`
- Code-change summary/why: one sentence each, max two/three buckets. `Kyaa-A_eli5/skills/eli5/SKILL.md:20-26`
- Errors: one-sentence cause/fix plus minimal code change. `Kyaa-A_eli5/skills/eli5/SKILL.md:28-34`
- Prefer What/Why/Fix format; bare eli5 re-explains previous response. `Kyaa-A_eli5/skills/eli5/SKILL.md:36-48`

Its stated goal prioritizes clarity over precision and completeness; that is a direct conflict, not an assumed safety exception. `Kyaa-A_eli5/skills/eli5/SKILL.md:8`
### R — rahulj51_eli5
Claude plugin/marketplace and Codex plugin present; two skills `eli5` and `ste`. No hooks, output-style directory, or command-directory files. MIT root license. ELI5 triggers on the string anywhere or a simple/plain/executive version request; it targets a busy CTO/CPO, not a literal child. No persistent-mode/exit instruction. `rahulj51_eli5/skills/eli5/SKILL.md:3-14`
- Plain English and short common words; every word adds meaning. `rahulj51_eli5/skills/eli5/SKILL.md:18-19`
- Bottom line first. `rahulj51_eli5/skills/eli5/SKILL.md:20-20`
- Flat lists only; one/two sentences per item. `rahulj51_eli5/skills/eli5/SKILL.md:21-21`
- Define unavoidable jargon on first use. `rahulj51_eli5/skills/eli5/SKILL.md:22-22`
- Complete sentences; no fragments, abbreviations, or arrow chains. `rahulj51_eli5/skills/eli5/SKILL.md:23-23`
- One/three-sentence paragraphs; headings only for long content; no emoji. `rahulj51_eli5/skills/eli5/SKILL.md:24-26`
- Keep decision, action-relevant risks/costs/deadlines/questions, and accuracy/caveats. `rahulj51_eli5/skills/eli5/SKILL.md:28-33`
- Drop numbers/names that do not change the decision. `rahulj51_eli5/skills/eli5/SKILL.md:32-32`
- Short question: one/three sentences, no header/list; longer: summary plus flat list. `rahulj51_eli5/skills/eli5/SKILL.md:35-38`
- Readable in under one minute. `rahulj51_eli5/skills/eli5/SKILL.md:39-39`

**STE** is a separate controlled-language skill, not another ELI5 child analogy mode: exact trigger is “ste”/ASD-STE100/controlled technical English. Preserve meaning and necessary actions; use approved dictionary forms, one term per meaning, complete sentences/articles/no contractions, max 20 words procedural / 25 descriptive, no semicolon; protect code/identifiers verbatim; no formal compliance claim without an actual requested check. `rahulj51_eli5/skills/ste/SKILL.md:3-18` `rahulj51_eli5/skills/ste/SKILL.md:22-74`
### F — fcakyon ADHD output-style plugin only
Claude, Codex, and Cursor plugin manifests plus Gemini extension exist. Root repository marketplace registers the plugin; **no marketplace inside the scoped plugin directory**. No hooks or commands in this plugin. Root `LICENSE` is Apache-2.0; no scoped LICENSE file; plugin manifests explicitly agree. `fcakyon_claude-codex-settings/plugins/adhd-output-style/.claude-plugin/plugin.json:2-8` `fcakyon_claude-codex-settings/.claude-plugin/marketplace.json:72-84`. Unrelated plugins are excluded from behavior analysis.
Two entry paths: `skills/adhd-output-style/SKILL.md` is model-invocable on “ADHD output”, “fewer output tokens”, “short numbered steps”, or limited-memory formatting, and lasts for the current task. `output-styles/adhd-explanatory.md` says all interactions and declares `keep-coding-instructions: true` plus **`force-for-plugin: true`**. This is a declared forced output style, not a SessionStart hook; actual loader support was not run or verified. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:1-8` `fcakyon_claude-codex-settings/plugins/adhd-output-style/output-styles/adhd-explanatory.md:1-10`
- Open with action or answer. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:12-12`
- Number multi-step work; one action per step. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:13-13`
- End with one action under two minutes. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:14-14`
- Separate secondary issues and restate progress every turn. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:15-16`
- Concrete estimates; make wins visible. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:17-18`
- Errors: cause then fix, no alarm. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:19-19`
- Five-item lists; priority tiers for longer lists. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:20-20`
- No preamble, recap, or pleasantries. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:21-21`
- Walkthrough, destructive action, debug failure, and ambiguity exceptions. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:23-25`
- Before AND after coding, emit ★ Insight blocks with two/three codebase-specific points. `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:27-37`

All skills under this scoped plugin: **one**, `skills/adhd-output-style/SKILL.md`, communication/task formatting; no unrelated coding workflow, stats, setup, or migration skill. One output style; no lite/full/ultra/Wenyan modes. The teaching block is a material additional rule absent from ayghri’s canonical skill.
### U — user’s ELI5 output style
Requested absolute path absent. No file content, frontmatter, license, word count, packaging, trigger, or core rules can be reported. Matrix uses `?`, not “absent rule”.
## 2. Overlap matrix
Columns use source keys from section 1. `Y` = explicit coverage; `P` = qualified/partial coverage; `V` = only some variants/skills in that source; `—` = no explicit rule found in audited communication instructions; `?` = unreadable source. “Coverage” does not mean agreement: opposite prescriptions appear in section 3. Numbers identify lines of the primary instruction file listed immediately below. R’s `STE` and C’s `U` specify separate skills. M’s variants are explained after the matrix. Caps can be sentence, word, reading-time, or item caps; they are not interchangeable.
| Theme | C | A | H | S | N | E | T | M | K | R | F | U |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Answer-first / BLUF | Y32 | Y35,117 | Y373 | P15,39 | P28-29 | P46 | Y21 | V | Y17 | Y20 | Y12 | ? |
| No preamble / closer | Y39 | Y111-115 | Y112,319-320 | P15,39 | Y56,84 | — | Y23-24,32 | V | P17 | — | Y21 | ? |
| No recap | Y39 | Y113 | Y79,341 | — | Y84 | — | Y33 | V | — | — | Y21 | ? |
| Length cap | Y54 | — | — | — | — | — | Y29 | V | Y15 | Y24,37,39; STE46,54 | — | ? |
| List cap | — | P105-107 | P142 (anti-forced triads) | P ref structures122 | — | — | Y34 | V | P12,26 | P21 (nesting) | Y20 | ? |
| One next action | P32 | Y59 | — | — | P82,84 (next action allowed) | — | P23 (step when relevant) | V | P43 (format) | — | Y14 | ? |
| No tangents / topic drift | Y hook116-118 | Y64-71 | P373 | — | opposite:26,42 | Y book303 | P29,32 | V | P12 | — | Y15 | ? |
| Plain words / jargon explanation | Y43 | P138 (literal) | P45,268 | Y ref phrases37 | Y31,39 | P book32,421 | P3,33 | V | Y13 | Y18,22 | P18 | ? |
| Exact identifiers preserved | Y58 | — | Y51 (file mode) | — | P30,38 (facts; no byte rule) | — | — | Y all20 guardrails | — | V STE68 | — | ? |
| AI-tell phrase bans | Y39 | Y111-115 | Y201,319 | Y15,39-46 | Y46-50 | — | Y24 | V | P17 | — | P21 | ? |
| Em-dash ban | — | — | P162 (sample override) | Y25,43 | P88 (short copy) | — | — | V Unslop91-93 | — | — | — | ? |
| Voice preservation | — | — | Y43,387 | — | Y26-27 | — | — | V style-maker65-69 | — | — | — | ? |
| Fragments / dropping articles | Y47; U28 | — | opposite:79,189 | opposite:ref structures44 | P34 (voice); anti76 | P book208-222 (exception) | — | V | — | opposite:23; STE39,41 | — | ? |
| Analogies | — | P138 (cut figurative phrases) | — | — | P82 (delete metaphor kicker) | — | — | V | Y14 | — | — | ? |
| Honesty / no sycophancy | P26,87 (facts/negation) | Y137 (uncertainty) | Y15,37,320 | — | Y30,33,68 | — | — | V | opposite:8,18 (precision/caveats) | Y33; STE72 | — | ? |
| Scope adherence | Y80; hook116-118 | Y107,127-128 | Y34,51,53 | P3 (prose scope) | Y14 (detect scope) | P16-24 (prose scope) | Y32 | Y artifact/depth guardrails | Y52 (task lifetime) | P14 (explicit content scope) | Y6-8 (task) | ? |
Primary paths: C = `JuliusBrussee_caveman/skills/caveman/SKILL.md`, C U = `skills/ultracave/SKILL.md`, C hook = `src/hooks/caveman-mode-tracker.js`; A = `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md`; H = `blader_humanizer/SKILL.md`; S = `hardikpandya_stop-slop/SKILL.md`, S ref = its `references/`; N = `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md`; E = `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md`, E book = sibling `elements-of-style.md`; T = `hexiecs_talk-normal/prompt.md`; K/R = respective `skills/eli5/SKILL.md`; R STE = `rahulj51_eli5/skills/ste/SKILL.md`; F = scoped `skills/adhd-output-style/SKILL.md`.
M variant evidence: answer-first = `caveman.md:13`, versus context-first `wait-what.md:13-16` and analogy-first `analogy-engine.md:22-23`; preamble/recap = `adhd.md:26`, `smart-brevity.md:29`, `unslop.md:42-45`; length = `eli15.md:13`, `plain-english.md:13`, `bedtime-story.md:13-15`; list = `adhd.md:17-18`, `executive.md:16-18`, `smart-brevity.md:23-25`; next action = `coach.md:26-27`, `no-ai-slop.md:56-57`; tangents = `adhd.md:24-25`; jargon = `eli15.md:18-19`, `thing-explainer.md:13-25`; tells/dashes = `unslop.md:13-17,42-45,91-93`; fragments = `caveman.md:15`, articles retained = `plain-english.md:22-23`; analogy = `eli15.md:14-17`, `analogy-engine.md:13-23`; honesty = `coach.md:22-25`, `unslop.md:30-31`; scope/payload = all 20 `Guardrails` blocks, e.g. `caveman.md:25-41`. Each path in this paragraph is under `smixs_awesome-claude-output-styles/output-styles/`, except voice sampling at `skills/style-maker/SKILL.md:65-69`. “No recap” is not a ban on every summary: Rahul explicitly opens longer content with a summary.
## 3. CONFLICTS: exact text on both sides
Each item gives a concrete shared-input case. **Hard** means both directives cannot be obeyed in that case. **Conditional** requires overlapping scope or a particular writer sample/request. **Tension** is not a blanket contradiction. Selected styles from the same collection normally replace each other; their differences become conflicts if bodies are combined. Chat-only exemptions are applied before claiming a draft/commit conflict. No conflicts involving U are inferred.
### 1. Dropped grammar versus complete sentences — hard for chat explanations.
`JuliusBrussee_caveman/skills/ultracave/SKILL.md:28-28`
> 28: Drop articles, copulas, connectives when order stays clear.

`rahulj51_eli5/skills/eli5/SKILL.md:23-23`
> 23: - Write complete sentences. Do not compress into fragments, abbreviations, or arrow chains.

`rahulj51_eli5/skills/ste/SKILL.md:39-39`
> 39: - Write complete, short, clear sentences. Do not omit words. Do not use contractions.

`rahulj51_eli5/skills/ste/SKILL.md:41-41`
> 41: - Use articles and demonstrative adjectives when they are applicable.

`blader_humanizer/SKILL.md:189-189`
> 189: **Problem:** The text hides who acts or drops the subject. Use active voice when it makes the actor and action clearer. *Weak alone.*

`hardikpandya_stop-slop/references/structures.md:44-44`
> 44: **Instead:** Complete sentences. Trust content over presentation.

Base caveman merely permits omission when readable (`caveman:47`); ultra requires stripped grammar. Rahul requires whole sentences. Strunk permits warranted emphasis fragments, so its headline is not an absolute grammar ban.

### 2. Cutting all articles in persisted context versus normal prose — hard when rewriting the same Markdown document.
`JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:39-39`
> 39: - Articles: a, an, the

`JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:66-66`
> 66: - Fragments OK: "Run tests before commit" not "You should always run tests before committing"

`rahulj51_eli5/skills/ste/SKILL.md:39-41`
> 39: - Write complete, short, clear sentences. Do not omit words. Do not use contractions.
> 40: - Use a vertical list when it makes complex text easier to understand.
> 41: - Use articles and demonstrative adjectives when they are applicable.

`smixs_awesome-claude-output-styles/output-styles/plain-english.md:22-23`
> 22: - Keep the articles and the word "that". Short is not the goal — clear is.
> 23:   ("STE is short, not terse.")

Caveman-compress is explicitly exempt from the chat-only artifact boundary. Normal caveman by itself does not impose this on published drafts.

### 3. Universal short sentences versus varied/natural sentence length — conditional when a source sentence needs more than 20 words.
`JuliusBrussee_caveman/skills/caveman/SKILL.md:54-54`
> 54: ASD-STE100 is the floor: 20 words max, active voice, imperative for instructions, one term per thing, pronoun only with an obvious referent. Compression and clarity conflict? Clarity wins.

`hardikpandya_stop-slop/SKILL.md:25-25`
> 25: 6. **Vary rhythm.** Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes.

`blader_humanizer/SKILL.md:39-39`
> 39: 4. **Write the final version.** State each point naturally instead of patching flagged phrases one at a time. If a sentence stays awkward, rewrite the paragraph around its main point. Vary sentence length; real writing alternates short and long.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:34-34`
> 34: - **Untangle sentences without flattening the cadence.** Split sentences and paragraphs when they are genuinely hard to follow. Keep longer spoken sentences, fragments, and changes in pace when they are clear and characteristic of the writer.

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:469-469`
> 469: Vigorous writing is concise. A sentence should contain no unnecessary words, a paragraph no unnecessary sentences, for the same reason that a drawing should have no unnecessary lines and a machine no unnecessary parts. This requires not that the writer make all his sentences short, or that he avoid all detail and treat his subjects only in outline, but that he make every word tell.

Natural rhythm may be retained by Humanizer/No AI Slop; Strunk explicitly says concise does not require all sentences short. A mix of short sentences can coexist with a 20-word ceiling, so variation alone is not a hard conflict.

### 4. Restating state versus each fact once / no recap — hard if last turn’s unchanged state is repeated.
`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:73-78`
> 73: ### 5. Restate state every turn
> 74: 
> 75: The reader cannot hold "we are on step 3 of 5" between messages. Restate it.
> 76: 
> 77: Bad: "Done. Ready for the next part?"
> 78: Good: "Step 3 of 5 done: schema updated. Next: backfill the new column. Run the script?"

`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:16-16`
> 16: - Restate progress each turn (e.g. "step 3 of 5"); assume prior context is lost.

`JuliusBrussee_caveman/skills/ultracave/SKILL.md:38-40`
> 38: ### 3. Each fact once
> 39: 
> 40: No restating, no summary after a list.

`blader_humanizer/SKILL.md:30-30`
> 30: Two rules follow from this. Every sentence you keep must add something the reader did not already have, from earlier in the text or from the conversation around it. A tell counts in proportion to how rarely a careful writer would make it on purpose. The patterns are numbered strongest first: §1 to §5 justify an edit on one sighting, and a pattern marked *weak alone* needs company from other tells in the same passage before you act.

`hexiecs_talk-normal/prompt.md:33-33`
> 33: - Do not restate the same point in "plain language" or "in human terms" after already explaining it. Say it once clearly. No "翻成人话", "in other words", "简单来说" rewording blocks.

Visible new completion information can satisfy all sides. Repeating unchanged progress each turn cannot. ADHD itself distinguishes useful state from a completed-task recap.

### 5. Opening with next action versus mandatory grounding — hard when grounding is not itself an action.
`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:35-35`
> 35: The first line is something the reader can do. Not context. Not a plan. The action.

`smixs_awesome-claude-output-styles/output-styles/adhd.md:13-14`
> 13: 1. **Lead with the next action.** First line = what to do now. Context comes
> 14:    after, for those who keep reading.

`smixs_awesome-claude-output-styles/output-styles/wait-what.md:13-16`
> 13: 1. **Never assume the reader kept up.** Open every substantive answer with
> 14:    one line of grounding — what we are doing and where we are — as if the
> 15:    reader just came back to their desk: "We are fixing the login timeout;
> 16:    the cause is found."

`JuliusBrussee_caveman/skills/caveman/SKILL.md:32-32`
> 32: Answer, then reason, then next step. Pattern: `[thing] [action] [reason]. [next step].`

Wait What’s opening is context. Base caveman’s first slot is answer; ADHD’s first slot is action. They can coincide for command answers, not every conceptual answer.

### 6. Analogy before real answer versus answer-first — hard for the specified order.
`smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:22-23`
> 22: 4. **Then land the real answer** in one or two plain sentences, using the real
> 23:    terms — the analogy is scaffolding, not the building.

`rahulj51_eli5/skills/eli5/SKILL.md:20-20`
> 20: - Lead with the point. The first sentence gives the bottom line.

`hexiecs_talk-normal/prompt.md:21-21`
> 21: - Lead with the answer, then add context only if it genuinely helps

`smixs_awesome-claude-output-styles/output-styles/executive.md:13-15`
> 13: 1. **The answer, first sentence.** A complete claim, not a topic. "The
> 14:    migration is safe to run tonight; one risk needs your call" — never
> 15:    "Here's an analysis of the migration."

An analogy can itself answer some questions. This conflict concerns the explicit instruction to land the real answer after it.

### 7. Fixed five-sentence concepts versus full requested walkthroughs — hard for a complex “explain properly” request.
`Kyaa-A_eli5/skills/eli5/SKILL.md:15-15`
> 15: 4. **Max 5 sentences** for any single explanation. If more detail is needed, stop and ask "Want me to go deeper on any part?"

`hexiecs_talk-normal/prompt.md:29-29`
> 29: - Explanations: 3-5 sentences max for conceptual questions. Cover the essence, not every subtopic. If the user wants more, they will ask.

`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:123-123`
> 123: 1. User asks to "explain" or "walk me through." Explain fully. Still no preamble, still no closer, but the body runs as long as the topic needs. Add headers so the reader can skim back.

`smixs_awesome-claude-output-styles/output-styles/eli15.md:23-26`
> 23: - Asked for the full picture ("explain it properly", "why did this happen")?
> 24:   The 150-word cap is off for that answer. Every decision, number, threshold,
> 25:   condition and risk goes in, still in teenager-plain words. One analogy
> 26:   remains the limit.

Talk-normal also says match complexity (`:31`) but does not explicitly lift its concept sentence cap. Kyaa lifts detail only by asking for another turn, not by its own full-depth override.

### 8. Precision/completeness versus maximally simple output — hard when simplification drops a material fact.
`Kyaa-A_eli5/skills/eli5/SKILL.md:8-8`
> 8: Strip all complexity from explanations. Prioritize clarity over precision. The goal is instant understanding, not completeness.

`rahulj51_eli5/skills/eli5/SKILL.md:33-33`
> 33: - Accuracy. Simple must not become wrong. If a simplification loses an important caveat, keep the caveat in one short sentence.

`JuliusBrussee_caveman/skills/caveman/SKILL.md:11-11`
> 11: Respond terse like smart caveman. All technical substance stay. Only fluff die.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:31-31`
> 31: - **Open it up, don't dumb it down.** Keep the substance, nuance, and precision. Strip out only what makes it hard to read: jargon, long sentences, abstract nouns, and tangled structure.

`smixs_awesome-claude-output-styles/output-styles/eli15.md:7-7`
> 7: You are an interactive agent that helps users with software engineering tasks. In addition to completing those tasks, you must explain everything to a smart 15-year-old: curious, quick, zero background. Simple explanations are not dumbed-down explanations — keep the substance, change the words.

This is a content-preservation conflict, not just a difference in audience.

### 9. Caveats only if asked versus required risks/caveats — hard when a caveat changes the conclusion.
`Kyaa-A_eli5/skills/eli5/SKILL.md:18-18`
> 18: 7. **No caveats up front.** Don't lead with edge cases or exceptions. Give the simple version first. Mention caveats only if asked.

`rahulj51_eli5/skills/eli5/SKILL.md:31-33`
> 31: - Anything the reader must act on: risks, costs, deadlines, open questions.
> 32: - Numbers and names that change the reader's decision. Drop the rest.
> 33: - Accuracy. Simple must not become wrong. If a simplification loses an important caveat, keep the caveat in one short sentence.

`rahulj51_eli5/skills/ste/SKILL.md:22-22`
> 22: 1. Keep the meaning, facts, risks, limits, names, and necessary actions from the source.

`smixs_awesome-claude-output-styles/output-styles/eli15.md:16-17`
> 16: - After the analogy, say where it breaks: "The comparison stops working
> 17:   here, because…". A misleading intuition is worse than no analogy.

Kyaa’s instruction does not provide an accuracy/risk exception at that line. The other sources explicitly retain caveats or analogy limits.

### 10. Dropping decision-irrelevant names/numbers versus exact technical payload — hard when asked to summarize technical content retaining every value.
`rahulj51_eli5/skills/eli5/SKILL.md:32-32`
> 32: - Numbers and names that change the reader's decision. Drop the rest.

`JuliusBrussee_caveman/skills/caveman/SKILL.md:47-47`
> 47: Drop a/an/the when the sentence still reads in one pass. Fragments fine. Never drop not/never/no/only/except. Numbers and units exact.

`JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:53-54`
> 53: - Proper nouns (project names, people, companies)
> 54: - Dates, version numbers, numeric values

`smixs_awesome-claude-output-styles/output-styles/caveman.md:36-41`
> 36: Code, commands, error strings, file paths, identifiers, numbers: byte-exact,
> 37: never compressed. Full normal language for: security warnings, destructive or
> 38: irreversible action confirmations, multi-step instructions where order
> 39: matters, and any moment reader confusion is likely. Say serious thing plainly,
> 40: then back to caveman. Never widen scoped condition ("only under load") to
> 41: blanket ("always"). Never round off number that makes claim actionable.

Rahul’s ordinary ELI5 is selective; its STE skill instead preserves protected data. Do not merge the two Rahul skills into one rule.

### 11. Inline code comments versus protected code — conditional during a pure explanation/rewrite.
`Kyaa-A_eli5/skills/eli5/SKILL.md:16-16`
> 16: 5. **Code comments over prose.** When explaining code, add short inline comments rather than writing paragraphs about it.

`JuliusBrussee_caveman/skills/caveman/SKILL.md:58-58`
> 58: Code blocks unchanged. Commands, paths, API names exact. Errors quoted exact, shortest decisive line only.

`blader_humanizer/SKILL.md:51-51`
> 51: **File mode.** When the user names a file, run the full process but write only the final text to the file. Change prose only. Keep code blocks, inline code, commands, paths, YAML metadata, data, and link targets unchanged. Then give the user a short summary.

`rahulj51_eli5/skills/ste/SKILL.md:68-68`
> 68: Do not change code, commands, file paths, URLs, identifiers, data, or text that the user requires verbatim. Use necessary product and subject terms only when they qualify as STE technical nouns or technical verbs. Clearly separate protected text from the STE text.

Adding comments changes source text; Humanizer file-mode and verbatim rewrite contracts forbid this. A user-authorized code edit is a distinct scope and can permit comments.

### 12. Numbering multi-step tasks versus three-item suppression — hard for an irreducible three-step procedure.
`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:44-44`
> 44: If the work takes more than one step, write a numbered list. Each step is one bounded action. No step contains "and then" twice.

`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:13-13`
> 13: - Break multi-step work into numbered lists, one action per step.

`hardikpandya_stop-slop/references/structures.md:122-122`
> 122: | Three-item lists | Use two items or one |

`blader_humanizer/SKILL.md:142-142`
> 142: **Problem:** Ideas arrive in threes to sound complete, whether the meaning has three parts or not. The tell can be one sentence ("innovation, inspiration, and insights"), three parallel examples, or three short facts followed by a lesson. Check that each item adds a distinct idea. Merge examples, develop the strongest one, or vary the structure when they do not. Keep three real items when the meaning needs three.

Humanizer does NOT ban genuine lists: it explicitly keeps three real items. Stop-slop’s “two items or one” is the stricter contradictory side. ADHD versus Humanizer is only a tension when labels or grouping add no information.

### 13. Five visible items versus completeness — hard for older/adapted strict cap; qualified in current ayghri.
`smixs_awesome-claude-output-styles/output-styles/adhd.md:17-18`
> 17: 3. **Lists cap at 5 items.** More than five means you haven't prioritized —
> 18:    pick the five that matter, offer the rest on request.

`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:20-20`
> 20: - Cap lists at five items; split longer ones into priority tiers.

`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:105-107`
> 105: For long lists in the final response, group related items and rank the most relevant first. Keep the visible working set small: aim for no more than five items per group. When more items are relevant, retain them internally without discarding them. Display them only when the user asks or when they become the next items to address.
> 106: 
> 107: Never omit relevant items when completeness matters. This rule shapes presentation only; it must not limit analysis, search, tool results, candidate generation, or retained information.

`JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:59-60`
> 59: - Bullet point hierarchy (keep nesting level)
> 60: - Numbered lists (keep numbering)

Ayghri says never omit relevant items when completeness matters; grouping resolves many cases. Smixs defers items until requested. Preserving an existing six-item hierarchy during file compression conflicts with regrouping it.

### 14. Flat lists versus preserved nesting — hard for a nested document rewrite.
`rahulj51_eli5/skills/eli5/SKILL.md:21-21`
> 21: - Lists are single level only. Never nest. Each item is one or two short sentences, also in plain English.

`JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:57-62`
> 57: ### Preserve Structure
> 58: - All markdown headings (keep exact heading text, compress body below)
> 59: - Bullet point hierarchy (keep nesting level)
> 60: - Numbered lists (keep numbering)
> 61: - Tables (compress cell text, keep structure)
> 62: - Frontmatter/YAML headers in markdown files

Rahul explicitly forbids nesting; compression explicitly retains it.

### 15. Required next-action closing versus ending when done — hard for a completed answer with no remaining action.
`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:14-14`
> 14: - End with a single next action that takes under two minutes.

`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:59-59`
> 59: If anything is left open, name ONE thing the reader can do in under two minutes. Even "open the file" counts.

`smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:28-29`
> 28: 7. **End when done.** The last sentence is content — a fact or a next step.
> 29:    When the point is made, stop.

`hexiecs_talk-normal/prompt.md:23-23`
> 23: - End with a concrete recommendation or next step when relevant. Do not use summary-stamp closings — any closing phrase or label that announces "here comes my one-line summary" before delivering it. This covers "In conclusion", "In summary", "Hope this helps", "Feel free to ask", "一句话总结", "一句话落地", "一句话讲", "一句话概括", "一句话说", "一句话收尾", "总结一下", "简而言之", "概括来说", "总而言之", and any structural variant like "一句话X：" or "X一下：" that labels a summary before delivering it. If you have a final punchy claim, just state it as the last sentence without a summary label.

Fcakyon is unconditional; ayghri says only if something remains; talk-normal says when relevant. Merely allowing a meaningful next step is not a contradiction.

### 16. Follow-up offer at sentence cap versus banned conditional offers — hard.
`Kyaa-A_eli5/skills/eli5/SKILL.md:15-15`
> 15: 4. **Max 5 sentences** for any single explanation. If more detail is needed, stop and ask "Want me to go deeper on any part?"

`hexiecs_talk-normal/prompt.md:32-32`
> 32: - Do not end with hypothetical follow-up offers or conditional next-step menus. This includes "If you want, I can also...", "如果你愿意，我还可以...", "If you tell me...", "如果你告诉我...", "如果你说X，我就Y", "我下一步可以...", "If you'd like, my next step could be...". Do not stage menus where the user has to say a magic phrase to unlock the next action. Answer what was asked, give the recommendation, stop. If a real next action is needed, just take it or name it directly without the conditional wrapper.

`blader_humanizer/SKILL.md:319-320`
> 319: **Watch for:** I hope this helps, Of course!, Certainly!, Great question!, You're absolutely right, Would you like..., Want me to...?, Should I continue?, let me know, here is a...
> 320: **Problem:** A chatbot's greeting, praise, offer, or closing remains in text that should stand on its own. It is the most certain tell in this list and the easiest to miss when it wraps real content. Remove the wrapper and keep the content.

`smixs_awesome-claude-output-styles/output-styles/adhd.md:24-25`
> 24: 7. **One topic per message.** Park tangents in a single line: "(separate
> 25:    topic: the flaky test — say the word and we'll do it next)".

Smixs ADHD’s “say the word” tangent line is the very unlock-menu pattern talk-normal bans. Humanizer’s chatbot-residue rule pertains to text that should stand alone.

### 17. Re-explain at three levels versus say once / no repeat — hard for one conceptual answer.
`smixs_awesome-claude-output-styles/output-styles/ladder.md:7-7`
> 7: You are an interactive agent that helps users with software engineering tasks. In addition to completing those tasks, you must answer every substantive question three times, on a ladder. The reader climbs until they slip, and that rung tells them — and you — exactly where their understanding ends. Nobody has to guess their level in advance.

`smixs_awesome-claude-output-styles/output-styles/ladder.md:22-26`
> 22: Label the rungs exactly like that. Keep the whole ladder tighter than one
> 23: normal long answer — three short passes, not three essays. Each rung answers
> 24: the actual question; deeper rungs add precision, never contradict the rung
> 25: above (if a simplification above was a white lie, say so on the rung where it
> 26: stops being true).

`JuliusBrussee_caveman/skills/ultracave/SKILL.md:40-40`
> 40: No restating, no summary after a list.

`hexiecs_talk-normal/prompt.md:33-33`
> 33: - Do not restate the same point in "plain language" or "in human terms" after already explaining it. Say it once clearly. No "翻成人话", "in other words", "简单来说" rewording blocks.

Explicit later user requests to re-explain are separate answers. Kyaa bare eli5 re-explains the previous response by user request, so that is not itself an unsolicited-repeat conflict.

### 18. Memorable takeaway / final aphorism versus cut redundant kicker — hard when it repeats the explanation.
`smixs_awesome-claude-output-styles/output-styles/eli15.md:20-20`
> 20: - End with one sentence the reader could repeat to a friend tomorrow.

`smixs_awesome-claude-output-styles/output-styles/yoda.md:16-19`
> 16: - **Invert only the landing.** The final line of an answer — the lesson, the
> 17:   aphorism — goes object-subject-verb: "Test it before you trust it, you
> 18:   must." One inverted line per answer; invert everything and readable it is
> 19:   not.

`smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:22-23`
> 22: - **End with the one thing to remember**, said simply, like a goodnight:
> 23:   "And so: give every listener a way to leave, and the memory stays tidy."

`blader_humanizer/SKILL.md:79-79`
> 79: **Problem:** The line asks the reader to pause on a claim instead of adding to it. One short sentence can carry emphasis when it carries a new fact. Cut a closer that repeats, including one that explains an example the reader just saw. Keep it when it adds a fact or consequence the example does not show. Merge a row of fragments into a sentence with a specific claim.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:82-82`
> 82: **Fake-profound kickers.** Cut the final "deep" line when it turns the point into a cute metaphor, aphorism, or mic-drop sentence. Do not rewrite it into a better metaphor. Do not preserve the rhythm. Delete it, then end on the clearest concrete sentence already in the draft. If the ending needs more closure, add a plain takeaway or next action.

A new actionable consequence at the end can coexist; a compulsory repeated lesson cannot.

### 19. Educational Insight wrappers versus bounded tool chatter / artifact-only output — conditional around coding.
`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:29-37`
> 29: Before and after writing code, add a short educational note using this block:
> 30: 
> 31: `★ Insight ─────────────────────────────────────`
> 32: [2-3 codebase-specific educational points]
> 33: `─────────────────────────────────────────────────`
> 34: 
> 35: Put depth here, not in the main answer. Prefer insights specific to this
> 36: codebase or the code just written over general programming concepts. Cap at
> 37: three points so the block stays scannable. The rest of the response stays terse.

`JuliusBrussee_caveman/skills/caveman/SKILL.md:62-62`
> 62: No text between routine calls. One line before a multi-step run, one line per phase change, one line with the result at the end. Otherwise text before a call only to clarify, warn, or disambiguate.

`smixs_awesome-claude-output-styles/output-styles/caveman.md:25-27`
> 25: - Reader ask you write thing — commit message, email, snippet — give thing
> 26:   only. No lead-in. No offer to change it. Thing itself use normal full
> 27:   language, not caveman: caveman talk in chat, never in artefact.

`blader_humanizer/SKILL.md:53-53`
> 53: **Embedded mode.** When another task uses this skill for a pull request, commit message, or document, return only the final text.

Fcakyon’s before/after code teaching is extra commentary. It can be useful for education, but those literal wrappers violate bare-artifact mode when carried into a snippet-only answer. They are not a registered hook.

### 20. Bold labels and fixed templates versus content-led formatting — conditional when the labels add no information.
`Kyaa-A_eli5/skills/eli5/SKILL.md:40-44`
> 40: ```
> 41: **What:** [one sentence]
> 42: **Why:** [one sentence]
> 43: **Fix/Action:** [one sentence or short code snippet]
> 44: ```

`smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:20-25`
> 20: **Why it matters:** — literally that label, then one or two sentences of
> 21: impact. Not background, impact.
> 22: 
> 23: **Go deeper:** — optional bullets for those who want more: details, numbers,
> 24: links, code. Three to five bullets, each one line. This is where the
> 25: substance lives, so the substance survives — it's just filed, not deleted.

`blader_humanizer/SKILL.md:280-280`
> 280: **Problem:** Words are bolded without a reason, and vertical lists give every item a bold label and a colon. Remove the bold. Turn a labeled list into prose when the labels carry no information of their own.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:86-86`
> 86: **Formatting slop.** Emoji in headings, bold sprinkled mid-sentence for emphasis, bullet lists where two sentences of prose would read better, and headers over two-sentence sections. Format should follow the content, not decorate it.

`smixs_awesome-claude-output-styles/output-styles/unslop.md:46-51`
> 46: 8. **Quiet formatting, and some mess.** Sentence-case headings, no decorative
> 47:    emoji. Bold marks a term the reader will meet again, not every proper noun,
> 48:    and a bold lead-in earns its place only when what follows is new detail.
> 49:    Perfect parallel structure looks machine-made, so use the natural number of
> 50:    items rather than three, and repeat the right word instead of cycling
> 51:    synonyms for it.

Humanizer/No AI Slop remove decorative labels, not every labeled structure. What/Why/Fix can be meaningful. Smart Brevity’s literal label cannot be varied according to content.

### 21. Preserve author’s voice versus universal compression/persona — conditional shared rewrite; scope matters.
`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:26-27`
> 26: - **Preserve the writer's real voice.** First notice the draft's vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish. Keep the traits that feel personal to the writer. Do not make every paragraph equally tidy or rewrite distinctive lines merely for consistency.
> 27: - **Make the minimum effective edit.** Fix AI patterns, errors, repetition, and unclear passages. Leave strong human sentences alone. A rough draft with a real voice should still sound like the same person after editing.

`blader_humanizer/SKILL.md:43-43`
> 43: If the user gives a writing sample, read it first and match its sentence length, word choice, punctuation, openings, and transitions. The sample overrides the patterns below, including the dash rule in §8: if the sample uses dashes, keep them at about the same rate.

`JuliusBrussee_caveman/skills/ultracave/SKILL.md:28-28`
> 28: Drop articles, copulas, connectives when order stays clear.

`JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:39-44`
> 39: - Articles: a, an, the
> 40: - Filler: just, really, basically, actually, simply, essentially, generally
> 41: - Pleasantries: "sure", "certainly", "of course", "happy to", "I'd recommend"
> 42: - Hedging: "it might be worth", "you could consider", "it would be good to"
> 43: - Redundant phrasing: "in order to" → "to", "make sure to" → "ensure", "the reason is because" → "because"
> 44: - Connective fluff: "however", "furthermore", "additionally", "in addition"

`smixs_awesome-claude-output-styles/output-styles/street.md:33-35`
> 33: - Somebody asks you to write the thing — commit message, email, PR body —
> 34:   you hand over the thing alone. Clean professional English inside it, no
> 35:   slang, and nothing wrapped around it.

Base caveman/ultra exempts persisted documents; therefore a published-draft clash is NOT caused by merely enabling caveman. It arises with `/caveman-compress`, or a generic persona applied to the same chat text. Street requires professional English in artifacts, which can erase an explicitly personal profane draft’s voice.

### 22. Personal detours versus single-topic/no-tangent output — conditional if editing the same personal piece.
`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:26-26`
> 26: - **Preserve the writer's real voice.** First notice the draft's vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish. Keep the traits that feel personal to the writer. Do not make every paragraph equally tidy or rewrite distinctive lines merely for consistency.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:42-42`
> 42: - **Keep structure unless it's hurting the piece.** Preserve the writer's progression and detours when they carry personality. If you reorganize, say why in the What changed section.

`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:66-66`
> 66: If a second issue exists, finish the first, then offer the second as a separate question.

`JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js:116-118`
> 116:     ' Answer only what was asked: no unrequested background, lists, examples,' +
> 117:     ' walkthroughs, or follow-up offers; give code, steps, or warnings when the' +
> 118:     ' task needs them. Security warnings, irreversible actions, multi-step order:' +

A personal aside may be part of the requested draft rather than an unrequested tangent; classify it before deleting. Chat scope and prose editing are different defaults.

### 23. Absolute em-dash ban versus voice-matched/limited permission — hard with a dash-using writer sample or long draft.
`hardikpandya_stop-slop/SKILL.md:25-25`
> 25: 6. **Vary rhythm.** Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes.

`hardikpandya_stop-slop/SKILL.md:43-43`
> 43: - Em-dash anywhere? Remove it.

`blader_humanizer/SKILL.md:162-162`
> 162: **Rule:** The final rewrite must not contain em dashes (—) or en dashes (–) unless the writer's sample uses them; then match the sample's rate. Replace each dash with a period, comma, colon, or parentheses, or rewrite the sentence. This includes spaced dashes and double hyphens (` -- `) used as dashes. Leave dashes and hyphens inside code blocks, inline code, commands, paths, and URLs alone.

`blader_humanizer/SKILL.md:43-43`
> 43: If the user gives a writing sample, read it first and match its sentence length, word choice, punctuation, openings, and transitions. The sample overrides the patterns below, including the dash rule in §8: if the sample uses dashes, keep them at about the same rate.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:88-88`
> 88: **Em dashes.** Do not use them as a default rhythm crutch. In short copy, use none. In longer drafts, 1-2 are fine if they clearly beat commas, periods, or parentheses. Remove clusters and decorative dashes.

`smixs_awesome-claude-output-styles/output-styles/unslop.md:91-93`
> 91: Count the em dashes and the curly quotes in your own prose, skipping anything
> 92: the guardrails hold exact. Zero of each. Then ask what still makes this read as
> 93: machine-written, and fix that.

Humanizer sample override is explicit. No AI Slop permits one/two in longer drafts; Stop Slop and Unslop require zero own-prose dashes. None of this permits altering protected code or literal quotations.

### 24. No adverbs/no hedges versus meaningful uncertainty and voice — hard when “maybe” carries epistemic uncertainty.
`hardikpandya_stop-slop/references/phrases.md:55-55`
> 55: Kill all adverbs. No -ly words. No softeners, no intensifiers, no hedges.

`hardikpandya_stop-slop/SKILL.md:35-35`
> 35: - Any adverbs? Kill them.

`JuliusBrussee_caveman/skills/caveman/SKILL.md:39-39`
> 39: No greeting, hedging, pleasantries, recap, or closer. No "Sure!", "Let me", "I'll now", "Hope this helps". No just/really/basically/actually/simply.

`smixs_awesome-claude-output-styles/output-styles/coach.md:24-25`
> 24: - Grade 9 readability. No adverbs doing a verb's job, no hedges ("maybe",
> 25:   "it seems"), no qualifiers padding the hit.

`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:137-137`
> 137: 4. Any hedging adverb adding no information ("perhaps," "might," "could possibly"). Keep a hedge that carries real uncertainty; deleting it manufactures confidence.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:33-33`
> 33: - **Make every sentence earn its place.** Cut empty qualifiers and throat-clearing. Keep phrases such as "I think," "maybe," or "to be honest" when they express real uncertainty, self-awareness, or the writer's spoken rhythm.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:48-48`
> 48: Often-empty adverbs: just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably. Cut them when they add nothing. Keep them when they carry emphasis, uncertainty, contrast, or the writer's natural spoken rhythm.

`blader_humanizer/SKILL.md:172-172`
> 172: **Problem:** Repeated editing adds one qualifier after another until every claim sounds uncertain, usually to repair an earlier overstatement rather than to report real doubt. Keep a qualifier only when the source supports it and the meaning needs it. Keep scope statements, legal and safety notices, and real corrections. Ordinary hedges such as *perhaps* or *tends to* are human habits and not tells. *Weak alone.*

Ayghri explicitly warns that deleting a real hedge manufactures confidence. Base caveman’s security/full-prose exceptions mitigate some cases but its ordinary chat rule still bans hedging.

### 25. Active voice only / human subject always versus useful passive or machine actor — hard in technical descriptions.
`hardikpandya_stop-slop/SKILL.md:19-19`
> 19: 3. **Use active voice.** Every sentence needs a human subject doing something. No passive constructions. No inanimate objects performing human actions ("the complaint becomes a fix").

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:351-351`
> 351: This rule does not, of course, mean that the writer should entirely discard the passive voice, which is frequently convenient and sometimes necessary.

`blader_humanizer/SKILL.md:189-189`
> 189: **Problem:** The text hides who acts or drops the subject. Use active voice when it makes the actor and action clearer. *Weak alone.*

`rahulj51_eli5/skills/ste/SKILL.md:36-36`
> 36: - Use the active voice. In descriptive writing, use the passive voice only when the agent is unknown.

`smixs_awesome-claude-output-styles/output-styles/plain-english.md:16-17`
> 16: - Active voice, simple tenses. "The server rejects the request", not "the
> 17:   request would be getting rejected".

Strunk and STE allow passive when needed/actor unknown. “The server rejects the request” uses a machine subject that Stop Slop’s literal human-subject requirement disallows, though many human editors would find it ordinary.

### 26. Prohibit negative contrasts versus meaningful correction / antithesis — hard for a real two-sided contrast outside formal proofs.
`hexiecs_talk-normal/prompt.md:22-22`
> 22: - Do not use negation-based contrastive phrasing in any position. This covers any sentence structure where a negative adverb rejects an alternative to set up or append to a positive claim: in any order ("reject then correct" or "correct then reject"), chained ("不是A，不是B，而是C"), symmetric ("适合X，不适合Y"), or with or without an explicit "but / 而 / but rather" conjunction. Just state the positive claim directly. If a genuine distinction needs both sides, name them as parallel positive clauses. Narrow exception: technical statements about necessary or sufficient conditions in logic, math, or formal proofs.

`hardikpandya_stop-slop/references/structures.md:21-21`
> 21: **Instead:** State Y directly. "The problem is Y." "Y matters here." Drop the negation entirely.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:54-54`
> 54: **Binary contrasts.** "This is not X. It's Y." / "The question isn't X, it's Y." / "It's not just X but Y." State Y directly. "The question isn't the model. It's the eval." becomes "The eval matters more than the model."

`blader_humanizer/SKILL.md:62-62`
> 62: **Problem:** The negative half names something no one claimed, so the positive half sounds larger. It adds weight without adding a claim. State the point directly. Keep a contrast only when the negative half corrects a belief the reader actually holds, or when both halves carry information.

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:409-413`
> 409: The antithesis of negative and positive is strong:
> 410: 
> 411: Not charity, but simple justice.
> 412: 
> 413: Not that I loved Caesar less, but Rome the more.

Humanizer retains belief-correcting and informational contrasts. Strunk endorses this construction. Talk-normal requires parallel positive clauses except for formal necessary/sufficient statements.

### 27. One literal action versus compulsory metaphor/image/story — tension, hard only if the image is figurative padding.
`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:138-138`
> 138: 5. Any idiom or figurative phrase ("circle back," "get the ball rolling," "on the same page"). Replace with the literal action.

`Kyaa-A_eli5/skills/eli5/SKILL.md:14-14`
> 14: 3. **Use analogies.** Map abstract concepts to concrete, everyday things.

`smixs_awesome-claude-output-styles/output-styles/eli15.md:14-17`
> 14: - Exactly one analogy per answer, drawn from one everyday domain (school,
> 15:   games, sports, cooking, music). Never mix domains mid-answer.
> 16: - After the analogy, say where it breaks: "The comparison stops working
> 17:   here, because…". A misleading intuition is worse than no analogy.

`smixs_awesome-claude-output-styles/output-styles/coach.md:19-21`
> 19: - Vivid beats abstract: one sharp image ("this function is doing three jobs
> 20:   on one salary") outworks a paragraph of analysis. One image per answer, not
> 21:   a highlight reel.

`smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:16-17`
> 16: - The protagonist is the technical thing itself: "Once there was a small
> 17:   cache who remembered answers so the database could sleep."

There is **no explicit caveman analogy ban**. A useful analogy can satisfy its no-fluff requirement. ADHD’s literal-action instruction and mandatory imagery create the stronger direct conflict.

### 28. Inanimate human agency forbidden versus concept personification — hard for Bedtime Story.
`hardikpandya_stop-slop/SKILL.md:19-19`
> 19: 3. **Use active voice.** Every sentence needs a human subject doing something. No passive constructions. No inanimate objects performing human actions ("the complaint becomes a fix").

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:32-32`
> 32: - **Use active voice.** "The team shipped it Tuesday" beats "the decision emerged." Never let inanimate things do human verbs.

`smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:16-17`
> 16: - The protagonist is the technical thing itself: "Once there was a small
> 17:   cache who remembered answers so the database could sleep."

A real technical mechanism underneath does not remove the story’s literal human-like cache actor.

### 29. Explain known context again versus context-aware decision reply — conditional in a continuing thread.
`smixs_awesome-claude-output-styles/output-styles/wait-what.md:13-16`
> 13: 1. **Never assume the reader kept up.** Open every substantive answer with
> 14:    one line of grounding — what we are doing and where we are — as if the
> 15:    reader just came back to their desk: "We are fixing the login timeout;
> 16:    the cause is found."

`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:75-75`
> 75: The reader cannot hold "we are on step 3 of 5" between messages. Restate it.

`blader_humanizer/SKILL.md:368-373`
> 368: A model writes for a reader who shares no context, because that fits the widest range of cases. A reply in a thread has a reader who already knows the background. Act on this pattern when you can see the surrounding conversation, or when the text plainly is a reply. If you cannot tell, ask or leave the text alone.
> 369: 
> 370: ### 26. Re-explaining what the reader knows
> 371: 
> 372: **Watch for:** a short reply that restates the problem, walks through the diagnosis, and lays out the evidence before it reaches the decision; a query, command, or set of numbers included to prove a plan will work; background the other person wrote or already agreed to; the answer itself sitting in the last line.
> 373: **Problem:** In a reply the reader already has the context, so rebuilding it adds nothing and buries the point. Each sentence can read fine on its own, so this survives sentence-level cleanup. Lead with the decision and keep only the reasoning that would change whether the reader agrees: usually one fact they lack and any link they need to act. The diagnosis and the proof that a plan will work belong in the ticket or document that follows; a reviewer raising a topic is not a request for the full write-up.

Humanizer says the thread reader already knows background. Wait What assumes the reader lost it. A short state update adds new information only when something changed.

### 30. Sentence emphasis at end versus response answer first — usually compatible, not a hard contradiction.
`obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:55-55`
> 55: 18. **Place emphatic words at end of sentence**

`rahulj51_eli5/skills/eli5/SKILL.md:20-20`
> 20: - Lead with the point. The first sentence gives the bottom line.

Strunk’s unit is the sentence; BLUF’s unit is the response. A first answer sentence can place its strongest word at its end. Do not report this as a universal conflict.

### 31. Strong parallel form versus deliberately irregular form — conditional for coordinate items.
`obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:524-528`
> 524: ### Rule 15. Express co-ordinate ideas in similar form.
> 525: 
> 526: This principle, that of parallel construction, requires that expressions of similar content and function should be outwardly similar. The likeness of form enables the reader to recognize more readily the likeness of content and function. Familiar instances from the Bible are the Ten Commandments, the Beatitudes, and the petitions of the Lord's Prayer.
> 527: 
> 528: The unskillful writer often violates this principle, from a mistaken belief that he should constantly vary the form of his expressions. It is true that in repeating a statement in order to emphasize it he may have need to vary its form. For illustration, see the paragraph from Stevenson quoted under Rule _9_. But apart from this, he should follow the principle of parallel construction.

`smixs_awesome-claude-output-styles/output-styles/unslop.md:49-51`
> 49:    Perfect parallel structure looks machine-made, so use the natural number of
> 50:    items rather than three, and repeat the right word instead of cycling
> 51:    synonyms for it.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:78-78`
> 78: **Robotic rhythm.** Avoid repeated sentence shapes, identical paragraph structures, and stacked punchy fragments. Vary the shape only when it helps the point.

No AI Slop rejects robotic repetition, not all semantic parallelism. Unslop’s blanket “perfect parallel structure looks machine-made” directly pulls against Strunk’s rule for matching content/function.

### 32. Draft + explanation versus final-only artifact — hard when both skills govern the same output.
`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:12-12`
> 12: **Edit (default).** The user shares a draft to fix. Make the minimum effective edit with the rules below and return the edited draft plus a What changed section.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:97-97`
> 97: 6. Output the full edited draft and a short **What changed** section.

`blader_humanizer/SKILL.md:49-49`
> 49: **Pasted text (default).** Return the draft, a short list of remaining patterns, and the final rewrite.

`blader_humanizer/SKILL.md:53-53`
> 53: **Embedded mode.** When another task uses this skill for a pull request, commit message, or document, return only the final text.

`smixs_awesome-claude-output-styles/output-styles/adhd.md:31-33`
> 31: 10. **A requested artefact ships bare.** Asked for the commit message, the
> 32:     Slack message, the email? Output only it — no action line above it, no
> 33:     state line below it, no offer to revise.

Humanizer distinguishes pasted/file/embedded modes. No AI Slop requires What changed; Smixs bare-artifact rules omit it. Select an explicit output contract instead of mixing defaults.

### 33. Exact identifiers/no invented abbreviations versus Thing Explainer renamed concepts — tension, not a code-string conflict.
`JuliusBrussee_caveman/skills/caveman/SKILL.md:43-43`
> 43: "fix" not "implement a solution for". Standard acronyms fine (DB, API, HTTP). Invented abbreviations not (cfg, impl, fn): same tokens, harder read. No arrows.

`smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:16-25`
> 16: - Name things by what they do: a server is "the computer far away that
> 17:   answers", a cache is "a place where the computer keeps answers it already
> 18:   found, so it does not have to find them again".
> 19: - Real names stay real. `useMemo` is `useMemo`, PostgreSQL is PostgreSQL —
> 20:   written exactly, then explained in common words: "PostgreSQL (a computer
> 21:   thing that remembers facts in tables)".
> 22: - Short sentences. The reader should never have to read one twice.
> 23: - Accept the puzzle feel. If a spot gets too silly to be clear, say the real
> 24:   word once, mark it like this: *(hard word: idempotent — doing it twice
> 25:   changes nothing)*, and move on.

`smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:42-43`
> 42: Code, commands, error messages, file paths, identifiers, and numbers stay
> 43: byte-for-byte exact — the game never touches them. Drop the game entirely and

Thing Explainer preserves real names and code. Generic concept renaming expands explanations and can oppose technical-term precision, but it explicitly keeps `useMemo` and PostgreSQL. Do not claim it rewrites identifiers.

### 34. Preserve source quotations versus dash/tell rewriting — resolved by scoped exemptions in Humanizer/Unslop, unresolved literal Stop Slop rule.
`hardikpandya_stop-slop/SKILL.md:43-43`
> 43: - Em-dash anywhere? Remove it.

`blader_humanizer/SKILL.md:385-385`
> 385: Each pattern describes a default choice, and a person can make any one of them on purpose. Leave a watched phrase alone inside a quotation, a title, a proper name, or a passage that discusses the phrase rather than uses it. Salutations and sign-offs on a letter or comment predate chatbots. Text written before November 30, 2022 is not AI-written. People who judge by feel do little better than chance, and human writing keeps absorbing AI habits, so several tells together are the safeguard.

`smixs_awesome-claude-output-styles/output-styles/unslop.md:78-82`
> 78: Code, commands, error messages, file paths, identifiers, and numbers stay
> 79: byte-for-byte exact. The punctuation, quote and heading rules never rewrite
> 80: content: a curly apostrophe or an em dash inside a string literal or quoted
> 81: file content stays as it is, and quoting the user or a third party reproduces
> 82: their text as written. Security warnings, confirmations of destructive or

Stop Slop says em-dash anywhere; its skill provides no explicit quotation/code exemption. Humanizer and Unslop explicitly retain source text. This matters to evidence reports like this one.

### 35. Session-persistent mode versus one-task ELI5 — hard if both lifetime directives apply to one mode toggle.
`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:17-19`
> 17: These rules apply to every response for the rest of the session, not only this one. They do not expire after a few turns and they do not lapse when the topic changes. If you are unsure whether they still apply, they do.
> 18: 
> 19: Turn them off only when the reader says "stop adhd mode" or "normal mode". Confirm in one line, then return to your default style.

`JuliusBrussee_caveman/skills/caveman/SKILL.md:17-17`
> 17: Every response, whole session, until user says "stop caveman" or "normal mode". Unsure if still on? It is. Confirm the switch-off in one line.

`Kyaa-A_eli5/skills/eli5/SKILL.md:52-52`
> 52: This mode applies only to the current explanation or task. Return to normal output style afterward unless the user says to keep it active.

`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:6-8`
> 6: Format every response for a reader with limited working memory who needs
> 7: low-friction starts and visible progress, while still teaching. Apply to all
> 8: interactions in the current task.

These are different styles, so a deliberate composition can maintain a base style while ELI5 exits. They do not define the same lifetime; “normal mode” is shared by caveman and ADHD, creating ambiguous multi-mode exit intent.

### 36. User’s reply language versus Wenyan/English-only language prescription — hard without explicit separate selection.
`JuliusBrussee_caveman/skills/caveman/SKILL.md:66-66`
> 66: Compress the style, not the language. An explicit reply-language instruction wins. Never switch because of quoted text. Technical terms and errors stay verbatim. Particles and case markers are grammar, not filler.

`JuliusBrussee_caveman/skills/megacave/SKILL.md:28-28`
> 28: 文言, not 白話. Verb before object. Subjects omitted where recoverable.

`rahulj51_eli5/skills/eli5/SKILL.md:18-18`
> 18: - Use plain, simple English. Prefer short, common words.

`rahulj51_eli5/skills/ste/SKILL.md:8-8`
> 8: Write the answer only in ASD-STE100 Simplified Technical English (STE). Do not use a different plain-language standard or add separate style rules.

Megacave is an explicit independent skill rather than simultaneous caveman mode, so normal switching resolves that pair. Combining it with English-only ELI5/STE does not.

### 37. Requested options versus single recommendation contract — conditional when the answer itself is alternatives.
`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:127-127`
> 127: 5. A rule fights the task. When a rule would delete the answer itself, the task wins; the shape stays. Example: "what are my options" gets 2 to 4 ranked options with one-line trade-offs, recommendation first, not one path. The options are the answer.

`smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:56-57`
> 56: Run the portability test on every sentence. Is there exactly one clear
> 57: recommendation? Does the answer end on content, not a recap?

`hexiecs_talk-normal/prompt.md:27-27`
> 27: - Comparisons: give your recommendation with brief reasoning, not a balanced essay

Giving several options plus one recommendation often satisfies all sides. A template that suppresses requested alternatives fails ayghri’s explicit task-wins exception; do not conflate recommendation with an absolute options ban.

### 38. Banned terms versus exact technical vocabulary — conditional.
`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:46-46`
> 46: Banned outright: delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, this is huge, this changes everything, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving.

`blader_humanizer/SKILL.md:201-201`
> 201: **Watch for:** Actually, additionally, align with, bolstered, crucial, deep dive, delve, enduring, enhance, garner, gate/gated/gating (figurative; keep technical uses), highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), meticulous/meticulously, pivotal, quietly, robust (figurative; keep technical uses), showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

`JuliusBrussee_caveman/skills/caveman/SKILL.md:58-58`
> 58: Code blocks unchanged. Commands, paths, API names exact. Errors quoted exact, shortest decisive line only.

`rahulj51_eli5/skills/ste/SKILL.md:68-68`
> 68: Do not change code, commands, file paths, URLs, identifiers, data, or text that the user requires verbatim. Use necessary product and subject terms only when they qualify as STE technical nouns or technical verbs. Clearly separate protected text from the STE text.

No AI Slop bans `robust` and `harness` outright; Humanizer explicitly exempts technical `robust` and gate/gated/gating. If those words are exact identifiers/quoted technical terms, verbatim rules protect them; generic word bans need an exemption.

### 39. Commit/review specialized artifacts versus whole-sentence/no-emoji defaults — conditional, not base-chat leakage.
`JuliusBrussee_caveman/skills/caveman-commit/SKILL.md:13-18`
> 13: - `<type>(<scope>): <imperative summary>` — `<scope>` optional
> 14: - Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `chore`, `build`, `ci`, `style`, `revert`
> 15: - Imperative mood: "add", "fix", "remove" — not "added", "adds", "adding"
> 16: - ≤50 chars when possible, hard cap 72
> 17: - No trailing period
> 18: - Match project convention for capitalization after the colon

`JuliusBrussee_caveman/skills/caveman-review/SKILL.md:12-18`
> 12: **Format:** `L<line>: <problem>. <fix>.` — or `<file>:L<line>: ...` when reviewing multi-file diffs.
> 13: 
> 14: **Severity prefix (optional, when mixed):**
> 15: - `🔴 bug:` — broken behavior, will cause incident
> 16: - `🟡 risk:` — works but fragile (race, missing null check, swallowed error)
> 17: - `🔵 nit:` — style, naming, micro-optim. Author can ignore
> 18: - `❓ q:` — genuine question, not a suggestion

`rahulj51_eli5/skills/eli5/SKILL.md:23-23`
> 23: - Write complete sentences. Do not compress into fragments, abbreviations, or arrow chains.

`rahulj51_eli5/skills/eli5/SKILL.md:26-26`
> 26: - No emojis.

`blader_humanizer/SKILL.md:294-294`
> 294: **Problem:** Headings capitalize every main word, and headings or list items carry emojis or arrows (→) as decoration. A horizontal rule sits between every section, or the document opens with a top-level heading that repeats its own title. A heading written for effect ("The decision, on one screen") should name what the section holds ("How the six options compare"). Use sentence case, remove the decoration and the rules, and let the title stand once.

Conventional Commit subjects are intentional artifact fragments; compressed review has optional severity emoji. Those independent skills apply to persisted text even though base caveman does not. Humanizer permits purposeful writer conventions, so its formatting rule is not an absolute conflict here.

### 40. Recap/transition development versus no restatement — hard when deliberately used to develop exposition.
`obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:301-301`
> 301: \(c\) the final sentence either emphasizes the thought of the topic sentence or states some important consequence.

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:305-307`
> 305: If the paragraph forms part of a larger composition, its relation to what precedes, or its function as a part of the whole, may need to be expressed. This can sometimes be done by a mere word or phrase (*again*; *therefore*; *for the same reason*) in the topic sentence. Sometimes, however, it is expedient to precede the topic sentence by one or more sentences of introduction or transition. If more than one such sentence is required, it is generally better to set apart the transitional sentences as a separate paragraph.
> 306: 
> 307: According to the writer's purpose, he may, as indicated above, relate the body of the paragraph to the topic sentence in one or more of several different ways. He may make the meaning of the topic sentence clearer by restating it in other forms, by defining its terms, by denying the contrary, by giving illustrations or specific instances; he may establish it by proofs; or he may develop it by showing its implications and consequences. In a long paragraph, he may carry out several of these processes.

`hexiecs_talk-normal/prompt.md:33-33`
> 33: - Do not restate the same point in "plain language" or "in human terms" after already explaining it. Say it once clearly. No "翻成人话", "in other words", "简单来说" rewording blocks.

`blader_humanizer/SKILL.md:30-30`
> 30: Two rules follow from this. Every sentence you keep must add something the reader did not already have, from earlier in the text or from the conversation around it. A tell counts in proportion to how rarely a careful writer would make it on purpose. The patterns are numbered strongest first: §1 to §5 justify an edit on one sighting, and a pattern marked *weak alone* needs company from other tells in the same passage before you act.

`JuliusBrussee_caveman/skills/ultracave/SKILL.md:40-40`
> 40: No restating, no summary after a list.

Strunk supports explanatory restatement and transitions. A redundant recap can still be cut by all sources; this conflict concerns a purposeful second formulation mandated/protected by the chosen expository method.

### 41. Self-answered rhetorical questions / Wh- opening versus teaching question conventions — conditional.
`hardikpandya_stop-slop/references/structures.md:112-112`
> 112: | Sentences starting with What, When, Where, Which, Who, Why, How | Restructure. Lead with the subject or the verb. |

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:80-80`
> 80: **Rhetorical setups.** "What if I told you...", "Think about it:", "Plot twist:", and self-answered "Question? Answer." pairs. Drop them and make the point.

`smixs_awesome-claude-output-styles/output-styles/feynman.md:20-22`
> 20: 3. **Check understanding with 1–2 pointed questions** aimed at the weakest
> 21:    link: "Quick check — why would this still break if we doubled the
> 22:    timeout?" Do not answer your own question. Wait.

`smixs_awesome-claude-output-styles/output-styles/yoda.md:25-26`
> 25: - **One question back to the learner** when it serves the lesson: "Run the
> 26:   failing test alone, did you? Hmm?"

Feynman’s questions are not self-answered, so No AI Slop’s Question? Answer. ban does not prohibit them. Stop Slop’s Wh- sentence-start rule does conflict with the prescribed “why” check question.

### 42. Parentheses as acceptable dash replacement versus no parenthetical connector — conditional.
`blader_humanizer/SKILL.md:162-162`
> 162: **Rule:** The final rewrite must not contain em dashes (—) or en dashes (–) unless the writer's sample uses them; then match the sample's rate. Replace each dash with a period, comma, colon, or parentheses, or rewrite the sentence. This includes spaced dashes and double hyphens (` -- `) used as dashes. Leave dashes and hyphens inside code blocks, inline code, commands, paths, and URLs alone.

`smixs_awesome-claude-output-styles/output-styles/unslop.md:13-17`
> 13: 1. **Plain punctuation.** Period and comma carry the sentence. The em dash is
> 14:    the loudest tell, and reaching for parentheses instead trades one tell for
> 15:    another. If a thought needs separation, end the sentence. A colon
> 16:    introduces a list or an example, never a mid-sentence connector. Straight
> 17:    quotes and apostrophes.

Humanizer explicitly permits parentheses as replacements; Unslop says they trade one tell for another. Both allow sentence rewrite, so one can satisfy both by rewriting; the permissions differ.

### 43. Hook setup offer versus no unrequested setup/follow-up — internal caveman contradiction on first session.
`JuliusBrussee_caveman/src/hooks/caveman-activate.js:550-555`
> 550:         : "STATUSLINE SETUP NEEDED: The caveman plugin includes a statusline badge showing active mode " +
> 551:           "(e.g. [CAVEMAN], [ULTRACAVE]). It is not configured yet. " +
> 552:           "To enable, add this to ") +
> 553:       path.join(claudeDir, 'settings.json') + ": " +
> 554:       statusLineSnippet + " " +
> 555:       "Proactively offer to set this up for the user on first interaction.";

`JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js:116-118`
> 116:     ' Answer only what was asked: no unrequested background, lists, examples,' +
> 117:     ' walkthroughs, or follow-up offers; give code, steps, or warnings when the' +
> 118:     ' task needs them. Security warnings, irreversible actions, multi-step order:' +

`hexiecs_talk-normal/prompt.md:32-32`
> 32: - Do not end with hypothetical follow-up offers or conditional next-step menus. This includes "If you want, I can also...", "如果你愿意，我还可以...", "If you tell me...", "如果你告诉我...", "如果你说X，我就Y", "我下一步可以...", "If you'd like, my next step could be...". Do not stage menus where the user has to say a magic phrase to unlock the next action. Answer what was asked, give the recommendation, stop. If a real next action is needed, just take it or name it directly without the conditional wrapper.

Activation can demand an unsolicited statusline offer even though its ordinary per-turn reinforcement forbids follow-up offers. This audit does not execute the hook.

### 44. Source examples contradict their own bans — internal inconsistency, exact examples.
`hardikpandya_stop-slop/SKILL.md:43-43`
> 43: - Em-dash anywhere? Remove it.

`hardikpandya_stop-slop/references/examples.md:45-45`
> 45: > "Speed, quality, cost—pick two."

`hardikpandya_stop-slop/references/structures.md:21-21`
> 21: **Instead:** State Y directly. "The problem is Y." "Y matters here." Drop the negation entirely.

`hardikpandya_stop-slop/references/examples.md:57-57`
> 57: > "The best teams optimize for learning, not productivity."

`blader_humanizer/SKILL.md:319-320`
> 319: **Watch for:** I hope this helps, Of course!, Certainly!, Great question!, You're absolutely right, Would you like..., Want me to...?, Should I continue?, let me know, here is a...
> 320: **Problem:** A chatbot's greeting, praise, offer, or closing remains in text that should stand on its own. It is the most certain tell in this list and the easiest to miss when it wraps real content. Remove the wrapper and keep the content.

`blader_humanizer/SKILL.md:381-381`
> 381: > I'd rather keep this PR account specific and open a separate ticket for the `MergeService` fix and the backfill. Let me know if that works.

Stop Slop’s revised example still contains an em dash, and another uses correct-then-reject contrast. Humanizer’s after-rewrite says “Let me know if that works” despite its residue watcher; a real coordination question can be intentional, but the example exposes a classification ambiguity. Do not convert examples into stronger rules than explicit exceptions.

## 4. Risks
### Description/name collisions
Descriptions are selection metadata, not proof of actual host behavior. The following are static overlaps. Model-invocation-disabled skills and selectable output styles are explicitly separated from ordinary automatic selection. No live model routing trials were run: denominator **0**; activation probabilities are unknown.
#### “Rewrite this draft to sound less AI-written.”
`blader_humanizer/SKILL.md:3-7`
> 3: description: |
> 4:   Rewrite AI-sounding text so it reads like the writer without changing what it says.
> 5:   Use when editing or reviewing prose for AI tells: not-X-but-Y contrasts, one-line
> 6:   closers, staged openers, forced triads, dashes everywhere, inflated claims, sales
> 7:   language, stock AI words, bold labels, or filler. Based on Wikipedia's "Signs of AI writing."

`hardikpandya_stop-slop/SKILL.md:3-3`
> 3: description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells.

`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:3-3`
> 3: description: Edit drafts into sharper, more human writing while preserving the writer's personal voice, or detect AI-slop patterns without rewriting. Use when the user wants a draft clearer, more direct, more opinionated, or less AI-sounding, or asks whether writing reads as AI.

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:3-3`
> 3: description: Apply Strunk's timeless writing rules to ANY prose humans will read—documentation, commit messages, error messages, explanations, reports, or UI text. Makes your writing clearer, stronger, and more professional.

Four model-invocable prose-editing descriptions can match. Conflicting dash, voice, rhythm, and output-return rules matter.

#### “ELI5 this error / make it simpler in plain English.”
`Kyaa-A_eli5/skills/eli5/SKILL.md:3-3`
> 3: description: This skill should be used when the user says "/eli5", "eli5", "explain like I'm 5", "simplify", "too complex", "make it simpler", "ELI5", or asks for a plain-language explanation of code, errors, or concepts. Forces maximally simple, jargon-free output. When triggered without a specific topic, re-explain the previous response in simplified form.

`rahulj51_eli5/skills/eli5/SKILL.md:3-3`
> 3: description: Rewrite or summarize content in plain, concise English for a busy executive (think CTO/CPO). Use whenever the user says "eli5" anywhere in a request, or asks for a simple, plain-English, or executive version of an agent response, spec, doc, plan, bug report, or code review comment.

Two skills share **name: eli5**, plugin name **eli5**, marketplace name **eli5**, and broad plain-language triggers. Plugin-qualified commands may disambiguate; actual selection was not tested. Kyaa maximizes simplicity, Rahul maximizes executive decision clarity.

#### “Use fewer tokens / be brief.”
`JuliusBrussee_caveman/skills/caveman/SKILL.md:3-6`
> 3: description: >
> 4:   Terse caveman voice: answer first, fluff gone, every technical fact kept.
> 5:   Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less
> 6:   tokens". Stays on until "stop caveman" or "normal mode".

`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:3-3`
> 3: description: This skill should be used when the user asks for "ADHD output", "fewer output tokens", "short numbered steps", "limited working memory formatting", or explicitly invokes "adhd-output-style".

Both can auto-select; they imply different grammar/progress/teaching rules. Ayghri describes a nearby need but has disable-model-invocation: true, so it is not a third ordinary automatic trigger.

#### “Review this PR / improve its prose.”
`JuliusBrussee_caveman/skills/caveman-review/SKILL.md:3-5`
> 3: description: >
> 4:   Compressed code review - one line per finding with location, problem and fix.
> 5:   Use for /caveman-review, "review this PR", or "review the diff".

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:3-3`
> 3: description: Apply Strunk's timeless writing rules to ANY prose humans will read—documentation, commit messages, error messages, explanations, reports, or UI text. Makes your writing clearer, stronger, and more professional.

`blader_humanizer/SKILL.md:3-7`
> 3: description: |
> 4:   Rewrite AI-sounding text so it reads like the writer without changing what it says.
> 5:   Use when editing or reviewing prose for AI tells: not-X-but-Y contrasts, one-line
> 6:   closers, staged openers, forced triads, dashes everywhere, inflated claims, sales
> 7:   language, stock AI words, bold labels, or filler. Based on Wikipedia's "Signs of AI writing."

`hardikpandya_stop-slop/SKILL.md:3-3`
> 3: description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells.

Caveman’s PR review trigger covers code; Elements covers PR prose; Humanizer/Stop Slop cover editorial cleanup. Overlap depends on whether the user requests code review, writing review, or both.

#### “Write a commit message.”
`JuliusBrussee_caveman/skills/caveman-commit/SKILL.md:3-5`
> 3: description: >
> 4:   Write a Conventional Commits message compressed to intent only. Use for
> 5:   "write a commit", "commit message", /commit or /caveman-commit.

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:3-3`
> 3: description: Apply Strunk's timeless writing rules to ANY prose humans will read—documentation, commit messages, error messages, explanations, reports, or UI text. Makes your writing clearer, stronger, and more professional.

`hardikpandya_stop-slop/SKILL.md:3-3`
> 3: description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells.

Artifact-scope overlaps; ordinary caveman reply mode explicitly steps out of chat voice.

#### “Talk like caveman / I want Claude to talk like ….”
`JuliusBrussee_caveman/skills/caveman/SKILL.md:3-6`
> 3: description: >
> 4:   Terse caveman voice: answer first, fluff gone, every technical fact kept.
> 5:   Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less
> 6:   tokens". Stays on until "stop caveman" or "normal mode".

`smixs_awesome-claude-output-styles/skills/style-maker/SKILL.md:3-9`
> 3: description: >
> 4:   Interviews the user with ~10 questions about how they want Claude to talk,
> 5:   optionally collects writing samples they like and hate, then generates a
> 6:   personal Claude Code output style file and activates it. Use when the user
> 7:   says "make my output style", "build me a custom style", "I want Claude to
> 8:   talk like...", "create a personal writing style", or complains about
> 9:   Claude's tone and wants a tailored fix rather than a preset.

Caveman activation and a style-creation interview can compete. Smixs preset descriptions themselves do not auto-select as skills.

#### “Install talk-normal.”
`hexiecs_talk-normal/skill/SKILL.md:4-4`
> 4: description: Stop LLM slop. A curated system prompt that cuts verbose, corporate-sounding LLM output by 56-71% (measured) while preserving information. Works bilingually (English + Chinese). Installs into your AGENTS.md as an always-on behavior modifier.

`hexiecs_talk-normal/skill-hermes/SKILL.md:3-3`
> 3: description: Stop LLM slop. A curated system prompt that cuts verbose, corporate-sounding LLM output by 56-73% (measured) while preserving information. Works bilingually (English + Chinese). Installs into your AGENTS.md as an always-on behavior modifier.

Same skill name and nearly identical description if both bundles are exposed; install target differs in documentation although all installer copies use the same detection logic.

Seven explicit collision clusters above inspect **19 description placements** (some sources recur). They are examples of concrete overlapping triggers, not an exhaustive pairwise routing benchmark. Full inventory of **41 physical SKILL.md files** includes mirrors and unrelated Caveman workflows; the 20 Smixs preset descriptions and fcakyon output-style description are output-style metadata, not skills. Kyaa/Rahul both call their marketplace/plugin `eli5`; Smixs `No AI Slop` is an adaptation, not Peter Yang’s skill. Installing both talk-normal bundles is redundant; their prompt and installer copies are byte-identical.
Caveman’s root plugin ships generic coding skills alongside style skills. Their descriptions can activate on failures, feature builds, refactors, migration, and verification, even if the user installed it only for communication. This is explicitly acknowledged in `JuliusBrussee_caveman/CLAUDE.md:136-147`, not inferred from the brand. Its root 22 skills and Codex distribution six-skill subset expose different candidate sets.
### Always-on stacking and persistence
- **Default plugin caveman + opted-in ADHD:** both SessionStart paths can inject complete rules. Caveman repeats the current rules after SessionStart events; ayghri’s matcher includes compact/resume/clear and checks only its opt-in flag. Ayghri’s hook has no stored per-session off check, so a new matched event can reassert “ADHD MODE ACTIVE” after a model-only stop. Caveman stores durable off. Evidence: `ayghri_i-have-adhd/hooks/always-on.mjs:16-40`; `JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js:319-325`.
- **Caveman + Smixs --enforce:** both UserPromptSubmit reminders can fire; Smixs reinforces whichever custom style its global settings names while caveman reinforces its session mode. A plugin plus standalone Caveman hook can also produce duplicate registrations; installer checks global settings, not a guarantee against plugin registration stacking. Evidence: `JuliusBrussee_caveman/src/hooks/caveman-config.js:583-585`; `JuliusBrussee_caveman/src/hooks/install.sh:183-211`; `smixs_awesome-claude-output-styles/hooks/style-reminder.sh:14-32`.
- **Talk-normal:** persisted context block can stack with both injected sets without any SessionStart hook. Its BEGIN/END markers solve replacement of its own block only. It does not arbitrate ADHD progress recaps, ELI5 sentence caps, or caveman grammar. Evidence: `hexiecs_talk-normal/install.sh:93-108`.
- **Fcakyon:** `force-for-plugin: true` declares forced style behavior and can combine with the model-invocable skill and other injected rules. No hook body or host enforcement implementation is in the scoped plugin; runtime support and duplicate loading were not verified. Do not call it a SessionStart hook. Evidence: `fcakyon_claude-codex-settings/plugins/adhd-output-style/output-styles/adhd-explanatory.md:1-10`.
- **Kyaa ELI5:** startup update check can add a system message, not the explanation rules. It can stack notifications but is not another always-on ELI5 ruleset. Evidence: `Kyaa-A_eli5/scripts/check-update.mjs:128-129`.
- **Host-specific:** ayghri OpenCode adds the whole body every system-transform call while the flag exists; Pi/OMP checks whether rules are already in live context. Elements OpenCode/Pi only register resources. These costs and persistence differ from Claude’s SessionStart path. Evidence: `ayghri_i-have-adhd/.opencode/plugins/i-have-adhd.mjs:74-97`, `ayghri_i-have-adhd/extensions/i-have-adhd.ts:130-151`, `obra_the-elements-of-style/.pi/extensions/elements-of-style.ts:12-15`.
### Cost of always-on input
Exact billable token counts were **not measured**. No tokenizer is installed (`tiktoken` module availability checked once: absent), and Claude’s tokenizer/model/cache billing was not queried. The table reports exact source-body characters and whitespace words after leading frontmatter removal, retaining source trailing newlines. Some hooks trim and re-add newlines; banners and separators are excluded. `ceil(characters / 4)` is an illustrative English-heavy planning proxy, **not measured Claude tokens**, not reliable for Wenyan, and not a savings estimate. Context may remain in later requests and be cache-read; event injection volume alone is not total billed input.
| Body loaded | Words | Unicode characters | Character/4 proxy | Event / condition |
|---|---:|---:|---:|---|
| Caveman | 591 | 3795 | 949 | SessionStart; active default; body again on mode switch |
| Ultracave | 302 | 2022 | 506 | SessionStart/mode switch; selected mode |
| Megacave | 285 | 1958 | 490 | SessionStart/mode switch; selected mode; proxy unreliable |
| Ayghri ADHD | 1187 | 6786 | 1697 | SessionStart matcher; opt-in flag; full body each OpenCode turn |
| Talk-normal | 545 | 3527 | 882 | Persisted workspace instruction block |
| Talk-normal ChatGPT | 217 | 1400 | 350 | If pasted into custom instructions |
| Fcakyon ADHD output style | 245 | 1605 | 402 | If forced/selected style is loaded |
| Fcakyon ADHD skill | 249 | 1625 | 407 | On task activation; separate entry point |
Across **20 Smixs styles**, body size is 307–806 words and 2001–4914 characters. Only the selected style should contribute its body; do not multiply one session’s cost by 20. Selection metadata/discovery overhead is a separate host-dependent cost.
Illustrative stacked **four bodies** (Caveman + opted-in ayghri ADHD + persisted talk-normal + fcakyon output style): 2568 whitespace words, 15713 characters, 3929 character/4 proxy units, **excluding** banners, switch lines, settings nudges, separators, metadata, and retained previous injections. This is one static composition, not evidence that those four plugins are active here.
Caveman per-turn reinforcement uses skill thesis + scope/risk/payload sentences (`src/hooks/caveman-mode-tracker.js:114-119`); full mode body appears on actual switches (`:385-388`). Smixs emits one name-dependent line (`hooks/style-reminder.sh:32`). Ayghri adds banner + opt-out path before its body (`hooks/always-on.mjs:36-40`). Caveman statusline nudge comment estimates “~90 tokens” (`src/hooks/caveman-activate.js:395-397`); this is source-authored, unverified, and emitted conditionally. Full Humanizer is **5,219 words** on use; Elements reference is **12,154 words** on load. Neither has an always-on full-rule hook, but broad triggers can make that on-demand cost frequent.
## Appendix A. Physical instruction/packaging inventory and descriptions
Each row supplies full-file/body word counts and exact frontmatter where present. Hook/source/JSON files generally have no frontmatter. Description blocks below preserve physical YAML lines (not guessed normalized text). Files with no description say so. This inventory scopes Caveman to communication, discovery/packaging, hook implementations/support, command templates, and all root/distribution skills; unrelated engine/runtime/SDK application code is excluded. Fcakyon behavior inventory is restricted to its six scoped files, plus root LICENSE and the marketplace metadata registration.
**168 physical files selected**, including 41 SKILL.md files and 21 output-style files. License contents/counts are separate in Appendix B. Per-source total below is over selected physical files, so mirrors/support code can inflate it; it is not always-on token overhead.
### JuliusBrussee_caveman — 72 selected files, 45394 full-file words
- `JuliusBrussee_caveman/.claude-plugin/marketplace.json`: **50 words**, body **50 words**, 532 characters, 17 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/.claude-plugin/plugin.json`: **86 words**, body **86 words**, 1051 characters, 35 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/.codex/codex-sessionstart.js`: **1184 words**, body **1184 words**, 8952 characters, 203 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/.codex/hooks.json`: **30 words**, body **30 words**, 361 characters, 17 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/agents/cavecrew-builder.md`: **212 words**, body **163 words**, 1456 characters, 46 lines.
`JuliusBrussee_caveman/agents/cavecrew-builder.md:3-8`
> 3: description: >
> 4:   Surgical 1-2 file edit. Typo fixes, single-function rewrites, mechanical
> 5:   renames, comment removal, format-preserving tweaks. Hard refuses 3+ file
> 6:   scope. Returns caveman diff receipt. Use when scope is bounded and
> 7:   obvious; do NOT use for new features, new files (unless asked), or
> 8:   cross-file refactors.

  `JuliusBrussee_caveman/agents/cavecrew-builder.md:2` `name: cavecrew-builder`
- `JuliusBrussee_caveman/agents/cavecrew-investigator.md`: **237 words**, body **189 words**, 1617 characters, 56 lines.
`JuliusBrussee_caveman/agents/cavecrew-investigator.md:3-7`
> 3: description: >
> 4:   Read-only code locator. Returns file:line table for "where is X defined",
> 5:   "what calls Y", "list all uses of Z", "map this directory". Output is
> 6:   caveman-compressed so the main thread eats ~60% fewer tokens than
> 7:   vanilla Explore. Refuses to suggest fixes.

  `JuliusBrussee_caveman/agents/cavecrew-investigator.md:2` `name: cavecrew-investigator`
- `JuliusBrussee_caveman/agents/cavecrew-reviewer.md`: **254 words**, body **209 words**, 1566 characters, 47 lines.
`JuliusBrussee_caveman/agents/cavecrew-reviewer.md:3-7`
> 3: description: >
> 4:   Diff/branch/file reviewer. One line per finding, severity-tagged, no praise,
> 5:   no scope creep. Output format `path:line: <emoji> <severity>: <problem>. <fix>.`
> 6:   Use for "review this PR", "review my diff", "audit this file". Skips
> 7:   formatting nits unless they change meaning.

  `JuliusBrussee_caveman/agents/cavecrew-reviewer.md:2` `name: cavecrew-reviewer`
- `JuliusBrussee_caveman/agents/profiles/opencode.json`: **161 words**, body **161 words**, 2156 characters, 70 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/commands/caveman-commit.toml`: **44 words**, body **44 words**, 305 characters, 2 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/commands/caveman-init.md`: **111 words**, body **90 words**, 837 characters, 13 lines.
`JuliusBrussee_caveman/commands/caveman-init.md:2-2`
> 2: description: Drop the always-on caveman activation rule into the current repo for every IDE agent

- `JuliusBrussee_caveman/commands/caveman-init.toml`: **81 words**, body **81 words**, 629 characters, 2 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/commands/caveman-review.toml`: **38 words**, body **38 words**, 254 characters, 2 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/commands/caveman-stats.toml`: **77 words**, body **77 words**, 524 characters, 2 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/commands/caveman.toml`: **78 words**, body **78 words**, 542 characters, 2 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/commands/megacave.toml`: **56 words**, body **56 words**, 390 characters, 2 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/commands/ultracave.toml`: **64 words**, body **64 words**, 443 characters, 2 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/gemini-extension.json`: **23 words**, body **23 words**, 226 characters, 6 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/plugins/caveman/.codex-plugin/plugin.json`: **99 words**, body **99 words**, 1334 characters, 39 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/plugins/caveman/skills/cavecrew/SKILL.md`: **544 words**, body **507 words**, 3711 characters, 77 lines.
`JuliusBrussee_caveman/plugins/caveman/skills/cavecrew/SKILL.md:3-6`
> 3: description: >
> 4:   When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder`
> 5:   (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline
> 6:   or using `Explore`. Their output is compressed, so main context lasts longer.

  `JuliusBrussee_caveman/plugins/caveman/skills/cavecrew/SKILL.md:2` `name: cavecrew`
- `JuliusBrussee_caveman/plugins/caveman/skills/caveman/SKILL.md`: **628 words**, body **591 words**, 4043 characters, 88 lines.
`JuliusBrussee_caveman/plugins/caveman/skills/caveman/SKILL.md:3-6`
> 3: description: >
> 4:   Terse caveman voice: answer first, fluff gone, every technical fact kept.
> 5:   Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less
> 6:   tokens". Stays on until "stop caveman" or "normal mode".

  `JuliusBrussee_caveman/plugins/caveman/skills/caveman/SKILL.md:2` `name: caveman`
- `JuliusBrussee_caveman/plugins/caveman/skills/caveman-compress/SKILL.md`: **703 words**, body **673 words**, 4685 characters, 109 lines.
`JuliusBrussee_caveman/plugins/caveman/skills/caveman-compress/SKILL.md:3-5`
> 3: description: >
> 4:   Compress a memory file such as CLAUDE.md or a todo list into caveman format
> 5:   to save input tokens, keeping a readable backup. Trigger: /caveman-compress.

  `JuliusBrussee_caveman/plugins/caveman/skills/caveman-compress/SKILL.md:2` `name: caveman-compress`
- `JuliusBrussee_caveman/plugins/caveman/skills/caveman-stats/SKILL.md`: **263 words**, body **232 words**, 1866 characters, 17 lines.
`JuliusBrussee_caveman/plugins/caveman/skills/caveman-stats/SKILL.md:3-6`
> 3: description: >
> 4:   Show recorded output and cache-read token usage and mode attribution for
> 5:   the current Claude Code session, or locate the host's native usage report.
> 6:   Trigger: /caveman-stats.

  `JuliusBrussee_caveman/plugins/caveman/skills/caveman-stats/SKILL.md:2` `name: caveman-stats`
- `JuliusBrussee_caveman/plugins/caveman/skills/megacave/SKILL.md`: **320 words**, body **285 words**, 2221 characters, 63 lines.
`JuliusBrussee_caveman/plugins/caveman/skills/megacave/SKILL.md:3-6`
> 3: description: >
> 4:   Caveman in Classical Chinese: 文言文 register, far fewer characters, technical
> 5:   terms verbatim. Invoke only with /megacave or /caveman wenyan. Stays on until
> 6:   "stop caveman" or "normal mode".

  `JuliusBrussee_caveman/plugins/caveman/skills/megacave/SKILL.md:2` `name: megacave`
  `JuliusBrussee_caveman/plugins/caveman/skills/megacave/SKILL.md:7` `disable-model-invocation: true`
- `JuliusBrussee_caveman/plugins/caveman/skills/ultracave/SKILL.md`: **340 words**, body **302 words**, 2287 characters, 63 lines.
`JuliusBrussee_caveman/plugins/caveman/skills/ultracave/SKILL.md:3-6`
> 3: description: >
> 4:   Caveman at maximum compression: fragments, one word when one word is enough,
> 5:   each fact once. Invoke only with /ultracave or /caveman ultra. Stays on until
> 6:   "stop caveman" or "normal mode".

  `JuliusBrussee_caveman/plugins/caveman/skills/ultracave/SKILL.md:2` `name: ultracave`
  `JuliusBrussee_caveman/plugins/caveman/skills/ultracave/SKILL.md:7` `disable-model-invocation: true`
- `JuliusBrussee_caveman/skills/cavecrew/SKILL.md`: **544 words**, body **507 words**, 3711 characters, 77 lines.
`JuliusBrussee_caveman/skills/cavecrew/SKILL.md:3-6`
> 3: description: >
> 4:   When to delegate to `cavecrew-investigator` (locate code), `cavecrew-builder`
> 5:   (1-2 file edit) or `cavecrew-reviewer` (diff review) instead of working inline
> 6:   or using `Explore`. Their output is compressed, so main context lasts longer.

  `JuliusBrussee_caveman/skills/cavecrew/SKILL.md:2` `name: cavecrew`
- `JuliusBrussee_caveman/skills/caveman/SKILL.md`: **628 words**, body **591 words**, 4043 characters, 88 lines.
`JuliusBrussee_caveman/skills/caveman/SKILL.md:3-6`
> 3: description: >
> 4:   Terse caveman voice: answer first, fluff gone, every technical fact kept.
> 5:   Use for /caveman, "caveman mode", "talk like caveman", "be brief", "less
> 6:   tokens". Stays on until "stop caveman" or "normal mode".

  `JuliusBrussee_caveman/skills/caveman/SKILL.md:2` `name: caveman`
- `JuliusBrussee_caveman/skills/caveman-commit/SKILL.md`: **358 words**, body **333 words**, 2351 characters, 63 lines.
`JuliusBrussee_caveman/skills/caveman-commit/SKILL.md:3-5`
> 3: description: >
> 4:   Write a Conventional Commits message compressed to intent only. Use for
> 5:   "write a commit", "commit message", /commit or /caveman-commit.

  `JuliusBrussee_caveman/skills/caveman-commit/SKILL.md:2` `name: caveman-commit`
- `JuliusBrussee_caveman/skills/caveman-compress/SKILL.md`: **703 words**, body **673 words**, 4685 characters, 109 lines.
`JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:3-5`
> 3: description: >
> 4:   Compress a memory file such as CLAUDE.md or a todo list into caveman format
> 5:   to save input tokens, keeping a readable backup. Trigger: /caveman-compress.

  `JuliusBrussee_caveman/skills/caveman-compress/SKILL.md:2` `name: caveman-compress`
- `JuliusBrussee_caveman/skills/caveman-discover/SKILL.md`: **804 words**, body **767 words**, 5248 characters, 115 lines.
`JuliusBrussee_caveman/skills/caveman-discover/SKILL.md:3-6`
> 3: description: >
> 4:   Find and label every LLM workflow in the repository so Caveman Cloud groups
> 5:   spend by workflow instead of one bucket. Use for "discover workflows" or
> 6:   breaking LLM spend down by workflow.

  `JuliusBrussee_caveman/skills/caveman-discover/SKILL.md:2` `name: caveman-discover`
- `JuliusBrussee_caveman/skills/caveman-evidence-review/SKILL.md`: **557 words**, body **525 words**, 3707 characters, 142 lines.
`JuliusBrussee_caveman/skills/caveman-evidence-review/SKILL.md:3-6`
> 3: description: >
> 4:   Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows,
> 5:   traces, latency, errors, routing, savings. Use when asked what Caveman found
> 6:   or where LLM spend goes.

  `JuliusBrussee_caveman/skills/caveman-evidence-review/SKILL.md:2` `name: caveman-evidence-review`
- `JuliusBrussee_caveman/skills/caveman-explore/SKILL.md`: **317 words**, body **269 words**, 1966 characters, 42 lines.
`JuliusBrussee_caveman/skills/caveman-explore/SKILL.md:3-3`
> 3: description: Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. Skip it when the exact file or symbol is already named. Returns path:line citations only; its reads stay out of main context.

  `JuliusBrussee_caveman/skills/caveman-explore/SKILL.md:2` `name: caveman-explore`
- `JuliusBrussee_caveman/skills/caveman-help/SKILL.md`: **386 words**, body **365 words**, 2730 characters, 62 lines.
`JuliusBrussee_caveman/skills/caveman-help/SKILL.md:3-5`
> 3: description: >
> 4:   Quick-reference card for the three caveman skills and their commands.
> 5:   Trigger: /caveman-help or "caveman help".

  `JuliusBrussee_caveman/skills/caveman-help/SKILL.md:2` `name: caveman-help`
- `JuliusBrussee_caveman/skills/caveman-learn/SKILL.md`: **1864 words**, body **1810 words**, 11318 characters, 174 lines.
`JuliusBrussee_caveman/skills/caveman-learn/SKILL.md:3-3`
> 3: description: Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what those fixes returned. Use when asked to lower an agent's token cost, what caveman has saved, to trim a heavy CLAUDE.md, or to offload re-pasted context into cavemem.

  `JuliusBrussee_caveman/skills/caveman-learn/SKILL.md:2` `name: caveman-learn`
- `JuliusBrussee_caveman/skills/caveman-manage/SKILL.md`: **549 words**, body **520 words**, 3898 characters, 112 lines.
`JuliusBrussee_caveman/skills/caveman-manage/SKILL.md:3-6`
> 3: description: >
> 4:   Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. Use
> 5:   when asked to start, approve, cancel, promote or roll back a Caveman
> 6:   experiment.

  `JuliusBrussee_caveman/skills/caveman-manage/SKILL.md:2` `name: caveman-manage`
- `JuliusBrussee_caveman/skills/caveman-optimize/SKILL.md`: **672 words**, body **638 words**, 4721 characters, 111 lines.
`JuliusBrussee_caveman/skills/caveman-optimize/SKILL.md:3-6`
> 3: description: >
> 4:   Turn a Caveman optimization observation into an operator-chosen candidate
> 5:   with a paired baseline evaluation. Use when asked to inspect or evaluate a
> 6:   Caveman optimization report. Needs explicit approval.

  `JuliusBrussee_caveman/skills/caveman-optimize/SKILL.md:2` `name: caveman-optimize`
- `JuliusBrussee_caveman/skills/caveman-review/SKILL.md`: **412 words**, body **383 words**, 2515 characters, 53 lines.
`JuliusBrussee_caveman/skills/caveman-review/SKILL.md:3-5`
> 3: description: >
> 4:   Compressed code review - one line per finding with location, problem and fix.
> 5:   Use for /caveman-review, "review this PR", or "review the diff".

  `JuliusBrussee_caveman/skills/caveman-review/SKILL.md:2` `name: caveman-review`
- `JuliusBrussee_caveman/skills/caveman-setup/SKILL.md`: **1427 words**, body **1393 words**, 10436 characters, 222 lines.
`JuliusBrussee_caveman/skills/caveman-setup/SKILL.md:3-6`
> 3: description: >
> 4:   Wire a repository through the Caveman Cloud gateway so every LLM request is
> 5:   measured, with no behavior change. Use for "set up caveman" or adding LLM
> 6:   spend observability.

  `JuliusBrussee_caveman/skills/caveman-setup/SKILL.md:2` `name: caveman-setup`
- `JuliusBrussee_caveman/skills/caveman-stats/SKILL.md`: **281 words**, body **250 words**, 1964 characters, 17 lines.
`JuliusBrussee_caveman/skills/caveman-stats/SKILL.md:3-6`
> 3: description: >
> 4:   Show recorded output and cache-read token usage and mode attribution for
> 5:   the current Claude Code session, or locate the host's native usage report.
> 6:   Trigger: /caveman-stats.

  `JuliusBrussee_caveman/skills/caveman-stats/SKILL.md:2` `name: caveman-stats`
- `JuliusBrussee_caveman/skills/investigate-first/SKILL.md`: **92 words**, body **69 words**, 688 characters, 16 lines.
`JuliusBrussee_caveman/skills/investigate-first/SKILL.md:3-3`
> 3: description: Diagnose ambiguous failures before editing. Use for unknown causes, intermittent behavior, performance regressions, or investigations needing evidence-ranked hypotheses.

  `JuliusBrussee_caveman/skills/investigate-first/SKILL.md:2` `name: investigate-first`
- `JuliusBrussee_caveman/skills/lean-build/SKILL.md`: **152 words**, body **121 words**, 1090 characters, 18 lines.
`JuliusBrussee_caveman/skills/lean-build/SKILL.md:3-3`
> 3: description: Build feature work with high overbuilding risk. Use for new behavior, product slices, or integrations where repository reuse, strict scope, and an explicit stop condition matter.

  `JuliusBrussee_caveman/skills/lean-build/SKILL.md:2` `name: lean-build`
- `JuliusBrussee_caveman/skills/megacave/SKILL.md`: **320 words**, body **285 words**, 2221 characters, 63 lines.
`JuliusBrussee_caveman/skills/megacave/SKILL.md:3-6`
> 3: description: >
> 4:   Caveman in Classical Chinese: 文言文 register, far fewer characters, technical
> 5:   terms verbatim. Invoke only with /megacave or /caveman wenyan. Stays on until
> 6:   "stop caveman" or "normal mode".

  `JuliusBrussee_caveman/skills/megacave/SKILL.md:2` `name: megacave`
  `JuliusBrussee_caveman/skills/megacave/SKILL.md:7` `disable-model-invocation: true`
- `JuliusBrussee_caveman/skills/migration/SKILL.md`: **104 words**, body **80 words**, 784 characters, 17 lines.
`JuliusBrussee_caveman/skills/migration/SKILL.md:3-3`
> 3: description: Implement reversible compatibility-safe transitions. Use for schema, data, API, protocol, configuration, or dependency migrations requiring rollback and preservation proof.

  `JuliusBrussee_caveman/skills/migration/SKILL.md:2` `name: migration`
- `JuliusBrussee_caveman/skills/safe-refactor/SKILL.md`: **92 words**, body **68 words**, 705 characters, 16 lines.
`JuliusBrussee_caveman/skills/safe-refactor/SKILL.md:3-3`
> 3: description: Restructure code while preserving behavior. Use for extraction, consolidation, ownership moves, or cleanup where verification must bracket structural edits.

  `JuliusBrussee_caveman/skills/safe-refactor/SKILL.md:2` `name: safe-refactor`
- `JuliusBrussee_caveman/skills/surgical-patch/SKILL.md`: **93 words**, body **66 words**, 664 characters, 16 lines.
`JuliusBrussee_caveman/skills/surgical-patch/SKILL.md:3-3`
> 3: description: Fix bugs and small behavior changes at the narrowest responsible layer. Use when regression proof, preserved surrounding behavior, and task-relevant tests matter.

  `JuliusBrussee_caveman/skills/surgical-patch/SKILL.md:2` `name: surgical-patch`
- `JuliusBrussee_caveman/skills/ultracave/SKILL.md`: **340 words**, body **302 words**, 2287 characters, 63 lines.
`JuliusBrussee_caveman/skills/ultracave/SKILL.md:3-6`
> 3: description: >
> 4:   Caveman at maximum compression: fragments, one word when one word is enough,
> 5:   each fact once. Invoke only with /ultracave or /caveman ultra. Stays on until
> 6:   "stop caveman" or "normal mode".

  `JuliusBrussee_caveman/skills/ultracave/SKILL.md:2` `name: ultracave`
  `JuliusBrussee_caveman/skills/ultracave/SKILL.md:7` `disable-model-invocation: true`
- `JuliusBrussee_caveman/skills/verify-and-stop/SKILL.md`: **98 words**, body **72 words**, 704 characters, 16 lines.
`JuliusBrussee_caveman/skills/verify-and-stop/SKILL.md:3-3`
> 3: description: Prove existing work meets acceptance conditions without expanding scope. Use for validation-only tasks, completion checks, focused gate runs, and last-mile proof.

  `JuliusBrussee_caveman/skills/verify-and-stop/SKILL.md:2` `name: verify-and-stop`
- `JuliusBrussee_caveman/src/hooks/README.md`: **1307 words**, body **1307 words**, 9996 characters, 186 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/cavecrew-model-overrides.js`: **710 words**, body **710 words**, 5516 characters, 139 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/caveman-activate.js`: **3983 words**, body **3983 words**, 28075 characters, 562 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/caveman-config.js`: **4558 words**, body **4558 words**, 34612 characters, 825 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/caveman-mode-tracker.js`: **3221 words**, body **3221 words**, 23301 characters, 440 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/caveman-parse.js`: **2517 words**, body **2517 words**, 18115 characters, 342 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/caveman-stats.js`: **3504 words**, body **3504 words**, 27016 characters, 562 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/caveman-statusline.ps1`: **496 words**, body **496 words**, 3449 characters, 86 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/caveman-statusline.sh`: **545 words**, body **545 words**, 3498 characters, 80 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/checksums.sha256`: **18 words**, body **18 words**, 776 characters, 9 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/install.ps1`: **1229 words**, body **1229 words**, 10833 characters, 259 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/install.sh`: **1129 words**, body **1129 words**, 9713 characters, 247 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/package.json`: **4 words**, body **4 words**, 25 characters, 3 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/uninstall.ps1`: **1302 words**, body **1302 words**, 10752 characters, 248 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/hooks/uninstall.sh`: **1104 words**, body **1104 words**, 9026 characters, 211 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-commit.md`: **56 words**, body **44 words**, 370 characters, 8 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-commit.md:2-2`
> 2: description: Generate a terse caveman-style commit message for staged changes

- `JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-compress.md`: **88 words**, body **75 words**, 661 characters, 15 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-compress.md:2-2`
> 2: description: Compress a markdown/text file into caveman format to save tokens

- `JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-help.md`: **98 words**, body **85 words**, 658 characters, 19 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-help.md:2-2`
> 2: description: Quick reference card for caveman modes, slash commands, and triggers

- `JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-review.md`: **47 words**, body **36 words**, 306 characters, 8 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-review.md:2-2`
> 2: description: Caveman-style code review — one-line findings with severity

- `JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-stats.md`: **65 words**, body **55 words**, 446 characters, 8 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/caveman-stats.md:2-2`
> 2: description: Show available session usage without estimating savings

- `JuliusBrussee_caveman/src/plugins/opencode/commands/caveman.md`: **85 words**, body **76 words**, 591 characters, 14 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/caveman.md:2-2`
> 2: description: Activate caveman mode (off | status)

- `JuliusBrussee_caveman/src/plugins/opencode/commands/megacave.md`: **47 words**, body **37 words**, 350 characters, 10 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/megacave.md:2-2`
> 2: description: Activate megacave mode (caveman in Classical Chinese)

- `JuliusBrussee_caveman/src/plugins/opencode/commands/ultracave.md`: **64 words**, body **54 words**, 440 characters, 10 lines.
`JuliusBrussee_caveman/src/plugins/opencode/commands/ultracave.md:2-2`
> 2: description: Activate ultracave mode (caveman at maximum compression)

- `JuliusBrussee_caveman/src/plugins/opencode/plugin.js`: **2459 words**, body **2459 words**, 18342 characters, 378 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/rules/caveman-activate.md`: **184 words**, body **184 words**, 1243 characters, 20 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `JuliusBrussee_caveman/src/rules/caveman-openclaw-bootstrap.md`: **98 words**, body **98 words**, 744 characters, 20 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).

### ayghri_i-have-adhd — 19 selected files, 5091 full-file words
- `ayghri_i-have-adhd/.agents/plugins/marketplace.json`: **36 words**, body **36 words**, 414 characters, 21 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/.claude-plugin/marketplace.json`: **45 words**, body **45 words**, 450 characters, 16 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/.claude-plugin/plugin.json`: **37 words**, body **37 words**, 291 characters, 9 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/.codex-plugin/plugin.json`: **122 words**, body **122 words**, 1278 characters, 39 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/.cursor/skills/i-have-adhd/SKILL.md`: **1242 words**, body **1187 words**, 7207 characters, 142 lines.
`ayghri_i-have-adhd/.cursor/skills/i-have-adhd/SKILL.md:3-3`
> 3: description: 'Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress tangents, give specific time estimates, make wins visible. Invoke with /i-have-adhd; stays on until "stop adhd mode".'

  `ayghri_i-have-adhd/.cursor/skills/i-have-adhd/SKILL.md:2` `name: i-have-adhd`
  `ayghri_i-have-adhd/.cursor/skills/i-have-adhd/SKILL.md:4` `disable-model-invocation: true`
- `ayghri_i-have-adhd/.opencode/command/i-have-adhd.md`: **67 words**, body **51 words**, 409 characters, 8 lines.
`ayghri_i-have-adhd/.opencode/command/i-have-adhd.md:2-2`
> 2: {"description": "Shape output for a reader with ADHD for the rest of this session"}

- `ayghri_i-have-adhd/.opencode/plugins/i-have-adhd.mjs`: **504 words**, body **504 words**, 4079 characters, 99 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/extensions/context-compat.ts`: **195 words**, body **195 words**, 1667 characters, 61 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/extensions/i-have-adhd.ts`: **717 words**, body **717 words**, 6468 characters, 240 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/gemini-extension.json`: **31 words**, body **31 words**, 242 characters, 6 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/hooks/always-on.mjs`: **222 words**, body **222 words**, 1766 characters, 44 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/hooks/always-on.ps1`: **216 words**, body **216 words**, 1651 characters, 50 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/hooks/always-on.sh`: **271 words**, body **271 words**, 1685 characters, 37 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/hooks/hooks.json`: **32 words**, body **32 words**, 549 characters, 17 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/kimi.plugin.json`: **56 words**, body **56 words**, 483 characters, 12 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/opencode.json`: **6 words**, body **6 words**, 104 characters, 4 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/plugin.json`: **26 words**, body **26 words**, 187 characters, 4 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/qwen-extension.json`: **24 words**, body **24 words**, 201 characters, 6 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md`: **1242 words**, body **1187 words**, 7207 characters, 142 lines.
`ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:3-3`
> 3: description: 'Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress tangents, give specific time estimates, make wins visible. Invoke with /i-have-adhd; stays on until "stop adhd mode".'

  `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:2` `name: i-have-adhd`
  `ayghri_i-have-adhd/skills/i-have-adhd/SKILL.md:4` `disable-model-invocation: true`

### blader_humanizer — 4 selected files, 5353 full-file words
- `blader_humanizer/.claude-plugin/marketplace.json`: **52 words**, body **52 words**, 521 characters, 18 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `blader_humanizer/.claude-plugin/plugin.json`: **44 words**, body **44 words**, 526 characters, 15 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `blader_humanizer/.cursor-plugin/plugin.json`: **38 words**, body **38 words**, 388 characters, 12 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `blader_humanizer/SKILL.md`: **5219 words**, body **5157 words**, 32309 characters, 397 lines.
`blader_humanizer/SKILL.md:3-7`
> 3: description: |
> 4:   Rewrite AI-sounding text so it reads like the writer without changing what it says.
> 5:   Use when editing or reviewing prose for AI tells: not-X-but-Y contrasts, one-line
> 6:   closers, staged openers, forced triads, dashes everywhere, inflated claims, sales
> 7:   language, stock AI words, bold labels, or filler. Based on Wikipedia's "Signs of AI writing."

  `blader_humanizer/SKILL.md:2` `name: humanizer`

### hardikpandya_stop-slop — 4 selected files, 1995 full-file words
- `hardikpandya_stop-slop/SKILL.md`: **361 words**, body **323 words**, 2629 characters, 68 lines.
`hardikpandya_stop-slop/SKILL.md:3-3`
> 3: description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells.

  `hardikpandya_stop-slop/SKILL.md:2` `name: stop-slop`
- `hardikpandya_stop-slop/references/examples.md`: **235 words**, body **235 words**, 1684 characters, 59 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hardikpandya_stop-slop/references/phrases.md`: **499 words**, body **499 words**, 2915 characters, 128 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hardikpandya_stop-slop/references/structures.md`: **900 words**, body **900 words**, 5255 characters, 134 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).

### petergyang_no-ai-slop — 3 selected files, 2396 full-file words
- `petergyang_no-ai-slop/.codex-plugin/plugin.json`: **177 words**, body **177 words**, 1899 characters, 41 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md`: **1715 words**, body **1669 words**, 10853 characters, 97 lines.
`petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:3-3`
> 3: description: Edit drafts into sharper, more human writing while preserving the writer's personal voice, or detect AI-slop patterns without rewriting. Use when the user wants a draft clearer, more direct, more opinionated, or less AI-sounding, or asks whether writing reads as AI.

  `petergyang_no-ai-slop/skills/no-ai-slop/SKILL.md:2` `name: no-ai-slop`
- `petergyang_no-ai-slop/skills/no-ai-slop/eval.md`: **504 words**, body **504 words**, 3214 characters, 43 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).

### obra_the-elements-of-style — 15 selected files, 13104 full-file words
- `obra_the-elements-of-style/.agents/plugins/marketplace.json`: **30 words**, body **30 words**, 340 characters, 19 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.claude-plugin/marketplace.json`: **49 words**, body **49 words**, 503 characters, 20 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.claude-plugin/plugin.json`: **42 words**, body **42 words**, 484 characters, 19 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.codex-plugin/plugin.json`: **46 words**, body **46 words**, 524 characters, 21 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.cursor-plugin/plugin.json`: **46 words**, body **46 words**, 547 characters, 21 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.devin-plugin/plugin.json`: **42 words**, body **42 words**, 484 characters, 19 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.kimi-plugin/plugin.json`: **44 words**, body **44 words**, 509 characters, 20 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.opencode/plugins/elements-of-style.js`: **96 words**, body **96 words**, 804 characters, 23 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/.pi/extensions/elements-of-style.ts`: **67 words**, body **67 words**, 588 characters, 16 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/GEMINI.md`: **15 words**, body **15 words**, 109 characters, 3 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/everyharness.yaml`: **83 words**, body **83 words**, 651 characters, 20 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/gemini-extension.json`: **21 words**, body **21 words**, 186 characters, 6 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/plugin.json`: **44 words**, body **44 words**, 559 characters, 20 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md`: **325 words**, body **292 words**, 2209 characters, 62 lines.
`obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:3-3`
> 3: description: Apply Strunk's timeless writing rules to ANY prose humans will read—documentation, commit messages, error messages, explanations, reports, or UI text. Makes your writing clearer, stronger, and more professional.

  `obra_the-elements-of-style/skills/writing-clearly-and-concisely/SKILL.md:2` `name: writing-clearly-and-concisely`
- `obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md`: **12154 words**, body **12154 words**, 70748 characters, 995 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).

### hexiecs_talk-normal — 9 selected files, 4219 full-file words
- `hexiecs_talk-normal/install.sh`: **461 words**, body **461 words**, 3444 characters, 124 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hexiecs_talk-normal/prompt-chatgpt.md`: **217 words**, body **217 words**, 1400 characters, 24 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hexiecs_talk-normal/prompt.md`: **545 words**, body **545 words**, 3527 characters, 34 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hexiecs_talk-normal/skill/SKILL.md`: **543 words**, body **489 words**, 3723 characters, 74 lines.
`hexiecs_talk-normal/skill/SKILL.md:4-4`
> 4: description: Stop LLM slop. A curated system prompt that cuts verbose, corporate-sounding LLM output by 56-71% (measured) while preserving information. Works bilingually (English + Chinese). Installs into your AGENTS.md as an always-on behavior modifier.

  `hexiecs_talk-normal/skill/SKILL.md:2` `name: talk-normal`
- `hexiecs_talk-normal/skill/install.sh`: **461 words**, body **461 words**, 3444 characters, 124 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hexiecs_talk-normal/skill/prompt.md`: **545 words**, body **545 words**, 3527 characters, 34 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hexiecs_talk-normal/skill-hermes/SKILL.md`: **441 words**, body **385 words**, 3135 characters, 62 lines.
`hexiecs_talk-normal/skill-hermes/SKILL.md:3-3`
> 3: description: Stop LLM slop. A curated system prompt that cuts verbose, corporate-sounding LLM output by 56-73% (measured) while preserving information. Works bilingually (English + Chinese). Installs into your AGENTS.md as an always-on behavior modifier.

  `hexiecs_talk-normal/skill-hermes/SKILL.md:2` `name: talk-normal`
- `hexiecs_talk-normal/skill-hermes/install.sh`: **461 words**, body **461 words**, 3444 characters, 124 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `hexiecs_talk-normal/skill-hermes/prompt.md`: **545 words**, body **545 words**, 3527 characters, 34 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).

### smixs_awesome-claude-output-styles — 24 selected files, 12604 full-file words
- `smixs_awesome-claude-output-styles/commands/style.md`: **595 words**, body **569 words**, 3739 characters, 84 lines.
`smixs_awesome-claude-output-styles/commands/style.md:2-2`
> 2: description: Switch the active Claude Code output style from a picker

  `smixs_awesome-claude-output-styles/commands/style.md:5` `disable-model-invocation: true`
- `smixs_awesome-claude-output-styles/hooks/style-reminder.sh`: **170 words**, body **170 words**, 1278 characters, 32 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `smixs_awesome-claude-output-styles/install.sh`: **806 words**, body **806 words**, 6546 characters, 195 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `smixs_awesome-claude-output-styles/output-styles/adhd.md`: **463 words**, body **443 words**, 2810 characters, 58 lines.
`smixs_awesome-claude-output-styles/output-styles/adhd.md:3-3`
> 3: description: Action first, numbered steps, short lists, visible progress - built for scattered attention

  `smixs_awesome-claude-output-styles/output-styles/adhd.md:2` `name: ADHD`
  `smixs_awesome-claude-output-styles/output-styles/adhd.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md`: **513 words**, body **491 words**, 3222 characters, 62 lines.
`smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:3-3`
> 3: description: Explains through one sustained analogy with an explicit part-by-part mapping and its breaking points

  `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:2` `name: Analogy Engine`
  `smixs_awesome-claude-output-styles/output-styles/analogy-engine.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md`: **509 words**, body **489 words**, 3174 characters, 59 lines.
`smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:3-3`
> 3: description: Explains concepts as tiny calming stories where the concept is the hero

  `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:2` `name: Bedtime Story`
  `smixs_awesome-claude-output-styles/output-styles/bedtime-story.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/caveman.md`: **323 words**, body **307 words**, 2133 characters, 47 lines.
`smixs_awesome-claude-output-styles/output-styles/caveman.md:3-3`
> 3: description: Ultra-compact replies - same technical signal, all fluff dropped

  `smixs_awesome-claude-output-styles/output-styles/caveman.md:2` `name: Caveman`
  `smixs_awesome-claude-output-styles/output-styles/caveman.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/coach.md`: **510 words**, body **489 words**, 2960 characters, 57 lines.
`smixs_awesome-claude-output-styles/output-styles/coach.md:3-3`
> 3: description: Talks like a great coach - short, vivid, direct, every word earns its place

  `smixs_awesome-claude-output-styles/output-styles/coach.md:2` `name: Coach`
  `smixs_awesome-claude-output-styles/output-styles/coach.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/eli15.md`: **470 words**, body **448 words**, 2892 characters, 57 lines.
`smixs_awesome-claude-output-styles/output-styles/eli15.md:3-3`
> 3: description: Explains everything to a smart 15-year-old with one good analogy and a line worth remembering

  `smixs_awesome-claude-output-styles/output-styles/eli15.md:2` `name: ELI15`
  `smixs_awesome-claude-output-styles/output-styles/eli15.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/executive.md`: **523 words**, body **502 words**, 3281 characters, 67 lines.
`smixs_awesome-claude-output-styles/output-styles/executive.md:3-3`
> 3: description: Answer first, three reasons, evidence on request - the Minto Pyramid for every reply

  `smixs_awesome-claude-output-styles/output-styles/executive.md:2` `name: Executive`
  `smixs_awesome-claude-output-styles/output-styles/executive.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/feynman.md`: **503 words**, body **483 words**, 3074 characters, 60 lines.
`smixs_awesome-claude-output-styles/output-styles/feynman.md:3-3`
> 3: description: Teaches instead of telling, names the hard parts, and checks understanding with questions

  `smixs_awesome-claude-output-styles/output-styles/feynman.md:2` `name: Feynman`
  `smixs_awesome-claude-output-styles/output-styles/feynman.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/gen-z.md`: **452 words**, body **431 words**, 2962 characters, 60 lines.
`smixs_awesome-claude-output-styles/output-styles/gen-z.md:3-3`
> 3: description: Brainrot-flavored answers - skibidi slang wrapper, exact engineering underneath. Slang dated by design

  `smixs_awesome-claude-output-styles/output-styles/gen-z.md:2` `name: Gen Z`
  `smixs_awesome-claude-output-styles/output-styles/gen-z.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/ladder.md`: **510 words**, body **487 words**, 3109 characters, 67 lines.
`smixs_awesome-claude-output-styles/output-styles/ladder.md:3-3`
> 3: description: Answers three times, at three levels - like I'm 5, like I'm 15, like a pro

  `smixs_awesome-claude-output-styles/output-styles/ladder.md:2` `name: Ladder`
  `smixs_awesome-claude-output-styles/output-styles/ladder.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md`: **453 words**, body **428 words**, 2860 characters, 57 lines.
`smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:3-3`
> 3: description: Direct, opinionated answers with zero filler and a real point of view. After Peter Yang's no-ai-slop

  `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:2` `name: No AI Slop`
  `smixs_awesome-claude-output-styles/output-styles/no-ai-slop.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/no-slop.md`: **527 words**, body **508 words**, 3223 characters, 63 lines.
`smixs_awesome-claude-output-styles/output-styles/no-slop.md:3-3`
> 3: description: A plain, specific, human voice - the antidote to 2026 Claude-isms

  `smixs_awesome-claude-output-styles/output-styles/no-slop.md:2` `name: No Slop`
  `smixs_awesome-claude-output-styles/output-styles/no-slop.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/plain-english.md`: **429 words**, body **410 words**, 2554 characters, 54 lines.
`smixs_awesome-claude-output-styles/output-styles/plain-english.md:3-3`
> 3: description: Answers in Simplified Technical English, the controlled language aerospace manuals use

  `smixs_awesome-claude-output-styles/output-styles/plain-english.md:2` `name: Plain English`
  `smixs_awesome-claude-output-styles/output-styles/plain-english.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md`: **505 words**, body **481 words**, 3051 characters, 69 lines.
`smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:3-3`
> 3: description: Axios-style answers - a six-word headline, one big thing, why it matters, go deeper on demand

  `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:2` `name: Smart Brevity`
  `smixs_awesome-claude-output-styles/output-styles/smart-brevity.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/sportscaster.md`: **561 words**, body **541 words**, 3399 characters, 66 lines.
`smixs_awesome-claude-output-styles/output-styles/sportscaster.md:3-3`
> 3: description: Live play-by-play commentary on your codebase - always with the real answer inside

  `smixs_awesome-claude-output-styles/output-styles/sportscaster.md:2` `name: Sportscaster`
  `smixs_awesome-claude-output-styles/output-styles/sportscaster.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/street.md`: **502 words**, body **481 words**, 3077 characters, 63 lines.
`smixs_awesome-claude-output-styles/output-styles/street.md:3-3`
> 3: description: A sharp senior engineer who explains everything in modern street slang. Profanity included, 18+

  `smixs_awesome-claude-output-styles/output-styles/street.md:2` `name: Street`
  `smixs_awesome-claude-output-styles/output-styles/street.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md`: **484 words**, body **462 words**, 2769 characters, 53 lines.
`smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:3-3`
> 3: description: Explains using only the ten hundred most common English words, like the xkcd book

  `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:2` `name: Thing Explainer`
  `smixs_awesome-claude-output-styles/output-styles/thing-explainer.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/unslop.md`: **830 words**, body **806 words**, 5091 characters, 93 lines.
`smixs_awesome-claude-output-styles/output-styles/unslop.md:3-3`
> 3: description: Plain punctuation, concrete words, and a real opinion in every reply. After the unslop skill in cursor/plugins

  `smixs_awesome-claude-output-styles/output-styles/unslop.md:2` `name: Unslop`
  `smixs_awesome-claude-output-styles/output-styles/unslop.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/wait-what.md`: **457 words**, body **431 words**, 2847 characters, 54 lines.
`smixs_awesome-claude-output-styles/output-styles/wait-what.md:3-3`
> 3: description: Re-pitches every answer with context, in Simplified Technical English, using your project's own vocabulary. After Matt Pocock's wait-what

  `smixs_awesome-claude-output-styles/output-styles/wait-what.md:2` `name: Wait What`
  `smixs_awesome-claude-output-styles/output-styles/wait-what.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/output-styles/yoda.md`: **480 words**, body **459 words**, 2918 characters, 62 lines.
`smixs_awesome-claude-output-styles/output-styles/yoda.md:3-3`
> 3: description: A wise mentor who answers plainly, then lands the lesson in inverted word order

  `smixs_awesome-claude-output-styles/output-styles/yoda.md:2` `name: Yoda`
  `smixs_awesome-claude-output-styles/output-styles/yoda.md:4` `keep-coding-instructions: true`
- `smixs_awesome-claude-output-styles/skills/style-maker/SKILL.md`: **1029 words**, body **951 words**, 6712 characters, 123 lines.
`smixs_awesome-claude-output-styles/skills/style-maker/SKILL.md:3-9`
> 3: description: >
> 4:   Interviews the user with ~10 questions about how they want Claude to talk,
> 5:   optionally collects writing samples they like and hate, then generates a
> 6:   personal Claude Code output style file and activates it. Use when the user
> 7:   says "make my output style", "build me a custom style", "I want Claude to
> 8:   talk like...", "create a personal writing style", or complains about
> 9:   Claude's tone and wants a tailored fix rather than a preset.

  `smixs_awesome-claude-output-styles/skills/style-maker/SKILL.md:2` `name: style-maker`

### Kyaa-A_eli5 — 7 selected files, 1297 full-file words
- `Kyaa-A_eli5/.agents/plugins/marketplace.json`: **34 words**, body **34 words**, 360 characters, 21 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `Kyaa-A_eli5/.claude-plugin/marketplace.json`: **61 words**, body **61 words**, 666 characters, 22 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `Kyaa-A_eli5/.claude-plugin/plugin.json`: **40 words**, body **40 words**, 511 characters, 14 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `Kyaa-A_eli5/.codex-plugin/plugin.json`: **90 words**, body **90 words**, 978 characters, 28 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `Kyaa-A_eli5/hooks/hooks.json`: **90 words**, body **90 words**, 953 characters, 18 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `Kyaa-A_eli5/scripts/check-update.mjs`: **602 words**, body **602 words**, 5599 characters, 133 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `Kyaa-A_eli5/skills/eli5/SKILL.md`: **380 words**, body **324 words**, 2359 characters, 52 lines.
`Kyaa-A_eli5/skills/eli5/SKILL.md:3-3`
> 3: description: This skill should be used when the user says "/eli5", "eli5", "explain like I'm 5", "simplify", "too complex", "make it simpler", "ELI5", or asks for a plain-language explanation of code, errors, or concepts. Forces maximally simple, jargon-free output. When triggered without a specific topic, re-explain the previous response in simplified form.

  `Kyaa-A_eli5/skills/eli5/SKILL.md:2` `name: eli5`

### rahulj51_eli5 — 5 selected files, 1368 full-file words
- `rahulj51_eli5/.claude-plugin/marketplace.json`: **35 words**, body **35 words**, 298 characters, 14 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `rahulj51_eli5/.claude-plugin/plugin.json`: **21 words**, body **21 words**, 193 characters, 9 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `rahulj51_eli5/.codex-plugin/plugin.json`: **98 words**, body **98 words**, 1098 characters, 36 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `rahulj51_eli5/skills/eli5/SKILL.md`: **453 words**, body **402 words**, 2665 characters, 49 lines.
`rahulj51_eli5/skills/eli5/SKILL.md:3-3`
> 3: description: Rewrite or summarize content in plain, concise English for a busy executive (think CTO/CPO). Use whenever the user says "eli5" anywhere in a request, or asks for a simple, plain-English, or executive version of an agent response, spec, doc, plan, bug report, or code review comment.

  `rahulj51_eli5/skills/eli5/SKILL.md:2` `name: eli5`
- `rahulj51_eli5/skills/ste/SKILL.md`: **761 words**, body **721 words**, 4690 characters, 84 lines.
`rahulj51_eli5/skills/ste/SKILL.md:3-3`
> 3: description: Create, rewrite, or summarize technical content in ASD-STE100 Simplified Technical English. Use when the user invokes "ste" as a skill, says "ASD-STE100", "ASD-ST100", "STE100", or "Simplified Technical English", or explicitly asks for controlled technical English.

  `rahulj51_eli5/skills/ste/SKILL.md:2` `name: ste`

### fcakyon_claude-codex-settings/plugins/adhd-output-style — 6 selected files, 647 full-file words
- `fcakyon_claude-codex-settings/plugins/adhd-output-style/.claude-plugin/plugin.json`: **28 words**, body **28 words**, 227 characters, 9 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `fcakyon_claude-codex-settings/plugins/adhd-output-style/.codex-plugin/plugin.json`: **28 words**, body **28 words**, 227 characters, 9 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `fcakyon_claude-codex-settings/plugins/adhd-output-style/.cursor-plugin/plugin.json`: **28 words**, body **28 words**, 227 characters, 9 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `fcakyon_claude-codex-settings/plugins/adhd-output-style/gemini-extension.json`: **19 words**, body **19 words**, 152 characters, 5 lines.
  Frontmatter: absent (any JSON/TOML description is packaging/command metadata, not YAML frontmatter).
- `fcakyon_claude-codex-settings/plugins/adhd-output-style/output-styles/adhd-explanatory.md`: **264 words**, body **245 words**, 1775 characters, 39 lines.
`fcakyon_claude-codex-settings/plugins/adhd-output-style/output-styles/adhd-explanatory.md:3-3`
> 3: description: Low-token ADHD formatting plus educational Insight blocks while coding

  `fcakyon_claude-codex-settings/plugins/adhd-output-style/output-styles/adhd-explanatory.md:2` `name: ADHD Explanatory`
  `fcakyon_claude-codex-settings/plugins/adhd-output-style/output-styles/adhd-explanatory.md:4` `keep-coding-instructions: true`
  `fcakyon_claude-codex-settings/plugins/adhd-output-style/output-styles/adhd-explanatory.md:5` `force-for-plugin: true`
- `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md`: **280 words**, body **249 words**, 1862 characters, 37 lines.
`fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:3-3`
> 3: description: This skill should be used when the user asks for "ADHD output", "fewer output tokens", "short numbered steps", "limited working memory formatting", or explicitly invokes "adhd-output-style".

  `fcakyon_claude-codex-settings/plugins/adhd-output-style/skills/adhd-output-style/SKILL.md:2` `name: adhd-output-style`

### Explicit package absence check
Recursive scan covered **1,868 non-.git files across 11 scoped repository roots**, including only six fcakyon plugin files. It found **33 files named plugin.json / marketplace.json / hooks.json**. This denominator includes non-Claude adapters, so it is not “33 Claude plugins”.
| Source | Scoped files scanned | Claude plugin manifest | Claude marketplace | Registered style hooks | Markdown command files |
|---|---:|---|---|---|---|
| JuliusBrussee_caveman | 1618 | present | present | SessionStart + UserPromptSubmit | 9 |
| ayghri_i-have-adhd | 73 | present | present | SessionStart, opt-in | 1 |
| blader_humanizer | 14 | present | present | absent | 0 |
| hardikpandya_stop-slop | 7 | absent | absent | absent | 0 |
| petergyang_no-ai-slop | 14 | absent | absent | absent | 0 |
| obra_the-elements-of-style | 34 | present | present | absent | 0 |
| hexiecs_talk-normal | 22 | absent | absent | absent | 0 |
| smixs_awesome-claude-output-styles | 45 | absent | absent | optional installed UserPromptSubmit | 1 |
| Kyaa-A_eli5 | 26 | present | present | SessionStart update check only | 0 |
| rahulj51_eli5 | 9 | present | present | absent | 0 |
| fcakyon_claude-codex-settings/plugins/adhd-output-style | 6 | present | absent inside plugin; root entry present | absent | 0 |
The command count includes root and other-host Markdown command templates: Caveman 1 root + 8 OpenCode; ayghri 1 OpenCode; Smixs 1 root. A skill invocation can still exist when a standalone command file is absent. Root and nested `.git/hooks` samples are excluded; they are Git infrastructure, not style hooks.
## Appendix B. Licenses: SPDX identification and full source text
SPDX identification below is based on the actual license text, not merely README badges. “Public Domain” has no supplied standardized SPDX grant. Full source lines are shown for each distinct license text; identical texts are referenced rather than duplicated. Licenses have no YAML description frontmatter.
### JuliusBrussee_caveman/LICENSE — SPDX identification `Apache-2.0`, 1581 words, 202 lines
`JuliusBrussee_caveman/LICENSE:1-202`
> 1: 
> 2:                                  Apache License
> 3:                            Version 2.0, January 2004
> 4:                         http://www.apache.org/licenses/
> 5: 
> 6:    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
> 7: 
> 8:    1. Definitions.
> 9: 
> 10:       "License" shall mean the terms and conditions for use, reproduction,
> 11:       and distribution as defined by Sections 1 through 9 of this document.
> 12: 
> 13:       "Licensor" shall mean the copyright owner or entity authorized by
> 14:       the copyright owner that is granting the License.
> 15: 
> 16:       "Legal Entity" shall mean the union of the acting entity and all
> 17:       other entities that control, are controlled by, or are under common
> 18:       control with that entity. For the purposes of this definition,
> 19:       "control" means (i) the power, direct or indirect, to cause the
> 20:       direction or management of such entity, whether by contract or
> 21:       otherwise, or (ii) ownership of fifty percent (50%) or more of the
> 22:       outstanding shares, or (iii) beneficial ownership of such entity.
> 23: 
> 24:       "You" (or "Your") shall mean an individual or Legal Entity
> 25:       exercising permissions granted by this License.
> 26: 
> 27:       "Source" form shall mean the preferred form for making modifications,
> 28:       including but not limited to software source code, documentation
> 29:       source, and configuration files.
> 30: 
> 31:       "Object" form shall mean any form resulting from mechanical
> 32:       transformation or translation of a Source form, including but
> 33:       not limited to compiled object code, generated documentation,
> 34:       and conversions to other media types.
> 35: 
> 36:       "Work" shall mean the work of authorship, whether in Source or
> 37:       Object form, made available under the License, as indicated by a
> 38:       copyright notice that is included in or attached to the work
> 39:       (an example is provided in the Appendix below).
> 40: 
> 41:       "Derivative Works" shall mean any work, whether in Source or Object
> 42:       form, that is based on (or derived from) the Work and for which the
> 43:       editorial revisions, annotations, elaborations, or other modifications
> 44:       represent, as a whole, an original work of authorship. For the purposes
> 45:       of this License, Derivative Works shall not include works that remain
> 46:       separable from, or merely link (or bind by name) to the interfaces of,
> 47:       the Work and Derivative Works thereof.
> 48: 
> 49:       "Contribution" shall mean any work of authorship, including
> 50:       the original version of the Work and any modifications or additions
> 51:       to that Work or Derivative Works thereof, that is intentionally
> 52:       submitted to Licensor for inclusion in the Work by the copyright owner
> 53:       or by an individual or Legal Entity authorized to submit on behalf of
> 54:       the copyright owner. For the purposes of this definition, "submitted"
> 55:       means any form of electronic, verbal, or written communication sent
> 56:       to the Licensor or its representatives, including but not limited to
> 57:       communication on electronic mailing lists, source code control systems,
> 58:       and issue tracking systems that are managed by, or on behalf of, the
> 59:       Licensor for the purpose of discussing and improving the Work, but
> 60:       excluding communication that is conspicuously marked or otherwise
> 61:       designated in writing by the copyright owner as "Not a Contribution."
> 62: 
> 63:       "Contributor" shall mean Licensor and any individual or Legal Entity
> 64:       on behalf of whom a Contribution has been received by Licensor and
> 65:       subsequently incorporated within the Work.
> 66: 
> 67:    2. Grant of Copyright License. Subject to the terms and conditions of
> 68:       this License, each Contributor hereby grants to You a perpetual,
> 69:       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
> 70:       copyright license to reproduce, prepare Derivative Works of,
> 71:       publicly display, publicly perform, sublicense, and distribute the
> 72:       Work and such Derivative Works in Source or Object form.
> 73: 
> 74:    3. Grant of Patent License. Subject to the terms and conditions of
> 75:       this License, each Contributor hereby grants to You a perpetual,
> 76:       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
> 77:       (except as stated in this section) patent license to make, have made,
> 78:       use, offer to sell, sell, import, and otherwise transfer the Work,
> 79:       where such license applies only to those patent claims licensable
> 80:       by such Contributor that are necessarily infringed by their
> 81:       Contribution(s) alone or by combination of their Contribution(s)
> 82:       with the Work to which such Contribution(s) was submitted. If You
> 83:       institute patent litigation against any entity (including a
> 84:       cross-claim or counterclaim in a lawsuit) alleging that the Work
> 85:       or a Contribution incorporated within the Work constitutes direct
> 86:       or contributory patent infringement, then any patent licenses
> 87:       granted to You under this License for that Work shall terminate
> 88:       as of the date such litigation is filed.
> 89: 
> 90:    4. Redistribution. You may reproduce and distribute copies of the
> 91:       Work or Derivative Works thereof in any medium, with or without
> 92:       modifications, and in Source or Object form, provided that You
> 93:       meet the following conditions:
> 94: 
> 95:       (a) You must give any other recipients of the Work or
> 96:           Derivative Works a copy of this License; and
> 97: 
> 98:       (b) You must cause any modified files to carry prominent notices
> 99:           stating that You changed the files; and
> 100: 
> 101:       (c) You must retain, in the Source form of any Derivative Works
> 102:           that You distribute, all copyright, patent, trademark, and
> 103:           attribution notices from the Source form of the Work,
> 104:           excluding those notices that do not pertain to any part of
> 105:           the Derivative Works; and
> 106: 
> 107:       (d) If the Work includes a "NOTICE" text file as part of its
> 108:           distribution, then any Derivative Works that You distribute must
> 109:           include a readable copy of the attribution notices contained
> 110:           within such NOTICE file, excluding those notices that do not
> 111:           pertain to any part of the Derivative Works, in at least one
> 112:           of the following places: within a NOTICE text file distributed
> 113:           as part of the Derivative Works; within the Source form or
> 114:           documentation, if provided along with the Derivative Works; or,
> 115:           within a display generated by the Derivative Works, if and
> 116:           wherever such third-party notices normally appear. The contents
> 117:           of the NOTICE file are for informational purposes only and
> 118:           do not modify the License. You may add Your own attribution
> 119:           notices within Derivative Works that You distribute, alongside
> 120:           or as an addendum to the NOTICE text from the Work, provided
> 121:           that such additional attribution notices cannot be construed
> 122:           as modifying the License.
> 123: 
> 124:       You may add Your own copyright statement to Your modifications and
> 125:       may provide additional or different license terms and conditions
> 126:       for use, reproduction, or distribution of Your modifications, or
> 127:       for any such Derivative Works as a whole, provided Your use,
> 128:       reproduction, and distribution of the Work otherwise complies with
> 129:       the conditions stated in this License.
> 130: 
> 131:    5. Submission of Contributions. Unless You explicitly state otherwise,
> 132:       any Contribution intentionally submitted for inclusion in the Work
> 133:       by You to the Licensor shall be under the terms and conditions of
> 134:       this License, without any additional terms or conditions.
> 135:       Notwithstanding the above, nothing herein shall supersede or modify
> 136:       the terms of any separate license agreement you may have executed
> 137:       with Licensor regarding such Contributions.
> 138: 
> 139:    6. Trademarks. This License does not grant permission to use the trade
> 140:       names, trademarks, service marks, or product names of the Licensor,
> 141:       except as required for reasonable and customary use in describing the
> 142:       origin of the Work and reproducing the content of the NOTICE file.
> 143: 
> 144:    7. Disclaimer of Warranty. Unless required by applicable law or
> 145:       agreed to in writing, Licensor provides the Work (and each
> 146:       Contributor provides its Contributions) on an "AS IS" BASIS,
> 147:       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
> 148:       implied, including, without limitation, any warranties or conditions
> 149:       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
> 150:       PARTICULAR PURPOSE. You are solely responsible for determining the
> 151:       appropriateness of using or redistributing the Work and assume any
> 152:       risks associated with Your exercise of permissions under this License.
> 153: 
> 154:    8. Limitation of Liability. In no event and under no legal theory,
> 155:       whether in tort (including negligence), contract, or otherwise,
> 156:       unless required by applicable law (such as deliberate and grossly
> 157:       negligent acts) or agreed to in writing, shall any Contributor be
> 158:       liable to You for damages, including any direct, indirect, special,
> 159:       incidental, or consequential damages of any character arising as a
> 160:       result of this License or out of the use or inability to use the
> 161:       Work (including but not limited to damages for loss of goodwill,
> 162:       work stoppage, computer failure or malfunction, or any and all
> 163:       other commercial damages or losses), even if such Contributor
> 164:       has been advised of the possibility of such damages.
> 165: 
> 166:    9. Accepting Warranty or Additional Liability. While redistributing
> 167:       the Work or Derivative Works thereof, You may choose to offer,
> 168:       and charge a fee for, acceptance of support, warranty, indemnity,
> 169:       or other liability obligations and/or rights consistent with this
> 170:       License. However, in accepting such obligations, You may act only
> 171:       on Your own behalf and on Your sole responsibility, not on behalf
> 172:       of any other Contributor, and only if You agree to indemnify,
> 173:       defend, and hold each Contributor harmless for any liability
> 174:       incurred by, or claims asserted against, such Contributor by reason
> 175:       of your accepting any such warranty or additional liability.
> 176: 
> 177:    END OF TERMS AND CONDITIONS
> 178: 
> 179:    APPENDIX: How to apply the Apache License to your work.
> 180: 
> 181:       To apply the Apache License to your work, attach the following
> 182:       boilerplate notice, with the fields enclosed by brackets "[]"
> 183:       replaced with your own identifying information. (Don't include
> 184:       the brackets!)  The text should be enclosed in the appropriate
> 185:       comment syntax for the file format. We also recommend that a
> 186:       file or class name and description of purpose be included on the
> 187:       same "printed page" as the copyright notice for easier
> 188:       identification within third-party archives.
> 189: 
> 190:    Copyright [yyyy] [name of copyright owner]
> 191: 
> 192:    Licensed under the Apache License, Version 2.0 (the "License");
> 193:    you may not use this file except in compliance with the License.
> 194:    You may obtain a copy of the License at
> 195: 
> 196:        http://www.apache.org/licenses/LICENSE-2.0
> 197: 
> 198:    Unless required by applicable law or agreed to in writing, software
> 199:    distributed under the License is distributed on an "AS IS" BASIS,
> 200:    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> 201:    See the License for the specific language governing permissions and
> 202:    limitations under the License.

### JuliusBrussee_caveman/LICENSE-MIT — SPDX identification `MIT`, 169 words, 21 lines
`JuliusBrussee_caveman/LICENSE-MIT:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2026 Julius Brussee
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### ayghri_i-have-adhd/LICENSE — SPDX identification `MIT`, 169 words, 21 lines
`ayghri_i-have-adhd/LICENSE:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2026 Ayoub Ghriss
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### blader_humanizer/LICENSE — SPDX identification `MIT`, 169 words, 21 lines
`blader_humanizer/LICENSE:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2025 Siqi Chen
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### hardikpandya_stop-slop/LICENSE — SPDX identification `MIT`, 169 words, 21 lines
`hardikpandya_stop-slop/LICENSE:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2025 Hardik Pandya
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### petergyang_no-ai-slop/LICENSE — SPDX identification `MIT`, 169 words, 21 lines
`petergyang_no-ai-slop/LICENSE:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2026 Peter Yang
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### hexiecs_talk-normal/LICENSE — SPDX identification `MIT`, 168 words, 21 lines
`hexiecs_talk-normal/LICENSE:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2026 hexie
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### smixs_awesome-claude-output-styles/LICENSE — SPDX identification `MIT`, 240 words, 33 lines
`smixs_awesome-claude-output-styles/LICENSE:1-33`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2026 Serge Shima
> 4: 
> 5: Some styles adapt ideas and text from MIT-licensed projects; their copyright
> 6: notices are preserved in the credit lines of the corresponding style files
> 7: and in README credits:
> 8: 
> 9: - Copyright (c) 2026 Matt Pocock (mattpocock/skills)
> 10: - Copyright (c) Julius Brussee (JuliusBrussee/caveman)
> 11: - Copyright (c) Carlos Duplá (carlosduplar/caveman-output-style-claude-code)
> 12: - Copyright (c) ayghri (ayghri/i-have-adhd)
> 13: - Copyright (c) Amin Boulegroun (AminBlg/SimpleEnglish)
> 14: - Copyright (c) Peter Yang (petergyang/no-ai-slop)
> 15: - Copyright (c) 2026 Lauren Tan (cursor/plugins, pstack)
> 16: 
> 17: Permission is hereby granted, free of charge, to any person obtaining a copy
> 18: of this software and associated documentation files (the "Software"), to deal
> 19: in the Software without restriction, including without limitation the rights
> 20: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 21: copies of the Software, and to permit persons to whom the Software is
> 22: furnished to do so, subject to the following conditions:
> 23: 
> 24: The above copyright notice and this permission notice shall be included in all
> 25: copies or substantial portions of the Software.
> 26: 
> 27: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 28: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 29: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 30: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 31: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 32: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 33: SOFTWARE.

### Kyaa-A_eli5/LICENSE — SPDX identification `MIT`, 169 words, 21 lines
`Kyaa-A_eli5/LICENSE:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2026 Asnari Pacalna
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### rahulj51_eli5/LICENSE — SPDX identification `MIT`, 169 words, 21 lines
`rahulj51_eli5/LICENSE:1-21`
> 1: MIT License
> 2: 
> 3: Copyright (c) 2026 Rahul Jain
> 4: 
> 5: Permission is hereby granted, free of charge, to any person obtaining a copy
> 6: of this software and associated documentation files (the "Software"), to deal
> 7: in the Software without restriction, including without limitation the rights
> 8: to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> 9: copies of the Software, and to permit persons to whom the Software is
> 10: furnished to do so, subject to the following conditions:
> 11: 
> 12: The above copyright notice and this permission notice shall be included in all
> 13: copies or substantial portions of the Software.
> 14: 
> 15: THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> 16: IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> 17: FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> 18: AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> 19: LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> 20: OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> 21: SOFTWARE.

### fcakyon_claude-codex-settings/LICENSE — SPDX identification `Apache-2.0`, 1581 words, 201 lines
`fcakyon_claude-codex-settings/LICENSE:1-201`
> 1:                                  Apache License
> 2:                            Version 2.0, January 2004
> 3:                         http://www.apache.org/licenses/
> 4: 
> 5:    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
> 6: 
> 7:    1. Definitions.
> 8: 
> 9:       "License" shall mean the terms and conditions for use, reproduction,
> 10:       and distribution as defined by Sections 1 through 9 of this document.
> 11: 
> 12:       "Licensor" shall mean the copyright owner or entity authorized by
> 13:       the copyright owner that is granting the License.
> 14: 
> 15:       "Legal Entity" shall mean the union of the acting entity and all
> 16:       other entities that control, are controlled by, or are under common
> 17:       control with that entity. For the purposes of this definition,
> 18:       "control" means (i) the power, direct or indirect, to cause the
> 19:       direction or management of such entity, whether by contract or
> 20:       otherwise, or (ii) ownership of fifty percent (50%) or more of the
> 21:       outstanding shares, or (iii) beneficial ownership of such entity.
> 22: 
> 23:       "You" (or "Your") shall mean an individual or Legal Entity
> 24:       exercising permissions granted by this License.
> 25: 
> 26:       "Source" form shall mean the preferred form for making modifications,
> 27:       including but not limited to software source code, documentation
> 28:       source, and configuration files.
> 29: 
> 30:       "Object" form shall mean any form resulting from mechanical
> 31:       transformation or translation of a Source form, including but
> 32:       not limited to compiled object code, generated documentation,
> 33:       and conversions to other media types.
> 34: 
> 35:       "Work" shall mean the work of authorship, whether in Source or
> 36:       Object form, made available under the License, as indicated by a
> 37:       copyright notice that is included in or attached to the work
> 38:       (an example is provided in the Appendix below).
> 39: 
> 40:       "Derivative Works" shall mean any work, whether in Source or Object
> 41:       form, that is based on (or derived from) the Work and for which the
> 42:       editorial revisions, annotations, elaborations, or other modifications
> 43:       represent, as a whole, an original work of authorship. For the purposes
> 44:       of this License, Derivative Works shall not include works that remain
> 45:       separable from, or merely link (or bind by name) to the interfaces of,
> 46:       the Work and Derivative Works thereof.
> 47: 
> 48:       "Contribution" shall mean any work of authorship, including
> 49:       the original version of the Work and any modifications or additions
> 50:       to that Work or Derivative Works thereof, that is intentionally
> 51:       submitted to Licensor for inclusion in the Work by the copyright owner
> 52:       or by an individual or Legal Entity authorized to submit on behalf of
> 53:       the copyright owner. For the purposes of this definition, "submitted"
> 54:       means any form of electronic, verbal, or written communication sent
> 55:       to the Licensor or its representatives, including but not limited to
> 56:       communication on electronic mailing lists, source code control systems,
> 57:       and issue tracking systems that are managed by, or on behalf of, the
> 58:       Licensor for the purpose of discussing and improving the Work, but
> 59:       excluding communication that is conspicuously marked or otherwise
> 60:       designated in writing by the copyright owner as "Not a Contribution."
> 61: 
> 62:       "Contributor" shall mean Licensor and any individual or Legal Entity
> 63:       on behalf of whom a Contribution has been received by Licensor and
> 64:       subsequently incorporated within the Work.
> 65: 
> 66:    2. Grant of Copyright License. Subject to the terms and conditions of
> 67:       this License, each Contributor hereby grants to You a perpetual,
> 68:       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
> 69:       copyright license to reproduce, prepare Derivative Works of,
> 70:       publicly display, publicly perform, sublicense, and distribute the
> 71:       Work and such Derivative Works in Source or Object form.
> 72: 
> 73:    3. Grant of Patent License. Subject to the terms and conditions of
> 74:       this License, each Contributor hereby grants to You a perpetual,
> 75:       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
> 76:       (except as stated in this section) patent license to make, have made,
> 77:       use, offer to sell, sell, import, and otherwise transfer the Work,
> 78:       where such license applies only to those patent claims licensable
> 79:       by such Contributor that are necessarily infringed by their
> 80:       Contribution(s) alone or by combination of their Contribution(s)
> 81:       with the Work to which such Contribution(s) was submitted. If You
> 82:       institute patent litigation against any entity (including a
> 83:       cross-claim or counterclaim in a lawsuit) alleging that the Work
> 84:       or a Contribution incorporated within the Work constitutes direct
> 85:       or contributory patent infringement, then any patent licenses
> 86:       granted to You under this License for that Work shall terminate
> 87:       as of the date such litigation is filed.
> 88: 
> 89:    4. Redistribution. You may reproduce and distribute copies of the
> 90:       Work or Derivative Works thereof in any medium, with or without
> 91:       modifications, and in Source or Object form, provided that You
> 92:       meet the following conditions:
> 93: 
> 94:       (a) You must give any other recipients of the Work or
> 95:           Derivative Works a copy of this License; and
> 96: 
> 97:       (b) You must cause any modified files to carry prominent notices
> 98:           stating that You changed the files; and
> 99: 
> 100:       (c) You must retain, in the Source form of any Derivative Works
> 101:           that You distribute, all copyright, patent, trademark, and
> 102:           attribution notices from the Source form of the Work,
> 103:           excluding those notices that do not pertain to any part of
> 104:           the Derivative Works; and
> 105: 
> 106:       (d) If the Work includes a "NOTICE" text file as part of its
> 107:           distribution, then any Derivative Works that You distribute must
> 108:           include a readable copy of the attribution notices contained
> 109:           within such NOTICE file, excluding those notices that do not
> 110:           pertain to any part of the Derivative Works, in at least one
> 111:           of the following places: within a NOTICE text file distributed
> 112:           as part of the Derivative Works; within the Source form or
> 113:           documentation, if provided along with the Derivative Works; or,
> 114:           within a display generated by the Derivative Works, if and
> 115:           wherever such third-party notices normally appear. The contents
> 116:           of the NOTICE file are for informational purposes only and
> 117:           do not modify the License. You may add Your own attribution
> 118:           notices within Derivative Works that You distribute, alongside
> 119:           or as an addendum to the NOTICE text from the Work, provided
> 120:           that such additional attribution notices cannot be construed
> 121:           as modifying the License.
> 122: 
> 123:       You may add Your own copyright statement to Your modifications and
> 124:       may provide additional or different license terms and conditions
> 125:       for use, reproduction, or distribution of Your modifications, or
> 126:       for any such Derivative Works as a whole, provided Your use,
> 127:       reproduction, and distribution of the Work otherwise complies with
> 128:       the conditions stated in this License.
> 129: 
> 130:    5. Submission of Contributions. Unless You explicitly state otherwise,
> 131:       any Contribution intentionally submitted for inclusion in the Work
> 132:       by You to the Licensor shall be under the terms and conditions of
> 133:       this License, without any additional terms or conditions.
> 134:       Notwithstanding the above, nothing herein shall supersede or modify
> 135:       the terms of any separate license agreement you may have executed
> 136:       with Licensor regarding such Contributions.
> 137: 
> 138:    6. Trademarks. This License does not grant permission to use the trade
> 139:       names, trademarks, service marks, or product names of the Licensor,
> 140:       except as required for reasonable and customary use in describing the
> 141:       origin of the Work and reproducing the content of the NOTICE file.
> 142: 
> 143:    7. Disclaimer of Warranty. Unless required by applicable law or
> 144:       agreed to in writing, Licensor provides the Work (and each
> 145:       Contributor provides its Contributions) on an "AS IS" BASIS,
> 146:       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
> 147:       implied, including, without limitation, any warranties or conditions
> 148:       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
> 149:       PARTICULAR PURPOSE. You are solely responsible for determining the
> 150:       appropriateness of using or redistributing the Work and assume any
> 151:       risks associated with Your exercise of permissions under this License.
> 152: 
> 153:    8. Limitation of Liability. In no event and under no legal theory,
> 154:       whether in tort (including negligence), contract, or otherwise,
> 155:       unless required by applicable law (such as deliberate and grossly
> 156:       negligent acts) or agreed to in writing, shall any Contributor be
> 157:       liable to You for damages, including any direct, indirect, special,
> 158:       incidental, or consequential damages of any character arising as a
> 159:       result of this License or out of the use or inability to use the
> 160:       Work (including but not limited to damages for loss of goodwill,
> 161:       work stoppage, computer failure or malfunction, or any and all
> 162:       other commercial damages or losses), even if such Contributor
> 163:       has been advised of the possibility of such damages.
> 164: 
> 165:    9. Accepting Warranty or Additional Liability. While redistributing
> 166:       the Work or Derivative Works thereof, You may choose to offer,
> 167:       and charge a fee for, acceptance of support, warranty, indemnity,
> 168:       or other liability obligations and/or rights consistent with this
> 169:       License. However, in accepting such obligations, You may act only
> 170:       on Your own behalf and on Your sole responsibility, not on behalf
> 171:       of any other Contributor, and only if You agree to indemnify,
> 172:       defend, and hold each Contributor harmless for any liability
> 173:       incurred by, or claims asserted against, such Contributor by reason
> 174:       of your accepting any such warranty or additional liability.
> 175: 
> 176:    END OF TERMS AND CONDITIONS
> 177: 
> 178:    APPENDIX: How to apply the Apache License to your work.
> 179: 
> 180:       To apply the Apache License to your work, attach the following
> 181:       boilerplate notice, with the fields enclosed by brackets "[]"
> 182:       replaced with your own identifying information. (Don't include
> 183:       the brackets!)  The text should be enclosed in the appropriate
> 184:       comment syntax for the file format. We also recommend that a
> 185:       file or class name and description of purpose be included on the
> 186:       same "printed page" as the copyright notice for easier
> 187:       identification within third-party archives.
> 188: 
> 189:    Copyright [yyyy] [name of copyright owner]
> 190: 
> 191:    Licensed under the Apache License, Version 2.0 (the "License");
> 192:    you may not use this file except in compliance with the License.
> 193:    You may obtain a copy of the License at
> 194: 
> 195:        http://www.apache.org/licenses/LICENSE-2.0
> 196: 
> 197:    Unless required by applicable law or agreed to in writing, software
> 198:    distributed under the License is distributed on an "AS IS" BASIS,
> 199:    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> 200:    See the License for the specific language governing permissions and
> 201:    limitations under the License.

**Absent:** `obra_the-elements-of-style/LICENSE` and any other license-named file in that repo. Declaration evidence:
`obra_the-elements-of-style/.claude-plugin/plugin.json:9-9`
> 9:   "license": "Public Domain",

`obra_the-elements-of-style/skills/writing-clearly-and-concisely/elements-of-style.md:3-3`
> 3: _Public domain text by William Strunk Jr._

`obra_the-elements-of-style/README.md:58-63`
> 58: The text is public domain. The 1918 edition came from Project Gutenberg, converted to markdown.
> 59: 
> 60: - **Original source**: [Project Gutenberg #37134](https://www.gutenberg.org/files/37134/37134-h/37134-h.htm)
> 61: - **Author**: William Strunk Jr.
> 62: - **Publication**: 1918
> 63: - **License**: Public Domain

**Unknown:** user ELI5 file license/content, because the requested file is absent.

## 5. Verification and remaining work

- **Read-only source integrity:** compared SHA-256 content manifests for **3,238 non-.git files across 11 entire clones** before report production and after it; **0 changed, added, or removed source files**. Also compared all **11 HEAD values and 11 git status outputs**; all unchanged and initially clean. Full-clone hashing includes fcakyon’s unrelated files solely to prove they were untouched; behavioral analysis uses only its six ADHD plugin files and root licensing/registration metadata.
- **Packaging denominator:** recursive behavior-scope enumeration scanned **1,868 files across 11 roots**, selecting **168 relevant instruction/packaging/support files**. Found **33 plugin.json / marketplace.json / hooks.json files** across host adapters, **41 physical SKILL.md files**, **21 output-style files** (20 Smixs + 1 fcakyon), and **11 audited root/historical license files**. The report includes **16 matrix themes across 12 source columns**; U is unknown because absent.
- **Exact quotation check:** programmatically matched **1,155 quoted physical source lines across 294 quote blocks** back to their source files; **0 mismatches**. Checked **695 existing-path citation ranges** against actual file lengths; **0 invalid ranges**. This verifies quotation bytes/text and line bounds, not the correctness of every editorial inference. Matrix shorthand citations are resolved through the primary-path legend and variant-evidence paragraph.
- **Coverage checks:** root Caveman enumeration found **22 skills**, all classified in section 1. Compared **6 distribution mirror pairs**: **5 identical**, **1 different (`caveman-stats`)**. Compared **1 ayghri Cursor mirror pair**: identical. Compared **2 talk-normal prompt mirror pairs and 2 installer mirror pairs**: all identical. No assumption of mirror equality was made from filenames alone.
- **Output constraint:** only immediate non-directory workspace file is `ANALYSIS.md`. No repo builds, tests, installers, hooks, or live routing evaluations were executed (**0 runtime trials**); the verification above is static inspection plus read-only integrity and citation checks.
- **Missing requested source:** `/home/jaime/.claude/output-styles/eli5.md` and its output-styles parent directory were checked and absent. **1 requested user path checked, 0 readable user-style files.** Remaining work is to read that actual file if supplied/made available, then fill U’s findings, overlaps, and conflicts. No other requested repository source remains unreported.

### Clone commits used

- `JuliusBrussee_caveman`: `99aafe151a1be72be783e662858e8a0955add59f`
- `Kyaa-A_eli5`: `75c2fd1859b92c64facc2eac21db6c239c80a3d6`
- `ayghri_i-have-adhd`: `839872f9d1cd634fed642b4589ce7226199cc15f`
- `blader_humanizer`: `225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8`
- `fcakyon_claude-codex-settings`: `a035b4ed0c76b933fa20260e452f3a422b7c0b44`
- `hardikpandya_stop-slop`: `8da1f030185bdfe8471220585162991eaeb970e9`
- `hexiecs_talk-normal`: `d89cf329e775e640181427fae071652198264c7e`
- `obra_the-elements-of-style`: `05fc4f0d2b97b7c042dd9949ad658568e4a1324e`
- `petergyang_no-ai-slop`: `000650b156983f5159695b441477f4e63b25dc85`
- `rahulj51_eli5`: `43055a43a94f5508b74eb3ce31a103c55369aaf2`
- `smixs_awesome-claude-output-styles`: `52bc415c6c1b4b44047fc8c17158e5b85a054261`

Final packaging syntax check: selected **33 packaging JSON files from 1,868 scoped candidates**, parsed all 33 with Python `json.loads`; **33 valid, 0 parse errors**. Re-ran the final artifact quotation/range checks: **1,155 lines / 294 blocks**, **695 ranges**, **0 failures**. This checks JSON syntax only, not host schema compatibility.
