---
name: eli5
description: "Plain-language or executive version of specified content for the current task. Preserve necessary facts and qualifications. Load only on explicit request or when the communication-stack router selects it."
---

# eli5

<!-- Adapted from rahulj51/eli5 (MIT); reviewed base 43055a43a94f5508b74eb3ce31a103c55369aaf2. Task scope and conflict rulings changed. -->

## Context contract

Preserve required facts, conditions, risks, and genuine uncertainty.
Keep protected code, commands, paths, identifiers, data, errors, and quotations exact.
An explicit task may authorize changing engineering artifacts; speaking style cannot.
Follow the requested language, audience, structure, and output contract.
Presentation limits yield to requested coverage and necessary substance.
Chat profiles do not override the voice or conventions of a requested artifact.
In chat, start with the requested answer and end on the same requested goal.
Give a next action only when needed; omit redundant recap and hypothetical offers.
Writer samples, meaningful existing voice, and useful punctuation outrank pattern defaults.
These instructions apply only to the current requested transformation or artifact.
They do not establish a session-wide mode or govern later unrelated tasks.
The context contract and explicit rules outrank conflicting illustrative examples.

"eli5" here does not mean explaining to a literal five-year-old. It means explaining to a busy executive, like a CTO or CPO: someone smart who has no time and may not know the technical details.

## When this applies

Use for an explicit current-task simplification or executive-summary request about specified content. A quoted mention of eli5 or an unrelated heading is not a mode change.

## Style rules

- Use the requested reply language; default to English when context supplies no other language. Prefer short, common words.
- Be concise. Cut every word that does not add meaning.
- Lead with the point. The first sentence gives the bottom line.
- Prefer single-level lists and short items. Keep meaningful hierarchy, requested depth, and necessary coverage.
- Avoid jargon. If a technical term is unavoidable, explain it in a few plain words the first time it appears.
- Write complete sentences. Do not compress into fragments, abbreviations, or arrow chains.
- Keep paragraphs short: one to three sentences.
- Use headings only when the content is long enough to need them.
- No emojis.

## What to keep

- The conclusion or decision. That is the whole point.
- Anything the reader must act on: risks, costs, deadlines, open questions.
- In a requested summary, omit only details outside its required scope. Preserve every required fact and retained protected value exactly.
- Accuracy. Simple must not become wrong. If a simplification loses an important caveat, keep the caveat in one short sentence.

## Output shape

- A short question gets one to three plain sentences. No headers, no list.
- Longer content starts with its main point, then uses the structure requested or needed for clarity.
- Aim for a short read. Reading-time and length targets yield to requested coverage and necessary substance.

## Example

Before:

> The migration failed because the reconciler's idempotency check compares the resource hash against the previously persisted state snapshot, but the snapshot serialization was changed in #4123 to exclude default-valued fields, so hashes no longer match and every resource is treated as drifted, triggering a full re-apply which exceeds the API rate limits.

After:

> The migration failed because of a change we made last month, not bad data. A recent PR changed how we save state, so the system now thinks every resource changed. It tried to re-apply everything at once and hit rate limits. Fix: regenerate the saved state once, then re-run.
