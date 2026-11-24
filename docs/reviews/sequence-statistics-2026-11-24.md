# Sequence read: Statistics, 2026-11-24

Expert cold read of the Curio Class Statistics scope and sequence (grade 12), done under docs/pipeline/briefs/sequence-read.md with the statistics lens, the math lens and docs/RUBRIC-MATH-HS.md (The grade 12 courses). I did not write the scope and read it cold. First sequence read of a grade 12 math elective.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/statistics.md and math.md, docs/RUBRIC-MATH-HS.md (grade 12 section and parts table), docs/pipeline/briefs/sequence-read.md and sequence-write.md.
- docs/courses/statistics/scope-and-sequence.md in full; docs/courses/statistics/frame.md in full.
- data/plans/statistics/days.csv (160 rows) and source-map.csv (106 rows).
- data/progressions/math.csv, the 22 stat- rows; data/standards/curio-math-electives.txt (CUR-ST.1 to CUR-ST.21) and the S-CP.B.9 and S-MD lines of ccss-math-standards.txt.
- docs/courses/CALENDAR.md and the statistics rows of data/plans/calendar.csv; DESK-ANSWERS on collect once and task forms; the Algebra II sequence read for the band's conventions.
- The base: OpenStax, Statistics (2020), its table of contents and chapter objectives read from the PDF in S:\CurioClass-sources\openstax-statistics.
- Gates, filtered to this course: `plan.py check` (sequence statistics: 0 failures; frame statistics: 0 failures), `sequence.py check statistics` (0 failures, no rule 2 note), `frame.py calendar` (grade 12 has only the finals-week rule; no break), `stale.py check` (nothing for statistics).

## Verdict

A sound, carefully built year that keeps the frame's ten units, days and owned rows, places every owned code and lettered part on a teaching day, reads readiness by grade number correctly, and puts simulation before formula at every turn. The biggest risk is honest inference: two days run tests on data that are not random samples (park visit totals on day 141, home listing prices on day 123), and one microdata sample is made to serve both homogeneity and independence, which is the very distinction CUR-ST.19 teaches. The change that matters most is to carry the two widened clauses no day teaches (statistical versus practical significance in CUR-ST.13; interval and test agreement for means in CUR-ST.18) and fix those data choices; no unit moves.

## Findings

### 1. Two widened clauses are carried by no day and asked by no end item (serious)

- What is wrong: CUR-ST.13 ends "and tell statistical from practical significance"; no day's goal or note teaches it, and day 115's prompt list for CUR-ST.13 (hypotheses, conditions, p-value in words, conclusion at a stated level) omits both it and "what a p-value does not tell". CUR-ST.18 ends "explain how a two-sided test at a level and an interval at the matching confidence agree"; day 104 does this for one proportion (tagged CUR-ST.12 and CUR-ST.13), but no unit 8 day does it for means, and day 134's prompt list for CUR-ST.18 omits it. Both clauses were added in the 2026-11-16 fix pass (frame For the lead 6).
- Why it matters: the owned-outcome account says every owned code is taught in full and assessed on its unit's end day. A unit planner builds from days.csv and will miss both clauses.
- Fix: day 102's goal adds "and tell a statistically significant result from one that matters in practice"; day 120 revisits it (finding 12). Day 129's goal adds "and show that a two-sided test at a level and the interval at the matching confidence agree". Day 115's CUR-ST.13 prompt list adds "what a p-value does not tell; statistical against practical significance"; day 134's CUR-ST.18 list adds "test and interval agreement".
- Evidence: curio-math-electives.txt lines CUR-ST.13, CUR-ST.18; days.csv 101 to 104, 115, 128 to 134. Confidence: firm. LAYER: sequence. REPEAT: yes (end items missing a part of a code, grade 6 and earlier reads).

### 2. Two inference days use data that are not random samples (serious)

- What is wrong: day 141 runs a chi-square analysis "from question to conclusion" on "park visits by season and region": these are full-population visit totals in the millions, not counts of independently sampled individuals, so any chi-square test is meaningless and will always reject. Day 123 estimates and tests a mean from "published home prices" (the base's home costs lab), a listing, not a random sample, and names no source or date.
- Why it matters: the frame's Real data bullet says every inference procedure runs on data that really is a random sample or a randomized experiment, and that full-population tables are never fed into a sampling formula; the lens asks that each conclusion say which kind of randomness it rests on. These two days would teach the habit the course exists to break.
- Fix: settled below. Day 141 uses a new variable pair from the supplied worker microdata sample (departure-time band by commuting mode, one sample, independence). Day 123 runs the single mean on a random sample of station annual means (unit 8's source) and the single proportion on the microdata or seat-belt sample; the home costs lab stays only as a conditions case, where students explain why an interval from a listing does not reach all homes. Update source-map.csv's OS 8.4 row to match.
- Evidence: days.csv 123, 141; frame Real data bullet; statistics lens, "Concepts before recipes". Confidence: firm. LAYER: sequence. REPEAT: new.

### 3. One sample serves both homogeneity and independence (serious)

- What is wrong: days 138 and 139 both cite "a supplied simple random sample of about 400 worker records ... commuting mode by region"; day 139's note repeats day 138's data line although its goal says "a second variable in one sample". A test of homogeneity needs separate samples from each population; one simple random sample cross-classified is the independence design.
- Why it matters: CUR-ST.19 is "choosing the right one from how the data were gathered". If both days use one file, the data contradict the lesson, and the person preparing the microdata files (frame For the lead 3) will draw one sample.
- Fix: day 138 uses separate random samples per region (about 100 records from each of the four census regions); day 139 uses one simple random sample with commuting mode by travel-time band, and its note names that variable. The microdata file list grows to: one state's person sample (unit 7), two states' person samples (scope For the lead 1), four regional worker samples and one national worker sample (unit 9).
- Evidence: days.csv 138, 139; frame unit 9 Data. Confidence: firm. LAYER: sequence. REPEAT: new.

### 4. Day 126 uses the two-sample procedure three days before it is taught (moderate)

- What is wrong: day 126 asks students to "analyze the station data wrongly as two independent samples and rightly as pairs, and explain why the paired interval is narrower". The two-sample t interval is first taught on day 129.
- Why it matters: nothing may be used before it is taught; a teacher would have to teach the two-sample interval in passing on a paired day, and day 129 then loses its first teaching.
- Fix: settled below. Day 126 compares the spread of the raw station values with the spread of the differences on dot plots, so students see what pairing removes without a second procedure; the wrong-then-right interval contrast moves to day 132, which already chooses between paired and two-sample designs.
- Evidence: days.csv 124 to 132. Confidence: firm. LAYER: sequence. REPEAT: yes (used before taught, grade 6 read).

### 5. Each check's first day repeats the unit sitting's form two days later (moderate)

- What is wrong: days 44, 90 and 149 are short unseen items, two days after days 42, 88 and 147, which are short unseen items. Collect once (DESK-ANSWERS 2026-11-15) says a course-level check never repeats a task form given in the last two weeks. Scope For the lead 3 names the clash and picks keep.
- Why it matters: the rule says never, and the band has read "audit and sort instead of direct solving" as a changed form (Algebra II read). Students sit the same form twice in three days.
- Fix: each check's first day becomes an audit-and-choose form: short items that give a worked analysis or a study to judge (find and fix the error, choose the display or procedure and say why, read given output in context), still sampling the earlier units' codes, with Check 3's fluency station kept direct. Day goals 44, 90 and 149 and the check table say so; the frame's Course-level checks sentence ("short unseen items on the first check day") changes in the scope fix pass. This also serves the lens's "a choice of method with its reason".
- Evidence: days.csv 42, 44, 88, 90, 147, 149; DESK-ANSWERS 2026-11-15 collect once. Confidence: firm. LAYER: sequence and frame. REPEAT: yes (Algebra I and Algebra II reads).

### 6. Day 149 cannot hold its station and its code list (moderate)

- What is wrong: day 149 holds a fluency station sampling seven procedures, four of them full inference procedures (CUR-ST.12, 13, 16, 18), which the frame defines as a four-move write-up, plus short items on eleven codes, in about 45 minutes.
- Why it matters: four write-ups alone take about 40 minutes; the planner will either rush the station or drop codes the day claims.
- Fix: settled below. The station gives each inference fluency as one short item on its conditions and calculation from a given summary (no full write-up; day 150 holds the full write-up), about 15 minutes; the short items sample at most five other codes (CUR-ST.11, 14, 15 and two of units 1 to 5), and day 149's codes list only those.
- Evidence: days.csv 149, 150; frame Fluency bullet. Confidence: likely. LAYER: sequence. REPEAT: yes (Algebra II day 158).

### 7. No practice is tied to a day (moderate)

- What is wrong: the frame's C3 column places all eight practices by unit, but the scope and days.csv name none (no "MP" anywhere). The high school rubric lists "named tasks per practice in each scope and sequence" as the open gap for 2e to 2l.
- Why it matters: a unit planner has nothing to build the practice tasks from, and an adoption reviewer scores practices by named tasks.
- Fix: one "Practices:" line per unit section naming a day for each practice in C3, for example MP2 day 9 (compare in context), MP6 day 3 (precise distribution language), MP4 days 23 and 28, MP7 days 19 and 25, MP3 days 35 and 41, MP1 days 55 and 76, MP8 days 62 and 81, MP5 days 84 and 121, MP3 and MP6 days 104 and 113, MP2 and MP5 days 126 and 131, MP3 and MP7 days 140 and 145, unit 10 days 153 and 157.
- Evidence: frame Practices bullet; RUBRIC-MATH-HS parts table. Confidence: firm. LAYER: sequence. REPEAT: new.

### 8. The investigative cycle is not named per unit (moderate)

- What is wrong: the lens asks each unit to name where students pose a question, collect or consider data, analyze and interpret, and that a unit which only analyzes supplied numbers says so and why. The scope does this only for unit 10. Units 2, 5, 7 and 9 work almost entirely on supplied data and do not say why (the frame's privacy rules are the reason).
- Why it matters: the lens's first check; without it the year can read as "the investigation at the end, recipes before".
- Fix: one "Cycle:" sentence per unit, for example unit 3: pose (day 35), collect (days 32, 33), analyze (33), interpret (39, 41); unit 7: pose (108), consider (93, 97), analyze (94 to 113), interpret (95, 112); for units 2, 5 and 9: "supplied data only, because students never collect their own money, health, home or identity data; students pose the question on day 23 (or 76, 141)".
- Evidence: statistics lens, "The investigative cycle". Confidence: firm. LAYER: sequence. REPEAT: new.

### 9. The senior presentation fold does not fit the period (moderate)

- What is wrong: the Seniors fold moves presentations from three days to two, "half the class a day": 15 students at about 3 minutes and one question each is about 60 minutes, more than the 50-minute period before the opening and changeovers. The frame's Grade 12 calendar bullet has the same arithmetic.
- Why it matters: the fold is planned from the start where a school knows its seniors leave early; a teacher would find it cannot run.
- Fix: settled below. On the two-day fold, talks are 2 minutes with one question, 15 a day, and the opening is dropped on those days (about 45 minutes); the frame bullet is updated in the fix pass.
- Evidence: scope Shorter path; frame Grade 12 calendar bullet. Confidence: firm. LAYER: sequence and frame. REPEAT: new.

### 10. Day 72 is over its minutes (low)

- What is wrong: day 72 holds the 5-minute opening, the 15-minute response to day 69's sitting, the lottery, the dice prize game and about 5 minutes to count the dice kit back in: about 25 minutes for S-MD.B.5 and S-MD.B.5a. Scope For the lead 4 accepts the response time; that is right, the crowding is not.
- Fix: settled below. Day 72 holds the response and the lottery only, with no kit; the dice prize game (OS 4.8) moves to day 74, which already uses dice and asks what "fair" means, and day 74 adds S-MD.B.5a to its codes.
- Evidence: days.csv 69, 72, 74; frame Days bullet (kit minutes). Confidence: likely. LAYER: sequence. REPEAT: new.

### 11. The calendar file still shows the frame's spread, not the written days (low)

- What is wrong: data/plans/calendar.csv and CALENDAR.md's generated row for statistics place unit 4 on days 47 to 55, unit 10 as one block on days 148 to 160 and Check 3 in weeks 29 to 30; days.csv puts Check 3 on days 149 to 151 (weeks 30 to 31) and holds days 47, 48, 70 and 71 for unit 10. `frame.py sync` has not run since days.csv was written; days_calendar would read it.
- Why it matters: unit_skeleton.py and day_skeleton.py read calendar.csv for weeks, so skeletons would print wrong weeks, and the scope's "frame.py calendar shows no break" rests on the stale file.
- Fix: the lead runs `python -X utf8 scripts/frame.py sync`, then checks that the statistics rows show the held days in their own weeks.
- Evidence: calendar.csv statistics rows; CALENDAR.md generated table; scripts/frame.py days_calendar. Confidence: firm. LAYER: process. REPEAT: yes.

### 12. Day 120's "answer known by design" is not safe (low)

- What is wrong: day 120 tests whether post-1982 coins' mean mass equals the mint's specified mass and calls it a case whose answer is known by design. Circulated coins wear and the mint allows a tolerance, so with a 0.01 gram scale a class may well reject (from memory). The frame's known-by-design case is the before-and-after-1982 difference (day 128).
- Fix: settled below. Day 120's goal reads "a test against the mint's specified mass, where wear may move the mean", and the day names statistical against practical significance (finding 1).
- Evidence: days.csv 120, 128; frame unit 8 data. Confidence: likely. LAYER: sequence. REPEAT: new.

### 13. Day 87 practices a skill no day taught (low)

- What is wrong: Fluency day 87 practices "probabilities about sample proportions" with the normal model; day 80 describes that sampling distribution but no day finds a probability with it (day 86 does so for means only).
- Fix: settled below. Day 80's goal adds "and find a probability about a sample proportion with it".
- Evidence: days.csv 80, 86, 87. Confidence: firm. LAYER: sequence. REPEAT: yes (Fluency on untaught work).

### 14. Respond days do not list what their check sampled (low)

- What is wrong: day 92 omits CUR-ST.7, S-MD.A.1, S-MD.B.5b, S-MD.B.6 and S-MD.B.7, which days 90 and 91 sample; day 151 omits CUR-ST.2, 3, 8, 11, 14 and 15, which day 149 samples (the fluency station among them).
- Fix: each respond day lists the codes its check sampled; day 151's note says fluency station misses are repaired in its first part, then the inference repair for the investigation.
- Evidence: days.csv 90 to 92, 149 to 151. Confidence: firm. LAYER: sequence. REPEAT: new.

### 15. Source map: small gaps (low)

- What is wrong: OS 1.2 is marked keep on day 31 while its why says part is met on day 1 (a split, days 1; 31). The Lane rows leave order_conflict blank although Lane's chapters are placed out of their own order (16 and 14 in unit 2, 6 in unit 3 before 5 in unit 4). Days 14, 22 and 87 use base lab data with no source line (lens: every data set has a source).
- Fix: OS 1.2 becomes split, days 1; 31. Lane rows out of order get "yes: placed where the course needs it (gap filler)" and harms_learning "no". Days 14, 22 and 87 notes add "Data: OpenStax, Statistics, lab data (as published)".
- Evidence: source-map.csv; base table of contents (checked: every section of chapters 1 to 13 is placed). Confidence: firm. LAYER: base text. REPEAT: new.

### 16. Frame notes the scope has outgrown (low)

- What is wrong: the frame's Focus bullet plans about 995 minutes (the scope's correct count is 1,020, 13.5 percent); its Grade 12 calendar bullet folds unit 2's review days, which first-teach part of CUR-ST.4 (scope For the lead 2); its unit 7 data name no two-sample case (scope For the lead 1); its Units table unit 10 cell says the respond day is "for revision", while the Investigation bullet and days.csv put revision on day 156.
- Fix: the scope fix pass updates those four frame cells to match the scope.
- Evidence: frame.md; scope For the lead 1, 2 and 5. Confidence: firm. LAYER: frame. REPEAT: yes (stale frame notes after a scope).

### 17. How 30 investigations gather data in one day is unstated (low)

- What is wrong: day 70 has every project run its class experiment or draw its sample in one period, but nothing says whether projects are individual or in groups, or how class experiments share classmates as subjects. Days 157 to 159 score "one performance per student".
- Fix: the scope's unit 10 section says projects are in groups of three (about 10 projects), each scored per student on the report section and the talk the student gives, and day 70 runs class experiments as a station rotation; the unit plan sets the details.
- Evidence: days.csv 47, 70, 157 to 159. Confidence: judgment call. LAYER: sequence. REPEAT: new.

## Checks the brief asks for

- **Order inside each unit:** holds except day 126 (finding 4) and day 87 (finding 13). Every unit arc reaches its compelling question; unit 9 closes the year's loop on unit 1's tables and unit 2's lines.
- **Assessments:** an end sitting per unit on its second-last day, unit 5 sitting twice, unit 10 scored on the revised report and the talk; every prompt list names each code's parts, except the two clauses in finding 1. No unit is over 25 days, so no mid-unit assessment is due. Response time is counted once, including unit 5's first sitting (15 minutes of day 72).
- **Readiness or retrieval:** correct by grade number with one hop, and the gate agrees. alg1-two-way-tables (grade 10) gets readiness on day 1 after the hook; geo-conditional-independence and geo-addition-rule (grade 10) get readiness on day 46, three days before unit 4, with only the investigation's held days between: within "a few days". Every grade 11 row is retrieved inside a teaching day; rows used earlier this year (alg1-center-spread, alg2-experiments-significance, alg2-sample-estimates-margin, alg1-two-way-tables, alg1-scatter-linear-models) are retrieved, none checked. No other unit's first day holds a readiness check.
- **Checks that do not repeat:** each check follows a unit end and draws its items from earlier units, reusing that unit's record with its date; the scope and the day goals say so. The form repeats (finding 5).
- **Standards in full:** every owned code and S-MD.B.5a, S-MD.B.5b are on a teaching day; the two clauses in finding 1 are not.
- **Days by load:** each part follows its row's load within a day (for example unit 7: 6, 6, 4 and 6 days against loads of 7, 7, 4 and 6, with the end and respond days); no run is far off.
- **The calendar:** Check 1 days 44 and 45 (week 9), respond 46 (week 10); Check 2 days 90 and 91 (week 18), respond 92 (week 19); Check 3 days 149 and 150 (week 30), respond 151 (week 31): all on the frame's target weeks. Grade 12 has only the finals-week rule: no break. The frame has no same-year leans (the science leans fall on grades 9 and 10), so no bridge is owed. calendar.csv is stale (finding 11).
- **Candidate cells:** every unit's candidates (the GAISE lens and the Progressions checks) are kept as read checks with no day cost, and unit 10's rubrics are kept and written with the unit plan. Settled correctly; math has no check set, so none costs days.
- **Shorter path:** present: a 45-minute period, and ten fold-in days (2, 8, 22, 50, 63, 87, 103, 122, 127, 133), each a practice, lab or review day, none assessed, none a feedback, revision, check or respond day, 500 minutes, 150 of 160 days. The senior fold's presentations do not fit (finding 9).
- **Source map:** all 79 base sections and labs of chapters 1 to 13 placed or cut with a reason (16 cuts: out of the owned outcomes, or a lab that collects students' bodies or homes); the base order is kept, with each departure given a reason, except the Lane rows (finding 15). Rule 8 layout is used.
- **Our words:** every goal compared with the base's 250 chapter objective lines; the closest match scores 0.57 (day 59), no goal at or above 0.6. Copy rate: 0 of 160.
- **Minutes line:** 575 + 50 + 20 + 375 = 1,020 of 7,550 unit minutes, 13.5 percent, under the 15 percent cap; the arithmetic holds.
- **Stale notes:** stale.py has nothing for this course; the rest is in findings 11 and 16.

## Lens checklist (scope and sequence layer)

| Lens line | Holds | Note |
| --- | --- | --- |
| Each unit names its cycle phases, or says why supplied | missed | finding 8 |
| Questions are statistical | met | |
| The investigation runs the whole cycle with its scope of inference | met | days 47, 48, 70, 71, 152 to 160 |
| Variability is the thread; no summary without its spread | met | days 6, 9, 33, 81, 126 |
| Real context, free source, "as of" date, or labeled invented | partly | days 14, 22, 87, 123 (findings 2, 15) |
| Several variables together often | met | units 1, 2, 9; day 4 |
| Conditions and meaning taught, not only steps | met | days 14, 94, 121, 143 |
| Each conclusion says which randomness it rests on | partly | days 123, 141 (finding 2); day 39's grid is right |
| Simulation before or beside formula | met | days 79 to 85, 93, 99, 106, 128, 130, 136, 142 |
| p-value and confidence level read with what they do not say | partly | taught days 95, 101; not on day 115 (finding 1) |
| Students produce and argue from data in class | met | |
| Technology to explore, with the paper path; no outcome tied to one product | met | |
| Items ask interpretation, method choice, design judgment | met | strengthened by finding 5 |
| Reports scored after draft, feedback, revision | met | days 154 to 156 |
| End results feed a named next step | met | a respond day per unit and check |
| No student's sensitive data collected | met | microdata fields dropped; no place of birth asked |
| Practices tied to tasks (rubric 2e to 2l) | missed | finding 7 |
| Fluency spaced and mixed, sampled directly at year end | met | station overloaded (finding 6) |

## The scope's "For the lead" items

| Item | Judgment |
| --- | --- |
| 1. Two states' microdata for days 110 and 111 | Agree: a real two-independent-samples case, states compared, never groups. The microdata file list grows further with finding 3; the frame's unit 7 data cell is updated (finding 16). |
| 2. Fold day 22, not unit 2's review | Agree: days 18 and 19 first-teach r from z-scores. Update the frame bullet (finding 16). |
| 3. Same task form within two weeks, keep | Disagree: the rule says never. Change each check's first-day form to audit and choose (finding 5). |
| 4. Unit 5's first sitting answered in 15 minutes of day 72 | Agree on the response time; move the dice game off day 72 (finding 10). |
| 5. Minutes line 13.5 percent | Agree: the arithmetic is right and under the cap. The frame's Focus bullet takes the 1,020 count (finding 16). |

## What is right and should not be touched

- Readiness by grade number, with one hop, placed in the last ten minutes of day 1 and of Check 1's respond day; every other unit's day 1 is clean for its hook.
- Simulation before every formula: class intervals checked against a known percent (day 93), a simulated null (day 99), power by simulation (day 106), re-randomization beside the t test (day 130).
- The county counter-case for the central limit theorem (day 85) and Old Faithful where the normal model fails (day 14).
- Unit 5's two sittings with the investigation's gathering days marked during them (days 69 to 72).
- The polio trial met as a design (day 37) and analyzed as two proportions (day 113).
- Privacy: no place of birth, home, body, money or health asked of a student; microdata income and household fields dropped.

## What I could not judge

- Whether the microdata samples can be drawn at the sizes named; that is the lead's data step (frame For the lead 3).
- Whether a teacher can write feedback on 30 plans overnight (day 47 to 48) and 30 reports in a day and a half (days 154 to 156); the unit plan should test it with group sizes (finding 17).
- Outside sources were not fetched for this read; the statistics points rest on the lens's reading of GAISE and on memory of the high school Statistics and Probability Progressions, marked where it matters.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Day 141 uses departure-time band by commuting mode from the national worker sample (independence), replacing park visit totals | Inference only on a random sample (finding 2) | days.csv day 141 |
| Day 123 runs the single mean on a random sample of station annual means and the single proportion on the microdata or seat-belt sample; home costs kept only as a conditions case | Inference only on a random sample (finding 2) | days.csv day 123; source-map.csv OS 8.4 |
| Day 138 uses separate random samples per region; day 139 one simple random sample, mode by travel-time band | Homogeneity and independence told by how data were gathered (finding 3) | days.csv days 138, 139 |
| Day 126 compares spreads of raw values and differences on dot plots; the independent-versus-paired interval contrast moves to day 132 | Nothing used before taught (finding 4) | days.csv days 126, 132 |
| Day 149's station gives each inference fluency as one short conditions-and-calculation item; at most five other codes sampled | Fits the period; day 150 holds the full write-up (finding 6) | days.csv day 149; check table |
| Senior fold: presentations 2 minutes with one question, 15 a day, no opening on those days | Fits 50 minutes (finding 9) | scope Shorter path; frame Grade 12 calendar bullet |
| Dice prize game moves from day 72 to day 74, which adds S-MD.B.5a | Day 72's minutes (finding 10) | days.csv days 72, 74; source-map.csv OS 4.8 |
| Day 120 reworded: a test against the mint's specified mass, where wear may move the mean | Known-by-design claim unsafe (finding 12) | days.csv day 120 |
| Day 80's goal adds finding a probability about a sample proportion | Day 87 practices it (finding 13) | days.csv day 80 |
| Respond days 92 and 151 list the codes their checks sampled | Finding 14 | days.csv days 92, 151 |

## For Cory

Nothing. No finding changes scope, money, people or audience, and no standard moves between units.

## Sources

- docs/agents/lenses/statistics.md: our own reading of the GAISE College Report (2016) and Pre-K-12 Report II (2020), used as the lens checklist; the reports themselves were not reopened.
- OpenStax, Statistics (2020, CC BY 4.0), S:\CurioClass-sources\openstax-statistics: table of contents (source map check) and chapter objectives (our words check).
- Common Core State Standards for Mathematics, S-CP.B.9 and S-MD (data/standards), and Curio Class's CUR-ST outcomes (data/standards/curio-math-electives.txt).
- Progressions for the Common Core, High School Statistics and Probability: from memory, for the homogeneity and independence distinction and inference on random samples.
- US Mint coin specifications and coin wear: from memory, for finding 12; to be confirmed when the unit plan writes the coin data.

## For the source list

- None new.
