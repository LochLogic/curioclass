# Sequence read: Earth and Space Science (grade 12 elective), 2026-11-24

Expert cold read of the Earth and Space Science scope and sequence, done to docs/pipeline/briefs/sequence-read.md with subject science, the lens docs/agents/lenses/science.md and the bar docs/RUBRIC-SCIENCE.md (high school). The scope and sequence was written 2026-11-23/24 by a Claude writer under docs/pipeline/briefs/sequence-write.md; I did not write it. No Codex read of this course was opened.

## What I read

- docs/pipeline/briefs/sequence-read.md and sequence-write.md; docs/agents/EXPERT.md; docs/agents/lenses/science.md; docs/RUBRIC-SCIENCE.md (rows S1 to S13 and the band notes); docs/GLOSSARY.md (teaching day, readiness check, course-level check, end-of-unit assessment).
- docs/courses/earth-and-space-science/scope-and-sequence.md (all of it, the "For the lead" section included), DEFAULTS.md, and frame.md (course in brief, Seams, Models carried, Units, Unit by unit, Course-level checks, Cross-subject, For the lead, Source map head).
- data/plans/earth-and-space-science/days.csv (all 160 rows, every column) and source-map.csv (all 260 rows; every placed section cross-checked against the "Adapts" line of the day it lands on).
- data/standards/curio-science-electives.txt (CUR-ESS.1 to CUR-ESS.26); data/progressions/science.csv (the grade 12 ess rows, what they assume, and the grade 9 to 11 design rows).
- docs/courses/CALENDAR.md (rule 4, 9 to 12) and data/plans/calendar.csv (grade 12 rows); data/plans/english-language-arts-grade-12/days.csv (assessment and due days only).
- The Astronomy 1st edition copy in the source store (its PDF outline for chapter 12).
- Earlier reads: docs/reviews/sequence-physics-2026-11-14.md and sequence-chemistry-2026-11-14.md (format and settled findings); frame-earth-and-space-science-2026-11-16.md was not reopened.
- Gates, filtered to this course: `plan.py check`: sequence and frame 0 failures; `sequence.py check earth-and-space-science`: 0 failures, eight "reads like hands-on" notes (days 1, 25, 29, 64, 73, 97, 115, 117); `frame.py calendar`: prints K to 8 only, so it says nothing about grade 12; `stale.py check`: 0 failures. The course breaks no stagger rule (grade 12 has only the finals-week rule, and check 3 sits in week 32).

## Verdict

A strong, well-ordered sequence: every unit opens on a real anchor, the tools arrive in the order the evidence needs them, readiness and retrieval are counted correctly by grade with every check in the right slot, the source map is complete, and the Shorter path is real. The biggest risk is one false claim the frame passed down: day 127 says a single-layer greenhouse "works for Earth and Mars", which is wrong for Mars by about 40 degrees, and a writer will build the day and its key from it. The one change that matters most after that is naming the parts each course-level check day samples, as the end days already do. Everything here fits inside the existing days.

## Findings

### 1. Serious: day 127 says the single-layer greenhouse works for Mars; it overshoots by about 40 degrees (sequence, frame; REPEAT new; firm on the arithmetic, fact-sheet values from memory)

What is wrong. Day 127's goal, the scope's unit 8 arc and the frame's CUR-ESS.22 cell say one fully absorbing layer "works for Earth and Mars and fails for Venus". With the planetary fact-sheet values (Mars albedo about 0.25, mean surface about 210 K; Earth albedo about 0.31, 288 K; Venus albedo about 0.77, 737 K), the effective temperatures are about 210 K, 255 K and 230 K. One layer multiplies by the fourth root of 2 (1.19): Mars about 250 K against 210 K measured (about 40 degrees too warm), Earth about 303 K against 288 K (about 15 too warm), Venus about 275 K against 737 K. Fitting n in T = Te (n+1)^(1/4) gives Mars about 0, Earth about 0.6, Venus about 100.

Why it matters. Rubric row S10 is a door: a false statement fails the course. Students who run the numbers on day 127 will find Mars does not fit, and a key written to the goal will mark them wrong.

Fix. Day 127 goal: "Add a single fully absorbing layer and test it on all three planets: it runs Earth about 15 degrees warm, Mars about 40 degrees warm (its thin air absorbs little) and Venus more than 400 degrees cold; argue why." Day 128 goal adds: "fit n for each planet (Mars near none, Earth under one, Venus about a hundred)". Scope unit 8 arc: "one layer that fits no planet well, and fails Venus worst (day 127)". Frame CUR-ESS.22 cell: replace "which works for Earth and Mars and fails for Venus by more than 400 degrees" with "which runs Earth and Mars warm and Venus more than 400 degrees cold". The unit plan re-reads the fact sheet and pins the numbers.

### 2. Moderate: course-level check days name one part of codes that have two or three (sequence; REPEAT yes, the Physics and Chemistry reads' finding 3 and 2; firm)

What is wrong. The end days list each part with minutes (days 17, 32, 50, 70, 87, 102, 122, 136, 154). The check days say only "A short prompt per part of each code listed", and their goals name one part: day 52 (CUR-ESS.3 and .4: "identify", not the property explained from make-up or the setting inferred); day 53 (CUR-ESS.6 has no correlation item; CUR-ESS.7 has no uncertainty); day 104 (CUR-ESS.10: recurrence only, no reconstruction from lines of evidence); day 105 (CUR-ESS.13: chances only, not paving; CUR-ESS.16: track and cone only, not the energy gained and lost); day 158 (CUR-ESS.14: flow direction only, not storage and permeability). The scope's line 7 says every check task is "timed in the day's note"; no check day is.

Why it matters. The unit plan writer builds items from the goal; the likely reading drops the unnamed parts, and the check then claims codes it does not sample (sequence-write rule 2, "checks claim only what they sample").

Fix. Give each check day's note the end-day form: one short prompt per part with minutes. Day 52: CUR-ESS.1 profile and gradient (14), CUR-ESS.3 identification and one property explained from make-up (14), CUR-ESS.4 texture, make-up and setting (14). Day 53: CUR-ESS.5 order (12), CUR-ESS.6 section and one correlation of two columns (15), CUR-ESS.7 bracket with its uncertainty (15). Day 104: CUR-ESS.8 location and magnitude (14), CUR-ESS.9 velocity and the locked boundary (12), CUR-ESS.10 one line of evidence judged and the chance (16). Day 105: CUR-ESS.13 chance and the paving effect (12), CUR-ESS.16 energy and the cone (12), CUR-ESS.17 maps read, the forecast and its score (22). Day 157 gains CUR-ESS.14 (storage and permeability, then flow from well levels, 15) beside CUR-ESS.22 (30), and day 158 keeps CUR-ESS.11 alone (monitoring, eruption history, ash and mudflows, 40); days 159 and 160 already list both. Rewrite scope line 7's "timed in the day's note" to hold once this is done.

### 3. Moderate: six first-teaching days are typed Application (sequence; REPEAT yes, the grade 6 read; firm on the glossary rule)

What is wrong. GLOSSARY row "teaching day": Understanding is the first explicit teaching of anything new (a concept, method, model or term set). These days teach something no earlier day taught: day 24 (correlation with key beds and index fossils), day 82 (the advisory, intensity and the cone of uncertainty), day 96 (distant effects of El Niño, and an irregular cycle set against a periodic one), day 118 (regional projections and their spread), day 127 (the greenhouse layer), day 145 (mass of main-sequence stars from the diagram).

Why it matters. An Application day tells the section writer the idea is already taught, so the day gets no explicit teaching and students are asked to use what nobody showed them (lens: "a model is used before the unit that builds it", at day scale).

Fix. Set `kind` to Understanding on days 24, 82, 96, 118, 127 and 145; no goal changes except finding 1's on day 127. None is scored, so no assessment moves.

### 4. Moderate: CUR-ESS.11 (volcanic hazard) has one teaching day and no practice before it is scored (sequence; REPEAT new; likely)

What is wrong. The scope's load line gives "eight with the argument" to CUR-ESS.10 and CUR-ESS.11, but CUR-ESS.11 is taught on day 45 alone, then drafted into the argument on day 46 and scored on day 49; CUR-ESS.10 has days 42 to 44. CUR-ESS.11 is also the only unit 3 item on the year-end check (day 158), 23 weeks later. Meanwhile day 39 is a Fluency day on earthquake location that the Shorter path already treats as foldable.

Why it matters. A monitoring record (swarms, swelling, gas) and a dated eruption history are two readings, each new; one 50-minute day cannot teach both and leave students ready to state a hazard on a new volcano.

Fix (a day swap inside the unit, no day added). Move the Fluency day to the end of section 3.4: old days 40 to 45 become days 39 to 44, and the new day 45 is Fluency: "Practice locating one new earthquake and comparing magnitudes (20 minutes), then read a second Cascade volcano's monitoring summary and dated eruptions for its hazard (30 minutes)". Section 3.2 becomes days 36 to 38, 3.3 days 39 and 40, 3.4 days 41 to 45. Update the candidate days (multiple lines of evidence: days 41, 42 and 49; rates of change: days 40 and 43), the sensitivity days (34, 42, 44, 46), the scope's load line, the coverage table and the Shorter path row (fold day 45 into day 44).

### 5. Moderate: unit 3's scored argument is built on the anchor's own evidence, so CUR-ESS.10 and CUR-ESS.11 are never scored on a new case inside the unit (sequence; REPEAT new; likely)

What is wrong. Days 46 to 49 draft and score "the hazard argument for a coastal town" from the 1700 evidence the class worked through on days 42 to 45 and Mount St. Helens from day 45. Lens: "The end-of-unit task reuses the anchor or a lesson's phenomenon, so it tests memory, not transfer"; rubric S3 asks the end-of-unit assessment to use a new phenomenon or problem. The sitting on day 50 is unseen, but it covers only CUR-ESS.8 and CUR-ESS.9.

Why it matters. The two outcomes the unit spends most on are scored on recall of class work; transfer for them comes only at check 2 (day 104, CUR-ESS.10) and check 3 (day 158, CUR-ESS.11).

Fix. Day 46's goal names "a coastal town the class has not studied, on the Cascadia margin and near a Cascade volcano other than Mount St. Helens, with its own evidence card (one site's buried soil and sand sheet, its station record and the volcano's monitoring summary and eruption dates)". Day 49's prompt list reads "the reconstruction from the town's new site and the class's lines, the stated chance, that volcano's hazard and the advice". The unit plan picks the town and volcano.

### 6. Moderate: the practice and crosscutting concept coverage table undercounts what the days do (sequence; REPEAT new; firm)

What is wrong. The table says Constructing Explanations is done on no day in units 1 and 4 to 9, yet goals there explain phenomena outright: days 15, 66, 68, 78, 81, 85, 91, 92, 94, 101, 120, 133. Argument shows "none" in units 1, 2 and 7 though day 30 argues which events cannot be dated and day 117 states a model's limits from evidence. Cause and Effect is "none" in units 5, 7, 8 and 9 (day 78, the band from a warm lake; day 133, where the water went), and Systems is "none" in units 5, 7 and 8 (days 75, 114, 133).

Why it matters. The table is what an adoption reader checks for rubric row S11 and Gateway 2 coherence; read as written, it says the course builds explanation in three units of nine, which the days contradict.

Fix. Recount every cell from the goals and notes as the brief says (doing it, not a label in passing): add E to units 1 (15), 4 (66, 68, 69), 5 (75, 78, 81, 85), 6 (91, 92, 94, 101), 7 (113, 120), 8 (133) and 9 (140, 151); A to units 2 (30) and 7 (117); CE to units 5 (78, 81), 7 (114, 117) and 8 (125, 133); Sys to units 5 (78), 7 (114, 115) and 8 (133). Then shift the day numbers for finding 4.

### 7. Minor: the scope says every hands-on day names its no-kit path; 17 do not (sequence; REPEAT yes, the Biology read; firm)

Days 5, 7, 10 to 14, 17, 36, 72, 75, 124, 138 to 140, 152 and 153 list supplies with a hazard but carry no no-kit or photograph path in the note, though the frame gives one for each unit (rock photographs and supplied test results; a supplied survey; published soundings; the no-sky path of photographs and a sky chart). Day 17 matters most: a school without kits cannot sit unit 1's assessment as written. Fix: add the frame's no-kit clause to each of those notes, with day 17's reading "No-kit path: a supplied test record for each specimen, the same prompts".

### 8. Minor: day 10's density measurement asks for a reading below the instrument's step, and its tools are not costed (sequence, frame; REPEAT new; likely)

Day 10 lists a kitchen scale and a "graduated cup" for density from displaced water. A hand-sized mineral specimen displaces a few milliliters and weighs tens of grams; a kitchen cup marked in tens of milliliters cannot read it (DEFAULTS.md: "a reading sits inside the instrument's step"). Neither item is in the frame's unit 1 cost cell. Fix: supplies "0.1 g digital scale (shared, one per two groups); 25 mL plastic graduated cylinder", with the unit plan choosing specimens large enough to read; add about $40 to unit 1's cost (5 scales, 10 cylinders), still inside the $1,000 ceiling.

### 9. Minor: day 17's sitting leaves no minutes for kits, and ten sets serve thirty students at once (sequence; REPEAT new; judgment call)

Day 17 gives 45 minutes of prompts plus 5 minutes of clean-up, with no time to hand out kits, give directions or put on eye protection, and an individual sitting shares 10 mineral and rock sets among 30 students. Fix: 40 minutes of prompts (CUR-ESS.1 14, CUR-ESS.3 13, CUR-ESS.4 13) and the CUR-ESS.3 and CUR-ESS.4 items run as a station rotation, one set per three students, each student testing one specimen and reading a supplied record for the rest, said in the note.

### 10. Minor: day 59's stream work in week 12 names no cold-water limit (sequence; REPEAT new; judgment call)

Day 59 falls in mid to late autumn in most of the country. The safety cell covers depth, rain and thunder but not cold water. Fix: add "cold water: measure from the bank only, no wading, when the water or air is below about 10 °C" to day 59's safety, and the no-kit path is used when it applies. The safety agent confirms the threshold against the field work guidance the frame names.

### 11. Minor: stale or loose lines (sequence, frame; REPEAT yes; firm)

- Scope line 132: "`frame.py calendar` shows no break" is vacuous, since the calendar prints K to 8 only. Write: "Grade 12 has only the finals-week rule (CALENDAR.md rule 4), and check 3 sits in week 32."
- Scope line 52: "six days on CUR-ESS.5 and CUR-ESS.6, five on CUR-ESS.7" counts day 25 (Hutton, CUR-ESS.5) under CUR-ESS.7. Write: "seven days on CUR-ESS.5 and CUR-ESS.6 (days 19 to 25), four on CUR-ESS.7 (days 26 to 29)".
- Frame line 251 (Source map head): "the copies are not on file" contradicts the Base text bullet, which says three of the four are in the source store. Write: "Built from the published tables of contents, then checked against the loaded copies in the scope and sequence (source-map.csv); Introduction to Oceanography was not loaded."

## Checklist from the brief

- **Order inside each unit:** met, but for findings 3 and 4. Every unit opens on its anchor and question board, revises its model at named points (days 15, 30, 48, 64 and 69, 78 and 85, 99, 113 and 120, 127 and 133, 151) and answers the board before its end days.
- **Assessments:** each unit closes with an end-of-unit sitting on its second-last day and a respond day last; products are scored after feedback and revision; no unit runs over 25 days; response time is counted once. Part coverage is met on end days and missed on check days (finding 2).
- **Readiness or retrieval:** met. Every assumed row's last use matches the frame's Seams table and the gate; the five readiness checks sit on days 33, 54, 71, 106 and 137 (a respond day or the previous unit's last day, one day ahead), with the reteach on each unit's second day; no first day of a unit after unit 1 holds one; unit 1 correctly needs none. The design practices on day 46 are retrieval, rightly: Physics's phys-collision-safety-design assumes chem-energy-device-design, so the row was used in grade 11.
- **Checks that do not repeat:** met. Checks 1, 2 and 3 leave out the unit just assessed and say so in the scope and the day notes; no task form recurs inside the ten days before a check.
- **Standards in full:** met at unit level; check-day gaps are finding 2.
- **Days by load:** met, but CUR-ESS.11 (finding 4).
- **Calendar:** met. Checks sit in weeks 11, 21 and 32 as the frame and calendar.csv set; every lean is an earlier year; ELA 12 due days (14, 37, 101, 119, 158) check out against its days.csv. Day 121 (unit 7 report scored in class) shares a day with ELA 12's check 3; it is in-class revision, so no change.
- **Candidate cells:** all 18 settled at no added day; one dropped (unit 4, designed systems) with a sound reason.
- **Shorter path:** met: a shorter period, ten named Fluency fold-ins at 50 minutes each (500 minutes, 150 lessons against 160), the frame's early-leave order kept.
- **Source map:** met. 260 rows (19 keep, 16 split, 125 merge, 100 cut, every cut with a reason); each placed section appears in the "Adapts" line of the day it names; order conflicts carry harms_learning.
- **Lens, scope layer:** anchors are phenomena, not topics (met); no model is used before the unit that builds it (met); engineering appears as retrieval in unit 3 and the course owns none, as the frame and Desk set (met); equipment with a substitute or no-kit path (missed in the day notes, finding 7).
- **Stale notes:** stale.py clean; the rest is finding 11.

## For the lead (the scope's five items, judged)

1. **The sitting moves one day.** Agree. Second-last sitting with the respond day last names the response time inside the unit's days, as rule 2 asks, and changes no count. Take the pick.
2. **Astronomy 12.5.** Agree, checked: in the loaded Astronomy 1st edition, chapter 12 is Rings, Moons and Pluto, 12.2 is the Galilean moons and 12.5 is planetary rings. Day 134 rightly keeps 12.2. Take the pick.
3. **Introduction to Oceanography.** Agree: it is not in the source store, and unit 6 holds without it. The frame's item 6 pick stays open; if taken, the source map gains its rows on the days named.
4. **Anchor evidence still to pin.** Acceptable to leave to the unit plans, since no day changes, but unit 1 is first, so the Monadnock bedrock check is owed now. From memory, the summit is metamorphosed schist and quartzite (the Littleton Formation), which fits "quartz-rich metamorphic"; the unit plan confirms it on the state map.
5. **Gate notes.** Agree, checked: the eight "reads like hands-on" days handle no materials.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 24, 82, 96, 118, 127, 145 typed Understanding | First explicit teaching (GLOSSARY, teaching day) | data/plans/earth-and-space-science/days.csv |
| Unit 3 Fluency day moves from day 39 to day 45; old days 40 to 45 become 39 to 44; new day 45 practices location and a second volcano's record | A second CUR-ESS.11 day before the draft; no day added | days.csv; scope-and-sequence.md unit 3 and Shorter path |
| Check-day minutes as given in finding 2, with CUR-ESS.14 moved from day 158 to day 157 | Each part gets its prompt; days 157 and 158 balanced | days.csv days 52, 53, 104, 105, 157, 158 |
| Day 128's candidate note reads "energy is conserved: at steady state a planet radiates what it absorbs" | A planet is not a closed system; the conservation reading still holds | days.csv day 128; scope-and-sequence.md unit 8 |
| Day 17 prompts at 40 minutes with a station rotation for the specimen items | Kit hand-out time and 10 sets for 30 students | days.csv day 17 |
| Day 10 supplies: a 0.1 g scale and a 25 mL graduated cylinder | Reading inside the instrument's step | days.csv day 10; frame.md unit 1 cost cell |
| For the lead 1, 2, 5: picks taken as written | Checked as above | frame.md (Unit by unit, Source map) |

## For Cory

None. Finding 8 adds about $40 to the year, inside the settled $1,000 ceiling.

## What is right and should not be touched

- The readiness count and slots, and the reteach on each unit's second day with an extension for students already ready.
- Evidence before number in unit 2, and records before the model and the human cause in unit 7, with the belief notes asking students to explain evidence, never to declare a belief.
- Unit 3's nation credits and the rule that oral histories are never treated as waiting for science to confirm them.
- The course-level checks' design: each leaves out the unit just assessed and samples older units on unseen data.
- The source map's completeness and its rule that days are ours, credited once.
- The Shorter path's ten Fluency folds and the senior early-leave order.

## What I could not judge

- The anchor facts in For the lead item 4 (rainfall-frequency estimates, the county study, the Copalis homeland nations): no source page was opened in this run.
- Whether the clamp-lamp and thermometer set-up on day 125 shows a clean fall with distance; the unit plan's trial run should say.
- No defect rows were logged with `plan.py defect`: this job's brief allows writing only this report. The caller can log the eleven findings with found_by `expert`.

## Sources

- No outside page was fetched in this run. Finding 1 rests on the energy-balance arithmetic and planetary fact-sheet values recalled from memory (the national space science data center's fact sheets, which the frame already names); the unit plan re-reads them.
- S:\CurioClass-sources\openstax-astronomy-1e (the PDF outline, chapter 12): For the lead item 2.
- Monadnock bedrock (Littleton Formation): from memory, for For the lead item 4.

## Confidence

Finding 1 firm (arithmetic) on values from memory; findings 2, 3, 6, 7 and 11 firm; findings 4, 5 and 8 likely; findings 9 and 10 judgment calls.
