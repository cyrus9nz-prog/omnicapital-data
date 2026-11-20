# AMCR — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $43.70 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $42.34 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 36 — Cold — Aligned
Heat = round(0.6 × Substance 44 + 0.4 × Buzz 25) [computed in Python]. Yesterday: 36 (Cold).

**Substance 44/100**
- Playbook fit 6/25: scout's fired rules R-058, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 43.70 vs 200-day 42.34 (above, +5); 6-month return +18.32% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: Scherger sold 12,615 @ $45.14 (11-10); Galvez 9,279 @ $41.80 (10-06). No buys.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: no 7-day items (scored neutral 20).
- News volume 0/20: 0 items 11-12..11-18 vs 5 in the prior window (weekly avg 1.25; ratio 0.00) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** 6.0% yield passes R-058; above 200-day; 6-month +18.3%.
- **Strongest against:** EPS outlook cut (11-04); FCF method -28%; last EPS miss.
- **Long-term case:** Largest global packaging consolidator after Berry; the case rests on delivering $650M synergies and de-levering to ~3x by end-2027 while paying ~$2.64/yr in dividends. Execution and cost pass-through lags are the risk, and working-capital swings make FCF lumpy. A deleveraging story, not yet proven.

## What changed since 11-17
- Heat 36 → 36. Nothing since 11-12 (8-K 5.07, S-8, Form 4). No items 11-12..11-18.

## Filings (last 90 days)
Today: Nothing since 11-12 (8-K 5.07, S-8, Form 4).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: Form 4 + 8-K (5.07) + S-8 11-12; Form 144 11-10; 10-Q 11-05; 8-K 11-04 (2.02/9.01); DEFA14A x4; DEF 14A + ARS 09-29; Form 4s. Auditor change 8-K (4.01) dated 08-14: PwC Switzerland to PwC US, no disagreements. No S-1/S-3/424B, no going concern.

## Insiders (6 months)
Scherger sold 12,615 @ $45.14 (11-10); Galvez 9,279 @ $41.80 (10-06). No buys.
Carried context: no rows after 11-10 (CFO Scherger 12,615 @ $45.14, withholding per prior run). Galvez 9,279 @ $41.80 (10-06). Class none (8).

## Institutions
MarketBeat failed. Today's SEC read shows no SC 13G/13D in the window; prior 13Gs 08-13 (CIK 914208), 05-12, 04-27 and 13G/A 03-26 not opened. Short interest 4.97% of float is the caller's figure (not re-sourced). (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor (consumer/healthcare packaging; not searched).

## Connections
Berry Global merger closed (subsidiary); $650M synergy target by end-2027, ~$60M realized in the Sept quarter. Divestitures cut quarterly sales ~$112M. Customers: food, beverage, healthcare and personal-care CPGs (no concentration % sourced). Hurt by lagged pass-through of energy/distribution costs.

## Sentiment
News 11-12..11-18: 0 items vs 5 in the prior feed (feed incomplete before ~10-19; ratio 0.00); tone no 7-day items (scored neutral 20), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): No items 11-12..11-18.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. Unscored: transition-period adj EPS guide cut to $1.70-1.80 (11-04); quarterly FCF -$820M; net debt up to $14.01B, leverage ~3.6x; GAAP EPS $0.52 vs $0.57. Auditor change (08-14, PwC AG to PwC US, no disagreements) looks benign. S-8 is employee-plan registration.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars AMCR and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions AMCR — 2026-11-18
- https://data.sec.gov/submissions/CIK0001748790.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://news-static.webullfintech.com/us/news-html/20261104/15868147861462016.html · https://www.sec.gov/Archives/edgar/data/0001748790/000110465926096303/tm2622721d1_8k.htm · https://data.sec.gov/submissions/CIK0001748790.json?v=20261116R · https://www.thailand-business-news.com/?p=338827&v=20261113R
