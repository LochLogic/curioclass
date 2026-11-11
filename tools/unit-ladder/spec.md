# Unit Ladder

## One idea
Beside a school track stands a tall ladder, and the child picks a unit set (feet and inches, yards and feet, meters and centimeters, kilometers and meters, kilograms and grams, pounds and ounces, liters and milliliters, or hours, minutes and seconds) and climbs against a ghost of their own last run: each rung asks for the next row of a two-column table (1 ft = 12 in, 2 ft = 24 in, 3 ft = 36 in), and later rungs skip ahead (7 ft = ? in) so the pattern, not counting, carries the climb; then it's track-meet day and the table comes along: relay legs are 400 m and the race is 2 km, so how many legs; one runner finishes in 3 min 45 s and the next in 228 s, so who was faster; a 4 L cooler fills cups of 250 mL, so how many cups; entry is $2.50 a runner, so what do four pay; half a kilometer is how many meters; and each problem is drawn on the track as a number line before the answer; at the end the child's tables and the meet results sit together, and the child sees that bigger units are bundles of smaller ones and that putting everything in the same unit solves the problem, so a fourth grader learns the relative sizes of units in one system, to record conversions in a two-column table, and to solve word problems on distance, time, liquid volume, mass and money on a number line.

## Not like
- kitchen-lab (3, spec): measuring and elapsed time. Here converting between units.
- fence-builder (3, spec): area and perimeter. Here unit sizes.
- seed-sprout-data (5, concept): conversions with line plots. Here conversion tables and word problems.
- community-plot-planner (4, spec): area and perimeter formulas. Here measurement conversions.

## Who and how
- Grade 4, Math, module "Measurement Conversions". Standards: 4.MD.1 (know relative sizes of measurement units within one system of units including km, m, cm; kg, g; lb, oz.; l, ml; hr, min, sec; within a single system of measurement, express measurements in a larger unit in terms of a smaller unit; record measurement equivalents in a two-column table), 4.MD.2 (use the four operations to solve word problems involving distances, intervals of time, liquid volumes, masses of objects, and money, including problems involving simple fractions or decimals, and problems that require expressing measurements given in a larger unit in terms of a smaller unit; represent measurement quantities using diagrams such as number line diagrams that feature a measurement scale).
- Format: race (against your own ghost, by rungs, with no clock). Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (written out in full, 2026-11-11): the ladder, the ghost, the eight unit sets and the eight meet problems stay. Now stated: the coach builds one table first as the model; every rung, compare card and meet problem is listed with its answer; the retry rule; the track marker is checked, not only the typed answer; eight "which is more" cards for relative size. The ghost no longer runs on time: it stands on the rung the child reached without a miss last run, because tools carry no timers. Added the three hooks: six items on your own with the end screen by code, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. Each unit name shows with its short form and a picture of something that size the first time it is used (a paper clip for a gram, a door for a meter). Meet problems use short sentences and no idioms.
- Eight unit sets of ten rungs, eight compare cards, eight track-meet problems drawn on the track, six items on your own. Extra: Class ghost (climb past the best class run). tool.json `modes: ["Ladder", "Class ghost"]`, `minutes: "30-40"` (two sittings is fine; sets are saved on the device), `grades_label: "Grade 4"`.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.MD.1 (express, record) | express a larger unit in terms of a smaller unit; record equivalents in a two-column table | the student | Type each next row of the table, then jump ahead by the pattern | 80 rungs over 8 unit sets (40 next rows, 40 jumps), 3 on your own | the child's table growing, units in words | 2, 6 |
| 4.MD.1 (relative sizes) | know relative sizes of units within one system | the student | After each table, say which of two measures in different units is more, and by how much | 8 compare cards | the two measures side by side, then both in the small unit | 3 |
| 4.MD.2 (solve) | use the four operations to solve word problems on distance, time, liquid volume, mass and money, with simple fractions or decimals, changing a larger unit to a smaller one | the student | Solve each meet problem and type the answer in the unit asked | 8 problems (2 distance, 2 time, 1 volume, 2 mass, 1 money; one with a fraction, one with a decimal), 3 on your own | the meet program filling in | 4, 6 |
| 4.MD.2 (represent) | represent measurement quantities on number line diagrams with a measurement scale | the student | Place the marker, or the hops, on the track scale before the answer box opens | 8 | the track as a number line in the small unit | 5 |

## Screens and modes
Header (kit): title "Unit Ladder"; `Ladder`, `Class ghost`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A tall ladder next to a school track, the child's climber at the bottom and a faint ghost climber. The welcome is queued (`welcomeAfter: true`): "Each rung is one more row of the table. Climb past your ghost. Tap a unit set to start." First hint: "Tap a unit set."

**The coach goes first (the model).** The coach builds a table for weeks and days, which is not one of the eight sets: "One week is seven days. Two weeks, two sevens, fourteen." She writes three rows, then jumps to 6 weeks: "I don't count up. Six sevens are forty-two." It cannot be skipped the first time and `Coach's table` reopens it.

**Climbing (focus: the table).** At 1366x768 the ladder fills the left with the table right; at 680x425 the table is a sheet over the ladder. The table has two columns headed with the unit names in words. Rungs 1 to 5 each ask for the next row, and the child types the small-unit number. Rungs 6 to 10 jump (7 ft = ? in). A right row adds a rung and the climber steps up. A wrong row can be tried once more with no hint; after a second miss the coach points at the rows above and says the rule ("each foot is twelve inches"), the row fills in tagged "coach helped", and one more jump rung with a new number is added at the top. The ghost stands on the highest rung reached without a miss last run. There is no clock.

**Which is more?** After each table, one card with two measures in the set's two units ("3 ft or 30 in?"). The child taps the greater one and types how much more, in the small unit. The table stays in view. One retry, then the coach changes both to the small unit and a second card of the same set is given.

**Track meet.** Eight problems, one at a time. The track runs along the bottom as a number line with a scale in the small unit of that problem (meters, seconds, milliliters, cents, grams, ounces, minutes). The child first shows the problem on the track: drags the finish marker to the total, or lays down equal hops, or marks two times. The marker must sit on the keyed point (to the nearest tick) before the answer box opens; a marker in the wrong place gets "Check the scale. What is each tick worth?" once, then the coach places it and tags the problem. The answer box names the unit it wants. A wrong answer gets one more try with the reminder "Put both in the same unit first"; after a second miss the coach works it on the track and a twin problem with new numbers is added at the end.

**Same unit (the aha).** After problem 2, the child's work shows 225 s against 228 s. Narrator: "Once both times were in seconds, the answer was easy. Bigger units are bundles of smaller ones."

**On your own.** Six items with the coach quiet: no tables in view, no track ticks filled in, no hints, one answer each. Nothing is marked until all six are in.

**The end.** The tables and meet results, and a results strip for the teacher: for 4.MD.1 and for 4.MD.2, how many of the three items on your own were right, in numbers and words, each item missed with the answer the child gave, and how many rows and problems were tagged "coach helped". `Print` prints them.

**Class ghost (extra).** The ghost stands where the best run on this device ended.

## Content
- All readable with `Read`. Only conversions inside one system; no metric to customary.
- The eight sets. Rungs 1 to 5 are 1 to 5 of the large unit. Jump rungs, large unit and answer:

| Set | One large unit | Jump rungs 6 to 10 |
|---|---|---|
| feet and inches | 12 in | 7 (84), 9 (108), 12 (144), 15 (180), 20 (240) |
| yards and feet | 3 ft | 8 (24), 12 (36), 25 (75), 40 (120), 100 (300) |
| meters and centimeters | 100 cm | 7 (700), 12 (1,200), 30 (3,000), 45 (4,500), 108 (10,800) |
| kilometers and meters | 1,000 m | 6 (6,000), 9 (9,000), 14 (14,000), 20 (20,000), 35 (35,000) |
| kilograms and grams | 1,000 g | 7 (7,000), 11 (11,000), 16 (16,000), 24 (24,000), 50 (50,000) |
| pounds and ounces | 16 oz | 6 (96), 8 (128), 10 (160), 12 (192), 20 (320) |
| liters and milliliters | 1,000 mL | 6 (6,000), 8 (8,000), 13 (13,000), 19 (19,000), 40 (40,000) |
| hours, minutes, seconds | 60 min; 60 s | 8 hr (480 min), 12 hr (720 min), then a second table: 2 min (120 s), 5 min (300 s), 10 min (600 s) |

- Which is more, with the answer and the gap: 3 ft or 30 in (3 ft, by 6 in); 5 yd or 16 ft (16 ft, by 1 ft); 4 m or 380 cm (4 m, by 20 cm); 2 km or 2,500 m (2,500 m, by 500 m); 3 kg or 2,900 g (3 kg, by 100 g); 2 lb or 30 oz (2 lb, by 2 oz); 5 L or 5,200 mL (5,200 mL, by 200 mL); 3 min or 200 s (200 s, by 20 s). The larger number is the greater measure on four cards and the lesser on four.
- Meet problems, with the track picture and the answer:
  1. Relay legs are 400 m and the race is 2 km. How many legs? (Hops of 400 on a 0 to 2,000 m line: 5.)
  2. One runner finishes in 3 min 45 s, the next in 228 s. Who was faster? (225 s and 228 s marked: the first, by 3 s.)
  3. A 4 L cooler fills cups of 250 mL. How many cups? (Hops of 250 to 4,000 mL: 16.)
  4. Entry is $2.50 a runner. What do four runners pay? (Four hops of 250 cents: $10.00.)
  5. The warm-up is half a kilometer. How many meters? (The halfway mark of 0 to 1,000 m: 500.)
  6. A shot put weighs 4 kg. How many grams? (4,000.)
  7. A 1 lb bag of trail mix is shared equally into 4 bags. How many ounces in each? (16 oz cut in four: 4.)
  8. The meet starts at 9:00 and runs 2 hr 30 min. When does it end, and how many minutes is that? (11:30; 150 min.)
- Twins for a second miss, same order: 300 m legs in 3 km (10); 2 min 50 s or 175 s (the first, 170 s); a 3 L jug into 500 mL bottles (6); $1.75 times 3 ($5.25); a quarter of a kilometer (250 m); 6 kg (6,000 g); 2 lb into 8 bags (4 oz); starts 1:15, runs 1 hr 50 min (3:05; 110 min).
- On your own, with what each common wrong answer means:
  - 4.MD.1: "9 ft = ? in" (108). A blank pounds and ounces table: fill the rows for 3 lb and 5 lb (48 and 80). "Which is more, 4 kg or 3,800 g?" (4 kg.) An answer of 21 means the child added 12 where each foot is a group of 12; 30 and 50 mean the child used tens for every unit; picking 3,800 g means the child compares the numbers and not the measures.
  - 4.MD.2: "A jug holds 3 L. The runners drink 1,800 mL. How many milliliters are left?" (1,200.) "Ana ran for 2 min 15 s. Ben ran for 140 s. Who ran longer, and by how many seconds?" (Ben, by 5.) "Ribbon costs $0.75 a foot. How much is 2 yards?" ($4.50.) An answer of 1,797 means the child subtracted without changing liters; Ana, or a gap of 75, means minutes and seconds were read as one number (215); $1.50 means the yards were never changed to feet.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Rungs, compare cards and meet answers follow the retry rule in Screens: one more try, then the coach, a "coach helped" tag and one more item of the same kind.
- The ghost counts rungs, never time. A pause of any length costs nothing.
- Keyboard: Tab to unit sets, the row box, the track marker and the answer box; arrows move the track marker one tick; Enter checks.
- Access: every action works by tap and by keyboard. The marker and hops can be dragged, or placed with a tap on a tick. The ghost is labeled "your last run" and tagged rows carry the words "coach helped", never color alone. Motion can be paused.
- On your own: one answer each, no feedback until the sixth is in.
- With Motion off the climber appears on each rung and the ghost shows as a rung number.

## Look
- Accent `--brand` #0f6466 track teal (header, the ladder rails, buttons); gold #f4c542 (the rung in hand, the finish line); paper #ecf6f6; ink #04201f; muted #4a5a5a.
- Contrast (WCAG 2.1, computed): white on brand 6.92:1; brand on paper 6.29:1; ink on paper 15.49:1; muted on paper 6.58:1; ink on gold 10.48:1.
- Never color alone: the ghost is labeled "your last run"; rows carry units in words.
- Different from this batch (craft-fair plum, brick orange, quilt navy, workbench olive).

## Art
- People (illustrated): two runners and a coach, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the track with the ladder (1, 16:9), the meet (1, 16:9).
- Drawn in code: the ladder, climbers, the table, the track number line.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as the coach; `news-reader` as the meet announcer and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.set + ':' + state.rung + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `rung`: "Type the next row of the table."
- how `skip`: "Use the pattern to jump ahead."
- how `more`: "Tap the one that is more. Then type how much more."
- how `track`: "Show it on the track first. Then type the answer."
- how `own`: "Six more on your own. No table this time."
- event `rule`: the coach's rule for the set, after a second miss.
- event, whole, the coach's table.
- event, whole, same unit.
- event, whole, `end`.
Every `how` line is also shown as text beside its control. Instructions use no idioms. Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: unit sets and tables, the ghost replay (kept on the device), the meet problems. The track scale uses `kit/number-line.js` as described in roller-coaster-rounding's spec.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Rungs | Count up by ones; retry until right | Jump rungs need the pattern (7 ft is 7 x 12), and a second miss tags the row and adds another jump. |
| Which is more | Tap the bigger number | On four of the eight cards the bigger number is the lesser measure, and the gap must be typed. |
| Meet | Answer in mixed units; type a number from the problem | The answer box asks for one stated unit, and no answer is a number printed in its problem. |
| Track | Skip the marker; drop it anywhere | The answer box opens only when the marker is on the keyed tick; a second miss is tagged. |
| On your own | Look at the tables; retry | The tables are closed, one answer each, nothing marked until all six are in. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). First set: the coach's table (whole), waits. `rung`; `skip`; `rule` as it fires.
2. `more` on the first compare card.
3. `track`.
4. Same unit (whole), waits.
5. `own`.
6. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.MD.1, 4.MD.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Customary equivalents: 1 ft = 12 in, 1 yd = 3 ft, 1 lb = 16 oz | NIST, Handbook 44, appendix C, "General tables of units of measurement" | NIST, Special Publication 811, "Guide for the Use of the International System of Units", appendix B | yes |
| Metric equivalents: 1 km = 1,000 m, 1 m = 100 cm, 1 kg = 1,000 g, 1 L = 1,000 mL | NIST, Special Publication 330, "The International System of Units" | BIPM, "The International System of Units (SI Brochure)", 9th edition | yes |
| A relay leg of 400 m is one lap of a standard outdoor track | World Athletics, "Track and Field Facilities Manual" | NFHS, "Track and Field and Cross Country Rules Book" | yes |
| Shot put for high school girls and women is 4 kg | World Athletics, "Competition and Technical Rules", implement specifications | NFHS, "Track and Field and Cross Country Rules Book" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s13, 2026-11-10): 7 ft = 84 in; 2 km over 400 m is 5 legs; 3 min 45 s is 225 s, faster than 228 s; 4 L over 250 mL is 16 cups; 4 x $2.50 = $10.00; half a kilometer is 500 m; 4 kg is 4,000 g; 16 oz over 4 is 4 oz; 9:00 plus 2 hr 30 min is 11:30; contrast as in Look.
Checks run for the full write-out (Python, 2026-11-11): every jump rung in the table (for example 108 x 100 = 10,800, 20 x 16 = 320, 12 x 60 = 720); compare gaps 36 - 30 = 6 in, 16 - 15 = 1 ft, 400 - 380 = 20 cm, 2,500 - 2,000 = 500 m, 3,000 - 2,900 = 100 g, 32 - 30 = 2 oz, 5,200 - 5,000 = 200 mL, 200 - 180 = 20 s; twins 3,000 / 300 = 10, 170 s under 175 s, 3,000 / 500 = 6, 3 x $1.75 = $5.25, 250 m, 6,000 g, 32 / 8 = 4 oz, 1:15 plus 1 hr 50 min is 3:05; on your own 108, 48, 80, 3,000 - 1,800 = 1,200, 140 - 135 = 5, 6 x $0.75 = $4.50; 2 hr 30 min is 150 min.

## Done when
1. Focus and fold: at 1366x768 ladder and table; at 680x425 table as a sheet.
2. Eight unit sets are climbed into two-column tables, five next rows and five jumps each; a second miss tags the row and adds a jump. (4.MD.1)
3. Eight "which is more" cards are answered with the gap in the small unit. (4.MD.1)
4. Eight meet problems are solved in the unit asked; a second miss brings its twin. (4.MD.2)
5. Each problem is shown on the track scale first, and the marker's place is checked. (4.MD.2)
6. Six items on your own run with no table, hint or filled ticks, one answer each; the end screen shows the result for 4.MD.1 and 4.MD.2 and the items missed.
7. The coach's table plays first and can be reopened.
8. The ghost counts rungs and the tool has no clock; the ghost stays on the device; runners are labeled illustration.
9. `Read` reads every card; every control is 48 px or more; every spoken instruction is also on screen, and each unit shows with a picture at first use.
10. Every action works by keyboard as well as tap, the marker has a tap way, nothing is shown by color alone, and motion can be paused.
11. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
12. Motion off: climbers appear on rungs; no network requests.

## Open questions
- The idea card moves 4.MD.3 (area and perimeter formulas) out of this tool (default used: 4.MD.3 is taught in community-plot-planner; this tool keeps 4.MD.1 and 4.MD.2).
