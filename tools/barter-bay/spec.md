# Barter Bay

## One idea
The child is a potter at the Barter Bay harbor market who wants a loaf of bread, but the baker doesn't want pots, so the child hunts a chain of swaps (a pot for rope, rope for fish, fish for bread) while a sun clock shows half the market day gone; then the bay agrees that rare moon shells are money and the same errand takes one trade; then the child drops a sack of new shells into the bay, lets shells wash away, or closes the fish cannery, and watches a price board, a jobs board and three people (a saver, a borrower, a cannery worker) show what inflation, deflation and unemployment do, so a fourth grader learns why money makes trading easier and what those three big words mean for real people.

## Not like
- border-trade-post (6, concept): barter to money to tariffs between countries. Here money's value inside one market and three shocks (the idea card's overlap flag; this tool stays on money's value).
- market-day (1, spec): buying and selling at a market with prices. Here why money exists and what changes its value.
- paper-plane-assembly-line (concept): production. Here exchange and money.
- skateboard-fund-chances (4, spec, this batch): saving and investing. Here what money is.

## Who and how
- Grade 4, Social Studies (Economics), module "Barter Bay". Standards: D2.Eco.5.3-5 (explain the role of money in making exchange easier), D2.Eco.11.3-5 (explain the meaning of inflation, deflation, and unemployment).
- Driver: one child alone (tool.json `driver: "student"`); the class version uses printed goods cards. `Read` reads every line. Controls 44 px or more.
- Three parts: Barter, Money, Shocks; then the Explain card. Extra: Class market (printable goods and shell cards, a projector price board). tool.json `modes: ["Market", "Class market"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.5.3-5 | Find a chain of swaps to turn a pot into bread, then do the same errand with shells | the want bubbles over each trader, the sun clock, and the trades-per-day counter before and after money | 2, 3 |
| D2.Eco.11.3-5 (inflation) | Drop the sack of new shells and read the price board | prices doubling; the saver's shells buying half as much | 4 |
| D2.Eco.11.3-5 (deflation) | Let shells wash away and read the board | prices halving; sellers holding back; the borrower's debt feeling heavier | 4 |
| D2.Eco.11.3-5 (unemployment) | Close the cannery and read the jobs board | ten workers without jobs, fewer buyers, the baker selling less | 5 |

## Screens and modes
Header (kit): title "Barter Bay"; `Market`, `Class market`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A harbor market in the morning: five stalls (baker, fisher, ropemaker, weaver, cannery gate), boats, a sun clock on the harbor wall. The child's potter stall holds three pots. The welcome is queued (`welcomeAfter: true`): "You're a potter on Barter Bay. You want bread, but there's no money here yet. Find someone who will take a pot." First hint: "Tap a trader to see what they want."

**Barter (focus: the market).** At 1366x768 all five stalls fit around the child's stall; at 680x425 stalls are a row of tabs.
- Tapping a trader shows a want bubble:
  - Mo the baker has bread and wants fish.
  - Hal the fisher has fish and wants rope.
  - Wren the ropemaker has rope and wants a pot.
  - Ada the weaver has cloth and wants bread.
- The child drags a pot to a trader. Wrong trader: "I don't need a pot. I want [want]." Each trade or walk costs one hour on the sun clock. The chain that works: pot to Wren for rope, rope to Hal for fish, fish to Mo for bread: three trades, plus any wrong tries. A day counter shows "Trades today" (the whole market: 12 trades, because most people spend the day hunting).
- When the child has bread: "Three trades and half the day, just for one loaf! What if everyone took one thing that anyone would trade for?"

**Money (focus: the moon shells).** The bay's people meet and agree: the rare moon shell is money. The price board lights up: bread 2 shells, fish 3, rope 4, cloth 5, a pot 6. The child sells a pot to anyone for 6 shells and buys bread for 2: one hour, two trades, any traders. "Trades today" jumps to 60. A line: "Money is something everyone agrees to take. Now you don't have to find someone who wants exactly what you have."

**Shocks (focus: the price board, the jobs board and three people).** Three shock buttons. The bay starts with 100 moon shells in use; each shock can be run, then `Reset the bay`.
- `Drop a sack of shells` (100 more shells, the same goods): prices double over a market week (bread 4, fish 6, rope 8, cloth 10, a pot 12). Granny Nell saved 20 shells: before, 10 loaves; now, 5. Mo borrowed 10 shells for a new oven: the 10 he owes are now easier to pay back. Narrator: "More money, same goods: prices go up. That's inflation."
- `Let shells wash away` (half the shells lost in a storm, 50 left): prices fall by half (bread 1, fish 1.5 shown as "3 for 2 shells" on the board, rope 2, cloth 2.5 as "2 for 5", a pot 3). Sellers wait for better prices and fewer trades happen ("Trades today" falls from 60 to 35). Granny Nell's 20 shells now buy 20 loaves. Mo's 10-shell debt is now worth 10 loaves instead of 5, so it's harder to pay. Narrator: "Less money, same goods: prices go down. That's deflation. It sounds good, but sellers wait and borrowers struggle."
- `Close the cannery` (the cannery shuts after a poor fishing year): the jobs board shows 50 workers, 10 now without jobs. Jo, a cannery worker, can't buy bread this week; Mo sells 20 fewer loaves and cuts his helper's hours. Narrator: "People who want jobs but can't find one are unemployed. When they buy less, other workers feel it too."
- Each shock's three people cards flip to show before and after.

**Explain card (end state).** The child finishes four sentences by picking from choices: "Money made trading easier because..."; "Inflation means..."; "Deflation means..."; "Unemployment means..." Each has one right ending and two that sound close. `Print` prints the card with the price board snapshots.

**Class market (extra).** Printable goods cards (with want bubbles) and shell cards for a five-minute barter round and a five-minute shell round, a projector price board the teacher updates for each shock, and the count of trades for each round.

## Content
- Five traders with wants (one chain of three swaps solves the errand); prices for five goods; three shocks with numbers; three people cards per shock; four sentence choices.
- Barter Bay and its people are made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The Money part opens only after bread is bought by barter. The three shock buttons show only after the Money part. `Reset the bay` shows only after a shock.
- Keyboard: Tab between traders; Enter to offer the selected good.
- With Motion off the sun clock and the price board change without animating.

## Look
- Accent `--brand` #7a4f00 shell ochre (header, stall signs, price board frame); gold #f4c542 (the moon shell, the selected good, price arrows); paper #fbf6ec; ink #261800; muted #5e5546.
- Contrast (WCAG 2.1, computed): white on brand 7.13:1; brand on paper 6.62:1; ink on paper 16.07:1; muted on paper 6.81:1; ink on gold 10.64:1.
- Never color alone: price changes carry up and down arrows and numbers; jobs carry counts.
- Different from this batch (ripple blue, fix-it plum, skateboard berry, valley olive).

## Art
- People art goes to Gemini with `people: true`: Mo, Hal, Wren, Ada, Granny Nell, Jo (2 poses each: at the stall, happy or worried; cutout yes); the potter's hands only (1).
- Local FLUX (`scripts/localart.py`): the harbor market (2: morning and evening, 16:9); the cannery gate open and closed (2); goods (5: bread, fish, rope, cloth, pot; 1:1, cutout yes); a moon shell (1).
- Drawn in code: want bubbles, the sun clock, the trade counter, the price and jobs boards, people cards, the explain card.
About 23 images.

## Voice
Five bank voices, each unique in this batch: `smooth-narrator` as the narrator; `hero-coach` as Mo; `gravel-ranger` as Hal; `knowing-guide` as Wren and Granny Nell; `firm-captain` as Jo and Ada. `Curio.voice` with `scope: () => state.part + ':' + state.trader + ':' + state.shock`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each want bubble and each "I don't need that" line.
- event, whole, `half-day`: "Three trades and half the day, just for one loaf!..."
- event, whole, `money`: "Money is something everyone agrees to take..."
- how `shock`: "Tap a shock to see what happens to the bay."
- event, whole, each shock's narrator line and each person's before-and-after line.
- how `explain`: "Pick the best ending for each sentence."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: want bubbles and the swap chain, the sun clock, the price board with a simple money-and-goods rule (prices scale with shells in use when goods stay the same), the jobs board and people cards.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Barter | Offer the pot to everyone | Only Wren takes it; each wrong try costs an hour, and the day can run out (the errand restarts next morning). |
| Shocks | Tap through without reading | The Explain card asks for each meaning; wrong endings replay that shock's line. |
| Explain card | Pick the longest ending | Lengths are matched; the near-miss endings name the opposite shock. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Taps: want lines (whole); offers.
2. Bread: `half-day` (whole), waits; Money: `money` (whole).
3. Shocks: `shock`; each shock: narrator line (whole), then people lines (whole).
4. End: `explain`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.5.3-5 and D2.Eco.11.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Barter needs a "double coincidence of wants"; money removes it as a medium of exchange | Federal Reserve Bank of St. Louis, Econ Lowdown, "Functions of money" | Wikipedia, Barter and Coincidence of wants (checked 2026-11-09) | yes |
| Shells (such as cowries) have been used as money | British Museum, "Cowrie shell money" | Wikipedia, Shell money (checked 2026-11-09) | yes |
| More money chasing the same goods raises prices (inflation); a falling price level is deflation, which can make debts harder to repay and make buyers wait | Federal Reserve Bank of St. Louis, Page One Economics, "Inflation" and "Deflation" | International Monetary Fund, Finance and Development, "Back to Basics: Inflation" and "Deflation" | yes |
| Unemployed means wanting work and looking for it but not having a job | U.S. Bureau of Labor Statistics, "How the government measures unemployment" | Federal Reserve Bank of St. Louis, Econ Lowdown, "Unemployment" | yes |
Backed twice: 5. Cut: 0. The prices follow a simple rule (shells in use over goods) chosen to show the idea; real prices move for many reasons, and the narrator says "when goods stay the same".

Checks run (Python, scratchpad r6, 2026-11-09): the want graph has exactly one three-swap path from pot to bread; doubling shells doubles each price and halving halves them; Granny Nell's 20 shells buy 10, 5 and 20 loaves at bread 2, 4 and 1; Mo's 10-shell debt equals 5, 2.5 and 10 loaves; 10 of 50 workers is one in five; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 all stalls fit; at 680x425 stalls become tabs.
2. Only the chain pot to rope to fish to bread gets bread by barter. (D2.Eco.5.3-5)
3. After money, any trader sells and the trades counter rises from 12 to 60. (D2.Eco.5.3-5)
4. Inflation and deflation scale every price and update the saver and borrower cards. (D2.Eco.11.3-5)
5. The cannery closing shows ten workers without jobs and the baker's lower sales. (D2.Eco.11.3-5)
6. The shock buttons and `Reset the bay` are never named before they show.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animated clock or board; no network requests.

## Open questions
- None for Cory.
