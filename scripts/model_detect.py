#!/usr/bin/env python3
"""Optional model-based AI-text detector, run fully offline after a one-time model download.

Usage: python3 model_detect.py file.tex [--model yuchuantian/AIGC_detector_env3] [--ai-label 1]
                                        [--max-tokens 510] [--json] [--calibrate]

Uses the ICLR'24 "Multiscale Positive-Unlabeled" English detector (RoBERTa-based) from Hugging
Face. Needs torch and transformers. The paper's text never leaves the machine. Label 1 is the
AI class (the authors' dataset.py maps the ChatGPT corpus to label 1), checked on 2026-11-03 with
control texts: Anderlini-Felli and Enke-Graeber paragraphs score 0.001, Reddit and Wikipedia
paragraphs 0.09, a synthetic slop paragraph 1.0; but a Caplin-Dean and a Dean-Enke-Graeber-Ortoleva
paragraph also score 0.999, so formal academic prose does draw false positives.

Output: per paragraph P(AI) on each <=510-token window, the document-level average weighted by
window length, and the share of paragraphs above 0.5. These are one detector's scores on one
release and drift across versions; formal academic prose draws false positives. Do not edit
toward this number (see SKILL.md, hard rule 6).
"""
import argparse, json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from detect_tells import strip_latex, paragraphs  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--model", default="yuchuantian/AIGC_detector_env3")
    ap.add_argument("--ai-label", type=int, default=1, help="index of the AI class in the model's output (default 1)")
    ap.add_argument("--max-tokens", type=int, default=510)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--calibrate", action="store_true", help="also score two built-in control texts")
    args = ap.parse_args()
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    tok = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForSequenceClassification.from_pretrained(args.model).eval()

    def score(text):
        ids = tok(text, add_special_tokens=False)["input_ids"]
        out = []
        for i in range(0, max(len(ids), 1), args.max_tokens):
            chunk = ids[i:i + args.max_tokens]
            if len(chunk) < 20 and out:
                break
            inp = torch.tensor([[tok.cls_token_id] + chunk + [tok.sep_token_id]])
            with torch.no_grad():
                p = torch.softmax(model(input_ids=inp).logits, -1)[0]
            out.append((len(chunk), float(p[args.ai_label])))
        return out

    raw = open(args.file, encoding="utf-8", errors="replace").read()
    text = strip_latex(raw) if args.file.endswith(".tex") else raw
    pars = list(paragraphs(text))
    rows = []
    for p in pars:
        w = score(p)
        n = sum(a for a, _ in w)
        rows.append({"tokens": n, "p_ai": round(sum(a * b for a, b in w) / n, 3), "snippet": p[:80]})
    tot = sum(r["tokens"] for r in rows)
    doc = sum(r["tokens"] * r["p_ai"] for r in rows) / tot if tot else 0.0
    share = sum(r["p_ai"] > 0.5 for r in rows) / len(rows) if rows else 0.0
    summary = {"model": args.model, "paragraphs": len(rows), "tokens": tot,
               "doc_p_ai_token_weighted": round(doc, 3), "share_paragraphs_over_0.5": round(share, 3),
               "paragraphs_over_0.5": sum(r["p_ai"] > 0.5 for r in rows)}
    if args.calibrate:
        human = ("Apparently mistaken decisions are ubiquitous. To what extent does this reflect irrationality, as opposed to a rational trade-off between the costs of information acquisition and the expected benefits of learning? We develop a revealed preference test that characterizes all patterns of choice mistakes consistent with a general model of optimal costly information acquisition and identify the extent to which information costs can be recovered from choice data. Limits on attention impact choice. Shoppers may buy unnecessarily expensive products due to their failure to notice whether or not sales tax is included in stated prices.")
        ai = ("In recent years, the intricate interplay between information acquisition and decision-making has attracted increasing attention from researchers across economics and psychology. This paper delves into a novel framework that seamlessly integrates costly information with rational choice, shedding light on a pivotal question: to what extent do observed mistakes reflect genuine irrationality? By leveraging a comprehensive set of tools, we demonstrate that our approach not only unifies existing models but also paves the way for future research. Our findings underscore the importance of considering attention constraints, highlighting their crucial role in shaping economic behavior.")
        summary["calibration"] = {"human_CD15_intro": round(sum(a*b for a,b in score(human))/sum(a for a,_ in score(human)),3),
                                  "synthetic_ai_slop": round(sum(a*b for a,b in score(ai))/sum(a for a,_ in score(ai)),3)}
    if args.json:
        print(json.dumps({"summary": summary, "paragraphs": rows}, indent=1)); return 0
    print(json.dumps(summary, indent=1))
    for r in sorted(rows, key=lambda r: -r["p_ai"])[:10]:
        print(f"  P(AI)={r['p_ai']:.2f} [{r['tokens']} tok] {r['snippet']}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
