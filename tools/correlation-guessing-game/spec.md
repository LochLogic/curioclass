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
Stage: a square scatter plot (no axis numbers in guessing rounds, so scale can't give it away; equal x and y
spread) with a thin box plot along the bottom and left edges. Under it a strip where the residual plot appears.
Panel: the guess slider, readouts, score.

### Cloud lab (explore)
A slider `Target r` (−1 to 1, step 0.01) regenerates a 40-point cloud with exactly that r. Buttons:
`New cloud` (same r, new points), `Add outlier` (then click the plot to place one point; r updates live and the
old r shows struck through beside it), `Bend it` (switches to a curved pattern), `Two groups`, `Show line`
(least-squares line and its equation), `Show residuals`. Points can be dragged; r, the line and the residuals update
every frame. Readouts: n, r (3 places), line y = mx + b.

### Run (arcade)
Ten rounds. Each round: a plot appears; you set the `Your guess` slider (−1 to 1, step 0.01; arrow keys 0.01, Page
keys 0.1) and press `Lock in` (or Enter). A sweep bar along the top shows 10 seconds; it never ends the round,
it only sets the speed bonus. Then the reveal: the true r, your error, points, and the residual plot slides in
(instant with Motion off).
- Rounds 1 to 6: plain clouds (generated). Round types 7 to 9 are tricks (one each of Curve, Outlier, Clusters, Fan,
  Exponential, chosen at random without repeats). In trick rounds, before the reveal, also answer `Is a line a good
  model?` with `Yes` or `No`.
- Round 10: a Headline round (Content): a made-up chart with axis names and units, and a headline. After the r
  guess, answer `Does x cause y?` with `Yes` or `Not shown`, then the card names the lurking variable and reads the
  slope in context ("each extra degree goes with 14 more cones sold").
- End card: total points, best run on this device (localStorage `curio-correlation-best`, try/catch), average
  error, and `Play again`, `Clear best`. Toggle `Relaxed` (no sweep bar and no speed bonus).

## Content
Plain cloud generator (seeded): n from 25 to 60; x standard normal; target r drawn from −0.95 to 0.95 (at least
one negative and one below 0.3 in absolute value per run). Construction for an exact sample r: standardize x to zx;
draw noise e, remove its projection on zx and standardize it to ze; y = r·zx + √(1 − r²)·ze. The sample r of the
plotted points then equals the target (to floating point).
Trick plots (generated with the seed; r computed from the plotted points):
- Curve: x evenly spaced from −5 to 5 (11 to 21 points), y = x² plus small noise. Example with no noise:
  x = −5..5, y = x², r = 0 exactly; residuals form a U. Line is not a good model.
- Outlier: nine points on y = x (x = 1..9) and one at (10, −10): r = −0.051, while the nine alone have r = 1.
- Clusters: two groups of 5 points each, one shifted by (8, 8): r = 0.952 while each group alone has r = −0.6.
- Fan: y = 2x + noise whose spread grows with x; r about 0.7; residuals open like a fan.
- Exponential: x = 0..10, y = 2^(x/2): r = 0.909, residuals curve (positive, negative, positive).
For Clusters and Fan the answer to `Is a line a good model?` is No; for Outlier it is "No, not with that point"
(the button `No` is right and the card shows r for the other nine).
Headline rounds (made-up data, labeled "made-up data"):
- "Beach town: ice cream cones sold vs. sunburn cases, 30 summer days. Headline: Ice cream causes sunburn!"
  Lurking variable: sunny hot days. Slope read in context: cones per sunburn case.
- "School: hours of sleep vs. math quiz score, 40 students." Lurking: many things (study, health); the card says a
  correlation alone can't show cause; an experiment could.
- "Town: number of firefighters at a fire vs. damage in dollars, 25 fires." Lurking: the size of the fire.
Each headline dataset is generated with r between 0.75 and 0.85 and units on the axes.

## Interactions in detail
- r is Pearson's correlation of the plotted points, computed in double precision and shown to 3 places; the line is
  least squares; residual = y − (mx + b), plotted against x with a zero line.
- Points per round: 100 × max(0, 1 − 2|guess − r|), rounded; speed bonus up to 20 (20 if locked in within 3 s,
  falling linearly to 0 at 10 s); trick question right: 30; headline question right: 30. Streak: three rounds in a
  row within 0.1 add 25. Relaxed: no speed bonus.
- The guess slider starts at 0 every round; keyboard focus lands on it with `focus({preventScroll: true})`.
- Cloud lab: a dragged point stays inside the plot; r with fewer than 3 distinct x values shows "not defined"
  (all x equal means no spread), and the line hides.
- Reset: Run's `Play again`; Cloud lab's `New cloud`. Seeds come from the time unless the URL has `?seed=n` (for
  testing).
- `window.__tool = {state, setMode, seed(n), points(), r(), guess(v), lock()}`.

## Look
Accent `--brand #e59cff` (orchid, arcade neon), `--brand-ink #22082b`. Plot `#0e1520` with a faint frame; points
`#e8edf3` (r 4, 6 on touch); the guess shown as a dashed ellipse in the accent tilted by the guess; the line
`--gr-1`; residual bars `#ffd166` above and `#7af0c8` below zero, also marked by direction from the zero line.
Contrast (computed): brand on panel 8.68:1, on --sec-bg 8.23:1, brand-ink on brand 9.26:1. No confetti; a best run
gets one line of text.

## Art
none: drawn in code.

## Voice
Bank voice `lively-host` (game show energy, matches an arcade). Not used by math 9-12 neighbors or group siblings.
- wLab (how, Cloud lab welcome): "Slide Target r and watch the cloud. Then drag a point and see how much one point can move r."
- wRun (how, Run welcome): "Ten rounds. Set your guess with the slider, then press Lock in."
- trick (how, first trick round): "Trick round. Before the reveal, say whether a line is a good model."
- close (event, error 0.05 or less; stale on next round): "Right on it."
- trickReveal (event, trick round revealed; stale on next round): "Look at the residuals. A pattern there means the line missed something."
- headline (how, first headline round): "Guess r, then decide: does this chart show cause, or not?"
- done (event, run ends; stale on Play again): "Run complete. Check your average error."

## Family engine
none (not in data-desk; its charts are its own).

## Sources
- S-ID.A, S-ID.B, S-ID.C: Common Core State Standards for Mathematics, High School Statistics and Probability, Interpreting Categorical and Quantitative Data, https://www.thecorestandards.org/Math/Content/HSS/ID/
- Correlation coefficient, least-squares line and residual plots: OpenStax, Introductory Statistics 2e, 12.3 "The Regression Equation" and 12.4 "Testing the Significance of the Correlation Coefficient", https://openstax.org/books/introductory-statistics-2e/pages/12-3-the-regression-equation
- Correlation is not causation, lurking variables: OpenStax, Introductory Statistics 2e, chapter 12 "Linear Regression and Correlation", https://openstax.org/books/introductory-statistics-2e/pages/12-introduction
- Construction of samples with an exact correlation (residualize and rescale the noise): standard linear algebra; the r of every plotted dataset is recomputed from the points, never taken from the target.
- Fixed examples recomputed in Python (2026-10-27): U-shape r = 0; outlier r = −0.051 (nine points alone r = 1); clusters r = 0.952 (each group −0.6); exponential r = 0.909.

## Done when
1. For any plot (use `?seed=7`), the r shown equals Pearson r recomputed from `points()` to 3 places.
2. Cloud lab: Target r = 0.80 gives r = 0.800; `Add outlier` at a far corner changes r and shows the old value struck through.
3. Run: a guess of 0.5 on r = 0.7 scores 60 plus any speed bonus; Relaxed removes the bonus and the sweep bar.
4. The Outlier trick reads r = −0.051 for the fixed example, the residual plot shows one huge residual, and `No` scores the trick points.
5. The Curve example (y = x², x = −5..5) shows r = 0.000 and a U in the residuals.
6. The headline round asks the cause question and names the lurking variable; every headline chart is labeled made-up data.
7. Best run survives a reload; `Clear best` clears it.
8. Every size in STANDARDS.md keeps the plot, slider and Lock in visible without page scrolling; keyboard-only play works; console clean, no network.

## Open questions
- The module lists S-ID.A (one-variable data: shape, center, spread). This tool only touches it through the box plots on each axis. data-desk-distributions (gr 12) owns one-variable work. Is that light touch enough, or should a one-variable round type be added here?
