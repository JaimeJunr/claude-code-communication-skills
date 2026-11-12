# Research behind stt-repair

Sources found by web search on 2026-11-08; method details come from search
snippets and abstracts, so read the papers before quoting numbers.

- **Correct from candidates, not from nothing.**
  [HyPoradise (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6492267465a7ac507be1f9fd1174e78d-Abstract.html)
  builds an open benchmark where an LLM corrects speech recognition output from
  its N-best hypotheses. Here we have only one transcript, so the glossary and
  the session context play the role of the candidate list.
- **Phonetic matching plus local context.**
  [He et al., arXiv 2506.10779](https://arxiv.org/html/2506.10779v1) finds
  phonetically similar entities with Double Metaphone and gives the filtered
  candidates and local context to an LLM. This is step 3.
- **Retrieve a few candidates, not the whole database.** A voice-assistant
  study (Lei et al., 2024) detects entities first and retrieves similar entries
  from a personal database, reporting large named-entity error reductions
  without putting the full database in the prompt.
- **Spelling similarity is not enough.**
  [Luo et al., arXiv 2508.20700](https://web3.arxiv.org/pdf/2508.20700) argues
  that edit-distance and phonetic retrieval fail when the written form is far
  from the sound (loanwords, digits). Hence the alias column and the
  "compare by sound" rule.
- **Rewriting text over-corrects.**
  [LOGIC, arXiv 2601.15397](https://arxiv.org/html/2601.15397v1) notes that
  text-level LLM rewriting tends to over-correct and invent entities never
  spoken. Hence: candidates only from the glossary, the session or the repo.
- **Ask when it is really ambiguous, and only then.**
  [CLAM (arXiv 2212.07769)](https://arxiv.org/abs/2212.07769),
  [Zhang et al., ICLR 2025 (arXiv 2410.13788)](https://arxiv.org/abs/2410.13788v2)
  and [Clarify When Necessary (arXiv 2311.09469)](https://ar5iv.labs.arxiv.org/html/2311.09469)
  show that models often answer confidently instead of asking, and that the
  hard part is deciding when a question is worth it. Hence the confidence
  rule in step 4 and the limit of three short questions.
