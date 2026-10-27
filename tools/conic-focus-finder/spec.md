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

Stage: a coordinate plane from the graphing engine, x and y from -10 to 10, equal scale, grid 1, labels every 2.
Pins are drawn as push pins (code), the pencil as a small pencil tip, the string as two straight segments from the
pins to the pencil, the rail (directrix) as a heavy ruler line. Ink trail in `--brand`.

### Draw (explore, default)
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
One pin (focus at the origin) and a vertical rail (directrix x = -d, d slider 1 to 6). Slider e from 0.10 to 2.50
(step 0.05). The curve is every point with PF = e x (distance to rail). Live label: "e < 1: ellipse", "e = 1:
parabola", "e > 1: hyperbola" (with both branches when e > 1). A second pin appears for the ellipse and the hyperbola
(the other focus), showing that the same curve is a two-pin curve too. Readout: e = c / a for e ≠ 1.

### Match (optional)
Picker `M1` to `M6`. A ghost curve (dashed, `--gr-2`) with its equation printed. Task: drag the pins (and rail) and set
the string so your curve lies on the ghost, then fill the blanks: "foci at ( , ) and ( , ), string ...". The match is
checked live: "Pins match: yes / not yet", "String matches", then a quiet "Matched" with the work: "c² = a² - b², so c = 4."

### Uses
Three cards, each a small animated diagram (Motion off: still frame plus text):
- `Ellipse: orbits and whispers`: a planet on an ellipse with the Sun at one focus; then rays from one focus bounce off
  the ellipse and all pass through the other focus.
- `Parabola: dishes`: parallel rays come in along the axis, bounce, and meet at the focus; reversed, a bulb at the
  focus sends a parallel beam.
- `Hyperbola: radio timing`: two stations send a pulse at once; a ship hears one pulse 30 microseconds before the
  other, which puts it on one branch of a hyperbola with the stations as foci.
Each card has a `Try it in Draw` button that loads that curve.

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
- Equation numbers print as exact as the snaps allow (halves give quarters in a², shown as fractions like 81/4 when not
  whole).
- Match checks: pins within 0.05 of the answer (either order), string within 0.05.
- Keyboard: pins and the pencil are engine points (arrows move 0.5; the pencil steps along the curve 2° of its
  parameter per press). 44 px targets.
- Mode change: `Curio.stop()`, `V.hush()`. Match check marks per device (localStorage `curio-conic-focus`, try/catch)
  with `Clear marks`.

## Look
Accent (`--brand`) #8ff0ff, pale ice cyan (a lit string): 13.3:1 on --panel #141b25, 12.6:1 on --sec-bg #18202b;
--brand-ink #10161f on it 13.9:1. Paler and greener than motion-graph-match's #36c9dd and than flight-planner's sky
blue; no group sibling or 9-12 math neighbor uses it.
Scene: a drafting board at night: plane background #0f1820, grid from the theme, pins brass #d9b26a heads, string
#e8edf3, rail #a6b3c4 with tick marks.

## Art
none: drawn in code (pins, pencil, string, rail, orbit, dish, stations, rays, preview.svg).

## Voice
`knowing-guide` (Sadaltager), style "Say in a knowledgeable, friendly way, like a science museum curator at a drawing
table." Not used by a group sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`.
- draw (how, Draw welcome): "Drag the pencil. The string keeps the two distances adding to the same number, so the ink makes an ellipse."
- rules (how, first rule change): "Try the other rules. A fixed difference makes a hyperbola. Equal distance to a pin and a rail makes a parabola."
- tooShort (event, string too short; stale when it reaches): "The string is too short to reach around both pins."
- circle (event, pins on one spot with the Sum rule; stale when they move apart): "Two pins on one spot. That's a circle."
- ecc (how, Eccentricity welcome): "Slide e. Below one you get an ellipse, at one a parabola, above one a hyperbola."
- match (how, Match welcome): "Move the pins and set the string until your curve lies on the ghost. Then fill in the foci."
- matched (event, a match; stale on a new target): "Matched."
- uses (how, Uses welcome): "Pick a card to watch how each curve is used. Then try it in Draw."

## Family engine
Graphing (`kit/graphing.js`, docs/families/graphing.md), used as a plotting tool, not as a family sibling (this tool
is not in the graphing family). Uses `Plane`, `g.param` (each conic drawn parametrically: ellipse (h + a cos t,
k + b sin t), hyperbola branches (h ± a cosh t, k + b sinh t), parabola (x, x²/4p)), `g.point` for pins, pencil and
rail handle (`snap`, `lock`), `g.segment` for the string, `g.clear`. Ink, pins and pencil art go in the `front` and
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
- Match targets and defaults are made up; foci and constants checked by hand and in Python (2026-10-27).

## Done when
1. Default Draw: dragging the pencil around keeps d1 + d2 = 10.00 at every spot (to 0.01) and the equation card shows
   x²/25 + y²/16 = 1 with a = 5, b = 4, c = 3.
2. Difference rule with pins (±5, 0) and 6: x²/9 - y²/16 = 1, both branches, asymptotes y = ±(4/3)x.
3. Pin (0, 2) and rail y = -2: x² = 8y; the pencil's two distances read equal everywhere.
4. Sum 5 with pins 6 apart says the string is too short; pins together draw a circle of radius sum / 2.
5. Eccentricity: e = 0.5 labels ellipse, 1.00 parabola, 1.5 hyperbola with two branches.
6. Match M2 accepts foci (2, 3), (2, -5) and sum 10 in either order; M4 accepts foci (0, ±3) and difference 4; M6
   accepts focus (2, 0) and rail x = -2.
7. Uses: the ellipse animation's reflected rays all pass through the other focus; the hyperbola card shows 9 km.
8. Pins and pencil work by keyboard with 44 px targets; how-to lines are spoken once each in five actions.
9. Controls visible without scrolling at 1366x768; plane text at least 10 px in the 680x425 preview.
10. No network, no images, no em dashes; the concept line and folder rename are flagged for the integrating session.

## Open questions
- cone-slicer: renamed "Conic Focus Finder" and reshaped as the overlap note suggested (no cone, no slicing). The
  folder stays tools/cone-slicer until the integrating session moves it. Agree with the name?
