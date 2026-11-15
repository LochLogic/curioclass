# Sequence read: Chemistry (grade 10), 2026-11-14

Expert cold read of the Chemistry scope and sequence, done to docs/pipeline/briefs/sequence-read.md with subject science and the bar docs/RUBRIC-SCIENCE.md. Read blind: no Codex read of this course was opened.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md, docs/pipeline/briefs/sequence-write.md, docs/lenses/science.md, docs/RUBRIC-SCIENCE.md.
- docs/courses/chemistry/frame.md, docs/courses/chemistry/scope-and-sequence.md, data/plans/chemistry/days.csv (all 160 rows, every column, including supplies and safety).
- data/progressions/science.csv (Chemistry rows and what they assume), data/standards/ngss-pe-dimensions.csv for the 21 owned codes.
- data/plans/calendar.csv (grade 10 rows: Geometry, ELA 10, World History II) and docs/CALENDAR.md.
- data/plans/science-grade-6, -7, -8 and biology days.csv, to find each assumed row's last use.
- The "Settled by the expert" tables and "Across the band" sections of docs/reviews/sequence-science-grade-*-2026-11-14.md.
- Gates: `scripts/plan.py check`, `scripts/frame.py calendar`, `scripts/stale.py check`. Chemistry passes all three. The only plan failure is english-language-arts-kindergarten (no scope file yet), from the Codex ELA run under way, not this course.

## Verdict

This is the strongest of the three high school sequences. It applies the counted readiness rule on its own, overriding the frame's retrieval wording for the grade 8 rows (days 56 and 112), and it books its end-day products honestly so no end day is overloaded. Two things need fixing: one grade 6 row is called "maintained through Biology" though no Biology day uses it, and the course-level checks claim every part of up to five codes in a period.

## Findings

### 1. Moderate: s6-insulator-design needs a readiness check before unit 7 (sequence, frame; REPEAT yes; likely)

What is wrong. The frame (Seams, line 60) and day 88 treat s6-insulator-design as "maintained skill, kept in use through Biology (bio-evaluate-impact-solutions)", so unit 7 opens with retrieval. No Biology day names the row; its last use is grade 7 day 25. Under the counted rule a row last used in grade 7 gets a readiness check in grade 10. "Kept in use" in passing is exactly the reading sequence-write.md rule 2 excludes.

Why it matters. Unit 7's solar device rests on controlling thermal energy with insulation; three grades on, many students will not hold it.

Fix. Day 87 (unit 6 respond): last ten minutes become the unit 7 readiness check on s6-insulator-design; set `assess` to `readiness`. The response goes inside day 89, whose sub-problems already include insulation. Change day 88's note from "retrieve maintained s6-insulator-design" to "day 87 readiness shapes support". In the frame fix pass, change line 60 to "last used in grade 7: readiness check".

The same fix pass should bring the frame into line with what the scope and sequence already does: s6-particle-temperature and s8-energy-transfer-argument (frame says retrieval; day 56 rightly checks them) and the earth-sun-moon and wave-model models (frame line 86 says "idle in grade 9 only... retrieval"; day 112 rightly checks them).

### 2. Moderate: course-level checks claim all-part prompts on too many codes (sequence; REPEAT yes, the K to 8 reads' finding; firm)

What is wrong. Day 54 claims all-part prompts on three codes, day 101 on four, day 156 on five and day 157 on four (fission, fusion, three decay types, conserved nucleons, the bond model, a thermal portfolio and a new plan, in one period).

Why it matters. No fifty-minute block holds that, so the claim will be false in use, and it hides which parts are actually sampled.

Fix. As settled in grades 6 to 8: each check day names the parts its block samples and calls itself a sample; full coverage stays with the end-of-unit assessments. On day 157, sample nuclear processes and the thermal account, and leave the carried portfolio as already credited on day 73.

### 3. Minor: s8-earth-sun-moon is assumed but no day names it (sequence; REPEAT new; firm)

The progression assumes s8-earth-sun-moon for unit 9; day 112's check names the earth-sun-moon model but not the row. Fix: add `s8-earth-sun-moon` to day 112's readiness note so the trace from progression to day is complete.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| End days 73 and 129 stay single days with three codes | Each day says which carried product stands for which code (thermal investigation and computational model on day 73; the forecast due day 129), as rule 2 allows | data/plans/chemistry/days.csv |
| Readiness on day 143 for s7-resource-distribution stays | Biology names it only in passing on day 113 ("maintained by"), which is not a use; the check is correct | data/plans/chemistry/days.csv day 143 |
| s7-food-molecules and s7-reactions-atoms stay retrieval | Biology days 26 and 34 use them, and still do once Biology adds its readiness checks | data/plans/chemistry/days.csv day 17 |
| Readiness on grade 8 math rows (scientific notation day 41, powers of ten day 130) stays | Consistent with the counted rule; whether math leans get readiness in every science course is raised for the lead in the Physics report | data/plans/chemistry/days.csv |
| Omitted frame options (steel wool and copper enrichment, the breath-through-straw demonstration) stay omitted | The frame marked them optional | docs/courses/chemistry/scope-and-sequence.md |
| No base text, no source map | Frame line 10: Curio Class's own, reference units for ideas only | docs/courses/chemistry/frame.md |

## For Cory

None.

## What is right and should not be touched

- The readiness placements on days 16, 31, 41, 56, 112, 130 and 143, each with its response inside a named lesson, and the reteach days the frame counts.
- Calendar citations all match calendar.csv (Geometry units 4 and 5, ELA 10 units 4 and 7, World History II units 2, 6, 9 and 11); check weeks 11, 20 to 21 and 32; the device report due day 97 (week 20) and the forecast due day 129 (week 26) avoid ELA's due weeks. Day 91's bridge for Geometry unit 5 being unfinished is the right same-year lean.
- Supplies and safety on every hands-on day are specific and conservative: rubbing alcohol with no flame, soft zip bags never rigid containers, plastic bottles never glass for freezing, sealed hand warmers only, hot tap water with teacher checks, oven gloves and no looking at the Sun for solar ovens.
- Course-level checks use earlier-unit contexts and do not repeat the unit assessment just given.
- Shorter path present with ten fold-ins; all candidate cells settled at zero added days.
