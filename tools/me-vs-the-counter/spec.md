# Me vs the Counter

## One idea
A ball drops on the gym floor and a sensor pad counts every time it hits, while the class counts the same bounces out
loud with a tap for each; the two counts line up on a bounce timeline, so the class sees exactly which fast little
bounces they missed, and then uses the computer's steady counts to pick the bounciest ball.

## Not like
- class-poll (1, math): a class vote turned into a graph. Here nobody votes: the data is measured by a sensor, and the
  point is how a computer collects and counts data compared with people.
- robot-dance (K): step-by-step commands. No program here.
- secret-keeper (K, this group): private information; a sort, not a measurement.
- computer-builder (1): parts and their jobs. This tool shows one input (a sensor) collecting data, nothing to build.
- spot-the-ai (1, this group): rules versus learned patterns. The counter here learns nothing; it just counts.

## Who and how
- Grade K, computer science. Module: Count and Decide (Data and Analysis).
- Topic line: how computers collect and count data
- Driver: teacher on a projector. Half the class counts bounces out loud (or makes tally marks on whiteboards); a
  helper or the teacher taps the big hand button for each "bounce!". The other half watches the computer's count.
- 10 to 20 minutes. tool.json: driver "teacher", minutes "10-20", modes ["Bounce Lab", "Bounciest Ball"],
  grades_label "Kindergarten".
- Standards (CSTA 2026 ids from the module): EK-DAT-DC-08, EK-DAT-DI-09, EK-DAT-IM-10. 2017 crosswalk: 1A-DA-06 (collect and
  present the same data in different visual formats), 1A-DA-07 (identify patterns in data and make predictions).
- Reads nothing: icons on every control, every fixed line voiced, 60 px targets.

## Screens and modes
Header (kit): title "Me vs the Counter", small line "Who counts better?"; mode buttons "Bounce Lab" (ball icon) and
"Bounciest Ball" (trophy icon); Motion, Sound, Read.

Stage (painted pieces placed over the painted gym, re-laid per size; see Art):
- The gym (art: gym-backdrop): wall and wooden floor in one painted scene. The drop stand (art: drop-arm-closed /
  drop-arm-open) stands at the center top and holds the chosen ball (art: ball-*).
- The sensor pad (art: sensor-pad): a grey mat on the floor under the ball. A row of round lights is drawn in code over
  the mat's blank strip; they flash on every hit. A cable drawn in code runs from the pad to the computer.
- Two counters flank the drop column at eye height, each a big number on a cream plate drawn in code with tally marks
  under it: left "Me" (the painted hand, art: tap-hand, orange plate edge) and right "Counter" (the painted computer,
  art: counter-computer, with the number drawn in code on its blank screen, teal plate edge).
- After a drop: the bounce timeline (code, a chart) slides up over the lower floor, 10 s wide. Top row: a teal tick for
  every hit the pad felt. Bottom row: an orange hand mark for every tap. Matched pairs are joined by a short line. A
  hit with no tap gets a soft yellow ring ("missed"); a tap with no hit gets a small grey "extra" ring.

Panel:
- `#hint`.
- Ball rack: four 72 px ball buttons showing the ball cutouts: bouncy ball, basketball, tennis ball, beanbag. The chosen
  ball sits in the drop stand.
- Big buttons: "Drop" (down arrow, `.big-btn.gold`), the hand button "Bounce!" (120 px round, orange, showing the
  tap-hand cutout; also the space bar), "Again" (circular arrow: same ball), "Slow" toggle (turtle: half speed; the
  counts do not change).
- After a drop: "Our count" with minus and plus buttons (60 px) to type in a paper tally instead of taps.

### Mode 1: Bounce Lab (explore, opens first)
Focus: the falling ball over the pad, with the two counters on either side of it; once the ball rests, the timeline.
The drop column is the center of the stage and the tallest thing on it; the counters sit beside it, never above or
below, so the eye moves between ball, pad and numbers without leaving the middle. The timeline replaces the lower
floor when it slides in.
Pick any ball, press Drop. The ball falls and bounces; the pad flashes and the Counter number goes up on every hit; the
class taps along. When the ball rests, the timeline slides in and the narrator compares. Again repeats the same ball.
No table, no winner: just counting and comparing.

### Mode 2: Bounciest Ball (data)
Focus, in turn: the question card (four big ball cutouts), then the drop column as in Bounce Lab (the results table
shrinks to a strip on the stage edge), then the picture graph, which fills the stage center when it is shown.
A question card over the stage: "Which ball is the bounciest?" with the four balls. The class predicts by pointing;
the teacher taps that ball on the card (a star sticker marks it; optional, "Skip" closes the card too). Then each ball
is dropped in any order. A results table on the stage edge fills in: one row per ball (ball cutout), column "Me" (the
class count for each try, up to three tries), column "Counter" (the computer count). When all four balls have a
Counter count, "Show the chart" (bar icon) builds a picture graph: one dot per hit in a row for each ball, the ball
cutout at the start of each row, so the longest row is the bounciest. The narrator asks which ball is bounciest; the
teacher taps a row; the row glows and the answer line plays. "Start over" clears the table.

## Content
Every ball is dropped from the same height, 1.8 m above the floor (a fair test: same drop for every ball). A hit is
counted every time the ball touches the floor. The model: the ball falls for 0.606 s (time to fall 1.8 m, g = 9.8),
and bounce n (n = 1, 2, ...) lasts `2 x 0.606 x e^n` seconds; a ball stops once its next bounce would be shorter than
0.25 s (the tool's own cut-off: too small to see). Use g = 9.8 and the e values below exactly: the bouncy ball's 16th
bounce would last 0.249 s, just under the cut-off.

| Ball | Bounce factor e | Source of e | Hits | Hit times (s) |
|---|---|---|---|---|
| Bouncy ball | 0.90 | the tool's own choice for a small rubber ball | 15 | 0.61, 1.70, 2.68, 3.56, 4.36, 5.07, 5.72, 6.30, 6.82, 7.29, 7.71, 8.09, 8.43, 8.74, 9.02 |
| Basketball | 0.85 | FIBA: dropped from 1.8 m it rebounds 1.2 to 1.4 m; midpoint 1.3/1.8, e = square root of 0.722 | 10 | 0.61, 1.64, 2.51, 3.26, 3.89, 4.43, 4.88, 5.27, 5.60, 5.88 |
| Tennis ball | 0.745 | ITF: dropped from 254 cm it rebounds 135 to 147 cm; midpoint 141/254, e = square root of 0.555 | 6 | 0.61, 1.51, 2.18, 2.68, 3.06, 3.33 |
| Beanbag | 0 | it does not bounce | 1 | 0.61 |

First bounce heights drawn: bouncy 1.46 m, basketball 1.30 m, tennis 1.00 m (1.8 x e squared). Every drop lasts
under 10 seconds, so the timeline is 10 s wide for all balls. The computer count is the same on every drop; that is
the lesson the Again button shows. Slow plays the same times at half speed (the timeline still shows real seconds).

Matching taps to hits (for the timeline): taps and hits are matched in time order (a later tap never pairs with an
earlier hit than a previous pair). A tap may pair with a hit if it comes from 0.15 s before to 0.40 s after the hit
(the tool's own window; children tap late). Among all in-order matchings, use the one with the most pairs, and among
those the smallest total gap (a small dynamic program over the two sorted lists). Leftover hits are "missed",
leftover taps are "extra". With Slow on, tap times are halved back to real seconds before matching.

## Interactions in detail
- Drop: the stand opens (drop-arm-open), the ball falls; each hit squashes the ball cutout (a short vertical squash,
  Motion on), flashes the pad lights, plays a pitched tick (bouncy ball highest, beanbag a soft thud) and adds a teal
  tally mark.
- The hand button is always live. Before a drop, a tap gives a soft tap sound and a wiggle (practice; not recorded).
  From the moment the stand opens until 1 s after the last hit, each tap is recorded and adds an orange tally mark at
  once (the class sees their own count grow). On the first drop of the page load the hand button pulses gently.
- When the ball rests: the Counter number pulses, the timeline slides in, and one compare line plays: same, fewer or
  more. If there were no taps at all, the "Our count" stepper glows instead and the compare waits until it is used (or
  the teacher drops again).
- Our count stepper: 0 to 30; changing it replaces the tap count for that try and hides the hand marks row (a paper
  count has no times), keeping only the two totals.
- Again keeps the table row and adds a new "Me" try (up to three per ball; a fourth replaces the oldest).
- Every control stays live while a ball bounces, and responds at once: Drop or Again restarts the drop from the top
  (the unfinished try is dropped, no row, no compare); a ball in the rack swaps the ball and restarts with it; Slow
  changes the speed of the bounces still to come at once; a mode switch stops the drop and keeps each mode's finished
  data for the page load. Nothing is saved except the kit settings.
- Prediction and chart in Bounciest Ball: the chart button is disabled (dimmed, lock icon) until every ball has a
  Counter count. Tapping a non-longest row plays line 17 and keeps the chart; the longest plays line 16.
- Keyboard: space is the hand button; D drops; Tab order rack, Drop, hand, Again, Slow, stepper, table rows, chart.
- Motion off: the ball jumps between floor and peak positions on the same times (no squash, no arcs); sounds, counts
  and timing unchanged, so tapping along still works.
- Sizes: the hand button, Drop, the drop column and both counters visible without scrolling at every size; at 680x425
  the timeline sits over the floor and the table becomes a strip of four mini rows.

## Look
- Band K-2, own `:root`: `--paper #fdf8f1`, `--ink #2a1f14`, `--muted #6b5a48`, `--line #ecdcc6`, `--brand #b45309`
  (gym orange, the accent; header and the Me plate edge), `--focus #1d4ed8` with a white inner ring, counter teal
  `#0f6e74` for the Counter side, `--gold #ffd23f` for Drop. Counter plates `#fffaf2`.
- Scene (asked of the painter): warm maple floor, pale cream block wall, soft daylight; grey pad; the balls in their
  own bright colors. Timeline and chart on a cream card `#fffaf2` with a soft shadow so they read over the floor.
- Neighbors: robot-dance magenta, computer-builder cobalt, class-poll (math) and siblings: snowy-mail-route post red,
  secret-keeper evergreen, spot-the-ai steel navy. Gym orange is new among them.
- Contrast (computed): white on header 5.02:1; ink on paper 15.23:1; muted on paper 6.25:1; orange brand text on
  paper 4.75:1 (used at 20 px or more); ink on counter plate 15.49:1; teal on plate 5.77:1; orange on plate 4.83:1
  (20 px or more); ink on gold 11.15:1; white on teal 6.0:1; focus on paper 6.34:1. Me and Counter are told apart by
  picture and side, not only color.

## Art
Local FLUX (`scripts/localart.py`) unless marked people; one flat, bright picture-book style for all, ask in one session.
- gym-backdrop: "A school gymnasium seen straight on, pale cream painted cinder block wall, a high row of windows with
  daylight, a folded basketball hoop at the far left, a warm maple wooden floor filling the lower third, soft even light,
  flat bright picture-book illustration"; 16:9; cutout no; people no; the whole stage behind everything, the floor's
  center left open for the pad.
- sensor-pad: "A flat grey rubber floor mat seen from a low front angle, rounded corners, a blank dark strip along its
  front edge, flat bright picture-book illustration, plain white background"; 4:1; cutout yes; people no; on the floor
  under the drop column; lights drawn in code on the blank strip.
- drop-arm-closed: "A tall silver metal stand with a red claw at the top holding closed around an empty space, flat
  bright picture-book illustration, plain white background"; 3:4; cutout yes; people no; holds the ball before a drop.
- drop-arm-open: the same stand with the red claw swung open wide; 3:4; cutout yes; people no; swapped in on Drop.
- ball-bouncy: "A small shiny hot pink rubber ball with a white swirl, flat bright picture-book illustration, plain
  white background"; 1:1; cutout yes; people no; drop column, rack button, table and chart rows; squashed in code.
- ball-basket: "A plain orange basketball with black seams and a smooth blank surface, flat bright picture-book
  illustration, plain white background"; 1:1; cutout yes; people no; same uses.
- ball-tennis: "A fuzzy bright yellow-green tennis ball with one curving white seam, flat bright picture-book
  illustration, plain white background"; 1:1; cutout yes; people no; same uses.
- beanbag: "A soft square cloth beanbag in red and blue patchwork with big stitches, flat bright picture-book
  illustration, plain white background"; 1:1; cutout yes; people no; same uses; flattens a little in code on its one hit.
- counter-computer: "A chunky friendly beige desktop computer with a big blank pale screen and a small keyboard in
  front, flat bright picture-book illustration, plain white background"; 1:1; cutout yes; people no; the Counter
  side; the count is drawn in code on the blank screen.
- tap-hand: "A child's open hand raised high, palm facing the viewer, warm brown skin, an orange sleeve cuff at the
  wrist, flat bright picture-book illustration, plain white background"; 1:1; cutout yes; people: true (Gemini,
  `scripts/art.py`, Cory reviews); the Me side and the hand button.
Pad lights, cable, plates, numbers, tally marks, timeline, table, picture graph, star sticker and preview.svg are drawn
in code (they are counts, charts and controls).

## Voice
Bank voice `easy-coach` (Umbriel), "Say in an easy-going, encouraging way, like a relaxed sports coach": a gym coach
with a clipboard. Not used by any neighbor (robot-dance lively-host, computer-builder bright-teacher, data-table-builder
knowing-guide, secret-keeper warm-teacher, spot-the-ai curious-librarian, snowy-mail-route gentle-storyteller).
`Curio.voice`, `scope: () => state.mode`. Read speaks `#hint`. No line plays while a ball is bouncing except the
tap-along line below (it is dropped once the first hit happens); lines wait for the ball to rest.
How (spoken the first time its moment comes, then hint only):
1. w-lab (Bounce Lab entered; stale on Drop): "Welcome to the gym! You count the bounces, and the computer counts them
   too. Tap a ball. Then press Drop."
2. tap-along (first ball picked or first Drop, whichever comes first; stale at the first hit): "Every time the ball
   hits the floor, say bounce, and tap the hand!"
3. sensor (after the first drop's compare line; stale on the next Drop): "The pad on the floor is a sensor. It feels
   every hit and tells the computer."
4. w-ball (Bounciest Ball entered; stale when a guess is tapped, Skip, or a Drop): "Which ball is the bounciest? Point
   to your guess. Then tap that ball on the card."
5. drop-all (guess tapped or Skip; stale when all four balls have counts): "Now tap a ball and press Drop. Drop every
   ball, one at a time."
6. paper (first time the stepper glows, no taps; stale when the stepper is used or on Drop): "Did you count on paper?
   Tap plus or minus to show your count."
19. pick-row (chart first shown; stale when a row is tapped): "Which ball is the bounciest? Tap its row."
Events (every time; stale when a new drop starts or the mode changes):
7. "The computer counted the same as you! Nice counting!"
8. "You counted fewer than the computer. Look for the yellow circles. Those are the bounces you missed."
9. "You counted more than the computer. The gray circles are extra taps."
10. "The bounces got small and fast at the end. Those are the hardest to count."
11. "Again! The computer got the same number. It counts the same way every time."
12. "Bouncy ball: the computer counted fifteen." 13. "Basketball: the computer counted ten." 14. "Tennis ball: the
computer counted six." 15. "Beanbag: the computer counted one. Plop!"
16. (stale on the next row tap) "Yes! The bouncy ball has the longest row. It's the bounciest ball!"
17. (stale on the next row tap) "Look again. Which row is the longest? Tap it."
18. (fourth ball's first count; stale when the chart is shown) "Every ball has a count. Tap Show the chart!"
Which line when: after each drop, 12 to 15 for that ball, then 7, 8 or 9 (8 or 9 adds 10 when a missed or extra mark
falls after the 5th hit); an Again drop says 11 before the compare.

## Family engine
none (no data-desk features at K: the table and picture graph are drawn in the tool).

## Sources
- CSTA K-12 CS Standards (2017) 1A-DA-06, 1A-DA-07: https://csteachers.org/k12standards/ ; 2026 ids from
  data/standards/csta-2026-ids.txt.
- FIBA Official Basketball Rules, Basketball Equipment, ball rebound test (dropped 1.8 m, rebounds 1.2 to 1.4 m):
  https://www.fiba.basketball/documents (Official Basketball Rules, "Basketball Equipment"); summary at
  https://new.topendsports.com/biomechanics/coefficient-of-restitution.htm
- ITF Rules of Tennis, Appendix I, ball rebound (dropped 100 in or 254 cm onto concrete, rebounds 53 to 58 in or 135 to
  147 cm): https://www.itftennis.com/en/about-us/governance/rules-and-regulations/
- Fall time t = square root of (2h / g), g = 9.8 m per second squared; bounce height ratio = e squared (standard
  physics, e.g. OpenStax College Physics 2e, ch. 2.7 and 8.5: https://openstax.org/books/college-physics-2e).
- Bouncy ball e = 0.90, the 0.25 s cut-off and the matching window are the tool's own choices.
- Checks run (Python, 2026-10-29): fall time 0.6061 s; hit counts 15, 10, 6, 1 and every hit time in the table
  reproduced (the tennis ball's last hit is 3.3348 s, so 3.33, not the 3.34 the first draft had); next bounce after
  the last hit 0.249, 0.239, 0.207 s, all under 0.25; e basketball 0.8498, tennis 0.7451; first bounce heights 1.46,
  1.30, 1.00 m; shortest gap between hits 0.277 s (bouncy), 0.281 (basketball), 0.278 (tennis).
- Matching check: the first draft's rule (nearest unpaired hit within 0.3 s, greedy) failed a perfect counter who taps
  0.15 s late (14 of 15 paired on the bouncy ball) and at 0.35 s late paired only 9 of 15, because the late hits are
  closer together than the window. The in-order matching above pairs 15/15, 10/10 and 6/6 at a steady lag of 0, 0.15,
  0.25 and 0.35 s. Simulated noisy child (lag 0.22 s, spread 0.1 s, cannot tap faster than every 0.3 s), 2,000 runs:
  on average 0.30 (bouncy), 0.20 (basketball), 0.10 (tennis) taps per drop fall outside the window and show as extra.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Each ball's pad hits match the Content times to within one animation frame (log them) and the Counter shows 15,
   10, 6 and 1 on every drop, including Slow and Motion off.
2. Hand taps add marks at once; the timeline pairs taps and hits with the in-order rule (a scripted pattern of taps
   0.35 s late on the bouncy ball shows 15 pairs and no rings; one skipped tap shows exactly one yellow ring).
3. Compare lines 7, 8, 9 match the totals; 10 plays only when a miss or extra falls after the 5th hit.
4. The Our count stepper replaces the tap count and the compare uses it.
5. Bounciest Ball: the chart unlocks only after four Counter counts, rows have 15, 10, 6 and 1 dots, and the row taps
   give lines 16 and 17.
6. Again keeps up to three Me tries per ball and line 11 plays.
7. Focus: at 1366x768 and 680x425 the drop column with the ball and pad is the center and the largest thing on the
   stage, with both counters beside it; after a drop the timeline is the largest thing on the stage.
8. Tap while it plays: mid-bounce, the hand records at once, Slow changes speed at once, a rack ball or Again restarts
   at once with the new ball, and a mode switch stops the drop, all with no stale line afterwards.
9. Every size in STANDARDS.md: hand button, Drop and counters visible without scrolling; 60 px targets at full screen.
10. Voice: how lines once each; the ball line and compare line on every drop; no line names a disabled control, and the chart line plays only once the chart is unlocked; Read and Sound rules pass with held clicks;
   keyboard (space, D, Tab) runs a full
   Bounciest Ball round; console clean.

## Open questions
- tap-hand is the only picture of a person (a child's hand). Keep it painted (Cory reviews), or use a plain hand icon?
