# Expert cold read: course frame, Statistics (2026-11-16)

Brief: docs/pipeline/briefs/frame-read.md, course `statistics`, subject math, bar docs/RUBRIC-MATH-HS.md. Read cold; I did not write the frame or the rows. Report only; no other file edited.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-HS.md, AGENTS.md.
- The frame docs/courses/statistics/frame.md in full, its row in data/plans/frames.csv (10 units, 160 days, 50 minutes, 5 a week, 32 weeks). The course has no data/plans/statistics/ folder yet, so the Source map is the table inside the frame.
- All 22 stat- rows of data/progressions/math.csv, and the grade 10 and 11 rows they assume (geo-addition-rule, geo-conditional-independence, the four alg2- statistics rows, alg2-combining-functions-models).
- data/standards/curio-math-electives.txt (CUR-ST.1 to CUR-ST.21), the S-CP.B.9 and S-MD lines of data/standards/ccss-math-standards.txt, data/plans/later.csv L25 and L49, the statistics row of data/courses.csv.
- Beside it: docs/courses/algebra-ii/frame.md (unit 7 in full), docs/courses/algebra-i/frame.md (unit 1), docs/courses/precalculus/frame.md and docs/courses/calculus/frame.md (seams, L49 and stale-line proposals); the chem-reaction-rates and chem-climate-forecast rows of data/progressions/science.csv; a grep of every progression file for leans on stat-, CUR-ST, S-MD or S-CP.B.9 (none outside math.csv).
- The base-text scout notes (side-session notes, base-text-scout-2026-11-16.md, section 2 and the OpenStax licence table) for the Source map check.
- openstax.org pages for the book's labs 1.5, 2.8, 4.8, 6.3, 7.4, 9.6, 10.5, 11.7 and 11.8 (read only), to see what each lab asks students to collect.
- docs/reviews/frame-algebra-ii-2026-11-14.md for shape, and the earlier frame reads by grep for repeat kinds.
- Gates: `python -X utf8 scripts/plan.py check` gives statistics 0 failures (10 units, 160 days, 151 in units, 9 for checks and respond days); `python -X utf8 scripts/stale.py check` gives 0 failures. Unit days equal the row loads exactly (19, 13, 13, 9, 19, 9, 24, 19, 13, 13 = 151), and the loads include each unit's end-of-unit assessment and respond day, as in the Calculus frame.

## Verdict

The frame is sound in shape: every stat- row sits in one unit, every CUR-ST code, S-CP.B.9 and all nine S-MD codes (with S-MD.B.5a and S-MD.B.5b) are owned in full, the unit order never uses a method before it is taught, the seams with Algebra I, Geometry and Algebra II are complete, and its answer to L49 is the right one. The biggest risk is statistical honesty in the data and labs: several picks would have students run inference that the data cannot support (census population tables and a complex national survey treated as simple random samples, a county population too skewed for the central limit theorem to show at classroom sample sizes), and six base-text labs kept "as is" collect exactly the personal data (money, possessions, language at home, gender) the frame's own sensitivity rules forbid. The one change that matters most is to name, for every inference unit, a data set that really is a random sample or a randomised experiment (supplied random samples from the census bureau's public-use records, with the full-table value kept as the known truth to check an interval against), and to mark the six labs "split" with supplied data.

## Findings, most serious first

### 1. Six base labs kept unchanged collect students' personal data (serious; firm)

LAYER base text. REPEAT new.

What is wrong: the Source map marks these labs "keep" with no note, but read at source each one has students collect data the frame's Sensitivity reads bullet rules out ("no task asks about a student's family money", "no student is asked where they or their family were born", "Students never share their own sensitive data"):
- 2.8 Descriptive statistics (unit 1): each student's number of pairs of shoes, surveyed across 30 classmates (a wealth marker).
- 7.4 Pocket change (unit 6): students count the money in their pockets and survey 30 classmates' change.
- 9.6 Single mean and single proportion (unit 8): whether each student speaks a language other than English at home; pairs of jeans owned; hours of television.
- 10.5 Two means and two proportions (unit 8): shoes owned compared by sex; buying packets of candy; a day's newspaper stock pages.
- 11.7 Goodness of fit (unit 9): grocery receipt totals collected from 30 shoppers leaving a supermarket or from cashiers.
- 11.8 Test of independence (unit 9): each classmate's gender against favourite snack.
The frame was careful with 6.4, 8.5, 8.6 and 12.6 (left out or split for the same reasons), so these read as missed, not chosen.

Why it matters: a scope writer adapts "keep" rows as they stand; the days would ask about family money, home language and gender, and 11.7 sends students to approach strangers. The sensitivity agent would catch some of it late, after days are written.

Evidence: openstax.org/books/statistics pages 2-8, 7-4, 9-6, 10-5, 11-7, 11-8 (read 2026-11-16).

Fix: change each row's Decision to "split" and its Notes to:
- 2.8: "Kept with a supplied data set (unit 1's park visits or commute times); the base's survey of shoes owned is cut."
- 7.4: "Kept with a supplied population (a jar of coins counted by the teacher, or Old Faithful intervals); the base's count of students' own pocket money is cut."
- 9.6: "Kept with supplied data; the base's surveys of home language, clothes owned and television hours are cut."
- 10.5: "Kept with supplied data (unit 8's coin masses and seat-belt counts); the base's shoe survey by sex, candy purchase and stock pages are cut."
- 11.7: "Kept with a supplied count (Mendel's peas, or a die rolled in class); the base's collection of shoppers' receipts is cut."
- 11.8: "Kept with a supplied census sample (finding 2); the base's survey of classmates' gender is cut."
Add one line to the Source map's opening paragraph: "No lab collects students' own money, possessions, home language, gender, body or home location; such steps are cut and supplied data used."

### 2. Inference run on population tables and a complex survey as if they were simple random samples (serious; firm)

LAYER frame. REPEAT new.

What is wrong: three inference picks do not meet the conditions the course teaches.
- Unit 7: "supplied census place-of-birth tables for a state" for a one-proportion interval. A published census table is an estimate built from hundreds of thousands of responses (or a full count), already weighted, and published with its own 90 percent margin of error. A student who puts its percent and its count into the one-proportion formula gets an interval a fraction of a point wide and a wrong idea of what the published margin means.
- Unit 7: the national seat-belt use survey. It is a multistage probability sample of road sites, observed vehicles, with design-based standard errors; vehicles at one site are not independent. Treating its published percent as a simple random sample of n drivers breaks the independence condition the row itself lists ("random sample, large enough counts, independence").
- Unit 9: "census tables of commuting mode by region for independence". Counts in the millions make every chi-square statistic huge and every p-value effectively zero; the counts are weighted estimates, not observed counts; and region against commuting mode is homogeneity of populations if anything, not independence in one sample.

Why it matters: the frame promises accuracy about conditions (Focus bullet: "what a confidence level means, what a p-value does and does not say"). These days would teach that conditions are a box to tick. A college instructor would mark it down; so would an adoption reviewer reading the unit assessments.

Evidence: from memory, firm: census survey tables are published with 90 percent margins of error; the census bureau publishes public-use microdata samples (person and household records) for exactly this kind of teaching; the national seat-belt survey reports design-based standard errors.

Fix (Real data bullet and units 7 and 9 cells):
- Unit 7, replace "supplied census place-of-birth tables for a state" with "a supplied simple random sample of about 200 person records for one state, drawn from the census bureau's public-use microdata, with the published state percent kept as the known value each class interval is checked against".
- Unit 7, seat belts: "the national seat-belt survey's published estimate and margin, read beside a supplied simple random sample of observations from one site list, with a note on why a clustered survey's margin is wider than the simple formula gives". If no such sample can be supplied, keep the survey for reading published margins only and run the procedures on the microdata sample.
- Unit 9, replace "supplied census tables of commuting mode by region for independence" with "a supplied simple random sample of about 400 worker records from the public-use microdata, commuting mode by region (homogeneity, one sample per region) and commuting mode by a second variable in one sample (independence)".
- Add to unit 7's What students learn: "why a published survey margin differs from the simple formula when the sample is clustered or weighted".

### 3. The central limit theorem shown on a population too skewed to show it (moderate; firm on direction, likely on size)

LAYER frame. REPEAT new.

What is wrong: unit 6 uses "the strongly skewed populations of all US counties ... whose sample means turn normal". County populations are among the most skewed real populations there are (a largest county near 10 million, a median near 25,000; skewness well above 10, from memory). The skewness of a sample mean is about the population's divided by the square root of n, so at the n of 25 to 50 a class can draw, the simulated means stay plainly right-skewed. On the paper path (drawing samples of 30 from a printed list of over 3,000 rows and averaging by hand) it is worse: few samples, slow work.

Why it matters: the hinge day of the course would show a picture that contradicts the theorem as stated, unless the teacher knows to turn it into the "how large is large enough" lesson.

Fix: settled below (Settled by the expert 1): the "turns normal" demonstration uses the uniform parent (5.2) and Old Faithful's two-humped intervals (unit 1's data), where means of 10 to 30 look normal; the county populations stay as the deliberate counter-case, with the unit 6 cell reading "the strongly skewed populations of all US counties, where samples of 30 are not yet large enough, so students see that 'large enough' depends on the shape".

### 4. The investigation's inference may rest on a convenience sample, and ruler-drop clashes with the body rule (moderate; likely)

LAYER frame. REPEAT new.

What is wrong: unit 10 asks each student to "choose and carry out an inference procedure", and the suggested classmate surveys (reaction time by ruler drop, estimating 30 seconds, letters in a word) give a convenience sample of one class, so the conditions for inference to any population are not met. Separately, the Source map leaves out 6.4 because "students never measure or share their bodies", yet the investigation suggests reaction time by ruler drop, a body-performance measure that a student with a motor disability may not want shown.

Why it matters: the report's grade rests on a procedure whose conditions the student cannot honestly claim; the rubric writer and the teacher will not know which designs to approve.

Fix (unit 10 cell and The investigation bullet): add "An approved plan is one of two kinds: a randomised experiment within the class (for example, two ways to memorise a list, assigned at random; the conclusion is about these students and the treatments), or a random sample from a public data set; the report states its scope of inference." Replace "reaction time by ruler drop" with "recall of a list after one of two study methods", and keep the rule that students never measure or share their bodies.

### 5. The owned outcomes are thinner than the rows on what a college course grades hardest (moderate; likely)

LAYER standard. REPEAT new.

What is wrong: the outcomes are in Curio Class's own words, at first-year college level, and cover a full one-semester introductory course; but the interpretive clauses the frame promises sit only in rows and frame prose, not in the owned code:
- CUR-ST.13 has no "what a p-value does not say" and no statistical against practical significance, though the Focus bullet promises the first and both are central to a college course.
- CUR-ST.15 drops "and say what each design lets you conclude", which the row and unit 7 carry.
- CUR-ST.16, CUR-ST.18 and CUR-ST.20 say "build" an interval but never "interpret" it in context (CUR-ST.12 does).
- CUR-ST.2 says "describe" but not "display" (dot plots, histograms, stemplots, box plots), and CUR-ST.3 omits density curves, which unit 1 teaches (base 5.1).
- No outcome names the link between a two-sided test and an interval.

Why it matters: assessments are written to the code. What the code does not say is the first thing cut when a unit runs long, and these are the clauses that separate understanding from procedure (rubric 2a).

Fix (data/standards/curio-math-electives.txt, version 2, and the matching row notes): CUR-ST.2 begins "Display and describe the distribution ..."; CUR-ST.3 adds "using density curves as areas"; CUR-ST.13 adds "say what a p-value does not tell (the probability the null hypothesis is true, or the size or importance of an effect), and tell statistical from practical significance"; CUR-ST.15 adds "and say what each design lets you conclude"; CUR-ST.16, CUR-ST.18 and CUR-ST.20 add "and interpret it in context"; CUR-ST.18 adds "and explain how a two-sided test at a level and an interval at the matching confidence agree". Each widens no unit's scope: the rows already teach it.

### 6. Units 4 and 6 are tight for what they own once assessment days are counted (moderate; judgment call)

LAYER frame (and progression loads). REPEAT new.

What is wrong: loads include each unit's end-of-unit assessment and respond day. Unit 6 (9 days) leaves 7 teaching days for two sampling distributions, the central limit theorem, bias against variability, and simulations on paper as well as by technology. Unit 4 (9 days, 3 of them review of Geometry) leaves about 4 new days for the law of large numbers, harder rule problems, permutations and combinations. Unit 1 (19 days) carries by its rows about 7.5 review days (2 + 3.5 + 2), more than the "about 6" the frame states, so the frame's "about 14 review days" total is right but unit 1's share is understated. Common one-year pacing for this content (from memory) gives the sampling distribution unit 10 to 12 days with its assessment.

Why it matters: the frame itself calls unit 6 the hinge; a scope writer squeezing it will cut the paper simulation first, which is the paper path.

Fix: move 2 days from unit 1 to unit 6 (unit 1 to 17 with about 5.5 review days, unit 6 to 11), changing stat-quantitative-distributions' load to "about 6 days; about 2.5 review" and stat-position-normal's to "about 6 days; 1 reviews Algebra II unit 7", and stat-sampling-distributions' to "about 11 days". Leave unit 4 at 9 but name in its cell "about 4 new days: law of large numbers 1, counting 2, compound problems 1". Correct the unit 1 cell to the review count the rows give. This moves days between units, not standards, so the lead can make it.

### 7. Chemistry's rate data do not suit a linear slope test (moderate; likely)

LAYER frame. REPEAT new.

What is wrong: unit 9 uses "Chemistry's rate data" for inference on a slope. chem-reaction-rates collects class data on tablet reactions against temperature or concentration: a handful of chosen x values, often one run each, and a rate that grows roughly exponentially with temperature. The linearity and equal-spread conditions fail unless the rate is logged, and with five points the test means little.

Fix (unit 9 cell and the Real data bullet): "Chemistry's rate data, with the rate logged as in unit 2, as a conditions-checking case where a straight-line test on the raw data would mislead" or drop it from the slope work and keep it in unit 2's transformations. Old Faithful (eruption length against the next wait) stays as the main slope case, with one teacher note that successive eruptions are not fully independent, so the class names this as a limit.

### 8. Unit 8's data picks are weak for inference (minor; likely)

LAYER frame. REPEAT new.

What is wrong: the coin masses differ by design (the metal changed), so the two-sample test's answer is known before it starts, and the frame names no source (weighed in class with what scale, or a supplied set; 1982 itself has both kinds). The paired temperatures use one day's high at each station, which is mostly weather noise, from stations not drawn at random.

Fix: settled below (Settled by the expert 5 and 6).

### 9. The Source map's opening names two moves; there are more (minor; firm)

LAYER base text. REPEAT new.

What is wrong: the opening says the base order is kept "with two moves" (producing data to unit 3, regression to unit 2). The map also moves proportions before means (8.3 and 10.3 to unit 7 ahead of 8.1, 8.2, 10.1 in unit 8), splits chapter 5 (5.1 to unit 1, 5.2 and 5.4 to unit 6) and splits chapter 9 across units 7 and 8. The reasons exist in the Units table but the brief asks the map to name them.

Fix: replace "with two moves for teaching" through "joins unit 9." with: "with four moves for teaching: producing data (1.2, 1.4, 1.6) comes in unit 3 after both describing units; regression (chapter 12) moves up to unit 2 so the descriptive half is whole before probability, its inference section joining unit 9; density curves (5.1) join the normal model in unit 1 and the uniform distribution (5.2, 5.4) serves unit 6; and proportions (8.3, 9.1 to 9.5, 10.3) come before means (8.1, 8.2, 9.6, 10.1, 10.4) because their sampling distribution is simpler and the logic of interval and test is built once (unit 7)."

### 10. The week line leaves out the investigation's held days (minor; firm)

LAYER frame. REPEAT yes (week drift found in earlier frame reads, for example Geometry and ELA grades 9 and 10).

What is wrong: the Cross-subject weeks ("unit 4 weeks 10 to 12 ... Check 2 week 18 ... Check 3 weeks 29 to 30, unit 10 weeks 30 to 32") ignore the 4 held investigation days. Counted in order (unit 1 days 1 to 19, unit 2 to 32, unit 3 to 45, Check 1 46 to 48, held 49 to 50, unit 4 51 to 59, unit 5 with 2 held days 60 to 80, unit 6 81 to 89, Check 2 90 to 92, unit 7 93 to 116, unit 8 117 to 135, unit 9 136 to 148, Check 3 149 to 151, unit 10 152 to 160), unit 4 is weeks 11 to 12, Check 2 weeks 18 to 19, unit 7 weeks 19 to 24, Check 3 weeks 30 to 31, unit 10's last 9 days weeks 31 to 32. (Finding 6 shifts no boundary after unit 6.)

Fix: replace the week sentence with the counted weeks above, and Check 2's "(week 18)" with "(weeks 18 to 19)", Check 3's with "(weeks 30 to 31)".

### 11. Three frames propose three different replacements for the same stale lines (minor; firm)

LAYER process. REPEAT new.

What is wrong: docs/RUBRIC-MATH-HS.md's "Precalculus, Statistics and Calculus are not active courses ..." line, docs/agents/lenses/math.md's "Past Algebra 2 has no base text and no progression" and docs/sources/BASE-TEXTS.md's "Math past Algebra 2 (precalculus, statistics, calculus)" are stale (stale.py does not catch them), and the Statistics (For the lead 2 and 3), Precalculus (For the lead 2) and Calculus (For the lead 3 and 6) frames each give different replacement text. Applied in turn, each would overwrite the last.

Fix: the lead writes each line once, after all three frames are read. For BASE-TEXTS.md: "Our own (no base text): none in math; Precalculus, Statistics and Calculus each have a base text in the table above." For the lens: "Past Algebra 2: Precalculus, Statistics and Calculus have progression rows (pc-, stat-, calc-, grade 12), Curio Class's own outcome list (data/standards/curio-math-electives.txt) and a base text named in each frame." For the rubric: see "The L49 answer" below. Each frame's For the lead item then reads "applied with the shared line (date)".

### 12. Two small wording faults (minor; firm)

LAYER frame. REPEAT new.

- Unit 4's reason says simulation was "met in units 1 and 3"; unit 1 teaches no simulation. Fix: "so that simulation, met in unit 3's random selection and Algebra II's re-randomisation, opens it."
- Unit 1's cell says "About 6 of the 19 days are review"; its rows give about 7.5. Fix as in finding 6.

## The L49 answer (judged)

The frame's proposal is right for Statistics: focus 1a to 1c score the standards without a (+) mark and a series majority of time on the prerequisite list, neither of which a grade 12 elective can carry, so an owned-outcome account (every code taught in full in a named unit, assessed on a named end-of-unit assessment and a later check) is the honest replacement; coherence, assessment, rigor with direct fluency, the practices, supports and the multilingual criteria transfer unchanged. Two points to carry into the shared line:
- In the Common Core the whole Statistics and Probability category is modeling, so the modeling-cycle clause of 1a must survive inside the account. The frame keeps gap 2 (the modeling record), which does this; the shared line should say so.
- 1c ("work at high school level") becomes "work at the course's stated level (first-year college for Statistics and Calculus), with no day that only reteaches an earlier course's row", which the frame's gap 7 reading already holds.
Suggested single line for docs/RUBRIC-MATH-HS.md: "Precalculus, Statistics and Calculus apply this file in full except focus 1a to 1c, which are replaced by an owned-outcome account in each frame's Focus bullet: every owned code taught in full and assessed on a named check, a modeling record (gap 2), work at the course's stated level, and no day that only reteaches an earlier course's row; there is no focus percentage line (later.csv L49)."

## Checked and found right (do not undo)

- Ownership: all 22 stat- rows placed once; CUR-ST.1 to CUR-ST.21, S-CP.B.9 and S-MD.A.1 to S-MD.B.7 each owned by one unit; S-MD.B.5a and S-MD.B.5b named in unit 5 and sampled on Check 2. Every S-MD example the standard text gives (quiz guessing, households, lottery, deductibles, lots, product and medical testing, the goalie) has a named context.
- Order: no method used before it is taught (r after z-scores, binomial after combinations, two-proportion work after the spread of a difference, matched pairs designed in unit 3 before analysed in unit 8, slope inference after t).
- Seams: every handoff from Algebra I, Geometry and Algebra II is in the rows' assumes and the earlier rows' hands_on; readiness and retrieval follow the count-by-grade rule, and For the lead 1 correctly flags the row notes that say otherwise. Precalculus and Calculus frames agree with the beside-it prose (combinations shown in Precalculus unowned; no cross-assumes).
- Cross-subject: every science lean falls on Biology (grade 9) or Chemistry (grade 10) rows taught earlier; no other subject leans on a stat- row (checked by grep).
- Data picks avoid Algebra II unit 7's contexts (polls, health-study outcomes) and its function contexts; no crime data; the lottery and insurance are analysed, never played.
- Source map: every section of chapters 1 to 13 and the appendices is placed or left out with a reason; no NC or reference source is mapped; the licence (CC BY 4.0, live, archive 7dea80a) and Lane's public-domain status match the scout notes; Lane's chapters (5, 6, 9, 13, 14, 16) are the right ones for the named gaps.
- The paper path is real for almost everything (random digit table, printed normal, t and chi-square tables, printed regression output).
- Wording of inference ideas in the frame is correct: confidence level as a property of the method, p-value "read in words", conditions before calculation, scope of inference from design.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Not applicable: no focus line for a (+) and own-outcome course (L49 answer above) |
| A supporting cluster that does not practise major work | Not applicable, same reason; every unit works on owned outcomes |
| A source map row with no keep, split, merge, cut or ours decision | Met: every row has a decision; six "keep" decisions are wrong (finding 1) |
| Progression: a model used before its grade | Met: normal-curve introduced in unit 1, used from unit 5 on; tree and two-way table reactivated |
| Progression: a handoff that skips a grade | Met: grade 10 rows get readiness checks |
| Course past Algebra 2 names a source for order and limits | Met: base text plus Lane, placed in the map |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| 1. Unit 6 "turns normal" demonstration uses the uniform parent and Old Faithful's intervals (means of 10 to 30); county populations are the counter-case where 30 is not enough | The theorem must be visible at class sample sizes (finding 3) | docs/courses/statistics/frame.md, unit 6 cell and Real data bullet |
| 2. Unit 3 stratifies the county population by the four census regions, not by state; the printed population is one copy per group | 50 strata, many with few counties, cannot be worked by hand | frame.md, unit 3 cell and Real data bullet |
| 3. Paper path calculator: "a scientific calculator with a statistics mode (mean, standard deviation, linear regression)"; add "a printed binomial table" to the printed tables | Unit 5's cumulative binomial work and unit 1's summaries have no paper route otherwise | frame.md, Technology and the paper path bullet |
| 4. Unit 9 extension: Mendel's counts fit better than chance would usually allow, a famous later analysis; a strong student reads why a goodness-of-fit test cannot flag a fit that is too good | A teacher should not be surprised by the question | frame.md, unit 9 Check set adds |
| 5. Unit 8 paired temperatures: each station's annual mean (or its published 30-year normal) in two periods, stations drawn at random from the national station list | One day's high is weather noise; inference needs a random sample of stations | frame.md, unit 8 cell and Real data bullet |
| 6. Unit 8 coin masses: a supplied published set or class-weighed coins on a 0.01 gram scale, 1982 excluded, used first for intervals and as the case where a test's answer is known; add one two-sample case whose answer is not known in advance (for example two supplied random samples of station annual means from two regions) | A test whose answer is fixed by design teaches little about testing | frame.md, unit 8 cell |
| 7. Unit 4 reason wording (finding 12) | Unit 1 has no simulation | frame.md, unit 4 cell |

## For Cory

- One grade 12 math slot: Statistics, Precalculus and Calculus are alternatives on the core route, and data/courses.csv allows Statistics in grade 11. The frame's pick (keep it at grade 12, Algebra II only prerequisite, grade 11 left to the parked accelerated path, later.csv L15) is sound; it is a scope call.

## What I could not judge

- Whether the CUR-ST statements echo a published exam framework's wording: I did not open one (product, and not in the source list). They read as our own words and grouping.
- The GAISE College Report's licence and contents: not read this run; the frame rightly keeps it a candidate.
- Exact skewness of US county populations and the seat-belt survey's design details rest on memory (marked in findings 2 and 3); the direction of both findings does not depend on the exact figures.

## Sources

- OpenStax, Statistics (2020), lab pages 1.5, 2.8, 4.8, 6.3, 7.4, 9.6, 10.5, 11.7, 11.8 at https://openstax.org/books/statistics/pages/ : what each lab collects (finding 1).
- Base-text scout notes, 2026-11-16, section 2: table of contents, licence, version (Source map check).
- Common Core State Standards for Mathematics (data/standards/ccss-math-standards.txt): S-CP.B.9 and S-MD text and examples.
- docs/RUBRIC-MATH-HS.md and its EdReports and Publishers' Criteria summary: the L49 judgment.
- From memory: census bureau survey tables (90 percent margins, public-use microdata), the national seat-belt survey's multistage design, county population skew, common one-year pacing for introductory statistics.

## For the source list

- GAISE College Report (American Statistical Association, 2016) and GAISE II, PreK-12 (2020) are not in docs/APPROACH-SOURCES.md; both belong there as the statistics teaching reference, licence to be checked at amstat.org before any use.
- The census bureau's public-use microdata (person and household records) as the supplied-sample source for units 7 and 9: public domain as a federal work, to be confirmed and recorded.
