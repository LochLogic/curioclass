# Border Trade Post

## One idea
At a border post between two made-up neighbors, Southland and Northland, the child runs three quick rounds of trade: barter (hunting for someone who has what you want and wants what you have, while a clock counts the wasted minutes), money (the same trades in a fraction of the time), and a tariff on Northland's bikes, where shoppers pay more, Southland's bike makers sell more and hire back workers, Northland answers with a tariff on Southland's apples, and the apple farmers lose sales; a scoreboard then compares the tariff with two other answers to the same problem (no tariff, and no tariff plus training for laid-off bike workers) group by group, so a sixth grader learns how money cuts the cost of trading, how barriers like tariffs change trade between nations, and how to weigh who gains and who pays.

## Not like
- barter-bay (4, spec): barter to money and prices inside one town. Here barter is a short timed opener and the focus is trade between countries.
- smoke-and-honey (concept): hidden costs inside one town. Here costs and benefits across a border.
- cocoa-chain (concept): a supply chain. Here a trade barrier.
- market-day (2, spec): buying and selling at a market. Here a tariff's ripple through groups.

## Who and how
- Grade 6, Social Studies (Economics), module "Border Trade Post". Standards: D2.Eco.5.6-8 (explain ways in which money facilitates exchange by reducing transactional costs), D2.Eco.15.6-8 (explain barriers to trade and how those barriers influence trade among nations), D2.Eco.2.6-8 (evaluate alternative approaches or solutions to current economic issues in terms of benefits and costs for different groups and society as a whole).
- Format: simulator. Driver: one child alone, or two players running the two countries (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Three rounds, then the scoreboard and a written judgment. Extra: Two countries (each player sets one country's tariff; they see each other's answer). tool.json `modes: ["Trade post", "Two countries"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.5.6-8 | Make the same five trades by barter, then with money | the clock: minutes wasted searching in barter, few with money; a "double coincidence" line each time a match is found | 2 |
| D2.Eco.15.6-8 | Set a tariff on imported bikes and watch prices, sales, jobs and the other country's answer | the stalls' price tags, sales counts, jobs, and Northland's tariff on apples | 3 |
| D2.Eco.2.6-8 | Compare three answers on the scoreboard and write which is fairest and why | the scoreboard of six groups across three answers; the judgment card | 4, 5 |

## Screens and modes
Header (kit): title "Border Trade Post"; `Trade post`, `Two countries`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A border gate with a striped barrier, a market stall on each side (Southland's apples and bikes; Northland's bikes and wool), and a big clock. The welcome is queued (`welcomeAfter: true`): "This border post connects two neighbors. First, trade the old way, with no money. Tap a trader to see what they have and what they want." First hint: "Tap a trader."

**Round 1: Barter (focus: six traders and the clock).** At 1366x768 six traders stand in a row with have-and-want cards; at 680x425 they are a scrolling row.
- The child has 10 crates of apples and wants a bike part, wool for a sweater and a wheel. Each trader has one thing and wants one thing; most don't want apples. The child has to find chains (apples to the baker for bread, bread to the weaver for wool...).
- Each visit costs 5 minutes on the clock. Five trades take about 60 to 90 minutes, depending on the path. Narrator: "Barter only works when you find someone who has what you want and wants what you have."
- Kept short: one goal, five trades (barter-bay teaches barter in depth).

**Round 2: Money (focus: the same traders with price tags).** The same five trades, now with coins: sell apples to whoever wants them, buy what you need from whoever has it. Each visit still costs 5 minutes, so five trades take 25 to 30. The clock shows both rounds side by side. Narrator: "Money doesn't make the apples better. It makes trading faster, because everyone takes it."

**Round 3: The tariff (focus: the bike stalls, the scoreboard strip).** A story card: Northland's bikes got cheaper last year. Southland's bike shop, Ridgeline Cycles, used to employ 10 workers and now employs 6; 4 lost their jobs. Southland's council asks the child to set a tariff on imported bikes: 0, 10, 25 or 50 percent.
- The season model (100 Southland shoppers who want a bike; numbers made for this game):
  - No tariff: Northland bikes $100, Southland bikes $120; shoppers buy 70 Northland and 30 Southland (100 bikes, $10,600 spent, average $106). Ridgeline employs 6. Southland sells Northland 200 crates of apples at $10 ($2,000), with 4 apple pickers.
  - 25 percent tariff: Northland bikes $125; Ridgeline raises its price to $122. Shoppers buy 90 bikes, 50 Southland and 40 Northland, spending $11,100 (average about $123). The government collects $1,000. Ridgeline hires back to 10 workers. Northland answers with its own tariff on apples: sales drop to 150 crates ($1,500), and one apple picker is let go. Northland's bike sales in Southland fall from $7,000 to $4,000.
  - 10 and 50 percent follow the same model with smaller or larger effects.
- After each choice the strip shows six groups: shoppers, Ridgeline's owners, bike workers, apple farmers and pickers, Northland's bike makers, Southland's government.

**The scoreboard (the aha).** Three answers side by side: No tariff; 25 percent tariff; No tariff plus help (Southland spends $600 a season in taxes on job training for the 4 laid-off bike workers). For each group the child marks Gains, Pays or Same, and the board checks:
- Shoppers: pay more and get fewer bikes under the tariff; same under the other two.
- Bike workers: gain jobs under the tariff; get training under help; same under no tariff.
- Apple farmers and pickers: pay under the tariff (Northland's answer); same under the others.
- Government and taxpayers: gain tariff money; pay $600 under help.
- Northland's bike makers: pay under the tariff.
- A real-world card: in 2018 the U.S. put tariffs on imported washing machines; economists found prices rose for shoppers and about 1,800 U.S. jobs were added, at a cost to shoppers of about $815,000 a year for each job (Flaaen, Hortaçsu and Tintelnot, 2020). The card is offered as one study's finding, not a verdict.

**The judgment (D2.Eco.2.6-8).** The child picks the answer they think is fairest and writes why from tiles plus a free line ("It helps the most people", "It protects the workers who lost jobs", "It keeps prices low for shoppers", "It doesn't hurt the apple farmers"). Narrator: "Every answer helps some people and costs others. Good decisions say who pays." There is no right answer; the board checks only the gains-and-pays marks.

**The end.** The clock comparison, the scoreboard, the judgment. `Print` prints them.

**Two countries (extra).** Each player sets one country's tariff each season for three seasons; the board shows both sides' groups after each season.

## Content
- Six barter traders with haves and wants, the price list for round 2, the tariff model with four rates, the three answers, six groups, the real-world card and judgment tiles.
- Southland, Northland, Ridgeline Cycles and every number in the model are made for this game and labeled; the washing machine study is real.
- The topic is kept neutral: no current country, leader or party is named; the real-world card names a study and its numbers.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Barter: tap a trader to visit (the clock adds 5 minutes); tap Trade when a match exists.
- The tariff dial snaps to 0, 10, 25 or 50; `Run the season` plays the result.
- Keyboard: Tab to traders, dial and board cells; Enter to visit, trade, run or mark; arrows on the dial.
- With Motion off the clock hands jump and stalls update without sliding.

## Look
- Accent `--brand` #3d5a1e border-post olive (header, the gate, the dial); gold #f4c542 (the clock hand, the chosen answer); paper #f4f7ef; ink #141f08; muted #535a4b.
- Contrast (WCAG 2.1, computed): white on brand 7.84:1; brand on paper 7.24:1; ink on paper 15.78:1; muted on paper 6.62:1; ink on gold 10.50:1.
- Never color alone: Gains, Pays and Same carry the words and arrows (up, down, flat).
- Different from this batch (agora blue, silk road mulberry, Rome crimson, farmer ochre).

## Art
- People art goes to Gemini with `people: true`: six barter traders (1 each; cutout yes); Ridgeline's owner and two workers (1 scene); apple pickers (1 scene); a shopper family (1).
- Local FLUX (`scripts/localart.py`): the border post with two stalls (1, 16:9); the bike shop (1, 3:2); the orchard (1, 3:2).
- Drawn in code: the clock, price tags, the dial, the scoreboard, the judgment card.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as the narrator; `playful-friend` as Pip, a young trader (made for this game) who reads haves and wants. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `visit`: "Tap a trader to see what they have and want."
- event, whole, each trade.
- how `money`: "Now trade with coins. Tap a trader."
- event, whole, the clock comparison.
- how `tariff`: "Set the tariff dial, then tap Run the season."
- event, whole, each season result.
- how `board`: "Mark Gains, Pays or Same for each group."
- how `judge`: "Pick the fairest answer and say why."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the barter search with a clock, the price round, the tariff model from a small table, the scoreboard checks and the judgment card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Barter | Visit every trader | It works but the clock shows the cost; that is the lesson. |
| Tariff | Set 0 and skip | The scoreboard still needs all three answers marked; the tariff column runs on 25 percent if not set. |
| Scoreboard | Mark everything "Gains" | Each cell checks against the model and explains. |
| Judgment | Leave it blank | Print waits for a pick and a reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `visit`; trades (whole).
2. `money`; clock comparison (whole).
3. `tariff`; season result (whole), waits.
4. `board`; `judge`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.5.6-8, D2.Eco.15.6-8 and D2.Eco.2.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Money lowers the cost of trading by ending the need for a double coincidence of wants | Federal Reserve Bank of St. Louis, Page One Economics, "Functions of money" | Council for Economic Education, Voluntary National Content Standards in Economics, Standard 11 | yes |
| A tariff raises prices for buyers, helps protected producers, brings in government revenue, and can bring retaliation | Federal Reserve Bank of St. Louis, "What are tariffs?" | Council for Economic Education, Standard 5 (trade) | yes |
| The 2018 washing machine tariffs: prices rose, about 1,800 jobs added, about $815,000 a year in shopper costs per job | Flaaen, Hortaçsu and Tintelnot, "The Production Relocation and Price Effects of US Trade Policy," American Economic Review (2020) | Federal Reserve Board, FEDS Notes summary of the same study (2019) | yes |
| Governments use job training for workers hurt by trade | U.S. Department of Labor, Trade Adjustment Assistance program | Congressional Research Service, "Trade Adjustment Assistance for Workers" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r10, 2026-11-09): no tariff 70 x $100 + 30 x $120 = $10,600 for 100 bikes; 25 percent tariff 50 x $122 + 40 x $125 = $11,100 for 90 bikes, average $123.33; tariff money 40 x $25 = $1,000; jobs at 5 bikes per worker, 6 and 10; apples 200 crates at $10 = $2,000 and 150 = $1,500, pickers at 50 crates each, 4 and 3; Northland bike sales $7,000 and $4,000; barter at 5 minutes a visit takes 60 to 90 minutes and money 25 to 30; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 traders in a row; at 680x425 they scroll.
2. The clock shows barter taking longer than money for the same five trades. (D2.Eco.5.6-8)
3. Each tariff rate changes prices, sales, jobs and brings Northland's answer. (D2.Eco.15.6-8)
4. The scoreboard checks Gains, Pays and Same for six groups under three answers. (D2.Eco.2.6-8)
5. The judgment takes a pick and a reason and prints. (D2.Eco.2.6-8)
6. Two countries runs three seasons with both dials.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no moving clock hands; no network requests.

## Open questions
None.
