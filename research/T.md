# T — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $21.95 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $24.34 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 46 — Neutral — Aligned
Heat = round(0.6 × Substance 48 + 0.4 × Buzz 44) [computed in Python]. Yesterday: 41 (Neutral).

**Substance 48/100**
- Playbook fit 10/25: scout's fired rules R-056, R-058 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 5/15: close 21.95 vs 200-day 24.34 (below, 0); 6-month return -9.77% vs SPY -0.99% (126 sessions from 2026-05-20) (0); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: Cakaric sold 15,211 @ $24.24 (10-06); Stankey 13,000 @ $0 (10-23); small plan buys. Class none.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 10/10: carried from prior scoring (dated positive catalyst in last 90 days: yes).
- Red-flag penalty 0: none scored.

**Buzz 44/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: no 7-day items (scored neutral 20).
- News volume 0/20: 0 items 11-12..11-18 vs 50 in the prior window (weekly avg 12.50; ratio 0.00) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 15/20: Webull community posts stand in for Reddit: 20 posts 11-12..11-18, tone mixed (5 spam) (heavy = 10+). X: null.

Note: Biggest driver: catalysts (10); biggest drag: trend (5). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Passes both A-graded screens (P/CF 3.67, 5.1% yield).
- **Strongest against:** Below 200-day ($24.34), 6-month -9.8%; SpaceX wireless entry; last EPS 0.12 vs 0.62.
- **Long-term case:** Fiber-plus-wireless convergence and the GIP fiber JV give a path to slow growth with lower capex, but heavy debt, capital intensity and a well-funded fourth entrant (SpaceX) cap pricing power. An income stock (~5% yield) rather than a compounder unless SpaceX's terrestrial build stalls.

## What changed since 11-17
- Heat 41 → 46. Nothing new since five Form 4s filed 11-03. No T items 11-12..11-18; latest 11-11 FCC accepts SpaceX 800MHz transfer.

## Filings (last 90 days)
Today: Nothing new since five Form 4s filed 11-03.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18 (SEC JSON): 15 Form 4s 11-03; Form 4 10-26; 10-Q + 8-K 10-21; 8-K 10-16; 8-K 5.02 09-09; Form 3 09-16; 25-NSE 09-08. No S-3/424B/S-4/144/NT in window (424B2 notes 08-11/12 just before it). Nothing new since 11-03 [SOURCED 2026-11-16, SEC submissions].

## Insiders (6 months)
Cakaric sold 15,211 @ $24.24 (10-06); Stankey 13,000 @ $0 (10-23); small plan buys. Class none.
Carried context: no rows after 10-23 (CEO Stankey 13,000 @ $0, gift-like). Cakaric 15,211 @ $24.24 (10-06; plan status not shown). Plan-like small buys Lee 369 @ $24.40 (09-30), Sanders 145 (09-30). Class none (8), as scored 11-16.

## Institutions
Not determined: MarketBeat institutional page not reachable (client_error pattern; not retried for T). No SC 13G/13D filed 08-18..11-16 per SEC JSON. (carried from 11-16; not re-checked)

## Government contracts
No new award 08-18..11-16. FirstNet $2B agreement-in-principle (2026-03-31) is a MODIFICATION of the 25-yr FirstNet contract (cost reduction + AT&T-funded investment), not new revenue. FAA FENS $74.3M task order 08-13 is just outside the window.

## Connections
GIP fiber JV (10-21). AST SpaceMobile D2D partner (ground-to-satellite handoff 10-21; beam handover validated per 11-10 ASTS call). Selling AT&T Mexico for $2B to Televisa/Fintech (close 1Q27). Boost leases capacity; AT&T may cut it off if SpaceX buys it. AWS/Microsoft AI connectivity. Threat: SpaceX Starlink Mobile.

## Sentiment
News 11-12..11-18: 0 items vs 50 in the prior feed (feed incomplete before ~10-19; ratio 0.00); tone no 7-day items (scored neutral 20), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 20 posts, mixed (5 spam). X unreadable (null).
Headlines (7 days): No T items 11-12..11-18; latest 11-11 FCC accepts SpaceX 800MHz transfer.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Scored: none (no equity issuance; T is not a REIT). Unscored: SpaceX terrestrial entry (FCC accepted 800MHz transfer application 11-10; pleadings due Dec; Qualcomm 5G build from 2027); mgmt flagged 2027+ FCF pressure; fiber ARPU -4%; ~$100M Q4 vendor settlement; $2.6B Mexico impairment; Oct PT cuts.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars T and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions T — 2026-11-18
- https://data.sec.gov/submissions/CIK0000732717.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0000732717.json?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261021/15786512301239296.html · https://news-static.webullfintech.com/us/news-html/20261111/15904744466793472.html · https://news-static.webullfintech.com/us/news-html/20261109/15895122474496000.html
