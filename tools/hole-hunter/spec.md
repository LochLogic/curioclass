# Hole Hunter

## One idea
The graph is dark and your flashlight beam lights only a small circle of it: sweep the beam to hunt down every break
(holes, moved points, jumps and asymptotes), walk in from the left and the right to read the one-sided limits, then
try to patch each break with a single point, which works only when both sides agree on a finite value.

## Not like
- zoom-to-the-limit (this group, precalculus): limits of slopes on smooth curves. Here limits of function values, and every level is built around a break.
- function-family-reunion (this group, graphing): asymptotes of moved parent functions as features. Here asymptotes come from factors that do not cancel, and the job is classifying and repairing breaks.
- undo-machine (gr 11, built puzzle): chains of function machines; nothing about continuity.
- rollercoaster-polynomials (gr 11, built): zeros from factors; here factors in the denominator make holes and asymptotes, the other half of that story.
- speedometer (this group): derivatives; continuity is only assumed there.

## Who and how
Grade 12, calculus (Limits and Continuity). Students drive, 25 to 40 minutes. Explore first: Bench opens with a lit
rational function to change; Hunt is the puzzle.
Topic line: "limits and continuity".
Standards: AP-CALC.U1 (1.2 to 1.6 limits from graphs and tables, one-sided limits; 1.10 to 1.13 types of
discontinuity, removing discontinuities, continuity of piecewise functions; 1.14 to 1.15 infinite limits, vertical and
horizontal asymptotes).
tool.json: driver "students", minutes "25-40", modes ["Bench", "Hunt"].

## Screens and modes
Header (kit, 9-12 theme): "Hole Hunter", small line "Find every break. Patch what you can." Modes `Bench`, `Hunt`;
kit `Motion`, `Sound`, `Read`.

Stage: a graphing plane, x from -8 to 8, y from -8 to 8 (per level, Content), grid 1, filling the stage. Breaks are
drawn the standard way: a hole is an open circle (`--paper` fill, curve-color ring); a defined point is a filled dot;
vertical asymptotes dashed `--muted` lines; horizontal asymptotes dotted. The probe: a vertical hairline at the
pointer's x with a readout "x = ..., f(x) = ..." (or "undefined").

### Bench (explore, default)
Focus: the lit plane with the curve and its breaks, center stage and largest; the factor tiles and readouts are in the
panel.
Build f(x) = c(x - p1)(x - p2)(x - p3) / ((x - r1)(x - r2)(x - r3)) from factor tiles.
- Panel "Top" and "Bottom": up to three factor tiles each, `Add factor` and a remove (x) on each tile; each tile has a
  value stepper (whole numbers -5 to 5) showing "(x - 2)" or "(x + 3)". A constant c stepper (-4 to 4, not 0).
- Matching tiles (same value top and bottom) are linked with a line and labeled "cancels: hole at x = 2".
- Readouts: the simplified form; holes with their (x, y); vertical asymptotes with the sign on each side ("left -∞,
  right +∞"); zeros; horizontal asymptote or "none" with the reason (degrees compared).
- Probe works everywhere; `Walk in` on any break shows the approach table (below).

### Hunt (the puzzle)
Focus: the dark plane and the flashlight beam, center stage and largest; the step card sits in the panel beside it
(under it below 1000 px wide, kept short so the plane still fills the view at 1366x768).
Picker `Level 1` to `Level 13`. The plane is black except the flashlight beam: a circle of radius 1.2 units around the
pointer (or the keyboard probe), lit softly at the edge. The flashlight cutout (art: flashlight) sits at the bottom
edge of the plane, sliding along under the beam's x and tilting to point at it. Asymptote lines and holes show only
inside the beam.
Card "Breaks found: 0 of N" (N shown). Steps for each break:
1. Find: with the beam over a break, press `Mark here` (or Enter). Within 0.3 of a break's x it snaps and pins the
   break; elsewhere: "Nothing broken here." Breaks may be found in any order.
2. Walk in: the approach table for the pinned x = c: rows x = c - 0.1, c - 0.01, c - 0.001 and c + 0.001, c + 0.01,
   c + 0.1 with f(x) (number format in Interactions).
3. Name it: left limit, right limit, f(c), then the kind. Limits take a number or the buttons `+∞`, `-∞`; f(c) takes a
   number or `undefined`; kind buttons `Hole`, `Moved point`, `Jump`, `Asymptote`; then `Check`. The two-sided limit
   is then filled in by the tool ("exists, = 4" or "does not exist").
4. Patch: `Patch it` gives a draggable glowing dot on the line x = c (snaps 0.25, typed values exact). It sticks only at
   the limit value of a hole or moved point: the curve becomes continuous, the break turns green with "Continuous at
   x = c". For a jump or asymptote, the correct answer is the button `No single point fixes this` and the card says why.
Parameter levels (11 and 13) replace steps 1 to 4 with a "Make it continuous" card: sliders and number boxes for the
parameters; the seam lights green when continuous; checked exactly.
End of level: the whole graph lights up, every break labeled. `Next level`.
Ends at infinity: levels with a horizontal asymptote add a last card "Far away": limits as x goes to -∞ and +∞
(number or ±∞), with `Walk out` rows x = ±10, ±100, ±1000.

## Content
Levels (f, view, breaks with left limit, right limit, f(c), kind; patch value):
1. f(x) = (x² - 4)/(x - 2). x = 2: 4, 4, undefined, hole; patch 4.
2. g(x) = (x² - 1)/(x + 1) for x ≠ -1, g(-1) = 3. x = -1: -2, -2, 3, moved point; patch -2.
3. f(x) = x + 1 for x < 1, x - 2 for x ≥ 1. x = 1: 2, -1, -1, jump; no single point.
4. f(x) = 1/(x - 3). x = 3: -∞, +∞, undefined, asymptote. Far away: 0 and 0 (y = 0).
5. f(x) = 1/(x + 2)². x = -2: +∞, +∞, undefined, asymptote. Far away: 0 and 0.
6. f(x) = (x - 1)/(x² - 1). x = 1: 1/2, 1/2, undefined, hole (patch 0.5). x = -1: -∞, +∞, undefined, asymptote.
7. f(x) = sin(x)/x (radians). x = 0: 1, 1, undefined, hole; patch 1. Note after: "The table shows 0.998334, 0.999983,
   1.00000 (to six figures) from each side, closing in on 1."
8. f(x) = abs(x)/x. x = 0: -1, 1, undefined, jump.
9. f(x) = (x³ - 8)/(x - 2), view y from -4 to 20. x = 2: 12, 12, undefined, hole; patch 12.
10. f(x) = (x² + x - 6)/(x² - 4). x = 2: 5/4, 5/4, undefined, hole (patch 1.25). x = -2: -∞, +∞, undefined, asymptote.
    Far away: 1 and 1.
11. f(x) = kx + 1 for x < 2, x² - k for x ≥ 2. Make it continuous: k = 1 (both sides 3). Wrong k shows the gap
    "left side 2k + 1, right side 4 - k".
12. f(x) = (2x² + 1)/(x² - 9). x = -3: +∞, -∞, undefined, asymptote. x = 3: -∞, +∞, undefined, asymptote. Far away: 2
    and 2.
13. f(x) = x² for x < 1, ax + b for 1 ≤ x < 3, 12 - x for x ≥ 3. Make it continuous: a + b = 1 and 3a + b = 9, so
    a = 4, b = -3.
Bench default: c = 1, top (x - 2)(x + 1), bottom (x - 2)(x - 3): hole at (2, -3), asymptote x = 3 (left -∞, right +∞),
zero at x = -1, horizontal asymptote y = 1. (Simplified (x + 1)/(x - 3); at x = 2: 3/(-1) = -3.)

## Interactions in detail
- Bench analysis per value v: m = count on top, n = count on bottom. n = 0, m > 0: a zero. n > 0, m ≥ n: a hole at v
  with y from the cancelled form (if m > n the hole sits on the x-axis, y = 0). m < n: a vertical asymptote; the sign
  on each side comes from the cancelled form just left and right of v (same sign both sides when n - m is even).
  Horizontal asymptote: top degree < bottom degree: y = 0; equal: y = c; greater: "none: the top grows faster".
  Edge: no bottom tiles: a polynomial ("no breaks"); all tiles cancel: a constant with holes.
- Number format in the approach and walk-out tables: 6 significant figures with trailing zeros kept ("1.00000",
  "-1000.00"); sizes of 10⁶ or more, or under 10⁻³ (but not 0), in scientific form to 3 significant figures
  ("1.00 x 10⁶", "9.96 x 10⁻⁷").
- Answer checks: numbers exact as fractions or decimals within 0.001 ("5/4", "1.25" both right); ±∞ by button only;
  wrong answers name the clue: "Look at the table from the left: the values keep getting more negative." Two misses
  show `Show me`.
- Patch dot: values within 0.001 of the limit stick. Patching a moved point moves the filled dot and removes the old
  one.
- Beam: follows the pointer with no lag, and also the keyboard probe (arrow keys move it 0.1, Shift 1; Up and Down
  move the beam along y). The beam never reveals the answer text, only the drawing. With Motion off the beam edge is
  hard, not animated, and the flashlight jumps instead of tilting smoothly.
- End of level: the light-up spreads across the plane in 0.8 s (instant with Motion off); `Next level`, `Skip level`
  and the level picker act at once during it.
- Table values come from direct evaluation (sin x / x at 0.001 is computed, not looked up); "undefined" when the
  formula divides by 0.
- Levels unlock in order but all are reachable with `Skip level`. Done levels get a check, per device (localStorage
  `curio-hole-hunter`, try/catch), `Clear marks`.
- Mode change: `Curio.stop()`, `V.hush()`.

## Look
Accent (`--brand`) #fff533, flashlight lemon: 15.1:1 on --panel #141b25, 14.3:1 on --sec-bg #18202b; --brand-ink
#10161f on it 15.9:1. Brighter and cooler than poll-workshop's gold #f0b650, the amber tools and the algebra group's
#ffe14d (Intersection Quest); no group sibling uses yellow.
Scene: the dark plane #07090d outside the beam (grid hidden there), the beam lit to the theme plane color #0e1520 with
the grid, a warm rim rgba(255,228,92,0.25). The curve `--gr-1`; a patched break `--ok` with a check glyph and text.
The flashlight art is a dark steel body, so it reads against #07090d by its lit lens and rim highlight.

## Art
Local FLUX (`scripts/localart.py`), no people. Everything else is the graph itself.
- flashlight: "A sturdy dark steel flashlight lying on its side and pointing to the upper right, its round lens glowing
  warm lemon yellow, small highlights along the knurled grip, painted illustration, plain white background"; 4:3;
  cutout yes; people no; Hunt only, at the bottom edge of the plane under the beam, tilted in code to point at it;
  also the small icon on the `Hunt` level card.
The plane, curves, holes, dots, asymptotes, beam mask, factor tiles, tables and preview.svg (the beam on a hole) are
drawn in code: they are the graph and its controls.

## Voice
`big-sister` (Leda), style "Say in a friendly, youthful way, like an older student who loves puzzles." Not used by a
group sibling, a 9-12 math neighbor or another spec in batch R05. `Curio.voice`, `scope: () => state.mode`. Tables
and cards are read on screen; Read speaks the hint.
- bench (how, Bench welcome; stale once a tile changes): "Step the numbers on the top and bottom factor tiles. A factor on both cancels and leaves a hole."
- asym (how, first asymptote made on Bench; stale on a mode change): "A bottom factor that doesn't cancel makes the graph shoot off. That's an asymptote."
- hunt (how, Hunt welcome; stale on the first Mark here): "The graph is dark. Sweep the flashlight over it, and press Mark here when you see a break."
- walk (how, first break pinned; stale once Check is pressed): "Read the table from each side. Type the left limit, the right limit and the value, pick the kind, then press Check."
- patch (how, first break named; stale once that break is patched or ruled out): "Press Patch it and drag the dot, or press No single point fixes this."
- seam (how, first parameter level; stale when the seam lights): "Move the sliders until both pieces meet. The seam turns green when they do."
- far (how, first Far away card; stale once it is answered): "Press Walk out and watch where the values settle at each end."
- nothing (event, Mark here with no break; stale on the next mark): "Nothing broken here."
- patched (event, a patch sticks; stale on a new break): "Patched. It's continuous there now."
- noPatch (event, No single point chosen correctly; stale on a new break): "Right. The two sides don't meet, so one point can't fix it."
- levelDone (event, all breaks done; stale on a new level): "Every break found. Press Next level when you're ready."

## Family engine
none. Uses `kit/graphing.js` `Plane` as a plotting tool (`g.fn` breaks at the undefined points, `g.point` with `lock`
for the patch dot and the probe, `g.segment` for asymptotes, `g.roots` for Bench zeros); the beam is an SVG mask in the
`front` layer.

## Sources
- One-sided limits, limits from tables and graphs, types of discontinuities, removable discontinuities, continuity of
  piecewise functions, infinite limits and asymptotes: College Board, AP Calculus AB and BC Course and Exam
  Description (2020), Unit 1, https://apcentral.collegeboard.org/courses/ap-calculus-ab
- Same topics with worked examples (including lim sin x / x = 1): OpenStax, Calculus Volume 1, 2.2 "The Limit of a
  Function", 2.4 "Continuity", 4.6 "Limits at Infinity and Asymptotes",
  https://openstax.org/books/calculus-volume-1/pages/2-4-continuity
- Every level is made up.
- Checks run (Python, 2026-10-29): every level's six approach rows evaluated directly; each matches its listed left and
  right limits (level 1: 3.999 and 4.001; level 9: 11.994 and 12.006; level 10 at 2: 1.25006 and 1.24994; level 12
  at -3: 3168.14 and -3165.19, so +∞ then -∞). Level 7: 0.998334, 0.999983, then 1 at ±0.001, which the first draft's
  "6 significant figures" would print as "1"; the format now keeps trailing zeros so it reads "1.00000" as the note
  says. Level 5 reaches 1.00 x 10⁶ at ±0.001, and walk-out values reach 9.96 x 10⁻⁷, so the scientific rule now covers
  both very large and very small sizes. Far away at ±1000: level 4 about ±0.001, level 10 0.999 and 1.001, level 12
  2.00002. Level 11 at k = 1: both sides 3; level 13 at a = 4, b = -3: 1 and 1 at x = 1, 9 and 9 at x = 3. Bench default
  hole y = -3, and just left and right of 3: -3999 and 4001. Every patch value (4, -2, 0.5, 1, 12, 1.25) lies on the
  0.25 snap. The closest two breaks in any level are 2 apart, so the 0.3 snap never pins the wrong one.

## Done when
1. Bench default shows the hole at (2, -3), asymptote x = 3 (left -∞, right +∞), zero -1, horizontal y = 1.
2. Bench with top (x - 1)(x - 1) and bottom (x - 1): hole on the x-axis at (1, 0) and no asymptote.
3. Level 1: marking near x = 2 pins it; 4, 4, undefined, Hole accepted; patch at 4 sticks; 3.9 does not.
4. Level 2 needs Moved point and f(-1) = 3; the patch moves the dot to -2.
5. Level 3 and Level 8 accept only `No single point fixes this` as the repair.
6. Level 6 has two breaks; the hole accepts 1/2 and 0.5.
7. Level 7's table shows 0.998334 at ±0.1, 0.999983 at ±0.01 and 1.00000 at ±0.001; Level 5 shows 1.00 x 10⁶ at ±0.001.
8. Level 11 lights the seam only at k = 1; Level 13 only at a = 4, b = -3. Level 12 far away accepts 2 and 2.
9. Focus: at 1366x768 and 1000x625 the plane is the largest thing on the stage in both modes, and in Hunt the step
   card never covers the beam.
10. Tap while it plays: during the end-of-level light-up, `Next level` loads the next level at once; the beam and the
    flashlight follow a fast sweep with no lag.
11. The beam follows arrow keys; how-to lines are spoken once each in five actions; "Nothing broken here." on every
    miss; no line names a control that is not on screen.
12. Controls visible without scrolling at 1366x768; one painted image, no people; no network, no em dashes.

## Open questions
none
