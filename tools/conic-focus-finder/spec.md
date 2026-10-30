# Conic Focus Finder
Renamed from: Cone Slicer

## One idea
Hold a pencil on a string pinned to two points and drag it around: keep the sum of the two distances fixed and the
ink makes an ellipse, keep their difference fixed and it makes a hyperbola, keep the distance to a pin equal to the
distance to a rail and it makes a parabola; the pins and the string then hand you the curve's equation.

## Not like
- slice-it (gr 10, explorer) and solid-spinner (this group): both cut or spin solids. The overlap pass flagged this tool as a third one, so it no longer slices a cone at all: every curve here is drawn by a distance rule in a flat plane (the overlap note's suggested reshape, taken).
- coordinate-proof-lab (gr 10): proves properties with coordinates; G-GPE there is lines and polygons. Here G-GPE.A.3 only: equations of conics from foci.
- fire-lookout-triangles (this group): distances to fixed towers too, but two angles fix one point; here one rule traces a whole curve.
- polar-rose-studio (this group): curves from an angle rule; here from distances.
- launch-pad (gr 9, graphing): parabolas as projectile paths from a formula; here the parabola comes from a focus and a rail, and its reflecting property.

## Who and how
Grade 12, precalculus (Conic Sections). Students drive, 25 to 40 minutes. Explore first: Draw opens with an ellipse's
pins and string ready and no task.
Topic line: "conic sections from their foci".
Standards: G-GPE.A.3 (derive ellipse and hyperbola equations from foci, using that the sum or difference of distances
is constant; parabola from focus and directrix is G-GPE.A.2, named here as support), AP-PRECALC.U4 (4.6 to 4.7
conic sections in the AP course framework).
CCSS per mode: Draw and Match G-GPE.A.3 (and A.2 for parabolas); Eccentricity G-GPE.A.3; Uses supports both.
tool.json: driver "students", minutes "25-40", modes ["Draw", "Eccentricity", "Match", "Uses"].

## Screens and modes
Header (kit, 9-12 theme): "Conic Focus Finder", small line "One distance rule, one curve." Modes `Draw`,
`Eccentricity`, `Match`, `Uses`; kit `Motion`, `Sound`, `Read`.

Stage: a coordinate plane from the graphing engine, x and y from -10 to 10, equal scale, grid 1, labels every 2, laid
over a painted drafting-paper texture (art: drafting-paper, dimmed so the grid and labels keep their contrast). Pins
are painted brass push pins (art: brass-pin, cutout, centered on the pin point), the pencil is a painted pencil
(art: pencil, cutout, its tip on the pencil point, tilted in code toward the pin it is farther from), the string is two
straight code segments from the pins to the pencil tip, the rail (directrix) is a heavy code ruler line with ticks
(it must stretch to the plane edge and turn, so it stays in code). Ink trail in `--brand`.
The plane is the focus in Draw, Eccentricity and Match: it is the largest thing on screen, centered on the stage, with
the panel beside it (under it below 1000 px wide, where the plane still fills the width).

### Draw (explore, default)
Focus: the pencil, the string and the ink on the plane; the two distance bars in the panel sit at the top so the
eye can move between them and the pencil.
Panel:
- Rule buttons: `Sum (ellipse)`, `Difference (hyperbola)`, `Pin and rail (parabola)`.
- Live distances: "d1 = PF1", "d2 = PF2" (or "to rail"), and the rule: "d1 + d2 = 10.00" (or |d1 - d2|, or d1 = d2),
  as two bars side by side whose total (or gap) stays the same while the pencil moves.
- String slider: the fixed sum (2 to 24) or difference (0 to 18), step 0.5. Toggle `Line up pins` (on: pins share a y
  or an x, so the equation has no xy term).
- `Clear ink`, `Draw it all` (the pencil runs the whole curve in 3 s; instant with Motion off), `Show equation`.
- Equation card (after `Show equation` or once the ink covers half the curve): center (h, k), a, c, b with "b² = a² - c²"
  (ellipse) or "b² = c² - a²" (hyperbola), or p for the parabola, then the standard form with numbers.
Drag the pencil anywhere near the curve: it slides to the nearest point that obeys the rule and leaves ink there, so
students draw the curve by hand. Drag pins (snap 0.5) or the rail and the curve and its equation change (old ink
clears).

### Eccentricity
Focus: the one curve and its label ("e < 1: ellipse") on the plane; the e slider sits at the top of the panel.
One pin (focus at the origin) and a vertical rail (directrix x = -d, d slider 1 to 6). Slider e from 0.10 to 2.50
(step 0.05). The curve is every point with PF = e x (distance to rail). Live label: "e < 1: ellipse", "e = 1:
parabola", "e > 1: hyperbola" (with both branches when e > 1). A second pin appears for the ellipse and the hyperbola
(the other focus), showing that the same curve is a two-pin curve too. Readout: e = c / a for e ≠ 1.

### Match (optional)
Focus: your curve over the dashed ghost on the plane, with the live "Pins match" and "String matches" lines just under
the plane's top edge so they sit inside the eye's path.
Picker `M1` to `M6`. A ghost curve (dashed, `--gr-2`) with its equation printed. Task: drag the pins (and rail) and set
the string so your curve lies on the ghost, then fill the blanks: "foci at ( , ) and ( , ), string ...". The match is
checked live: "Pins match: yes / not yet", "String matches", then a quiet "Matched" with the work: "c² = a² - b², so c = 4."

### Uses
Focus: the open card's animated diagram, large and centered; the three card buttons sit in a row above it.
Three cards, each a painted header picture with a code diagram animated over a calm part of it (Motion off: still
frame plus text):
- `Ellipse: orbits and whispers` (art: whisper-hall header; the orbit uses art: sun and planet): a planet cutout on an
  ellipse with the Sun cutout at one focus; then rays from one focus bounce off the ellipse and all pass through the
  other focus.
- `Parabola: dishes` (art: radio-dish): parallel rays come in along the axis, bounce, and meet at the focus; reversed,
  a bulb at the focus sends a parallel beam.
- `Hyperbola: radio timing` (art: loran-coast): two stations send a pulse at once; a ship hears one pulse 30
  microseconds before the other, which puts it on one branch of a hyperbola with the stations as foci.
Each animation loops in 6 s or less; a tap on another card, `Try it in Draw` or a mode button acts at once (the loop
stops on the spot). Each card has a `Try it in Draw` button that loads that curve.

## Content
Default Draw: Sum rule, pins (-3, 0) and (3, 0), string 10: x²/25 + y²/16 = 1 (a = 5, c = 3, b = 4).
Difference default: pins (-5, 0), (5, 0), difference 6: x²/9 - y²/16 = 1 (a = 3, c = 5, b = 4), asymptotes y = ±(4/3)x
drawn dashed.
Parabola default: pin (0, 2), rail y = -2: x² = 8y (p = 2, 4p = 8). Rail can be horizontal or vertical (toggle).
Shifted example in a tip: pins (1, 2) and (1, 8), string 10: (x - 1)²/16 + (y - 5)²/25 = 1.

Match targets:
| Id | Ghost equation | Answer |
|---|---|---|
| M1 | x²/25 + y²/9 = 1 | foci (±4, 0), sum 10 |
| M2 | (x - 2)²/9 + (y + 1)²/25 = 1 | foci (2, 3) and (2, -5), sum 10 |
| M3 | x²/16 - y²/9 = 1 | foci (±5, 0), difference 8 |
| M4 | y²/4 - x²/5 = 1 | foci (0, ±3), difference 4 |
| M5 | y - 1 = x²/12 | focus (0, 4), rail y = -2 (p = 3) |
| M6 | x = y²/8 | focus (2, 0), rail x = -2 (p = 2) |

Uses facts (on screen):
- "Planets move on ellipses with the Sun at one focus (Kepler's first law). Earth's orbit is nearly a circle: e is
  about 0.017."
- "In an elliptical room a whisper at one focus can be heard at the other. The U.S. Capitol's National Statuary Hall
  is famous for this effect."
- "A satellite dish is a parabola turned around its axis: signals coming in straight meet at the focus, where the
  receiver sits."
- "Radio navigation once used timing like this: a fixed time difference from two stations puts a ship on a hyperbola
  (the LORAN system)." Worked: radio travels about 0.3 km per microsecond, so 30 microseconds is about 9 km of
  difference (the string difference, in km).

## Interactions in detail
- Nearest point: the tool samples the current curve at 1,440 points (both branches for hyperbolas), finds the nearest
  to the pointer, then refines; the pencil only moves if the pointer is within 2 units of the curve, otherwise it
  stays and the tip says "Bring the pencil closer to the string's reach."
- Impossible and edge settings (both said in the panel, never silent):
  - Sum less than the pin gap: "The string is too short to reach around both pins." No curve.
  - Sum equal to the gap: the curve is the segment between the pins ("flattened ellipse").
  - Pins on one spot: a circle of radius sum / 2 ("Two pins on one spot: a circle.").
  - Difference 0: the perpendicular bisector line; difference equal to or more than the gap: "No point can be that much
    closer to one pin." No curve.
  - Pin on the rail: the parabola degenerates to a line through the pin perpendicular to the rail.
- `Line up pins` off: the conic is tilted; the equation card says "Tilted conic: its equation needs an xy term, which
  this course leaves out" and shows c, a and b only.
- Equation numbers print as exact as the snaps allow. Pins snap to 0.5 and the string to 0.5, so a and c are
  multiples of 0.25 and a², b², c² can be sixteenths; they show as fractions like 441/16 when not whole (sum 10.5
  gives a = 21/4, a² = 441/16).
- `Draw it all` runs 3 s; a drag on a pin, the pencil, the string slider or a rule button during it stops the run and
  acts at once.
- Match checks: pins within 0.05 of the answer (either order), string within 0.05.
- Keyboard: pins and the pencil are engine points (arrows move 0.5; the pencil steps along the curve 2° of its
  parameter per press). 44 px targets.
- Mode change: `Curio.stop()`, `V.hush()`. Match check marks per device (localStorage `curio-conic-focus`, try/catch)
  with `Clear marks`.

## Look
Accent (`--brand`) #8ff0ff, pale ice cyan (a lit string): 13.3:1 on --panel #141b25, 12.6:1 on --sec-bg #18202b;
--brand-ink #10161f on it 13.9:1. Paler and greener than motion-graph-match's #36c9dd and than flight-planner's sky
blue; no group sibling or 9-12 math neighbor uses it.
Scene: a drafting board at night: the painted drafting paper is dimmed under a #0f1820 wash at 80 percent so the
plane background reads #0f1820 to #13202a; grid from the theme, string #e8edf3, rail #a6b3c4 with tick marks. The
brass pins (about #d9b26a) and the yellow pencil come from the art. Plane labels keep a #10161f halo (over 12:1 for
--ink). Uses cards: header pictures sit above the diagram on a #10161f band; diagram rays in `--brand`.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: soft painted illustration, warm lamp light at night.
- drafting-paper: "Close top-down view of a sheet of pale blue-gray drafting paper on a wooden drafting board, faint
  paper fibers, soft even lamp light, painted texture, full frame"; 16:10; cutout no; people no; full-frame texture
  under the plane, dimmed (the grid is drawn in code over it).
- brass-pin: "A single brass push pin with a round domed head seen from slightly above, warm lamp light, painted
  illustration, plain white background"; 1:1; cutout yes; people no; both foci in Draw and Match, the focus in
  Eccentricity (about 36 px).
- pencil: "A yellow wooden pencil with a sharpened graphite tip, lying diagonally with the tip at the lower left, warm
  lamp light, painted illustration, plain white background"; 1:1; cutout yes; people no; the pencil the student drags
  (about 64 px, tip on the pencil point, rotated in code).
- sun: "A glowing golden sun with soft flaring rays, painted illustration, plain black background"; 1:1; cutout yes;
  people no; at one focus of the orbit diagram.
- planet: "A small blue and green planet with swirling white clouds, lit from one side, painted illustration, plain
  black background"; 1:1; cutout yes; people no; moves along the orbit ellipse.
- whisper-hall: "A grand empty semicircular marble hall with a domed coffered ceiling, tall columns and bronze
  statues on stone pedestals, a polished checkered marble floor, soft daylight, painted illustration"; 16:9; cutout
  no; people no; header of the ellipse card.
- radio-dish: "A large white radio dish antenna on a grassy hill at dusk, tilted up toward a deep blue sky with first
  stars, painted illustration"; 16:9; cutout no; people no; header of the parabola card.
- loran-coast: "A small ship at sea at night with its lights on, two tall radio masts with red lights on a distant
  dark coastline, calm water reflecting the lights, painted illustration"; 16:9; cutout no; people no; header of the
  hyperbola card.
The plane, grid, string, rail, ink, curves, asymptotes, rays, labels, equation cards and preview.svg are drawn in code
(they are the diagram itself and must follow the math exactly).

## Voice
`knowing-guide` (Sadaltager), style "Say in a knowledgeable, friendly way, like a science museum curator at a drawing
table." Not used by a group sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`.
- draw (how, Draw welcome; stale after the first pencil drag): "Drag the pencil around the pins. The string keeps the two distances adding to the same number, so the ink makes an ellipse."
- rules (how, first time the pencil has inked a quarter of the ellipse; stale once a second rule button is tapped): "Now tap Difference or Pin and rail, and drag the pencil again. A fixed difference makes a hyperbola. Equal distance to a pin and a rail makes a parabola."
- tooShort (event, string set too short; stale when the string reaches or a pin moves): "The string is too short to reach around both pins. Slide the string longer or drag the pins closer."
- circle (event, pins dropped on one spot with the Sum rule; stale when they move apart): "Two pins on one spot. That's a circle."
- ecc (how, Eccentricity welcome; stale after the first e slider move): "Slide e. Below one you get an ellipse, at one a parabola, above one a hyperbola."
- match (how, Match welcome; stale once a target is matched): "Drag the pins and slide the string until your curve lies on the dashed ghost. Then type the foci."
- matched (event, a match; stale on a new target): "Matched."
- uses (how, Uses welcome; stale once a card is opened): "Tap a card to watch how each curve is used. Then tap Try it in Draw."

## Family engine
Graphing (`kit/graphing.js`, docs/families/graphing.md), used as a plotting tool, not as a family sibling (this tool
is not in the graphing family). Uses `Plane`, `g.param` (each conic drawn parametrically: ellipse (h + a cos t,
k + b sin t), hyperbola branches (h ± a cosh t, k + b sinh t), parabola (x, x²/4p)), `g.point` for pins, pencil and
rail handle (`snap`, `lock`), `g.segment` for the string, `g.clear`. Ink, pin and pencil images go in the `front` and
`points` layers with `g.px`.

## Sources
- Ellipse and hyperbola as constant sum and difference of distances to foci, b² = a² - c² and c² = a² + b²,
  parabola focus and directrix, eccentricity: OpenStax, Precalculus 2e, 10.1 "The Ellipse", 10.2 "The Hyperbola",
  10.3 "The Parabola", 10.5 "Conic Sections in Polar Coordinates",
  https://openstax.org/books/precalculus-2e/pages/10-1-the-ellipse
- Kepler's first law: NASA Science, "Orbits and Kepler's Laws", https://science.nasa.gov/resource/orbits-and-keplers-laws/
- Earth's orbital eccentricity 0.0167: NASA Goddard, Earth Fact Sheet, https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
- Whispering effect in National Statuary Hall: Architect of the Capitol, "National Statuary Hall",
  https://www.aoc.gov/explore-capitol-campus/buildings-grounds/capitol-building/national-statuary-hall
- LORAN hyperbolic navigation by time differences: U.S. Coast Guard Navigation Center, LORAN-C history,
  https://www.navcen.uscg.gov/ ; radio speed 299,792 km/s (about 0.3 km per microsecond): NIST, speed of light,
  https://physics.nist.gov/cgi-bin/cuu/Value?c
- Standards: CCSS Math G-GPE.A, https://www.thecorestandards.org/Math/Content/HSG/GPE/ ; College Board AP Precalculus
  CED (2023), Unit 4.
- Match targets and defaults are made up.
- Checks run (Python, 2026-10-29): default ellipse a 5, b 4, c 3; shifted example a 5, b 4, c 3 with center (1, 5);
  hyperbola b 4, asymptote slope 4/3; parabola x² = 8y: distance to pin equals distance to rail at x = -4, 0, 3, 7.
  M1 c 4; M2 c 4, foci (2, 3) and (2, -5); M3 c 5; M4 c 3; M5 and M6 pin and rail distances equal at three points
  each. Eccentricity rule PF / (x + d) returns e exactly for e 0.5, 1.0 and 1.5 at three angles; e 0.5 with d 3 gives
  a 2, c 1, c / a 0.5. LORAN 30 microseconds × 0.299792 km = 8.99 km. Ellipse reflection: a ray from one focus
  reflected at four points passes through the other focus (cosine 1.000000000). Snap fractions: with 0.5 snaps a²,
  b² and c² have denominators 1, 4 or 16, so the first draft's "quarters" was wrong and now says sixteenths. Sampling
  1,440 points on the largest circle (radius 12) spaces them 0.052 units apart, well inside the 2 unit reach.

## Done when
1. Default Draw: dragging the pencil around keeps d1 + d2 = 10.00 at every spot (to 0.01) and the equation card shows
   x²/25 + y²/16 = 1 with a = 5, b = 4, c = 3.
2. Difference rule with pins (±5, 0) and 6: x²/9 - y²/16 = 1, both branches, asymptotes y = ±(4/3)x.
3. Pin (0, 2) and rail y = -2: x² = 8y; the pencil's two distances read equal everywhere.
4. Sum 5 with pins 6 apart says the string is too short; pins together draw a circle of radius sum / 2; string 10.5
   with pins (±3, 0) prints a² as 441/16.
5. Eccentricity: e = 0.5 labels ellipse, 1.00 parabola, 1.5 hyperbola with two branches.
6. Match M2 accepts foci (2, 3), (2, -5) and sum 10 in either order; M4 accepts foci (0, ±3) and difference 4; M6
   accepts focus (2, 0) and rail x = -2.
7. Uses: the ellipse animation's reflected rays all pass through the other focus; the hyperbola card shows 9 km.
8. Focus: at 1366x768 and 1000x625 the plane (Draw, Eccentricity, Match) or the open card's diagram (Uses) is the
   largest thing on the stage, and the pins and pencil read as the painted brass pins and pencil.
9. Tap while it plays: during `Draw it all` or a Uses animation, a pin drag, slider, rule button or card tap acts at
   once and the readouts match the new state.
10. Pins and pencil work by keyboard with 44 px targets; how-to lines are spoken once each in five actions; no line
    names a control that is hidden or disabled at that moment.
11. Controls visible without scrolling at 1366x768; plane text at least 10 px in the 680x425 preview.
12. No network, no people in any image, no em dashes.

## Open questions
- cone-slicer: renamed "Conic Focus Finder" and reshaped as the overlap note suggested (no cone, no slicing). The
  folder is already tools/conic-focus-finder; the concept line in the catalog still says "Slice a double cone". Agree
  with the name and the new concept line?
