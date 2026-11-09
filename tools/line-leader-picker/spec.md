# Line Leader Picker

## One idea
The class writes a two-step rule card for picking the line leader, feeds it to a Turn Machine that follows it for a
pretend month of 20 school days, and the sticker chart shows at a glance that the same 20 friends get four very
different months: the rule a person chose decides who leads 20 times and who never leads at all.

## Not like
- three-route-rules (3-5, concept): route apps and travelers, outcomes for people with different needs. Here it is
  one familiar classroom job, turns counted with stickers, and a fairness check simple enough for K-2.
- robot-dance (K, built): the class follows a card sequence and watches Bolt do it. Here nobody acts the steps out:
  the rule runs for 20 days and the point is the month's result, not each step.
- snowy-mail-route (1, built): a swapped card sends Pip to a different stop (one run, one outcome). Here one changed
  step changes a whole month for 20 friends, and the change is about who is left out.
- sorting-showdown (9-12, spec): algorithm speed races. Here there is no speed; the outcome is people.
- question-jar (K-2, concept): sorts questions and asks who a data plan leaves out. Here the "left out" is a rule's
  outcome counted on a chart, not a survey plan.

## Who and how
- Grades K-2, computer science. Module: Fair Rules for Turns (Algorithms and Programming).
- Driver: teacher on a projector; the class answers out loud and a helper taps. Works for one child alone (every
  choice is a picture, every line spoken). tool.json: driver "teacher", minutes "10-20",
  modes ["Make a Rule", "Change a Step", "Is It Fair?"], grades_label "Grades K-2".
- Each mode leans on one grade's code (K, 1, 2), shown as a small grade tag on the mode button; any mode works for
  any grade.
- Standards (CSTA 2026): EK-ALG-IM-03 (describe how people create algorithms to solve problems), E1-ALG-IM-03
  (explain how a change to an algorithm leads to a different outcome), E2-ALG-IM-03 (describe how an algorithm might
  impact peers in varied situations). The E2 boundary statement uses this very case (drawing line-leader names from a
  bucket) and lists the three checks this tool uses. It also says grade 2 is not expected to design fixes, so the
  idea card's "build a new rule from parts" for grade 2 is replaced by the fairness check plus Bee's sick-day month.
- No personal prompts: the feelings lines are about the animal classmates. Nothing is stored or sent.

## Standards map
| Code | Student action | What they see | Done when |
|---|---|---|---|
| EK-ALG-IM-03 | Make a Rule: hear the job ("pick a line leader every day"), choose step 1, then step 2, tap Run, then answer "Who made this rule?" | the rule card fills step 1 then step 2; on day 1 the Turn Machine lights step 1, then step 2; a "Made by our class" stamp lands on the card | Run is disabled until both steps are chosen; step 2 tiles show only after step 1; after the first month the Who question appears and either answer ends with the line that people made the rule and the stamp |
| E1-ALG-IM-03 | Change a Step: start from last month (first in line, stays at the front: Ant 20, 19 friends 0), change one step, Run, then tap the step that made the month change | dashed "Before" outlines stay behind the new stars on every column; the compare line; the changed step glows | changing "stays at the front" to "goes to the back" turns Ant 20 / nineteen 0 into twenty 1s with the Before outlines still visible; the Which step prompt accepts only a changed step |
| E2-ALG-IM-03 | Is It Fair?: for each of four rules, answer three picture checks from the chart (same chance? anyone left out? someone led more than once while a friend got none?), then make their own Fair / Not fair call and tell a friend why; turn on Bee's sick day and check again | evidence on the chart for each check (rings on zero columns, the tallest column marked); the summary board of all four rules; Bee in bed on day 2 | the draw-and-put-back rule shows "same chance: yes" and "left out: yes" together with the same-chance line; with Bee sick, "goes to the back" gives Bee 0 and Ant 2 and plays the situation line; the verdict is never marked right or wrong |

## Screens and modes
Header (kit): title "Line Leader Picker"; mode buttons with icons and grade tags: "Make a Rule" (pencil on card, K),
"Change a Step" (two arrows swapping, 1), "Is It Fair?" (balance scale, 2); Motion, Sound, Read.

Stage (all modes), top to bottom, drawn at real pixel size and re-laid per size:
1. Day strip: at the left the classroom door (part of the painted wall) with the Leader spot, where today's leader
   cutout stands under a small code flag "Leader". To its right, the calendar: 20 day squares in 4 weeks of 5
   (labels "Week 1" to "Week 4", days numbered 1 to 20). A finished day shows the leader's face (small crop of the
   cutout, 40 px).
2. Sticker chart (the focus): 20 columns in ABC order, one per classmate. Each column stacks gold star stickers, 10
   per column of stars, wrapping into a second column of stars from 11 to 20, with the count as a big number above
   (0 shows as "0"). Columns with 0 at the end of a month get a dashed ring.
3. Class row: the 20 classmate cutouts under their columns (60 x 80 px at 1366), each a button. After a full month a
   friend with 0 shows the waiting (droopy) pose; everyone else the happy pose.
Bottom band: the Turn Machine (painted) holding the rule card (code card over its blank slot): the job line at top
with a door-and-flag icon, then slot "1" and slot "2", each with two picture tiles (96 x 96); beside it the run
buttons: Run (play; becomes Pause while running), One day (single step), To the end (fast forward), New month
(circle arrow); and the hint line. Jar and done tray (painted) sit beside the door in jar rules only.

On load: Make a Rule, slots empty ("?" tiles), chart empty with all happy poses, nothing plays (nothing speaks before
the first tap). Hint: "Every day, one friend leads the line. People make the rule that picks the leader. Tap a
picture for step 1." The first tap on a step-1 tile chooses it and speaks its name (the welcome is skipped, BASELINE
16); the job premise stays in the hint and Read and in the "who" line later. First tap on a classmate: their name
and "has not led yet". First tap on a mode button: that mode's welcome.

### Make a Rule (K)
- Focus: the rule card while choosing, then the sticker chart while the month runs.
- Step 1 tiles: "First in line" (code icon: a row of dots, the front dot ringed, the door) and "Draw a name" (painted
  jar). Step 2 tiles appear after step 1: for First in line, "Stays at the front" (arrow curling back to the front)
  and "Goes to the back" (arrow from the front to the end of the row); for Draw a name, "Name goes back in" (slip with
  an arrow into the jar) and "Name stays out" (slip landing on the tray). Changing step 1 clears step 2.
- Run is disabled until both steps are chosen. The run buttons do nothing visible until then; the hint never names
  them.
- After the first finished month in this page load, an overlay card on the chart center asks "Who made this rule?"
  with two 120 px picture buttons: Turn Machine (cutout) and Our class (the 20 faces in a small group). Either answer
  stamps "Made by our class" on the rule card (stays until the rule changes), then the hint becomes the try-another
  line. The overlay never blocks the class row; Close (x) dismisses it unanswered.
- 1366x768: header 56, day strip 72, chart 260, class row 84, bottom band 200: all above the fold.
- 680x425: day strip folds to a "Day 7 of 20" chip and the door spot; chart and class row become two banks of 10
  columns; bottom band becomes a compact side panel (tiles 56 px, buttons icon-only with labels as tooltips).

### Change a Step (1)
- Opens with last month already on the chart (no animation): rule First in line + Stays at the front, Ant 20, all
  others 0 in the waiting pose. Hint: welcome line below.
- Tapping any tile changes the rule; the current stars turn into dashed "Before" outlines and the chart clears. Run
  plays the new month over the outlines. When it ends: the compare line, then "Which step made the month change? Tap
  that step." A changed tile glows when tapped. Tapping an unchanged tile gets the "stayed the same" line.
- Each new change makes the last shown month the new "Before".
- Focus: the chart, with Before and now side by side in every column. Layout as Make a Rule.

### Is It Fair? (2)
- Day strip is replaced by a row of four rule cards (each shows its two step pictures, 300 x 72): A First in line +
  Stays at the front; B First in line + Goes to the back; C Draw a name + Name goes back in; D Draw a name + Name
  stays out. At its right, the Bee switch: "Bee is home sick on day 2" (picture of Bee in bed; on/off).
- Tapping a card plays that rule's month at To-the-end speed (stickers pop in over about 1.5 s; instant with Motion
  off apart from the pop). The day strip is not shown here; the calendar result is in the chart.
- Bottom band: three check chips across, each a picture question with thumbs up / thumbs down (60 px):
  Q1 "Same chance for every friend?" (four equal circles), Q2 "Was any friend left out?" (one dim face among bright
  ones), Q3 "Did someone lead more than once while a friend got none?" (a tall stack beside an empty one). Each
  answer shows the evidence (below), then a verdict pair "Fair" (thumbs up, green) / "Not fair" (thumbs down, red,
  also a cross icon) and New month (draw rules only). An "Our chart" button opens the summary board over the chart:
  rows A to D (and A to D with Bee sick, once used), columns Q1, Q2, Q3 (yes / no icons from the data) and the
  student's verdict (blank until given).
- Focus: the chart; the evidence is drawn on it.
- 1366x768: header 56, rule row 80, chart 260, class row 84, checks band 180. 680x425: rule cards become 4 icon
  buttons, checks become icon-only chips in a side panel.

## Content
Classmates (ABC order, t-shirt color, so faces differ at button size): Ant (red), Bee (yellow), Cat (orange),
Duck (teal), Elephant (purple), Fox (green), Goat (navy), Hippo (pink), Iguana (lime), Koala (sky blue), Lion
(maroon), Mouse (gold), Owl (brown), Pig (aqua), Rabbit (lavender), Sheep (coral), Turtle (olive), Wolf (gray),
Yak (cream with blue stripes), Zebra (bright blue). Bee is "she"; no other pronouns are used.

Rules (a rule = step 1 + step 2; the month is 20 school days; the line starts in ABC order; the jar starts full):
| Rule | Each day | Normal month | Bee sick on day 2 |
|---|---|---|---|
| A First in line, stays at the front | the first present friend in line leads; the line does not change | Ant 20, nineteen 0 | same |
| B First in line, goes to the back | the first friend in line leads, then walks to the back; a sick friend at the front also goes to the back (the turn passes) | everyone 1, Ant to Zebra | Bee 0, Ant 2 (day 20), everyone else 1 |
| C Draw a name, name goes back in | draw one name from all 20; it goes back; a sick friend's name: draw again | random; about 7 friends 0 on average (3 to 12 in practice), most 3 | random, Bee may still lead later |
| D Draw a name, name stays out | draw from the jar; the name goes on the tray; a sick friend's name goes back in, draw again; refill when empty (never within 20 days) | everyone 1, random order | everyone 1, Bee always gets a turn |

Check evidence (Q1 is the rule's own fact; Q2 and Q3 read the month's counts):
- Q1: A no; B, C, D yes. Q2: yes when any column is 0 (rings the zero columns). Q3: yes when a column is 2 or more
  and a column is 0 (marks the tallest and rings the zeros).

## Interactions in detail
- Run: 20 days at 450 ms a day (9 s). Each day: the Turn Machine lights step 1 (the tile's border pulses), the leader
  cutout slides to the Leader spot (jar rules: a blank paper slip pops from the jar and the name is written on it in
  code), step 2 lights (the slip goes back into the jar or onto the tray; line rules: the leader walks to the front or
  the back, shown by the code row of dots under the door), a star flies to the leader's column, the day square fills.
  Day 1 in Make a Rule runs at 1200 ms so the two steps are seen in order; later days at 450 ms.
- Every control stays live while a month plays: Pause stops at the end of the current day's animation (under 450 ms)
  and shows Run; One day pauses and plays exactly one day; To the end fills the rest at once (stars pop); New month
  clears and starts day 1 with the same rule; tapping a tile stops the run, clears the month (Change a Step keeps
  Before) and shows the new rule; a mode switch stops everything (V.hush); the Bee switch or a rule card in Is It Fair?
  replaces the month at once. Tapping a classmate mid-month speaks their count so far.
- Draws use Math.random; `__tool.seed(n)` makes them repeatable for tests. If a draw month ever has no zero column
  (about 2 in 100 million), the lines and checks follow the data ("Everyone got one turn.").
- Classmate tap: name, then "led n times" (or "never led this month" at the end of a month, "has not led yet" before
  it ends), then for 0 at month end the left-out line, for 3 or more the lots line, for Bee with 0 in a sick month the
  sick line first. A new tap drops the older tap's lines that have not started.
- Is It Fair? answers: a thumb that matches the data gets "The chart agrees." plus the evidence line; one that does not
  gets "Look at the chart again." plus the same evidence; either way the evidence shows and the next chip opens. No
  points, no score. The verdict is the student's: both buttons speak "You said ... Tell a friend why." and fill the
  summary.
- Reset: mode switch keeps each mode's state for the page load; New month resets the month only. Nothing is saved.

## Look
- Accent `--brand #1d6b3a` (leaf green; white text on it 6.53:1). Paper `#fbf6ea`, ink `#2a2320` (14.32:1), muted
  `#6b5d52` (5.88:1), star gold `#f2b705` with ink outline and ink count numbers (8.5:1 on gold), Before outline
  `#1f4fbf` dashed (6.65:1 on paper), zero ring `#b8441f` dashed (white on it 5.41:1). Different from neighbors
  (robot-dance magenta, snowy-mail-route red, computer-builder and teach-the-robot blues).
- Fair green and Not fair red always carry thumb icons (and a cross on Not fair), never color alone.
- Scene: warm wood door, cream wall, cork board behind the chart, soft morning light.

## Art
All local model (no people). One flat, friendly children's-book style for every classmate; same scale and ground line.
- classroom-wall: a sunny classroom wall with a wooden door at the left, a wide blank cork board across the middle,
  a low bench along the bottom; 16:9; no cutout; stage backdrop (cover, door kept at left).
- 20 classmates x 2 poses (40 cutouts), each "a cartoon kid-sized [animal] classmate in a [color] t-shirt, full body,
  standing": pose happy (smiling, upright) and pose waiting (sitting on the floor, chin on hands, droopy ears or head);
  3:4; cutout yes; class row, Leader spot, calendar face crop. Whole body inside the frame with margin (elephant
  ears included); the face sits in the top third so the 40 px crop works.
- bee-sick: the Bee classmate in yellow pajamas tucked in a small bed with a blanket; 4:3; cutout yes; Bee switch and
  Bee's column on day 2.
- turn-machine: a friendly wooden and brass box machine with a big blank card slot on the front, a side crank and two
  round lamps; 4:3; cutout yes; holds the rule card; also the Who button picture.
- jar-full / jar-half / jar-empty: a clear glass jar with folded blank paper slips (full, half, two slips); 3:4;
  cutout yes; jar rules (D drains it; C stays full).
- done-tray: a small wooden tray with a few folded blank paper slips; 4:3; cutout yes; rule D.
- Drawn in code: stars, chart, calendar, rule card, step-tile icons, slips, flag, rings, Before outlines, thumbs.

## Voice
Bank voice `friendly-dad` (Achird): "Say in a relaxed, friendly way, like a kind dad helping with homework". K-2 CS
neighbors use lively-host, bright-teacher, big-sister, warm-teacher, curious-librarian, playful-friend, hero-coach,
knowing-guide and gentle-storyteller. A calm, fair-minded voice for a talk about turns.
Every line below is fixed; numbers and names are their own clips joined as sequences (V.say list).

How (spoken once, then hint only):
- wMake (welcome, Make): "Every day, one friend leads the line. People make the rule that picks the leader. Tap a
  picture for step 1." Stale when step 1 is chosen.
- step2: "Step 2 says what happens after a turn. Tap a picture for step 2." When step 1 is chosen. Stale when step 2 is.
- runReady: "Our rule is ready. Tap Run to play a month of school." needs #run. Stale when a run starts.
- machine: "The Turn Machine does just what our card says." On the first Run. Stale when the month ends.
- who (whole): "Who made this rule? Tap the Turn Machine, or tap Our class." With the overlay. Stale when answered.
- another: "Make a new rule. Tap a picture in step 1 or step 2." After the who answer.
- tapFriend: "Tap a friend to hear how many turns they had." After the first month-end result, any mode.
- wChange (welcome, Change): "Last month, first in line stayed at the front. Change one step, then tap Run." Stale
  when a step changes.
- chRun: "You changed a step. Tap Run to see the new month." needs #run.
- chWhich (whole): "Which step made the month change? Tap that step." After the compare line.
- wFair (welcome, Fair): "Let's check four rules. Tap a rule card to see its month." Stale when a card is tapped.
- fChecks: "Look at the chart. Tap thumbs up or thumbs down for each question." After the first month shown.
- fVerdict: "Is this rule fair? Tap Fair or Not fair. Then tell a friend why." After the third check.
- fNext: "Tap another rule card, or turn on Bee's sick day." After the first verdict.
- fSame (teaching): "The same chance is not the same as a turn for everyone." Rule C, after Q2 shows zeros.
- fBeeB (teaching, whole): "Last month this rule gave everyone a turn. This month Bee was sick on her day, so the same
  rule left Bee out." Rule B with Bee sick, after the month.
- fBeeD (teaching): "Bee's name went back in the jar on her sick day, so Bee still got a turn." Rule D, Bee sick.
- fSummary: "Here are all four rules. Which one would you pick for our class?" When Our chart first opens.

Events (spoken each time, dropped when stale):
- Tiles, on tap: "First in line leads." / "Draw a name from the jar." / "The leader stays at the front." / "The leader
  goes to the back of the line." / "The name goes back in the jar." / "The name stays out of the jar."
- Month result (whole; Run and One day wait for it): "The month is done." then [name] + "led the most: n times." or
  "Some friends led n times each." (tie, n 2 to 8), unless all 1; then "One friend never got a turn." /
  "n friends never got a turn." (n 2 to 19) / "Everyone got one turn."
- Names (20 clips): "Ant." to "Zebra."
- Counts: "led one time." "led two times." to "led twenty times."; "never led this month."; "has not led yet."
- left: "That friend waited all month and never led. Being left out feels sad." lots: "That is a lot of turns!"
  beeSick: "Bee was home sick on her turn day."
- whoClass: "Yes! People made the rule. The Turn Machine just follows it." whoMachine: "The Turn Machine only
  follows the card. You chose the steps, so people made the rule."
- chCompare: "One step changed, and the whole month changed." chYes: "Yes. Changing that step changed who got a
  turn." chSame: "That step stayed the same. Look for the step you changed."
- Q1 per rule: A "Only the friend at the front can lead. The others never get a chance." B "Everyone gets a turn,
  one after another." C "Every name is in the jar every day, so everyone has the same chance." D "Every name gets
  drawn once before any name goes back."
- Q3: "One friend led more than once while a friend got none." / "No one led twice while a friend got none."
- agree: "The chart agrees." look: "Look at the chart again." fair: "You said fair. Tell a friend why." notFair:
  "You said not fair. Tell a friend why."
Repeats: tile and classmate lines play per tap (newer drops older unstarted); no line plays per day during a run.

## Family engine
none

## Sources
Claims table:
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Standard wording and the E2 line-leader example | 2026 CSTA PK-12 Computer Science Standards PDF, p. 44 to 45 (csteachers.org/2026-csta-pk-12-computer-science-standards, CC BY-NC-SA 4.0) | docs/agents/gapfill/cs/notes.md row (read from the same PDF; not independent) | yes |
No real-world fact is shown on screen: the class, month and Turn Machine are pretend. Rule C's "about 7 of 20" is a
computed result for teacher notes only (exact formula 20 x (19/20)^20 = 7.17 and simulation agree).
Number checks run (Python, S:/CurioClass-codex-scratch/specs/line-leader-picker/check.py, contrast.py):
- Names are 20, unique, in ABC order. Rule A: Ant 20, 19 zeros (normal and Bee sick). Rule B: all 1, days Ant to
  Zebra; Bee sick: Bee 0, Ant 2 (days 1 and 20). Rule D: all 1 in 100,000 sick months, Bee never 0.
- Rule C, 100,000 months: mean zeros 7.17 (exact 7.17); zeros from 2 to 13, exact P(3 or more) = 0.9998; the most
  turns 2 (12%), 3 (58%), 4 (24%), up to 8; every friend exactly once: 2.3 in 100 million.
- Checks through wrong behaviors: no score exists, so doing nothing, mashing thumbs or always "Fair" earns nothing;
  evidence shows whatever was tapped. Q2 and Q3 read data, so a lucky Rule C month is never called unfair by the tool.
- Contrast ratios listed in Look (WCAG AA all pass).

## Done when
1. Focus: in every mode at 1366x768 the sticker chart is the largest element, centered, with counts readable.
2. Fold: at 1366x768 the class row, both rule slots and every run or check button are above the fold; at 680x425 the
   compact layout shows all 20 faces and the controls without page scroll.
3. Make a Rule: Run is disabled until both steps are chosen; day 1 lights step 1 then step 2; the Who overlay appears
   after the first month and stamps "Made by our class" (EK).
4. Change a Step: stays-to-back change turns Ant 20 / nineteen 0 into twenty 1s over dashed Before outlines; the
   compare line plays; the Which step prompt accepts only a changed tile (E1).
5. Is It Fair?: rule C shows Q1 yes and Q2 yes with the zero columns ringed and the same-chance line; rule A shows Q1
   no; with Bee sick, rule B shows Bee 0, Ant 2 and the Bee line; verdicts are never marked right or wrong (E2).
6. Tap while playing: during a run, a tile tap stops it and clears the month at once; a classmate tap speaks their
   count so far; Pause, One day and To the end act within one day's animation.
7. Pre-readers: every tile, check and verdict is a picture and every question and choice is spoken.
8. The month result plays whole and Run waits for it; no line plays per day during a run.
9. Five taps on tiles 2 s apart: each tile name is heard; the step2 and runReady how lines are spoken once only.
10. Motion off: no sliding or flying, same day pacing (1200 ms day 1 in Make a Rule, then 450 ms), stars appear in place.

## Open questions
none
