#!/usr/bin/env python3
"""Flashlight for AI writing tells in economics prose (.tex or .md).

Deterministic, offline, no model. It counts patterns per paragraph so an editor knows where to
look. It never outputs an "AI probability"; counts are not verdicts, and every pattern here has
legitimate uses (see references/preserve.md).

Usage:
    python3 detect_tells.py file.tex [--min-hits 2] [--all] [--json]

What it counts per paragraph:
  words     banned or overused words (C1 / F3 / F5 list)
  notbut    "not X but Y" frames (A1)
  riders    trailing -ing riders ", highlighting ..." (C3)
  copula    "serves as / stands as / functions as / represents a" (C5)
  conn      connective openers: Moreover / Furthermore / Additionally / Importantly / Notably (F6, F10)
  boiler    "it is worth noting", "it should be emphasized", ... (F10)
  hedgev    vague hedges: somewhat / relatively / fairly / to some extent / quite (F9)
  dash      em or en dashes used as connectors (B3)
  long      sentences over 35 words (F11)
  runs      runs of 3+ adjacent sentences of about the same length (B5)
  sameopen  3+ consecutive sentences with the same first word (B2)
  triad     "A, B, and C" lists of three single words or short phrases (B1, weak)
"""
import argparse
import json
import re
import sys

BANNED = [
    "delve", "delves", "delving", "underscore", "underscores", "underscoring", "tapestry",
    "landscape", "realm", "journey", "testament", "pivotal", "crucial", "crucially", "intricate",
    "intricacies", "meticulous", "meticulously", "seamless", "seamlessly", "vibrant", "showcase",
    "showcases", "showcasing", "foster", "fosters", "fostering", "harness", "harnesses", "navigate",
    "navigating", "leverage", "leverages", "leveraging", "interplay", "enduring", "garner",
    "bolster", "bolsters", "enhance", "enhances", "paramount", "groundbreaking", "cutting-edge",
    "comprehensive", "extensive", "novel", "multifaceted", "nuanced", "holistic", "transformative",
    "myriad", "plethora", "unprecedented", "noteworthy", "robustly",
]
BANNED_PHRASES = [
    r"in recent years", r"has attracted (increasing|growing|considerable) attention",
    r"to the best of our knowledge", r"for the first time", r"paves? the way", r"sheds? light on",
    r"bridges? the gap", r"opens? new avenues", r"plays? a (key|crucial|pivotal|central) role",
    r"a wide range of", r"it is well known that", r"with the rapid development",
    r"in today'?s", r"at its core", r"the real question is", r"let alone",
]
BOILER = [
    r"it is worth (noting|mentioning|emphasi[sz]ing)", r"it should be (noted|emphasi[sz]ed|stressed)",
    r"it is important to (note|stress|emphasi[sz]e)", r"needless to say", r"as mentioned (above|earlier)",
]
HEDGEV = [r"\bsomewhat\b", r"\brelatively\b", r"\bfairly\b", r"\bto some extent\b", r"\bquite\b", r"\brather\b (?!than)"]
RIDERS = r",\s*(highlighting|underscoring|emphasi[sz]ing|ensuring|reflecting|symboli[sz]ing|contributing to|fostering|showcasing|demonstrating|illustrating)\b"
COPULA = r"\b(serves|serve|stands|stand|functions|function|operates|operate) as\b|\brepresents? an?\b|\bboasts?\b"
NOTBUT = r"\bnot (just|only|merely|simply|so much)\b.{0,80}\bbut\b|\bnot\b[^.;:]{0,60}\bbut rather\b|\bit is not\b[^.;:]{0,60}\bit is\b|\bisn'?t\b[^.;:]{0,60}\bit'?s\b"
CONN = r"^(Moreover|Furthermore|Additionally|Importantly|Notably|Interestingly|Crucially|In addition)\b"
TRIAD = r"\b\w+(?:\s\w+)?,\s\w+(?:\s\w+)?,?\s(?:and|or)\s\w+(?:\s\w+)?\b"


def strip_latex(text: str) -> str:
    # Remove comments, preamble is kept (harmless), display and inline math, common commands.
    text = re.sub(r"(?<!\\)%.*", "", text)
    text = re.sub(r"\\begin\{(equation|align|gather|multline|eqnarray|cases|array|tikzpicture|tabular|table|figure)\*?\}.*?\\end\{\1\*?\}", " [MATH] ", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", " [MATH] ", text, flags=re.S)
    text = re.sub(r"\$\$.*?\$\$", " [MATH] ", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", " [MATH] ", text, flags=re.S)
    text = re.sub(r"(?<!\\)\$[^$]*\$", " [MATH] ", text)
    text = re.sub(r"\\(cite[tp]?|ref|eqref|label|autoref|cref|Cref|input|include|bibliography|bibliographystyle|usepackage|documentclass|newcommand|renewcommand|def|DeclareMathOperator)\*?(\[[^\]]*\])?\{[^}]*\}", " [REF] ", text)
    text = re.sub(r"\\(section|subsection|subsubsection|paragraph|chapter)\*?\{([^}]*)\}", r"\n\n\2\n\n", text)
    text = re.sub(r"\\(emph|textit|textbf|textsc|underline|enquote)\{([^}]*)\}", r"\2", text)
    text = re.sub(r"\\footnote\{", " (", text)
    text = re.sub(r"\\begin\{[^}]*\}(\[[^\]]*\])?|\\end\{[^}]*\}", "\n\n", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(\[[^\]]*\])?(\{[^}]*\})?", " ", text)
    text = text.replace("~", " ").replace("``", '"').replace("''", '"')
    text = re.sub(r"[{}]", "", text)
    return text


def paragraphs(text: str):
    for block in re.split(r"\n\s*\n", text):
        block = " ".join(block.split())
        if len(block.split()) >= 25:
            yield block


def sentences(par: str):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[\"'])", par)
    return [p for p in parts if len(p.split()) >= 3]


def analyze(par: str) -> dict:
    low = par.lower()
    sents = sentences(par)
    lens = [len(s.split()) for s in sents]
    hits = {}
    words = sum(len(re.findall(rf"\b{re.escape(w)}\b", low)) for w in BANNED)
    words += sum(len(re.findall(p, low)) for p in BANNED_PHRASES)
    hits["words"] = words
    hits["notbut"] = len(re.findall(NOTBUT, low))
    hits["riders"] = len(re.findall(RIDERS, low))
    hits["copula"] = len(re.findall(COPULA, low))
    hits["conn"] = sum(1 for s in sents if re.match(CONN, s))
    hits["boiler"] = sum(len(re.findall(p, low)) for p in BOILER)
    hits["hedgev"] = sum(len(re.findall(p, low)) for p in HEDGEV)
    hits["dash"] = len(re.findall(r"\s[—–]\s|—|\s--\s", par))
    hits["long"] = sum(1 for n in lens if n > 35)
    runs = 0
    i = 0
    while i + 2 < len(lens):
        a, b, c = lens[i], lens[i + 1], lens[i + 2]
        m = max(a, b, c)
        if m > 0 and (m - min(a, b, c)) / m <= 0.2:
            runs += 1
            i += 3
        else:
            i += 1
    hits["runs"] = runs
    firsts = [re.sub(r"\W", "", s.split()[0]).lower() for s in sents if s.split()]
    same = 0
    for i in range(len(firsts) - 2):
        if firsts[i] == firsts[i + 1] == firsts[i + 2] and firsts[i] not in ("the", "a", "an", "we", "if", "in"):
            same += 1
    hits["sameopen"] = same
    hits["triad"] = len(re.findall(TRIAD, par))
    weighted = (words + hits["notbut"] * 2 + hits["riders"] * 2 + hits["copula"] + hits["conn"]
                + hits["boiler"] * 2 + hits["hedgev"] + hits["dash"] + hits["long"] + hits["runs"]
                + hits["sameopen"] + 0.5 * hits["triad"])
    return {"hits": hits, "score": round(weighted, 1), "sentences": len(sents),
            "mean_len": round(sum(lens) / len(lens), 1) if lens else 0.0, "snippet": par[:90]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--min-hits", type=float, default=2.0, help="report paragraphs with weighted hits >= this (default 2)")
    ap.add_argument("--all", action="store_true", help="report every paragraph")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    raw = open(args.file, encoding="utf-8", errors="replace").read()
    text = strip_latex(raw) if args.file.endswith(".tex") else raw
    results = [analyze(p) for p in paragraphs(text)]
    totals = {}
    for r in results:
        for k, v in r["hits"].items():
            totals[k] = totals.get(k, 0) + v
    flagged = [r for r in results if args.all or r["score"] >= args.min_hits]
    if args.json:
        print(json.dumps({"paragraphs": len(results), "totals": totals, "flagged": flagged}, indent=1))
        return 0
    if args.all:
        print(f"{args.file}: {len(results)} paragraphs scanned, all shown")
    else:
        print(f"{args.file}: {len(results)} paragraphs scanned, {len(flagged)} flagged (weighted hits >= {args.min_hits})")
    print("totals: " + ", ".join(f"{k}={v}" for k, v in totals.items()))
    print("note: counts point at paragraphs to read; they are not verdicts (see references/preserve.md)\n")
    for i, r in enumerate(flagged, 1):
        nz = ", ".join(f"{k}={v}" for k, v in r["hits"].items() if v)
        print(f"[{r['score']:>4}] {r['sentences']} sent, mean {r['mean_len']} w | {nz}")
        print(f"       {r['snippet']}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
