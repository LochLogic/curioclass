# Launch Pad

## One idea
A foam ball fired straight up follows h(t) = −16t² + vt + h0, and every mission question ("when does it land?",
"when does it pass the drone?", "does it ever reach 80 feet?") is a quadratic equation you solve before you press
Launch; the flight then plays and the clock proves you right, so the four methods (factor, square root, complete the
square, formula) each earn their place, and a mission with no real answer shows a ball that never gets there.

## Not like
- rollercoaster-polynomials and ferris-wheel-trig (gr 11, graphing): design or read a curve's shape. Here one family, and the work is solving it for time.
- imaginary-island (gr 11): complex numbers on a plane. Here complex roots appear once, as the answer to "never reaches".
- graph-story-lab (gr 9, same group): reads many functions' features. Here one quadratic per mission, solved exactly.
- equation-golf (gr 9, same group): linear equations by moves. Cory's split: quadratic solving (A-REI.B.4) lives here.
- algebra-tile-studio (gr 9, same group): factors with tiles. Here factoring is one of four methods and the output is a time.

## Who and how
- Grade 9, Algebra 1, Quadratic Equations. Students drive. 20 to 40 minutes.
- Topic line: "solving quadratic equations by factoring, square roots, completing the square and the formula".
- Standards (module): A-REI.B.4 (4a completing the square and deriving the formula; 4b inspection, square roots, completing the square, the formula, factoring; complex solutions written a ± bi).
- CCSS cluster: A-REI.B in every mode; missions 1 to 4 serve 4b (factoring), 6 serves 4b (square roots), 7 serves 4a, 8 and 9 serve 4b (formula), 5 serves 4b (complex).
- tool.json: driver "students", minutes "20-40", modes ["Launch", "Missions"], grades_label "Grade 9".

## Screens and modes
Header: title, subtitle "Solve it first. Then fire." Modes `Launch` (opens first), `Missions`. Kit buttons.
Layout: left the launch scene (a tall column: ground, launcher, optional platform and drone, a height ruler in feet);
right a plane with h against t and the panel. A mission clock sits over the scene. Under 900 px tall the scene and
plane stay side by side with the scene narrowed; at 760 wide the scene sits above the plane, both shorter.

### Launch (explore)
Sliders `Speed v` (0 to 120 ft/s, step 4) and `Height h0` (0 to 100 ft, step 1), and `Launch`. The ball flies in
real time (Motion off: the path draws at once); the plane traces h(t). Readouts: the equation h(t) = −16t² + vt + h0,
the peak (time v/32 and height), and the landing time. A `Line at height` slider draws a horizontal line H on the
plane and lists when the ball is at H (two times, one, or "never").

### Missions
Nine missions in order (Content); each opens a card with the setup and the question. Steps:
1. `Write it`: the tool shows h(t) for the setup; the student sets the equation to solve by choosing the height
   (0 for landing, H for the drone) and the tool shows it in the form at² + bt + c = 0 after a `Tidy` button
   (dividing out a common factor when there is one, shown).
2. `Method` strip: `Factor`, `Square root`, `Complete the square`, `Formula`. Each opens a small work area:
   - Factor: two boxes for (t − p)(t − q); checked by expansion.
   - Square root: the tool isolates the square; the student types ± the root.
   - Complete the square: the student fills (t − k)² = m, then the roots.
   - Formula: the student fills a, b, c; the tool shows the discriminant b² − 4ac first (a box asks how many real
     answers it means), then the student types the roots.
   Any method that works is accepted; a method that can't be done cleanly (factoring mission 8) says so ("No whole
   number pair works. Try the formula.").
3. `Answer`: type the time(s) and choose which answer fits (a negative time is rejected with a reason).
4. `Launch`: the flight plays with the mission clock; at the student's time the clock stops and the ball's height
   shows; a ring flashes if it matches the mission event.
Completed missions saved on this device (localStorage `curio-launch-pad`, try/catch) with `Clear missions`.

## Content
All flights use g = 32 ft/s² (Earth's is about 32.17) and no air resistance; the card says "simple model: no air".
1. Speed 64, from the ground. When does it land? −16t² + 64t = 0, t = 0 or 4. Answer 4 s (0 is the launch).
2. Speed 64, from a roof 80 ft up. When does it land? −16t² + 64t + 80 = 0, t² − 4t − 5 = 0, t = 5 or −1. Answer 5 s.
3. Speed 64 from the ground, a drone hovers at 48 ft. When does the ball pass it? t² − 4t + 3 = 0, t = 1 and 3.
4. Speed 64 from the ground, drone at 64 ft. t² − 4t + 4 = 0, t = 2 (once: the peak just touches it).
5. Speed 64 from the ground, drone at 80 ft. t² − 4t + 5 = 0, t = 2 ± i. Never reaches; the ball tops out at 64 ft.
6. Dropped (speed 0) from a ledge 144 ft up. When does it land? 16t² = 144, t = 3.
7. Speed 48 from a 5 ft launcher. When does it land? 16t² − 48t − 5 = 0, completing the square: (t − 3/2)² = 41/16,
   t = (6 + √41)/4 ≈ 3.1008 s.
8. Speed 40 from a 6 ft launcher. When does it land? 8t² − 20t − 3 = 0, formula: t = (5 + √31)/4 ≈ 2.6419 s.
9. Speed 56 from a 4 ft launcher; a friend on a balcony at 40 ft catches it on the way down. When? 4t² − 14t + 9 = 0,
   t = (7 ± √13)/4 ≈ 0.8486 and 2.6514; answer 2.6514 s (the first is on the way up).

## Interactions in detail
- All algebra is exact: roots as integers, fractions, p ± √q forms reduced (√52 = 2√13), or a ± bi; decimals accepted
  within 0.01 of the exact value. The tool always shows the exact form after a right answer.
- Discriminant step: b² − 4ac > 0 two real, = 0 one, < 0 none real (two complex); the box checks the student's call.
- Complex answers: typed as 2 + i, 2 - i, or "2 ± i"; the readout notes the ball's peak is below the drone.
- Flight: positions from the exact formula each frame; the clock shows seconds to 0.01; the clock stops at the
  student's time and prints h at that time (which should be 0 or H).
- Launch mode lists times at a height H using the same solver, so it doubles as a checker.
- Keyboard: sliders with arrow keys; method buttons and boxes in Tab order; Enter submits a box.
- `window.__tool = {state, setMode, mission(n), method(name), answer(text), launch()}`.

## Look
Accent `--brand #ff7a5c` (signal coral), `--brand-ink #2a0c05`. The scene: a dark sky `#0e1520`, ground band
`#2a3340`, the ball a white circle with a coral trail, the drone a simple outline with a blinking light, a height
ruler in feet with ticks every 10. Plane curve `--gr-1`, line at H `--gr-2` dashed, root markers rings. Contrast
(computed): brand on panel 6.75:1, on --sec-bg 6.40:1, brand-ink on brand 7.10:1. Minimal celebration: a matched
mission shows "Mission complete" in text and the ring flash (none with Motion off).

## Art
One background, optional: FLUX (cfart) "open sports field at dusk, flat painted style, no people, no text,
wide view, dark sky", 1600x900, used dim behind the scene column; the tool works without it (plain sky color).
people: false.

## Voice
Bank voice `firm-captain` (mission control). Not used by math 9-12 neighbors or group siblings.
- wLaunch (how, Launch welcome): "Set the speed and height, then press Launch. Watch the curve it draws."
- wMissions (how, Missions welcome): "Each mission is one equation. Solve it, then launch to check."
- disc (how, first Formula method): "Check the discriminant first. It tells you how many answers to expect."
- neg (event, a negative time chosen; stale on next answer): "Negative time is before launch. Pick the other answer."
- never (event, mission 5 solved; stale on mission change): "No real answer. The ball never gets that high."
- done (event, a mission matches; stale on mission change): "Mission complete."

## Family engine
graphing (`kit/graphing.js`, docs/families/graphing.md), unchanged API. Uses `Plane` (t from 0 to the flight time
plus margin, h from 0 to the peak plus margin), `g.fn` for h(t), a horizontal `g.fn` for H, `g.roots` as a
cross-check of the exact answers, `g.extrema` for the peak, `g.trace` for the clock dot, `g.slider` for v and h0,
`g.label`. The scene column and exact-root solver are the tool's own.

## Sources
- A-REI.B.4: Common Core State Standards for Mathematics, High School Algebra, Reasoning with Equations and Inequalities, https://www.thecorestandards.org/Math/Content/HSA/REI/
- Projectile height h(t) = −16t² + v0t + h0 in feet: OpenStax, Elementary Algebra 2e, 10.6 "Solve Applications Modeled by Quadratic Equations", https://openstax.org/books/elementary-algebra-2e/pages/10-6-solve-applications-modeled-by-quadratic-equations
- Standard gravity 9.80665 m/s² (32.174 ft/s²): NIST, CODATA value "standard acceleration of gravity", https://physics.nist.gov/cgi-bin/cuu/Value?gn
- Methods (square root property, completing the square, quadratic formula, discriminant, complex solutions): OpenStax, Intermediate Algebra 2e, chapter 9, https://openstax.org/books/intermediate-algebra-2e/pages/9-3-solve-quadratic-equations-using-the-quadratic-formula
- Every mission root recomputed in Python (2026-10-27): 3.1008, 2.6419, 0.8486, 2.6514; mission 5 discriminant −4.

## Done when
1. Mission 2 by Factor (t − 5)(t + 1) passes; answering −1 is rejected with the before-launch reason; 5 passes and the flight lands at 5.00 s.
2. Mission 3 accepts 1 and 3 in either order; the flight clock stops at each with h = 48.
3. Mission 4's discriminant is 0 and the call "one" checks; mission 5's is −4 and 2 ± i is accepted; the flight peaks at 64 ft.
4. Mission 7 by Complete the square accepts (t − 3/2)² = 41/16 and (6 + √41)/4; 3.10 also passes.
5. Mission 8 by Factor shows the no-pair message; by Formula (5 + √31)/4 passes; 2.64 passes, 2.6 does not.
6. Mission 9 needs 2.6514 (or (7 + √13)/4) as the catch; choosing 0.8486 explains it is on the way up.
7. Launch mode: v = 64, h0 = 0, H = 48 lists t = 1 and 3; H = 80 lists "never".
8. Missions survive a reload; `Clear missions` works; Motion off draws paths at once; every size in STANDARDS.md keeps scene, plane and the mission card visible; console clean, no network.
