# Baseline 1, part A: the science column (subject=science), 2026-11-14

Reader: the curriculum expert (docs/agents/EXPERT.md), fresh run, brief docs/pipeline/briefs/baseline-1.md.

## What I read

- AGENTS.md; docs/PRODUCTION-PATH.md steps 2 to 4; docs/GLOSSARY.md; docs/pipeline/briefs/frame-write.md;
  docs/agents/lenses/science.md; docs/RUBRIC-SCIENCE.md (rows S1 to S13, scoring, band differences).
- All 12 science frames side by side: docs/courses/science-kindergarten, science-grade-1 to science-grade-8,
  biology, chemistry, physics (each frame.md): brief, seams, models carried, units table, course-level checks,
  and the grades 6 to 8 source maps and loss checks.
- data/progressions/science.csv (198 rows), read by script for the model threads (model_in, model_out by grade),
  the engineering rows and the handoffs.
- The band reads' findings, by search, so as not to repeat them: docs/reviews/frame-science-*, frame-biology-*,
  frame-chemistry-*, frame-physics-* and the four science fix reports.
- `python -X utf8 scripts/plan.py check`: progression science 198 rows, 0 failures; all 12 science frames 0
  failures. Placement, owned standards and day totals are proven; this read spends nothing on them.

Outside sources: none fetched for this run. NGSS crosscutting-concept elements for 3-LS4-1 and the clarification
examples of 3-LS4-1 and MS-PS1-6 are from memory (marked below). The elementary science time figures in finding 6
are from memory of the 2018 National Survey of Science and Mathematics Education and are marked "likely".

## Verdict

The science column is sound in its spine: every model is built before it is used, the grades 6 to 8 base text is
used the same way in all three years (order kept, every base lesson placed, condensations named with their
evidence kept, the same loss check), and engineering climbs cleanly from K-2-ETS1-1 to HS-ETS1-4. The biggest risk
is one no band read could see: the same phenomenon or design task comes back across bands with nobody saying so
(the hand-crank flashlight in grade 4 and Physics, a sea fossil on a hill in grade 3 and grade 6, the plant in the
dark in kindergarten and grade 2, the chemical heater design in grade 7 and Chemistry), because the high school
repeat rule looks only at grades 6 to 12 and kindergarten to grade 5 has no repeat rule at all. The one change that
matters most is a K to 12 repeat rule in the frame-write brief and the frames, with the swaps listed under "Settled
by the expert"; the second is filling the grades 6 to 8 C3 cells, so the practice and crosscutting threads can be
traced through the middle school years.

## Findings, most serious first

### 1. Phenomena and design tasks repeat across bands, unsaid; no repeat rule spans K to 12
LAYER: frame, process. REPEAT: new. Confidence: firm (read from the frames).

**What is wrong.** Biology, Chemistry and Physics each check their anchors against "the grades 6 to 8 base text"
and the earlier high school courses (biology/frame.md, "How phenomena are chosen"; chemistry and physics the same
line), never against kindergarten to grade 5. The K to 5 frames have no repeat check at all. The pairs found:

| Pair | Where | Same at the same depth? |
|---|---|---|
| Hand-crank flashlight with no battery | science-grade-4 unit 2 anchor; physics unit 5 anchor ("Shake a flashlight") | Same object as the anchor; physics asks the deeper question (induction) but does not say it returns on purpose |
| A sea fossil high on dry land | science-grade-3 unit 5 anchor (seashell fossils in a hill far from the sea); science-grade-6 unit 4 anchor (sea fossil near the top of Everest, base text, fixed) | Same puzzle; grade 3 is ours and can change |
| A plant kept in the dark | science-kindergarten unit 4 anchor (class plant on a dark shelf); science-grade-2 unit 5 anchor (plant left in the closet); biology unit 3 anchor (seeds in a dark cupboard) | Grade 2 repeats kindergarten's set-up as its anchor; Biology measures dry mass, so it is deeper |
| Cat in a dark room | science-grade-1 end-of-year check ("why a cat in a dark room cannot be seen until a lamp is on"); science-grade-4 unit 6 anchor A (a cat crossing a yard at night) | Grade 1 uses up grade 4's puzzle as a check case |
| Grand Canyon | science-grade-2 unit 2 pick for slow change; science-grade-4 unit 4 anchor | Grade 2 shows the answer (slow carving) before grade 4 asks it |
| Chemical heater design | science-grade-7 unit 2 (flameless heater, MS-PS1-6 design); chemistry unit 7 design problem ("from sunlight or a chemical pack") | Chemistry's own list rules out the flameless heater as an anchor, then lets the same design back in as an option |
| Drop-cushioning design with eggs | science-grade-8 unit 1 (protective case and cushioning; eggs as a stand-in); physics unit 2 (egg-drop package) | Physics adds momentum and collision time, but the build is the grade 8 build |
| Sealed baking soda and vinegar, mass kept | science-grade-5 unit 1 (bottle with a balloon); science-grade-7 unit 1 (bath bomb, mass down when open); chemistry unit 4 anchor (sealed zip bag) | Chemistry's anchor is grade 5's demonstration; its new puzzle is counting, which the anchor does not show |
| Shadow stick | science-grade-1 unit 1 anchor; science-grade-5 unit 4 anchor ("the class's shadow stick") | A tool reused on purpose, with a readiness check on grade 1; only the "on purpose" line is missing |

**Why it matters.** An anchor works when the class cannot yet explain it (lens, "A phenomenon drives the unit";
RUBRIC-SCIENCE S1). A student who met the flashlight, the sea fossil or the dark-closet plant two to six years
earlier comes in with the answer, or with the feeling of "we did this". The rubric's 2h row asks for tasks that
grow harder; a repeated anchor at a similar depth reads as the same task. The writers of steps 3 and 5 will copy
the frames' picks into days, so the fix is cheapest now.

**The fix.**
- docs/pipeline/briefs/frame-write.md, lesson 11, add after "...do not repeat another grade's picks.": " In science
  this runs kindergarten to Physics: an anchor, design problem or check case used in any other science course is
  either swapped or marked 'returns on purpose from <course> unit <n>: what is new here'."
- In biology, chemistry and physics frames, "How phenomena are chosen": replace "not an anchor the grades 6 to 8
  base text or Biology already uses" (and the Chemistry and Physics equivalents) with "not an anchor, design
  problem or check case any other science course uses, kindergarten to Physics, unless the unit says it returns on
  purpose and what is new".
- The swaps and the "on purpose" lines are item-level picks and are listed under "Settled by the expert".

### 2. Grades 6 to 8 name no practices or crosscutting concepts per unit (C3 = "n/a" in all 18 units)
LAYER: frame. REPEAT: new (the band reads raised only the column's name, not the empty cells).
Confidence: firm.

**What is wrong.** In kindergarten to grade 5 and in Biology, Chemistry and Physics, the C3 column holds each
unit's practices and crosscutting concepts, and K to 2 add a "Practices across the year" line. In
science-grade-6, 7 and 8, every unit's C3 cell reads "n/a", and no brief line lists practices or crosscutting
concepts for the year. The model columns of the progression carry some concepts (patterns, cause-effect,
scale-proportion), but not the eight practices.

**Why it matters.** The climb of a practice (using mathematics, developing models, analysing data, argument) can
be traced from kindergarten to grade 5 and again from grade 9, and is blank in between, the three years where the
NGSS practice elements are most numerous (Appendix F, from memory). RUBRIC-SCIENCE S11 counts "every practice and
crosscutting concept element owed by the band" for K to 8; a 6 to 8 scope and sequence writer has no frame-level
place to see which unit owes which. It also hides real steps: grade 5 builds a first computational step (graphing
weights), Biology unit 5 claims "a first computational model", and no frame says what grades 6 to 8 did with
computational thinking in between.

**The fix.** In each of the 18 grades 6 to 8 unit rows, replace "n/a" with "Practices: ...; Crosscutting: ...",
taken from the base unit's own list of focal practice and crosscutting elements (each OpenSciEd unit overview in
S:\CurioClass-sources\openscied-ms names them), at the same grain as grades 3 to 5 (two or three practices, two
crosscutting concepts). Then add one brief bullet to each 6 to 8 frame, "**Practices across the year.**", in the
K to 2 form. A writer's job, not a choice: the base text decides the elements.

### 3. Idle handoffs are handled by three names and no shared rule
LAYER: process, frame. REPEAT: yes for single courses (the Biology and Chemistry band reads touched their own
wording); the cross-grade rule is new. Confidence: firm.

**What is wrong.** When a skill or model comes back after a gap, the frames use three treatments with no stated
rule for which:
- science-grade-4 and 5 and science-grade-8: "readiness check" with a one-lesson reteach, for rows called
  "dormant" (grade 8: "twelve dormant readiness checks"). "Dormant" is defined nowhere (GLOSSARY, frame-write
  brief, scripts: none).
- biology: grade 7 rows idle one year open with a "retrieval task"; models idle in grade 8 get a "reactivation
  task" (a third word, not in the GLOSSARY).
- chemistry brief: grade 7 rows idle two years and grade 6 rows idle three open "with retrieval or a readiness
  check", leaving the choice to a later writer.
- physics: grade 6 rows idle five years get a readiness check and reteach; grade 8 rows idle two years open with
  retrieval.
So a row idle two years gets a readiness check in grade 4 and grade 8, "retrieval or a readiness check" in
Chemistry, and retrieval in Physics.

**Why it matters.** The readiness check is a glossary word with a fixed form (items.csv `check` = `readiness`)
and a cost (the reteach lesson is counted in days). Units that should carry one will not, and day budgets differ
for the same gap. The scope and sequence writers in step 5 need one rule.

**The fix.**
- docs/pipeline/briefs/frame-write.md, add lesson 16: "**Returning skills, one rule (science first, any subject
  may use it).** A skill or model last used two or more grades before opens the first unit that needs it with a
  readiness check and a one-lesson reteach, counted in the unit's days. One used in the grade before (or earlier
  this year) opens with a retrieval task, a few minutes inside a lesson. Do not write 'dormant' or
  'reactivation'."
- docs/GLOSSARY.md, "The course" table, add a row: "**retrieval task** | A few minutes inside a lesson that bring
  back a skill or model last used within the past grade | reactivation, warm-up (that is the day's opening) |
  none".
- chemistry/frame.md, "Course in brief": replace "opens with retrieval or a readiness check with a one-lesson
  reteach" with the per-row result of the rule (grade 6 rows: readiness check; grade 7 rows: readiness check, as
  two grades have passed). biology/frame.md: replace "reactivation task" with "retrieval task" (food-web,
  matter-cycle and plate-model were last used in grade 7, one grade before). science-grade-4, 5, 8: replace
  "dormant" with "last used in grade <n>".

### 4. Scale, proportion and quantity is used in grade 3 but recorded as new in grade 5
LAYER: progression. REPEAT: new. Confidence: likely (the 3-LS4-1 crosscutting element is from memory: "observable
phenomena exist from very short to very long time periods").

**What is wrong.** science-grade-3 unit 5 lists "Crosscutting: scale, proportion and quantity (deep time)", which
is the crosscutting concept 3-LS4-1 itself names. But data/progressions/science.csv row s3-fossils has model_out
"patterns" only, and science-grade-5's Models carried says scale-proportion is "New in grade 5".

**Why it matters.** One thread, one starting point: grade 5's unit 1 will be written as the introduction of a
concept grade 3 already used, and grade 3's deep-time work is invisible to the grade 4 rock-layer unit that needs
it.

**The fix.**
- data/progressions/science.csv, s3-fossils, model_out: "patterns" becomes "patterns; scale-proportion".
  s4-rock-layers, model_in: "patterns; stability-change" becomes "patterns; stability-change; scale-proportion"
  (rock layers laid down over very long times), which keeps the thread continuous through grade 4.
- science-grade-5/frame.md, Models carried, row scale-proportion, column 2: "New in grade 5" becomes "From grade 3
  (s3-fossils: very long times) and grade 4 (s4-rock-layers); very small scale is new here". Grade 3 and 4 frames'
  Models carried each gain a scale-proportion row.
- The fixer runs `scripts/plan.py check` after the row edit.

### 5. The nature of science changes its name in grades 3 to 5
LAYER: frame. REPEAT: new. Confidence: firm.

**What is wrong.** Kindergarten to grade 2 and grades 6 to 12 write "nature of science" (brief bullets and unit
text); science-grade-3, 4 and 5 write "How science works" (brief bullet, line 58, 59 and 54, and in unit text).
RUBRIC-SCIENCE scores it as 2f ("nature of science") for K to 8.

**Why it matters.** A reader tracing 2f through the grades, or a script searching for it, loses grades 3 to 5,
and a scope and sequence writer may think grades 3 to 5 owe nothing.

**The fix.** In science-grade-3, 4 and 5, the brief bullet "**How science works.**" becomes "**Nature of science
(how science works).**", and each in-table "How science works:" becomes "Nature of science:". Kindergarten to
grade 2, which list it inside "Practices across the year", gain the same bold bullet so all twelve frames carry
it in one place.

### 6. Shape: the weekly time more than doubles from grade 2 to grade 3, and grades 6 to 8 give their year checks one day
LAYER: frame. REPEAT: new. Confidence: likely (national time figures from memory).

**What is wrong.**
- Time a week: kindergarten about 60 minutes, grade 1 about 65, grade 2 about 80, then grades 3 to 5 180 minutes
  (four 45-minute lessons). All six frames give the same reason ("science shares the day"); the grades 3 to 5
  frames justify 111 unit days by row load, but the owned load rises far less than the time (grade 2 owns 13
  expectations in about 2,800 minutes; grade 3 owns 16 in about 5,000). From memory of the 2018 national survey,
  US elementary classes average roughly 20 minutes of science a day in kindergarten to grade 3 and about 25 in
  grades 4 to 6: the K to 2 frames sit near or under that, the 3 to 5 frames well above it.
- Course-level checks: kindergarten to grade 2 give each check 2 days, grades 3 to 5 give three checks of 2 days,
  Biology, Chemistry and Physics give 2, 2 and 3 days (11 days with respond days); grades 6 to 8 give two checks of
  1 day each (4 days a year), each covering three units, in the band with the heaviest load (grade 8 owns 26
  rows). No 6 to 8 frame says why one day is enough.

**Why it matters.** A grade 3 teacher in a school that gives science two or three lessons a week cannot run the
year as framed and will cut from the end (unit 6, the weather and hazards unit, in grade 3; the design units in
grades 4 and 5). A one-day check on three units is the thinnest year-level evidence in K to 12, where the record
handed to grade 9 matters most.

**The fix.**
- science-grade-3, 4 and 5, "**Days.**" bullet, add: "A school with about 120 minutes a week runs the year at
  three lessons a week across the same 30 weeks (90 days) by taking the shorter path the unit plans name in each
  unit; no expectation is dropped." Each unit plan then names its shorter path. The frame keeps 120 days. (Whether
  Curio Class plans for the higher time at all is under "For Cory".)
- science-grade-6, 7 and 8, "**Days.**" bullet, add the reason: "Each check is one day because every unit already
  ends in its own end-of-unit assessment on an unseen case inside its days; the course check samples across units."
  If the scope and sequence finds a 50-minute check cannot sample three units, it takes a day from the unit before
  the check and says so.

### 7. Year checks that should climb ask the same thing in grades 5 and 7
LAYER: frame. REPEAT: new. Confidence: firm.

**What is wrong.** science-grade-5 check 1 asks "an argument about where an unseen plant's added weight came from,
from given data"; science-grade-7 check 2 asks "where a plant's mass comes from". As written, grade 7 can be
answered at grade 5 depth ("from air and water").

**Why it matters.** Year-end checks are the record each grade passes on; the grade 7 one should show the atom-level
step (MS-LS1-6 and the grade 7 matter-cycle model), or it cannot tell a grade 7 student from a grade 5 one.

**The fix.** science-grade-7/frame.md, Course-level checks, check 2: "where a plant's mass comes from" becomes
"where an unseen plant's mass comes from, traced as atoms of carbon dioxide and water regrouped into sugar and
then into the plant's body, with the energy from light shown".

### 8. Places lean to North America; Africa, South Asia and Oceania are absent
LAYER: frame. REPEAT: new. Confidence: firm (counted from the anchors).

**What is wrong.** Of about 90 unit anchors from kindergarten to Physics, fewer than ten are set outside North
America and the North Atlantic (Japan and Everest in grade 6, the oil palm rainforest in grade 7, Peru in grade 8,
the axolotl in Biology, river deltas unnamed in Chemistry). None is set in Africa, South Asia or Oceania.
Washington State appears twice (grade 5 unit 5's Cascades; Biology unit 9's river). The historical investigation in
grade 5 unit 2 is told without its person.

**Why it matters.** The brief's "fair spread of peoples, places and periods over K to 12"; science as done by
people everywhere is part of the nature of science (Appendix H, from memory).

**The fix.** Item-level picks, settled below: grade 3 unit 5, Chemistry unit 11 and Physics unit 10 gain named
places in Africa, South and Southeast Asia, Oceania and Latin America; grade 5 unit 2 names the person and place
of its experiment.

## What is right and should not be touched

- Grades 6 to 8 use the base text one way in all three years: the 18 units in order, one source map shared by the
  three frames, every base lesson placed, optional lessons named and left out with reasons, condensations named
  each with its evidence kept, Curio Class additions named where the base stops short (MS-ESS3-1, MS-PS2-3,
  MS-PS2-5, MS-PS3-2, MS-LS1-2), and the "+CS" variants never mapped.
- Engineering climbs without a gap: K-2-ETS1-1, 2, 3 in kindergarten, grade 1, grade 2; 3-5-ETS1-1, 2, 3 in grades
  3, 4, 5; MS-ETS1-1 to 4 started in grade 6 and owned in grades 7 and 8; HS-ETS1-1, 3, 4 in Biology and 2 in
  Chemistry.
- Every model is built before it is used (checked by script), and the models' names stay the same from grade to
  grade (cause-effect, patterns, data-graph, design-cycle, claim-evidence-reasoning, system-model all from
  kindergarten to Physics).
- The early weather chart (kindergarten) and the grade 3 weather log are kept on purpose as habits, and the
  shadow stick is a tool kept on purpose; they need only the "on purpose" line (Settled below).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Physics unit 5 anchor becomes a bicycle wheel dynamo that lights a lamp only while the wheel turns, faster turning, brighter lamp | The hand-crank flashlight is grade 4 unit 2's anchor; the dynamo shows the magnet and coil and the rate dependence induction needs | physics/frame.md, unit 5 row |
| Grade 3 unit 5 anchor becomes fossils of tropical plants (ferns and palms) found in rock in the Arctic, Svalbard in Norway; the class's own state fossil swap stays | 3-LS4-1 names tropical plant fossils in Arctic areas (from memory); the sea fossil on a mountain is grade 6 unit 4's base anchor | science-grade-3/frame.md, unit 5 row |
| Grade 2 unit 5 anchor becomes the yellow, pale grass found under a board or tarp left on the lawn for two weeks | The dark-shelf plant is kindergarten unit 4's anchor; the investigation itself stays as the standard sets it | science-grade-2/frame.md, unit 5 row |
| Grade 1 end-of-year check case becomes "why a toy inside a closed tent cannot be seen until the flap is opened or a lamp is on" | The cat in the dark is grade 4 unit 6's anchor | science-grade-1/frame.md, Course-level checks |
| Grade 2 unit 2 slow-change picks drop the Grand Canyon and keep the worn stone step, adding a sea cliff worn back by waves over many years | Grade 4 unit 4's anchor is the Grand Canyon | science-grade-2/frame.md, unit 2 row |
| Chemistry unit 7 design problem drops "or a chemical pack": the device heats food or water from sunlight, or turns another form (motion, electrical) into the energy wanted | Grade 7 unit 2 designs a chemical heater (MS-PS1-6) | chemistry/frame.md, unit 7 row |
| Physics unit 2 design becomes a bicycle helmet liner or a model car crumple zone, with collision time and force measured; the egg-drop package is dropped, and the row says "returns on purpose from science-grade-8 unit 1: new here, momentum and collision time measured" | Grade 8 unit 1 builds a cushioning design with eggs as a stand-in | physics/frame.md, unit 2 row |
| Chemistry unit 4 adds: "the sealed-bag reaction returns on purpose from science-grade-5 unit 1 as the readiness opener; new here, how many particles, counted by weighing" | Grade 5 runs the same demonstration | chemistry/frame.md, unit 4 row |
| Grade 5 unit 4 adds: "the grade 1 shadow stick returns on purpose, now measured" | Tool reused on purpose; only the line is missing | science-grade-5/frame.md, unit 4 row |
| Chemistry unit 11 names its deltas: the Nile, the Ganges-Brahmaputra and the Mekong | Places in Africa and South and Southeast Asia | chemistry/frame.md, unit 11 row |
| Physics unit 10 age table includes the Allende meteorite (fell in Mexico, 1969) and the Murchison meteorite (fell in Australia, 1969) | Real dated samples from Latin America and Oceania | physics/frame.md, unit 10 row |
| Grade 5 unit 2 names Jan Baptist van Helmont and Brussels in the anchor | A historical investigation tells its person and place | science-grade-5/frame.md, unit 2 row |
| Grade 7 check 2 wording as in finding 7 | Year checks climb | science-grade-7/frame.md, Course-level checks |

## For Cory

1. **Science time in grades 3 to 5.** The grades 3 to 5 frames plan 180 minutes of science a week (four 45-minute
   lessons, 120 days a year); kindergarten to grade 2 plan 60 to 80. Many elementary schools give grades 3 to 5
   about 120 minutes or less (from memory). My pick: keep 120 days as the full course, and have every unit name a
   shorter path for a school with three lessons a week (finding 6). The alternative is to plan grades 3 to 5 at
   three lessons a week (about 90 days) as the main course. This decides which schools can run the course as
   written, so it is an audience call.

## What I could not judge

- The NGSS practice and crosscutting elements owed per grade in 6 to 8 could not be counted against the frames,
  because the frames do not list them (finding 2). A count is possible once the C3 cells are filled.
- Whether the grades 3 to 5 day loads are right per unit needs the unit plans; this read judged only the whole
  year's time against its neighbours.

## Sources

- docs/RUBRIC-SCIENCE.md: rows S1, S11, 2f, 2h, the band rules.
- docs/agents/lenses/science.md: anchors, models, transfer.
- NGSS performance expectations and their crosscutting elements (3-LS4-1, MS-PS1-6, MS-LS1-6) and Appendices F and
  H: from memory, not fetched in this run.
- 2018 National Survey of Science and Mathematics Education, elementary instructional time: from memory, not
  fetched; finding 6 is marked likely for that reason.
