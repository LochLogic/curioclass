# Zipline Energy

## One idea
Design a 300 m zipline from a cliff platform to a far tree and test it with a light, a medium and a heavy rider: an
energy ledger follows every joule from height into speed, rolling friction, air drag and the brake, and the design
only passes when all three riders arrive, stop before the platform and never brake harder than 1.5 g.

## Not like
- rollercoaster-polynomials (built, math): a polynomial track shaped to fit points. Here the shape is fixed by a
  cable and the question is where the energy goes.
- skate-park-energy (gr 8): frictionless back and forth between height and speed. Here friction, air drag and a brake
  take energy out, and riders of different masses must all be safe on one design.
- curling-stones (this group): forces and acceleration on flat ice. Here energy bookkeeping on a slope; forces appear
  only as the work they do.
- hot-meets-cold (this group): thermal energy moving between objects. Here thermal energy is where friction sends
  the ride's energy, one bar in the ledger.
- grid-operator (gr 12 environmental, this wave): power plants and a city grid. Here one small generator brake
  turning a rider's motion into electricity.
- launch-pad (gr 9 math, wave 1): projectile paths from equations. Here no free flight; the rider rides a cable.

## Who and how
Grade 11, physics (Energy and Work). Students drive, 30 to 45 minutes. Explore first: Design opens with a working
cable and a 70 kg rider ready to go.
Topic line: "conservation of energy with friction, roller coaster physics".
Standards: HS-PS3-1, HS-PS3-2, HS-PS3-3.
tool.json: driver "students", minutes "30-45", modes ["Design", "Ledger", "Notebook"].

## Screens and modes
Header (kit, 9-12 theme): "Zipline Energy", small line "Every joule goes somewhere." Modes `Design`, `Ledger`,
`Notebook`; kit `Motion`, `Sound`, `Read`.

### Design (builder, default)
Stage: a side view of a valley 300 m across, a cliff platform at the left (cable anchor 45 m up), a tall tree at the
right with a landing platform, the cable drawn as the path the trolley follows (Content), the brake zone painted on
the last 20 m before the landing platform's edge. Height and distance scales on the edges.
Panel, Cable: Tree anchor height (5 to 35 m, step 1, default 15), Cable sag (5 to 20 m, step 0.5, default 10).
Panel, Trolley and rider: Trolley `New` / `Worn`, Rider posture `Upright` / `Tuck`, Rider `35 kg` / `70 kg` /
`120 kg` (default 70) or a mass slider 30 to 130 kg.
Panel, Brake: `None`, `Pad` (force 200 to 2000 N, step 50, default 800), `Generator` (strength 20 to 300 N·s/m, step
5, default 70).
- `Ride` (Space) sends the chosen rider; the trolley rolls along the cable with a speed readout and a small speed
  trace under the stage. `Test all three` runs 35, 70 and 120 kg one after another (ghost riders stay on the cable).
- The lab card at the right checks three rules for each rider (Content) with a tick or a cross and the measured value:
  "reached the brake zone at 11.32 m/s", "stopped at 281.4 m (edge at 296)", "peak braking 1.24 g".
- `Friction off` toggle (a what-if, no lab card): no rolling friction, no air drag; the ledger shows only height and
  speed.
- `Reset` (R).

### Ledger
The last ride replayed with a stacked bar beside the stage that always has the same total height (the energy at the
start, measured from the lowest point of the cable as zero height). Bars: height energy (mgh), motion energy (½mv²),
rolling friction heat, air drag (heat in the air), brake heat, battery (generator only). A scrubber moves along the
ride; the bars update to that point. Computation cards under the bar, filled from the ride:
- "Height energy lost by 281.4 m: 20,673 J" with the work: m g Δh = 70 × 9.81 × 30.11.
- "Where it went: rolling 2,879 J + drag 13,512 J + brake 4,285 J = 20,676 J" (rounding note when it differs by a few
  joules).
- "With friction off, speed at the zone would be 24.33 m/s: √(2 g h)."

### Notebook
Table of every ride: tree height, sag, trolley, posture, brake and setting, mass, speed at zone, stop point, peak g,
each ledger total, pass or fail. `Copy table`, `Clear notebook`. Plot: speed at the brake zone against rider mass for
the current design, with and without friction (the friction-off points sit on one flat line; with friction the
heavier riders arrive faster because drag matters less per kilogram). Conclusion box (unsaved): "Why does a brake that
pushes harder at higher speed treat light and heavy riders more evenly?" with `Compare`.

## Content
Cable (trolley path): the anchors are at (0, 45) and (300, H2) in meters. A pulley on a cable of fixed length traces an
ellipse with the two anchors as foci; the sag b is the ellipse's semi-minor axis, a = √(b² + c²), c = half the anchor
distance. Defaults H2 15, b 10: anchor distance 301.50 m, cable length 2a = 302.16 m. The rider starts at x = 4 m
(42.14 m high); the landing platform edge is at x = 296 m; the brake zone runs from x = 276 to 296 m. Lowest point
11.97 m.
Ride equation along the cable (s is distance along the path, u = v²): du/ds = 2g sin θ − 2μ_r g − (ρ C_dA / m) u −
2F_b / m, where θ is the downhill angle. g 9.81 m/s², air density ρ 1.20 kg/m³. C_dA (drag area): upright 0.50 m²,
tuck 0.30 m². Rolling friction μ_r: new 0.015, worn 0.030. Pad brake: constant force F_b. Generator brake: F_b = k v,
80 percent of its energy to the battery, 20 percent heat. All four are lab settings. Left out (said on screen): cable
stretch and bounce, wind, the rider swinging, the trolley's spin energy.
Lab rules: reach the brake zone at 1 m/s or more; stop before x = 296 m; peak braking (deceleration along the cable)
at most 1.5 g. A trolley stopped in the zone is held by a ratchet catch (no rolling back).

Check values (default cable, new trolley, upright):
| Rider | Brake | Speed at zone (m/s) | Stop or end | Peak (g) | Ledger (J) |
|---|---|---|---|---|---|
| 35 kg | none | 6.79 | reaches the edge at 2.86 m/s | | |
| 70 kg | none | 11.32 | reaches the edge at 9.05 m/s | | rolling 3,030, drag 14,065, motion 2,867 |
| 120 kg | none | 14.76 | reaches the edge at 13.06 m/s | | |
| 35 kg | pad 800 N | 6.79 | stops 277.0 m | 2.39 (fails) | height 10,356 = rolling 1,417 + drag 8,145 + brake 795 |
| 70 kg | pad 800 N | 11.32 | stops 281.4 m | 1.24 | height 20,673 = 2,879 + 13,512 + 4,285 |
| 120 kg | pad 800 N | 14.76 | stops 290.7 m | 0.77 | height 34,949 = 5,100 + 18,089 + 11,760 |
| 35 kg | generator 70 | 6.79 | stops 279.1 m | 1.44 | |
| 70 kg | generator 70 | 11.32 | stops 285.7 m | 1.23 | brake 4,116, battery 3,293 J (0.91 Wh) |
| 120 kg | generator 70 | 14.76 | stops 294.8 m | 0.95 | |
| 70 kg | friction off, no brake | 24.33 | edge at 23.88 m/s | | |
Design findings (all computed): no pad force passes all three riders on the default cable (the light rider needs
under 500 N, since 500 N brakes it at 1.51 g, and the heavy rider needs at least 550 N); generator 65 and 70 pass all
three, 60 leaves the 120 kg rider moving at the edge (1.55 m/s), 75 brakes the 35 kg rider at 1.54 g. Tree anchor 30
m: the 35 kg rider stalls at 266.3 m before the zone. Sag 20 m: the 35 kg rider stalls at 274.7 m. Worn trolley,
speed at zone: 5.40, 9.85, 13.18. Tuck: 10.08, 14.59, 17.37; with tuck, generator 70 fails (35 kg at 2.13 g, 70 kg at
1.56 g, 120 kg not stopped).
Challenge cards in Design (optional, checked by running the three riders):
- Z1 "Safe for everyone": default cable, pass all three. Answers: generator 65 or 70.
- Z2 "Low tree": tree anchor at 25 m, pass all three. Answers: generator 35 to 125 or pad 250 to 450 N (the 35 kg
  rider reaches the zone at only 2.97 m/s).
- Z3 "Rainy day": worn trolley, pass all three. Answers: generator 50 to 90 or pad 400 to 450 N.

## Interactions in detail
- Integration: RK4 along the path in steps of at most 0.01 m, so check values hold within 1 percent (speeds) and 0.5
  m (stops); the ledger closes to within 0.2 percent of the starting energy.
- Stalls: speed reaching 0 before the zone shows "Stuck at 266.3 m. The crew hauls them in." and a cross on the first
  rule.
- Edge arrivals: reaching x = 296 m still moving shows "Hit the platform at 9.05 m/s" (the rider is drawn stopping
  against a padded bumper, no injury shown) and a cross on the second rule.
- `Test all three` runs riders 2 s apart at 4x speed; the lab card fills per rider.
- Sliders lock during a ride; changing the cable redraws it and clears ghost riders.
- Sound: a rising zip whose pitch follows speed, a brake hiss (pad) or a whine (generator); off with Sound.
- Keyboard: Space = Ride, T = Test all three, R = Reset, arrows on focused sliders.
- Layout by real stage pixels: wide (stage with panel at side), compact, stack (375 wide: the stage keeps the whole
  valley at a smaller scale, panel and lab card below).
- Mode change: `Curio.stop()`, `V.hush()`. Notebook and passed challenges per device (localStorage
  `curio-zipline-energy`, try/catch), `Clear notebook`.

## Look
Accent (`--brand`) #d0c440, hemp rope gold: 9.60:1 on --panel #141b25, 9.10:1 on --sec-bg #18202b; --brand-ink
#10161f on it 10.07:1. Distinct from rollercoaster-polynomials' #f2a93b; moved off #dcd070 (close to
equilibrium-seesaw #c0b959); nearest 9-12 accents health-claim #ffe066 (ΔE 14), api-playground and intersection-quest
(15).
Scene: dusk valley sky #1b2433 to #2c3a4f, cliff rock #4a4440 with ledges #5c554f, forest floor #1f3326, tree trunk
#5a4030 and canopy #2f5a3a, steel cable #b8c0c8, trolley in the accent, rider helmet #e8edf3, brake zone striped
#ff8a8a at 35 percent. Ledger colors: height `--gr-1`, motion `--gr-3`, friction heat `--gr-4`, drag #c9a0ff (gr-2),
brake heat #ffb070, battery #9ee6d8.

## Art
none: drawn in code (valley, cliff, tree, cable, trolley, rider silhouette, ledger, preview.svg).

## Voice
`big-sister` (Leda), style "Say in a friendly, youthful way, like a zipline guide in her twenties." No group sibling
uses it; shared in 9-12 science only with mitosis-mixer (gr 9 biology). `Curio.voice`, `scope: () => state.mode`.
- design (how, Design welcome): "Set the cable and the brake, then press Ride. The card checks three safety rules."
- three (how, after the first single ride): "Now press Test all three. One design has to work for every rider."
- stall (event, a stall before the zone; stale on Reset): "Stuck in the middle. Not enough height for that cable."
- hard (event, peak over 1.5 g; stale on the next ride): "That brake grabbed too hard for this rider."
- pass (event, all three pass; stale on any change): "All three riders safe. That is a design."
- ledger (how, Ledger welcome): "Drag along the ride. The bars always add up to the energy you started with."

## Family engine
none. Speed trace and the Notebook plot use `kit/graphing.js` `Plane` if present; otherwise the tool's own SVG.

## Sources
- Work, kinetic and potential energy, conservation of energy with friction: OpenStax, College Physics 2e (2022),
  chapter 7, https://openstax.org/books/college-physics-2e/pages/7-introduction-to-work-energy-and-energy-resources
- Air drag F = ½ ρ C_d A v²: OpenStax, College Physics 2e, 5.2 "Drag Forces". Drag areas for a person: Hoerner,
  "Fluid-Dynamic Drag" (1965), chapter 3 (the lab's 0.50 and 0.30 m² sit inside the range for standing and crouched
  people).
- Air density 1.2 kg/m³ near sea level: NASA Glenn Research Center, "Earth Atmosphere Model",
  https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html
- Ellipse as the set of points with a constant sum of distances to two foci: OpenStax, Precalculus 2e, 8.1 "The
  Ellipse", https://openstax.org/books/precalculus-2e/pages/8-1-the-ellipse
- Generators turn motion into electrical energy (HS-PS3-3 device): OpenStax, College Physics 2e, 23.5 "Electric
  Generators".
- Rolling friction values, brake settings, the 80 percent battery share and the 1.5 g limit are lab settings; every
  check value computed in Python (2026-10-27).

## Done when
1. Default 70 kg with pad 800 N: zone at 11.32 m/s, stop 281.4 m, peak 1.24 g, all three rules pass.
2. `Test all three` with pad 800 N fails the 35 kg rider on braking (2.39 g); with generator 70 all three pass and
   "All three riders safe." plays once.
3. No brake: the 70 kg rider hits the platform at 9.05 m/s; the ledger shows rolling 3,030, drag 14,065, motion
   2,867 J out of 19,963.
4. Friction off: zone speed 24.33 m/s for every mass.
5. Tree anchor 30 m: the 35 kg rider stalls at 266.3 m with the stall line.
6. Ledger for 70 kg with generator 70 shows battery 3,293 J (0.91 Wh) and the bars add to the start total.
7. Notebook plot: friction-off points flat; with friction 6.79, 11.32, 14.76 rising with mass.
8. How-to lines once each; event lines as listed.
9. Valley, cable and lab card visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the 680x425
   preview; no network, no images, no em dashes.

## Open questions
- [zipline-energy] The lab rules (1.5 g peak braking, 1 m/s at the zone) and the drag and friction values are lab
  settings, not an industry standard. Fine as lab rules, or source a real zipline standard (for example ASTM F2959)
  before build?
