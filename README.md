# econ-prose

A Claude Code skill for **language-only** polishing of economics theory prose, in the voice of a
distilled corpus of behavioral and decision-theory papers (Caplin, Dean, Martin, Enke, Graeber,
Ortoleva, Chambers, Liu, Rehbeck, Anderlini, Felli, ...). It removes AI writing tells without
casualizing, keeps every claim, symbol, number, citation and LaTeX command intact, and edits toward
the corpus's sentence habits rather than toward a generic "human" voice.

一个只改语言、不改内容的经济学论文润色 skill。目标不是"像人写的"，而是像 Caplin、Dean、Enke、
Anderlini–Felli 这一类论文写的：平叙开篇、先断言后解释、定理后一句直觉、自问自答、公式后一句解读。
去 AI 味但不口语化，数学、引用、定理陈述、数字一律不动。

## Lineage

| Source | What was taken | License |
|---|---|---|
| [blader/humanizer](https://github.com/blader/humanizer) | the 25-pattern tell catalog (staging, rhythm by rule, inflation, formatting, leftovers), the "keep what it says" rule | MIT |
| [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) | the phrase and structure lists, the quick checks | MIT |
| [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | the academic layer: over-claiming verbs, significance hype, novelty padding, connective stacking, the "preserve" discipline | MIT |
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | two-stage review-then-fix, replace 74 / delete 18 / insert 8, the deletion and reversion tests, the false-positive whitelist, "aim at the band, not the opposite pole" | MIT |
| [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | the distillation method: capture how they write, a pattern counts only when it recurs, record honest boundaries, never self-grade | see repo |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | the principle: decisions anchored in real references beat defaults; look at what you made | MIT |

What is new here: the economics register filter (`references/preserve.md`), the LaTeX rules, the
distilled style corpus with tagged exemplars, the distill protocol for adding papers, and the
offline tell scanner.

## Install

```bash
git clone git@github.com:veleskaaar/econ-prose.git ~/.claude/skills/econ-prose
```

Claude Code picks up `~/.claude/skills/econ-prose/SKILL.md` automatically. For a single project,
clone into `<project>/.claude/skills/econ-prose` instead.

## Use

- "用 econ-prose 润色第 3 节" / "polish section 3 with econ-prose" → **polish** (default): minimal
  in-place edits plus a report and a change log.
- "review the abstract for AI tells" → **review**: diagnosis only, no edits.
- "rewrite this paragraph in the corpus voice" → **rewrite** of the named span only.
- "蒸馏这篇论文的风格" with a PDF → **distill**: adds the paper's habits to the corpus.

Flashlight (optional, offline, no model):

```bash
python3 ~/.claude/skills/econ-prose/scripts/detect_tells.py draft.tex
```

It prints per-paragraph counts of banned words, "not X but Y" frames, -ing riders, connective
openers, dashes, overlong sentences and runs of same-length sentences. It never outputs an AI
probability; the counts tell the editor where to read first.

For a model-based score, `scripts/model_detect.py` runs the ICLR'24 detector of
[YuchuanTian/AIGC_text_detector](https://github.com/YuchuanTian/AIGC_text_detector) offline (one-time
500 MB download from Hugging Face; needs torch and transformers) and reports a token-weighted P(AI)
per paragraph and for the document, with `--calibrate` scoring two control texts. The offline toolbox
[Gx664/AIGC](https://github.com/Gx664/AIGC) is another option. The skill never optimizes against these
scores: they drift across detector versions, and genuine top-journal paragraphs score as AI.

## Add a paper to the corpus

```bash
python3 scripts/extract_pdf_text.py paper.pdf corpus/raw/paper.txt   # corpus/raw is gitignored
```

then follow `references/distill-protocol.md` and update `references/corpus-index.md`.

## Files

```
SKILL.md                       the skill: rules, operations, the run, report format
references/style-corpus.md     the distilled voice, with tagged exemplars
references/corpus-index.md     which papers, what was read, when
references/ai-tells.md         merged tell catalog, filtered for economics
references/preserve.md         what a generic humanizer would flip and this skill keeps
references/latex-rules.md      protected spans and safe mechanics for .tex
references/distill-protocol.md how to add a paper
references/examples.md         before / after pairs
scripts/detect_tells.py        offline pattern counter
scripts/model_detect.py        optional offline model detector (RoBERTa, ICLR'24)
scripts/extract_pdf_text.py    PDF to text
```

## License

MIT for this repository's own text and code. Quoted exemplars in `references/style-corpus.md` are
short excerpts from published papers, cited by source tag, used for study.
