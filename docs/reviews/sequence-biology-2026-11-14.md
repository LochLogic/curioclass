# Sequence read: Biology (grade 9), 2026-11-14

Expert cold read of the Biology scope and sequence, done to docs/pipeline/briefs/sequence-read.md with subject science and the bar docs/RUBRIC-SCIENCE.md. Read blind: no Codex read of this course was opened.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md, docs/pipeline/briefs/sequence-write.md, docs/lenses/science.md, docs/RUBRIC-SCIENCE.md.
- docs/courses/biology/frame.md, docs/courses/biology/scope-and-sequence.md, data/plans/biology/days.csv (all 160 rows, every column).
- data/progressions/science.csv (Biology rows and the grade 6 to 8 rows they assume), data/standards/ngss-pe-dimensions.csv for the 30 owned codes.
- data/plans/calendar.csv (grade 9 rows: Algebra I, ELA 9, World History I) and docs/CALENDAR.md.
- data/plans/science-grade-6, -7 and -8 days.csv, to find the last grade in which each assumed row is taught or assessed.
- The "Settled by the expert" tables and "Across the band" sections of docs/reviews/sequence-science-grade-*-2026-11-14.md, and the grade 8 frame's "Handed on to high school" lines.
- Gates: `scripts/plan.py check`, `scripts/frame.py calendar`, `scripts/stale.py check`. Biology passes all three. The only plan failure is english-language-arts-kindergarten (no scope file yet), from the Codex ELA run under way, not this course.

## Verdict

The sequence is well built: unit order follows the frame, each unit's model is revised at named points, course-level checks draw on earlier-unit contexts, every candidate is settled at zero added days, and the calendar citations are exact. It does not meet the readiness rule: it treats every grade 7 row as one grade idle, so seven units that open on grade 7 rows have no readiness check. Three end days ask for full performances on three or four expectations in one 50-minute period, and the course-level checks claim every part of six codes in a period. Fix those and the course is ready for unit plans.

## Findings

### 1. Serious: readiness is missing for every grade 7 row (sequence, frame; REPEAT yes; firm, except where marked)

What is wrong. The scope and sequence says the course has no readiness check, and the frame says "Every row and model Biology picks up was last used in grade 7 or 8, so the course has no readiness check"; its Models carried table calls matter-cycle, food-web and plate-model "idle one grade". Under the counted rule a row last used in grade 7 is due a readiness check in grade 9 (g+2). This is the same gloss fault already known in the Chemistry and Physics frames, and it is in Biology's frame too.

Why it matters. Grade 7 rows are the foundation of units 1, 3, 4, 8, 9 and 10. Without the check, a teacher learns of a missing grade 7 idea only from the end-of-unit assessment.

Rows the counted rule changes, with the exact fix (no day added; each check takes the last ten minutes of the named day, and the response goes inside the lesson that first uses the row):

| Unit | Rows (last used) | Check on | Response inside |
|---|---|---|---|
| 1 | s7-body-systems-food (grade 7; grade 8 days never name it, though s8-senses-brain assumes it in the progression). Likely. | Day 1, last ten minutes after the hook; set day 1's `assess` to `readiness` | Day 2 (the artery and tissue lesson) |
| 3 | s7-reactions-atoms, s7-food-molecules, matter-cycle (grade 7) | Day 25 (unit 2 respond) | Day 26 for reactions and matter cycle; day 34 for food molecules |
| 4 | s7-ecosystem-matter-energy, food-web (grade 7) | Day 46 (respond day between the units) | Day 47 |
| 8 | s6-plate-evidence (grade 7, grade 7 day 143), plate-model (grade 7) | Day 112 (unit 7 respond) | Day 113, and day 117 where the plate evidence is used |
| 9 | s7-biodiversity-solutions, s7-human-impact-design (grade 7) | Day 123 (unit 8 respond) | Day 124 |
| 10 | s7-population-consumption (grade 7) | Day 140 (unit 9 respond) | Day 141 or 142 |

Rows that stay retrieval because a grade 8 day teaches or assesses them: s7-photosynthesis (grade 8 day 112), s7-cell-respiration-growth (grade 8 days 108 and 112), s7-reaction-energy (grade 8 day 57), s7-resources-populations and s7-ecosystem-disruption (grade 8 day 145), and every s8-* row.

Also change: the scope and sequence's unit 8 argument for retrieval ("plate-model idle only in grade 8", and day 113's note that s6-plate-evidence is "maintained by s7-resource-distribution"). A row named in passing is not a use. Delete the "no readiness check" sentences, retitle the day notes on days 1, 26, 34, 47, 113, 124 and 141 from "retrieve" to "respond to day N readiness", and in the frame fix pass change the Seams wording and the Models carried "idle one grade" cells for matter-cycle, food-web and plate-model.

### 2. Moderate: three end days ask for too many full performances in one period (sequence; REPEAT new; firm on the rule, judgment call on the split)

What is wrong. Day 42 (unit 3) and day 74 (unit 5) each ask for full performances on four expectations, and day 93 (unit 6) on three, in one 50-minute period. sequence-write.md rule 2 says to spread them over the unit's last days, no day added.

Why it matters. With a short prompt per part of each code, four codes do not fit fifty minutes; teachers will cut parts, and the "every part" claim becomes false on the day it matters most.

Fix.
- Day 41 becomes end part 1 (HS-LS1-5, HS-LS1-7); day 42 is end part 2 (the other two codes).
- Day 73 becomes end part 1 (HS-LS2-1, HS-LS2-2); day 74 is end part 2.
- Day 92 becomes end part 1 (HS-LS3-1); day 93 is end part 2.
- Days 41, 73 and 92 are fluency consolidation days that the Shorter path already folds into days 40, 72 and 91, so the consolidation moves into those days in the full year too. The Shorter path then folds day 40 into 39, day 72 into 71 and day 91 into 90 in their place.

### 3. Moderate: course-level checks claim every part of every code (sequence; REPEAT yes, the K to 8 reads' finding; firm)

What is wrong. Day 45 lists six codes, day 44 two and day 156 six, each claiming all parts in one period. The check days also reuse the day 4 to 8 investigation record that day 12's end-of-unit assessment already credited.

Why it matters. Six full expectations cannot be met in fifty minutes, and crediting one record twice inflates the coverage claim.

Fix. As settled in grades 6 to 8: name the parts each check block samples, call the block a sample, and leave full coverage to the end-of-unit assessments. Drop the reuse of the day 4 to 8 record from day 45; use an unseen data set instead.

### 4. Moderate: unit 1's root option is the wrong mechanism, and the leaf-pore option has no safety cell (frame, sequence; REPEAT new; firm)

What is wrong. Unit 1 offers "roots growing toward water" as a feedback example for HS-LS1-3. Hydrotropism is a growth response, not a feedback holding an internal condition near a set point, so it is a weak fit for the code (S10 accuracy). Separately, the leaf-pore option on days 4 to 8 has no supplies or safety cells, though a nail polish peel brings solvent, ventilation and a microscope.

Why it matters. A wrong mechanism on the anchor investigation teaches the code's core idea incorrectly; the safety door (S5) needs every hands-on option covered.

Fix. Drop the root option (which also removes the seed-bag mould lines). Options become heart-rate recovery, or leaf pores with teacher-applied clear nail polish in a ventilated room and a microscope, or supplied micrographs as the no-kit path. Add those supplies and the solvent and ventilation controls to days 4 to 8 in days.csv, and change the unit 1 cell in the frame.

### 5. Minor: the seedling cohorts may not show a dry-mass gain (sequence; REPEAT new; judgment call)

Cohorts set on day 27 and harvested on day 36, about two weeks, will often show a smaller loss in the light than in the dark rather than a gain. Fix: the scope and sequence says that the likely class result is a smaller loss, keeps the supplied data set for the gain, and the unit plan pilots the timing.

### 6. Minor: unit 10's device need is named but not sized (sequence; REPEAT new; firm)

HS-ESS3-3 and HS-LS4-6 need a shared device, and the scope and sequence says so. Fix: the unit plan names the minimum (one device per group) and says the paper path is weaker evidence for the computational simulation.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| A row counts as used in a grade only where a day of that grade names it as taught, assessed, readiness or retrieval; a row only in the progression's assumes column, or named "maintained" in passing, is not a use | sequence-write.md rule 2 ("not where it is revisited or kept in use in passing") | data/plans/biology/days.csv |
| s7-body-systems-food gets readiness on day 1 though s8-senses-brain assumes it | No grade 8 day names it | data/plans/biology/days.csv day 1 |
| Rows last used in grade 8 (s7-photosynthesis, s7-cell-respiration-growth, s7-reaction-energy, s7-resources-populations, s7-ecosystem-disruption, s8-*) stay retrieval | Grade 8 days 57, 108, 112, 145 teach or assess them | data/plans/biology/days.csv |
| Readiness responses go inside the first lesson that uses the row; no reteach day added | Grade 7 settled practice; no days beyond the frame | data/plans/biology/days.csv |
| End days split only where three or more full performances share a period; two-code end days stay | Short prompt per part fits two codes in fifty minutes | data/plans/biology/days.csv days 41, 42, 73, 74, 92, 93 |
| Course-level checks are samples with the parts named | Same as grades 6 to 8 | docs/courses/biology/scope-and-sequence.md |
| No base text, no source map | Frame line 10: Curio Class's own; OpenSciEd units read for ideas only | docs/courses/biology/frame.md |
| Math leans (m6-*, m7-percent-problems, m7-compound-events) left as retrieval here | The cross-subject rule for math rows is raised for the lead in the Physics report's Across the band | docs/reviews/sequence-physics-2026-11-14.md |

## For Cory

None.

## What is right and should not be touched

- Unit order and ownership exactly as the frame; 160 days with check weeks 9, 16 and 32, and every calendar citation matching calendar.csv (Algebra I, ELA 9, World History I).
- Course-level checks draw the just-assessed skills from earlier-unit content and say so.
- All 20 candidate cells settled at zero added days; the Shorter path has ten fold-ins.
- Dimension elements are used, for example HS-LS3-3's nature of science element on day 89.
- The 9:3:4 Labrador ratio is correct. Sensitivity notes on bodies, health, deep time and the Lower Elwha Klallam account are in place.

## What I could not judge

- Crosscutting-concept models (system-model, structure-function, cause-effect, data-graph and the like) are not traced by id in the grade 6 to 8 days, so I did not apply the readiness rule to them; they recur every year.
- Whether the seedling timing in finding 5 works in a real classroom needs a pilot.
