# Snow Season Prices

## One idea
In a snowy mountain town with a ski lift, two hotels and a rental row, the child runs a ski-rental shop for one 12-week winter, and Mr. Lindqvist, the retired owner who sold them the shop (made up, labeled "illustration"), offers advice and a $3,000 bank loan offer for new skis; each week the child sets a daily rental price and a wage for two staff, skiers arrive based on the snow and the price, and a rival shop sets its own price, and the week's sales, costs and profit post to a season chart; in week 4 a huge snowfall brings crowds, and a higher price still fills every rack; in week 7 a new rental shop opens across the street, and customers drift away unless the price comes down to match; in week 9 the hotels raise their pay, and the child's staff ask for more or leave; the child decides whether to take the loan to buy more skis on credit and sees the weekly payment; at the end of the season the chart shows price, skiers, wages and profit by week with each event marked, and the child writes one line for each turn, naming which side moved, buyers, sellers or workers; at the end the child sees that prices and wages move when buyers, sellers and competitors change, not because one shop wants them to, so a student in grades 6 to 8 learns how buyers, sellers and competition move prices and wages.

## Not like
- market-day (1, spec): tokens and choices. Here prices and wages over a season.
- the-buyout (12, spec): monopoly. Here competition arriving.
- concert-ticket-market (Grades 11-12, live): supply and demand curves. Here a shop's weekly choices.
- economy-checkup (Grades 6-8, spec): national data. Here one town's market.

## Who and how
- Grades 6-8, Economics (CTE explore), module "Snow Season Prices". Standards: D2.Eco.3.6-8 (roles of buyers and sellers in product, labor and financial markets), D2.Eco.4.6-8 (role of competition in prices and wages), D2.Eco.6.6-8 (changes in supply and demand change prices and quantities), C3 Framework.
- Format: tycoon. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card and line. Controls 48 px or more.
- Twelve weeks, a price and a wage dial, a rival, three events, the loan choice, the season chart with lines. Extra: Two shops (two students run rival shops on one device, taking turns). tool.json `modes: ["Season", "Two shops"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.3.6-8 | Sell rentals, hire staff, borrow for skis | three markets, each with a buyer's side | 2 |
| D2.Eco.4.6-8 | Respond to the rival and the hotels | price down; wages up | 3 |
| D2.Eco.6.6-8 | Explain each turn as a supply or demand shift | the marked season chart | 4 |

## Screens and modes
Header (kit): title "Snow Season Prices"; `Season`, `Two shops`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** The town map with the lift, two hotels, the rental row and the child's shop, a price board, and Mr. Lindqvist by the stove. The welcome is queued (`welcomeAfter: true`): "Your shop, your prices. Set this week's price on the board." First hint: "Turn the price dial."

**Week (focus: the shop).** At 1366x768 the town is left with the price board and week card right; at 680x425 the card is a sheet. The child sets price and wage, taps `Open the week`, and sees skiers arrive and the week's numbers.

**Events.** Week 4 snow (demand up), week 7 rival (more sellers), week 9 hotel pay (labor supply tighter). Each starts with a short news card.

**Loan.** The bank's offer: $3,000 for skis at a set rate; payments show in each week's costs if taken.

**Season chart.** Price, skiers, wages and profit by week; events marked. The child picks or writes a line for each turn ("More skiers wanted rentals, so a higher price still sold out.").

**Nobody sets it alone (the aha).** Mr. Lindqvist: "You set the price on the board. The snow, the shop across the street and the hotels set what it could be."

**The end.** The chart and lines. `Print` prints them.

**Two shops (extra).** Two players.

## Content
- The market model is simple and labeled "simulated"; skier counts follow price, snow and the rival's price.
- The town, shops and people are made up; no ski area brand names.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The season can be replayed; lines can be edited until `Print`.
- Keyboard: arrows turn the dials; Tab to Open the week, the loan, the chart and line chips; Enter picks.
- With Motion off skiers appear as a count.

## Look
- Accent `--brand` #9e2b25 ski-lift red (header, the price board, buttons); gold #f4c542 (the week in focus, events); paper #fcf0ef; ink #2b0806; muted #5f4b4a.
- Contrast (WCAG 2.1, computed): white on brand 7.43:1; brand on paper 6.67:1; ink on paper 16.53:1; muted on paper 7.27:1; ink on gold 11.33:1.
- Never color alone: chart lines carry dash styles and labels; events carry icons and names.
- Different from this batch (late-night indigo, clipboard teal, pitch-fair green, crayon magenta).

## Art
- People (illustrated): Mr. Lindqvist and two staff, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the snowy town (1, 16:9), the shop inside (1, 4:3), the rival shop (1, 4:3), skiers (2, 1:1).
- Drawn in code: dials, the board, the chart and news cards.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Mr. Lindqvist; `lively-host` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.week + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `price`: "Turn the price dial."
- how `wage`: "Turn the wage dial."
- how `open`: "Tap Open the week."
- how `loan`: "Tap Take the loan or No thanks."
- how `explain`: "Pick a line for this turn."
- event, whole, nobody sets it alone.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
Market family (no kit engine; concert-ticket-market keeps its own code). Tool-only code: a weekly demand model by price, snow and rival price; a staff supply rule tied to the hotels' wage; the loan schedule; the season chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Price | Keep one price all season | The rival and the snow make it lose money in weeks 4 and 7. |
| Wages | Never raise wages | Staff leave in week 9 and the shop can't open fully. |
| Lines | Pick any line | Each line must name the side that moved. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `price`; `wage`; `open`.
2. `loan`.
3. `explain`.
4. Nobody sets it alone (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 D2.Eco.3, 4 and 6 for grades 6-8 wording | data/standards/c3-indicators.txt | data/modules.csv module line | yes |
| Demand rises with snow; more sellers push prices down; tighter labor pushes wages up | OpenStax, "Principles of Economics", 3rd edition, chapters 3 and 4 | Council for Economic Education, "Voluntary National Content Standards in Economics", standards 7 and 8 | yes |
| Ski-town employers compete with hotels for seasonal workers | U.S. Bureau of Labor Statistics, seasonal employment in leisure and hospitality | Federal Reserve Bank of Kansas City, regional reports on mountain resort labor markets | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s27, 2026-11-10): 30 skiers a day at $40 is $8,400 a week; a $3,000 loan at 8 percent costs about $55 in interest over 12 weeks; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 town and board; at 680x425 card as a sheet.
2. Twelve weeks are run with price, wage and the loan choice. (D2.Eco.3.6-8)
3. The rival and the hotel pay change are answered. (D2.Eco.4.6-8)
4. Each turn on the chart gets a line naming the side that moved. (D2.Eco.6.6-8)
5. The model is labeled simulated; no brands.
6. `Read` reads every card and line; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: skiers as counts; no network requests.

## Open questions
None.
