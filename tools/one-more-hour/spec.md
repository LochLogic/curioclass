# One More Hour

## One idea
It's Saturday for Dani, a made-up high school senior, and the student spends Dani's 14 waking hours one hour at a time among a shift at the grocery store ($15 an hour, time and a half after eight hours), studying for Monday's chemistry test, sleep and rest, and friends; after each hour a chart plots what that hour added (pay, test points, energy, fun) against what it cost, and the student sees the benefit of each extra hour of the same thing fall while its cost rises, then finds where to stop; surprises change the incentives (overtime kicks in, a shift gets canceled, the test is moved); then the same reasoning moves to Millbrook, a made-up town whose council is weighing a fare-free bus, a tax on sugary drinks and a downtown congestion fee, each with real cases on its card (fare-free buses in Kansas City, the Philadelphia beverage tax, congestion pricing in London, Stockholm and New York); for each, the student sees how riders, shop owners, drivers and low-income families change their choices and who gains and loses; at the end the student writes a one-paragraph argument for or against one policy that the tool checks for a margin, an incentive and the groups affected, so a twelfth grader learns how incentives shape choices and policies with costs and benefits for different groups, and how to argue with marginal benefits and costs.

## Not like
- market-day (1, spec): first choices with coins. Here choices at the margin.
- concert-ticket-market (11-12, live): supply and demand. Here one more unit at a time.
- the-buyout (12, spec): market structure. Here incentives and policy.
- two-villages (12, spec): property rights. Here marginal reasoning.

## Who and how
- Grade 12, Social Studies (Economics), module "Scarcity and Choice". Standards: D2.Eco.1.9-12 (analyze how incentives influence choices that may result in policies with a range of costs and benefits for different groups), D2.Eco.2.9-12 (use marginal benefits and marginal costs to construct an argument for or against an approach or solution to an economic issue).
- Format: simulator (the idea card proposes the change from arcade). Driver: one student alone, or the class voting on the council (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- The Saturday with 14 hours and three surprises; three town policies with real cases; the argument. Extra: Council vote (the class votes each policy, then sees who in town wins and loses). tool.json `modes: ["Saturday", "Council vote"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.2.9-12 (margins) | Place each hour and find where the extra benefit drops below the extra cost | the marginal chart for each activity | 2 |
| D2.Eco.1.9-12 (incentives) | React to surprises that change the incentives | the chart shifting; Dani's new plan | 3 |
| D2.Eco.1.9-12 (policy groups) | Apply each policy and see how four groups change choices | the town board with gains and losses | 4 |
| D2.Eco.2.9-12 (argument) | Write an argument with a margin, an incentive and the groups | the checked paragraph | 5 |

## Screens and modes
Header (kit): title "One More Hour"; `Saturday`, `Council vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A clock face with 14 waking hours, Dani's phone with texts from friends, a work schedule and a chemistry book. A card: "Where does the next hour go?" Dani is labeled "made up for this tool". The welcome is queued (`welcomeAfter: true`): "Dani has fourteen hours and a lot of pulls. Don't plan the whole day. Just decide the next hour, then the next. Tap an activity." First hint: "Tap Work, Study, Rest or Friends."

**Saturday (focus: the clock and the chart).** At 1366x768 the clock fills the left with the marginal chart right; at 680x425 the chart is a sheet. Each hour placed shows its added benefit (the 3rd hour of study adds fewer test points than the 1st; the 9th hour of work pays more with overtime but costs more energy) and its cost (what the next best use would have given). The model's rules are on a card. Surprises:
1. Overtime: after 8 hours, pay rises to $22.50 an hour.
2. A canceled shift: work hours vanish; where should they go?
3. The test moves to Wednesday: the value of a study hour today drops.
- The student marks where each activity's line crosses and explains the stop in one line.

**Millbrook council (D2.Eco.1.9-12).** Three policies, each with a real case card:
1. Fare-free buses: Kansas City made its buses fare-free in 2020; ridership effects and the cost to the budget are shown.
2. A tax on sugary drinks: Philadelphia's tax of 1.5 cents an ounce (2017); sales of taxed drinks in the city fell sharply while some shoppers bought outside the city.
3. A downtown congestion fee: London (2003), Stockholm (made permanent in 2007) and New York (2025); traffic in the zone fell.
- For each, four groups (riders, shop owners, drivers, low-income families) show how their choices change and what they gain or lose.

**The argument (the aha).** "Millbrook should (or shouldn't) ___ because the extra benefit of ___ is greater (or less) than the extra cost of ___. It changes the incentive for ___ to ___. It helps ___ and costs ___." The tool checks for a margin, an incentive and at least two groups. Narrator: "Nobody decides a whole day at once. Towns don't either. It's always one more hour, one more dollar."

**The end.** Dani's day, the marginal charts, the town board and the argument. `Print` prints them.

**Council vote (extra).** The class votes on each policy, then sees each group's gains and losses.

## Content
- Dani and Millbrook are made up and labeled; the stated hour model with falling benefit; three surprises; three policies with real case cards; four groups; the argument checker.
- Real cases are shown with findings both for and against; the tool takes no side.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Any hour can be moved before the day ends.
- Keyboard: Tab to activities, the clock, the chart, policies and the argument; Enter places an hour.
- With Motion off the clock hand jumps and the chart draws at once.

## Look
- Accent `--brand` #2b4c9b clock blue (header, the clock, the chart); gold #f4c542 (the hour being placed, the stop point); paper #f0f3fb; ink #0b1533; muted #525a6e.
- Contrast (WCAG 2.1, computed): white on brand 8.05:1; brand on paper 7.25:1; ink on paper 16.18:1; muted on paper 6.21:1; ink on gold 11.04:1.
- Never color alone: activities carry names and icons; chart lines carry labels; gains and losses carry plus and minus signs.
- Different from this batch (harvest ochre, clinic teal, line crimson, map slate).

## Art
- Local FLUX (`scripts/localart.py`): Dani's room (1, 16:9), the grocery store (1, 16:9), Millbrook's main street (1, 16:9), a bus stop (1, 4:3).
- People (illustrated) for Dani and the four town groups, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Drawn in code: the clock, the marginal chart, the town board.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Dani and the hints; `lively-host` as the council meeting host. `Curio.voice` with `scope: () => state.mode + ':' + state.hour + ':' + state.policy + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `hour`: "Pick where the next hour goes."
- event, whole, each surprise.
- how `stop`: "Mark where the extra hour stops being worth it."
- event, whole, each policy's case card.
- how `argue`: "Write your argument with a margin, an incentive and the groups."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the hour model, the clock, the marginal chart, the town board, the argument checker. Policy cards sit in a marked block `/* ONE-MORE-HOUR DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Hours | Put all 14 in one activity | The chart shows the falling benefit; the stop mark asks where it should have ended. |
| Surprises | Ignore them | The day's total shows the lost value. |
| Argument | Write an opinion | The checker needs a margin, an incentive and two groups. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `hour`.
2. Surprises (whole), waits; `stop`.
3. Policy case cards (whole).
4. `argue`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.1.9-12 and D2.Eco.2.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Time and a half after 40 hours is federal law; the tool's daily rule is labeled a model | U.S. Department of Labor, "Overtime Pay" | Fair Labor Standards Act, 29 U.S.C. 207 | yes |
| Kansas City fare-free buses from 2020 | Kansas City Area Transportation Authority, "Zero Fare" | American Public Transportation Association, fare-free transit report | yes |
| Philadelphia's 1.5 cents an ounce tax (2017) and the drop in taxed sales | Roberto and colleagues, JAMA (2019) | City of Philadelphia, "Philadelphia Beverage Tax" | yes |
| London (2003), Stockholm (2007) and New York (2025) congestion pricing; traffic fell | Transport for London, "Congestion Charge" impacts reports | Eliasson, "The Stockholm congestion charges" (Transport Policy, 2009); MTA, "Congestion Relief Zone" | yes |
| Diminishing marginal benefit | Mankiw, "Principles of Economics" (9th ed., 2020) | Council for Economic Education, "Voluntary National Content Standards in Economics" (2010) | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r24, 2026-11-09): $15 an hour at time and a half is $22.50; a 12-ounce can at 1.5 cents an ounce carries 18 cents of tax; three policies with four groups each is 12 group cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 clock and chart; at 680x425 sheet.
2. Each hour shows added benefit and cost, and the student marks a stop. (D2.Eco.2.9-12)
3. Three surprises shift the incentives. (D2.Eco.1.9-12)
4. Three policies show four groups' choices, gains and losses. (D2.Eco.1.9-12)
5. The argument passes the margin, incentive and groups check. (D2.Eco.2.9-12)
6. Real cases show findings both ways; Dani and Millbrook are labeled made up.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animation; no network requests.

## Open questions
- The idea card changes the format from arcade to simulator (default used: simulator, one hour at a time, as the card proposes).
