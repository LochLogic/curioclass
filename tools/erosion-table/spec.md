# Erosion Table

## One idea
A long stream table of sand, clay and pebbles sits on a tilt stand next to a water tap, a fan, a freezer switch and a tray of grass and shrub plugs, and the student picks one thing to change (water flow, slope, wind, freezing nights or plant cover), predicts how much land will move, and runs a fast-forwarded season while the table weighs the sediment caught in the end tray and measures the depth of the channel; fair-test prompts lock every other setting, and each result goes on a bar chart; at a weathering bench, water in a rock's crack freezes and thaws until the rock splits and a tree root slowly widens another crack, and the student counts the cycles; each result links to a real photo of the same thing outdoors (a gully on a bare hillside, a river delta from the air, a dune in the wind, a frost-split boulder, roots in a sidewalk); at the end a results board ranks which agents moved the most land and which slowed it, such as plants holding soil in place, using only the student's own measurements, so a fourth grader learns to measure the effects of water, ice, wind and plants on weathering and on the rate of erosion.

## Not like
- fast-or-slow (2, spec): which changes are fast or slow. Here measuring how much each moves.
- island-maker (2, spec): shapes of land and water. Here how land wears away.
- canyon-reader (4, spec): reading layers. Here carving them.
- world-layers-map (4, spec): where features are on the globe. Here how a feature forms on a table.

## Who and how
- Grade 4, Science, module "Weathering and Erosion". Standards: 4-ESS2-1 (make observations and/or measurements to provide evidence of the effects of weathering or the rate of erosion by water, ice, wind, or vegetation).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five variables with three settings each, the fast-forwarded season, two measurements, the bar chart, the weathering bench with two tests, five real photos, the results board. Extra: Class runs (each group runs one variable and the class board fills). tool.json `modes: ["Table", "Class runs"]`, `minutes: "25-35"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4-ESS2-1 (water, wind, slope) | Change one variable, run a season and measure sediment and channel depth | the table; the tray; the chart | 2 |
| 4-ESS2-1 (ice, plants) | Count freeze-thaw cycles to split a rock; run bare and planted soil | the weathering bench; the chart | 3 |
| 4-ESS2-1 (evidence) | Rank agents on the results board from the student's own data | the board; the real photos | 4 |

## Screens and modes
Header (kit): title "Erosion Table"; `Table`, `Class runs`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A long sand table on a tilt stand, a tap, a fan, a freezer switch and a tray of plant plugs. The welcome is queued (`welcomeAfter: true`): "Pick one thing to change. Predict how much sand will move. Tap a control." First hint: "Tap the tap to set the water flow."

**The table (focus: the land).** At 1366x768 the table fills the left with controls and chart right; at 680x425 controls are a sheet. Five variables, three settings each: water flow (trickle, steady, flood), slope (low, medium, steep), wind (calm, breezy, strong), freezing nights (none, some, many), plants (bare, half, full cover). Fair-test prompts lock all but one. The student predicts sediment (a little, some, a lot), then runs a season. Channels carve, a delta forms in the tray, sand drifts into a small dune in wind. The table reports sediment in grams and channel depth in millimeters.

**Weathering bench.** A rock with water in a crack: each freeze widens it a little until it splits. The student counts cycles. A tree root in a second crack widens it over years. A note says water grows about 9 percent bigger when it freezes.

**Real-world check.** Each result links to a real photo: a gully on a bare hillside, a river delta from the air, a sand dune, a frost-split boulder, roots lifting a sidewalk.

**The results board (the aha).** Agents ranked by sediment moved with bars from the student's own runs, and a line for what slowed erosion. Narrator: "Water, wind and ice wear land away, some fast and some slow. And plants hold it together."

**The end.** The board and chart. `Print` prints them.

**Class runs (extra).** Each group runs one variable and the class board fills.

## Content
- Five variables with stated rules for sediment and depth, the weathering bench, five real photos, the results board.
- Photos are public domain (USGS, NRCS, NPS) and checked one by one, with credits in the data block.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each run waits for a prediction; any run can be repeated.
- Keyboard: Tab to controls, the prediction, `Run`, the bench and the board; arrow keys change a setting; Enter runs.
- With Motion off each run shows the table before and after.

## Look
- Accent `--brand` #4f6420 moss green (header, the chart, the board); gold #f4c542 (the changed variable, the prediction); paper #f4f7ec; ink #161d08; muted #545a4a.
- Contrast (WCAG 2.1, computed): white on brand 6.61:1; brand on paper 6.10:1; ink on paper 15.96:1; muted on paper 6.59:1; ink on gold 10.64:1.
- Never color alone: bars carry numbers and names; settings carry words.
- Different from this batch (workshop teal, civic blue, canyon rust, dusk purple).

## Art
- Local FLUX (`scripts/localart.py`): the sand table setup (1, 16:9).
- Public domain photos (USGS, NRCS, NPS), checked one by one (5, 4:3).
- Drawn in code: the land surface, water, sand drift, the tray, the rock and root, the chart and board.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the lab guide; `easy-coach` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.variable + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pick`: "Tap one control to change."
- how `predict`: "Tap how much sand you think will move."
- how `run`: "Tap Run season."
- event, whole, each run's result.
- how `bench`: "Tap Freeze, then Thaw, and count."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the table surface, the sediment model, the bench, the chart and board.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fair test | Change several settings | Prompts lock all but one. |
| Runs | Run only floods | The board needs each of the five agents. |
| Board | Rank by guess | The board ranks from the student's own runs only. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pick`; `predict`; `run`.
2. Result (whole), waits.
3. `bench`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 4-ESS2-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Water expands about 9 percent when it freezes, splitting rock (frost wedging) | U.S. Geological Survey, Water Science School, "Ice" | National Park Service, "Frost wedging" | yes |
| Plant cover reduces soil erosion by water and wind | USDA Natural Resources Conservation Service, "Soil erosion" | U.S. Environmental Protection Agency, "Erosion and sediment control" | yes |
| Steeper slopes and faster water move more sediment | U.S. Geological Survey, "Sediment and suspended sediment" | National Park Service, "Erosion" | yes |
| Wind moves sand into dunes | U.S. Geological Survey, "Sand dunes" | National Park Service, Great Sand Dunes, "Dune formation" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r29, 2026-11-09): five variables with three settings each is fifteen runs for a full board; 100 liters of water freezes into about 109 liters of ice; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 table and controls; at 680x425 sheet.
2. Water, slope and wind runs measure sediment and channel depth in fair tests. (4-ESS2-1)
3. Freeze-thaw cycles split a rock and plants slow erosion in measured runs. (4-ESS2-1)
4. The results board ranks agents from the student's own data. (4-ESS2-1)
5. Each result links to a checked public domain photo.
6. The model's rules are stated.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: before and after; no network requests.

## Open questions
- The idea card moves 4-ESS2-2 out of this tool to the new world-layers-map (default used: this tool teaches 4-ESS2-1 only; world-layers-map carries 4-ESS2-2).
