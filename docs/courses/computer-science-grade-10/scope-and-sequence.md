# Scope and sequence: Computer Science, Grade 10

Course `computer-science-grade-10`, grade 10, draft 2026-11-26. 64 course days, two 45-minute lessons a week for 32
weeks; the days and their goals live in data/plans/computer-science-grade-10/days.csv.

**Calendar formula.** Course days 2w-1 and 2w fall in week w, on the second and fourth school day of that week:
`school_day = 5(w-1) + 2` for an odd course day and `5(w-1) + 4` for an even one, so week = (school_day - 1) // 5 + 1
gives the frame's weeks. Grade 10 computer science is an elective outside the core; no stagger rule binds it
(CALENDAR.md rules 1 and 3 cover K to 8).

**Every day.** From day 2 on, a lesson opens with a three-minute retrieval trace (or, on a unit's first day, the hook
and its retrieval or predict task), and device lessons keep their last three minutes to save or print and close
devices (APPROACH.md, "How a day opens"). Each device day's note carries its four paths (one device per pair,
stations with paper, one screen with predict and vote, no device), the pair roles switched at the halfway signal and
the frame's two safety lines; each security day carries the case-card-only line. The credit line "Standards: 2026
CSTA PK-12 Computer Science Standards (CC BY-NC-SA 4.0)" goes on every day that leans on a statement. No base text:
every program, case card and data set is written by Curio Class, and no day leans on an unloaded source (later.csv
L149 names grade K to 8 and grade 11 sources only).

**Earlier-grade rows and their treatment** (rule 2, counted by grade number). From grade 9, the year before:
g9-modular, g9-structures-program, g9-design-with-structures, g9-optimize-procedures, g9-ai-tour, g9-network-sketch,
g9-security-measures, g9-data-dictionary, g9-simulate-data, g9-algorithm-impacts, g9-career-interests,
g9-emerging-differences and g9-computing-history: retrieval inside the named day for students who took grade 9;
because grade 9 is an elective, the same items are a ten-minute readiness check before each unit for students who did
not (frame, Course order), with a worked example in the retrieving lesson. The review threads g9-operating-systems
(day 22) and g9-det-vs-prob (day 7) are review, with a worked example inside the day for students who did not take
grade 9, not readiness items. From grade 8, two grades back: g8-evaluate-ai-code and g8-attribution (readiness for every student,
day 1) and g8-network-failure (the packet-strip item, readiness for every student, day 20). Readiness days: 1, 11, 20,
31, 41 and 53, each the previous unit's last day or the respond day between units.

## Unit 1: Reading code closely (course days 1 to 11, weeks 1 to 6)

Concept area: programming.

The year opens on a working twenty-line guessing game, run once and then read. Days 2 and 3 trace a procedure call
on a trace-table and pass a list into it on the list-diagram; day 4 modifies the anchor with every part already
taught; day 5 reads one saved code sample against a test-table (a first look at HS-PRO-RD-18). Days 6 to 9 turn to
someone else's code: a documentation page read unplugged, two supplied library calls modified and one added from it
(day 7, the modify lesson on library calls), the debugger and the credit comment (a first look at HS-PRO-PD-14), and
a second feature made by each pair. Trace before modify before make, on the anchor and on the library, as APPROACH.md
asks, and reading a call comes before using a library because the documentation describes calls in the
same terms. Readiness: day 1's last ten minutes. End-of-unit assessment: day 10, unseen items on both owned ids
(HS-PRO-RD-17 explained and traced; HS-PRO-PD-13 written from a new documentation page and the step-through debugger
used to find a wrong return value, part met without a device on paper); response on respond day 11, which also holds unit 2's readiness check. Candidate: kept, the teacher's "if you
are stuck" sheet on the anchor's three commonest bugs, on day 8, zero added days.

## Unit 2: Which algorithm is better? (course days 12 to 20, weeks 6 to 10)

Concept area: algorithms and design, with AI inside it.

Two searches for one name in a sorted list are written as pseudocode (day 12), stepped through on number cards with
memory use named as a second cost (day 13) and run with a step counter on growing lists (day 14). Days 15 and 16 are
modify lessons on correctness (four test cases on a buggy halving search) and clarity. Days 17 and 18 turn the same
question to AI: the data each task card has and what an error costs, then a two-sentence justification. Counting
comes before testing so students see why the halving search is worth its extra care, and the AI days come last
because "which suits the task" is the question the searches just answered. End-of-unit assessment: day 19, one
extended task on HS-ALG-PS-03 plus a short written item on HS-ALG-ML-06, so no day holds two full performances;
response on day 20, which holds unit 3's readiness check. Candidate: kept, a step-count table template, on day 13,
zero added days.

## Unit 3: Networks and breaches (course days 21 to 28, weeks 11 to 14)

Concept area: systems and security.

All unplugged. One office network is diagrammed and a request traced (days 21 and 22), then drawn from a description
by each student (day 23); several networks are joined with a packet strip (day 24) and the internet is seen as a
network of networks with shared rules, clients and servers, and layers (day 25). Days 26 to 28 sort breaches and scams
by cause on the cia-triangle, then by impact on four groups and by kind, on an invented hospital case and on a staff
impersonation case from a dated public announcement. One network before many, and networks before breaches, because
a breach needs the parts it broke into. Assessment: the mid-year check (days 29 and 30) is this unit's end-of-unit assessment and
day 31 its respond day. Readiness for unit 4: day 31. Candidate: kept, a one-page diagram
key of symbols, on day 21, zero added days. Sensitivity: every breach and scam day names the flag and carries
health's steps.

## Unit 4: Clean data, checked data (course days 32 to 41, weeks 16 to 21)

Concept area: data and analysis.

An invented volunteer list with one person three ways and a birthdate in 2099 sits beside its data dictionary (day
32). Days 33 to 35 clean it with supplied functions: case and spaces, then misspellings, invalid entries and
duplicates, then structure (one name split in two, dates in one format). Days 36 and 37 judge three ways to verify
against the dictionary and apply them to a new table. Days 38 and 39 plot the clean table with three variables and
say what the chart cannot show (a first look at HS-DAT-DI-25; a worked chart first bridges from grade 8 math scatter
plots). Clean before verify, verify before chart, since a chart of unchecked data misleads. End-of-unit assessment:
day 40, unseen items on HS-DAT-DC-23 (part met without a device on paper) and HS-DAT-DC-24; response on day 41, which
holds unit 5's readiness check. Candidate: kept, an error-letter key for the five commonest cleaning mistakes, on day
34, zero added days.

## Unit 5: Design for every user (course days 42 to 53, weeks 21 to 27)

Concept area: algorithms and design (impacts of design), with computing and society (careers).

The year's team project. A kiosk screen three users cannot finish names the human-centered steps (day 42); teams
research users from persona cards read aloud, never acted (day 43), learn accessibility as a constraint and the laws
by their government names (day 44), compare options on a benefit-risk-chart (day 45), prototype (day 46) and test
with access checks (day 47). The product is drafted (day 48), gets written feedback the lesson after (day 49), is
revised (day 50) and is scored when teams present (day 51), with each student's own page on one change. The portfolio
lesson (day 52, not scored, a contributing use of HS-SOC-CE-46) follows the score because by then the year's work is
built, and the unit ends on respond day 53, which holds unit 6's readiness check. End-of-unit assessment: day 51, a
product. Candidate: kept, team role cards switched halfway, on day 42, zero added days. Sensitivity: disability
content on days 42 to 47 and 51, with the frame's guard.

## Unit 6: Who decides? (course days 54 to 61, weeks 27 to 31)

Concept area: computing and society.

All unplugged. A tutoring tool offered to every school in a district is evaluated for learning and fairness (day 54),
for the environment and access with two dated views (day 55), and in writing that names the weakest claim (day 56).
Day 57 places a 1998 privacy law on the timeline (a first look at HS-SOC-HI-39). Days 58 to 60 lay out the Michigan
automated fraud system and an invented data-driven case at four decision points, then argue which decision mattered
most. Effects before choices, because who decides only matters once students see what the technology does. End-of-
unit assessment in two parts, as the frame sets: day 61 scores HS-SOC-HU-43 on an unseen case, and the year-end
check's first lesson (day 62) scores HS-SOC-ET-41; response on day 64. Candidate: kept, a source-line template, on day
54, zero added days. Sensitivity: work and benefits on days 58 and 60, home internet on days 54 and 55, with health's
steps.

## Course-level checks

| Check | Course days | Weeks (school days) | What it samples |
|---|---|---|---|
| Mid-year | 29 and 30, respond 31 | 15 (72, 74); respond week 16 (77) | Day 29 scores unit 3 in full (HS-SYS-NT-34, HS-SYS-NT-35 with the layers and routers, HS-SYS-SE-32 with a breach and a social engineering case); day 30 samples HS-PRO-RD-17, HS-ALG-PS-03, HS-ALG-ML-06 |
| Year-end | 62 and 63, respond 64 | 31 (154) and 32 (157); respond week 32 (159) | Day 62 scores HS-SOC-ET-41 (unit 6 part 2); day 63 samples HS-PRO-RD-17, HS-ALG-PS-03, HS-DAT-DC-24, HS-ALG-IM-09 and a three-variable chart read |

Both checks stand for the end-of-unit assessment of the unit before them, so neither repeats an assessment just
given. Owned codes not sampled on a check day (rule 3): HS-PRO-PD-13 and HS-DAT-DC-23 need a device to be met in
full and all checks are on paper, so their end-of-unit records (days 10 and 40) are carried unscored; HS-SOC-HU-43 is
scored on day 61, two lessons before the check, and carried into its record, since the frame keeps one full
performance per day.

## Shorter path

**A shorter period (40 minutes).** The retrieval trace stays at three minutes and device save minutes stay; each
lesson trims its practice by five minutes, and a check lesson holds its one scored performance of about 25 minutes.

**A year about 10 days short (54 days).** Ten fold-in days, each removing one 45-minute lesson (450 minutes in all,
64 days to 54); the neighbor takes 10 to 15 minutes of the folded work, nothing assessed or owned is cut, and no
fold-in removes a modify day or the only practice of a scored performance (days 4, 7, 56 and 60 stay whole; day 6's
page read moves into day 7's first minutes, since day 7 is now the modify lesson on library calls):

| Fold-in day | Folds into | Minutes saved |
|---|---|---|
| 5 (saved code sample read) | 4, last 15 minutes | 45 |
| 6 (reading a documentation page) | 7, first 15 minutes, before the calls are modified from it | 45 |
| 14 (step counter on growing lists) | 13, the counts from the printed table | 45 |
| 16 (clarity) | 15 | 45 |
| 18 (AI justification practice) | 17 | 45 |
| 28 (second breach case and review) | 27 | 45 |
| 37 (verification applied) | 36 | 45 |
| 39 (reading the chart) | 38 | 45 |
| 52 (portfolio) | 53, first 15 minutes | 45 |
| 57 (policy on the timeline) | 56, first 15 minutes | 45 |

Total 450 minutes, 10 of 64 days.

## For the lead

1. **Tool asks** stay as the frame's For the lead 5 (step counter, cleaning functions with a table view, contrast
   checker, three-variable chart tool); their days run on the paper path until built.

Item-level choices made here: memory use is named on day 13 so day 16 stays practice; day 5's test-table includes a
missing-item and an empty-list case so day 15's four test cases are practice; day 15 runs on paper by default (a
printed trace-table), with a device optional; day 7 is the modify lesson on library calls before day 9's make; days 10
and 40 are device sittings with a paper version (part met without a device for HS-PRO-PD-13 and HS-DAT-DC-23); each
week's two lessons sit on its second and fourth school day (the formula above).
