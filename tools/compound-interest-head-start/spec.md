# Compound Interest Head Start

## One idea
Two savers put the same $50 a month into the same plain savings account, one from age 16 and one from 26, and a stacked bar for every year splits each balance into what they deposited, the interest on those deposits, and the interest on earlier interest, so you can watch that third layer, the one only time builds, grow until it is the biggest part of the head start.

## Not like
- market-time-machine (9-12, money, built): real market returns that rise and fall. Here one fixed savings rate, no risk, no history.
- savings-plan (math 11, built): deposits that grow as a sequence, no interest at all. Here the deposits never change; all the growth is interest.
- interest-rate-dial (CTE 6-8, not built): one dial and four people (saver, borrower, card, cafe). Here only saving, and the lever is time.
- first-apartment-budget (9-12, money, built): one year of a budget. Here fifty years and no spending.
- paycheck-decoder, the-credit-card-diaries (9-12, money, this group): one paycheck; four years of credit. Here saving only.

## Who and how
- Grade 9-12, career and technical education (personal finance), module "Saving and Compound Interest".
- Topic line: saving and compound interest
- Driver: students on laptops; the teacher can project Race for a whole-class opener ("who ends up with more?"). 15 to 35 minutes.
- Standards: NSPFE.Saving (simple and compound interest, the effect of time and rate, emergency savings).
- Data as of line: "Savings rates as of mid-2026: national average about 0.4 percent (FDIC); some online accounts pay about 4 percent. Rates change; this account's rate is fixed for learning."

## Screens and modes
Header: title, topic line, modes (`.seg`): `Race` (default), `Rate and compounding`, `Rule of 72`; then `Read`, `Motion`, `Sound`.

**Race.** Stage: two lanes, one above the other, labeled "Saver A starts at 16" and "Saver B starts at 26". Each lane is a row of stacked bars, one per year of age from 16 to 66 (51 bars; B's first ten are empty). Each bar has three layers: Deposits (slate), Interest on deposits (green), Interest on interest (gold, with a diagonal hatch so it differs by pattern too). A big readout at each lane's right end: balance at 66 and its three parts.
- `Play` grows both lanes year by year (about 6 seconds for 50 years; instant with Motion off). `Pause`, and a year scrubber under the lanes that moves an age marker across both lanes.
- Hover or tap any bar (44 px hit area per bar column; arrows step it): a tooltip card with that age's balance, deposits so far, interest on deposits, interest on interest.
- Panel: `Monthly deposit` ($10 to $200, step $10, default $50, the same for both), `Rate` (0.0 to 10.0 percent, step 0.1, default 4.0), `Compounds` select (yearly, quarterly, monthly, daily; default monthly), and the what-if switch `Saver A stops at 26` (A deposits only from 16 to 26, ten years, then leaves the money alone).
- Under the lanes a gap line: "At 66, A has $36,369.75 more than B. A put in $6,000 more." (live).
- With `Saver A stops at 26` on, a prompt appears: "Can the early saver who stopped still win? Change the rate to find out." When A's balance at 66 passes B's, a marker on the rate slider shows the crossover rate (event line).

**Rate and compounding.** One saver, one lump of money, so compounding is easy to see. Stage: a single growing bar per year for 30 years and a table under it.
- Panel: `Start with` ($100 to $10,000, default $1,000), `Rate` (as above), and four toggles that each draw a line on a small chart, one per compounding choice (yearly, quarterly, monthly, daily), with the formula A = P(1 + r/n)^(nt) written under the chart with the current numbers filled in.
- Table: n, rate per period, APY (annual percentage yield) to three decimals, balance after 10 and 30 years.
- Note line: "Compounding more often helps a little. The rate and the years help a lot."

**Rule of 72.** Stage: a row of coins doubling (1, 2, 4, 8) along a timeline in years. Panel: `Rate` slider. Readouts: "Rule of 72 says 72 / rate = (x) years" and "Exact doubling time (monthly compounding): (y) years". A small table for 1, 2, 4, 6, 8, 10 and 12 percent shows both and the difference.
- Optional prompt (challenge): "Pick a rate where the rule is off by less than a month." The readout marks it when |rule - exact| x 12 < 1.

## Content
- Savers: A and B, no names, no pictures, so nothing is about who they are.
- Account: a plain savings account with a fixed rate (made up for learning, labeled "fixed for learning"). Deposits go in at the end of each month.
- Defaults: $50 a month, 4.0 percent, monthly compounding, ages 16 to 66 (A: 600 deposits; B: 480).
- Default results (4.0 percent, monthly): A at 66 $95,467.82 = deposits $30,000 + interest on deposits $29,950.00 + interest on interest $35,517.82. B at 66 $59,098.07 = $24,000 + $19,160.00 + $15,938.07. A stops at 26: $36,369.75 = $6,000 + $10,790.00 + $19,579.75.
- Crossover: with A stopping at 26, A first ends ahead of B at 6.6 percent ($117,785.37 to $117,383.68); at 6.5 percent B still leads ($114,180.95 to $112,574.16). The exact crossover is about 6.58 percent.
- Emergency fund note (a card in the Race panel, `Why savings, not investing?`): "Money you may need soon, like an emergency fund of a few months of expenses, belongs where it can't drop in value. Savings accounts at insured banks are insured by the FDIC up to $250,000 per depositor, per bank, per ownership category. Investing is for money you won't need for years (see Market Time Machine)."
- Rates to try (buttons under the Rate slider): `National average 0.4%`, `High-yield 4%`.

## Interactions in detail
- One monthly step for every compounding choice: the effective monthly rate i = (1 + r/n)^(n/12) - 1 (money engine `grow`). Each month: balance x (1 + i), then add the deposit. With yearly or quarterly compounding this credits deposits made between compounding dates their fair fraction of a period; the `Compounds` card says so: "Real banks add interest on each day's balance; this is the same idea in monthly steps."
- The split, computed alongside: deposits = the sum of deposits; interest on deposits (simple interest) grows each month by (deposits made before this month) x r/12; interest on interest = balance - deposits - interest on deposits. At 0 percent all interest is $0.00 and the bars are deposits only (note: "No rate, no growth: just your deposits.").
- Amounts shown to the cent, computed in full precision and rounded only for display.
- Daily compounding uses n = 365.
- Exact doubling time for Rule of 72: ln 2 / (12 ln(1 + r/1200)) years at monthly compounding (r in percent); at 0 percent it says "Never: nothing grows at 0 percent" and the coins stay at 1.
- Crossover marker: on each rate change with A stopping at 26, compare the two balances at 66; the marker shows the lowest step (0.1) where A leads; the event line plays the first time A takes the lead after a rate change (and again only if B retakes the lead and A wins back).
- Scrubber and arrow keys move one year; Home and End jump to 16 and 66. Tab order: modes, panel controls, then lanes.
- Sizes: bars are drawn at real pixels; at 680x425 the lanes show every fifth year label and the readouts shrink to one line; at 375 wide the lanes scroll sideways inside their frame with the readouts pinned above.
- Reset (`Start over` in the panel) returns every control to its default.

## Look
- Accent `--brand #9be564` (spring green: the active mode, Play, the slider thumb), `--brand-ink #132600`. Base `kit/theme-912.css`.
- Layers: deposits `#7d8fa8` slate, interest on deposits `#4fbf7a` green, interest on interest `#f2c14e` gold with a hatch. Lane background `#0f1620`, year grid `#24303f`.
- Contrast: accent on panel 11.36:1, on `--sec-bg` 10.77:1; brand-ink on accent 10.56:1; layer colors on the lane are 3:1 or more (graphics), and each layer also has a label and a pattern.
- Differs from market-time-machine's paper and brass, savings-plan's dark ledger, and this group's other accents (yellow, raspberry, cyan, violet, orange, green trail map, periwinkle, coral).

## Art
none: drawn in code (bars, coins, chart).

## Voice
Bank voice `smooth-narrator` (Algieba), "Say smoothly and warmly, like an audiobook narrator": the race is told like a short story over fifty years. Not used by another tool in this group or by a 9-12 CTE tool. `Curio.voice`, `scope: () => state.mode`.
- welcomeRace (how): "Two savers, the same fifty dollars a month. Tap Play to watch fifty years go by."
- barHow (how, after the first Play ends): "Tap any year to see its three parts. The gold part is interest on interest."
- stopHow (how, first time Saver A stops at 26 is turned on): "Saver A stopped at twenty-six. Change the rate to see if A can still win."
- crossover (event, when A takes the lead; stale if the rate changes again first): "At (rate) percent, the saver who stopped early comes out ahead."
- welcomeRate (how): "Turn on each compounding choice and compare the lines."
- welcome72 (how): "Drag the rate. Seventy-two divided by the rate is close to the years it takes to double."

## Family engine
The money family engine, described in full in paycheck-decoder's spec. This tool uses `grow({start, deposit, months, rate, perYear})` with its yearly split (deposits, interest on deposits, interest on interest), `money`, `pct` and `r2`. It feeds it: the two savers' schedules (start ages 16 and 26, end 66, optional stop at 26), the lump sum for Rate and compounding, and the rate list for Rule of 72.

## Sources
- Compound interest formula, APY and compounding frequency: CFPB, "What is the difference between APR and APY?" (https://www.consumerfinance.gov/ask-cfpb/) and the FDIC, Money Smart for Young Adults, Module "Pay Yourself First" (https://www.fdic.gov/consumer-resource-center/money-smart).
- National average savings rate (about 0.38 to 0.42 percent through 2025 and mid-2026): FDIC, National Rates and Rate Caps (https://www.fdic.gov/national-rates-and-rate-caps); builder shows the latest monthly value with its date.
- Deposit insurance $250,000 per depositor, per insured bank, per ownership category: FDIC, Deposit Insurance (https://www.fdic.gov/resources/deposit-insurance).
- Rule of 72 as an estimate of doubling time: Investor.gov (SEC), "Rule of 72" glossary (https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-72).
- Emergency fund guidance: CFPB, "An essential guide to building an emergency fund" (https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/).
- All balances: computed by the tool; worked values recomputed in Python for this spec.

## Done when
1. Defaults give A $95,467.82 ($30,000 / $29,950.00 / $35,517.82) and B $59,098.07 ($24,000 / $19,160.00 / $15,938.07) at 66.
2. A stops at 26 at 4.0 percent: $36,369.75 ($6,000 / $10,790.00 / $19,579.75); A at 26 before stopping: $7,362.49.
3. With the stop on, the crossover marker sits at 6.6 percent (A $117,785.37, B $117,383.68) and 6.5 percent still shows B ahead.
4. A at 4 percent by compounding: yearly $93,267.70, quarterly $95,055.37, monthly $95,467.82, daily $95,669.33; APY yearly 4.000, quarterly 4.060, monthly 4.074, daily 4.081.
5. Rate and compounding: $1,000 at 4 percent monthly for 10 years shows $1,490.83 (yearly $1,480.24).
6. Rule of 72 at 6 percent: rule 12.0, exact 11.58 years; at 0 percent "Never" with no division by zero.
7. At 0 percent every bar is deposits only and all interest reads $0.00.
8. Every bar is reachable by keyboard and its tooltip matches the split; layers differ by pattern and label as well as color.
9. Lanes, readouts and Play are visible without scrolling at every STANDARDS.md size; the 680x425 preview is readable.
10. How lines once each in five actions in a row; crossover plays every time A takes the lead and drops when stale.

## Open questions
- The concept fixes $50 a month from 16 and 26. At savings-account rates the saver who stops at 26 does not catch the one who keeps going (the crossover is about 6.58 percent, above most savings rates). The tool shows that honestly. Fine, or should the stop-at-26 what-if be left out to keep the message simple?
