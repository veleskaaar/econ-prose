#!/usr/bin/env python3
"""Extract plain text from a PDF for style distillation.

Usage: python3 extract_pdf_text.py paper.pdf out.txt
Needs: pip install pypdf

Keep the output outside the repository or under corpus/raw/ (gitignored): the text of a paper is
copyrighted; only short quoted exemplars go into references/style-corpus.md.
"""
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    try:
        from pypdf import PdfReader
    except ImportError:
        print("pypdf is not installed: run  python3 -m pip install --user pypdf")
        return 1
    reader = PdfReader(sys.argv[1])
    text = "\n\n".join((page.extract_text() or "") for page in reader.pages)
    # Common ligature and spacing repairs from PDF extraction.
    for a, b in (("ﬁ", "fi"), ("ﬂ", "fl"), ("ﬀ", "ff"), ("ﬃ", "ffi"), ("ﬄ", "ffl")):
        text = text.replace(a, b)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{len(reader.pages)} pages, {len(text.split())} words -> {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
