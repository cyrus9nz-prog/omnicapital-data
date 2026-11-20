# Signals — 2026-11-17 (after-close trader run, Tuesday)

Paper signals under the desk's rules; nothing here is an order or advice. Prices: Webull daily bars (regular session), close 2026-11-17 [SOURCED 2026-11-17, Webull get_stock_bars]. Regime: R-050 ON (SPY 50-day SMA 762.89 > 200-day 729.79 through 11-17 [SOURCED 2026-11-17, Webull SPY daily bars; computed in code]; SPY closed 732.44). Account $1,000; tiers core $15 (tested lane), speculative $10 (small/mid). R-044 colours computed in code (SlowStoch 14,3,3; RSI 7; MACD 12,26,9) and reproduce the 11-16 ledger values for ACGL. Labels recomputed at the 11-17 close from the scout's 11-17 midday fair-value methods [ESTIMATED]. Researcher reports dated 2026-11-17 (dashboard dataset). No ledger call is past its review date yet.

## Today's ratings

| Ticker | Lane | Rating | Verdict | Price | Trigger / exit / level that would make it a buy | Stop | Target | Shares | Risk $ | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|
| PFE | S&P 500 | BUY | LONG-TERM BUY ZONE | $28.47 | at-price: opened at the 2026-11-17 close 28.47 (≤ $28.63 low end of fair value) | 24.16 | 37.09 | 3 | 12.93 | C-0081 |
| RYTM | Small/mid | BUY | LONG-TERM BUY ZONE (swing entry: R-044 buy-stop) | $116.61 | buy-stop 118.51 (R-044, $0.01 above the 2026-11-17 first aligned bar high 118.50) | 108.76 | 138.0 | 1 | 9.75 | C-0082 |
| ADMA | Small/mid | BUY | LONG-TERM BUY ZONE (swing entry: R-044 buy-stop) | $13.63 | buy-stop 13.67 (R-044, $0.01 above the 2026-11-17 first aligned bar high 13.655) | 12.76 | 15.48 | 10 | 9.1 | C-0083 |
| O | S&P 500 | SELL NOW | AVOID | $58.04 | none (AVOID) | — | — | — | — | C-0084 |
| OXY | S&P 500 | HOLD | LONG-TERM WATCH (position P-0005 open) | $56.52 | open since 2026-11-13 close 58.75; no exit triggered | 50.56 | 75.14 | 1 | 8.19 | C-0085 |
| ACGL | S&P 500 | HOLD | LONG-TERM WATCH | $109.22 | P-0007 cancelled (R-044 black bar 11-17 before fill); next R-044 first aligned bar or close ≤ $91.84 | — | — | — | — | C-0086 |
| HIG | S&P 500 | HOLD | LONG-TERM WATCH | $136.22 | next R-044 first aligned bar or close ≤ $123.61 | — | — | — | — | C-0087 |
| EOG | S&P 500 | HOLD | LONG-TERM WATCH | $154.91 | next R-044 first aligned bar or close ≤ $147.28 | — | — | — | — | C-0088 |
| APA | S&P 500 | HOLD | LONG-TERM WATCH | $46.88 | close ≤ $31.58 (low end of fair value) | — | — | — | — | C-0089 |
| CF | S&P 500 | HOLD | NO ACTION | $119.34 | next R-044 first aligned bar (would make 3 rules) | — | — | — | — | C-0090 |
| VICI | S&P 500 | HOLD | NO ACTION | $24.51 | close above the 200-day $26.07 plus an R-044 first aligned bar | — | — | — | — | C-0091 |
| PRU | S&P 500 | HOLD | LONG-TERM WATCH | $122.34 | P-0006 closed at the 11-17 open 122.56; next R-044 first aligned bar or close ≤ $103.66 | — | — | — | — | C-0092 |
| DOC | S&P 500 | HOLD | NO ACTION | $19.46 | next R-044 first aligned bar (would make 3 rules) | — | — | — | — | C-0093 |
| OKE | S&P 500 | HOLD | LONG-TERM WATCH | $88.55 | close ≤ $69.56 or next R-044 first aligned bar; STRONG BUY blocked by dilution flag | — | — | — | — | C-0094 |
| AMCR | S&P 500 | HOLD | NO ACTION | $43.45 | next R-044 first aligned bar (would make 3 rules) | — | — | — | — | C-0095 |
| T | S&P 500 | HOLD | NO ACTION | $22.29 | close above the 200-day $24.36 with a live R-044 buy-stop | — | — | — | — | C-0096 |
| VZ | S&P 500 | HOLD | NO ACTION | $45.93 | close back above the 200-day $45.95 plus an R-044 first aligned bar | — | — | — | — | C-0097 |
| UPS | S&P 500 | HOLD | NO ACTION | $110.31 | next R-044 first aligned bar after a non-green bar (would make 3 rules) | — | — | — | — | C-0098 |
| NBIX | Small/mid | HOLD | LONG-TERM BUY ZONE | $165.92 | fits no tier: below the $223.09 low end of fair value, but R-061's 20% stop ($33.18/share) exceeds the $10 tier; swing path: next R-044 first aligned bar (1.5×ADR(7) $7.64 fits 1 sh) | — | — | — | — | C-0099 |
| TGTX | Small/mid | HOLD | NO ACTION | $62.71 | next R-044 first aligned bar (would make 3 rules) | — | — | — | — | C-0100 |

## Paper positions (open first, then pending, then closed/cancelled)

| ID | Ticker | Status | Opened | Entry (fill or trigger) | Stop | Target | Shares | Cost $ | Last | Return % | SPY % same days | Invalidation / exit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P-0005 | OXY | open | 2026-11-13 | 58.75 | 50.56 | 75.14 | 1 | 58.75 | 56.52 (2026-11-17) | -3.8 | -2.91 | Stop 50.56; exit if R-056 fails/top 6 lost, R-050 OFF, researcher Contradicts, or label below UNDERVALUED (above $69.86); review 2027-02-13 |
| P-0008 | PFE | open | 2026-11-17 | 28.47 | 24.16 | 37.09 | 3 | 85.41 | 28.47 (2026-11-17) | 0.0 | 0.0 | Stop 24.16 (R-169); exit if R-058 fails or leaves the top 10, R-050 OFF, researcher Contradicts, or a dividend cut; review 2027-02-17 |
| P-0009 | RYTM | pending | 2026-11-17 | 118.51 | 108.76 | 138.0 | 1 | 118.51 | 116.61 (2026-11-17) | — | — | Black bar before fill cancels; stop 108.76 (R-045 1.5×ADR7 6.4975); black bar after fill → next open; 20-trading-day time stop |
| P-0010 | ADMA | pending | 2026-11-17 | 13.67 | 12.76 | 15.48 | 10 | 136.7 | 13.63 (2026-11-17) | — | — | Black bar before fill cancels; stop 12.76 (R-045 1.5×ADR7 0.6045); black bar after fill → next open; 20-trading-day time stop |
| P-0001 | UHS | closed 2026-11-13 | 2026-11-11 | 198.27 | 188.05 | 218.71 | 1 | 198.27 | 192.15 (2026-11-13) | -3.09 | 0.81 | R-044 black bar 2026-11-12 → closed at the 2026-11-13 open (SELL) |
| P-0002 | INCY | closed 2026-11-13 | 2026-11-11 | 123.09 | 116.32 | 136.64 | 1 | 123.09 | 121.89 (2026-11-13) | -0.97 | 0.81 | R-044 black bar 2026-11-12 → closed at the 2026-11-13 open (SELL) |
| P-0003 | ADMA | closed 2026-11-17 | 2026-11-11 | 13.29 | 11.96 | 15.94 | 7 | 93.03 | 13.34 (2026-11-17) | 0.38 | -2.07 | R-044 black bar 2026-11-16 → closed at the 2026-11-17 open 13.34 (SELL) |
| P-0006 | PRU | closed 2026-11-17 | 2026-11-13 | 124.34 | 119.8 | 133.41 | 3 | 373.02 | 122.56 (2026-11-17) | -1.43 | -1.5 | R-044 black bar 2026-11-16 → closed at the 2026-11-17 open 122.56 (SELL); stop 119.80 not touched at the open |
| P-0004 | CVS | cancelled 2026-11-13 | 2026-11-12 | 90.34 | 84.85 | 101.32 | 2 | 180.68 | 89.35 (2026-11-13) | — | — | R-044 black bar 2026-11-13 before fill (high 89.92 < 90.34 trigger) → buy-stop cancelled |
| P-0007 | ACGL | cancelled 2026-11-17 | 2026-11-16 | 111.93 | 108.82 | 118.14 | 4 | 447.72 | 109.22 (2026-11-17) | — | — | R-044 black bar 2026-11-17 before fill (high 110.615 < 111.93 trigger) → buy-stop cancelled |

SPY same-days returns [SOURCED 2026-11-17, Webull SPY daily bars]: ADMA 11-12 open 753.98 → 11-17 open 738.39; PRU 11-16 open 749.66 → 11-17 open 738.39; OXY 11-13 close 754.37 → 11-17 close 732.44. Returns before costs.
Paper cash after open and pending positions: $600.63 ($1,000 − OXY 58.75 − PFE 85.41 − RYTM 118.51 − ADMA 136.70).

**Record:** 2 open, 2 pending, 4 closed (1 winner), 2 cancelled; closed average -1.28% vs SPY -0.49% over the same days; open average -1.9% vs SPY -1.46% (before costs).
