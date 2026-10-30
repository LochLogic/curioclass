# Intersection Quest

## One idea
Every system on the course can be solved down three lanes (Graph, Substitute, Eliminate), and you race a ghost of
your own best time, so the race teaches the choice: whole-number crossings are fastest by graph, a lone y makes
substitution quick, matching coefficients make elimination quick, and a 13/6 answer makes the graph lane crawl.

## Not like
- two-trains (gr 8, graphing): one system as two trains on a railroad, dragged, no timer, the three solution cases as stories. Here no scenario: a timed course of systems and a choice of method for each, including line and curve systems and half-planes.
- graph-story-lab and launch-pad (gr 9, graphing, same group): one function's features, and one quadratic's roots in a flight. Here two equations at once.
- model-my-world (gr 9, same group): writes constraints for a situation. Here constraints are given and shaded.
- equation-golf (gr 9, same group): one variable, fewest moves. Here two variables, fastest time.
- motion-graph-match (gr 11, race): matches a motion graph against the clock. Same race format; nothing else shared.

## Who and how
- Grade 9, Algebra 1, Systems of Equations. Students drive. 15 to 35 minutes (a course takes 3 to 8 minutes).
- Topic line: "solving systems by graphing, substitution and elimination".
- Standards (module): A-REI.C (C.5 elimination keeps the solutions, C.6 linear systems, C.7 a line and a quadratic or circle), A-REI.D (D.10 a graph is all solutions, D.11 crossings are where f(x) = g(x), D.12 half-planes and systems of inequalities).
- CCSS clusters: Lines course serves A-REI.C.5 and C.6; Curves course C.7 and D.11; Shade course D.12; Practice lap D.10.
- tool.json: driver "students", minutes "15-35", modes ["Practice lap", "Race"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "Three roads to one crossing." Modes `Practice lap` (opens first), `Race`. Kit buttons.
Layout: plane left, lane panel right; the timer and ghost bar across the top of the stage in Race. Under 900 px tall
the lane panel stays beside the plane (compact); at 760 wide it goes under the plane with the lane buttons first.

### Practice lap (explore)
Focus: the plane with both graphs and their crossings, center stage and the largest thing on it.
Type two equations (`Equation 1`, `Equation 2`, forms y = mx + b, ax + by = c, y = ax² + bx + c, x² + y² = r²) or
drag the line handles (two points per line). The plane draws both; a hover or focus point reads (x, y) and
"on line 1: yes / no, on line 2: yes / no" (every point on a graph solves its equation). The crossing points are
marked with exact coordinates. No clock.

### Race
Focus: the plane with the current system, center stage; the lane panel beside it; the thin timer and ghost bar above.
Course picker: three course cards with painted pictures (art: course-lines, course-curves, course-shade) named
`Lines` (7 systems), `Curves` (4), `Shade` (2). `Start` begins the clock. For each system, the equations appear;
pick a lane:
- `Graph`: both graphs drawn; drag the crosshair and press `This is it` (once per crossing on two-crossing systems).
  Zoom buttons `+` `−` halve or double the view around the crosshair, and the crosshair's snap halves or doubles
  with the view (0.25 at the start view, then 0.125, 0.0625, 0.03125). For "No crossing" or "Same line", buttons
  with those names.
- `Substitute`: tap a variable term in one equation to solve for it (the tool shows the rearranged equation,
  fractions exact); press `Substitute` and the tool shows the one-variable equation simplified to ax = b or
  ax² + bx + c = 0; type the value(s) of that variable, then the other variable's value(s).
- `Eliminate` (Lines course only): two multiplier steppers (−6 to 6, not 0), one per equation; the sum row shows
  live; `Add` is enabled when one variable's coefficient is 0; then type the remaining variable, then the other.
  A 0 = 0 sum is "Same line"; 0 = nonzero is "No crossing" (buttons appear).
A wrong answer adds 10 s and says which part is wrong; you may switch lanes at any time (the clock runs on).
Ghost bar: a small painted race car (art: race-car) for you and the same car, gray and see-through, for your best run
on this course, both moving along the system list in real time.
End card over the dimmed finish line (art: finish-line): total time, penalties, the time per system with the lane
used, and a "Your lanes" table across runs this session (average seconds per lane per course). Best time per course
saved on this device (localStorage `curio-intersection-quest`, try/catch) with `Clear times`.

### Shade course
Focus: the plane with the boundary being set and the shading.
Each inequality: drag two points to set the boundary (or type it), choose `Solid` or `Dashed`, then tap the side
to shade. A test point (0, 0) is shown with its check after you shade. System 13 needs all three shadings, then a
pin dropped anywhere in the overlap.

## Content
Lines course (answer; the quick lane):
1. y = 2x + 1; y = −x + 7. (2, 5). Graph or Substitute.
2. x + y = 10; x − y = 4. (7, 3). Eliminate (add).
3. 3x + 2y = 16; 5x − 2y = 0. (2, 5). Eliminate (add: 8x = 16).
4. y = 3x − 4; 2x + 5y = 14. (2, 2). Substitute (17x = 34).
5. 4x + 3y = 10; 2x − 3y = 3. (13/6, 4/9). Eliminate (6x = 13); the graph lane needs two zooms.
6. y = 0.5x + 3; y = 0.5x − 1. No crossing (parallel).
7. 6x − 2y = 8; y = 3x − 4. Same line (every point on it).
Curves course:
8. y = x² − 4; y = x + 2. (3, 5) and (−2, 0). x² − x − 6 = 0.
9. x² + y² = 25; y = x + 1. (3, 4) and (−4, −3). x² + x − 12 = 0.
10. y = x² + 1; y = 2x. (1, 2), one touching point. x² − 2x + 1 = 0.
11. y = x²; y = −1. No crossing.
Shade course:
12. y > 2x − 3: dashed boundary, shade above; (0, 0) is a solution.
13. x + y ≤ 6, y ≥ x, x ≥ 0: solid boundaries; the overlap is the triangle with corners (0, 0), (3, 3), (0, 6).
The order of systems in a course is fixed (so the ghost compares fairly).

## Interactions in detail
- All algebra is exact (fractions). Typed answers accept integers, fractions "13/6", and terminating decimals that
  equal the exact value; a repeating value needs a fraction (the tip says so: "13/6 doesn't end as a decimal").
- Two-answer systems accept the pairs in any order, typed one pair at a time; each x is followed by its y.
- Graph lane accepts a crosshair within 0.05 of the exact point in both coordinates, then prints the exact point.
  For system 5 that takes the 0.0625 snap (two zooms): the nearest 0.125 point is 0.056 off in y.
- Substitute lane: solving for a variable with coefficient ±1 is one tap; otherwise the tool divides and shows the
  fractions (allowed, slower to read). On the Curves course, substitution into the circle expands (x + 1)².
- Elimination: the sum row is k1·(eq 1) + k2·(eq 2); a note under it: "Adding equal things to equal things keeps
  every solution" (A-REI.C.5).
- Shade: boundary line must pass within 0.1 of two points of the true line; solid vs dashed must match ≤/≥ vs
  </>; the shaded side is checked with the test point. Pin in the overlap checked exactly.
- Timer: starts on `Start`, stops on the last answer; Motion off keeps the clock and replaces the ghost's motion
  with a number ("Ghost: system 4").
- The clock and ghost never block input: lane buttons, the crosshair, steppers and boxes act at once while they run.
- Keyboard: lanes are buttons; the crosshair moves with arrow keys (one snap step, Shift 4 steps); steppers with arrow
  keys.
- `window.__tool = {state, setMode, course(id), lane(name), answer(text), time()}`.

## Look
Accent `--brand #ffe14d` (race-flag yellow), `--brand-ink #231c00`. Plane on `--gr-bg` with `--gr-1` and `--gr-2`
for the two equations (solid and dashed); crossings marked with a ring and a label; the ghost car at 40% opacity and
grayscale with a `#a6b3c4` outline; penalties in `--warn` with a "+10 s" label. The course cards and the end card are
the only painted surfaces; the plane stays plain for reading. Contrast (computed): brand on panel 13.29:1, on
--sec-bg 12.60:1, on --gr-bg 14.06:1, brand-ink on brand 13.03:1. Minimal celebration: a new best shows "New best"
in text.

## Art
Local FLUX (`scripts/localart.py`); no people. One style: dusk road views from above, painted illustration.
- course-lines: "Two straight desert highways crossing at a four-way junction, seen from above at dusk, painted
  illustration"; 16:9; cutout no; people no; the Lines course card.
- course-curves: "A winding mountain road curving across a straight railway line, seen from above at dusk, painted
  illustration"; 16:9; cutout no; people no; the Curves course card.
- course-shade: "Farm fields split by straight fences into green and gold patches, seen from above at dusk, painted
  illustration"; 16:9; cutout no; people no; the Shade course card.
- race-car: "A small yellow toy race car with a blank white number plate, side view, painted illustration, plain
  white background"; 16:9; cutout yes; people no; your marker and (grayed) the ghost on the ghost bar.
- finish-line: "A checkered finish line banner stretched across a race track between two posts, the banner blank
  above the checks, dusk light, painted illustration"; 16:9; cutout no; people no; behind the end card, dimmed.
The plane, graphs, crosshair, shading, steppers, timer and preview.svg are drawn in code (graphs and controls).

## Voice
Bank voice `upbeat-guide` (bright, clear). Not used by math 9-12 neighbors, group siblings or batch specs.
`Curio.voice`, `scope: () => state.mode + ':' + state.course`. Equations and tips are read on screen; Read speaks the
hint.
- wPractice (how; Practice lap entered; stale after the first edit or drag): "Type two equations or drag their handles. Every crossing is a solution to both."
- wRace (how; Race entered; stale on Start): "Pick a course card and press Start. For each system, tap a lane: Graph, Substitute or Eliminate."
- graphLane (how; first Graph lane; stale on the first This is it): "Drag the crosshair onto the crossing, then press This is it. Press plus to zoom if it falls between grid points."
- subLane (how; first Substitute lane; stale on Substitute): "Tap a variable in one equation to solve for it. Then press Substitute."
- elim (how; first Eliminate; stale on Add): "Set the multipliers until one variable cancels. Then press Add."
- shade (how; Shade course starts; stale after the first shading): "Drag two points to set the boundary, tap Solid or Dashed, then tap the side to shade."
- wrong (event; wrong answer; stale on the next system): "Not quite. Ten seconds added."
- finish (event; course done; stale on Start): "Course complete. Look at which lane was fastest for each system."
- best (event; new best time; stale on Start): "New best time."

## Family engine
graphing (`kit/graphing.js`, docs/families/graphing.md), unchanged API. Uses `Plane` (ticks 'axis', ranges per
system), `g.fn` for lines and parabolas, `g.param` for the circle, `g.point` for line handles (draggable, snap) and the
crosshair (snap set per zoom, keyboard), `g.intersect` only as a cross-check of the exact answers, `g.view` for zoom,
`g.label`, `g.clear`. Half-plane shading is the tool's own polygon in the `back` layer clipped to the plane. The
lane panel, timer and ghost are the tool's own.

## Sources
- A-REI.C and A-REI.D: Common Core State Standards for Mathematics, High School Algebra, Reasoning with Equations and Inequalities, https://www.thecorestandards.org/Math/Content/HSA/REI/
- Systems by graphing, substitution and elimination; one, none or infinitely many solutions: OpenStax, Elementary Algebra 2e, chapter 5 (5.1 to 5.3), https://openstax.org/books/elementary-algebra-2e/pages/5-2-solving-systems-of-equations-by-substitution
- Nonlinear systems (line with parabola or circle): OpenStax, College Algebra 2e, 7.3 "Systems of Nonlinear Equations and Inequalities", https://openstax.org/books/college-algebra-2e/pages/7-3-systems-of-nonlinear-equations-and-inequalities-two-variables
- Graphing linear inequalities and systems: OpenStax, Elementary Algebra 2e, 4.7 and 5.6, https://openstax.org/books/elementary-algebra-2e/pages/5-6-graphing-systems-of-linear-inequalities
- Checks run (Python with sympy, 2026-10-29): all 11 systems solved exactly and match Content (system 6 no
  solution, system 7 one equation, system 11 only complex roots). Shade 13 corners (0, 0), (3, 3), (0, 6). Graph
  lane on system 5 (13/6, 4/9): the nearest snap point is off by 0.083 and 0.056 at snap 0.25, 0.042 and 0.056 at
  0.125, 0.021 and 0.007 at 0.0625, so it passes the 0.05 rule only after two zooms. The first draft kept the snap
  at 0.25 while zooming, so system 5 could never pass by graph; the snap now halves with each zoom. 2.17 is 0.0033
  from 13/6 and is refused because it is not exact.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. System 5 by Eliminate (k1 = 1, k2 = 1) gives 6x = 13; typing 13/6 then 4/9 is right; typing 2.17 is refused with the fraction tip.
2. System 4 by Substitute: tapping y in equation 1 then Substitute shows 17x = 34; (2, 2) is right.
3. System 6 by Eliminate (1, −1) gives 0 = 4 and `No crossing` is right; system 7 gives 0 = 0 and `Same line`.
4. System 9 accepts (3, 4) and (−4, −3) in either order; system 10 accepts the single point (1, 2); system 11 `No crossing`.
5. Graph lane accepts (2.0, 5.0) on system 1 and refuses (2.25, 5) with a hint; system 5 passes by graph after two zooms and not before.
6. Shade 12 requires dashed and the upper side; Shade 13's pin inside the triangle passes, outside fails.
7. A wrong answer adds 10 s; best time per course survives a reload; `Clear times` works; the ghost car runs on the second try.
8. Focus: at 1366x768 and 1000x625 the plane is the largest thing on the stage in both modes.
9. Tap while it plays: with the clock and ghost running, a lane button, a crosshair key or a stepper acts at once.
10. Every size in STANDARDS.md keeps the plane, the lane buttons and the timer visible; keyboard-only completes the Lines course; no voice line names a disabled control; console clean, no network.
