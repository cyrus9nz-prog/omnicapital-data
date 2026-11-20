# OKE — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: UNDERVALUED · Close $87.72 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $87.61 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 43 — Neutral — Quiet strength
Heat = round(0.6 × Substance 55 + 0.4 × Buzz 25) [computed in Python]. Yesterday: 43 (Neutral).

**Substance 55/100**
- Playbook fit 12/25: scout's fired rules R-056, R-058, R-042, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 20/20: scout label UNDERVALUED.
- Trend 10/15: close 87.72 vs 200-day 87.61 (above, +5); 6-month return -2.60% vs SPY -0.99% (126 sessions from 2026-05-20) (0); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: Director/officer sales 09-23 @ $90.09; 05-20 director rows at $92.15 look like annual grants. No open-market buys.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 10/10: carried from prior scoring (dated positive catalyst in last 90 days: yes).
- Red-flag penalty -10: see Red flags (scored item carried).

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: no 7-day items (scored neutral 20).
- News volume 0/20: 0 items 11-12..11-18 vs 11 in the prior window (weekly avg 2.75; ratio 0.00) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: value (20); biggest drag: insiders (8); red-flag penalty -10. Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Passes both A-graded screens; two methods +35-45%; Q3 beat.
- **Strongest against:** $1B ATM (scored); FCF method -21%; 6-month return -2.6% lags SPY.
- **Long-term case:** Scaled investment-grade midstream network (BBB+) with Permian growth via Brazos and gas demand from data centers and utilities; management targets mid-to-high single-digit EBITDA growth over 5-7 years at <=3.25x leverage. Holds if Apollo's $9B Class B is priced as senior capital and ATM issuance stays modest.

## What changed since 11-17
- Heat 43 → 43. Nothing new since SCHEDULE 13G 11-10. No items 11-12..11-18 (latest 11-10 Barclays EW $94).

## Filings (last 90 days)
Today: Nothing new since SCHEDULE 13G 11-10.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 8-K 08-31 (1.01/3.02 unregistered equity sale/7.01/8.01); 8-K12B 09-10 (holdco successor); S-8 POS x6 + POSASR x2 09-11; 8-K 09-15 (1.01/7.01) + 424B5 09-15 (ATM prospectus); 25-NSE 09-18; SD + Form 4s 09-24; 15-12G 09-28; 13G/13G-A 10-05; Form 4 10-19; 8-K 10-27 (Q3); 10-Q 10-28; 13G 11-10.

## Insiders (6 months)
Director/officer sales 09-23 @ $90.09; 05-20 director rows at $92.15 look like annual grants. No open-market buys.
Carried context: no rows after 09-24. 09-23 withholding @ $90.09 (Swords 1,905; Taylor 2,793; Burdick 1,270). 05-20 director share grants @ $92.15. Class none (8).

## Institutions
Unknown. 13G 11-10 (accession prefix 0000093751), 13G and 13G/A 10-05 (prefix 0002012383) - holders not opened. MarketBeat client_error. Apollo's $9B is a Class B holdco interest, not common stock. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor. Not searched.

## Connections
Apollo: $9B nonvoting Class B holdco interest (7% IRR cap first 9 years) that funded the $4.425B Brazos Midstream Midland Basin G&P buy (announced 08-31, closed) and $5.5B debt paydown; S&P/Fitch to BBB+. Customers: Permian, Rockies, Mid-Continent producers; data-center gas demand cited.

## Sentiment
News 11-12..11-18: 0 items vs 11 in the prior feed (feed incomplete before ~10-19; ratio 0.00); tone no 7-day items (scored neutral 20), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): No items 11-12..11-18 (latest 11-10 Barclays EW $94).
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Scored: dilution - $1B at-the-market common equity program (Latham, 2026-08-28) with 424B5 on 09-15 under the new holdco (~1.8% of mcap). Unscored: Apollo $9B Class B sits ahead of common (deduct as minority interest); Benzinga notes Rep. Hern's past OKE purchases (no dated trade in window).

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars OKE and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions OKE — 2026-11-18
- https://data.sec.gov/submissions/CIK0001039684.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://www.lw.com/en/news/2026/08/latham-advises-oneok-on-at-the-market-equity-program · https://data.sec.gov/submissions/CIK0001039684.json?v=20261116R · https://www.secform4.com/insider-trading/1039684.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261028/15826742215967744.html
