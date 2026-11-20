# Workflow A ingest: Fisher (Philip A. Fisher, "Common Stocks and Uncommon Profits and Other Writings", 2015 Wiley ed.)

Book parts by loc: Ken Fisher's preface and introduction loc.3–37 (2003; mostly biography) · Part One, Common Stocks and Uncommon Profits loc.38–174 (1958, revised 1960) · Part Two, Conservative Investors Sleep Well loc.175–215 (1975) · Part Three, Developing an Investment Philosophy loc.216–263 (1980; appendix loc.261–263) · index loc.264–267.
Checked against the local copy of the playbook (/home/claude/pb/playbook.md; next ID R-234). instructions.md could not be read in this session (no Projects tool), so the WORKFLOW A rules were taken from the task brief and the playbook header.

## New rules

### R-NEW1 Cycle-peak EPS test: hold or sell a growth holding
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a holding's expected per-share EPS at the next business-cycle peak (adjusted for splits and stock dividends, not for shares issued to raise capital) will not be up from today's EPS by at least as much as today's EPS is up from EPS at the last cycle peak, OR multi-year sales and EPS growth has slowed to about the economy's rate with no new product line in sight THEN sell; otherwise hold | EXIT the rule is the exit; when the cause is an exhausted market rather than weaker management, sell gradually (part can wait for a replacement), and capital-gains tax should not block the sale | INVALIDATED BY today's EPS sitting at a cyclical trough (use R-112 instead)
Inputs: EPS history → 10-K/10-Q; last cycle-peak year → NBER business-cycle dates; forward EPS → desk forecast or consensus; split and stock-dividend factors → price data; nominal GDP growth → BEA/FRED
Sources: [BOOK Fisher loc.111] (Part One); [BOOK Fisher loc.110] (Part One); agrees: [BOOK Fisher loc.260] (Part Three, point 3: hold until growth no longer beats the economy)
Evidence: D — the book states the test with no cases or tally
Conflicts: none yet (related R-188, which covers flat earnings)
Status: UNTESTED

### R-NEW2 No promotional companies: 2–3 years of commercial sales and a year of operating profit first
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company has fewer than about 2–3 years of commercial operations OR has not yet reported one full year of operating profit THEN don't buy it; leave such financing to venture groups that can supply management | EXIT n/a (a filter) | INVALIDATED BY n/a
Inputs: first year of commercial revenue → S-1/10-K business history; operating income by fiscal year → 10-K
Sources: [BOOK Fisher loc.126–127] (Part One)
Evidence: D — reasoned argument with no cases
Conflicts: R-127 — decided by sleeve (see Conflicts); complementary with R-107 (listing age, not operating history)
Status: UNTESTED

### R-NEW3 Outside CEO at a large company: no new buying, re-underwrite the holding
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a large, established company names a chief executive recruited from outside THEN read it as a sign that something was badly wrong with the existing management, whatever recent earnings show: make no new purchases, re-run the full quality review on a holding (and check what in your own process missed it) | EXIT sell at once, whatever the market outlook or the tax, if the review confirms management has deteriorated | INVALIDATED BY a later record of the new chief building an internal team (the stock can qualify again)
Inputs: CEO appointment and prior employer → 8-K Item 5.02, proxy biographies (DEF 14A)
Sources: [BOOK Fisher loc.184] (Part Two); [BOOK Fisher loc.262] (Part Three appendix: outside CEO recruitment is a dangerous sign); [BOOK Fisher loc.110] (Part One: sell at once on management deterioration)
Evidence: D — author's observation; the claim that senior outside hires often leave within a few years comes with no statistics (loc.184)
Conflicts: R-131 and R-198 — decided by school and starting point (see Conflicts)
Status: UNTESTED

### R-NEW4 CEO pay far above the next executives: one-man-management flag
School: process | Horizon: long-term (years) | Instrument: shares
IF the proxy's summary compensation table shows the top executive paid very much more than each of the next two or three THEN flag one-man management (depth and succession risk, counted against Points 8–9 and R-233); pay that steps down gradually is no flag | EXIT n/a (a flag) | INVALIDATED BY n/a. The book gives no ratio; the desk sets one as a test parameter (e.g. CEO pay at least 2× the next highest)
Inputs: named-executive total pay → DEF 14A summary compensation table
Sources: [BOOK Fisher loc.185] (Part Two)
Evidence: D — the book offers it as a clue, untested; it says the flag tells nothing about how good the team is
Conflicts: none yet (complementary with R-233)
Status: UNTESTED

### R-NEW5 Operating-margin leader by a modest, lasting gap
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF operating margin measured over a run of years (not one year) is at or near the top of the company's industry AND it leads the next-best competitor by a modest margin (the book: 2–3 points of sales is enough; a margin many times the industry's invites entry) THEN favour the company as a long-term candidate; IF it is one of the lowest-margin (marginal) firms in its industry THEN don't hold it long-term | EXIT the margin lead is lost over several years | INVALIDATED BY a low margin deliberately caused by R&D and promotion well beyond what normal growth needs (R&D ÷ sales and selling ÷ sales clearly above peers, gross margin at or above peers), or margins improving through a real internal change (efficiency, new products) and not only through volume; those cases may still qualify
Inputs: operating margin for 5+ years, company and peers → 10-K; R&D ÷ sales, SG&A ÷ sales, gross margin → 10-K
Sources: [BOOK Fisher loc.66–67] (Part One); [BOOK Fisher loc.199] (Part Two); [BOOK Fisher loc.193] (Part Two: for safety, use margin on sales; a 2% cost rise wipes out a 1% margin but only a fifth of a 10% margin); agrees: [BOOK Fisher loc.178] (Part Two: low-cost producer)
Evidence: D — author asserts most big gains in older companies came from broad-margin firms; no tally
Conflicts: R-231 — decided by purpose (see Conflicts)
Status: UNTESTED

### R-NEW6 Debottlenecking: small added capital, large added output, before earnings show it
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company whose plants are already profitable and fully running commits roughly 15% of their cost to raise output by roughly 40% with little added overhead AND the project is big enough to move company EPS AND the share price has not yet moved on it THEN buy before the extra output reaches reported earnings | EXIT the desk's long-term sell rules (R-NEW1, R-NEW9) | INVALIDATED BY demand not absorbing the added output (utilisation or selling prices falling)
Inputs: capex plan and capacity figures → 10-K, 8-K, investor presentations; utilisation → filings, industry data; price reaction since the announcement → price data
Sources: [BOOK Fisher loc.104] (Part One; capital-intensive chemical example)
Evidence: D — hypothetical arithmetic, no case
Conflicts: none yet (related R-204: an earnings rise not yet in the price)
Status: UNTESTED

### R-NEW7 War scare: buy slowly on the threat, faster on the outbreak
School: process | Horizon: long-term (years) | Instrument: shares
IF you had already decided to buy a stock AND a war scare knocks its price down THEN start buying, slowly and on a scale-down; IF fighting actually breaks out (US forces engaged) THEN buy noticeably faster; buy only companies whose demand holds in wartime or that can convert to war work | EXIT the desk's long-term sell rules | INVALIDATED BY a war the country could lose (the book: money and stocks would both lose their value)
Inputs: price → market data; dates of the scare and of the outbreak → news wires
Sources: [BOOK Fisher loc.146–148] (Part One); agrees: [BOOK Fisher loc.11] (Ken Fisher's introduction: his late-1990 buy columns during the Gulf war scare); agrees: [BOOK Wyckoff p.78] (prices more often bottom on the threat than on the event)
Evidence: C — author's survey of 20th-century wars (WWI, WWII, Korea) and about ten scares in 22 years, with no data table; Ken Fisher's own 1990 call
Conflicts: R-050 — decided by level and horizon (see Conflicts)
Status: UNTESTED

### R-NEW8 Three-year rule for a conviction holding
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF a holding bought on a fundamental thesis has not produced worthwhile results (total return at or below the market's) three years after purchase AND nothing learned since has changed the original view THEN sell it; before three years, lagging the market is no reason to sell | EXIT the rule is the exit | INVALIDATED BY the author's one exception: a candid management whose profits are depressed by a specific, identified spending programme that is being corrected (then hold or add)
Inputs: purchase date and total return vs S&P 500 → desk ledger, price data
Sources: [BOOK Fisher loc.232] (Part Three); [BOOK Fisher loc.233–234] (Motorola 1955: 5–10% below cost for over a year, then led the insurer's whole portfolio within three years); [BOOK Fisher loc.234–235] (Rogers: the one exception)
Evidence: C — author's own practice; the author says he can recall no sale made only under this rule that he later regretted (loc.234)
Conflicts: R-102 — decided by method (see Conflicts)
Status: UNTESTED

### R-NEW9 Hold a qualifying compounder through a high multiple or a feared bear market
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a holding still passes the quality review (fifteen points; management and growth intact) AND its P/E has run above its usual level (the book's example: 35× against a normal 25×) or a market decline is expected THEN hold; don't sell on the multiple, on a market forecast or because it has already risen a lot; IF the multiple is above what even strong fundamentals justify THEN keep it but put no new money in | EXIT only for the fundamental reasons: a mistaken thesis, deterioration (R-NEW3), growth exhaustion (R-NEW1) or a clear-cut better switch (R-NEW18) | INVALIDATED BY earnings stalling or an operating crack at the high multiple (→ R-187)
Inputs: P/E and its 5–10-year range → price data, 10-K EPS; quality review → desk checklist
Sources: [BOOK Fisher loc.112–117] (Part One); [BOOK Fisher loc.202–203] (Part Two: the risk ladder; legendary quality at too high a P/E = hold, no fresh buying); [BOOK Fisher loc.246–249] (Part Three: Texas Instruments fell 80% from its 1962 peak, then traded at more than double that peak; a client who sold in 1956 at a 125% gain saw the stock's 1960s low still almost 40% above his sale price)
Evidence: C — author's own cases; author claims that fewer than one in ten investors who sold ahead of a bear market got back in lower (loc.113)
Conflicts: R-187; R-119; R-061 — see Conflicts
Status: UNTESTED

### R-NEW10 Position caps at cost by company risk class
School: risk/sizing | Horizon: long-term (years) | Instrument: shares
IF building a long-term portfolio THEN cap each position at original cost by class: large, entrenched growth companies at most 20% each (so at least five names) with little product overlap between them; mid-sized established companies with team management (the book: $15–100 million of sales in 1959 dollars; rescale) 8–10% each, 8% for the riskier; small young companies at most 5% each, and only with money you can afford to lose. An individual holding more than about 20 names has too many (10–12 is usually better). Don't trim a holding because growth has raised its weight (the book: 40% after ten years is acceptable while the outlook holds; a small company that matures into the mid class can be held larger) | EXIT n/a (a sizing rule) | INVALIDATED BY n/a
Inputs: cost basis → desk ledger; revenue and market cap class → 10-K, price data; industry and product overlap → SIC/GICS codes, 10-K segment data
Sources: [BOOK Fisher loc.138–139] (Part One); [BOOK Fisher loc.144–146] (Part One); [BOOK Fisher loc.88] (Part One: example of up to 15% of a fortune in small young companies, or new savings only); [BOOK Fisher loc.260] (Part Three, point 6: more than 20 holdings shows incompetence; companies under $25 million of sales need wider diversification)
Evidence: D — guidance with no test
Conflicts: R-139; R-200; R-175 — see Conflicts
Status: UNTESTED

### R-NEW11 Long-term buys at the market; give block buys a price range
School: process | Horizon: long-term (years) | Instrument: shares
IF a stock has passed the long-term buy work AND the order is small next to normal trading THEN buy at the market rather than holding out for a fraction of a point; IF the order is a large block THEN give the broker the full size and discretion up to an agreed amount above the last sale, passing up small offerings that would draw competing bids | EXIT n/a | INVALIDATED BY n/a
Inputs: order size vs average daily volume → market data
Sources: [BOOK Fisher loc.135–137] (Part One: an investor held out for half a point and missed a stock that later sold above 500); [BOOK Fisher loc.237–238] (Part Three: a client's limit 3/4 point below the close missed a rise of over 50%; the author's own limit sell missed by a quarter point)
Evidence: C — anecdotes from the author and his clients
Conflicts: principle "Enter with limit orders…" [BOOK MetaStock p.10] and R-023 — decided by horizon (see Conflicts)
Status: UNTESTED

### R-NEW12 Value a long-run compounder at its own normal multiple of the market's P/E
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company has sold for many years at a steady multiple of the market's P/E (the book's case: about twice the Dow's for decades) AND the new-product flow that earned the premium is still visible THEN project its future price at that same relative P/E: twice the market's P/E with earnings doubling in five years is not discounting five years ahead; IF the coming earnings spurt is a one-time event THEN assume the relative P/E falls back to the market's | EXIT n/a (a valuation input) | INVALIDATED BY the new-product flow ending (then use the market's multiple)
Inputs: company P/E and index P/E over 10+ years → price data, EPS history; product pipeline → 10-K, R&D disclosures
Sources: [BOOK Fisher loc.133–135] (Part One); [BOOK Fisher loc.155] (Part One: past P/E is the base, but a company moving up a class can go from 8× to 15×); [BOOK Fisher loc.210] (Part Two: the further ahead profits keep growing, the higher the P/E an investor can afford)
Evidence: D — a worked fictitious example
Conflicts: none yet (complementary with R-184's own-history band)
Status: UNTESTED

### R-NEW13 Disclosure retreat after bad news: exclude
School: process | Horizon: long-term (years) | Instrument: shares
IF after a disappointment the company discloses less than it did in good times (drops guidance or segment detail it used to give, files late with an NT 10-K/10-Q, or its annual report leaves out matters of real significance) THEN exclude it from new buying and count a holding as failing Point 14 | EXIT for a holding, re-run the integrity and thesis review | INVALIDATED BY a prompt, full account of the problem and the plan to fix it (the book's positive case is the Rogers president who reported repeated bad news openly)
Inputs: NT 10-K/10-Q filings → SEC EDGAR; segment notes and guidance history → 10-K, 10-Q, earnings releases
Sources: [BOOK Fisher loc.80] (Part One, Point 14); [BOOK Fisher loc.133] (Part One: reports that omit significant matters); [BOOK Fisher loc.234] (Part Three)
Evidence: D — assertion
Conflicts: none yet
Status: UNTESTED

### R-NEW14 Capital-growth sleeve: low or no payout where reinvestment is rich
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF the goal is capital growth AND a company pays out a high share of earnings while it has high-return uses for the money (payout stressed so much it limits growth) THEN don't buy it; favour low- or no-payout companies; a maturing grower paying about 25–40% of earnings on a steady, announced policy is acceptable; one-off extra dividends count for nothing | EXIT n/a (a screen) | INVALIDATED BY retained earnings earning subnormal returns or piling up as idle cash (then retention adds nothing; see R-113)
Inputs: payout ratio → 10-K; ROIC or return on retained earnings → 10-K; cash vs needs → balance sheet
Sources: [BOOK Fisher loc.120–125] (Part One); [BOOK Fisher loc.118] (Part One); [BOOK Fisher loc.250–251] (Part Three)
Evidence: D — the author says every study he has seen found high-yield stocks did worse on price, but names none (loc.90, loc.122)
Conflicts: R-177 — decided by goal and reinvestment returns (see Conflicts)
Status: UNTESTED

### R-NEW15 Prefer the clear profit leader to the number two or three
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF one company clearly leads its field in both sales and profitability AND its management stays competent THEN prefer it to the number two or three; don't buy a follower on the theory that it can catch up | EXIT leadership lost (share and margin rank falling) | INVALIDATED BY a field with no clear leader
Inputs: market share and margin rank → 10-K, industry data
Sources: [BOOK Fisher loc.195] (Part Two: GE vs Westinghouse, Sears vs Montgomery Ward, IBM in computers); [BOOK Fisher loc.196] (Part Two: pharmaceutical saying, first entrant about 60% of the market, second about 25%, next three 10–15%)
Evidence: C — author's observed cases; the pharmaceutical split is an industry saying with no data
Conflicts: none yet
Status: UNTESTED

### R-NEW16 Industry margins widening only on price rises: no long-term buy
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF an industry's margins are widening mainly because selling prices keep rising (strong demand, costs passed on) AND new competing capacity is being announced THEN don't buy its companies as long-term holdings; expect margins to shrink as that capacity arrives | EXIT a holding bought for margin expansion once the capacity starts up | INVALIDATED BY a company that is widening margins through cost cutting (new equipment, methods, logistics, branch plants), which is the book's preferred case
Inputs: product prices → BLS PPI, commodity price series; industry margins → peer 10-Ks; capacity announcements → 8-Ks, industry data
Sources: [BOOK Fisher loc.68–69] (Part One: aluminum moved from shortage to aggressive selling within weeks in fall 1956; copper 1956–57)
Evidence: C — two industry cases from 1956–57
Conflicts: none yet (complementary with R-196)
Status: UNTESTED

### R-NEW17 Research productivity: share of sales from new products
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a company reports the share of sales coming from products launched in the last few years AND that share is high or rising against peers THEN credit its research (Point 3); IF R&D ÷ sales is well above peers while the new-product share stays low THEN flag research that isn't productive. Book benchmarks: a 1957 survey expected about 10% of 1960 manufacturing sales from products less than three years old; Ampex had 80% of sales from products that did not exist four years earlier | EXIT n/a | INVALIDATED BY inconsistent R&D accounting (sales engineering booked as R&D, pilot plants charged to production); compare like with like (see R-136)
Inputs: new-product share of sales → 10-K, investor presentations; R&D ÷ sales → 10-K
Sources: [BOOK Fisher loc.43] (Part One: McGraw-Hill / Business Week surveys, 1956–57); [BOOK Fisher loc.59–60]; [BOOK Fisher loc.64]; [BOOK Fisher loc.144]
Evidence: D — the benchmark comes from outside surveys, but the rule itself is untested
Conflicts: none yet (complementary with R-100's R&D ÷ assets test)
Status: UNTESTED

### R-NEW18 Switch only for clearly faster growth
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF a new candidate passes the same quality work AND its well-evidenced long-run EPS growth is clearly above the holding's (the book: 20% against 12% a year) THEN switch, even after capital-gains tax; if the evidence isn't clear-cut, keep the holding you know | EXIT n/a | INVALIDATED BY doubtful evidence on the new company (the book warns that a holding you know well has fewer surprises)
Inputs: long-run EPS growth estimates → desk forecast, consensus; tax lots → desk ledger
Sources: [BOOK Fisher loc.111–112] (Part One); [BOOK Fisher loc.97] (Part One: American Cyanamid sold in 1959 at about +110% for a better-looking company; the author later questioned the sale); agrees: [BOOK Fisher loc.260] (Part Three: as holdings near 20, switch the least attractive into more of the best); agrees: [BOOK Wyckoff p.81–82]
Evidence: C — author's own switch, with its doubtful result reported
Conflicts: none yet
Status: UNTESTED

### R-NEW19 Industry-specific cost ratio as a check on management (Point 11)
School: growth/momentum | Horizon: long-term (years) | Instrument: shares
IF the industry has a cost line that decides margins (retail leases: occupancy cost ÷ sales; lending: credit losses ÷ loans; insurance-heavy operations: insurance cost ÷ sales) THEN compare it with peers of similar size and count a clearly better ratio as evidence of overall management skill (the book: insurance costs 35% below a same-size rival can widen the margin) | EXIT n/a (supporting evidence) | INVALIDATED BY n/a
Inputs: occupancy or lease cost, net charge-offs, insurance expense → 10-K, bank call reports
Sources: [BOOK Fisher loc.75] (Part One)
Evidence: D — assertion
Conflicts: none yet
Status: UNTESTED

## Merges
R-087 | agrees: [BOOK Fisher loc.78–79] (Point 13: count every convertible as converted and every option and warrant as exercised; reject when equity financing within a few years leaves only a small gain in per-share earnings; if cash plus prudent borrowing covers the next several years, ignore capital structure)
R-113 | agrees: [BOOK Fisher loc.118] (cash piled up beyond any present or prospective need gives holders no benefit; nor do earnings retained to enlarge an operation earning subnormal returns)
R-129 | agrees: [BOOK Fisher loc.182] (Part Two: a profit stream that grows at least as fast as sales)
R-130 | agrees: [BOOK Fisher loc.240] (Part Three: when a proven management's project fails, P/E falls below its usual level and the shares can be bargains); [BOOK Fisher loc.256–259] (Raychem 1976: Stilan write-off and reorganisation, stock fell to about a third of its high and more than doubled within one to two years after the January 1978 meeting)
R-158 | agrees: [BOOK Fisher loc.152–153] (Texas Instruments 1956: officers sold a small part of large holdings for diversification and estate needs; the author bought the block at 20× expected EPS, and a year later the stock had roughly doubled)
R-198 | agrees: [BOOK Fisher loc.94–96] (first full-scale plant shake-down depresses EPS and the price; buy then; American Cyanamid's Fortier plant, 1954); [BOOK Fisher loc.98–100] (Food Machinery's chemical divisions, 1957); [BOOK Fisher loc.102–103] (labour trouble fixable in months; buying points A and B while officers bought heavily)
R-199 | agrees: [BOOK Fisher loc.108–109] (sell a purchase once the facts are clearly worse than believed; waiting to break even is the costliest habit)
R-204 | agrees: [BOOK Fisher loc.104] (the buying range is an earnings rise coming in the right company that the price has not yet reflected); [BOOK Fisher loc.164] (improvements made by little-known executives re-rate slowly)
R-230 | agrees: [BOOK Fisher loc.106–107] (new money after a long rise: start buying now and spread the rest over several years); [BOOK Fisher loc.244] (Part Three: a small first position while contact with management is slight)
R-233 | agrees: [BOOK Fisher loc.80–81] (Point 15: options granted far beyond a fair reward, relatives on the payroll, related-party leases and broker arrangements; integrity is the one point that allows no exception)

## Conflicts
- R-NEW9 Hold a compounder through a high multiple vs R-187 Sell a high-multiple holding on stalled earnings — decided by the earnings trend: fundamentals on track and quality review passed → R-NEW9; flat earnings or an operating crack at the high multiple → R-187 [BOOK Fisher loc.113–114]; [BOOK Fisher loc.202–203]; [BOOK Plotnick p.184–185]
- R-NEW9 Hold a compounder through a high multiple vs R-119 Sell only when price passes a refreshed fair value — decided by school: a growth compounder held for its management and growth → R-NEW9 (Fisher holds even above value); a valuation-based holding → R-119 [BOOK Fisher loc.114]; [BOOK Ramnarayanan p.54–58]
- R-NEW9 Hold a compounder through a high multiple vs R-061 20% stop from cost, 20% trailing stop — decided by school and horizon: a fundamental long-term compounder is reviewed on its fundamentals (Texas Instruments fell 80% and later more than doubled its peak) → R-NEW9; a price-managed growth holding → R-061 [BOOK Fisher loc.247–248]; [BOOK Anderson loc.34]
- R-NEW10 Position caps at cost by class vs R-139 Trim a single stock near a fifth of the portfolio — decided by measurement base: caps at original cost, with no trim for growth-driven drift while the outlook holds → R-NEW10; market-weight trims → R-139; the desk's C7 tiers govern every verdict [BOOK Fisher loc.139]; [BOOK Snow loc.33]
- R-NEW10 Position caps at cost by class vs R-200 15–25 holdings, at most 12% per stock at cost — decided by company risk class: large entrenched companies up to 20% at cost (Fisher), mid-sized 8–10%, small at most 5%; a portfolio not classified this way → R-200 [BOOK Fisher loc.139]; [BOOK Wachenheim loc.56]
- R-NEW10 small companies at most 5% each vs R-175 Speculative bets at 1–2% in total — decided by bet type: one-year speculative bets on outsized gains → R-175; multi-year small-company holdings that pass the full quality work → R-NEW10 [BOOK Fisher loc.144]; [BOOK Fridson loc.8]
- R-NEW14 Low or no payout for capital growth vs R-177 Favour dividend payers — decided by goal and reinvestment returns: a capital-growth sleeve where retained earnings earn high returns → R-NEW14; income goals, or comparable stocks without such opportunities → R-177 [BOOK Fisher loc.122]; [BOOK Fisher loc.251]; [BOOK Wildermuth p.95–96]
- R-NEW8 Three-year rule (sell a three-year laggard) vs R-102 Favour three-year losers — decided by method: a concentrated conviction holding judged on its own thesis → R-NEW8; a diversified statistical basket → R-102 [BOOK Fisher loc.232]; [BOOK Zacks loc.43–44]
- R-NEW2 No promotional companies vs R-127 Weight a young or loss-making company's value by its chance of surviving — decided by sleeve: Fisher growth sleeve → never buy before an operating record; a valuation sleeve that prices survival → R-127 [BOOK Fisher loc.126–127]; [BOOK Damodaran p.109]
- R-NEW7 War-scare buying vs R-050 Index trend filter — decided by level and horizon: long-term accumulation of single names already chosen → R-NEW7; index-level exposure switched on the 50/200 cross → R-050 [BOOK Fisher loc.148]; [BOOK Piard loc.17–20]
- R-NEW3 Outside CEO: no new buying vs R-131 Badly managed company with a path to management change and R-198 Strong franchise with a temporary problem (a new CEO committing to cuts) — decided by school and starting point: a growth holding bought for its existing management → R-NEW3; a value turnaround where the change of management is the catalyst → R-131/R-198 [BOOK Fisher loc.184]; [BOOK Damodaran p.160]; [BOOK Wachenheim loc.66–67]
- R-NEW11 Buy at the market vs principle "Enter with limit orders…" and R-023 Don't chase past the planned entry — decided by horizon: swing and day entries at planned levels → limit orders / R-023; long-term growth buys sized small against volume → R-NEW11 [BOOK Fisher loc.135–136]; [BOOK MetaStock p.10]; [BOOK Regan loc.25]
- R-NEW5 Margin on sales vs R-231 Favour high, sustained ROIC — decided by purpose: Fisher distrusts return on assets because assets sit at historic cost, and uses margin on sales for safety (R-NEW5); ROIC ranks profitability where asset costs are comparable (R-231); use both, with age-adjusted assets when comparing ROIC [BOOK Fisher loc.193]; [BOOK Martin p.176]
- Fisher principle (low P/E is as often a trap as a bargain) vs R-101 Value premium (cheapest fifth) — decided by method: a diversified statistical basket → R-101 (B); a single-name pick → explain the low P/E with scuttlebutt before buying [BOOK Fisher loc.221–222]; [BOOK Zacks loc.82]

## Principles
- Return dispersion across stocks dwarfs the market's own move: in the author's Stanford class sample (all 140 NYSE common stocks starting with A or T, utilities and preferreds excluded, end-1956 to 13 Oct 1961, Dow +41%), 27% lost money and 4% lost over half; the five best turned $10,000 into $70,260 and the five worst into $3,180; a repeat with two other letters gave a similar spread (figures not shown); table not converted [BOOK Fisher loc.253–254] (Part Three) — A (one small sample, one window; check table loc.254)
- Scuttlebutt: competitors, customers, vendors, research scientists, trade-association staff and former employees (check why they left) give a clear picture once enough views agree; promise and keep anonymity [BOOK Fisher loc.50–51]; Ken Fisher calls it a craft that takes years, built on follow-up questions [BOOK Fisher loc.4–8] (introduction) — D
- Visit management only after gathering about half the knowledge you need, introduced by a banker, customer or large holder; the author's funnel: about one buy per 2–2.5 companies visited, one per 40–50 looked at, one per ~250 considered [BOOK Fisher loc.170–172] (Part One) — C
- Drop an investigation when outside sources can't be reached: what matters is being right on the few buys, not having an answer on every company [BOOK Fisher loc.169] — D
- Source of ideas: the author's own review found about four-fifths of his investigations and five-sixths of his worthwhile buys started with a few able investment men, about one-fifth and one-sixth with executives and scientists; public brokerage bulletins are a poor source [BOOK Fisher loc.166–168] (Part One) — C
- First read of a prospect: SEC prospectus/proxy for sales by product line, competition, officer ownership, depreciation, margins, R&D and nonrecurring costs, not years of old balance sheets [BOOK Fisher loc.169] — D
- Don't time buys or sells on economic or market forecasts, except in rare manic years like 1928–29 (the author guesses about one year in ten); he puts his short-term calls at about 60% right against about 90% for spotting outstanding companies [BOOK Fisher loc.92]; [BOOK Fisher loc.105]; [BOOK Fisher loc.246–247] — D; agrees [BOOK Wachenheim loc.89–90]; agrees [BOOK Martin p.80–81]
- A low P/E guarantees nothing and often flags weakness: the author's 1929 buys of low-P/E locomotive, billboard and taxi stocks were nearly wiped out by 1932; judge price against earnings a few years ahead [BOOK Fisher loc.221–222] (Part Three) — C (see Conflicts vs R-101)
- Former price ranges have little bearing on value; buying the stock that "hasn't gone up yet" assumes all stocks rise alike [BOOK Fisher loc.149–150]; [BOOK Fisher loc.213] — D
- Past five years' EPS is a secondary tool, useful for cyclicality and as a P/E base; even the best growers have one- to three-year dips [BOOK Fisher loc.151]; [BOOK Fisher loc.155] — D
- Sales growth should be judged in blocks of several years: research and launches make it come in uneven spurts [BOOK Fisher loc.53] — D
- A stock's moves against the market come from a changed appraisal by the financial community; the biggest gains combine rising EPS with a rising P/E (the book's G company: EPS $1 to $1.82 and P/E 10 to 22 took the price from $10 to $40) [BOOK Fisher loc.200–202] (Part Two) — D
- Price blends three appraisals (market, industry, company); industries re-rate when the emphasis shifts, not the facts (chemicals 1950s vs 1960s, computer peripherals 1969, franchising 1969–72, A. C. Nielsen 1958) [BOOK Fisher loc.205–208] (Part Two) — C
- In falling markets a worse image is accepted faster than a better one: Motorola jumped about 25% on selling its TV business in March 1974, then gave it back as rates rose [BOOK Fisher loc.212] (Part Two) — C
- Improvement by little-known executives re-rates slowly; a famous new president makes the stock over-react at first [BOOK Fisher loc.164] (Part One) — D
- Going against the crowd pays only when you are very sure you are right (buying streetcar stocks just because they were unloved would have been costly) [BOOK Fisher loc.230–231] (Part Three) — D; agrees [BOOK Regan loc.21]
- Market-wide misjudgements recur: the 1927–29 "new era"; 1946–49, when good earnings were dismissed in expectation of a post-war crash and companies were "worth more dead than alive" around 1949; 1972–74 [BOOK Fisher loc.159]; [BOOK Fisher loc.213–214]; [BOOK Fisher loc.241–242] — C
- Interest rates set the general level of stocks (high rates pull money away); new-issue volume follows the market more than it leads it [BOOK Fisher loc.215] (Part Two) — D (in tension with the principle that heavy issuance precedes weak returns [BOOK Zacks loc.60–61])
- For long-term holders, bonds lose real value under the post-1932 inflation bias: 16 countries' money lost value 1946–56 (US −29%, 3.4% a year against a 2.19% Treasury yield) per a First National City Bank letter of Dec 1956 [BOOK Fisher loc.46–48] (Part One) — B (one decade; era-bound)
- In-and-out trading: the author profited three times trading California Packing in the 1930s, judged the gains trivial next to long holds and riskier, and stopped after WWII [BOOK Fisher loc.236]; [BOOK Fisher loc.248–249] — C; agrees [BOOK Wyckoff p.132–133]
- Ego is the costliest habit: holding until "at least even"; review every loss for its lesson; take small losses and let big profits run, never take a profit just to take one [BOOK Fisher loc.109]; [BOOK Fisher loc.260] — D; agrees [BOOK Anderson loc.56]
- Be most thorough when things are going well: a 1960s drug stock bought on one specialist's and one officer's word fell over 50%, and later complacency at "Central California Electronics" missed management decline [BOOK Fisher loc.243–244]; [BOOK Fisher loc.248] (Part Three) — C
- Don't pay a hot market's entry price for real promise: a 1969 equipment company grew for years but was sold near cost [BOOK Fisher loc.244–245] (Part Three) — C
- Stay inside your competence: the author's results outside industrial and technology manufacturing (consumer products, real estate) disappointed him [BOOK Fisher loc.216]; [BOOK Fisher loc.245–246] (Part Three) — C
- A large company relying mainly on patents for its margin is weak; for a small young company the patent position matters, though steady engineering leadership protects better [BOOK Fisher loc.76–77] (Part One) — C
- Labour and people signals: turnover and applicant waiting lists against local employers, above-area wages paid out of above-average profits, quick grievance handling; Texas Instruments' sales ÷ payroll index rose from about 2.25 to 2.5 over 1969–73 [BOOK Fisher loc.71]; [BOOK Fisher loc.188–190] — C
- Management depth becomes necessary once sales reach somewhere between $15 and $40 million (1958 dollars): delegation, merit promotion, openness to criticism; promotion from within is the norm [BOOK Fisher loc.72–73]; [BOOK Fisher loc.183–184] — D
- Research takes seven to eleven years to pay off; crash programmes and stop-start budgets raise its cost; government-funded research is worth what transfers to commercial lines [BOOK Fisher loc.43]; [BOOK Fisher loc.61–63] — D
- For a top-quality company, financial structure matters little if cash plus prudent borrowing covers several years; never buy a weak company for its cash [BOOK Fisher loc.78–79] — D
- Retained earnings help holders only if reinvested well; under inflation, depreciation doesn't cover replacement, which hurts fast-growing firms less [BOOK Fisher loc.118–119] — D
- Steady dividend policy wins a following; one-off extra dividends leave no lasting mark on the price [BOOK Fisher loc.123–124] — D
- A low-cost producer survives price wars, takes share from closing rivals and funds growth itself; high-cost firms' profits jump more in booms and fall harder after (the widget arithmetic) [BOOK Fisher loc.66]; [BOOK Fisher loc.178] — D
- High margins draw competitors; the lasting defences are efficiency, multidisciplinary technology and specialised niches with many small customers for whom the product is critical but cheap [BOOK Fisher loc.194]; [BOOK Fisher loc.197–198]; [BOOK Fisher loc.199] (ask what the company can do that others can't) — D; agrees [BOOK Martin p.174] (signs of a structural advantage, incl. operating margins well above direct competitors)
- Don't buy on an annual report's tone, photos or charts [BOOK Fisher loc.132] — D
- Over-the-counter stocks with two or more high-grade dealers can be liquid enough (describes 1950s market structure) [BOOK Fisher loc.130–132] — D
- The author's view that over about five years a statistical bargain hunter makes a small fraction of what growth-company appraisal makes [BOOK Fisher loc.82–83] — D
- Pick an adviser on at least five years of results against the market, checked for style (bond-heavy in falls, marginal companies in rises, market guessing) [BOOK Fisher loc.85–86] — D; agrees [BOOK Gibbs loc.86–87]
- Invest only true surplus funds, after an emergency reserve and money set aside for specific needs [BOOK Fisher loc.89] — D
- Efficient-market theory fails the diligent long-term investor: Raychem's frank January 1978 meeting moved the stock not at all, though it more than doubled from $23¼ over the next year or two [BOOK Fisher loc.252–253]; [BOOK Fisher loc.258–259] (Part Three) — C
- Ken Fisher: stop making investment decisions before you grow old; his father's late-life sales of FMC, Texas Instruments and Raychem were consistently badly timed [BOOK Fisher loc.23–24] (introduction) — C
- Ken Fisher: a falling market is the time to swap the weakest holding for a better company, not to sell out [BOOK Fisher loc.12] (introduction) — D
- Ken Fisher claims the fifteen points and scuttlebutt would have kept investors out of Enron, Tyco, WorldCom and the 2000–02 "95 percent club" [BOOK Fisher loc.4]; [BOOK Fisher loc.6] (introduction) — D

## Ingest log row
| 2026-11-19 | Fisher | loc.267/267 | 19 (growth/momentum 13, process 4, risk/sizing 2; C 7, D 12) | 10 (R-087, R-113, R-129, R-130, R-158, R-198, R-199, R-204, R-230, R-233) | 43 new + 9 agreements | classic growth-stock book plus two later monographs: Part One 1958 (rev. 1960) loc.38–174, Part Two 1975 loc.175–215, Part Three 1980 loc.216–263, and Ken Fisher's 2003 preface/intro loc.3–37 (mostly biography); all examples 1929–1979 with unadjusted prices and dollar size thresholds (rescale $15–100m sales classes); case-based and winner-heavy, but the author reports misses (Mallory, Elox, the Cyanamid sale, a 1960s drug stock, a 1969 equipment company, "Central California Electronics"); the only systematic data is the Stanford dispersion sample, whose table was not converted (check table loc.254); likely conversion error in Raychem EPS "$.08 from $7.95" (loc.256); appendix OCR garble ("profitable" replaces "w", loc.261–263); stray editor notes (loc.23, loc.236); no product promotion; instructions.md not read (no Projects tool) |

## Run report
Read loc.1–267 of 267 in order (END OF BOOK confirmed at loc.267), using tools/read_chunk.py's own segmentation. Coverage: Ken Fisher's preface and introduction (loc.3–37), Common Stocks and Uncommon Profits (loc.38–174), Conservative Investors Sleep Well (loc.175–215), Developing an Investment Philosophy (loc.216–263), index (loc.264–267).
New rules: 19 (growth/momentum 13, process 4, risk/sizing 2; C 7, D 12; no A or B). 10 merges, 14 conflicts, 43 principles (9 marked as agreeing). One principle is graded A (the 140-stock dispersion sample) and one B (the 1946–56 inflation data). Partial flags: the dispersion table is missing (loc.254); the Raychem EPS figure looks garbled (loc.256); the appendix is OCR-damaged; instructions.md was not available, so its exact rule-vs-principle wording was not checked.
Test first: R-NEW1, the cycle-peak EPS test. Every input is observable (split-adjusted EPS, NBER peak dates, forward estimates), it gives a clear hold/sell answer for long-term holdings, and it can be backtested on historical point-in-time EPS against the desk's other sell rules (R-187, R-188, R-119).

## Cut
- Buy on a date, not a price: time purchases to the milestone at which the company's past ventures were priced in, e.g. about a month before a pilot plant [BOOK Fisher loc.156–157]
- People-effectiveness index (sales ÷ payroll) rising against peers [BOOK Fisher loc.190] (payroll seldom disclosed)
- Labour turnover and applicant waiting list against local employers [BOOK Fisher loc.71] (no routine data source)
- Patent-dependence flag for large companies [BOOK Fisher loc.76] (kept as a principle)
- Scuttlebutt coverage gate: drop the name if outside sources can't be reached; meet management only after half the work [BOOK Fisher loc.169–171] (kept as principles)
