# Scope and sequence: Computer Science, Grade 7

Course `computer-science-grade-7`, grade 7, draft 2026-11-26, from the frame (docs/courses/computer-science-grade-7/frame.md). The days are in data/plans/computer-science-grade-7/days.csv.

## How the days sit on the calendar

- 64 course days, two 45-minute sessions a week for 32 weeks: 58 in six units, 4 course-level check lessons and 2 respond days, as the frame sets. Course days 2k-1 and 2k fall in week k.
- **school_day** is filled on every day by one formula: course day 2k-1 is school day 5k-2 and course day 2k is school day 5k (the third and fifth school day of week k). Week = (school_day - 1) // 5 + 1. This gives the frame's check days: 31 and 32 on school days 78 and 80 (week 16), 33 on 83 (week 17), 62 on 155 (week 31), 63 on 158 and 64 on 160 (week 32).
- Every session from day 2 on opens with a three-minute retrieval trace or a short predict task; the `retrieves` column names the row it brings back. Device sessions keep their last four minutes to save or print work and shut devices down, and their notes carry the frame's device lines (devices on the table, cords behind it) and the four ways a device day runs.
- Device days are 2, 5, 7, 12 to 14, 16 to 20, 23, 25, 36 to 38 and 46 (17 of the 50 teaching days); every unit has unplugged days.
- Days outside the standards (bar C1): the three list days 11 to 13, 3 of 50 teaching days (6 percent). Teaching days are the 64 less the end-of-unit, check and respond days.
- Credit line "Standards: 2026 CSTA PK-12 Computer Science Standards (CC BY-NC-SA 4.0)" goes on every day that leans on a statement; ids are cited and stated in our own words.
- **Kinds.** By GLOSSARY "teaching day": Understanding is an unplugged or trace day (first teaching of a row or method, and predict-and-watch days), Fluency a modify day (days 5 and 16 only), Application a make, design or society day. Day 6 is Understanding (MS-ALG-PS-01's first day, taught from a worked design) and day 48 Application (a society day using day 47's triangle on a real case); the frame's Day kinds bullet now says the same.
- **Sources not yet loaded** (later.csv L149): days 1 to 8 (archived Year 8 "Introduction to Python programming"), 12 and 13 (archived Year 9 "Python programming with sequences of data" lessons 2 and 4) and 59 (archived Year 8 "Layers of computing systems" lesson 5, read for order) lean on the partial base, which the source store does not hold yet. They are planned from the frame's Source map and stay provisional until the store folder is made and each file's license line and third-party check are read.
- **Readiness and retrieval.** Every row this course assumes is a grade 6 row, the year before. For a student who took grade 6 it opens as a retrieval task on the day the frame's Seams name; for a student who did not, the same items are a ten-minute readiness check on days 1 (after the hook), 10, 22, 33, 43 and 54, with a worked example inside the next unit's first understanding day (days 2, 11, 23, 34, 44, 55). Day 33 also covers a whole class whose school left out grade 6's unit 4. No row reaches back two grades.

## Unit 1. Read it, then design it (days 1 to 10, weeks 1 to 5)

The anchor quiz program is printed and traced before it is ever run (day 1), then run and compared (day 2), its loop and choice traced (day 3), a two-procedure version read (day 4) and modified in small checked steps (day 5). Day 5 also finds one planted bug with the four-step debugging routine (predict, run, find the first line that differs from the trace, change one thing and rerun), unscored, so the bugs of day 7 meet a taught step. Day 6 teaches design from a worked example, has students change that design for one new requirement and retrace it, then each student designs a new algorithm with three variable types as a flowchart and pseudocode and traces it; day 7 finishes the design in its first minutes and builds it in Python text with a partner trace; day 8 revises the design and writes how it works. The order is read, modify, then design and make, so the student designs only with constructs already traced. The base's order (input and output, arithmetic, selection, iteration) is kept inside days 1 to 3.

- **Readiness:** day 1, last ten minutes (g6-variable-types, g6-procedures, g6-model-algorithm).
- **End-of-unit assessment:** day 9, unseen items: construct roles and output for a new fifteen-line program (MS-PRO-RD-17, about 17 minutes) and a short design with three variable types in pseudocode with a trace-table (MS-ALG-PS-01, about 18 minutes), inside the 35 teaching minutes. Response time: day 10.
- **Candidate:** kept, the base's order inside days 1 to 3, zero added days.
- **Math lean:** day 6 (school day 15) sits two days after math grade 7 unit 2 opens; the converter uses one given rate and no proportional test, and the reading log is the default.

## Unit 2. Build it as a team (days 11 to 22, weeks 6 to 11)

Lists are taught unplugged as a named box with numbered slots (day 11), traced on the device (day 12) and looped over from a worked example (day 13). Day 14 teaches the offline reference page and error guide from one worked lookup each, then a changed call, then one found alone (MS-PRO-PD-13); day 15 plans tests before running (MS-PRO-TR-19); day 16 modifies the shelf tracker, one fix at a time with a change log and every test rerun, each bug looked up in the error guide. Days 17 and 18 are the pairs' draft build from the menu, with each student's own reference-page call and supplied-error fix; day 19 is the written code review (~MS-PRO-PD-15, grade 6's); day 20 revises, retests and hands in, and the team product is scored. Days 17 to 20 name their paper path: lined code sheets, tests run "be the computer", the reference entry and error guide printed; MS-PRO-TR-19 is met in full on paper and MS-PRO-PD-13 part met without a device. Lists and the reference page come before the build that uses them; testing sits beside the build so the review feeds refinement.

- **Readiness:** day 10, last ten minutes (g6-variable-types, g6-procedures, g6-verify-algorithm, g6-inclusive-collab).
- **End-of-unit assessment:** day 21 (a list trace, a hand-written call from a new reference entry as supplementary evidence for MS-PRO-PD-13, and a test plan with the first failing test and a logged fix for MS-PRO-TR-19; about 8, 7 and 20 minutes), with the day 20 product scored. Response time: day 22.
- **Candidate:** kept, the base's pair programming and live coding on days 12 and 13, zero added days.
- **Science lean:** day 15 is school day 38, inside science grade 7 unit 2 (school days 24 to 41); the teacher names the same test and improve idea.

## Unit 3. What the data shows, and what it costs (days 23 to 30, weeks 12 to 15)

The weather log is grouped and summarized with the table tool (day 23, ~MS-DAT-DC-23 used again), graphed three ways (day 24) and charted twice by each student with a screen-reader description (day 25, MS-DAT-DI-26). The second half moves from data about things to data about people: metadata, benefits and risks (day 26), ownership and consent (day 27), data sovereignty told from a nation's own published account, its two views on a choice inside the case and never on whether the nation may govern its data (day 28), a written claim on a new case (day 29), and a pair brief joining a fairer chart to fair collection (day 30), kept work the teacher reads, unscored. Charts come first so the personal-data days can ask what a chart of people's data would cost.

- **Readiness:** day 22, last ten minutes (g6-sort-filter-tool, g6-precision-metadata, g6-data-about-people).
- **End-of-unit assessment:** the mid-year check (days 31 and 32) stands for it, as the frame sets; day 31 comes right after the unit's last day. Response time: day 33.
- **Candidate:** kept, a chart-reading partner test on day 25, zero added days.
- **Math lean:** samples come in math unit 8 (weeks 28 to 32); the table is the whole data set and no population claim is made.
- **Sensitivity:** days 26 to 30 personal data, day 28 Native content; the teacher pages carry health's steps word for word.

## Unit 4. Algorithms that decide (days 34 to 43, weeks 17 to 22)

Choosing an approach opens the unit (days 34 and 35, MS-ALG-PS-04), so a learned method is first met as one choice among several. The sorter is tested (day 36), its results read for missing and misleading examples (day 37), and its training set improved and retested (day 38, MS-ALG-ML-07). The bias days follow the training-data days so the cause is already seen: daily algorithms and AI cases, each worded as its dated study found it (day 39: a 2020 speech study, NISTIR 8280 of December 2019), why biases happen (day 40) and a written claim (day 41, MS-ALG-IM-10).

- **Readiness:** day 33, last ten minutes (g6-model-algorithm, g6-ml-hypothesis, g6-data-quality, g6-hcd-evaluate).
- **End-of-unit assessment:** day 42, one item set per id. Response time: day 43.
- **Candidate:** kept, a second retrain round on day 38 for pairs that finish, zero added days.
- **Tool:** the in-page sorter trainer is queued with tool work (later.csv L148), so days 36 to 38 run on the paper path (sorting cards as the model) and MS-ALG-ML-07 stays part met without a device until it exists.
- **Math lean:** probability is math unit 8; day 34 reasons from invented class totals in words, with no probability number.
- **Sensitivity:** days 39 to 41 race, dialect and disability bias.

## Unit 5. Keep the library running (days 44 to 54, weeks 22 to 27)

One library anchor carries all four rows. The network is built on cards (day 44), broken with yarn (day 45) and broken again on the toy network (day 46, MS-SYS-NT-35). The CIA triangle explains effects on people (day 47) and is used on a real breach, from two dated sources, beside invented school cases (day 48, MS-SYS-SE-32). Access barriers are charted (day 49) and set against a dated source on home internet and the 2025-09-30 federal vote to end E-Rate support for hotspot lending, its majority and dissent as the two views (day 50, MS-SYS-IM-37; programs named as of the day read). Requirements for a family or shop system (day 51, ~MS-SYS-HW-30 used again) lead into the pair's library brief (day 52), which joins all four rows.

- **Readiness:** day 43, last ten minutes (g6-packets, g6-cia-practice, g6-compare-systems, g6-devices-industry).
- **End-of-unit assessment:** day 53, one item set per owned id. Response time: day 54.
- **Candidate:** kept, a second toy-network map with a single point of failure on day 46, zero added days.
- **Safety:** day 45's yarn is on tables, never across a walkway.
- **Sensitivity:** days 47 and 48 security (health's steps), days 49 and 50 disability, income and rural access.

## Unit 6. Computing changes things (days 55 to 61, weeks 28 to 31)

The move to computer-controlled telephone exchanges is traced on a two-arrow timeline for people (day 55) and, through the phones the network made common, the environment (day 56, MS-SOC-HI-39). Automation cases follow (days 57 and 58, MS-SOC-CE-45), then what emerging technologies can and cannot do, from a dated source (day 59) and a task set judged with a person-decides flag (day 60, MS-SOC-ET-40, ~MS-SOC-HU-43 used again). Day 61 is the year's written claim with partner feedback, kept work the teacher reads, unscored. History comes first so automation and emerging technology are seen as the next chapter of the same story.

- **Readiness:** day 54, last ten minutes (g6-computing-eras, g6-careers-ct, g6-human-decisions).
- **End-of-unit assessment:** the year-end check (days 62 and 63) stands for it; day 62 comes right after the unit's last day. Response time: day 64.
- **Candidate:** kept, a class vote on one verdict with reasons shown on day 60, zero added days.
- **Sensitivity:** days 57 and 58 families' jobs; day 55 operators were mostly women, said from the source without blame.

## Course-level checks

| Check | Days | School days and weeks | What it samples |
|---|---|---|---|
| Mid-year | 31, 32; respond 33 | 78 and 80, week 16; respond 83, week 17 | Day 31 scores unit 3 in full (MS-DAT-DI-26, MS-DAT-IM-28), standing for its end-of-unit assessment. Day 32 samples units 1 and 2 with new item forms (MS-PRO-RD-17, MS-PRO-TR-19) |
| Year-end | 62, 63; respond 64 | 155, week 31; 158, week 32 (finals); respond 160 | Day 62 scores unit 6 in full (MS-SOC-HI-39, MS-SOC-CE-45, MS-SOC-ET-40), standing for its end-of-unit assessment. Day 63 samples units 1, 4 and 5 (MS-ALG-PS-01, MS-ALG-ML-07, MS-SYS-NT-35) |

Since each check stands for the unit just ended, no end-of-unit assessment comes right before it, and the second lesson draws only on earlier units with forms not given in the last two weeks. Calendar: grades 6 to 8 stagger mid-year checks by school day (CALENDAR.md rule 3); school days 78 and 80 hold no other grade 7 mid-year check in calendar.csv (physical education 76 and 77, SEL 75, health 84, dance 83, ELD 85 and 86, library 89). Year-end checks sit in week 32 with the rest.

**Owned codes on no course-level check** (rule 3), each scored on its own end-of-unit day and carried unscored, because the frame fixes each second lesson at about 30 minutes, one ten-minute item per id: MS-ALG-PS-04 and MS-ALG-IM-10 (day 42), MS-SYS-SE-32 and MS-SYS-IM-37 (day 53), and MS-PRO-PD-13 (scored in the day 20 product; its full look-for needs a device). Kept as is (expert read 2026-11-26): each is scored on an unseen end-of-unit sitting, and a six-minute item on day 63 would be too short to ask each part of MS-ALG-IM-10 or MS-SYS-SE-32.

## Shorter path

- **A shorter period (40 minutes):** the opening trace stays at three minutes and the device close at four; the exit ticket drops to one item, an assessment sitting keeps every id's item and cuts one read item per id (about 30 minutes), and the three Candidate extras (day 38's second retrain, day 46's second map, day 60's class vote) become extension only. No day moves.
- **A year about 10 school days short** (four sessions at two a week): fold in these days, nothing assessed and no owned part cut.
  1. Day 8 into day 7: the partner trace and the design revision take day 7's last 15 minutes; the written account becomes three lines at the end of day 7, never a home task. Saves 45 minutes.
  2. Day 13 into day 12: the worked list loop is traced on day 12 and changed on day 16. Lists are outside the standards, so no owned id loses a day. Saves 45 minutes.
  3. Day 27 into days 26 and 28: ownership and consent become the second half of day 26 and the opening of day 28. Saves 45 minutes.
  4. Day 35 into day 34: the mixed-approach worked example becomes day 34's fifth problem. Saves 45 minutes.
  5. Day 58 into day 57 (spare): the two views and the adaptation line close day 57's case cards. Saves 45 minutes.
- Total: four fold-ins save 180 minutes (four sessions, 60 of 64 days); the fifth gives 225 minutes (59 of 64) if the year runs shorter still.
- **Bar C1 on the shorter path:** fold 2 joins two of the three list days, so the days outside the standards fall to 2 of 46 teaching days (about 4 percent); with the fifth fold-in, 2 of 45. The share stays under 10 percent on either path.

## For the lead

1. **No source-map.csv in this run** (lead call 2026-11-26): waits on L149. The placement list stays here: Year 8 Python lessons 1 to 6 on days 1 to 8 (lessons 1, 2 on days 1, 2; 3 to 5 on day 3; 6 on days 6 to 8), Year 9 sequences lessons 2 and 4 on days 12 and 13, Year 8 Layers lesson 5 on day 59, and the other units cut with the frame's reasons.
2. **Tool asks:** the in-page sorter (days 36 to 38) and the toy network (day 46) are not built; both days run on paper now. Day 46's toy network is not named in L148's three modes; check it is on the tool list.
