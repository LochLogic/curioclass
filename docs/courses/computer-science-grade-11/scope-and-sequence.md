# Scope and sequence: Computer Science, Grade 11

Course `computer-science-grade-11`, grade 11, draft scope and sequence, 2026-11-26, written from the frame (docs/courses/computer-science-grade-11/frame.md). The days live in data/plans/computer-science-grade-11/days.csv; this page holds the judgment. Pending(docs/sources/BASE-TEXTS.md#noaa-climate-data-online): the NOAA extract is not in the source store (later.csv L149), so the frame and unit 3 are provisional.

## The calendar

64 course days, two 45-minute lessons a week for 32 weeks. Course days 2k-1 and 2k sit in week k, on the week's second and fourth school days: `school_day = 5 * (ceil(n / 2) - 1) + 2` for an odd day n and `+ 4` for an even one, so week = (school_day - 1) // 5 + 1 = ceil(n / 2). Every unit and check falls in the frame's weeks: unit 1 days 1 to 9 (weeks 1 to 5), unit 2 days 10 to 22 (weeks 5 to 11), unit 3 days 23 to 32 (weeks 12 to 16), the mid-year check days 33 and 34 (week 17) with its respond day 35 (week 18), unit 4 days 36 to 47 (weeks 18 to 24), unit 5 days 48 to 54 (weeks 24 to 27), unit 6 days 55 to 61 (weeks 28 to 31), the year-end check days 62 (week 31) and 63 (week 32, the finals week) with its respond day 64 (week 32).

Every lesson from day 2 on opens with a retrieval trace or predict task of at most five minutes. Device lessons keep 3 minutes to open the page and 4 to save or print work and close devices. Each device day's note names its four paths (one device per pair, stations, one screen, no device) and its paper version; the toy-system, test-runner, chart, simulation and model-training tools do not exist yet (frame For the lead 4), so every device day runs on its paper path meanwhile, with HS-ALG-ML-08 and HS-DAT-DI-25 part met without a device. Security days (1 to 8 and day 34's flaw item) and device days carry the frame's Safety lines in their notes: the toy system or described case only; no scanning, no attack steps, no test of a real school or home system; a student who knows of a real flaw tells the teacher privately and never tries it.

**Elective entry.** Grade 11 never assumes grade 10 was taken. Each grade 10 row opens as a retrieval task for students who took it and is given as a ten-minute readiness check, before its unit, for students who did not: day 1 (last ten minutes, after the hook), day 9, day 22, day 35, day 47 and day 54. The session that first uses the row carries a short worked example for the students the check flags, inside its own minutes. Rows from two or more grades back get a readiness check for every student: g9-data-and-people on day 47, g8-design-for-all and grade 8's data center debate on day 54. Readiness rows are named by id in those days' notes.

**Days outside the standards (bar C1).** The Specialty I parts count as days outside the course's own standards, session by session as the frame names them: day 2 (half), day 3 (whole), day 12 (whole), day 13 (half), day 27 (whole), day 42 (half). 4.5 of the 50 teaching days, 9 percent. No other day sits outside the standards. The shorter year keeps the share under 10 percent too (see Shorter path).

**Day kinds.** As GLOSSARY defines them: the first teaching of a row or method is Understanding, so days 4 (the flaw-report method, traced before it is modified), 13 (judging generated test suggestions), 42 (the training-set change) and 49 (where bias comes from in a rule and in training data) are Understanding even where they also modify or audit.

## Unit 1. Find it, rate it, fix it (days 1 to 9, weeks 1 to 5)

The arc runs from a toy club sign-up page with two flaws to a flaw report students can write alone. Day 1 reads the anchor and rates a breach case on the cia-triangle (retrieval of g10-breach-causes); days 2 and 3 give the tools for rating: data states and control types, then the two named threats (S1-CYB-TS-08 in full on day 3). Day 4 traces the worked flaw report on the weak password rule and modifies its fix; day 5 is the make day on the second flaw, which students find themselves; day 6 moves the same habit to a described phishing case on paper; day 7 revises the reports after partner feedback (IC3). The order is trace, modify, make, then transfer and revise.

- **Readiness:** day 1, last ten minutes (g10-breach-causes, for students who did not take grade 10).
- **End-of-unit assessment, day 8:** a new printed toy system with an unseen flaw to find, rate and solve, and one unseen threat to rate; a prompt for each part of HS-SYS-SE-33 and S1-CYB-TS-08. Response: day 9.
- **Candidate:** kept, a station plan for a room with four devices on days 4 and 5, zero added days.
- **Sensitivity:** days 1 and 6 carry health's "If a student tells you something" steps; no real password is typed. Days 1 to 8 carry the Safety line.

## Unit 2. Does it do what was asked? (days 10 to 22, weeks 5 to 11)

The specification test comes first (days 10 to 16), so the generated samples (days 17 to 20) are judged with a plan students already wrote. Day 10 reads the specification, traces one function (retrieval of g10-analyze-code) and has the class set two values on the specification sheet (the overdue list shows titles, never borrowers' names; plain messages and keyboard use), about five minutes; day 11 sorts kinds of test case; day 12 traces unit and integration tests (S1-SWD-TR-07); day 13 extends a worked plan and judges generated test suggestions (modify); day 14 writes the whole plan; day 15 runs it and traces the first failure; day 16 judges the program against its specification for users and the day 10 values (HCD11, ESR2). Day 17 reads the second-largest requirement and traces two saved samples (retrieval of g10-apis-docs); day 18 tests them; day 19 judges reliability and writes ownership notes (~HS-PRO-PD-14); day 20 places a generated function in the program under the integration tests. Mixed trace and test practice by error letter runs in the openings of days 18 to 20.

- **Readiness:** day 9, last ten minutes (g10-analyze-code, g10-apis-docs, for students who did not take grade 10).
- **End-of-unit assessment, day 21:** a new short program and specification: a test plan of every kind (the one full performance), three tests run by trace, a judgment against the specification, one unseen generated sample with its flaw, reliability, fit to the requirement and ownership note, and two supplied generated test suggestions kept, changed or dropped with the reason; covers HS-PRO-TR-19, S1-SWD-TR-07, HS-PRO-RD-18. Response: day 22.
- **Candidate:** kept, a printed hand-trace version of the test runner for days 15, 18 and 20 (the frame's sessions 6, 9 and 11), zero added days.

## Unit 3. Charts that let us decide (days 23 to 32, weeks 12 to 16)

Making a chart comes before judging other people's, and the conventions sit between the draft and the revision. Day 23 reads a three-variable chart and cleans messy rows (retrieval of g10-visual-data and g10-clean-text) and meets the weather extract and its question; day 24 matches chart kinds to many-variable data; day 25 modifies a given chart's encoding; day 26 makes the pair's visualization and its first caption; day 27 sorts honest and broken charts (S1-DSC-VZ-11); day 28 revises the chart to the conventions. Days 29 and 30 run and judge the crosswalk simulation; day 31 judges a printed chart with a cut axis for a decision; day 32 is mixed practice from units 1 to 3 before the check.

- **Readiness:** day 22, last ten minutes (g10-visual-data, g10-clean-text, for students who did not take grade 10).
- **End-of-unit assessment:** the mid-year check (days 33 and 34) stands for it, as the frame sets. The revised chart is handed in on day 28 and scored once on its look-fors after the check (HS-DAT-DI-25). Day 33 scores the rest. Response: day 35.
- **Candidate:** kept, a hand-drawn plot on printed graph paper as the no-device path on days 25, 26 and 28, zero added days.
- **Unloaded source:** days 23 to 28 and 33 use the NOAA Climate Data Online extract (approved download). Pending(docs/sources/BASE-TEXTS.md#noaa-climate-data-online): the extract is not in the source store; fallback an extract invented for practice, marked so.

## Course-level check, mid-year (days 33 to 35, weeks 17 and 18)

Day 33 scores unit 3 in full on a 40-minute paper sitting: a new chart and simulation run judged (HS-DAT-DI-26) with one broken convention redrawn (S1-DSC-VZ-11), about 25 minutes, and each student's own caption, about 10 minutes, with day 28's chart scored outside the sitting (HS-DAT-DI-25). Day 34 samples units 1 and 2 with short new items in forms not given on day 8 or day 21 (six and eleven weeks earlier): an unseen flaw rated and fixed, with the Safety line (HS-SYS-SE-33, S1-CYB-TS-08), a function with a generated variant tested against its requirement (HS-PRO-RD-18), and four test cases for a short specification, one unit and one integration (HS-PRO-TR-19, S1-SWD-TR-07). Day 35 responds by error letter and holds unit 4's readiness check in its last ten minutes. Week 17 holds no grade 11 core check.

## Unit 4. What did the model learn? (days 36 to 47, weeks 18 to 24)

The data review comes before the build (the row's in-grade order), and the rebalance comes after the first comparison so its effect can be measured. Day 36 justifies an AI type for the digit reader (retrieval of g10-choose-ai-type); day 37 traces a worked data review of another set (retrieval of g10-verify-consistency); day 38 writes the digit set's review. Day 39 writes the build steps as pseudocode and splits example cards into training, comparison and sealed final test piles (retrieval of g10-evaluate-algorithms, ~HS-ALG-PS-03, and g10-clean-text). Day 40 predicts which 7s the model will miss, then trains it on the training pile by the pseudocode lines (the guided first run); day 41 tests it on the comparison pile; day 42 changes the training set and keeps only changes that improve both fairness and accuracy (S1-AIN-DD-02); day 43 builds a second model on a chosen task (the pair's own make). On days 40 to 43 driver and navigator switch at the halfway signal (IC5); day 44 freezes the model, runs the final test once and writes the report's first version, each student writing the claim paragraph alone; day 45 revises it.

- **Readiness:** day 35, last ten minutes (g10-choose-ai-type, g10-verify-consistency, g10-evaluate-algorithms, for students who did not take grade 10).
- **End-of-unit assessment, day 46:** a new training-set summary to review and a supplied comparison test-table on which to keep or drop a proposed rebalance, a prompt for each part of HS-ALG-ML-07 and S1-AIN-DD-02; the revised model report from day 45 is scored as the unit's product (HS-ALG-ML-08). Response: day 47.
- **Candidate:** kept, the card model's rules written as a decision table for the paper path, zero added days.

## Unit 5. Who does it serve? (days 48 to 54, weeks 24 to 27)

It audits the kind of model students just built. Day 48 sets the laptop-loan program's two outputs side by side (retrieval of g10-design-hcd); day 49 audits the ten cases for where bias comes from in a rule and in training data; day 50 writes the hiring audit, which carries HS-ALG-IM-10, from two views. View one: the EEOC's technical assistance on software and algorithms in employment selection (issued May 2023, removed from eeoc.gov January 2025; the Title VII duty it explained still stands, and the removal is itself a dated fact for the audit) with NIST SP 1270 (March 2022, current): algorithmic selection can carry bias and must be checked. View two: a dated government or university source arguing that structured or algorithmic screening makes decisions more consistent than unstructured human judgment (candidate, from memory: the US Office of Personnel Management's structured interview guide, 2008), opened and dated by the unit writer. Day 51 uses the same case's applicant data to open large-scale collection (HS-DAT-IM-27), shaped by the day 47 readiness results; day 52 writes the evaluation, starting from a Native body's own published position (the CARE Principles).

- **Readiness:** day 47, last ten minutes: g9-data-and-people for every student; g10-design-hcd for students who did not take grade 10.
- **End-of-unit assessment, day 53:** a new pair of rule-based and data-driven outputs to audit with a refinement for each and one thing the audit could not see, and a short evaluation of a new collection case with two views. Response: day 54.
- **Candidate:** kept, a second set of ten cases on library room bookings for a school that swaps the loan cases, zero added days.
- **Sensitivity:** days 49 to 52 carry the frame's guards (talk on how the system was built and tested; no company named); day 52 is Native content, told in the Native body's own words. Grade 7 unit 3's sovereignty case is four grades back, so its one-page card goes to every student, not only to those who missed grade 7 (my call; it is a recalled case, not an assumed row).

## Unit 6. Who carries the cost? (days 55 to 61, weeks 28 to 31)

Day 55 traces one upload through a network-diagram (retrieval of g10-network-diagram) and widens it to the infrastructure on a printed map; day 56 traces who a data center siting and water case affects. Day 57 places a state recycling law on a timeline (retrieval of g10-history-policy); day 58 writes the one-page proposal to change it, weighing two views (one who would gain, one who would bear the cost) and citing the law with its date. Day 59 plans the team, its roles and a local problem, with a dated source for the main claim about the technology (retrieval of g10-emerging-impacts, g10-human-choices, g10-career-skills); day 60 writes the design document's first version, with benefits and harms from two views; day 61 revises it.

- **Readiness:** day 54, last ten minutes, one page of six one-minute items: kiosk users (g8-design-for-all) and one data center claim from grade 8's debate for every student; for students who did not take grade 10, one upload traced (g10-network-diagram), one policy placed on a timeline (g10-history-policy), one emerging technology's benefit and harm with whose choice it was (g10-emerging-impacts and g10-human-choices in one item) and one role matched to a skill (g10-career-skills).
- **End-of-unit assessment:** the year-end check (days 62 and 63) stands for it. The revised design document is handed in on day 61 and scored on each student's own section after the check (HS-SOC-ET-42). Response: day 64.
- **Candidate:** kept, the school's own county and state as the case, from their public pages, zero added days.
- **Lean:** g11-policy-change leans on social-studies us1-progressivism (the progression's cross_subject cell). US history I teaches it in unit 8, weeks 25 to 28, before day 57 (week 29), so no bridge is owed; day 57's note links the law to Progressive Era regulation for students taking it.
- **Sources (checked 2026-11-26).** Washington's Electronic Product Recycling law is chapter 70A.500 RCW, first enacted 2006 (c 183), opened on the Legislature's RCW page (app.leg.wa.gov/RCW/default.aspx?cite=70A.500); the frame's memory holds. The E-Cycle guidance pages on ecology.wa.gov were not opened; the unit writer opens them. Siting and water case, my pick: The Dalles, Oregon, where after a 2022 public records settlement the city released data showing its data centers used about 29 percent of city water in 2021; later reporting puts the share near a third (OPB, 2026-01-15) and the city's mayor disputed parts of that reporting (OPB, 2026-01-23), told without the company. The city's 2026 plan to draw more water from national forest land is a current development with two views on record. Figures checked by search 2026-11-26, not opened. Two views: the city's own public statements on the data centers, and residents' and a water group's concerns over water. Sources to open at the unit plan: the City of The Dalles's public pages and the Oregon Water Resources Department's critical groundwater area pages. I found these by search only; no page was opened, so the facts stay unchecked until the unit writer opens them.

## Course-level check, year-end (days 62 to 64, weeks 31 and 32)

Day 62 (week 31) scores unit 6 in full on a 40-minute paper sitting: a new infrastructure chain (HS-SYS-IM-37) about 12 minutes, one change proposed to an unseen policy, with how it encourages innovation and cuts a named risk, one piece of evidence and who it affects (HS-SOC-HI-39) about 13, and each student's own justification of their section, about 10, with day 61's document scored outside the sitting (HS-SOC-ET-42). Day 63 (week 32, the finals week, which grades 9 to 12 may share) samples units 4 and 5 with new short items in forms not given on day 46 or day 53: a training-set summary (HS-ALG-ML-07), a model claim on a final test-table (HS-ALG-ML-08), a pair of outputs to audit (HS-ALG-IM-10), and one effect of a new collection named with its group (HS-DAT-IM-27). Day 64 returns the work by error letter and records gains for grade 12.

**Codes on a course-level check.** Every owned code is sampled on days 33, 34, 62 or 63 except S1-AIN-DD-02. It is scored in full on day 46 and in the model report, and day 63's four items already fill its 35 task minutes, as the frame sets them. It stays off the checks (settled by the expert read, 2026-11-26). The contributes codes (~HS-ALG-PS-03, ~HS-PRO-PD-14, ~HS-SOC-HU-44, ~HS-SOC-CE-45) are used, not claimed, and are not sampled.

## Shorter path

**A shorter period (40 minutes).** The opening stays at three minutes and the device minutes stay at seven, so a device lesson teaches about 28 minutes and an unplugged one about 33. Each day's exit ticket moves into the next day's opening. On the four check days the retrieval opening is dropped so the 40-minute sitting keeps its full time.

**A year about 10 days short (54 days).** Ten fold-in days, each with nothing assessed and no owned part cut, 45 minutes each, 450 minutes in all, 64 to 54 days:

| Fold-in day | Folds into | What is kept |
|---|---|---|
| 6 (phishing case on paper) | day 7 | The case becomes the feedback task; HS-SYS-SE-33 is met on day 5 |
| 11 (kinds of test case) | days 10 and 12 | The card sort runs 15 minutes on day 10; day 12 adds the kinds to the test-table |
| 13 (extend the worked plan) | day 14 | Day 14 opens with the worked plan and the suggestion list judged in 15 minutes, so S1-SWD-TR-07's judging part stays |
| 20 (generated function in the program) | day 19 | One integration test of the sample is run in day 19's last 15 minutes |
| 25 (modify a chart's encoding) | day 26 | The encoding change is the first 10 minutes of the make day |
| 27 (honest and broken charts) | day 28 | The sort and one broken chart's faults named run in day 28's first 15 minutes, before the revision, so S1-DSC-VZ-11's conventions part stays |
| 32 (mixed practice before the check) | openings of days 29 to 31 | Practice by error letter in the retrieval minutes |
| 37 (worked data review) | day 38 | The worked review is traced in the first 15 minutes; the range-check retrieval stays |
| 43 (second dataset model) | day 44 | The claim rests on the digit model; HS-ALG-ML-08 is met on days 40 to 44 |
| 56 (siting and water case) | day 55 | The case is the chain's worked example, and day 55's exit ticket is each student's own written link: one group affected and why; HS-SYS-IM-37 is met on day 55 and day 62 |

**Specialty share on the shorter year (bar C1).** The shorter year has 40 teaching days. Folding day 27 (whole Specialty) into day 28 and day 13 (half) into day 14, each kept as about 15 minutes, leaves days 2 (half), 3, 12 and 42 (half) plus about a third of a day each in days 14 and 28: about 3.7 of 40 days, 9 percent, under the 10 percent line. Day 31 (the printed cut-axis chart) stays a day so the shorter year still has ten folds.

The two folds that save the most real work are days 13 and 43; a school cutting fewer days folds the others first. The once-a-week path is not set for grades 6 to 12, which meet twice a week.

## For the lead

1. **Tool asks for TOOL-ASKS.md** (frame For the lead 4): the toy-system page (days 4, 5), the test runner (days 13 to 15, 18, 20), the chart tool (days 25, 26, 28), the crosswalk simulation (day 29), the model-training page (days 40 to 43). I did not write TOOL-ASKS.md (not my file).
2. **Sources to add to docs/APPROACH-SOURCES.md:** chapter 70A.500 RCW (checked 2026-11-26); The Dalles case: WaterWatch of Oregon and OPB (2026-01-15, 2026-01-23), by search only, to be opened at the unit plan (unit 6 above); the EEOC technical assistance dated as issued May 2023 and removed from eeoc.gov 2025-01-27 (Cooley 2025-02-21, National Law Review 2026, by search only); the US Office of Personnel Management's structured interview guide (2008, from memory) as day 50's second view, to be opened. The rest are the frame's list.
3. **Calendar.** rame.py calendar reports grades K to 8 only; grade 11's checks sit in weeks 17 and 31 to 32 as the frame set, off every grade 11 core check week except the shared finals week (CALENDAR.md rule 4). Week 17 also holds ELD's grade 11 mid-year check, which is for the after-core pass.
4. **Rule 2 notes.** sequence.py printed no rule 2 notes for this course. The skeleton may not count computer science yet, so the readiness rows were counted by hand from the frame's Seams table.
