# Skate Park Angles

## One idea
Dev's spin is the angle: drag his board around the turn dial and the arc it sweeps is the angle, so a 180 is half
the circle, a degree is one of 360 slices, two spins stack into one bigger arc, and the same turn shows up again when
you lay a protractor on a ramp; then Dev's crew jumps, and you plot their heights in eighths of a foot.

## Not like
- quilt-block-studio (gr 4, studio, concept): names and draws lines, rays and angle types (acute, right, obtuse) and symmetry (4.G.A). Here angles get a number: measured in degrees, built to a size, added and subtracted. No naming of angle types, no symmetry.
- seed-sprout-data (gr 5, lab, concept): line plot of plant heights to 1/8 inch with grade 5 operations (sharing out equally, unlike units). Here grade 4: feet in eighths, like-denominator addition and subtraction only, read off a measuring pole.
- graph-glow-up (gr 3, builder, concept): picture and bar graph scales, line plot to the quarter inch. Here eighths, and the plot answers fraction questions.
- ramp-and-roof (gr 10, builder, spec): slope as a ratio, trig. Here the ramp is only an angle measured with a protractor; no ratios, no rise and run.
- half-pipe-energy (gr 8, science simulator, concept): a skater on a ramp for kinetic and potential energy. Here no energy; the skater is the turn and the jump data.
- skateboard-fund-chances (gr 4, social studies cards): same skateboard theme, money and chance. No shared mechanic; different palette and art (no shared images).
- roller-coaster-rounding (gr 3, simulator, spec): the ride is a number line. Here the ride is a circle.

## Who and how
Grade 4 math, module math-4-angles-and-line-plots. Driver: students (solo by default) or teacher on a projector.
20 to 40 minutes (one sitting per mode works). Standards: 4.MD.B (4.MD.4) and 4.MD.C (4.MD.5a, 4.MD.5b, 4.MD.6,
4.MD.7). No personal prompts. The crew (Dev, Rae, Mina, Walt) and their jumps are made up, and the tool says so on
the Jump Log card ("Dev's crew and their jumps are made up for practice.").
Role: lesson. Change note (spec fix, 2026-11-10; the tool is built, so the code follows this spec later): five Spin
jobs were added (7 to 11) and nothing was taken away. Jobs 7 and 8 bring 4.MD.5a to five kinds of item (sixths,
twelfths, and degrees back to fourths and eighths). Jobs 9 and 10 make the student answer on 4.MD.5b, which before
was only a readout. Job 11 has the student write the angle equation, which before was always given. The park counter
goes from 14 to 19. Not added: choosing the line plot's scale (4.MD.4, a small part; the axis stays given so the
session fits one sitting).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.MD.5a | Drag the board around the dial; do Spin jobs 1 to 3, 7 and 8 (fraction of a turn to degrees and degrees to a fraction, in fourths, eighths, thirds, sixths and twelfths; five kinds of item) | the swept arc as a colored wedge; readout "135 degrees, 135/360 of a full turn" and, at landmarks, "= 3/8 turn"; job wedges cut into equal slices | Spin job 2 (3/8 of a turn) accepts 135 only; 37 or 38 gets the "a full turn is 360" reason |
| 4.MD.5b | Step the dial with the arrow keys one degree at a time; Spin jobs 9 and 10: count the one-degree slices in a wedge and type its degrees, then say how many one-degree turns fill a given angle and a full turn | the readout's first line counts one-degree turns ("1 degree: 1 one-degree turn, 1/360 of a full turn"); in jobs 9 and 10 a wedge cut into one-degree slices with no number on it | arrow keys move exactly 1 degree and the line updates each press; Spin job 9 with 12 slices accepts 12 only; job 10 needs 37 and 360 |
| 4.MD.6 (measure) | Ramp jobs 1 to 3: place the protractor on a ramp, pick the right scale, type the angle | a real two-scale protractor (0 to 180 both ways) over a code-drawn ramp; no angle number anywhere | a ramp of 20 accepts 19 to 21; 160 (the other scale) fails with the scale reason and the next try is a new ramp |
| 4.MD.6 (sketch) | Ramp jobs 4 and 5: drag the ramp's lip handle to a given angle, check it with the protractor | the ramp bends as you drag; no readout in Jobs | a kicker built to 25 passes at 24 to 26 only; a miss never says the angle you made |
| 4.MD.7 | Stack spins in Explore; Spin jobs 4 to 6 (total, missing part, three parts) written as equations; Spin job 11, where the student writes the equation with a ? and then solves it; Ramp job 3 (straight line split in two); five kinds of item | wedges in two colors with their own labels; the equation strip "90 + 45 = ?" and "125 + ? = 180" with no ticks on the dial | Spin job 5 accepts 55 only; 305 gets the "you added" reason |
| 4.MD.4 | Jump Log: read each jump on the pole, tap the line plot to place its dot; answer three fraction questions per session | a pole marked in eighths (labels only at 0, 1/2, 1, 1 1/2); a line plot 0 to 1 1/2 ft with all 13 eighth ticks | the Low session's three answers are 3/8, 2 and 1/8 (equivalents accepted); a dot on the wrong tick is refused |

## Screens and modes
Header: title, mode buttons **Park**, **Spin Deck**, **Ramp Shop**, **Jump Log**, then kit Motion, Sound, Read.
Each workshop has a two-way switch **Explore / Jobs** at the top of its panel (Explore is the default). A job shows
one card at a time, with **Check**, a job pager (dots 1 to 6, tap any) and **Rae's tip** after a miss.

On load: Spin Deck, Explore. Dev's board sits on the dial pointing at 0 (up, toward the drop-in gate), the wedge is
empty, the hint reads "Drag Dev's board around the dial, then tap Go." Nothing plays before the first tap. The first
tap on the board starts the drag (the main path); the first tap on Go with a 0 spin plays Dev's "ready" nod and the
hint stays. The welcome (wSpin) queues after the first tap that has no line of its own and may be cut (rule 16); its
content is the hint.

**Spin Deck.** Focus: the dial, a circle 520 px across at 1366x768, centered in the stage, with Dev's side-view
cutout at its lower right (200 px tall) who performs the spin on Go. Top-down painted board (board-top) lies across
the dial's center; its nose is the arrow. Explore: drag the nose (or arrow keys: 1 degree; Shift: 10); whole degrees
only; the wedge fills from 0 clockwise; past 360 a lap ring appears and the readout says "1 full turn + 180 = 540".
Readout panel under the dial (always above the fold): line 1 "135 degrees", line 2 "135 one-degree turns", line 3
"135/360 of a full turn", line 4 at landmarks only "= 3/8 turn" (landmarks in Content). Buttons: **Go** (Dev spins
that much over about 1.5 s per full turn; at 360 or more the trick name shows, see Content), **Add a spin** (freezes
the current wedge in violet with its label and starts a second wedge in orange from where the first ended; up to
three spins; the equation strip shows "90 + 45 = 135"), **Clear**, **Save as Dev's trick** (the total becomes the
spin Dev does in Park's Ride). Jobs: the dial shows the job's wedges cut into equal slices or labeled parts, with no
ticks and no readout; the card holds the equation strip with a box for the unknown, an on-screen keypad (0 to 9,
fraction bar, mixed-number space, delete) and Check. After a right answer Dev spins the answer and the readout
appears. Leaving Jobs (to Explore or another mode) re-rolls the open job to another variant.

**Ramp Shop.** Focus: a side view of one ramp (code-drawn, plywood texture) on the painted ground strip, ramp arm
380 px long, with the protractor (radius 180 px, so the ramp edge always crosses the scale). Explore: drag the ramp's
lip handle (5 to 60 degrees, whole degrees; arrow keys 1 degree), flip direction with **Flip ramp**, drag the
protractor anywhere and turn it by its rotate knob; within 24 px of the ramp's corner and 10 degrees of the ground it
snaps (center on the corner, baseline on the ground). **Show angle** (off by default) puts the number in a sign over
the ramp. **Test ride**: Dev rolls off the ramp; air height follows the bands in Content; over 35 he bails (bail pose,
helmet on, laughing) and Rae's line plays. **Put in park** sends this ramp to Park's open slot. Jobs: Show angle is
removed; measure jobs give a fixed ramp and a number box; sketch jobs give a target and a ramp that starts at least 10
degrees away from it.

**Jump Log.** Focus: the line plot across the bottom half of the stage (1100 px wide at 1366x768, 13 ticks 80 px
apart), with the jump scene above it: the painted ramp-side view, the measuring pole at right, the skater's air
cutout frozen at the peak and a dashed line from the board's wheels to the pole. Panel: session buttons **Low
kicker**, **Mid kicker**, **Big kicker**, jump count "Jump 3 of 10", then Questions once all dots are placed.
Each jump: the skater rolls in and jumps (1.2 s, Motion off shows the peak at once), freezes; the student taps a
tick; right: the dot drops onto its stack; wrong: the dot shakes off and "Count the eighths up from the last label on
the pole" shows; second miss: Rae places it (outlined dot, "Rae placed"). **Next jump** is not needed: the next jump
starts 0.6 s after the dot lands, and any tap on the plot during the jump is ignored until the freeze (the tick
highlight shows it is waiting). Questions (three per session, Content) use the same keypad. In Big kicker, **Show Low
kicker too** adds the Low session's fixed dots (whether or not Low was played) as faded rings on the same axis (needed for question B3). Explore here is the plot
itself: after a session, tapping a dot shows which skater and jump it was.

**Park.** Focus: the painted park panorama (16:9) filling the stage, with five ramp slots, six prop spots and a
blank scoreboard. Each finished job adds its piece (Content). Counter in the panel: "Park pieces 3 of 19 (2 on your
own)". **Ride** plays Dev's run left to right, about 12 s: he airs every ramp in its slot (bands in Content) and
does his saved trick (default 180) off the last ramp; any tap on Ride restarts at once, **Stop** ends it, a mode
switch stops it.

What the picture shows for every outcome (Ride and Test ride): ramp 5 to 14 degrees: small hop, board stays level,
low dotted arc; 15 to 24: middle arc, knees tucked (dev-air); 25 to 35: high arc and the saved spin drawn as a wedge
above him; over 35: Dev stops at the lip, bail pose beside the ramp, run ends with "Bailed" on the scoreboard. A
spin of 360 or more draws the lap ring above him.

1366x768: header 52 px; stage left about 900 px, panel right about 440 px; the focus, Explore/Jobs switch, job card,
keypad and Check all sit above the fold. 680x425: stage and panel stay side by side; panel 250 px with a 4-row keypad
of 44 px keys, the job pager becomes "Job 2 of 6" with arrows, Dev's side cutout in Spin Deck hides (the board on
the dial still spins), the Jump Log scene shrinks to 120 px tall above the plot.

## Content
Landmarks (readout line 4): 0, 30 (1/12), 45 (1/8), 60 (1/6), 90 (1/4), 120 (1/3), 135 (3/8), 150 (5/12), 180 (1/2),
210 (7/12), 225 (5/8), 240 (2/3), 270 (3/4), 300 (5/6), 315 (7/8), 330 (11/12), 360 (1 full turn).

Trick names on Go (total): 180 "a one-eighty, half a turn"; 360 "a three-sixty, a full turn"; 540 "a five-forty,
one and a half turns"; 720 "a seven-twenty, two turns"; 900 "a nine hundred, two and a half turns. Tony Hawk landed
the first one at the 1999 X Games." Dial maximum 900.

Spin jobs (each has three variants; one shows, a miss keeps it, leaving Jobs re-rolls):
1. Fraction to degrees: "Dev turns 1/4 of a full turn. How many degrees?" (1/4 = 90, 1/2 = 180, 3/4 = 270). Wedge cut into 4 equal slices.
2. Eighths: 3/8 = 135, 5/8 = 225, 1/8 = 45. Wedge cut into 8 slices.
3. Degrees to a fraction: "A 120 degree spin is what fraction of a full turn?" (120 = 1/3, 60 = 1/6, 240 = 2/3; any equal fraction accepted, such as 2/6 or 120/360).
4. Total: "90 + 45 = ?" (135); "180 + 90 = ?" (270); "45 + 30 = ?" (75). Two labeled wedges.
5. Missing part: "Dev needs a 180 to face the exit. His first part was 125. 125 + ? = 180" (55); "70 + ? = 180" (110); "200 + ? = 360" (160).
6. Three parts: "150 + 90 + ? = 360" (120); "100 + 150 + ? = 360" (110); "60 + 70 + ? = 180" (50).
7. Sixths and twelfths: "Dev turns 1/6 of a full turn. How many degrees?" (1/6 = 60, 5/6 = 300, 1/12 = 30). Wedge cut into 6 or 12 equal slices.
8. Degrees to a fraction, fourths and eighths: "A 270 degree spin is what fraction of a full turn?" (270 = 3/4, 225 = 5/8, 315 = 7/8; any equal fraction accepted).
9. One-degree slices: the wedge is drawn cut into thin one-degree slices, drawn large (the dial zooms so each slice is at least 14 px wide at the rim), with no label. "Each slice is a one-degree turn. How many degrees is this angle?" (12, 7, 15). Then a second box on the same card: "So 50 one-degree turns make an angle of how many degrees?" (50; variants 90, 200).
10. Turns in an angle: "This wedge measures 37 degrees. How many one-degree turns fill it?" (37; variants 112, 8). Second box: "How many one-degree turns fill a full turn?" (360). After both are right the card shows "So one one-degree turn is 1/360 of a full turn."
11. Write the equation: "Dev wants a 270. He has turned 115. Write an equation with ? for the part left. Then solve it." The strip is empty and the keypad gains +, -, = and ? keys for this job. Accepted equations: 115 + ? = 270, ? + 115 = 270, 270 - 115 = ? and 270 - ? = 115. Answer 155. Variants: turned 90 of a 225 (135); turned 240 of a 360 (120). The equation is checked first, then the answer box opens.

Ramp jobs (measure jobs: a miss loads the next variant; sketch jobs keep the target):
1. Measure, ramp opening right: 20, 35, 48.
2. Measure, ramp opening left: 25, 40, 15.
3. Straight line: a bank of 30 (variants 40, 25) is shown with its angle labeled; "Measure the angle behind it, between the deck and the ramp" (150, 140, 155); the card then shows "30 + 150 = 180: a straight line is a half turn."
4. Sketch a kicker opening right: 15, 25, 30.
5. Sketch a bank opening left: 20, 35, 40.
Tolerance: measure answers within 1 degree; sketch within 1 degree of the target.

Jump Log sessions (heights in eighths of a foot; order shuffled each visit; skaters rotate Dev, Mina, Walt, Rae):
- Low kicker (15 degrees), 10 jumps: 2, 3, 3, 4, 4, 4, 5, 3, 4, 2. Questions: L1 "How much higher was the highest jump than the lowest?" 3/8. L2 "Add up all the 4/8 ft jumps. How many feet is that?" 2. L3 "How much higher was the highest jump than the most common height?" 1/8.
- Mid kicker (25 degrees), 12 jumps: 4, 5, 6, 6, 6, 7, 8, 5, 6, 7, 9, 6. M1 highest minus lowest 5/8. M2 "Add up all the 6/8 ft jumps" 3 6/8 (= 3 3/4). M3 "Add the two lowest jumps" 9/8 (= 1 1/8).
- Big kicker (35 degrees), 12 jumps: 6, 7, 8, 9, 9, 10, 11, 9, 12, 8, 9, 10. B1 highest minus lowest 6/8 (= 3/4). B2 "Add up all the 9/8 ft jumps" 36/8 (= 4 1/2). B3 "How much higher was Big's highest jump than Low's highest?" 7/8.
Axis and question wording use eighths so every sum is like denominators (4.NF.3); answers in any equal form count.
The pole and axis run 0 to 12/8. Card line: "Same speed, steeper kicker: the jumps get higher. These jumps are made up."

Spin jobs 7 to 11 each add a line to the scoreboard's trick list ("Sixth turns", "Spins as fractions", "One-degree
turns", "Turns in an angle", "Dev's own equation"); they add no new props.

Park pieces (19): Spin jobs 1 to 6 add, in order, a rail, a bench, a light pole, a planter, a bike rack, a shade tree (painted
props on their spots). Ramp jobs 1 to 5 add their ramp at its angle in slots 1 to 5 (Explore's Put in park uses
slot 5 until job 5 is done, then a sixth slot). Each Jump Log session adds a line on the scoreboard ("Low kicker: 10
jumps logged"). A job finished after Rae showed it adds the piece with a small "Rae helped" tag.

## Interactions in detail
- Dial drag: angle from the dial center to the pointer, unwrapped so a drag past 0 keeps counting (no jump from 359 to 0); dragging backward lowers it to 0, never negative. Max 900; at 900 the nose stops.
- Add a spin with a 0 current spin does nothing (button disabled until the spin is above 0). Three spins max; then Add a spin is disabled and the hint says "Tap Go or Clear."
- Go during a Go restarts the spin from 0 at once.
- Keypad: one answer box per card; typing a fraction bar enters numerator/denominator; a space makes a mixed number. Denominator 0 is refused with "A fraction can't have 0 pieces." Check is disabled while empty.
- Each job: two tries. A first miss shows the reason line for that miss (Content of Voice) and, after a miss, Rae's tip appears. A second miss: Rae shows the answer worked out (the equation filled, or the protractor reading highlighted), the job counts as done with "Rae helped".
- Protractor: drag by its body, rotate by its knob (keys: arrows move 2 px, Q and E rotate 1 degree). Not snapped, it still works like a real one (no auto-align in jobs beyond the snap described).
- Sketch jobs: Check reports only "Built to 25: yes" or "Not 25 yet. Measure it with the protractor." It never prints the angle the student made.
- Jump Log: switching sessions mid-way keeps each session's placed dots; Reset session clears that session only.
- Park: Ride with no ramps built: Dev rolls across, does his trick off the flat ground as a ground spin.
- Reset (in each panel's footer) clears that mode's Explore state; jobs and park pieces are saved on this device (localStorage, try/catch) with the line "Saved on this device only." under the counter; **Start over** in Park clears everything after a confirm.

## Look
Concrete paper `--paper #f4f2ee`, ink `#1d2026` (14.6:1), muted `#575c66` (6.0:1). Accent `--brand #5b2bb5`
grip-tape violet (7.64:1 on paper; white on it 8.54:1), used for spin 1 wedges, mode buttons and Check. Second spin
orange `#b54708` (4.85:1 on paper; white on it 5.43:1). Unknown part: gray `#6b7280` hatched wedge (4.32:1, non-text
only; its label is in ink). Stage night-slab `#2a2d34` behind the dial with chalk ticks `#f4f2ee` (12.33:1) and gold
`#f2b705` for the dashed jump line and highlights (7.58:1). Wedges always carry their number label, and the unknown is
hatched as well as gray, so color is never the only signal. Different from roller-coaster-rounding teal and
estimation-station freight red.

## Art
- park-bg: daytime concrete skate park seen from the side, smooth flat ground in front, chain-link fence, trees and sky, empty open slots along the ground for ramps; 16:9; no cutout; no people; Park and Ride backdrop.
- ground-strip: concrete ground and fence seen from the side, plain and calm; 4:1; no cutout; behind the ramp in Ramp Shop and the jump scene.
- plywood-texture: smooth light plywood surface, full frame, even light; 1:1; texture clipped to code-drawn ramps.
- board-top: a skateboard seen straight from above, dark grip tape, plain, four wheels visible; 4:1; cutout; on the dial (it rotates).
- dev-roll, dev-air, dev-spin, dev-land, dev-bail, dev-nod: Dev, about 11, brown skin, short black curls under a blue helmet, red hoodie, knee pads, on a skateboard; poses: rolling, tucked in the air, mid-spin with arms out, landing, sitting on the ground laughing with helmet on, nodding ready; 3:4; cutouts; people: true. Spin Deck (lower right), Ramp Shop and Park.
- rae-portrait, rae-point: Rae, a teen crew lead, freckles, red curly hair under a green helmet, denim jacket; head and shoulders smiling, and pointing to the side; 3:4; cutouts; people: true. Panel avatar and "Rae helped" moments.
- mina-air: Mina, about 10, East Asian girl, purple helmet, yellow shirt, tucked in the air on a skateboard; 3:4; cutout; people: true. Jump Log.
- walt-air: Walt, a man in his sixties, gray beard, white helmet, flannel shirt, calm grab in the air on a skateboard; 3:4; cutout; people: true. Jump Log.
- rae-air: Rae from rae-portrait, in the air on a skateboard; 3:4; cutout; people: true. Jump Log.
- prop-rail, prop-bench, prop-light, prop-planter, prop-bikerack, prop-tree: each one object, side view, painted to match park-bg; rail, bench 4:1; light, tree 9:16; planter, bike rack 4:3; cutouts; no people. Park pieces.
- scoreboard-blank: a plain wooden park scoreboard with a blank dark board face; 4:3; cutout; Park (text in code).
Drawn in code: the dial, wedges, readouts, ramps (exact angles), protractor, pole, line plot and dots.
20 images. Each cutout shows whole in every mode (Dev's 200 px cutout sits fully inside the stage at both sizes).

## Voice
Bank voice `big-sister`, style: "Say in a friendly, youthful way, like a teen skater showing a younger kid the
park." She is Rae. Not used by any neighbor (roller-coaster-rounding upbeat-guide, estimation-station gravel-ranger;
the other grade 3 to 5 math neighbors are unbuilt). `Curio.voice`, scope = mode + Explore/Jobs + job id. Lines carry
no numbers, so all are recordable; job prompts with numbers are read on screen and Read speaks the card and hint
(browser voice for numbers). Welcomes and hows are `how`; results are `event`.
- wSpin (how, Spin Deck welcome; stale once the board has moved): "I'm Rae. This is Dev's turn dial. Drag his board around, then tap Go."
- addHow (how, first time a spin is above 0 in Explore): "Tap Add a spin to stack another turn on top."
- wRamp (how, Ramp Shop welcome): "Every ramp makes an angle with the ground. Drag the protractor onto the corner and read it."
- scaleHow (how, first snap): "Start from the zero that lies on the ground. Follow that scale up to the ramp."
- bail (event, Test ride or Ride over 35, once per ride): "Too steep for Dev today. He's fine. Try a gentler ramp."
- wLog (how, Jump Log welcome): "Watch the jump, read the pole, then tap that height on the line plot."
- plotRight (event, every correct dot; kept short): "Got it."
- plotMiss (event, first miss on a dot): "Count the eighths up from the last number on the pole, then tap again."
- plotShown (event): "I placed that one. Watch where it goes."
- askHow (how, first question card): "Use the line plot. Type your answer in feet, then tap Check."
- wPark (how, Park welcome): "Every job you finish adds a piece to the park. Tap Ride to watch Dev skate it."
- jobHow (how, first job card in any mode): "Type your answer with the keypad, then tap Check."
- sketchHow (how, first sketch job): "Drag the ramp's lip to bend it. Check it with the protractor, then tap Check."
- right (event, every right job answer, whole): "Nailed it."
- missAdd (event, typed answer equals the sum where a difference was asked): "You added. The total is already known. Take the part you know away from it."
- missHundred (event, answer equals the fraction of 100): "A full turn is 360 degrees, not 100. Try again."
- missScale (event, other-scale reading): "That's the other scale. This angle is smaller than a square corner. Try this new ramp."
- missCount (event, answer equals a count of dots): "That's how many jumps. The question asks for feet. Try again."
- missOther (event, any other miss): "Not yet. Check Rae's tip, then try again."
- shown (event, whole): "Here's how I'd do it. Watch the equation."
- sessionDone (event, whole): "Session logged. It's on the scoreboard now."
How lines play once, then live in the hint. Results never repeat a reason more than once per miss. No line names a
control that is hidden or disabled (addHow waits for Add a spin to be enabled; jobHow needs Check's box visible).

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Spin jobs 1 and 2 (fraction to degrees) | guess; read ticks; size of the wedge by eye; switch to Explore and sweep the dial to the landmark, then come back; type the fraction of 100 (25, 75, 37, 38); type the digits (34) | exact answer, two tries (guess odds near 0); job dials have no ticks or readout; eye estimates are not exact; leaving Jobs re-rolls the variant, so the Explore reading is for a different fraction; 25, 75, 37.5, 38, 34 fail (missHundred or missOther) |
| Spin job 3 (degrees to fraction) | guess a common fraction (1/2, 1/4); type the degrees over 100 (120/100); elimination | answers 1/3, 1/6, 2/3 are not 1/2 or 1/4; 120/100 = 6/5 fails; typed, so no options to eliminate |
| Spin job 4 (total) | type a number on screen; subtract; guess | answers 135, 270, 75 differ from every shown label (90, 45, 180, 30); the subtraction (45, 90, 15) fails with missOther, and in variant 1 the wrong 45 equals a shown label, so the "type what you see" path fails there too |
| Spin job 5 (missing part) | add the two numbers (305, 250, 560); type a shown number; count ticks; eye the gray wedge | missAdd for the sums; shown numbers (125, 180, 70, 200, 360) are never the answer; no ticks; exact answer required |
| Spin job 6 (three parts) | add all three (600, 610, 310); subtract only one part (210, 270; 260, 210; 120, 110); add the two parts (240, 250, 130); type a shown number; guess | all fail: checked in Python, no common wrong equals its variant's answer (120, 110, 50), and no answer equals a number shown on its card |
| Spin jobs 7 and 8 (sixths, twelfths, back to fourths and eighths) | as jobs 1 to 3: guess; eye the wedge; type the fraction of 100 (17, 83, 8); type degrees over 100 (270/100) | exact answers 60, 300, 30 and 3/4, 5/8, 7/8, two tries; no ticks or readout; 17, 83 and 8 fail with missHundred; 270/100, 225/100 and 315/100 are not the answers |
| Spin jobs 9 and 10 (one-degree turns) | type a number on the card; guess; count slices carelessly | job 9's card and wedge show no number, so the count is the only way in; the second boxes ask about numbers that are stated (50; 37), which is the point of 4.MD.5b: the count of turns is the measure. A child who types them without thought still meets the full-turn box, where 360 must be recalled; 100 gets missHundred |
| Spin job 11 (write the equation) | type the two shown numbers with any sign; add them (385, 315, 600); skip the equation | the equation must be one of the four true forms before the answer box opens; the sums get missAdd; answers 155, 135, 120 are never shown on their own card |
| Ramp measure jobs 1 and 2 | guess; read the wrong scale then try the other one (elimination by two readings); type a round number | guess odds 3 in 81 per try; a wrong-scale miss loads a new ramp, so the second scale reading belongs to an old ramp; the common wrong (160, 145, 132, 155, 140, 165) fails with missScale |
| Ramp job 3 (straight line) | type the shown bank angle; type 180; guess | 30, 40, 25 and 180 are not 150, 140, 155; the miss loads the next variant |
| Ramp sketch jobs 4 and 5 | drag at random and mash Check; use Check's message to step by the difference with arrow keys; set it in Explore with Show angle, then switch | two Checks only; the miss message never says the angle made, so there is no difference to step; the job ramp starts 10+ degrees from target and does not come from Explore; random hit odds about 3 in 56 per try |
| Jump Log dot taps | tap every tick; tap the same tick; read the axis against the pole by lining them up; take the order of jumps | taps go one at a time with two tries, then Rae places it and it counts "Rae placed" (mash success about 15 percent per dot, a full session by mashing near 0); the pole is vertical and the axis horizontal, with different spacing, so nothing lines up; the pole is labeled only at halves, so reading it means counting eighths; order is shuffled |
| Jump Log questions | type an axis label you see; type a count of dots; type the numerators' total (30, 36); add numerators and denominators | labels are on screen, so a lucky label is possible (6 of 9 answers are labels; two tries gives about 15 percent per question), but a session's "on your own" mark needs all three on the first or second try and three lucky labels in a row is under 0.4 percent; counts (4, 5) fail with missCount; 30 and 36 whole fail; 9/16 fails |
| Park pieces counter "on your own" | let Rae show every job; retry a finished job | shown jobs add the piece but not the "on your own" count; a finished job can be replayed, but the counter counts each job once |
| Ride and Test ride | none (no check) | they show outcomes only; Show angle is Explore only |
| Explore readouts | none (no check) | Explore has no checks; it can't feed a job because jobs re-roll when you return |

## Heard in order
Grade 4, so not every action speaks, but a result must land before the next prompt:
1. Load, first tap on the board: drag starts; wSpin queues after the tap (may be cut, rule 16); addHow waits for wSpin and for Add a spin to be enabled. Next action spoken: "Drag his board around, then tap Go."
2. Spin Explore, Go: the trick name shows on screen (no line); Read speaks it.
3. Jobs, first card: jobHow (once). Check: right (whole) or a miss reason (whole); the next job's card appears at once, and its prompt is on screen only; nothing new is spoken until the student acts.
4. Second miss: shown (whole), then the equation fills; the job pager moves on only after shown ends or a tap.
5. Ramp Shop: wRamp, then scaleHow at the first snap (waits for wRamp). A wrong-scale Check: missScale (whole) plays before the new ramp draws. Sketch: sketchHow on the first sketch card.
6. Test ride over 35: bail plays once per ride, after the bail pose shows.
7. Jump Log: wLog; each dot: plotRight, or plotMiss then (second miss) plotShown (whole), before the next jump starts (the jump waits for it). After the last dot: askHow; each answer: right or a miss reason (whole) before the next question shows. Session end: sessionDone (whole).
8. Park: wPark on first visit; Ride plays with no speech except bail.
No line contains a number or a bare letter; fractions and degrees are on screen and spoken by Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| A full turn is 360 degrees; a one-degree angle turns through 1/360 of a circle; n one-degree angles make n degrees | CCSS Math 4.MD.5a, 4.MD.5b (corestandards.org) | Wikipedia, "Degree (angle)" | yes |
| Angle measure is additive; parts of an angle add to the whole | CCSS Math 4.MD.7 | Math is Fun, "Angles" (adjacent angles) | yes |
| Angles on a straight line add to 180 degrees | Wikipedia, "Straight angle" | Math is Fun, "Supplementary Angles" | yes |
| Read a protractor from the 0 on the scale that lies along one ray | Math is Fun, "Using a Protractor" | Khan Academy, "Measuring angles with a protractor" | yes |
| Skaters name spins by degrees: 180 half a turn, 360 a full turn, 540 one and a half | X Games, "Tricktionary: guide to skateboard terms and tricks" | Exploratorium, Skateboarding Glossary | yes |
| Tony Hawk landed the first 900 (two and a half turns) at the 1999 X Games (June 27, San Francisco) | Wikipedia, "900 (skateboarding)" | Guinness World Records, "First 900 on a skateboard" | yes |
| At the same speed, a steeper launch (under 90 degrees) gives a higher jump (peak height = v squared times sin squared of the angle over 2g) | HyperPhysics, "Trajectories" | OpenStax University Physics Vol. 1, 4.3 Projectile Motion | yes |
Cut: a spoken helmet rule (only retail and one hospital source found in this pass; Dev just wears a helmet in the art);
the number of tries Hawk took (sources disagree: 10 or 11).

Number checks (Python, run 2026-11-06): every landmark is 360 times its fraction (17 landmarks); all spin answers
(fraction x 360, sums, missing parts) recomputed; every common wrong (fraction of 100, digits, sums, single
subtractions, all-part sums) differs from its answer; job 6's first draft had a variant (45 + 90 + ? = 180) whose answer
equaled a shown label, and job 4's subtraction slip equaled a shown label, so variant 6c was changed to 60 + 70 + ? =
180 (50) and 6b to 100 + 150 (110); other-scale readings 180 minus the angle (all differ by 84 or more); guess odds
(measure 3/81, sketch 3/56, dot mash 2/13 over two tries); line plot data: counts per tick (max stack 5, fits), min,
max, mode; all nine answers (3/8, 2, 1/8, 5/8, 15/4, 9/8, 3/4, 9/2, 7/8); count, numerator and nums-plus-dens wrongs
all fail (one coincidence: L2 nums-plus-dens 16/32 = 1/2 also fails, as 1/2 is not 2); session means rise with the
kicker (0.425, 0.78, 1.125 ft), matching the steeper-higher claim; contrast ratios in Look.

Number checks for the spec fix (Python, run 2026-11-10): 360/6 = 60, 5 x 360/6 = 300, 360/12 = 30; 270/360 = 3/4,
225/360 = 5/8, 315/360 = 7/8; fraction-of-100 slips 17, 83 and 8 differ from the answers; 270 - 115 = 155,
225 - 90 = 135, 360 - 240 = 120, and the sums 385, 315, 600 differ from them; no answer in jobs 7, 8 or 11 is a
number shown on its card; 14 pieces plus 5 trick-list lines is 19.

## Done when
1. Focus: in every mode the dial, ramp, line plot or park is the biggest central thing, and at 1366x768 every control the mode needs (switch, card, keypad, Check) is above the fold; at 680x425 stage and panel stay side by side.
2. Dragging the board to 135 shows "135 degrees", "135 one-degree turns", "135/360 of a full turn", "= 3/8 turn"; arrow keys step 1 degree.
3. Two stacked spins 90 and 45 show violet and orange labeled wedges and "90 + 45 = 135"; Go spins Dev 135 and a 540 shows its trick name.
4. Spin job 5 accepts only 55; 305 plays missAdd; leaving Jobs and coming back shows another variant.
5. A ramp of 20 accepts 19 to 21; 160 plays missScale and draws a new ramp; no angle number shows anywhere in Jobs.
6. A sketch job built to 25 passes at 24 to 26; a miss never shows the built angle.
7. Jump Log Low session: every dot only lands on its true tick; answers 3/8 (or 6/16), 2 (or 16/8) and 1/8 pass; 4 plays missCount.
8. A tap while anything plays acts at once: Go during a spin restarts it, Ride during a ride restarts it, Stop ends it, a mode switch stops it.
9. Test ride at 40 shows the bail pose and plays bail once; 30 shows the high arc with the saved spin wedge.
10. Park counter reaches 19 with the right pieces (14 as before plus five trick-list lines); a shown job adds a "Rae helped" tag and is not counted as on your own; "Saved on this device only." shows.
11. Voice: each how line speaks once in five repeats; right and miss lines speak every time and finish before the next card's line; no line names a disabled control.
12. Spin job 7 (1/6) accepts 60 only and 17 plays missHundred; job 9 with 12 slices accepts 12 and shows no number before the answer; job 10 needs 37 and 360; job 11 opens its answer box only after a true equation such as 115 + ? = 270 and accepts 155 only.

## Open questions
none
