# Expert cold read: scope and sequence of Computer Science, Grade 7 (2026-11-26)

Job: docs/pipeline/briefs/sequence-read.md, course `computer-science-grade-7`, subject computer science (lens
docs/agents/lenses/computer-science.md; bar: docs/ADOPTION-BAR-SUBJECTS.md section "5. Computer science" with
docs/courses/computer-science/STANDARD.md and docs/courses/computer-science/APPROACH.md), with the additions in
build/scope-writes/CS-READ.md and the writer's brief build/scope-writes/CS-BRIEF.md. The scope was written by a fresh
agent; read cold.

## What I read

- docs/courses/computer-science-grade-7/scope-and-sequence.md (all) and data/plans/computer-science-grade-7/days.csv
  (all 64 rows: goal, skills, codes, assess, school_day, note, retrieves).
- docs/courses/computer-science-grade-7/frame.md (all: the course in brief, Seams, Models carried, Units, Course-level
  checks, Cross-subject, For the lead, Source map).
- The 19 grade 7 rows of data/progressions/computer-science.csv; the 15 owned statements in
  data/standards/csta-2026-statements.txt (read for parts only, not copied).
- docs/agents/EXPERT.md, the lens, the bar section, STANDARD.md and APPROACH.md in full; docs/courses/CALENDAR.md
  (rules 1 and 3); the grade 7 rows of data/plans/calendar.csv; the grade 7 parts of
  docs/reviews/frame-computer-science-grades-6-to-12-2026-11-25.md and
  frame-computer-science-grades-1-to-12-fixes-2026-11-26.md. Repeat tags are judged against those and the 2026-11-26
  arts sequence reads (for example sequence-music-grades-6-to-8-2026-11-26.md); no earlier computer science
  sequence read exists.
- Gates: `scripts/sequence.py check computer-science-grade-7`: 0 failures. `scripts/plan.py check`: this course's
  sequence and frame 0 failures ("6 units, 64 days (58 in units, 6 for checks and respond days)"). `scripts/frame.py
  calendar`: grade 7 computer science checks in weeks 16, 31 and 32, no break. `scripts/stale.py check`: nothing for
  this course.
- One web search (FCC hotspot vote, finding 1). The bias study and OPM facts in findings 4 and 11 are from memory and
  say so.
- EXPERT.md asks for each finding to be logged with `scripts/plan.py defect`; this brief says to edit no file but this
  report, so the caller logs them.

## Verdict

The scope and sequence is sound: all 15 owned ids sit on teaching days and on an end-of-unit assessment or a check
that stands for one, no id is claimed outside the frame's owned rows (the five used-again ids carry `~` in notes only),
school_day follows one stated formula that lands every unit and check in the frame's weeks, every unit has unplugged
days, and the readiness and retrieval plan matches the Seams. The biggest risk is in what a teacher would say on
society days: day 50 sends students to help programs that changed or ended in 2024 and 2025, and the day 39 bias cases
are worded beyond what their studies found. The one change that matters most is finding 1 (date-check the access
programs and use the 2025 vote as the day's two views), with the 40-minute assessment sittings on days 9 and 21
(finding 2) next.

## Findings, most serious first

### 1. Day 50 teaches access programs that no longer run

**What is wrong.** Day 50's goal sets "what libraries, hotspots and government programs do" about home internet. Two
of the best-known programs changed: the federal Affordable Connectivity Program stopped taking new funds and ended in
June 2024 (from memory), and on 2025-09-30 the Federal Communications Commission voted 2 to 1 to end E-Rate support for
library and school hotspot lending and school bus Wi-Fi (Route Fifty and ALA pages below). A writer working from the
frame's wording would build a day on help that is gone. **Why it matters.** Bar item 4 (real, current cases); a
student whose family relied on a lending hotspot hears it described as available. **Fix.** In day 50's note: "Programs
named as of the day read; the teacher page checks each is still running." Use the 2025-09-30 vote as the day's case:
government bodies may be named (STANDARD.md "Real cases"), and the majority order and the dissenting statement give the
society day its two views, each dated. Keep the NTIA survey as the data source. LAYER: sequence. REPEAT: new.
Confidence: firm for the 2025 vote (two sources), likely for the 2024 end date.

### 2. Days 9 and 21 hold 40 minutes of items in a session that teaches about 35

**What is wrong.** Day 9 budgets about 20 minutes for MS-PRO-RD-17 and 20 for MS-ALG-PS-01; day 21 budgets 10, 10 and
20. The frame says a 45-minute session teaches about 35 minutes after its opening and set-up. Days 42 and 53 (36) and
the checks (35, 25, 30) fit; these two do not, and the Shorter path's 40-minute line says nothing about sittings at
all. **Why it matters.** A sitting that overruns ends with the design or the test-plan task half done, the task each
unit most depends on. **Fix.** Day 9: about 17 and 18 minutes (the new program cut to fifteen lines, every construct
role still asked). Day 21: 8, 7 and 20. Shorter path, first bullet, add: "At 40 minutes a sitting keeps every id's
item and cuts one read item per id (about 30 minutes)." LAYER: sequence. REPEAT: yes (sequence-music-grades-6-to-8
finding 5, sittings without a budget that fits). Confidence: firm.

### 3. Days 30 and 61 still carry `end` marks the gate no longer needs

**What is wrong.** Days 30 and 61 are teaching days marked `end` "so the gate sees the unit close", and For the lead 1
asks for the sequence.py fix. The lead fix of 2026-11-26 is in: a course-level check on the day right after a unit's
last day now counts as that unit's end-of-unit assessment. **Why it matters.** An `end` mark on a teaching day reads as
an assessment of work students make while still learning, and "read with the check" invites double scoring of the
brief and the claim. **Fix.** Clear `assess` on days 30 and 61; drop "End-of-unit, part 1 ... Marked end" from both
notes and from the unit 3 and unit 6 bullets of the .md; the brief and the claim stay as kept work the teacher reads,
unscored. Delete For the lead 1. Rerun the gate. LAYER: sequence. REPEAT: yes (stale lines, sequence-music-grades-6-to-8
finding 11). Confidence: firm.

### 4. The day 39 bias cases are worded beyond their sources

**What is wrong.** Day 39 says "speech recognition that misses some accents more often" and "face matching wrong more
often for some groups". The two sources the frame names say narrower things (from memory, check before use): the 2020
speech study (Proceedings of the National Academy of Sciences) compared Black and white American speakers and found
about twice the word error rate for Black speakers across the five systems tested; it is about dialect and race, not
"accents" in general. NISTIR 8280 (December 2019) found demographic differences in false matches in most of the many
algorithms tested, with the size varying widely and a few of the most accurate showing very small differences. Neither
source is named on the day. **Why it matters.** Lens: society with evidence; a case students later find overstated
teaches them the course exaggerates. **Fix.** Day 39 goal and note: "speech recognition that, in a 2020 study, misheard
Black speakers' words about twice as often as white speakers'; face matching that, in a 2019 federal test, made more
false matches for some groups in most of the systems tested, by very different amounts". Source lines: NISTIR 8280,
December 2019; Proceedings of the National Academy of Sciences, 2020. The sensitivity guard stays as written. LAYER:
sequence. REPEAT: new. Confidence: likely (memory of both reports; the frame's sensitivity pack holds both).

### 5. Unit 1 has students change and build code with no debugging step taught

**What is wrong.** Day 5 modifies the anchor and day 7 builds the design in text, but no unit 1 day teaches what to do
when the run differs from the prediction; debugging arrives on days 15 and 16. The frame's Out line excludes debugging
as a scored skill, not as a step. **Why it matters.** Lens day error: "a bug students meet with no debugging step
taught"; on day 7 pairs will hit errors and a non-specialist teacher is not to debug on the fly (APPROACH teacher page
rule). **Fix.** Day 5 note: "One planted bug in the anchor is found with the four-step routine (predict, run, find the
first line where the run differs from the trace, change one thing and rerun); the routine is on the day 7 build
sheet." Unscored, no day added. LAYER: sequence. REPEAT: new. Confidence: likely.

### 6. Day 14 asks students to use the reference page before one lookup is worked

**What is wrong.** Day 14's goal opens with students finding and calling a function not yet shown. APPROACH ("How a day
opens"): no "try it" on a construct before one worked example has been shown and traced. MS-PRO-PD-13 then goes
straight from this day to the make days (17 and 18). **Why it matters.** Trace before modify before make is the brief's
first check; the reference-page skill is the one most likely to stall a class, and it is a scored look-for in the
product. **Fix.** Day 14 goal: "From a worked lookup (the teacher finds the count entry, reads its example, writes the
call and the class predicts the output), pairs change the worked call for a new list, then find and call a second
function alone; one worked error-guide lookup before pairs use it." Day 16's bug fixes name the error guide, so it is
used again before day 17. LAYER: sequence. REPEAT: new. Confidence: likely.

### 7. Days 17 to 20, the scored product, name no paper path

**What is wrong.** Every other device day names its paper path; days 17, 18, 19 and 20 carry only the generic "written
four ways" line. These are the days that score MS-PRO-PD-13 and MS-PRO-TR-19. **Why it matters.** CS-READ: a device day
always has a paper path that meets the same ids. A class with no devices would not know how the product runs, or that
MS-PRO-TR-19 is met in full on paper while MS-PRO-PD-13 is part met. **Fix.** Days 17 and 18: "Paper path: the program
written on lined code sheets, tests run 'be the computer' on the test-table, the reference entry and error guide
printed; MS-PRO-TR-19 met in full, MS-PRO-PD-13 part met without a device." Day 19: "Paper path: printed programs
swapped." Day 20: "Paper path: the revised sheet, test-table and change log handed in." LAYER: sequence. REPEAT: new.
Confidence: firm.

### 8. Day 6 goes from a worked design straight to a student's own

**What is wrong.** Day 6 shows one worked design, then each student designs for a new problem in the same session;
there is no modify step on a design before the make (day 7 builds, day 8 revises). **Why it matters.** MS-ALG-PS-01 is
the unit's scored design; trace, modify, make is the course's order for algorithms as well as code (APPROACH "Order
inside a unit"). **Fix.** Inside day 6: after the worked design, students first change it for one new requirement (add
the "goal met" value, or a second rate) and retrace, then start their own design, finished on day 7's first minutes
before the build. No day added. LAYER: sequence. REPEAT: new. Confidence: judgment call.

### 9. Day 28's "two views" could set a nation's right to govern its data up for debate

**What is wrong.** Day 28 gives data sovereignty "with two views and a dated source each". Read by a busy writer, the
two views become "should a tribal nation control data about its people", which the frame's guard ("not as a problem to
solve") forbids. **Why it matters.** Native content; the frame's sensitivity pack (CARE Principles) treats the nation's
authority as given. **Fix.** Day 28 note: "The two views are on a choice inside the case (where the data is stored, who
may see it, what is shared back), never on whether the nation may govern its data; the nation's own published account
is one of the two sources." LAYER: sequence. REPEAT: new. Confidence: likely.

### 10. Unit 6's anchor and its environment source fit loosely

**What is wrong.** The anchor is the automatic telephone exchange, with facts "from the Computer History Museum
timeline". The early automatic exchange was electromechanical switching; the computing case is the computer-controlled
exchange that came into service in 1965 (from memory). Day 56 adds "energy used, e-waste" from the EPA electronics
donation and recycling page, which is about household electronics, not exchanges. **Why it matters.** MS-SOC-HI-39
asks for a historical computing technology's impacts on society and the environment; a day whose source does not speak
to the anchor leaves the environment half unsupported. **Fix.** Day 55: anchor on the move to computer-controlled
exchanges (told without a company name), with the teacher page confirming the date from a museum or government source
before use. Day 56: the environment half follows the phones the network made common (handsets to today's phones) with
the EPA page as its source, or uses the frame's personal-computer option for this day. LAYER: sequence. REPEAT: new.
Confidence: likely.

### 11. Two society days lack a second view or a dated source

**What is wrong.** Day 48 (Application, society) has one source, the 2016 House Oversight Committee report on the 2015
OPM breach; APPROACH asks a society day for two views, each with a dated source. Day 59 says what AI, robots and
virtual reality "can and cannot do now" with no source or date. **Fix.** Day 48: add the agency's own inspector
general reporting as the second dated source (from memory, check), and a guard: talk stays on what was taken and the
effect on people, not on who is said to have done it. Day 59: "From a dated source, as of the day read; the teacher
page rechecks it each year." LAYER: sequence. REPEAT: new. Confidence: likely.

### 12. Program retrieval thins out after unit 2

**What is wrong.** From day 23 to day 61 only days 24, 28, 29, 35 and 46 open with a program or pseudocode trace, yet
day 63 scores MS-ALG-PS-01 and grade 8's text project needs unit 1 and 2's constructs. Several openers repeat the day
before's row (day 41 and 40 both g7-personal-data; day 45 and 44 both g6-packets). Day 8's `retrieves` is
g6-model-algorithm while its note says "a retrieval trace of the anchor loop". **Fix.** Day 8 retrieves
g7-analyze-code. Day 41 retrieves g7-design-with-variables (a pseudocode trace), day 45 g7-lists (a list loop), day 50
g7-test-refine (a test-table). Seams retrievals are untouched. LAYER: sequence. REPEAT: new. Confidence: likely.

### 13. Small points

- Pair roles are named on days 7 and 17 only; the frame keeps IC5 roles all year. Add "Pair roles: driver and
  navigator, switching at the halfway signal" to the notes of days 2, 5, 12 to 14, 16, 18 to 20, 23, 25, 36 to 38 and
  46.
- Shorter path fold 1 moves the written account "to homework"; a home task assumes home time. Make it three lines at
  the end of day 7 instead.
- For the lead 2 (five owned codes on no course-level check): each of the five is scored on an unseen end-of-unit
  sitting, which is enough; a six-minute item on day 63 would be too short to ask each part of MS-ALG-IM-10 or
  MS-SYS-SE-32. My pick: keep as is.
- For the lead 3 (kinds of days 6 and 48) is right; the frame's Day kinds list should take the change at the lead's
  next frame pass.

LAYER: sequence. REPEAT: new. Confidence: likely.

## What the gates settled, and what holds

- **Standards in full.** Each owned statement's parts are carried: RD-17's four constructs (days 1 to 4, all asked on
  day 9); PS-01's several data types (day 6, day 9); PS-04's four approaches and the mix (days 34, 35); ML-07's examples
  and non-examples with accuracy and bias (days 36 to 38); IM-10's benefit, harm, ethics and bias (days 39 to 41);
  DI-26's design choices (days 24, 25); IM-28's benefits, risks, metadata, ownership, privacy and sovereignty (days 26
  to 29); PD-13 (days 14, 17, 18, 20); TR-19's test, refine and document (days 15 to 20); HI-39's society and
  environment (days 55, 56; see finding 10); ET-40's capability, limits and environmental cost (days 59, 60); CE-45's
  create and replace (days 57, 58); NT-35's roles and resilience (days 44 to 46); SE-32's three sides (days 47, 48);
  IM-37's ability, place, income and age (days 49, 50).
- **Order.** Read before modify before make holds on every programming row except findings 6 and 8. Lists (days 11 to
  13) come before the build that uses them; tests are planned (day 15) before the bug-fix day (16) and the product.
- **Readiness and retrieval.** Every assumed row is a grade 6 row, the year before; each is retrieved on its Seams day
  and readiness-checked in the last ten minutes of day 1 or a respond day (10, 22, 33, 43, 54), never on another
  unit's first day. Day 33 covers a class whose school left out grade 6 unit 4.
- **Calendar.** school_day = 5k-2 and 5k for course days 2k-1 and 2k; days 31 and 32 on school days 78 and 80
  (week 16), no other grade 7 mid-year check that day; days 62, 63 and 64 on 155, 158 and 160, week 32 the finals week
  (CALENDAR rule 3). Leans meet math and science on the stated days.
- **Load.** Units teach on 8, 10, 8, 8, 9 and 7 days as the frame sets; the three list days are 6 percent of teaching
  days, under C1's 10.
- **Shorter path.** Five named fold-ins; none cuts an assessed day or an owned part.
- **Source map.** Base days are named and provisional until the store folder exists (For the lead 4).
- **Checks that do not repeat.** Days 32 and 63 sample earlier units with new item forms, and the .md says so.

## The lens checklist (scope and sequence layer)

| Line | State |
|---|---|
| All five concepts taught, programming not most days | Met: programming 22 days, data 8, algorithms 10, systems 11, society 7 |
| AI inside the concepts, not one late unit | Met: data (unit 3) under the model (unit 4) under society (unit 6) |
| Read, then modify, then make | Met, except findings 6 and 8 |
| Unplugged teaches, plugged tests | Met: every unit has unplugged days; device days name their job |
| Notional machine taught | Met: day 1 names it, trace-tables on days 1 to 8 |
| Debugging taught as a method | Part: from day 15; finding 5 for unit 1 |
| Practices inside content | Met: each unit names its practice codes on days |
| Society with evidence, dated, two views, no company | Part: findings 1, 4, 9, 10 and 11 |
| Non-specialist teacher | Met at this layer (teacher-page items belong to the section plan) |
| Construct used before taught | Met: lists before list loops; variables before design |
| Id below or past its boundary; Specialty claimed | Met: none; lists counted as outside days |
| Every device day has a paper path | Part: finding 7 |
| Pair work with roles | Part: finding 13 |
| No claim that coding improves thinking | Met |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 9 items about 17 and 18 minutes, its new program fifteen lines; day 21 items 8, 7 and 20 | A sitting fits the 35 teaching minutes | days.csv days 9, 21 |
| Clear `end` on days 30 and 61; the brief and the claim stay unscored kept work | The gate now takes the check as the unit's end | days.csv days 30, 61; scope-and-sequence.md |
| Day 5's planted bug and four-step routine, unscored | Students meet bugs on days 5 and 7 | days.csv day 5 |
| Day 14 opens with a worked lookup, then a changed call, then one alone | Worked example before "try it" | days.csv day 14 |
| Day 6: modify the worked design before the student's own | Trace, modify, make on designs | days.csv day 6 |
| Day 8 retrieves g7-analyze-code; days 41, 45, 50 retrieve g7-design-with-variables, g7-lists, g7-test-refine | Spaced program retrieval before day 63 and grade 8 | days.csv |
| Day 39's case wording and source lines as finding 4 | Match the studies | days.csv day 39 |
| Day 50 uses the 2025-09-30 vote as its two views | Current, government body, two dated views | days.csv day 50 |
| Shorter path fold 1: the written account at the end of day 7, not at home | No home task assumed | scope-and-sequence.md |
| For the lead 2: keep as is | Each code has an unseen end-of-unit sitting | scope-and-sequence.md |

## For Cory

Nothing. Every finding is inside the course's standards and cases.

## For the source list

- Route Fifty, "FCC ends federal funding for Wi-Fi hotspots, access on buses", October 2025:
  https://www.route-fifty.com/digital-government/2025/10/fcc-ends-federal-funding-wi-fi-hotspots-access-buses/408519
  (the 2025-09-30 vote, 2 to 1).
- American Library Association, FAQ on the reversal of E-Rate hotspot lending:
  https://www.ala.org/advocacy/federal-resources/broadband-policy/erate/hotspot-FAQ (the libraries' view, dated).

## Sources

- The two pages above, for finding 1.
- NISTIR 8280 (nvlpubs.nist.gov) and the 2020 speech recognition study, named in the frame; read from memory for
  finding 4, not opened in this run.
- The House Oversight Committee's 2016 OPM report, named in the frame; from memory for finding 11.
