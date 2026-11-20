# ADMA — researcher deep dive, 2026-11-18

Lane: Small/mid · untested rules · Scout label: FAIR · Close $13.56 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $10.67 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 38 — Cold — Aligned
Heat = round(0.6 × Substance 47 + 0.4 × Buzz 25) [computed in Python]. Yesterday: 43 (Neutral).

**Substance 47/100**
- Playbook fit 5/25: scout's fired rules R-043, R-025, R-027, R-020, R-042 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 13.56 vs 200-day 10.67 (above, +5); 6-month return +58.41% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 12/20: NEW: CEO Adam Grossman sold 21,000 @ $13.72 and director Guiheen 10,000 @ $13.92 on 11-16 (exercise-and-sell; 10b5-1 not shown); CEO sold 147,000 @ $12.00 on 11-05. Director Jerrold Grossman open buy 6,400 @ $7.91 (05-27) keeps class one.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed (1 loosely tagged item).
- News volume 0/20: 1 items 11-12..11-18 vs 10 in the prior window (weekly avg 2.50; ratio 0.40) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Q3 beat, EBITDA guide raised to $275M; 16.5M shares bought back YTD.
- **Strongest against:** CEO and a director selling into the post-earnings rally (11-05, 11-16); class action and derivative suits allege channel stuffing.
- **Long-term case:** Vertically integrated plasma-to-IVIG maker. High-margin ASCENIV (+31% y/y, $124.7M of $141.1M Q3) and buybacks (6.3% of shares retired YTD) drive EPS. It compounds only if ASCENIV demand is real end-use: filed suits alleging channel stuffing via a related-party distributor must clear first, and BIVIGAM faces pricing pressure.

## What changed since 11-17
- Heat 43 → 38. SEC: Form 144 and two Form 4s 11-16; Schedule 13Gs 11-10 and 11-16. No S-1/S-3/424B. No ADMA-specific items; 11-12 short-seller Nvidia item loosely tags ADMA.

## Filings (last 90 days)
Today: SEC: Form 144 and two Form 4s 11-16; Schedule 13Gs 11-10 and 11-16. No S-1/S-3/424B.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18 (SEC JSON 11-16): NEW SCHEDULE 13G 11-16; SC 13G 11-10; Form 4 + Form 144 11-05 (CEO); 10-Q + 8-K 11-04. No S-1/S-3/424B/ATM. Buyback of 16.5M shares ($181.4M) YTD. Profitable; going concern unlikely (10-Q text not opened).

## Insiders (6 months)
NEW: CEO Adam Grossman sold 21,000 @ $13.72 and director Guiheen 10,000 @ $13.92 on 11-16 (exercise-and-sell; 10b5-1 not shown); CEO sold 147,000 @ $12.00 on 11-05. Director Jerrold Grossman open buy 6,400 @ $7.91 (05-27) keeps class one.
Carried context: Webull feed stale (latest 2025-12-16). Carried from 11-16 read: director Jerrold Grossman open-market buy 6,400 @ $7.91 (05-27); CEO Adam Grossman exercised 105,000 @ $5.40 and sold 147,000 @ $12.00 (11-05). Class one (12) per prior scoring (05-27 buy just outside a strict 6-month window from 11-17: 05-17 start -> still inside).

## Institutions
Unverified. New SCHEDULE 13G 11-16 (holder not identified) and SC 13G 11-10 (prefix 0000093751 = State Street, not opened). MarketBeat unavailable. (carried from 11-16; not re-checked)

## Government contracts
No federal award found (one search, 11-13). Prior run: VA NAC pharmaceutical BPA 36E79724A0025 (2024-08-01 to 2027-07-31), a purchasing vehicle, not revenue; not re-opened.

## Connections
Sells via specialty distributors; filed suits allege an undisclosed insider-tied ASCENIV distributor (unproven). BIVIGAM revenue fell to $15.4M from $23.8M on competitive pricing. SG001 pneumococcal hyperimmune IND planned 2027 after constructive FDA pre-IND feedback.

## Sentiment
News 11-12..11-18: 1 items vs 10 in the prior feed (feed incomplete before ~10-19; ratio 0.40); tone mixed (1 loosely tagged item), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): No ADMA-specific items; 11-12 short-seller Nvidia item loosely tags ADMA.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored: the Culper short report (2026-03-24) is outside the 90-day window. Filed securities class action (June 2026) and derivative suit (09-02, D.N.J.) allege ASCENIV channel stuffing via a hidden related-party distributor. CEO sold 147k on 11-05. FY revenue guide (>=$530M) is below the $535.4M estimate. New unscored: CEO and director sales 11-16.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars ADMA and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions ADMA — 2026-11-18
- https://www.secform4.com/insider-trading/1368514.htm?v=20261118R
- https://data.sec.gov/submissions/CIK0001368514.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0001368514.json?v=20261116R · https://www.secform4.com/insider-trading/1368514.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261112/15912726752510976.html · https://news-static.webullfintech.com/us/news-html/20261105/15869614549474304.html
