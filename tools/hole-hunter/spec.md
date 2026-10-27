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

Stage: a graphing plane, x from -8 to 8, y from -8 to 8 (per level, Content), grid 1. Breaks are drawn the standard
way: a hole is an open circle (`--paper` fill, curve-color ring); a defined point is a filled dot; vertical asymptotes
dashed `--muted` lines; horizontal asymptotes dotted. The probe: a vertical hairline at the pointer's x with a readout
"x = ..., f(x) = ..." (or "undefined").

### Bench (explore, default)
Build f(x) = c(x - p1)(x - p2)(x - p3) / ((x - r1)(x - r2)(x - r3)) from factor tiles.
- Panel "Top" and "Bottom": up to three factor tiles each, `Add factor` and a remove (x) on each tile; each tile has a
  value stepper (whole numbers -5 to 5) showing "(x - 2)" or "(x + 3)". A constant c stepper (-4 to 4, not 0).
- Matching tiles (same value top and bottom) are linked with a line and labeled "cancels: hole at x = 2".
- Readouts: the simplified form; holes with their (x, y); vertical asymptotes with the sign on each side ("left -∞,
  right +∞"); zeros; horizontal asymptote or "none" with the reason (degrees compared).
- Probe works everywhere; `Walk in` on any break shows the approach table (below).

### Hunt (the puzzle)
Picker `Level 1` to `Level 13`. The plane is black except the flashlight beam: a circle of radius 1.2 units around the
pointer (or the keyboard probe), lit softly at the edge. Asymptote lines and holes show only inside the beam.
Card "Breaks found: 0 of N" (N shown). Steps for each break:
1. Find: with the beam over a break, press `Mark here` (or Enter). Within 0.3 of a break's x it snaps and pins the
   break; elsewhere: "Nothing broken here." Breaks may be found in any order.
2. Walk in: the approach table for the pinned x = c: rows x = c - 0.1, c - 0.01, c - 0.001 and c + 0.001, c + 0.01,
   c + 0.1 with f(x) to 6 significant figures (very large values in scientific form like 1.00 x 10⁶).
3. Name it: left limit, right limit, f(c), then the kind. Limits take a number or the buttons `+∞`, `-∞`; f(c) takes a
   number or `undefined`; kind buttons `Hole`, `Moved point`, `Jump`, `Asymptote`. Then the two-sided limit is filled
   in by the tool ("exists, = 4" or "does not exist").
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
- Answer checks: numbers exact as fractions or decimals within 0.001 ("5/4", "1.25" both right); ±∞ by button only;
  wrong answers name the clue: "Look at the table from the left: the values keep getting more negative." Two misses
  show `Show me`.
- Patch dot: values within 0.001 of the limit stick. Patching a moved point moves the filled dot and removes the old
  one.
- Beam: also follows the keyboard probe (arrow keys move it 0.1, Shift 1; Up and Down move the beam along y). The beam
  never reveals the answer text, only the drawing. With Motion off the beam edge is hard, not animated.
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

## Art
none: drawn in code (plane, beam, holes, dots, asymptotes, preview.svg with the beam on a hole).

## Voice
`big-sister` (Leda), style "Say in a friendly, youthful way, like an older student who loves puzzles." Not used by a
group sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`.
- bench (how, Bench welcome): "Change the factors on top and bottom. A factor on both cancels and leaves a hole."
- asym (how, first asymptote made on Bench): "A bottom factor that doesn't cancel makes the graph shoot off. That's an asymptote."
- hunt (how, Hunt welcome): "The graph is dark. Sweep the flashlight, and press Mark here when you see a break."
- walk (how, first break marked): "Read the table from each side. Then type the left limit, the right limit and the value."
- nothing (event, Mark here with no break; stale on the next mark): "Nothing broken here."
- patched (event, a patch sticks; stale on a new break): "Patched. It's continuous there now."
- noPatch (event, No single point chosen correctly; stale on a new break): "Right. The two sides don't meet, so one point can't fix it."
- levelDone (event, all breaks done; stale on a new level): "Every break found."

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
- Every level is made up; every limit and table value checked in Python (2026-10-27).

## Done when
1. Bench default shows the hole at (2, -3), asymptote x = 3 (left -∞, right +∞), zero -1, horizontal y = 1.
2. Bench with top (x - 1)(x - 1) and bottom (x - 1): hole on the x-axis at (1, 0) and no asymptote.
3. Level 1: marking near x = 2 pins it; 4, 4, undefined, Hole accepted; patch at 4 sticks; 3.9 does not.
4. Level 2 needs Moved point and f(-1) = 3; the patch moves the dot to -2.
5. Level 3 and Level 8 accept only `No single point fixes this` as the repair.
6. Level 6 has two breaks; the hole accepts 1/2 and 0.5.
7. Level 7's table shows 0.998334 at ±0.1 and 0.999983 at ±0.01.
8. Level 11 lights the seam only at k = 1; Level 13 only at a = 4, b = -3. Level 12 far away accepts 2 and 2.
9. The beam follows arrow keys; how-to lines are spoken once each in five actions; "Nothing broken here." on every miss.
10. Controls visible without scrolling at 1366x768; no network, no images, no em dashes.

## Open questions
none
