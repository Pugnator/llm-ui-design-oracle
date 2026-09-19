#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_quotes - check that every quotation in the oracle is in a read source.

The contract's first constraint is that no citation may be added that was not
read (`UI_ORACLE_CONTRACT.md` §7). This tool enforces the stronger property
that the quoted *words* are the source's words: it extracts every `*"..."*`
span from the oracle's documents and looks for it in the archived corpus, the
local books, and the sources whose licence forbids archiving.

Exit status is 0 when every quotation is accounted for, 1 otherwise.

    python tools/verify_quotes.py                 # all oracle documents
    python tools/verify_quotes.py UX_WRITING_ORACLE.md

A quotation may legitimately fail to match for reasons that are not defects:
the source renders it inside a table, a code block or bold markup; a book's
PDF text breaks it across a page; or the source is one of the few that could
not be archived. Those cases are listed in ALLOWLIST with the reason. Adding
an entry there is a deliberate act and should be rare.
"""
import io
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Where the research scratch copies live. Sources that licence forbids us to
# archive are read from here when present; when absent, quotations that depend
# on them are reported as UNCHECKABLE rather than as failures.
SCRATCH = os.environ.get("ORACLE_SCRATCH", "")

CORPUS_DIRS = ["corpus/copy", "corpus/writing", "corpus/platform",
               "corpus/cli", "corpus/imgui"]

# Quotations that are the oracle's own illustrations, not quotations of a
# source: invented bad strings used as examples.
INVENTED = [
    r"^(oops|uh-oh|whoops)", r"^sorry, that value", r"^please select a file",
    r"^could not disarm", r"^passthruwritemsgs", r"^error: eperm",
]

# Known-good quotations the matcher cannot confirm, with the reason.
ALLOWLIST = {
    "to get the building blocks for crafting windows experiences, use winui":
        "FLUENT2-WIN: the page carries no archivable content (conflict C4); "
        "quoted from the 2026-09-18 fetch recorded in UI_SOURCE_MATRIX.md",
    "each describes a different set of behavioral attributes":
        "AF4 Ch. 9: the phrase spans a page break in the PDF text layer",
    "error messages from other noninteractive programs should look like this":
        "GNU-STD 4.4: the message forms that follow are in code blocks",
}


def norm(s):
    """Fold the differences between a quotation and its rendered source."""
    s = (s.replace("’", "'").replace("‘", "'")
           .replace("“", '"').replace("”", '"')
           .replace("—", "-").replace("–", "-")
           .replace("…", "...").replace(" ", " ")
           .replace("�", " "))
    s = re.sub(r"-\s*\n\s*", "", s)              # words hyphenated across lines
    s = re.sub(r"^\s*>\s?", "", s, flags=re.M)   # blockquote markers
    s = re.sub(r"<[^>]{1,40}>", " ", s)          # html tags in source markup
    s = s.replace('"', "").replace("'", "")      # quote-character style
    s = re.sub(r"[`*_>\[\]|]+", " ", s)          # inline markup and table pipes
    s = re.sub(r"[-‐‑]+", " ", s)      # dash spacing and hyphenation
    s = re.sub(r"\s+([,.;:!?])", r"\1", s)       # converter-spaced punctuation
    s = re.sub(r"\s*/\s*", "/", s)               # spacing left by stripped code marks
    return re.sub(r"\s+", " ", s).strip().lower()


def load_sources():
    blobs, missing = [], []
    for d in CORPUS_DIRS:
        p = os.path.join(ROOT, d)
        if os.path.isdir(p):
            for f in sorted(glob.glob(os.path.join(p, "*.md"))):
                blobs.append(io.open(f, encoding="utf-8", errors="replace").read())
    if SCRATCH and os.path.isdir(SCRATCH):
        for pat in ("books/*.txt", "copy/*.md", "cli/*.md"):
            for f in sorted(glob.glob(os.path.join(SCRATCH, pat))):
                blobs.append(io.open(f, encoding="utf-8", errors="replace").read())
    else:
        missing.append("books and unarchivable sources (set ORACLE_SCRATCH)")
    return norm(" || ".join(blobs)), missing


def documents(argv):
    if argv:
        return argv
    docs = sorted(glob.glob(os.path.join(ROOT, "*.md")))
    docs += sorted(glob.glob(os.path.join(ROOT, "modules", "*.md")))
    return [os.path.relpath(d, ROOT) for d in docs]


def main(argv):
    corpus, missing = load_sources()
    invented = [re.compile(p, re.I) for p in INVENTED]
    checked = allowed = 0
    seen, bad = set(), []
    for rel in documents(argv):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path) or "corpus" in rel:
            continue
        text = io.open(path, encoding="utf-8").read()
        for m in re.finditer(r'\*"(.+?)"\*', text, re.S):
            q = m.group(1)
            key = norm(q)
            if len(q.split()) < 4 or any(p.match(key) for p in invented):
                continue
            if key in seen:
                continue
            seen.add(key)
            checked += 1
            if any(key.startswith(a) or a in key for a in ALLOWLIST):
                allowed += 1
                continue
            parts = [p.strip(" .,;:!?")
                     for p in re.split(r"\s*\.\.\.\s*", key)
                     if len(p.strip().split()) >= 3]
            ok = all(p in corpus for p in parts) if parts else (key.strip(" .,;:!?") in corpus)
            if not ok:
                bad.append((rel, q))
    print("quotations checked : %d" % checked)
    print("allowlisted        : %d" % allowed)
    print("unverified         : %d" % len(bad))
    if missing:
        print("not loaded         : %s" % "; ".join(missing))
    for rel, q in bad:
        print("\nUNVERIFIED  %s" % rel)
        print("  %s" % re.sub(r"\s+", " ", q)[:160])
    if bad:
        print("\nEach one is a defect unless the source renders it in a way the "
              "matcher cannot fold. Fix the quotation, or add it to ALLOWLIST "
              "with the reason.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
