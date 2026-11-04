# Corpus index

Papers whose prose has been distilled into `style-corpus.md`. The raw extracted text of a paper is
never committed (copyright); only short quoted exemplars with a source tag. Keep this table current
when you distill a new paper (see `distill-protocol.md`).

| Tag | Paper | Venue / year | Sections read | Distilled on |
|---|---|---|---|---|
| AF00 | Anderlini and Felli, "Bounded Rationality and Incomplete Contracts" | LSE STICERD DP, 2000 | Abstract, §1 to §6 (definitions, remarks, Proposition 1, intuition) | 2026-11-03 |
| GGS25 | Ghosh, Goswami and Sarkar, "Moral wiggle room in the dictator game" | J. Behav. Exp. Econ., 2025 | Abstract, §1 to §3 | 2026-11-03 |
| CDM11 | Caplin, Dean and Martin, "Search and Satisficing" | AER, 2011 | Abstract, intro, §I to §III | 2026-11-03 |
| CD15 | Caplin and Dean, "Revealed Preference, Rational Inattention, and Costly Information Acquisition" | AER, 2015 | Abstract, intro, §I to §II.A | 2026-11-03 |
| CM15 | Caplin and Martin, "A Testable Theory of Imperfect Perception" | Economic Journal, 2015 | Abstract, intro, §1 incl. Theorem 1 and proof | 2026-11-03 |
| CLR20 | Chambers, Liu and Rehbeck, "Costly information acquisition" | JET, 2020 | Abstract, §1 to §3.1 | 2026-11-03 |
| DEGO26 | Dean, Enke, Graeber and Ortoleva, "Reference Points as Information" | Working paper, March 2026 | Abstract, intro, §2, §3 incl. Proposition 1 | 2026-11-03 |
| EG23 | Enke and Graeber, "Cognitive Uncertainty" | QJE, 2023 | Abstract, intro | 2026-11-03 |
| EGOY24 | Enke, Graeber, Oprea and Yang, "Behavioral Attenuation" | Working paper, Sept 2024 | Abstract, intro, §2 opening | 2026-11-03 |
| DM16 | Dean and Martin, "Measuring Rationality with the Minimum Cost of Revealed Preference Violations" | REStat, 2016 (WP 2015) | Abstract, intro, §2 to §2.1 | 2026-11-03 |
| ENKE-R | Enke, "The Cognitive Turn in Behavioral Economics" | Review, 2024 (rev. May 2026) | Abstract, intro, framework §1 | 2026-11-03 |

Reference document in the corpus voice: the thesis "The Letter as Shelter: How Rules Shape
Information Acquisition" (draft 20.0), whose introduction already follows most of these patterns and
is quoted in `style-corpus.md` as a worked target.

## Adding a paper

1. Extract the text: `python3 scripts/extract_pdf_text.py <paper.pdf> <out.txt>` (keep `out.txt`
   outside the repo or under `corpus/raw/`, which is gitignored).
2. Follow `distill-protocol.md`.
3. Append a row here with a new tag (initials and year), and add exemplars to `style-corpus.md`
   under the section they belong to, each tagged.
4. A pattern that appears in only one paper, once, goes into "Candidates" below until a second
   sighting promotes it.

## Candidates (seen once; not yet in style-corpus.md)

- (none)
