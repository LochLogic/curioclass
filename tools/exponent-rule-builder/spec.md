# Exponent Rule Builder

## One idea
On a power ladder every rung up multiplies by the base, so the rules are just climbing (climb 3 then 2 lands on
rung 5), and when you split one rung into two equal half-steps, the half-step factor has to be a number that
times itself gives the base: you find it with a slider, and that number is the square root.

## Not like
- square-root-hunt (gr 8, number-line): squeezes √2 between decimals on a number line. Here √2 is forced by the rule that two half-steps make one step; decimals are only the slider's readout.
- size-of-everything (gr 8): powers of ten as a scale of real sizes. Here any base, and the exponent axis between and below the rungs (zero, negative and fractional exponents).
- polynomials-as-numbers (gr 9, same group): place-value columns for polynomials. Here one base and its exponents, no polynomials.
- outbreak-model and savings-plan (gr 11): growth over time with logs and series. Here no time and no context: exponents as moves on a ladder.
- undo-machine (gr 11, same format): chains of machines and their inverses. Here a single multiplication repeated, split and reversed.

## Who and how
- Grade 9, Algebra 1, Rational Exponents and Real Numbers. Students drive. 15 to 35 minutes.
- Topic line: "exponent rules, roots and rational exponents".
- Standards (module): N-RN.A (A.1 rational exponents defined by extending the rules; A.2 rewrite radicals and rational exponents), N-RN.B (B.3 sums and products of rational and irrational numbers).
- CCSS clusters: Ladder and Rule lab serve N-RN.A.1; Rung puzzles serve N-RN.A.2; Rational or not serves N-RN.B.3.
- tool.json: driver "students", minutes "15-35", modes ["Ladder", "Rule lab", "Rung puzzles", "Rational or not"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "Every rung multiplies by the base." Modes `Ladder` (opens first), `Rule lab`,
`Rung puzzles`, `Rational or not`. Kit buttons.
Stage: the power ladder drawn horizontally across a painted canyon wall (art: canyon-wall): an exponent axis along the
bottom (rungs at whole numbers, labeled "−2", "−1", "0", "1"...), and above each rung a stone step whose height is the
value b^n on a log scale (so each rung up is the same rise: multiplying is a fixed step). The steps are code shapes
filled with the painted rock texture (art: rock-texture) and a `#a5a8ff` top edge. Between rungs an arc labeled
"× b"; climbing down the arc reads "÷ b". The climber is a painted mountain goat (art: goat-stand, goat-leap) that
stands on the step tops. Panel at right; under 1000 px wide below, with the base picker and buttons first.

### Ladder (explore)
Focus: the goat on the ladder and the "b^n = value" readout right above it.
Base picker `2` `3` `4` `9` `10` `1/2`. The goat can be dragged anywhere along the exponent axis from −3 to 5
(snapping to the current split), or moved with arrow keys; it shows the leap pose while moving (200 ms per rung,
instant with Motion off) and the standing pose at rest. Readout: "b^n = value", exact when the exponent has
denominator 1, 2, 3 or 4 ("2^(3/2) = 2√2 ≈ 2.828"), decimal otherwise. `Split` `1` `2` `3` `4`: each rung is cut
into that many equal small steps; each small arc is labeled "× r", where r is the small-step factor shown exactly
(√2, ∛2) once Rule lab card R6 or R7 is done, and "× ?" before.

### Rule lab (puzzles that unlock rule cards)
Focus: the ladder with the experiment's climb on it; the trial table and the three rule choices sit in the panel.
Seven experiments, in order; each unlocks a rule card (a code card over the painted blank stone tablet, art:
rule-tablet) that stays on the card shelf (this page session). Every experiment has a short goal, a trial table the
tool fills as you climb, and three candidate rules to pick from (one right, two common wrong ones). A wrong pick
shows the trial that breaks it.
- R1 Climb then climb: start on rung m, climb n more. Trials (2, 3), (1, 4), (3, 2) on base 2. Pick b^m × b^n = b^(m+n) (wrong: b^(m×n); (b×b)^(m+n)).
- R2 Climb down: start on rung m, go down n. Pick b^m ÷ b^n = b^(m−n) (wrong: b^(m÷n); b^(m+n)).
- R3 Rung zero: from rung 1 go down one rung. Pick b^0 = 1 (wrong: b^0 = 0; b^0 = b).
- R4 Below zero: keep going down. Pick b^(−n) = 1 / b^n (wrong: b^(−n) = −b^n; b^(−n) = −n·b).
- R5 Climb in jumps: repeat a climb of m rungs n times. Pick (b^m)^n = b^(m×n) (wrong: b^(m+n); b^m × n).
- R6 Half a rung (the proof): Split 2 on base 2. Two equal half-steps must make one whole step (× 2). A slider `r`
  sets the half-step factor (from 1 to 2 on base 2, from 1 to 4 on base 9; step 0.0001, with a number box). Readout
  "r × r = 1.9600 (one whole step needs 2)". When |r × r − 2| < 0.001 the tool states the proof in three lines: "If
  2^(1/2) follows the climbing rule, then 2^(1/2) × 2^(1/2) = 2^(1/2 + 1/2) = 2^1 = 2. So 2^(1/2) is the number whose
  square is 2: √2. Its decimals never end or repeat: 1.41421356..." Then `Try base 9` sets the same slider on base 9,
  where it lands exactly on r = 3.
- R7 Thirds and more: Split 3 on base 8, slider `r` from 1 to 4: r × r × r = 8 gives r = 2 = ∛8; then
  8^(2/3) = (∛8)^2 = 4. Pick b^(m/n) = (ⁿ√b)^m (wrong: b^(m/n) = b^m ÷ n; (b ÷ n)^m).

### Rung puzzles
Focus: the ladder with its labeled rungs, center stage; the tile tray sits under it.
Levels 1 to 8. Each shows a ladder with the rungs listed and a tray of expression tiles; drag each tile onto the
rung where its value lands (more than one tile may share a rung). `Check` (enabled once every tile is placed) marks
each tile placed right or wrong (check or cross glyph, plus text). A level clears when all tiles are right. Levels
unlock in order; cleared levels are saved on this device (localStorage `curio-exponent-rules`, try/catch) with
`Clear progress`.

### Rational or not
Focus: the two bins and the tile being dragged; the reason card opens under them.
Twelve tiles. Drag each to the `Rational` or `Irrational` bin (painted bins with code labels, art: sorting-bins).
After each drop the reason card shows the rule that decides it (Content). A wrong drop slides back (300 ms) with the
reason; no score is kept.

## Content
Rung puzzle levels (base; rungs shown; tiles with their rung):
1. Base 2; rungs −3 to 5. 2²·2³ → 5. 2⁶/2⁴ → 2. (2²)² → 4. 2⁰ → 0. 2^(−1) → −1. 1/8 → −3.
2. Base 3; rungs −3 to 4. 3⁴/3⁶ → −2. (3^(−1))^(−2) → 2. 3²·3^(−2) → 0. 1/27 → −3. 81 → 4. 3 → 1.
3. Base 4; halves from −1 to 3. √4 → 1/2. √(4³) → 3/2. 4^(−1/2) → −1/2. 32 → 5/2. 1/4 → −1. 1 → 0.
4. Base 8; thirds from 0 to 2. ∛8 → 1/3. 4 → 2/3. 8^(2/3) → 2/3. (∛8)⁵ → 5/3. 16 → 4/3. 64 → 2.
5. Base 9; halves from −2 to 3. 27 → 3/2. 9^(−1/2) → −1/2. √(9⁵) → 5/2. 9^(1/2)·9^(1/2) → 1. 1/81 → −2. 3 → 1/2.
6. Base 2; halves from −1 to 3. √2 → 1/2. 2√2 → 3/2. √8 → 3/2. 1/√2 → −1/2. √32 → 5/2. (√2)⁴ → 2.
7. Base 16; quarters from −1/2 to 3/2. 16^(1/4) → 1/4. 16^(3/4) → 3/4. √16 → 1/2. 16^(−1/4) → −1/4. 32 → 5/4. (16^(1/2))^(1/2) → 1/4.
8. Base x (x > 0, rungs labeled by exponent only): −1/2, 1/2, 2/3, 3/4, 5/6, 1, 3/2. Tiles: √(x³) → 3/2. x√x → 3/2.
   ∛(x²) → 2/3. 1/√x → −1/2. (∜x)³ → 3/4. √x·∛x → 5/6. √x → 1/2.
Rational or not (answer; reason card):
√2 irrational (no fraction squares to 2). √9 = 3 rational. 8^(1/3) = 2 rational. 2^(1/2)·2^(3/2) = 4 rational
(two irrationals can multiply to a rational). √2 + 1 irrational (rational plus irrational is irrational: if
√2 + 1 = q were rational, √2 = q − 1 would be rational). 3√2 irrational (a nonzero rational times an irrational is
irrational). 0·√2 = 0 rational (zero is the exception). 4^(1/2) + 1/2 = 5/2 rational. √2 + √2 = 2√2 irrational.
√2·√3 = √6 irrational. 1/3 + 2/7 = 13/21 rational (a/b + c/d = (ad + bc)/bd, a fraction). 0.75 + 1/4 = 1 rational.

## Interactions in detail
- Every tile, rung and climber position is an exact (base, exponent) pair with the exponent a fraction; placement
  is checked by exact exponent equality (2√2 is stored as 2^(3/2), √32 as 2^(5/2)). No floating point decides a check.
- Exact readouts write a base that is a perfect power as its root first (4 = 2², 9 = 3², 8 = 2³, 16 = 2⁴), then pull
  out whole powers: 9^(1/4) = √3, 4^(3/4) = 2√2, 2^(5/4) = 2∜2. Negative exponents read as a fraction with the
  radical kept in the denominator to match the tiles: 2^(−1/2) = 1/√2. Base 1/2: 2^(−n) the same way.
- Values on the ladder's log scale: step height ∝ n (the exponent), so the picture never overflows; the value
  label prints above. Base 1/2 makes the ladder descend; the readout says "each rung multiplies by 1/2".
- Ladder readout precision: decimals to 4 significant figures with "≈"; exact forms for denominators up to 4.
- R6 and R7 slider: values outside the slider's range are refused in the box; keyboard steps 0.0001 (Shift 0.01).
  The proof text appears only after the slider is within tolerance (|r^k − b| < 0.001); it never states √2 as a
  decimal that ends.
- Rule lab picks are not scored; a wrong pick shows "Try it: climb 2 then 3 on base 2. b^(m×n) says rung 6; the
  ladder says rung 5."
- Short animations (the goat's leap, a tile sliding back) never block input: a drag, key or tap during one ends it
  at once and acts.
- Reset: `Start over` in each puzzle level and each lab card; mode switches keep state for the session.
- Keyboard: tiles are buttons; Enter picks a tile up, arrow keys choose a rung, Enter drops.
- `window.__tool = {state, setMode, level(n), place(tile, rung), rules()}`.

## Look
Accent `--brand #a5a8ff` (periwinkle), `--brand-ink #10112b`. The painted canyon wall (art: canyon-wall) fills the
stage, dimmed to 45% under a `#111827` wash so rung lines `#2b3646` (drawn brighter, `#5a6a80`, over the painting),
step tops `#a5a8ff`, arcs `#c9d3df` and "× b" labels `#e8edf3` stay readable; rung labels and the readout sit on
`#111827` chips at 85%. Climber is the painted goat; tiles and cards are code with dark ink.
Contrast (computed): brand on panel 7.95:1, on --sec-bg 7.53:1, brand-ink on brand 8.48:1; labels on their chips
above 12:1. Right and wrong marks use glyphs and words, not color alone.

## Art
Local FLUX (`scripts/localart.py`); no people. One style: warm desert canyon, painted illustration.
- canyon-wall: "A tall sandstone canyon wall in warm red and orange layers under a clear evening sky, ledges stepping
  up across the rock, painted illustration"; 16:9; cutout no; people no; stage background on every mode, dimmed.
- rock-texture: "A full-frame close-up texture of layered red sandstone, even light, painted illustration"; 1:1;
  cutout no; people no; fills the step shapes, which the code draws to height.
- goat-stand: "A white mountain goat standing side view on all four hooves, alert, painted illustration, plain white
  background"; 1:1; cutout yes; people no; the climber at rest, sized to 1.2 rung widths.
- goat-leap: "A white mountain goat leaping side view with legs tucked, painted illustration, plain white background";
  1:1; cutout yes; people no; the climber while moving between rungs, same size as goat-stand.
- rule-tablet: "A small smooth stone tablet with a blank flat face and chipped edges, painted illustration, plain
  white background"; 4:3; cutout yes; people no; behind each rule card on the shelf, rule text in code on the face.
- sorting-bins: "Two wooden sorting bins side by side with blank plank fronts, painted illustration, plain white
  background"; 16:9; cutout yes; people no; the Rational and Irrational bins, labels in code on the blank fronts.
The ladder's axis, rungs, arcs, labels, tiles, trial tables and preview.svg are drawn in code (a diagram).

## Voice
Bank voice `calm-professor` (even, clear). Different from the math 9-12 neighbors, group siblings and batch specs.
`Curio.voice`, `scope: () => state.mode`. Cards and reason text are read on screen; Read speaks the hint.
- wLadder (how; Ladder entered; stale after the first climb): "Drag the goat along the ladder, or use the arrow keys. Every rung up multiplies by the base."
- wLab (how; Rule lab entered; stale after the first climb in a card): "Climb the way the card asks. Then tap the rule that matches every trial."
- wPuzzle (how; Rung puzzles entered; stale after the first tile placed): "Drag each tile to the rung where its value lands. Then press Check."
- wRational (how; Rational or not entered; stale after the first drop): "Drag each number into the Rational or Irrational bin. The card says why."
- half (how; R6 opens; stale once the proof shows): "Two half steps must make one whole step. Slide r until r times r is 2."
- wrongRule (event; a wrong rule pick; stale on the next pick): "That rule breaks on the trial shown. Tap another rule."
- proof (event; R6 tolerance met, on base 2 or base 9; stale when the card or base changes): "There it is. The half step is the square root of the base."
- proof3 (event; R7 tolerance met; stale when the card changes): "Three equal steps make one rung, so each is the cube root of 8."
- rule (event; a lab card unlocked; stale on the next card): "Rule unlocked. It's on your shelf."
- cleared (event; a puzzle level cleared; stale on level change): "Level cleared."

## Family engine
none.

## Sources
- N-RN.A and N-RN.B: Common Core State Standards for Mathematics, High School Number and Quantity, The Real Number System, https://www.thecorestandards.org/Math/Content/HSN/RN/
- Rules of exponents, zero and negative exponents, rational exponents: OpenStax, Intermediate Algebra 2e, 5.2 "Use Multiplication Properties of Exponents" and 8.3 "Simplify Rational Exponents", https://openstax.org/books/intermediate-algebra-2e/pages/8-3-simplify-rational-exponents
- √2 is irrational; sums and products of rational and irrational numbers: OpenStax, Prealgebra 2e, 7.1 "Rational and Irrational Numbers", https://openstax.org/books/prealgebra-2e/pages/7-1-rational-and-irrational-numbers
- Checks run (Python with sympy, 2026-10-29): all 42 tiles of levels 1 to 7 land on their listed rung (exact log
  base b); level 8's seven tiles reduce to exponents 3/2, 3/2, 2/3, −1/2, 3/4, 5/6, 1/2 as listed; all 12 Rational
  or not answers match sympy's is_rational. R6 tolerance window on base 2 is r from 1.41386 to 1.41457 (about 7
  slider steps): 1.4142 passes (1.99996), 1.41 fails (1.9881). Base 9's window is 2.99983 to 3.00017 and R7's cube
  window on base 8 is 1.99992 to 2.00008. The first draft's R6 slider ran 1 to 2, so base 9 could never reach r = 3;
  the range is now 1 to 4 off base 2. Exact readouts: 2^(3/2) = 2√2 ≈ 2.828, 2^(−2) = 1/4, 9^(1/4) = √3, 4^(3/4) =
  2√2, 2^(5/4) = 2∜2 ≈ 2.378, 10^(1/3) ≈ 2.154; the perfect-power rule was added because 9^(1/4) and 4^(3/4) need it.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Ladder base 2, goat at 3/2 reads "2^(3/2) = 2√2 ≈ 2.828"; at −2 reads "1/4"; base 9 at 1/4 reads "√3"; base 1/2 descends.
2. R1 accepts only b^(m+n); picking b^(m×n) shows the trial (2, 3) landing on rung 5, not 6.
3. R6: the proof appears at r = 1.4142 (r × r = 1.99996) and not at r = 1.41 (1.9881); `Try base 9` lets the slider reach r = 3 exactly.
4. Level 4: 8^(2/3) and 4 both belong on rung 2/3 and both check right; (∛8)⁵ belongs on 5/3.
5. Level 6: √8 and 2√2 both land on 3/2; level 8: x√x and √(x³) both land on 3/2, √x·∛x on 5/6.
6. Rational or not: 2^(1/2)·2^(3/2) is Rational, √2 + √2 is Irrational, 0·√2 is Rational, each with its reason card.
7. Focus: at 1366x768 and 1000x625 the ladder with the goat (Ladder, Rule lab, Rung puzzles) and the two bins (Rational or not) are the largest things on the stage.
8. Tap while it plays: during the goat's leap or a tile sliding back, a drag, arrow key or new tile acts at once.
9. Cleared levels survive a reload; `Clear progress` resets them.
10. All sizes in STANDARDS.md keep the ladder and tile tray visible; keyboard-only play clears level 1; no voice line names a disabled control; console clean, no network.
