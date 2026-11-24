# Sequence read: Environmental Science (grade 12 elective), 2026-11-24

Expert cold read, PRODUCTION-PATH step 3, under docs/pipeline/briefs/sequence-read.md. The scope and sequence was
written 2026-11-23/24 by a Claude writer under docs/pipeline/briefs/sequence-write.md; I did not write it.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md (rows S1 to S13), AGENTS.md.
- docs/pipeline/briefs/sequence-read.md and sequence-write.md (both bind).
- docs/courses/environmental-science/scope-and-sequence.md (all, including "For the lead" and the practice and
  crosscutting concept table), data/plans/environmental-science/days.csv (all 160 rows) and source-map.csv (all rows).
- docs/courses/environmental-science/frame.md (all), the 21 env- rows of data/progressions/science.csv with their
  assumes and notes, data/standards/curio-science-electives.txt (CUR-ENV.1 to 21).
- docs/courses/CALENDAR.md and the grade 12 rows of data/plans/calendar.csv (Economics, US Government and Politics,
  US History II, ELA 12, Earth and Space Science).
- Earlier reads: docs/reviews/frame-environmental-science-2026-11-16.md and its fixes file, and the sequence reads of
  Biology, Chemistry and Physics (2026-11-14) for the REPEAT tags.
- Gates, filtered to this course: `plan.py check` prints "sequence environmental-science: 0 failure(s)" and "frame
  environmental-science: 0 failure(s)" (the run exits 1 on other courses only); `sequence.py check
  environmental-science`: 0 failures, no rule 2 notes; `frame.py calendar`: no stagger break for grade 12 (9 to 12 has
  only the week 32 finals rule); `stale.py check`: 0 failures, nothing for this course. I also ran the unit skeleton
  for units 2 and 7 into the scratchpad to see how the gate counts last use.
- No outside source was opened in this read. Where a finding rests on subject knowledge, it says "from memory".

## Verdict

The sequence is sound and close to ready: every unit keeps the frame's days and order, each opens on a real
phenomenon, readiness and retrieval follow the counted rule with clean timing, the calendar leans carry their
bridges, and the Shorter path is real. The biggest risk is assessment coverage: unit 5's end days and five
course-level check days list codes whose parts they never ask about, so a unit writer building items from these
notes would leave town waste, biomagnification, stream health and the measuring parts of CUR-ENV.1 and CUR-ENV.17
unassessed. The one change that matters most is to name a prompt for every part of every code on those days (no day
added), then to name the missing model revision points in units 4, 5, 6 and 9.

Findings: 0 serious, 4 moderate, 7 minor.

## Findings, most serious first

### 1. Moderate: unit 5's end days miss two parts of its codes, and town waste gets one day (sequence; REPEAT new; firm)

CUR-ENV.10 includes "the waste a town makes and how it is reduced, reused, recycled or landfilled" and contaminants
moving from "mine and town waste". CUR-ENV.11 includes "how persistent substances build up in bodies and food chains".
The scored evidence report (days 80 to 82) is on "one mine's pathway and risk", and uranium does not build up a food
chain; day 84's Love Canal sitting says only "a prompt per part". Town waste, landfill liners and e-waste are taught
on day 78 alone (1 of 16 days, against 4 days for the mine pathway, 70 to 73), and biomagnification on day 75 alone.
Day 78 also sits inside section 5.2 (risk), between the cleanup decision (77) and the dose practice (79), away from
the material-tracing days it belongs with. Cost: the unit plan writer reads two broad end-day notes and builds a mine
report and a dump case; the widened parts the frame read asked for (frame read finding 2, settled by Cory
2026-11-17) go unassessed.
Fix (no day added): day 83's "short unfamiliar case" becomes a town landfill leak case (a lined, watched landfill
against an unlined one, and what reduce, reuse and recycle remove from the stream), so the town-waste part is taught
twice; day 84's note names its prompts: pathway, exposure and dose, a dose-response reading, one persistent substance
moving up a food chain (a fish advisory item beside the Love Canal case), how a lined and watched landfill would have
changed the outcome, who bears the risk, and one cleanup choice weighed. Optional: move day 78 to sit after day 73 in
section 5.1, shifting days 74 to 77 down by one, if the writer also updates the day numbers in the scope prose.

### 2. Moderate: five course-level check days list codes without asking each part (sequence; REPEAT yes, the Biology, Chemistry and Physics reads' finding in another form; firm)

Rule 2 ("Each part of each code") binds check tasks too. Read as a busy writer would:
- Day 53: CUR-ENV.4 "relate ... to its formation" has no water-and-nutrient-holding prompt; CUR-ENV.5 "judge its
  erosion record" has no practice-judged-from-yield prompt.
- Day 101: CUR-ENV.7 asks about supply and treatment only, not a stream or lake judged from tests and animals.
- Day 102: CUR-ENV.11 asks risk and who bears it, not dose-response (the frame's check table names it), persistence in
  food chains, or a cleanup choice.
- Day 156: CUR-ENV.12 asks the projection only, not growth from rates or the demographic transition.
- Day 157: CUR-ENV.17's note says the measuring is not sampled; day 158: CUR-ENV.1 asks a plan, not recording counts
  and cover with their uncertainty.
Cost: checks that claim a code but sample part of it overstate what the year-end evidence shows, the same fault three
core reads found.
Fix (no day added): add a short prompt per missing part to each day's note, for example day 101 a short stream test
and tolerance index item (the unit 3 sitting was over 50 days before, so no task form repeats); day 157 a prompt to
plan where, when and in what order to take surface and air readings and why; day 158 a supplied set of quadrat
counts to record as cover with its spread. Where a part truly cannot be asked on paper, drop the code from the day's
codes column rather than claim it.

### 3. Moderate: four units name no model revision point, and unit 9 has no first model (sequence; REPEAT new; firm)

The scope says each unit "names the day its model is revised", and rubric row S4 asks for a model revised at named
points and used in the end task. days.csv names a first model and a revision point in units 1 (12), 2 (24), 3 (48),
7 (108, 115) and 8 (123). Units 4 (first model of a national grid, day 55), 5 (first pathway model, day 70) and 6
(first population model, day 86) name no revision; unit 9's day 136 builds a question board and no model at all.
Cost: the unit plan writer has no day on which evidence changes the class model in three units, and the capstone
has no model for its design to rest on (the lens: "a model that does not change after an investigation means the
investigation did not matter").
Fix (no day added): name revision points in the notes: day 65 (the mix tool tests the grid model: prices, rules and
the mix now in it), day 73 (the leaching run revises the pathway model: speed and distance in sand), day 92 (the
population model gains age structure and stated assumptions); day 136 sketches a first model of how rain leaves the
school site and day 145 revises it with the team data and feedback loops. Add the days to the M column of the
coverage table.

### 4. Moderate: day 22's infiltration test has sharp can edges and outdoor work with no control (sequence, frame; REPEAT new; firm)

Day 22 lists "tin cans open at both ends" and times infiltration "outdoors on two surfaces", but its safety cell is
the bench-lab soil sentence (gloves, eye protection, glass jars on a tray). A can cut open at both ends has sharp
rims (from memory; the NSTA safety position the frame names covers cuts), and the outdoor part has no adult, ground or
thunder control. The frame's unit 2 "Safety (days.csv words)" sentence has the same gap. Cost: a hazard with no
control on the student sheet (lens, day errors); the safety agent would catch it later, but the cell is copied into
the skeleton now.
Fix: add to day 22's safety cell, and to the frame's unit 2 words, "tin cans: rims taped or filed smooth, pressed in
with a board, never by hand; outdoor test: groups with an adult, school grounds only, outdoor work stops at the first
thunder". Day 22's clean-up can stay at 5 minutes.

### 5. Minor: units 1 and 5 return written feedback overnight (sequence; REPEAT new; judgment call)

Unit 1's report is drafted day 13 and feedback returns day 14; unit 5's is drafted day 80 and returns at the end of
day 81. That is 30 written-feedback reports a night per section, and a science teacher often has several sections.
Units 8 and 9 give two nights. Cost: feedback thin enough to make the revision lesson a formality.
Fix (settled below): swap days 15 and 16 in unit 1 (close the question board on day 15, revise on day 16; the sitting
stays on day 17); swap days 79 and 80 in unit 5 (draft on day 79, dose practice on day 80). Both stay inside their
units and keep revision before scoring.

### 6. Minor: the Toledo anchor's toxin is never taught (sequence; REPEAT new; likely, from memory)

The 2014 order came from a toxin made by the bloom reaching treated water (the frame read's anchor check names
microcystin), not from low oxygen. Day 37 teaches bloom, decay and low oxygen (the Gulf case), day 47 treatment
failure points, day 48 the whole chain. No day says that some blooms make toxins that boiling does not remove, which
the anchor's own question ("how did a treatment plant fail") needs.
Fix: day 37's goal adds "and why some blooms make toxins that boiling does not remove"; day 48's note names the toxin
in the field-to-tap chain.

### 7. Minor: transects are named in CUR-ENV.1 but never run (sequence; REPEAT new; firm)

CUR-ENV.1 lists "quadrats, transects, random placement, enough samples". Day 3 names transect in a term set; no day
samples along one (unit 8's heat walk transect is a different outcome). Fix: day 5 resamples along a short transect
from the mown into the unmown site as well as repeating one plot, and day 7's practice set includes one transect set.

### 8. Minor: seven hands-on days carry no no-kit line (sequence; REPEAT new; firm)

The scope says "each hands-on day has a no-kit path in its note", but days 5, 22, 23, 40, 106, 120 and 141 name
supplies and no no-kit path (the frame's unit-level paths exist). Rubric row S6 and the frame's partial-coverage rule
for CUR-ENV.1, 4, 7, 17 and 19 need it on the day. Fix: add one line to each note ("No-kit path: as day 4", "supplied
soil results, partial coverage of CUR-ENV.4", "supplied test readings", "the tool's bean counts", "supplied surface
and air readings, partial coverage of CUR-ENV.17", "as day 140").

### 9. Minor: a Shorter path fold eats an end sitting's reading time (sequence; REPEAT new; firm)

Day 133 (unit 8 Fluency) folds into "134's reading time"; day 134 is the end-of-unit sitting on CUR-ENV.16. Folding
practice into an assessment's time shortens the assessment. Fix: day 133 folds into day 132 as a five-minute opening
set, like the other Fluency folds.

### 10. Minor: progression notes say readiness where the gate counts retrieval (progression; REPEAT yes, the "maintained" and last-use gloss of the core reads; firm)

The notes of env-soil-conservation (bio-evaluate-impact-solutions) and env-conservation-strategies
(bio-define-human-impact-problem) still say "readiness check before the unit opens"; the frame, the scope and the
gate count both rows as last used in Physics unit 2, so retrieval. env-water-quality's note says s7-human-impact-design
was last used in Biology, grade 9; the frame says Chemistry, grade 10 (same treatment). The Physics "use" rests on
day 19, a hook day that lists chem-energy-device-design for retrieval, whose assumes carry the Biology rows one hop;
the gate accepts it, and I do too, but the lead should know the retrieval rests on that one day.
Fix: the progression fix pass rewrites the three notes to the frame's wording.

### 11. Minor: small frame wording the scope has outgrown (frame; REPEAT new; firm)

The frame's Unit by unit table says the sittings of units 1, 5 and 8 fall "on the last day"; the scope puts them on
the next-to-last day so the response stays inside the unit (its "For the lead" 2, which I accept). The frame's unit 6
row says "Adapted readings from Harris chapters 2 and 8", but chapter 2 is cut in both source maps. Fix: the frame
reads "on the unit's last teaching day, before its respond day" and "Harris chapters 3, 4 and 8" for unit 6.

## The data the brief asks me to check

- **Order inside each unit:** sound. Each unit builds on its days, nothing is used before it is taught (day 7 practices
  what day 6 taught; day 22 reads jars set on day 21; tests and index come before the stream day; risk before the
  cleanup decision; cause before remedy in unit 7), and each arc closes on its question. Gaps: findings 1, 3 and 6.
- **Assessments:** an end per unit, response counted once, no unit over 25 days. Gaps: findings 1 and 2.
- **Readiness or retrieval:** every assumed row is in the scope's table with its last use, matching the gate (no rule
  2 notes) and the skeleton. Every readiness check sits in the last ten minutes of the previous unit's last day or the
  respond day between units (18, 33, 54, 69, 85, 103, 117), unit 1's on day 1 after the hook, none on another unit's
  first day and none more than one day ahead. No unit checks a year-before row or retrieves an older one. The grade
  11 taker's case (bio-sources-of-variation on day 69) is handled.
- **Checks that do not repeat:** met. No check samples the unit it follows, and the scope and each day's goal say so.
- **Standards in full:** the CUR-ENV codes have no lettered parts; every code is on teaching days. Transects (finding
  7) are the one named method never carried.
- **Days by load:** follows the frame's loads, except town waste (finding 1: 1 day of 16).
- **The calendar:** checks in weeks 11, 21 and 32, week 32 being the finals week; grade 9 to 12 has no other rule.
  Each same-year lean meets data/plans/calendar.csv: Economics units 1 (school days 81 to 88), 2 (89 to 98) and 4 (108
  to 114) come after days 26, 59 and 63, which carry their bridges; Government unit 8 (64 to 71) runs alongside day
  64, which judges by records only; Government units 3 and 9, US History II unit 6 (67 to 83) and Economics unit 1
  before day 94 are earlier this year, so retrieval is right.
- **Candidate cells:** all 19 settled, each kept on named days with no day added; checked in days.csv.
- **Shorter path:** present, 10 named fold-ins, 500 minutes, nothing assessed, no owned part's only teaching cut;
  arithmetic checks (149 to 140 unit days, 11 to 10 check days). One fold to change (finding 9).
- **Source map:** every Harris section placed or cut with a reason; order changes carry a reason and "no" harm;
  licence limits for chapters 8 and 14 recorded. Harris 6.5 is "cut" while its case facts become day 84's items on
  an `ours` day, consistent with the frame's rule.
- **Practice and crosscutting concept table:** present, every practice and concept on at least one day; spot checks
  of units 1, 4 and 7 match days.csv. It needs the model days of finding 3.

## Lens checklist, scope and sequence layer

| Line | Result |
|---|---|
| A unit's anchor is a topic, not a phenomenon | Met: nine phenomena or decision cases a class can read as data |
| A model is used before the unit that builds it | Met: no new model; each returns with retrieval (computational model day 89, food web day 93) |
| Engineering design in no unit | Met: unit 9 runs a full design cycle; units 2, 3 and 7 judge real practices |
| Equipment assumed with no substitute or no-kit path | Mostly met: every unit has a path; seven days lack the line (finding 8) |
| Plain facts (climate, BASELINE rule 5) | Met: day 61 reads the records first and teaches what they show |
| Safety: hazards and controls per hands-on day | Missed on day 22 (finding 4); otherwise met in the frame's words |
| Models built and revised | Missed in units 4, 5, 6 and 9 (finding 3) |
| Transfer at the end | Met: every end sitting uses an unseen case, named as such |

## Judging "For the lead"

1. Frame fits, 19 Candidate cells kept in existing days: agreed, confirmed against days.csv.
2. Sittings on the next-to-last day in units 1, 5 and 8: agreed; the rule that response stays inside the unit wins.
   The frame's wording should follow (finding 11).
3. Harris licence read: accepted. Days 93, 119 and 147 carry the CC BY-only limit in their notes; the unit writer
   confirms each section. Nothing more for the scope.
4. Anchor figures pinned to named sources, no page opened: accepted for this layer; the frame read checked four of
   them. The unit writer opens each source and dates the figure before any student page uses it.
5. TOOL-ASKS.md not written: a real gap, but the writer was right to stay inside its three files. Other science
   courses have one (chemistry, physics, grades 3 to 8). The lead assigns it from the days.csv tools column; the nine
   names are there.
6. ELA 12's senior research presentations (school days 150 to 156) overlap unit 9's report (151) and presentations
   (153): agreed that neither unit moves. The lead asks the ELA 12 writer whether its presentation days can sit after
   day 153 inside its own unit 8 (125 to 160); if not, both stand and the unit 9 plan notes the load.
7. Unit 9 has no Fluency day: agreed; the frame's "about one a unit" is a guide, and the capstone has nothing new to
   practice.

## Stale notes

`stale.py check` reports nothing for this course. Found by reading: the three progression notes of finding 10; the
frame's "on the last day" and "chapters 2 and 8" (finding 11). The scope's own Earlier learning table and Math leans
paragraph match days.csv.

## What is right and should not be touched

- The readiness timing and the Earlier learning table: every row, last use and day, matching the gate.
- The bridges for the same-year Economics and Government leans, each placed where the calendar needs it.
- The draft, written feedback, revision, then score pattern on every product, and one full performance per end day.
- Course-level checks that never sample the unit they follow, with the reason in the day's goal.
- Field days placed while the season allows (unit 1) and the stream day after the tests are taught (unit 3).
- The sensitivity notes on unit 5 (the Nation's own material only, no family health history) and unit 6.
- The Shorter path's ten folds and its separate early-leaver order from the frame.

## What I could not judge

- Anchor figures and safety guide links: no page was opened in this read.
- Whether a 50-minute stream day (day 42) leaves enough sampling time after travel; that depends on the school's site.
- The tool names against a tools file: none exists yet for this course (For the lead 5).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 1: swap days 15 and 16 (close the question board on 15, revise and score on 16; sitting stays on 17) | Two nights for written feedback on 30 reports | days.csv; scope unit 1 prose |
| Unit 5: swap days 79 and 80 (draft on 79, dose practice on 80); the Shorter path fold-in becomes day 80 | Two nights for written feedback | days.csv; scope unit 5 prose and Shorter path |
| Day 83's practice case is a town landfill leak (lined against unlined) | Gives the town-waste part of CUR-ENV.10 a second day | days.csv |
| Day 84's note names a prompt per part, including a persistent substance in a food chain and the landfill | CUR-ENV.10 and 11 in full at the end | days.csv; scope unit 5 |
| Days 53, 101, 102, 156, 157, 158: a short prompt per missing part, named in each note | Checks ask each part of each code they list | days.csv; scope course-level checks table |
| Model revision points on days 65, 73, 92 and 145; a first model on day 136 | Rubric S4; the scope's own claim | days.csv; scope coverage table |
| Day 22 safety cell: can rims taped or filed, pressed in with a board; outdoor test with an adult, stops at thunder | Hazard without a control | days.csv; frame unit 2 safety words |
| Day 37 goal names bloom toxins that boiling does not remove; day 48 note names the toxin | The anchor's mechanism | days.csv |
| Day 5 adds a short transect from the mown into the unmown site; day 7's set includes a transect set | CUR-ENV.1 names transects | days.csv |
| No-kit lines on days 5, 22, 23, 40, 106, 120, 141 | Rubric S6, partial-coverage rule | days.csv |
| Shorter path: day 133 folds into day 132's opening, not day 134's reading time | Keeps the end sitting whole | scope Shorter path |

## For Cory

None. Every finding is inside the standards' limits and the frame's units and days.

## Sources

No outside source was opened in this read. The findings rest on the repository files listed under "What I read",
the rubric and lens, and subject knowledge marked "from memory" (sharp edges on cut cans, the Toledo bloom toxin).
The NSTA position statement on safety and school science instruction and the CDC harmful algal bloom pages, both named
in the frame's safety read, are the sources the safety and sensitivity agents should check these two points against.

## For the source list

Nothing new.
