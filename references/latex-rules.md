# LaTeX rules: protected spans and safe mechanics

## Protected spans (never edited by this skill)

- Inline and display math: `$...$`, `\(...\)`, `\[...\]`, `equation`, `equation*`, `align`,
  `align*`, `gather`, `multline`, `cases`, `array`, `tikzpicture`, `tabular` cells with math.
- Commands and their arguments: `\cite`, `\citet`, `\citep`, `\ref`, `\eqref`, `\label`,
  `\footnote{...}` *content may be edited as prose*, but the command stays; `\section{}`,
  `\subsection{}`, `\paragraph{}` *titles may be edited only if asked*; `\newcommand`, `\def`,
  preamble, `\begin{...}`/`\end{...}` lines.
- Theorem-like statements (`theorem`, `lemma`, `proposition`, `corollary`, `definition`,
  `assumption`, `remark` environments): the mathematical content is frozen. Prose inside them may be
  clarified only when the quantifiers, conditions and conclusions stay identical, word by word where
  they are formal ("for every", "there exists", "if and only if", "strictly", "weakly").
- Proof steps: the logical chain is frozen. Connectives may be clarified ("Hence" for "So we get").
- Numbers, parameter values, running-example figures ("0.13 under permission and 0.09 under
  silence"), dates, names, acronyms, cross-references ("Section~\ref{sec:agent}").
- Comments (`% ...`): leave them, including commented-out text.
- Non-breaking ties (`Section~\ref`, `Figure~1`): keep the tie.

## Safe mechanics

- Edit the `.tex` source in place with minimal diffs. One sentence per edit where possible, so the
  author can review each change in `git diff`.
- Never reflow or re-wrap lines the author did not touch; keep the file's line-breaking habit.
- Keep `\emph{}` on defined terms at first use; do not add or remove emphasis elsewhere.
- Keep the document's quote style (`` ``...'' `` or `\enquote{}`), its dash policy, and its
  spelling (the thesis: American; "behavior", "modeling", "organization").
- When splitting a sentence that ends in a display equation, keep the equation attached to the
  clause that introduces it; the sentence after the display starts with its interpretation.
- After editing, check balance: every `\begin{x}` has its `\end{x}`, braces match, no `$` left
  unpaired. If a toolchain exists (`latexmk`, `pdflatex`, `tectonic`), compile and report the
  result; otherwise say the compile check was not run.
- Do not touch `.bib` files, figures, or `\input`/`\include` targets unless they were named.

## What counts as prose

Everything outside the protected spans: abstract, introduction, literature, the sentences around
definitions and formulas, the intuition paragraphs, the conclusion, footnote text, captions (if
asked). Captions and titles are edited only when the user names them.
