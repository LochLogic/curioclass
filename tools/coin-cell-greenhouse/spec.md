# Coin Cell Greenhouse

## One idea
A made-up board called Sprout-1 waters a seedling tray on one coin battery, and its limits are hard: reading the soil sensor takes 2 seconds, the log has room for 384 entries, and waiting awake burns 600 times the current of sleeping, so the starter program (read, log, water, wait a minute, repeat) fills its memory and resets in 7 hours; you reshape the same program, by turning repeated watering code into one `water(seconds)` procedure, reading the sensor once, logging averages and sleeping instead of waiting, until a 30-day run of the greenhouse's weather ends with the plants never dry and most of the battery left.

## Not like
- sorting-showdown (9-12 CS): fixed algorithms raced on comparisons. Here you edit one program and the cost is charge and memory on a device with limits, not speed.
- api-playground (9-12 CS): modules that call a town's APIs. Here procedures are a refactor of your own repeated code, and the payoff is changing one place.
- network-architect (9-12 CS): a system built from parts and tested. Here the hardware is fixed and only the algorithm changes.
- simulation-studio (9-12, data desk): simulating chance. This simulation is deterministic: the same program and weather always give the same 30 days.
- computer-builder and loop-garden (3-5 CS): parts of a computer, and loops that water a garden. Here the loop already works; the problem is that it works too hard for its battery and memory.
- emerging-tech-pitch, cloud-through-time (this group): energy as a social cost. Here energy is the budget your code spends, counted in milliamp-hours.

## Who and how
- Grades 9 to 12, computer science. Module: Device Limits and Optimization (Systems and Security), "Capabilities and limits of a simulated device; optimize its algorithm with procedures". Topic line: "device limits, procedures and optimizing code".
- Driver: students on laptops, alone or in pairs. 30 to 45 minutes.
- Standards (module codes, CSTA 2026): HS-SYS-HW-30 (capabilities and limits of a device: the Device sheet, battery, memory, sensor time, sleep), HS-ALG-PS-02 (optimize an algorithm using procedures: Program, Run, Compare). CSTA 2017 crosswalk: 3A-CS-01 (abstractions hide implementation details of computing systems embedded in everyday objects), 3A-AP-17 (decompose problems using procedures), 3B-AP-11 (evaluate algorithms in terms of efficiency).
- tool.json: driver "students", minutes "30-45", modes ["Device", "Program", "Run", "Compare"], grades_label "Grades 9-12". Kit starter, `kit:theme-912`.

## Screens and modes
Header (kit): "Coin Cell Greenhouse", small line "Make one battery last a month". Modes: **Device** (first), **Program**, **Run**, **Compare**. Motion, Sound, Read.

Panel in every mode: the **goal card** ("30 days. No memory reset. Soil never below 25%.") and the three live gauges from the last run: **Battery** (mAh used of 220, with "days it would last"), **Memory** (log entries used of 384), **Driest soil** (lowest moisture in percent). Before any run they read "No run yet".

### Device
Focus: the painted setup, center stage. Stage: the setup, painted (art `cg-greenhouse` behind, with `cg-parts` cutouts placed on it): a seedling tray in a small greenhouse, a soil probe, a valve on a drip line from a rain barrel, and the Sprout-1 board with a coin cell. The board's tiny LCD is a blank painted screen with its text in code (lime on dark). The drip line between barrel, valve and tray is a code-drawn tube, so it can show water flowing when the valve is open. Tapping each part opens its **spec card** (Content): what it does, how long it takes, what current it draws. A table under the drawing, **Where the charge goes**, lists every action with time, current and charge per use (Content), so the arithmetic is on screen before any code runs. **Start programming** opens Program.

### Program
Focus: the program stack, center stage and widest. Stage left: the **block palette** (Content). Stage main: the **program**, a vertical stack of blocks that reads like code, with line numbers; it starts as the starter program. Blocks are added by dragging from the palette or by selecting a line and tapping a palette block (inserts after it). Every block can be moved (drag or Alt+Up/Down), deleted, and edited in place (numbers by a small stepper or typing). Two quick toggles on blocks: `wait` and `sleep` switch with one tap (same seconds), and an inline `readSoil()` can be switched to the variable `m` once `m = readSoil()` exists above it.
**Make procedure**: select two or more neighboring lines, tap Make procedure, name it from a short list (`water`, `checkSoil`, `logIt`, `rest`) and choose which number becomes the input (for example the 600 in `wait(600)` becomes `seconds`). The lines move into a **procedure card** above the forever loop, and every other place with the same lines (same blocks, any number) is offered for replacement: "Also replace lines 8 to 10 with water(300)?" Editing inside the procedure card changes every call.
Under the program: **Step one loop** (a trace table: line, time spent, current, charge, moisture, log count, for one pass through the loop) and **Run 30 days** (goes to Run). **Undo** and **Reset to starter**.

### Run
Focus: the moisture chart, the largest thing on the stage. Stage top: the **30-day strip**, one tile per day with the weather (cool, warm, hot as a painted icon, art `cg-weather`, and a word); the run plays across it in about 10 seconds (instant with Motion off). Under it the **moisture chart**: soil moisture over 30 days as a line, the healthy band 30 to 80 percent shaded, the stress line at 25 percent, and a small mark at every watering. Beside it the **charge breakdown**: a bar split into awake waiting, sleep, sensor, valve and logging, in mAh, with each share. Then the **result line**, one of:
- "Memory full after 7.0 hours: the board reset and stopped watering."
- "Battery empty on day 2.5."
- "Made it 30 days: 27.7 mAh used, about 238 days of battery at this rate. Driest soil 34.6%."
If the board stops, the chart greys the rest of the month and the tray picture (small, at the right) swaps from the healthy tray (`cg-tray-healthy`) to the wilted one (`cg-tray-wilted`) for the days after; it shows healthy again whenever the soil is above 25 percent. **Save run** stores the program and its numbers for Compare (up to 8 runs, in the page; Save on this device keeps them).

### Compare
Focus: the runs table. Stage: a table of saved runs (name it from a short list: Starter, Try 1 to Try 7), columns: how it ended, days lasted, mAh per day, log entries used, driest soil, stress hours, waterings. A bar chart of mAh per day (log scale switch) and a **What changed** column that lists the edits between two runs picked with checkboxes ("wait(60) became sleep(600); readSoil() 3 times became once"). **Copy table** copies plain text.

## Content
Device specs (made-up board, real-world sized numbers):
- Coin cell: 220 mAh usable (a CR2032 is rated about 225 to 235 mAh; the board stops a little before the cell is fully drained).
- Board awake (running code or waiting): 3.0 mA. Board asleep: 0.005 mA (5 microamps). Waking is instant.
- `readSoil()`: 2 seconds at 10 mA (board and probe together); returns moisture 0 to 100 percent.
- `openValve()` and `closeValve()`: a latching valve, 0.1 second pulse at 153 mA each; it stays where it was put without power.
- `log(value)`: 0.01 second at 3 mA; stores one 4-byte entry. Memory: 2,048 bytes; the program takes 512; 1,536 bytes left = 384 entries. Entry 385: "Memory full: board resets", and the run ends there.
- `logAverage(value, N)`: adds value to a running total; every N calls stores one entry (the average) and starts over. Costs the same as log only when it stores.
- `wait(s)`: stays awake s seconds (3 mA). `sleep(s)`: sleeps s seconds (0.005 mA).

Where the charge goes (table on Device): one readSoil 0.0056 mAh; one valve pulse 0.0043 mAh; one log 0.00001 mAh; one minute awake 0.05 mAh; one minute asleep 0.00008 mAh; one day awake 72 mAh; one day asleep 0.12 mAh.

Greenhouse model: soil starts at 60 percent. With the valve closed it dries by a rate set by the day's weather: cool 0.6, warm 1.2, hot 2.4 percent per hour. With the valve open it rises 0.1 percent per second, up to 100. The month's weather (30 days): C C W W W H H W W C C W W H H H W W C C W W W H H H H W W C (7 cool, 14 warm, 9 hot). Stress hours: time spent below 25 percent. Healthy band shown: 30 to 80 percent. The model is deterministic: same program, same 30 days.

Starter program:
```
forever:
  log(readSoil())
  if readSoil() < 25:
    openValve()
    wait(600)
    closeValve()
  else if readSoil() < 35:
    openValve()
    wait(300)
    closeValve()
  wait(60)
```
The two watering parts are the same three lines with a different number: the natural first procedure, `water(seconds)`.

Block palette: `m = readSoil()`; `readSoil()` (inline, inside log or an if); `if ... < N:`, `else if ... < N:`, `else:`; `openValve()`; `closeValve()`; `wait(s)`; `sleep(s)`; `log(value)`; `logAverage(value, N)`; procedure call (once a procedure exists). Thresholds and seconds are editable numbers (thresholds 0 to 100, seconds 1 to 86,400, N 1 to 1,000).

Checked runs (same model as the build, to verify):
| Program | How it ends | mAh per day | Logs | Driest |
|---|---|---|---|---|
| Starter | memory full at 7.04 h | 87.3 | 385 | 55.8% |
| logAverage(m, 60), still wait, readSoil 3 times | battery empty day 2.52 | 87.3 | 54 | 35.0% |
| + sleep(60) at loop end, watering still waits | battery empty day 9.95 | 22.1 | 216 | 35.0% |
| + read once into m | memory full day 16.64 | 8.11 | 385 | 35.0% |
| logAverage 144 instead of 60 | battery empty day 27.08 | 8.12 | 261 | 35.0% |
| + water(seconds) sleeps instead of waits | battery empty day 28.07 | 7.84 | 270 | 35.0% |
| loop sleep(600), logAverage 144, all sleeping | 30 days, 27.71 mAh used | 0.92 | 29 | 34.6% |
| loop sleep(600), logAverage 6 | memory full day 16.15 | 0.92 | 385 | 34.6% |
| loop sleep(600), logAverage 12 | 30 days, 27.71 mAh used | 0.92 | 357 | 34.6% |
| loop sleep(3600), logAverage 24 | 30 days, 7.87 mAh used | 0.26 | 29 | 32.7% |
| loop sleep(10800), log every check | 30 days, 5.22 mAh used | 0.17 | 240 | 27.9% |
| loop sleep(21600), log every check | 30 days, 4.52 mAh, 5.3 stress hours | 0.15 | 120 | 20.9% |
The last row is the trap the panel calls out: sleeping too long saves charge but lets the hot days dry the tray. Waterings in the 30-day runs: 30 to 34.

## Interactions in detail
- The run plays across the strip in about 10 s, under the 30 s limit. Every control stays live while it plays: tapping a day tile jumps the play to that day at once, Run 30 days restarts from day 1, a mode switch stops the play and keeps the finished result, and Save run is enabled from the start (the result is computed before the play begins; the play only reveals it).
- Running: Run 30 days is always available; a program with an empty forever loop shows "The loop does nothing: add at least one block." A program that never sleeps or waits runs as fast as its blocks take (the sim still advances by each block's time).
- The run ends at the first moment charge passes 220 mAh, a 385th log entry is stored, or the clock reaches exactly 30 days (even in the middle of a sleep); the result line gives the hour or day to two decimals.
- Step one loop: the trace table walks the program once from the current state of day 1, hour 0, listing every line executed in order (procedure calls expand, indented). The total charge row is the number a student can multiply by loops per day.
- The panel calls out (once per run, as a short note under the result line, not a score): the largest bar in the charge breakdown (on the starter: "Awake waiting is 75% of the charge"), memory filling ("Logs fill at about 55 per hour"), and stress (on the sleep(21600) run: "Soil dropped below 25% on day 6, a hot day").
- Make procedure: lines must be neighbors and inside the same block; it refuses with "Pick lines next to each other" otherwise. Replacing other copies is offered, never forced. Procedures cost no charge (calling is free on this board).
- Save on this device: saved runs and the current program stay in localStorage; **Clear saved** removes them. Nothing about the student is stored.
- Keyboard: palette, program lines (Up/Down, Enter to edit, Alt+Up/Down to move, Delete), then Step, Run. Visible focus. Screen readers hear each line as text ("Line 4, wait 600 seconds").
- Sizes: at 1366x768 and 1280x720 the palette, a 14-line program and the panel fit without page scroll (the program scrolls inside itself past 14 lines); at 760 wide the palette becomes a drawer; at 680x425 Program shows the program with an Add block button. Code text at least 14 px, monospace.

## Look
- Accent `--brand #c4ef6a` (sprout lime: the board's LCD text, Run, gauges' fill, procedure card border) with `--brand-ink #16210a`, on `kit:theme-912`. The board's LCD and the program editor sit on `#0a120c`.
- Moisture chart: line in the theme ink, healthy band in a soft green tint, stress line dashed; weather icons carry words too. Charge breakdown parts have patterns as well as tints.
- Contrast (computed): brand on `--panel` 13.11:1, on `--sec-bg` 12.42:1, on the editor `#0a120c` 14.39:1; brand-ink on brand 12.66:1; theme ink on the editor 16.15:1. All pass AA.
- Neighbors: api-playground lemon #ffd75e (lime here is greener), simulation-studio orange, network-architect sky blue, sorting-showdown violet, capture-the-flag and ai-evaluator pinks; group siblings coral, cyan, orchid and light pages. The theme's mint `--ok` is kept for "Made it 30 days" with a check icon, never as the only signal.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: bright, tidy painted illustration of a hobby workbench project, soft daylight. Charts, the program editor, gauges, the charge bar, the drip line and the LCD text stay code.
- cg-greenhouse: "A small backyard greenhouse of clear panels with a wooden potting bench inside, an empty spot on the bench and a green rain barrel just outside, soft daylight, painted illustration"; 16:10; cutout no; people no; the Device stage backdrop.
- cg-parts (kit of 4, one cutout each, one prompt line): "A single {small green circuit board with a silver coin battery in a holder and a tiny blank dark screen and smooth plain chips | thin metal two-pronged soil moisture probe with a short cable | small black plastic water valve with two tube fittings and a short cable | green plastic rain barrel with a brass tap}, painted illustration, plain white background"; 1:1; cutout yes; people no; board, probe, valve, barrel. Sizing: each placed on the greenhouse at fixed spots (board on the bench at left, probe in the tray, valve on the tube between barrel and tray, barrel outside the right wall), tappable for its spec card; the board also shows at 96 px in the Program header.
- cg-tray-healthy, cg-tray-wilted: "A black plastic seedling tray of 24 cells with {bright green upright seedlings in dark moist soil | drooping yellowing wilted seedlings in pale cracked dry soil}, seen from slightly above, painted illustration, plain white background"; 4:3; cutout yes; people no; on the bench in Device (healthy) and at the right of the Run chart (swaps as described).
- cg-weather (kit of 3, one cutout each, one prompt line): "A single painted garden thermometer with a {low blue column and a frosty tip | middle yellow column | high red column and wavy heat lines around it}, centered, plain white background"; 1:1; cutout yes; people no; cool, warm, hot on the 30-day strip (28 px, with the word) and in the Device weather note.
The preview.svg is code (the moisture chart with the healthy band and the result line).

## Voice
Bank voice `friendly-dad` (Achird), style "Say in a relaxed, friendly way, like a kind dad helping with homework": a parent who built the greenhouse kit in the garage and handed you the board. Not used by a 9-12 CS tool or a group sibling (its users are grade 3-8 and 3-5 tools). `Curio.voice`, `scope: () => state.mode`. Light narration; Read speaks the hint. Program lines and numbers are on screen only.
1. wDevice (how; Device entered; stale when Start programming is pressed): "Tap each part to see what it costs. Then press Start programming and run the starter."
2. memFull (event; first run that ends in memory full; stale when a new run starts): "Seven hours and the memory's full. Open Program and look at what it logs every minute."
3. battery (event; first run where the battery runs out; stale when a new run starts): "Battery's gone. Check the breakdown for the biggest bar, then open Program and change that part."
4. makeProc (how; first time two neighboring lines are selected in Program; stale when Make procedure is pressed or the selection clears): "Same lines in two places? Press Make procedure."
5. made30 (event; first run that makes it 30 days with no stress hours; stale when a new run starts): "Thirty days, and the seedlings never went dry. Press Save run, then open Compare to see how far you came."
6. tooDry (event; every 30-day run with stress hours; stale when a new run starts): "It lasted, but the soil got too dry. Open Program and make the loop sleep a little less."
The memFull line's "seven hours" only plays on a memory-full run shorter than 8 hours; a later memory-full run plays it as: "The memory's full. Open Program and look at how often it logs." 

## Family engine
None. The simulator, the editor and the two charts are this tool's own (`tools/coin-cell-greenhouse/sim.js` in the page).

## Sources
- CSTA 2026 PK-12 Computer Science Standards: https://csteachers.org/2026-csta-pk-12-computer-science-standards/ ; CSTA 2017: https://csteachers.org/k12standards/
- Coin cell capacity, CR2032 about 225 to 235 mAh: Energizer CR2032 product datasheet, https://data.energizer.com/pdfs/cr2032.pdf ; Panasonic CR2032 datasheet, https://na.industrial.panasonic.com/products/batteries/primary-batteries/lineup/lithium-coin-batteries
- Microcontroller sleep currents in the microamp range and awake currents in milliamps: Microchip ATmega328P datasheet, power-down and active supply current, https://www.microchip.com/en-us/product/ATmega328P
- The Sprout-1 board, its latching valve pulse, its exact numbers, the drying rates and the weather month are made up so the math is clean; brands are not shown on screen.
- Checks run (Python simulator written from the Content rules, 2026-10-29; the run stops at exactly 30 days, mid-block): the charge table (readSoil 0.0056, valve pulse 0.0043, log 0.00001, minute awake 0.05, minute asleep 0.00008, day awake 72, day asleep 0.12 mAh; awake to asleep 600 to 1); the starter's loop is 66.01 s and 0.0667 mAh, 75.0% of it awake waiting, logs at 54.5 per hour; 384 entries = 1,536 / 4 bytes. All 12 checked runs reproduced. Fixed: the starter's mAh per day is 87.3 (25.61 mAh over 7.04 h), not 87.5; the sleep(10800) and sleep(21600) runs use 5.22 and 4.52 mAh (the draft let the last sleep run past day 30, adding about 0.02); the stress note's example now matches the sleep(21600) run, which first drops below 25% on day 6 (hot), not day 14. 220 / 27.71 x 30 = 238 days. Waterings in the 30-day runs: 30 to 34.

## Done when
1. Device lists every action's time, current and charge; one day awake reads 72 mAh, one day asleep 0.12 mAh.
2. Run 30 days on the starter ends "Memory full after 7.04 hours" with 385 entries and 87.3 mAh per day.
3. Every row of the checked runs table reproduces (ending, mAh per day to two places, logs, driest soil).
4. Make procedure on lines 4 to 6 offers to replace lines 8 to 10 too, and the program then shows two `water(...)` calls with 600 and 300.
5. Switching `wait` to `sleep` inside the water procedure changes both calls at once.
6. Step one loop on the starter (soil 60%, no watering) lists every executed line with its time and charge: 66.01 seconds and 0.0667 mAh per pass, 6 of those seconds reading the sensor three times.
7. Compare shows saved runs and the edits between any two.
8. Fits at 1366x768 with a 14-line program; Program works by keyboard alone.
9. Focus: the program stack is the widest column in Program and the moisture chart the largest thing in Run, at 1366x768 and 680x425.
10. Taps while a run plays: tapping a day tile jumps there at once; Run 30 days restarts; Save run works mid-play and saves the full result.
11. Art: the greenhouse, four part cutouts, both trays and three weather icons load; each part opens its spec card; the tray wilts after a failed run.

## Open questions
- [coin-cell-greenhouse] The board and its numbers are made up but sized like real parts. OK, or should it name a real chip's numbers in Sources only?
- [coin-cell-greenhouse] A blocks editor that reads like code, not typed code: right for 9-12, or add a typed text view as a second way in?
