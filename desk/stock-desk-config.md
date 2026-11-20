# Stock Desk — settings for the daily jobs

Read first by the weekday jobs (pre-open check, scout, researcher, trader). Anything here overrides the defaults written into each job. Change a setting by editing this file or asking Claude.

## Settings (Cyrus, 2026-11-10)
- Account size: $1,000. Risk tiers by max loss per play: core 1.0–1.5% ($10–$15), speculative 0.5–1.0% ($5–$10), lotto ≤0.5% (≤$5).
- Price cap: every stock on the list trades under $250 (Cyrus, 2026-11-10).
- Universe: two lanes, always labeled.
  - "S&P 500 · tested rules": S&P 500 members under $250, where the playbook's A-graded screens (R-056 value, R-057 growth, R-058 dividend) and filters (R-050) were tested.
  - "Small/mid · untested rules": US-listed, price $1–$250, sectors biotech, quantum computing, space, semiconductors, AI infrastructure. No playbook rule has been tested here.
- List size: 10–20 stocks (Cyrus, 2026-11-10; this raises the project instructions' default cap of 10 researched per run). Aim for roughly half per lane. Every listed stock must still pass its lane's rules on sourced data: if fewer than 10 qualify, list only those and say why; never pad the list.
- Margin of safety: 20% (Workflow B3).
- Intraday / day trades: out of scope. The desk has no execution speed to call them. (The pre-open check flags gaps and events, and the scout's midday run watches the list on live prices; neither calls entries. Ratings change only in the trader's after-close run, from completed daily bars.)
- Bearish views: puts or put spreads. Short-selling shares only if Cyrus says his account allows it (not stated yet).
- Options liquidity gate (C5): bid-ask ≤10% of mid and open interest ≥500 at the chosen strike.

## Data access (verified 2026-11-10 ~9:45pm PT; Webull added 2026-11-11; this section wins over any data instructions inside a job)
Webull connector (connected 2026-11-11): the desk's primary market-data source. Read-only market-data tools only. No job ever calls a Webull tool that places, changes or cancels orders or instructions (place_*, revoke_instruction), reads Cyrus's account (get_account_*, get_open_orders, get_order_*, get_pending_instruction, get_processed_instruction), or creates, edits or deletes watchlists.
- Works: get_stock_snapshot (up to 100 symbols; live price, pre_close, extended-hours price with extend_hour_required, P/E, EPS TTM, BPS, shares, 52-week range, yield), get_stock_bars (daily up to 260+, monthly; older bars are dividend-adjusted), quarterly and annual income statement, cash flow and balance sheet, get_financial_indicators, get_stock_earnings_calendar (past quarters' EPS actual vs estimate; no next date), get_analyst_rating (rating counts only, sometimes empty), get_analyst_target_price, get_company_profile, get_fund_holdings, get_insider_transactions (Form 4 rows with insider, date, side, shares, price), get_stock_news, get_community_posts, get_macroeconomic_calendar. Large results are saved to files: parse in Python.
- Option contracts: get_option_contracts lists strikes and expiries, but option quotes (get_option_snapshot) return "MARKET_DATA_NOT_SUBSCRIBED" — Cyrus's Webull account has no options-data subscription (2026-11-11). Use the Cboe chain below for bid, ask, IV and open interest until that changes.

GitHub data repo (pending): cyrus9nz-prog/omnicapital-data (public). The pipeline that fills it is built but not pushed yet (Claude needs GitHub linked to the account). Jobs ignore the repo until this line says "live".

Paid connectors are limited: Financial Datasets has no credits; FMP's plan refuses quotes, charts and statements (SPY daily works); Alpha Vantage is a free key (25 calls a day for all jobs, 1 per second, no premium endpoints: no bulk or realtime quotes, no realtime options). Use Alpha Vantage only for NEWS_SENTIMENT, INSIDER_TRANSACTIONS or CONGRESS_TRADES on the most important names, and as a price cross-check. Budget: scout 6 a day (at most 2 per run), researcher 12, trader 7, pre-open check 0.

Other sources, all through WebFetch (each verified 2026-11-10). ALWAYS add a unique cache-busting parameter such as v=<YYYYMMDD><job letter> to every URL, or the fetcher can return a days-old copy. Check each page's own date stamp and reject anything older than the last trading day. stockanalysis.com rate-limits parallel fetches: one page at a time.
- Daily prices (OHLCV), newest first, 50 rows per page: https://stockanalysis.com/stocks/<ticker lowercase>/history/?p=daily&v=<stamp> (older rows with &page=2, &page=3). Fallback to Webull bars.
- Valuation and technicals: https://stockanalysis.com/stocks/<t>/statistics/?v=<stamp> → short % of float (no as-of date shown), plus market cap, shares, ratios, moving averages, RSI, analyst consensus and price target. This page can lag a day: take the price from Webull or the history page. No next earnings date is shown there.
- Financial statements: https://stockanalysis.com/stocks/<t>/financials/?p=quarterly&v=<stamp> (also /financials/balance-sheet/ and /financials/cash-flow-statement/, and annual views); can lag the latest 10-Q. For filing-grade numbers or to settle a discrepancy, SEC XBRL: https://data.sec.gov/api/xbrl/companyconcept/CIK<10-digit CIK>/us-gaap/<Concept>.json (e.g. Revenues, NetIncomeLoss, OperatingIncomeLoss, NetCashProvidedByUsedInOperatingActivities).
- Universe lists: https://stockanalysis.com/list/sp-500-stocks/?v=<stamp> or Wikipedia's S&P 500 constituent list (worked 2026-11-11); industry and theme lists on stockanalysis.com found by WebSearch. Filter to price under $250 before fetching details.
- Option chains (15-minute delayed, refreshed after the close): https://cdn-api.cboe.com/api/global/delayed_quotes/options/<TICKER>.json — large file: page through it with WebFetch offsets and ask only for the expiries and strikes needed. Entries give the OCC symbol (expiry and strike), bid, ask, iv, open_interest, volume and greeks; the top-level timestamp is the chain time.
- SEC filing list (8-K, 10-Q, S-3, 424B, Form 4, Form 144 with dates): https://data.sec.gov/submissions/CIK<10-digit CIK>.json. EDGAR's browse and Archives pages are blocked.
- Insider trades (insider, role, buy/sell/award, shares, price): Webull get_insider_transactions, cross-checked at https://www.secform4.com/insider-trading/<CIK without leading zeros>.htm.
- Congressional trades: https://www.marketbeat.com/stocks/<EXCHANGE>/<TICKER>/insider-trades/ lists them next to insiders.
- News, government contracts, Reddit and X: Webull get_stock_news and get_community_posts, plus WebSearch (news queries; site:usaspending.gov, site:sam.gov, site:defense.gov contracts; site:reddit.com; site:x.com), then WebFetch the pages that load.
- Blocked or stale, don't use: Yahoo Finance, Stooq, Nasdaq's API, Finviz, CNBC's quote API, Google Finance (stale), openinsider, EDGAR browse/Archives pages; curl through the proxy (403).
- Web pages pass through a summarizer: ask for values "exactly as shown", recompute every ratio in code from raw inputs, and cross-check a price against a second source when a value looks off. Mark figures from a single page "(one web source)".

## Signals: strong buy to sell now (added 2026-11-10 at Cyrus's request)
The trader rates every listed stock each day. Ratings are the desk's paper signals under its rules, never orders.
- BUY: verdict LONG-TERM BUY ZONE (at least 3 fired rules from at least 2 schools, an entry rule triggering at today's price), countercase written, nothing disqualifying, and a share position fits the tier: shares = floor(tier dollars ÷ (entry − stop)), at least 1, within the paper cash left ($1,000 minus open and pending positions). Tested lane sizes at core (up to $15 risk), untested lane at speculative (up to $10). Otherwise HOLD, "fits no tier".
- STRONG BUY: everything BUY needs plus label UNDERVALUED, researcher "Confirms", no red flags, no "Hype ahead of evidence" flag, R-050 ON, and 4+ fired rules from 3+ schools or at least one A-graded rule.
- HOLD: the default. No position: the price or event that would make it a buy. Open position: no exit triggered.
- SELL: an exit by plan (target reached, 20-day time limit, mixed-indicator bar per R-044), or a supported bearish lean on a stock with no position (bearish trades only via options that pass C3–C7).
- SELL NOW: a hard exit (stop hit, invalidation met, researcher Contradicts or a disqualifying red flag, R-050 OFF for the tested lane) or verdict AVOID.

Paper positions: a BUY or STRONG BUY opens one per ticker (P-0001 upward). Buy-stop triggers stay pending until a later day trades through them (cancelled on a mixed-indicator bar first); at-price triggers open at that day's close. Stops and targets are checked on daily highs and lows; if both fall in one day's range the stop is assumed. Returns are before costs and compared with SPY over the same days.

## Heat score (heat tracker; added 2026-11-10 at Cyrus's request)
Scored daily by the researcher for each listed stock, in code, whole-number points. Untested desk score: not a playbook rule, not a buy signal, never counts toward the trader's confluence (C1); a "Hype ahead of evidence" flag goes into the trader's countercase and blocks a STRONG BUY.

Substance, 0–100:
- Playbook fit 0–25: 5 per A-graded rule that fired, 3 per B, 2 per C, 1 per D, capped at 25.
- Value 0–20: UNDERVALUED 20, FAIR 10, CAN'T TELL 5, OVERVALUED 0.
- Trend 0–15: 5 each for price above its 200-day average, 6-month return ahead of SPY's, and R-050 ON.
- Insiders 0–20: open-market buying by 2+ officers or directors in 6 months 20; by one 12; no open-market activity 8; net selling outside 10b5-1 plans 0.
- Institutions 0–10: 13F holders or shares held rose last quarter 10, flat or unknown 5, fell 0.
- Catalysts 0–10: a dated positive catalyst in the last 90 days (government award, major customer or partner deal, regulatory approval) 10, else 0.
- Red-flag penalty: −10 each for dilution filings or an at-the-market program, going-concern language, a short-seller report, sponsor or creator distribution. Floor 0.

Buzz, 0–100:
- News tone 0–40: 20 + 20 × relevance-weighted 7-day ticker sentiment (−1 to +1), clipped. Without Alpha Vantage calls left, score tone from the past week's headlines (Webull news or search: mostly positive 30, mixed 20, mostly negative 10) and say so.
- News volume 0–20: last 7 days vs the prior 4 weeks' weekly average: ≥2× 20, 1–2× 10, less 0.
- Reddit 0–20 and X 0–20: none 0; some, mixed or neutral 10; heavy and mixed 15; heavy and mostly positive 20; heavy and mostly negative 5. An unreadable source is null and Buzz is rescaled over the rest (Webull community posts may stand in; say so).

Heat = round(0.6 × Substance + 0.4 × Buzz). Bands: Hot 80+, Warm 60–79, Neutral 40–59, Cold under 40. Flags: Buzz − Substance ≥ 30 → "Hype ahead of evidence" (scanning rule R2: buying the top); Substance − Buzz ≥ 30 → "Quiet strength"; else "Aligned". Every day's scores are kept with the price so heat can later be checked against what the stocks did.

## Schedule (Pacific, weekdays; Cyrus asked for morning, noon and end-of-day coverage, 2026-11-11)
- 5:43am — Pre-open check (morning): pre-market gaps, pending buy-stops likely to fill or gapped past entry (R-023), stops and invalidations at risk, overnight news and filings, earnings today, macro releases. Alerts only; no ratings.
- 11:47am — Scout, midday run (noon): intraday list refresh on live prices, tagged intraday; watches only.
- 1:47pm — Scout, close run (end of day): uses the day's close; the run the researcher and trader rely on.
- 3:13pm — Researcher: deep dive on each listed stock (filings, insiders, institutions, government contracts, partners, news/Reddit/X/Webull community sentiment) and the heat score.
- 4:41pm — Trader: reviews due calls (Workflow D), updates paper positions, then one verdict and one rating (strong buy to sell now) per stock and any options play that passes the gates (Workflow C). Re-enabled 2026-11-11.
- These five scheduled tasks were created 2026-11-11 with the Webull connector attached. Older copies without Webull (scout, researcher, trader) are disabled, not deleted. The earlier 7:47am scout run was folded into the 5:43am pre-open check.

## Where things go
- claude/morning-brief.md — the pre-open check's alerts (replaced each weekday).
- claude/watchlist.md — the current list (scout; overwritten each run).
- claude/research/<TICKER>.md — one report per stock, heat breakdown at the top (researcher).
- claude/calls-ledger.md — every verdict and rating, append-only (trader). claude/signals.md — today's ratings and the paper positions record (trader). claude/rule-paper-tally.md — review tallies per rule (trader).
- Dashboard: https://claude.ai/artifact/VppPc9Ba1Ys3xBh7W2NWGr (datasets: watchlist, research, plays, heat, ratings, positions). Old data files are never deleted by the jobs; Cyrus approves cleanups himself.

## Limits that apply to every job
- Analysis only. Nothing is an order or advice; Cyrus decides and sizes. No job calls a Webull trading, account or watchlist-writing tool.
- Every number carries [SOURCED <date>, <source>] or [ESTIMATED] with assumptions; no recalled prices, ratios, IV or dates.
- Public information only: filings, insider and institutional disclosures, government contract databases, congressional disclosures, news and public forums. No material non-public information.
- One-month and three-month ranges are 1-standard-deviation volatility spreads, not forecasts. No job predicts that a stock will become "the next Nvidia"; it counts observable big-winner traits instead.
