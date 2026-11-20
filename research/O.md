# O — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $58.28 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $60.22 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 40 — Neutral — Aligned
Heat = round(0.6 × Substance 34 + 0.4 × Buzz 50) [computed in Python]. Yesterday: 40 (Neutral).

**Substance 34/100**
- Playbook fit 6/25: scout's fired rules R-058, R-042 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 5/15: close 58.28 vs 200-day 60.22 (below, 0); 6-month return -3.80% vs SPY -0.99% (126 sessions from 2026-05-20) (0); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: No rows after 09-10 (McLaughlin sold 3,475 @ $60.15). No buys.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 10/10: carried from prior scoring (dated positive catalyst in last 90 days: yes).
- Red-flag penalty -10: see Red flags (scored item carried).

**Buzz 50/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 30/40: positive (1 item).
- News volume 0/20: 1 items 11-12..11-18 vs 14 in the prior window (weekly avg 3.50; ratio 0.29) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 10/20: Webull community posts stand in for Reddit: 6 posts 11-12..11-18, tone mixed (heavy = 10+). X: null.

Note: Biggest driver: catalysts (10); biggest drag: playbook fit (6); red-flag penalty -10. Untested desk score, not a buy signal.

## Verdict vs scout: Confirms
- **Strongest for:** Wells Fargo PT $61 vs $58.28; 5.6% monthly yield.
- **Strongest against:** Below 200-day ($60.22); ATM dilution (scored); new 8-K 5.02 leadership change unread.
- **Long-term case:** A slow compounder: monthly dividend (~5.6% yield) plus ~3-4% AFFO/share growth from buying net-lease assets at ~170bp spreads; Europe, credit and the KKR JV widen the funnel. Size, cost of capital and steady ATM issuance cap per-share growth, so returns are mostly yield.

## What changed since 11-17
- Heat 40 → 40. SEC: 8-K filed 11-17, items 5.02/7.01/9.01 (officer/director change; not opened). 11-16 Wells Fargo EW, PT raised to $61.

## Filings (last 90 days)
Today: SEC: 8-K filed 11-17, items 5.02/7.01/9.01 (officer/director change; not opened).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: 8-K 11-06 (5.02/9.01, not opened); 10-Q 11-03; 8-K 11-02 (2.02/7.01/9.01); Form 4 + 144 09-10; 8-K 08-25 (8.01/9.01). No S-3/424B/13G/13D; nothing new since 11-06 [SOURCED 2026-11-16, SEC submissions]. ATM: 150M-share program (est. 2026-05-07) actively used.

## Insiders (6 months)
No rows after 09-10 (McLaughlin sold 3,475 @ $60.15). No buys.
Carried context: no rows after 09-10 (McLaughlin sold 3,475 @ $60.15). Redington 240 @ $63.12 (06-27). No buys. Class none (8) per prior scoring.

## Institutions
Not determined: MarketBeat client_error pattern (not retried for O this run after VICI failed). No SC 13G/13D filed 08-18..11-16 per SEC JSON. (carried from 11-16; not re-checked)

## Government contracts
None found; not a plausible federal contractor (net-lease REIT).

## Connections
KKR paid EUR 528M for 49% of an unlevered JV of 54 European assets (11-02; O can call KKR's stake in years 10-17). Q3 invested ~$2.6B at 6.8% cash yield: $940M Europe at 7.1%, $250M credit investments; 53% investment-grade clients; $5.4B liquidity. Top-tenant % not obtained.

## Sentiment
News 11-12..11-18: 1 items vs 14 in the prior feed (feed incomplete before ~10-19; ratio 0.29); tone positive (1 item), headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 6 posts, mixed. X unreadable (null).
Headlines (7 days): 11-16 Wells Fargo EW, PT raised to $61.
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
SCORED dilution: 150M-share ATM program (est. 2026-05-07, direct or forward sales) actively used: ~$470M settled in Q3 plus $1.1B unsettled forward equity at $60.61 (Q3 call). Unscored: $1.0B 3.75% convertible notes (Aug, debt), net debt/EBITDA 5.4x, rate sensitivity, 8-K 11-06 (5.02) not opened. New unscored: 8-K 5.02 filed 11-17, not opened.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars O and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions O — 2026-11-18
- https://news-static.webullfintech.com/us/news-html/20261116/15933987985223680.html
- https://data.sec.gov/submissions/CIK0000726728.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0000726728.json?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261116/15933987985223680.html · https://news-static.webullfintech.com/us/news-html/20261102/15856728873737216.html · https://www.boerse-express.com/news/articles/realty-income-aktie-150-millionen-atm-programm-gestartet-902867
