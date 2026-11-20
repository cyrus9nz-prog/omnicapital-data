# Run report — 2026-11-10 — Heitkoetter, The PowerX Strategy, 2nd ed. (2019)
Read: loc.69/69 (END OF BOOK), in order, in chat.
Rules added: 6. swing-technical 1 (R-044 PowerX first aligned bar, C); risk/sizing 3 (R-045 ADR stop 1.5× / target 3×, C; R-047 fixed-ratio risk step-up, D; R-049 account circuit breaker, D); options-directional 1 (R-046 in-the-money option 30–45 days managed on the stock, C); process 1 (R-048 40 paper trades + 4 profitable weeks, D).
Merged: R-009 (2% while starting), R-010 (exactly 2:1), R-023 (first signal only), R-034 (in-the-money strike), R-040 (≤5% of funds per trade). Principles: 10 new, 3 agreements.
Conflicts: R-047 vs R-009 (step risk above 2% after a track record); R-046 vs R-010 (option leg about 1.7:1).
Flags: vendor book selling software and coaching; hypothetical-performance disclaimer (loc.2); chart examples only; all growth figures are projections; tax remarks not carried.
Test first: R-044 with R-045. Every input is in daily OHLC and the rules are mechanical, so a backtest needs no judgement calls. The author's only evidence is chart examples.
