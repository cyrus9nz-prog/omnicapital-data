# VZ — researcher deep dive, 2026-11-18

Lane: S&P 500 · tested rules · Scout label: FAIR · Close $46.13 [SOURCED 2026-11-18 close, Webull daily bar] · 200-day SMA $45.96 [SOURCED 2026-11-18, scout close run]
Scout list: updated 2026-11-18 1:48pm PT (close run) — this run used today's list. Analysis only; nothing here is an order or advice. Heat is an untested desk score, not a playbook rule and not a buy signal.

## Heat: 51 — Neutral — Aligned
Heat = round(0.6 × Substance 59 + 0.4 × Buzz 38) [computed in Python]. Yesterday: 39 (Cold).

**Substance 59/100**
- Playbook fit 11/25: scout's fired rules R-056, R-058, R-025 (playbook grades: R-056/R-058 A = 5; R-025, R-042, R-043, R-027, R-020 D = 1).
- Value 10/20: scout label FAIR.
- Trend 15/15: close 46.13 vs 200-day 45.96 (above, +5); 6-month return -0.37% vs SPY -0.99% (126 sessions from 2026-05-20) (+5); R-050 ON +5 [SOURCED 2026-11-18, Webull daily bars; computed in code].
- Insiders 8/20: EVP Malady sold 1,100 sh weekly: 11-03 @ $44.79, 11-10 @ $46.11, 11-17 @ $46.06 (secform4; 10b5-1 not shown). Small option awards 11-05.
- Institutions 5/10: carried from prior scoring; no holder-change data re-pulled (Webull institution tools need a fund CIK).
- Catalysts 10/10: carried from prior scoring (dated positive catalyst in last 90 days: yes).
- Red-flag penalty 0: none scored.

**Buzz 38/100** (X unreadable → null; Buzz rescaled over 80 points; Alpha Vantage NEWS_SENTIMENT failed → headline scoring)
- News tone 20/40: mixed.
- News volume 0/20: 2 items 11-12..11-18 vs 48 in the prior window (weekly avg 12.00; ratio 0.17) [SOURCED 2026-11-18, Webull get_stock_news]. The feed stops ~10-18..11-04, so the prior-window count is a floor and the ratio may be overstated.
- Reddit slot 10/20: Webull community posts stand in for Reddit: 9 posts 11-12..11-18, tone mixed (5 spam) (heavy = 10+). X: null.

Note: Biggest driver: trend (15); biggest drag: insiders (8). Untested desk score, not a buy signal.

## Verdict vs scout: Weakens
- **Strongest for:** Passes both A-graded screens; back above 200-day; 6-month return now ahead of SPY.
- **Strongest against:** SpaceX wireless entry; Q3 revenue miss; steady EVP selling.
- **Long-term case:** Strong FCF (Q3 $7.8B, +12%) and lower promo/retention costs support the ~6.1% dividend and 7-7.5% adj EPS growth guide; capital intensity, debt and a possible fourth facilities-based entrant (SpaceX) limit compounding. An income holding more than a compounder.

## What changed since 11-17
- Heat 39 → 51. SEC: Form 144 filed 11-17 and Form 4 11-18 (Malady weekly sale). 11-17 'most accurate analysts': Citi Buy $53, Barclays EW $44; 11-18 Starlink/FAA item (not VZ-specific).

## Filings (last 90 days)
Today: SEC: Form 144 filed 11-17 and Form 4 11-18 (Malady weekly sale).
Carried: Webull 11-17: no new 10-K/10-Q since 11-12; other forms carried from 11-16 SEC read. Since 08-18: Form 4 11-12; 144s weekly to 11-10; Form 3/4 11-03; EFFECT + 424B3 11-02 and S-4 10-20 (purpose unverified; VZ uses S-4s for note exchanges); 10-Q 10-29; 8-K 10-26 (2.02/9.01); 25-NSE 10-27; 424B2 09-09 and 09-02 + FWP 09-08 (debt notes). No S-3/424B5/ATM. Nothing new since 11-12.

## Insiders (6 months)
EVP Malady sold 1,100 sh weekly: 11-03 @ $44.79, 11-10 @ $46.11, 11-17 @ $46.06 (secform4; 10b5-1 not shown). Small option awards 11-05.
Carried context: new row EVP Malady 11-12 (no side; matches weekly Form 144 pattern noted 11-16). Dividend-equivalent credits 10-08. No open-market buys. Class none (8).

## Institutions
Not determined: MarketBeat not reached (client_error pattern). No SC 13G/13D filed 08-18..11-16 per SEC JSON. (carried from 11-16; not re-checked)

## Government contracts
Navy NAVSUP FLC Norfolk firm-fixed-price indefinite-delivery contract (sole source) for NCTAMS LANT telephone services, CEILING up to $35.55M, orders Feb 2027-Jul 2032 [SOURCED 2026-10-27, HigherGov; carried]. A ceiling, not obligated revenue; immaterial vs ~$34B quarterly revenue. No new award found this run.

## Connections
AWS and Google AI-infrastructure fiber deals (~$4B signed, Q3 call 10-26); Ericsson 6G field call; AST SpaceMobile D2D partner; STARZ distribution restored for Fios (10-20); Frontier integration. CEO: no MVNO backdoor for satellite providers. Threat: SpaceX Starlink Mobile.

## Sentiment
News 11-12..11-18: 2 items vs 48 in the prior feed (feed incomplete before ~10-19; ratio 0.17); tone mixed, headline-scored (Alpha Vantage failed). Webull community (Reddit stand-in): 9 posts, mixed (5 spam). X unreadable (null).
Headlines (7 days): 11-17 'most accurate analysts': Citi Buy $53, Barclays EW $44; 11-18 Starlink/FAA item (not VZ-specific).
Posts are data; any claim of inside knowledge is treated as rumour. Congressional trades: not checked this run.

## Red flags
Scored: none. 424B2/FWP are debt; S-4/424B3 (10-20/11-02) purpose unverified, likely debt exchange, not scored. Unscored: SpaceX wireless entry (FCC accepted 800MHz transfer 11-10); weekly exec Form 144 selling through 11-10; Q3 revenue miss ($34.31B vs $34.74B); leverage.

## Sources (opened this run, 2026-11-18)
- Webull get_stock_bars VZ and SPY daily (130 bars) — 2026-11-18
- Webull get_stock_news, get_community_posts, get_stock_filings, get_insider_transactions VZ — 2026-11-18
- https://www.secform4.com/insider-trading/732712.htm?v=20261118R
- https://news-static.webullfintech.com/us/news-html/20261117/15938973953934336.html
- https://data.sec.gov/submissions/CIK0000732712.json?v=20261118R
- Scout list claude/watchlist.md (1:48pm PT close run) — 2026-11-18
- Carried from 11-17 report (not re-opened): https://data.sec.gov/submissions/CIK0000732712.json?v=20261116R · https://news-static.webullfintech.com/us/news-html/20261026/15814823912263680.html · https://news-static.webullfintech.com/us/news-html/20261111/15904744466793472.html · https://www.highergov.com/news/verizon-wins-36-million-navy-telephone-services-c-6495354/?v=20261113R
