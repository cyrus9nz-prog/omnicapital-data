# Notes — Mourya, Leipold, Adhikari, Contextual Quantum Neural Networks for Stock Price Prediction (Sci Rep 2026, article in press) — read 2026-11-09 in chat.
p.1      Licence page (CC BY-NC-ND); unedited early-access manuscript.
p.2–3    Quantum ML to predict next-step return distributions for several stocks at once; new training trick (quantum batch gradient update) and a multi-task circuit ("share-and-specify"). Data: S&P 500 prices for 4 mega-caps (Apple, Google, Microsoft, Amazon). Claim: multi-task beats single-task by capturing cross-asset correlation.
p.4–5    Preprocessing: price differences (returns) then moving-average smoothing; returns quantised to up/down bits (d = 2), predicting one step ahead (τ = 1).
p.5–9    Circuit/training mechanics (parameter shift, SPSA, fidelity/SWAP loss, loading the context distribution once). No trading rule, no costs, no P&L.
p.9–10   Multi-asset architecture (shared + asset-specific gates, label qubits).
p.11     4-asset control circuit; sequential (multi-step) prediction idea is future work.
p.12     Test setup: Apple daily prices, 10,033 points, weekly-averaged with 1-day stride → 10,029 samples; 80/20 train/test split; 3-day context → next-step up/down; 3000 epochs, seed 42. (Systematic test of DISTRIBUTION FIT, not of trading.)
p.13     Table I: multi-task models fit the conditional up/down distributions better (lower KL divergence) than single-task for Apple and Google, with half the parameters. Authors state plainly that classical deep models (Transformers, LSTMs) outperform near-term quantum models on large-scale price forecasting; accuracy is not their main KPI.
p.14     Scaled to 4 then 8 stocks (AAPL, GOOG, MSFT, AMZN, PEP, WDC, TXN, IBM), same parameter count; MSE loss with SPSA failed to fit — fidelity (SWAP) loss used throughout.
p.16     4-level quantisation experiment; simulated hardware noise raises KL divergence (gate noise worse than readout noise).
p.17–19  Conclusion, references. Data available on request only.
END OF BOOK reached p.19.
Rules: none — the output is a fitted probability of up/down moves, with no entry/exit, no costs, no out-of-sample trading result. Principles: 2 (process).
