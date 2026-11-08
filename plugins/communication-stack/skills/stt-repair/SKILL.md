---
name: stt-repair
description: Use when the user's message looks like speech-to-text (dictation) output - brand, product or tool names that came out as ordinary words ("Performance" for IVT Portfolio, "Ambima 5" for ANBIMA XML5), words that do not fit the sentence, wrong word boundaries, numbers or acronyms spelled by sound, missing punctuation - or when the user says "isso veio de ditado", "o speech to text errou", "não era isso que eu falei", or calls /stt-repair. Repairs the intent from a glossary and context, corrects when sure, and asks one short question when not.
---

# Speech-to-text repair

Goal: understand what the user meant to say, not what the transcriber wrote.
Never guess silently on anything that decides an action.

## 1. Is it really dictation?

Act only when at least two signals show up: a name or acronym spelled like
common words, a word that breaks the sentence, odd word boundaries ("flow
atômico"), a number or version said as a word, no punctuation with spoken
fillers. A plain typo is not dictation; fix it quietly and move on.

## 2. Mark the suspect spans

List the fragments that may be wrong: product, tool, repo, person and customer
names, acronyms, versions, file or command names. Ignore fragments that read
fine and do not change what you will do.

## 3. Find candidates (look up, do not invent)

Read the glossary only now, not before: first `.claude/stt-glossary.md` in the
project, then `~/.claude/stt-glossary.md`. Each row maps what the transcriber
wrote to what was meant. Candidates come only from these sources:

1. A glossary alias that matches the fragment.
2. A glossary term that sounds like the fragment when said aloud in Portuguese
   (compare by sound, not by spelling: loanwords, spelled letters and digits
   often look nothing alike).
3. Names already present in the session or the repo: file, package, ticket
   prefix, earlier turns.

Take only a few best candidates per span. Never load the whole glossary into
the answer, and never invent a name that none of these sources contains.

## 4. Decide per span

- **One candidate backed by an alias, or by the glossary plus context:**
  correct it and show it in one line before acting ("Li 'Performance' como
  IVT Portfolio.").
- **Several candidates, or one with no support:** ask (step 5).
- **The span picks a target of something destructive or outward** (which
  repo, environment, customer, what to delete or send): ask even if you are
  fairly sure.

When in doubt, ask. Models tend to answer confidently instead of asking, and
they also over-correct and invent names, so the rule is: few questions, and
only where the answer changes what you do.

## 5. Ask well

One message, at most three spans, in order of impact. For each span quote what
you read and give two or three options from the candidates, plus "outro".
Example: *Você disse "Ambima 5": é ANBIMA XML5, ANBIMA XML4 ou outra coisa?*
Use the question tool when the session has one. Do not ask about spans that
do not change the work.

## 6. Learn

After the user confirms a correction that is not in the glossary, offer one
ready row to add and say which file. Write it only if the user agrees.
Glossary format and examples: `glossary.example.md` in this folder.

## 7. Then do the task

State the repaired request in one line, then continue the work. Repairing is a
means; do not turn the answer into an essay about transcription.

Why these rules, with sources: `references/research.md`.
