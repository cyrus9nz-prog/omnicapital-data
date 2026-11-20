# OmniCAPITAL data

Working files for Cyrus's Stock Desk: the rules playbook, the desk's ledgers and research, the scout's screening and valuation code, the dashboard page, and dated watchlist snapshots. Analysis only — nothing here is an order or advice.

Mirrored from the OMNI 2.0 Claude Project (`OmniCAPITAL/knowledge/`) and the books folder on Cyrus's Mac. The playbook, library, reading notes and run reports are pushed after every book-ingest run; the other files are snapshots unless a job says otherwise.

## Layout
- `playbook/playbook.md` — the rules ledger (R-### rules with page cites and evidence grades), built from the book library.
- `playbook/library.md` — the book ingest queue and status.
- `playbook/notes/<Key>.md` — running notes taken while reading each book (paraphrased, with loc/page markers).
- `playbook/runs/<date>-<Key>.md` — the short report written after each book is ingested.
- `playbook/scanning-rules.md`, `playbook/knowledge-base.md`, `playbook/evals-track-record.md` — OmniCapital's developed rules, durable context and eval set.
- `desk/stock-desk-config.md` — settings every daily job reads first (account size, risk tiers, universe, data sources, heat score, schedule).
- `desk/calls-ledger.md` — every verdict and rating, append-only. `desk/signals.md` — latest ratings and paper positions. `desk/rule-paper-tally.md` — review tallies per rule. `desk/morning-brief.md` — latest pre-open alerts.
- `research/<TICKER>.md` — the researcher's latest deep dive per stock (heat score, filings, insiders, red flags).
- `setup/` — project instructions, the OmniCapital v5 skill, setup guide and the daily book-ingest runbook.
- `tools/convert_books.py` — converts the PDF book library into page-marked Markdown.
- `scout/analyze.py` — per-ticker metrics from Webull data files: price, σ and 1-/3-month 1-SD ranges, SMA/EMA/RSI, TTM ratios, own-history valuation (earnings, cash flow, book), label (UNDERVALUED / FAIR / OVERVALUED / CAN'T TELL). Set `LIVE=1` to price off an intraday snapshot.
- `scout/build.py` — applies the playbook screens (R-056 value, R-058 dividend; small/mid trend + R-043), writes `watchlist.json` (dashboard rows) and the markdown table.
- `scout/DATA_SPEC.md` — the per-ticker JSON schema the data pulls fill (raw vendor data is not committed).
- `dashboard/index.html` — the Stock Desk Watchlist dashboard page (tabs, filters, watchlist cards).
- `watchlist/<date>/` — each scout run's list: `watchlist.md` (full table with sources and rules) and `watchlist.json` (dashboard rows).

## Conventions
- Every number is tagged `[SOURCED <date>, <source>]` or `[ESTIMATED]`; ratios are computed in code from raw statement lines.
- Margin of safety 20%; a label needs two methods to agree; a method is dropped with fewer than 3 usable years or an own median P/E or P/FCF above 40x.
- Ranges are one-standard-deviation volatility spreads, not forecasts.
