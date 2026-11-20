# Stock Desk — setup and first test

## What's real, what you wire
| Piece | Tag | State |
|---|---|---|
| `PROJECT-INSTRUCTIONS.md` | [PROMPT] | Ready. Paste into a new Claude Project. |
| `tools/convert_books.py` | [CODE] | Ready. Runs on your Mac; tested on a sample PDF. |
| Fundamentals data | [EXTERNAL] | Web search works for ≤10 tickers a run. A connector is better (step 5). |
| Options chain data | [EXTERNAL] | Paste or attach from your broker, or a connector that returns IV and open interest. Without it the desk names structure families only, by design. |
| Scheduled runs | [SCAFFOLD] | Prompts below. Set up only after the manual test passes. |

## 1. Convert the books (Mac, ~5 min + OCR time)
1. Put the PDFs in `~/Downloads/stock-books/`. Install poppler: `brew install poppler`
   (and `brew install tesseract` if any book is a scan).
2. Run: `python3 convert_books.py ~/Downloads/stock-books --ocr` and re-run until no book
   says "partial".
3. Optional but worth it: create `stock-books/text/catalog-tags.json` so each book gets a
   clean cite key and its school, then run the converter again:
   ```json
   {"one-up-on-wall-street": {"short": "Lynch", "title": "One Up on Wall Street",
     "author": "Peter Lynch", "year": "1989", "tradition": "growth/momentum"}}
   ```
   The key is the file's slug (lowercase, dashes), shown in the converter's output.

This copy differs from the Almanac one in one way: numeric-table pages leave a marker
instead of disappearing, because in trading books the table is often where the backtest
lives and the evidence grade depends on it.

## 2. Create the project
New Claude Project, "Stock Desk". Paste all of `PROJECT-INSTRUCTIONS.md` into custom
instructions. Upload `text/catalog.md` and the book `.md` files (not the PDFs). Turn on
code execution. The state files (`playbook.md`, `library.md`, `watchlist.md`,
`calls-ledger.md`) are created on first use.

If the project can't write files, every run ends with the full updated file and
"NOT SAVED"; you re-upload it. That's the honest fallback, and it's tedious enough
that you'll notice if it's happening.

## 3. Walking-skeleton test (do this before book #2)
1. `ingest <one book you know well>`. Open the PDF at three cited pages chosen at random.
   **Pass:** each page says what the rule says, and nothing is graded A or B without a
   cited test. **Fail:** stop and fix before ingesting anything else. Every later verdict
   inherits these citations.
2. `research <3 tickers you know> using R-###`. Check each number against the filing.
   **Pass:** every number is tagged with a date and matches.
3. `verdict <one ticker>` with no options chain. **Pass:** no strikes or premiums, just
   the structure family and the inputs needed. Then paste a chain and ask again: C3–C6
   should now run, with the move check computed in code.

## 4. Schedules (only after step 3 passes)
**Books:** I'd run these manually ("next book") rather than on a schedule. The library
is finite, each run needs a spot-check, and a silent partial read on a schedule is the
failure you won't see. If you still want it scheduled, daily:
> In the Stock Desk project, run Workflow A on the first `pending` book in `library.md`,
> following the project instructions exactly. If you cannot read the book file or write
> `playbook.md`, stop and report that in one line. Never build rules from memory.

**Weekly review + watchlist** (Sunday evening, after Friday's close):
> In the Stock Desk project, run Workflow D (review calls past due), then Workflow B on
> the tickers in `watchlist.md` (max 10), then Workflow C on the top 3 by margin of
> safety. Every price must be [SOURCED] today; if data can't be retrieved, mark the
> ticker CAN'T TELL. Open the report with how many tickers got NO ACTION.

Unconfirmed: whether a scheduled session can read and write this project's files. Fire
the weekly task once by hand and check that `watchlist.md` changed before trusting it.

## 5. Data connectors
The Claude connector directory lists three with market-data tools: Alpha Vantage
(stocks, options, fundamentals, earnings, filings), Financial Datasets (statements,
filings, earnings) and FMP. Not verified: their pricing, and whether the options data
includes per-strike IV and open interest, which gate C3 needs. Check both before
connecting.

SEC EDGAR is the free primary source for financial statements: no API key, but it
requires a User-Agent header with contact details, which Claude's web fetch can't set.
In practice the desk reads filings through search results, or a connector does it.

## 6. Defaults to tune (in the instructions)
Margin of safety 20% (B3) · price freshness 1 trading day (B2), 5 days before a
re-research (C) · bid-ask ≤10% of mid, OI ≥500 (C5) · tiers 1.0–1.5 / 0.5–1.0 / ≤0.5% (C7)
· ≥10 reviewed calls before a retire proposal (D). These are reasonable starting points,
not tested values. Change them once the ledger says so.

## 7. If you use OmniCapital
Stage C reuses OmniCapital v4's confluence rule and risk tiers, so the two don't
disagree on gates. If its `rules/scanning-rules.md` exists, add its six developed rules
to `playbook.md` as Evidence C ("own trades") with the track record as the source, and
run one desk instead of two.
