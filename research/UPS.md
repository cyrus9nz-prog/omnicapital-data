# UPS — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $111.03 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $101.54 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 44 — Neutral — Aligned
Heat = round(0.6 × Substance 44 + 0.4 × Buzz 44) [computed in Python]. Yesterday: 46 (Neutral).

**Substance 44/100**
- Playbook fit 6/25: scout's fired rules R-058, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 111.03 vs 200-day 101.54 (above, +5); 6-month return +15.78% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: Webull stale; secform4 (11-16 read): Guffey sold 8,318 @ $105.39 (10-28). No buys.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 44/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed/neutral.
- News volume 0/20: 2 items 11-12..11-18 vs 23 in the prior window (weekly avg 5.75; ratio 0.35) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 15/20: Webull community posts stand in for Reddit: 11 posts 11-12..11-18, tone mixed, leaning positive (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** 5.9% yield passes R-058; above 200-day; 6-month +15.8%.
- **Strongest against:** Dividends exceed FY2025 FCF; Amazon volume glide-down; R-056 fails (P/CF 10.17). A community post's 'acquisition' claim is unconfirmed rumour.
- **Long-term case:** Network re-engineered toward fewer, higher-margin packages (US Domestic margin 7.0%, +60bp; revenue/piece +6.1%) with automation, healthcare logistics and SMB growth. If revenue per piece keeps rising while costs fall, margins rebuild over years. Amazon glide-down, tariffs and a dividend above FY2025 FCF make it mainly an income/recovery case.

## What changed since 11-17
- Heat 46 → 44. Nothing since 11-06 (Form 4). No UPS-specific items; 11-18 BofA Amazon automation note tags UPS.

## Filings (last 90 days)
Today: Nothing since 11-06 (Form 4).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 8-K 08-18 (8.01); 8-K 08-31 (5.02/7.01); Form 3 + 4 x3 09-03; 8-K 10-27 (2.02 Q3); Form 4 10-30; 10-Q 11-04; 8-K 11-05 (5.02/7.01, director Eisenhardt); Form 3 + 4 11-06. The $1B 4.850% notes 424B5 (08-14) is just outside the window and was debt. No equity shelf/ATM.

## Insiders (6 months)
Webull stale; secform4 (11-16 read): Guffey sold 8,318 @ $105.39 (10-28). No buys.
Carried context: Webull feed stale (latest row 09-01 Ramos, no side). Carried from 11-16 secform4 read: Guffey sold 8,318 @ $105.39 (10-28); option awards 09-01. No open-market buys. Class none (8).

## Institutions
Unknown. No SC 13G/13D on UPS's SEC list since 08-18; MarketBeat institutional page unreachable (client_error). (carried from 11-16; not re-checked)

## Government contracts
USTRANSCOM/AMC NGDS 2 delivery IDIQ HTC71123DC025 (awarded 2022-12-19, ceiling $5.35B); modification P00016 dated 2026-08-19, est. face $2.72B, appears to cover the 2026-10-01..2030-09-30 option period. Modification/option of an existing IDIQ; ceiling is not revenue. Carried from 11-12.

## Connections
Amazon (largest customer) volume being cut deliberately; Q4 US ADV guided lower y/y. Core ex-Amazon volume +1.8%, SMB/enterprise +3.7%; healthcare revenue >$3B/qtr; Supply Chain Solutions revenue +18.2% to $2.98B; CEO cites $15B data-center logistics opportunity; China-US lanes recovering; DoD (NGDS 2).

## Sentiment
News 11-12..11-18: 2 items vs 23 in the prior feed (feed incomplete before ~10-19; ratio 0.35); tone mixed/neutral, headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 11 posts, mixed, leaning positive. X unreadable (null).
Headlines (7 days): No UPS-specific items; 11-18 BofA Amazon automation note tags UPS.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Scored: none. Unscored: scout caveat that dividends exceeded FY2025 FCF (yield 5.87%); scout notes last EPS missed while Benzinga shows Q3 adj EPS $1.69 beat $1.63 (adj EPS fell from $1.74 y/y) - basis mismatch; Amazon glide-down; tariffs; officer sale 10-28; Barclays Underweight PT $95.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars UPS and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions UPS — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261118/15946043986079745.html
- https://data.sec.gov/submissions/CIK0001090727.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0001090727.json?v=20261116R · https://www.secform4.com/insider-trading/1090727.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261027/15820478296150016.html · https://www.highergov.com/idv/HTC71123DC025/
