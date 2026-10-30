# Medical Test Paradox

## One idea
Test a whole town for a rare, made-up condition, and the town sorts itself into four groups you can see (has it and
caught, has it and missed, well but flagged, well and cleared); then look only at the people who tested positive,
and most of them are well, because a small error rate on a huge healthy crowd makes more false alarms than a good
test finds true cases. Slide how common the condition is and watch that one fraction swing from 9% to 91%.

## Not like
- carnival-odds (gr 7 simulator, same family): long-run frequency of one chance game. Here two events at once (condition and test) and the question is which group you divide by.
- game-show-strategist (gr 12 simulator, same family): choices and expected value. Here no choice to make; the lesson is reading a conditional probability the right way round.
- correlation-guessing-game (gr 9 arcade): reading relationships in scatter plots. Here categories and counts, not measurements.
- poll-workshop (live, sampling): a sample estimates a population. Here the whole population is shown and nothing is estimated.

## Who and how
- Grade 10, Statistics and Probability, module Probability Rules. Students drive, own laptops or pairs; Town also
  works on a projector for a whole-class reveal. 15 to 40 minutes.
- Topic line: "conditional probability and two-way tables".
- Standards (module): S-CP.A (events as subsets; independence; conditional probability; two-way tables; everyday
  language), S-CP.B (conditional probability as a fraction of outcomes; the addition rule; (+) the multiplication
  rule; (+) counting).
- CCSS clusters: Town serves S-CP.A.1, A.3 and B.6; Table serves A.4, A.5 and B.7; Second test serves A.2 and A.3,
  and its tree shows B.8 (+); the coin-test case serves A.2. B.9 (+) is not taught here (Open questions).
- tool.json: driver "students", minutes "15-40", modes ["Town", "Table", "Second test", "Cases"], grades_label
  "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Medical Test Paradox", subtitle "A positive test, and what it really means."
Modes `Town` (opens first), `Table`, `Second test`, `Cases`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: stage left (the town as an icon grid), panel right (sliders, readouts). Under 1000 px wide the panel goes
under the stage, sliders first. Under 900 px tall the grid shrinks to fit, the painted band is hidden and the
readouts stay in view.
A note under the header on every mode: "Glimmer fever is made up. Real tests have their own numbers; ask a doctor
about yours."

### Town (simulator)
Focus: the icon grid of the town, the largest thing on screen, with the big readout directly under it. A short
painted band of the town (art: town-street, 4:1) runs across the top of the stage above the grid.
- Controls: `People` 1,000 / 10,000 / 100,000; `How common` (prevalence, log slider 0.1% to 50%); `Catches`
  (sensitivity, 50% to 100%); `Clears` (specificity, 50% to 99.9%). Each slider has a number box.
- `Test everyone` plays in three beats of about 1 s each (instant with Motion off): people with glimmer fever fill
  in; the test marks positives with a raspberry color and a plus badge; the grid sorts into four blocks with counts.
- Before the third beat it pauses: a `Predict` slider asks "Of the people who test positive, what share have it?"
  (0% to 100%) with `Lock in guess` (runs the third beat) and `Skip guess` (runs it without a guess).
- `Positives only` fades everyone who tested negative. The big readout: "Of 981 who tested positive, 90 have it:
  9.17%." Your prediction sits beside it.
- `On average` (default) shows expected counts, one decimal when not whole, labeled "on average". `Random run`
  draws each person with a seeded random number (seed shown, `New run`), so counts are whole and vary a little.
  `Run 100 towns` plots the running share of positives who have it against the on-average value (Converge chart),
  drawn over at most 5 s.
- Tap while it plays: a slider, a mode switch or any button during a beat, the sort or Run 100 towns acts at once: a
  beat jumps to its end state, a run is stopped (its partial chart stays, labeled "stopped") and the new numbers show
  straight away.
### Table
Focus: the two-way table, center stage and large, with the lit fraction in big type under it; the Which question?
sentences and the addition panel in the panel.
- The same numbers as a two-way table: rows Has it / Doesn't, columns Positive / Negative, with totals. Tap a row
  or a column to divide by it: the cells in it light and the fraction shows ("90 out of 100 = 90%: of people who
  have it, the share who test positive").
- `Which question?`: six everyday sentences to drag onto the fraction they ask about, such as "If I test positive,
  how likely is it I have it?" (90/981) and "If I have it, how likely is the test to catch it?" (90/100). Two of the
  six sound alike on purpose.
- Addition rule panel: P(has it or positive) = P(has it) + P(positive) − P(both) = 100/10,000 + 981/10,000 −
  90/10,000 = 991/10,000 = 0.0991, with the double-counted block flashing.
### Second test
Focus: the tree, center stage, with the double-positive share in big type under it. Two test strips (art:
test-strip, shown twice) mark the first and second rounds above the tree.
- Everyone who tested positive takes a second test with the same Catches and Clears, assumed independent of the
  first given the condition (stated on screen). A tree shows both rounds with counts on every branch, and a toggle
  `Counts` / `Chances` shows probabilities instead (multiplication rule along a branch). Readout: share of double positives who have it.
### Cases
Focus: the open case's question with its Predict slider, then the grid and readout it reveals, center stage. The
case picker is a row of seven case cards, each with its painting (Art) and title.
- Case cards that set the sliders and ask one question; drag `Predict` to your answer, then `Show answer` runs the
  town and reveals it (Content). The last card, the coin
  test, is a "test" that says positive half the time no matter what: P(has it | positive) equals P(has it), the
  meaning of independence.

## Content
Cases (made-up condition; counts recomputed in Python, expected values):
- C1 Screening the town: 10,000 people, 1%, catches 90%, clears 91%. Has it 100: TP 90, FN 10. Doesn't 9,900: FP
  891, TN 9,009. Positives 981; P(has it | positive) = 90/981 = 9.17%; P(well | negative) = 9,009/9,019 = 99.89%;
  P(has it or positive) = 0.0991. These are the numbers of a classic teaching example (Gigerenzer et al. 2007); the
  card says "Told as percentages, many doctors guessed far too high. Told as counts, like this town, most got it
  right."
- C2 A clinic where many are sick: 30%, same test. TP 2,700, FP 630, P(has it | positive) = 81.08%.
- C3 A better test, a rarer condition: 100,000 people, 0.1%, catches 99%, clears 99%. TP 99, FP 999, 9.02%.
- C4 Test twice: C1 then a second test on the 981. TP 81, FP 80.19 ("80.2 on average"), 50.25%.
- C5 Half the town: 50%, catches 90%, clears 91%. TP 4,500, FP 450, 90.91%.
- C6 A perfect test: catches 100%, clears 100% (shown as a what-if beyond the slider's 99.9%): 100%.
- C7 The coin test: catches 50%, clears 50%, 1%: P(has it | positive) = 1%, the same as before testing.
Glossary chips (tap for one line): sensitivity ("catches"), specificity ("clears"), prevalence ("how common"),
false positive, false negative.

## Interactions in detail
- Expected counts: has it = N × p; TP = has × sensitivity; FP = (N − has) × (1 − specificity). Shares to 2 decimals
  of a percent; counts to 1 decimal only when not whole. All values from unrounded numbers.
- Random run: `Rand(seed)` (mulberry32); each person draws once for the condition and once for the test. A run with
  no positives shows "0 out of 0: nobody tested positive, so there is nothing to divide." 100,000 people are drawn
  in batches so the page never stalls.
- 100,000 people: each square stands for 10 people, a part-filled square shows the remainder; the legend says so.
- Sliders: How common uses log steps (0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 30, 50 marked); the number box takes any value
  in range to 0.1%.
- Which question?: a wrong drop springs back with the fraction it actually asks about; no score.
- Keyboard: every slider and toggle is focusable; table rows and columns are buttons; the grid has a text summary
  ("90 have it and tested positive, 10 have it and tested negative..."). Color is never the only signal (filled vs
  outline for the condition, a plus badge for a positive test).
- Reset per mode; settings last for the page session; nothing is saved.
- `window.__tool = {state, setMode, set({N, p, se, sp}), testAll(), positivesOnly(), counts(), run(seed),
  table(), divideBy(rowOrCol), second(), caseCard(id)}`.

## Look
Accent `--brand #ff3d9a` (the raspberry line on a home test strip), `--brand-ink #10161f`. Stage `#0f141c`; people
icons: well and negative are slate outlines `#6b7a90`, has-it fills the body, positives are raspberry with a plus
badge. Tree and table highlights in the accent at 25%. The pastel paintings (town band, case cards) never sit behind the
grid, table or text; the band fades into the stage color at its lower edge.
Contrast (computed): brand on --panel 5.26:1, on --sec-bg 4.99:1, on the stage 5.62:1; brand-ink on brand 5.52:1;
slate icons on the stage 4.23:1 (graphics, need 3:1); ink on the stage 15.69:1. Redder and deeper than
identity-proof-race's #ff5cf0 and the pinks #ff8ab6 and #ff8fd0; bluer than ramp-and-roof's #ff4d6d.

## Art
Local FLUX (`scripts/localart.py`), all without people. One style: soft pastel painted illustration, morning light.
- town-street: "A quiet small-town main street at dawn, brick shops with plain blank awnings, a small clinic with a
  green cross lamp, trees and a water tower behind, soft pastel painted illustration"; 4:1; cutout no; people no;
  the band over the Town grid and the case cards for C1 and C5 (C5 adds a "half the town" label in code).
- test-strip: "A white plastic home test cassette lying flat with a small oval window showing one raspberry red
  line, plain blank label area, soft pastel painted illustration, plain white background"; 1:1; cutout yes; people
  no; the Second test round markers and the case cards for C4 (two copies) and C6.
- clinic-hall: "An empty bright clinic waiting room with rows of teal chairs, a reception desk with a plain blank
  sign, potted plants, soft pastel painted illustration"; 4:3; cutout no; people no; case card C2.
- lab-rack: "A rack of capped test tubes and a microscope on a clean lab bench by a window, soft pastel painted
  illustration"; 4:3; cutout no; people no; case card C3.
- coin-flip: "A single silver coin spinning on its edge on a wooden table, soft pastel painted illustration, plain
  white background"; 1:1; cutout yes; people no; case card C7 (the coin test).
The people icons are an icon array (a chart of counts), so they stay in code with the table, tree, Converge chart,
badges and preview.svg.

## Voice
Bank voice `curious-librarian` (Aoede), style "Say calmly and curiously, like a librarian helping you check a
surprising fact". Not used by math 9-12 neighbors, group siblings or the R02 batch. `Curio.voice`,
`scope: () => state.mode`. Readouts, notes and case texts are read on screen; Read speaks the hint.
- wTown (how, Town welcome; stale on Test everyone): "Set the sliders, then press Test everyone."
- predictHow (how, the first Predict pause; stale on Lock in guess or Skip guess): "Drag Predict to your guess, then press Lock in guess."
- positivesHow (how, the first time the sort finishes; stale on Positives only): "Press Positives only to look at just the people who tested positive."
- wTable (how, Table welcome; stale on the first row or column tap): "Tap a row or a column to divide by it. Then drag each question onto its fraction."
- wSecond (how, Second test welcome; stale on the Counts or Chances toggle): "Everyone who tested positive takes the test again. Follow the branches, or tap Chances to see probabilities."
- wCases (how, Cases welcome; stale on Show answer): "Tap a case card, drag Predict to your answer, then press Show answer."
- surprise (event, Positives only shows a share under 20% after a prediction 30 points higher; stale on slider change): "Most of these positives are false alarms. The healthy crowd is just so much bigger."
- close (event, a prediction within 5 points; stale on slider change): "Close. You read it the right way round."
- coin (event, the coin test case is revealed; stale on case change): "The test knows nothing, so a positive tells you nothing new."

## Family engine
probability (`kit/probability.js`, inlined after `kit:curio`). This spec holds the full description for the
family; carnival-odds (gr 7 simulator, 7.SP.C) and game-show-strategist (gr 12 simulator, not yet specced) reuse it.
- `Rand(seed)`: seeded mulberry32. `.next()` in [0, 1), `.int(a, b)`, `.pick(list)`, `.shuffle(list)`,
  `.bern(p)`; `seed` readable so a run can be repeated.
- `Frac`: exact fractions, shared with coordinate and balance (proposed as `Curio.Frac`), for theoretical
  probabilities ("1/6") and natural frequencies ("90 out of 981").
- `Trials(fn, n, {rand, batch: 500, onBatch})`: runs an experiment n times, one batch per animation frame (all at
  once with Motion off), returns a promise of the results; `stop()`.
- `Tally(categories)`: `.add(cat)`, `.count(cat)`, `.rel(cat)`, `.total`, `.reset()`.
- `Converge(svg, {expected, label, xMax, logX: true})`: the running relative frequency against a dashed expected
  line, `push(value)`.
- `Population(svg, {n, groups: [{id, count, fill, outline, badge}], perIcon: 1 | 10, arrange: 'mixed' | 'sorted',
  focus: [ids]})`: an icon grid with animated sort and fade; part-filled icons for remainders; text summary for
  screen readers.
- `TwoWay(container, {rows, cols, cells, totals: true, onDivide})`: a two-way table whose rows and columns are
  buttons; `divideBy(rowOrCol)` lights the cells and returns `{part, whole, frac}`.
- `Tree(svg, {branches, show: 'counts' | 'probs'})`: a probability tree with counts or probabilities on the
  branches and products at the leaves.
- Fixed by the engine: icon shapes, the filled-vs-outline and badge signals, number formats ("90 out of 981",
  "9.17%", "on average" for expected values), seeded repeatable runs, batch pacing.
- What each sibling feeds it: carnival-odds: Rand, Trials, Tally, Converge and Frac for the theory value; its
  spinners and dice are drawn in that tool. game-show-strategist: Rand, Trials, Tally, Converge, and Tree for the
  host's choices; expected value stays in that tool. This tool: Population, TwoWay, Tree, Rand and Converge for
  random towns, Frac.

## Sources
- S-CP text: Common Core State Standards for Mathematics, High School Statistics and Probability, Conditional Probability and the Rules of Probability, https://www.thecorestandards.org/Math/Content/HSS/CP/
- The 1%, 90%, 9% example and natural frequencies: Gigerenzer G, Gaissmaier W, Kurz-Milcke E, Schwartz LM, Woloshin S, "Helping Doctors and Patients Make Sense of Health Statistics", Psychological Science in the Public Interest 8(2):53-96, 2007, https://pubmed.ncbi.nlm.nih.gov/26161749/
- Doctors do better with natural frequencies: Association for Psychological Science, "Just a Numbers Game? Making Sense of Health Statistics", https://www.psychologicalscience.org/news/releases/just-a-numbers-game-making-sense-of-health-statistics.html
- Sensitivity, specificity and predictive values: Shreffler J, Huecker MR, "Diagnostic Testing Accuracy: Sensitivity, Specificity, Predictive Values and Likelihood Ratios", StatPearls (NCBI Bookshelf NBK557491), https://www.ncbi.nlm.nih.gov/books/NBK557491/
- Checks run (Python, 2026-10-29): C1 TP 90, FN 10, FP 891, TN 9,009, 90/981 = 9.17%, 9,009/9,019 = 99.89%,
  (100 + 981 − 90)/10,000 = 0.0991; C2 (10,000 people) TP 2,700, FP 630, 81.08%; C3 TP 99, FP 999, 9.02%; C4 TP 81,
  FP 80.19, 50.25%; C5 TP 4,500, FP 450, 90.91%; C6 100%; C7 TP 50, FP 4,950, 1.00%. Slider extremes: 0.1% with a
  coin-like test gives 0.10%; 50% with 100% and 99.9% gives 99.90%; no setting gives zero positives on average.
  Random runs (numpy, 300 runs of 100 towns of 10,000 at C1): pooled share mean 9.17%, spread 0.09 points, worst
  0.29 points off, so "within 0.5 points" in Done when is safe; a single town of 10,000 spreads 0.93 points (1st to
  99th percentile 7.0% to 11.4%).

## Done when
1. C1 shows TP 90, FN 10, FP 891, TN 9,009 and "Of 981 who tested positive, 90 have it: 9.17%".
2. C2 gives 81.08%, C3 gives 9.02%, C5 gives 90.91%, C7 gives 1.00%.
3. C4's tree shows 81 and 80.2 on average, and 50.25%.
4. Table: dividing by the Positive column gives 90/981; by the Has it row gives 90/100; the addition panel ends at 0.0991.
5. Random run with the same seed gives the same counts twice; a new seed changes them; Run 100 towns at C1 ends within 0.5 points of 9.17%.
6. 100,000 people draws without stalling and the legend says each square is 10 people.
7. Focus: at 1366x768 and 1000x625 the grid is the largest thing in Town and Cases, the two-way table in Table and the tree in Second test.
8. Tap while it plays: moving a slider during a beat or during Run 100 towns shows the new numbers at once; Test everyone waits at the Predict pause until Lock in guess or Skip guess.
9. Color is never the only signal: positives carry a plus badge and has-it is filled; the paintings load on the band and the case cards.
10. Keyboard alone can run C1 and the Table; every size in STANDARDS.md keeps the grid and the main readout visible without page scrolling; no voice line names a disabled or hidden control.
11. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- S-CP.B.8 (+) shows only as the tree's probability view, and S-CP.B.9 (+) (counting) is not taught. Keep the
  module's codes, or place B.9 elsewhere?
- The condition is made up ("glimmer fever") but C1 uses the numbers of a real screening example, credited on the
  card without naming the disease. OK?
