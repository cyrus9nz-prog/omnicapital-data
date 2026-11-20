# Notes — LopezLira (The Predictive Edge, 2024) — run 2026-11-16 (second run of the day; budget left ≈51,700 words after Broker)
## p.4–36 (front matter, preface, intro)
- Book built on author's April 2023 paper with Yuehua Tang: ChatGPT scores news headlines good/bad for a stock; long positive / short negative. Author claims >400% simulated return over ~18 months vs ~10%/yr market [p.19, p.20]. Simulated, not traded. Look-ahead bias said to be addressed (p.31). Details in Ch.6–7.
- No rules in front matter.
## p.37–57 (Ch.1 market basics)
- Primer only; no rules. Order-type definitions (stop becomes market order; fills can gap below trigger) p.49 — principle-level, already common.
- Claim: small caps are traded less by active managers due to costs, so their returns are "easier to predict" p.47 — D assertion (no study cited here). Possible principle.
- Fundamental-analysis limits (subjective intrinsic value, book value misses intangibles, earnings forecasts unreliable) p.51–52 — D.
- Technical analysis: author notes academic skepticism; suggests it may work only via self-fulfilling herding p.53–54; limits listed p.54–56 — D principle.
## p.58–82 (Ch.1 end, Ch.2 start)
- Sentiment analysis limits: context (e.g. R&D cost cut read as positive), overreliance, speed vs HFT — by the time a slow trader acts, price may already have moved p.59–60 — D principle (speed decay of news signals).
- Passive indexing called the most recommended approach p.62 — D.
- Short-sale worked example arithmetic garbled ($105 repay, $110−$95−$10) p.64 — flag, not carried.
- Performance metrics defined (alpha, beta, Sharpe, Sortino, max drawdown) p.66–68 — definitions; useful for desk evaluation, principle-level: judge strategies on risk-adjusted return + drawdown, not raw return.
- Ch.2 AI primer p.74–82: no rules.
## p.83–102 (Ch.2 AI history, ML types)
- No rules. Principle candidate: supervised and reinforcement-learning models trained on price history fail in finance because markets are non-stationary — investors adapt, so only recent data is relevant and long stable training sets don't exist p.98, p.99–100 — D (author's view, no study cited here). Agrees with Chhibber/Mourya principles.
## p.103–128 (Ch.2 end, Ch.3 NLP/LLM primer)
- No rules. NER over 10-K/10-Q to track new facilities, suppliers/subsidiaries appearing or dropping off p.116–117 — idea only, D; no test.
- Financial jargon and central-bank ambiguity are hard for NLP p.115 — D.
## p.129–153 (Ch.3 end, Ch.4 start)
- No rules. Principle: LLM output used for investing can hallucinate plausible data and trends; verify outputs with a second check or human review before acting p.134–135 — D (consistent with desk's SOURCED-tag policy).
## p.154–177 (Ch.4 end, Ch.5 ChatGPT capabilities)
- No rules. LLM landscape list dated (2023). Principle: LLMs fail on long multi-step causal reasoning; break tasks into small steps p.177 — D.
- Words read through p.153 ≈ 25,176.
## p.178–204 (Ch.5 limitations, prompting)
- No rules. Process principles: give the model the source text (e.g. the press release) rather than asking it to recall or browse p.182, p.184; ask unambiguous closed questions ("is the price likely to go up?") rather than open "prospects" p.180–181; check outputs, since LLMs can invent statistics and backtests p.183 — D. Agrees with existing desk SOURCED-tag policy.
- Prompt Engineering Canvas (author's own framework) p.193–204 — tooling, out of desk rule scope.
## p.205–233 (Ch.5 end; Ch.6 the study)
- Ch.6 = Lopez-Lira & Tang (2023) study. Data: CRSP daily returns, all NYSE/NASDAQ/AMEX common stocks with news; web-scraped headlines matched to RavenPack by timestamp/title; high relevance score only; full articles/press releases, excluded stock-move items; de-duplicated p.225–227. Look-ahead: vendor timestamps within ms of release p.227.
- Method: LLM asked (persona: financial expert) to answer YES/NO/UNKNOWN whether a headline is good/bad for the named company's stock in the short/long term, then one sentence; temperature 0 p.227–230. Scores +1/0/−1, averaged per stock-day p.231. Timing: pre-open news → that day's return; intraday news → to end of next day; after-close → next day p.231. Regression of next-day return on score with stock and time controls p.231. Compared with BERT, GPT-1, GPT-2 p.231.
- Strategy: zero-cost long positive / short negative, entered at open or close depending on news time, held one day/overnight p.231–232.
- Results: author reports GPT-3.5 long-short ~550% Oct 2021–Dec 2022 BEFORE costs; GPT-4 lower return, lower volatility and drawdown; short leg ~250%; stays positive under modest costs, falls with higher costs p.233. (Note: p.19/20 says >400% over ~18 months — figures differ by section.) → grade A for the test (defined rules, universe, period, out-of-sample relative to model training cutoff?) — check later pages for sample size/period and model cutoff.
- Example: headline about a competitor fined judged positive for the named company — context beats word-level sentiment p.229–230.
## p.234–255 (Ch.6 end; Ch.7 start)
- GPT-3.5/4 beat GPT-1/2 and BERT; GPT-4 spread picks across more names (lower volatility); newer models did as well or better on hard-to-read (low-readability) news, older ones worse p.234.
- Short leg (bad news) strongest; author still recommends combining long and short p.240.
- Ch.7: buy positive-news stocks, short negative-news stocks if allowed; hedge to market-neutral with an index if needed p.244–245. Author: any edge has a limited lifespan as others adapt; treat as starting point p.245 — principle (strategy decay).
- Where edges persist: illiquid/small/excluded corners institutions can't trade (market impact, mandate limits), and information asymmetry from alternative data p.246–248 — D principle.
- Selection criteria: (1) relevance — company-specific material news (M&A, product launch, regulatory approval, earnings) over general industry items; (2) strength/clarity — strong positive/negative more actionable than mixed; (3) consistency over time more than one-off p.255 — D (no test of these filters shown).
- Set success criteria (return, volatility, alpha) and review regularly p.254 — principle.
## p.256–277 (Ch.7 body)
- Focus on smaller, less liquid stocks: author says they underreact to news because institutions avoid them; retail can trade them with less impact; costs/spreads higher — check they don't eat the edge p.256 — D/B (no test shown here; consistent with p.47).
- Smaller allocation per illiquid name; monitor closely p.257.
- Rebalancing horizon: too frequent → costs; too long → no longer trading the signal p.257–258 — principle.
- Corroborate sentiment with price history, trend and financial metrics before trading p.259 — D.
- Position cap per stock (long or short) at a fixed % of portfolio, examples 1/2/5/10%; trim when a winner exceeds the cap p.260 — D (merge candidate with existing caps).
- Inverse-variance weighting: weight each position ∝ 1/historical variance, within the cap p.261 — D (no test shown).
- Backtest: avoid overfitting; evaluate return, volatility, Sharpe, max drawdown vs a benchmark; test across periods p.262–265 — principle; the 5-year backtest p.264 is hypothetical ("let's consider"), no results.
- Automation rule examples: long on strong positive only if weight ≤1%; 5% stop on any position; sector cap; alerts p.267 — D, illustrative.
- Sector concentration from clustered news → cap sector or hedge with index p.270–271 — D.
- Crowding: many traders using similar AI tools could homogenise and amplify moves p.272 — D principle.
## p.278–299 (Ch.8)
- Combining sentiment with momentum: positive momentum + negative sentiment → flag as riskier; positive momentum + strong positive sentiment → stronger candidate; building positive sentiment may lead momentum p.282–284 — D, hypothetical firm example, no test. Merge candidate with R-098 (12-month momentum).
- Risk use: a growing negative-sentiment shift on a holding → review with price/volume, may reduce p.285–288 — D; illustrative scenario with a hindsight "outcome" (invented example, not evidence).
- Order type in volatile conditions: spreads widen, market orders risk fills outside the quote → prefer limit orders p.290 — D principle.
- Risks: over-reliance, homogenisation/echo chambers, feedback loops amplifying errors (fake articles), stale training data — feed current info in the prompt, model obsolescence p.292–299 — D principles.
## p.300–305 (Ch.8 end)
- Black-swan / regime-break: models trained on history lose power in novel conditions; keep human override p.300–301 — D principle.
stopped p.305 (day budget reached: 120,000 − 68,247 Broker = 51,753; read ≈51,400 words through p.305). Resume at p.306 (Ch.9).
