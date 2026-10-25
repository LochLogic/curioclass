# Motion Graph Match

## One idea
You drive a cart down a track live, controlling only one of position, velocity or acceleration, and watch all three
graphs draw themselves at once, so you feel that each graph is the slope of the one above it (and the area under the
one below it) before anyone writes it down.

## Not like
- story-graphs (grade 8, graphing): matches written stories to one graph shape and lets you sketch. Here nothing is
  matched by reading or drawing; you produce the graph with real-time motion, in real units, on three linked graphs.
- graph-story-lab (grade 9, graphing): labels features of static real graphs. Here the graphs are live and generated
  by your own control input.
- two-trains (grade 8, graphing): two fixed lines and where they meet. Here there is one moving object and the link
  between its x, v and a graphs.
- intersection-quest (grade 9, graphing): races your best time solving a system. Here the race is against a ghost of
  your best run on a motion target, scored by how closely you track it.
- space-cargo (grade 11): F = ma with mass and surfaces as the game. Here mass is fixed; force is only a readout
  arrow, and the point is reading and making kinematics graphs.
- roller-coaster-physics (grade 11): energy conservation on a built track. No energy here.
- collision-lab (grade 11): momentum between two carts. Here one cart, no collisions (wall stops are just stops).

## Who and how
Grade 11, physics (Physical Science, Motion and Kinematics). Driver: students, alone or in pairs on laptops; also works
on a projector with a student at the keyboard. 15 to 30 minutes. Standards: HS-PS2-1 (the net force readout ties the
acceleration graph to F = ma; the core of the tool is the kinematics that the standard's data analysis rests on).

Look: links `kit:curio` then `kit:theme-912`. Own accent `--brand` a cyan (pass AA on the 9-12 panel). Pro-instrument
look like a motion-sensor lab readout. No confetti, no mascot.

## Screens and modes
Header: title, mode buttons `Explore` and `Race` (`.seg`), then Sound and Motion icon buttons from the kit.

Layout (both modes): top strip is the track scene; below it three stacked graphs sharing one time axis; right side is
the panel. On narrow screens the panel moves under the graphs.

- **Track scene:** a 10 m track drawn in code, tick marks every 1 m labeled 0 to 10, a motion sensor box at the 0 m end,
  end stops at 0 m and 10 m, the cart (a lab cart with wheels, drawn in code) and a net force arrow on the cart
  labeled in newtons (hidden when the force is under 0.05 N). In Race a ghost cart (outline only, dotted) runs too.
- **Graphs (top to bottom):** Position x (m), range 0 to 10. Velocity v (m/s), range -3 to 3. Acceleration a (m/s
  squared shown as "m/s²" on screen), range -2 to 2. Time axis 0 to 12 s on all three, gridlines every 1 s. Each graph
  has a live value readout on its right edge with units. A zero line is drawn heavier on v and a.
- **Control picker (panel, both modes):** three big buttons `Hand` (you set position), `Throttle` (you set velocity),
  `Pedal` (you set acceleration). The graph you control gets a small "you control this" tag and a brighter frame.
- **Control surface (panel):** Hand: no slider, drag the cart itself on the track. Throttle: a vertical slider labeled
  "velocity" from -3 to 3 m/s, step 0.1, with a center detent at 0. Pedal: a vertical slider labeled "acceleration"
  from -2 to 2 m/s², step 0.05, center detent at 0. Both sliders spring back to 0 on release only if `Spring back`
  (a checkbox under the slider, off by default) is on.

### Explore (opens first)
Free drive. The clock runs from 0 to 12 s while you drive, sweeping the graphs like a scope.
Panel buttons: `Go` / `Pause` (one toggle), `Clear` (wipes traces, clock to 0, cart stays where it is), `Show links`
(toggle), `Start at` (a small number field for the cart start, 0 to 10 m, default 1 m, applies on Clear).
At 12 s the clock stops and the run freezes so it can be read; `Go` starts a fresh sweep (traces clear).
- **Show links:** when on, a vertical time cursor follows the pointer across all three graphs (or arrow keys move it
  in 0.1 s steps when a graph has focus). At the cursor: a tangent segment on the x graph with its slope printed
  ("slope 1.20 m/s"), and the v graph value at that time ringed with the same number; a tangent on the v graph with
  slope printed and the a graph value ringed; the area under v from 0 to the cursor shaded (positive above the zero
  line, negative below, two different fill patterns, not color alone) with the label "area = change in x = 3.4 m" and
  the matching rise on the x graph bracketed. This works on a paused or finished run only.
- **Hint line** (one sentence in the panel, changes with control): Hand: "Drag the cart. The computer works out your
  velocity and acceleration." Throttle: "You set the speed and direction. Position is the running total." Pedal: "You
  set the push. Velocity builds up from it, and position from velocity."

### Race
Pick a target, then match it. Panel shows the target list (10 cards, below), each with its name, which graph it is on,
a tiny thumbnail of the target curve drawn in code, and your best match percent per control if any.
Selecting a card: the target appears dashed on its graph (other graphs empty), the cart jumps to the target's start
position at rest, the suggested control is selected (you may change it), and the ghost of your best run for that
target and control is loaded if one exists.
Buttons: `Start` (3, 2, 1 countdown shown on the track, then a 12 s run), `Stop` (ends early, scores what is done as a
run of 12 s with the rest counted as misses), `Try again`, `Next target`.
During the run: your trace draws solid over the dashed target; a shaded tolerance band hugs the target; the readout on
the target graph shows "in band" or "off by 0.6 m" live. The ghost trace (dotted) and ghost cart play in step.
After the run, a results box: Match percent (time inside the band), RMS error with units, your best for this target and
control, and a plain line: "New best" or "Best stays 87 percent". Buttons in the box: `Show all three` (draws the
target's other two graphs dashed, computed from the target, so you can see what you should have done on them),
`Replay` (replays your run and the ghost at normal speed with the cart), `Try again`, `Next target`.
A small "hard way" tag appears on the card and results when the control is two steps from the target graph (Pedal on a
position target, Hand on an acceleration target).

## Content
Constants: track 0 to 10 m; run 12 s; cart mass 2.0 kg (force readout F = m a, in N); speed limit 3 m/s; Hand and
Throttle changes in velocity are rate-limited to 2 m/s² so the a graph stays on scale.
Tolerance bands: position plus or minus 0.4 m; velocity plus or minus 0.25 m/s; acceleration plus or minus 0.15 m/s².

Targets (t in s, x in m, v in m/s, a in m/s²; all start at rest at x0 unless the target itself says otherwise):
1. **Wait, then walk** (position, Hand suggested). x0 = 2. x = 2 for 0 to 3; rises steadily to 8 from 3 to 9
   (v = 1); x = 8 for 9 to 12.
2. **Out and back** (position, Hand). x0 = 1. x rises from 1 to 7 from 0 to 6 (v = 1), falls back to 1 from 6 to 12
   (v = -1).
3. **Fast, then slow** (position, Throttle). x0 = 1. x from 1 to 7 over 0 to 4 (v = 1.5), then 7 to 9 over 4 to 12
   (v = 0.25).
4. **Steady cruise** (velocity, Throttle). x0 = 1. v ramps 0 to 1 over 0 to 1; v = 1 from 1 to 7; ramps to 0 from 7 to
   8; v = 0 to 12. (Ends at x = 8.)
5. **Speed up, cruise, brake** (velocity, Throttle). x0 = 1. v ramps 0 to 1.5 over 0 to 3 (a = 0.5); v = 1.5 from 3 to
   5; ramps to 0 from 5 to 8 (a = -0.5); v = 0 to 12. (Ends at x = 8.5.)
6. **Turnaround** (velocity, Pedal). Starts at x0 = 4 already moving at v = 1.5 (the run gives the cart this starting
   velocity; the card says "starts moving"). v = 1.5 - 0.5 t from 0 to 6 (goes from 1.5 through 0 at t = 3 to -1.5);
   v = -1.5 + 0.5 (t - 6) from 6 to 9 (back to 0); v = 0 from 9 to 12. (Farthest point x = 6.25 at t = 3; ends at
   x = 1.75.) Card note: "The cart stops for an instant at 3 s. Is the acceleration zero there?"
7. **Steady push** (acceleration, Pedal). x0 = 1. a = 0.2 from 0 to 5; a = 0 from 5 to 7; a = -0.2 from 7 to 12.
   (v peaks at 1; ends at rest at x = 8.)
8. **Back up and stop** (acceleration, Pedal). x0 = 8. a = -0.2 from 0 to 5; a = 0 from 5 to 7; a = 0.5 from 7 to 9;
   a = 0 from 9 to 12. (v reaches -1, then returns to 0 at 9 s; ends at x = 2.5.)
9. **Smooth arrival** (position, Pedal). x0 = 1. x = 1 + 0.125 t² from 0 to 4 (reaches 3 m at 1 m/s); x = 3 + (t - 4)
   from 4 to 8; x = 7 + (t - 8) - 0.125 (t - 8)² from 8 to 12 (ends at 9 m at rest). Hidden a is 0.25, 0, -0.25.
10. **Two trips** (velocity, Throttle). x0 = 3. v ramps 0 to 1 over 0 to 0.5; v = 1 to 3; ramps to 0 by 3.5; v = 0 to
    6; ramps to -1 by 6.5; v = -1 to 10; ramps to 0 by 10.5; v = 0 to 12. (Goes 3 to 6 m, then back to 2 m.)

For targets defined by v or a, the tool computes the other graphs by integrating from x0 (and the starting velocity for
target 6); for position targets it differentiates analytically per piece. Kinks in a position target (targets 1 to 3)
have no defined acceleration there; `Show all three` draws a as steps with open gaps at the kinks and the note "a jumps
here: a real cart needs a sudden large push".

## Interactions in detail
- **Simulation:** fixed step 1/60 s; samples stored every 0.05 s (240 per run) for x, v, a and force.
- **Hand:** the cart follows the pointer's track position (clamped 0 to 10 m) but its speed is capped at 3 m/s and its
  velocity change rate at 2 m/s², so a fast flick makes the cart lag behind the pointer. v is the change in x over the
  last 0.15 s; a is the change in that smoothed v over the last 0.3 s. Releasing the cart leaves it where it is
  (v goes to 0 through the rate limit). Keyboard: Left and Right arrows move at 1 m/s while held, with Shift at
  0.3 m/s.
- **Throttle:** the slider sets the wanted v; actual v moves toward it at up to 2 m/s²; x integrates v. Up and Down
  arrows change it by 0.1 m/s, Page Up and Page Down by 0.5, Home sets 0.
- **Pedal:** the slider sets a; v integrates a and clamps at plus or minus 3 m/s (the a readout then shows 0 and the note
  "top speed"); x integrates v. Up and Down change it by 0.05, Page Up and Page Down by 0.25, Home sets 0.
- **End stops:** reaching 0 m or 10 m stops the cart: x clamps, v becomes 0, and the a graph gets a small triangle mark
  "end stop" instead of a huge spike (the spike is clipped at the graph edge). In Pedal mode, pushing into a stop keeps
  the cart parked and the force arrow shows the push with the note "the end stop pushes back".
- **Off scale:** any value past a graph's range is drawn clipped at the edge with a small arrow marker.
- **Switching control mid-run:** allowed in Explore (the trace keeps going, a small tick on the time axis marks the
  switch). Locked during a Race run (picker greys out until the results show).
- **Changing mode or target** stops any speech, any run and any replay; the cart goes to the new start.
- **Ghost:** best run per target and control saved in localStorage key `curio-mgm-best` (try/catch; works without it).
  A `Forget my bests` link at the bottom of the target list clears it after a confirm.
- **Score:** match percent = share of the 240 samples inside the band, rounded to a whole percent. RMS error printed to
  two decimals with units. Ties keep the older best.
- **Motion off:** the cart, ghost and traces still move (they are the data), but the countdown numbers do not zoom and
  graphs do not animate in; replays run at normal speed.
- **Reset:** `Clear` in Explore; `Try again` in Race. Reloading the page returns to Explore, Hand, cart at 1 m.

Code note: keep the simulation, smoothing, scoring and target math in one clearly marked block
(`/* ==== MOTION ENGINE (lift to a forces kit later) ==== */`). If `kit/graphing.js` exists at build time, use its
`Plane` for the three graph axes and `g.fn` for dashed targets, with live traces as polylines placed by `g.px`;
otherwise draw the axes in the tool's own SVG.

## Art
- track-bench: a dark lab bench surface, brushed aluminum air track rail along its length, soft overhead light, no
  text, no people or hands; aspect 5:1; cutout no; people no.
Everything else (cart, sensor, end stops, graphs, thumbnails, arrows) is drawn in code.

## Voice
Bank `hs-narrator`, voice `Kore`, style "Read clearly and naturally, at a moderate pace". 9 lines:
1. explore-welcome: "Drive the cart and watch three graphs draw at once: position, velocity and acceleration."
2. hand: "Hand control. Drag the cart. Its velocity and acceleration are worked out from how you move it."
3. throttle: "Throttle control. You set the velocity. Position is the running total of it."
4. pedal: "Pedal control. You set the acceleration. Velocity builds up from it, then position from velocity."
5. links: "Move across a finished run. The slope of each graph is the value of the one below it."
6. race-welcome: "Pick a target graph and match it as closely as you can. Your best run comes back as a ghost."
7. go: "Three, two, one, go."
8. hard-way: "This is the hard way. You control a graph two steps away from the target."
9. turnaround: "Watch the moment the cart turns around. Its velocity is zero, but is its acceleration?"
Lines 1 and 6 play on first entering each mode (after the first tap); 2 to 4 on picking a control the first time;
5 on first turning on Show links; 7 with the countdown; 8 on starting a hard-way run the first time; 9 on first
selecting target 6. Results are read on screen, not spoken.

## Family engine
none (family field is empty). Optional reuse of `kit/graphing.js` for axes only, as in the code note above.

## Sources
- Definitions of displacement, velocity, acceleration, slopes and areas of motion graphs, constant-acceleration
  equations: OpenStax, University Physics Volume 1, chapter 3 "Motion Along a Straight Line",
  https://openstax.org/books/university-physics-volume-1/pages/3-introduction
- Same at high school level: OpenStax, Physics (high school), chapter 2 "Motion in One Dimension",
  https://openstax.org/books/physics/pages/2-introduction
- F = m a for the force readout: OpenStax, University Physics Volume 1, section 5.3 "Newton's Second Law",
  https://openstax.org/books/university-physics-volume-1/pages/5-3-newtons-second-law
- Standard: NGSS HS-PS2-1, https://www.nextgenscience.org/pe/hs-ps2-1-motion-and-stability-forces-and-interactions
- Misconceptions targeted (zero velocity read as zero acceleration, graph as picture of the path): McDermott,
  Rosenquist and van Zee, "Student difficulties in connecting graphs and physics", American Journal of Physics 55,
  503 (1987); Beichner, "Testing student interpretation of kinematics graphs", American Journal of Physics 62, 750
  (1994).
- All target values are original and derived from the piecewise definitions above (check: integrate each to the
  stated end position).

## Done when
1. Explore opens with Hand control; dragging the cart from 1 m to 7 m and stopping draws a rising x trace, a v bump,
   and an a trace that goes positive then negative.
2. Throttle held at 1.0 m/s for 5 s gives a flat v line at 1.0 and an x line rising 5 m (readouts agree within 0.1).
3. Pedal held at 0.2 m/s² from rest for 5 s gives a flat a line, v rising to 1.0 m/s, and x rising about 2.5 m
   (curved); the force arrow reads 0.4 N.
4. Driving into the 10 m end stop stops the cart, sets v to 0 and shows an "end stop" mark, not a spike.
5. Show links on a finished run: the tangent slope printed on x matches the ringed v value, and the shaded v area
   matches the bracketed change in x, within 0.1.
6. Race: every one of the 10 targets loads, starts the cart at its x0 (target 6 already moving at 1.5 m/s), and each
   v or a target's `Show all three` ends at the end position stated in Content.
7. A run that sits still on target 1 scores about 28 percent (inside the band only for the first 3.4 s); a careful run
   scores over 80 percent; the results show match percent and RMS error with units.
8. A second run on the same target and control shows the first best as a ghost trace and ghost cart; a better score
   replaces it and survives a reload; `Forget my bests` clears it.
9. Everything works by keyboard alone (control picker, sliders, Hand arrows, Go, Start, results buttons) with visible
   focus; no color-only signals (target dashed, ghost dotted, yours solid).
10. Text has no em dashes; at 375 px wide the panel stacks under the graphs with no sideways scroll.
