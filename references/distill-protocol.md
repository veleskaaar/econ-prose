# Distill protocol: adding a paper's voice to the corpus

Adapted from alchaincyf/nuwa-skill's extraction framework (capture HOW they write, not WHAT they
said; a pattern counts only when it recurs; record what the corpus cannot do) and applied to prose
style rather than a person's thinking.

## 0. Scope

Distill **sentence-level and paragraph-level habits**: openers, paragraph architecture, recurring
sentence frames, model-section conventions, how results are described, lexicon, punctuation. Do not
distill the paper's content, model, or results. Do not copy more than a sentence or two of any
passage; exemplars are quotations for study.

## 1. Read

1. Extract text with `scripts/extract_pdf_text.py`. Read the abstract, the whole introduction, the
   model or design section, and one results section with a formal statement and its discussion.
   For a theory paper also read one proof sketch in prose.
2. While reading, mark every sentence that does one of these jobs:
   - opens a section or the paper (§1 of style-corpus);
   - states the contribution or the main result (§1.4, §1.5);
   - gives intuition after a formal statement (§2.3);
   - asks a question and answers it (§3.1);
   - names a concept, declares agnosticism, states what a result does not say (§3.2, §3.3, §3.5);
   - motivates a definition or interprets a formula (§4.2, §4.3);
   - positions the paper against one other paper (§3.9);
   - reports a magnitude or marks an interpretation (§5.2, §5.3).

## 2. Extract, with the recurrence test

A sentence frame becomes a **pattern** only if it passes one of:
- **Cross-section recurrence:** it appears in at least two sections of the paper (intro and model;
  model and results).
- **Cross-paper recurrence:** it matches a pattern already in `style-corpus.md` from another paper.
  Then add the new exemplar under that pattern.

A frame seen once goes to "Candidates" in `corpus-index.md`. A frame that appears in every paragraph
is a mannerism, not a pattern; record it in `preserve.md` under the author's habits with a "once per
paper" limit.

For each pattern record: the frame in abstract form ("Question, then the answer in the next
sentence"), two or more exemplars with tags, and the limit ("at most one per section").

## 3. Measure the fingerprint (quick, on 20 paragraphs)

| Dimension | How |
|---|---|
| Topic-sentence length | words in the first sentence of each paragraph (the corpus: 5 to 12) |
| Support-sentence length | words in the longest sentence of each paragraph (the corpus: 25 to 40) |
| Question share | questions per 100 sentences |
| Connective openers | Moreover / Furthermore / However / Thus per 100 sentences |
| Hedge share | may / might / suggests / appears per 100 sentences |
| First person | "we" per 100 sentences |
| Dash and parenthesis policy | which the paper uses for asides |
| Enumeration style | (i)(ii)(iii), First/Second, or lists |

Record the numbers in `corpus-index.md` only if they differ from the corpus's band; otherwise write
"in band".

## 4. Record what the paper never does

Add to style-corpus §8 anything the paper conspicuously avoids that AI drafts do (openers, filler
words, closers). This is the most useful part for editing.

## 5. Update

- `style-corpus.md`: new exemplars under existing patterns; new patterns only after the recurrence
  test; the §8 never-list.
- `corpus-index.md`: a row for the paper; candidates.
- `preserve.md`: any author habit that a ban list would wrongly flag.
- Bump `metadata.version` in `SKILL.md` and add a line to `CHANGELOG.md`.

## 6. Honest boundaries

- The corpus is behavioral and decision theory in top general-interest and field journals. It is
  not a guide to empirical IO, macro, or econometrics prose.
- Exemplars show habits, not a template; a paper that used every pattern in every section would read
  as parody. The limits in each pattern are part of the pattern.
- Extracted PDF text can garble ligatures ("ﬁ") and drop spaces; verify a quotation against the
  PDF before recording it.

## 7. Fidelity check (optional, before a release)

Blind test: give a fresh agent one paragraph polished by this skill and one from a corpus paper,
with names removed, and ask which was written by the paper's authors. The skill is in band when the
agent cannot tell at better than chance across five pairs. Never let the editing agent grade its own
output.
