---
name: communication-stack
description: Use when asked to edit publishable prose, remove AI writing patterns, simplify a specific explanation, or apply explicit action-first formatting or a brevity pass. Also use when the reader signals a state - confused ("não entendi", "não tô conseguindo entender"), tired or overloaded ("tô cansado", "cabeça cheia"), or lost context after a break ("é outro dia", "perdi o que fizemos"). Select one fixed action for the current task.
---

# Communication Stack router

Use one recipe for the requested transformation. Ordinary chat uses the selected
output style; do not load source recipes for routine answers or engineering work.

## Pick one recipe

| Request | Primary recipe | File inside its plugin |
|---|---|---|
| Edit a supplied draft while keeping my voice | `no-ai-slop:no-ai-slop` | `skills/no-ai-slop/SKILL.md` |
| Substantially rewrite AI-sounding prose | `humanizer:humanizer` | `skills/humanizer/SKILL.md` |
| Audit writing patterns without rewriting | `no-ai-slop:no-ai-slop`, detect mode | `skills/no-ai-slop/SKILL.md` |
| Give a plain-language or executive version of specified content | `eli5-ste:eli5` | `skills/eli5/SKILL.md` |
| Use Simplified Technical English / ASD-STE100-style writing | `eli5-ste:ste` | `skills/ste/SKILL.md` |
| Explicit action-first formatting for this task | `i-have-adhd:i-have-adhd` | `skills/i-have-adhd/SKILL.md` |
| Explicit brevity pass for this task | `caveman:caveman` | `skills/caveman/SKILL.md` |

## Reader state

When the message is about how the reader feels, not a text to edit, the action
is fixed. Do not pick another recipe.

| State | Action |
|---|---|
| Confused ("não entendi", "não tô conseguindo entender") | `eli5-ste:eli5` on your last answer: re-explain the same point in plainer words, one analogy at most, nothing new |
| Tired or overloaded ("tô cansado", "cabeça cheia") | `i-have-adhd:i-have-adhd`: only what matters now, at most 5 lines, one next action |
| Lost context ("é outro dia", "perdi o que fizemos") | no recipe: recap from this conversation in four lines: goal, done, where it stopped, next step |

Mixed signals: Lost context, then confused, then tired. Handle only the first
that applies; the recap is already short and plain.

A requested source wins over the default. Never chain editors automatically.
The selected recipe performs its own supported review. Keep `eval.md` beside
no-ai-slop's recipe and read it only for its edit review.

Invoke the chosen skill via the Skill tool using its namespaced name above;
load only that one skill. Never invoke more than one editor per task.
If it is not installed, say so and give `/plugin install <name>@communication-stack`.
Do not substitute another source silently.

## Precedence in three contexts

Apply these within Claude Code's normal instruction hierarchy. Accuracy,
required content, and exactness remain constraints.

1. **Chat:** current user request, language, and output contract → current-task
   recipe → selected output style → generic brevity defaults.
2. **Publishable prose:** user brief, audience, and output contract → writer
   sample and existing author voice → one selected editor → editor defaults.
   Chat persona rules do not control the artifact.
3. **Machine text:** required schema, project syntax, and verbatim contract →
   project conventions for new content. Speaking style affects surrounding
   prose only.

Keep existing code, comments, commit messages, commands, paths, identifiers,
errors, data, and quotations exact during a communication-only transformation,
including protected spans inside prose. An explicit engineering task may
authorize artifact changes; speaking style cannot. A summary may omit only
details outside its requested scope; retained protected values stay exact.

## Scope and finish

Recipes govern this task or artifact only. They do not switch the selected
output style or govern later unrelated tasks, even while their text remains
in conversation context. A quoted skill name is not activation.

Preserve required facts, caveats, conditions, risks, and honest uncertainty.
Length, item-count, and reading-time preferences yield to necessary or requested
coverage. Keep readable grammar, useful punctuation, and meaningful author
asides. Return final text once; critique, intermediate drafts, or edit notes
require a request. Detect mode returns findings without rewriting or guessing
authorship.

In chat, give the requested answer first and end on the same goal. Report changed
state; use one step indicator only when it helps ongoing work. Give a next action
only when needed. Avoid redundant recaps and hypothetical offers. Harness
progress and verification requirements still apply.

Read [references/conflicts.md](references/conflicts.md) when source defaults
disagree. Its rulings and this context contract outrank conflicting examples.
