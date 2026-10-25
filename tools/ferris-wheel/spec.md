# Ferris Wheel

## One idea
The wheel and the graph are the same thing seen two ways: drag the car on the wheel or the dot on the graph and the other one follows, so radius, hub height, speed and boarding point become amplitude, midline, period and phase in your hands.

## Not like
- function-family-reunion: sliders on abstract parent functions; here every parameter is a physical part of a wheel you can see, and the graph is grown by riding, not drawn at once.
- imaginary-island: rotation as multiplying by i on a complex-plane map; here rotation is a real ride, measured in meters and seconds, and radians are arc lengths.
- rollercoaster-polynomials: you shape a track from zeros; here the shape is fixed (a circle) and you only change the wheel, so the graph is always a sinusoid.
- polar-rose-studio: polar equations as art; here there is one circle and the point is height over time, not the curve itself.
- circle-theorem-explorer: angle relationships inside circles; here the circle moves in time and is unrolled into a graph.
- speedometer (and other simulators): a car on a position graph shows the derivative; here nothing is differentiated, the link is circle to sine.

## Who and how
Grade 11, math (Algebra 2 / precalculus, module "Trigonometric Functions"). Driver: students (own laptops), also fine on a projector. 15-30 minutes. Standards: F-TF.A (radian measure as arc length, unit circle), F-TF.B (model periodic phenomena with amplitude, frequency, midline), F-TF.C (Pythagorean identity sin squared plus cos squared equals 1).

Look: 9-12 dark instrument panel. Link `kit:curio`, then `kit:theme-912`. Tool accent `--brand` a warm amber (#f2a93b or close, must pass AA on the theme panel). No confetti, no mascot.

## Screens and modes
Header: title "Ferris Wheel", mode buttons (`.seg`) **Ride**, **Unit Circle**, **Real Wheels**, **Match**; icon buttons **Motion**, **Sound**, **Read** (ids `motion`, `sound`, `read`). Ride is the default.

Layout in every mode: stage on the left split into two panes side by side, the wheel (left) and the graph (right), with the car height drawn as a thin horizontal dashed "height line" from the car across to the graph's current dot. Panel on the right: sliders, readouts, buttons, `hint` paragraph. Below about 900 px wide, the wheel stacks above the graph.

### Ride (explore, default)
- Wheel: drawn in code. Ground line at height 0, support legs, hub, rim, 12 spokes, 8 cars evenly spaced, one rider car highlighted in the accent color (outlined, with a bold label "you"). Height scale on the left edge in meters.
- Graph (kit/graphing `Plane`): x axis "time (s)" 0 to 120, y axis "height (m)" 0 to 100. Fixed axes in this mode so slider changes are visible as changes in shape.
- Sliders (kit/graphing `g.slider`): **Radius** 2 to 40 m, step 1, default 15. **Hub height** 3 to 60 m, step 1, default 18. **Time for one turn** 10 to 120 s, step 5, default 40.
- Choice buttons: **Board at** with **Bottom** (default), **Right side**, **Top**, **Left side**. **Turn** with **Counterclockwise** (default), **Clockwise**.
- Clock buttons: **Play** / **Pause** (one button that toggles its label), **Restart**, **Speed 1x** / **Speed 4x** (toggle).
- Toggles: **Show sideways distance** (off), **Show arc traveled** (off).
- Keep buttons: **Keep this graph** (saves the current full curve as a dashed ghost, up to 3, each labeled with its equation), **Clear kept**.
- Readouts (monospace, from the theme): t in s; angle from start in radians (as a multiple of pi when it is a multiple of pi/12, else decimal) and degrees; arc traveled in m; height h in m; sideways distance x from the hub in m (only when that toggle is on); rim speed in m/s.
- Equation line under the graph, always visible and updated live (see Interactions).

### Unit Circle
- Wheel becomes the unit circle: radius 1, hub at the origin, axes through the hub, no ground or legs. Rim marked at every pi/6 and pi/4 with labels in radians (0, pi/6, pi/4, pi/3, pi/2, ... 2pi).
- Graph: x axis "angle (radians)" 0 to 4pi, ticks every pi/2 labeled "pi/2, pi, 3pi/2, 2pi, 5pi/2, 3pi, 7pi/2, 4pi"; y axis "height" -1.2 to 1.2. The curve plotted is sin(theta).
- Car starts at angle 0 (3 o'clock), turns counterclockwise.
- Buttons: **Play** / **Pause**, **Restart**, **Step pi/6**, **Step pi/4**, **One radian**, **Unroll the arc**, **Show cosine** (toggle).
- Readouts: theta in radians and degrees, sin theta, cos theta, arc length (equals theta, shown as "arc = theta x radius = theta"), and the identity line "cos squared + sin squared = 1.000" computed live to 3 decimals.

### Real Wheels
- A list of 4 wheel buttons: **Chicago 1893**, **London Eye**, **Singapore Flyer**, **High Roller**. Choosing one sets the wheel to scale and shows its fact card (name, city, year, published height, published diameter, cars, time for one turn).
- Graph: x axis "time (min)" 0 to 70, y axis "height (m)" 0 to 180, the same for all four so wheels can be compared. **Keep this graph** and **Clear kept** work here too, so a student can overlay all four.
- Clock: **Play** / **Pause**, **Restart**, **Speed 60x** (default) / **Speed 300x**.
- A 10 m scale bar beside the wheel. No sliders in this mode; a **Try it in Ride** button copies the wheel into Ride (clamped to Ride ranges, with a note when clamped).
- Readouts as in Ride plus rim speed in m/s and in km/h.

### Match (optional challenge)
- A dashed target curve (color `--gr-2`, dashed) on the Ride axes, labeled "Target 1 of 8". The student's wheel starts at the Ride defaults.
- Same sliders and Board at / Turn buttons as Ride. Buttons: **Check**, **Show my curve** (plots the full curve at once without riding), **Next target**, **Previous target**, **Reveal equation**.
- No score, no timer. A match shows "Matched. Your wheel draws this graph." and a quiet chime; the target turns solid.

## Content

### Real wheels (Real Wheels mode)
Model note shown on every fact card: "Model: the car rides a circle with the published diameter, and the top of the circle is at the published height. Real cars hang below or outside the rim, so true heights differ by a few meters."

| Button | Fact card | Model radius r | Hub height D = H - r | Lowest point H - 2r | Time for one turn P |
|---|---|---|---|---|---|
| Chicago 1893 | Ferris Wheel, World's Columbian Exposition, Chicago, opened June 21, 1893. 80.4 m (264 ft) tall, 76.2 m (250 ft) across, 36 cars, up to 60 riders each. One nonstop turn: about 9 minutes. | 38.1 m | 42.3 m | 4.2 m | 9 min |
| London Eye | London, opened to the public March 2000. 135 m tall, 120 m across, 32 capsules. One turn: about 30 minutes. | 60 m | 75 m | 15 m | 30 min |
| Singapore Flyer | Singapore, opened April 2008. 165 m tall, 150 m across, 28 capsules. One ride: about 32 minutes (treated as one turn). | 75 m | 90 m | 15 m | 32 min |
| High Roller | Las Vegas, opened March 31, 2014. 167.6 m (550 ft) tall, 158.5 m (520 ft) across, 28 cabins. One turn: about 30 minutes. | 79.25 m | 88.35 m | 9.1 m | 30 min |

Rim speed is computed, never quoted: v = 2 pi r / P. (London Eye: 2 x pi x 60 / 1800 = 0.21 m/s.) All four turn counterclockwise in the model, boarding at the bottom.

### Match targets (Ride axes, 0 to 120 s)
| # | Hub D | Radius r | P (s) | Board at | Turn | Note shown after match |
|---|---|---|---|---|---|---|
| 1 | 20 | 15 | 60 | Bottom | either | Midline 20, amplitude 15, period 60. |
| 2 | 30 | 25 | 40 | Bottom | either | A faster, bigger wheel: three full turns fit. |
| 3 | 20 | 10 | 30 | Top | either | Starting at the top flips the graph: it opens with a maximum. |
| 4 | 45 | 40 | 120 | Bottom | either | One slow turn fills the whole window. |
| 5 | 25 | 20 | 60 | Right side | Counterclockwise | From the side, the height starts at the midline and rises. |
| 6 | 25 | 20 | 60 | Right side | Clockwise | Same wheel, other direction: now it starts down. |
| 7 | 15 | 12 | 20 | Bottom | either | Period 20 means six turns in two minutes. |
| 8 | 50 | 8 | 90 | Left side | Counterclockwise | A small wheel on a tall tower: tiny amplitude, high midline. |

### Hints (panel `hint`, per mode)
- Ride: "Press Play to ride. Drag the car around the wheel, or drag the dot along the graph. Then change the wheel and ride again."
- Unit Circle: "Radius 1. The height of the car is the sine of the angle. Press One radian to see how big a radian is."
- Real Wheels: "Pick a wheel. All four use the same axes, so keep each graph to compare them."
- Match: "Change the wheel until your curve lands on the dashed one. Press Show my curve to see it all at once."

### Ride equation display
Angle in standard position: theta measured from the hub's 3 o'clock, counterclockwise positive. Start angle theta0: Bottom = -pi/2, Right side = 0, Top = pi/2, Left side = pi. Angular speed w = 2pi/P, negative for Clockwise.
- Main line: `h(t) = D + r sin(2pi t / P + theta0)` with numbers in, and for Clockwise `h(t) = D + r sin(-2pi t / P + theta0)`. theta0 printed as -pi/2, 0, pi/2 or pi (term dropped when 0).
- Second line, only when it applies: boarding at Bottom shows "same as h(t) = D - r cos(2pi t / P)" (true for both directions); Top shows "same as h(t) = D + r cos(2pi t / P)".
- Third line, labels: "midline D m, amplitude r m, period P s".

## Interactions in detail
- **Two-way link (the core).** When paused: drag the rider car along the rim (pointer, or arrow keys when the car has focus; Left/Down = back, Right/Up = forward along the direction of turn) and the clock time t is set to match; the graph dot moves to (t, h). Drag the graph dot (kit/graphing `g.trace`) along the time axis and the car moves to the matching spot. Dragging snaps to multiples of pi/12 of turn when Shift is held or with keyboard steps. While playing, dragging pauses first.
- **Riding.** Play advances t at 1x or 4x real seconds (60x/300x in Real Wheels). The curve is drawn only up to the current t (the trace "grows"); ahead of t nothing is drawn. When t reaches the window end (120 s, 70 min, 4pi), the clock pauses and the hint says "The graph is full. Press Restart to ride again."
- **Changing a slider or Board at / Turn** while riding or paused: the car jumps to its new position for the same t, and the drawn trace is redrawn from 0 to t with the new wheel (the old trace is not kept unless Keep this graph was pressed). The equation updates on every input event.
- **Ground clearance.** The hub can never be lower than radius + 1 m. Raising Radius past that raises Hub height with it (the hub slider moves) and the hint shows "Hub raised so the cars clear the ground." Lowering Hub height below radius + 1 stops at radius + 1.
- **Extremes.** Radius 40, hub 60: top at 100 m (top of axis). Period 10 s: 12 turns in the window; the curve must stay smooth (engine adaptive sampling). Period 120 s: exactly one turn.
- **Show sideways distance** adds x(t) = r cos(angle) as a second curve on the graph (color `--gr-3`, dash pattern) on its own small axis "sideways from hub (m)" -40 to 40 drawn under the main graph, plus a horizontal bar on the wheel from hub to car. A live line reads "x squared + (h - D) squared = r squared" with numbers, for example "8.8 squared + 12.1 squared = 15.0 squared".
- **Show arc traveled** paints the rim arc from the boarding point to the car (accent, thick), wrapping past one turn with a count "turns: 1.25".
- **Unit Circle buttons.** Step pi/6 and Step pi/4 move the car exactly that much (pause first). **One radian** draws a straight rod of length 1 from the hub along the radius, then (animated about 1.5 s, instant when Motion is off) bends it onto the rim from the car's position, marking an arc of 1 radian with the label "1 radian, about 57.3 degrees", then shows "about 6.28 of these fit around: that is 2pi". **Unroll the arc** lifts the painted arc from 0 to theta off the rim and lays it flat on the graph's x axis from 0 to theta (animated about 1.5 s), showing that the x coordinate of the graph dot is the arc length. **Show cosine** adds cos(theta) as a dashed curve and a horizontal bar on the circle.
- **Keep this graph** stores the full curve (0 to window end) of the current wheel, drawn dashed with its equation as a label at its right end. A 4th keep replaces the oldest. Kept graphs belong to their mode; switching modes hides them, switching back shows them.
- **Match.** Check compares the student's curve to the target at 241 sample times over 0 to 120 s; matched if every difference is at most 0.5 m. So any equivalent wheel matches (for example Clockwise for a Bottom target). Not matched: "Not yet. Biggest gap: 6.2 m near t = 35 s." with a small marker at that spot. Reveal equation shows the target's equation in the Ride format.
- **Motion off** (body.calm): no animated rotation easing, the One radian and Unroll animations jump to their end state, Play still advances the clock (it is the content, not decoration) but the car moves in steps of 0.25 s instead of smooth frames.
- **Sound** (off by default per kit): a soft tick each time the rider passes the top or bottom, and `Curio.yes()` on a Match.
- **Restart** sets t = 0, car to the boarding point, clears the growing trace (kept graphs stay), stops speech. Switching modes stops the clock and speech.
- Reading order for screen readers: equation line and readouts are an `aria-live="polite"` region updated at most once per second while playing.

## Art
- river-night-sky: a calm city riverbank skyline at night seen from far away, deep navy sky with faint stars, dark water reflecting a few warm lights, no people, no wheel, no fairground, low contrast so drawings read on top; 16:9; cutout no; people no. (Changed at the spec check: rollercoaster-polynomials already uses a fairground at dusk.) Used faintly behind the wheel pane in Ride and Match only.

Everything else (wheel, cars, ground, graph, unit circle, scale bar) is drawn in code.

## Voice
Bank `hs-narrator`, voice `Kore`, style "Read clearly and naturally, at a moderate pace". Spoken only on first entry to a mode (once per session) and when Read is pressed.
1. ride-welcome: "Welcome aboard. Press Play and watch your height turn into a graph as the wheel goes around."
2. ride-drag: "You can also drag the car around the wheel, or drag the dot along the graph. They always move together."
3. ride-change: "Now change the radius, the hub height, or the time for one turn, and ride again. Watch which part of the graph changes."
4. ride-board: "Try boarding from the side instead of the bottom. Does the graph start the same way?"
5. unit-welcome: "This is the unit circle. The radius is one, so the height of the car is exactly the sine of the angle."
6. unit-radian: "One radian is the angle you get when the arc along the rim is as long as the radius."
7. unit-unroll: "Unrolling the arc lays it flat on the axis. The distance along the axis is the angle in radians."
8. unit-cosine: "The sideways distance is the cosine. Cosine squared plus sine squared is always one."
9. real-welcome: "These are real wheels, drawn to scale. All four share the same axes, so you can compare them."
10. real-period: "The big wheels take about half an hour to turn once. The first Ferris wheel, in 1893, took about nine minutes."
11. match-welcome: "Here is a target graph. Change the wheel until your curve lands on top of it."
12. match-yes: "Matched. Your wheel draws that graph."
13. match-full: "The graph is full. Press Restart to ride again."

13 lines. Read in any mode reads that mode's hint (readFallback).

## Family engine
Family: none, but the tool plots functions, so it reuses `kit/graphing.js` (built by rollercoaster-polynomials to `docs/families/graphing.md`): `Plane` for all graphs, `g.fn` for the riding trace (with `domain: [0, t]`), target and kept curves (dashed), `g.trace` for the draggable graph dot, `g.slider` for the three sliders, `g.label` for kept-curve equations. Colors `--gr-1` (your curve), `--gr-2` (target), `--gr-3` (sideways or cosine), `--gr-4` (kept). The wheel, the unit-circle drawing, the rod and unroll animations are the tool's own SVG, positioned with `g.px` where they touch the graph. If the engine lacks something needed (for example a trace that can be dragged on the time axis only), add it to the engine and its doc in the same change, per the family rules.

## Sources
- Chicago 1893 wheel: height 80.4 m (264 ft), 36 cars, up to 60 people each, nine-minute nonstop rotation, opened June 21, 1893: Wikipedia, "Ferris Wheel (1893)", https://en.wikipedia.org/wiki/Ferris_Wheel_(1893); height also Guinness World Records "First Ferris wheel", https://www.guinnessworldrecords.com/world-records/first-ferris-wheel/
- Chicago 1893 diameter 250 ft (76.2 m): commonly cited (Wikipedia "List of Ferris wheels", https://en.wikipedia.org/wiki/List_of_Ferris_wheels); the 1893 article itself does not state it. Builder must confirm against one more source.
- London Eye: 135 m tall, 120 m diameter, 32 capsules, about 30 minutes per turn, public opening 9 March 2000: Wikipedia, "London Eye", https://en.wikipedia.org/wiki/London_Eye (its quoted 26 cm/s does not match 2 pi x 60 / 1800 = 0.21 m/s, so the tool computes speed and does not quote it).
- Singapore Flyer: 165 m tall, 150 m diameter, 28 capsules, opened 15 April 2008, ride about 32 minutes: Wikipedia, "Singapore Flyer", https://en.wikipedia.org/wiki/Singapore_Flyer
- High Roller: 167.6 m (550 ft) tall, 158.5 m (520 ft) diameter, 28 cabins, about 30 minutes per turn, opened March 31, 2014: Wikipedia, "High Roller (Ferris wheel)", https://en.wikipedia.org/wiki/High_Roller_(Ferris_wheel)
- 1 radian = 180/pi degrees, about 57.2958; 2pi about 6.2832; sin squared plus cos squared equals 1: standard definitions, Common Core F-TF.A.1, F-TF.A.2, F-TF.C.8 (http://www.corestandards.org/Math/Content/HSF/TF/).

## Done when
1. Ride defaults (r 15, D 18, P 40, Bottom, Counterclockwise): pressing Play grows a curve with minimum 3 m at t = 0, maximum 33 m at t = 20 s, back to 3 m at t = 40 s; equation reads h(t) = 18 + 15 sin(2pi t / 40 - pi/2) and "same as h(t) = 18 - 15 cos(2pi t / 40)".
2. Paused, dragging the car a quarter turn moves the graph dot to t = 10 s, h = 18 m; dragging the graph dot to t = 30 s puts the car at the opposite side. Arrow keys do the same with visible focus.
3. Bottom start gives the identical curve for Clockwise and Counterclockwise; Right side start gives different curves (one rises, one falls).
4. Raising Radius to 40 with Hub at 18 pushes Hub to 41 and shows the clearance note; Hub can never go below radius + 1.
5. Unit Circle: Step pi/6 three times shows theta = pi/2, sin 1.000, cos 0.000; One radian marks an arc labeled about 57.3 degrees; Unroll the arc lands the arc's end on the graph dot's x position; the identity line always reads 1.000.
6. Real Wheels: London Eye shows lowest 15 m, top 135 m, period 30 min, rim speed 0.21 m/s; keeping all four graphs shows four labeled dashed curves on one set of axes.
7. Match: target 1 is matched by r 15, D 20, P 60 from Bottom in either direction; target 6 is not matched by the target 5 wheel; a miss reports the biggest gap and where.
8. Motion off: One radian and Unroll jump to their end state, Play still advances; Sound off makes no ticks.
9. Each mode speaks its welcome line once on first entry after a tap; Read speaks the mode hint; mode switch stops speech and the clock.
10. Usable at 375 px wide (wheel above graph) and in a 16:10 iframe; no network requests; no em dashes in any text.
