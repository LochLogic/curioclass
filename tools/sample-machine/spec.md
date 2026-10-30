# Sample Machine

## One idea
A machine with a hopper of 100 tickets: set the sample size, pull the lever, and it draws a sample, computes one
statistic and drops it as a ball into the bin below. Pull it a thousand times and the bin fills into a sampling
distribution you can see being built, one ball at a time. Predict first, then watch: the mean's pile narrows by √n
and turns bell shaped even from a lopsided hopper, while the maximum's pile sits too low and won't come back.

## Not like
- poll-workshop (gr 11, sampling family): sampling methods and bias in a poll of a town. Here no method choice: simple random samples only, and the subject is the sampling distribution of different statistics.
- jellybean-jar (gr 7, sampling family): estimating from one sample of a jar. Here thousands of samples and the shape, center and spread of the statistic.
- courtroom-statistics (gr 12, same group): uses a null sampling distribution as given. Here it is built.
- data-desk-distributions (gr 12, same group): distributions of data. Here distributions of a statistic.
- design-the-study (gr 12, same group): random assignment in an experiment. Here random sampling from a population.

## Who and how
- Grade 12, Statistics, Math: statistics. Students drive, alone or in pairs; a teacher can project the Machine. 15 to 35 minutes.
- Topic line: "sampling distributions and the central limit theorem".
- Standards (module): S-IC.A; AP-STAT.U5.
- CCSS clusters: Machine serves S-IC.A.1 (a statistic from a random sample estimates a population parameter);
  Predict serves S-IC.A.2 (decide whether a model fits results from a simulation: does the pile match your prediction
  and the theory?).
- AP-STAT.U5 (Sampling Distributions): sampling distributions of a sample proportion and a sample mean, the central
  limit theorem, biased and unbiased estimators, the 10% condition and large counts. Differences of two statistics are
  not covered (see Open questions).
- tool.json: driver "students or teacher", minutes "15-35", modes ["Machine", "Predict"], grades_label "Grade 12".

## Screens and modes
Header: title, subtitle "One sample is a story. A thousand is a shape." Modes `Machine` (opens first), `Predict`. Kit
buttons.
Stage, on a blueprint background (code grid), built as one machine from top to bottom: the hopper (the population as
a ticket histogram on a code glass panel with μ and σ or p marked), the painted brass funnel under it (art:
hopper-funnel) narrowing into the tray (the current sample's tickets, art: ticket, laid out as a small dot plot with
its statistic marked), and the bin (the sampling distribution: one ball per sample, stacked as a dot plot that switches
to a histogram above 300 balls) standing on the painted base plate (art: bin-base). The painted lever (art: lever)
stands at the machine's right side and swings when a draw runs. Panel: controls and readouts.

### Machine
Focus: the bin, the largest strip (about half the stage height, the full stage width), with the newest ball in the
accent; the hopper and tray are slimmer strips above it.
- Hopper picker: four cards with painted icons (art: hopper-icons) `Texts per hour`, `Commute minutes`, `Digits`,
  `Yes or no`, and a fifth card `Draw your own` (a code mini histogram).
- Sample size n: stops 1, 2, 3, 5, 10, 15, 20, 30, 50, 100 (slider snaps to stops).
- `With replacement` or `Without replacement`.
- Statistic: `Mean`, `Median`, `Maximum`, `Variance (n - 1)`, `Variance (n)`, `Proportion` (only for Yes or no).
- Lever: `Draw 1` (animated, about 1 s: tickets fly to the tray, the ball drops), `Draw 100`, `Draw 1,000` (batched;
  instant with Motion off). `Empty the bin`. The painted lever swings on every draw.
- Readouts: number of samples; mean and SD of the balls; the parameter; theory where it exists (mean and SD of x̄ or p̂,
  with the finite population factor without replacement); skewness of the balls.
- Toggles: `Show theory` (normal curve with the theory mean and SD over the bin), `Show parameter` (a line in the bin
  at the parameter, so bias shows as a gap).
- Changing n, the hopper, the statistic or replacement empties the bin (with a one-line note), so a bin never mixes settings.

### Predict
Focus: the empty bin with the student's center marker and ± 1 SD bracket on it, then the 1,000 balls landing under
them; the bin keeps the Machine's size.
A run of 8 challenges. Each sets hopper, n, replacement and statistic, then asks for a prediction before any draws:
drag a center marker, drag a bracket for ± 1 SD of the balls, pick a shape (`Like the hopper`, `More symmetric`, `Bell
shaped`, `Skewed`). `Draw 1,000` is enabled once all three are set, and checks it (rules in Content). A result line per
item and a `Next challenge` button; a final count out of 24. Best count on this device (localStorage
`curio-sample-machine-best`, try/catch) with `Clear`.
Challenges: Texts mean n 5; Texts mean n 30; Texts maximum n 5; Texts variance (n) n 5; Commute mean n 10; Digits
maximum n 5; Yes or no proportion n 50 without replacement; Draw your own mean n 30 (the student's own hopper).

## Content
Hoppers (100 tickets each, made up but plausible, labeled "made-up population"):
- Texts per hour, for 100 students (value: count): 0: 22, 1: 18, 2: 14, 3: 11, 4: 9, 5: 7, 6: 5, 7: 4, 8: 3, 10: 2,
  12: 2, 15: 1, 20: 1, 30: 1. μ = 3.41, σ = 4.3706 (divisor N), σ² = 19.1019, median 2, skewness 3.137 (strong right skew).
- Commute minutes (two kinds of commute: walkers and bus riders): 5: 4, 8: 8, 10: 12, 12: 10, 15: 6, 25: 6, 28: 10,
  30: 16, 32: 14, 35: 10, 40: 4. μ = 22.82, σ = 10.7251, median 28, skewness -0.267, two peaks.
- Digits: 0 to 9, ten tickets each. μ = 4.5, σ = 2.8723.
- Yes or no: 30 Yes, 70 No. p = 0.3.
- Draw your own: 21 columns (values 0 to 20); drag heights; the engine's apportion() rounds the shape to exactly 100
  tickets (largest remainder).
Theory checks (all exact or from exact sums; shown in Why panels and used in Predict):
- Texts, mean, n = 5: SD of x̄ 1.9546 with replacement (σ/√5), 1.9147 without (× √(95/99)). n = 30: 0.798 with,
  0.671 without (× √(70/99)).
- Skewness of x̄ for Texts (with replacement) = 3.137/√n: n = 5 1.403, n = 30 0.573, n = 100 0.314. The pile gets
  more symmetric but slowly, which is why "n ≥ 30" is a rule of thumb, not a law.
- Texts, maximum, n = 5, with replacement: E[max] = 8.651 against a population maximum of 30: biased low.
- Digits, maximum, n = 5, with replacement: E[max] = 9 - (1⁵ + ... + 9⁵)/10⁵ = 7.79175.
- Texts, variance (n), n = 5, with replacement: mean of the balls 15.282 = σ² × 4/5: biased low; variance (n - 1)
  centers on 19.1019 with replacement (unbiased). Without replacement it centers on N/(N - 1) × σ² = 19.2948, and the
  Why panel says so.
- Yes or no, proportion, n = 50: SD of p̂ 0.0648 with replacement, 0.04606 without (× √(50/99)). Large counts:
  np = 15, n(1 - p) = 35. The 10% condition here means n ≤ 10; at n = 50 without replacement the theory line with the
  factor fits and the one without doesn't, which is the point of the condition.
Predict scoring (one point each for center, spread and shape; compared with the true mean and SD of the statistic,
exact or from 200,000 stored simulated samples):
- Center: within 10% of the hopper's range (max minus min) for the mean, median, maximum and proportion; within 10% of
  σ² for the two variances (they are in squared units). So guessing σ² = 19.10 for Variance (n) misses (true center
  15.28, allowed 1.91), and guessing 9 for the Digits maximum misses (true 7.79, allowed 0.9).
- Spread: the bracket's half width within 20% of the true SD of the statistic.
- Shape, accepted answers (true skewness of the statistic in brackets): Texts mean n 5 (1.41): More symmetric or
  Skewed. Texts mean n 30 (0.57): More symmetric or Bell shaped. Texts maximum n 5 (1.95): Skewed. Texts variance (n)
  n 5 (3.2): Skewed or Like the hopper. Commute mean n 10 (-0.08): More symmetric or Bell shaped. Digits maximum n 5
  (-1.27): Skewed. Yes or no proportion n 50 (0.01): Bell shaped. Draw your own mean n 30: Bell shaped when |g1|/√30 is
  under 0.5 (g1 the hopper's skewness), else Skewed; also More symmetric when the hopper's |g1| is 0.3 or more.
- True SDs of the statistic used for Spread: Texts mean n 5 1.9546, n 30 0.7980; Texts maximum n 5 6.40; Texts
  variance (n) n 5 27.7; Commute mean n 10 3.392 (σ/√10); Digits maximum n 5 1.390; Yes or no n 50 without
  replacement 0.04606; Draw your own from its own σ/√30.

## Interactions in detail
- Seeded draws (`?seed=n` for tests). With replacement: n independent r.int(100) picks. Without: partial Fisher-Yates
  (the engine's simple()).
- Statistics: mean; median (average of the middle two for even n); maximum; variance with n - 1 (undefined for n = 1,
  button disabled with the reason); variance with n; proportion of Yes.
- Readouts to 3 or 4 significant places; skewness of balls is the sample skewness g1.
- `Draw 1,000` runs in batches of 100 per frame so the bin fills visibly (instant with Motion off); never more than
  20,000 balls in a bin (older balls fade from the readout, not the chart).
- Taps while it plays: during a `Draw 1` animation, `Draw 100` or `Draw 1,000` lands that ball at once and starts the
  batch; during a batch, `Empty the bin`, any setting or a mode switch stops it on that frame; toggles (`Show theory`,
  `Show parameter`) change the bin at once without stopping the batch.
- Keyboard: Space pulls the lever (Draw 1), Shift+Space Draw 100; arrows move n; the center marker and bracket move with
  arrows; focus visible on every control.
- `window.__tool = {state, setMode, seed(n), hopper(k), setN(n), replace(b), stat(k), draw(k), bin(), theory()}`.

## Look
Blueprint stage `#0e2a4a` with a faint white grid, panels from kit/theme-912.css. The machine's painted brass parts
(funnel, lever, base plate) sit on the blueprint; the hopper, tray and bin panels are code glass (a 1 px `#a9c1e0`
edge over the blueprint). Tickets are the painted cream ticket (about `#f4ead2`) with dark numbers in code; text on the
stage `#e8f1ff`, muted `#a9c1e0`. Accent `--brand #ff6a1a` (safety orange: the current sample's statistic, the newest
ball, the lever's knob matches it), `--brand-ink #10161f`. The parameter line is white and dashed; the theory curve is
a dotted line, so color is never the only signal. Contrast (computed): brand on panel 6.04:1, on sections 5.72:1, on
the blueprint 5.06:1; brand-ink on brand 6.34:1; tickets on blueprint 12.11:1; stage text 12.74:1; stage muted 7.86:1.
No celebration: Predict ends with the count.

## Art
Local FLUX (`scripts/localart.py`); no people. One style: clean painted illustration of polished brass and dark green
enamel machine parts, even studio light.
- hopper-funnel: "A wide polished brass funnel with a riveted rim and dark green enamel bands, seen straight from the
  front, narrowing to a short round spout at the bottom center, clean painted illustration, plain white background";
  4:1; cutout yes; people no; spans the stage under the hopper histogram; tickets fly from its spout to the tray.
- ticket: "A single blank cream paper raffle ticket with a perforated edge on both short sides, smooth empty face,
  clean painted illustration, plain white background"; 16:9; cutout yes; people no; every ticket in the tray and in
  flight (numbers drawn in code on its blank face); the hopper histogram stays code.
- lever: "A brass machine lever arm with a round orange enamel knob on top, mounted on a riveted dark green pivot
  plate, seen from the side, clean painted illustration, plain white background"; 3:4; cutout yes; people no; the arm
  rotates about the pivot on every draw (one cutout, rotated in code; Motion off holds it still).
- bin-base: "A long riveted brass base plate with dark green enamel trim and four short round feet, seen straight from
  the front, clean painted illustration, plain white background"; 5:1; cutout yes; people no; under the bin strip,
  stretched only in width by the layout's bin width (the build keeps its height).
- hopper-icons (kit of four, one shared prompt, each "a single <piece> centered, clean painted illustration, plain
  white background"): a smartphone with a blank glowing screen; a yellow school bus beside a pair of sneakers; a short
  stack of ten blank wooden number tiles; a small wooden ballot box with a slot on top. 1:1; cutout yes; people no;
  sizing: each icon fills 80 percent of its hopper card's icon square; text labels in code.
Balls, histograms, dot plots, markers, the bracket, the theory curve and preview.svg are drawn in code (they are charts).

## Voice
Bank voice `playful-friend` (light, a little cheeky; the machine's operator). Not used by math 9-12 neighbors or group
siblings. `Curio.voice`, `scope: () => state.mode`. Readouts, Why panels and result lines are read on screen.
- wMachine (how, Machine welcome; stale on the first draw): "Pick a hopper and a sample size, then press Draw 1 to pull the lever. Watch where the ball lands."
- thousand (how, first Draw 1,000 finishes; stale on any setting change): "A thousand samples. That pile is the sampling distribution."
- narrower (event, n raised with Mean on the same hopper, second time; stale on hopper change): "Bigger samples, narrower pile. Check the SD readout."
- maxLow (event, Maximum with Show parameter on, first time; stale on statistic change): "See the gap? The maximum of a sample keeps landing below the real maximum."
- wPredict (how, Predict welcome; stale once all three parts are set): "Drag the center marker and the spread bracket onto the bin, then pick a shape."
- ready (how, first time all three parts are set; stale on Draw 1,000): "Now press Draw 1,000 to check your prediction."
- next (how, first result line; stale on Next challenge): "Read the result line, then press Next challenge."
- done (event, Predict run ends; stale on new run): "That's eight. Check which part you missed most."

## Family engine
sampling (`kit/sampling.js`, lifted from poll-workshop's block marked `/* SAMPLING ENGINE (family: sampling) */`; the
first tool to need it outside poll-workshop moves it into the kit and poll-workshop switches to the kit copy).
Kept as is: `rng(seed)` (mulberry32 with `.normal()` by Box-Muller and `.int(n)`), `town(cfg)`, `simple(r, from, to,
n, out)` (partial Fisher-Yates), `apportion(shares, n)` (largest remainder), `stratified`, `cluster`, `systematic`,
`weighted(r, N, weights, n)` (key method), `moe(p, n)` (196·√(q(1 - q)/n), q = 0.5 at p = 0 or 1).
Added for this tool (and jellybean-jar, gr 7):
```js
S.hopper(counts)              // {value: count} -> flat array of 100 values (or any N)
S.draw(r, N, n, replace)      // indices; replace -> n × r.int(N), else simple()
S.stat.mean / median / max / varN1 / varN / prop   // each takes an array of values
S.repeat(k, fn, {batch, onBatch})                  // k samples in batches, returns the array of statistics
S.theory(pop, n, replace)     // {mean, sd} of x̄ (and of p̂ for 0/1 values), with the finite population factor
```
Existing calls keep working; poll-workshop's numbers must not change when it moves to the kit copy.

## Sources
- S-IC.A: Common Core State Standards for Mathematics, Making Inferences and Justifying Conclusions, https://www.thecorestandards.org/Math/Content/HSS/IC/
- AP-STAT.U5: College Board, AP Statistics Course and Exam Description, https://apcentral.collegeboard.org/courses/ap-statistics
- Sampling distributions, the central limit theorem, finite population correction: OpenStax, Introductory Statistics 2e, chapter 7 "The Central Limit Theorem", https://openstax.org/books/introductory-statistics-2e/pages/7-introduction
- Biased and unbiased estimators, the 10% condition, large counts: OpenIntro Statistics 4e, 5.1 "Point estimates and sampling variability", https://www.openintro.org/book/os/
- Skewness of a mean shrinking as 1/√n: standard result (the third cumulant of a sum of n independent copies is n times the third cumulant).
- Hoppers are made up.
- Checks run (Python, numpy and scipy, 2026-10-29): hopper μ, σ, σ², median and skewness reproduced (Texts 3.41,
  4.3706, 19.1019, 2, 3.137; Commute 22.82, 10.7251, 28, -0.267; Digits 4.5, 2.8723). 200,000 simulated samples per
  challenge: Texts mean n 5 SD 1.957, skew 1.41; n 30 SD 0.797, skew 0.57; without replacement 1.914 and 0.671 (theory
  1.9147 and 0.6710); Texts maximum n 5 mean 8.651, SD 6.40, skew 1.95; variance (n) mean 15.31, SD 27.7, skew 3.2;
  variance (n - 1) 19.12 with and 19.36 without replacement (theory 19.10 and 19.29); Commute mean n 10 skew -0.08;
  Digits maximum mean 7.7905 (exact 7.79175), SD 1.390, skew -1.27; Yes or no n 50 without replacement SD 0.0460.
  The first draft scored every center against 10% of the hopper's range, which is in the wrong units for a variance;
  variances now use 10% of σ². The first draft named no stored shape answers; they are now listed from the skewness.
- Done when bands, 2,000 repeats of 1,000 draws: Texts mean n 30 ball SD within 0.07 in 99.95% (with) and 100%
  (without); variance (n) within 2.5 in 99.5%, variance (n - 1) within 3.2 in 99.8%; Digits maximum within 0.1 only
  98.2% (SD of the mean 0.044), so the band is now 0.15; Yes or no SD within 0.006 in 100%.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Texts hopper readouts: μ 3.41, σ 4.371, median 2.
2. Texts, mean, n 30, 1,000 draws with `?seed=3`: ball SD within 0.07 of 0.798 with replacement and of 0.671 without.
3. Texts, variance (n), n 5, 1,000 draws: ball mean within 2.5 of 15.28 (its run-to-run SD is about 0.86); variance (n - 1) within 3.2 of 19.10 (with replacement). The exact centers show in the Why line.
4. Digits, maximum, n 5: ball mean within 0.15 of 7.79; Texts maximum shows the gap to 30 with Show parameter.
5. Yes or no at n 50 without replacement: theory SD 0.04606 shown and the ball SD within 0.006 of it.
6. Predict: on Texts variance (n) n 5 a center at 19.1 scores no point and 15.3 scores one; Draw 1,000 stays disabled
   until the center, bracket and shape are all set; the run ends at a count out of 24.
7. Changing any setting empties the bin with a note; Draw your own always holds exactly 100 tickets.
8. Focus: at 1366x768 and 1000x625 the bin is the largest strip on the stage in both modes, and the funnel, tray and
   lever line up with it at every size.
9. Tap while it plays: during Draw 1,000, toggling Show theory redraws the curve at once and the batch keeps going;
   pressing Empty the bin stops it on that frame; during a Draw 1 animation, Draw 100 starts at once.
10. Every size in STANDARDS.md keeps the three strips and the Draw buttons visible without page scrolling; keyboard
    only works; no voice line names a disabled control; console clean, no network.

## Open questions
- [sample-machine] AP-STAT.U5 includes sampling distributions of a difference of two proportions or two means. This tool has one hopper at a time. Add a two-hopper mode, or leave differences to courtroom-statistics' cases?
