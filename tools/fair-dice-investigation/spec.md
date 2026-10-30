# Fair Dice Investigation

## One idea
Someone is cheating at the board game café's tournament, and you have a limited budget of rolls and three cases to
crack. Every accusation must survive a test: chi-square for a die's faces, chi-square for a table of wins by seat, and
a t test for a slope. Spend rolls badly or test everything in sight and you will accuse an honest die.

## Not like
- courtroom-statistics (gr 12, same group): z and t tests for means and proportions, run as a trial. Here the other AP tests (chi-square and slope) as detective work, with a roll budget.
- game-show-strategist (gr 12, same group): uses probability to choose a strategy. Here probability is the suspect: is this die what it claims?
- carnival-odds (gr 7, probability family): long-run frequencies for fair games. Here deciding from limited data whether a game is fair.
- correlation-guessing-game (gr 9): judges r by eye. Here the slope gets a test and an interval.

## Who and how
- Grade 12, Statistics, Math: statistics. Students drive, alone or in pairs. 25 to 45 minutes (each case is about 10).
- Topic line: "chi-square tests and inference for slope".
- Standards (module): AP-STAT.U8; AP-STAT.U9.
- AP clusters: Case 1 and Dice lab serve AP-STAT.U8 (goodness of fit); Case 2 serves AP-STAT.U8 (homogeneity of a two-way table); Case 3 serves AP-STAT.U9 (t test and interval for a slope). No CCSS codes in this module; the S-ID.C.8 and S-IC.B ideas show up only in passing.
- tool.json: driver "students", minutes "25-45", modes ["Cases", "Dice lab"], grades_label "Grade 12".

## Screens and modes
Header: title, subtitle "Something at this table isn't fair." Modes `Cases` (opens first), `Dice lab`. Kit buttons.
Stage: the game table (painted felt, art: felt-table) with the case's evidence on it; under it the test card (observed,
expected, contributions, statistic, df, p-value). Panel: the case notebook (budget, notes, Accuse button). A case
picker at the top of the notebook shows three case cards (Case 1: the four dice cutouts; Case 2: case2-file; Case 3:
case3-file) over the dimmed café (art: cafe-after-hours) the first time Cases opens.

### Cases (three, in order; finished cases stay open)
Each case opens with a short briefing card: the librarian's portrait (art: librarian) and two or three lines of text.
Case 1, The loaded die. Focus: the chosen die's six face-count bars with the expected count as a dashed line across
them, center stage; the four dice sit in a row above the bars, the test card below. Four dice (Red, Blue, Green,
White; art: die-*) with a budget of 1,200 rolls. Tap a die, roll it (`Roll 1`, `Roll 10`, `Roll 100`); its six face
counts grow as bars. `Test this die` (needs at least 30 rolls, so every expected count is at least 5) shows the
goodness-of-fit card at the α chosen in the notebook (0.10, 0.05, 0.01). `Accuse` one die. Right: case closed with the
die's true weights shown. Wrong: the café librarian shows that honest die's true weights and the "test everything"
note (Content). One more try. A second wrong accusation shows all four dice's true weights, stamps the case "Closed:
the evidence ran out" and opens Case 2.
Case 2, The first-player edge. Focus: the two-way table, center stage, large; the chi-square card beside it on wide
screens and under it on narrow ones. Results of 360 games across three games (120 each): rows are games, columns are
the seat that won (seat 1 moves first). Question: is the seat pattern the same for every game? Build expected counts
by dragging the row and column totals into a cell (the formula row total × column total / grand total fills in; also
`Fill the rest` once three cells are built by hand), then the full chi-square card. Then `Point to the cell` and tap
the cell that drives the result.
Case 3, The weighted dice. The suspect (art: suspect, on the briefing card) claims his hidden weights don't change
anything. Focus: the scatter plot being tested with its residual plot under it, center stage; a tab pair `Weight
depth` / `Temperature` switches which one is shown. Two scatter plots: mean roll against weight depth (12 dice; the
evidence bag of dice from case3-file sits beside the tab) and mean roll against café temperature (12 nights, the
decoy). For each: least squares line, residual plot, `Test the slope` (t, df, p) and a 95% interval for the slope.
Then decide: `Weights are the link` or `Temperature is the link`, and cite the evidence with `p-value` or `Interval`.
`Shuffle the y values` runs 1,000 shuffles and draws the shuffled slopes as a dot plot with the real slope marked.

### Dice lab
Focus: the share-flagged result (a big percent with its dot strip of 1,000 runs) and the table of n against share
flagged, center stage; the die and sliders in the panel. Free play. One die (art: die-white). Six sliders set its face
weights (they renormalize; presets Fair and Case 1). Pick n (30, 60, 120, 300, 600, 1,000) and α. `Roll once` shows
one test; `Run 1,000 investigations` shows the share that flag the die. With a fair die that share sits near α (the
false alarm rate); with the loaded die it is the power. A table builds up of n against share flagged.

## Content
Setting (made up, labeled "made-up café, made-up data"): the Night Owl board game café's tournament; the game names are
generic (Tile game, Train game, Castle game).
Case 1: the loaded die is chosen by seed among the four. Its face probabilities: 1/8, 1/6, 1/6, 1/6, 1/6, 5/24 (ones
show less, sixes more). Others fair.
- Goodness of fit: χ² = Σ (O - E)²/E with E = n/6, df 5. Critical values for df 5: 9.236 (0.10), 11.070 (0.05), 15.086 (0.01).
- Worked example (shown in the notebook's help): 600 rolls [71, 96, 104, 99, 101, 129]; contributions 8.41, 0.16,
  0.16, 0.01, 0.01, 8.41; χ² = 17.16, p = 0.0042. A fair-looking 60: [11, 9, 10, 8, 12, 10] gives χ² = 1.0, p = 0.963.
- Power at α 0.05 for the loaded die (noncentral chi-square approximation): 30 rolls 0.079, 60 0.112, 120 0.189,
  300 0.45, 600 0.788, 1,000 0.96. So 300 rolls on each of four dice finds it less than half the time. The budget
  rewards a quick look at every die (100 rolls each) and then putting each next 100 rolls on whichever die looks most
  suspicious so far; that finds the loaded die with p under 0.05 about 58% of the time, against 43% for 300 on each.
- Testing several honest dice at 0.05: chance of at least one false alarm 1 - 0.95³ = 14.3% for three, 1 - 0.95⁴ =
  18.5% for four.
- The "test everything" note (wrong accusation): "This die was honest. In this case three dice are honest; test all
  three at 0.05 and about one time in seven, at least one of them looks guilty by chance. Test four honest dice and it
  is nearly one in five."
Case 2 table (wins by seat, 120 games per row):

| Game | Seat 1 | Seat 2 | Seat 3 | Seat 4 |
|---|---|---|---|---|
| Tile game | 31 | 31 | 30 | 28 |
| Train game | 30 | 32 | 29 | 29 |
| Castle game | 54 | 25 | 22 | 19 |

Column totals 115, 88, 81, 76; expected per row 38.333, 29.333, 27, 25.333. χ² = 14.397, df 6, p = 0.0255. Biggest
cell: Castle game seat 1 (6.403); the Castle row contributes 6.403, 0.640, 0.926, 1.583. At α 0.05: the seat pattern
differs by game; the Castle game gives the first player an edge.
Case 3:
- Weight depth x (mm hidden under the 1 face): 0.0, 0.1, ..., 1.1. Mean of 600 rolls y: 3.46, 3.58, 3.49, 3.61, 3.52,
  3.70, 3.66, 3.59, 3.79, 3.68, 3.84, 3.77. ŷ = 3.4841 + 0.2850x; r = 0.849, r² = 0.720; s = 0.0672; SE(b) = 0.0562;
  t = 5.07, df 10, p = 0.00048; t* = 2.2281; 95% interval for the slope (0.160, 0.410).
- Decoy, café temperature 18 to 29 °C, mean of 1,200 rolls per night: 3.52, 3.44, 3.55, 3.49, 3.47, 3.58, 3.43, 3.51,
  3.56, 3.46, 3.50, 3.53. Slope 0.00119 per °C, r = 0.090, SE 0.00415, t = 0.286, p = 0.781, 95% interval (-0.0081, 0.0104).
- Conditions card for slope inference (linear, independent, normal residuals, equal spread, random) with the residual
  plot as the evidence.

## Interactions in detail
- Dice rolls come from a seeded generator (`?seed=n` for tests) using each die's weights; counts update every roll.
  The tapped die lifts and shows its rolled face (pips drawn in code on its blank top); `Roll 100` shows a quick
  tumble of under 1 s, then the bars jump. Any tap during the tumble (another die, another Roll, Test) acts at once:
  the rolls already drawn are counted and the new action starts.
- p-values: upper tail of chi-square with df (5 for one die, (rows - 1)(columns - 1) = 6 for Case 2) and two-sided t
  tail with df n - 2 for slopes; shown to 4 places. Slope SE = s / √Σ(x - x̄)².
- Answers checked: Case 1 accusation against the seed's loaded die; Case 2 expected cells to 0.01 and the pointed cell
  must be the largest contribution; Case 3 decision must pick the weight link and cite p or the interval (either
  citation is accepted; picking temperature shows the decoy's p 0.781 and interval crossing 0).
- Budget counter never goes below 0: a Roll bigger than what is left rolls only what is left, and the Roll buttons
  disable at 0 (Accuse stays live). Tests before 30 rolls are refused with the reason. The notebook logs every test
  run (die, n, χ², p), so a student can see how many tests they ran.
- `Shuffle the y values` and `Run 1,000 investigations` compute at once and draw their dots over at most 2 s; a slider,
  n, α or tab change during the draw cancels it and shows the new state at once.
- Solved cases saved on device (localStorage `curio-dice-cases`, try/catch) with `Clear`.
- `window.__tool = {state, setMode, seed(n), roll(die,k), test(die), accuse(die), table(), slope(set), lab(w,n,a,k)}`.

## Look
Dark noir theme from kit/theme-912.css with the stage paper `#0c0a12`; the table is painted green felt (felt-table,
about `#123d30`) with cards `#f4efe2`. Accent `--brand #ff5577` (dice ruby: the suspect die's outline, shaded tails,
the Accuse button), `--brand-ink #10161f`. Bars show counts as text; expected counts are dashed outlines, so color is
never the only signal. Contrast (computed): brand on panel 5.62:1, on sections 5.33:1, on the noir paper 6.38:1;
brand-ink on brand 5.89:1; cards on felt 10.54:1; theme ink on felt 10.28:1. No celebration: a closed case gets a
typed stamp "Case closed". The four dice keep their names as words on every control (Red, Blue, Green, White), never
color alone.

## Art
Local FLUX (`scripts/localart.py`) unless marked people. One style: moody, warm-lamp painted illustration.
- cafe-after-hours: "A cozy board game cafe after closing, wooden shelves of game boxes with blank spines, empty chairs
  pushed in, a green felt table with scattered dice under a single warm lamp, moody night lighting, painted
  illustration"; 16:9; cutout no; people no; dimmed behind the title card and case picker.
- felt-table: "Top-down view of a green felt game table surface with a dark wooden rim along the edges, soft warm
  lamp light pooling in the center, painted illustration"; 16:10; cutout no; people no; full-frame stage background
  under the dice, bars, tables and plots (dimmed under the plots).
- die-red, die-blue, die-green, die-white: "A single translucent ruby red resin game die with rounded corners seen from
  slightly above, every face smooth and blank, warm lamp light, painted illustration, plain white background" (same
  prompt with sapphire blue, emerald green, ivory white); 1:1; cutout yes; people no; the dice row in Case 1, the
  Dice lab die; pips drawn in code on the blank top face.
- case2-file: "Three closed board game boxes with blank lids stacked on a wooden table beside a clipboard of blank score
  sheets and a pencil, warm lamp light, painted illustration"; 4:3; cutout no; people no; the Case 2 card and briefing.
- case3-file: "A small workbench with a hand drill, a dish of tiny metal weights, calipers and a clear evidence bag of
  dice, under a desk lamp, painted illustration"; 4:3; cutout no; people no; the Case 3 card and the evidence beside
  the plot tab.
- librarian: "Portrait of a friendly game librarian in her sixties with silver hair in a bun, reading glasses on a
  chain and a cardigan, holding a worn record book, warm lamp light, painted illustration, plain dark background, chest
  up"; 1:1; cutout yes; people: true (Gemini, `scripts/art.py`, Cory reviews); briefing cards and the wrong-accusation
  note.
- suspect: "Portrait of a smug man in his forties with a neat mustache, a tweed vest and rolled sleeves, arms folded,
  warm lamp light, painted illustration, plain dark background, chest up"; 1:1; cutout yes; people: true (Gemini,
  `scripts/art.py`, Cory reviews); the Case 3 briefing card.
Bars, test cards, the two-way table, scatter and residual plots, dot plots, pips, stamps and preview.svg are drawn in
code (they are charts, tables and labels).

## Voice
Bank voice `curious-librarian` (Aoede), "Say curiously and warmly, like a friendly school librarian": the café's game
librarian, who keeps the tournament records. Not used by math 9-12 neighbors or group siblings (courtroom-statistics
clear-teacher, game-show-strategist hero-coach, sample-machine playful-friend, design-the-study news-reader,
data-desk-distributions upbeat-guide). `Curio.voice`, `scope: () => state.mode + ':' + state.caseId`. Briefing text,
notes and cards are read on screen; Read speaks the hint.
- wCases (how, Cases welcome; stale on the first roll): "One of these four dice is loaded. Tap a die and press Roll 100, then press Test this die."
- budget (how, first time any die passes 300 rolls; stale on Accuse): "Careful with the budget. Give every die a quick look, then keep rolling whichever one looks most suspicious."
- wrongDie (event, wrong accusation; stale on the next accusation or case change): "That die was honest. Test enough dice and one will look guilty by chance. Pick another die and press Accuse."
- outOfEvidence (event, second wrong accusation; stale when Case 2 opens): "The evidence ran out on this one. Here are the true weights. On to Case 2."
- wCase2 (how, Case 2 opens; stale when the first cell is built): "Drag a row total and a column total into each cell to build the expected count."
- pointCell (how, first time the Case 2 chi-square card completes; stale when a cell is tapped): "Now press Point to the cell, and tap the cell that adds the most to chi-square."
- wCase3 (how, Case 3 opens; stale when both slopes are tested): "Two suspects for the higher rolls. Press Test the slope on each plot, then pick the real link."
- closed (event, case solved; stale on next case): "Case closed. I'll file it."
- wLab (how, Dice lab welcome; stale on the first run): "Set the weights, pick a number of rolls, then press Run 1,000 investigations."

## Family engine
none (its chi-square and slope cards are its own; the scatter plots are simple and do not need data-desk).

## Sources
- AP-STAT.U8 and U9: College Board, AP Statistics Course and Exam Description, https://apcentral.collegeboard.org/courses/ap-statistics
- Chi-square goodness of fit and homogeneity: OpenStax, Introductory Statistics 2e, 11.2 "Goodness-of-Fit Test" and 11.4 "Test for Homogeneity", https://openstax.org/books/introductory-statistics-2e/pages/11-2-goodness-of-fit-test
- Inference for the slope of a regression line: OpenIntro Statistics 4e, 8.4 "Inference for linear regression", https://www.openintro.org/book/os/
- Multiple testing (at least one false alarm across several tests): OpenIntro Statistics 4e, 7.5 and 8.4 notes on multiple comparisons, https://www.openintro.org/book/os/
- The café, the dice, the tables and the scatter data are made up.
- Checks run (Python, numpy and scipy, 2026-10-29): worked example χ² 17.16, p 0.0042, contributions 8.41, 0.16, 0.16,
  0.01, 0.01, 8.41; fair 60 χ² 1.0, p 0.963; critical values 9.236, 11.070, 15.086; loaded weights sum to 1.
  Power, noncentral approximation against 20,000 simulated runs each: 30 rolls 0.079 / 0.076, 60 0.112 / 0.105, 120
  0.189 / 0.190, 300 0.45 / 0.445, 600 0.788 / 0.792, 1,000 0.96 / 0.964. Fair die false alarm rate by simulation
  0.047 to 0.052 at every n from 30 to 1,000 (so the chi-square approximation holds at 30 rolls). False alarm across
  three and four honest dice 14.3% and 18.5%.
- Budget strategies, 10,000 to 20,000 simulated cases each (success = the die with the smallest p is the loaded one
  and p < 0.05): 300 on each 43%; 150 each then 600 on the leader 46%; 100 each then 800 on the leader 41%; 100 each,
  then each next 100 on the current leader 58%. The first draft's advice ("a quick look, then most rolls on the
  suspect") matches the last strategy only if the student keeps switching, so the advice now says so. The draft's
  wrong-accusation note said four honest dice; Case 1 has three, so the note now gives both numbers.
- Case 2: column totals, expected cells, χ² 14.397, df 6, p 0.0255 and the twelve contributions (largest 6.403)
  reproduced with scipy chi2_contingency. Case 3: ŷ = 3.4841 + 0.2850x, r 0.849, r² 0.720, s 0.0672, SE 0.0562, t 5.07,
  p 0.00048, t* 2.2281, interval (0.160, 0.410); decoy slope 0.00119, r 0.090, SE 0.00415, t 0.286, p 0.781, interval
  (-0.0081, 0.0104). Shuffle test on the weight data, 5,000 shuffles: 0.06% as extreme as the real slope.
- 1,000-run bands in Done when: binomial spread 0.0069 at 0.05 and 0.0129 at 0.79, so ±0.02 and ±0.04 are about three
  spreads wide.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. The worked example [71, 96, 104, 99, 101, 129] gives χ² 17.16, p 0.0042, and the contributions shown.
2. Case 2 reads χ² 14.397, df 6, p 0.0255; expected cells match to 0.01; the Castle seat 1 cell is the one accepted.
3. Case 3 reads slope 0.2850, t 5.07, p 0.00048, interval (0.160, 0.410); the decoy reads p 0.781.
4. Dice lab, 1,000 investigations: a fair die is flagged 5% ± 2% at α 0.05; the Case 1 die at 600 rolls is flagged 0.79 ± 0.04.
5. Tests under 30 rolls are refused; the budget stops at 1,200; a wrong accusation shows the false alarm note; a
   second wrong accusation closes Case 1 and opens Case 2.
6. Focus: at 1366x768 and 1000x625 the face bars (Case 1), the two-way table (Case 2), the scatter with residuals
   (Case 3) and the share flagged (Dice lab) are each the largest thing on the stage.
7. Tap while it plays: during a Roll 100 tumble, a shuffle draw or a 1,000-run draw, another Roll, a slider or a tab
   acts at once and the counts stay exact.
8. Solved cases survive reload; `Clear` clears them.
9. Every size in STANDARDS.md keeps the table, the test card and the Roll buttons visible without page scrolling;
   keyboard only works; no voice line names a disabled control; console clean, no network.

## Open questions
- [fair-dice-investigation] The concept title suggests a casino. The spec uses a board game café tournament instead, to keep gambling out of a school tool. OK?
- [fair-dice-investigation] Case 2 is a homogeneity test; a test of independence (one sample, two variables) is not in its own case, only explained in the card's help. Enough for AP-STAT.U8?
- [fair-dice-investigation] Case 1 is hard on purpose: even the best play with 1,200 rolls finds the loaded die with p under 0.05 only about 58% of the time (64% with 1,500, 71% with 2,000). Keep 1,200, or raise the budget?
- [fair-dice-investigation] Two new portraits with people (librarian, suspect) for Cory's review.
