# VICI — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: UNDERVALUED · Close $24.39 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $26.05 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 44 — Neutral — Aligned
Heat = round(0.6 × Substance 48 + 0.4 × Buzz 38) [computed in Python]. Yesterday: 41 (Neutral).

**Substance 48/100**
- Playbook fit 10/25: scout's fired rules R-056, R-058 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 20/20: scout label UNDERVALUED.
- Trend 5/15: close 24.39 vs 200-day 26.05 (below, 0); 6-month return -11.01% vs SPY -0.99% (126 sessions from 2026-05-20) (0); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: Only zero-price director/officer awards since May; Pitoniak 06-01 20,000 @ $0. No open-market buys.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: neutral (1 item).
- News volume 0/20: 1 items 11-12..11-18 vs 9 in the prior window (weekly avg 2.25; ratio 0.44) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 10/20: Webull community posts stand in for Reddit: 4 posts 11-12..11-18, tone mixed (heavy = 10+). X: null.

Note: Biggest driver: value (20); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Now passes both A-graded screens (R-056 P/CF 9.92, R-058); 7.4% yield; two methods +46-54%.
- **Strongest against:** Below 200-day ($26.05), 6-month return -11%, last EPS miss; forward-equity settlement dilution (carried).
- **Long-term case:** Slow compounder at best: CPI-linked triple-net leases give ~4% AFFO/share growth plus a ~7.3% yield, and a new $2B buyback signals management sees value. Caesars/MGM concentration, a $458M CECL allowance and the unresolved Caesars Regional lease are real risks; growth needs acquisitions at a pressured cost of capital.

## What changed since 11-17
- Heat 41 → 44. Nothing since 8-K 8.01 on 11-12 (likely the $500M term loan; not opened). 11-13 Benzinga high-yield REIT roundup (7.3% yield, PTs trimmed to $29-30, $500M term loan).

## Filings (last 90 days)
Today: Nothing since 8-K 8.01 on 11-12 (likely the $500M term loan; not opened).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 8-K 11-12 (8.01; likely $500M term loan per Benzinga), 10-Q + 8-K (2.02/7.01/9.01) 10-28, Form 4 x7 10-05, Form 3/4 09-28, 8-K/A 09-22 (5.02), 8-K 09-08 (5.02). No S-3/424B/144; nothing new since 11-12 [SOURCED 2026-11-16, SEC submissions].

## Insiders (6 months)
Only zero-price director/officer awards since May; Pitoniak 06-01 20,000 @ $0. No open-market buys.
Carried context: no rows after 10-05; quarterly director awards @ $0 (10-01); Sullivan initial 5,562 (09-24); CEO Pitoniak 20,000 @ $0 (06-01, gift-like). Class none (8).

## Institutions
Not determined: MarketBeat client_error (1 try this run, also failed 11-11..11-13). No SC 13G/13D filed 08-18..11-16 per SEC submissions JSON. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor (gaming/experiential REIT).

## Connections
Top tenants Caesars and MGM (~29%/~25% of Q3 revenue, carried from 11-11 derivation). Caesars Regional lease under review in Fertitta go-private; $331M of $458M CECL tied to Caesars. New tenant Highfield. Golden Entertainment transaction issued 24.3M shares in 2026. $500M 5-yr term loan 11-12.

## Sentiment
News 11-12..11-18: 1 items vs 9 in the prior feed (feed incomplete before ~10-19; ratio 0.44); tone neutral (1 item), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 4 posts, mixed. X unreadable (null).
Headlines (7 days): 11-13 Benzinga high-yield REIT roundup (7.3% yield, PTs trimmed to $29-30, $500M term loan).
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Not scored (lead override): SCORED dilution (desk REIT rule): 7.75M shares issued on physical settlement of equity forward sale agreements in 9M-2026 (quarter not disclosed; Q3 shows no forward dilution, likely settled before the 08-18 window). ATM program not verified this run. Unscored: $458M CECL, Caesars Regional lease, tenant concentration, AFFO $0.62 missed $0.67, serial PT cuts.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars VICI and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions VICI — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261113/15916297153343488.html
- https://data.sec.gov/submissions/CIK0001705696.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0001705696.json?v=20261116R · https://pdf.dfcfw.com/pdf/H2_AN202610291831152924_1.pdf · https://news-static.webullfintech.com/us/news-html/20261113/15916297153343488.html · https://news-static.webullfintech.com/us/news-html/20261029/15832184341275648.html
