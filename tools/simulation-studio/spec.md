# Simulation Studio

## One idea
The real 1985 Old Faithful log says long eruptions are followed by short waits, until you find that one column is shifted by a row; cleaned, it says the opposite, and the simulated geyser you build from the clean numbers matches the real one's chart so well that only a second check shows what it misses (a short eruption is never followed by another short one), before both answer the ranger's question: what should the sign say?

## Not like
- which-model-wins (9, same family): fits curves to clean data and picks the best. Here the data starts wrong, the fix is a cleaning recipe, and the model is a simulation you run, not a curve.
- data-desk-distributions (12, same family): describes the shape of given data. Here the shape (two humps) is the target a simulation must reproduce. This tool claims the Old Faithful data set for the family.
- data-table-builder (4, same family and group): prevents messy data by designing columns. Here the mess is already in a real published file and has to be found and fixed.
- outbreak-model (9-12, built) and poll-workshop (9-12, built): a simulation with given rules. Here you write the model's rules and numbers from data, then test it against that data.
- ai-evaluator (9-12): tests a trained model's errors by slice. Here the model is a hand-built simulation and the evidence is a cleaned log.
- sorting-showdown (9-12): algorithm speed. Nothing here is timed.

## Who and how
- Grades 9 to 12, computer science. Module: Simulation and Data Science (Data and Analysis), "Simulate, clean and visualize multivariate data". Topic line: "cleaning real data and building a simulation from it".
- Driver: students on laptops, alone or in pairs. 30 to 45 minutes.
- Standards (CSTA 2026 ids from the module): HS-DAT-DC-21, HS-DAT-DC-23, HS-DAT-DI-25, HS-DAT-DI-26. 2017 crosswalk: 3A-DA-11 (create interactive data visualizations), 3A-DA-12 (create computational models that represent relationships in data), 3B-DA-05 (use data analysis tools to identify patterns in complex systems), 3B-DA-07 (evaluate the ability of models and simulations to test and support the refinement of hypotheses). Reference: Wickham, "Tidy Data", Journal of Statistical Software 59(10), 2014 (cleaning steps as a recipe).
- tool.json: driver "students", minutes "30-45", modes [] (one studio, no score), grades_label "Grades 9-12".

## Screens and modes
Kit frame with the 9-12 theme (`kit:theme-912`). Header: title "Simulation Studio", small line "Old Faithful, August 1985"; Motion, Sound, Read.

Under the header, the pipeline strip: four nodes joined by arrows, "Raw log", "Clean", "Model", "Answer". Each node shows a one-line status ("299 rows", "2 steps", "fitted", "90 percent on time"). Tapping a node opens its bench (stage) and its controls (panel). When anything upstream changes, the arrows after it pulse once and downstream status lines update (no pulse with Motion off). All four nodes are open from the start; nothing is locked.

### Raw log
Stage: the file as published, `table.inst` with 15 rows per page and "Previous" / "Next" / page number, columns "#", "duration (min)", "waiting (min)". A scatter of duration (x) against waiting (y) for the same row, with its line and r. Panel: "Data notes" section with the two real notes, shown as file cards:
- "Original files: waiting = the time until the next eruption."
- "Corrected in a later version of the package (MASS 7.3-30): waiting = the waiting time for this eruption, so the time since the eruption before."
- "Some night durations were written down as short, medium or long and coded as 2, 3 or 4 minutes."
Plus a "Ranger's rule" card: "Rangers predict the next eruption from the one that just ended: a longer eruption means a longer wait." The raw scatter says the reverse (r = -0.65), which is the hook.

### Clean
Stage: the recipe, shown as code lines in the readout font, one per step, with up and down buttons and a remove "x" on each; below it the result: the scatter and a histogram of waits, live. Panel: "Add a step" with three step buttons:
- "Pair each eruption with the wait after it" (code: `log.wait_after = log.waiting.shift(-1)`; the last row gets no wait and is dropped from charts).
- "Flag night codes" (code: `log.night = log.duration in [2, 3, 4]`; flagged rows keep their short or long class but leave the duration axis of every chart; they still count in wait charts and in the pairs table).
- "Drop night-coded rows" (code: `log = log.drop(log.duration in [2, 3, 4])`).
Readouts under the charts: rows used, r, line "wait = a + b times duration", and the class table: "After a short eruption (under 3 min): n, mean, spread" and "After a long one". When "Drop" comes before "Pair", a warning row: "26 pairs now join eruptions that were not next to each other." and those points get a ring.

### Model
Stage: the two histograms of waits, real (from the cleaned log) and simulated, overlaid in 5 minute bins (real as outlined bars, simulated as filled), with "Match: 89 percent" (the overlap). Below, the pairs table: "Short then short", "Short then long", "Long then short", "Long then long", real counts beside simulated counts. A strip of the first 40 simulated eruptions as tall (long) and short markers with their waits.
Panel, "Your geyser" section (the model's rules as sliders, each with a number box):
- "After a short eruption, chance the next is long" 0 to 1, step 0.01.
- "After a long eruption, chance the next is long" 0 to 1, step 0.01.
- "Wait after a short eruption" mean 30 to 120 and spread 1 to 20 (minutes).
- "Wait after a long eruption" mean 30 to 120 and spread 1 to 20.
- "Fill from my clean log" (sets all six from the current Clean result), "Run 299 eruptions" (big button), "New run" (a new seed), "Reset model".

### Answer
Stage: the sign, drawn as a park sign: "Next eruption: [time] give or take [w] minutes", with a clock and the last eruption's length. Below, two result bars: "On the real log: 269 of 298 on time" and "On a simulated summer: about 1,830 eruptions, 89 percent on time".
Panel, "Ranger's sign" section: "If the last eruption was under [3.0] minutes, next in [56] minutes; otherwise next in [81] minutes. Window: give or take [10]." Number boxes and a window slider 1 to 20. "Fill from my clean log" (the two class means, rounded). "Test the sign". A line: "On the real log, each sign is checked against when the next eruption really started."

## Content
Data: MASS `geyser` (Azzalini and Bowman 1990), 299 eruptions, continuous from 1 to 15 August 1985, columns waiting (whole minutes) and duration (minutes, decimals). Copy it in as JSON from the Rdatasets CSV (URL in Sources), with the date pulled in the credit comment. Values below were computed from that file on 2026-10-27.
Checked numbers:
| Setup | Rows | r | Line | After short | After long |
|---|---|---|---|---|---|
| Raw, same row | 299 | -0.645 | wait = 99.31 - 7.80 x duration | 83.2 (105) | 66.4 (194) |
| Pair only | 298 | 0.888 | | 55.6, spread 6.3 (104) | 81.2, spread 6.8 (194) |
| Pair, then flag night codes | 221 on the duration axis | 0.898 | wait = 34.88 + 10.63 x duration | 55.6 (104) | 81.2 (194) |
| Drop, then pair (wrong order) | 220 | 0.816 | | | |
Night codes: 78 rows (2.0 x 23, 3.0 x 2, 4.0 x 53). Short means under 3 minutes (the rangers' cut); the two 3.0 codes (medium) count as long.
Waits: 43 to 108 minutes, mean 72.3, spread 13.9. Histogram of the 298 waits after an eruption, 5 minute bins from 40: 1, 15, 38, 22, 16, 16, 26, 55, 49, 40, 16, 3, 0, 1.
Real pairs: Short then short 0, Short then long 104, Long then short 105, Long then long 89. So "after a short, chance long" = 1.00 and "after a long, chance long" = 89 / 194 = 0.46.
Simulation (exact, so runs reproduce): the tool carries its own mulberry32 (`a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296`), seed 1 for the first run, +1 for each "New run". The first eruption is long. For each eruption: draw its wait after with z = sqrt(-2 ln(1 - u1)) cos(2 pi u2), wait = round(mean + spread z) clamped to 30 to 130; then draw the next class with one more u. Match = the sum over bins of the smaller of the two shares.
Model results over seeds 1 to 200 (5th to 95th percentile):
| Model | Match | Short then short |
|---|---|---|
| Start: chance 0.50 and 0.50, waits 70 spread 10 both | 60 to 69 percent | 59 to 89 |
| Filled from clean log: 1.00, 0.46, 55.6 / 6.3, 81.2 / 6.8 | 85 to 93 percent | 0 |
| Same waits, no memory: 0.65 and 0.65 | 85 to 93 percent | 25 to 46 |
| Filled from raw log (no Pair step): 1.00, 0.46, 83.2 / 6.6, 66.4 / 13.2 | 78 to 86 percent | 0 |
Seed 1, filled from clean log: Match 89 percent, pairs 0, 100, 100, 98.
Sign test on the real log (sign checked against the true next start):
| Sign | Window 5 | Window 10 | Window 15 |
|---|---|---|---|
| 56 after short, 81 after long | 163 | 269 | 294 |
| 72 always (the mean) | 60 | 136 | 205 |
| 83 after short, 66 after long (from the raw log) | | 49 | |
Simulated summer (92 days, 1,830 eruptions, filled from clean log, 56 and 81, window 10): 87 to 90 percent on time over seeds 1 to 50.
Comparison line on the Answer bench: "The park says about 90 percent of its predictions land within 10 minutes. The park's worksheet today uses 68 minutes after a short eruption and 94 after a long one, longer than in 1985, so the 1985 sign would not work now."

## Interactions in detail
- Every change recomputes in under 150 ms; histograms tween over 300 ms (instant with Motion off).
- Recipe order is the order shown; moving a step re-runs the recipe. Adding a step twice is not allowed (its button disables). Removing every step returns to the raw view.
- The scatter shows flagged night points only while "Flag night codes" is absent; with it, they leave the scatter (they would sit on three vertical stripes at 2, 3 and 4). A toggle "Show night codes" draws them faint on the scatter for comparison.
- Model sliders change nothing until "Run 299 eruptions"; the stage greys with "Changed: run again" until then. "Fill from my clean log" fills from whatever the Clean bench currently produces (raw if the recipe is empty), and says which ("Filled from: raw log").
- Spread 0 is not allowed (minimum 1). Chances of 1.00 and 1.00 give all long eruptions; the pairs table then shows 0 short and the histogram one hump.
- Answer always tests against the true timeline: an eruption's real next start is the next row's start, whatever the recipe says. The sign's numbers can be typed (30 to 130); the window slider 1 to 20.
- Tapping a histogram bin or a table row highlights the matching rows on the Raw log bench.
- Keyboard: pipeline nodes are tabs (arrow keys), recipe steps reorder with Alt plus arrow keys. Visible focus.
- Sizes: the pipeline strip, the open bench's main chart and its main button visible without scrolling at 1280x720 and 1366x768; at 680x425 the pipeline collapses to four short labels and the panel is compact; at 760 wide and below the stage stacks above the panel. Chart labels at least 11 px in the preview.
- Nothing is saved.

## Look
- Accent `--brand #ff7f32` (hot spring orange, like the colored mats around Yellowstone's pools), `--brand-ink #1c0d02`, on the 9-12 theme.
- Real data in `#5aa9ff` (outlined bars, circles), simulated in `#ffd166` (filled bars, triangles); night codes `#a6b3c4` rings; wrong pairs a ring in the theme `--warn`. Park sign: wood brown `#3b2a1e` with cream `#f3ead8` lettering.
- Neighbors: ai-evaluator and capture-the-flag pinks, network-architect sky blue, the theme's default amber on built 9-12 tools. A redder orange keeps it apart; siblings in this group are chalk yellow, deep sky, fuchsia and navy.
- Contrast: brand on panel 6.87:1, brand on section 6.51:1, brand-ink on brand 7.52:1, real blue on chart background 7.46:1, simulated yellow on chart background 12.70:1, brand on chart background 7.27:1, cream on wood 11.44:1. All pass AA.

## Art
none: drawn in code (pipeline, tables, charts, the park sign, preview.svg: two overlaid two-humped histograms, blue outline and yellow fill, under the pipeline strip).

## Voice
Bank voice `gravel-ranger` (Algenib), "Say warmly with a gravelly voice, like an old park ranger telling stories": the ranger who needs the sign. Not used by a group sibling or a 9-12 CS neighbor (ai-evaluator wise-mentor, network-architect calm-professor, capture-the-flag wise-mentor); leaf-sorter-ai (5) uses it with a different look. Numbers stay on screen; Read speaks the hint.
1. how, welcome: "This is the real eruption log from August 1985. Something in it is backwards. Tap Clean when you think you know what."
2. how, first Raw log page turn: "Read the data notes. One of them changes what a column means."
3. how, first recipe step added: "Each step is a line of the recipe. Order matters. Try moving one."
4. event, the Pair step is added: "Now a long eruption comes before a long wait. That matches what rangers see."
5. event, Drop placed before Pair: "Careful. Dropping rows first joins eruptions that weren't next to each other."
6. how, first Model visit: "Set your geyser's rules, or fill them from your clean log. Then run it."
7. event, after a run with Match at least 85 percent and short then short above 0: "The humps match. Now check the pairs table." Stale on any model change.
8. event, after a run with short then short 0 and Match at least 85 percent: "That's a geyser that never follows a short one with a short one. Just like the real thing."
9. how, first Answer visit: "Write the sign. Then test it against what really happened."
10. event, after a sign test: "On time for [n] of 298 eruptions." (299 fixed lines, 0 to 298). Stale on any sign change.

## Family engine
data-desk (`kit/data-desk.js`, docs/families/data-desk.md). Uses `DataTable` for the raw log, the cleaned log and the simulated log; `renderTable` with paging; `Chart` type `scatter` with `fit('linear')` (r from the fit, signed), `histogram` with `bins` of 5 minutes and two tables overlaid, and `box` for waits by class on the Clean bench. Engine additions this tool needs (into the engine and the family doc in the same change): `renderTable(el, {page: 15})`; `histogram` accepting a second table as an overlay series with its own style; `fit` returning `r`. The recipe, pipeline, simulation, pairs table and sign stay in this tool.
Dataset claim for the family table: Old Faithful 1985 (MASS geyser); no other sibling may use it.

## Sources
- Data: Azzalini, A. and Bowman, A. W. (1990), "A look at some data on the Old Faithful geyser", Applied Statistics 39, 357-365; as distributed in R package MASS (Venables and Ripley, Modern Applied Statistics with S, 4th ed., Springer 2002), data set `geyser`, including the night codes note and the waiting-time correction in MASS 7.3-30. CSV and documentation: https://vincentarelbundock.github.io/Rdatasets/csv/MASS/geyser.csv and https://vincentarelbundock.github.io/Rdatasets/doc/MASS/geyser.html
- Rangers predict from the last eruption's length (under 3 minutes: next in 68 minutes; over 3 minutes: 94): National Park Service, "Predict Old Faithful" worksheet (YELL 003): https://www.nps.gov/common/uploads/teachers/lessonplans/YELL_003-PredictOldFaithful.pdf
- About 90 percent of predictions land within plus or minus 10 minutes; only one eruption ahead can be predicted: Old Faithful Visitor Education Center exhibit, "Prediction": https://home.nps.gov/features/yell/ofvec/exhibits/eruption/prediction/predict7.htm and predict8.htm
- A similar line from other ranger data (next = 33.8 + 10.7 x duration), used as a cross-check: Penn State STAT 415, "A Prediction Interval for a New Y": https://online.stat.psu.edu/stat415/
- Tidy data and cleaning as repeatable steps: Wickham, H. (2014), "Tidy Data", Journal of Statistical Software 59(10).
- All other numbers above were computed from the data file and the stated simulation.

## Done when
1. Raw log shows 299 rows over 20 pages and a scatter with r = -0.65.
2. Adding "Pair each eruption with the wait after it" turns r to 0.89 and the class means to 55.6 and 81.2; adding "Flag night codes" gives r = 0.90 on 221 points.
3. Putting "Drop night-coded rows" before the Pair step shows the 26 wrong pairs warning and r = 0.82; after it, r = 0.90.
4. Model with seed 1 filled from the clean log gives Match 89 percent and pairs 0, 100, 100, 98; setting both chances to 0.65 keeps Match at 85 percent or more but short then short above 0.
5. Answer with 56, 81, window 10 shows 269 of 298; 72 for both shows 136; the raw-log fill (83 and 66) shows 49.
6. The simulated summer result is between 87 and 90 percent for the clean fill.
7. Lines 2, 3, 6 and 9 are each spoken once in a run of five actions; line 10 after every test.
8. Pipeline, main chart and main button visible without scrolling at 1366x768 and 680x425; real and simulated series told apart by outline versus fill and by marker shape.

## Open questions
- The data-desk rule asks for public data such as government statistics. This log is a published research data set (Azzalini and Bowman 1990, measured at Yellowstone and distributed in the R package MASS). Its real flaws (the night codes and the corrected column meaning) are the point of the tool. Is that source acceptable?
- The log has 299 rows, over the family's "under about 200 rows on screen"; the table pages 15 rows at a time. Fine, or trim to the first 10 days (about 200 eruptions; the numbers above would be recomputed)?
- Old Faithful is a classic for data-desk-distributions (grade 12) too. This spec claims it for simulation-studio; say if you would rather keep it for distributions.
