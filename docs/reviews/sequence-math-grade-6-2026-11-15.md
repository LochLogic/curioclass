# Sequence read: math grade 6, 2026-11-15

Expert cold read of the Curio Class math grade 6 scope and sequence, done under docs/pipeline/briefs/sequence-read.md with the bar in docs/RUBRIC-MATH-K8.md and the math lens. First of three middle school math reads; the grade 8 report carries "Across the band".

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/math-grade-6/scope-and-sequence.md in full; docs/courses/math-grade-6/frame.md (course in brief, units, course-level checks, cross-subject, for the lead).
- data/plans/math-grade-6/days.csv (160 rows) and source-map.csv (176 rows).
- data/progressions/math.csv, grade 5 to 8 rows; data/plans/math-grade-3/4/5/days.csv for last use of every assumed row.
- The base: Illustrative Mathematics grade 6, 1st edition (S:\CurioClass-sources\illustrative-math\grade-6), every lesson's title, teacher learning goals and student goals, and the unit overviews for optional lessons.
- Earlier reads: math kindergarten to grade 5 (2026-11-15), above all grade 5's "Across the band"; science grade 6, 7 and 8 (2026-11-14) for the math hand-offs.
- Gates: `plan.py check` passes for math-grade-6 (one failure elsewhere, geometry, another course being written now); `sequence.py check math-grade-6` 0 failures with one note (6.EE.A.1 "on no day", a frame punctuation fault, finding 6); `frame.py calendar` math weeks 16, 24, 32, no stagger break; `stale.py check` 0 failures.

## Verdict

A sound, base-faithful course: IM's eight units and lesson order are kept, the nine cuts are all IM-optional lessons, the readiness rule is applied exactly by grade number, and every end-of-unit window pairs one retained performance with short prompts and reuses it as collect once intends. The biggest risk is the year-end check: days 158 and 159 sample neither named fluency (6.NS.B.2, 6.NS.B.3), and day 159 lists 21 codes for 45 minutes. Fix the year-end check first; the rest is one standard part (6.SP.B.5a and b) assessed before any day teaches it, one mislabelled base lesson, and tidying.

## Findings

### 1. The year-end check does not sample either fluency standard (serious)

- What is wrong: check 3 day 158 lists 6.RP and 6.NS.A.1; day 159 lists 6.EE, 6.NS.C and 6.SP. Neither carries 6.NS.B.2 (multi-digit division) or 6.NS.B.3 (the four decimal operations). The last direct sample is check 2 on day 118.
- Why it matters: the band rule says every year-end check samples each fluency standard directly. Without it the day 160 hand-off to grade 7 has no current record of the two algorithms grade 7 unit 5 (rational arithmetic, decimal expansions) builds on. A writer following the CSV would build a check with no computation in it.
- Fix: in day 158, set the split to ratios and rates 10, percent 10, fraction division 15, and a 10-minute untimed independent station: about three long divisions (one with a zero in the quotient, one with a decimal quotient) and one of each decimal operation, no supplied work, recorded for the day 160 hand-off. Add 6.NS.B.2 and 6.NS.B.3 to day 158's codes and m6-long-division and m6-decimal-operations to its skills.
- Evidence: days.csv days 118, 158, 159, 160; frame "Fluency without a timer". Confidence: firm. LAYER: sequence. REPEAT: yes (grades 3, 4 and 5 year-end fluency).

### 2. Day 159 lists 21 codes for 45 minutes and claims a prompt for every part (moderate)

- What is wrong: day 159 lists 6.EE.A.1 to A.4 with A.2a to c, B.5 to B.8, 6.NS.C.6a to c, C.7a to d and three statistics codes, and its note says short prompts address every part of each listed code, in 20 + 15 + 10 minutes. That is about two minutes a code for 13-year-olds, with expansion, factoring, inequalities and absolute value among them.
- Why it matters: the plan will either be built with one-line items that show no reasoning or will overrun. Each of these codes already had its full end-of-unit assessment (days 116, 140, 156).
- Fix: list on day 159 only the codes it truly samples (proposal: 6.EE.A.3, 6.EE.A.4, 6.EE.B.7, 6.EE.B.8, 6.NS.C.7c, 6.NS.C.8, plus 6.SP.B.5 through the reused day 155 record), and say in the note and in the scope and sequence's check table that the year-end check samples named parts across units because each end-of-unit assessment covered its codes in full.
- Evidence: days.csv day 159; science band read finding 2 (the same overclaim in all six science checks). Confidence: likely. LAYER: sequence. REPEAT: yes.

### 3. 6.SP.B.5a and 6.SP.B.5b are assessed before any day teaches them (moderate)

- What is wrong: no teaching day carries 6.SP.B.5a (reporting the number of observations) or 6.SP.B.5b (what was measured, how, and in what units). They first appear on day 155, the end-of-unit performance, then day 156's prompts. Days 142 to 154 carry only 5c and 5d.
- Why it matters: "every lettered part carried by a day" and "nothing used before it is taught". The progression row m6-summarize-data says the full written summary is built in base lessons 17 and 18; lesson 17 sits inside merged day 154, which lists neither part.
- Fix: add 6.SP.B.5a and 6.SP.B.5b to day 154 (box plots), with a goal clause "and write the summary's opening: how many observations, what was measured, how and in what units", and to day 143 (dot plots), where the supplied data set is first described. No day added.
- Evidence: days.csv days 142 to 156; progression row m6-summarize-data. Confidence: firm. LAYER: sequence. REPEAT: new.

### 4. Day 40 credits base lesson 6.3.1 but teaches something else (low)

- What is wrong: the source map keeps 6.3.1 ("The Burj Khalifa") on day 40, whose base purpose is a rate per one in an unfamiliar context (minutes per window). Day 40's goal is comparing lengths in different units, carrying 6.RP.A.3d, which is 6.3.2 to 6.3.4's content. The day is ours in all but its credit, and the base's rate-per-one hook that joins units 2 and 3 is gone.
- Why it matters: the credit line will name a lesson the day does not use, and the source map reports base order kept where it is not.
- Fix: either follow the base (goal: "Use a rate per one to answer a question about a job in an unfamiliar setting", codes 6.RP.A.2, 6.RP.A.3b, retrieving day 26), or keep the day as written and mark 6.3.1 "cut" with the reason and day 40 "ours". Pick: follow the base. It keeps the unit opening on the idea the unit is named for, and conversion still has days 41 to 43.
- Evidence: base 6.3.1 learning goals; days.csv days 40 to 44; source-map.csv row 6.3.1. Confidence: firm. LAYER: base text. REPEAT: new.

### 5. Rebuilds placed on a unit's first day, far from their use (low)

- What is wrong: the factors and multiples rebuild sits after the hook on day 120 (unit 7's first day, a signed-number lesson), and GCF does not start until day 136. The scaled-axis rebuild sits on day 142 (unit 8's first day), three days before histograms on day 145.
- Why it matters: a first day should stay clean for the hook and the compelling question. A rebuild 16 days before its use will need re-teaching anyway, as the plan admits by adding a retrieval on day 136.
- Fix: move the array rebuild into day 136's core (replacing the retrieval note there and part of the first activity), and the scaled-axis rebuild into day 143's frequency-to-dot demonstration (its 10 minutes already teach frequency). Days 120 and 142 regain their 10 minutes for their own cores.
- Evidence: days.csv days 119, 120, 136, 141 to 145; the science grade 8 read praised a reteach on the day after the hook, never on day 1. Confidence: judgment call. LAYER: sequence. REPEAT: new.

### 6. Stale "provisional" notes and two stale frame lines (low)

- What is wrong: the readiness table and 23 day notes say grade 5 last use is "provisional", awaiting grade 5's days. Grade 5's days.csv now exists. I checked all 23 grade 5 rows: each is taught or assessed on grade 5 days, so retrieval is right for all of them, and m4-factors-multiples (last used grade 4) and m3-scaled-graphs (grade 3) rightly get readiness. The frame still says "a short readiness check opens each unit". The frame's unit 1 code list has "6.EE.A.1," with a comma, which the gate reads as a separate code.
- Fix: drop "provisional, day-level verification" and "Grade 5 day-level last use awaits its sequence" from the scope and sequence and days.csv notes, and close the "For the lead" item 1 as verified. In the frame, replace the readiness sentence with the brief's wording, and remove the stray comma after 6.EE.A.1.
- Confidence: firm. LAYER: process (notes), frame. REPEAT: yes (frame readiness wording in grades 3 to 5 and science 6 to 8).

## Checks the brief asks for

- **Source map against the base:** all 147 lessons in IM 6.1 to 6.9 have a row; titles match. Decisions: 124 keep, 14 merge (seven pairs), 9 cut, 29 ours. The nine cuts are all optional in IM (6.1.16, 6.5.2, 6.5.15 by their own lesson narratives; 6.9 is the optional unit); reasons hold. Base order is kept in every unit; day 40 is the one mislabel (finding 4). Columns follow the band layout (base_lesson, base_title, course, stretch, day, decision, reason, omitted_activities, source_url, license).
- **Departures:** the merges (6.1.1 with 6.1.2, 6.1.12 with 6.1.13, 6.5.1 with 6.5.3, 6.8.1 with 6.8.2, 6.8.3 with 6.8.4, 6.8.6 with 6.8.7, 6.8.16 with 6.8.17) each carry a 45-minute budget and name what is omitted. These are reasonable pairings: each pair shares one model. The tightest is day 145 (reading and building histograms in one core); it is acceptable because science 6 unit 5 has already taught histogram reading.
- **Our words:** I compared all 131 base-linked goal cells with their base lessons' titles, teacher goals and student goals. One copies a title sentence with "Explain why" added (day 46, "Explain why equivalent ratios have the same unit rates"); five more are close paraphrases (0.65 to 0.70 similarity: days 91, 108, 122, 136, 153) that keep only shared mathematical words. **Copy rate: 1 of 131 (0.8 percent).** Notes and source-map reasons are ours. Settled: day 46 becomes "Show that every ratio in an equivalent set gives the same amount per one."
- **Focus:** the scope and sequence reports 64.4 percent of minutes strictly major and 77.3 percent with connected geometry; by days 83 of 131 teaching days strictly, 102 with connected work. Connected-work counting was settled in the frame review. Holds.
- **Coherence into grade 7 and Algebra I:** ratio language, tables and plotted pairs (unit 2) feed grade 7 proportional relationships; one-step equations, equivalence and dependent variables (unit 6) feed grade 7 two-step equations and grade 8 functions; signed numbers stop before arithmetic, with the "no arithmetic with negative numbers" limit on every unit 7 day; tape diagram and hanger models carry forward. Percent change, tax and tip wait for grade 7 on every percent day.
- **Rigor:** every unit has understanding, fluency or practice, and application days; unit 8 has no fluency-kind day, which is right for statistics. Fluency 6.NS.B.2 and B.3: unit 5 explains the algorithms before practice (days 85 to 92), then three minutes of every opening from day 96 rotate long division and the four decimal operations, untimed. Only the year-end sample is missing (finding 1).
- **Readiness:** verified by grade number (finding 6): two readiness checks, both in the last ten minutes of the day before the unit (days 119 and 141), none on a first day; 23 grade 5 rows retrieved.
- **Assessments and end days:** every unit holds an end window of one retained application product plus a short-prompt day and one respond day. The extended tasks (days 16, 37, 57, 77, 93, 115, 139, 155) are base culminating lessons; each end day holds at most one. Mid-unit assessments in units 2, 3, 4, 6 and 7 follow IM's own and are not required by length (no unit is over 25 days); their response runs in the next two openings, counted once.
- **Collect once:** day 80 reuses days 77 and 78; day 118 reuses 115 and 116; day 159 reuses 155. Check forms change (error-analysis stations, decision-tree audit, resource case, plan audit) and draw on earlier units, and the scope and sequence says so.
- **Calendar:** checks on weeks 16, 24 and 32, the CALENDAR targets; no other subject's mid-year check shares days 80 or 118. Leans: science 6 ratios, rates and magnification come after math units 2 and 3; histograms (science days 116 to 135) and repeated-trial summaries (science days 1 to 51) come before math, and science carries its own bridge; the thermometer and social studies timeline precede unit 7, with bridges named on days 120 and 131. The S&S checks the hand-offs science 6 leans on and each holds.
- **Candidate cells:** all eight settled, each zero days or dropped with a reason.
- **Shorter path:** present, with a 45-minute plan and ten named fold-in days, none assessed; it names the eight performance days that must not fold.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | 64.4 percent strict minutes, 77.3 with connected work |
| Progression coherence | yes | limits kept (no signed arithmetic, no percent change) |
| Standard taught in part with no finishing day | partly | 6.SP.B.5a and b (finding 3) |
| Problems that join units | yes | tent formulas, paint plan, box volume, course-level cases |
| Fluency spaced and mixed | yes | year-end sample missing (finding 1) |
| Practices named | yes | all eight, each tied to a day |
| Models consistent | yes | tape, double number line, ratio table, hanger, area model, number line |
| Readiness by grade number | yes | verified against grade 3 to 5 days |
| End days not stacked | yes | one extended task per window |
| Collect once | yes | |
| Our words | yes | 0.8 percent |
| Source-map layout | yes | |

## What is right and should not be touched

- The two-day end window: one retained performance, then short independent prompts, then one respond day.
- "No arithmetic with negative numbers" on every unit 7 day, and the timeline note (no year zero, never subtract BCE labels).
- The 6.RP.A.3 parent record shared between units 2 and 3 and completed on day 58.
- Supplied, safe data in unit 8 and fictional prices and wages throughout.
- The untimed rotating algorithm practice from day 96.

## What I could not judge

- Whether the merged 45-minute cores hold in a real room; the unit plans must test them with actual items.
- Whether the tools named (equation-balance, function-table, histogram) exist in the tools file.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| All 23 grade 5 rows get retrieval; m4-factors-multiples and m3-scaled-graphs get readiness | Verified on grade 3 to 5 days | scope-and-sequence.md; days.csv notes |
| Day 158 time split 10 / 10 / 15 / 10 with an untimed algorithm station | Year-end fluency sample (finding 1) | days.csv day 158 |
| Day 159 samples six named codes plus the reused statistics record | 45 minutes; full coverage was on the end days | days.csv day 159 |
| Day 40 follows base 6.3.1 (rate per one) | Credit and base order | days.csv day 40; source-map.csv 6.3.1 |
| Day 46 goal reworded | Close to the base title | days.csv day 46 |
| Array rebuild to day 136, scaled-axis rebuild to day 143 | Rebuild where the skill is used; first days stay clean | days.csv days 120, 136, 142, 143 |
| The unit 8 project stays one period beside the social studies and ELA research weeks | Calendar fixed; one supplied-data period is light | days.csv day 155 (closes lead item 2) |

## For Cory

Nothing.

## Sources

- Illustrative Mathematics, grade 6, 1st edition (openly licensed pages), S:\CurioClass-sources\illustrative-math\grade-6: lesson order, learning goals, optional lessons.
- Common Core State Standards for Mathematics, grade 6 (data/standards), and the Progressions for ratios and proportional relationships, expressions and equations, the number system, and statistics (from memory for the limits named; consistent with data/progressions/math.csv).
- docs/RUBRIC-MATH-K8.md (EdReports criteria summary): focus, coherence, rigor indicators.

## For the source list

Nothing new.
