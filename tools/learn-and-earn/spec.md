# Learn and Earn

## One idea
The child runs a kid's bike repair business for one year of 52 weeks, and each week chooses to fix bikes (earn now), take a class (wheel truing or brake repair, two weeks each, no pay those weeks but higher-paying jobs after), or spend savings on a repair stand ($30, one more bike every week after), while their friend Rudy across the street fixes three flat tires every week and never trains; a running chart shows Rudy ahead early and the child pulling ahead later, and job cards along the way show how people are paid (wages, salaries, tips, commissions, owning a business), so a fourth grader learns that learning costs time now and can raise what you earn later.

## Not like
- paper-plane-assembly-line (concept): a team splitting work to make more (the idea card's overlap flag). Here one worker's own skills and tools over time.
- skateboard-fund-chances (4, spec): saving versus investing money. Here investing time in skills and tools.
- teddy-bear-makers (1, spec): steps and costs to make one product. Here how skills change pay over a year.
- careers family (later grades): exploring careers. Here one small business and the idea of human capital.

## Who and how
- Grade 4, Social Studies (Economics and Personal Finance), module "Learn and Earn". Standards: D2.Eco.6.3-5 (explain the relationship between investment in human capital, productivity, and future incomes); National Standards for Personal Financial Education (2021), grade 4: NSPFE.Earning Income.4-1b (discuss the types of knowledge, skills, interests, and experience required for different types of jobs), 4-2a (give examples of how an individual's knowledge, skills, and experience could affect their ability to earn income), 4-2b (brainstorm ways to improve one's ability to earn income), 4-3b (describe the difference between wages, salaries, commissions, and tips), 4-4a (list several businesses they would be interested in owning as an entrepreneur).
- Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- One year in four seasons, with job cards at season breaks; then the year's chart. Extra: Class strategies (enter several plans and compare). tool.json `modes: ["Year", "Class strategies"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.6.3-5 | Choose each week's action and watch money and bikes fixed against Rudy's | a 52-week calendar strip and a two-line chart (You, Rudy) of money earned | 2, 5 |
| NSPFE.Earning Income.4-2a, 4-2b | After each class, see which new jobs open and how much they pay; name one way to earn more | job board with locked and open jobs and their pay | 3 |
| NSPFE.Earning Income.4-3b | At season breaks, sort four workers by how they're paid: a bike shop mechanic (wages by the hour), a school teacher (salary), a bike salesperson (commission), a pizza delivery driver (wages plus tips) | the pay-type sort with each worker | 4 |
| NSPFE.Earning Income.4-1b, 4-4a | At year end, pick a business they'd like to own and the skills it needs | the "my business" card | 6 |

## Screens and modes
Header (kit): title "Learn and Earn"; `Year`, `Class strategies`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Two garages facing each other across a street. The child's has a toolbox, a pump and a line of bikes with flat tires; Rudy's across the street looks the same. A calendar strip reads "Week 1". The welcome is queued (`welcomeAfter: true`): "You and Rudy both fix bikes. Each week you choose: fix bikes, take a class, or buy a tool. Rudy always fixes bikes. Who will earn more this year? Tap a choice." First hint: "Tap Fix bikes, Take a class or Buy a tool."

**The year (focus: the week card and the chart).** At 1366x768 garages sit at the top, the week card center, the chart right; at 680x425 the chart folds into a `Chart` tab.
- Each week three big buttons: `Fix bikes`, `Take a class` (opens two choices: Wheel truing, Brakes), `Buy a tool` (shows only when savings reach $30).
- Pay rules (shown on the job board):
  - Flat tire fix: $4 a bike, 3 bikes a week to start.
  - Wheel truing (after the 2-week class): one wheel job a week at $8, in place of one flat fix.
  - Brake repair (after the 2-week class): one brake job a week at $6, in place of one flat fix.
  - Repair stand ($30, bought from savings): one more bike every week.
  - A class week earns $0. Classes are free at the library's fix-it club.
- Rudy: 3 flat fixes every week, $12 a week.
- A sample year (the narrator suggests it only if the child asks `Show me a plan`): wheel class weeks 1 and 2, fix weeks 3 and 4, buy the stand in week 5, brake class weeks 6 and 7, then fix every week. With it: Rudy leads until week 13; the child leads from week 14 on; at year end Rudy has $624 and 156 bikes, the child $1,012 (after paying for the stand) and 190 bikes, earning $22 a week to Rudy's $12.
- Season breaks (after weeks 13, 26, 39): a job card shows a real kind of worker and how they're paid; the child sorts it by pay type (`Wages`, `Salary`, `Commission`, `Tips`); the fourth break is the year end.
- Rudy's line at week 13: "Ha, I'm ahead! You wasted weeks on classes." At week 26 (if the child leads): "Wait, how are you fixing four bikes a week? Can you teach me wheels?"

**Year end.** The two-line chart with a marker where the lines cross. Narrator: "Learning cost you weeks of pay at the start. Then your skills and your tool helped you earn more every week. That's called investing in yourself." Then the "my business" card: the child picks a business they'd like to own one day from eight pictures (bike shop, bakery, dog walking, lemonade stand, video game studio, hair salon, farm, food truck) and picks two skills it needs from tiles. `Print` prints the chart and card.

**Class strategies (extra).** Up to six plans typed as week lists (or chosen from presets: never train, train early, train late, buy the tool first) and their year-end results side by side.

## Content
- 52 weeks; four actions (fix, two classes, a tool) with set pay rules; Rudy's fixed plan; four pay-type workers; eight business pictures and twelve skill tiles.
- Rudy and the businesses are made up; pay amounts are kid-sized, not real wages.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Buy a tool` shows only when savings reach $30 and only once. A class already taken shows "Done" in place of its button.
- `Fast forward` shows after week 8 and plays four weeks of the same choice at once.
- Keyboard: 1, 2 and 3 pick the week's action; Tab through cards.
- With Motion off the chart draws at once and bikes don't roll.

## Look
- Accent `--brand` #1d5c63 bike teal (header, your chart line, the week card frame); gold #f4c542 (the active button, crossing marker); paper #eef6f6; ink #08201f; muted #4c5a5b.
- Contrast (WCAG 2.1, computed): white on brand 7.60:1; brand on paper 6.93:1; ink on paper 15.48:1; muted on paper 6.56:1; ink on gold 10.44:1.
- Never color alone: chart lines are labeled You and Rudy and use solid and dashed strokes.
- Different from this batch (inquiry rust, made-for-whom slate, economy map blue, bill maroon).

## Art
- People art goes to Gemini with `people: true`: the child's helper character (a kid mechanic, gender-neutral, 3 poses: fixing, in class, proud; cutout yes); Rudy (3 poses: fixing, bragging, curious; cutout yes); four workers for the pay sort (1 pose each).
- Local FLUX (`scripts/localart.py`): the street with two garages (1, 16:9); the library fix-it club (1, 16:9); the repair stand (1, 1:1); eight business pictures (8, 1:1).
- Drawn in code: the calendar strip, week card, job board, chart, cards.
About 21 images.

## Voice
Three bank voices, each unique in this batch: `upbeat-guide` as the narrator; `casual-peer` as Rudy; `warm-teacher` as the fix-it club teacher who opens each class ("Today we learn to true a wheel. Spin it and watch for the wobble."). `Curio.voice` with `scope: () => state.mode + ':' + state.week + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `week`: "Pick this week's choice."
- event, whole, each class opening line and each new job line.
- event, whole, Rudy's lines at weeks 13 and 26.
- how `pay-sort`: "How does this worker get paid? Tap one."
- event, whole, `year-end`: as at year end.
- how `business`: "Pick a business you'd like to own, then two skills it needs."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the weekly plan runner with pay rules, Rudy's plan, the chart with a crossing marker, the pay-type sort and the business card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| The year | Fix every week | The chart ties Rudy all year and the narrator asks "What could help you earn more each week?" |
| The year | Take both classes and never fix | Savings never reach $30, so no stand, and the chart shows $0 for those weeks; any mix is allowed, and the end line explains the result. |
| Pay sort | Tap Wages for all | Each worker has one pay type; a wrong tap says how that worker is paid. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Each week: `week`.
2. Classes and new jobs: lines (whole). Rudy at 13 and 26 (whole).
3. Season breaks: `pay-sort`.
4. End: `year-end` (whole); `business`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.6.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| NSPFE grade 4 Earning Income outcomes 4-1b, 4-2a, 4-2b, 4-3b, 4-4a | National Standards for Personal Financial Education (CEE and Jump$tart, 2021), consumerfinance.gov copy, read 2026-11-09 | data/standards/nspfe-2021.txt (codes) | yes |
| Human capital (skills and training) raises productivity and earnings | Federal Reserve Bank of St. Louis, Econ Lowdown, "Human capital" | U.S. Bureau of Labor Statistics, "Education pays" | yes |
| Wages are paid by the hour, salaries by the year, commissions as a share of sales, tips by customers | U.S. Department of Labor, Wage and Hour Division, fact sheets on tipped employees and commissions | Consumer Financial Protection Bureau, Money as You Grow, earning income | yes |
| Bike mechanics true wheels and repair brakes; a repair stand speeds work | Park Tool, repair help ("Wheel truing", "Brake adjustment") | Wikipedia, Bicycle mechanic (checked 2026-11-09) | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-09): with the sample plan the child has $32 after week 4 and buys the stand in week 5; Rudy leads until week 13 and the child leads from week 14 to the end; year end: Rudy $624 and 156 bikes, child $1,012 and 190 bikes, $22 a week to $12; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 garages, card and chart fit; at 680x425 the chart is a tab.
2. The weekly runner gives the checked totals for the sample plan. (D2.Eco.6.3-5)
3. Classes open their jobs at their pay. (NSPFE.Earning Income.4-2a, 4-2b)
4. Four workers sort to their pay types. (NSPFE.Earning Income.4-3b)
5. The chart marks where the lines cross. (D2.Eco.6.3-5)
6. The business card prints with two skills. (NSPFE.Earning Income.4-1b, 4-4a)
7. `Buy a tool` and `Fast forward` are never named before they show.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no rolling bikes or drawn lines; no network requests.

## Open questions
- None for Cory.
