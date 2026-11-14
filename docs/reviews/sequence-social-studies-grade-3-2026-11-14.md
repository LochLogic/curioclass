# Sequence read: social-studies-grade-3 (Grade 3: Communities Then and Now), 2026-11-14

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, the social studies part of docs/ADOPTION-BAR-SUBJECTS.md,
  docs/courses/social-studies/STANDARD.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md (rule 2),
  frame-write.md lesson 16, docs/GLOSSARY.md (readiness check, retrieval task).
- Cold: docs/courses/social-studies-grade-3/scope-and-sequence.md and data/plans/social-studies-grade-3/days.csv (all 160
  days).
- Beside them: docs/courses/social-studies-grade-3/frame.md, the grade 1 to 3 rows of data/progressions/social-studies.csv,
  docs/courses/CALENDAR.md, data/plans/calendar.csv (grade 3, all subjects), and the ELA grade 3 frame's unit table for the
  leans. The Massachusetts 2018 grade 3 codes in data/standards/ma-hss-2018.txt.
- Gates: `plan.py check` passes for this course (0 failures); `frame.py calendar` places grade 3 social studies checks in
  weeks 14, 25 and 28 with no stagger break; `stale.py check` fails only in us-history-ii/frame.md, not this course.
- For REPEAT: the non-Codex sequence reads already in docs/reviews/ (economics, World Geography and Ancient Civilizations I
  and II). I did not open the Codex reads.

## Verdict

A sound year that a unit-plan writer can build from: the units, day counts and arcs match the frame and calendar.csv, every
lettered anchor part is carried by a day, the leans are met or bridged, and the readiness calls are right. Two things need
fixing before unit plans: the end-of-unit and mid-unit check days name only some of each unit's owned codes, so the
checks as written would leave whole standards unassessed; and unit 5 teaches its three colonies in reverse time order
while claiming time order. Both are fixed inside the units with no change of scope. Four smaller fixes follow.

## Findings, most serious first

### 1. The check days name only part of what each unit owns

- **LAYER** sequence. **REPEAT** new. **Confidence** firm (on what the codes column says); likely (on the harm).
- **What is wrong.** The end-of-unit assessment must cover every part of every standard the unit teaches. The codes
  column on each check day names a few codes; many owned codes sit on no unit check, and several on no check at all in
  the year:
  - Unit 1 (day 23): MA.3.T2.1, MA.3.T2.2, D2.Geo.2, D2.Geo.4, D2.Geo.5, D1.1 to D1.4.
  - Unit 2 (day 47): D2.Civ.2, 4, 5, 6, 7, 9, 10, 11; D2.Eco.12.
  - Unit 3 (day 67): D2.Eco.2, 5, 7, 9, 10.
  - Unit 4 (day 88): MA.3.T2.3a to d (only the parent MA.3.T2.3 is named).
  - Unit 5 (days 104 and 120): MA.3.T3.2, MA.3.T3.3, MA.3.T4.1a to c, MA.3.T5.1, MA.3.T5.5a to c, D2.His.2, D2.Geo.7.
  - Unit 6 (day 135): D2.Civ.5.
  - Unit 7 (day 159): D4.2, D4.3, D4.7, D4.8 (the biography, the sharing and the action).
  - Course-level check 3, part 1 (day 137) has an empty codes column.
- **Why it matters.** The unit-plan writer builds the check from the day's goal and codes. A busy writer will write items
  for the codes named and leave the rest, so unit 1's New England map, unit 2's civic virtues and rules, unit 3's
  economics and unit 5's Mayflower Compact, Pilgrim hardships and sea trade would be taught and never assessed. The bar's
  assessment items (C4, C8) need each owned standard checked.
- **Fix.** On each unit's end check day (and day 104 for the part of unit 5 before it), list in the codes column every code
  and lettered part the unit owns, as the frame's Units table gives them: add the codes above to days 23, 47, 67, 88, 104
  or 120 (MA.3.T3.2, MA.3.T4.1a to c to day 104; MA.3.T3.3, MA.3.T5.1, MA.3.T5.5a to c, D2.His.2, D2.Geo.7 to day 120),
  135 and 159. Where a code is judged by a product rather than a task (unit 7's D4.2, D4.3, D4.7, D4.8; the D1 inquiry
  codes), keep it on the check day and add to the note "judged from the unit's product with the unit rubric". Day 137:
  codes "MA.3.T1.1; D2.Geo.1.3-5; D2.Civ.1.3-5; D2.Eco.1.3-5" or whatever the part 1 tasks draw on, as the course-level
  table states.

### 2. Unit 5 teaches its colonies in reverse time order

- **LAYER** sequence. **REPEAT** new. **Confidence** firm.
- **What is wrong.** The scope and sequence says "Time order. The timeline is taught first ... so every event after it lands
  on the line", then places Plymouth (1620) on days 97 to 100, Jamestown (1607) on 101 to 102 and St. Augustine (1565) on
  day 105, after the mid-unit assessment. No reason is given for leaving time order, and the lens asks for one.
- **Why it matters.** The unit taught the timeline on days 91 to 92 so that each colony lands on it in turn; teaching the
  colonies backwards undoes that, and leaves St. Augustine (the oldest European town in what is now the United States) as
  an afterthought on a compressible day, outside the mid-unit assessment.
- **Fix (settled here, a swap inside the unit, no day cost).** Day 97: St. Augustine and the Timucua (was day 105; keep
  "compressible (shorter block)" and the sensitivity note). Days 98 to 99: Jamestown and the Powhatan; the 1622 war (were
  101 to 102). Days 100 to 103: Plymouth, who came and why; the Mayflower Compact; hardships; the Wampanoag and Plymouth
  (were 97 to 100). Day 104: add first meetings and the three colonies to the timeline; review (was 103). Day 105: the
  mid-unit assessment, now naming St. Augustine, Jamestown and Plymouth with their Native neighbors (was 104); its
  response opens day 106. In the scope and sequence, rewrite the unit 5 order paragraph to match, change "day 104" to
  "day 105" and "response opens day 105" to "opens day 106", and change the compressible list's "105" to "97". Day 106
  onward is unchanged.

### 3. The biography thread the frame promises is on two days of the year only

- **LAYER** sequence. **REPEAT** new. **Confidence** likely.
- **What is wrong.** The frame says "A short biography read in most units from unit 1". ss3-biography appears on day 1 and
  then only in unit 7 (days 149 to 151, 158 to 159).
- **Why it matters.** Unit 7 asks students to write a biography from two sources. Reading short biographies across the year
  is how they meet the form (time order, a life's turning points) before writing one, and it carries the bar's person
  focus at grade 3.
- **Fix (settled here, no day cost).** Add ss3-biography to the skills column, with the note "short biography read", on one
  existing day in each of units 2 to 6 where a person already stands at the centre: day 30 or 36 (a local leader in unit
  2), a day in unit 3 that names a worker or business owner, day 83 (a person from one of the nations), day 107 (one
  leader in a pair), and a unit 6 day naming a founder or the 1776 New Jersey voters. Each read is a few minutes inside the
  day, not a new day.

### 4. Day 78 leaves the Cherokee only in Oklahoma

- **LAYER** sequence. **REPEAT** new. **Confidence** a judgment call.
- **What is wrong.** Day 78: "the Cherokee Nation, its Southeast homelands told apart from its present lands in Oklahoma".
  That is true of the Cherokee Nation, but the Eastern Band of Cherokee Indians governs in its homeland in North Carolina
  today. A grade 3 student told "homelands then, Oklahoma now" will think no Cherokee live in the Southeast.
- **Why it matters.** The lens asks that Native nations be shown in the present tense and as more than a forced move;
  grade 2 already met the Cherokee as a forced move.
- **Fix.** Day 78 note: add "the Eastern Band of Cherokee Indians still governs in the North Carolina homeland; name it,
  from its own pages".

### 5. The readiness and retrieval calls are right; rule 2's wording has a gap

- **LAYER** process. **REPEAT** yes (the World Geography and Ancient Civilizations I and II sequence reads raised the
  readiness or retrieval question). **Confidence** firm (on the call); likely (on the wording).
- **What is wrong.** Nothing in the days. Grade 1 rows not used in grade 2 (ss1-leaders on day 1; ss1-elected-leaders,
  ss1-citizens, ss1-voting, ss1-group-roles on day 25; ss1-national-symbols in unit 6) get readiness checks; grade 2 rows
  open as retrieval tasks. But rule 2 says a readiness check is for a skill "idle two or more grades", and a grade 1 row
  skipped across grade 2 is idle one grade, so a strict reader could argue retrieval.
- **The right call for this course: as written.** A skill last used two grades back, by a younger child, needs a check that
  tells the teacher who has it, and the reteach that follows is cheap (one small-group lesson inside the next day). The
  readiness checks stay.
- **Fix.** None in this course. For the lead: reword rule 2 in sequence-write.md (and frame-write lesson 16) to "a skill last
  used two or more grades back (the grade before did not use it) gets a readiness check on the unit's first day; one used
  the year before opens as a retrieval task inside a day".

### 6. A stale lean note; the For the lead items stand

- **LAYER** sequence. **REPEAT** yes (stale notes, as in the economics sequence read, finding 8). **Confidence** firm.
- Day 86 note says ELA W.3.1 is "(its unit 3, days 81 to 119, later)"; day 86 is inside those days. Change "later" to
  "running now, begun day 81; the one-sentence frame holds until unit 5".
- The frame's two For the lead items in the scope and sequence are right (unit 7 runs days 141 to 160; unit 2 carries
  Native content on days 28 and 43). Apply both as written.

## Checked and found right (do not undo)

- Units, day counts and dates match the frame and data/plans/calendar.csv exactly; no look-back day is held, so nothing
  shifts. The right call on held look-back days here: none needed.
- Every lettered anchor part (MA.3.T2.3a to d, MA.3.T4.1a to c, MA.3.T5.5a to c) and every owned C3 code is carried by a
  teaching day, not only named.
- Unit 5 runs 32 days and has its mid-unit assessment; no other unit is over 25 days. Each unit has one respond day after
  its end check; course-level checks have their own respond days; response time is counted once.
- Course-level checks sit on CALENDAR.md's target weeks 14, 25 and 28; the grade's math, science and ELA checks fall in
  other weeks.
- Leans: math 3.NBT.A.2 is bridged on days 53 and 60; the science lean on day 6; ELA SL.3.1 and RI.3.7 (its unit 1) are met;
  W.3.7 and W.3.2 are met before unit 7; SL.3.4 is met before day 152; W.3.1 is bridged on day 86.
- Order elsewhere: unit 1's person, globe, town, region arc; unit 2's why rules, then levels, then deliberation; unit 4's
  local worked case before the four rotated nations; unit 5's daily life before slavery and sea trade last, with reasons.
  Slavery and the Triangular Trade are named plainly with enslaved people's own words.
- King Philip's War not placed, with the reason (grade 5 unit 1 teaches it from both sides); the frame allows that.
- Unit 2's day 25 checks four grade 1 rows at once. It is a lot for one opening, but they are one cluster (leaders,
  citizens, voting, roles) and one small-group reteach covers them; leave it.
- Candidate cells: each kept candidate sits on a named day with no added day; none is left open.

## Lens checklist, scope and sequence layer

| Lens line | Status |
|---|---|
| History in time order unless a reason is given | Missed in unit 5 (finding 2); met elsewhere |
| More than one account of contested events | Met (days 95, 100, 102, 106; two sources in each claim) |
| Values rule a to d | Met; day 84 sovereignty stated as law; day 78 present tense needs finding 4 |
| No role play or simulation of hard history | Met (named on days 102, 106 and the slavery days) |
| Native nations named, in the present, from their own pages | Met with the sensitivity notes; finding 4 |
| Informed action once, chosen by students | Met (days 153 to 157) |
| Inquiry arc to a claim from sources each unit | Met |
| Own-place method with a local thread | Met |
| No timers shown to students; paper path | Met (no timed task named) |

## Settled by the expert

| Item | Settled as |
|---|---|
| Unit 5 colony order | Swap inside the unit: St. Augustine 97, Jamestown 98 to 99, Plymouth 100 to 103, timeline 104, mid-unit 105 |
| Biography reads | ss3-biography with a short read on one existing day in units 2 to 6, no added day |
| Day 78 present tense | Name the Eastern Band in the day note |
| Check day codes | Every owned code and lettered part named on its unit's check day; product codes judged by rubric |
| Readiness versus retrieval | As written: readiness for grade 1 rows skipped across grade 2, retrieval for grade 2 rows |
| Held look-back days | None held; no unit shifts |
| Day 25's four-row readiness check | Leave as written |
| For the lead items 1 and 2 | Apply as written |

## For Cory

None. Nothing here moves a standard between units or changes scope, money, people or audience.

## What I could not judge

- Whether the five worked-case nations in unit 4 suit a given school's region; the own-place method leaves that to the
  unit plan.
- Facts on individual days (dates, names in the record for the Timucua leader); the day writer checks them.

## Sources

- S:\CurioClass\docs\courses\social-studies-grade-3\scope-and-sequence.md; data\plans\social-studies-grade-3\days.csv;
  docs\courses\social-studies-grade-3\frame.md; data\progressions\social-studies.csv; docs\courses\CALENDAR.md;
  data\plans\calendar.csv; data\standards\ma-hss-2018.txt; docs\courses\english-language-arts-grade-3\frame.md.
- docs\pipeline\briefs\sequence-read.md, sequence-write.md; docs\agents\EXPERT.md; docs\agents\lenses\social-studies.md;
  docs\ADOPTION-BAR-SUBJECTS.md; docs\courses\social-studies\STANDARD.md.
