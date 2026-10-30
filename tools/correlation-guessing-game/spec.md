# Correlation Guessing Game

## One idea
Guess r by eye in a few seconds, round after round, until your eye is calibrated; then the trick plots arrive (a
curve, one wild point, two clusters), where r says "strong line" or "no relationship" and the residual plot that
flips in underneath shows the line was the wrong story.

## Not like
- data-detective (gr 8, data-desk): fits a line to real data and reads a two-way table. Here no fitting by hand and no real dataset: fast rounds of judging r, then residuals.
- which-model-wins (gr 9, same group): compares model families on real data. Here only the straight line, and the question is whether r can be trusted.
- data-desk-distributions (gr 12): one-variable shape, center and spread with guided prompts. Here two variables.
- factor-forge (gr 6, same format): an arcade of prime factors. Same arcade pacing, different look and skill.
- misleading-charts (6-8, CS): charts drawn to mislead. Here honest charts whose single number misleads.

## Who and how
- Grade 9, Algebra 1, Data in One and Two Variables. Students drive. 10 to 25 minutes (a run is about 4 minutes).
- Topic line: "correlation, residuals and lines of fit".
- Standards (module): S-ID.A (light: each plot carries a box plot on each axis), S-ID.B (B.6 scatter plots, fitted line, residuals), S-ID.C (C.7 slope and intercept in context, C.8 the correlation coefficient, C.9 correlation is not causation). See Open questions on S-ID.A.
- CCSS clusters: Cloud lab and Runs serve S-ID.C.8; trick rounds serve S-ID.B.6; Headline rounds serve S-ID.C.7 and C.9.
- tool.json: driver "students", minutes "10-25", modes ["Cloud lab", "Run"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "How straight is the cloud?" Modes `Cloud lab` (opens first), `Run`. Kit buttons.
Stage: a square scatter plot, center stage and the largest thing on it (no axis numbers in guessing rounds, so scale
can't give it away; equal x and y spread) with a thin box plot along the bottom and left edges. Under it a strip where
the residual plot appears. Panel: the guess slider and `Lock in` at the top, then readouts, then score.

### Cloud lab (explore)
Focus: the cloud on the plot and r beside it; every control changes the cloud at once.
A slider `Target r` (−1 to 1, step 0.01) regenerates a 40-point cloud with exactly that r. Buttons:
`New cloud` (same r, new points), `Add outlier` (then click the plot to place one point; r updates live and the
old r shows struck through beside it), `Bend it` (switches to a curved pattern), `Two groups`, `Show line`
(least-squares line and its equation), `Show residuals`. Points can be dragged; r, the line and the residuals update
every frame. Readouts: n, r (3 places), line y = mx + b.

### Run (arcade)
Focus: the round's plot; during the reveal, the plot and the residual strip under it.
A start card over the dimmed arcade (art: arcade-hall) with `Start run` and the toggle `Relaxed` (no sweep bar and no
speed bonus). Ten rounds. Each round: a plot appears; you set the `Your guess` slider (−1 to 1, step 0.01; arrow
keys 0.01, Page keys 0.1) and press `Lock in` (or Enter). A sweep bar along the top shows 10 seconds; it never ends
the round, it only sets the speed bonus. Then the reveal: the true r, your error, points, and the residual plot
slides in (300 ms, instant with Motion off). `Next round` (or Enter) moves on; it appears with the reveal.
- Rounds 1 to 5: plain clouds (generated).
- Rounds 6 to 9 are line-question rounds: three tricks (three of Curve, Outlier, Clusters, Fan, Exponential, chosen
  at random without repeats) and one honest plain cloud with |r| at least 0.6, in a shuffled order. In these rounds
  the plot also asks `Is a line a good model?` with `Yes` and `No`; `Lock in` is enabled once one is picked. The
  honest cloud's answer is Yes, so No is not always right.
- Round 10: a Headline round (Content): a made-up chart with axis names and units, and a headline over its picture
  (art: headline-*). Guess r and press `Lock in`; the reveal then asks `Does x cause y?` with `Yes` and `Not shown`,
  and after the pick the card names the lurking variable and reads the slope in context with units.
- End card over the dimmed arcade: total points, best run on this device (localStorage `curio-correlation-best`,
  try/catch), average error, and `Play again`, `Clear best`.

## Content
Plain cloud generator (seeded): n from 25 to 60; x standard normal; target r drawn from −0.95 to 0.95 (at least
one negative and one below 0.3 in absolute value per run). Construction for an exact sample r: standardize x to zx;
draw noise e, remove its mean and its projection on zx and standardize it to ze; y = r·zx + √(1 − r²)·ze. The sample
r of the plotted points then equals the target (to floating point).
Trick plots (generated with the seed; r computed from the plotted points):
- Curve: x evenly spaced from −5 to 5 (11 to 21 points), y = x² plus small noise. Example with no noise:
  x = −5..5, y = x², r = 0 exactly; residuals form a U. Line is not a good model.
- Outlier: nine points on y = x (x = 1..9) and one at (10, −10): r = −0.051, while the nine alone have r = 1.
- Clusters: two groups of 5 points. Fixed example: group A at x = 1, 2, 3, 4, 5 with y = 5, 4, 1, 2, 3 (r = −0.6);
  group B is group A shifted by (8, 8). Together r = 0.822, while each group alone has r = −0.6. Generated versions
  keep the shift and jitter the group.
- Fan: x uniform from 1 to 10, n = 30, y = 2x + noise with spread 0.9x; r is usually 0.5 to 0.85 (about 0.71 in the
  middle); residuals open like a fan.
- Exponential: x = 0..10, y = 2^(x/2): r = 0.909, residuals curve (positive, negative, positive).
Answers to `Is a line a good model?`: Curve, Clusters, Fan and Exponential: No. Outlier: No, not with that point (the
button `No` is right and the card shows r for the other nine). Honest cloud: Yes.
Headline rounds (made-up data, labeled "made-up data"; one is picked per run):
- "Beach town: sunburn cases vs. ice cream cones sold, 30 summer days. Headline: Ice cream causes sunburn!" x = cones
  sold that day (100 to 400), y = sunburn cases at the clinic (2 to 20). Lurking variable: sunny hot days. Slope read
  in context: "each extra 100 cones goes with about 5 more sunburn cases" (the numbers come from the plotted line).
  Art: headline-beach.
- "School: math quiz score vs. hours of sleep, 40 students." x = hours (5 to 10), y = score (50 to 100). Lurking: many
  things (study, health); the card says a correlation alone can't show cause; an experiment could. Slope read: "each
  extra hour of sleep goes with about N more points". Art: headline-desk.
- "Town: fire damage vs. number of firefighters at the fire, 25 fires." x = firefighters (4 to 40), y = damage in
  thousands of dollars (5 to 400). Lurking: the size of the fire. Slope read: "each extra firefighter goes with about
  N thousand dollars more damage". Art: headline-fire.
Each headline dataset is built with the exact-r construction at a target drawn from 0.75 to 0.85, then scaled to its
units. The answer to `Does x cause y?` is always Not shown.

## Interactions in detail
- r is Pearson's correlation of the plotted points, computed in double precision and shown to 3 places; the line is
  least squares; residual = y − (mx + b), plotted against x with a zero line.
- Points per round: 100 × max(0, 1 − 2|guess − r|), rounded; speed bonus 20 if locked in within 3 s, falling
  linearly to 0 at 10 s (round to whole points); line question right: 30; cause question right: 30. Streak: each
  time three rounds in a row are within 0.1 (rounds 3, 6, 9 of a streak) add 25. Relaxed: no speed bonus. Best
  possible run: 10 × 120 + 4 × 30 + 30 + 75 = 1425.
- The guess slider starts at 0 every round; keyboard focus lands on it with `focus({preventScroll: true})`.
- Cloud lab: a dragged point stays inside the plot; when all x are equal or all y are equal r shows "not defined"
  (no spread) and the line hides.
- The sweep bar and the reveal slide never block input: the slider, `Lock in`, `Next round` and mode switches act at
  once, and a tap during the reveal slide finishes it.
- Reset: Run's `Play again`; Cloud lab's `New cloud`. Seeds come from the time unless the URL has `?seed=n` (for
  testing).
- `window.__tool = {state, setMode, seed(n), points(), r(), guess(v), lock()}`.

## Look
Accent `--brand #e59cff` (orchid, arcade neon), `--brand-ink #22082b`. Plot `#0e1520` with a faint frame; points
`#e8edf3` (r 4, 6 on touch); the guess shown as a dashed ellipse in the accent tilted by the guess; the line
`--gr-1`; residual bars `#ffd166` above and `#7af0c8` below zero, also marked by direction from the zero line. The
arcade painting (art: arcade-hall) sits only behind the start and end cards, dimmed to 35%, never behind the plot.
Contrast (computed): brand on panel 8.68:1, on --sec-bg 8.23:1, on plot 9.18:1, brand-ink on brand 9.26:1. No
confetti; a best run gets one line of text.

## Art
Local FLUX (`scripts/localart.py`); no people. One style: painted illustration, warm and bright for the headline
cards, neon for the arcade.
- arcade-hall: "A dim retro arcade hall with rows of glowing game cabinets with dark blank screens, purple and pink
  neon light on a patterned carpet, painted illustration"; 16:9; cutout no; people no; behind the Run start card and
  the end card, dimmed.
- headline-beach: "A seaside boardwalk ice cream cart with a striped umbrella and a blank sign board, bright midday
  sun, sand and blue water behind, painted illustration"; 16:9; cutout no; people no; header of the beach headline
  card; the headline text is in code above it.
- headline-desk: "A tidy student desk by a window at dawn with a closed notebook, a pencil and a round alarm clock
  with a plain blank face, soft morning light, painted illustration"; 16:9; cutout no; people no; header of the
  school headline card.
- headline-fire: "A red fire engine parked at an empty curb at dusk, rolled hoses on wet pavement, gray smoke drifting
  from a brick building behind, warm streetlight, painted illustration"; 16:9; cutout no; people no; header of the
  town headline card.
The scatter plots, box plots, residual strip, guess ellipse, sweep bar and preview.svg are drawn in code (charts).

## Voice
Bank voice `lively-host` (game show energy, matches an arcade). Not used by math 9-12 neighbors, group siblings or
batch specs. `Curio.voice`, `scope: () => state.mode`. Cards and readouts are read on screen; Read speaks the hint.
- wLab (how; Cloud lab entered; stale after the first slider move or drag): "Slide Target r and watch the cloud. Then drag a point and see how much one point can move r."
- wRun (how; Run start card shown; stale on Start run): "Ten rounds. Press Start run. Turn on Relaxed first if you want no clock."
- guess (how; round 1 shown; stale on the first Lock in): "Drag the Your guess slider to your guess for r, then press Lock in."
- next (how; first reveal; stale on Next round): "Read the reveal, then press Next round."
- question (how; first line-question round; stale once Yes or No is pressed): "New question. Set your guess, tap Yes or No for a good line model, then press Lock in."
- close (event; error 0.05 or less; stale on Next round): "Right on it."
- trickReveal (event; a trick round revealed; stale on Next round): "Look at the residuals. A pattern there means the line missed something."
- honestReveal (event; the honest cloud revealed; stale on Next round): "No pattern in the residuals. This time the line tells the story."
- headline (how; Headline round shown; stale on Lock in): "Headline round. Guess r and press Lock in. Then decide if the chart shows cause."
- cause (how; cause question shown; stale once Yes or Not shown is pressed): "Does this chart show cause? Tap Yes or Not shown."
- done (event; run ends; stale on Play again): "Run complete. Check your average error."

## Family engine
none (not in data-desk; its charts are its own).

## Sources
- S-ID.A, S-ID.B, S-ID.C: Common Core State Standards for Mathematics, High School Statistics and Probability, Interpreting Categorical and Quantitative Data, https://www.thecorestandards.org/Math/Content/HSS/ID/
- Correlation coefficient, least-squares line and residual plots: OpenStax, Introductory Statistics 2e, 12.3 "The Regression Equation" and 12.4 "Testing the Significance of the Correlation Coefficient", https://openstax.org/books/introductory-statistics-2e/pages/12-3-the-regression-equation
- Correlation is not causation, lurking variables: OpenStax, Introductory Statistics 2e, chapter 12 "Linear Regression and Correlation", https://openstax.org/books/introductory-statistics-2e/pages/12-introduction
- Construction of samples with an exact correlation (residualize and rescale the noise): standard linear algebra; the r of every plotted dataset is recomputed from the points, never taken from the target.
- Checks run (Python with numpy, 2026-10-29): U-shape r = 0.000; outlier r = −0.051 (nine points alone r = 1);
  exponential r = 0.909; exact-r construction at targets −1, −0.95, 0, 0.3, 0.8, 0.95, 1 with n = 40 returns the
  target to 12 places. The first draft's Clusters claim (r = 0.952 with each group −0.6) had no points behind it;
  searching every 5-point integer group with r = −0.6 shifted by (8, 8) gives at most 0.822, so the fixed example and
  its value were replaced. Fan with spread 0.9x over 2,000 seeds: median r 0.71, 5% to 95% from 0.51 to 0.85. Scores:
  guess 0.5 on r 0.7 gives 60; error 0.05 gives 90; error 0.5 or more gives 0; speed bonus 20 at 3 s, 17 at 4 s,
  10 at 6.5 s, 0 at 10 s; best run 1425. The first draft asked the line question only on tricks, where the answer
  was always No; one honest cloud now joins rounds 6 to 9 so Yes is sometimes right. The draft's slope example
  ("each extra degree goes with 14 more cones") named an axis that no headline chart has; the reads now match the
  axes.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. For any plot (use `?seed=7`), the r shown equals Pearson r recomputed from `points()` to 3 places.
2. Cloud lab: Target r = 0.80 gives r = 0.800; `Add outlier` at a far corner changes r and shows the old value struck through.
3. Run: a guess of 0.5 on r = 0.7 scores 60 plus any speed bonus; Relaxed removes the bonus and the sweep bar.
4. The Outlier trick reads r = −0.051 for the fixed example, the residual plot shows one huge residual, and `No` scores the line-question points; the honest cloud scores them for `Yes`.
5. The Curve example (y = x², x = −5..5) shows r = 0.000 and a U in the residuals; the Clusters example shows r = 0.822.
6. The headline round asks the cause question after Lock in, names the lurking variable and reads the slope with the chart's own units; every headline chart is labeled made-up data.
7. Focus: at 1366x768 and 1000x625 the plot is the largest thing on the stage, with the guess slider and `Lock in` beside or under it.
8. Tap while it plays: during the sweep bar and the reveal slide, the slider, `Lock in` and `Next round` act at once.
9. Best run survives a reload; `Clear best` clears it.
10. Every size in STANDARDS.md keeps the plot, slider and Lock in visible without page scrolling; keyboard-only play works; no voice line names a disabled control; console clean, no network.

## Open questions
- The module lists S-ID.A (one-variable data: shape, center, spread). This tool only touches it through the box plots on each axis. data-desk-distributions (gr 12) owns one-variable work. Is that light touch enough, or should a one-variable round type be added here?
