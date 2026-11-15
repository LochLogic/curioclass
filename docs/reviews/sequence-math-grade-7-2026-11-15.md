# Sequence read: math grade 7, 2026-11-15

Expert cold read of the Curio Class math grade 7 scope and sequence, done under docs/pipeline/briefs/sequence-read.md with the bar in docs/RUBRIC-MATH-K8.md and the math lens. Second of three middle school math reads; the grade 8 report carries "Across the band".

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/math-grade-7/scope-and-sequence.md in full; docs/courses/math-grade-7/frame.md (course in brief, fluency, units, course-level checks, cross-subject).
- data/plans/math-grade-7/days.csv (160 rows) and source-map.csv (182 rows).
- data/progressions/math.csv, grade 4 to 8 rows; data/plans/math-grade-4/5/6/days.csv for the last use of every assumed row.
- The base: Illustrative Mathematics grade 7, 1st edition (S:\CurioClass-sources\illustrative-math\grade-7), every lesson's title, teacher learning goals, student goals and the unit overviews for optional lessons.
- docs/courses/CALENDAR.md and data/plans/calendar.csv for grade 7; the science grade 7 read (2026-11-14) and the science and social studies grade 7 days for the leans.
- Earlier reads: math kindergarten to grade 6 (2026-11-15), above all grade 5's "Across the band".
- Gates: `plan.py check` passes for math-grade-7 (a failure elsewhere, a course another run is writing now); `sequence.py check math-grade-7` 0 failures; `frame.py calendar` math weeks 9, 24, 32, no stagger break; `stale.py check` 0 failures.

## Verdict

A careful, base-faithful course: IM's eight units and lesson order are kept, readiness is applied exactly by grade number, the equation unit gets the longest run, and the percent and signed-number units sit before the science and social studies days that lean on them. The weakest layer is the course-level checks: all four are critique or audit forms, they list 20 to 26 codes each, day 119 counts unmarked retrieval openings as check evidence, and the year-end pair never has students compute signed rationals or solve a two-step equation on their own. One standard part, comparing two populations (7.SP.B.4), is first met on its assessment day. Fix the checks first; the rest is one in-unit swap and tidying.

## Findings

### 1. The year-end check does not sample the fluency standards directly (serious)

- What is wrong: the frame names 7.NS.A.1 to A.3 (rational operations) and 7.EE.B.4a (both two-step equation forms) as the grade's fluency work. Day 158 is "a linked decision grid with representations supplied" and day 159 "an annotated claim-chain audit". In both, students judge or repair supplied reasoning. Nowhere in week 32 does a student add, subtract, multiply or divide signed rationals, or solve px + q = r and p(x + q) = r, with no supplied work.
- Why it matters: the band rule says every year-end check samples each fluency standard directly. Spotting an error in a supplied computation is a different skill from carrying it out. The day 160 hand-off to grade 8 then has no current independent record of the arithmetic that grade 8 unit 5 (multi-step linear equations, 8.EE.C.7b) and slope calculations rest on.
- Fix: on day 158, cut the grid to 30 minutes and add a 10-minute untimed independent station: about six signed rational computations (one of each operation, at least two with fractions or decimals, one long division to a repeating decimal for 7.NS.A.2d). On day 159, cut the audit to 30 minutes and add a 10-minute untimed station of four two-step equations, two in each form, one with a negative coefficient. Name both stations in the notes and in the scope and sequence's check table as "direct fluency sample, no supplied work".
- Evidence: days.csv days 158 to 160; frame fluency line; grade 5 read "Across the band" and grade 6 finding 1. Confidence: firm. LAYER: sequence. REPEAT: yes.

### 2. The course-level checks overclaim coverage, all use critique forms, and day 119 marks retrieval openings (moderate)

- What is wrong: day 119 lists 26 codes, days 158 and 159 list 20 each, and day 45 lists 7; every note says "a short prompt or named saved product for every part of every listed code" inside 40 minutes. Day 119 also names "day 109 scale, day 112 proportional and day 115 circle records" as the units 1 to 3 portion: these are the 5-minute opening retrieval tasks on those days, which the plan tells teachers to "retain" for the check. All four forms (representation critique, branching solution audit, decision grid, claim-chain audit) ask students to judge supplied work.
- Why it matters: about 90 seconds a code cannot show reasoning. The glossary defines a retrieval task as not a check and not marked; turning three openings into scored evidence makes them a check in disguise, given in the middle of the unit 6 lessons, and it hides that day 119 itself never samples units 1 to 3. Four critique forms in a row also leave the year with no course-level task where a student produces a solution from a blank page.
- Fix: (a) on each check day list only the codes it samples, and say in the note and the check table that each end-of-unit assessment covered its codes in full, so the course-level check samples named parts across units. Proposals: day 45 7.RP.A.2a, 7.RP.A.2c, 7.G.A.1, 7.G.B.4; day 119 7.RP.A.3, 7.NS.A.2, 7.NS.A.3, 7.EE.B.3, 7.EE.B.4b, 7.G.A.1, 7.RP.A.2d; day 158 7.RP.A.2b, 7.RP.A.3, 7.NS.A.1 to A.3 (station), 7.EE.B.3; day 159 7.EE.B.4a (station), 7.EE.A.1, 7.G.B.5, 7.SP.C.8b, 7.SP.B.4, with the day 155 and 156 records reused for the rest of unit 8. (b) Drop the "retain for course-level check 2" sentences from days 109, 112 and 115; on day 119 give 10 minutes to two short independent scale and proportional prompts instead. (c) Keep the critique forms, and let the stations in finding 1 and the day 119 prompts be the independent production parts.
- Evidence: days.csv days 45, 109, 112, 115, 119, 158, 159; GLOSSARY "retrieval task". Confidence: firm on (b), likely on (a). LAYER: sequence. REPEAT: yes (grade 6 finding 2; science band finding 2).

### 3. 7.SP.B.4 (comparing two populations) is first met on its assessment day (moderate)

- What is wrong: IM teaches comparison of two populations from samples in 7.8.18 and 7.8.19. The plan uses 7.8.18 as day 155's assessment and cuts 7.8.19, a required lesson, for time. Day 153 carries 7.SP.B.4 but estimates one population's center. No day before 155 has students compare two populations using sample centers and variability.
- Why it matters: "nothing used before it is taught". The comparative inference that 7.SP.B.4 names is the part of the standard that grade 8 and high school statistics build on, and day 155 would assess it cold.
- Fix: in-unit swap, no day added. Fold day 147 (finding outcomes in a sample space, already a shorter-path fold) into day 146; move days 148 to 154 down one; on the freed day 154 teach base 7.8.18 (two populations, both mean with MAD and median with IQR, decide whether the difference is meaningful). Day 155 stays the assessment with new items in a changed context. Keep 7.8.19 cut and update its reason to "comparison taught on day 154 from 7.8.18". Add 7.SP.B.3 and 7.SP.B.4 to the new day 154.
- Evidence: days.csv days 146 to 155; source-map rows 7.8.18, 7.8.19; base 7.8.18 and 7.8.19 learning goals. Confidence: firm. LAYER: sequence. REPEAT: new.

### 4. Rebuilds placed on a unit's first day (low)

- What is wrong: day 69 (unit 5's first day, the temperature hook) reserves 10 minutes for the fraction refresher from the day 68 readiness check; day 121 (unit 7's first day) reserves 10 minutes for angle-addition rebuilding from day 120.
- Why it matters: a unit's first day stays clean for the hook and the compelling question (Cory, 2026-11-14). Fractions are first needed in signed sums on day 71; additive angles on day 122.
- Fix: move the fraction refresher to day 71's opening (the first signed sums with fractions) and the angle-addition rebuild to day 122 (complementary and supplementary angles, where it is used). Days 69 and 121 regain their 10 minutes.
- Evidence: days.csv days 68 to 71, 120 to 122. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 6 finding 5).

### 5. 7.G.A.3 and 7.EE.A.2 each rest on one teaching day (low)

- What is wrong: 7.G.A.3 (plane sections) is taught only on day 131, and day 137's assessment reuses day 131's slice explanation, so the same single product is the only evidence. 7.EE.A.2 (rewriting to show meaning, such as a + 0.05a = 1.05a) is taught only on day 116.
- Why it matters: one exposure and no independent assessment item is thin for any owned part, and 7.EE.A.2 is the hinge between unit 4 percent multipliers and grade 8 linear expressions.
- Fix: on day 137 add one short new slice prompt (a slanted cut of a prism) beside the reused record. Tag 7.EE.A.2 on days 52 and 55, where percent increase is written as one multiplier, and add a sentence there: "write the change both ways and say what each form shows".
- Evidence: days.csv days 52, 55, 116, 131, 137. Confidence: likely. LAYER: sequence. REPEAT: new.

### 6. The source map is in a different layout from grade 6's (low)

- What is wrong: grade 7's source-map.csv has columns base_lesson, source_url, stretch, day, decision, reason. Grade 6 uses base_lesson, base_title, course, stretch, day, decision, reason, omitted_activities, source_url, license; grade 8 has a third layout.
- Why it matters: the credit pipeline and any gate that reads omitted activities or licence lines will need three parsers, and a reader cannot see the base title beside the decision.
- Fix: rewrite grade 7's source map in the grade 6 layout (add base_title, course, omitted_activities and license; the omitted activities are already in the reason text). Lead call for one band layout (see grade 8 "Across the band").
- Confidence: firm. LAYER: process. REPEAT: new.

## Checks the brief asks for

- **Source map against the base:** every lesson in IM 7.1 to 7.9 has a row. Decisions: 121 keep, 4 merge (7.1.3 with 7.1.4, 7.1.11 with 7.1.12), 20 cut, 37 ours. The cuts are IM-optional lessons, the optional unit 7.9, and one required lesson, 7.8.19 (finding 3). Every reason is given and holds apart from 7.8.19.
- **Base order:** kept in every unit; no lesson out of order. Our teaching days are 14, 25, 48, 62, 83 and 88, each a short bridge that the base lacks (ratio-table tests, fractional rates, error intervals, the finite-remainder day), and each is placed after what it uses.
- **Our words:** I compared all 123 base-linked goal cells with their base lessons' titles, teacher goals and student goals. Highest similarity 0.59; none copies a title or goal sentence. **Copy rate: 0 of 123 (0 percent).**
- **Focus:** 66.9 percent of minutes on major clusters by the plan's own per-day allocation, which counts each minute once and credits no major minutes in earlier-grade retrieval. Above the 65 percent line on a strict count; holds.
- **Coherence into grade 8 and Algebra I:** scale factors (unit 1) feed grade 8 dilations; k as unit rate in tables, graphs and y = kx (unit 2) feeds slope; percent multipliers (unit 4) feed linear expressions; signed rational arithmetic (unit 5) and both two-step forms with inequalities (unit 6) feed grade 8 multi-step equations and systems. Cylinders, cones, spheres and congruence criteria are rightly left for grade 8.
- **Rigor:** each unit has understanding, practice and application days. Fluency for 7.NS.A.1 to A.3 and 7.EE.B.4a: explained first (days 69 to 91 and 92 to 102), then a 5-minute untimed mixed opening on most later days, no student timer. Only the year-end sample is missing (finding 1).
- **Readiness:** verified by grade number. m4-angle-concepts and m4-protractor (last used grade 4) checked on day 1 after the hook, rebuilt on day 2. m5-add-sub-unlike and m5-fraction-add-sub-problems (grade 5) checked in the last 10 minutes of day 68. m4-additive-angles, m5-shape-hierarchy and m5-volume-additive checked on day 120. Every m6 row is retrieved; m4 angle rows retaught on days 2 and 3 are rightly retrieved, not checked, on day 121. Rebuild placement is finding 4.
- **Assessments and end days:** every unit has an end window; each end day holds at most one extended task plus short items. Unit 6 (27 days) has its mid-unit equation assessment and respond day before inequalities. Response time is counted once.
- **Collect once:** end-of-unit days reuse the construction, slicing and simulation records instead of collecting them again; check forms differ from the preceding ten days. The misuse is day 119's retrieval reuse (finding 2).
- **Checks that do not repeat:** day 119 draws unit 6 items from unit 4 and 5 contexts and the scope and sequence says so; day 45 does the same for unit 3.
- **Standards in full:** every lettered part is carried by a day except the comparative half of 7.SP.B.4 (finding 3).
- **Days by load:** equations 27, signed numbers 23, percent 22, proportional relationships 21, probability and sampling 19, geometry 18, scale 12, circles 11. These follow what each unit owns.
- **Calendar:** checks on weeks 9, 24 and 32, the CALENDAR.md targets. Leans: science 7 proportional tables (science days 24 to 41) come after math days 13 to 20; science percent (days 129 to 158) comes after math finishes percent on day 68; social studies time zones (days 78 to 86) meet math's signed-number bridge on day 75 first. Each holds.
- **Candidate cells:** all settled, each at zero days or dropped with a reason.
- **Shorter path:** present, with a 45-minute plan and ten named fold-in days, none assessed; day 147 is one of them, which is why finding 3 can use it.
- **Stale notes:** none found beyond the gate.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | 66.9 percent of minutes, counted once |
| Progression coherence | yes | grade 8 limits kept |
| Standard taught in part with no finishing day | partly | 7.SP.B.4 (finding 3) |
| Problems that join units | yes | percent with signed change, scale with circles, rates in probability |
| Fluency spaced and mixed | yes | year-end sample missing (finding 1) |
| Practices named | yes | all eight, tied to days |
| Models consistent | yes | ratio table, tape, number line with directed moves, zero pairs, balance |
| Readiness by grade number | yes | verified against grade 4 to 6 days |
| End days not stacked | yes | one extended task per end day |
| Collect once | partly | retrieval openings used as check evidence (finding 2) |
| Our words | yes | 0 percent |
| Source-map layout | no | finding 6 |

## What is right and should not be touched

- The base order with six short bridge days of our own, each placed after what it uses.
- Two-step equations before inequalities, with the mid-unit assessment and respond day between them.
- The explicit finite-remainder day finishing 7.NS.A.2d before mixed applications.
- The per-day major-work allocation that counts each minute once.
- Neutral contexts: supplied prices, no gambling, no body measures, no family money; paper models instead of food cutting.

## What I could not judge

- Whether the 45-minute cores hold in a real room; the unit plans must test them.
- Whether the digital construction tool named on days 128 to 130 exists in the tools file.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Day 158 and 159 each gain a 10-minute untimed independent fluency station | Year-end fluency sample (finding 1) | days.csv days 158, 159 |
| Check days list only sampled codes, with the named lists in finding 2 | 40 minutes; full coverage was on end days | days.csv days 45, 119, 158, 159; scope-and-sequence.md check table |
| Retrieval openings on days 109, 112, 115 are not retained as evidence | Glossary: retrieval is not marked | days.csv days 109, 112, 115, 119 |
| Day 147 folds into 146; 7.8.18 taught on day 154; 7.8.19 stays cut | 7.SP.B.4 taught before assessed | days.csv days 146 to 155; source-map.csv |
| Fraction refresher to day 71; angle rebuild to day 122 | First days stay clean | days.csv days 69, 71, 121, 122 |
| 7.EE.A.2 tagged on days 52 and 55; one new slice prompt on day 137 | Single-day standards | days.csv days 52, 55, 137 |
| Source map moves to the grade 6 layout | One band layout | source-map.csv |

## For Cory

Nothing.

## Sources

- Illustrative Mathematics, grade 7, 1st edition (openly licensed pages), S:\CurioClass-sources\illustrative-math\grade-7: lesson order, learning goals, optional lessons.
- Common Core State Standards for Mathematics, grade 7 (data/standards), and the Progressions for ratios and proportional relationships, the number system, expressions and equations, and statistics and probability (from memory for the limits named; consistent with data/progressions/math.csv).
- docs/RUBRIC-MATH-K8.md (EdReports criteria summary): focus, coherence, rigor indicators.

## For the source list

Nothing new.
