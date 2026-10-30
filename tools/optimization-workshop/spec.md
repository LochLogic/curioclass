# Optimization Workshop

## One idea
On each workbench you build a real design by dragging one measurement (where to cut, how wide to fence, where to
dive in), every try drops a dot on a graph of the goal, and the derivative's zero shows the best design before your
dots reach it; a second bench moves one part at a steady speed and the derivative tells how fast the linked part moves.

## Not like
- speedometer (this group): the derivative as a speed on a dial, and the rules. Here the derivative is a tool for deciding: where it is zero, the design is best; in related rates, it links two speeds.
- packaging-challenge (gr 10, builder): surface area and volume of packages with formulas, no calculus. Here the best package is found with a derivative, and a price change moves it.
- zoom-to-the-limit (this group): rates at a point, no decisions.
- rain-gauge and solid-spinner (this group): integrals.
- launch-pad (gr 9, graphing): the maximum of a quadratic from its vertex; here maxima and minima of non-quadratic goals, with endpoints checked.

## Who and how
Grade 12, AP Calculus (Applications of Derivatives). Students drive, alone or in pairs, 30 to 45 minutes. Explore
first: the Best design bench opens on the barn fence with the slider live and no goal shown until `Show goal`.
Topic line: "optimization and related rates".
Standards: AP-CALC.U4 (4.4 and 4.5 related rates: the ladder, balloon and shadow; local linearity and L'Hospital's rule,
also in Unit 4, are not in this tool), AP-CALC.U5 (5.2 extreme value theorem and endpoints, 5.3 to 5.5 critical
points and the first derivative test, 5.10 to 5.11 optimization).
tool.json: driver "students", minutes "30-45", modes ["Best design", "Moving parts"].

## Screens and modes
Header (kit, 9-12 theme): "Optimization Workshop", small line "Build it, graph it, prove it." Modes `Best design`,
`Moving parts`; kit `Motion`, `Sound`, `Read`.

### Best design (default)
Focus: the bench scene (left) and the goal graph (right) as one pair, each at least 40 percent of the stage width and
together filling it, with the measurement slider directly under them; the work card opens in the panel, never over the
pair. Below 1000 px wide the scene sits above the graph, both still above the slider.
Each scene is a painted backdrop or texture (Art) with the design's shape drawn to scale in code over it, so it can
bend with the measurement: the fence along the barn (barn-field), the flat sheet and folded box (cardboard texture
clipped to the faces), the can (tin texture clipped to the side and lids), the poster (poster-print cropped to the
printed part, inside a white margin drawn in code), the beach (beach-top, with the lifeguard-stand at the start, the
swimmer in the water and the rescue-buoy at the entry point). Dimension lines and labels are drawn in code on small
dark chips.
Project picker: `Barn fence`, `Open box`, `Soup can`, `Poster`, `Lifeguard`.
- One slider for the design's measurement (with a number box). The scene redraws to scale as it moves; readouts show
  every dimension and the goal value with units.
- `Try this` (or Enter, or releasing the slider) drops a dot on the goal graph at (measurement, goal) and logs it.
  The best try so far is ringed.
- `Show goal`: shows the challenge line ("Make the box hold more than 1,950 cm³.") and ticks it when a try meets it.
- `Prove it` opens the work card: the goal as a function of the measurement, its derivative, the critical points
  (zeros of the derivative inside the allowed range), the candidates table (each critical point and each endpoint
  with its goal value), a sign chart of the derivative (+ then - means a maximum), and the answer. It also draws the
  whole goal curve and the derivative curve (second engine series, its own dash) on the graph.
- The soup can has a `Lid price` slider (lids cost 1 to 4 times the side metal per cm², step 0.5): the best can
  changes shape (h = 2 x price x r), and the graph's curve redraws.

### Moving parts (related rates)
Focus: the rig scene, center stage and largest, with the live rates readout directly under it; the small rate graph
and the rate slider in the panel.
Rig picker: `Ladder`, `Balloon`, `Shadow`. Each rig has one driven part that moves at a steady rate (`Run`, `Pause`,
`Reset`, and a rate slider), and one linked part. Scenes: the ladder cutout leaning on the brick-wall backdrop (placed
and turned in code so its ends touch the wall and the floor); the balloon cutout scaled to its radius, with the pump
hose in code; the street-lamp and delivery-robot cutouts on the street-dusk backdrop, with the light ray and the
shadow drawn in code.
- Live readouts: the driven quantity and its rate, the linked quantity and its rate, and the related-rates formula
  with numbers ("dy/dt = -(x/y) dx/dt = -(3/4)(0.5) = -0.375 m/s"), with the measured rate beside it (Interactions).
- `Freeze at` box: stops the rig when the driven quantity reaches a value, to read the rates at that instant.
- A small rate graph plots the linked rate over time.

## Content
Best design projects (measurement, range, goal, best, challenge):
- Barn fence: 40 m of fence makes three sides of a pen along a barn wall. x = width of the two sides that meet the barn,
  0 to 20 m. Area A(x) = x(40 - 2x). A'(x) = 40 - 4x = 0 at x = 10. Endpoints give 0. Best: 10 m by 20 m, 200 m².
  Challenge: "Fence more than 190 m²."
- Open box: cut equal squares of side x from the corners of a 30 cm by 30 cm sheet and fold up. 0 to 15 cm.
  V(x) = x(30 - 2x)². V'(x) = (30 - 2x)(30 - 6x) = 0 at x = 5 (x = 15 is an endpoint, V = 0). Best: 5 cm cut, 20 by 20
  by 5, 2,000 cm³. Challenge: "Hold more than 1,950 cm³."
- Soup can: a closed cylinder holding 355 cm³. Measurement r, 1 to 8 cm; h = 355/(πr²). Goal: metal cost
  C(r) = p x 2πr² + 2πrh = p x 2πr² + 710/r, with p the lid price (sides cost 1 per cm²). C'(r) = 4πpr - 710/r² = 0 at
  r = (355/(2πp))^(1/3). Best at p = 1: r = 3.84 cm, h = 7.67 cm, C = 277.5 (the plain surface area, cm²). At p = 2:
  r = 3.05 cm, h = 12.18 cm, C = 349.7. Always h = 2pr. Challenge: "At lid price 1, use under 280 cm² of metal."
- Poster: the printed part must be 300 cm², with 3 cm margins top and bottom and 2 cm at each side. w = printed width,
  5 to 40 cm. Paper P(w) = (w + 4)(300/w + 6). P'(w) = 6 - 1200/w² = 0 at w = √200 ≈ 14.14 cm, printed height 21.21 cm,
  paper 493.7 cm². Challenge: "Use under 500 cm² of paper."
- Lifeguard: a lifeguard on the sand 30 m from the water's edge sees a swimmer 20 m out, 80 m down the beach. Runs
  6 m/s on sand, swims 2 m/s (made-up speeds). x = where along the edge to enter the water, 0 to 80 m. Time
  T(x) = √(x² + 900)/6 + √((80 - x)² + 400)/2. T'(x) = 0 near x = 73.5 m (solved by the tool with bisection; no
  simple formula). Best: enter at 73.5 m, 23.75 s. Straight line (enter at 48 m): 28.30 s. Running all the way to 80 m:
  24.24 s. Challenge: "Reach the swimmer in under 24 s."
Moving parts rigs:
- Ladder: a 5 m ladder against a wall; the foot starts 0.6 m out and slides out at 0.5 m/s (rate slider 0.2 to 1).
  x² + y² = 25, so dy/dt = -(x/y) dx/dt. Freeze at x = 3: y = 4, dy/dt = -0.375 m/s. At x = 4.8 (y = 1.4): -1.714 m/s.
  The rig stops at y = 0.2 m ("The formula blows up as the top reaches the floor.").
- Balloon: air pumped in at 100 cm³/s (slider 50 to 200). V = (4/3)πr³, so dr/dt = (dV/dt) / (4πr²). Freeze at r = 10:
  0.0796 cm/s; at r = 5: 0.318 cm/s. Starts at r = 2 cm, stops at r = 15 cm. The balloon's rig clock runs 10 times
  faster than real time (shown: "rig time x10"), so a full fill takes 14 s at 100 cm³/s.
- Shadow: a street lamp 6 m tall; a delivery robot 1.2 m tall rolls away from it at 1.5 m/s (slider 0.5 to 3), from
  1 m to 16 m. Similar triangles: s/1.2 = (x + s)/6, so s = 0.25x. Shadow length grows at 0.375 m/s and the shadow's tip
  moves at 1.875 m/s, the same at every x.

## Interactions in detail
- Each project's goal function, derivative and critical points are stored as formulas (above); candidates are
  computed, not looked up, and the table prints to 3 significant figures with units. The lifeguard's critical point
  comes from bisection on T' over [0, 80] to 0.001 m.
- Slider steps: fence 0.5 m, box 0.25 cm, can 0.05 cm, poster 0.25 cm, lifeguard 0.5 m; typed values to 2 decimals.
  Endpoints are allowed and drawn (a flat pen, a flat box, a can of radius 8 that is very short).
- Challenges check the goal value of the current design, not of the best try; ticking one plays one soft tone.
- Sign chart: derivative sign on each side of every critical point, sampled at midpoints; "+ to -: maximum",
  "- to +: minimum".
- Related rates: rates in readouts come from the formula at the current instant. The measured rate (the change over
  the last 0.01 s of rig time, computed from the rig's own position at those two times) is shown beside it in muted
  text; it agrees within 3 percent while the ladder top is at least 1 m up and everywhere on the balloon and shadow.
  Below 1 m the ladder's measured value is replaced by "changing too fast to measure", which is the point of the
  ladder line.
- Run lengths: at every slider setting a full run is 30 s or less (ladder at most 22 s, balloon at most 28 s, shadow at
  most 30 s). The rig plays on its own, and `Pause`, `Reset`, the rate slider, `Freeze at` and the rig picker stay live:
  a rate change takes effect from that instant, and a new rig or `Reset` stops the run at once. With Motion off, `Run`
  steps the rig in 0.5 s jumps on each press of `Step`.
- Keyboard: sliders are range inputs (arrows one step, PageUp/PageDown ten); `Try this` on Enter.
- Mode change: `Curio.stop()`, `V.hush()`. Tries are kept per project for the page session only (not saved).

## Look
Accent (`--brand`) #2ff0b0, workshop mint (a carpenter's chalk line): 11.7:1 on --panel #141b25, 11.1:1 on --sec-bg
#18202b; --brand-ink #10161f on it 12.3:1. Greener and brighter than imaginary-island's teal #3ec9b6 and more vivid than
the algebra group's #7af0c8 (Graph Story Lab); different from the group's leaf green (slope-field-garden) and every
other group accent.
Bench scenes are painted (Art), each framed by a thin #1b1f24 border; shapes drawn over them in code use a 2 px dark
outline so they read on any backdrop. Dimension lines in the accent; labels #e8edf3 on #10161f chips (15.4:1). Goal
curve `--gr-1`, derivative `--gr-2`, try dots in the accent.

## Art
Local FLUX (`scripts/localart.py`) unless marked people. One style: sunny, clean painted illustration with soft shadows.
Every backdrop leaves room for shapes drawn in code; the code places exact lines (barn edge, water's edge, floor) over
the painted ones.
- barn-field: "Top-down view of a green grassy farm field, the long straight edge of a red barn's roof running along
  the top of the frame, soft daylight, painted illustration"; 16:10; cutout no; people no; the Barn fence backdrop
  (the fence and pen are drawn in code along the barn edge).
- cardboard: "Full-frame flat sheet of plain brown corrugated cardboard seen straight on, fine fibers, soft even light,
  painted texture"; 1:1; cutout no; people no; clipped to the flat sheet and the folded box faces (faces shaded in code).
- tin: "Full-frame brushed silver tin plate with soft vertical highlights, painted texture"; 1:1; cutout no; people no;
  clipped to the can's side and lids.
- poster-print: "A bold painted landscape of layered purple and orange mountains under a sunset sky with a winding
  river, simple strong shapes, painted illustration"; 3:4; cutout no; people no; cropped (never stretched) to the
  printed part of the poster.
- beach-top: "Top-down aerial view of a wide sandy beach meeting calm turquoise sea along a straight horizontal
  shoreline across the middle of the frame, sand in the lower half and water in the upper half, soft daylight, painted
  illustration"; 16:10; cutout no; people no; the Lifeguard backdrop (the path and the water's edge line are code).
- lifeguard-stand: "A white wooden lifeguard tower with a red roof standing on sand, seen from above at a steep angle,
  painted illustration, plain white background"; 1:1; cutout yes; people no; the start point on the sand.
- rescue-buoy: "A red rescue torpedo buoy with a coiled yellow strap, seen from above, painted illustration, plain
  white background"; 4:3; cutout yes; people no; sits at the entry point and slides along the water's edge with the
  slider.
- swimmer: "A swimmer seen from above treading water with one arm raised, wearing a bright orange swim cap, small
  ripples around, painted illustration, plain white background"; 1:1; cutout yes; people: true (Gemini,
  `scripts/art.py`, Cory reviews); the swimmer 20 m out.
- brick-wall: "A plain red brick wall rising from a smooth gray concrete floor, side view, even daylight, painted
  illustration"; 4:3; cutout no; people no; the Ladder backdrop (floor and wall lines drawn in code over it).
- ladder: "A plain wooden straight ladder with eight rungs, front view, standing upright, painted illustration, plain
  white background"; 9:16; cutout yes; people no; turned and placed in code so its ends touch the wall and the floor.
- balloon: "A round bright red latex party balloon, nearly a perfect sphere, with a small knot at the bottom and a soft
  highlight, painted illustration, plain white background"; 1:1; cutout yes; people no; scaled evenly to the radius.
- street-dusk: "A quiet sidewalk at dusk seen from the side, flat gray pavement running left to right along the bottom
  of the frame, low houses far behind under a deep blue evening sky, painted illustration"; 16:9; cutout no; people
  no; the Shadow backdrop, dimmed so the light ray and shadow read.
- street-lamp: "A tall black iron street lamp post with one glowing warm lamp at the top, side view, painted
  illustration, plain white background"; 9:16; cutout yes; people no; scaled to 6 m.
- delivery-robot: "A small white six-wheeled sidewalk delivery robot with a smooth blank lid and a tiny orange flag on a
  thin pole, side view, painted illustration, plain white background"; 1:1; cutout yes; people no; scaled to 1.2 m,
  rolling away from the lamp.
Fence, folded box, can outline, poster margins, paths, dimension lines, light rays, shadows, graphs, sign charts and
preview.svg are drawn in code: they are diagrams and shapes that bend with the measurement.

## Voice
`friendly-dad` (Achird), style "Say in a relaxed, friendly way, like a dad working on a project in the garage." Not
used by a group sibling or another spec in batch R05; polynomials-as-numbers (gr 9) also uses it, and every bank voice
suited to grade 12 is taken by some math neighbor, so it stays. `Curio.voice`, `scope: () => state.mode`. Readouts and
the work card are read on screen; Read speaks the hint.
- design (how, Best design welcome; stale on the first try): "Drag the slider to build a design, then press Try this. Each try puts a dot on the graph."
- prove (how, first Prove it; stale on a project change): "The best design is where the derivative is zero, or at an end. The table checks every candidate."
- goal (event, a challenge met; stale on a new project): "That meets the goal."
- lid (how, first Lid price change; stale on a project change): "Pricier lids make the best can taller and thinner."
- parts (how, Moving parts welcome; stale once Run is pressed): "Pick a rig and press Run. One part moves at a steady speed. Watch how fast the other part moves."
- freeze (how, the first run ends or is paused; stale once Freeze at is used): "Type a value in Freeze at and press Run again. The rig stops right there so you can read the rates."
- ladder (event, the ladder rig passes y = 1; stale on Reset): "The top is falling faster and faster as it nears the floor."

## Family engine
none. Uses `kit/graphing.js` `Plane` as a plotting tool for the goal graph and rate graph (`g.fn`, `g.point` for try
dots, `g.extrema` as a cross-check of the stored critical points, `g.roots` for the derivative's zero on the lifeguard);
benches are the tool's own SVG over the painted backdrops.

## Sources
- Optimization, extreme value theorem, critical points, first derivative test, related rates: College Board, AP
  Calculus AB and BC CED (2020), Units 4 and 5, https://apcentral.collegeboard.org/courses/ap-calculus-ab
- Worked forms of the fence, box, can and ladder problems: OpenStax, Calculus Volume 1, 4.1 "Related Rates" and
  4.7 "Applied Optimization Problems", https://openstax.org/books/calculus-volume-1/pages/4-7-applied-optimization-problems
- Sphere volume (4/3)πr³ and cylinder area: same text, and the formula sheet in the CED.
- 355 cm³ is simply the chosen can size (no real can is described); all projects, speeds and rigs are made up.
- Checks run (Python, 2026-10-29): fence 200 m² at 10, 0 at both ends; slider steps 8 to 12 meet the challenge. Box
  2,000 cm³ at 5, 0 at 0 and 15; steps 4.25 to 5.75 meet 1,950. Can: p = 1 gives r 3.837, h 7.674, C 277.5; p = 2 gives
  r 3.046, h 12.18, C 349.7; h/(pr) = 2.000 at p = 1, 1.5, 2, 4; ends cost 716.3 (r = 1) and 490.9 (r = 8, h 1.77);
  steps 3.50 to 4.20 meet 280. Poster: w 14.142, height 21.213, paper 493.71; w = 10 gives 504; ends 594; steps 11 to
  18.5 meet 500. Lifeguard: bisection gives x 73.511, T 23.746; T(48) 28.302, T(80) 24.240, T(0) 46.23; steps 68.5 to 78
  meet 24 s; at the best point sin/speed is equal in sand and water (0.1543), as Snell's law says. Ladder -0.375 at
  x = 3, -1.714 at x = 4.8. Balloon 0.0796 at r = 10 and 0.318 at r = 5. Shadow 0.375 and 1.875 m/s.
- Run-length and measured-rate checks (same day): the first draft's balloon (r 2 to 20 at 100 cm³/s) took 335 s and
  its slowest ladder (0.1 m/s) 44 s, so the balloon now stops at r = 15 with a x10 rig clock and a 50 to 200 slider
  (7 to 28 s), and the ladder starts at x = 0.6 with a 0.2 to 1 slider (4 to 22 s); the shadow takes 5 to 30 s. The
  first draft measured over 0.1 s, which missed by 6 percent at x = 4.8 and 42 percent near the floor; over 0.01 s it
  misses by at most 2.4 percent while y ≥ 1 m at any ladder speed and by at most 1.9 percent anywhere on the balloon,
  but by 8 to 30 percent below y = 0.5 m, hence the "changing too fast to measure" rule.

## Done when
1. Barn fence at x = 10 shows 200 m²; Prove it lists x = 10 (200) and endpoints 0 and 20 (0), with + to - at 10.
2. Open box at x = 5 shows 2,000 cm³; the table also lists x = 15 (0) and x = 0 (0).
3. Soup can at lid price 1 gives r 3.84, h 7.67, 277.5 cm²; at price 2 gives r 3.05, h 12.18; h = 2 x price x r both times.
4. Poster best at w 14.14, paper 493.7 cm²; w = 10 gives 504 (paper (14)(36) = 504) and does not meet the challenge.
5. Lifeguard best at 73.5 m, 23.75 s; x = 48 shows 28.30 s.
6. Ladder frozen at x = 3 shows y = 4 and dy/dt = -0.375 m/s; balloon frozen at r = 10 shows 0.0796 cm/s; shadow shows
   0.375 and 1.875 m/s at any x.
7. Try dots land where the readouts say; the best try is ringed; the scene's shape matches its dimension labels at
   every slider end.
8. Focus: at 1366x768 and 1000x625 the scene and goal graph pair (Best design) and the rig scene (Moving parts) are
   the largest thing on the stage, and the work card never covers them.
9. Tap while it plays: during a run, moving the rate slider changes the speed from that instant, `Pause` stops it at
   once, and picking another rig replaces it at once; no run lasts over 30 s.
10. How-to lines spoken once each in five actions; "That meets the goal." each time a challenge ticks; no line names a
    control that is not on screen.
11. Bench, graph and slider visible without scrolling at 1366x768 and 1280x720; stacks at 760 wide; 14 painted images,
    one with a person; no network, no em dashes.

## Open questions
- optimization-workshop: AP-CALC.U4 also holds local linearity and L'Hospital's rule, which this tool leaves out.
  Fine, or should they live somewhere else in the calculus set?
- optimization-workshop: the swimmer is the one image with a person (Gemini, waits on Cory's review). OK to keep a
  person there, or show the swimmer's spot with an object instead?
