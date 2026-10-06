---
name: ste
description: "Explicitly requested Simplified Technical English for specified technical content. Load only on explicit request or when the communication-stack router selects it."
---

# ASD-STE100

<!-- Adapted from rahulj51/eli5 (MIT); reviewed base 43055a43a94f5508b74eb3ce31a103c55369aaf2. Task scope and conflict rulings changed. -->

## Context contract

Preserve required facts, conditions, risks, and genuine uncertainty.
Keep protected code, commands, paths, identifiers, data, errors, and quotations exact.
An explicit task may authorize changing engineering artifacts; speaking style cannot.
This explicitly requested STE transformation uses English. Follow the requested audience, structure, and output contract.
Presentation limits yield to requested coverage and necessary substance.
Chat profiles do not override the voice or conventions of a requested artifact.
In chat, start with the requested answer and end on the same requested goal.
Give a next action only when needed; omit redundant recap and hypothetical offers.
Writer samples, meaningful existing voice, and useful punctuation outrank pattern defaults.
These instructions apply only to the current requested transformation or artifact.
They do not establish a session-wide mode or govern later unrelated tasks.
The context contract and explicit rules outrank conflicting illustrative examples.

Write the answer only in ASD-STE100 Simplified Technical English (STE). Do not use a different plain-language standard or add separate style rules.

Use the ASD-STE100 Issue 9 rules in this skill for normal requests. Do not search the web to confirm these rules.

Search for the official standard only when the user asks for one of these results:

- Verification against the latest official issue.
- An exact controlled dictionary check.
- A formal ASD-STE100 compliance check.

For these checks, get the current official standard from [asd-ste100.org](https://www.asd-ste100.org/).

## Method

1. Keep the meaning, facts, risks, limits, names, and necessary actions from the source.
2. Identify each part as procedural writing or descriptive writing. An answer can contain both types. Use descriptive writing for text that does not give work steps.
3. Rewrite the text with the STE writing rules and the STE dictionary.
4. Check the result against the requirements below before you give the answer.

## STE requirements

- Use only words that the STE dictionary approves, or words that qualify as technical nouns or technical verbs.
- Use each approved word only with its approved meaning, part of speech, and form.
- Use one term for one meaning. Use the same term each time.
- Use American English spelling, unless an applicable official directive requires different spelling.
- Use multi-word nouns of three words or fewer. If an official technical noun is longer, write it in full first and make its meaning clear.
- Use only the infinitive, imperative, simple present, simple past, simple future, and past participle as an adjective.
- Do not use an `-ing` form unless it is a technical noun or a modifier in a technical noun.
- Use the active voice. In descriptive writing, use the passive voice only when the agent is unknown.
- Do not use complex auxiliary verb constructions or phrasal verbs.
- Use a verb, not a noun, to state an action when the dictionary approves that verb.
- Write complete, short, clear sentences. Do not omit words. Do not use contractions.
- Use a vertical list when it makes complex text easier to understand.
- Use articles and demonstrative adjectives when they are applicable.
- Do not use a semicolon.

For procedural writing:

- Use a maximum of 20 words in each sentence.
- Give one instruction in each sentence. Give two actions only when they occur at the same time.
- Write instructions in the imperative form.
- Put a necessary condition before the command and divide it from the command with a comma.
- Use notes only for information, not instructions.

For descriptive writing:

- Use a maximum of 25 words in each sentence.
- Give information gradually and in a logical sequence.
- Keep one topic in each paragraph.
- Use no more than six sentences in each paragraph.
- Do not use the imperative form.

For safety instructions:

- Identify the risk level with the applicable word, such as `WARNING` or `CAUTION`.
- Start with a clear command or condition.
- Explain the risk or possible result.

## Protected text

Do not change code, commands, file paths, URLs, identifiers, data, or text that the user requires verbatim. Use necessary product and subject terms only when they qualify as STE technical nouns or technical verbs. Clearly separate protected text from the STE text.

## Compliance

Do not claim formal ASD-STE100 compliance for a normal request. Do not add a compliance disclaimer unless the user asks about compliance.

For a requested compliance check, check every word and sentence against the applicable official standard. State clearly when you cannot complete a controlled dictionary check.

## Example

Before:

> The migration failed because the reconciler's idempotency check compares the resource hash against the previously persisted state snapshot, but the snapshot serialization was changed in #4123 to exclude default-valued fields, so hashes no longer match and every resource is treated as drifted, triggering a full re-apply which exceeds the API rate limits.

After:

> A change from last month caused the migration failure. The data did not cause the failure. The change modified how the system saves state. Thus, the system identifies all resources as changed. The system tried to apply all resources again and reached the rate limit. Regenerate the saved state. Then, start the migration again.
