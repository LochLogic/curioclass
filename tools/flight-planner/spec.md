# Flight Planner

## One idea
The plane flies where its own velocity plus the wind's velocity point, not where its nose points, so you draw the
two arrows tip to tail, watch the plane slide along their sum, and learn to aim into the wind until the sum lands
you on the next island.

## Not like
- imaginary-island (gr 11, map): adding a complex number walks a fixed step. Here the arrows are velocities (knots), they act for a time, the wind changes per leg, and you solve backward for the heading.
- two-trains (gr 8, simulator): speeds on one line; here speeds have directions and add as vectors in the plane.
- fire-lookout-triangles (this group): azimuths there are sight lines that cross; here they are directions of arrows that add.
- image-transformer (this group): vectors there are columns of a matrix that move a picture; here a vector is a velocity that moves a plane.
- ferris-wheel (gr 11, simulator): circular motion and sine; no vectors added.

## Who and how
Grade 12, precalculus (Vectors). Students drive, alone or in pairs, 25 to 40 minutes. Explore first: Free fly opens
with the plane parked and both arrows live.
Topic line: "adding velocity vectors".
Standards: N-VM.A (magnitude and direction, components, end minus start), N-VM.B (add tip to tail and by components,
subtract, multiply by a scalar), AP-PRECALC.U4 (vectors in context, 4.5 to 4.6 in the AP course).
CCSS clusters per mode: Free fly N-VM.A and N-VM.B.4a; Flight plans N-VM.B.4 (add, and subtract in Find the wind)
and N-VM.B.5 (time times velocity); Landing N-VM.A.1 and components.
tool.json: driver "students", minutes "25-40", modes ["Free fly", "Flight plans", "Landing"].

## Screens and modes
Header (kit, 9-12 theme): "Flight Planner", small line "Islands of the Saltwind Chain, a made-up map". Modes
`Free fly`, `Flight plans`, `Landing`; kit `Motion`, `Sound`, `Read`.

Stage left: a chart of the made-up Saltwind islands at real pixel size, x from -55 to 105 nautical miles east, y from
-40 to 45 north, equal scale, north up, scale bar "20 nm", compass rose. The sea is a painted texture (art: sea-texture)
and each island is its fixed code polygon filled with a painted land texture (art: land-texture, clipped to the
polygon), so the coastlines stay exact. Six airfields (runway symbol and name in code). The plane is the painted
top-view plane (art: plane-top, cutout, about 36 px), turned in code so its nose points along its heading.
The chart is the focus in Free fly and Flight plans: it is the largest thing on the stage, centered, with the vector
card beside it; the same three arrows are drawn at the plane so the eye need not leave the chart.
Stage right (or below the chart under 1000 px): the vector card, a small square plane of its own (knots, -120 to 120
both ways, grid every 20) where the three arrows are drawn tip to tail from the origin: air arrow (`--gr-1` solid,
"plane"), wind arrow starting at the air arrow's tip (`--gr-2` dashed, "wind"), and their sum from origin to the wind
tip (`--brand`, thick, "ground"). The same three arrows are drawn small on the chart at the plane.

Panel cards: "Plane" (heading box and slider 000 to 359, airspeed box and slider 60 to 140 kt), "Wind" (from box and
slider 000 to 359, speed 0 to 40 kt, with a painted windsock, art: windsock, turned in code to stream the way the wind
blows), "Components" (table, east and north for plane, wind, ground; ground row = sum,
magnitude and direction), "Flight" (`Fly`, `Pause`, `x4` speed toggle, `Reset`, clock "0:00 flown").

### Free fly (explore, default)
Focus: the plane on the chart with its 30-minute line, and the ground arrow on the vector card.
The plane sits on Pelican Key. Drag the tip of the air arrow or the wind arrow on the vector card (or use the sliders
and boxes) and everything updates live: the ground arrow, the components table, and a dashed "where you will be in
30 minutes" line on the chart (0.5 h times the ground velocity). `Fly` moves the plane along the ground velocity, nose
still pointing along the heading, so in a crosswind it visibly flies sideways (crab). Time: 1 real second = 2 flight minutes (x4 makes it 8), so the longest plan (39 min) plays in about 20 s. The plane leaves a thin trail. Flying off the chart pauses with "Off the chart. Press Reset."

### Flight plans
Focus: the chart with the course line, the plane and the target field; the plan card and the three number boxes sit at
the top of the panel.
Picker: `Plan 1` to `Plan 5`, then `Find the wind 1`, `Find the wind 2`. A plan card gives from, to, course
(the direction you must travel over the ground), distance, wind and airspeed (always 100 kt). The wind card is locked
to the plan. The student:
1. Sets a heading (box or the air arrow's tip, airspeed locked at 100). The ground arrow shows where that heading goes;
   a thin target line shows the course.
2. Types the ground speed they expect (kt) and the flight time (minutes).
3. `Fly it`: the plane flies their heading. It lands "On the field" if it ends within 2.5 nm of the field (the
   field's circle, drawn) when the clock reaches their time, otherwise the chart marks where it ended and how far off, and `Try again` resets.
A `Check my numbers` button grades heading (within 1 degree), ground speed (within 1 kt) and time (within 1 min)
separately, with the error direction ("Your ground speed is too high: the wind has a part against you.").
Find the wind: the card gives a heading and airspeed flown and the track and ground speed actually made good; the
student drags the wind arrow (or types from and speed) until air + wind = ground. Checked within 1 kt and 2 degrees.

### Landing
Focus: the zoomed runway (art: runway-top, its number in code at the threshold) with the plane on final, centered and
large; the "Wind on the runway" card sits beside it.
Picker `Approach 1` to `Approach 3`. The chart zooms to one runway (drawn 1 nm long, numbered). Approach airspeed 65 kt.
The wind is given "from" a direction. Panel card "Wind on the runway": two boxes the student fills, crosswind and
headwind components (kt), then the crab heading. `Fly final` animates the last 2 nm: a correct crab keeps the plane on
the centerline (within 2 degrees) and it touches down with "Landed on the centerline"; otherwise it drifts and the
tool shows the drift side and "Go around" (no crash, no sound beyond one soft tone).

## Content
Airfields (nm, Pelican Key at the origin): Pelican Key (0, 0); Harbor Town (60, 0); West Cay (-45, 0); Coral Point
(95.36, 35.36); Gull Rock (71.42, -30.42); North Shoal (-20, 34.64).
Conventions on screen: "Heading: where the nose points. Course or track: where you go over the ground. Wind is named
for where it blows from: wind from 360 pushes you south." "On this chart north is compass north. Real pilots also
correct for the difference between true and magnetic north; this chart leaves it out."

Plans (airspeed 100 kt; worked answers):
| Plan | From to | Course | Dist | Wind from / kt | Heading | Ground speed | Time |
|---|---|---|---|---|---|---|---|
| 1 | Pelican Key to Harbor Town | 090 | 60 | 360 / 20 | 078 (78.46) | 97.98 | 36.7 min |
| 2 | Pelican Key to West Cay | 270 | 45 | 270 / 25 | 270 | 75.00 | 36.0 min |
| 3 | Harbor Town to Coral Point | 045 | 50 | 090 / 30 | 057 (57.25) | 76.51 | 39.2 min |
| 4 | Coral Point to Gull Rock | 200 | 70 | 320 / 18 | 209 (208.97) | 107.78 | 39.0 min |
| 5 | Pelican Key to North Shoal | 330 | 40 | 240 / 22 | 317 (317.29) | 97.55 | 24.6 min |
Plan 2 is a pure headwind (the sum is just 100 - 25). Plan 4 has a tailwind part, so ground speed beats airspeed.
Flying the rounded heading misses the field by at most 0.49 nm at the exact time (Plan 1) and 0.63 nm at the nearest
whole minute (Plan 5). A heading 1 degree off and a time 1 minute off, the most Check my numbers accepts, miss by at
most 2.44 nm (Plan 5), so the field's circle is 2.5 nm: numbers the checker accepts always land. Heading 090 on
Plan 1 still misses by 12 nm.
Components check (Plan 1): plane (97.98, 20.00) + wind (0, -20.00) = ground (97.98, 0).

Find the wind:
- 1: flew heading 000 at 100 kt, made good track 010 at 104 kt. Wind = ground - air = (18.06, 2.42): 18.2 kt blowing
  toward 082, so wind from 262.
- 2: flew heading 090 at 100 kt, made good track 080 at 90 kt. Wind = (-11.37, 15.63): 19.3 kt, from 144.

Approaches (approach airspeed 65 kt; runway number = its direction divided by 10):
| Approach | Runway | Wind from / kt | Crosswind | Headwind | Crab heading | Ground speed |
|---|---|---|---|---|---|---|
| 1 | 27 (270) | 300 / 15 | 7.50 from the right | 12.99 | 277 (276.63) | 51.58 |
| 2 | 9 (090) | 090 / 12 | 0 | 12.00 | 090 | 53.00 |
| 3 | 18 (180) | 240 / 20 | 17.32 from the right | 10.00 | 195 (195.45) | 52.65 |
Crosswind = wind speed x sin(angle between wind and runway); headwind = wind speed x cos(that angle); crab angle =
arcsin(crosswind / 65), turned toward the wind.

## Interactions in detail
- Vector math: a direction d and speed s give components (s sin d, s cos d) (east, north; azimuth clockwise from
  north). Wind from W points toward W + 180. Ground = air + wind, component by component; its direction is
  atan2(east, north) in degrees mod 360. Printed to 2 decimals in the table, headings as three digits.
- Solving a plan (for the checker): wind correction angle = arcsin(-crosswind part / airspeed), where crosswind part
  = wind speed x sin(wind-to direction - course); heading = course + that angle; ground speed = airspeed x cos(angle)
  + wind speed x cos(wind-to direction - course). If crosswind part is larger than airspeed no heading works: the card
  says "This wind is too strong for this plane." (Only possible in Free fly, where wind is at most 40 and airspeed at
  least 60, so never; the guard stays in the code.)
- Arrow tips on the vector card are draggable (44 px targets), keyboard: arrows turn 1 degree, Shift 10, PageUp and
  PageDown change speed by 1 kt. Tips snap to whole degrees and whole knots. Wind speed 0 hides the wind arrow and
  says "Calm".
- Zero ground speed (possible in Free fly only if wind could match airspeed; it cannot) is guarded anyway: "You are
  hovering over one spot."
- Any change while flying acts at once: the arrows and the plane's ground velocity update on the spot and the plane
  keeps flying the new way (in Flight plans the card then notes "Heading changed in flight"; Landing's `Fly final`
  takes the crab as set when pressed, and a change restarts final from 2 nm). `Pause` stops the clock. `Reset` returns the plane to the start of the current leg and clears the
  trail. Mode change: `Curio.stop()`, `V.hush()`.
- Typed boxes accept "78", "078", "78.5"; out-of-range values clamp with a tip.
- Plan progress: check marks on the picker, kept per device (localStorage `curio-flight-planner`, try/catch) with
  `Clear marks`.

## Look
Accent (`--brand`) #3aa8ff, clear sky blue: 6.8:1 on --panel #141b25, 6.4:1 on --sec-bg #18202b; --brand-ink #10161f
on it 7.1:1. Different from every 9-12 math neighbor (amber, orange, teal, cyan #36c9dd, green, gold), deeper than the
algebra group's #6cc4ff (Algebra Tile Studio), and apart from this group's cornflower (rain-gauge) by hue and lightness.
Chart palette (night chart): sea #0f1d2b, shallows #16314a, land #2a3a2c with coast line #6d8f6a, airfield symbols
#e8edf3, course lines `--muted`. Chart text #e8edf3 on the sea is over 13:1.

## Art
Local FLUX (`scripts/localart.py`), no people. One style: soft painted illustration, night chart colors (deep teal
sea, muted green land), seen from straight above.
- sea-texture: "Top-down view of deep blue-teal open ocean at night, gentle swells and faint moonlit ripples, painted
  texture, full frame"; 16:10; cutout no; people no; the chart's sea, dimmed so chart text keeps its contrast.
- land-texture: "Top-down view of a small tropical island interior, low green scrub, palm crowns and sandy paths,
  painted texture, full frame"; 1:1; cutout no; people no; tiled and clipped to each island polygon.
- plane-top: "A small white single-engine propeller airplane seen from directly above, nose pointing up, wings level,
  painted illustration, plain white background"; 1:1; cutout yes; people no; the plane on the chart and on final
  (turned in code).
- runway-top: "Top-down view of one long gray asphalt runway with plain white edge lines and a white dashed center
  line, grass on both sides, painted illustration"; 9:16; cutout no; people no; Landing's zoom, turned in code to the
  runway's direction (its number is code text at the threshold).
- windsock: "An orange and white striped airport windsock on a short pole, streaming straight out to the right in a
  breeze, painted illustration, plain white background"; 1:1; cutout yes; people no; the Wind card, turned with the
  wind.
The vector card, arrows, grid, course lines, compass rose, scale bar, airfield symbols, labels, coast lines and
preview.svg are drawn in code (they are the vectors and the chart).

## Voice
`firm-captain` (Alnilam), style "Say firmly but kindly, like a calm flight instructor in the right seat." Not used by
any group sibling; launch-pad (gr 9) also uses it (see Open questions). `Curio.voice`, `scope: () => state.mode`.
Cards and readouts are read on screen; Read speaks the hint.
- free (how, Free fly welcome; stale after the first arrow drag): "Drag the tip of the plane arrow or the wind arrow. The thick arrow is where you really go. Then press Fly."
- crab (how, first flight with a crosswind; stale on Reset): "See the nose point one way while the plane moves another. That is the wind adding on."
- plans (how, Flight plans welcome; stale once a plan is picked): "Tap Plan 1. Set a heading so the thick arrow lies on the course line, then press Fly it."
- numbers (how, first plan opened; stale once both boxes are filled): "Type your ground speed and time too. Time is distance divided by ground speed."
- onField (event, landed within tolerance; stale on Reset or a new plan): "On the field. Nice flying."
- off (event, missed; stale on Try again): "You missed the field. Check which way the wind pushed you, then press Try again."
- findWind (how, first Find the wind; stale after the first wind drag): "Drag the wind arrow until plane plus wind matches the track you made good."
- landing (how, Landing welcome; stale once both boxes are filled): "Type the crosswind and the headwind, then set a crab heading into the wind and press Fly final."
- landed (event, touchdown on the centerline; stale on a new approach): "Landed on the centerline."
- goAround (event, drift off the centerline; stale on a new try): "Go around. The crosswind pushed you off the centerline. Change the crab and press Fly final."

## Family engine
none. The vector card may reuse `kit/graphing.js` `Plane` for its grid and arrows (`g.segment` with `arrow: 'end'`,
`g.point` for draggable tips); the chart is the tool's own SVG.

## Sources
- Wind triangle, heading versus course, wind correction angle, ground speed; wind is reported by the direction it
  blows from: FAA, Pilot's Handbook of Aeronautical Knowledge (FAA-H-8083-25C), chapter 16 "Navigation",
  https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak
- Crab method on a crosswind approach; crosswind and headwind components: FAA, Airplane Flying Handbook
  (FAA-H-8083-3C), chapter 9, https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/airplane_handbook
- Runway numbers are the runway's magnetic direction in tens of degrees: FAA, Aeronautical Information Manual 2-3-3,
  https://www.faa.gov/air_traffic/publications/atpubs/aim_html/
- 1 knot = 1 nautical mile per hour; 1 nautical mile = 1852 m: NIST SP 811, Appendix B,
  https://www.nist.gov/pml/special-publication-811
- Vector addition, components, magnitude and direction: OpenStax, Precalculus 2e, 10.8 "Vectors",
  https://openstax.org/books/precalculus-2e/pages/10-8-vectors
- Standards: CCSS Math N-VM, https://www.thecorestandards.org/Math/Content/HSN/VM/ ; College Board, AP Precalculus
  Course and Exam Description (2023), Unit 4.
- Islands, plans, winds and approaches are made up; every value above computed in Python (2026-10-27).
- Checks run again (Python, 2026-10-29): courses, distances, headings, ground speeds and times for Plans 1 to 5 match
  the table; components check (97.98, 20.00); Find the wind 1 (18.06, 2.42), 18.22 kt from 262.4; Find the wind 2
  (-11.37, 15.63), 19.33 kt from 144.0; Approaches 1 to 3 crosswind, headwind, crab and ground speed match. Misses:
  rounded heading at exact time 0.49, 0, 0.28, 0.04, 0.21 nm; at the nearest whole minute 0.58, 0, 0.35, 0.06, 0.63 nm;
  worst within the checker's 1 degree and 1 minute 2.33, 1.64, 1.92, 2.30, 2.44 nm. The first draft's 1.5 nm field
  could reject numbers the checker passed, so the field is now 2.5 nm. Heading 090 on Plan 1 ends at (60, -12), 12 nm
  south. Plan times at 2 flight minutes per second: 12 to 20 s each.

## Done when
1. Free fly: heading 090, airspeed 100, wind from 360 at 20 shows ground (97.98, 0.00), 97.98 kt toward 090, and the
   plane flies east with its nose pointing 078 only if the heading is set to 078; with heading 090 it drifts south.
2. Plan 1 with heading 078, ground speed 98, time 37 lands "On the field" (0.58 nm off); heading 090 misses to the south by about
   12 nm (60 nm at 20 kt for 0.6 h).
3. Plan 2: heading 270, 75 kt, 36 min. Plan 4: ground speed 108 is accepted (tailwind part).
4. Find the wind 1 accepts wind from 262 at 18 kt; Find the wind 2 accepts from 144 at 19 kt.
5. Approach 1: crosswind 7.5, headwind 13.0, crab 277 lands on the centerline; heading 270 drifts left and goes around.
6. The components table always sums: ground east = plane east + wind east (spot-check three settings).
7. Arrow tips work by keyboard; headings print as three digits; wind 0 shows "Calm".
8. Each how-to line is spoken once in a run of five actions; "On the field" is spoken every time.
9. Focus: at 1366x768 and 1000x625 the chart is the largest thing on the stage in Free fly and Flight plans, and the
   runway in Landing; the painted plane turns with the heading.
10. Tap while it plays: during a flight, a heading, wind or speed change acts at once (the plane changes course on the
   spot and the components table matches); `Pause` and `Reset` work mid-flight.
11. Main controls visible without scrolling at 1366x768, 1280x720 and in the 800x500 preview; 375 wide stacks chart,
   vector card, panel.
12. No network, no people in any image, no em dashes.

## Open questions
- [flight-planner] Voice: firm-captain is also launch-pad's (gr 9, listed as a neighbor). Every kept 9-12 voice is already used by a math 9-12 neighbor; the only free ones are the K-2 teachers and lively-host, which do not fit a flight instructor. Keep firm-captain, or take lively-host?
- flight-planner: the chart leaves out magnetic variation (said on screen). Fine for grade 12, or add a variation
  line on one plan?
