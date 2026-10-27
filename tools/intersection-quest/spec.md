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
Type two equations (`Equation 1`, `Equation 2`, forms y = mx + b, ax + by = c, y = ax² + bx + c, x² + y² = r²) or
drag the line handles (two points per line). The plane draws both; a hover or focus point reads (x, y) and
"on line 1: yes / no, on line 2: yes / no" (every point on a graph solves its equation). The crossing points are
marked with exact coordinates. No clock.

### Race
Course picker `Lines` (7 systems), `Curves` (4), `Shade` (2). `Start` begins the clock. For each system, the
equations appear; pick a lane:
- `Graph`: both graphs drawn; drag the crosshair (snap 0.25, zoom buttons `+` `−` that halve or double the view
  around the crosshair) and press `This is it`. For "No crossing" or "Same line", buttons with those names.
- `Substitute`: tap a variable term in one equation to solve for it (the tool shows the rearranged equation,
  fractions exact); press `Substitute` and the tool shows the one-variable equation simplified to ax = b or
  ax² + bx + c = 0; type the value(s) of that variable, then the other variable's value(s).
- `Eliminate` (Lines course only): two multiplier steppers (−6 to 6, not 0), one per equation; the sum row shows
  live; `Add` is enabled when one variable's coefficient is 0; then type the remaining variable, then the other.
  A 0 = 0 sum is "Same line"; 0 = nonzero is "No crossing" (buttons appear).
A wrong answer adds 10 s and says which part is wrong; you may switch lanes at any time (the clock runs on).
Ghost bar: your best run on this course as a second marker moving along the system list in real time.
End card: total time, penalties, the time per system with the lane used, and a "Your lanes" table across runs this
session (average seconds per lane per course). Best time per course saved on this device (localStorage
`curio-intersection-quest`, try/catch) with `Clear times`.

### Shade course
Each inequality: drag two points to set the boundary (or type it), choose `Solid` or `Dashed`, then tap the side
to shade. A test point (0, 0) is shown with its check after you shade. System 2 needs all three shadings, then a
pin dropped anywhere in the overlap.

## Content
Lines course (answer; the quick lane):
1. y = 2x + 1; y = −x + 7. (2, 5). Graph or Substitute.
2. x + y = 10; x − y = 4. (7, 3). Eliminate (add).
3. 3x + 2y = 16; 5x − 2y = 0. (2, 5). Eliminate (add: 8x = 16).
4. y = 3x − 4; 2x + 5y = 14. (2, 2). Substitute (17x = 34).
5. 4x + 3y = 10; 2x − 3y = 3. (13/6, 4/9). Eliminate (6x = 13); the graph lane needs zoom.
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
- Substitute lane: solving for a variable with coefficient ±1 is one tap; otherwise the tool divides and shows the
  fractions (allowed, slower to read). On the Curves course, substitution into the circle expands (x + 1)².
- Elimination: the sum row is k1·(eq 1) + k2·(eq 2); a note under it: "Adding equal things to equal things keeps
  every solution" (A-REI.C.5).
- Shade: boundary line must pass within 0.1 of two points of the true line; solid vs dashed must match ≤/≥ vs
  </>; the shaded side is checked with the test point. Pin in the overlap checked exactly.
- Timer: starts on `Start`, stops on the last answer; Motion off keeps the clock and replaces the ghost's motion
  with a number ("Ghost: system 4").
- Keyboard: lanes are buttons; the crosshair moves with arrow keys (0.25, Shift 1); steppers with arrow keys.
- `window.__tool = {state, setMode, course(id), lane(name), answer(text), time()}`.

## Look
Accent `--brand #ffe14d` (race-flag yellow), `--brand-ink #231c00`. Plane on `--gr-bg` with `--gr-1` and `--gr-2`
for the two equations (solid and dashed); crossings marked with a ring and a label; ghost marker `#a6b3c4`
outlined; penalties in `--warn` with a "+10 s" label. Contrast (computed): brand on panel 13.29:1, on --sec-bg
12.60:1, on --gr-bg 14.06:1, brand-ink on brand 13.03:1. Minimal celebration: a new best shows "New best" in text.

## Art
none: drawn in code.

## Voice
Bank voice `upbeat-guide` (bright, clear). Not used by math 9-12 neighbors or group siblings.
- wPractice (how, Practice lap welcome): "Type two equations or drag their handles. Every crossing is a solution to both."
- wRace (how, Race welcome): "Pick a course and press Start. For each system, choose a lane: Graph, Substitute or Eliminate."
- elim (how, first Eliminate): "Set the multipliers until one variable cancels, then press Add."
- shade (how, Shade course starts): "Set the boundary, choose solid or dashed, then tap the side to shade."
- wrong (event, wrong answer; stale on the next system): "Not quite. Ten seconds added."
- finish (event, course done; stale on Start): "Course complete. Look at which lane was fastest for each system."
- best (event, new best time; stale on Start): "New best time."

## Family engine
graphing (`kit/graphing.js`, docs/families/graphing.md), unchanged API. Uses `Plane` (ticks 'axis', ranges per
system), `g.fn` for lines and parabolas, `g.param` for the circle, `g.point` for line handles (draggable, snap) and the
crosshair (`snap: 0.25`, keyboard), `g.intersect` only as a cross-check of the exact answers, `g.view` for zoom,
`g.label`, `g.clear`. Half-plane shading is the tool's own polygon in the `back` layer clipped to the plane. The
lane panel, timer and ghost are the tool's own.

## Sources
- A-REI.C and A-REI.D: Common Core State Standards for Mathematics, High School Algebra, Reasoning with Equations and Inequalities, https://www.thecorestandards.org/Math/Content/HSA/REI/
- Systems by graphing, substitution and elimination; one, none or infinitely many solutions: OpenStax, Elementary Algebra 2e, chapter 5 (5.1 to 5.3), https://openstax.org/books/elementary-algebra-2e/pages/5-2-solving-systems-of-equations-by-substitution
- Nonlinear systems (line with parabola or circle): OpenStax, College Algebra 2e, 7.3 "Systems of Nonlinear Equations and Inequalities", https://openstax.org/books/college-algebra-2e/pages/7-3-systems-of-nonlinear-equations-and-inequalities-two-variables
- Graphing linear inequalities and systems: OpenStax, Elementary Algebra 2e, 4.7 and 5.6, https://openstax.org/books/elementary-algebra-2e/pages/5-6-graphing-systems-of-linear-inequalities
- Every answer checked with exact fractions (2026-10-27).

## Done when
1. System 5 by Eliminate (k1 = 1, k2 = 1) gives 6x = 13; typing 13/6 then 4/9 is right; typing 2.17 is refused with the fraction tip.
2. System 4 by Substitute: tapping y in equation 1 then Substitute shows 17x = 34; (2, 2) is right.
3. System 6 by Eliminate (1, −1) gives 0 = 4 and `No crossing` is right; system 7 gives 0 = 0 and `Same line`.
4. System 9 accepts (3, 4) and (−4, −3) in either order; system 10 accepts the single point (1, 2); system 11 `No crossing`.
5. Graph lane accepts (2.0, 5.0) on system 1 and refuses (2.25, 5) with a hint.
6. Shade 12 requires dashed and the upper side; Shade 13's pin inside the triangle passes, outside fails.
7. A wrong answer adds 10 s; best time per course survives a reload; `Clear times` works; the ghost runs on the second try.
8. Every size in STANDARDS.md keeps the plane, the lane buttons and the timer visible; keyboard-only completes the Lines course; console clean, no network.
