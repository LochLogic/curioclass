# Town Planner: Disaster Ready

## One idea
A made-up river town sits on a coast near an offshore fault and a volcano on the skyline, much like towns in the Pacific Northwest, and the student is mayor for twenty sped-up years: each year they choose where the town's power comes from (coal, natural gas, wind, sun, a river dam), and a resource card shows where each comes from (a mine, a well, moving air, sunlight, a river) and what it does to the land, air and water (smoke, spills, a flooded valley behind a dam, land covered by panels), while a town meter tracks clean air, clean water, cost and steady power; four hazards based on real ones arrive across the years (spring floods, an earthquake, a tsunami warning after it, an ashfall), and before each one the student compares two or three ways to reduce harm (levees or moving homes uphill, bracing buildings, sirens and marked walk-out routes uphill, a tall evacuation tower, ash masks and covered water tanks) by cost and how many people each protects; losses are counted as town numbers and damaged buildings, never shown as injured people; at the end a twenty-year report shows the town's power mix and its trade-offs, and a replay runs the same hazards with no protections next to the student's plan, so a fourth grader learns that energy and fuels come from natural resources whose use affects the environment, and to compare solutions that reduce the effects of natural hazards on people.

## Not like
- grid-operator (12, spec): electricity markets. Here where power comes from and what it costs the land.
- climate-postcards (3, spec): weather hazards in real cities. Here Earth hazards in one town over time.
- community-solutions (5, concept): a town meeting on local problems. Here running the town.
- fast-or-slow (2, spec): fast and slow land changes. Here getting ready for fast ones.

## Who and how
- Grade 4, Science, module "Natural Resources and Hazards". Standards: 4-ESS3-1 (obtain and combine information to describe that energy and fuels are derived from natural resources and their uses affect the environment), 4-ESS3-2 (generate and compare multiple solutions to reduce the impacts of natural Earth processes on humans).
- Format: tycoon. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twenty years, five power sources with resource cards, the town meter with four gauges, four hazards with two or three solutions each, the report and replay. Extra: Town council (the class votes each year's choices). tool.json `modes: ["Mayor", "Town council"]`, `minutes: "30-40"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4-ESS3-1 | Choose power sources each year and read where they come from and what they do | the resource cards; the town meter | 2 |
| 4-ESS3-2 | Compare solutions before each hazard by cost and people protected | the solution cards; the hazard result | 3 |
| 4-ESS3-2 (compare) | Read the replay with no protections beside the plan | the side-by-side replay | 4 |

## Screens and modes
Header (kit): title "Town Planner: Disaster Ready"; `Mayor`, `Town council`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A town map with a river, a beach, low ground, hills and a snowy volcano on the skyline; a mayor's desk with a budget. The welcome is queued (`welcomeAfter: true`): "You're the mayor! Your town needs power, and it needs to be ready. Tap a power source to learn about it." First hint: "Tap a power source."

**Power (focus: the town).** At 1366x768 the town fills the left with the desk right; at 680x425 the desk is a sheet. Five sources with resource cards: coal (from a mine; smoke and ash), natural gas (from a well; less smoke, can leak), wind (from moving air; turbines on ridges, quiet days), sun (from sunlight; land for panels, night), a river dam (from a river; floods the valley behind it, blocks fish). The student sets the mix each year. The town meter's four gauges move: clean air, clean water, cost, steady power.

**Hazards (4-ESS3-2).** Four events over twenty years, each with a short "based on real events" card:
1. Spring floods on the low ground. Solutions: levees, moving homes uphill, a flood warning plan.
2. An earthquake. Solutions: bracing old buildings, a school safety drill, stronger bridges.
3. A tsunami warning after the earthquake. Solutions: sirens with marked walk-out routes uphill, a tall evacuation tower near the beach, both.
4. Ash from the volcano. Solutions: ash masks, covered water tanks, roof cleaning crews.
Each solution card shows cost and how many of the town's people it protects. The student picks before the event plays. Results show damaged buildings and a "people safe" count.

**The report and replay (the aha).** The twenty-year report shows the power mix and gauges over time. A replay plays the same four hazards with no protections next to the student's plan. Narrator: "Every power source comes from somewhere and changes something. And you can't stop an earthquake, but planning ahead keeps people safe."

**The end.** The report and a "Get ready at home" card pointing to real preparedness pages. `Print` prints them.

**Town council (extra).** The class votes each year's choices.

## Content
- A made-up town and people; real hazard types, solutions and costs stated as low, medium or high; twenty years; the report.
- Losses are town numbers and damaged buildings; no injured or dead people shown or named.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each year waits for a power choice; each hazard waits for a solution choice.
- Keyboard: Tab to sources, sliders, solution cards, `Next year` and the report; arrow keys set the mix; Enter picks.
- With Motion off hazards show before and after pictures without shaking or waves.

## Look
- Accent `--brand` #2d4a8a civic blue (header, the desk, the meter); gold #f4c542 (the chosen card, a protected building); paper #f0f3fa; ink #0c1630; muted #525a6b.
- Contrast (WCAG 2.1, computed): white on brand 8.54:1; brand on paper 7.69:1; ink on paper 16.12:1; muted on paper 6.23:1; ink on gold 11.01:1.
- Never color alone: gauges carry numbers and words; damaged buildings carry a mark.
- Different from this batch (workshop teal, canyon rust, dusk purple, moss green).

## Art
- Local FLUX (`scripts/localart.py`): the town (1, 16:9), five power sources (5, 4:3), four hazards as places, not victims (4, 16:9), solution pictures (11, 4:3).
- Drawn in code: the map, gauges, cards, the report and replay.
About 21 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as the emergency manager; `news-reader` as the town radio and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.year + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `power`: "Set this year's power mix."
- event, whole, each resource card.
- how `prepare`: "Pick a solution before the event."
- event, whole, each hazard's result, told calmly as damage and people safe.
- how `report`: "Tap Replay to compare."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the year loop, the power mix, gauges, hazards, the replay.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Power | Pick one source every year | Allowed, but the report asks what it cost the land, air or water. |
| Hazards | Buy every solution | The budget can't cover them all. |
| Report | Skip the replay | The report needs the replay viewed first. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `power`; resource card (whole), waits.
2. `prepare`; hazard result (whole).
3. `report`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 4-ESS3-1, 4-ESS3-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Where coal, gas, wind, solar and hydropower come from and their effects | U.S. Energy Information Administration, "Energy Kids: Energy sources" | U.S. Department of Energy, "Energy sources" | yes |
| The Cascadia fault's last great earthquake and tsunami was January 26, 1700 | U.S. Geological Survey, "Cascadia Subduction Zone" | Atwater and colleagues, "The Orphan Tsunami of 1700" (USGS and University of Washington Press, 2005) | yes |
| Tsunami walk-out routes and vertical evacuation towers (Ocosta Elementary, Westport, Washington) | Washington Emergency Management Division, tsunami program | National Tsunami Hazard Mitigation Program (NOAA) | yes |
| Ashfall effects and protections (masks, covered water) | U.S. Geological Survey, Volcano Hazards Program, "Volcanic ash" | International Volcanic Health Hazard Network | yes |
| Bracing buildings and flood planning reduce harm | Federal Emergency Management Agency, Ready.gov | U.S. Geological Survey, "Earthquake Hazards" | yes |
Backed twice: 6. Cut: 0.
Sensitivity note: natural disasters can frighten children and touch families who have lived through one; the town and its people are made up, losses are shown only as damaged buildings and a "people safe" count, hazards are told calmly, and the end points to real preparedness pages.

Checks run (Python, scratchpad r29, 2026-11-09): twenty years and four hazards; three solutions for each of four hazards is twelve, and the combined tsunami choice reuses two pictures, so eleven solution pictures; the Cascadia earthquake of 1700 was 326 years before 2026; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 town and desk; at 680x425 sheet.
2. Power is chosen each year with resource cards and the town meter. (4-ESS3-1)
3. Solutions are compared before each of four hazards. (4-ESS3-2)
4. The replay with no protections plays beside the plan. (4-ESS3-2)
5. No injured people are shown; losses are town numbers.
6. The end card points to real preparedness pages.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no shaking or waves; no network requests.

## Open questions
- Sensitivity flag: natural disasters (default used: made-up town, losses only as damaged buildings and a people-safe count, calm telling, preparedness pages at the end, fresh-agent read before build).
