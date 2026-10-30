# Grid Operator

## One idea
Electricity has to match demand every hour, so you plan a power fleet for Ridgeport, an island city with no lines to
its neighbors, then run it through three real-feeling test weeks hour by hour (a mild spring week, a heat wave with a
plant trip, a still and cloudy winter week with a gas squeeze) and watch a stack of plants rise to meet the demand
line, cheapest first; every plan gets a scorecard for cost, hours in the dark and CO2, and no fleet wins all three.

## Not like
- community-project-planner (live, 9-12): runs a neighborhood project with volunteers; here there is no city
  management at all, only the grid control room and its plants.
- Power Grid (the board game): no auctions, no map, no network building; the title is the job's real name.
- circuit-builder (grade 11 spec): the physics of one generator and its load; here plants are blocks of megawatts and
  the question is which ones run, when, and at what cost.
- island-economy (grade 9): resources over generations; here one week at a time, one resource (electricity).
- cloud-through-time and emerging-tech-pitch (wave 2): the electricity and water of data centers, and who a
  technology reaches; here the supply side.
- startup-tycoon (wave 2, "Startup Booth"): a business to profit from; here no profit, three scores to balance.
- Population Dashboard (this group): real data only; this tool is a model with real unit costs and emission factors.

## Who and how
- Grade 12, Environmental science (Earth and Space Science), Energy Sources. Students drive, pairs work well. 30 to
  45 minutes (one plan and three weeks take about 10).
- Topic line: "energy sources, cost, reliability and emissions".
- Standards (module): HS-ESS3-2 (evaluate competing design solutions for developing, managing and using energy
  resources by cost-benefit ratios): each plan is a design solution, and the scorecard is the cost-benefit evidence.
- tool.json: driver "students", minutes "30-45", modes ["Plan", "Run", "Compare"], grades_label "Grade 12".

## Screens and modes
Layout: stage left (the chart or the fleet), control panel right. A thin status bar across the top of the stage: a
skyline strip (art) whose windows dim in hours with unserved demand, the week name, day and hour. At 1366x768 the
Run controls, the chart and the live readouts fit without scrolling; at 760 wide and below the readouts move under
the chart in a two-column grid and the Run buttons stay above the chart.

**Plan (default).** Focus: the fleet, eight plant cards filling the stage in a 4 x 2 grid, each headed by its painted
plant picture (Art) with its color swatch and pattern, numbers and controls:
Nuclear, Coal unit 1, Coal unit 2, Gas combined cycle, Gas peakers, Wind, Solar, Battery.
Each card shows: megawatts now, run cost ($/MWh), CO2 (t/MWh), a "typical in the US 2024" capacity factor line, and
for buildable types the build cost per 100 MW and its weekly charge. Controls: **Retire** / **Keep** on existing
plants (coal units, the existing nuclear, CC, peakers, wind, solar); **-100** / **+100** steppers for new builds
(nuclear as small modular reactors, CC, peakers, wind, solar, battery), 0 to 1,000 MW added per type. Footer:
**Battery charging**: **Spare sun and wind only** (default) or **Also from gas overnight**. Buttons **Save plan**
(names it Plan A, B, C, D; a fifth save asks which to replace), **Run week** (goes to Run), **Start over** (base
fleet).

**Run.** Focus: the stacked chart, the biggest thing on the stage, with the live readouts in the panel. Week chips: **Spring**, **Heat wave**, **Still winter week**. Coal toggles **Coal 1 on** / **Coal 2 on** for
the week (a coal unit is committed for the whole week: on means at least 40 percent output all week). Buttons
**Play** / **Pause**, **Step hour**, **Speed** (6 or 24 hours per second), **Skip to end**. The stage: a 168-hour
stacked area chart (MW), order from the bottom: nuclear, coal minimum, wind, solar, CC, coal above minimum, battery
discharge, peakers; the demand line on top in `--ink`; unserved demand as a red cross-hatched gap between the stack
and the line; curtailed wind and solar as hollow outlines above the line; battery charging drawn below the zero axis.
Live readouts: demand now, each source now, battery charge (MWh and percent), running cost, CO2 so far, unserved
MWh and hours. Events appear as a banner and a marker on the time axis. **Scorecard** opens at the end of the week.

**Compare.** Focus: the comparison table, on the stage, with the three bar charts under it. Up to four saved plans
as columns, each week as rows, plus a three-week total row: total cost, $ per
MWh served, unserved MWh and hours, CO2 t and t per MWh, wind and solar share, curtailed MWh. Three small bar charts
(cost per MWh, unserved MWh, CO2 t) with the plan names on the bars. **Challenge cards** (optional, a drawer): four
cards, each checked live against saved plans; met cards get a check mark.

## Content
**Ridgeport:** an island city of about half a million people; peak demand 770 MW in spring, 1,000 MW in the heat
wave, 900 MW in the winter week; no imports.

**Plants** (run cost = heat rate x fuel price + variable upkeep; CO2 from fuel carbon):
| Type | Base fleet | Run $/MWh | CO2 t/MWh | Build $ per 100 MW | Weekly capital per 100 MW | Fixed upkeep $/kW-yr | US 2024 capacity factor |
|---|---|---|---|---|---|---|---|
| Nuclear (existing; new = small modular) | 300 MW, runs flat out | 9.31 | 0 | 834.9 million | 1,293,877 | 136.91 | 90.8% |
| Coal (2 units) | 2 x 200 MW, min 40% when on | 31.68 | 1.048 | (none built) | | 45.68 | 42.6% |
| Gas combined cycle | 300 MW | 19.74 | 0.337 | 117.6 million | 182,249 | 13.73 | 60.5% |
| Gas peakers | 200 MW | 32.50 | 0.524 | 86.7 million | 134,362 | 7.88 | 19.9% |
| Wind | 150 MW | 0 | 0 | 209.8 million | 325,135 | 29.64 | 34.3% |
| Solar | 100 MW | 0 | 0 | 144.8 million | 224,402 | 17.16 | 23.2% |
| Battery (100 MW, 400 MWh) | 0 | 0 | 0 | 127.0 million | 268,152 | 45.76 | n/a |
Run cost inputs: nuclear fuel 6.64 + upkeep 2.67; coal 10.777 MMBtu/MWh x $2.47 + 5.06; CC 6.370 x $2.77 + 2.10;
peaker 9.905 x $2.77 + 5.06. CO2: coal 2.31 lb/kWh; gas 116.65 lb CO2 per MMBtu times heat rate. Weekly capital =
build cost x 0.080586 / 52 (7 percent, 30 years); battery uses 0.109795 (15 years). Existing plants are paid off and
pay fixed upkeep only (base fleet: $1,369,269 a week); a retired plant pays nothing. Battery round trip 85 percent,
counted when charging (1 MWh in stores 0.85 MWh; discharge is 1 to 1); it starts each week half full. Note on screen: "Build costs are 2022 dollars, fuel 2024 prices. Use them to compare
plans, not as a bill."

**Demand** MW = day peak x hour shape. Day peaks (Mon to Sun): spring 760 770 760 750 740 660 640; heat wave 880 930
980 1,000 990 900 850; winter 870 890 900 900 880 800 780. Hour shapes (0:00 to 23:00):
- spring .70 .67 .65 .65 .66 .70 .78 .86 .91 .93 .94 .95 .95 .94 .93 .93 .94 .97 1.00 .99 .95 .88 .80 .74
- heat .62 .58 .56 .55 .55 .57 .62 .68 .73 .78 .83 .87 .91 .94 .97 .99 1.00 1.00 .97 .93 .88 .82 .74 .67
- winter .66 .63 .62 .62 .64 .70 .82 .93 .96 .92 .88 .85 .83 .81 .80 .81 .86 .96 1.00 .98 .94 .88 .80 .72
**Wind** output = MW x min(1, day factor x (1 + 0.15 cos(2 pi (hour - 3) / 24))). Day factors: spring .55 .48 .40
.45 .52 .38 .42; heat .20 .15 .10 .08 .10 .15 .22; winter .30 .12 .04 .03 .03 .05 .25.
**Solar** output = MW x peak x cloud x sin(pi x) where x = (hour + 0.5 - sunrise) / day length, only for 0 < x < 1.
Spring sunrise 6, length 13, peak .80, cloud 1 1 .6 .9 1 .7 1; heat 6, 14, .85, cloud 1 1 1 1 1 .95 1; winter 8, 9,
.55, cloud .6 .3 .2 .2 .25 .3 .5.
**Dispatch each hour.** Must-run = nuclear + coal minimums + wind + solar. If must-run covers demand: the surplus
charges the battery, then solar is curtailed, then wind; anything left is "spilled" (counted, not shown as a cost).
Otherwise fill the gap in order: CC, coal above minimum, battery discharge, peakers; anything still missing is
unserved. With "Also from gas overnight", from 0:00 to 5:00 spare CC charges the battery.
**Events.** Heat wave, day 3 at 15:00 (hour 63): the biggest fossil unit trips for the rest of the week: coal unit 2
if it is on, else coal unit 1 if on, else 200 MW of CC. Still winter week, days 3 and 4: gas supply is short and CC
is held to 70 percent of its megawatts (like the gas shortfalls in Winter Storm Elliott, December 2022).
**Challenge cards:** 1 "Coal free, lights on": both coal units retired, zero unserved in all three weeks. 2 "Under
0.2 t per MWh every week, lights on". 3 "Spring at 40 percent wind and solar". 4 "Cheapest lights-on plan": lowest
three-week $ per MWh with zero unserved (the card shows the best saved so far).
**Model note** (Plan footer, always visible): "Leaves out: power lines inside the city, start-up costs, ramp limits,
spinning reserves, maintenance outages, water use, land use, mining and fuel supply chains, and emissions other than
CO2 from burning fuel."

## Interactions in detail
- Steppers clamp at 0 and +1,000. Retiring a plant greys its card and keeps a **Keep** button to undo.
- Changing the plan while a week is running stops the run and clears the chart, with a line "Plan changed: run the
  week again".
- Every Run control stays live while Play runs: Pause stops on the current hour at once; Step hour pauses and
  steps one; Skip to end finishes at once; Speed changes the pace from the next frame; a week chip or coal toggle
  resets the run at once. A week plays in 28 s at 6 hours per second (the default, so each day is readable) or 7 s at
  24.
- The chart draws hour by hour while playing; Step hour advances one; Skip to end computes the rest at once. Pausing
  and changing week chips resets the run.
- Unserved hours flash the skyline windows dark for 300 ms in Play (no flashing faster than 3 times a second); the
  count is always in words too.
- The scorecard computes from the full 168 hours. $ per MWh divides total cost (run + fixed upkeep + weekly capital)
  by MWh served; unserved MWh is never priced.
- Compare marks the lowest value in each row with "best" in words.
- Saved plans persist in localStorage under `grid-operator`; **Clear saved plans** in Compare's footer wipes them.
- Reset (kit) returns to the base fleet, Spring, coal on, battery mode default; saved plans stay until cleared.
- `window.__tool`: `{mode, plan, week, hour, score: {cost, perMWh, unserved, shortHours, co2, co2PerMWh, wsShare,
  curtailed}, events}`.

## Look
Accent `--brand #ffbf66` (control-room amber), `--brand-ink #10161f`. Stage `#0c1219` with a faint grid `#1a2431`.
Source colors, each with a pattern and a label at the right edge of the stack: nuclear `#c9a0ff` (solid), coal
`#9aa3ad` (diagonal hatch), CC `#5aa9ff` (solid), peakers `#2f6fb8` (dots), wind `#5fd39a` (solid), solar `#ffe066`
(solid), battery `#ff9f43` (vertical lines), unserved `#ff5a5a` (cross-hatch), curtailed (outline only). Contrast
(computed): brand on --panel 10.63:1, on --sec-bg 10.07:1; brand-ink on brand 11.15:1. Nearest accent on any spec is
#ffd75e (dE 17.4); the closest in this group is Design Challenge Studio's #00f28d (dE 86).

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 9 images. Prompts say only what is in the picture.
- go-control-room: an empty grid control room at night, a wall of glowing screens with line charts, rows of empty
  desks and chairs, amber and blue light; 16:9; cutout no; people no; Plan and Compare backdrop at 15 percent
  opacity behind the cards.
- go-skyline: coastal city skyline at dusk across calm water, many lit windows, a few wind turbines on a far hill;
  4:1; cutout no; people no; status bar strip (windows dim in code with an overlay when unserved).
Plant pictures: one shared prompt, "<plant>, seen from a low hill at a distance, clear afternoon light, painted
realistic illustration, wide view"; 16:9; cutout no; people no; the header of each plant card (about 180 px wide;
the two coal cards share one picture; existing nuclear and small modular nuclear share one).
- go-nuclear: a nuclear power plant with a domed reactor building and a low turbine hall beside a coast
- go-coal: a coal power plant with a tall smokestack, a conveyor and a long black coal pile
- go-gas-cc: a modern gas combined cycle plant with two short stacks and a steam turbine hall
- go-peakers: a row of small gas turbine units in white enclosures with short stacks inside a fenced yard
- go-wind: a line of tall white wind turbines along a grassy ridge
- go-solar: rows of solar panels on a flat field under a blue sky
- go-battery: rows of white battery storage containers on a gravel pad beside a substation
Drawn in code: the stacked chart, readouts, cards' numbers and controls, color swatches and patterns, the comparison
table and bars, preview.svg.

## Voice
Bank voice `firm-captain` (Alnilam, "Say firmly but kindly, like a ship captain giving clear directions"), here the
shift supervisor. No neighbor and no other spec in this batch uses it. `Curio.voice`, `scope: () => state.mode`.
- wPlan (how; Plan welcome; stale once a Retire, Keep or stepper is pressed): "Set your fleet on the plant cards.
  Then press Run week to test it."
- wRun (how; Run welcome; stale once Play, Step hour or Skip to end is pressed): "Pick a week chip and press Play.
  Watch the stack rise to meet the demand line."
- trip (event; hour 63 of the heat wave while playing or stepping; stale after Skip to end or a reset): "A coal unit just tripped. The rest of the fleet has to cover the gap." (When the CC block trips: "A gas
  unit just tripped. The rest of the fleet has to cover the gap.")
- squeeze (event; hour 48 of the winter week; stale the same way): "Gas supply is tight for two days. Combined cycle
  is held to seventy percent."
- dark (event; first unserved hour in a run; stale the same way): "Demand is above supply. Some customers are in the
  dark."
- done (event; week ends; stale on Plan change or a new run): "Week complete. Read the scorecard, then try another
  week."
- wCompareEmpty (how; Compare opened with fewer than two saved plans; stale once two exist): "Save plans in Plan with
  Save plan. Then compare them here, week by week."
- wCompare (how; Compare opened with two or more plans; stale once the challenge drawer opens): "Read across each
  row. The word best marks the lowest number."
- challenge (event; a card is met; stale on card change): "Challenge met. Check the other two scores before you
  celebrate."

## Family engine
none.

## Sources
- Nuclear fuel and upkeep: EIA Electric Power Annual, Table 8.4 (2025 values), https://www.eia.gov/electricity/annual/
- Coal heat rate: EIA Electric Power Annual, Table 8.1 (2024). Coal and gas prices to power plants: EIA Electric Power
  Annual Table 7.20 and Electric Power Monthly Table 4.1 (2024), https://www.eia.gov/electricity/monthly/
- CC and peaker heat rates, build costs, fixed upkeep, variable upkeep and lead times: EIA, Cost and Performance
  Characteristics of New Generating Technologies, Annual Energy Outlook 2023, Table 1 (2022 dollars),
  https://www.eia.gov/outlooks/aeo/assumptions/pdf/elec_cost_perf.pdf
- Capacity factors 2024: EIA Electric Power Monthly Tables 6.07.A and 6.07.B (released 2026-10-23).
- Coal CO2 per kWh: EIA FAQ "How much carbon dioxide is produced per kilowatthour?" (2023 data, updated 2024-12-11),
  https://www.eia.gov/tools/faqs/faq.php?id=74&t=11
- Gas CO2 per MMBtu (116.65 lb): EIA Carbon Dioxide Emissions Coefficients (released 2024-09-18),
  https://www.eia.gov/environment/emissions/co2_vol_mass.php
- Gas shortfalls in cold weather: FERC and NERC, Inquiry into Bulk-Power System Operations During December 2022
  Winter Storm Elliott (October 2023), https://www.ferc.gov/media/winter-storm-elliott-report-inquiry-grid-operations-december-2022
- Demand shapes, wind and solar weeks, Ridgeport: made up for this tool, sized to the capacity factors above.
- Number checks (Python, 2026-10-29, scratch grid.py, grid2.py, grid3.py): the hourly dispatch as written (battery
  loss on charge, coal minimums must-run, trip at hour 63, CC at 70 percent on winter days 3 and 4, CO2 from 2.31
  lb/kWh and 116.65 lb/MMBtu x heat rate) reproduces every Done when number exactly (base three-week $9,843,446,
  $28.59/MWh, 116,140 t; all the retire and build cases). Run costs 9.31, 31.68, 19.74, 32.50 and CO2 1.048, 0.337,
  0.524 recomputed from their inputs; base fixed upkeep $1,369,269 a week. Every card is reachable: card 3 needs coal
  retired (with coal on, must-run curtails wind and +600 wind reaches only 25.7 percent); retire coal, +600 wind,
  +300 solar, +300 battery, +400 CC gives 50.1 percent with zero unserved. +100 and +200 CC without coal still leave
  heat wave gaps (6,248.4 and 2,216.1 MWh); +300 CC leaves 227.9 MWh in 11 hours; +400 is the smallest CC-only fix.
  Play length: 168 hours at 6 per second is 28 s, inside the 30 s guide.

## Done when
1. Base fleet, coal on: Spring total $2,948,769 ($28.43/MWh), CO2 32,582 t, no unserved, 2,000 MWh curtailed; Heat
   wave $3,407,466 ($27.82), CO2 39,115 t, no unserved; Winter $3,487,211 ($29.52), CO2 44,444 t, no unserved.
   Three-week total $9,843,446 ($28.59/MWh), CO2 116,140 t.
2. Retire both coal, build nothing: Spring $21.69/MWh, no unserved; Heat wave 12,673.6 MWh unserved in 79 hours;
   Winter 3,142.6 MWh in 46 hours.
3. Retire one coal unit (keep unit 1): Heat wave 2,216.1 MWh unserved in 30 hours (the trip hits unit 1).
4. Retire both coal, +400 CC: zero unserved all weeks; CO2 12,706 / 21,725 / 21,744 t; $29.56 / $29.37 / $30.46 per
   MWh; meets cards 1 and 2.
5. Retire both coal, +300 solar, +200 battery: Spring 27.0 percent wind and solar, no unserved; Heat wave 5,944.7 MWh
   short in 43 hours; Winter 2,889.5 MWh in 40 hours.
6. Base plus +200 battery: winter CO2 unchanged at 44,444 t (nothing spare to store), spring curtailment falls to
   1,530 MWh. Retire coal, +600 wind, +300 solar, +300 battery, +400 CC meets card 3 (50.1 percent).
7. Focus: at 1366x768 and 680x425 the plant cards fill the stage in Plan, the stacked chart is the biggest thing in
   Run, and the table in Compare; stack labels are at least 10 px in the preview.
8. A tap while Play runs: Pause stops on that hour in the same frame; a week chip resets at once; Skip to end
   finishes at once.
9. At 1366x768 Play, Step hour and the week chips sit above the fold with the chart; at 375 wide the stack labels
   stay readable and Play is visible without scrolling; all 9 images load and none shows a person.
10. Each how-to line speaks once in five actions; trip, squeeze and dark speak every run; Compare with one saved
    plan plays wCompareEmpty.

## Open questions
- [grid-operator] Build costs come from AEO2023 (2022 dollars) mixed with 2024 fuel prices, and capital uses a flat
  7 percent over 30 years (battery 15). Fine as a comparison tool, or move to newer AEO tables?
- [grid-operator] Existing coal is paid off, so the base fleet is the cheapest lights-on plan. That is true of real
  grids and is the lesson; OK, or add a carbon price slider (it would bring in policy)?
- [grid-operator] Unserved energy is never given a dollar value, so reliability stays its own score. Agree?
