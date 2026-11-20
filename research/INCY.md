# INCY — researcher deep dive, 2026-11-13

Lane: Small/mid · untested rules · Scout label: FAIR (methods disagree) · Scout lean: Long · Close $120.97 [SOURCED 2026-11-13 close, Webull daily bar]
Scout list updated 2026-11-13 1:47pm PT close run — scout ran today. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 42 — Neutral — Aligned
Heat = round(0.6 × Substance 53 + 0.4 × Buzz 25) [computed in Python].

**Substance 53/100**
- Playbook fit 5/25: scout's fired rules R-043 D1, R-025 D1, R-027 D1, R-020 D1, R-042 D1 (grades from playbook.md: A=5, B=3, C=2, D=1).
- Value 10/20: scout label FAIR.
- Trend 15/15: above 200-day yes +5 (close 120.97 vs SMA200 108.92); 6-month return +26.92% vs SPY +2.57% (126 sessions from 2026-05-15) +5; R-050 ON +5 [SOURCED 2026-11-13, Webull daily bars; computed in code].
- Insiders 8/20: none — no open-market buying (sales, if any, not shown as outside 10b5-1 plans — desk convention).
- Institutions 5/10: flat_unknown.
- Catalysts 10/10: 2026-10-24: clinical trial collaboration with Genmab (Incyte co-funds Ph1/2 of INCB161734 + petosemtamab in 1L KRAS G12D mCRC); Natera collaboration followed 11-10. Clinical collaborations, not revenue deals - weak catalyst.
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT is a premium endpoint on this key → headline scoring)
- News tone 20/40: mixed headlines → 20.
- News volume 0/20: 2 items in 7 days vs 15 in the prior 4 weeks (weekly avg 3.75; ratio 0.53) [SOURCED 2026-11-13, Webull get_stock_news].
- Reddit slot 0/20: Webull community posts stand in for Reddit (no dated Reddit posts found); Webull posts last 7 days: 0 → none (heavy = 10+ posts) — none (latest 2026-10-24, neutral repost of Genmab news). X: null.

Note: Biggest driver: trend (15/15); biggest drag: playbook fit (5/25). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- Strongest evidence for the scout's call: Q3 revenue $1.56B (+14% y/y), Opzelura +36% to $255M, Opzelura and heme/onc guides raised; Oppenheimer upgrade (PT $144), Leerink $150, Barclays $143 [SOURCED 2026-10-29/30, Webull news].
- Strongest evidence against: Pipeline that must replace Jakafi lost a planned Ph3 (MAESTRA-3, INCB123667, 8-K 11-13) while executives keep selling (CMO 11-06, new Form 144 11-13) and no insider buys.
- Long-term case: Jakafi funds a broad pipeline (Opzelura, povorcitinib, VGA039, mutCALR, KRAS G12D), but the late-decade Jakafi exclusivity loss must be replaced. Today's MAESTRA-3 cancellation trims one Ph3 shot. It compounds only if the post-2029 pipeline delivers; insiders are not buying.

## 1 Identity
Webull profile: Incyte Corp, NASDAQ, CEO William J. Meury, Wilmington DE; Jakafi, Iclusig, Monjuvi, Niktimvo, Pemazyre, Zynyz, Opzelura; VGA039 in Ph3. Matches ticker.

## 2 Filings (last 90 days)
SEC JSON since 08-15: NEW 8-K (8.01) 11-13 = decision not to run Ph3 MAESTRA-3 of INCB123667; NEW Form 144 11-13; Schedule 13G/A 11-12 (filer not opened); 10-Q + 8-K (2.02) 10-29; 8-K (8.01) 08-31; Form 144s 08-19, 10-15, 11-03, 11-06, 11-13; Form 4s incl. 11-05, 11-10. No S-1/S-3/424B/ATM, going-concern or restatement. [SOURCED 2026-11-13, SEC submissions JSON]

## 3 Insiders (last 6 months)
No open-market buys by officers/directors since 05-13 (director rows Clancy/Harrigan ~200 sh at quarter-end prices = fee shares; Baker Bros 322/400 sh $0 = fund credits). Sales: CMO Stein 48,576 @ $119.66 (11-06; prior report via secform4: 240,193 after exercise @ $118.39); Pres. Cagnoni 2,642 @ $112.71 (10-15), 10,801 @ $125.56 (08-19), 25,469 @ $95.59 (06-01); CSO Mayes 2,207 @ $123.99 (08-05); Clancy 15,000 @ $94.93 (05-19); plus small withholding-type sales (Tray, Heeson, Gardner, Basi, Meury 07-02). 10b5-1 not shown. [SOURCED 2026-11-13, Webull get_insider_transactions] Cluster buying: no.

## 4 Institutions
MarketBeat institutional-ownership page failed (client_error) this run. Baker Bros. (10% owner) ~31.6M shares (Webull insider feed, 09-30). Schedule 13G/A 11-12, filer not opened.

## 5 Government contracts
None found (not a plausible federal contractor; not searched).

## 6 Connections
Genmab: Incyte co-funds Ph1/2 of petosemtamab + KRAS G12D INCB161734 in 1L mCRC (10-24). Natera: Signatera MRD clinical collaboration for INCA33890 Ph2 in CRC (11-10). 30 abstracts at ASH (11-04). Jakafi is the cash engine (FY guide $3.22-3.27B), exclusivity loss late decade; Opzelura +36% to $255M. Customer concentration not checked.

## 7 Sentiment
Webull news: 2 items in 7d (one positive collaboration, one negative pipeline cut) vs 15 in prior 4 weeks, mostly positive PT raises/upgrade after Q3 [SOURCED 2026-11-13, Webull get_stock_news]. 0 community posts. Analysts upbeat while every insider trade is a sale. Close $120.97 (-0.6%) [SOURCED 2026-11-13, Webull snapshot] does not yet reflect the after-close MAESTRA-3 news.
Headlines: 2026-11-13 Incyte decides not to proceed with planned Phase 3 MAESTRA-3 study of INCB123667; no effect on guidance or long-term outlook | 2026-11-10 Natera-Incyte clinical collaboration for Ph2 CRC study (INCA33890) | 2026-11-05 Leerink maintains Outperform, PT lowered to $150 | 2026-11-04 Incyte to present 30 abstracts at ASH | 2026-10-30 Oppenheimer upgrades to Outperform, PT $144 | 2026-10-29 Q3 revenue $1.56B (+14%), Opzelura +36%; Opzelura and heme/onc guides raised
Reddit: site:reddit.com search returned only stocktwits/marketbeat pages, no reddit posts.
X: site:x.com search returned no x.com posts.
Congressional trades: Not re-verified this run (MarketBeat failing); prior report cited Rep. Ro Khanna buy $1,001-15,000 on 2026-05-15.

## 8 Red flags
Scored: none. NEW 11-13 (after close): Incyte decided not to proceed with planned Ph3 MAESTRA-3 of INCB123667; says no effect on guidance or long-term outlook (reason not in headline; 8-K text not opened). Also: steady exec exercise-and-sell (6 Form 144s in 90d, new one 11-13); Jakafi patent cliff; large Q3 GAAP loss per scout (cause unverified).

## What changed since yesterday's report
NEW: 8-K 8.01 (11-13, after close) - Incyte will not proceed with Ph3 MAESTRA-3 of INCB123667, says guidance/long-term outlook unaffected; NEW Form 144 (11-13, filer not opened). Close $120.97 vs $121.70. Check stays Weakens; pipeline risk up a notch.

## Sources (opened this run, 2026-11-13)
- Webull get_company_profile — 2026-11-13
- Webull get_stock_filings — 2026-11-13
- Webull get_insider_transactions — 2026-11-13
- Webull get_stock_news — 2026-11-13
- Webull get_community_posts — 2026-11-13
- Webull get_stock_snapshot (2026-11-13 close) — 2026-11-13
- [SEC submissions CIK0000879169](https://data.sec.gov/submissions/CIK0000879169.json?v=20261113R) — 2026-11-13
- [Webull news: Incyte not proceeding with MAESTRA-3 (headline only)](https://news-static.webullfintech.com/us/news-html/20261113/15918526696648704.html?v=20261113R) — 2026-11-13
- WebSearch: Incyte INCB123667 MAESTRA-3 Phase 3 not proceed November 2026 — 2026-11-13
- WebSearch: site:reddit.com INCY Incyte stock — 2026-11-13
- WebSearch: site:x.com $INCY Incyte — 2026-11-13
- [MarketBeat INCY institutional ownership (failed)](https://www.marketbeat.com/stocks/NASDAQ/INCY/institutional-ownership/?v=20261113R) — 2026-11-13
- Project claude/research/INCY.md (prior report) — 2026-11-12
- Webull get_stock_bars daily, 210 sessions to 2026-11-13 (trend, SMA200, 6-month return); SPY 2026-05-15 close 735.44 → 2026-11-13 close 754.37

Data caveats: MAESTRA-3 item: headline only; reason, indication and drug class not in any source opened (INCB123667 recalled as a CDK2 inhibitor for ovarian cancer [RECALLED], unverified). 11-13 Form 144 filer and 13G/A filer not opened. Stein sale size differs: Webull 48,576 vs prior secform4 240,193. AV not called; MarketBeat failed.
