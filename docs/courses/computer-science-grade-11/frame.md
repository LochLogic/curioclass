# Course frame: Computer Science, Grade 11

Course `computer-science-grade-11` (catalogue id `cs-k12`), grade 11, one year. Draft frame, 2026-11-25, written to the kindergarten pilot's shape and fixes; the scope and sequence sets the days later.

## The course in brief

- **Units.** 6, in the order the year's ideas build: find, rate and fix a security flaw (systems and security, the
  shortest re-entry from grade 10's breach causes, and the find, test and fix habit the year keeps), test a program
  against its specification and judge generated code (programming, which turns that habit on code), charts that let
  us decide (data, widening grade 10's three-variable chart to a dataset of many variables), what a model learned (machine learning, which needs
  unit 2's test-table and unit 3's data work), who an algorithm serves and who pays for the data (impacts, which
  audits what unit 4 built), and who carries the cost of our computing (systems, policy and emerging technology, the
  year's closer).
- **Days.** 64 course days: 60 in units, 2 for course-level checks (1 after unit 3, 1 after unit 6) and 2 respond
  days (one after each check). Two lessons a week of about 45 minutes, 32 weeks: the computer science default for
  grades 6 to 12 (docs/courses/computer-science/STANDARD.md section 2, Cory, Desk q-fix-cs-1), so course day n falls
  in week n/2 rounded up. The 45 minutes hold set-up, clean-up and collecting work: each lesson opens with a retrieval
  trace or predict task of at most five minutes (APPROACH.md, "How a day opens"), a device lesson keeps three minutes
  at the start to open the page and four at the end to save or print work and close devices, so a device lesson
  teaches for about 33 minutes and an unplugged one for about 38. Each unit's days include its end-of-unit
  assessment and end with a respond day, with one shape for a unit that a course-level check follows directly (the
  kindergarten pilot's pattern, docs/reviews/frame-computer-science-kindergarten-fixes-2026-11-25.md): in units 3
  and 6 the check stands for the unit's own end-of-unit assessment and the check's respond day is the unit's
  respond day. So units 1 to 6 run 9, 14, 11, 12, 7 and 7 days, of which 7, 12, 11, 10, 5 and 7 teach: 52 teaching
  days, 6 assessment days (4 end-of-unit, 2 course-level) and 6 respond days. Days follow the load of the rows,
  not equal shares: unit 2 owns two device rows with a Specialty I test plan on a several-function program and gets
  12 teaching days; unit 4 owns the year's only model build, a training-set review and its Specialty I rebalance
  and gets 10; units 5 and 6 own single unplugged society rows (the progression's notes call each one day) with one
  written evaluation, one proposal and one team design document between them, and get 5 and 7. 64 lessons for 13
  rows is about five a row, counted with checks; no unit runs over 25 days, so there are no mid-unit assessments.
- **Check weeks.** Grade 11's core checks take weeks 10 (US history I), 13 (physics), 14 to 15 (Algebra II), 16
  (English language arts), 19 (US history I), 22 (physics), 22 to 23 (Algebra II), 24 (English language arts) and the
  finals week 32 (docs/courses/CALENDAR.md). This course's mid-year check sits on day 35, week 18, a week no core
  course uses, with its respond day on day 36 in the same week; its year-end check sits on day 63 in the finals week
  32, which 9 to 12 may share (CALENDAR.md stagger rule 4), with its respond day on day 64, the year's last lesson.
  Overlaps with other after-core subjects' check weeks are the lead's calendar pass (For the lead 1).
- **Standard.** The 12 grade 11 HS Foundational ids of the 2026 CSTA PK-12 Computer Science Standards that the
  progression gives this grade (STANDARD.md "Ownership of MS and HS ids": grade 11 owns 12, with HS-DAT-IM-27 moved
  here, Cory 2026-11-20, Desk q-prework-cs-1): HS-SYS-SE-33, HS-PRO-TR-19, HS-PRO-RD-18, HS-DAT-DI-25, HS-DAT-DI-26,
  HS-ALG-ML-07, HS-ALG-ML-08, HS-ALG-IM-10, HS-DAT-IM-27, HS-SYS-IM-37, HS-SOC-HI-39, HS-SOC-ET-42; and grade 11's
  four named Specialty I ids, taught and checked in full inside the row that already teaches the topic (STANDARD.md
  "Specialty standards"): S1-CYB-TS-08 (unit 1), S1-SWD-TR-07 (unit 2), S1-DSC-VZ-11 (unit 3), S1-AIN-DD-02 (unit
  4). No S2 id and no X + CS id is claimed. Each id is taught at the depth its owner row's notes set in our own
  words, checked against the boundary statements in the source store's copy of the standards (read for this frame,
  2026-11-25, never copied or quoted; STANDARD.md "Depth"), and "What students learn" says what is out. Plans cite
  ids and state each action in a short phrase of our own (STANDARD.md "Quoting"); the credit line "Standards: 2026
  CSTA PK-12 Computer Science Standards (CC BY-NC-SA 4.0)" goes on any day that leans on a statement. Check set: each
  unit plan checks itself against the computer science bar (docs/ADOPTION-BAR-SUBJECTS.md part 5, items 1 to 9) and
  the lens (docs/agents/lenses/computer-science.md); the "Check set adds" column names what the writer expects that to
  add. Values rule (DESK-ANSWERS 2026-11-12) holds.
- **Days outside the standards (bar C1).** The Specialty I parts count as days outside the course's own standards
  (STANDARD.md "Specialty standards"). They share lessons with their Foundational rows and take about 4.5 lesson
  equivalents: unit 1 session 3 (one), unit 2 sessions 3 and 4 (one and a half), unit 3 sessions 5 and 6 (one),
  unit 4 session 7 (one). That is about 9 percent of the 52 teaching days, under the 10 percent line; no other day
  sits outside the standards, so the scope writer adds none.
- **Practices and concept areas.** The Units table's sixth column (the C3 column of the core frames) names, for
  computer science, the concept area each unit teaches and the CSTA practices it teaches inside the content, by
  code and our label (STANDARD.md section 3), as bar items 1 and 2 ask. Each unit plan names the practice's day and
  task. Across the year: CT6 define the problem (units 1, 2, 5, 6), CT7 abstract and find patterns (units 1, 2), CT8
  build and plan (units 3, 4), CT9 test, debug and refine (units 1, 2, 4, 5), IC3 explain and give feedback (units 1,
  3), IC4 run a project (units 3, 6), IC5 be a reliable teammate (units 2, 4, pair roles that switch at the halfway
  signal), HCD10 learn from and include different users (unit 6), HCD11 prototype, test and refine for use and access
  (unit 2), ESR1 weigh who gains and who is harmed (units 1, 3, 4, 5, 6), ESR2 respect people and protect their data
  (units 2, 4, 5, 6). Dispositions are named in the unit plans, not here.
- **Base text.** None. The partial base (England's Teach Computing Curriculum, archived edition) covers grades K to
  8 only (STANDARD.md section 2, Cory 2026-11-16), so there is no Source map. Every program, toy system, dataset,
  case card and simulation is Curio Class's own, written from the owner rows; public data and dated cases are named
  in the unit that uses them, each with its source and an "as of" date, or marked "invented for practice". The
  order of days (read and predict, then modify, then make) follows APPROACH.md "Honest limits".
- **Day kinds.** As docs/GLOSSARY.md (row "teaching day") defines them, in computer science's words (APPROACH.md):
  Understanding is an unplugged or trace lesson, the first teaching of a construct or idea (states of data sorted on
  cards, a worked test plan traced, a worked data review, an existing policy's reasons). Fluency is a modify lesson
  or short practice of what earlier days taught: change a working chart's encoding, extend a worked test plan,
  modify a worked flaw fix; grade 11 has little of it (unit 1 session 4, unit 2 session 4 and session 12, unit 3
  sessions 3 and 11, and the retrieval openings). Application is a make, design or society lesson: write a test plan
  and run it, build a visualization or a model, audit a case with evidence, and every lesson that drafts or revises
  a report, proposal or design document. Check is an end-of-unit assessment or a course-level check; Respond acts on
  it by error letter. Inside a unit: understanding before modify before make, and no make lesson before a trace or
  modify lesson on the same construct.
- **Evidence.** Daily evidence takes APPROACH.md's forms: an exit ticket with a short program, chart or case and
  "what happens?" or "what does this show?" on trace and understanding days; the program, chart, model report or
  test-table with its look-fors and one line "what I tested and what I changed" on make days; a claim with two views,
  each with a dated source, on society days. Each end-of-unit assessment is a 40-minute paper sitting with unseen
  items, never the unit's own anchor, with the device used only where an item says so; where a unit's evidence is a
  product (unit 3's visualization, unit 4's model report, unit 6's design document), the product is drafted on a
  named day, given written feedback by the teacher before the next lesson, and revised on a named day inside the
  unit's days, and the revised version is scored at the check. No score comes from a lesson that first teaches a row,
  and an end day holds one full performance. Every "design", "create", "develop", "propose" or "formulate" id has
  its own look-for on the student's own work (a written fix, a test plan, a chart, a model, a proposal, a design
  document), never a recognition item. The respond day reteaches by error letter and repeats the missed item in a
  new form.
- **Devices.** One device per pair is the default on a device day; no student account, nothing installed, nothing
  sent off the device (STANDARD.md section 5). Device lessons: unit 1 sessions 4 and 5 (the toy system), unit 2
  sessions 4 to 6, 9 and 11 (our own Python editor with its test runner), unit 3 sessions 3, 4, 7 and 8 (a chart
  tool and a supplied simulation), unit 4 sessions 5 to 8 (a model-training tool); units 5 and 6 are unplugged. Every
  unit has at least one unplugged lesson. Every device day is written four ways (STANDARD.md "Devices and rooms"):
  one device per pair, a few devices at stations with the other pairs on the paper version, one screen run by the
  class with a student at the device, or no device. Two owned ids need a device to be met in full: HS-ALG-ML-08
  (training a model with a tool, STANDARD.md's list) and HS-DAT-DI-25 (a visualization made with a computational
  tool); on the no-device path the same days teach the idea with a pretend model on cards and hand-drawn plots on
  printed data, and the course record marks those two ids "part met without a device", never met. Every other id is
  met in full on paper: HS-SYS-SE-33 and S1-CYB-TS-08 ask for a reasoned, high-level solution and rating of a
  described flaw, not an implementation; HS-PRO-TR-19, HS-PRO-RD-18 and S1-SWD-TR-07 are met by running each planned
  test by hand trace on the printed program, which is kept to functions of at most 20 lines so a trace fits the
  reading load (APPROACH.md, Supports); HS-DAT-DI-26 and S1-DSC-VZ-11 judge printed charts and printed runs of the
  simulation; S1-AIN-DD-02 is met on the card model by changing the card set and re-testing.
- **Paper path.** Every lesson runs on paper: printed programs with trace tables and a hand-run test-table, a
  printed toy system with its settings and log, printed data and graph paper, model cards, case cards and the
  benefit-risk-chart. No tool asks for a student account, stores a student's name or sends anything off the device
  (STANDARD.md "Privacy and safety"). Generated code and generated test suggestions are supplied saved samples, some
  right and some flawed; no student uses a live generated-text tool (STANDARD.md "Generated-text tools").
- **Reading level and vocabulary.** Grade 11 text at the course's level: a lesson's reading is one page of our own
  writing or a program read at most 20 lines at a time; case cards are at most 250 words, in our words, with the
  source in the teacher's source line. Each unit names five to eight words taught in depth (in the row's words
  column), with the everyday words that have a computing meaning taught as two meanings (model, train, flaw,
  specification, cloud). Sentence frames: "I predict ___ because line ___ says ___", "This chart supports ___ but
  cannot show ___", "This helps ___ and harms ___, because ___". Assignment is read as "gets", never "equals".
- **Swap or leave out.** STANDARD.md section 3 lets a school swap or leave out a named unit for its community's
  reasons. Unit 5's cases may be swapped for another set that still audits one rule-based and one data-driven
  algorithm and evaluates one large-scale data collection, and unit 6's local infrastructure case and policy may be
  swapped for the school's own state and county; neither is left out, since they hold the year's only data-impact
  and society ids (HS-ALG-IM-10, HS-DAT-IM-27, HS-SOC-HI-39, HS-SOC-ET-42) and the bar part 5 fails a course with
  nothing on society. If a school leaves one out anyway, the course page and the unit's family note name its ids as
  not claimed that year. Units 1 to 4 carry the test-table, the data work and the model the rest of the year uses and
  are not swapped or left out. A student 18 or over makes their own leave-out choice (AGENTS.md); grade 11 students
  rarely are.
- **Safety.** No lab or field work, so no laboratory or field safety guide applies. Security days use only the toy
  system built into the page: no scanning, no attack steps, no test of a real school or home system, ever
  (STANDARD.md "Privacy and safety"); a student who knows of a real flaw tells the teacher privately and never tries
  it. Devices stay on the table with cords behind it. The scope and sequence copies these lines into each security
  and device day.
- **Costs.** Provisional, for a class of 30, beyond the school's own devices: printing only. Unit 1 $4 (the printed
  toy system, threat and control cards, flaw-report forms), unit 2 $6 (printed programs, spec sheets, test-table
  forms, saved generated samples), unit 3 $6 (printed data extracts, broken-chart cards, graph paper, printed
  simulation runs), unit 4 $6 (model cards for the paper path, training-set summaries, data-review forms), unit 5 $3
  (case cards, benefit-risk-charts), unit 6 $4 (printed maps for the infrastructure chain, policy summary, design
  document forms), about $29 in all.
- **Sensitivity reads.** Every unit gets the fresh sensitivity agent's read (docs/pipeline/briefs/sensitivity-read.md);
  no outside reader is planned (Cory, 2026-11-14). Unit 1's described phishing case and unit 2's privacy values touch
  personal information: the agent checks each teacher page carries health's "If a student tells you something" steps
  word for word (docs/courses/health/APPROACH.md; APPROACH.md, Sensitive ground). Unit 4's digit reader and its
  writers in many countries, and unit 5's algorithm cases (bias by where a person lives, disability and background),
  need a starting pack: NIST Special Publication 1270, "Towards a Standard for Identifying and Managing Bias in
  Artificial Intelligence" (nist.gov, March 2022); the EEOC's 2023 technical assistance on software and algorithms in
  employment selection (eeoc.gov); and the National Center on Disability and Journalism's Disability Language Style
  Guide (ncdj.org/style-guide/). Unit 5's data sovereignty case is Native content: before it reads, the agent studies
  the Global Indigenous Data Alliance's CARE Principles for Indigenous Data Governance (gida-global.org/care) and the
  United States Indigenous Data Sovereignty Network's pages (usindigenousdata.org), both written by Indigenous data
  bodies, and checks the case is told in a Native nation's or body's own published words, never as a story about
  Native people told by others. Unit 6 touches mining, factory and e-waste workers and towns that host data centers:
  the agent studies the UN Global E-waste Monitor 2024 (ewastemonitor.info) and the US Environmental Protection
  Agency's electronics donation and recycling pages (epa.gov/recycle), and widens the pack to the brief's five
  sources, two of them from the communities named, and records them. No unit is hands-on in the laboratory sense, so
  no safety agent read is planned beyond the Safety lines above, which the sensitivity read confirms are on each day.
  The course's checks get the answer-key agent's read.

## Seams

### Picked up from Grade 10 computer science

Every grade 10 row here was taught the year before, so each opens as a retrieval task of at most five minutes inside
the lesson that first uses it (lesson 16), never as a readiness check or a reteach. Two rows come from further back
and get a readiness check of ten minutes, given at the end of the lesson before the unit opens (lesson 16, counted by
grade number as sequence-write.md rule 2 sets). The last use of each grade 10 row is the unit of
docs/courses/computer-science-grade-10/frame.md named below, with its course days; that frame's "Handed on to Grade 11"
table names the same grade 11 rows.

| Earlier row | Last use | What it hands on | Row here | Unit here | How it opens |
|---|---|---|---|---|---|
| g10-breach-causes | Grade 10 unit 3 (days 22 to 29) | Why a breach happened, rated on the cia-triangle | g11-fix-security-flaw | 1 | Retrieval, session 1: rate a short breach case's cause on the cia-triangle |
| g10-analyze-code | Grade 10 unit 1 (days 1 to 12) | Reading and tracing a several-function program with a list, and one saved generated sample traced | g11-evaluate-vs-spec; g11-evaluate-generated-code | 2 | Retrieval, session 1: trace a given function on a list and predict its output |
| g10-apis-docs | Grade 10 unit 1 (days 1 to 12) | Using a library function from its documentation, credited in a comment | g11-evaluate-generated-code | 2 | Retrieval, session 8: read a short documentation entry and say what the call returns and what credit it needs |
| g10-visual-data | Grade 10 unit 4 (days 33 to 42) | A three-variable chart read and made | g11-multivariate-viz; g11-evaluate-simulation | 3 | Retrieval, session 1: what does this three-variable chart show and not show? |
| g10-clean-text | Grade 10 unit 4 (days 33 to 42) | Cleaning messy text data before use | g11-multivariate-viz; g11-build-ml-model | 3 (first use); 4 | Retrieval, unit 3 session 1: clean three messy rows; again in unit 4 session 4 |
| g10-choose-ai-type | Grade 10 unit 2 (days 13 to 21) | Choosing an AI algorithm type for a task and justifying it | g11-training-data-review; g11-build-ml-model | 4 | Retrieval, session 1: which type fits a digit reader, and why, in two sentences |
| g10-verify-consistency | Grade 10 unit 4 (days 33 to 42) | Checking data for consistency and the expected types, values and ranges | g11-training-data-review | 4 | Retrieval, session 2: find the two rows that break the stated ranges |
| g10-evaluate-algorithms | Grade 10 unit 2 (days 13 to 21) | Comparing algorithms by test cases, counted steps and clarity | g11-build-ml-model | 4 | Retrieval, session 4: which of two given tests tells the two algorithms apart? |
| g10-design-hcd | Grade 10 unit 5 (days 43 to 53) | Human-centered design steps and the benefit-risk-chart for a small technology | g11-algorithm-ethics | 5 | Retrieval, session 1: who was this design for, on the benefit-risk-chart |
| g9-data-and-people | Grade 9 unit 4 (days 35 to 43), two grades back | A first look at who benefits from and who is exposed by data collection | g11-data-scale-ethics | 5 | Readiness check: the last ten minutes of day 48 (unit 4's respond day), a short case and "who gains, who is exposed?"; its results shape session 4 |
| g10-network-diagram | Grade 10 unit 3 (days 22 to 29) | A small network diagram with one request traced through it | g11-infrastructure-impact | 6 | Retrieval, session 1: trace one photo upload through a given network-diagram |
| g8-design-for-all | Grade 8 unit 1 (days 1 to 13), three grades back | Who can and cannot use a system, and design for different users | g11-infrastructure-impact | 6 | Readiness check: the last ten minutes of day 55 (unit 5's respond day), "who can and cannot use this kiosk, and why?"; its results shape session 2 |
| g10-history-policy | Grade 10 unit 6 (days 54 to 61) | A computing policy placed on a timeline with its reasons | g11-policy-change | 6 | Retrieval, session 3: place the existing policy on the timeline and say what it was for |
| g10-emerging-impacts | Grade 10 unit 6 (days 54 to 61) | The impacts of an emerging technology | g11-emerging-solution | 6 | Retrieval, session 5: one benefit and one harm of a named emerging technology |
| g10-human-choices | Grade 10 unit 6 (days 54 to 61) | The choices people make in what machines do | g11-emerging-solution | 6 | Retrieval, session 5 (with the line above): which choice in this system was a person's? |
| g10-career-skills | Grade 10 unit 5 (days 43 to 53) | The skills computing work asks for, in a private portfolio | g11-career-plan | 6 | Retrieval, session 5: match four team roles to the skill each asks for |

Models from earlier grades used here (test-table, text-program, list-diagram, data-table, data-visualization,
training-set, pseudocode, cia-triangle, network-diagram, system-diagram, timeline, benefit-risk-chart) are listed in
Models carried with the unit that first uses each.

### Handed on to Grade 12 computer science

| This course hands on | Unit here | Row that picks it up | What it does with it |
|---|---|---|---|
| g11-build-ml-model: a model built from a supplied dataset, tested on a split, with a claim checked against its test-table | 4 | g12-evaluate-ai-output | Judging AI output for accuracy and the people responsible for it |
| g11-evaluate-generated-code: saved generated code tested against a requirement, with an ownership note | 2 | g12-evaluate-ai-output; g12-attribution | Judging generated output in a team project; crediting every source the team's program uses |
| g11-evaluate-vs-spec: a test plan of ordinary, edge, error and unusual cases, unit and integration, run against a specification | 2 | g12-team-workflow; g12-refine-with-users; g12-capstone-build | The team's test plan and review in the capstone; refining with real users |
| g11-multivariate-viz: a multivariate visualization that answers a question or predicts, drawn to the conventions | 3 | g12-capstone-build | The capstone's data view |
| g11-algorithm-ethics: an audit of a rule-based and a data-driven algorithm with refinements | 5 | g12-values-in-design | Building values into a team's own design |
| g11-data-scale-ethics: a written evaluation of large-scale data collection, including for AI | 5 | g12-data-policy-debate | Debating whether a data policy works |
| g11-policy-change: a one-page proposal to change an existing technology policy | 6 | g12-data-policy-debate | The proposal's reasoning used to judge a data policy |
| g11-infrastructure-impact: a traced chain of who an infrastructure affects and why | 6 | g12-law-policy | Laws and policies on those effects |
| g11-emerging-solution: a conceptual solution with benefits and harms, raising human and artificial intelligence | 6 | g12-human-vs-ai | The debate on human and artificial intelligence |
| g11-career-plan: a team role plan and how a different perspective changes it | 6 | g12-diverse-teams; g12-career-goals | Working on a diverse team; a student's own career goals |

Every hand-on above is answered by that row's assumes in data/progressions/computer-science.csv. Three grade 11
threads end here: g11-training-data-review and g11-fix-security-flaw (with their Specialty I parts) have no grade 12
row, and g11-evaluate-simulation's judging of simulations ends the HS-DAT-DI strand; grade 12 meets the training-set
and cia-triangle again only where its own rows say.

## Models carried

| Model | Where it comes from | Introduced or first used here | Used again here |
|---|---|---|---|
| cia-triangle | Grade 9 (g9-security-measures), used in grade 10 (g10-breach-causes) | Unit 1, session 1: the breach retrieval, then each flaw and threat rated on its three corners | Unit 1 (sessions 3 to 7), the mid-year check (one unseen flaw) |
| network-diagram | Grade 9 (g9-network-sketch), grade 10 (g10-network-diagram) | Unit 1, session 2: where the club page's data sits, travels and is used | Unit 6, session 1 (one upload traced, then widened into the infrastructure system-diagram) |
| test-table | Grade 10 (g10-evaluate-algorithms) | Unit 2, session 2: each test case's input, expected and actual output | Unit 2 (the test plan is the test-table, sessions 4 to 11), unit 4 (sessions 6, 7 and 9, the model's results and claim), both checks |
| text-program | Grade 8 (g8-text-project), grades 9 and 10 | Unit 2, session 1: the library checkout program in Python | Unit 2 (sessions 3 to 12, the generated samples) |
| list-diagram | Grade 9 (g9-structures-program) | Unit 2, session 3: the checkout list drawn to trace an integration test | Unit 2 (sessions 9 and 11, the second-largest function's edge cases) |
| data-table | Grade 9 (g9-simulate-data, g9-data-dictionary) | Unit 3, session 1: the weather station extract | Unit 4 (the training set's columns), unit 5 (session 4, case data) |
| data-visualization | Grade 9 (g9-simulate-data), grade 10 (g10-visual-data) | Unit 3, session 1 | Unit 3 (sessions 2 to 10), the mid-year check |
| training-set | Grade 9 (g9-ai-tour), grade 10 (g10-choose-ai-type) | Unit 4, session 1: the digit reader's training examples | Unit 4 (sessions 2 to 9), the year-end check (a new training-set summary) |
| pseudocode | Grade 9 (g9-design-with-structures), grade 10 | Unit 4, session 4: the build steps (choose data, split, train, test, report) | Unit 4 (sessions 5 to 8 follow the lines) |
| benefit-risk-chart | Grade 8 (g8-design-for-all and earlier), grades 9 and 10 | Unit 5, session 1 | Unit 5 (sessions 2 to 5), unit 6 (sessions 2, 4 and 6) |
| system-diagram | Grade 8 (g8-design-for-all), grade 9 (g9-operating-systems) | Unit 6, session 1: the infrastructure behind one upload, drawn on a printed map | Unit 6 (session 2), the year-end check |
| timeline | Kindergarten on; grade 10 (g10-history-policy) | Unit 6, session 3: the existing policy and the changes before it | Unit 6 (session 4, the proposal) |

All go on to grade 12 except the cia-triangle and the network-diagram, whose grade 12 use is the grade 12 frame's call.

## Units

| # | Unit and compelling question | Days | Skills | Owned standards | Practices and concept areas | What students learn | Why this unit, here | Check set adds | Sensitive topics and teacher notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Find it, rate it, fix it. *What is wrong with this system, how bad is it, and what would make it safe?* Anchor: a pretend school club sign-up page built into the page, whose password rule accepts "1234" and whose sign-up list opens without a login (invented for practice) | 9 | g11-fix-security-flaw | HS-SYS-SE-33; S1-CYB-TS-08 | Concept area: systems and security. Practices: CT6 (state the flaw and what a fix must do); CT7 (classify a threat by property, data state and control type); CT9 (test the fix and record it); ESR1 (the consequences for the club's members if the flaw stays); IC3 (partner feedback on a flaw report) | Session 1 (unplugged): the anchor read on paper or one screen; retrieval rates a short breach case on the cia-triangle; the unit question. Session 2: the three states of data (at rest, in transit, in use) placed on the club page's network-diagram, and the three kinds of control (preventive, detective, corrective) sorted on cards. Session 3 (Specialty I): two common threats, a program that locks files for ransom and a flood of requests that takes a service down, each rated by which of confidentiality, integrity and availability it breaks, which data state it hits and which control type fits best (S1-CYB-TS-08 in full). Session 4 (device, modify): a worked flaw report on the weak password rule is traced (the flaw, its rating, a technical fix and a non-technical one, the consequences if it stays, a test), then each pair modifies the worked fix for a stricter rule and tests it in the toy system's settings. Session 5 (device, make): pairs find the second flaw (the open list page) themselves, rate it, write a high-level fix with a technical step and a non-technical step (a rule or training), and test the technical step by changing a setting and reading the log. Session 6: a described case, a pretend school whose staff login was caught by a fake email (invented for practice), solved on paper the same way. Session 7: flaw reports revised after a partner's written feedback. Out: no fix is written in code or implemented on any system (the standard asks for a reasoned, high-level solution); no real system probed, no attack steps, no security product named; encryption (S1-CYB-TS-09) and threat models beyond the two named are not claimed. End-of-unit (day 8): a new printed toy system with an unseen flaw to find, rate and solve, and one unseen threat to rate; respond day 9. Tools: a toy-system tool (the pretend club page with a settings panel and a log, job: show each flaw and test a setting change, nothing sent; tool ask for TOOL-ASKS.md). Curio Class writes: the toy system and its printed version, the threat and control cards, the described phishing case, the flaw-report form and its worked example | First because it is the shortest re-entry from grade 10: the cia-triangle and breach causes come straight from g10-breach-causes, the row's only assume, and the flaw report's find, rate, fix and test steps become the test habit unit 2 turns on programs. It holds one row, so it fits the opening weeks before the core courses' first checks. Our own (no base text) | Candidate: kept, a station plan for a room with four devices on sessions 4 and 5, zero added days | Phishing and logins touch personal information: no student types a real password or names a real account, and the teacher page carries health's "If a student tells you something" steps word for word. A student who knows a real flaw at school tells the teacher privately and never tries it. Agent reads: sensitivity. |
| 2 | Does it do what was asked? *How do we know a program, or code someone else wrote, is right, works well and respects its users?* Anchor: a short library checkout program in Python (functions to check out, return and list overdue books, on one list) with a one-page specification, and two saved generated versions of one more function | 14 | g11-evaluate-vs-spec; g11-evaluate-generated-code | HS-PRO-TR-19; S1-SWD-TR-07; HS-PRO-RD-18 | Concept area: programming. Practices: CT6 (read the requirement before testing); CT7 (sort test cases into kinds, test parts and the whole); CT9 (run the plan, find the first failure, judge the fix); HCD11 (judge use and access against the specification); ESR2 (privacy in the overdue list, credit for generated code); IC5 (driver and navigator roles that switch at the halfway signal) | Session 1: the specification read; retrieval traces one function on a list; predict what the program does for three given inputs. Session 2 (unplugged): kinds of test case, ordinary, edge, error and unusual user input, sorted on cards for the checkout function; the test-table. Session 3 (Specialty I): one function tested alone (a unit test) and the parts tested together (an integration test, an overdue book checked out, returned and listed), traced on the list-diagram. Session 4 (device, modify): a worked test plan for one function is extended with two new cases, and a supplied saved list of generated test suggestions is judged before use (keep, change or drop, with the reason). Session 5 (device, make): pairs write a test plan for the whole program before running it, with every kind of case and unit and integration tests (S1-SWD-TR-07 in full). Session 6 (device): the plan run, results on the test-table, first failure traced. Session 7: the program judged against the specification for correctness, how well it works for its users (plain messages, keyboard use) and the values the class set (the overdue list shows titles, never borrowers' names); a short written evaluation. Session 8: a requirement for a function that returns the second-largest number in a list, and two saved generated samples traced and predicted; retrieval on a documentation entry. Session 9 (device): each sample tested with the plan habit (an empty list, one item, the largest value twice), the flaw named. Session 10: reliability and fit to the requirement (it must use the list as given); an ownership note for each sample: who wrote it and what credit it needs, the next look at HS-PRO-PD-14 after grade 10's library credit, which grade 12 owns (g12-attribution). Session 11 (device): a generated function placed inside the checkout program and judged with the integration tests. Session 12 (fluency): mixed trace and test practice by error letter. Out: no automated testing framework, no formal verification, no live generated-text tool, nothing on how the generating model works; each function read is at most 20 lines. End-of-unit (day 22): a new short program and specification: write a test plan of every kind, run three tests by trace, judge it against the specification, and judge one unseen generated sample with its flaw and ownership note; respond day 23. Tools: our own Python editor with a step-through trace and a test runner that shows "yes" or "not yet" for each planned case (STANDARD.md "Our own editor"; tool ask for TOOL-ASKS.md). Curio Class writes: the checkout program and its specification, the worked test plan, the saved generated samples and test suggestions with their keys, the test-case cards | After unit 1, whose find, rate, fix and test steps are the habit this unit turns on code. Before unit 4, because the model's results and claim use this unit's test-table and test cases. Its two rows share one anchor program, and the specification test comes before generated code so the samples are judged with a plan students already wrote. It carries the Specialty I test plan and two device rows, the heaviest programming load of the year | Candidate: kept, a printed hand-trace version of the test runner for the no-device path on sessions 6, 9 and 11, zero added days | The values discussion is about the program's users, never a classmate; no real borrower data is used. Credit for generated code is taught as honesty about sources, not as suspicion of students. Agent reads: sensitivity. |
| 3 | Charts that let us decide. *What can a chart of many variables tell us, and when does a chart or a simulation mislead?* Anchor: a year of daily readings from one weather station (high and low temperature, rainfall, month) in a saved extract of NOAA Climate Data Online daily summaries (ncei.noaa.gov, as of the extract date), with the question "in which months do warm nights and heavy rain come together?" | 11 | g11-multivariate-viz; g11-evaluate-simulation | HS-DAT-DI-25; S1-DSC-VZ-11; HS-DAT-DI-26 | Concept area: data and analysis. Practices: CT8 (choose a chart for the data and the question, then build it); IC4 (pair roles and a milestone for the chart); IC3 (explain what each convention protects the reader from); ESR1 (who could be misled, and what decision a simulation supports) | Session 1: retrieval reads a three-variable chart from grade 10 and cleans three messy rows; the extract and the question. Session 2: a dataset of many variables (grade 10 read and made a three-variable chart), and the chart that fits each kind (a scatter plot, a line graph, a stacked bar chart, a heat map). Session 3 (device, modify): a given chart's encoding changed in the chart tool (color by month with a label, a second series). Session 4 (device, make): pairs make a visualization that answers the question, or classifies days or predicts a month's typical rainfall, and draft its caption (the draft). Session 5 (unplugged, Specialty I): graphical conventions, values rising from the bottom of the axis, bars starting at zero, color with a stated meaning, the chart type fitting the data; honest and broken charts sorted. Session 6 (Specialty I): a broken chart redrawn correctly and what each convention protects the reader from written beside it (S1-DSC-VZ-11 in full). Session 7 (device): each pair's chart revised after the teacher's written feedback (the revision). Session 8 (device): a supplied simulation of wait times at a crosswalk signal under different green-light lengths (invented for practice) is run and its output chart read. Session 9: the simulation judged: does it answer the question, what decision does it support, what does it assume, what can it not show. Session 10 (unplugged): a printed chart with a cut axis and missing weeks judged for a decision, its biases and limits. Session 11 (fluency): mixed practice from units 1 to 3 before the check. Out: no text code for the charts (the standard asks for a tool, not a program), no statistical tests, no 3D, interactive or logarithmic charts, no simulation built or its code debugged. End-of-unit: the mid-year course-level check (day 35) stands for it. Tools: a chart tool (scatter, line, stacked bar and heat map from a pasted table, no code, keyboard use, labels as well as color; tool ask) and a crosswalk simulation page (job: run with a chosen setting and show the output chart; tool ask). Curio Class writes: the weather extract and its data dictionary, the honest and broken chart cards and their keys, the simulation and its printed runs, a printed chart for session 10 | After unit 2 because a chart claim is tested like a program, by cases. Before unit 4 because the model's data and its results are read as a data-table and a chart. Its two rows share one dataset; making a chart comes before judging other people's, and the conventions sit between the draft and the revision so the revision uses them. Placed in weeks 12 to 17, before the mid-year check in week 18 | Candidate: kept, a hand-drawn plot on printed graph paper as the no-device path on sessions 3, 4 and 7, zero added days | Weather data is about places, never people. Agent reads: sensitivity. |
| 4 | What did the model learn? *Can we trust what a model learned from its data, and can we make it fairer?* Anchor: a digit reader that reads most handwritten 7s but misses the 7s written with a bar across the middle, a common way to write it in many countries (invented for practice; a supplied set of small pixel-grid digits) | 12 | g11-training-data-review; g11-build-ml-model | HS-ALG-ML-07; S1-AIN-DD-02; HS-ALG-ML-08 | Concept area: algorithms and design (machine learning). Practices: ESR1 (who the model fails); ESR2 (what personal information a training set holds); CT8 (plan the build as pseudocode, then train); CT9 (test, change the data, test again); IC5 (pair roles that switch) | Session 1: retrieval justifies an AI type for a digit reader; the anchor and the unit question. Session 2 (unplugged): a worked data review of a different supplied set: where it came from and why, how accurate and complete it is, who or what is missing, possible bias, what personal information it holds; retrieval finds the rows that break the stated ranges. Session 3: pairs write the data review of the digit set before any model is built. Session 4 (unplugged): the build steps written as pseudocode (choose data, split, train, test, report); the split into training and test done on cards and why test examples stay unseen; overfitting; retrieval on comparing two algorithms by test cases (HS-ALG-PS-03, owned in grade 10, used on a model here as review). Session 5 (device): the model trained in the browser tool on the training split. Session 6 (device): tested on the test split; accuracy as the fraction of test cases right; where it fails, recorded on the test-table by kind of 7. Session 7 (device, Specialty I): the training set changed (add barred 7s, drop duplicates, rebalance), the model retrained and compared on the same test-table; only changes that improve both fairness and accuracy are kept (S1-AIN-DD-02 in full). Session 8 (device): each pair chooses a task from three supplied datasets (leaf shapes, recycling-item features, simple sounds as number features; all invented for practice), builds and tests a model for it. Session 9: a claim about the pair's model ("it is right nine times in ten") tested against the test-table and a metric; the model report drafted (task, data, split, accuracy, failures, the claim), with each student writing the claim paragraph alone. Session 10: the report revised after written feedback. Out: no mathematics of the learning, no algorithm written from scratch, no fairness formulas, no formal bias correction or statistical proof of representativeness; the model is built with a tool. End-of-unit (day 47): a sitting with a new training-set summary to review and a supplied test-table on which students say whether a proposed rebalance should be kept and why; the revised model report is scored as the unit's product; respond day 48, whose last ten minutes give unit 5's readiness check. Tools: a model-training tool (train a small classifier on a supplied table or pixel grids, split, test, show results by group, nothing sent; tool ask), the Python editor for the pseudocode lines only. Curio Class writes: the digit set and its two kinds of 7, the worked review's dataset, the three task datasets, the card model for the paper path, the report form | After units 2 and 3: the model is judged with unit 2's test-table and test cases and read with unit 3's data-table and charts. The data review comes before the build (the row's in-grade order), and the rebalance comes after the first test so its effect can be measured. The year's only build of a model, so it gets the most device lessons | Candidate: kept, the card model's rules written as a decision table so the paper path can be retrained by changing cards, zero added days | Handwriting from many countries is shown with respect, as different correct ways to write, never as wrong. No student's own handwriting, face or voice goes into a dataset. Agent reads: sensitivity (the NIST and NCDJ pack in Sensitivity reads first). |
| 5 | Who does it serve? *Who does an algorithm help or harm, and who pays for the data behind it?* Anchor: a pretend school program that decides which students get a take-home laptop loan, sorted two ways for the same ten printed cases: a rule (only students enrolled since the fall) and a model trained on past loans (invented for practice) | 7 | g11-algorithm-ethics; g11-data-scale-ethics | HS-ALG-IM-10; HS-DAT-IM-27 | Concept area: algorithms and design, and data and analysis (impacts). Practices: ESR1 (who is helped, who is harmed, with evidence); CT9 (recommend a refinement and say how to test it); ESR2 (privacy, consent and data sovereignty); CT6 (frame what a written evaluation must weigh) | Session 1: the anchor's two outputs side by side; retrieval places the design's users on the benefit-risk-chart; the unit question. Session 2: where bias comes from in each kind, an explicit rule built into the system and training data that is unrepresentative or repeats past unfairness; the ten cases audited with evidence, what the audit could not see, and a recommended refinement for each algorithm. Session 3: a real case of algorithms in hiring, told without a company: the EEOC's 2023 technical assistance on software and algorithms in employment selection (eeoc.gov) and NIST SP 1270 (nist.gov, March 2022) as two dated sources with two views; a written audit. Session 4: large-scale collection and processing, including data used to train AI: privacy and consent, data sovereignty, bias, the spread of false information and the energy of data centers, on case cards; the readiness check's results shape the opening. Session 5: a written evaluation of one case with two views and a dated source for each; the class case is a Native nation's or Indigenous data body's own published position on who controls data about its people (the CARE Principles, gida-global.org/care, as of the read date), and pairs may pick a second case from the cards. Out: no law or regulation read (grade 12's g12-data-policy-debate), no legal or economic analysis, no proprietary system audited, no statistics, neither algorithm built. End-of-unit (day 54): a new pair of rule-based and data-driven outputs to audit with a refinement for each, and a short written evaluation of a new large-scale collection case with two views; respond day 55, whose last ten minutes give unit 6's readiness check. Tools: none (unplugged). Curio Class writes: the ten loan cases with both outputs, the hiring case card from the two dated sources, the large-scale data case cards, the evaluation form | After unit 4, because it audits the kind of model students just built and its data, so the data-driven algorithm is understood before it is judged. Its two rows share one week of cases and the evaluation habit; the policy debate on the same data is grade 12's | Candidate: kept, a second set of ten cases on a neutral program (library room bookings) for a school that swaps the loan cases, zero added days | Some students have been on the losing side of such decisions: talk stays on how the system was built and tested, never on a classmate. Cases name government bodies and courts, never companies (STANDARD.md "Real cases in society days"). The data sovereignty case is told in the Native body's own words. Agent reads: sensitivity (the CARE, US Indigenous Data Sovereignty Network, NIST, EEOC and NCDJ pack in Sensitivity reads first). |
| 6 | Who carries the cost? *Who carries the costs of the computing we use, and what should change?* Anchor: one phone traced backward and forward: where its minerals are mined, where it is built, the data center and power behind one photo upload, and where it goes when thrown away | 7 | g11-infrastructure-impact; g11-policy-change; g11-emerging-solution; g11-career-plan | HS-SYS-IM-37; HS-SOC-HI-39; HS-SOC-ET-42 | Concept area: systems and security (impacts) and computing and society. Practices: HCD10 (who the infrastructure serves and who it leaves out); ESR1 (benefits and harms to different groups and the environment); ESR2 (whose data and whose rights a policy protects); CT6 (frame the local problem before the solution); IC4 (a team plan with roles and milestones) | Session 1: retrieval traces one upload through a network-diagram, then the class widens it to a system-diagram of the infrastructure on a printed map (mines, factories, cables, data centers, power, repair, recycling); the readiness check's results shape who-can-use-it talk. Session 2: a local case, a data center's power and water use where it is built, with two views (the county's economic statement and residents' concerns) and dated sources, beside the US data center energy report of Lawrence Berkeley National Laboratory (December 2024) and the UN Global E-waste Monitor 2024; who is affected and why (geography, labor conditions, access, environmental burden), written as a traced chain. Session 3: an existing policy's reasons: a state electronics recycling law (the class example is Washington's electronic product recycling law, from memory, to be checked before use; a school may use its own state's), placed on the timeline with retrieval. Session 4: a one-page proposal to change it so it encourages responsible innovation and cuts risk, with evidence and who it affects. Session 5: team roles (design, build, test, explain) and the skill each asks for, by retrieval; a real local problem chosen from the teacher's list, and credible research on the problem and on what one emerging technology can do. Session 6: the team design document drafted: the problem, how the technology would solve it in concept, its benefits and harms to different groups and the environment, and how a different perspective on the team changed the plan; the human and artificial intelligence question it raises is noted for grade 12 (HS-SOC-HU-44, owned there by g12-human-vs-ai), and the role plan is a first look at HS-SOC-CE-45, owned by g12-diverse-teams. Session 7: the design document revised after written feedback. Out: no engineering detail and no novel technical fix for supply chains, no legal drafting or legislative process, no working prototype, no hiring or pay; the role plan stays private by default. End-of-unit: the year-end course-level check (day 63) stands for it. Tools: none (unplugged). Curio Class writes: the phone chain cards and printed map, the data center case card with its dated sources, the policy summary and timeline, the local problem list, the design document and role plan forms | Last because it gathers the year: unit 1's systems, unit 3's evidence and unit 5's impacts, widened from one system to a whole infrastructure. The policy row sits with the infrastructure row (the row's own placement) so the proposal changes a policy on the costs just traced, and the design document closes the year with a team product grade 12 builds on. Its rows hand on only to grade 12, so it can end at the finals week check | Candidate: kept, the school's own county and state as the case, from their public pages, zero added days | Mining, factory and e-waste work touches families: no student is asked about a family member's job, and workers are shown with respect, as people with a stake in the choices, never as victims. A data center or mine may be near the school: the case keeps two views. Agent reads: sensitivity (the UN e-waste and EPA pack in Sensitivity reads first). |

## Course-level checks

| Check | After unit | Check days | Respond days | What it checks |
|---|---|---|---|---|
| Course-level check, mid-year (day 35, week 18; it stands for unit 3's end-of-unit assessment) | 3 | 1 | 1 | Day 35 scores unit 3 in full and samples units 1 and 2. Unit 3, on a 40-minute paper sitting with unseen items: judge a new chart and a new printed simulation run for whether each answers its question, what decision it supports and what it cannot show (HS-DAT-DI-26); find the broken convention in a new chart, say what it hides and redraw it (S1-DSC-VZ-11); the pair's chart revised in session 7 is scored on its look-fors (HS-DAT-DI-25), each student writing a short caption of their own. Units 1 and 2 sampled with two short new items: an unseen flaw rated on the cia-triangle with a high-level fix (HS-SYS-SE-33, S1-CYB-TS-08), and a new short function with a generated variant to test against its requirement (HS-PRO-RD-18); units 1 and 2's end-of-unit records are carried unscored. Day 36, the respond day for unit 3 and the check, reteaches by error letter and repeats each missed item in a new form |
| Course-level check, year-end (day 63, week 32, the finals week; it stands for unit 6's end-of-unit assessment) | 6 | 1 | 1 | Day 63 scores unit 6 in full and samples units 4 and 5. Unit 6, on a 40-minute paper sitting with unseen items: trace a new infrastructure chain and say who is affected and why (HS-SYS-IM-37); from a short unseen policy summary, propose one change with its reason and who it affects (HS-SOC-HI-39); the team design document revised in session 7 is scored on each student's own section (HS-SOC-ET-42), and the role plan is recorded, not scored. Units 4 and 5 sampled with three short new items: a new training-set summary to review (HS-ALG-ML-07), a test-table on which to judge a model claim (HS-ALG-ML-08), and a new pair of outputs to audit (HS-ALG-IM-10); unit 4's model report and unit 5's end-of-unit records are carried unscored. Day 64, the year's last lesson and the respond day for unit 6 and the check, returns the scored work by error letter and records each student's gains for grade 12 |

## Cross-subject

No grade 11 row has a cross_subject lean in data/progressions/computer-science.csv, so no unit waits on another
course's unit and no availability calendar is owed.

### Mathematics, grades 6 to 8 (long taught)

The number work used here is taught well before grade 11, so no bridge is needed (lesson 13): accuracy as the
fraction or percent of test cases right (unit 4) uses grades 6 and 7 ratio and percent work; reading scatter plots and
association between two variables (unit 3) uses grade 8 statistics. The units state each as a retrieval line inside
the lesson, not a lean.

### Social studies and English language arts, grade 11

Unit 6's policy proposal and unit 5's written evaluations practice argument writing with sources and reading a
policy's reasons; they are practiced, not owned, and lean on no grade 11 social studies or English language arts unit.
Grade 12's own computer science rows lean on grade 12 English language arts (e12-informative, e12-seminar).

## For the lead

1. **Check weeks (calendar pass).** Mid-year day 35 in week 18, off every grade 11 core check week; year-end day 63
   in the finals week 32, which grade 11 shares with English language arts, Algebra II, physics, US history I and the
   after-core courses that use it (CALENDAR.md rule 4 allows it). Any after-core overlap `frame.py calendar` shows is
   for the lead's one pass across the after-core frames; this frame did not move weeks for it.
2. **Seams with grades 10 and 12.** The grade 10 frame's "Handed on to Grade 11" table and this frame's "Picked up"
   table name the same rows at both ends, and each grade 10 unit cited here is its calendar place. Its note at
   docs/courses/computer-science-grade-10/frame.md line 190 now fails stale.py, since this frame has landed; replacement
   text for its writer or the lead: "Each pick-up row's grade 11 unit is named in
   docs/courses/computer-science-grade-11/frame.md, Seams." The grade 12 frame does not exist; "Handed on to Grade 12"
   is taken from the progression's assumes and hands_on, which match at both ends, and the lead's seam read checks it
   against that frame.
3. **Row changes** (listed in the final report) bring four owner rows' notes to their boundary statements, read in
   the source store for this frame: g11-fix-security-flaw (the paper path meets the id in full; the fix is high-level,
   not implemented), g11-algorithm-ethics (recommend a refinement), g11-multivariate-viz (a tool, no text code), and
   g11-evaluate-generated-code (test each sample with edge cases).
4. **Tool asks for TOOL-ASKS.md** (the scope writer's step): a toy-system security page (settings panel and log), a
   test runner inside our own Python editor (planned cases with "yes" or "not yet"), a no-code chart tool (scatter,
   line, stacked bar, heat map), a crosswalk simulation page, and a small model-training page (split, train, test,
   results by group). Pick: all five go on the editor's build list as one-file pages with no account; every unit runs
   on paper meanwhile, with HS-ALG-ML-08 and HS-DAT-DI-25 part met without a device.
5. **Sources for docs/APPROACH-SOURCES.md:** NIST SP 1270 (2022); the EEOC's 2023 technical assistance on software
   and algorithms in employment selection; the GIDA CARE Principles; the US Indigenous Data Sovereignty Network; the
   UN Global E-waste Monitor 2024; the Lawrence Berkeley National Laboratory United States Data Center Energy Usage
   Report (December 2024); NOAA Climate Data Online; the EPA electronics recycling pages. Each is opened and dated by
   the unit writer; the Washington recycling law and the data center case are from memory, to be checked before use.
6. **A download for unit 3.** The weather station extract is a NOAA Climate Data Online download (free, public, no
   account for small daily-summary requests as far as known); it is a download, so it waits on Cory's yes. Fallback:
   an extract invented for practice, marked so.
