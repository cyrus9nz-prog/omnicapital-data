# CF — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $113.70 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $117.09 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 30 — Cold — Aligned
Heat = round(0.6 × Substance 33 + 0.4 × Buzz 25) [computed in Python]. Yesterday: 39 (Cold).

**Substance 33/100**
- Playbook fit 5/25: scout's fired rules R-056 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 5/15: close 113.70 vs 200-day 117.09 (below, 0); 6-month return -6.86% vs SPY -0.99% (126 sessions from 2026-05-20) (0); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: No rows after 05-26 (Scribner award). No open-market buys or sales in 6 months.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: no 7-day items (scored neutral 20).
- News volume 0/20: 0 items 11-12..11-18 vs 14 in the prior window (weekly avg 3.50; ratio 0.00) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: value (10); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Passes R-056 on sourced data (P/E 8.84, P/CF 5.48).
- **Strongest against:** Closed -4.7% to $113.70, below its 200-day ($117.09); last EPS missed; 6-month return -6.9%.
- **Long-term case:** Low-cost North American nitrogen producer with cheap US gas vs Europe, aggressive buybacks (~6% of shares in 12 months) and a low-carbon ammonia leg (Blue Point, CCS; +$400M mid-cycle EBITDA by 2030 target). But it is a commodity cyclical: current margins lean on disrupted Middle East/European supply, and Blue Point (~$3.7B) adds execution risk.

## What changed since 11-17
- Heat 39 → 30. SEC: SCHEDULE 13G/A filed 11-16 (holder not opened). No items 11-12..11-18 (latest 11-11: UBS PT cut to $133).

## Filings (last 90 days)
Today: SEC: SCHEDULE 13G/A filed 11-16 (holder not opened).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: SCHEDULE 13G/A 11-16 (new); 10-Q 11-05; two 8-Ks 11-04 (2.02/9.01); 8-K 09-03 (5.02, not opened). No S-1/S-3/424B/144, no 4.01/4.02, no going concern.

## Insiders (6 months)
No rows after 05-26 (Scribner award). No open-market buys or sales in 6 months.
Carried context: no rows after 05-26 (Scribner award). No open-market activity in 6 months. Class none (8).

## Institutions
MarketBeat failed. New SCHEDULE 13G/A filed 11-16 (accession 0000080255-26-000690; filer and share change not opened). Company bought back ~3M shares (~$367M) in Q3. Direction unknown. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor (not searched). Context: the 10-22 federal fertilizer-manufacturing financing ($139M) went to Intrepid Potash, not CF.

## Connections
Blue Point low-carbon ammonia JV (CF 40%; construction began Aug 2026, ~$3.7B, production 2029; JERA/Mitsui per older links, not re-verified). Donaldsonville/Yazoo City CCS. Helped by ~9 Mt lost Middle East urea and ~35% curtailed European ammonia; hurt when supply normalizes and by the 10-18 Russia tariff waiver.

## Sentiment
News 11-12..11-18: 0 items vs 14 in the prior feed (feed incomplete before ~10-19; ratio 0.00); tone no 7-day items (scored neutral 20), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): No items 11-12..11-18 (latest 11-11: UBS PT cut to $133).
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. Unscored: DOJ antitrust probe into US fertilizer pricing (reported 2026-03-04, status unknown); earnings ride a geopolitical supply shock (peak-cycle risk); $306M deposits tied to US-Canada transfer-pricing matter; Russia tariff waiver (10-18); heavy officer selling Jan-Mar 2026. New unscored: close below 200-day SMA.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars CF and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions CF — 2026-11-18
- https://data.sec.gov/submissions/CIK0001324404.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://news-static.webullfintech.com/us/news-html/20261105/15872268762113024.html · https://news-static.webullfintech.com/us/news-html/20261111/15907139165209600.html · https://data.sec.gov/submissions/CIK0001324404.json?v=20261116R · https://www.farmprogress.com/farm-business/doj-probes-u-s-fertilizer-market-for-possible-price-fixing
