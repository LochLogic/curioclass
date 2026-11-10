# Smoke and Honey

## One idea
In the valley town of Millbrook, the paper mill's smoke sends neighbors to the clinic and the mill never pays for it, while Ana the beekeeper's bees pollinate the orchards for free and she gets nothing for it; the child tries a smoke tax, a filter rule or a payment for hives and runs a year, watching paper made and its price, mill profit and jobs, clinic visits, honey and the fruit harvest, while four families tell how the year went, so a sixth grader learns that a market makes too much of a harmful thing and too little of a helpful one until the hidden cost or benefit is counted, and that every fix helps some people and costs others, ending on a real twist: California's almond growers pay beekeepers to bring their hives.

## Not like
- border-trade-post (6, spec): trade policy between countries. Here hidden costs and benefits inside one town.
- the-shrinking-lake (6, spec): environmental change over decades and borders. Here one town's market in one year.
- concert-ticket-market (12, concept): supply and demand and prices. Here costs and benefits the price leaves out.
- pool-repair-vote (3, spec): paying for a public good with taxes or fees. Here charging for harm and paying for help.

## Who and how
- Grade 6, Social Studies (Economics), module "Smoke and Honey". Standards: D2.Eco.8.6-8 (explain how external benefits and costs influence market outcomes), D2.Eco.1.6-8 (explain how economic decisions affect the well-being of individuals, businesses, and society).
- Format: simulator. Driver: one child alone, or the class setting the tax by vote (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- A no-policy year first, then up to three policy years, the family cards and the almond card. Extra: Class vote (the class votes on the smoke tax rate and the hive payment). tool.json `modes: ["Town", "Class vote"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.8.6-8 | Run the no-policy year and find who pays for the smoke and who gets the bees' help for free | the hidden-cost and hidden-benefit arrows that light up; the clinic and orchard meters | 2 |
| D2.Eco.8.6-8 (fix) | Try a smoke tax, a filter rule, or a hive payment and compare the year's results | paper made and price, clinic visits, hives and harvest after each policy | 3 |
| D2.Eco.1.6-8 | Read the four family cards after each year and mark who gained and who paid | family cards; the gains-and-costs grid | 4 |

## Screens and modes
Header (kit): title "Smoke and Honey"; `Town`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A valley town: the paper mill's chimney upwind, houses and a clinic downwind, Ana's hives at the edge, apple and cherry orchards beyond. Four family cards along the bottom, face down. The welcome is queued (`welcomeAfter: true`): "Millbrook's mill makes paper, and Ana's bees make honey. Some of what they do lands on other people. Tap Run the year to see a normal year." First hint: "Tap Run the year."

**The no-policy year (focus: the town and the meters).** At 1366x768 the town fills the top and meters line the right; at 680x425 meters become a strip.
- The model (made for this game): the mill makes 1,000 tons of paper at $500 a ton, with 50 workers and $100,000 profit; its smoke causes about 400 clinic visits a year at $150 each, a $60,000 cost the mill doesn't pay. Ana keeps 20 hives (1,000 pounds of honey); the orchards near her harvest 100 tons of fruit; with 60 hives they would harvest 130, but Ana gets nothing from the extra fruit, so she keeps 20.
- After the year, arrows appear: a gray arrow from the chimney to the clinic labeled "Cost the mill doesn't pay: $60,000", and a gold arrow from the hives to the orchards labeled "Help Ana isn't paid for". Narrator: "The price of paper leaves out the smoke. The price of honey leaves out the fruit."

**Policy years (focus: the policy panel).** The child picks one policy and runs a year; they can try each.
- Smoke tax ($60 a ton, about the clinic cost per ton): the mill raises paper to $530, makes 900 tons, keeps 45 workers, profit falls to $63,000; visits fall to 360; the $54,000 in tax goes to a clinic fund.
- Filter rule (the mill must run a $40,000-a-year filter): paper $520, 950 tons, 48 workers, profit $74,000; visits fall to 100.
- Hive payment (orchards pay Ana $50 a hive each season): Ana grows to 60 hives (3,000 pounds of honey); the harvest rises to 130 tons; the orchards pay $3,000 and gain about $30,000 of fruit.
- The child can combine one smoke policy with the hive payment.

**The families (D2.Eco.1.6-8).** After each year four cards turn over:
- Luis, a mill worker: worried when the tax cuts jobs from 50 to 45; relieved under the filter rule (48).
- Priya, a parent whose son has asthma: fewer clinic trips under both smoke policies, most under the filter.
- Ana, the beekeeper: paid for her hives, she grows from 20 to 60.
- Mr. Okoro, an orchard grower: pays $3,000 and harvests 30 more tons.
The child marks each family Gained, Paid or Both on a grid for each policy.

**The almond card (the aha).** A real card: in California's Central Valley, almond growers pay beekeepers to bring their hives each February, about two hives an acre, and fees have run near $200 a hive in recent years; more than half of U.S. managed honeybee colonies travel there each spring. Narrator: "When people bargain over a hidden benefit, it gets counted. Smoke is harder: one mill and hundreds of neighbors can't easily bargain, so towns use taxes and rules."

**The end.** The four years side by side, the gains-and-costs grid, and a choice card: "Which plan would you pick for Millbrook, and who pays for it?" (tiles plus a free line). `Print` prints the board and the choice.

**Class vote (extra).** The class votes on the tax rate ($30, $60 or $90 a ton) and on the hive payment; the year runs with the winning choices.

## Content
- The town model (made for this game; numbers in Checks run), three policies, four family cards with lines for each policy, the gains-and-costs grid, the real almond card.
- Millbrook, the mill, Ana, Luis, Priya and Mr. Okoro are made up and labeled; the almond pollination facts are real.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- One smoke policy at a time, plus the hive payment on or off.
- The grid fills by tapping a cell to cycle Gained, Paid, Both.
- Keyboard: Tab to policies, Run, family cards and the grid; Enter to choose.
- With Motion off smoke doesn't drift and bees don't fly; meters jump.

## Look
- Accent `--brand` #3f4d63 chimney slate (header, the policy panel, cost arrows); gold #f4c542 honey (hive arrows, the chosen policy); paper #f2f4f7; ink #111824; muted #545b66.
- Contrast (WCAG 2.1, computed): white on brand 8.56:1; brand on paper 7.77:1; ink on paper 16.15:1; muted on paper 6.22:1; ink on gold 10.94:1.
- Never color alone: cost arrows are dashed and labeled "Cost", benefit arrows solid and labeled "Help"; the grid uses words.
- Different from this batch (field trip teal, river green, museum terracotta, lake blue).

## Art
- Local FLUX (`scripts/localart.py`): Millbrook valley (1, 16:9) and its version with a filtered chimney (1, 16:9); hives and orchards close-up (1, 3:2); an almond orchard in bloom with hives for the real card (1, 3:2).
- People art goes to Gemini with `people: true`: Luis, Priya and her son, Ana, Mr. Okoro (4; cutout yes).
- Drawn in code: meters, arrows, the policy panel, the grid.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as the narrator; `friendly-dad` as the four family cards' reader (one warm voice for the town). `Curio.voice` with `scope: () => state.mode + ':' + state.year + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, the year summary.
- event, whole, the hidden arrows.
- how `policy`: "Pick a policy, then tap Run the year."
- event, whole, each family card.
- how `grid`: "Mark each family Gained, Paid or Both."
- event, whole, the almond card.
- how `choose`: "Pick a plan for Millbrook and say who pays."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the town model from a small table, meters, hidden arrows, policies, family cards, the grid.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Policies | Try only one | The grid needs a column for each policy; untried columns stay open. |
| Grid | Mark everyone Gained | Each cell checks against the year; Luis under the tax plays "Look at the jobs meter." |
| Choice | Pick a plan with no reason | Print waits for "who pays". |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Year summary (whole), waits; arrows (whole).
2. `policy`; summary; family cards (whole), each waits.
3. `grid`; almond card (whole).
4. `choose`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.8.6-8 and D2.Eco.1.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| External costs and benefits make markets produce too much or too little; taxes and rules as fixes | Federal Reserve Bank of St. Louis, Page One Economics, "Externalities" | Council for Economic Education, Voluntary National Content Standards in Economics, Standard 16 | yes |
| Smoke and fine particles send people to clinics, especially children with asthma | U.S. EPA, "Particulate matter (PM) basics" and health effects | CDC, "Asthma and air pollution" | yes |
| California almond growers rent honeybee hives for pollination, about two hives an acre, with fees near $200 a hive in recent years | USDA NASS, "Cost of Pollination" (2023) | Almond Board of California, "Bees and almonds" | yes |
| A large share of U.S. managed colonies go to almond pollination each spring | USDA Agricultural Research Service, "Honey bees and almonds" | Almond Board of California | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-09): no policy 1,000 tons x ($500 - $400) = $100,000 profit, 400 visits x $150 = $60,000; tax 900 x ($530 - $400) - $54,000 = $63,000, 360 visits; filter 950 x ($520 - $400) - $40,000 = $74,000, 100 visits; hives 20 to 60, honey 1,000 to 3,000 pounds at 50 a hive, harvest 100 to 130 tons, payment $3,000; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 town and meters; at 680x425 meters are a strip.
2. The no-policy year lights the hidden-cost and hidden-benefit arrows. (D2.Eco.8.6-8)
3. Each policy changes the meters by the model. (D2.Eco.8.6-8)
4. Family cards and the grid check gains and costs. (D2.Eco.1.6-8)
5. The almond card shows the real bargain.
6. Class vote sets the rates.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no drifting smoke or flying bees; no network requests.

## Open questions
None.
