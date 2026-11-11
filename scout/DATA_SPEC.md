# Data-gathering spec (stock desk scout, 2026-11-10 close)

Analysis only. NEVER call any Webull order/trade/instruction/watchlist-writing tool. Never use remembered numbers: every value must come from a tool call made now, written exactly as returned.

Tools: load Webull market-data tools with ToolSearch "select:mcp__Webull__get_stock_bars,mcp__Webull__get_stock_snapshot,mcp__Webull__get_income_statement,mcp__Webull__get_cash_flow,mcp__Webull__get_balance_sheet,mcp__Webull__get_stock_earnings_calendar,mcp__Webull__get_analyst_rating,mcp__Webull__get_company_profile,mcp__Webull__get_stock_dividend_calendar,mcp__Webull__get_financial_indicators". category is "US_STOCK" (use symbol as given). Large tool results are saved to files by the harness — parse those files with Python (`python3 -I`) rather than retyping numbers, whenever possible. Put scratch in /tmp/claude-0/-home-claude/32184348-10c5-526d-9bab-1617a3c1c3c2/scratchpad.

For EACH ticker write /home/claude/desk/data/<TICKER>.json with these keys (null when unavailable, and add a note in "notes"):

- ticker, company, exchange, sector, industry (company profile)
- daily: list of {date, open, high, low, close, volume}, NEWEST FIRST, at least 252 sessions (get_stock_bars timespan D count 260, category US_STOCK). Newest must be 2026-11-10.
- monthly: list of {date, close} newest first, count 72 (timespan M).
- snapshot: {price, pe_ratio, eps_ttm, bps, yield, last_trade_time, fifty_two_wk_high, fifty_two_wk_low} plus any other numeric fields it returns.
- income_annual: up to 6 fiscal years, each {period_end (YYYY-MM-DD), fiscal_year, revenue, operating_income, net_income, eps_diluted, shares_diluted}. income_quarterly: 8 quarters same fields (count 8). Use the provider's field names to map; record the exact field used in notes if ambiguous (e.g. total revenue vs revenue).
- cashflow_annual (5–6 yrs) and cashflow_quarterly (8 q): {period_end, operating_cash_flow, capex (as reported sign), free_cash_flow (compute ocf - |capex| if absent, note it), dividends_paid}.
- balance_annual (5–6 yrs) and balance_quarterly (latest 4 q): {period_end, total_debt (short+long-term debt incl. current portion; note what was summed), cash_and_equivalents, total_equity (parent shareholders), shares_outstanding}.
- dividends: list of {ex_date, amount} for the last 6 years if get_stock_dividend_calendar gives history; else null.
- earnings: {next_date, last_report_date, last_eps_actual, last_eps_estimate} from get_stock_earnings_calendar (record raw fields too in earnings_raw if small).
- analyst: rating summary as returned (consensus label, counts, target if present).
- short_interest_pct_float: try WebFetch https://stockanalysis.com/stocks/<ticker lowercase>/statistics/?v=20261110S<n> asking for "Short % of float, Short interest date, Shares outstanding, Earnings date, exactly as shown"; record value, as-of date and the page; if rate-limited or failing, null with a note. Don't spend more than 2 attempts.
- latest_10q_period: period_end of the newest quarterly income row.
- notes: list of strings (sources, caveats, anything odd).

Validate in Python before finishing: daily newest date is 2026-11-10 and len ≥ 200; quarterly income has ≥ 5 rows; JSON loads.

Return to the caller ≤120 words per ticker batch: files written, any missing fields, anything odd (e.g. one-off items, spin-offs, restated years, missing latest quarter).
