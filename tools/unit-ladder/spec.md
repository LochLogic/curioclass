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
- Format: race (against your own ghost). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight unit sets, ten rungs each, the two-column table, eight track-meet problems drawn on the track. Extra: Class ghost (race the best class time instead of your own). tool.json `modes: ["Ladder", "Class ghost"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.MD.1 (sizes, tables) | Climb rungs by writing the next row; skip ahead by the pattern | the two-column table growing | 2 |
| 4.MD.2 (problems) | Solve meet problems in one unit | the answer in the meet program | 3 |
| 4.MD.2 (number lines) | Mark each problem on the track before answering | the track as a measuring scale | 4 |

## Screens and modes
Header (kit): title "Unit Ladder"; `Ladder`, `Class ghost`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A tall ladder next to a school track, the child's climber at the bottom and a faint ghost climber. The welcome is queued (`welcomeAfter: true`): "Each rung is one more row of the table. Beat your ghost to the top! Tap a unit set to start." First hint: "Tap a unit set."

**Climbing (focus: the table).** At 1366x768 the ladder fills the left with the table right; at 680x425 the table is a sheet over the ladder. Each rung asks for the next row; a right row adds a rung and the climber steps up. Rungs 6 to 10 skip (7 ft = ? in). The ghost climbs at the pace of the last run; no penalty for slow, just a race.

**Track meet.** Eight problems, each first marked on the track as a number line with a scale:
1. Relay legs of 400 m in a 2 km race: how many legs?
2. 3 min 45 s against 228 s: who was faster?
3. A 4 L cooler, 250 mL cups: how many cups?
4. Entry is $2.50 a runner: what do four runners pay?
5. Half a kilometer is how many meters?
6. A shot put weighs 4 kg: how many grams?
7. A 1 lb bag of trail mix shared in 4 equal bags: how many ounces each?
8. The meet starts at 9:00 and runs 2 hr 30 min: when does it end?

**Same unit (the aha).** After problem 2, the child's work shows 225 s against 228 s. Narrator: "Once both times were in seconds, the answer was easy. Bigger units are just bundles of smaller ones."

**The end.** The tables and meet results. `Print` prints them.

**Class ghost (extra).** Race the class's best time.

## Content
- Eight unit sets with true equivalents, ten rungs each, eight meet problems, all readable with `Read`.
- Only conversions inside one system; no metric to customary.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A wrong row shows the pattern of rows above and asks again; the ghost keeps climbing.
- Keyboard: Tab to unit sets, the row box, the track marker and the answer box; arrows move the track marker; Enter checks.
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
- how `track`: "Drag the marker on the track, then type the answer."
- event, whole, same unit.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: unit sets and tables, the ghost replay (kept on the device), the meet problems. The track scale uses `kit/number-line.js` as described in roller-coaster-rounding's spec.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Rungs | Count up by ones | Skip rungs need the pattern (7 ft is 7 x 12). |
| Meet | Answer in mixed units | The answer box asks for one stated unit. |
| Track | Skip the marker | The answer box opens after the marker is placed. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `rung`; `skip`.
2. `track`.
3. Same unit (whole), waits.
4. `end` (whole).

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

## Done when
1. Focus and fold: at 1366x768 ladder and table; at 680x425 table as a sheet.
2. Eight unit sets are climbed into two-column tables, with skip rungs. (4.MD.1)
3. Eight meet problems are solved in one unit. (4.MD.2)
4. Each problem is marked on the track number line first. (4.MD.2)
5. `Read` reads every card; every control is 48 px or more.
6. The ghost stays on the device; runners are labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: climbers appear on rungs; no network requests.

## Open questions
- The idea card moves 4.MD.3 (area and perimeter formulas) out of this tool (default used: 4.MD.3 is taught in community-plot-planner; this tool keeps 4.MD.1 and 4.MD.2).
