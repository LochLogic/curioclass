# Fixes: science course frames, grades 3 to 5, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-science-grade-<n>-2026-11-14.md`) and the Codex reads to the grade 3, 4 and 5
frames and `data/progressions/science.csv`. Grade 3's Codex read is the rerun
(`frame-science-grade-3-codex-rerun-2026-11-14.md`, numbered as in that file); the first grade 3 Codex read was
withheld over a gate failure and is superseded by it. Every expert finding and every "Settled by the expert" row is
applied, except one settled row whose file is outside this pass (the C3 column rename in the frame-write brief),
which goes to "For the lead". Each Codex finding was weighed on its merits.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check science-grade-3
science-grade-4 science-grade-5` 0 failures each; `scripts/plan.py check` exit 0, its science progression gate 198
rows, 0 failures; `scripts/stale.py check` 56 files, 0 failures. No unit, skill or standard moved; every course
keeps 6 units and 120 days (111 in units, 9 at course level).

Applied in all three frames: the paper path and no-student-account line in Materials; the year named in the K to 2
form ("across 30 weeks (a school year of about 36 weeks, of which about 30 carry science lessons here)"); the math,
ELA and social studies calendars now cite the Curio Class frames' own units and day ranges, each "if later" cell
saying whether its bridge is used; a "No math ahead of math, later grades" line under each Cross-subject table;
"For the lead" items that are now settled or applied rewritten or dropped.

## Grade 3

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 4 anchor "no rainforest tree frog or cactus could live there"; the Arctic case is the polar bear (survives well), the wood frog (survives by freezing solid in winter) and a rainforest tree frog (cannot survive), linked back to ELA grade 3's frog unit; s3-habitat-survival notes changed |
| Expert | 2 | Applied | Unit 3 anchor: seedlings from one packet plus one kind of hydrangea, blue in one garden and pink in another (soil decides); the class test varies crowding; grade 2's light-and-water test retrieved in one opening task, not rerun; Seams row and s3-environment-traits notes changed |
| Expert | 3 | Applied, merged with Codex 3 | Brief "Planting day" bullet: science day 18, about 15 minutes, fast-cycling plants under a lamp, crowding pots, late-stage mealworms; named in unit 2's notes and unit 3's anchor and reason; s3-life-cycles notes |
| Expert | 4 | Applied | Unit 6: climates in words, maps and counts, no temperature below zero graphed; the log records "below zero" in words (brief); unit 4: hunting success as counts out of 10 on a bar graph, no percent; math leans added to s3-animal-groups and s3-climates |
| Expert | 5 | Applied | Unit 2 electromagnet as a teacher demonstration (no student circuit); unit 5 adds the warmed stream (temperature) and the spreading plant (other organisms); unit 4 adds the mates case; rows s3-magnet-static, s3-environment-change-solution, s3-variation-advantage |
| Expert | 6 | Applied | Paper path and no-student-account line |
| Expert | 7 | Applied | 3.MD.B.4 and 3.MD.A.2 now "math grade 3 unit 7 (about school days 117 to 133)"; 3.MD.B.3 math unit 1 (days 1 to 22) |
| Expert | 8 | Applied | Grade 2's Handed on row for s3-design-problem now reads need, criteria and constraints (3-5-ETS1-1), comparing several solutions grade 4, fair tests of a prototype grade 5; s2-compare-designs notes say the same. Weeks: grades 3 to 5 now name the year in grade 2's form, so the two counts read as one year |
| Expert | 9 | Applied | Unit 6 anchor: a weather warning "this year or last", from the National Weather Service county record if needed |
| Expert | settled | Applied, one row for the lead | Eight rows applied; the C3 rename touches docs/pipeline/briefs/frame-write.md, outside this pass: "For the lead" |
| Codex rerun | 1 | Applied, merged with expert 1 | Kept the expert's settled anchor wording (true as written); took Codex's caution: each organism judged from needs, characteristics and conditions, never its group, and the wood frog not labelled "survives less well" because its trait is special |
| Codex rerun | 2 | Applied in part | Electromagnet, mates and the two unit 5 cases as expert 5; added the changing-needs element of 3-5-ETS1-1 (a changed user need changes the latch's criteria) and a sourced, non-universal mates case. Rejected: an element-to-unit record in the frame; the element check already sits with the scope and sequence ("For the lead" 3) |
| Codex rerun | 3 | Applied, merged with expert 3 | Supplier timing recorded as the source; radishes only in the crowding test (not relied on to set seed); a dated photograph sequence covers missed stages; the class record marks seen against learned stages |
| Codex rerun | 4 | Applied | As expert 4, with equal-trial counts |
| Codex rerun | 5 | Applied | "For the lead" 1 now shows the arithmetic: 3 lessons a week give 90, 15 compressible days leave 105, no 90-lesson path exists, none made by cutting standards or checks. Same correction made in grade 4's item 1 |
| Codex rerun | 6 | Applied | Math and ELA units named; the three row changes applied; the math frame's own bridges already agree (checked) |
| Codex rerun | 7 | Applied | As expert 9 |
| Codex rerun | 8 | Applied | Paper path keeps the question and reasoning; tool days name a single-projector arrangement |
| Codex rerun | 9 | Applied | As expert 8 |
| Codex rerun | 10, 11 | Not acted on here | docs/RUBRIC-SCIENCE.md is outside this pass: "For the lead" with Codex's text |
| Codex rerun | 12 | Already met | Math grade 3's Cross-subject lead-in already names the science frame as written (checked, not edited) |
| Writer | lead 3 | Applied | Row changes for 3.MD.B.4 and 3.MD.A.2 (with real math unit timing) |
| Writer | lead 1, 5 | For Cory | Time a week; materials ceiling |

Conflict, Codex against expert on unit 3's anchor: Codex judged reusing grade 2's plant evidence defensible and the
hydrangea unnecessary. The expert's settled pick stands (not re-decided): grade 2's test is retrieved as review and
the new phenomenon is one grade 2 did not explain.

Counts: applied 18 (expert 1 to 9, Codex 1 to 9; Codex 2 in part), rejected 1 (part of Codex 2), not acted on 2
(Codex 10 and 11, outside this pass), already met 1 (Codex 12), for Cory 3.

## Grade 4

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 3: sound on a slinky pushed and pulled along its length, beside the rope or water wave, no wave-type names; amplitude and wavelength stay on rope and water; s4-wave-model notes |
| Expert | 2 | Applied | Unit 2: state energy data as an ordered bar or picture graph, "of every 10", no percent, no number over 1,000,000; unit 4: water in equal cupfuls until math grade 4 unit 6; s4-energy-resources and s4-weathering-erosion cross_subject |
| Expert | 3 | Applied | 4.OA.C.5 math unit 7 (school 97 to 111), bridge used unconditionally; 4.OA.A.3 unit 8 (with unit 6's two-step problems), 4.G.A.1 unit 9, 4.MD.A.1 unit 6 |
| Expert | 4 | Applied | Paper path line |
| Expert | 5 | Applied | Cross-subject paragraph states ELA grade 4 unit 2 teaches the structures its texts need; "For the lead" 2 rewritten as settled |
| Expert | 6 | Applied | Unit 4 anchor: a small river at the bottom of a canyon a mile deep, the same stripes on both walls; shells met in the lessons after a retrieval task on grade 3's fossils |
| Expert | settled | Applied | All five rows |
| Codex | 1 | Applied | Unit 6: a required internal plant case (an adult-cut celery or white flower stem in colored water), the flower dissection now required (new candidate: a fruit cut open), one plant and one animal argument in the unit task; Check 3 asks for one unseen animal and one unseen plant; s4-structures-function notes |
| Codex | 2 | Applied | Unit 3 and the brief's Design work: research and one reading before designing, at least two codes, proposals shared, the same message tested under two conditions, accuracy and one other measure recorded, compared on the data; the prototype fair test stays grade 5's; s4-information-codes notes. Days kept (both readers keep 120); the unit's note asks the scope and sequence to set it inside 15 days |
| Codex | 3 | Applied | Unit 3: waves of different amplitude and wavelength compared and the cork's motion explained by a revised model; Check 2's wave clause replaced with Codex's text |
| Codex | 4 | Applied | As expert 3; the budget and ruler row changes applied |
| Codex | 5 | Applied | Unit 5 opens with a grade 2 review reading a map of ice-covered areas; Seams row and s4-earth-feature-maps notes |
| Codex | 6 | Applied | As expert 5 |
| Codex | 7, 8 | Not acted on here | docs/RUBRIC-SCIENCE.md: "For the lead" |
| Codex | 9, 10, 11 | Not acted on here | docs/reviews/progression-science-fixes-2026-11-13.md and progression-science-2026-11-13.md: "For the lead" |
| Codex | settled | Applied | All seven rows |
| Writer | lead 4 | Applied | Row changes for 4.OA.A.3 and 4.G.A.1 with math's real units |
| Writer | lead 1, 6 | For Cory | Time a week; materials ceiling |

No conflict: the two reads agree on every shared point.

Counts: applied 12 (expert 1 to 6, Codex 1 to 6), rejected 0, not acted on 5 (Codex 7 to 11, outside this pass),
for Cory 3.

## Grade 5

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied, merged with Codex 2 | Brief: pots set up in the first week, soil dried and weighed dry, plant and dried soil weighed at the end of unit 2 (about science day 41); set-up day named in unit 1's notes; unit 2 and s5-plant-matter |
| Expert | 2 | Applied, merged with Codex 4 | Unit 5: two hundred-square grids and two bar graphs, all water (97 and 3) then fresh water as its own 100 (69 ice caps and glaciers, 30 ground water, 1 lakes, rivers and swamps); s5-water-distribution |
| Expert | 3 | Applied | Star distances as light travel time plus the grain-of-sand scale model, no number over 1,000,000; s5-star-brightness cross_subject and notes; the Handed on row |
| Expert | 4 | Applied | Math units 8, 8, 10 and 9 named; the line-plot "if later" as the expert wrote it |
| Expert | 5 | Applied | Paper path line |
| Expert | 6 | Applied, merged with Codex 1 | Quarter teaspoon and tablespoon; open bottle as the comparison |
| Expert | 7 | Applied | Shadow at the same sun time each month (brief, unit 4 anchor, s5-shadows-sky) |
| Expert | settled | Applied | All seven rows, including the frozen-bag cooling case and "lost less than a pound" |
| Codex | 1 | Applied in part | Kept the expert's settled small-amount balloon test (quantitative), since a barely filled balloon displaces too little air to move a gram scale; applied Codex's sentence (compare the whole system, investigate a difference rather than assume escaped gas) and a teacher note on why the amounts stay small; "loose cap" dropped from the sealing rule. Rejected: removing the balloon from the quantitative sequence |
| Codex | 2 | Applied | A supplied, sourced comparison of plants grown with more of the gas plants take in from air; the history told as evidence against soil whose water-only conclusion later evidence corrected (unit 2, brief "How science works", s5-plant-matter) |
| Codex | 3 | Applied | Unit 2 model includes air, water, food and waste exchanges, several species meeting their needs, and a supplied introduced-consumer case (rabbits brought to Australia); s5-matter-movement |
| Codex | 4 | Applied in part | Supplied table of shares, student-made graphs, every named reservoir on one of two graphs, combined categories said. Rejected: quantities in common units, since water volumes run far past 1,000,000 (shares only) |
| Codex | 5 | Applied | Unit 3: starting properties, the comparison, what stays the same, what is measured, three trials, resulting properties; retrieval of the grades 3 and 4 fair-test routine; s5-new-substances |
| Codex | 6 | Applied | Grade 6's Picked up row now says grade 5 supplies shadow and day-length patterns with spin and orbit, and grade 6 develops latitude, sunlight angle and uneven heating; s6-climate-circulation and s5-shadows-sky notes. Grade 6's unit 3 reason cell is outside its Seams: Cross-subject notes |
| Codex | 7 to 12 | Not acted on here | Other files (progression-science-fixes report, RUBRIC-SCIENCE, science-open-material review, the source catalog analysis): "For the lead" |
| Codex | settled | Applied | All eight rows (the line-plot bridge retrieves grade 4 line plots, 4.MD.B.4) |
| Writer | lead 4 | Applied | Row changes for 5.MD.A.1 and 5.G.A.2 with math's real units |
| Writer | lead 5 | Applied | s5-food-energy-sun model_out now energy-transfer only |
| Writer | lead 1, 2, 7 | For Cory | Time a week; grade 5 state tests; materials ceiling |

Conflict, Codex 1 against the expert on the balloon: Codex cites a demonstration losing about 3 grams as a large
balloon fills. The expert's settled fix addresses exactly that cause by keeping the gas volume tiny; it stands, and
Codex's measurement-honesty sentence is added so any residual difference is investigated, not explained away.

Counts: applied 13 (expert 1 to 7, Codex 2, 3, 5, 6 in full, Codex 1 and 4 in part), rejected 2 (parts of Codex 1
and 4), not acted on 6 (Codex 7 to 12), for Cory 4.

## Progression changes (data/progressions/science.csv, 34 rows)

| Row | Change |
|---|---|
| s2-compare-designs | Notes: grades 3 to 5 split as need, criteria and constraints (3), comparing several (4), fair tests of a prototype (5) |
| s3-motion-patterns, s3-environment-traits | cross_subject add math:2.MD.A.1 (whole units until math grade 3 unit 7) |
| s3-environment-traits | Notes: crowding test, hydrangea anchor case, grade 2 test retrieved not rerun |
| s3-design-problem | cross_subject math:3.MD.A.2 bridge (washers until grams); notes: changing needs element |
| s3-magnet-static | Notes: electromagnet teacher demonstration |
| s3-life-cycles | Notes: planting day 18, photograph fallback |
| s3-animal-groups | Notes: counts out of 10; cross_subject add math:3.MD.B.3 |
| s3-variation-advantage | Notes: mates case |
| s3-habitat-survival | Notes: the wood frog and tree frog case |
| s3-environment-change-solution | Notes: temperature and other-organism cases |
| s3-weather-data | Notes: below zero in words |
| s3-climates | Notes and cross_subject: counts, no temperature below zero graphed |
| s4-energy-device | cross_subject add math:3.OA.D.8 |
| s4-wave-model | cross_subject as the writer gave it; notes: amplitude and the cork, slinky for sound |
| s4-information-codes | cross_subject: the rule-following bridge; notes: research, sharing, two-condition test |
| s4-energy-resources | cross_subject add math:4.NBT.A.2 ("of every 10", no percent) |
| s4-weathering-erosion | cross_subject: cupfuls until math grade 4 unit 6 |
| s4-earth-feature-maps | Notes: the ice-map review placed |
| s4-structures-function | Notes: internal plant case, flower dissection, one plant and one animal argument |
| s5-conserve-weight | cross_subject math:3.MD.A.2 then 5.MD.A.1; notes: cooling case, small balloon, open bottle, honest comparison |
| s5-plant-matter | cross_subject as conserve-weight; notes: dry soil from week 1, the air evidence, the history's correction |
| s5-matter-movement | Notes: exchanges, several species, introduced consumer |
| s5-food-energy-sun | model_out energy-transfer (food-web dropped; s5-matter-movement introduces it) |
| s5-shadows-sky | cross_subject add math:3.MD.B.3; notes: same sun time, the grade 6 split |
| s5-star-brightness | cross_subject math:4.NBT.A.2 then 5.NBT.A.2; notes: light travel time and scale model |
| s5-water-distribution | Notes: two grids, 97 and 3, 69, 30 and 1 |
| s5-new-substances | Notes: recorded plan, three trials |
| s5-design-test | cross_subject: grade 4 line plots if math unit 9 comes later |
| s6-climate-circulation | Notes: what grade 5 supplies and what is new in grade 6 |

No assumes or hands_on changed. Both ends of every changed handoff were edited: grade 2's Handed on row
(s2-compare-designs to s3-design-problem) and grade 6's Picked up row (s5-shadows-sky to s6-climate-circulation),
in their Seams tables only.

## Cross-subject notes (for those frames' owners; not edited here)

- **Math grades 3, 4 and 5**: checked against this pass; their Cross-subject tables already name the science frames
  as written (Codex grade 3 rerun 12 is met there) and their science bridges already match science's (whole inches
  or centimetres and washers in grade 3; whole centimetres and cupfuls, no conversion, in grade 4; grams on one
  scale, light travel time and a scale model, bar graphs in grade 5). No change needed.
- **ELA grade 5** (brief Numbers line and unit 4): shows Earth's water as hundredths (97 of 100 parts salt water,
  most of the rest frozen), which agrees with science; science adds the fresh water as its own 100 (69, 30, 1), so
  ELA's "most of the rest frozen" holds. Optional: cite science unit 5's two grids. No change needed.
- **Science grade 6** unit 3 reason cell ("grade 5 sun angle" retrieval): outside its Seams table. Suggested: "grade
  5 shadow and day-length patterns".
- ELA grades 3 and 4, social studies grades 3 to 5: no change needed; their own bridges hold against science's
  timing.

## For the lead (outside this pass's files)

- **docs/pipeline/briefs/frame-write.md** (grade 3 expert, settled): "Units table, science: the column C3 is headed
  `Practices and crosscutting concepts`".
- **docs/RUBRIC-SCIENCE.md** lines 54 to 55 (Codex g3 rerun 10, g4 7, g5 9): "Science planning material now includes
  the science progression, course frames, the grade 4 scope and sequence draft, and the middle school base text.
  These establish planning commitments; they do not establish that a finished science course exists."
- **docs/RUBRIC-SCIENCE.md** Gateway 2 connections row (Codex g3 rerun 11, g4 8): "Course frames now name
  nature-of-science placements (grade 3 units 1 and 5, grade 4 units 4 and 6, grade 5 units 2 and 6). Unit plans
  must turn these into explicit student work and checks."
- **docs/reviews/progression-science-fixes-2026-11-13.md** (Codex g4 9 and 10, g5 7 and 8): closure notes as Codex
  wrote them (MS-PS4-2 and MS-PS3-5 owner moves done; high school math now placed in math.csv).
- **docs/reviews/progression-science-2026-11-13.md** For Cory (Codex g4 11): closure note on q-hs-science-core.
- **docs/reviews/science-open-material-2026-11-12.md** and **S:\CurioClass-sources\_catalog\analysis-science-ela-ss.md**
  (Codex g5 10 to 12): resolved notes as Codex wrote them.
- Source list (docs/APPROACH-SOURCES.md): Codex's grade 3 to 5 reads name the grade 4 and 5 evidence statements, the
  K-5 review criteria and evidence guide (current addresses), the wood frog, Utqiagvik normals, fast-cycling
  plant timing, balloon demonstration and willow-history sources.

## For Cory

- **Time a week (audience).** 180 minutes a week in grades 3 to 5 against about 60 to 80 in K to 2; no complete
  three-lesson (90-lesson) path exists. One decision for K to 5.
- **Grade 5 state science tests (audience).** Whether a spring band review is wanted.
- **Materials ceilings (money).** About $25 a unit (grade 3) and $30 a unit (grades 4 and 5) for a class of 30.
- **A science teacher's safety read (people).** Grade 3's electromagnet and fan tests, grade 4's circuits, solar
  heaters and shake table, grade 5's fizzing and mixing first.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Arctic case: polar bear, wood frog, rainforest tree frog; judged from needs and conditions | 3 | The old "no frog" claim was false; ELA has just taught frogs |
| Unit 3 anchor adds the hydrangea; the class test varies crowding | 3 | Grade 2 already solved the dark-shelf plant |
| Planting day science day 18; fast-cycling plants; photograph fallback | 3 | The life cycle watched inside unit 3 |
| Electromagnet as a teacher demonstration only | 3 | 3-PS2-3's example inside the no-circuits boundary |
| Changed user need changes the latch's criteria | 3 | 3-5-ETS1-1's needs-and-wants element |
| Hunting data as counts out of 10; no temperature below zero graphed | 3 | No percent or negatives before grade 6 |
| Warmed stream and spreading plant as 3-LS4-4 cases; a sourced bird mates case | 3 | Every clarification kind has a case |
| Sound on a slinky pushed along its length | 4 | Sound is not a sideways wave |
| Amplitude and the floating object compared and explained | 4 | 4-PS4-1 relates wave properties to motion |
| Codes: research, sharing, two-condition test, compared on data | 4 | 3-5-ETS1-2 in full |
| Required internal plant case and flower dissection; one plant and one animal argument | 4 | 4-LS1-1's plant half in full |
| State energy data "of every 10"; water in equal cupfuls | 4 | No percent; millilitres arrive in math unit 6 |
| Canyon anchor leads with the river and matching walls | 4 | Shells were grade 3's puzzle |
| Ice-map review in unit 5 | 4 | Grade 5's water handoff has a home |
| Dry-soil pots from week 1 | 5 | Wet soil weight hides the result |
| Air evidence beside the soil evidence; the willow history's correction told | 5 | 5-LS1-1 needs air as a source |
| Ecosystem exchanges, several species, rabbits in Australia | 5 | 5-LS2-1's relationships in full |
| Fresh water as its own 100: 69, 30, 1 | 5 | 5-ESS2-2's fresh-water shares with whole numbers |
| Star distance as light travel time and a scale model | 5 | Powers of ten arrive in math unit 8 |
| Small-amount balloon test, open bottle as comparison, differences investigated | 5 | Buoyancy kept under the gram |
| Shadow at the same sun time each month | 5 | Removes the clock-change jump |
| Unit 3 investigation recorded with three trials | 5 | 5-PS1-4's investigation practice |
| Grade 6 retrieves grade 5 shadow patterns; sun angle by latitude is new in grade 6 | 5, 6 | One thread, one depth |
| Math calendars cite the Curio Class math frames' units | 3, 4, 5 | The frames exist |
| The year named "about 36 weeks, of which about 30 carry science lessons here" | 3, 4, 5 | One year stated one way, as K to 2 |
| Every simulation has a paper path and needs no student account | 3, 4, 5 | Lesson 14 |
