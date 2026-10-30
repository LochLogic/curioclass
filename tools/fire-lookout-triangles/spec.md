# Fire Lookout Triangles

## One idea
Two fire lookouts each swing a sight onto the same column of smoke, and the two sight lines plus the known distance
between the towers make a triangle you solve with the law of sines to put the fire on the map; a third tower then
checks your answer with the law of cosines, and a radio call with one distance shows when a triangle has two answers.

## Not like
- imaginary-island (gr 11, map): the other 9-12 math map; there a map position is a complex number and arithmetic is travel. Here the map is a real-feeling forest and nothing moves except sight lines and a crew truck.
- shadow-measure (gr 10, geometry lab): right-triangle trig with shadows (G-SRT.C). Here no triangle has a right angle on purpose (except one radio case), and the tools are the laws of sines and cosines.
- flight-planner (gr 12, this group): bearings too, but there they set velocity vectors that add; here bearings are only lines of sight and nothing adds.
- conic-focus-finder (this group): distances to two fixed points too, but there the rule makes a curve; here two angles fix one point.
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

Stage: a map of the made-up Larkspur Range at real pixel size (equal scale both ways), x from -4 to 20 miles east, y
from -14 to 18 miles north, north up, with a north arrow and a scale bar ("5 mi"). The ground is a painted top-down
forest (art: forest-canopy, a 3:4 texture that fills the map frame, dimmed); contours, Blue Lake, Cedar Creek and the
roads are drawn in code over it, because their positions are part of the math. Three lookout towers: A Larkspur
Lookout, B Granite Dome Lookout, C Owl Point Lookout, each the painted tower cutout (art: lookout-tower, about 40 px)
standing on its point with its letter in code beside it.
The map is the focus in every mode: it is the largest thing on screen, centered, with the panel beside it (under it
below 1000 px, the map still filling the width).
The baseline A to B is drawn as a thin solid line labeled "14.0 mi". When a mode needs it, A to C is drawn too
("12.0 mi"). Each tower has a sight: a long thin line from the tower with a round handle 3 miles out; dragging the
handle turns the sight. Each tower shows its azimuth in a tag ("A 035°"). Sight colors: A `--gr-1` solid, B `--gr-2`
dashed, C `--gr-3` dotted, so no line relies on color.

Panel (`.sec` cards, scrolls inside itself; the mode's main button stays at the top):

### Spot (explore, default)
- Focus: the triangle A, B, smoke on the map; the "Triangle" readouts sit at the top of the panel.
- Tap anywhere on the map to put up a smoke there (the painted plume, art: smoke-plume, its base on the point, with a
  red-orange base dot in code). Both sights A and B swing to it (animated 400 ms; instant with Motion off). A new tap
  during the swing moves the smoke at once and the sights turn from where they are.
- The triangle A, B, smoke fills faintly. Panel "Triangle": angle at A, angle at B, angle at the fire (whole degrees
  from the rounded azimuths), sides AB, A to fire, B to fire (miles, 2 decimals).
- `Show the law of sines` opens a worked card: "AF / sin B = AB / sin F", the numbers put in, the answer.
- Toggle `Tower C check`: draws C's sight to the smoke and a circle around C with radius from the law of cosines
  (card "CF² = AC² + AF² - 2(AC)(AF)cos(angle CAF)" with numbers). The circle passes through the smoke.
- Edge: a smoke on the line through A and B (angle at the fire 0) shows "The sights line up. No triangle, so no fix:
  ask a tower off this line." Smokes are limited to the map; tapping a tower does nothing.

### Dispatch (the main task)
Focus: the map with the smoke and the sight being dragged; the open step card sits at the top of the panel, and the
step's number boxes sit next to its `Check`.
Picker: `Smoke 1` to `Smoke 4`, `New smoke` (random). A smoke appears; the sights start at their default azimuths
(A 000°, B 000°). Steps, each a card that unlocks the next:
1. "Sight the smoke": drag A's handle (or Tab to it, arrows turn 1°, Shift+arrows 10°) until the sight passes through
   the smoke; the tag reads the azimuth. The sight snaps when within 0.5° of the smoke's true azimuth. Same for B.
2. "Angles in the triangle": number boxes for angle A, angle B, angle F (whole degrees). Hint button
   `How do I get angle A?` shows: "Angle A is the gap between A's azimuth to B (070°) and A's azimuth to the smoke."
3. "Distance from A": a box for AF in miles. `Check`.
4. "Tower C confirms": a box for CF (law of cosines). `Check`. A correct CF draws C's circle through the fire.
5. `Dispatch crew`: the painted crew truck (art: crew-truck, top view, turned in code to face along the road)
   drives from A along the roads (drawn path, 3 s; instant with Motion off) to the fire; the smoke's base shows the
   painted flame (art: flame) until the truck arrives, then turns to a ring with "Crew on scene". A tap on another
   smoke, `Start over` or a mode button during the drive stops it at once. The log lists the smoke with AF and CF.
`Start over` clears the current smoke.

### Radio (the ambiguous case)
Focus: A's sight and the circle around B on the map, where the spots are tapped; the call text sits on a card with a
painted handheld radio (art: radio-handset) at the top of the panel.
A crew truck radios one distance; tower A sees its dust at one azimuth. Picker `Call 1` to `Call 3`. On screen: A's
sight (fixed at the call's azimuth), a circle around B with the radioed radius, and the call text. The student taps
`0 spots`, `1 spot` or `2 spots`, then taps each spot where the circle meets A's sight (or `No spot`). Each tapped
spot (within 0.3 mi of a true one) gets a pin with its distance from A. The card then shows the SSA work: "sin T =
AB sin A / BT", both angles T and 180 - T when both fit, and why.

### Burn area
Focus: the zoomed burn triangle, filled with the painted burn scar (art: burn-scar, a texture clipped to the triangle).
A fire's edge mapped by two crews leaving the same corner. Picker `Burn 1` to `Burn 3`. The map zooms (view x and y
2 miles wide, animated over 600 ms; a tap on another burn during it jumps there at once) to the burn: two walked sides with their lengths and the angle between, the third side dashed.
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
| 4 | 120° | 200° | 50 | 50 | 80 | 10.89 | 10.89 | 30 | 6.02 | 034.7° |
Fire positions: 1 (10.44, 14.91), 2 (14.45, -2.55), 3 (1.98, 11.24), 4 (9.43, -5.45).

`New smoke`: pick a random point inside the map at least 2 mi from every tower, with angle F between 25° and 155°;
round both azimuths to whole degrees; the fire for checking is where the rounded sights cross (so every number the
student works with is exact from the angles they read).

Radio calls (A's sight at azimuth 040°, so angle A = 30°; AB = 14.0; the height from B to A's sight is 14 sin 30° = 7):
- Call 1: "Engine 6: we're 9 miles from Granite Dome." 9 is between 7 and 14: two spots. T = 51.06° gives AT = 17.78 mi
  at (11.43, 13.62); T = 128.94° gives AT = 6.47 mi at (4.16, 4.95). Card adds: "Two answers fit. Ask the crew one
  more thing: they say Blue Lake is about 2 miles south of them." (Blue Lake's north shore, y = 11.5, lies 2.1 mi south
  of the far spot; from the near spot the lake is about 6 mi north and 7 mi east, so the far spot.)
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

Map features (drawn in code over the painted forest, positions in miles): ridgeline contours around each tower peak, Blue Lake (ellipse
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
Local FLUX (`scripts/localart.py`), no people. One style (from art/prompts.json): painterly, calm dusk colors, deep blue
haze over forested ridges, soft warm light; map pieces are painted from straight above.
- flt-lookout-dusk (made 2026-10-27, review pending): "A small wooden fire lookout cabin with wraparound windows on a
  rocky mountain summit at dusk, forested ridges fading into blue haze behind it, one thin column of gray smoke rising
  far away from a distant ridge, an empty landscape"; 16:9; cutout no; people no; behind the Spot welcome card (dimmed
  to 35 percent) and in preview.svg.
- forest-canopy: "Top-down aerial view of a dense dark green conifer forest at dusk, scattered rocky clearings and
  meadows, soft even light, painterly, full frame"; 3:4; cutout no; people no; the map's ground, dimmed so the code
  contours, lake, creek, roads and labels keep their contrast.
- lookout-tower: "A small wooden fire lookout tower on four tall timber legs with a square glass cab and a pointed roof,
  seen slightly from above, dusk light, painterly, plain white background"; 1:1; cutout yes; people no; towers A, B
  and C on the map (letters in code).
- smoke-plume: "A single thin column of gray wood smoke rising and curling to one side, soft dusk light, painterly, plain
  black background"; 9:16; cutout yes; people no; every smoke on the map, base on the fire point.
- flame: "A small bright orange and yellow campfire-sized flame with a few sparks, painterly, plain black background";
  1:1; cutout yes; people no; the fire point in Dispatch until the crew arrives.
- crew-truck: "A red wildland fire engine truck seen from directly above, a hose reel and ladder on its roof, painterly,
  plain white background"; 4:3; cutout yes; people no; drives the road to the fire (turned in code).
- radio-handset: "A rugged handheld two-way radio with a short antenna and a blank screen, painterly, plain white
  background"; 3:4; cutout yes; people no; the call card in Radio.
- burn-scar: "Top-down view of burned forest ground, black ash and charred logs with gray embers and patches of scorched
  orange needles, painterly, full frame"; 1:1; cutout no; people no; a texture clipped to the burn triangle.
The sights, handles, triangles, circles, contours, lake, creek, roads, labels, north arrow and scale bar are drawn in
code (they carry the math and must sit at exact positions).

## Voice
`gravel-ranger` (Algenib), style "Say warmly with a gravelly voice, like an old park ranger teaching a new lookout."
No other tool in this group or any 9-12 math neighbor uses it. `Curio.voice` with `scope: () => state.mode`. Cards and
readouts are read on screen; Read speaks the hint.
- spot (how, Spot welcome; stale after the first smoke): "Tap the map to put up a smoke. Both towers swing their sights onto it."
- spotC (how, first time Tower C check is on; stale when it is turned off): "Tower C draws a circle with the law of cosines. The fire sits on it."
- noCross (event, a Spot smoke whose sights never cross; stale on the next tap): "These sights never cross. Tap a smoke off the line between the towers."
- dispatch (how, Dispatch welcome; stale once a smoke is picked): "Tap Smoke 1 to start. Then drag each tower's sight handle onto the smoke."
- angles (how, step 2 opens; stale when step 3 opens): "Type the three angles inside the triangle. They add to one hundred eighty degrees."
- af (how, step 3 opens; stale when step 4 opens): "Use the law of sines. Type the distance from tower A to the fire, then press Check."
- cf (how, step 4 opens; stale when Dispatch crew is pressed): "Now tower C. Use the law of cosines to type the distance from C, then press Check."
- crew (how, step 4 passed the first time; stale once the truck leaves): "Press Dispatch crew to send the truck."
- right (event, a correct check; stale when the step changes): "That checks out."
- miss (event, a wrong check; stale on the next edit): "Not yet. Look at the step the note points to, then fix that box."
- onScene (event, the truck arrives; stale on a new smoke): "Crew on scene."
- radio (how, Radio welcome; stale once a count is chosen): "A crew radioed one distance. Tap how many spots fit, then tap each spot on the map."
- two (event, Call 1 solved; stale on a new call): "Two spots fit the same numbers. That is the ambiguous case."
- burn (how, Burn area welcome; stale after the first Check): "Two crews walked the fire's edge from one corner. Type the area, then press Check."

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
- Checks run again (Python, 2026-10-29): towers B (13.156, 4.788) and C (6.000, -10.392); for smokes 1 to 4 the angles,
  AF, BF, CAF, CF and fire positions all match the table, B's azimuth to each fire is exactly its listed reading, and
  sines rounded to 4 places land within 0.003 mi of AF (inside the 0.05 tolerance). Smoke 4's C reading is 034.7°, not
  034.5° as the first draft said; Smoke 2's is 047.1° (shown 047°). Radio: height 7.00; Call 1 T 51.06° and 128.94°, AT
  17.78 and 6.47 at (11.43, 13.62) and (4.16, 4.95); Call 2 T 90°, AT 12.12; Call 3 none. Blue Lake's north shore is 2.1
  mi south of the far spot, so the card now says "about 2 miles" instead of "just south". Burns 0.4013, 1.4095 and 0.32
  square miles, 256.8, 902.1 and 204.8 acres.

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
9. Focus: at 1366x768 and 1000x625 the map is the largest thing on the stage in every mode, with the painted forest,
   towers, smoke and truck on it and every label at least 10 px.
10. Tap while it plays: during a sight swing, the truck's drive or the Burn zoom, a new map tap, smoke, burn or mode
   button acts at once and the readouts match the new state.
11. Main controls visible without scrolling at 1366x768 and 1280x720; map text at least 10 px in the 680x425 preview.
12. No network requests; no em dashes; no image has people.

## Open questions
- fire-lookout-triangles: the fire finder history line names no inventor or year (I could not pin a source for one).
  Fine to leave the instrument unnamed, or should a later pass add the Osborne Firefinder with a checked source?
