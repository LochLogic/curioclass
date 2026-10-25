## A 5-minute start

1. Open **Ride** (radius 15 m, hub 18 m, one turn in 40 s, boarding at the bottom). Press **Play**. The graph grows as you ride: lowest 3 m at t = 0, highest 33 m at t = 20 s, back to 3 m at t = 40 s.
2. Press **Pause** and drag the car a quarter turn. The graph dot jumps to t = 10 s, h = 18 m: halfway up is the midline. Now drag the dot to t = 30 s and watch the car swing to the other side.
3. Change one slider at a time and ride again. Ask which part of the equation h(t) = 18 + 15 sin(2πt / 40 − π/2) changed, and which part of the graph.

## The four modes

- **Ride** (explore): the wheel and the graph are linked both ways. Sliders for radius (2 to 40 m), hub height (3 to 60 m, always at least radius + 1 so the cars clear the ground) and time for one turn (10 to 120 s); **Board at** Bottom, Right side, Top or Left side; **Turn** counterclockwise or clockwise. **Show sideways distance** adds x(t) = r cos(angle) on a small graph under the main one, with the live check x² + (h − D)² = r². **Show arc traveled** paints the rim and counts turns. **Keep this graph** saves up to 3 dashed curves with their equations.
- **Unit Circle**: radius 1, so the height is sin θ. **Step π/6** and **Step π/4** move exact amounts. **One radian** bends a radius-length rod onto the rim (about 57.3 degrees; about 6.28 fit around). **Unroll the arc** lays the arc from 0 to θ flat on the graph's axis, ending under the graph dot. **Show cosine** adds cos θ. The identity line always reads 1.000.
- **Real Wheels**: Chicago 1893, London Eye, Singapore Flyer and High Roller drawn to one scale (10 m bar) on shared axes (0 to 70 min, 0 to 180 m). Keep all four to compare. Rim speed is computed, v = 2πr / P. **Try it in Ride** copies a wheel into Ride, clamped to Ride's ranges (all four are bigger and slower than Ride allows, and the note says so).
- **Match** (optional): eight target graphs. Change the wheel until your curve lands on the dashed one; **Check** compares 241 times from 0 to 120 s and accepts any gap up to 0.5 m, so an equivalent wheel counts (from the bottom, either direction matches). A miss names the biggest gap and marks it. No score, no timer.

## Talk about it

- Which slider changes the midline, which the amplitude, which the period? Which changes nothing about the shape?
- Why do Bottom-counterclockwise and Bottom-clockwise give the same graph, but Right side does not?
- Why is h(t) = 18 + 15 sin(2πt / 40 − π/2) the same as h(t) = 18 − 15 cos(2πt / 40)?
- A radian is "about 57.3 degrees". Where does that number come from? Why does 2π of them fit around?
- The London Eye moves at about 0.21 m/s. Why can you barely feel it move, even though it is huge?

## Good to know

- Model: h(t) = D + r sin(θ0 + ωt), ω = 2π / P (negative for clockwise), θ0 = −π/2, 0, π/2 or π for Bottom, Right side, Top, Left side. Angles are measured from the hub's 3 o'clock, counterclockwise positive.
- Checked values: Ride defaults give 3 m, 33 m at t = 20 s, 18 m at t = 10 s and t = 30 s, rim speed 2.36 m/s. London Eye: lowest 15 m, top 135 m, 30 min, 0.21 m/s (0.75 km/h). Chicago 1893: lowest 4.2 m, top 80.4 m, 9 min, 0.44 m/s.
- Real wheel model: the car rides a circle with the published diameter, top at the published height. Real cars hang below or outside the rim, so true heights differ by a few meters (the fact card says so). Singapore Flyer's 32 minutes is one ride, treated as one turn.
- Chicago 1893: height 80.4 m (264 ft), 36 cars, up to 60 riders each, one nonstop turn about 9 minutes, opened June 21, 1893 (Wikipedia, "Ferris Wheel (1893)"). The 250 ft (76.2 m) diameter is not in that article; it is confirmed by Guinness World Records ("First Ferris wheel", 76 m / 250 ft) and JSTOR Daily ("The Big Wheel", 250 feet in diameter). Guinness gives 40 passengers per car (40 seats); Wikipedia gives up to 60 people with 40 chairs, which the card follows.
- The London Eye's own page quotes 26 cm/s, which does not match 2π × 60 / 1800 = 0.21 m/s; the tool computes speed and never quotes it.
- Unit Circle: the graph's x axis is in radians at its own scale, so the unrolled arc is drawn shorter on the graph than on the circle; its end lands exactly under the graph dot.
- Keyboard: Tab to the car or the graph dot; arrows turn the wheel by π/12 (15 degrees, a 24th of a turn): Left and Down go back, Right and Up go forward. Hold Shift while dragging to snap to the same steps. With Motion off, Play still runs but moves in 0.25 s steps, and One radian and Unroll jump to their end.
- Sound plays a soft tick at the top and bottom of each turn and a chime on a match. Narration says each mode's welcome once; Read speaks the current hint.
- Standards: F-TF.A (radians as arc length, unit circle), F-TF.B (periodic models: amplitude, frequency, midline), F-TF.C (sin² + cos² = 1).
