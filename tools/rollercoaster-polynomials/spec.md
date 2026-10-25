# Rollercoaster Polynomials

## One idea
You build a coaster track by planting its zeros in the ground and choosing how each zero meets the ground (cross,
touch and turn back, or cross flat), and the track you get is the polynomial, drawn to scale.

## Not like
- launch-pad (gr 9, graphing): a projectile's quadratic with roots where it lands; here you place the roots yourself, any degree up to 6, and multiplicity shapes the track.
- ski-slope-designer (gr 8, graphing): slope as a feeling on straight runs; no slope or speed physics here, only zeros, sign and shape.
- graph-story-lab (gr 9, graphing): labels an existing coaster graph; here you build the graph from factors, and survey hidden ones.
- function-family-reunion (gr 12, graphing): one slider per transformation parameter; here the controls are zeros on the ground line, not shifts and stretches.
- roller-coaster-physics (science gr 11): energy, friction and loops decide if a car makes it; this tool has no energy model at all. The car only rides the shape and reads out P(x).
- ferris-wheel (gr 11): height from a circle traces a sine wave; here height comes from multiplied factors.
- polynomial-garden (gr 9): multiplies polynomials as area models; here multiplying is shown only as a check that factored and standard form are the same track.
- imaginary-island (gr 11): complex numbers; this tool stops at "this part never touches the ground" and names complex zeros without using them.
- plot-rollercoaster (ELA gr 6) and roller-coaster-rounding (gr 3): coaster images for story and rounding; no shared mechanic.

## Who and how
Grade 11, Algebra 2, students drive (own laptops), 20 to 40 minutes. Explore first: Build is open with no goal.
Standards: A-APR.B.2 (remainder theorem), A-APR.B.3 (zeros from factors, rough graph), A-APR.C.4 (identities, light
touch: factored and standard form agree), with F-IF.C.7c (graph polynomials showing zeros and end behavior) as support.

## Screens and modes
Header: title "Rollercoaster Polynomials", subtitle "Plant the zeros. Ride the track." Mode buttons `Build`,
`Survey`, `Commissions`. Kit buttons `Motion`, `Sound`, `Read`.

Look: dark instrument panel (the 9-12 theme), night ground and sky drawn in code with the art background behind the
plane at low opacity. Track rails in an amber accent (`--brand` for this tool: a warm amber that passes AA on the
panel). No confetti, no mascot, no riders in the car.

Plane (all modes except Survey): x from -6 to 6, y from -4 to 8, equal pixels per unit so the shape is true to scale.
Axis labels "distance (tens of meters)" and "height (tens of meters)". A note under the plane: "Drawn to scale: one
square is 10 meters each way." Ground line y = 0 drawn heavy as earth; below it a darker soil band.

Track drawing: between the two stations the track is double rails. Where P(x) > 0, thin support posts every 1 unit
from ground to rail. Where P(x) < 0, the soil is cut away around the rail as a tunnel. Outside the stations the curve
continues dashed and faint ("unbuilt track") to the plane edge, with an arrowhead at each end showing up or down.

### Build (default)
- Zero handles: diamond footings sitting on the ground line, draggable left and right only. Each shows its
  multiplicity as a small number under it (1, 2 or 3) and a shape glyph (cross, touch, flat) so color is not the cue.
- Stations: the leftmost and rightmost zeros get platform shapes labeled "Start" and "End". The ride runs between them.
- Panel, top to bottom:
  - Equation box: factored form, for example `P(x) = -0.2(x + 4)(x - 4)`, and below it standard form
    `P(x) = -0.2x² + 3.2`. Both update live. Button `Show the multiplication`.
  - Zero list: one row per zero: "x = -4", buttons `1` `2` `3` (multiplicity, aria-pressed), `Split` (only when
    multiplicity is 2 or 3), `Remove`. Under the list: `Add zero`.
  - Leading coefficient a: a slider (log scale on the size of a, 0.001 to 2), a number box showing a to 3
    significant figures (typing a value sets it exactly), and `Flip track` (multiplies a by -1).
  - Toggle `Snap to half` (on by default).
  - Readouts: Degree; End behavior sentence; Highest point (m, and x); Deepest tunnel (m, and x); Ride length
    (distance between stations, m).
  - `Ride` and `New track`.

### Survey (the remainder theorem)
The engineering office sends a plan in standard form only. The track is hidden in fog; you find the footings.
- Plan picker: buttons `Plan 1` to `Plan 9`. The plan's standard form is shown large.
- Plane: x from -5 to 5, y from -10 to 10, axis label "height (plan units)" (no meters in this mode). Fog over
  everything except the ground line.
- A survey stake on the ground line, draggable, snapping to halves from -5 to 5. Clicking the ground also moves it.
  Button `Survey here` (or Enter) plants a post at x = c whose height is P(c); a post taller than the view is cut at
  the edge with an arrow and its value printed.
- Panel: a synthetic division table dividing the plan P(x) by (x - c): the coefficient row, the multiply row, the
  sum row, the remainder boxed, then the sentence "Remainder r, so P(c) = r." When r = 0: "Remainder 0, so (x - c) is
  a factor. A footing goes at x = c." and the footing locks.
- Factor tracker: "P(x) = (found factors) × (remaining part)". On a locked footing, button
  `Check for a double footing` divides the remaining part by (x - c) again; remainder 0 raises that footing's
  multiplicity and shrinks the remaining part; nonzero says "Not a double footing."
- Survey log: every c tried with its P(c), newest first.
- When the remaining part is a constant, the fog lifts (track draws left to right with Motion on, appears at once with
  Motion off), and a check table shows x = -2, 0, 2 with factored value and standard value side by side, equal.
- When the remaining part is a quadratic with negative discriminant (Plan 9): "The remaining part is never zero for a
  real x, so the track never touches the ground again. Its zeros are complex numbers." Then the fog lifts as above.
- Button `Start over` clears the plan's posts and footings.

### Commissions (optional challenges)
Two lists: `Orders` (C1 to C6) and `Blueprints` (B1 to B4). Choosing one loads Build's tools with a fresh default
track (except blueprints, which also draw a ghost track dashed in a second engine color with its own dash pattern).
- Order card: name, the customer line, and a requirement checklist that ticks live (text "met" / "not yet" plus a
  check or open-circle glyph).
- Blueprint card: "Match the ghost track." Live compare: "Zeros match: yes / no", "Multiplicities match", "a within
  5 percent". The tool never prints the blueprint's equation until it is matched.
- When every requirement is met: a quiet "Approved" stamp on the card, one chime, and the card gets a check in the
  list (remembered per device in localStorage `curio-rcp-done`, try/catch). Buttons `Ride`, `Back to list`.

## Content

Default Build track: zeros -4 and 4 (multiplicity 1 each), a = -0.2 (peak 32 m at x = 0).

End behavior sentences (by degree parity and sign of a):
- even, a > 0: "Even degree, a positive: both ends rise."
- even, a < 0: "Even degree, a negative: both ends fall."
- odd, a > 0: "Odd degree, a positive: falls on the left, rises on the right."
- odd, a < 0: "Odd degree, a negative: rises on the left, falls on the right."

Contact glyph names: multiplicity 1 "crosses", 2 "touches and turns back", 3 "crosses flat".

Orders (stations are the outermost zeros; H = a hill between neighboring ground points, T = a tunnel):
- C1 Kiddie Hop. "Small riders, one gentle hill." Start at -2, end at 2; pattern H; highest point 10 to 20 m.
  (Works: -0.4(x + 2)(x - 2), 16 m.)
- C2 Double Dipper. "Two hills that kiss the ground between them." Start -4, end 4; pattern H H; one touch zero
  between; highest point at most 50 m. (Works: -0.05(x + 4)x²(x - 4), 32 m.)
- C3 Into the Dark. "A hill, then a tunnel." Start -5, end 4; pattern H T; highest point at least 30 m; tunnel at
  most 30 m deep. (Works: 0.09(x + 5)x(x - 4): 37.8 m up, 25.7 m deep.)
- C4 Flat Spot. "Cross the ground flat, like a hover." Start -3, end 4; one crosses-flat zero between; pattern H T;
  degree at most 5; highest point at most 80 m; tunnel at most 30 m deep. (Works: 0.045(x + 3)(x - 1)³(x - 4): 73.6 m
  up, 24.2 m deep.)
- C5 Big Three. "Two big hills with a short tunnel between." Start -5, end 5; pattern H T H; tallest hill 40 to 80 m;
  tunnel at most 20 m deep. (Works: -0.033(x + 5)(x + 1.5)(x - 1.5)(x - 5): about 42.7 m up, 18.6 m deep. Narrow on
  purpose: the tunnel's zeros must sit close together.)
- C6 Triple Camel. "Three hills, touching down twice." Start -3, end 3; pattern H H H; two touch zeros between; every
  hill at least 10 m; tallest at most 40 m. (Works: -0.05(x + 3)(x + 1.5)²(x - 1.5)²(x - 3): three hills of about
  22.8 m.)

Requirement checks use: station x within 0.05; pattern read from the sign of P between consecutive distinct zeros;
heights from the engine's extrema on the ride interval, times 10 for meters; degree is the sum of multiplicities.

Blueprints (ghost tracks):
- B1 -0.5(x + 3)(x - 1): one hill, 20 m.
- B2 0.1(x + 4)x(x - 3): hill 20.7 m, tunnel 12.6 m.
- B3 -0.05(x + 4)(x - 1)²(x - 4): two hills touching at x = 1, tallest about 60 m.
- B4 0.03(x + 4)x³(x - 3): hill about 49 m, flat crossing at 0, tunnel about 16 m.
Match: same zeros within 0.1 each, same multiplicities, a within 5 percent.

Survey plans (standard form shown; factored form revealed only when solved):
1. x² - x - 6 = (x - 3)(x + 2)
2. x³ - 2x² - 5x + 6 = (x - 1)(x + 2)(x - 3)
3. x³ - 3x - 2 = (x + 1)²(x - 2)
4. -x³ + x² + 8x - 12 = -(x - 2)²(x + 3)
5. x⁴ - 5x² + 4 = (x - 1)(x + 1)(x - 2)(x + 2)
6. x⁴ - 2x³ - 3x² + 4x + 4 = (x + 1)²(x - 2)²
7. x³ - 3x² + 3x - 1 = (x - 1)³
8. 2x³ - 3x² - 3x + 2 = (x + 1)(x - 2)(2x - 1), zeros -1, 2 and one half (shown as 2(x + 1)(x - 2)(x - 0.5))
9. x³ - x² + x - 1 = (x - 1)(x² + 1), one real zero

## Interactions in detail
- Dragging a zero: track, both equations and readouts update every frame. Range -6 to 6. Keyboard: Tab to a footing,
  Left/Right move 0.5 (0.1 with Snap off), keys 1, 2, 3 set multiplicity, Delete removes.
- Dropping a zero on another zero's x merges them (multiplicities add) if the sum is 3 or less and degree stays 6 or
  less; otherwise it slides back to where it started and the tip says "That would make a multiplicity over 3."
- `Split` breaks a multiplicity 2 or 3 zero into separate simple zeros 0.5 apart (nearest free halves).
- Degree cap 6: `Add zero` and any multiplicity button that would pass 6 are disabled with a tip saying why. `Add
  zero` places a simple zero at the free half closest to 0.
- No zeros: P(x) = a, a flat line. Tip: "No footings: the track never reaches the ground." One distinct zero: one
  station only; tip "A ride needs two ground points to start and end." `Ride` is disabled in both cases.
- Track beyond the view: rail clips at the plane edge; the readout still gives the true height, marked "off the
  blueprint".
- a can never be 0: the slider and box stop at 0.001 in size; typing 0 restores the last value with a tip.
- `Show the multiplication`: a step list in the panel that multiplies the factors one at a time, left to right,
  each line in standard form, ending with the leading coefficient. Changing the track closes it.
- `Ride`: an empty car (drawn in code) rolls from Start to End at a steady horizontal pace (about 4 seconds for the
  full width), tilted to the track's slope. Live readout: x, P(x), height in meters, "above ground" or "in the
  tunnel". At each interior zero a short tone: one pitch for crosses, a lower double tone for touches, a slide for
  crosses flat (silent with Sound off; the readout also prints "crossed at x = 0"). Motion off: no rolling; the car
  appears at End and the readout lists every ground contact in order. Any edit stops the ride.
- `New track` restores the default track. Mode changes call Curio.stop().
- Survey: c already surveyed shows its old row again; posts persist per plan until `Start over`. Plan 8 needs the
  stake at 0.5; the table shows decimals to 2 places. `Check for a double footing` is disabled once the remaining part
  is degree 0, and on Plan 9 after the quadratic message.
- Commissions: requirements tick on every change; nothing grades a ride. Leaving a card keeps its done check only if it
  was approved.

## Art
- night-fairground: empty fairground field at dusk, dark blue sky, distant string lights and the silhouette of a
  wooden coaster frame, no people, no text, muted for a dark UI background; 16:9; cutout no; people no.
Everything else is drawn in code: plane, rails, posts, tunnels, footings, stations, car, fog, ghost track.

## Voice
Bank "hs-narrator", voice "Kore", style "Read clearly and naturally, at a moderate pace". Lines:
1. Welcome to Rollercoaster Polynomials. Drag the footings along the ground, and the track bends to fit them.
2. Each footing is a zero of the polynomial. The leftmost and rightmost zeros are your stations.
3. Multiplicity one crosses the ground. Two touches and turns back. Three crosses flat.
4. Odd degree ends point opposite ways. Even degree ends point the same way.
5. The leading coefficient sets how tall the track is. Flip it, and hills become tunnels.
6. Survey mode. The office sent a plan in standard form. Plant a stake to find out how high the track is there.
7. The remainder of dividing by x minus c is the height of the track at c.
8. Remainder zero. So x minus c is a factor, and a footing goes here.
9. Not a double footing. The remaining part is not zero here.
10. The remaining part never reaches zero for a real number, so the track never touches the ground again.
11. Every footing found. Factored form and standard form describe the same track.
12. Commissions. Each order lists what the park wants. Build a track that meets every line.
13. Match the ghost track. Read its zeros and how it meets the ground, then set the height.
14. Approved.
Lines 1, 6 and 12 play on entering each mode (after the first tap); 8 to 11 and 14 on those events; 2 to 5, 7 and 13
are Read lines for the matching hint.

## Family engine
Graphing (`kit/graphing.js`, per `docs/families/graphing.md`). This is the first tool built in the family, so the
build agent writes the engine to that spec; it is also the first 9-12 tool, so it writes `kit/theme-912.css`
(BATCH-G11). Uses: `Plane` (two views), `g.fn` (track, unbuilt dashed ends, ghost), `g.point` with y locked to 0 for
footings and the survey stake (`snap`, `onMove`, keyboard), `g.roots` and `g.extrema` for readouts and checks,
`g.trace` for the ride readout, `g.slider` for a, `g.segment` for posts, `g.clear`. Rails, tunnels, stations, car and
fog are the tool's own SVG positioned with `g.px`. If the engine needs a "point locked to an axis" option, add it to
the engine and the family doc, not to the tool.

## Sources
- Zeros, multiplicity behavior (cross, touch, flatten) and end behavior: OpenStax, College Algebra 2e, 5.3 "Graphs of
  Polynomial Functions", https://openstax.org/books/college-algebra-2e/pages/5-3-graphs-of-polynomial-functions
- Remainder theorem, factor theorem, synthetic division: OpenStax, College Algebra 2e, 5.4 "Dividing Polynomials" and
  5.5 "Zeros of Polynomial Functions", https://openstax.org/books/college-algebra-2e/pages/5-5-zeros-of-polynomial-functions
- Standards text: Common Core State Standards for Mathematics, High School Algebra (A-APR) and Functions (F-IF),
  https://www.thecorestandards.org/Math/Content/HSA/APR/
- All plan, order and blueprint values are original and were checked by expansion and numeric sampling (2026-10-25).

## Done when
1. Default Build shows -0.2(x + 4)(x - 4), standard form -0.2x² + 3.2, highest point 32 m at x = 0, "Even degree, a
   negative: both ends fall."
2. Setting a zero to multiplicity 2 makes the track touch and turn back there; 3 makes it cross flat; both equations
   update, and the degree readout matches the sum of multiplicities.
3. Dragging one zero onto another merges them; merging past 3 or degree past 6 is refused with a tip; `Split` works.
4. With zero or one distinct zero, `Ride` is disabled and the right tip shows; a cannot be set to 0.
5. `Ride` rolls the car Start to End with live P(x) readout and a contact tone per interior zero; with Motion off the
   car is placed at End and contacts are listed.
6. Survey Plan 3 at c = -1 gives remainder 0, locks a footing, and `Check for a double footing` raises it to
   multiplicity 2; c = 2 finishes it and the check table shows equal values at -2, 0, 2.
7. Survey Plan 9 shows the complex-zeros message after x = 1 is found; Plan 8 accepts c = 0.5.
8. Each order C1 to C6 can be approved with the listed working track, and each blueprint B1 to B4 matches when built
   exactly; a 10 percent wrong a does not match.
9. Every control works by keyboard with visible focus; footings and stake have 44 px targets; contact type and
   checklist state are readable without color.
10. No em dashes, no network requests, the only image has no people, and every spoken line is in `voice/lines.json`.
