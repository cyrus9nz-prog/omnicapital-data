#!/usr/bin/env python3
"""
convert_books.py — turn the PDFs in a books folder into page-marked Markdown that a
Claude Project can read in order and cite.

  python3 convert_books.py /path/to/books            # convert new/changed PDFs
  python3 convert_books.py /path/to/books --ocr      # also OCR scanned books (resumable)
  python3 convert_books.py /path/to/books --force    # rebuild everything

Writes  <books>/text/<slug>.md   one file per book, with [[Short p.N]] page markers
        <books>/text/catalog.md  the library index
Reads   <books>/text/catalog-tags.json  (optional) short/title/author/year/tradition per slug
        (for Stock Desk, "tradition" = the school: value, growth/momentum, swing-technical,
        day-trading, options-income, options-directional, risk/sizing, process)
Needs   pdftotext (poppler). OCR also needs pdftoppm + tesseract.
OCR is resumable: pages are cached in <books>/text/.ocr-cache/<slug>/ and the run stops
cleanly after --budget seconds (default 150), so re-run until it reports 0 pages left.

Stock Desk change from the Almanac copy: numeric-table pages are no longer dropped
silently. Each one leaves a marker at its page, because in trading books the table is
often where the backtest lives, and the evidence grade depends on it.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, time
from collections import Counter

LIG = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl",
       "­": "", "’": "'", "‘": "'", "“": '"', "”": '"'}
WORD = re.compile(r"[A-Za-z][a-z']*[,.;:!?]?")

def slugify(name):
    s = re.sub(r"[^A-Za-z0-9]+", "-", os.path.splitext(name)[0]).strip("-").lower()
    return s[:80]

def clean_ratio(text):
    toks = text.split()
    return sum(1 for t in toks if WORD.fullmatch(t)) / max(1, len(toks))

def quality(pages):
    """Clean-word ratio minus a penalty for split-letter artifacts ("Ca pr icor n")."""
    toks = " ".join(pages).split()
    singles = sum(1 for t in toks if re.fullmatch(r"[B-HJ-Zb-z]", t))
    return clean_ratio(" ".join(pages)) - 2 * singles / max(1, len(toks))

def is_table(page):
    return len(page.strip()) > 300 and clean_ratio(page) < 0.35

def pdftotext_pages(pdf, raw=False):
    args = ["pdftotext", "-enc", "UTF-8"] + (["-raw"] if raw else []) + [pdf, "-"]
    out = subprocess.run(args, capture_output=True, text=True, errors="replace").stdout
    pages = out.split("\f")
    return pages[:-1] if pages and not pages[-1].strip() else pages

def page_count(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, errors="replace").stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1)) if m else 0

def ocr_pages(pdf, cache, n, budget):
    os.makedirs(cache, exist_ok=True)
    t0 = time.time(); left = 0
    for p in range(1, n + 1):
        f = os.path.join(cache, f"p{p:04d}.txt")
        if os.path.exists(f):
            continue
        if time.time() - t0 > budget:
            left += 1; continue
        tmp = tempfile.mkdtemp()  # page images go outside the books folder
        subprocess.run(["pdftoppm", "-r", "250", "-f", str(p), "-l", str(p), "-gray", "-png", pdf,
                        os.path.join(tmp, "img")], capture_output=True)
        pngs = [x for x in os.listdir(tmp) if x.endswith(".png")]
        if pngs:
            subprocess.run(["tesseract", os.path.join(tmp, pngs[0]), f[:-4], "-l", "eng"], capture_output=True)
        shutil.rmtree(tmp, ignore_errors=True)
        if not os.path.exists(f):
            open(f, "w").close()
    pages = [open(os.path.join(cache, f"p{p:04d}.txt"), errors="replace").read()
             if os.path.exists(os.path.join(cache, f"p{p:04d}.txt")) else "" for p in range(1, n + 1)]
    return pages, left

def strip_running(pages):
    """Drop page numbers and headers/footers repeated across many pages."""
    norm = lambda s: re.sub(r"[\d\W_]+", "", s.lower())
    edge = Counter()
    split = []
    for pg in pages:
        lines = [l for l in pg.splitlines()]
        nonblank = [i for i, l in enumerate(lines) if l.strip()]
        split.append((lines, nonblank))
        for i in nonblank[:2] + nonblank[-2:]:
            k = norm(lines[i])
            if 0 < len(k) < 60:
                edge[k] += 1
    limit = max(5, int(0.2 * len(pages)))
    common = {k for k, c in edge.items() if c >= limit}
    out = []
    for lines, nonblank in split:
        drop = set()
        for i in nonblank[:2] + nonblank[-2:]:
            s = lines[i].strip()
            if norm(s) in common or re.fullmatch(r"[\divxlcIVXLC.\- ]{1,8}", s):
                drop.add(i)
        out.append("\n".join(l for i, l in enumerate(lines) if i not in drop))
    return out

def reflow(page):
    for a, b in LIG.items():
        page = page.replace(a, b)
    page = re.sub(r"[\x00-\x08\x0b-\x1f]", "", page)
    lines = [l.strip() for l in page.splitlines()]
    lens = sorted(len(l) for l in lines if l)
    med = lens[len(lens) // 2] if lens else 0
    paras, cur = [], ""
    for l in lines:
        if not l:
            if cur: paras.append(cur); cur = ""
            continue
        if cur.endswith("-") and l[:1].islower():
            cur = cur[:-1] + l; continue
        prev_short = med and len(cur.split("\n")[-1]) < 0.7 * med
        if cur and re.search(r"[.?!:\"']$", cur) and l[:1].isupper() and prev_short:
            paras.append(cur); cur = l; continue
        cur = (cur + " " + l) if cur else l
    if cur: paras.append(cur)
    return "\n\n".join(re.sub(r"[ \t]{2,}", " ", p) for p in paras)

def convert(pdf, outdir, tag, do_ocr, budget):
    name = os.path.basename(pdf); slug = slugify(name)
    n = page_count(pdf)
    a, b = pdftotext_pages(pdf), pdftotext_pages(pdf, raw=True)
    prose = lambda ps: [p for p in ps if not is_table(p)]
    ra, rb = quality(prose(a)), quality(prose(b))
    pages, mode = (b, "text (raw order)") if rb > ra + 0.01 else (a, "text")
    ratio = clean_ratio(" ".join(prose(pages)))
    chars_pp = sum(len(p) for p in pages) / max(1, n)
    cache = os.path.join(outdir, ".ocr-cache", slug)
    left = 0
    if ratio < 0.55 or chars_pp < 150 or os.path.isdir(cache):
        if os.path.isdir(cache) or do_ocr:
            if do_ocr and not shutil.which("tesseract"):
                return {"slug": slug, "status": "needs OCR — tesseract not installed"}
            pages, left = ocr_pages(pdf, cache, n, budget if do_ocr else 0)
            mode, ratio = "OCR", clean_ratio(" ".join(p for p in pages if not is_table(p)))
        else:
            return {"slug": slug, "file": name, "status": "needs OCR — re-run with --ocr",
                    "pages": n, "clean_ratio": round(ratio, 2)}
    short = tag.get("short") or slug.split("-")[0].title()
    body = [f"# {tag.get('title', name)}",
            f"Author: {tag.get('author', 'unknown')} | Year: {tag.get('year', '?')} | "
            f"Tradition: {tag.get('tradition', 'untagged')} | Kind: {tag.get('kind', 'untagged')}",
            f"Source file: {name} | PDF pages: {n} | Extraction: {mode} | Clean-word ratio: {ratio:.2f}",
            f"Cite as [[{short} p.N]] using the page markers below (N = PDF page in the source file).",
            ""]
    kept = 0; table_pages = []
    for i, pg in enumerate(strip_running(pages), 1):
        if is_table(pg):
            # Keep a marker: the table may hold the test results a rule's grade depends on.
            table_pages.append(i)
            body.append(f"[[{short} p.{i}]]\n\n[Numeric table omitted in conversion. "
                        f"If a rule depends on it, open the source PDF at page {i}.]\n")
            continue
        txt = reflow(pg).strip()
        if len(txt) < 40:
            continue
        body.append(f"[[{short} p.{i}]]\n\n{txt}\n"); kept += 1
    if table_pages:
        body.insert(4, f"Numeric-table pages (marked in place, not converted): "
                       f"{', '.join(map(str, table_pages))}")
    open(os.path.join(outdir, slug + ".md"), "w", encoding="utf-8").write("\n".join(body))
    return {"slug": slug, "file": name, "short": short, "status": "ok" if not left else f"partial — {left} OCR pages left",
            "pages": n, "pages_with_text": kept, "table_pages": table_pages, "mode": mode, "clean_ratio": round(ratio, 2),
            "chars": sum(len(x) for x in body), **{k: tag.get(k, "") for k in ("title", "author", "year", "tradition", "kind")}}

def write_catalog(outdir, rows):
    rows = sorted(rows, key=lambda r: (r.get("tradition", ""), r.get("title", "")))
    total = sum(r.get("chars", 0) for r in rows)
    lines = ["# Library catalog", "",
             "One row per converted book. Cite with each file's page markers.",
             "Clean-word ratio under 0.88 = OCR or table noise; paraphrase rather than quote those books.", "",
             "| Cite key | Title | Author | Year | School | Kind | Pages | Table pages | Text quality | File |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r.get('short','')} | {r.get('title','')} | {r.get('author','')} | {r.get('year','')} | "
                     f"{r.get('tradition','')} | {r.get('kind','')} | {r.get('pages','')} | "
                     f"{len(r.get('table_pages', []))} | "
                     f"{r.get('clean_ratio','')} ({r.get('mode','')}) | {r.get('slug','')}.md |")
    lines += ["", f"Total ≈ {total:,} characters (≈ {total // 4:,} tokens at ~4 chars/token, an estimate)."]
    open(os.path.join(outdir, "catalog.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("books"); ap.add_argument("--ocr", action="store_true")
    ap.add_argument("--force", action="store_true"); ap.add_argument("--budget", type=int, default=150)
    a = ap.parse_args()
    outdir = os.path.join(a.books, "text"); os.makedirs(outdir, exist_ok=True)
    tags_path = os.path.join(outdir, "catalog-tags.json")
    tags = json.load(open(tags_path)) if os.path.exists(tags_path) else {}
    state_path = os.path.join(outdir, ".catalog-state.json")
    state = json.load(open(state_path)) if os.path.exists(state_path) else {}
    report = []
    for name in sorted(os.listdir(a.books)):
        if not name.lower().endswith(".pdf"):
            continue
        pdf = os.path.join(a.books, name); slug = slugify(name)
        md = os.path.join(outdir, slug + ".md")
        fresh = os.path.exists(md) and os.path.getmtime(md) >= os.path.getmtime(pdf)
        if fresh and not a.force and slug in state and state[slug].get("status") == "ok" \
                and state[slug].get("tradition", "") == tags.get(slug, {}).get("tradition", ""):
            report.append({"slug": slug, "status": "unchanged"}); continue
        r = convert(pdf, outdir, tags.get(slug, {}), a.ocr, a.budget)
        report.append(r)
        if "pages" in r and "chars" in r:
            state[slug] = r
    json.dump(state, open(state_path, "w"), indent=1)
    write_catalog(outdir, list(state.values()))
    print(json.dumps(report, indent=1))

if __name__ == "__main__":
    main()
