# Coordinate Proof Lab

## One idea
A shape on a grid is a claim you can check with arithmetic: drag the corners of a quadrilateral and a measuring
table gives every side as an exact length, every slope as a fraction and every diagonal's midpoint, a name board
says which names the numbers prove (parallelogram, rectangle, rhombus, square, trapezoid), and on proof cards you
pick only the measurements a proof needs; a bowtie whose opposite sides are equal shows why "it looks like a
parallelogram" is never enough.

## Not like
- rigid-motion-twins (gr 10, this group): shapes move onto each other. Here shapes stay put and you measure them.
- proof-blocks, now Proof Tower (gr 10, this group): proofs as statements and reasons. Here a proof is a set of computed measurements a checker accepts.
- circle-theorem-explorer (gr 10, this group): circles with angles and arcs, no coordinates. Here a circle is an equation and a point is on it only if the numbers say so.
- intersection-quest (gr 9 race): where two lines cross. Here slopes compare sides; nothing is solved for a crossing.
- cone-slicer, now Conic Focus Finder (gr 12): the parabola from its focus and directrix (G-GPE.A.2 stays there).

## Who and how
- Grade 10, Geometry, module Coordinate Geometry. Students drive, own laptops or pairs; the Quad lab also works on a
  projector. 15 to 40 minutes.
- Topic line: "proving with coordinates".
- Standards (module): G-GPE.A (equations of conic sections: the circle by completing the square), G-GPE.B (use
  coordinates to prove simple theorems; slopes of parallel and perpendicular lines; partition a segment; perimeter
  and area).
- CCSS clusters: Quad lab serves G-GPE.B.4, B.5, B.7; Partition serves B.6; Circle serves A.1 and B.4 (is a point on
  the circle?); Prove serves B.4, B.5 and B.7.
- tool.json: driver "students", minutes "15-40", modes ["Quad lab", "Partition", "Circle", "Prove"], grades_label
  "Grade 10".

## Screens and modes
Header (kit, 9-12 theme): title "Coordinate Proof Lab", subtitle "Measure it. Then name it." Modes `Quad lab`
(opens first), `Partition`, `Circle`, `Prove`. Kit buttons `Motion`, `Sound`, `Read`.
Layout: square plane left (x and y from −10 to 10, lattice dots at every whole number), panel right. Under 1000 px
wide the panel goes under the plane, name board first. Under 900 px tall the measuring table scrolls inside the
panel; the plane and the name board stay in view.

### Quad lab (sandbox)
- Quadrilateral ABCD with four handles snapping to lattice points (or half points with `Snap ½`). Starts as P1.
- Measuring table (panel): sides AB, BC, CD, DA and diagonals AC, BD, each with d² (a whole number), exact length
  (simplest radical form: "√17", "2√5", "8") and decimal, slope as a reduced fraction ("1/4", "−5/2", "0",
  "undefined") and midpoint. Below: perimeter (like radicals combined: "4√17 ≈ 16.49"; otherwise the decimal) and
  area by the shoelace formula, exact.
- Name board: Parallelogram, Rectangle, Rhombus, Square, Trapezoid, Isosceles trapezoid, Kite, each with a light
  (on or off) and, when on, the one-line reason ("Both pairs of opposite sides have equal slopes").
- `Marks` layer: equal sides get the same number of tick marks, parallel sides the same number of arrows, right
  angles a small square. All marks come from exact arithmetic, never from how it looks.
- If two sides cross, the fill turns hatched warn and the board says "Sides cross: not a quadrilateral. No name
  applies." All lights go off.
- `Load` picks a preset: P1 to P5 and the Bowtie (Content).
### Partition
- Segment AB (handles, start A(−2, 1), B(7, 7)) and a ratio m:n (steppers 1 to 5 each, start 2:1). `Predict`:
  tap where the point P should go, then `Show` draws P and the slope staircase: the run and rise split into m + n
  equal steps, m of them from A. Readout: P = A + m/(m+n) × (B − A), each coordinate as an exact fraction.
- A miss shows the distance from your tap to P in grid units; within 0.25 counts as on it.
### Circle
- Center handle and a rim handle (both on lattice points). The equation updates live in two forms:
  (x − h)² + (y − k)² = r² and the expanded x² + y² + Dx + Ey + F = 0. The radius shows exact (√r² simplified).
- A test point handle: readout "(x − h)² + (y − k)² = 20, and r² = 25: not on the circle (inside)".
- `Complete the square`: choose one of five general forms (Content); steps reveal one at a time: group x and y
  terms, add (D/2)² and (E/2)² to both sides, factor, read the center and r². The last step draws the result,
  including the two odd cases (a single point, and no points at all).
### Prove
- Card list on the panel; each card loads its points (locked) and a claim ("ABCD is a rhombus"). Tap cells of the
  measuring table (one length, one slope or one midpoint) to put them in the proof tray, each counting as one
  measurement; choose the conclusion, then `Check`. Checker: the tray must contain a sufficient set for the claim (rules below). The tray count shows next to
  the card when it passes; no par is given.

## Content
Presets and proof cards (all values recomputed exactly):
- P1 A(1,1) B(5,2) C(6,6) D(2,5): rhombus, not a rectangle. All sides √17; slopes 1/4, 4, 1/4, 4; diagonals AC
  (slope 1, d² 50) and BD (slope −1, d² 18) are perpendicular and share midpoint (7/2, 7/2); area 15.
- P2 A(−3,0) B(1,−2) C(4,4) D(0,6): rectangle. Sides 2√5 and 3√5 (slopes −1/2 and 2); diagonals both √65; area 30.
- P3 A(0,0) B(3,1) C(2,4) D(−1,3): square. Sides √10 (slopes 1/3, −3); diagonals both √20 = 2√5, slopes 2 and
  −1/2; area 10.
- P4 A(−4,−2) B(4,−2) C(2,3) D(−2,3): isosceles trapezoid. AB and CD slope 0 (lengths 8 and 4); legs √29 with
  slopes −5/2 and 5/2; diagonals both √61; area 30.
- P5 A(0,0) B(5,0) C(6,3) D(0,3): right trapezoid, not a parallelogram. AB ∥ CD (slope 0), BC slope 3, DA
  undefined; area 33/2 = 16.5.
- Bowtie A(0,0) B(4,3) C(4,0) D(0,3): AB = CD = 5 and BC = DA = 3, yet sides AB and CD cross. Card claim "ABCD is a
  parallelogram because both pairs of opposite sides are equal": the correct conclusion is `Not a quadrilateral`.
- T1 triangle A(1,2) B(4,6) C(8,3): AB = BC = 5, AC = √50 = 5√2; slopes 4/3 and −3/4 multiply to −1; right
  isosceles at B.
- C1 circle center (2,−1) through (5,3), r² = 25: (−1,−5) and (2,4) are on it; (6,1) gives 20, not on it.
Partition (A(−2,1), B(7,7)): 2:1 gives (4, 5); 1:2 gives (1, 3); 1:1 gives (5/2, 4); 3:2 gives (17/5, 23/5).
Complete the square, the five general forms:
1. x² + y² − 4x + 6y − 12 = 0: center (2, −3), r² 25, r 5.
2. x² + y² + 8x − 2y + 8 = 0: center (−4, 1), r² 9, r 3.
3. x² + y² − 2x + 4y + 5 = 0: r² 0, only the point (1, −2).
4. x² + y² + 2x + 10 = 0: r² = −9, no points at all.
5. x² + y² − 6x − 8y = 0: center (3, 4), r 5, through the origin.
Sufficient sets the checker accepts (each measurement = one table cell; "simple" is checked by the tool, free):
- Parallelogram: both pairs of opposite slopes equal; or both pairs of opposite sides equal; or one pair of
  opposite sides both parallel and equal; or the two diagonal midpoints equal.
- Rectangle: a parallelogram set plus one right angle (two adjacent slopes multiplying to −1, or one 0 and one
  undefined); or a parallelogram set plus equal diagonals.
- Rhombus: four equal sides; or a parallelogram set plus perpendicular diagonals; or a parallelogram set plus two
  equal adjacent sides.
- Square: a rhombus set plus a rectangle condition.
- Trapezoid (exclusive: exactly one pair of parallel sides): slopes of all four sides. Isosceles: plus equal legs.
- Right triangle: two slopes multiplying to −1, or three d² values with a² + b² = c².
- On the circle: the point's d² from the center equals r².

## Interactions in detail
- All measures are exact (integers and fractions); decimals are display only, 2 places. Lattice snap keeps every d²
  whole; with `Snap ½` the table shows quarters in d² and fractions in slopes.
- Handles can't land on another vertex (they stop one step short). A degenerate quadrilateral (three collinear
  corners) shows "Three corners in a line: a triangle with an extra point" and turns the lights off.
- Partition steppers keep m and n from 1 to 5; when A = B the readout says "A and B are the same point".
- Circle: the rim can't sit on the center; radius shows "√20 = 2√5 ≈ 4.47" for lattice rims off the axes.
- Prove: a wrong conclusion says which light is off and why; a too-small tray says what the tray already proves
  ("This shows a parallelogram. A rectangle needs one more fact."). Extra cells never fail a proof.
- Keyboard: Tab through handles; arrows move one lattice step; aria-valuetext "A at 1, 1". Table rows are buttons
  in Prove: each cell is a button (Enter adds or removes). Every readout has a text label, so screen readers hear the table.
- Reset per mode; the last Quad lab shape and passed cards last for the page session; nothing is saved.
- `window.__tool = {state, setMode, setPoints(pts), measure(), names(), card(id), tray(cells), check(),
  partition(m, n), circle(h, k, r2), general(i)}`.

## Look
Accent `--brand #ffc400` (surveyor's marker yellow, like stake flags on a plot plan), `--brand-ink #10161f`. Plane
on `--gr-bg` with lattice dots `#a6b3c4` and grid lines from the theme; the quadrilateral filled with the accent at
16%, outlined in the accent; handles `#e8edf3` with a dark ring; marks in the accent.
Contrast (computed): brand on --panel 10.84:1, on --sec-bg 10.27:1, on --gr-bg 11.46:1; brand-ink on brand
11.37:1; lattice dots on --gr-bg 8.60:1. Nearest 9-12 math accents are intersection-quest's #ffe14d and the golds
#f2a93b and #f0b650 (all clearly lighter or more orange); a jade first planned here was too close to
optimization-workshop's #2ff0b0.

## Art
none: drawn in code (plane, shapes, marks, preview.svg).

## Voice
Bank voice `hs-narrator` (Kore), style "Read clearly and naturally, at a moderate pace". Chosen because the bank's
other kept voices are either on grade 9 to 11 math neighbors or are K-2 teachers (warm-teacher, bright-teacher).
`Curio.voice`, `scope: () => state.mode`.
- wQuad (how): "Drag the corners. The table measures every side, slope and diagonal for you."
- wPart (how): "Set a ratio, then tap where you think the point lands."
- wCircle (how): "Drag the center and the rim. Move the test point to see if it's on the circle."
- wProve (how): "Tap the measurements your proof needs, pick the conclusion, then tap Check."
- proved (event, Check passes; stale on the next card): "That's a complete proof."
- notYet (event, Check finds a gap; stale when the tray changes): "Not enough yet. One thing is still unproven."
- crossed (event, a drag makes two sides cross; stale when they uncross): "The sides cross. That isn't a quadrilateral any more."

## Family engine
coordinate (`kit/coordinate.js`, inlined after `kit:curio` and `kit:graphing`; built on the graphing `Plane`). This
spec holds the full description for the family; two-rule-race (gr 5 simulator, 5.OA.B.3) and sea-search-grid
(gr 5 cards, 5.G.A) reuse it.
- `Frac`: exact fractions, the same API as `kit/balance.js` (`Frac(3, 4)`, `.add .sub .mul .div .neg .cmp .eq
  .toString({decimal})`). Proposed: move it to `Curio.Frac` in kit/curio.js so balance, coordinate and probability
  share one copy (see Open questions).
- `Rad`: exact square roots of whole numbers and fractions. `Rad.of(n)` → `{k, r}` with k√r simplest
  (`Rad.of(20)` → 2√5), `.fmt()` with a true radical sign, `.approx`; `Rad.sum([...])` combines like radicals.
- `Coord` (pure functions on `[x, y]` pairs of numbers or Fracs): `dist2(a, b)`, `dist(a, b)` (a Rad),
  `slope(a, b)` (a Frac, or null for undefined), `midpoint(a, b)`, `partition(a, b, m, n)`, `area(poly)`
  (shoelace, absolute, exact), `perimeter(poly)`, `parallel(s1, s2)`, `perpendicular(s1, s2)`, `collinear(a, b, c)`,
  `simple(poly)` (no two non-adjacent sides cross or touch), `quad(poly)` → `{simple, convex, parallelogram,
  rectangle, rhombus, square, trapezoid, isoTrapezoid, kite, reasons: {...}}` (trapezoid exclusive by default,
  `{trapezoid: 'inclusive'}` switches), `circle({h, k, r2})` with `.has(p)`, `.general()` → `{D, E, F}`,
  `Coord.fromGeneral(D, E, F)` → `{h, k, r2}` (r2 may be 0 or negative), `Coord.proves(claim, cells)` (the
  sufficient-set checker above), `Coord.steps(a, b)` → `{dx, dy, taxi: |dx| + |dy|, d: Rad}`.
- `CoordPlane(svgGroup, opts)`: a `Plane` with `quadrant: 'all' | 'first'`, `range`, lattice dots, `snap: 1 | 0.5`,
  and `poly(points, {closed, labels: 'ABCD', draggable, fill, onChange})` (handles from `g.point`, 44 px targets,
  never two on one spot), `marks(poly)` (ticks, arrows, right-angle squares from exact tests), `pointAt(p, {label,
  hidden})`, `plotPairs(pairs, {connect, icon})`.
- `RuleTable(container, {rules: [{name, start, step} | {name, f}], n})`: a table of terms for two rules side by side
  and `pairs()` → corresponding terms as ordered pairs.
- Fixed by the engine: lattice look, handle style, vertex labels, mark style, number formats (true minus sign,
  reduced fractions with a slash, "undefined" for vertical slopes, radicals simplest first then a decimal).
- What each sibling feeds it: two-rule-race: first quadrant 0 to 30, RuleTable with two "start and add" rules, the
  pairs plotted as snail positions (`plotPairs` with a snail icon), no polygons. sea-search-grid: first quadrant 0 to
  10, hidden points (`pointAt` hidden), `Coord.steps` for "3 steps over, 2 up" feedback in whole steps, no radicals.
  This tool: all four quadrants, polygons, Rad, `quad`, `partition`, `circle`, `proves`.

## Sources
- G-GPE text: Common Core State Standards for Mathematics, High School Geometry, Expressing Geometric Properties with Equations, https://www.thecorestandards.org/Math/Content/HSG/GPE/
- Grade 5 sibling codes: CCSS 5.OA.B.3 and 5.G.A, https://www.thecorestandards.org/Math/Content/5/
- Distance and midpoint formulas, the circle equation and completing the square: OpenStax, Intermediate Algebra 2e, 11.1 "Distance and Midpoint Formulas; Circles", https://openstax.org/books/intermediate-algebra-2e/pages/11-1-distance-and-midpoint-formulas-circles
- Slopes of parallel and perpendicular lines: OpenStax, College Algebra 2e, 4.1 "Linear Functions", https://openstax.org/books/college-algebra-2e/pages/4-1-linear-functions
- Area from coordinates: Wikipedia, "Shoelace formula", read 2026-10-27, https://en.wikipedia.org/wiki/Shoelace_formula
- Exclusive and inclusive trapezoid definitions: Wikipedia, "Trapezoid", Definitions section, read 2026-10-27, https://en.wikipedia.org/wiki/Trapezoid
- Every preset, partition and circle value above was recomputed exactly in Python with fractions (2026-10-27).

## Done when
1. P1 shows four sides √17, slopes 1/4 and 4, diagonal slopes 1 and −1, area 15; Rhombus on, Rectangle off.
2. P2 lights Rectangle and Parallelogram only; diagonals both √65; area 30.
3. P3 lights Square, Rectangle, Rhombus and Parallelogram; P5 lights Trapezoid only (area 16.5).
4. The Bowtie shows sides 5, 3, 5, 3, hatched warn and no names; its card accepts only `Not a quadrilateral`.
5. Partition 3:2 gives (17/5, 23/5); 1:1 gives (5/2, 4).
6. Circle center (2,−1) with rim (5,3) shows (x − 2)² + (y + 1)² = 25 and x² + y² − 4x + 2y − 20 = 0; the test point at (6,1) reads 20, not on it.
7. General forms 3 and 4 end in "only the point (1, −2)" and "no points".
8. A P2 rectangle proof with only the four side lengths fails with the "one more fact" line (it proves a parallelogram); adding the two diagonal lengths passes.
9. Keyboard alone can move every handle and build a proof; every size in STANDARDS.md keeps the plane and the name board visible without page scrolling.
10. Console clean, no network, no em dashes, "Curio Class" only in full.

## Open questions
- Trapezoid uses the exclusive definition (exactly one pair of parallel sides), so a parallelogram is not a
  trapezoid. Keep, or use the inclusive one some curricula prefer?
- G-GPE.A.2 (parabola from focus and directrix) is left to Conic Focus Finder (grade 12). OK, or add a parabola mode
  here?
- Move the exact `Frac` into kit/curio.js as `Curio.Frac`, shared by balance, coordinate and probability?
- Voice is hs-narrator, which already speaks for many tools; the only unused kept voices are K-2 teachers. OK?
