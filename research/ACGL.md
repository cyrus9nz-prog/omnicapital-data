# ACGL — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $108.62 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $97.81 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 42 — Neutral — Aligned
Heat = round(0.6 × Substance 45 + 0.4 × Buzz 38) [computed in Python]. Yesterday: 42 (Neutral).

**Substance 45/100**
- Playbook fit 7/25: scout's fired rules R-056, R-042, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 108.62 vs 200-day 97.81 (above, +5); 6-month return +12.16% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: No new rows after 11-13 (Rajeh holdings-only line). 11-10 exercise-and-sell carried.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 30/40: positive (1 item).
- News volume 0/20: 1 items 11-12..11-18 vs 13 in the prior window (weekly avg 3.25; ratio 0.31) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** Q3 beat and $3B buyback add (carried); MS PT raise to $113 (11-17).
- **Strongest against:** President's ~$5.3M exercise-and-sell near highs (11-10).
- **Long-term case:** Disciplined specialty P&C, reinsurance and mortgage-insurance compounder; Q3 annualized ROE 16% and TBV/share +15% YoY. Returns capital via buybacks (authorization $3.6B, ~10% of mcap). At ~1.57x book and ~9.1x TTM EPS it looks fairly priced; upside depends on underwriting discipline as reinsurance pricing softens.

## What changed since 11-17
- Heat 42 → 42. SEC 11-13: Form 4 (Rajeh). Nothing flagged since. 11-17 Morgan Stanley EW, PT $113.

## Filings (last 90 days)
Today: SEC 11-13: Form 4 (Rajeh). Nothing flagged since.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 10-Q 11-04; 8-K 10-27 (2.02), 10-29 (5.02), 10-30 (1.01/2.03 debt), 10-30 (7.01), 11-05 (8.01 buyback +$3B to $3.6B); S-3ASR + F-N 11-10 (universal shelf, no 424B takedown seen); 144 08-18, 11-10; Form 4 08-20, 11-13; 13G 11-12. Nothing new after 11-13.

## Insiders (6 months)
No new rows after 11-13 (Rajeh holdings-only line). 11-10 exercise-and-sell carried.
Carried context: one new row: Rajeh (President) 11-13, no side/shares shown (holdings after 40,600; likely derivative/RSU line of the 11-10 exercise-and-sell). No open-market buys. 05-05 director awards (Pasquesi, Bunce, Houston, Posner etc., no price) are annual grants. Carried: Rajeh exercised 38,661 @ $21.55 and sold 48,661 @ $108.54 on 11-10 (secform4, 11-16 read); Morin row 08-20. Class: none (8), uncha…

## Institutions
Unknown. SCHEDULE 13G 2026-11-12 (accession 0000947484-26-000184, holder not opened). ACGL's own 13F-HR (11-04) covers its portfolio, not holders of ACGL. MarketBeat not reachable. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor. Mortgage-insurance segment depends on GSE eligibility rules (not a contract).

## Connections
Arch Insurance North America agreed 2026-10-30 to acquire Premier Dealer Holding / Premier Dealer Services (auto F&I administrator, Dublin OH, existing partner); terms undisclosed. Segments: Insurance GPW +7.8% (CR 94.4%), Reinsurance premiums -8% (CR 78.3%), Mortgage $201M UW income.

## Sentiment
News 11-12..11-18: 1 items vs 13 in the prior feed (feed incomplete before ~10-19; ratio 0.31); tone positive (1 item), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): 11-17 Morgan Stanley EW, PT $113.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Scored: none. Unscored: S-3ASR universal shelf 11-10 (registration only; watch for 424B equity takedown); reinsurance premiums -8% (softening cycle); Q3 revenue $4.014B missed $4.157B est, -6.3% YoY; President's ~$5.3M sale near 52-wk high.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars ACGL and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions ACGL — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261117/15939929487962112.html
- https://data.sec.gov/submissions/CIK0000947484.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0000947484.json?v=20261116R · https://www.secform4.com/insider-trading/947484.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261105/15873472040821760.html · https://news-static.webullfintech.com/us/news-html/20261028/15826537745875968.html
