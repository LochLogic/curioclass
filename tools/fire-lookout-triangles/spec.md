# Fire Lookout Triangles

## One idea
Two fire lookouts each swing a sight onto the same column of smoke, and the two sight lines plus the known distance
between the towers make a triangle you solve with the law of sines to put the fire on the map; a third tower then
checks your answer with the law of cosines, and a radio call with one distance shows when a triangle has two answers.

## Not like
- imaginary-island (gr 11, map): the other 9-12 math map; there a map position is a complex number and arithmetic is travel. Here the map is a real-feeling forest and nothing moves except sight lines and a crew truck.
- shadow-measure (gr 10, geometry lab): right-triangle trig with shadows (G-SRT.C). Here no triangle has a right angle on purpose (except one radio case), and the tools are the laws of sines and cosines.
- flight-planner (gr 12, this group): bearings too, but there they set velocity vectors that add; here bearings are only lines of sight and nothing adds.
- cone-slicer (Conic Focus Finder, this group): distances to two fixed points too, but there the rule makes a curve; here two angles fix one point.
- ramp-and-roof (gr 10): building slopes and right triangles; no surveying.

## Who and how
Grade 12, precalculus (Solving Any Triangle, Trigonometry). Students drive on their own laptops, alone or in pairs.
25 to 40 minutes. Explore first: Spot opens with no task.
Topic line: "law of sines and law of cosines".
Standards: G-SRT.D (D.9 area of any triangle, one half ab sin C; D.10 the laws as a tool; D.11 use the laws to find
unknown measurements in non-right triangles, with the ambiguous case).
tool.json: driver "students", minutes "25-40", modes ["Spot", "Dispatch", "Radio", "Burn area"].

## Screens and modes
Header (kit, 9-12 theme): "Fire Lookout Triangles", small line "Larkspur Range, a made-up forest". Mode buttons
`Spot`, `Dispatch`, `Radio`, `Burn area`; kit buttons `Motion`, `Sound`, `Read`.

Stage: a map of the made-up Larkspur Range drawn in code at real pixel size (equal scale both ways), x from -4 to 20
miles east, y from -14 to 18 miles north, north up, with a north arrow and a scale bar ("5 mi"). Three lookout towers:
A Larkspur Lookout, B Granite Dome Lookout, C Owl Point Lookout, each a small square cab on a peak with its letter.
The baseline A to B is drawn as a thin solid line labeled "14.0 mi". When a mode needs it, A to C is drawn too
("12.0 mi"). Each tower has a sight: a long thin line from the tower with a round handle 3 miles out; dragging the
handle turns the sight. Each tower shows its azimuth in a tag ("A 035°"). Sight colors: A `--gr-1` solid, B `--gr-2`
dashed, C `--gr-3` dotted, so no line relies on color.

Panel (`.sec` cards, scrolls inside itself; the mode's main button stays at the top):

### Spot (explore, default)
- Tap anywhere on the map to put up a smoke there (a gray plume drawn in code with a red-orange base dot). Both
  sights A and B swing to it (animated 400 ms; instant with Motion off).
- The triangle A, B, smoke fills faintly. Panel "Triangle": angle at A, angle at B, angle at the fire (whole degrees
  from the rounded azimuths), sides AB, A to fire, B to fire (miles, 2 decimals).
- `Show the law of sines` opens a worked card: "AF / sin B = AB / sin F", the numbers put in, the answer.
- Toggle `Tower C check`: draws C's sight to the smoke and a circle around C with radius from the law of cosines
  (card "CF² = AC² + AF² - 2(AC)(AF)cos(angle CAF)" with numbers). The circle passes through the smoke.
- Edge: a smoke on the line through A and B (angle at the fire 0) shows "The sights line up. No triangle, so no fix:
  ask a tower off this line." Smokes are limited to the map; tapping a tower does nothing.

### Dispatch (the main task)
Picker: `Smoke 1` to `Smoke 4`, `New smoke` (random). A smoke appears; the sights start at their default azimuths
(A 000°, B 000°). Steps, each a card that unlocks the next:
1. "Sight the smoke": drag A's handle (or Tab to it, arrows turn 1°, Shift+arrows 10°) until the sight passes through
   the smoke; the tag reads the azimuth. The sight snaps when within 0.5° of the smoke's true azimuth. Same for B.
2. "Angles in the triangle": number boxes for angle A, angle B, angle F (whole degrees). Hint button
   `How do I get angle A?` shows: "Angle A is the gap between A's azimuth to B (070°) and A's azimuth to the smoke."
3. "Distance from A": a box for AF in miles. `Check`.
4. "Tower C confirms": a box for CF (law of cosines). `Check`. A correct CF draws C's circle through the fire.
5. `Dispatch crew`: a truck icon drives from A along the roads (drawn path, 3 s; instant with Motion off) to the fire;
   the fire dot turns to a ring with "Crew on scene". The log lists the smoke with AF and CF.
`Start over` clears the current smoke.

### Radio (the ambiguous case)
A crew truck radios one distance; tower A sees its dust at one azimuth. Picker `Call 1` to `Call 3`. On screen: A's
sight (fixed at the call's azimuth), a circle around B with the radioed radius, and the call text. The student taps
`0 spots`, `1 spot` or `2 spots`, then taps each spot where the circle meets A's sight (or `No spot`). Each tapped
spot (within 0.3 mi of a true one) gets a pin with its distance from A. The card then shows the SSA work: "sin T =
AB sin A / BT", both angles T and 180 - T when both fit, and why.

### Burn area
A fire's edge mapped by two crews leaving the same corner. Picker `Burn 1` to `Burn 3`. The map zooms (view x and y
2 miles wide, animated) to the burn: two walked sides with their lengths and the angle between, the third side dashed.
Box: area in square miles (2 decimals) then acres (whole). `Check`. Readout after: "Area = ½ab sin C".

## Content
Towers (miles; A at the origin): A (0, 0). B at azimuth 070° from A, 14.0 mi: (13.156, 4.788). C at azimuth 150°
from A, 12.0 mi: (6.000, -10.392). Azimuth from B back to A is 250°; from C back to A is 330°.
Azimuth means degrees clockwise from north, 000° to 359°, always printed with three digits.

Dispatch smokes (azimuths as read; the fire is where the two sights cross):
| Smoke | from A | from B | angle A | angle B | angle F | AF (mi) | BF (mi) | angle CAF | CF (mi) | C reads |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 035° | 345° | 35 | 95 | 50 | 18.21 | 10.48 | 115 | 25.69 | 010° |
| 2 | 100° | 170° | 30 | 80 | 70 | 14.67 | 7.45 | 50 | 11.53 | 047° |
| 3 | 010° | 300° | 60 | 50 | 70 | 11.41 | 12.90 | 140 | 22.00 | 349.5° |
| 4 | 120° | 200° | 50 | 50 | 80 | 10.89 | 10.89 | 30 | 6.02 | 034.5° |
Fire positions: 1 (10.44, 14.91), 2 (14.45, -2.55), 3 (1.98, 11.24), 4 (9.43, -5.45).

`New smoke`: pick a random point inside the map at least 2 mi from every tower, with angle F between 25° and 155°;
round both azimuths to whole degrees; the fire for checking is where the rounded sights cross (so every number the
student works with is exact from the angles they read).

Radio calls (A's sight at azimuth 040°, so angle A = 30°; AB = 14.0; the height from B to A's sight is 14 sin 30° = 7):
- Call 1: "Engine 6: we're 9 miles from Granite Dome." 9 is between 7 and 14: two spots. T = 51.06° gives AT = 17.78 mi
  at (11.43, 13.62); T = 128.94° gives AT = 6.47 mi at (4.16, 4.95). Card adds: "Two answers fit. Ask the crew one
  more thing: they say Blue Lake is just south of them." (Blue Lake lies just south of the far spot only, so the far spot.)
- Call 2: "Engine 2: we're 7 miles from Granite Dome." Exactly the height: one spot, a right angle at T, AT = 12.12 mi
  at (7.79, 9.29).
- Call 3: "Engine 4: we're 6 miles from Granite Dome." Less than 7: no spot. Card: "No point on A's sight is that close
  to B. Someone misread a number."

Burns (two sides from one corner and the angle between):
- Burn 1: 1.2 mi and 0.9 mi, 48°: area 0.40 square miles, 257 acres (0.4013 x 640 = 256.8).
- Burn 2: 2.0 mi and 1.5 mi, 110°: area 1.41 square miles, 902 acres (1.4095 x 640 = 902.1).
- Burn 3: 0.8 mi and 0.8 mi, 90°: area 0.32 square miles, 205 acres (0.32 x 640 = 204.8). A right angle on purpose:
  sin 90° = 1, so the formula falls back to one half base times height.
Fact line under Burn area: "1 square mile = 640 acres."

Map features (drawn in code, positions in miles): ridgeline contours around each tower peak, Blue Lake (ellipse
centered (11, 11), 3 by 1 mi, clear of every fire, spot and the A to B line), Cedar Creek (a curve from (-4, 2) to (20, -6)), two dirt roads from A to the map
edge used by the truck (polylines; the truck's last leg goes straight to the fire).

## Interactions in detail
- Angles in the triangle are computed from azimuths as the smaller turn between two directions:
  `gap(p, q) = |((p - q + 540) mod 360) - 180|`. Angle A = gap(070, azA); angle B = gap(250, azB); F = 180 - A - B.
  If F is 0 or less, or the two sights point away from each other (do not cross on A's side), Spot says "These sights
  never cross." Dispatch smokes never do this.
- AF = AB sin B / sin F. CF = sqrt(AC² + AF² - 2 AC AF cos(gap(150, azA))).
- Checking: angle boxes take whole degrees and must be exact. Distance boxes accept a number within 0.05 mi of the
  value computed from the read azimuths (students who round sines to 4 places land inside). Area: square miles within
  0.01, acres within 1 percent. A wrong answer says which step to look at ("Angle F should make the three angles add
  to 180.") and never shows the answer; `Show me` appears after two misses and fills the box with the worked card.
- Typing accepts "18.2", "18.21", "18.2 mi"; anything else: "Type a number of miles."
- Sight handles: 44 px targets, keyboard as above, aria-valuetext "A sight, azimuth 35 degrees". Handles stay on the
  map edge if dragged off it.
- Radio taps: within 0.3 mi of a true spot pins it; elsewhere: "Not on both the sight and the circle." Choosing the
  wrong count first is allowed: the card says "Look where the circle crosses the sight" and lets them try again.
- Mode change calls `Curio.stop()` and `V.hush()`. Dispatch progress for the four fixed smokes is kept per device
  (localStorage `curio-flt-done`, try/catch) only as check marks on the picker; `Clear marks` removes them.

## Look
Accent (`--brand`) #ff6150, flame red-orange: 5.8:1 on --panel #141b25, 5.5:1 on --sec-bg #18202b; --brand-ink
#10161f on it 6.1:1. Not near any 9-12 math neighbor (amber, orange, teal, cyan, green, gold).
Map palette (night topo, low glare): terrain #18241e, contour lines #34483b (decorative only), lake #1b3347 with
shore #3f6d8f, creek #3f6d8f, roads #7a6649, tower cabs #e8edf3 outline. Text on the map uses --ink #e8edf3 on a
#10161f halo (over 12:1). Smoke plume gray #9aa3ad with the accent base dot.

## Art
- flt-lookout-dusk: a wooden fire lookout cabin with wraparound windows on a rocky summit at dusk, forested ridges
  fading into blue haze, one thin column of gray smoke rising far away, painterly, calm, empty landscape; 16:9;
  cutout no; people no. Used behind the Spot welcome card (dimmed to 35 percent) and in preview.svg.
Everything else (map, towers, sights, smoke, truck, circles, triangles) is drawn in code.

## Voice
`gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old park ranger teaching a new lookout."
No other tool in this group or any 9-12 math neighbor uses it. `Curio.voice` with `scope: () => state.mode`.
- spot (how, Spot welcome): "Tap the map to put up a smoke. Both towers swing their sights onto it."
- spotC (how, first time Tower C check is on): "Tower C draws a circle with the law of cosines. The fire sits on it."
- noCross (event, a Spot smoke whose sights never cross; stale on the next tap): "These sights never cross. Try a smoke off the line between the towers."
- dispatch (how, Dispatch welcome): "Pick a smoke. Drag each tower's sight onto it, then work out the triangle."
- angles (how, step 2 opens): "Find the three angles inside the triangle. They add to one hundred eighty degrees."
- af (how, step 3 opens): "Use the law of sines. Type the distance from tower A to the fire, then press Check."
- cf (how, step 4 opens): "Now tower C. Use the law of cosines to type the distance from C, then press Check."
- right (event, a correct check; stale when the step changes): "That checks out."
- miss (event, a wrong check; stale on the next edit): "Not yet. Look at the step the note points to."
- onScene (event, the truck arrives; stale on a new smoke): "Crew on scene."
- radio (how, Radio welcome): "A crew radioed one distance. Choose how many spots fit, then tap each one."
- two (event, Call 1 solved; stale on a new call): "Two spots fit the same numbers. That is the ambiguous case."
- burn (how, Burn area welcome): "Two crews walked the fire's edge from one corner. Type the area, then press Check."

## Family engine
none. The map, sights and triangles are the tool's own SVG (no plane or axes; positions in miles scaled to pixels).

## Sources
- Law of sines, law of cosines, the ambiguous case (SSA) and area = ½ab sin C: OpenStax, Algebra and Trigonometry 2e,
  10.1 "Non-right Triangles: Law of Sines" and 10.2 "Law of Cosines",
  https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-1-non-right-triangles-law-of-sines
- Lookouts locate fires by crossing azimuth readings from two towers on a fire finder: USDA Forest Service, "Fire
  Lookouts" history pages, https://www.fs.usda.gov/ (search "fire lookout"), and Forest Fire Lookout Association,
  https://www.firelookout.org/
- 1 square mile = 640 acres: NIST Handbook 44, Appendix C, units of area, https://www.nist.gov/pml/owm/nist-handbook-44-current-edition
- Standards: CCSS Math, High School Geometry, G-SRT.D, https://www.thecorestandards.org/Math/Content/HSG/SRT/
- The forest, towers, smokes, calls and burns are made up; every value above was computed in Python (2026-10-27).

## Done when
1. Spot: tapping the map swings both sights to the smoke and the triangle readouts add to 180°; a smoke on the A-B
   line gives the "sights line up" note.
2. Dispatch Smoke 1: A reads 035°, B 345°; angles 35, 95, 50 are accepted; AF 18.21 (and 18.2) is accepted, 18.0 is
   not; CF 25.69 is accepted and C's circle passes through the fire at (10.44, 14.91).
3. Smoke 2: AF 14.67, CF 11.53. Smoke 4: AF = BF = 10.89 (an isosceles triangle). Smoke 3: CF 22.00.
4. `New smoke` always gives sights that cross, and the checker uses the rounded azimuths.
5. Radio Call 1 accepts "2 spots" and pins both (AT 17.78 and 6.47); Call 2 has one spot at 12.12 mi; Call 3 has none.
6. Burn 1 accepts 0.40 square miles and 257 acres; Burn 2 0.41 is refused and 1.41 accepted.
7. Sight handles turn with arrow keys (1° and 10°) and read their azimuth aloud to a screen reader.
8. Every how-to line is spoken once in a run of five actions; "That checks out." is spoken on every correct check.
9. Main controls visible without scrolling at 1366x768 and 1280x720; map text at least 10 px in the 680x425 preview.
10. No network requests; no em dashes; the one image has no people.

## Open questions
- fire-lookout-triangles: the fire finder history line names no inventor or year (I could not pin a source for one).
  Fine to leave the instrument unnamed, or should a later pass add the Osborne Firefinder with a checked source?
