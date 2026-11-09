# Which Way Is Down?

## One idea
At four real schools on four sides of the world an apple falls "straight down" every time, but when the student puts
each school's down arrow on the globe and zooms out, the arrows point four different ways in space and all meet at
one spot, Earth's center, so "down" means "toward Earth's center" and the student uses that claim to predict down at
places they have never been.

## Not like
- pocket-universe (grade 6 sandbox): many bodies pulling each other into orbits, no ground and no people. Here one
  planet, one pull, and the question is only which way it points where you stand.
- shadow-clock (grade 5 lab): Earth's spin and orbit read from shadows over days. Here nothing moves in the sky; the
  data is a direction, recorded once per place.
- star-lanterns (grade 5 lab): measuring brightness against distance in a dark field. Here measuring a direction with
  a plumb line, by day.
- particle-zoom (grade 5 explorer): zooms in to the too-small. Here one zoom out, as the payoff of the evidence, not
  the main way to move around.
- moon-phase-model (grade 6, built): a lit Earth and Moon seen from space for phases. Here an X-ray globe with lines
  through the rock and no sunlight model.
- push-the-pumpkin (K lab): pushes and pulls you choose. Here the pull is never chosen, only found.
- world-layers-map (grade 4 map): data layers on a flat map. Here a spinning globe with no data layers.

## Who and how
Grade 5 science, module Gravity (Earth's gravity pulls objects down). Driver: students, one laptop each or pairs;
works on a projector too. 25 to 40 minutes: Drop about 12, Globe 5, Argue 10 to 15, Other worlds 3 (optional).
Standards: 5-PS2-1. Prompts are not personal; no disclosure note needed. tool.json: driver "students or teacher",
minutes "25-40", modes ["Drop", "Globe", "Argue", "Other worlds"], grades_label "Grade 5".
Header: title, `.seg` modes **Drop**, **Globe**, **Argue**, **Other worlds**, kit `motion`, `sound`, `read`.

## Standards map
| Code | Student action | What they see | Done when check |
|---|---|---|---|
| 5-PS2-1 (support an argument that Earth's gravitational force on objects is directed down; "down" = toward the center of the spherical Earth) | Drops an apple, ball and feather tube at four schools; sets each school's down arrow on the globe and records it; zooms out and extends the arrows; in Argue picks a claim, attaches at least three place records as evidence, checks the claim against them, types a reasoning sentence, then predicts down at new places with one try each | Every local drop falls along the plumb line; on the globe four arrows pointing four ways in space that meet at the center; a wrong claim's dashed arrows missing the evidence by a stated number of degrees; each prediction scored against the true plumb line | The argument card shows "Strong" only when: the claim fits every attached record within 8 degrees, at least 3 place records are attached, the reasoning box has 8 or more words, and the last 3 predictions in a row were each within 8 degrees |

## Screens and modes
**On load:** Drop mode at Anchorage, the yard scene filling the stage, Jonah holding the apple out at shoulder height
beside the plumb line stand, the plumb bob hanging still. Apple is picked. Nothing moves except the bob's tiny sway
(off with Motion off). Hint: "Pick something to drop, then tap Drop." The first tap on **Drop** drops the apple at
once; a first tap on a place button flies to that school; either may cut the welcome (BASELINE 16), and the welcome's
content is the hint.

**Layout at 1366x768 (all modes):** header 56 px; stage on the left about 910 x 690; panel on the right about 430
wide. Everything each mode needs is above the fold. At 680x425 the stage keeps at least 60 percent of the width; the
panel keeps the hint and the mode's main buttons on top; the notebook table and the Start over button fold below.
Under 900 px tall the panel uses its compact layout (buttons first, then hint, then the rest). At 760 and 375 wide
the stage stacks on top at 16:9, then the panel.

### Drop
Focus: the yard scene and the falling object (Yard view), then the globe and its arrow (Mark view).
- Panel top to bottom: place buttons **Anchorage, Alaska**, **Quito, Ecuador**, **Sydney, Australia**,
  **Esperanza Base, Antarctica** (each shows a check mark and "recorded" once recorded); object buttons **Apple**,
  **Ball**, **Feather tube**; big **Drop**; toggle **Slow motion** (off); **Mark on globe** (disabled until a drop
  has landed at this place); hint; notebook table (Place | Dropped | Arrow); **Start over** (asks "Clear all four
  records?" with **Clear** and **Keep**). "Saved only on this device." under the table.
- Yard view: painted yard, the kid cutout, the plumb line stand (code: a thin dark line from a hook to a painted
  brass bob), the object in the kid's hand at 1.5 m above the ground (scale bar "1 m" at the left edge). **Drop**:
  the object falls at real speed (0.55 s; Slow motion x10: 5.5 s), leaving a dotted trail that stays until the next
  drop or place change. On landing a small right-angle mark appears where the trail meets the ground, beside the
  plumb line, and the tag "Fell along the plumb line" shows for 3 s. The kid's speech bubble (on screen only) changes
  once per place on the first landing (Content). Taps during a fall: Drop again restarts the fall at once from the
  hand with the picked object; a place button cancels the fall and flies there.
- Flying between schools: a 1.2 s pan over a code globe from one school to the next (instant with Motion off), then
  the new yard. The yards look alike on purpose: in every yard, down is the bottom of the screen.
- Mark view (**Mark on globe**): the stage shows the globe large (radius 300 px, centered), turned so this school sits
  on the globe's edge (Content: side and angle), with a short tangent ground line at the school and a pin. The kid is
  not drawn on the globe in Mark view. A yard inset (260 x 146, top left of the stage) shows the yard with its
  plumb line and the right-angle mark, ground level. An arrow 120 px long sits at the pin pointing straight down the
  screen. The student drags the arrow head (turns it around the pin, 1 degree steps) or taps **Turn left** /
  **Turn right** (5 degrees), then **Record**. **Back to yard** returns without recording.
  - Hit (within 8 degrees of the true plumb direction, which is toward the globe's center): the arrow snaps to the
    true direction, turns gold, the notebook row fills, the place button gets its check.
  - Miss: the arrow stays where the student put it, red, with "Off by 52 degrees" beside it; the yard inset slides
    onto the globe and turns to lie along the tangent ground line, so its plumb line now points the true way on the
    globe (1 s; instant with Motion off). The student turns the arrow and taps Record again. Nothing is counted.
- After the fourth record: **Zoom out** appears at the top of the panel (gold) and the hint names it. Zoom out opens
  Globe and plays the reveal.

### Globe
Focus: the globe, centered, radius 320 px, on a painted starfield.
- Code globe (orthographic, Natural Earth 110m land, ocean #1d4f7a, land #6fa36b, latitude lines every 30 degrees)
  with each recorded school as a pin, its kid cutout standing on the edge when the school is within 10 degrees of the
  edge (rotated so feet are on the ground and head points out, so Ruby in Sydney looks upside down from space while
  standing on her own ground), and its recorded arrow.
- Reveal (once, after Zoom out; replay with **Replay**): the view turns to center 20 S, 100 W (Content); the globe
  fades to see-through (X-ray, 1 s); each arrow stretches through the rock in turn (Anchorage, Quito, Sydney,
  Esperanza, 0.8 s each), all four meet at a glowing dot labeled "Earth's center: 6,371 km below every school". Each
  step waits for its voice line (Heard in order). Any tap during the reveal finishes it at once.
- Controls: drag the globe to spin it (any axis; the lines always meet at the dot); **X-ray** (on after the reveal);
  **Extend lines** (on after the reveal; off shows arrows 120 px long); tap the globe's surface to stand a new kid
  there (up to 8; a pin with a gold plumb line to the center; on the edge the kid cutouts are reused in turn);
  **Clear kids**; **Reset view**; **Replay**. Before any record, the globe shows no arrows and the hint says
  "Tap the globe to stand a kid anywhere, or record drops in Drop."
- What the picture shows for each case: 0 records, plain globe; 1 record, one arrow and no dot; 2 to 4 records with
  Extend lines on, the lines meet at the dot; added kids on the far side show their lines through the X-ray rock.

### Argue
Focus while building: the argument card (stage left, 540 wide). Focus while testing: the globe (stage right grows
to 600 wide; the card shrinks to a 300 wide strip).
- Card sections: **Claim** slot, **Evidence** slots (up to 5), **Check** line, **Reasoning** box ("My evidence
  supports my claim because"), **Tests** list, status "Building", "Fits your evidence", "Strong".
- Panel: the four claim cards (Content; same size, same color, order shuffled per page load); the evidence cards
  (one per recorded place, plus **Feather tube** and **Other worlds** cards once those were used); **Check claim**;
  **Test it**; during a test **Turn left**, **Turn right**, **Predict**, **Next place**; hint.
- Tap a claim card to put it in the slot (tap another to swap). Tap an evidence card to attach or detach it. With
  fewer than 3 recorded places, the place cards show "Record this in Drop" and **Go to Drop** appears.
- **Check claim** (enabled with a claim and 3 or more place cards attached): the globe draws, at each attached place,
  the recorded arrow (solid gold) and the arrow the claim predicts (dashed white), with the gap in degrees. Fits only
  if every gap is 8 degrees or less. Feather tube and Other worlds cards draw nothing and the card notes "about how
  fast, not which way" beside them; they never count toward the 3.
- **Test it** (enabled once the claim fits): a new place from the test pool (Content) appears on the edge of a clean
  globe: opaque, no center dot, no old arrows, no kid, ground tangent and pin only. The arrow starts pointing straight
  down the screen. The student turns it and taps **Predict** (one try per place). Then X-ray turns on, the true plumb
  line draws to the center, an apple slides down it, and the verdict shows ("Hit: 3 degrees off" in gold, or
  "Miss: 41 degrees off" in red with both arrows kept). The Tests list adds the row. **Next place** (enabled after the
  result line ends) brings the next pool place. After 3 hits in a row the card turns "Strong" (if the reasoning box
  has 8 words; otherwise the hint asks for it) and tests may go on for fun.

### Other worlds
Focus: three side-by-side drop lanes, Earth, Moon, Mars (each 280 x 520 on the stage), each with its own painted
ground strip and a small painted globe of that world below with a gold plumb line to its center.
- **Drop all** drops three identical apples from 1.5 m at once; **Slow motion** is on by default here (x10). Each lane
  shows its landing time in real seconds when its apple lands: Earth 0.55 s, Mars 0.90 s, Moon 1.36 s. Any tap on
  Drop all during a fall restarts all three at once. **Slow motion** toggles take effect at once (the falls rescale
  from where they are).
- Panel: Drop all, Slow motion, hint, a three-row table (World | Gravity | Fall time), and the line "Slower or
  faster, every apple falls toward its own world's center."

## Content
Schools (edge view: globe center on the equator at the given longitude, north up; the school then sits on the edge
at its latitude, on the side given; the true arrow angle is measured counterclockwise from screen right):
| Place | Lat, lon | Kid | View center lon | Side | Edge angle | True arrow |
|---|---|---|---|---|---|---|
| Anchorage, Alaska | 61.2 N, 149.9 W | Jonah | 120.1 E | left | 118.8 | 298.8 |
| Quito, Ecuador | 0.2 S, 78.5 W | Sofia | 168.5 W | right | 359.8 | 179.8 |
| Sydney, Australia | 33.9 S, 151.2 E | Ruby | 118.8 W | left | 213.9 | 33.9 |
| Esperanza Base, Antarctica | 63.4 S, 57.0 W | Valentina | 147.0 W | right | 296.6 | 116.6 |
(Left side: view center = school lon minus 90 degrees, wrapped; right side: plus 90.)

Speech bubbles (on screen, first landing at each place): Jonah: "Down is down here in Alaska." Sofia: "Here near the
equator, it fell straight down too." Ruby: "In Sydney, the ground is under my feet, same as yours." Valentina:
"Esperanza Base has a school, and here the apple falls straight down too."
Place notes under the yard (on screen): Anchorage "Anchorage, Alaska, USA. 61 degrees north." Quito "Quito, Ecuador.
Almost on the equator." Sydney "Sydney, Australia. 34 degrees south." Esperanza "Esperanza Base, an Argentine
research base in Antarctica where families live and children go to school. 63 degrees south."

Objects: Apple, Ball (a rubber playground ball), Feather tube (a clear tube with the air pumped out and a feather
inside; the feather falls with the tube's own small apple, side by side, same speed). Tag after a Feather tube drop:
"With no air in the way, the feather falls as fast as the apple."

Claims (shuffled; all 84 to 89 characters):
- A (fits): "Gravity pulls things toward Earth's center, so down points a different way at each place."
- B: "Gravity pulls things toward the South Pole, so down points to the bottom of the globe."
- C: "Gravity pulls every place the same one way, so people in Australia hang upside down."
- D: "Gravity pulls toward Earth in the north, but in the south it pulls things off into space."
Predicted arrows: A toward the center; B toward the South Pole point; C parallel to Earth's axis, pointing south; D
toward the center for northern places, straight out for southern ones.

Test pool (shuffled per page load, side alternates right, left, right...; after all 8, reshuffle with sides flipped):
Tokyo 35.7 N, 139.7 E; Cairo 30.0 N, 31.2 E; Oslo 59.9 N, 10.8 E; Honolulu 21.3 N, 157.9 W; Nairobi 1.3 S, 36.8 E;
Cape Town 33.9 S, 18.4 E; Ushuaia 54.8 S, 68.3 W; Buenos Aires 34.6 S, 58.4 W. Each shows its name and latitude.

Reveal view center: 20 S, 100 W, chosen so all four schools are near the visible face or edge; any view works.
Other worlds: Earth 9.8, Moon 1.6, Mars 3.7 (table shows "m/s each second" as the unit, with "Earth's pull" 1, 0.17,
0.38 beside it); drop height 1.5 m.
Notebook and card are saved in localStorage key `wwd-v1` (try/catch).

## Interactions in detail
- Arrow angle: measured from the pin; drag uses the pointer's angle around the pin, rounded to 1 degree; buttons step
  5. Keyboard: with the arrow focused, Left and Right turn 5 degrees, Shift for 1, Enter records or predicts.
- Gap = smallest angle between the student's arrow and the true direction (0 to 180). Hit when 8 or less.
- Drop: the fall uses y = g t^2 / 2 with g = 9.81 m/s^2 and h = 1.5 m, scaled by Slow motion. Motion off: the object
  stays in the hand, then appears on the ground at the landing time, with the trail drawn at once (timing kept).
- Changing place mid-Mark leaves that place unrecorded. Re-recording a recorded place is allowed (Mark on globe stays
  enabled); the record keeps the newest hit.
- Start over clears records, the argument card and tests; the Globe kids stay until Clear kids.
- Argue with 0 records: claims can be picked; Check claim stays disabled; hint "Record at least three places in Drop
  first. Tap Go to Drop."
- Swapping the claim or detaching evidence after "Fits" clears Fits and the test streak (Tests list keeps its rows,
  greyed, with "before you changed your claim").
- Test misses never end anything; the streak restarts. There is no limit and no score beyond the list.

## Look
Grade 3-5 light theme set by the tool: `--paper #f6f1e7`, `--ink #1f2430` (13.78:1), `--muted #5b6170` (5.5:1),
accent `--brand #b4400f` (plumb-bob copper; white on it 5.71:1, it on paper 5.07:1). Space stage `#0d1626`: plumb
lines and hits `#ffd166` (12.56:1), text `#e8eef7` (15.52:1), misses `#ff8a5c` (7.8:1) and always with the word
"Miss" and the degrees, never color alone. School pins and arrows carry name labels; arrow colors Anchorage
`#7cc8ff` (9.97:1), Quito `#9be08a` (11.57:1), Sydney `#f4a3ff` (9.94:1), Esperanza `#ffd166`. Neighbors: pocket-universe
nebula pink #ff8fd8, biome-atlas leaf green #5cbf2a; copper is not used by either.

## Art
- wwd-yard-anchorage: a school playground in Anchorage, Alaska in early autumn, snowy Chugach mountains behind, a
  low school building with a blank sign, flat gravel and grass across the lower third, clear daylight; 16:9; no
  cutout; people false; Drop yard.
- wwd-yard-quito: a school courtyard in Quito, Ecuador, green Andes slopes and Pichincha volcano behind, a painted
  school wall with a blank sign, flat paved courtyard across the lower third, bright high sun; 16:9; people false.
- wwd-yard-sydney: a school playground in Sydney, Australia, eucalyptus trees and a red-brick school with a blank sign,
  flat green field across the lower third, summer light; 16:9; people false.
- wwd-yard-esperanza: Esperanza Base in Antarctica, red and orange station buildings, Hope Bay ice and dark peaks
  behind, flat packed snow across the lower third, soft polar light; 16:9; people false.
- wwd-kid-jonah, wwd-kid-sofia, wwd-kid-ruby, wwd-kid-valentina: one grade 5 child each, full body, side-on, dressed
  for that place's weather (Valentina in a red parka), two poses each: arm out holding a ball shape at shoulder height,
  and looking down and pointing at the ground; 3:4; cutout yes; people true (Gemini, Cory's contact sheet, fresh-agent
  representation check). The held object is drawn by the tool over the hand.
- wwd-apple, wwd-ball, wwd-feather-tube (clear upright acrylic tube with a white feather inside, 9:16), wwd-bob (a
  brass plumb bob); 1:1 except the tube; cutout yes; people false.
- wwd-stars: a deep blue starfield with a faint Milky Way band; 16:9; people false; Globe and Argue background.
- wwd-ground-earth, wwd-ground-moon (gray dust and small craters), wwd-ground-mars (rusty rocks and dust); 4:1; Other
  worlds lanes.
- wwd-globe-moon, wwd-globe-mars: the whole Moon and the whole Mars seen from space, lit evenly; 1:1; cutout yes.
The Earth globe, plumb lines, arrows, pins and the right-angle mark are drawn in code: the globe must spin and go
see-through and the lines must be exact.

## Voice
Bank `upbeat-guide` ("Say brightly and clearly, like an upbeat tour guide"): a guide flying the class to four schools.
No grade 5 science neighbor uses it (living-pond gravel-ranger, pocket-universe casual-peer). `Curio.voice`,
`scope: () => state.mode`. Grade 5: welcomes, how lines, results; kid bubbles and place notes are read on screen.
| Key | Kind | When | Stale when | Whole | Repeat | Text |
|---|---|---|---|---|---|---|
| wDrop | how | Drop welcome | a drop has started | no | once | Welcome to Anchorage, Alaska. Pick something to drop, then tap Drop. |
| fellA | event | first landing at Anchorage | place changed | no | once per page load | It fell straight down, along the plumb line. |
| fellQ | event | first landing at Quito | place changed | no | once | Straight down again, just like in Alaska. |
| fellS | event | first landing at Sydney | place changed | no | once | Down under, it still falls straight down to the ground. |
| fellE | event | first landing at Esperanza | place changed | no | once | Even in Antarctica, straight down along the plumb line. |
| hMarkBtn | how | after first landing anywhere | Mark view open | no | once | Now tap Mark on globe. |
| hMark | how | Mark view opens | view closed | no | once | Drag the arrow the way the apple fell there, then tap Record. |
| recOk | event | a hit on Record | view closed | no | every hit | Recorded. Your arrow matches the plumb line. |
| recMiss | event | a miss on Record | arrow moved | no | every miss | Not quite. Here is the yard turned to sit on the globe. Line the arrow up with its plumb line. |
| hNext | how | after the first record, fewer than 4 | a drop started | no | once | Pick the next school, then tap Drop. |
| hZoom | how | fourth record | Globe open | no | once | All four schools are recorded. Tap Zoom out. |
| rv1, rv2, rv3 | event | reveal steps | mode left | yes | each reveal | Watch what happens when we make the arrows longer. / They all meet at one spot, the center of Earth. / So down is not one direction in space. Down is toward Earth's center, wherever you stand. |
| wGlobe | how | Globe welcome, no reveal pending | reveal playing | no | once | This is all of Earth. Drag to spin it, or tap the globe to stand a kid anywhere. |
| wArgue | how | Argue welcome | a claim is in the slot | no | once | Build your argument. Tap a claim, then tap at least three place cards. |
| hCheck | how | claim plus 3 places attached | checked | no | once | Tap Check claim to test it against your arrows. |
| fits | event | Check claim fits | claim changed | no | every time | Your claim fits every arrow. Now tap Test it. |
| noFit | event | Check claim fails | claim changed | no | every time | The dashed arrows miss your evidence. Try a claim that fits all of it. |
| hTest | how | first test place shown | Predict tapped | no | once | A new place. Drag the arrow to show which way down is there, then tap Predict. |
| hit | event | a test hit | Next place tapped | yes | every hit | Hit. Your claim predicted it. Tap Next place. |
| miss | event | a test miss | Next place tapped | yes | every miss | Missed. See where the plumb line really points. Tap Next place. |
| strong | event | third hit in a row | Next place tapped | yes | each time it happens | Three in a row. Your claim keeps predicting new places. That's a strong argument. |
| needWords | how | strong reached, reasoning under 8 words | box has 8 words | no | once | Finish your reasoning in the box to complete the card. |
| needRec | event | Argue with fewer than 3 records and a place card tapped | records reach 3 | no | once per entry | Record at least three places in Drop first. Tap Go to Drop. |
| wWorlds | how | Other worlds welcome | a drop started | no | once | Same apple, three worlds. Tap Drop all. |
| worlds | event | all three landed | Drop all tapped again | no | every time | The Moon's apple is slowest, but on every world it falls toward the center. |
No line names a disabled control: hMarkBtn needs `#mark`, hZoom `#zoom`, hCheck `#check`, the test results `#next`.

## Family engine
none

## Can it be beaten?
| Check | Way to pass without the skill | Why it fails |
|---|---|---|
| Record (Drop, Mark view) | Guessing an angle | 16 of 360 degrees pass: 4 percent per try. |
| | Doing nothing (arrow starts screen-down) | Off by 29 (Anchorage), 90, 124, 153 degrees: never a hit. |
| | Common wrong answer: down = bottom of the screen, or toward the South Pole | Screen-down as above; South Pole off by 14, 45, 62, 77. Toward the axis is right only at Quito, which is correct there. |
| | Answer on screen: kid's body, a center dot, live green arrow | Kid not drawn in Mark view; no center dot before the reveal; no live verdict, only on Record. |
| | Mashing Record | Passes after the first miss, because the miss shows the turned yard. Design choice: Record is a recording step with a scaffold, never used as proof; Strong rests on the Test row below. |
| Check claim | Elimination (4 claims, retry freely) | Gets the claim slot right, but only unlocks Test; Strong still needs 3 unaided hits in a row. Each failed claim shows its dashed arrows missing the evidence with degrees, so elimination is evidence-reading. |
| | Position, size or color of the right claim card | Order shuffled per load, all cards one size and color, texts 84 to 89 characters. |
| | A count only the right option has | B, C and D each miss at least 2 of any 3 attached places (D fits only Anchorage). |
| | Attaching any cards to reach 3 | Only place cards count; Feather tube and Other worlds draw no arrows. |
| Test (Predict, 3 hits in a row) | Guessing | 4 percent a try; 3 in a row 0.009 percent. |
| | Doing nothing (screen-down start) | Off by 30 or more at every pool place (Oslo 30, the rest more). |
| | Common wrong answers | Toward the South Pole: off 15 (Oslo) to 72; parallel to the axis: same as screen-down; horizontal toward the axis: within 8 only at Nairobi, so it cannot hit 3 in a row; straight out: 180. |
| | Elimination or retry on the same place | One try per place; the next place is new; the arrow resets to screen-down. |
| | Answer on screen | Test globe is opaque with no center dot, no old arrows, no kid; Strong is not shown until the third result. |
| | Copying the last arrow | Sides alternate and latitudes differ, so the last angle misses. |
| | Mashing Predict | Each Predict spends the place at whatever angle the arrow shows; mashing is doing nothing. |
| Reasoning box (8 words) | Typing filler | Not judged by the tool; it gates only the word "Strong". The teacher reads it; notes.md says so. |

## Heard in order
Grade 5, but these steps must be heard:
1. Reveal (Globe after Zoom out): the view turns (no line) -> rv1 (X-ray fades in while it plays) -> wait for rv1 ->
   Anchorage line stretches, then Quito, Sydney, Esperanza -> rv2 starts when the dot appears; wait -> rv3; wait ->
   the hint becomes "Drag to spin it, or tap Argue to build your argument." (not spoken). A tap finishes the picture at
   once and drops the rest of the sequence; rv2's text then stays on screen under the dot.
2. Test: Predict -> line draws and apple slides (1.5 s, no line) -> hit or miss (whole; plus strong right after on a
   third hit, whole) -> Next place enables when the last line ends (or at once with Sound off) -> next place shows ->
   hTest only on the first test.
3. Drop at a new school: fly (no line) -> Drop -> landing -> fellX -> hMarkBtn (first time only).
Feedback always plays before the next place or school appears.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Down is the direction toward the center of the spherical Earth (5-PS2-1 clarification) | nextgenscience.org 5-PS2-1 page | NYSSLS 5-PS2-1 (nyssls.info) and CA item specs | yes |
| A plumb line hangs along the direction of gravity | Britannica, "plumb line" | NOAA NGS geodetic glossary, "plumb line" | yes |
| Plumb-line down misses the exact center by at most about 0.2 degrees (Earth is slightly flattened and spins); the tool shows it as the center (notes.md says so) | Wikipedia "Latitude" (geodetic vs geocentric, max 11.5 arcminutes) | NOAA NGS, deflection of the vertical | yes |
| Earth mean radius 6,371 km | NASA Earth fact sheet (NSSDCA) | IUGG mean radius (Wikipedia "Earth radius") | yes |
| Surface gravity Earth 9.8, Moon 1.62, Mars 3.71 m/s^2 | NASA NSSDCA planetary fact sheets | Wikipedia "Moon", "Mars" | yes |
| Without air a feather and a heavy object fall together | NASA Apollo 15 hammer and feather (1971) | BBC Human Universe vacuum-chamber drop at NASA's Space Power Facility (2014) | yes |
| Esperanza Base has families and a school (Escuela Provincial No. 38) | Wikipedia "Esperanza Base" | Worldcrunch, "Antarctica 101: inside the only school on the frozen continent" | yes |
| Coordinates of the 4 schools' towns and 8 test places (to 0.1 degree) | GeoNames | Wikipedia infoboxes | yes |
Cut: "the only school in Antarctica" and "first person born in Antarctica" (true per sources but not needed; the
Villa Las Estrellas school closed, so "only" depends on the year).
Checks run (Python): edge-view arrows for all 4 schools and 8 pool places on both sides; every wrong rule's gap
(table above; nearest misses 14.4 at Anchorage and 15.1 at Oslo for the South Pole rule, above the 8 degree
tolerance); claims B to D against the 4 schools in 3D (B 14.4/45.1/61.9/76.7, C 28.8/90.2/123.9/153.4, D 0/180/180/180);
guess rate 16/360 = 4.4 percent, three in a row 0.0088 percent; fall times from 1.5 m: Earth 0.55 s, Mars 0.90 s,
Moon 1.36 s (x10: 5.5, 9.0, 13.6 s); contrast ratios in Look.

## Done when
1. Focus: in Drop the yard fills the stage and the falling object is the moving thing; in Mark and Test the globe and
   arrow are the biggest thing; at 1366x768 every mode's controls (including Record, Predict, Next place, Zoom out)
   are above the fold; at 680x425 the hint and main buttons stay visible.
2. A drop at each school falls along the plumb line with the right-angle mark; real 0.55 s, Slow motion 5.5 s.
3. Record with the arrow untouched is a miss at all four schools; a correct arrow (true angle in Content) hits.
4. After 4 records, Zoom out plays the reveal in order (rv1, lines, dot, rv2, rv3), and a tap mid-reveal finishes it
   at once with no line playing after.
5. Spinning the X-ray globe keeps every line meeting at the center dot; an added kid on the far side shows its line.
6. Check claim: A fits; B, C and D each show dashed arrows with the gaps listed in Sources.
7. Test: pressing Predict without turning the arrow misses at every pool place; aiming at the globe's center hits;
   Next place waits for the result line; 3 hits in a row with 8 words of reasoning turns the card Strong.
8. Tapping Drop during a fall restarts it at once; tapping Drop all during Other worlds restarts all three; Slow
   motion changes speed mid-fall.
9. Other worlds lands Earth 0.55 s, Mars 0.90 s, Moon 1.36 s (real time readouts at any speed).
10. Every how line is spoken once then hint only; recOk, recMiss, hit and miss speak every time; no line names a
    disabled control.
11. Standards map row: a student who only clicks without thinking cannot reach Strong; the card's evidence rows match
    the notebook.

## Open questions
- Sensitivity and people check: four child portraits from Alaska, Ecuador, Australia and an Argentine Antarctic base
  (rule 11 contact sheet and fresh-agent representation check). No hard history or Native content; Esperanza is named
  only as "an Argentine research base", with no claim about territory.
