# TGTX — researcher deep dive, 2026-11-18

Lane: Small/mid · untested rules · Scout label: CAN'T TELL · Close $66.12 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $45.89 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 35 — Cold — Aligned
Heat = round(0.6 × Substance 42 + 0.4 × Buzz 25) [computed in Python]. Yesterday: 35 (Cold).

**Substance 42/100**
- Playbook fit 4/25: scout's fired rules R-043, R-025, R-027, R-020 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 5/20: scout label CAN'T TELL.
- Trend 15/15: close 66.12 vs 200-day 45.89 (above, +5); 6-month return +66.30% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: Webull stale; SEC Form 4 09-14 and 144 09-10 (Charney sold 5,000 @ $54.96, carried). No buys.
- Institutions 10/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 0/10: carried from prior scoring (dated positive catalyst in last 90 days: none found).
- Red-flag penalty 0: none scored.

**Buzz 25/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: no 7-day items (scored neutral 20).
- News volume 0/20: 0 items 11-12..11-18 vs 5 in the prior window (weekly avg 1.25; ratio 0.00) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 0/20: Webull community posts stand in for Reddit: 0 posts 11-12..11-18, tone none (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: catalysts (0). Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** FY revenue guide raised to $1B; $100M buybacks; above 200-day, +66% in 6 months.
- **Strongest against:** One-drug concentration; Evercore PT $71 near price; no news flow.
- **Long-term case:** Can compound if BRIUMVI keeps taking anti-CD20 share (FY26 revenue guide $1B; 14 straight quarters of sequential growth) and subQ (2028) and consolidated-dose (~mid-2027) expansions land. Risks: single-asset concentration (~90% of revenue), Roche/Novartis competition, early pipeline. Profitable, with a $100M buyback.

## What changed since 11-17
- Heat 35 → 35. Nothing since 10-Q/8-K 11-09 and 13G/A 10-27. No S-1/S-3/424B. No items 11-12..11-18; latest 11-10 Evercore PT cut to $71.

## Filings (last 90 days)
Today: Nothing since 10-Q/8-K 11-09 and 13G/A 10-27. No S-1/S-3/424B.
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18 (SEC JSON 11-16): 10-Q + 8-K 11-09; SC 13G/A 10-27; Form 4 09-14; Form 144 09-10. Nothing new since 11-09. No S-1/S-3/424B/ATM. $750M senior secured credit facility (debt) and $100M buyback in Q3.

## Insiders (6 months)
Webull stale; SEC Form 4 09-14 and 144 09-10 (Charney sold 5,000 @ $54.96, carried). No buys.
Carried context: Webull feed stale (latest 2025-11-24). Carried from 11-16 secform4: Charney sold 5,000 @ $54.96 (09-10); director option awards 06-11; 0 open-market buys. Class none (8).

## Institutions
Quiver (11-09 page): 227 added vs 172 reduced; D.E. Shaw +2.70M (+386%, Q2), T. Rowe +2.13M (+337%, Q2), Barclays +1.47M (+153%, Q3), Sixth Street +1.31M new (Q2); Soleus -27%, Man Group -86%. SC 13G/A 10-27 (prefix 0002012383) not opened. (carried from 11-16; not re-checked)

## Government contracts
None found (not a plausible federal contractor). A VA/GSA FSS listing cited earlier is a pricing vehicle, not an award (not re-verified).

## Connections
BRIUMVI US $233M of $260M Q3 revenue. Ex-US partner Neuraxpharm (prior report). Rivals: Roche (ocrelizumab), Novartis (ofatumumab). Pipeline: subQ BRIUMVI Ph3 readout YE26/early-27, azer-cel allogeneic CAR-T in progressive MS, myasthenia gravis expansion.

## Sentiment
News 11-12..11-18: 0 items vs 5 in the prior feed (feed incomplete before ~10-19; ratio 0.00); tone no 7-day items (scored neutral 20), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 0 posts, none. X unreadable (null).
Headlines (7 days): No items 11-12..11-18; latest 11-10 Evercore PT cut to $71.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
None scored. One-drug concentration (~90% of revenue). Q3 EPS $0.35 slightly missed (~$0.36-0.37). Evercore PT cut to $71 (11-10). Older 'short squeeze' community chatter is rumour.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars TGTX and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions TGTX — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261110/15899876475269120.html
- https://data.sec.gov/submissions/CIK0001001316.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0001001316.json?v=20261116R · https://www.secform4.com/insider-trading/1001316.htm?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261109/15894292795158528.html · https://news-static.webullfintech.com/us/news-html/20261110/15899876475269120.html
