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
- Run: every group runs at once, side by side on the bench, with three trials each (`Trials: 3`), each trial's
  result with seeded noise (±10 percent, `Noise` toggle on by default). The bench animates trial 1 of each group;
  trials 2 and 3 are computed at once and appear as dots on Graph and in the result row. `Run again` reseeds.
  `Skip to end` (live only while a run plays) jumps to the final state at once.
- Graph: the bench's plot with each trial as a dot and the group mean as a bar or line.
- Conclude: a claim box (unsaved) with the sentence starter "Changing ___ made ___ because water ___." `Compare` shows a
  model answer for the plan the student ran.
Focus by tab: Plan, the plan table (it sits in the panel beside a still view of the bench, so the bench stays the
largest thing); Run, the bench itself, central and biggest, with the gauge or scale readouts next to each group;
Graph, the plot takes the stage's place; Conclude, the claim box with the graph shrunk beside it.
Anything that plays keeps every control live: switching tabs or modes, editing a plan cell (which stops the run and
marks it "plan changed"), `Run again` and `Skip to end` all act at once, never at the next cycle or week.

### Freeze-Thaw (default)
Focus: the cracked rock blocks in the freezer, one per group, the crack gauges under them.
Stage: the painted freezer chamber (`ws-freezer`) with up to four rock blocks in a row, each a code shape filled with
its painted rock face (`ws-granite`, `ws-sandstone`, `ws-shale`) and split by a crack drawn in code in cross-section,
liquid in the crack, a cycle counter and a crack width gauge per block. Freeze turns the liquid white and pushes the
crack walls; thaw melts it back. Variables: Rock (granite, sandstone, shale), Crack fill (0, 50, 80, 90, 95, 100
percent), Liquid (water, vegetable oil), Cycles (10 to 60). Result: added crack width (mm) and the cycle it broke on
(break at 1.0 mm added). Default plan: sandstone, water, 40 cycles, fill 50 / 95 / 100 percent.

### Dissolve
Focus: the jars and the scale readouts under them.
Stage: three to four painted jars (`ws-jar`) on the bench of the painted lab room (`ws-lab-room`), each with a 20.0 g
painted rock chip (`ws-chip-limestone`, `ws-chip-marble`, `ws-chip-granite`) on the pan of a painted scale
(`ws-scale`, readout in code over its blank display) under water; a week counter. CO2-rich water shows fine rising
bubbles drawn in code.
Variables: Rock (limestone, marble, granite), Water (distilled, rainwater, CO2-rich water), Temperature (cold 5 °C,
warm 25 °C), Weeks (1 to 12). Result: mass left (g). A `What happened?` card shows calcite dissolving: calcium
carbonate + water + carbon dioxide → calcium and bicarbonate in solution, and links it to caves and sinkholes.

### Stream Table
Focus: the sand tray from above, with the channel cutting and the delta building.
Stage: the painted sand tray from above (`ws-stream-tray`), a water source at the top, a lake at the bottom; a small
side view in code shows the slope. The channel, water, delta and sand grains are drawn in code over the tray (they
bend and grow); gravel and pebbles are painted cutouts (`ws-gravel`, `ws-pebble`) moved and scaled in code. Group
tabs `A` to `D` over the tray show one group's run at a time; a tap shows that group at once. Variables: Slope
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
| 5 cm (medium) | 0.23 | 0.45 | 0.90 |
| 10 cm (high) | 0.36 | 0.72 | 1.44 |
| 15 cm (flood) | 0.47 | 0.94 | 1.88 |
Grains start moving (rounded from Hjulström's curve): sand 0.5 mm at 0.20 m/s, gravel 8 mm at 0.80 m/s, pebbles 32 mm
at 1.5 m/s. Fine silt and clay stay floating at any flow and settle only in the still lake (cloudy water). In the
delta, pebbles drop first, then gravel, then sand, then silt. Water is about 1,000 kg per cubic meter, roughly 830
times denser than air near sea level, which is why moving water pushes so much harder than wind.
So: low flow at 0.25 percent moves nothing; medium at 4 percent (0.90 m/s) moves sand and gravel; flood at 1 percent
(0.94) moves gravel; only flood at 4 percent (1.88) moves pebbles.

## Interactions in detail
- Fair test checker compares every pair of groups and lists each variable that differs; one difference is fair, none
  is "These groups are the same test", two or more is unfair.
- Noise: each trial multiplies the model rate by 1 + N(0, 0.05), clipped to ±10 percent, seeded per `Run`; the
  checks above are with `Noise` off.
- Freeze-Thaw animation: all blocks step together, one cycle per 0.25 s, so 60 cycles take 15 s (Motion off:
  instant); the crack gauge reads to 0.01 mm; a break shows the block's two halves pushed apart and stops that
  trial.
- Dissolve: one week per second, so 12 weeks take 12 s (Motion off: instant); the scale reads to 0.01 g; each chip
  cutout shrinks in area with its mass; granite never visibly changes.
- Stream Table: each group's run lasts 5 s and the groups play A to D in turn (20 s for four; Motion off: instant);
  a group tab shows that group at once. Grains that can move are carried and sorted; those that cannot stay put.
  The speed readout is the table value.
- Lab book: each run's plan, fairness, results and claim go into a table with `Copy table`.
- Sound (on at start, as the kit sets it): ice creak per freeze, a quiet trickle in the stream; off with Sound.
- Keyboard: Tab through the plan table cells (dropdowns open with Enter), Space = Run, arrows step the Graph tab.
- Layout by real stage pixels: wide (bench and plan side by side), compact, stack (375 wide: plan table scrolls
  sideways inside its own box, the page does not).
- Mode change: `Curio.stop()`, `V.hush()`. Lab book per device (localStorage `curio-water-shapes-earth`, try/catch),
  `Clear lab book`.

## Look
Accent (`--brand`) #58acac, stream teal: 6.52:1 on --panel #141b25, 6.18:1 on --sec-bg #18202b; --brand-ink #10161f on
it 6.84:1. Moved off two blues that sat close to algebra-tile-studio (#6cc4ff) and watershed-detective (#5aa6c8);
nearest now equation-balancer #59c0ab and climate-dashboard #94c4c4 (ΔE 15), collision-lab #3cc8dc (16).
Scene: the painted freezer, lab room and stream tray set the scene colors (cold blue-white frost, warm wood benches,
damp tan sand). Colors still drawn in code: water #4f8fd0 at 70 percent, ice #e8f4ff, oil #d8b440 at 70 percent,
crack and channel edges #2a2622, sand grains #d8c08a, silt cloud #b8a888 at 40 percent. Plots: groups in `--gr-1` to
`--gr-4`. Readouts sit on the kit panel or on blank painted displays, never on busy painting.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 13 images. Text, gauges and readouts stay in code.
- ws-freezer: the inside of a large lab chest freezer, frosted white metal walls, a wire rack floor, cold blue light;
  16:9; cutout no; people no; Freeze-Thaw backdrop behind the rock blocks.
- ws-lab-room: a quiet school earth science lab, long wooden benches, rock specimens on open shelves, soft daylight
  from tall windows; 16:9; cutout no; people no; Dissolve backdrop (the jars stand on its bench) and dimmed around
  the Stream Table tray.
- ws-granite: a flat sawn face of speckled grey granite with white, pink and black crystals, filling the frame; 1:1;
  cutout no; people no; texture clipped to the granite block shape (each half after a break).
- ws-sandstone: a flat sawn face of tan sandstone with fine sand grains and faint bedding lines, filling the frame;
  1:1; cutout no; people no; texture clipped to the sandstone block shape.
- ws-shale: a flat face of dark grey shale in thin layered sheets, filling the frame; 1:1; cutout no; people no;
  texture clipped to the shale block shape.
- ws-chip-limestone: a single fist-sized chip of pale cream limestone with a rough broken surface, on plain white;
  1:1; cutout yes; people no; the limestone chip on the scale pan, scaled down in code as it loses mass.
- ws-chip-marble: a single chip of white marble with soft grey veins and a sugary sparkle, on plain white; 1:1;
  cutout yes; people no; the marble chip, scaled the same way.
- ws-chip-granite: a single chip of speckled grey granite with white and black crystals, on plain white; 1:1; cutout
  yes; people no; the granite chip (it never shrinks).
- ws-jar: a tall clear glass jar with a metal screw lid, three quarters full of clear water, on plain white; 3:4;
  cutout yes; people no; one per Dissolve group, drawn over the chip and scale; water tint and bubbles in code.
- ws-scale: a small white digital lab balance with a round steel pan and a plain blank dark display, on plain white;
  4:3; cutout yes; people no; under each jar, the reading drawn in code over the display.
- ws-stream-tray: a long wooden stream table tray filled with smooth damp tan sand, seen from straight above, a small
  pool of still water at the low end; 16:9; cutout no; people no; Stream Table stage under the code channel and
  delta.
- ws-gravel: a single small rounded grey-brown gravel stone, on plain white; 1:1; cutout yes; people no; gravel
  grains, drawn small and many times with slight rotation.
- ws-pebble: a single smooth oval river pebble, dark grey with a pale band, on plain white; 1:1; cutout yes; people
  no; pebble grains, drawn larger than gravel.
Drawn in code: cracks, liquid and ice in the cracks, gauges, scale readouts, water, channel, delta, sand grains and
silt, the slope side view, plan tables, plots, preview.svg.

## Voice
`gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old park ranger at a canyon overlook."
Kept: reserve-designer, the one neighbor that shared it, has moved to warm-teacher in its own revision, and no tool
`neighbors.py` lists for this one or other spec in this batch uses gravel-ranger now (easy-coach was tried and
dropped: lake-commons, gr 9, now uses it). `Curio.voice`, `scope: () => state.mode`.
- freeze (how; Freeze-Thaw welcome with the default plan ready; stale once Run is pressed or a plan cell changes):
  "The plan is ready. Press Run and watch the crack gauges."
- fair (event; a run starts with an unfair plan; stale when the plan becomes fair or the run ends): "More than one
  thing changed. You will not know which one did it."
- break (event; the first block in a run splits; stale on Run again or a plan change): "Split. That is ice doing
  the work."
- dissolve (how; Dissolve welcome; stale once a plan cell changes or Run is pressed): "Pick the water for each jar in
  the Plan table. Change one thing, then press Run."
- stream (how; Stream Table welcome; stale once a plan cell changes or Run is pressed): "Set the slope and the flow
  in the Plan table, then press Run. Faster water carries bigger grains."
- conclude (how; the Conclude tab opens for the first time; stale once the student types or presses Compare):
  "Type what changed, what happened, and which property of water explains it. Then press Compare."

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
- Number checks (Python, 2026-10-29): ice volume ratio 0.9998 / 0.9167 = 1.0907 (critical fill 0.9169, used as
  0.917). Every Freeze-Thaw check value recomputed (granite 95 percent 0.0080 mm a cycle, breaks at 126; sandstone
  95 percent 0.0199, 0.795 mm at 40 cycles, shown 0.80; with noise at ±10 percent, sandstone 95 percent breaks
  between cycles 46 and 56). All 18 Dissolve cells at 8 weeks recomputed; the largest loss the tool allows is
  limestone, CO2-rich, cold, 12 weeks: 7.20 g, 12.80 g left. Manning table recomputed: medium at 4 percent is 0.9048
  m/s, so the old 0.91 is corrected to 0.90 (it still moves gravel, not pebbles); flood at 1 percent (0.94) also
  moves gravel, now said. Water over air 1,000 / 1.2 = 833. Noise N(0, 0.05) clipped at ±10 percent clips 4.5
  percent of draws; a dot can sit up to 13 percent from its group's mean, so Done when checks against the no-noise
  value. Auto-plays: the old run, group by group at 0.4 s a cycle, took up to 96 s; now groups run together, at most
  15 s (Freeze-Thaw), 12 s (Dissolve) and 20 s (Stream Table).

## Done when
1. Default Freeze-Thaw plan (noise off): 50 percent fill 0 mm; 95 percent 0.80 mm; 100 percent breaks at cycle 20.
2. Granite at 100 percent breaks at cycle 50; shale at 13; any rock at 90 percent shows no widening; oil shows none.
3. A plan with rock and fill both changing is flagged unfair and the fair line plays when it runs.
4. Dissolve (noise off): limestone, CO2-rich, cold, 8 weeks leaves 15.20 g; granite leaves 19.98 g.
5. Stream Table: medium flow at 4 percent reads 0.90 m/s and moves sand and gravel, not pebbles; flood at 4 percent
   (1.88 m/s) moves pebbles; low at 0.25 percent moves nothing.
6. Delta after a mixed run shows pebbles nearest the stream mouth and sand farthest, silt clouding the lake.
7. Noise on: every trial dot lies within ±10 percent of its group's no-noise value.
8. Focus: on the Run tab the bench (blocks, jars or tray) is the largest thing on screen at 1366x768 and in the
   680x425 preview; on Graph the plot is.
9. A tap while a run plays: a group tab, `Skip to end`, a plan cell or a mode button acts in the same frame; no run
   plays longer than 20 s.
10. How-to lines once each per page load; fair and break each time their event happens; no line names a control
    that is not live.
11. Bench, plan table and graph usable at 1366x768; stacked at 760 and 375 wide with no page scroll sideways; labels
    at least 10 px in the 680x425 preview; all 13 images load and none shows a person; no network, no em dashes.

## Open questions
- [water-shapes-earth] Freeze and dissolve rates are made up (in the right order, labeled on screen). OK for a lab
  model, or look for measured rates to show beside them?
