# DOC — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $19.34 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $18.82 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 36 — Cold — Aligned
Heat = round(0.6 × Substance 34 + 0.4 × Buzz 38) [computed in Python]. Yesterday: 45 (Neutral).

**Substance 34/100**
- Playbook fit 6/25: scout's fired rules R-058, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 19.34 vs 200-day 18.82 (above, +5); 6-month return +1.35% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: Patadia sold 6,115 @ $20.78 (11-09); Lewis award 11-05. No open-market buys.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty -10: see Red flags (scored item carried).

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed.
- News volume 10/20: 2 items 11-12..11-18 vs 8 in the prior window (weekly avg 2.00; ratio 1.00) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0); red-flag penalty -10. Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** Cash-flow method +22%; 6.3% yield; above 200-day.
- **Strongest against:** Last EPS miss (0.02 vs 0.07); standing $1.5B ATM (scored); Mizuho PT cut.
- **Long-term case:** Diversified healthcare REIT recycling capital (Brookfield JV, Janus Living) into higher-yield lab and senior housing growth (+26% NOI). If lab occupancy keeps recovering, FFO/share can re-grow from a lower base; until then it is a ~6.1% yield income name near fair value, with buybacks offset by standing ATM capacity.

## What changed since 11-17
- Heat 45 → 36. SEC: Form 4 filed 11-13 (Thomas holdings line). No dilution forms in window. 11-16 Mizuho Outperform PT cut to $23; 11-16 Wells Fargo EW PT raised to $20.

## Filings (last 90 days)
Today: SEC: Form 4 filed 11-13 (Thomas holdings line). No dilution forms in window.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18 (SEC JSON): Form 4 11-13, Form 4 + Form 144 11-09, Form 4 11-05, 10-Q 11-03, 8-K 11-02 (2.02/7.01/9.01). No S-3/424B, 4.01/4.02, NT or going-concern. Nothing new since 11-13 [SOURCED 2026-11-16, SEC submissions].

## Insiders (6 months)
Patadia sold 6,115 @ $20.78 (11-09); Lewis award 11-05. No open-market buys.
Carried context: new row director John T. Thomas 11-13, no side/shares (holdings 58; likely deferred-unit line). Patadia sold 6,115 @ $20.78 (11-09); Lewis 46,744 @ $0 (11-05, award). No open-market buys. Class none (8).

## Institutions
Not determined: MarketBeat client_error pattern (not retried for DOC). Only 13G items (08-07, 07-22) are outside the 08-18 window. Q3 diluted shares 689.5M vs 694.9M a year ago (buybacks) [SOURCED 2026-11-02, Q3 release]. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor (healthcare REIT).

## Connections
Brookfield JV: July 2026 contributed 86 outpatient properties (~$2.1B), sold 49% for ~$1.03B. Owns 214.7M Janus Living shares/units = 69% at 09-30. Q3: ~$2B outpatient sales/recaps at 6% cap; three lab buys at 41% occupancy. Health-system tenants (Baylor Scott & White, AdventHealth); lab tenants = biotech funding cycle.

## Sentiment
News 11-12..11-18: 2 items vs 8 in the prior feed (feed incomplete before ~10-19; ratio 1.00); tone mixed, headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): 11-16 Mizuho Outperform PT cut to $23; 11-16 Wells Fargo EW PT raised to $20.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
SCORED dilution by the desk REIT rule: standing $1.5B ATM with forward-sale provisions (Q1-26 10-Q: $1.5B remaining, no sales in Q1). No usage seen: Q3 diluted shares down 0.8% y/y after 5.9M buyback in April; $500M buyback renewed July. Unscored: FFO/share $0.44 (-4.3% y/y), lab lease-up risk, Treasurer sale.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars DOC and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions DOC — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261116/15934731185275904.html
- https://news-static.webullfintech.com/us/news-html/20261116/15933862168817664.html
- https://data.sec.gov/submissions/CIK0000765880.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0000765880.json?v=20261116R · https://s202.q4cdn.com/584270836/files/doc_news/Healthpeak-Properties-Reports-Third-Quarter-2026-Results-and-Increases-Full-Year-2026-Earnings-Guidance-2026.pdf · https://s202.q4cdn.com/584270836/files/doc_news/Healthpeak-Properties-Reports-Second-Quarter-2026-Results-and-Increases-Full-Year-2026-Earnings-Guidance-2026.pdf · https:
