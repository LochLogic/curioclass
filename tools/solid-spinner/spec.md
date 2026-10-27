# Solid Spinner

## One idea
A potter's wheel spins a flat region into a solid, and a wire cutter slices that solid into thin coins: each coin is a
disk or a washer whose volume is pi times (outer radius squared minus inner radius squared) times its thickness, so
stacking the coins is a sum you can see, and thinning them turns the sum into the integral that gives the exact volume.

## Not like
- rain-gauge (this group): an integral as water collected over time, sliced into time steps. Here the slices are real
  pieces of a solid you can hold up and inspect.
- cone-slicer, now Conic Focus Finder (this group): flat curves drawn with strings and pins. Here a flat region becomes
  a 3D solid by spinning.
- function-family-reunion (this group): graphs moved by parameters. Here a graph is only the edge of a region, and what
  matters is the solid it sweeps.
- rollercoaster-polynomials (gr 11, built): building a curve to meet rules. Here the curve is given (or drawn as a pot)
  and the question is how much space the spun shape holds.

## Who and how
Grade 12, AP Calculus (Applications of Integrals). Students drive, 25 to 40 minutes, alone or in pairs. Explore first:
the Shelf opens on the first piece, already spinning.
Topic line: "Volumes by disks, washers and cross sections".
Standards: AP-CALC.U8 (8.4 to 8.6 area between curves, 8.7 to 8.8 volumes with square, rectangle, triangle and
semicircle cross sections, 8.9 to 8.12 volumes by disks and washers, around the axes and around other lines).
tool.json: driver "students", minutes "25-40", modes ["Shelf", "Cross sections", "Throw a pot"].

## Screens and modes
Header (kit, 9-12 theme): "Solid Spinner", small line "Spin it, slice it, stack it." Modes `Shelf`,
`Cross sections`, `Throw a pot`; kit `Motion`, `Sound`, `Read`.

Stage: left, an engine plane with the flat region shaded and the axis of spin drawn as a dashed line; right, the solid
drawn in code as a stack of tilted ellipses (an oblique view, about 20 degrees from side on), slowly turning on the
wheel. A vertical cutting wire can be dragged along the solid; the plane shows the matching line through the region.

Layer toggles above the stage (an explorer's layers, any mix on or off): `Region`, `Solid`, `Slices`, `One slice`,
`Formula`.

Panel: the readouts for the wire's position: "x = ...", "outer R = ...", "inner r = ...", "slice area = pi(R² - r²) =
...", and below them the slice controls and the volume table.

### Shelf (explore, default)
- A shelf of nine pieces as cards with a small silhouette (Content): six lesson pieces L1 to L6 (a region and an axis)
  and three pots P1 to P3. Choosing one loads its region, axis and solid.
- The wire: drag it, or arrow keys (0.05 of the range). `One slice` lifts the coin at the wire out beside the solid
  and labels R, r and the thickness dx.
- Slices: buttons `4`, `8`, `32`, `128` and a slider 1 to 128. The solid is redrawn as that many midpoint coins
  (each coin's radius is taken at its middle). Table: n, sum of coin volumes (4 decimals), exact volume, error. Line
  under it: "Thinner coins, closer to the exact volume."
- `Formula` layer shows the integral for the piece, written out, and its exact value (for example "V = ∫ from 0 to 1 of
  pi((x+1)² - (x²+1)²) dx = 7pi/15").
- `Predict` box on each card (optional): type the exact volume as a decimal before opening `Formula`; checked within
  0.1 percent. A check mark stays on the card.

### Cross sections
- The base region lies flat on a table (seen from above, tilted); a shape choice stands slices on it perpendicular to
  the x-axis: `Squares`, `Semicircles`, `Equilateral triangles` (side or diameter across the region).
- Two bases: B1, the region between y = x and y = x² from 0 to 1 (side s = x - x²); B2, the disk x² + y² ≤ 9 (side
  s = 2√(9 - x²)).
- Same slice controls and table as the Shelf (midpoint sums). The panel names the slice area: s², (pi/8)s², or
  (√3/4)s².
- Readout "base area = ..." for B1 (1/6, the area between the curves, with its integral shown in `Formula`).

### Throw a pot (make)
- A profile with seven handles at heights 0, 2, 4, 6, 8, 10 and 12 cm; drag each handle sideways to set the radius
  (1 to 6 cm in steps of 0.5). The wheel spins the profile into a pot as you drag.
- Between handles the wall is straight, so each band is a frustum and the exact volume is the sum of frustum volumes
  pi h (R1² + R1R2 + R2²) / 3. The panel shows the coin sum next to it, so students see the slices agree.
- Readout "holds ... mL" (1 cm³ = 1 mL). `Fill` pours water in to show the volume (instant with Motion off).
- `Reset pot` returns to the starting pot.

## Content
Shelf (exact values; midpoint coin sums for n = 4 / 8 / 32 / 128; units are cubic units, or cm³ for pots):
| Piece | Region and axis | Integral | Exact | n = 4 / 8 / 32 / 128 |
|---|---|---|---|---|
| L1 Horn | under y = √x, 0 to 4, around the x-axis (disks) | pi∫x dx | 8pi ≈ 25.1327 | exact for every n |
| L2 Leaf | between y = x and y = x², 0 to 1, around the x-axis (washers) | pi∫(x² - x⁴) dx | 2pi/15 ≈ 0.4189 | 0.4349 / 0.4229 / 0.4191 / 0.4189 |
| L3 Leaf, raised | same region, around y = -1 | pi∫((x+1)² - (x²+1)²) dx | 7pi/15 ≈ 1.4661 | 1.5148 / 1.4783 / 1.4668 / 1.4661 |
| L4 Leaf, from above | same region, around y = 2 | pi∫((2-x²)² - (2-x)²) dx | 8pi/15 ≈ 1.6755 | 1.725 / 1.6878 / 1.6763 / 1.6756 |
| L5 Ball | under y = √(9 - x²), -3 to 3, around the x-axis | pi∫(9 - x²) dx | 36pi ≈ 113.0973 | 116.6316 / 113.9809 / 113.1526 / 113.1008 |
| L6 Cone | under y = x/2, 0 to 6, around the x-axis | pi∫x²/4 dx | 18pi ≈ 56.5487 | 55.6651 / 56.3278 / 56.5349 / 56.5478 |
| P1 Mug | radius 4 cm, height 10 cm (around the y-axis) | pi∫16 dy | 160pi ≈ 502.6548 | exact for every n |
| P2 Vase | radius 4 + 2 sin(pi y/15), y 0 to 15 cm | pi∫(4 + 2 sin(pi y/15))² dy | 270pi + 480 ≈ 1328.2300 | 1340.7926 / 1331.3282 / 1328.4228 / 1328.2421 |
| P3 Bowl | radius √(4y), y 0 to 9 cm | pi∫4y dy | 162pi ≈ 508.9380 | exact for every n |
L5 checks against the sphere formula (4/3)pi(3³) = 36pi; L6 against the cone formula (1/3)pi(3²)(6) = 18pi. L1 and P3
are exact for every n because R² is a straight line in x (midpoint coins over and under cancel). Pots P1 to P3 are
solids of revolution standing on the y-axis; their "holds" readout treats the solid as the pot's inside.

Cross sections (exact; midpoint sums n = 4 / 8 / 32 / 128):
- B1 squares: ∫(x - x²)² dx = 1/30 ≈ 0.03333; 0.03345 / 0.03334 / 0.03333 / 0.03333.
- B1 semicircles: (pi/8)(1/30) = pi/240 ≈ 0.01309; 0.01313 / 0.01309 / 0.01309 / 0.01309.
- B1 equilateral triangles: (√3/4)(1/30) = √3/120 ≈ 0.01443; 0.01448 / 0.01444 / 0.01443 / 0.01443.
- B2 squares: ∫ from -3 to 3 of 4(9 - x²) dx = 144; 148.5 / 145.125 / 144.0703 / 144.0044.
- B1 base area: ∫(x - x²) dx = 1/6.

Throw a pot starting profile (radii 3, 5, 6, 5, 3, 2, 3 cm at heights 0 to 12): exact volume 212pi ≈ 666.02 cm³, so
"holds 666 mL".

Spot slices for the wire: L2 at x = 0.5: R = 0.5, r = 0.25, slice area pi(0.25 - 0.0625) ≈ 0.5890. L4 at x = 0.5:
R = 1.75, r = 1.5, area ≈ 2.5525. P2 at y = 7.5: R = 6, area 36pi ≈ 113.0973.

## Interactions in detail
- Exact volumes are stored as the closed forms above (and printed both ways); coin sums are computed live from R and r
  at midpoints. Pot volumes are computed exactly from the frustum formula, so a pot's exact value is never a numeric
  estimate.
- Washers: when the axis is not on the region's edge, the panel names which curve gives R (farther from the axis) and
  which gives r (nearer), and the `One slice` coin shows the hole. For L3 and L4 the axis line is drawn and both radii
  are labeled as distances to it (for L4: R = 2 - x², r = 2 - x).
- Predict: accepts a decimal within 0.1 percent of exact; also accepts typed multiples of pi such as "7pi/15" or
  "8*pi" (a small parser for a number, optional "pi", optional "/number"). Two misses open `Formula`.
- Throw a pot: handles snap to 0.5 cm; the volume updates on every move; the coin sum uses n = 64.
- Solid drawing: each coin is an ellipse pair in SVG, shaded by the accent with a darker rim; `Motion` off stops the
  spin and the fill animation (the solid stays drawn).
- Sound: a soft wheel hum while spinning and a light tap per coin when the slice count changes; off with Sound.
- Keyboard: shelf cards are buttons; wire and handles are range inputs (arrows move one step); layer toggles are
  checkboxes in tab order before the stage.
- Mode change: `Curio.stop()`, `V.hush()`. Predict check marks per device (localStorage `curio-solid-spinner`,
  try/catch), `Clear marks`.

## Look
Accent (`--brand`) #e39b6e, kiln clay: 7.6:1 on --panel #141b25, 7.2:1 on --sec-bg #18202b; --brand-ink #10161f on it
7.9:1. Warmer and pinker than the grade 11 oranges (#ff9442, #e98a4c) and darker than Conic Focus Finder's ice blue.
Scene: a studio shelf in dim light, wall #1a1f27, shelf wood #5a4130, wheel head #6b7280, solid coins in the accent
with rims #a8663f, water #4f7fd9 at 75 percent. Region shading on the plane uses `--gr-3` at 30 percent with a
full-strength edge; the axis of spin is `--gr-4` dashed; R labels `--gr-1`, r labels `--gr-2`.

## Art
none: drawn in code (shelf, wheel, solids, coins, pots, planes, preview.svg).

## Voice
`wise-mentor` (Gacrux), style "Say slowly and warmly, like an old potter showing an apprentice." Not used by a group
sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`.
- shelf (how, Shelf welcome): "Pick a piece from the shelf. Drag the wire to see one slice of it."
- coins (how, first slice count change): "Each coin is pi times the radius squared times its thickness. Add them up."
- washer (how, first washer piece chosen): "This one has a hole. Outer radius squared, minus inner radius squared."
- thin (how, first n of 32 or more): "Thinner coins, and the sum settles on the exact volume."
- sections (how, Cross sections welcome): "Pick a shape. Each slice stands on the base, and its side spans the region."
- pot (how, Throw a pot welcome): "Drag the handles to shape your pot. The volume follows every move."
- predicted (event, a correct prediction; stale on a new piece): "That is the volume."

## Family engine
none. Uses `kit/graphing.js` `Plane` as a plotting tool for the region plane (`g.fn` for the curves, `g.trace` for
the wire line, shading drawn in the `plot` layer with `g.px`); the solid, wheel and pots are the tool's own SVG.

## Sources
- Volumes by disks, washers and known cross sections; area between curves: College Board, AP Calculus AB and BC CED
  (2020), Unit 8, https://apcentral.collegeboard.org/courses/ap-calculus-ab ; OpenStax, Calculus Volume 1, 6.1 "Areas
  between Curves" and 6.2 "Determining Volumes by Slicing",
  https://openstax.org/books/calculus-volume-1/pages/6-2-determining-volumes-by-slicing
- Frustum volume pi h (R1² + R1R2 + R2²)/3, sphere and cone formulas: OpenStax, Calculus Volume 1, 6.2 (same page).
- 1 cm³ = 1 mL: NIST SP 811, https://www.nist.gov/pml/special-publication-811
- Pieces and pots are made up; every exact value and coin sum computed in Python (2026-10-27).

## Done when
1. L3 (around y = -1) shows exact 7pi/15 ≈ 1.4661 and the coin sums 1.5148 (n = 4) and 1.4661 (n = 128).
2. L2 with the wire at x = 0.5 reads R = 0.5, r = 0.25, slice area 0.5890; L4 at x = 0.5 reads R = 1.75, r = 1.5.
3. L1 and P3 give the exact value for every n; L5 gives 36pi and the table agrees with (4/3)pi r³.
4. P2 Vase shows 270pi + 480 ≈ 1328.23 and the n = 4 sum 1340.7926.
5. Cross sections B1: squares 1/30, semicircles pi/240, triangles √3/120; B2 squares 144 with n = 4 sum 148.5.
6. Predict accepts "7pi/15", "1.466" for L3, and refuses "1.5".
7. Throw a pot starts at 212pi ≈ 666.02 cm³ ("holds 666 mL"); setting every handle to 4 cm gives 192pi ≈ 603.19.
8. How-to lines spoken once each in five actions; "That is the volume." once per piece.
9. Plane, solid and panel visible at 1366x768; at 760 wide the solid sits under the plane; labels at least 10 px in
   the 680x425 preview; Motion off stops the spin; no network, no images, no em dashes.

## Open questions
- solid-spinner: The module is "Area, volume and motion" (AP-CALC.U8). This tool teaches area between curves and volumes; it does not
  teach 8.1 average value or 8.2 to 8.3 motion along a line (position, velocity, distance from a rate). Should motion
  go to another tool (speedometer or rain-gauge could carry it), or should this one add a mode?
- solid-spinner: Shell method is left out on purpose (it is not in the current AP Calculus CED). Agree?
