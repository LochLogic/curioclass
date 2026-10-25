# Collision Lab

## One idea
Every collision you set up on the air track keeps its total momentum while kinetic energy is free to vanish, and on the crumple bench the same change in momentum shows up as an impulse you can stretch thin or spike tall, so you design for low peak force.

## Not like
- crash-test-lab (grade 8): cars and Newton's third law told qualitatively with a "safer bumper"; here it is a quantitative lab with momentum and energy ledgers, a coefficient of restitution, a force-time graph with measured impulse, and engineering specs with numbers.
- space-cargo (grade 11): one object pushed with F = ma on different surfaces; here two bodies interact and the forces are internal, so nothing pushes from outside.
- tug-of-war-arena (grade 3): balanced and unbalanced forces with teams; no collisions, no momentum.
- motion-graph-match (grade 11): you move to match a given graph; here graphs are outputs of an experiment you ran, never targets to trace.
- roller-coaster-physics (grade 11): energy conservation along a track; here energy is the thing that is NOT conserved, and momentum is.
- field-lines (grade 11): forces at a distance in a sandbox; here forces act only during contact, measured over milliseconds.
- three-pigs-lab (grade 2, same format): material tests with a teacher-led K-2 story; this is a student-driven instrument bench with recorded data.

## Who and how
- Grade 11, science (physics). Module: Momentum and Collisions.
- Students drive on their own laptops, alone or in pairs. Works on a projector for a teacher demo.
- 30 to 45 minutes for a full run (Air Track, Crumple Zone, Notebook). Each mode stands alone for a 10 minute demo.
- Standards: HS-PS2-2 (mathematical representations show total momentum is conserved with no net external force), HS-PS2-3 (design, evaluate and refine a device that minimizes force on an object during a collision).
- Look: 9-12 dark instrument theme. Link `kit:curio`, then `kit:theme-912`. Tool accent `--brand` is a cool cyan (builder picks the exact value, AA contrast on the theme panel). Glider A and glider B each get their own color AND their letter printed on the glider and on every bar, so color is never the only signal. No confetti, no mascots, no scores.

## Screens and modes
Header: title "Collision Lab", subtitle "Momentum and collisions", mode buttons (`.seg`) **Air Track**, **Crumple Zone**, **Notebook**, then the kit buttons **Motion**, **Sound**, **Read**. Scene is a fixed 1440 x 810 design scaled with `Curio.fit`. Keyboard: Space = Launch, R = Reset (in the two bench modes, when focus is not in a text box).

### Air Track (default mode)
- On screen: a 2.00 m air track drawn in code (rail with air holes, a ruler with ticks every 0.10 m and labels every 0.50 m, end stops at 0 m and 2.00 m). Two gliders, A (left) and B (right), each 0.20 m long, with stacked mass plates and a printed mass label. A velocity arrow on each glider, labeled in m/s. A small center-of-mass marker (a triangle under the track) when **Show center of mass** is on.
- Below the track, the ledger: two rows, "Before" and "After". Each row has a momentum bar chart (bars for A, B and Total, drawn from a center zero line, left is negative, right is positive, value in kg·m/s on each bar) and a kinetic energy bar chart (A, B, Total, in joules). Under the ledger, one line: "Momentum: before 0.150 kg·m/s, after 0.150 kg·m/s. Kinetic energy kept: 50 percent."
- Panel (right): sliders **Mass A**, **Velocity A**, **Mass B**, **Velocity B**; bumper buttons **Spring**, **Rubber**, **Velcro**, **Custom**; a **Bounciness (e)** slider shown only for Custom; a **Presets** dropdown; toggles **Show center of mass**, **Ride with center of mass**, **Slow motion**, **Measurement noise**, **Predict**; buttons **Launch**, **Reset**, **Record run**. Hint paragraph `hint` with one line of guidance.
- What the person does: sets masses and velocities, drags the gliders to new start spots, picks a bumper, launches, watches, records.
- What responds: gliders slide, collide, separate or stick; the After row of the ledger fills in at the moment of contact; arrows update; Record run adds a row to the Notebook.

### Crumple Zone
- On screen: a short track ending in a rigid wall with a force sensor plate. One glider (G) with a nose on its front. The nose is drawn to scale (in cm, magnified view inset shows the nose crushing or compressing). Above it, a force-time graph: x axis "time (ms)", y axis "force (N)". The area under the current curve is shaded and labeled "impulse = 0.50 N·s". The last three runs stay as dashed ghost curves with their nose name at the peak.
- Readout strip: **Peak force** (N), **Contact time** (ms), **Average force** (N), **Crush used** (cm), **Impulse** (N·s), **Change in momentum** m(v after minus v before) (kg·m/s), **Speed after** (m/s, negative means it bounced back). Tags that appear when true: "Bounced", "Stopped", "Bottomed out".
- Panel: sliders **Glider mass**, **Impact speed**; nose buttons **Steel**, **Spring**, **Rubber**, **Crumple**; for Crumple only, sliders **Crush force** and **Crush length**; toggles **Lock graph axes**, **Slow motion**; buttons **Launch**, **Reset**, **Clear ghosts**, **Record run**, **Spec sheet**.
- Spec sheet (optional challenge): opens a card listing the four specs (see Content). Picking a spec sets the mass and speed and locks those two sliders; the card shows the limits and, after each launch, a plain line per limit, for example "Peak force 9.0 N, limit 10 N: met." When all limits pass, the card says "Spec met." with a check mark. Button **Leave spec** unlocks the sliders.

### Notebook
- Two tables: "Air Track runs" and "Crumple Zone runs" (columns in Content). Each has **Copy table** (tab separated with a header row and units, for pasting into a spreadsheet) and **Clear table**.
- Plot 1, "Total momentum after vs before": one point per Air Track run, a dashed y = x line, point shape by bumper (circle Spring, square Rubber, triangle Velcro, diamond Custom), so shape and color both mark it.
- Plot 2, "Kinetic energy kept vs bounciness e": one point per Air Track run, x = e from 0 to 1, y = percent kept from 0 to 100.
- Plot 3, "Peak force vs contact time": one point per Crumple Zone run, labeled by nose.
- Conclusion boxes (text areas) with these prompts: "What stayed the same in every Air Track run? Use your plot." / "What did the bumper change, and where did the missing energy go?" / "Which nose design gave the lowest peak force, and why does a longer contact time help?" / "Which spec could not be met? Show the numbers." Text is saved on this device only.

## Content

### Air Track settings
- Mass A and Mass B: 0.10 to 1.00 kg, step 0.05, default 0.25 kg. Plates drawn: one base block plus round((m minus 0.10) / 0.10) plates.
- Velocity A and Velocity B: minus 1.00 to plus 1.00 m/s, step 0.05. Defaults: A plus 0.60, B 0.00. Positive is to the right.
- Start positions (glider centers): A at 0.50 m, B at 1.20 m. Drag to move before launch, snap 0.05 m, A stays left of B with at least 0.25 m between centers, and both stay fully on the track (centers from 0.15 m to 1.85 m).
- Bumpers and their coefficient of restitution e: Spring 1.00 (labeled "ideal spring"), Rubber 0.60, Velcro 0.00 (gliders stick), Custom 0.00 to 1.00 step 0.05.

### Air Track presets (dropdown "Presets")
1. "Equal masses, spring": A 0.25 kg at +0.60, B 0.25 kg at 0, Spring. Result: A 0.00, B +0.60.
2. "Equal masses, Velcro": A 0.25 at +0.60, B 0.25 at 0, Velcro. Result: both +0.30, KE kept 50 percent.
3. "Heavy hits light": A 0.50 at +0.40, B 0.10 at 0, Spring. Result: A +0.27, B +0.67.
4. "Light hits heavy": A 0.10 at +0.60, B 0.50 at 0, Spring. Result: A minus 0.40 (bounces back), B +0.20.
5. "Head on, Velcro": A 0.25 at +0.50, B 0.25 at minus 0.50, Velcro. Result: both 0.00, KE kept 0 percent.
6. "Rubber bumper": A 0.25 at +0.60, B 0.25 at 0, Rubber. Result: A +0.12, B +0.48, KE kept 68 percent.
7. "The chase": A 0.25 at +0.80, B 0.50 at +0.20, Velcro. Result: both +0.40.

### Air Track physics (self-contained block, see Family engine)
- Gliders move at constant velocity (no friction, the air track's point). Contact when the gap between glider faces reaches 0.
- After contact, with m1, v1 for A and m2, v2 for B:
  v1' = (m1 v1 + m2 v2 + m2 e (v2 minus v1)) / (m1 + m2)
  v2' = (m1 v1 + m2 v2 + m1 e (v1 minus v2)) / (m1 + m2)
  When e = 0 both move together as one glider.
- Momentum p = m v. Kinetic energy KE = one half m v squared. KE kept = KE after / KE before x 100, rounded to a whole percent.
- Center of mass velocity v_cm = (m1 v1 + m2 v2) / (m1 + m2). It is the same before and after.
- Ride with center of mass: the view scrolls so the center of mass stays fixed at screen center; arrows, bars and readouts show velocities relative to it (v minus v_cm), so the two momenta are equal and opposite and the Total bar is zero. A label "Frame: moving with the center of mass at +0.30 m/s" replaces "Frame: lab".
- Measurement noise: when on, every displayed and recorded velocity gets an independent random error of up to plus or minus 2 percent of its value (uniform), and Rubber's e becomes a random value from 0.55 to 0.65 each run. The physics underneath is unchanged. The ledger line then reads "Momentum: before 0.150, after 0.148 (difference 1.3 percent)". Default off.

### Crumple Zone settings and noses
- Glider mass 0.20 to 1.00 kg, step 0.05, default 0.50. Impact speed 0.20 to 2.00 m/s, step 0.05, default 1.00.
- x = how far the nose has been pushed in (m). v = speed toward the wall (positive). Force on the glider points away from the wall.
- Steel: spring with k = 50,000 N/m, fully elastic, F = k x.
- Spring: spring with k = 200 N/m, fully elastic, F = k x.
- Rubber: loads with k = 1,000 N/m; from the peak (x_max, F_max) it unloads along F = F_max minus 4,000 (x_max minus x), which is k / e squared with e = 0.50, so it bounces back at half speed. Contact ends when F reaches 0.
- Crumple: a crushable block. Crush force F_c from 1.0 to 40.0 N, step 0.5, default 5.0. Crush length L from 1.0 to 10.0 cm, step 0.5, default 5.0. While moving toward the wall and x less than L, F = F_c. If the glider stops first, contact ends with the glider at rest (Stopped). If x reaches L with speed left (Bottomed out), a steel backing with k = 50,000 N/m engages: moving in, F = F_c + 50,000 (x minus L); moving out, F = 50,000 (x minus L) only, since crushed material does not push back.
- Bottomed out test uses energy: one half m v squared greater than F_c L plus 0.000001 J. Exactly equal counts as Stopped with Crush used = L.
- Readouts: Impulse is the area under the F-t curve. Change in momentum m (v after minus v before) is shown beside it, and the two must agree to 1 percent. Average force = impulse / contact time.
- Context line under the graph (on screen only): "Car crumple zones, airbags and helmet foam all work this way: a longer stop means a smaller force for the same change in momentum."

### Reference results (0.50 kg at 1.00 m/s, used in Done when)
- Steel: peak 158 N, contact 9.9 ms, crush 0.32 cm, speed after minus 1.00 m/s, impulse 1.00 N·s.
- Spring: peak 10.0 N, contact 157 ms, crush 5.0 cm, speed after minus 1.00 m/s, impulse 1.00 N·s.
- Rubber: peak 22.4 N, contact 52.7 ms, crush 2.24 cm, speed after minus 0.50 m/s, impulse 0.75 N·s.
- Crumple, F_c 6.0 N, L 5.0 cm: peak 6.0 N, contact 83 ms, crush 4.17 cm, Stopped, impulse 0.50 N·s.
- Crumple, F_c 2.0 N, L 5.0 cm: Bottomed out, peak about 122 N, rebounds at about minus 0.76 m/s.

### Spec sheet (design specs are invented for the lab, not real standards)
1. "Gentle stop": 0.50 kg at 1.00 m/s. Peak force under 10 N, crush length at most 5.0 cm, must not bounce. (Works for crush force 5.0 to 9.5 N with length 5.0 cm.)
2. "Heavy cart": 1.00 kg at 1.50 m/s. Peak force under 30 N, crush length at most 6.0 cm, must not bounce. (Needs crush force at least 18.75 N at 6.0 cm.)
3. "Fast and light": 0.50 kg at 2.00 m/s. Peak force under 15 N, crush length at most 10.0 cm, must not bounce. (Needs at least 10 N at 10 cm.)
4. "The impossible brief": 1.00 kg at 2.00 m/s. Peak force under 15 N, crush length at most 10.0 cm, must not bounce. Cannot be met: the lowest possible peak force is m v squared / (2 L) = 20 N. The card header says "One of these specs cannot be met. Find it and show why with numbers." The tool never reveals which; after a run on spec 4 the line still reads plainly, for example "Peak force 20.0 N, limit 15 N: not met."
- Any spec is met only with Crumple; Steel, Spring and Rubber bounce, so "must not bounce" fails for them, and the line says so.

### Notebook columns
- Air Track runs: Run, Bumper, e, mA (kg), vA (m/s), mB (kg), vB (m/s), vA after (m/s), vB after (m/s), p before (kg·m/s), p after (kg·m/s), KE before (J), KE after (J), KE kept (percent), Frame (lab or center of mass). Values are always stored in the lab frame.
- Crumple Zone runs: Run, Nose, F_c (N, Crumple only), L (cm, Crumple only), m (kg), v (m/s), Peak force (N), Contact time (ms), Crush used (cm), Impulse (N·s), Speed after (m/s), Result (Stopped, Bounced, Bottomed out).
- Number format: velocities and momenta 2 to 3 significant decimals as shown above (m/s to 2 places, kg·m/s to 3, J to 4, N to 1, ms to 1, cm to 2).

## Interactions in detail
- Air Track Launch: if both velocities are 0, nothing moves and the hint says "Nothing is moving. Give a glider some speed." If A is not gaining on B (v1 at most v2), the gliders run until one reaches an end stop, the After row copies Before, and the hint says "No collision: A never catches B." Record run is disabled for that run.
- If contact would take more than 8 seconds of sim time, a **Jump to collision** button appears beside Launch and skips ahead to 0.5 s before contact.
- The After row and Predict comparison fill in at the instant of contact. The run then continues until a glider reaches an end stop (it stops there, no bounce off the end) or 3 s after contact, whichever comes first.
- Sliders, bumper buttons, presets and dragging are locked during a run; Reset unlocks and returns gliders to their start spots with the current settings. Changing any setting after a run resets automatically.
- Slow motion plays at one quarter speed. With Motion off, the gliders jump to their final places and the ledger fills at once; timing of the run summary is unchanged.
- Predict toggle: two number boxes, "Your vA after" and "Your vB after" (m/s, minus 2.00 to 2.00), appear in the panel. Launch is disabled until both are filled. After contact the panel shows "You: +0.30, measured: +0.30, off by 0.00 m/s" for each glider. No points, no streaks.
- First-time voice beats (once per page load each): after the first Air Track run, after the first run with KE kept under 100 percent, the first time Ride with center of mass is turned on.
- Crumple Launch: the glider rolls in from the left at the set speed, the nose compresses or crushes (inset magnified), and the F-t curve draws in step with the animation, stretched in time so even a 10 ms steel hit takes about 1.5 s to draw. Axes auto-scale to the tallest and longest curve on screen unless Lock graph axes is on; when locked, curves taller than the axis are clipped with a "peak off scale: 158 N" label.
- Ghosts: up to three previous curves, oldest dropped first. Clear ghosts removes them.
- Crumple nose sliders (Crush force, Crush length) show only when Crumple is picked. Steel, Spring and Rubber show their k and e values as read-only text.
- First-time voice beats: after the first Crumple run, the first Bottomed out, the first Bounced run.
- Record run: adds the run to the matching Notebook table and plot and shows "Recorded as run 4." Each table holds 30 rows; at 30, Record run is disabled with the hint "Notebook full. Copy and clear a table to keep going."
- Copy table: uses the clipboard; if that fails, shows the text in a selectable box with "Select all and copy."
- Notebook tables, plots and conclusion text are saved in localStorage key `curio-collision-lab` (try/catch). If storage fails, the tool still works and the Notebook shows "Notes will not be saved on this device."
- Switching modes calls `Curio.stop()` and pauses any run (Reset state on return).
- All sliders are native range inputs with visible labels and live value text; arrow keys nudge by one step. Every button is at least 44 px tall.

## Art
none: drawn in code (track, gliders, plates, bumpers, noses, sensor wall, bars, graphs, plots).

## Voice
`voice/lines.json`: `"bank": "hs-narrator"`, `"voice": "Kore"`, `"style": "Read clearly and naturally, at a moderate pace"`. On screen text is the main channel; these are the only spoken lines.
1. at-welcome: "This is an air track. The gliders ride on air, so almost nothing slows them down. Set the masses and speeds, pick a bumper, and launch."
2. at-first-run: "Look at the momentum bars. The total before and the total after are the same."
3. at-energy: "Now look at the energy bars. Kinetic energy was not all kept. Where do you think it went?"
4. at-cm-frame: "You are riding along with the center of mass. From here the two momenta are equal and opposite, and they add up to zero."
5. at-predict: "Type the speeds you expect after the collision, then launch and compare."
6. at-no-collision: "Glider A never catches glider B, so they never collide."
7. cz-welcome: "This is the crumple zone bench. A glider hits a force sensor through a nose you choose, and the graph shows force over time."
8. cz-first-run: "The shaded area under the curve is the impulse. It always equals the glider's change in momentum."
9. cz-bounce: "This glider bounced back. Its change in momentum is bigger than a glider that just stops, so the impulse is bigger too."
10. cz-bottom: "It bottomed out. The crumple zone ran out of room, and the stiff steel behind it took the rest of the hit."
11. cz-spec: "Each spec sets a force limit and a crush length. One of them cannot be met. Find it and show why with numbers."
12. cz-spec-met: "Spec met."
13. nb-welcome: "Every run you record lands here. If momentum is conserved, your points fall on the dashed line."

## Family engine
Family forces has no engine doc yet. Keep all physics in one clearly marked block in the tool script, `/* FORCES ENGINE: begin */ ... /* FORCES ENGINE: end */`, with no DOM access inside it, so it can later move to `kit/forces.js`:
- `collide1D(m1, v1, m2, v2, e)` returns `{v1, v2, p0, p1, ke0, ke1, vcm}`.
- `contactTime1D(x1, v1, x2, v2, gap)` returns seconds until contact or null.
- `noseRun(m, v, nose)` with nose `{type: 'spring', k}`, `{type: 'rubber', k, e}` or `{type: 'crumple', Fc, L, kBack: 50000}` returns `{samples: [[t, F]...], peak, contactTime, crushUsed, vAfter, impulse, result}`, integrated with velocity Verlet at dt = 0.00001 s (closed forms in Content are the check values).
The three plots may use `kit/graphing.js` (`Plane`, `g.param` for the F-t curve, `g.point` for Notebook points) if it exists when this tool is built; otherwise draw them in the tool's own SVG.

## Sources
- Conservation of momentum, elastic and inelastic collisions, center of mass: OpenStax, University Physics Volume 1, chapter 9, sections 9.3 to 9.6. https://openstax.org/books/university-physics-volume-1/pages/9-introduction
- Impulse equals change in momentum, longer contact time lowers force (padding, crumple zones, airbags): OpenStax, College Physics 2e, section 8.2 Impulse. https://openstax.org/books/college-physics-2e/pages/8-2-impulse
- Coefficient of restitution as ratio of separation speed to approach speed: OpenStax, University Physics Volume 1, section 9.4 (Types of Collisions) and HyperPhysics, "Coefficient of Restitution". http://hyperphysics.phy-astr.gsu.edu/hbase/elacol.html
- Spring force F = k x, spring energy one half k x squared, and period 2 pi square root of m over k (used for contact times): OpenStax, University Physics Volume 1, sections 7.2 and 15.1. https://openstax.org/books/university-physics-volume-1/pages/15-1-simple-harmonic-motion
- Work done by a constant force over a distance (crumple stopping distance one half m v squared / F): OpenStax, University Physics Volume 1, section 7.1. https://openstax.org/books/university-physics-volume-1/pages/7-1-work
- Standards text: NGSS HS-PS2-2 and HS-PS2-3. https://www.nextgenscience.org/dci-arrangement/hs-ps2-motion-and-stability-forces-and-interactions
- Glider masses, spring constants, crush forces and the four specs are invented lab settings chosen to give clean numbers; they are not real equipment ratings or crash standards, and the tool says "design specs for this lab" on the Spec sheet.

## Done when
1. Air Track preset 2 (Equal masses, Velcro) gives both gliders +0.30 m/s, p before and after 0.150 kg·m/s, and "Kinetic energy kept: 50 percent".
2. Preset 4 (Light hits heavy) shows A moving left at minus 0.40 m/s and B at +0.20 m/s, and the Total momentum bar is the same length in Before and After.
3. Turning on Ride with center of mass in preset 3 makes the Total momentum bar read 0.000 in both rows and the center of mass marker stays still on screen.
4. A at +0.20 and B at +0.50 m/s gives "No collision: A never catches B" and Record run is disabled; both velocities 0 gives the "Nothing is moving" hint.
5. Crumple Zone at 0.50 kg and 1.00 m/s matches the Reference results within 2 percent for Steel, Spring, Rubber and Crumple (6.0 N, 5.0 cm), and the shaded impulse matches the change in momentum to 1 percent each time.
6. Crumple with 2.0 N and 5.0 cm shows the "Bottomed out" tag and a peak force above 100 N; 5.0 N and 5.0 cm shows "Stopped" with crush used 5.00 cm.
7. Spec 1 is met with 6.0 N and 5.0 cm; spec 4 cannot be met with any slider setting, and the card never says which spec is impossible.
8. Recorded Air Track runs appear in the Notebook table and on the momentum plot on the y = x line; with Measurement noise on they scatter near it; Copy table pastes into a spreadsheet as columns with units in the headers.
9. With Motion off, runs finish with no sliding animation and the same results; every control works by keyboard with visible focus; no em dashes and no network requests in the file.
10. Reload keeps the Notebook rows and conclusion text; blocking storage still lets every mode run.
