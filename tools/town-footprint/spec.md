# Town Footprint

## One idea
Maple Falls, a small made-up river town, starts with 5,000 people, and the student turns two dials over the years, population (up to 20,000) and spending per person (how much each household uses and buys), and watches three meters rise on a dashboard beside the town: water drawn from the river and wells (about 82 gallons per person per day at home, so 1,640,000 gallons a day at 20,000 people), land covered by houses, roads and parking, and electricity used; the town map grows outward, the river runs lower in late summer and a wetland shrinks, so the student sees that impacts grow with both more people and more use per person; then the student picks one impact, chooses where to put monitors (water meters with leak alerts, a river gauge, a land survey from aerial photos), sets a goal, picks fixes (fixing leaks, smart watering, water-saving fixtures, building up instead of out, rooftop solar), runs five more years and checks the monitors to see whether the fix worked; at the end a report card holds the student's design and the before and after data, so an eighth grader learns to construct an argument that increases in population and per-capita consumption raise impacts on Earth's systems, and to design a method for monitoring and minimizing a human impact on the environment.

## Not like
- lake-commons (9, spec): a shared fishery over generations. Here a whole town's water, land and energy.
- up-the-watershed (12, spec): a river basin from source to sea. Here one growing town and one fix.
- resource-map (7, spec): where resources are found. Here how fast a town uses them.
- hazard-forecaster (8, concept): natural hazards. Here impacts people cause.

## Who and how
- Grade 8, Science, module "Human Impact on Earth". Standards: MS-ESS3-3 (apply scientific principles to design a method for monitoring and minimizing a human impact on the environment), MS-ESS3-4 (construct an argument supported by evidence for how increases in human population and per-capita consumption of natural resources impact Earth's systems).
- Format: simulator. Driver: one student alone, or a teacher leading the class (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- Two dials, three meters, the growing town map, three monitor types, five fixes, a five-year test run, the argument card and the report card. Extra: Town meeting (the class votes on which impact to tackle first). tool.json `modes: ["Town", "Town meeting"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-ESS3-4 | Turn population and spending separately and argue from the meters | the dials; three meters; the river and wetland | 2, 3 |
| MS-ESS3-3 | Place monitors, set a goal, pick fixes, run and check | monitor readings; the goal line; the report card | 4 |

## Screens and modes
Header (kit): title "Town Footprint"; `Town`, `Town meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A small town from above on a bend of a river, a wetland on one side, farms around. A note: "Maple Falls is made up. Its numbers come from U.S. averages." The welcome is queued (`welcomeAfter: true`): "Maple Falls is growing. What will that do to its water, land and energy? Turn the population dial." First hint: "Turn the population dial up."

**Growing (focus: the meters).** At 1366x768 the town map is left with the dials and meters right; at 680x425 the map fills the top and the meters are a strip below. Each dial step adds five years. Population alone: meters rise in step with people. Spending alone (same people, bigger houses, more devices, greener lawns): meters rise too. Both: they rise fastest. The river line drops in late summer; the wetland shrinks as the edge of town spreads.

**The argument card.** "When ___ grew, the ___ meter rose from ___ to ___. Spending per person ___." The student taps two meter readings as evidence, one for each dial.

**Design (MS-ESS3-3).** The student picks one impact (water, land or energy). Step 1, monitor: drag monitors onto the map (water meters on homes, a river gauge, aerial photos for land, smart electric meters). Step 2, goal: set a target line (for example, cut water use 20 percent). Step 3, fixes: pick up to three (fix leaks, which can waste nearly 10,000 gallons a year in a home; smart watering; water-saving fixtures; build up instead of out; rooftop solar). Step 4, run five years. Monitors show whether the line crossed the goal. If not, change a fix and run again.

**The report card (the aha).** Before and after readings, the monitors used and the fixes. Narrator: "More people and more stuff per person both push harder on the river, the land and the air. But what you measure, you can fix."

**The end.** The argument and the report card. `Print` prints them.

**Town meeting (extra).** The class votes on which impact to tackle; results show as a bar.

## Content
- A stated town model (per-person water, land and electricity from cited U.S. averages, scaled by the spending dial), three monitors, five fixes with stated effects, the argument and report cards.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Dials can be turned down to test; the map rewinds to match.
- Keyboard: Tab to dials, meters, monitors, the goal line, fixes and `Run`; arrows turn dials; Enter places.
- With Motion off the map jumps between five-year stills.

## Look
- Accent `--brand` #2b6b2b town green (header, meters, the goal line); gold #f4c542 (the monitor in hand, the reading cited); paper #f1f7f0; ink #0c1f0b; muted #4b5a4a.
- Contrast (WCAG 2.1, computed): white on brand 6.48:1; brand on paper 5.96:1; ink on paper 15.87:1; muted on paper 6.75:1; ink on gold 10.61:1.
- Never color alone: meters carry numbers and units; the goal line carries a label.
- Different from this batch (radio navy, orchid, bone tan, safety orange).

## Art
- Local FLUX (`scripts/localart.py`): the town from above at 5,000, 10,000 and 20,000 people (3, 16:9), the river in late summer (1, 4:3), the wetland (1, 4:3).
- Drawn in code: dials, meters, monitors, the goal line, the cards.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as the town planner; `easy-coach` as hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.year + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `dial`: "Turn the population or spending dial."
- how `argue`: "Tap two meter readings as evidence."
- how `monitor`: "Drag a monitor onto the map."
- how `goal`: "Drag the goal line."
- how `fix`: "Tap up to three fixes, then tap Run."
- event, whole, the five-year result.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the town model, the growing map, monitors. Per-person figures and fix effects sit in a marked block `/* TOWN-FOOTPRINT DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Argument | Cite one dial only | The card needs a reading for each dial. |
| Design | Pick fixes without monitors | `Run` waits for at least one monitor that measures the chosen impact. |
| Goal | Set the goal at zero change | The goal must be a cut of at least 10 percent. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `dial`; `argue`.
2. `monitor`; `goal`; `fix`.
3. Five-year result (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-ESS3-3, MS-ESS3-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Americans use about 82 gallons of water a day at home | U.S. Environmental Protection Agency, WaterSense, "Statistics and facts" | U.S. Geological Survey, "Water use in the United States" | yes |
| Household leaks can waste nearly 10,000 gallons a year | U.S. Environmental Protection Agency, WaterSense, "Fix a Leak Week" | Alliance for Water Efficiency, "Leaks" | yes |
| An average U.S. home uses about 10,800 kWh of electricity a year | U.S. Energy Information Administration, "How much electricity does an American home use?" | U.S. Department of Energy, "Energy Saver" | yes |
| Growth and spreading development cover land and reduce wetlands | U.S. Environmental Protection Agency, "Smart growth and water" | U.S. Fish and Wildlife Service, "Status and Trends of Wetlands" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r4, 2026-11-10): 20,000 people at 82 gallons a day is 1,640,000 gallons; that is four times the town of 5,000; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and meters; at 680x425 strip.
2. Population and spending are turned separately and the meters rise with each. (MS-ESS3-4)
3. The argument cites one reading for each dial. (MS-ESS3-4)
4. Monitors, a goal and fixes are set, run and checked on the report card. (MS-ESS3-3)
5. Per-person figures match the cited U.S. averages.
6. The made-up town note shows.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: five-year stills; no network requests.

## Open questions
- Overlap risk with up-the-watershed and lake-commons (default used: those keep river basins and shared fisheries for high school; this tool stays with one growing town, its three meters and one monitored fix).
