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

Stage (drawn in code over one backdrop image, re-laid per size):
- A school gym: wall (art: gym-wall), wooden floor drawn in code. A drop arm at the top holds the ball.
- The sensor pad: a flat grey mat on the floor under the ball with a row of little lights; it flashes on every hit.
- Two counters above the floor, side by side, each a big number with tally marks under it:
  left "Me" (a raised hand icon, orange) and right "Counter" (a small computer chip icon, teal).
- After a drop: the bounce timeline slides in under the floor (10 s wide). Top row: a teal tick for every hit the
  pad felt. Bottom row: an orange hand mark for every tap. Matched pairs are joined by a short line. A hit with no tap
  gets a soft yellow ring ("missed"); a tap with no hit gets a small grey "extra" ring.

Panel:
- `#hint`.
- Ball rack: four 72 px ball buttons with drawings: bouncy ball (small, bright pink with a swirl), basketball, tennis
  ball, beanbag (a square cloth bag with stitches). The chosen ball sits in the drop arm.
- Big buttons: "Drop" (down arrow, `.big-btn.gold`), the hand button "Bounce!" (120 px round, orange, raised hand
  icon; active only while the ball is falling or bouncing; also the space bar), "Again" (circular arrow: same ball),
  "Slow" toggle (turtle: half speed; the counts do not change).
- After a drop: "Our count" with minus and plus buttons (60 px) to type in a paper tally instead of taps.

### Mode 1: Bounce Lab (explore, opens first)
Pick any ball, press Drop. The ball falls and bounces; the pad flashes and the Counter number goes up on every hit; the
class taps along. When the ball rests, the timeline slides in and the narrator compares. Again repeats the same ball.
No table, no winner: just counting and comparing.

### Mode 2: Bounciest Ball (data)
A question card over the stage: "Which ball is the bounciest?" with the four balls. The class predicts by pointing;
the teacher taps "Our guess" on a ball (optional, a star sticker marks it). Then each ball is dropped in any order.
A results table on the stage edge fills in: one row per ball (ball picture), column "Me" (the class count for each try,
up to three tries), column "Counter" (the computer count). When all four balls have a Counter count, "Show the chart"
(bar icon) builds a picture graph: one dot per hit in a row for each ball, so the longest row is the bounciest. The
narrator asks which ball is bounciest; the teacher taps a row; the row glows and the answer line plays. "Start over"
clears the table.

## Content
Every ball is dropped from the same height, 1.8 m above the floor (a fair test: same drop for every ball). A hit is
counted every time the ball touches the floor. The model: the ball falls for 0.606 s (time to fall 1.8 m), and each
bounce lasts `2 x 0.606 x e^n` seconds; a ball stops once its next bounce would be shorter than 0.25 s (the tool's own
cut-off: too small to see).

| Ball | Bounce factor e | Source of e | Hits | Hit times (s) |
|---|---|---|---|---|
| Bouncy ball | 0.90 | the tool's own choice for a small rubber ball | 15 | 0.61, 1.70, 2.68, 3.56, 4.36, 5.07, 5.72, 6.30, 6.82, 7.29, 7.71, 8.09, 8.43, 8.74, 9.02 |
| Basketball | 0.85 | FIBA: dropped from 1.8 m it rebounds 1.2 to 1.4 m; midpoint 1.3/1.8, e = square root of 0.722 | 10 | 0.61, 1.64, 2.51, 3.26, 3.89, 4.43, 4.88, 5.27, 5.60, 5.88 |
| Tennis ball | 0.745 | ITF: dropped from 254 cm it rebounds 135 to 147 cm; midpoint 141/254, e = square root of 0.555 | 6 | 0.61, 1.51, 2.18, 2.68, 3.06, 3.34 |
| Beanbag | 0 | it does not bounce | 1 | 0.61 |

First bounce heights drawn: bouncy 1.46 m, basketball 1.30 m, tennis 1.00 m (1.8 x e squared). Every drop lasts
under 10 seconds, so the timeline is 10 s wide for all balls. The computer count is the same on every drop; that is
the lesson the Again button shows. Slow plays the same times at half speed (the timeline still shows real seconds).

Matching taps to hits (for the timeline): each tap is paired with the nearest unpaired hit within 0.3 s (the tool's own
window); leftover hits are "missed", leftover taps are "extra".

## Interactions in detail
- Drop: the arm opens, the ball falls; each hit squashes the ball (Motion on), flashes the pad, plays a pitched tick
  (bouncy ball highest, beanbag a soft thud) and adds a teal tally mark.
- The hand button records a tap time from the moment the arm opens until 1 s after the last hit; taps outside that are
  ignored. Each tap adds an orange tally mark at once (the class sees their own count grow).
- When the ball rests: Counter number pulses, the timeline slides in, and one compare line plays: same, fewer or more.
  If there were no taps at all, the "Our count" stepper glows instead and the compare waits until it is used (or the
  teacher drops again).
- Our count stepper: 0 to 30; changing it replaces the tap count for that try and hides the hand marks row (a paper
  count has no times), keeping only the two totals.
- Again keeps the table row and adds a new "Me" try (up to three per ball; a fourth replaces the oldest).
- Prediction and chart in Bounciest Ball: the chart button is disabled (dimmed, lock icon) until every ball has a
  Counter count. Tapping a non-longest row plays line 17 and keeps the chart; the longest plays line 16.
- Drop, ball rack and mode switch are disabled while a ball is bouncing; a mode switch keeps each mode's data for the
  page load. Nothing is saved except the kit Motion setting.
- Keyboard: space is the hand button; D drops; Tab order rack, Drop, hand, Again, Slow, stepper, table rows, chart.
- Motion off: the ball jumps between floor and peak positions on the same times (no squash, no arcs); sounds, counts
  and timing unchanged, so tapping along still works.
- Sizes: the hand button, Drop and both counters visible without scrolling at every size; at 680x425 the timeline
  sits over the floor and the table becomes a strip of four mini rows.

## Look
- Band K-2, own `:root`: `--paper #fdf8f1`, `--ink #2a1f14`, `--muted #6b5a48`, `--line #ecdcc6`, `--brand #b45309`
  (gym orange, the accent; header and the Me counter), `--focus #1d4ed8` with a white inner ring, counter teal
  `#0f6e74` for the Counter side, `--gold #ffd23f` for Drop.
- Scene: maple floor #e9c99a with board lines #d3ab72, pad grey #5b6470 with lights #7ee0d6.
- Neighbors: robot-dance magenta, computer-builder cobalt, class-poll (math) and siblings: snowy-mail-route post red,
  secret-keeper evergreen, spot-the-ai steel navy. Gym orange is new among them.
- Contrast: white on header 5.02:1; ink on paper 15.23:1; muted on paper 6.25:1; orange brand text on paper 4.75:1
  (used at 20 px or more); ink on maple floor 10.18:1; white on teal #0f6e74 6.0:1 (builder confirms); focus 6.34:1.
  Me and Counter are told apart by icon and side, not only color.

## Art
- gym-wall: "An empty school gymnasium wall seen straight on, pale painted cinder blocks, a high window row with
  daylight, a folded basketball hoop at one side, blank walls, soft even light, flat illustration"; 16:9; cutout no;
  people no; Cloudflare FLUX (scripts/cfart.py); the stage backdrop above the floor drawn in code.
Balls, pad, counters, timeline, chart and preview.svg are drawn in code.

## Voice
Bank voice `easy-coach` (Umbriel), "Say in an easy-going, encouraging way, like a relaxed sports coach": a gym coach
with a clipboard. Not used by any neighbor (robot-dance lively-host, computer-builder bright-teacher, teach-the-robot
playful-friend) or sibling.
How (spoken once per page load, then hint only):
1. welcome Bounce Lab: "Welcome to the gym! Let's count bounces. You count, and the computer counts too."
2. "Pick a ball. Then press Drop. Every time it hits the floor, say bounce, and tap the hand."
3. "The pad on the floor is a sensor. It feels every hit and tells the computer."
4. welcome Bounciest Ball: "Which ball is the bounciest? Point to your guess. Then tap the star on it."
5. "Now drop every ball. We'll count each one."
6. "Did you count on paper? Tap plus and minus to show your count."
Events (every time; stale when a new drop starts or the mode changes):
7. "The computer counted the same as you! Nice counting!"
8. "You counted fewer than the computer. Look for the yellow circles. Those are the bounces you missed."
9. "You counted more than the computer. The gray circles are extra taps."
10. "The bounces got small and fast at the end. Those are the hardest to count."
11. "Again! The computer got the same number. It counts the same way every time."
12. "Bouncy ball: the computer counted fifteen." 13. "Basketball: the computer counted ten." 14. "Tennis ball: the
computer counted six." 15. "Beanbag: the computer counted one. Plop!"
16. "Yes! The bouncy ball has the longest row. It's the bounciest ball!"
17. "Look again. Which row is the longest?"
18. "Every ball has a count. Tap Show the chart!"
19. "Which ball is the bounciest? Tap its row."
Which line when: after each drop, 12 to 15 for that ball, then 7, 8 or 9 (8 or 9 adds 10 when a missed or extra mark
falls after the 5th hit); an Again drop says 11 before the compare. Read speaks `#hint`.

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
- Bouncy ball e = 0.90, the 0.25 s cut-off and the 0.3 s matching window are the tool's own choices.

## Done when
1. Each ball's pad hits match the Content times to within one animation frame (log them) and the Counter shows 15,
   10, 6 and 1 on every drop, including Slow and Motion off.
2. Hand taps add marks at once; the timeline pairs taps and hits with the 0.3 s rule (check a scripted tap pattern
   by hand in Python), with missed and extra rings in the right places.
3. Compare lines 7, 8, 9 match the totals; 10 plays only when a miss or extra falls after the 5th hit.
4. The Our count stepper replaces the tap count and the compare uses it.
5. Bounciest Ball: the chart unlocks only after four Counter counts, rows have 15, 10, 6 and 1 dots, and the row taps
   give lines 16 and 17.
6. Again keeps up to three Me tries per ball and line 11 plays.
7. Every size in STANDARDS.md: hand button, Drop and counters visible without scrolling; 60 px targets at full screen.
8. Voice: welcome and how lines once each; the ball line and compare line on every drop; a new drop drops stale lines;
   Read and Sound rules pass with held clicks.
9. Keyboard (space, D, Tab) runs a full Bounciest Ball round; console clean.
