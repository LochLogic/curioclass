# Scope and sequence: Computer Science, Grade 4

Course `computer-science-grade-4` (catalog id `cs-k12`), grade 4, draft, written 2026-11-26 from the frame and fixed the same day after the expert read
(docs/courses/computer-science-grade-4/frame.md). The days live in data/plans/computer-science-grade-4/days.csv; this
page holds the judgment.

## On the first page

- **Meeting days.** One 40-minute session a week, 32 weeks, a specials rotation (STANDARD.md section 2), so course day
  n sits in week n. Each session opens with a three-minute retrieval trace, or on a respond day with the most-missed
  wrong example (APPROACH.md, How a day opens, b), and every device session keeps its last four minutes to save or
  print, shut lids and return devices: about 33 minutes teach.
- **How `school_day` is counted.** One session in the last school day of each week: `school_day = 5 x n`, and the week
  is `(school_day - 1) // 5 + 1 = n`. This matches frame.py's even spread, so calendar.csv does not move. Checked day by
  day: the mid-year check is day 11 (school day 55, week 11), its respond day 12 (week 12); the year-end check day 24
  (school day 120, week 24), respond day 25 (week 25); the end-of-unit assessments sit on days 5, 17 and 31 (weeks 5,
  17, 31), as the frame's Check weeks bullet gives.
- **The stagger rule.** Computer science is a special in K to 5 and does not count against the classroom teacher's
  stagger (CALENDAR.md rule 1). Week 11 and week 24 hold no grade 4 core check (core weeks 8, 9, 10, 12, 16, 19, 21,
  23, 27, 30, 31, 32). Week 24 also holds music's year 4 year-end check, another special: named, not a break.
- **Ownership.** All 19 E4 ids are owned here and placed on days; grade 3 rows are retrieval, never claims.
- **Readiness and retrieval (rule 2).** Every row the course assumes is a grade 3 row, used the year before, so each
  opens as a retrieval task inside the day that first uses it (the `retrieves` column), and no unit holds a readiness
  check. The one math lean of the year before (m3-scaled-graphs) is a retrieval on day 14. Days that retrieve an
  earlier unit of this year name it in the note.
- **Devices and paper.** Device days: 1, 13 to 15, 17, 19 to 23 (and the one-screen sorter on day 26 once it exists).
  Every device day is written four ways (one device per pair, stations, one screen, no device) and carries the frame's
  Safety lines in its note. Two queued tool modes (later.csv L148) do not exist yet: the table tool's report view (day
  15 and day 17's report item run on a handwritten report beside a printed or hand-drawn chart, so E4-DAT-DI-10 is part
  met until it exists) and the sorter trainer (day 26 runs with the class as the sorter, which meets E4-ALG-ML-02 in
  full in grade 4; E5-ALG-ML-02 is grade 5's). On the no-device path E4-DAT-DC-09 and E4-DAT-DI-10 are part met without
  a device; every other id is met in full on paper.
- **Sources not yet loaded** (later.csv L149). The archived Teach Computing Curriculum (2023) is not yet in the source
  store, so the days that adapt it are provisional and say so: days 1, 13, 14, 16, 19, 20, 21, 22 and 23. The base's
  name appears once a day, in the credit line; no other day says "Base".
- **Kinds.** Understanding before modify before make, as APPROACH sets. Fluency is day 8 alone; day 21 is
  Understanding, since it first teaches the test-table and the piece-by-piece method (the frame's Day kinds bullet
  now says so).

## The calendar

| Unit | Course days | Weeks | Days |
|---|---|---|---|
| 1. When it breaks and how it connects | 1 to 6 | 1 to 6 | 6 |
| 2. Algorithms in words | 7 to 10 | 7 to 10 | 4 |
| Mid-year check and respond | 11, 12 | 11, 12 | 2 |
| 3. Tables, charts and people | 13 to 18 | 13 to 18 | 6 |
| 4. The class quiz, built in pieces | 19 to 23 | 19 to 23 | 5 |
| Year-end check and respond | 24, 25 | 24, 25 | 2 |
| 5. Machines that learn, and people who make tools | 26 to 32 | 26 to 32 | 7 |

## Unit 1: When it breaks and how it connects (days 1 to 6, weeks 1 to 6)

Concept area: systems and security. Practices CT9, CT6, ESR2, ESR1. The year's first device session is the staged-fault
station (day 1): a think-aloud on one fault with the five steps, then pairs at the stations, so the troubleshooting
steps exist before every later device day. Networks (day 2), login and permission (day 3) and device resources (day 4)
follow unplugged, one row a day as their single-session load asks; resources closes the unit because it opens the
benefit-risk-chart unit 2 uses. Day 2 carries the science bridge (science's waves and messages unit comes in weeks 11
to 14). Day 3 is sensitive ground: pretend paper logins only, no question about home devices, and health's "If a
student tells you something" steps on the teacher page.

Assessments: end-of-unit day 5, about 30 minutes of unseen items, one prompt per part of each code (two faults, one hardware and one software, each found, fixed with a safe step and
checked; a connection chosen with its reason; six cards sorted and one explained; a device life with one effect on
resources, one on the environment and one user action). Response on day 6. No readiness check (all assumed rows are grade 3's). Candidate kept,
zero days: the base's input, process and output sort of systems of different sizes is day 1's retrieval.

## Unit 2: Algorithms in words (days 7 to 10, weeks 7 to 10)

Concept area: algorithms and design. Practices CT8, CT7, IC3, ESR1, HCD10. Trace (day 7: the choose-your-path anchor,
its event, repeat and choice lines), modify (day 8: the pattern algorithm rewritten with a repeat, one line changed to a
choice), make (day 9: each pair's own algorithm, followed word for word by another pair and fixed). Day 10 needs two
algorithms students can read and run, so it comes last, with unit 1's benefit-risk-chart. Day 8 carries the math bridge
(math's pattern unit is weeks 20 to 22; students only follow the given rule). Day 10 is sensitive ground (being chosen
last, disability): invented case-card people only, no team picked in the room, no food.

Assessments: the mid-year check (day 11) stands for this unit's end-of-unit assessment, as the frame sets. Each pair's fixed
algorithm from day 9 is collected and read beside day 11; it is practice, not scored. Response on day 12. Candidate kept, zero days: a reading-aloud partner step on day 9.

## Course-level check, mid-year (days 11 and 12, weeks 11 and 12)

Day 11, about 30 minutes, paper version and read-aloud. Unit 2 is scored in full with unseen items: each student's own
numbered algorithm with an event, a repeat and a choice on three look-fors, plus a trace of a new written algorithm
(E4-ALG-PS-01); a written judgment of who two new algorithms help or disadvantage on new case cards (E4-ALG-IM-03).
Unit 1 is sampled with new forms, not day 5's items: a new picture fault card that shows the device's response after each
chosen step (E4-SYS-HW-12) and two new
login-or-permission cards (E4-SYS-SE-13); day 5's records for E4-SYS-NT-14 and E4-SYS-IM-15 are carried unscored. Since
the check stands for unit 2's end-of-unit assessment, no unit 2 assessment comes just before it to repeat. Day 12
reteaches by error letter and gathers fresh evidence on the missed items.

## Unit 3: Tables, charts and people (days 13 to 18, weeks 13 to 18)

Concept area: data and analysis. Practices CT6, CT7, IC3, ESR1, ESR2. Records and attributes first, on cards and the
paper table, then in the table tool with a column sorted (day 13); the class question answered with a chart (day 14,
math grade 3's scaled graphs retrieved); the written report beside the chart, a partner comment and a revision (day
15); then data about people on invented case cards (day 16). Two days go to the investigation and its report, the row
the read counts as the heaviest. Class data is about the class library's books only.

Assessments: end-of-unit day 17, about 30 minutes, pairs taking turns at the device for the record and chart items
while the others write the case card; day 15's revised report is read beside it, unscored. The case card item asks for one person and one group who could
be helped or hurt (E4-DAT-IM-11 names individuals and groups). Response on day 18.
Candidate kept, zero days: the base's paper database start (record cards) inside day 13.

## Unit 4: The class quiz, built in pieces (days 19 to 23, weeks 19 to 23)

Concept area: programming. Practices CT9, CT7, CT8, IC4, IC5, IC3. Trace (day 19: the counting loop and the score
program in a trace-table, predicted then stepped through), compare (day 20: two programs, one result), build in small
pieces with the test-table (day 21: the anchor's broken build and a second buggy build, bugs in the order of steps, an
event, a repeat and a choice), then the team make (day 22: the quiz shell, a paper plan as numbered steps, each
member's part, tests and comment) and the reader's feedback and revision (day 23). The ELA lean (explaining a
procedure, ELA unit 2, weeks 8 to 16) is met before day 22. Driver and navigator switch at the halfway signal. Students
trace the supplied score logic and do not write a variable's start, update or comparison (grade 5).

Assessments: the year-end check (day 24) stands for this unit's end-of-unit assessment. Day 23 carries `end` for the
kept-work part: the revised team quiz, scored on the rubric with three look-fors for each member (the working part, its comment checked against
the code, and the member's test-table rows from when the part was added and after the revision), after the day 22 build and
the day 23 note and revision (frame-write rule 19); it carries E4-PRO-PD-05 and E4-PRO-RD-07 into day 24. Response on
day 25. Candidate kept, zero days: the base's quiz-evaluating step is day 23's reader check.

## Course-level check, year-end (days 24 and 25, weeks 24 and 25)

Day 24, about 26 minutes. Unit 4 with unseen items: a trace-table for a new score program (E4-PRO-VD-06, about 5
minutes), two new programs compared (E4-PRO-PD-04, about 5), a new piece-by-piece build to find, fix and retest on a
test-table, on paper with a partner as the computer (E4-PRO-TR-08, about 10). E4-PRO-PD-05 and E4-PRO-RD-07 come from
day 23's scored quiz; no comment item is repeated. E4-PRO-TR-08 is met by the debug item together with day 23's
test-table record, which shows debugging repeated as the program grew. Units 1 to 3 sampled with three short new items (about 6 minutes):
a written algorithm's choice line traced (E4-ALG-PS-01), a new data case card (E4-DAT-IM-11), a new network need
(E4-SYS-NT-14). Unit 3's end-of-unit record is carried unscored. The unit 4 items do not repeat an assessment just
given: the team product is scored, not re-asked. Day 25 reteaches and records each student's support and gains for
grade 5.

**Codes no course-level check samples** (rule 3): E4-SYS-IM-15, E4-DAT-DC-09 and E4-DAT-DI-10 are left to their
end-of-unit records (days 5 and 17), carried unscored, because the frame budgets the year-end sitting at 26 minutes
and the two data ids need device time a sitting cannot hold. Unit 5's five ids (E4-ALG-ML-02, E4-SOC-HU-18,
E4-SOC-HI-16, E4-SOC-ET-17, E4-SOC-CE-19) are taught after the year-end check, which the frame places in week 24 so
unit 5 has seven weeks, and are checked by unit 5's own end-of-unit assessment on day 31.

## Unit 5: Machines that learn, and people who make tools (days 26 to 32, weeks 26 to 32)

Concept area: algorithms and design (machine learning) with computing and society. Practices CT7, IC3, HCD10, ESR1.
The sorter anchor and one property of the training-set changed at a time (day 26), then the human and machine
learning comparison (day 27) as one story, the order the row sets; then the people on the timeline (day 28), a tool's
limit and what it led to (day 29, the timeline and chart from day 28 and unit 1), and workers learning new tools
(day 30). The two rows the progression read counts as two sessions each (g4-ml-learning, g4-history-limits) get two
days each. Days 28 and 30 are sensitive ground (Native, Black and women's history; work change in a family): every
card carries a dated source the unit writer opens; workers are invented. Both days get the sensitivity read before the case cards (docs/pipeline/briefs/sensitivity-read.md).

Assessments: end-of-unit day 31, about 30 minutes, five unseen items, one per code; the worker item asks
what the worker had to learn when the tool arrived and one way they keep learning (both parts of E4-SOC-CE-19). Response on day 32. Candidate
dropped: a local worker's visit (the cases carry the row, and a visit needs a school's own arrangement).

## Shorter path

**A shorter period (30 minutes).** Every day keeps its place and its ids. The retrieval trace stays at three minutes
and the device close at four, so teaching drops from about 33 to about 23 minutes: each Understanding day keeps its
worked example and its first practice and moves the last practice round into the next day's retrieval; days 22 and 23
keep the build and revision on separate days (no score before the revision). The four 30-minute sittings (days 5, 11,
17, 31) open with settling and instructions, not a retrieval trace, at every length; in a 30-minute period day 5's fault items run on picture fault cards, with no
device close; day 17 moves its case-card item to the first ten minutes of day 18, before the
reteach, so the device items keep their time.

**A year about 10 school days short (two weeks, two sessions).** Two fold-in days, nothing assessed on either and no
owned part only there:

| Fold-in day | Where its work goes | Minutes saved |
|---|---|---|
| 8 (modify the pattern algorithm) | The rewrite with a repeat becomes day 7's last ten minutes; the one-line change to a choice opens day 9 as its retrieval | 40 |
| 6 (unit 1 respond) | The most-missed day 5 item opens day 7 as its wrong example; the E4-SYS-NT-14 retry is day 11's new connection item, inside the sitting; in the short year day 9's retrieval becomes a new device-life item for E4-SYS-IM-15 in place of the login-or-permission cards, which day 11 samples anyway; day 12 adds both codes to its reteach beside E4-SYS-HW-12 and E4-SYS-SE-13 | 40 |

That is 30 of the frame's 32 sessions, 80 minutes saved. Day 6 follows the unit 1 end-of-unit sitting, so it may
fold. The shorter-year rule, the same from kindergarten to grade 5: a respond day after an end-of-unit sitting may fold into the next day's opener with a self-check; a respond day after a course-level check never folds; check days keep their weeks, and a lost week before a check moves the teaching days, never the check. No other day folds: every other teaching day is the only day
of its id or a check, a respond day after a check, or a step of the team quiz.

## For the lead

1. **Day 26 tool.** The one-screen picture sorter (frame For the lead 4, a TOOL-ASKS item) and the queued sorter trainer
   (later.csv L148) may be one tool or two; day 26 runs on the class-as-sorter path either way and meets E4-ALG-ML-02 in
   full. Say which in the tool queue.
2. **Calendar.** Week 24 is shared with music's year 4 year-end check (both specials, not a rule 1 break).

Unsure of: whether the 30-minute shorter period should instead merge days, as the arts once-a-week paths do; I kept
every day because the course already meets once a week.
