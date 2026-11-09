# Roller Coaster Rounding

## One idea
The coaster track is the number line with its stations in the valleys at every ten (or hundred) and its hilltops at
every 5 (or 50), so a car let go anywhere rolls downhill to the nearest station, which is exactly rounding; a car on
the very top could go either way, so the park has a rule, and the rounded numbers then become the ride's quick check
on exact sums, differences and trains of cars.

## Not like
- jump-line (gr 2, same engine): draws your own jumps on an open line; here the line is a fixed track with a shape,
  and nothing is drawn by the student.
- fraction-trail (gr 3, same engine): a hiking trail split into fractions; no trail, campsite or hike scenery here.
- stadium-count (gr 4): rounding to any place for headlines while zooming crowds; here only 10 and 100, felt as
  downhill rolls, never zoom.
- rollercoaster-polynomials (gr 11, near in name): its track bends to fit polynomial zeros at a sunset park; ours is
  a fixed wave on a daytime lawn, with its own palette (teal, not orange) and art.
- road-trip-logbook (gr 4): column add and subtract on an odometer; here grade 3 within 1000 with ticket rolls,
  strips and singles that the student bundles and breaks by hand.
- pattern-painter (gr 3): estimates to check two-step word answers (3.OA.8); here the estimate is a shaded stretch on
  the track, and the student uses it to catch a clerk's slips.
- equal-groups-zoo (gr 3): equal groups as arrays of food; here each coaster car is one ten, so a train array shows
  6 x 4 tens = 24 tens.
- place-value-vault (gr 2): reads three-digit codes; here place value is a tool for adding and subtracting.

## Who and how
Grade 3 math. Students drive on laptops (solo by default); a teacher can project Track mode and have the class call
"left" or "right" before each Drop. 20 to 30 minutes. Standards 3.NBT.A.1, 3.NBT.A.2, 3.NBT.A.3. Nothing personal is
asked. `tool.json`: driver "students or teacher", modes ["Track", "Line", "Trains"].

## Standards map
| Code | Student action | What they see | Done when |
|---|---|---|---|
| 3.NBT.A.1 round to 10 or 100 | Set a number, guess a station, Drop; switch to the Hundreds track; in Line, tap the station each count rolls to | The car tilts on the slope, rolls to the lower or higher valley; two spans read "3 to 50, 7 to 40"; at 45 or 350 it teeters and the park rule sign shows | Drops at 44, 45, 47, 349, 350, 995 land at 40, 50, 50, 300, 400, 1000; a wrong station tap in Line is not accepted |
| 3.NBT.A.2 add and subtract within 1000 by place value | Type each column's count, bundle 10 singles into a strip or 10 strips into a roll, break a strip or roll when a column is short, then type each column's result | Ticket rolls (100), strips (10) and singles (1) in three columns; bundles fly left, breaks spill right | All 9 cards finish only with the right column entries and trades; Take away on a short column is refused with the reason |
| 3.NBT.A.2 (estimate as a check) | Round both counts, type the estimate, then judge the clerk's slips with Makes sense / Far off | The sensible stretch (one station each side of the estimate) shaded yellow on the result track; the exact car lands inside or outside | The two big slips are caught only with Far off; the sneaky slip shows inside the stretch and is then found in the columns |
| 3.NBT.A.3 one digit times a multiple of 10 | Set trains (1 to 9) and cars per train (1 to 9); in a card, type the tens, then the seats | An array of cars, each car plated "10"; the chain "6 x 4 tens = 24 tens = 240 seats" | 6 x 40, 9 x 80, 5 x 60 and the other cards accept only 24/240, 72/720, 30/300 and so on; 24, 2400 and 46 each get their own coaching |

## Screens and modes
Kit header: title, mode tabs `Track`, `Line`, `Trains`, then Motion, Sound, Read. Stage left (about 920 px at
1366x768), panel right (about 420 px) with the hint at the top and the keypad (0 to 9, `Back`, `Enter`) at the
bottom in every mode. At 680x425 stage and panel stay side by side, the keypad folds behind a `Keys` button, the
backdrop crops to a lawn strip, and the park board folds away; the focus and its controls stay above the fold at
every size in STANDARDS.md.

**On load (Track mode, Tens track, view 0 to 100).** The park backdrop, the track across the middle of the stage,
the car held by a red brake clamp at 47 (tilted on the slope toward 50). Station flags 40 and 50 glow as guess chips
under a small "Your guess?" label. Hint: "The car is held at 47. Tap Drop to see which way it rolls." The welcome is
queued for the first tap. First tap on `Drop`: the clamp opens and the car rolls (about 1.2 s) into 50. First tap on a
guess chip: it outlines that chip only. First tap on an arrow or key: moves the held car (the welcome may be cut,
BASELINE 16; its content is in the hint and Read).

**Park board** (panel, under the hint, page load only, never stored): `Rolls 0`, `Line 0 of 9`, `Trains 0 of 7`.
It counts; it never locks anything. Any card can be chosen from the card picker in any order.

### Track (explore)
Focus: the car and the two stations either side of it, centred, the track at least 55 percent of the stage width
and height band. Layout at 1366x768: track band y 260 to 560 of the stage; under it the readout chip; panel: the big
number (the car's value), `-10` `-1` `+1` `+10` (on Hundreds: `-100` `-10` `+10` `+100`, and `-1` `+1` stay), `Drop`
(big, brand), segmented `Tens track` / `Hundreds track`, `Back 100` / `Ahead 100` (Tens track only), `Tricky drop`,
the park board, the keypad. Typing a number 0 to 1000 and `Enter` moves the held car there (and pans the view).
- Dragging the car or tapping the track moves the held car (snap 1 on Tens, 10 on Hundreds; arrow keys step 1).
- `Drop`: the car rolls to its station. Outcomes, each different at a glance:
  1. Left of the hilltop: the car tilts left, rolls left, the left station's bell rings; spans "3 to 40" (short, teal)
     and "7 to 50" (long, grey) with the short one bold. Chip: "44 rolls to 40. 40 is nearer."
  2. Right of the hilltop: mirror of 1, rolling right.
  3. Exactly on a hilltop (45, 350): the car sits level on the peak and rocks twice (about 1 s); both spans are equal
     and dashed; the yellow `Park rule` sign pops up beside it: "On the top, it could go either way. Park rule: roll
     forward to the bigger number." Then it rolls right. Chip: "45 is halfway. The rule sends it to 50."
  4. Already in a valley (40, 0, 1000): the car does not move; the station flag flashes. Chip: "40 is a station.
     It stays."
- After every roll a ticket stub under the chip shows both tracks: "47: nearest ten 50, nearest hundred 0"
  (on Hundreds: "347: nearest ten 350, nearest hundred 300"). A strip of the last 6 drops sits under it.
- Guess chips: the two neighbour stations of the held car. After the roll: "You guessed 50. It rolled to 50." or
  "You guessed 40. It rolled to 50: 50 is nearer." Never scored.
- `Tricky drop` puts the car at the next number from the tricky list (Content) and switches track if needed.
- `Back 100` / `Ahead 100`: pan the Tens view by 100 (0 to 100 ... 900 to 1000), carrying the held car with the same
  ones and tens. Disabled at the ends.
- Tens to Hundreds: the line zooms out (0 to 1000, about 0.6 s) and the track reshapes to one hill per hundred; the
  held car keeps its number.

### Line (the morning queue)
Focus: the ticket bin in the stage centre (three columns, Hundreds, Tens, Ones, at least 520 x 300 px), with the card
strip across the top of the stage (time, story, the two counts) and the result track (130 px) under it. Panel: hint,
the current step's buttons, card picker `Card 1` to `Card 9` plus `Clerk 1` to `Clerk 4` and `More riders`, keypad.
Steps of a card (each step names its control in the hint):
1. **Round.** Two mini cars sit on the result track at the two counts (track set to the card's place). Tap the
   station each one rolls to (station flags are buttons). Right: the car rolls there. Wrong: the car rolls the
   other way to the right station and the hint says "It rolled to 300. Tap 300." The step needs the right tap.
2. **Estimate.** Type the estimate of the rounded numbers and `Enter`. Right: an amber estimate flag stands on the
   track. Wrong: "Add the two stations: 300 and 300." and the student types again.
3. **Exact, by place.** The ticket bin.
   - Adding: both counts are in the bin as two rows. Ones first: "8 ones and 6 ones. How many ones? Type it, then
     Enter." Right: the rows slide together. With 10 or more, `Next column` refuses ("14 ones won't fit in one place.
     Tap the ones pile to bundle ten into a strip.") until the student taps the pile (or `Bundle 10`): ten singles
     snap into a strip and fly to the Tens column, marked as the carried one. Then tens (bundle into a roll if 10 or
     more), then hundreds.
   - Subtracting: only the first count is in the bin; a chip says "Take away 278". Each column: the student taps
     `Take away` or breaks a bigger piece. `Take away` on a short column: "Only 6 ones. Tap a strip to break it into
     10 ones." Tapping a strip (or roll) spills it into the column to its right. An empty tens column with ones short:
     "No strips here. Tap a roll to break it into 10 strips." After a legal `Take away`, the student types how many
     are left in that column and `Enter`.
   - A wrong column entry: "Not quite. Count the ones again." A second miss numbers the pieces 1, 2, 3... on screen.
4. **Ride check.** The exact answer's car drops onto the result track. The sensible stretch (yellow, one station each
   side of the estimate, labelled "Sensible stretch: 500 to 700") is shaded. Inside: the gate light turns green, chip
   "624 is 24 from the estimate 600. The numbers check." and the ride runs its lap (Content, Lap).

**Clerk cards** (the booth): the booth's board shows the clerk's sum, for example "278 + 346 = 514", and the place to
round to. Steps 1 and 2 as above, then the clerk's answer drops onto the track and the student taps `Makes sense` or
`Far off`. Far outside the stretch, `Far off` is right ("Good catch. 514 is far from 630."); `Makes sense` gets "Look
where it landed: outside the stretch." Inside the stretch, `Makes sense` is right, and then the sneaky card says "It
could be right. An estimate catches big slips, not small ones. Check the clerk's columns." and opens the bin with the
clerk's column entries filled in; the student taps the wrong column, then types the fix.

**More riders** makes a new card (Content, generator) after the nine.

### Trains (explore, then cards)
Focus: the train array in the stage centre: each row one train at the station, each car the painted coaster car
with a "10" plate, lead car first. Panel: `Trains` stepper (`-` `+`, 1 to 9), `Cars per train` stepper (1 to 9),
the chain readout, card picker `Train 1` to `Train 7` plus `More trains`, keypad.
- Explore (no card): changing a stepper adds or removes a train or car at once (cars roll in, about 0.3 s). The chain
  shows live: "6 trains x 4 tens = 24 tens = 240 seats". Every tenth car gets a thin bracket "100 seats" so ten cars
  make a hundred.
- A card fixes the steppers to its numbers and hides the chain's numbers: "6 trains of 40 seats. How many seats?"
  Step 1: "Count the cars. Each car is a ten. Type how many tens, then Enter." Step 2: "Now type the seats." Right:
  the chain fills in and the ride runs its lap. Coaching (Content) answers the common wrong answers.
- Train cards 6 and 7 tie to Line card 1: "Will 7 trains of 40 carry the 278 riders?" (280, yes, 2 seats spare) and the
  same for 6 trains (240, no, 38 still waiting): the student taps `Enough` or `Not enough` after typing the seats.

**Lap** (Line card or Train card done): a 4 s run of the riders car along the visible track, then the gate sign
"Open". Every control stays live: a tap during the lap ends it at once and acts. Motion off: the riders car shows
still at the station with the sign for the same 4 s, and taps still act at once.

## Content
- Park: Hilltop Park, the ride "the Hilltopper". Fictional; no real park or ride is named or claimed.
- Tracks: Tens track, valleys at multiples of 10, hilltops at every 5, view 100 wide (ten windows); Hundreds track,
  valleys at multiples of 100, hilltops at every 50, view 0 to 1000, ticks every 10, labels every 100. Range 0 to
  1000 inclusive. Track height h(v) = (1 - cos(2 pi v / p)) / 2 times the band height, p = 10 or 100; the car tilts to
  the slope and rolls downhill; the station brakes catch it in the valley (said in Read: "Station brakes stop the car
  in the valley").
- Tricky drop list, in order: 45, 44, 349, 350, 5, 995, 250, 651, 0, 1000.
- Line cards (place, counts, estimate, exact): 1 9:00 "278 riders in the morning line, 346 at noon. How many in all?"
  hundreds, 300 + 300 = 600, 624. 2 10:00 "152 + 239" tens, 150 + 240 = 390, 391. 3 11:00 "346 riders were in line;
  278 have ridden. How many still wait?" tens, 350 - 280 = 70, 68 (break a strip, then a roll). 4 12:00 "503 tickets
  in the bin; 268 used" tens, 500 - 270 = 230, 235 (break a roll first, then a strip). 5 1:00 "467 + 285" hundreds,
  500 + 300 = 800, 752. 6 2:00 "395 + 407" tens, 400 + 410 = 810, 802 (395 is halfway: rule). 7 3:00 "720 seats; 456
  filled" hundreds, 700 - 500 = 200, 264. 8 4:00 "649 + 251" hundreds, 600 + 300 = 900, 900. 9 5:00 "1000 tickets
  printed; 375 sold" tens, 1000 - 380 = 620, 625 (375 halfway; the bin starts with 10 rolls).
- Clerk cards: 1 "278 + 346 = 514", tens: 280 + 350 = 630, stretch 620 to 640, outside, Far off (forgot both
  carries). 2 "503 - 268 = 365", hundreds: 500 - 300 = 200, stretch 100 to 300, outside, Far off (took the smaller
  digit from the bigger). 3 "467 + 285 = 752", hundreds: 800, stretch 700 to 900, inside, Makes sense, and it is right
  ("The columns agree."). 4 sneaky "152 + 239 = 381", tens: 390, stretch 380 to 400, inside, Makes sense; the clerk's
  tens column reads 8 (forgot the carried strip); the fix is 391.
- Generator (More riders): add: a and b from 100 to 899, a + b at most 1000; subtract: 100 to 1000, a > b; place
  alternates tens, hundreds; at least one regroup in two of every three cards. Always inside the stretch (checked).
- Train cards (trains x seats, tens, seats): 1 6 x 40, 24, 240. 2 3 x 70, 21, 210. 3 9 x 80, 72, 720. 4 5 x 60, 30, 300.
  5 8 x 20, 16, 160. 6 7 x 40 for 278 riders: 280, Enough, 2 spare. 7 6 x 40 for 278: 240, Not enough, 38 wait.
  More trains: 2 to 9 trains by 2 to 9 cars.
- Train coaching: tens answer typed as seats (24): "That's the cars. Each car is ten seats: 24 tens is how many?";
  extra zero (2400): "Too big. 24 tens is 2 hundreds and 4 tens."; added (46): "That adds them. 6 equal trains is 6
  times."; other: "Count the cars in one train, then the trains."

## Interactions in detail
- One car in Track. Setting a value while a roll plays cancels the roll and holds the car at the new value at once.
  `Drop` during a roll restarts from the held value. Mode switch, card change or `Tens/Hundreds` hush the voice and end
  any roll or lap.
- Extremes: 0 and 1000 are valleys (stay). 995 on Tens is a hilltop, rolls to 1000. 950 on Hundreds rolls to 1000.
  `-1` at 0 and `+1` at 1000 are disabled; typed values over 1000 show "The track ends at 1000." and keep the old value.
- Keypad accepts up to 4 digits; `Back` deletes; `Enter` with nothing typed does nothing.
- Line: a step's buttons not yet in use are hidden, not disabled. Bundling with fewer than 10 is refused: "Bundles need
  ten." Breaking a piece when the column already has enough is allowed (it is still correct place value) and the
  hint notes "You didn't need to break that one."
- Trains: steppers at 1 and 9 disable their `-` / `+`. At 9 x 9 (81 cars) every car still shows in the array.
- Reset: each mode has `Start over` in its panel (Track: car to 47, Tens; Line: current card from step 1; Trains: 6 x 4).
  The park board resets only on reload.

## Look
Daytime fair, distinct from rollercoaster-polynomials' sunset orange and two-trains' maroon. `:root`: `--paper
#fbf6ec`, `--ink #1e2430` (14.44:1), `--muted #566072` (5.89:1), `--brand #0d6f7a` teal (5.46:1 on paper; white on it
5.88:1), `--btn #0a5a63` (white 7.91:1), `--focus #c2410c` (4.81:1). Track rail candy red `#a3262f` with a dark
outline over the lawn (4.09:1) and sky (5.78:1); sensible stretch `#ffd75e` with ink labels (11.21:1); estimate flag
amber, exact car teal; chips white with ink (15.55:1). Spans also differ by dash and weight, never only colour.

## Art
- park-backdrop: a sunny small-town amusement park seen from a grassy hill, striped tents, a carousel roof and pennant
  strings far off, soft summer clouds, an open green lawn filling the lower half, storybook painting; 16:9; no cutout;
  people false; behind every mode, cropped per size.
- coaster-car: a single teal roller coaster car in side view facing right, two rows of empty padded seats, lap bars,
  red wheels, a blank round plate on its side; 4:3; cutout; people false; Track car (rotated to the slope) and every
  Trains car (plate text in code).
- coaster-lead-car: the same teal car with a rounded nose and a headlamp, blank round plate; 4:3; cutout; people false;
  first car of each train.
- coaster-car-riders: the same teal car full of smiling riders of many ages and backgrounds with arms raised; 4:3;
  cutout; people true (Gemini, on Cory's contact sheet); the lap only.
- station-platform: a small wooden loading platform with a striped roof and a blank sign board; 4:1; cutout; people
  false; at every valley, the station number in code on the sign; all of it shows above the lawn at every size.
- ticket-single: one orange admission ticket with a punched hole and a blank face; 16:9; cutout; people false; ones,
  and ten in a row joined by a code perforation line make a strip (never a painted strip: the count must be exact).
- ticket-roll: a fat roll of orange tickets on a spindle, blank faces; 1:1; cutout; people false; a hundred, "100" in code.
- ticket-booth: a striped red and white ticket booth with a blank chalkboard on its front; 3:4; cutout; people false;
  the clerk cards, sum written in code on the board.
Track, number line, ticks, spans, stretch, flags, clamp, park rule sign, chips and arrays are drawn in code.

## Voice
Bank `upbeat-guide` (Zephyr), style "Say brightly and clearly, like an upbeat tour guide", here the park's ride
guide. No neighbour uses it (corner-store friendly-dad, marching-band firm-captain, rollercoaster-polynomials
hs-narrator). `Curio.voice`, scope = mode + card. Lines carry no numbers so all are recordable; numbers live on
screen and Read speaks the card and hint (browser voice for templated text).
- wTrack (how, welcome): "Welcome to Hilltop Park! Every station sits in a valley. Tap Drop and watch which way the
  car rolls." Stale after the first Drop.
- setNext (how, after the first roll): "Set a new number with the arrows or the keypad, then tap Drop."
- rollLeft / rollRight (event, first two times each per load, then chime only): "Downhill to the left. The lower
  station is nearer." / "Downhill to the right. The higher station is nearer."
- peak (event, whole, first two times per load, then the sign only): "Right on the top! It could go either way, so
  the park rule sends it forward to the bigger number."
- stays (event, once per load): "Already at a station. It stays put."
- hundreds (how): "Now one hill for every hundred. Find where the hilltop is." Stale on leaving Hundreds.
- wLine (how, welcome): "Riders are lining up! Round the counts for a quick estimate, then work it out exactly with
  tickets." Stale once step 1 is done.
- round (how): "Tap the station each count rolls to." estimate (how): "Add the two stations. Type it, then tap Enter."
- cols (how): "Start with the ones. Type how many, then tap Enter." bundle (how): "Too many for one place. Tap the
  pile to bundle ten." break (how): "Not enough to take away. Tap a bigger piece to break it."
- check (event, whole; the lap waits for it): "Inside the sensible stretch. The numbers check. The ride is open!"
- clerk (how): "Does the clerk's answer make sense? Tap Makes sense or Far off." caught (event): "Good catch! That's far
  from the estimate." sneaky (event, whole): "It could be right. An estimate catches big slips, not small ones. Tap
  the column that slipped."
- wTrains (how, welcome): "Each car holds ten riders. Add trains and cars, and watch the seats count by tens."
- tens (how): "Count the cars. Each car is a ten. Type how many tens, then tap Enter." seats (how): "Now type the seats."
- trainsDone (event): "Ten tens make a hundred. All aboard!" again (event, at most twice per card, then hint only):
  "Not quite. Count again."
A coaching line names only controls shown at that moment (the hidden-step rule above keeps `Next column` out of
lines until it shows).

## Family engine
number-line (`kit/number-line.js`). This is the family's first build: write the engine to docs/families/number-line.md
and correct that file's table row in the same change ("stations in the valleys at the tens and hundreds; the car
rolls to the nearer station; 45 rolls up by the park rule"). Uses: `NumberLine` (0 to 100 windows and 0 to 1000,
ticks every 10 and 1 or every 100 and 10), `nl.x` to place the tool's own track curve, car, clamp, platforms and
flags, `nl.span` (distance spans, sensible stretch), `nl.mark` (estimate flag, guess outlines), `nl.zoom` (pans and the
Tens/Hundreds switch), `nl.draggable` on an invisible pin under the car, `nl.on('tap')`. The track curve, car and
tickets are this tool's own SVG; the engine draws no scenery.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| 3.NBT.A.1 to A.3 wording (round to 10 or 100; add and subtract within 1000 by place value; one digit times multiples of 10 in 10 to 90, e.g. 9 x 80, 5 x 60) | thecorestandards.org/Math/Content/3/NBT/ | Utah Core Guide, Grade 3 Number and Operations in Base Ten (schools.utah.gov) | yes |
| Halfway numbers round up by convention (45 to 50); it is a rule people chose, not a fact of the line | Illustrative Mathematics Grade 3, Unit 3, Lesson 15 (im.kendallhunt.com) | ClassWeekly teaching wiki, "Rounding" (classweekly.com) | yes |
| Rounding by nearest benchmark and the midpoint (478: 470, 480, midpoint 475) | Utah Core Guide (above) | Illustrative Mathematics Grade 3, Unit 3, Lesson 15 | yes |
No real-world claims about parks, rides or seats: Hilltop Park and its trains are labelled made up in notes.md. Cut:
any claim about real coaster capacity.

Checks run (`S:/CurioClass-codex-scratch/specs/roller-coaster-rounding/check.py`):
- The track model (downhill on h(v), forward on the peak) equals round half up for every whole number 0 to 1000, on
  both tracks: OK. Examples 44, 45, 47, 349, 350, 995 give 40, 50, 50, 300, 400, 1000.
- The sensible stretch holds for every pair within 1000: worst add gap 10 and 100, worst subtract gap 9 and 99, so
  "one station each side" always contains the exact answer; generated cards can never fail it.
- All 9 Line cards: estimates, exact answers and column work (carries 14/12, 11/9, 12/15, 12/10, 10/10; trades for
  cards 3, 4, 7, 9) as listed in Content.
- Clerk slips through the wrong behaviours: 514 and 365 fall outside (Far off right; Makes sense refused); 752 and the
  sneaky 381 fall inside; 381 is only caught by the column step, which the card makes the student do. Tapping Makes
  sense on every slip fails cards 1 and 2. 503 - 268 smaller-from-bigger digits give 3, 6, 5 = 365.
- Train cards and their wrong answers (24, 2400, 46; 21, 2100, 73; 72, 7200, 89; 30, 3000, 65; 16, 1600, 28; 28,
  2800, 47) differ from every right answer; 7 x 40 = 280 is 2 over 278, 6 x 40 = 240 is 38 short.
- Contrast ratios as in Look.

## Done when
1. Focus: in each mode the car, the ticket bin or the train array is the largest thing, centred, and at 1366x768 it
   and every control the step needs (Drop, steppers, the step's buttons, keypad) show without scrolling; at 680x425
   the keypad sits behind `Keys` and nothing else needed is lost.
2. First tap on `Drop` rolls the car from 47 to 50 within a second, with the chip and both spans.
3. Rounding row: 44, 45, 47, 349, 350, 995, 0, 1000 land where Sources says; 45 and 350 teeter and show the park rule;
   the four outcomes look different at a glance.
4. Addition and subtraction rows: all 9 cards finish only through right column entries, bundles and breaks; Take away on
   a short column and Next column with 10 or more are refused with the reason.
5. Estimate row: clerk cards 1 and 2 need Far off; card 3 Makes sense; the sneaky card leads into the column fix 391.
6. Multiplication row: every Train card accepts only its tens and seats and answers 24, 2400 and 46 with their lines.
7. A tap during a roll or a lap acts at once (new value, new card or mode) and the lap ends.
8. Voice: rollLeft and rollRight speak twice each in ten drops, then chime only; no line names a hidden control; the
   check line finishes before the lap.
9. Motion off: no roll or lap movement, results and the still lap frame keep their timing.
10. No score, timer or lock anywhere; the park board only counts, resets on reload, stores nothing.

## Open questions
None for Cory. Sensitivity review: not needed (no cultural or hard-history content); the riders image goes on the
people contact sheet (BASELINE 11).
