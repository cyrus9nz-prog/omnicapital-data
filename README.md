# OmniCAPITAL data

Working files for Cyrus's Stock Desk: the scout's screening and valuation code, the dashboard page, and dated watchlist snapshots. Analysis only — nothing here is an order or advice.

## Layout
- `scout/analyze.py` — per-ticker metrics from Webull data files: price, σ and 1-/3-month 1-SD ranges, SMA/EMA/RSI, TTM ratios, own-history valuation (earnings, cash flow, book), label (UNDERVALUED / FAIR / OVERVALUED / CAN'T TELL). Set `LIVE=1` to price off an intraday snapshot.
- `scout/build.py` — applies the playbook screens (R-056 value, R-058 dividend; small/mid trend + R-043), writes `watchlist.json` (dashboard rows) and the markdown table.
- `scout/DATA_SPEC.md` — the per-ticker JSON schema the data pulls fill (raw vendor data is not committed).
- `dashboard/index.html` — the Stock Desk Watchlist dashboard page (tabs, filters, watchlist cards).
- `watchlist/<date>/` — each scout run's list: `watchlist.md` (full table with sources and rules) and `watchlist.json` (dashboard rows).

## Conventions
- Every number is tagged `[SOURCED <date>, <source>]` or `[ESTIMATED]`; ratios are computed in code from raw statement lines.
- Margin of safety 20%; a label needs two methods to agree; a method is dropped with fewer than 3 usable years or an own median P/E or P/FCF above 40x.
- Ranges are one-standard-deviation volatility spreads, not forecasts.
