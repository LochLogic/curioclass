# Water Shapes Earth

## One idea
Three lab benches where you plan fair tests on rock: freeze water in cracks (ice needs about 9 percent more room, so a
crack only breaks when it is nearly full), soak rock chips in water with more or less dissolved CO2, and run a stream
table at different slopes and flows; every result traces back to one property of water.

## Not like
- hazard-forecaster (gr 8): predicting natural hazards. Here slow, everyday processes that shape land.
- watershed-detective (gr 12 environmental, this wave): pollution moving through a watershed. Here water breaking,
  dissolving and moving rock.
- climate-dashboard and feedback-loop-builder (this group): data and systems at planet scale. Here hands-on fair tests
  at bench scale.
- hand-warmer-lab and ph-mystery-liquids (gr 10 chemistry, this wave): reactions and pH in the chemistry lab. Here pH
  only as the reason rain dissolves limestone.
- erosion-table (gr 4): a sand table with water, wind and ice to carve canyons and deltas by play. Here the stream
  table is one of three benches, run as a fair test with measured water speeds and grain thresholds, and the point is
  why water does it (expansion, solvent, density).

## Who and how
Grade 9, Earth and space science (Water and Earth Materials). Students drive, 35 to 50 minutes. Explore first:
Freeze-Thaw opens with a planned test ready to run.
Standards: HS-ESS2-5.
tool.json: driver "students", minutes "35-50", modes ["Freeze-Thaw", "Dissolve", "Stream Table"].

## Screens and modes
Header (kit, 9-12 theme): "Water Shapes Earth", small line "Ice, acid and current." Modes `Freeze-Thaw`, `Dissolve`,
`Stream Table`; kit `Motion`, `Sound`, `Read`.

Every bench has the same four steps as tabs: `Plan`, `Run`, `Graph`, `Conclude`, and a property card pinned at the top
("Water expands when it freezes", "Water with CO2 is a weak acid", "Moving water is heavy").
- Plan: a table of up to four test groups (columns) and the bench's variables (rows). Each cell is a dropdown. A fair
  test checker reads the table: "Fair test: only fill level changes" or "Two things change between groups A and B
  (rock and fill). Change one." `Run` stays enabled either way, but an unfair plan is marked in the lab book.
- Run: the bench animates each group with three trials (`Trials: 3`), each trial's result with seeded noise (±10
  percent, `Noise` toggle on by default). `Run again` reseeds.
- Graph: the bench's plot with each trial as a dot and the group mean as a bar or line.
- Conclude: a claim box (unsaved) with the sentence starter "Changing ___ made ___ because water ___." `Compare` shows a
  model answer for the plan the student ran.

### Freeze-Thaw (default)
Stage: a rock block in a freezer chamber with a crack drawn in cross-section, liquid in the crack, a cycle counter and
a crack width gauge. Freeze turns the liquid white and pushes the crack walls; thaw melts it back. Variables: Rock
(granite, sandstone, shale), Crack fill (0, 50, 80, 90, 95, 100 percent), Liquid (water, vegetable oil), Cycles (10 to
60). Result: added crack width (mm) and the cycle it broke on (break at 1.0 mm added). Default plan: sandstone, water,
40 cycles, fill 50 / 95 / 100 percent.

### Dissolve
Stage: three to four jars on a shelf, each with a 20.0 g rock chip on a scale pan under water; a week counter.
Variables: Rock (limestone, marble, granite), Water (distilled, rainwater, CO2-rich water), Temperature (cold 5 °C,
warm 25 °C), Weeks (1 to 12). Result: mass left (g). A `What happened?` card shows calcite dissolving: calcium
carbonate + water + carbon dioxide → calcium and bicarbonate in solution, and links it to caves and sinkholes.

### Stream Table
Stage: a tilted sand tray from the side and above, a water source at the top, a lake at the bottom. Variables: Slope
(0.25, 1, 4 percent), Flow (low, medium, high, flood: water depth 2, 5, 10, 15 cm in the channel), Sediment (sand,
gravel, pebbles, mixed). Result: water speed (m/s), which grains move, and a drawing of the channel and delta after a
run (more speed, deeper channel; grains sorted in the delta, biggest first).

## Content
Freeze-Thaw (lab model): ice takes 1.0907 times the room of the same water (0.9998 / 0.9167 g/cm³ at 0 °C), so ice
needs the crack to be no more than 91.7 percent full. Above that, each freeze widens the crack by rate × (fill −
0.917) / (1 − 0.917). Rates (mm per cycle at 100 percent fill; made up for the lab): granite 0.02, sandstone 0.05,
shale 0.08. Oil shrinks when it freezes: no widening. Model note: real rocks also crack from ice lenses that pull in
water as they grow; this lab shows only expansion.
Check values (no noise):
| Rock | 100 percent fill | 95 percent fill | 90 percent or less |
|---|---|---|---|
| Granite | 0.02 mm a cycle, breaks at cycle 50 | 0.008 mm, breaks at 126 (not within 60) | no widening |
| Sandstone | 0.05, breaks at 20 | 0.020, breaks at 51 | no widening |
| Shale | 0.08, breaks at 13 | 0.032, breaks at 32 | no widening |
Default plan, sandstone 40 cycles: 50 percent fill 0 mm; 95 percent 0.80 mm (no break); 100 percent breaks at cycle 20.

Dissolve (lab model, mass lost per week in grams; made up for the lab, in the right order):
| Rock | Distilled | Rainwater (pH about 5.6) | CO2-rich water |
|---|---|---|---|
| Limestone | 0.02 | 0.10 | 0.40 |
| Marble | 0.016 | 0.08 | 0.32 |
| Granite | 0.002 | 0.002 | 0.002 |
Temperature: cold water holds more dissolved CO2, so rainwater dissolves 1.2 times faster cold and CO2-rich water 1.5
times faster cold; distilled water and granite do not change with temperature. Marble is the same mineral as
limestone (calcite) in larger, tighter crystals: 0.8 times the rate. Check values after 8 weeks (no noise): limestone,
CO2-rich, cold 15.20 g left (4.80 lost); limestone, CO2-rich, warm 16.80 g; limestone, rainwater, warm 19.20 g;
marble, rainwater, warm 19.36 g; granite, any water 19.98 g; limestone, distilled 19.84 g.

Stream Table: water speed from Manning's equation v = (1/n) R^(2/3) S^(1/2) with n = 0.03 and R taken as the water
depth (a wide, shallow channel):
| Depth | Slope 0.25 percent | 1 percent | 4 percent |
|---|---|---|---|
| 2 cm (low) | 0.12 m/s | 0.25 | 0.49 |
| 5 cm (medium) | 0.23 | 0.45 | 0.91 |
| 10 cm (high) | 0.36 | 0.72 | 1.44 |
| 15 cm (flood) | 0.47 | 0.94 | 1.88 |
Grains start moving (rounded from Hjulström's curve): sand 0.5 mm at 0.20 m/s, gravel 8 mm at 0.80 m/s, pebbles 32 mm
at 1.5 m/s. Fine silt and clay stay floating at any flow and settle only in the still lake (cloudy water). In the
delta, pebbles drop first, then gravel, then sand, then silt. Water is about 1,000 kg per cubic meter, roughly 830
times denser than air near sea level, which is why moving water pushes so much harder than wind.
So: low flow at 0.25 percent moves nothing; medium at 4 percent moves sand and gravel; flood at 4 percent moves
pebbles too.

## Interactions in detail
- Fair test checker compares every pair of groups and lists each variable that differs; one difference is fair, none
  is "These groups are the same test", two or more is unfair.
- Noise: each trial multiplies the model rate by 1 + N(0, 0.05), clipped to ±10 percent, seeded per `Run`; the
  checks above are with `Noise` off.
- Freeze-Thaw animation: one cycle per 0.4 s (Motion off: instant); the crack gauge reads to 0.01 mm; a break shows a
  split block and stops that trial.
- Dissolve: the scale reads to 0.01 g; chips shrink visibly; granite never visibly changes.
- Stream Table: the run lasts 10 s; grain particles that can move are carried and sorted; those that cannot stay
  put. The speed readout is the table value.
- Lab book: each run's plan, fairness, results and claim go into a table with `Copy table`.
- Sound: ice creak per freeze, a quiet trickle in the stream; off with Sound.
- Keyboard: Tab through the plan table cells (dropdowns open with Enter), Space = Run, arrows step the Graph tab.
- Layout by real stage pixels: wide (bench and plan side by side), compact, stack (375 wide: plan table scrolls
  sideways inside its own box, the page does not).
- Mode change: `Curio.stop()`, `V.hush()`. Lab book per device (localStorage `curio-water-shapes-earth`, try/catch),
  `Clear lab book`.

## Look
Accent (`--brand`) #58acac, stream teal: 6.52:1 on --panel #141b25, 6.18:1 on --sec-bg #18202b; --brand-ink #10161f on
it 6.84:1. Moved off two blues that sat close to algebra-tile-studio (#6cc4ff) and watershed-detective (#5aa6c8);
nearest now equation-balancer #59c0ab and climate-dashboard #94c4c4 (ΔE 15), collision-lab #3cc8dc (16).
Scene: lab room #151c25, benches #3a3530, rock colors granite #9a9590 with flecks #d8d0c8 and #3a3a3a, sandstone
#c8a070, shale #5a5f66 in layers, limestone #d8d2c0, marble #ece8e0 veined #b8b4ac; water #4f8fd0 at 70 percent, ice
#e8f4ff, oil #d8b440 at 70 percent; sand #d8c08a, gravel #8a8070, pebbles #6a6560. Plots: groups in `--gr-1` to
`--gr-4`.

## Art
none: drawn in code (freezer, rock cross-sections, jars, scale, stream table, delta, plots, preview.svg).

## Voice
`gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old park ranger at a canyon overlook."
No group sibling uses it; shared in 9-12 science only with reserve-designer
(gr 9 biology, habitat design, a different setting). `Curio.voice`, `scope: () => state.mode`.
- freeze (how, Freeze-Thaw welcome): "The plan is ready. Press Run and watch the crack gauge."
- fair (event, an unfair plan is run; stale when the plan becomes fair): "More than one thing changed. You will not know which one did it."
- break (event, first break in a run; stale on Run again): "Split. That is ice doing the work."
- dissolve (how, Dissolve welcome): "Pick the water for each jar. Change one thing, then run the weeks."
- stream (how, Stream Table welcome): "Set the slope and the flow. Faster water carries bigger grains."
- conclude (how, first Conclude tab): "Say what changed, what happened, and which property of water explains it."

## Family engine
none. Plots use `kit/graphing.js` `Plane` if present; otherwise the tool's own SVG.

## Sources
- Water expands about 9 percent when it freezes; water and ice densities at 0 °C: USGS Water Science School, "Ice,
  Snow, and Glaciers and the Water Cycle" and "Water Density",
  https://www.usgs.gov/special-topics/water-science-school/science/water-density
- Critical saturation near 91 percent for frost damage: Fagerlund 1977, "The critical degree of saturation method of
  assessing the freeze/thaw resistance of concrete", Materials and Structures 10:217.
- Rain pH about 5.6 from dissolved CO2; carbonic acid dissolving limestone, caves and karst: USGS, "pH and Water" and
  "Sinkholes", https://www.usgs.gov/special-topics/water-science-school/science/ph-and-water
- Gas solubility falls as water warms: USGS Water Science School, "Dissolved Oxygen and Water" (same principle for
  CO2); OpenStax Chemistry 2e, 11.3 "Solubility".
- Manning's equation: USGS, "Measurement and Computation of Streamflow", Water-Supply Paper 2175 (1982).
- Erosion thresholds by grain size: Hjulström 1935, Bulletin of the Geological Institute of Uppsala 25:221 (curve
  values rounded).
- Air density 1.2 kg/m³: NASA Glenn Research Center, "Earth Atmosphere Model".
- Freeze and dissolve rates are made up for the lab (in the right order); every check value computed in Python
  (2026-10-27).

## Done when
1. Default Freeze-Thaw plan (noise off): 50 percent fill 0 mm; 95 percent 0.80 mm; 100 percent breaks at cycle 20.
2. Granite at 100 percent breaks at cycle 50; shale at 13; any rock at 90 percent shows no widening; oil shows none.
3. A plan with rock and fill both changing is flagged unfair and the fair line plays once.
4. Dissolve (noise off): limestone, CO2-rich, cold, 8 weeks leaves 15.20 g; granite leaves 19.98 g.
5. Stream Table: medium flow at 4 percent reads 0.91 m/s and moves sand and gravel, not pebbles; flood at 4 percent
   (1.88 m/s) moves pebbles; low at 0.25 percent moves nothing.
6. Delta after a mixed run shows pebbles nearest the stream mouth and sand farthest, silt clouding the lake.
7. Noise on: three trial dots scatter within ±10 percent around each mean.
8. How-to lines once each; event lines as listed.
9. Bench, plan table and graph usable at 1366x768; stacked at 760 and 375 wide with no page scroll sideways; labels at
   least 10 px in the 680x425 preview; no network, no images, no em dashes.

## Open questions
- [water-shapes-earth] Freeze and dissolve rates are made up (in the right order, labeled on screen). OK for a lab
  model, or look for measured rates to show beside them?
