# Span and Spire

## One idea
Every beam in a structure is being pulled or squeezed, and you can watch which: drag a real truck (pickup to 36.3 t
semi) across the bridge you drew over a farm creek and every member glows blue when stretched, amber when squeezed and
bows in slow motion when it buckles; then build a tower on a giant shake table, pluck it to feel its own sway, and find
out why a stiffer tower can be the one that shakes apart.

## First minute
No reading needed. Nothing is locked.
- 0 s. Dusk over a farm valley. A bare road deck (seven joints, six plain timber beams) spans the creek. A painted
  pickup with hay bales idles on the left bank, headlights on, a soft engine hum after the first tap. The big pink `Go`
  button breathes once. The pickup has a small "drag me" hand cue that bobs twice.
- 2 s. The student taps `Go` (or drags the pickup onto the road). The deck folds at its joints, slowly (loose joints
  flash white with a wooden rattle), the pickup tips, slides and splashes into the creek: a white splash cutout, a low
  "sploosh", ripples in the code-drawn water.
- 6 s. A crane hook drops in, lifts the pickup back to the bank and the road snaps back into place with a click. The
  seven joints pulse pink one after another, left to right.
- 10 s. The student drags up from a joint: a beam stretches like a rubber band from the joint to the pointer and a new
  joint lands on the grid with a wooden knock. Beams already carrying the road's weight glow faintly. Loose joints
  shiver until the student closes a triangle; then the shiver stops with a soft "tok".
- 25 s. Most students now have a lumpy row of triangles. `Go` again: the pickup rolls across, each beam lighting up blue
  or amber as the wheels pass over, the sag shown 20 times bigger so the bridge visibly flexes. The pickup parks on the
  far bank, a three-note bell rises, and the first inspection tag stamps into the corner: "Crossed".
- 40 s. The truck shelf shows four bigger trucks. The student taps the school bus; it rolls in. Some will try the semi
  at once and watch the end post bow, crack and drop the semi into the creek in slow motion. That is the fun, and the
  hook.
- 60 s. The student is dragging the bus back and forth by hand on the deck and watching the colors ripple, which is the
  influence line, unnamed.

## Not like
- zipline-energy (gr 11 builder): energy bookkeeping for a rider on a cable. Here forces in a structure, and sway.
- reserve-designer (gr 9 builder): a budget buys land cells on a map. Here a budget buys beams and a solver judges them.
- design-challenge-studio (gr 12): an open process for any problem. Here one physical problem and a real truss solver.
- crash-test-lab and half-pipe-energy (gr 8): collisions and a drawn skate ramp. Here a drawn frame held in balance.
- molecule-forge (super tool): pieces snap only where rules allow. Here anything snaps; physics decides if it holds.
- proof-tower (gr 10 math) and three-pigs-lab (gr 2): a logic metaphor, and a wolf's breath. Here measured loads.
- Bridge games and West Point Bridge Designer: no levels, stars or section catalog. Real trucks with legal axle weights,
  a truck you drag by hand, pull and squeeze drawn differently, promises you choose, a Yard to borrow parts, and a
  second half (towers, wind, shake table, pluck, resonance) they do not have.

## Who and how
Grades 6 to 12 (anchor: grade 8 science, module Engineering Design). Students drive, alone or in pairs on laptops, 20 to
60 minutes. Explore first: the bridge is live from the first second; goals are optional tags. Topic line: "bridges,
towers, forces in structures, engineering design". Standards: MS-ETS1-1 (Promises: criteria and constraints from the
people who use it), MS-ETS1-2 (Yard compare table scores designs against the promises), MS-ETS1-3 (Borrow combines the
best parts of tested designs), MS-ETS1-4 (the solver is the model for repeated testing). High school reach: HS-ETS1-2,
HS-ETS1-3, HS-ETS1-4. tool.json: driver "students", minutes "20-60", modes ["Bridge", "Tower", "Yard"], grades_label
"Grades 6-12".

## Screens and modes
Header (kit): title "Span and Spire", small line "Pulled or squeezed?". Mode buttons `Bridge` (opens first), `Tower`,
`Yard`; then `Tags` (opens the tag book drawer), kit `Motion`, `Sound`, `Read`.
Layout: stage left, panel right (300 to 340 px). Under 1000 px wide the panel goes under the stage, buttons first. Under
900 px tall the panel goes compact: trucks and materials become icon rows, Promises fold to one line of six ticks. The
stage is drawn at real pixel size and re-laid out per size (STANDARDS.md); the world scales to fit the stage width.

### Bridge (default)
Focus: the bridge and the truck, the biggest thing on screen, centered over the creek.
Stage: world x from -6 to 30 m, y from -6 to 12 m, 1 m grid of faint dots. Painted far hills and sky behind; banks are a
painted soil-and-rock texture clipped to the terrain shape (code); grass strip along the bank tops; creek water drawn in
code (gently moving surface line and ripples), the dashed spring high-water line at y = -2 with a small label "spring
flood", the canoe opening shown as a faint dotted box with a painted canoe floating under it. Abutments (painted
concrete seats) at (0, 0) and (24, 0). Scale bar "4 m" bottom left. Readouts top left on dark chips: truck name and
weight, "Each side carries half: 18.1 t", heaviest pull and squeeze right now in kN with the member's use.
Panel, top to bottom:
- `Go` (Space, big, pink) and `Rebuild` (R; shown after a collapse, restores the design and the truck).
- Trucks: `Pickup 3.0 t`, `School bus 13.6 t`, `Fire engine 20.0 t`, `Grain truck 23.4 t`, `Semi 36.3 t`, each with its
  painted thumbnail. Tapping one swaps the truck in place at once.
- Pieces: `Timber`, `Big timber`, `Steel`, `Big steel`, `Cable` (the piece new beams use; tapping a beam on the stage
  turns it into the selected piece). Each button shows its price per meter.
- Tools: `Build` (default), `Erase`, `Undo`, `Redo`.
- Views: `Worst spots` (toggle), `True size` (toggle, sag at real size instead of 20 times).
- Readout: Cost $ / Members n of 60 / Joints n of 40.
- Promises (card): six rows, each with a painted icon and a checkbox (Content). Ticked rows show a live tick or cross
  after each test.
- `Save to Yard`, `New` (back to the bare deck; asks "Start over? Your design stays if you saved it." with `Start over`
  and `Keep building`).
- hint.

### Tower
Focus: the tower on the shake table, the biggest thing, with the small resonance chart second.
Stage: world x from -8 to 8 m, y from -1 to 32 m (portrait world centered in a landscape stage; the free side space
holds the resonance chart at the right and the wind and pressure readouts at the left). Painted open-air test yard
backdrop at bright noon, painted shake table platform (12 m wide, x -6 to 6) that slides left and right during a shake;
a painted water tank or bell sits on the top joint when chosen. A height ruler at the left with marks every 2 m and the
tap pressure for a tank at that height. Wind: code streaks whose speed and density follow the wind, a painted windsock
(limp or full) at the table edge, two painted clouds drifting at a speed tied to the wind.
Panel:
- `Shake` (Space) / `Stop`, `Rebuild` (R; after a collapse).
- Shake settings: Strength slider 0.05 to 0.60 g (step 0.05, default 0.30), Speed slider 0.40 to 4.00 shakes a second
  (step 0.05, default 1.20), presets `Valley quake` (0.30 g, 1.20 a second).
- Wind: `Wind` toggle and speed slider 0 to 70 m/s (step 5, default 30), scale marks: 10 breezy, 20 gale, 33 hurricane,
  70 top hurricane.
- Top load: `None`, `Bell 2 t`, `Tank 8 t` (default Tank).
- Pieces and Tools as in Bridge (shared rows), `Worst spots`, `True size`.
- Readout: Members n of 60 / Joints n of 40 / Tank height and tap pressure "26 m: 284 kPa (41 psi)" / "Sway: 0.77 a
  second" (appears after the first pluck).
- Promises (Tower set, Content), `Save to Yard`, `New`, hint.

### Yard
Focus: the compare table, the biggest thing, with the design cards above it.
Up to 12 saved designs (bridges and towers) as cards with a code-drawn thumbnail, name (editable), cost, heaviest truck
crossed or tower results. One sample is always there: "Old farm bridge" (read only, Content).
- Tap cards to pick up to three; the compare table shows one column each and one row per promise (both sets), plus cost,
  members, heaviest truck, worst use with each truck, sway per second, wind and shake results. Each cell is a tick, a
  cross, a number or "not tested" (run `Test all` to fill).
- `Test all` (runs every truck and the Tower tests in the background on the picked designs, about 1 s each, no
  animation), `Open` (loads into its mode), `Borrow` (Interactions), `Replay` (plays the design's best test with the
  cinematic camera), `Rename`, `Delete` (asks).

## Goals
Inspection tags. The `Tags` drawer shows 25 tag shapes (code-drawn, each with a painted icon reused from the art); found
ones are stamped with the date, missing ones show only their name and target. Tags never block anything. Saved on this
device. A stamp makes a thunk, the tag flies to the `Tags` button, and the drawer badge counts up.

| # | Tag | Target | Check (exact) | Secretly teaches |
|---|---|---|---|---|
| 1 | Crossed | Get the pickup across | pickup crossing completes, no member over 100% | triangles carry load |
| 2 | Folded | Watch a frame fold | a test or shake finds a loose design (Bridge or Tower) | squares fold, triangles do not |
| 3 | Buckled | See a squeezed beam buckle | a compression failure where the buckling limit is below the crush limit | long squeezed members bow |
| 4 | Snapped | See a stretched beam snap | a tension failure (timber or steel over its pull limit, or a cable over 1000 kN) | pull limits are material limits |
| 5 | School run | Bus across | bus crossing completes | load grows, forces grow |
| 6 | Fire call | Fire engine across | fire engine completes | |
| 7 | Harvest | Grain truck across | grain truck completes | |
| 8 | Big rig | Semi across | semi completes | the largest legal truck |
| 9 | Old bridge | Find what broke the old bridge | Old farm bridge opened from the Yard and a truck fails on it | test a design before replacing it |
| 10 | On the edge | Semi across, worst beam 95 to 100% | max use over the semi crossing in [95, 100] | no margin is a gamble |
| 11 | Margin | Semi across, every beam at 67% or less | max use ≤ 66.7% | safety factor 1.5 |
| 12 | County budget | Tag 11 for $9,000 or less | margin semi and cost ≤ $9,000 | shape beats material |
| 13 | Shoestring | Tag 11 for $8,500 or less | margin semi and cost ≤ $8,500 | pull-only pieces where pull is certain |
| 14 | Pull only | Semi across with 8 or more cables | ≥ 8 cable members and semi completes | cables carry pull, never push |
| 15 | Taking turns | A cable goes slack and the bridge holds | during a completed crossing some cable reaches 0 kN | counters: crossed cables share the work |
| 16 | Brace it | Fix a buckle with a joint in its middle | the last failure was a buckle of beam P-Q; the design now has a joint X on segment P-Q, beams P-X and X-Q, one more beam at X, and the same truck completes | half the length, four times the buckling limit |
| 17 | Pier shortcut | Semi across with a footing in the stream | a footing below the high-water line and semi completes | a cheap fix can break a promise |
| 18 | Every promise | All six bridge promises ticked and kept | all six ticked, all pass in one design | criteria and constraints together |
| 19 | Stand tall | Tank stands at 10 m | tank top joint ≥ 10 m, no member over 100% under its own weight | load paths down to the ground |
| 20 | Pluck | Count a tower's sway | a pluck shows 3 or more sways | every structure has its own sway rate |
| 21 | Gale | Tank at 20 m in 50 m/s wind | top ≥ 20 m, wind 50 holds for 5 s | wind grows with height |
| 22 | Spire | Tank at 30 m in 70 m/s wind | top ≥ 30 m, wind 70 holds for 5 s | a wide base resists tipping |
| 23 | Resonance | Shake a tower apart at its own sway | a shake fails with speed within 15% of the tower's sway rate | resonance |
| 24 | Stiffer is not safer | Survive a shake that broke a stiffer tower | a shake setting failed design A; design B with a lower sway rate holds the same setting for 15 s | moving away from the shake's speed matters, not raw strength |
| 25 | Town tower | Tank at 26 m, wind 50 and the Valley quake | top ≥ 26 m (41 psi), wind 50 holds 5 s, 0.30 g at 1.20 a second holds 15 s | combine the best parts of two designs |

## Depth from combining
Parts: (1) joints and triangles, (2) pieces (timber, steel, cable: cables only pull), (3) lengths and depth (long
squeezed beams buckle; shallow frames squeeze their chords harder), (4) the load (which truck, where it stands, how its
weight is spread), (5) mass and stiffness (a tower's own sway rate against the table's shake speed, and wind).
Surprising combinations, each run on the real model (Sources lists the numbers):
1. Cables as Pratt diagonals carry the pickup (30.1%) but fold under the school bus as soon as its front axle is 4.7 m
   onto the bridge: the middle diagonals flip from pull to push and a cable cannot push. The same cables as Howe
   diagonals fold under the bridge's own weight. Crossing a second cable in every middle panel holds the semi (99.6%);
   during the crossing 6 of the 8 cables go slack at some point and their partners take over.
2. Taller is not always stronger: an all-timber Pratt with a 2 m top fails the fire engine, 4 m carries the semi at
   99.6%, 5 m fails the grain truck (110.5%), 6 m fails the fire engine (115.6%). Depth eases the chords but lengthens
   the end posts, which buckle.
3. Halving a squeezed beam: the 6 m Pratt's end posts buckle at 100.1% under the fire engine; a joint at each end post's
   middle with one timber brace to the deck makes the semi a 37.8% stroll, for $49 less than swapping the end posts to
   Big timber.
4. Shape beats material: an all-timber Warren (top joints between the deck joints, 4 m deep) carries the semi at 56.3%
   for $8,783 where the Pratt of the same depth needs 99.6%; its end diagonals are 4.47 m, not 5.66 m. Turning its deck
   and four end diagonals into cables keeps every promise for $8,364.
5. Heavier is not always harder: the 36.3 t semi is 55% heavier than the 23.4 t grain truck yet works the Warren no
   harder (56.3% against 57.4%): its weight is spread over 18.3 m instead of 6.8 m. That is why the Federal Bridge
   Formula limits weight by axle spacing.
6. A pier in the stream turns the failing shallow Pratt (grain truck 114.4%) into a semi carrier (65.2%) and breaks two
   promises (Trout, Canoe club).
7. Stiffer is not safer: at 0.30 g and 1.4 shakes a second, a 20 m, 2 m wide timber tower with the tank (sway 0.77 a
   second) holds at 36%; the stiffer 4 m wide tower (1.43) fails at 2.1 s (273%); the steel tower (1.36) fails at 2.5 s
   (217%).
8. A lighter top can be worse: on that 2 m timber tower, swapping the 8 t tank for the 2 t bell raises its sway to 1.47
   a second and it now fails the 1.4 shake (129%) that the tank rode out. Emptying the top raises the sway to 4.32, and
   the 0.8 shake that broke it with the tank (440%) now barely moves it (4%).
9. Wind and quake pull opposite ways: at 26 m a straight 2 m timber tower holds the Valley quake (28%) but the wind tips
   it (111% at 50 m/s); a stepped 6-4-2 m tower holds the wind (45%) but the quake breaks it (227%). Keeping the narrow
   tower and borrowing Big timber legs holds both (wind 50%, quake 36%). An all-timber 4-then-2 m tower also holds both
   (61%, 52%).
10. Guy wires: two cables from the top of the 20 m tank tower to the table edges raise its sway to 1.91 a second; the
    0.8 shake that broke it now reaches 43%, but the 1.4 shake it used to survive now breaks it (120%).

## Content
Bridge world. Road deck at y = 0. Ground: y = 0 for x ≤ 0 and x ≥ 24; bank slopes from (0, 0) to (5, -5) and from (19,
-5) to (24, 0); creek bed y = -5 from x = 5 to 19; normal water surface y = -4; spring high-water line y = -2. Supports:
(0, 0) pinned abutment, (24, 0) rolling abutment (moves sideways, like real bridge bearings). Any joint placed on the
ground line becomes a pinned footing ($2,000). Footings below the high-water line (y < -2) are "in the stream". Canoe
opening: x 8 to 16, y -4 to -1; no beam may pass through it to keep that promise. Starting design: deck joints at x = 0,
4, 8, 12, 16, 20, 24; six Timber deck beams. The road needs a chain of beams along y = 0 from 0 to 24 with no gap over 4
m between deck joints (the road slab reaches 4 m).
Sides: the student draws one side truss; an identical one stands behind it; each side carries half of every truck and
half the road slab (2.0 kN per meter of deck per side).
Pieces (per side, 1 m grid; beam length up to 12 m, cable up to 30 m):

| Piece | Section | Pull limit | Squeeze limit | Stiffness E | Mass | Price |
|---|---|---|---|---|---|---|
| Timber | 150 x 150 mm | 450 kN | smaller of 450 kN and π²EI/L² | 12 GPa | 11.2 kg/m | $50/m |
| Big timber | 250 x 250 mm | 1,250 kN | smaller of 1,250 kN and π²EI/L² | 12 GPa | 31.2 kg/m | $120/m |
| Steel | 150 mm square tube, 8 mm wall | 1,136 kN | smaller of 1,136 kN and π²EI/L² | 200 GPa | 35.7 kg/m | $150/m |
| Big steel | 250 mm square tube, 10 mm wall | 2,400 kN | smaller of 2,400 kN and π²EI/L² | 200 GPa | 75.4 kg/m | $320/m |
| Cable | 40 mm wire rope | 1,000 kN | 0 (goes slack) | 160 GPa on 754 mm² | 6.0 kg/m | $40/m |

Timber strength 20 MPa both ways; steel yield 250 MPa (A36). Squeeze limits shown on the beam info chip, e.g. Timber 4
m: 312 kN, 5.66 m: 156 kN, 8 m: 78 kN. Every joint $300 (gusset plate), the two abutment joints included; the abutment
seats are free. Prices are game prices set for play, not quotes; the panel says so in its tip.
Trucks (axle offsets behind the front axle, tonnes; drawn at true length; speed 5 m/s on `Go`):

| Truck | Axles | Total | Length |
|---|---|---|---|
| Pickup with hay | 0 m: 1.4; 3.7 m: 1.6 | 3.0 t (6,600 lb) | 5.8 m |
| School bus | 0: 4.6; 6.1: 9.0 | 13.6 t (30,000 lb) | 11.6 m |
| Fire engine | 0: 8.2; 5.0: 5.9; 6.3: 5.9 | 20.0 t (44,100 lb) | 10.0 m |
| Grain truck | 0: 8.0; 5.5: 7.71; 6.8: 7.71 | 23.4 t (51,600 lb) | 9.4 m |
| Semi with grain trailer | 0: 5.44; 5.5: 7.71; 6.8: 7.71; 17.0: 7.71; 18.3: 7.71 | 36.3 t (80,000 lb) | 21.0 m |

Truck info chip (tap the truck): the weight, "each side carries half", and one fact: pickup "Loaded, more of a pickup's
weight rides on the back axle."; bus "Full-size school buses are Class 7: 26,001 to 33,000 pounds."; fire engine "A
pumper must carry at least 300 gallons (1,136 liters) of water."; grain truck "The Federal Bridge Formula allows about
23.9 t on three axles this close."; semi "80,000 pounds is the most the federal law allows on the Interstate."
Promises (Bridge), each off until ticked: Farmer "Carry the loaded grain truck (23.4 t)" (grain truck icon); Fire chief
"Carry the fire engine (20.0 t)"; School district "Carry the school bus (13.6 t)"; Trout biologist "Nothing in the
stream" (no footing below the high-water line); Canoe club "Keep the canoe opening clear" (no beam through the box);
County "$9,000 or less, every beam at 2/3 of its limit or less with the heaviest promised truck" (the pickup when no
truck is promised).
Promises (Tower): Water district "40 psi or more at the taps" (water surface = top joint + 3 m; 40 psi needs 28.1 m, so
the top joint must be 26 m or higher on the 1 m grid); Weather "Hold the tank in a 50 m/s wind"; Earthquake "Ride out
the Valley quake" (0.30 g, 1.20 a second, 15 s).
Old farm bridge (Yard sample, read only, can be opened and changed as a copy): timber Howe truss 2 m deep, deck joints
every 4 m, top joints (4,2) to (20,2), end posts (0,0)-(4,2) and (24,0)-(20,2), verticals at x = 4 to 20, diagonals
(4,0)-(8,2), (8,0)-(12,2), (12,2)-(16,0), (16,2)-(20,0). $7,442. Card note: "Built for horses and Model Ts. Holds the
fire engine. The farmer says it groans under his grain truck."
Tower world. Shake table x -6 to 6 at y = 0; any joint on the table top is pinned to it. Wind from the left. Top load
sits on the highest joint (split over two if they share the highest height): Bell 2,000 kg (drag area 1.5 m², drag
coefficient 1.2), Tank 8,000 kg (8,000 L of water; 9.0 m², 0.8). Members drag coefficient 2.0 on their width (timber
0.15 or 0.25 m, steel 0.15 or 0.25 m, cable 0.04 m) times their height span. Wind speed at height z: v(z) = v₁₀
(z/10)^(1/7), z at least 2 m; pressure ½ρv² with ρ = 1.225 kg/m³. Cables in towers are installed with 100 kN of pull.
Damping 5% of critical.
Tap pressure: p = 1000 × 9.81 × (top joint + 3 m); 1 psi = 6.895 kPa. Examples: top 10 m: 128 kPa (18.5 psi); 20 m: 226
kPa (32.7 psi); 26 m: 284 kPa (41.3 psi); 30 m: 324 kPa (47.0 psi).

## Interactions in detail
Building (both modes). Drag from a joint to an empty grid point: a new joint and beam of the selected piece; to another
joint: a beam. Drag a joint that is not a support: it moves, its beams follow, blocked (red flash, click) if a beam
would pass 12 m (cable 30 m) or go underground. Tap a beam: it becomes the selected piece. `Erase`: tap a beam to remove
it; a joint with no beams goes too (supports and the deck's end joints stay). Crossing beams do not connect (one lies in
front of the other). Same pair twice is refused. Keyboard: arrows move a grid cursor, Enter starts and ends a beam,
Delete erases the beam under focus, 1 to 5 pick the piece. Undo and Redo keep 50 steps. At 60 members or 40 joints: the
new beam rubber-bands back with a dull thunk and the hint says "The yard is out of members (60). Erase one to add one."
Live forces. Whenever the design, truck or truck position changes, the solver runs that frame: direct stiffness method,
two directions per joint, beams carry only pull or squeeze, own weight lumped at the ends, axle loads shared between the
two deck joints around each axle by distance.
Cables: start all active; re-add a slack cable whose ends spread apart, else drop the most squeezed active cable; repeat
(at most 2 x cables times). A design whose stiffness has a free motion (smallest eigenvalue below 1e-9 of the largest,
or a zero pivot) is loose: its free motion is drawn by shivering the loose joints and the test becomes a collapse.
Use = force / limit (pull limit for pull; squeeze limit for squeeze; a squeezed cable is slack, use 0). Colors by use: 0
to 30% faint, 30 to 70% clear, 70 to 90% bright and thicker, 90 to 100% pulsing, over 100% fails.
Truck. Drag it along the road from x = -14 to 44 (front axle); it stays where dropped, live forces follow. `Go` drives
from the left bank at 5 m/s until the last axle passes x = 26, then the pass bell; the truck drives off right and rolls
back in from the left after 1 s. Every control stays live during a run: a new truck swaps at the same spot, an erased
beam is gone that frame (and may collapse the bridge), a piece swap re-solves at once.
Failure. When a member first passes 100%: time slows to 0.2 for 2.5 s. Buckle: the beam bows sideways as a half sine
growing to 30% of its length over 1.2 s with a rising creak, then a crack. Snap: the beam splits at its middle and the
halves recoil with a twang. The member is removed and the solver runs again; if the rest holds, the run continues at
full speed (members may fail one after another). If loose, the collapse runs on the explicit engine (below): joints fall
under gravity, the truck rides the deck piece under it until that piece tilts past 20 degrees, then slides and falls,
splash at the water line. `Rebuild` restores everything. A collapse never loses the design.
Worst spots. Runs the chosen truck across in 0.05 m steps without animation (under 1 s for 60 members) and labels each
beam with its worst use and a small tick on the deck where the truck was then. Beam colors show the worst use. Any edit
refreshes it.
Promises. Ticking a row adds a column to the Yard table and a live tick or cross; a cross names the reason ("Footing at
(4, -4) is in the stream", "Worst beam 99.6% with the grain truck: over 67%").
Tower: build up from the table. Pluck: drag the top joint sideways (up to 1 m, drawn 20 times bigger) and let go: free
sway at the lowest sway rate, decaying with 5% damping; the readout counts sways and shows "Sway: 0.77 a second (1.30 s
each)". `Shake`: the table moves with acceleration A g sin(2πft), ramping up over 2 s, for 15 s; a time bar fills; the
table slides (drawn at true size), sway drawn 5 times bigger (label). Each run adds a dot to the resonance chart (x:
shake speed 0.4 to 4, y: biggest top sway in cm; dots of the current design only, cleared on a design change, kept with
the design in the Yard), and a dashed line marks the tower's own sway rate once plucked. Wind: the static wind load with
height is solved every frame with gusts drawn between 70% and 100% of the slider (the check uses the slider value); the
tower leans (20 times bigger, label).
Tower engine. While whole: modal superposition with the lowest 6 modes of K φ = ω² M φ (lumped masses: half of each
member at each end, 20 kg per joint plate, the top load), 5% damping, 1 ms steps (16 per frame), member forces from the
displacements plus gravity. On the first failure (or a cable falling below 0 kN): switch to the explicit engine: central
differences on joint positions, beam forces from current lengths and directions (so large motion and collapse are real),
Rayleigh damping matched to 5% at the two lowest modes, cables only pull, time step from the stability limit, at most
600 steps per frame; when more are needed, the scene runs in slow motion (shown as "slow motion" on the stage). The
Bridge collapse uses the same explicit engine with gravity only.
Yard. `Save to Yard` stores the design, its promises and its test results. Borrow: with a design open, tap a Yard card
and `Borrow`: its beams appear as a pink ghost over the stage (joints matched by position); tap ghost beams to adopt
them (new joints come along), `Borrow all`, `Done`. Saved on this device (localStorage `curio-span-and-spire`, wrapped
in try/catch; if storage fails the Yard still works for the session and says "Not saved on this device").
Reset: `New` asks first; mode switches keep each mode's design and test state.
Budget: 60 members and 40 joints per design. A 55-member bridge crosses the semi in 0.05 m steps in under 1 s in Python;
the build must keep a frame under 16 ms on a school Chromebook at 60 members during a collapse.

## Look
Chrome: dark blueprint night. --paper #0f1a24, --panel #16232f, --ink #eef3f7, --muted #a7b6c2, --line #2b3d4c, --focus
#7aa2ff, accent --brand #ff6fae (survey-flag pink; dark text on it #2a0614). Neighbors: zipline gold
#d0c440, reserve-designer #ff4a2e, water-shapes-earth #58acac, model-mechanic #a3e635, orbit-lab #a9c4ff: all
different.
Forces: pull #3fc8ff (cyan), squeeze #ffab2e (amber), failing white #fff4e0 with a #ff5a5a edge. Pull and squeeze have
the same brightness on purpose, so color is never the only signal: pulled beams draw as a single line with small outward
arrowheads at both ends and fine stretch dashes that drift outward; squeezed beams draw as a double line with inward
chevrons. Slack cables draw wavy and gray. Pieces by line: timber wide with a wood-grain dash in #b98a56 under the force
glow, steel narrower with a center highlight, cable thin.
Contrast (WCAG): ink on paper 15.75:1, ink on panel 14.29:1, muted on paper 8.47:1, muted on panel 7.69:1, pink on paper
6.82:1, dark text on pink 7.17:1, cyan on paper 9.15:1, amber on paper 9.31:1, focus on paper 7.07:1, red edge 5.75:1.
Labels over the painted scene sit on
#0f1a24 chips at 85% opacity. Scenes: Bridge at dusk (teal sky to peach horizon, warm lamplight in a far farmhouse);
Tower at bright noon (blue sky, pale concrete yard). Distinct from each other and from the chrome.
Shine. Joints are small gusset plates that glint when touched. The truck's wheels show a turning hub mark; the deck dips
under each axle (sag 20 times bigger). At over 70% a beam hums; over 90% it pulses. Buckling bows in slow motion; snaps
recoil. Splash and ripples on a fall; dust puff when a tower hits the table. Wind streaks and windsock; the shake table
slides with a low thump on each swing.
Sound (Web Audio, kit Sound): place joint: wood knock (timber), clank (steel), short twang (cable) whose pitch rises
with that cable's pull (mapped to 200 to 800 Hz, not the cable's real, too-low pitch); engine hum (low-passed sawtooth,
lower for heavier trucks, pitch with speed); creak (filtered noise grains, louder with the worst use over 70%); buckle:
falling "bwong" plus crack; snap: noise burst and high ping; splash: low-passed noise; pass: three rising bell tones;
tag: stamp thunk; shake: low thump per table swing; wind: filtered noise, louder with speed.

## Art
All local FLUX, no people (trucks have dark tinted windows). Text on signs stays blank.
- sas-hills: dusk farm valley far hills, fields, a distant farmhouse with one warm window, teal-to-peach sky, empty
  foreground; 16:9; no cutout; Bridge backdrop behind the terrain.
- sas-bank: cross-section of creek bank soil, roots and rounded river rocks, full frame texture; 1:1; no cutout; clipped
  to the terrain polygon.
- sas-grass: strip of meadow grass tufts and clover seen from the side; 5:1; cutout; along the bank tops.
- sas-abutment: weathered concrete bridge seat block, side view; 1:1; cutout; at (0, 0) and (24, 0).
- sas-footing: small square concrete footing block, side view; 1:1; cutout; at each footing.
- sas-pickup: red farm pickup truck with hay bales in the bed, side view facing right, dark tinted windows; 16:9;
  cutout; truck.
- sas-bus: yellow full-size school bus, side view facing right, dark tinted windows, blank side panel; 4:1; cutout.
- sas-fire: red fire engine pumper, side view facing right, dark tinted windows, blank door panel; 16:9; cutout.
- sas-grain: green farm grain truck with a full open box of golden grain, side view facing right; 16:9; cutout.
- sas-semi: blue semi tractor pulling a grain hopper trailer, side view facing right, dark tinted windows; 5:1; cutout.
- sas-hook: steel crane hook on a short cable, side view; 9:16; cutout; lifts a fallen truck back.
- sas-splash: white water splash burst; 1:1; cutout; at a fall.
- sas-canoe: green canoe floating side view; 4:1; cutout; under the canoe opening and on its promise.
- sas-trout: rainbow trout side view; 4:1; cutout; Trout promise and tag 17.
- sas-ledger: open county ledger book with blank ruled pages; 4:3; cutout; County promise.
- sas-yard: open-air shake table test yard at noon, distant brown hills, steel reaction wall at one side, empty center;
  16:9; no cutout; Tower backdrop.
- sas-table: wide steel shake table platform on hydraulic actuators, side view; 5:1; cutout; slides during shakes.
- sas-tank: round steel water tank on a short skirt, side view, blank sides; 1:1; cutout; top load.
- sas-bell: bronze bell hanging in a small wooden frame; 1:1; cutout; top load.
- sas-sock-limp: orange windsock hanging limp on a pole; 3:4; cutout.
- sas-sock-full: orange windsock streaming straight out on a pole; 3:4; cutout.
- sas-cloud-a, sas-cloud-b: soft white cumulus clouds; 16:9; cutout; drift with the wind.
- sas-dust: tan dust puff; 1:1; cutout; when tower pieces hit the table.
- sas-tap: kitchen faucet running water; 1:1; cutout; Water district promise and tag 25.
- sas-quake: cracked dry ground with a small fault line; 4:3; cutout; Earthquake promise.
- sas-card: a timber truss bridge over a farm creek at dusk with a water tower on the far hill; 16:10; no cutout; tool
  card and preview.

27 images. Beams, joints, water, grid, charts, ghosts, tags and all labels are code (beams must bend, buckle and
recolor).

## Voice
Bank `firm-captain`, restyled: "Say firmly but kindly, like a county bridge inspector calling a load test." (neighbors
use big-sister, warm-teacher, wise-mentor, gravel-ranger, easy-coach, clear-teacher, friendly-dad; none uses it.) Most
text is read on screen; lines only where they help. Event line ids: every line marked event below.
- bWelcome (how; Bridge entry, valid when no run is playing; stale after the first test): "Press Go to send the pickup
  across. Or drag the truck onto the road."
- bBuild (how; after the first fold; stale once a beam was added): "Drag up from a joint to add a beam. Triangles hold
  their shape."
- bLoose (event; a test finds a loose design; stale when nothing is loose): "Those shaking joints are loose. Close a
  triangle with a beam."
- bGap (event; Go with a gap in the road): "The road has a gap. Add a beam along the road."
- bPass (event; each completed crossing, one clip per truck): "The pickup made it across." / "The school bus made it
  across." / "The fire engine made it across." / "The grain truck made it across." / "The semi made it across."
- bBuckle (event; first failure is a buckle): "A squeezed beam buckled."
- bSnap (event; first failure is a snap): "A stretched beam snapped."
- bSlack (event; a collapse caused by slack cables): "The cables went slack. A cable can pull but never push."
- bWorst (how; first `Worst spots`): "Each beam shows its hardest moment as the truck crosses."
- bPromise (how; first tick in Promises): "Tick the promises your bridge must keep. The Yard scores them."
- bLimit (event; member or joint limit hit): "The yard is out of members. Erase one to add one."
- tWelcome (how; Tower entry): "Drag up from the table to build. Then press Shake or turn on the wind."
- tPluck (how; first time a tower stands with a top load; stale after a pluck): "Drag the top sideways and let go to
  feel its sway."
- tFold (event): "No triangles, so it folded."
- tShakeFail (event): "It shook apart."
- tWindFail (event): "The wind pushed it over."
- tHold (event; a full 15 s shake held): "It rode out the shake."
- tResonance (event; first failure within 15% of the sway rate): "The table shook at the tower's own sway speed. That is
  resonance."
- yWelcome (how; Yard entry): "Tap up to three designs to compare them. Tap Borrow to copy parts."
- tag (event; each new tag): "New inspection tag."
Read speaks the hint. No line names a disabled control (`Rebuild` only after a collapse).

## Family engine
none. The truss solver, modal and explicit engines live in the tool.

## Teacher note
Three ways to use a period: free play (ten minutes, then ask "what did you figure out about squeezed beams?"); a goal
set (tags 5 to 11 one day, 19 to 24 another); a challenge for the room ("Every promise for the least money": students
save, the class compares Yard costs on the board; ours was $8,364). Reaches MS-ETS1-1 to 4 and HS-ETS1-2 to 4. No
worksheets.

## Sources
- Truss analysis by the direct stiffness method, pin joints, axial members: Hibbeler, Structural Analysis (any edition),
  chapter "Truss analysis using the stiffness method"; MIT OCW 1.050 Solid Mechanics lecture notes on trusses.
- Euler buckling P = π²EI/L² for pinned ends: OpenStax University Physics Volume 1, 12.4 (elasticity) and any mechanics
  of materials text (Gere and Goodno, chapter 11).
- Steel A36 yield 250 MPa, E 200 GPa: ASTM A36; AISC Steel Construction Manual. Timber E about 12 GPa, design strength
  near 20 MPa for a simplified single value: USDA Forest Products Laboratory, Wood Handbook (FPL-GTR-282, 2021),
  chapters 5 and 7 (Douglas fir; the tool uses one value both ways, a simplification it states).
- Wire rope 40 mm about 1,000 kN breaking strength, E about 100 to 160 GPa on metallic area: manufacturer tables (e.g.
  Bridon-Bekaert Oil and Gas / Crane rope catalog); 1,000 kN used as the failure value.
- Federal weight limits 80,000 lb gross, 20,000 lb single axle, 34,000 lb tandem, and the Bridge Formula W = 500(LN/(N -
  1) + 12N + 36): 23 CFR 658.17; FHWA "Bridge Formula Weights" (FHWA-HOP-06-105),
  https://ops.fhwa.dot.gov/freight/publications/brdg_frm_wghts/
- Vehicle weight ranges (pickup, bus, fire engine): FHWA vehicle weight classes (Class 2 to 8), US DOE Alternative Fuels
  Data Center "Vehicle Weight Classes and Categories", https://afdc.energy.gov/data/10380. Axle splits are typical
  values chosen inside the legal limits (all single axles ≤ 9.07 t, tandems ≤ 15.42 t).
- Roller bearings at one end of a bridge: FHWA Bridge Inspector's Reference Manual (FHWA NHI 12-049), bearings chapter.
- Pratt counters (crossed diagonals in middle panels): Historic American Engineering Record, "Trusses: A Study of the
  Historic American Engineering Record" (1976, HAER), Pratt truss entry.
- Wind speed profile power law with exponent 1/7 over open land and q = ½ρv²: ASCE 7 commentary; NASA Glenn air density
  1.225 kg/m³ at sea level. Drag coefficients 2.0 (square sections) and 0.8 (short cylinder): Hoerner, Fluid-Dynamic
  Drag (1965). Saffir-Simpson: Category 1 starts at 74 mph (33 m/s), Category 5 at 157 mph (70 m/s): NOAA NHC,
  https://www.nhc.noaa.gov/aboutsshws.php
- Modal analysis, base excitation, 5% damping as the usual structural value: Chopra, Dynamics of Structures, chapters 2,
  6 and 13; ASCE 7 design spectra assume 5%. Large outdoor shake tables exist: UC San Diego LHPOST (7.6 x 12.2 m).
- Fire pumper water tank at least 300 gallons: NFPA 1901, Standard for Automotive Fire Apparatus.
- Water pressure 9.81 kPa per meter of head; 1 psi = 6.895 kPa: OpenStax College Physics 2e, 11.4.
- Checks run (Python, numpy and scipy, 2026-10-29; the same rules as the spec: half truck per side, slab 2.0 kN/m,
  member self weight, lever-rule axles, cable slack loop, 0.05 m truck steps). Worst use per truck (Pickup, Bus, Fire,
  Grain, Semi): bare deck: loose for every truck. Pratt 4 m timber $8,297, 21 members, 12 joints: 30.4, 65.4, 83.3,
  95.0, 99.6 (end post (0,0)-(4,4), 155 kN against 156, front axle at 22.3 m: just passing). Pratt 5 m: 35.5, 76.1,
  96.9, 110.5, 115.8. Pratt 6 m $9,263: 42.6, 90.9, 115.6, 131.8, 138.1 (end post buckles first at front 8.2 m: the
  failing bridge). Pratt 2 m: 37.4, 78.4, 100.4, 114.4, 112.1. Old farm bridge (Howe 2 m) $7,442: 33.7, 72.1, 91.5,
  103.8 (top chord (8,2)-(12,2), 313 kN against 312 at front 12.9 m), 107.1. Pratt cable diagonals $8,071: 30.1, then
  loose from bus front 4.7 m. Howe cable diagonals: loose under own weight. Crossed cables $8,976, 25 members: 30.4,
  65.4, 83.3, 95.0, 99.6; 6 of 8 cables go slack during the semi, 10 slack switches. Warren 4 m timber $8,783, 23
  members: 18.9, 39.4, 50.4, 57.4, 56.3. Warren shoestring (deck and diagonals (2,4)-(4,0), (6,4)-(8,0), (16,0)-(18,4),
  (20,0)-(22,4) as cables) $8,364: 18.7, 39.2, 50.2, 57.2, 56.0 (found by trying each member as a cable). Pratt 2 m + 5
  m timber pier at (12,-5) $9,992: 21.6, 43.3, 56.8, 63.6, 65.2. Pratt 1 m with Big timber top chord and diagonals
  $9,939: bus 102.4 (bottom chord snaps: tag 4). Pratt 6 m with Big timber end posts $10,273 and with braced end posts
  $10,224: both 12.9, 26.6 (26.5), 33.9, 38.6 (38.5), 37.8. Largest design tried: 12 panels, 3 m deep, crossed cables,
  55 members, 24 joints, $14,656: semi 53.7, 169 positions in 0.68 s in Python. Bridge Formula: grain truck 6.8 m, 3
  axles: 52,732 lb (23.92 t); semi 18.3 m, 5 axles: 85,525 lb, capped at 80,000. Dead load alone: 20 to 29% use.
- Tower checks (lumped masses, 20 kg joint plates, tank 8 t): ladder without diagonals loose. 20 m, 2 m wide timber, 40
  members: sway 0.77 a second (1.30 s), wind 50 72%, wind 70 132%; 0.30 g at 0.8: fails at 1.9 s (440%); at 1.4: 36%. 4
  m wide: 1.43, wind 70 72%, 0.8: 53%, 1.4: fails 2.1 s (273%). Steel 2 m: 1.36, 1.4: fails 2.5 s (217%). Empty top:
  4.32, 0.8: 4%. Bell: 1.47, 1.4: fails 3.5 s (129%). 10 m 2 m wide timber tank: sway 2.04, wind 70 46%. 30 m, 60
  members, 32 joints: 2 m wide 0.42 (wind 50 143%); 4 m wide (wind 70 141%); stepped 6 m to 10 m height, 4 m to 20 m, 2
  m to 30 m: wind 70 98% (tag 22, just). 26 m town tower, wind 50 and 0.30 g at 1.20 for 15 s: straight 2 m timber 111%
  / 28%; stepped timber (6 m wide to 8 m, 4 m to 18 m, 2 m above) 45% / 227%; straight 2 m with Big timber legs 50% /
  36%; 4 m then 2 m (step at 12 m) timber 61% / 52%. Guy wires on the 20 m tank tower (cables to (-6,0) and (6,0), 100
  kN pull): sway 1.91, 0.8: 43%, 1.4: 120% (explicit engine). Explicit and modal engines agree within about 10% (2 m
  timber tank, 0.8: 393% and 440%; 1.4: 37% and 36%; steel 1.4: 204% and 217%); the explicit steel tower falls 5.3 m
  sideways within 8 s after one member fails. A slow frequency sweep was tried and dropped: its peak lags the true sway
  (0.77 read as 1.0 to 1.06), so the tool uses Pluck and the per-run resonance dots instead.
- Reference shapes in these checks: Pratt with depth h: deck joints every 4 m, top joints (4,h) to (20,h), end posts
  (0,0)-(4,h) and (24,0)-(20,h), verticals at x = 4 to 20, diagonals (4,h)-(8,0), (8,h)-(12,0), (12,0)-(16,h),
  (16,0)-(20,h); Howe mirrors the diagonals; Warren: top joints (2,4) to (22,4), zigzag diagonals, no verticals. Towers:
  two legs, a rung every 2 m, one diagonal per panel, alternating.
- Tap pressure: 10 m 128 kPa (18.5 psi), 20 m 226 (32.7), 26 m 284 (41.3), 30 m 324 (47.0); 40 psi needs 28.1 m of
  water.

## Done when
1. The bare deck folds under the pickup within 1 s of `Go`, loose joints shiver, the truck splashes and the hook returns
   it; a fresh player with no instructions gets the pickup across within two minutes.
2. Pratt 4 m timber (Sources) with the semi: Worst spots labels the end posts 99.6% and the crossing passes; Pratt 6 m
   with the fire engine: the end post bows in slow motion near front 8.2 m and the bridge falls.
3. Warren 4 m timber shows $8,783, grain 57.4% and semi 56.3%; the shoestring version shows $8,364 and keeps all six
   promises; Pratt cable diagonals fold under the bus; crossed cables draw slack cables wavy during the semi and hold.
4. Tower: the 20 m, 2 m wide timber tank tower plucks at "0.77 a second", fails 0.30 g at 0.8 within about 2 s, holds
   1.4 for 15 s; the 4 m wide one fails at 1.4; the resonance chart shows each run's dot.
5. Focus: the bridge and truck (Bridge) and the tower (Tower) are the biggest thing at 1366x768 and in the 680x425
   preview; `Go`, the truck row and the piece row are visible without scrolling at every STANDARDS size.
6. A tap while a run plays: swapping the truck, erasing a beam or changing a piece re-solves in the same frame; moving a
   shake slider changes the table's motion at once.
7. 60 members and 40 joints stay at 60 frames a second on a school Chromebook through a collapse; the limit message
   shows at member 61.
8. How lines play once per load, then hint only; event lines each time; no line names `Rebuild` before a collapse.
9. Tags stamp on their exact checks, survive a reload (Save on this device), and the Yard compare table fills with `Test
   all`.
10. A fresh player with no instructions is still choosing to play after 10 minutes, and can name one thing they figured
    out.

## Open questions
1. Shake options: sine only (as specced), or add one real earthquake record (for example El Centro 1940, public domain)
   as a button? It is more vivid but needs a data file and its own checks.
2. Prices are game prices. Keep, or swap for rough real costs per meter (bigger numbers, same lessons)?
3. The Old farm bridge sample shows one working truss shape in the Yard from the start. Keep it (good story, a reason to
   test before replacing) or hide it until the first save?

