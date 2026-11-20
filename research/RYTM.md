# RYTM — researcher deep dive, 2026-11-18

Lane: Small/mid · untested rules · Scout label: CAN'T TELL · Close $119.04 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $97.36 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 49 — Neutral — Aligned
Heat = round(0.6 × Substance 48 + 0.4 × Buzz 50) [computed in Python]. Yesterday: 49 (Neutral).

**Substance 48/100**
- Playbook fit 5/25: scout's fired rules R-043, R-025, R-027, R-020, R-042 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 5/20: scout label CAN'T TELL.
- Trend 15/15: close 119.04 vs 200-day 97.36 (above, +5); 6-month return +31.33% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: NEW: director Jean Christophe exercised 10,000 options and sold 10,000 @ $109.66 on 11-17 (10b5-1 not shown). Aug-Sep exec sales ~131.7k sh carried. No buys.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 10/10: carried from prior scoring (dated positive catalyst in last 90 days: yes).
- Red-flag penalty 0: none scored.

**Buzz 50/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 30/40: positive (1 item).
- News volume 0/20: 1 items 11-12..11-18 vs 8 in the prior window (weekly avg 2.00; ratio 0.50) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 10/20: Webull community posts stand in for Reddit: 1 posts 11-12..11-18, tone positive (rumour flagged) (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: playbook fit (5). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Sourced two-year Phase 3 data (11-17); revenue up every year; +31% in 6 months.
- **Strongest against:** Steady insider exercise-and-sell, new director sale 11-17; price leans on an unconfirmed takeover report. 'Lilly $150' post is rumour.
- **Long-term case:** Rare-obesity MC4R franchise. Fast hypothalamic-obesity launch (700+ start forms; Q3 sales $92.1M, +79.6% y/y), Japan approval and oral bivamelagon could compound. It is loss-making and adding obligations ($750M term loan, $350M to LG Chem), and part of the price still rests on an unconfirmed $10B AstraZeneca report.

## What changed since 11-17
- Heat 49 → 49. SEC: Form 144 11-17 and 11-18; Form 4 11-18. No S-1/S-3/424B. 11-17 two-year TRANSCEND Ph3: BMI -18.8% on setmelanotide. Carried: 11-04 WSJ AstraZeneca $10B offer report.

## Filings (last 90 days)
Today: SEC: Form 144 11-17 and 11-18; Form 4 11-18. No S-1/S-3/424B.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18 (SEC JSON 11-16): 10-Q + 8-K 2.02 11-03; SC 13G 10-13; Form 4s 08-18, 09-01, 09-14; Form 144s 08-31, 09-14; Form 3 08-18. Nothing new since 11-03, so no filing explains the 11-16 drop. No S-1/S-3/424B/ATM. Financing is debt ($750M term loan).

## Insiders (6 months)
NEW: director Jean Christophe exercised 10,000 options and sold 10,000 @ $109.66 on 11-17 (10b5-1 not shown). Aug-Sep exec sales ~131.7k sh carried. No buys.
Carried context: no rows after 09-14 (Meeker 2,300 @ $105.19). Smith 28,188 @ $106.20 (08-31); Lee 75,834 @ $117.38 (08-13). No open-market buys. Class none (8).

## Institutions
Unverified. SC 13G 10-13 (accession prefix 0000019617 = JPMorgan; not opened). MarketBeat unavailable. (carried from 11-16; not re-checked)

## Government contracts
None found (not a plausible federal contractor).

## Connections
LG Chem: bivamelagon royalty cut from 5-7% to 1% for $350M over 4 years. Japan launch under way. Competes with NBIX (VYKAT XR) in hyperphagia. RUMOUR: WSJ (11-04) reported an AstraZeneca ~$10B offer; no confirmation, denial or follow-up found through 11-16. AZ cut 600 US sales staff (Bloomberg, 11-13); no RYTM link stated.

## Sentiment
News 11-12..11-18: 1 items vs 8 in the prior feed (feed incomplete before ~10-19; ratio 0.50); tone positive (1 item), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 1 posts, positive (rumour flagged). X unreadable (null).
Headlines (7 days): 11-17 two-year TRANSCEND Ph3: BMI -18.8% on setmelanotide. Carried: 11-04 WSJ AstraZeneca $10B offer report.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. Loss-making (TTM EPS -$2.91). $750M term loan plus $350M LG Chem obligation (debt, not dilution). Steady executive exercise-and-sell. Price leans on an unconfirmed takeover report now 12 days old; 11-17 +8.5% move followed sourced Ph3 data; rumour still circulating on Webull communitysistent with that premium fading (inference, not sourced). New unscored: director sale 11-17; Form 144s 11-17/18.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars RYTM and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions RYTM — 2026-11-18
- https://www.secform4.com/insider-trading/1649904.htm?v=20261118R
- https://news-static.webullfintech.com/us/news-html/20261117/15939744662089728.html
- https://data.sec.gov/submissions/CIK0001649904.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0001649904.json?v=20261116R · https://www.secform4.com/insider-trading/1649904.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261104/15867503007130624.html · https://news-static.webullfintech.com/us/news-html/20261104/15865631285091328.html
