# Course frame: Computer Science, Grade 10

Course `computer-science-grade-10` (catalogue id `cs-k12`), grade 10, one year. Draft frame, 2026-11-25; the scope and sequence sets the days later.

## The course in brief

- **Units.** 6, in the order the ideas build: reading code closely (programming: a call with parameters, return
  values and a list, then libraries and their documentation), which algorithm is better (algorithms: comparing two
  algorithms by step counts, tests and clarity, then justifying an AI type for a task), networks and breaches (systems
  and security), clean data, checked data (data and analysis), design for every user (the year's team design project,
  with the portfolio session), and who decides (computing and society, the year's closer). Every concept area is
  taught in the year, and AI sits inside the algorithms unit, not in a unit of its own (lens).
- **Days.** 64 course days: 58 in units, 4 for course-level checks (2 at mid-year, 2 at year-end) and 2 respond days
  (one after each check). Two lessons a week of about 45 minutes, 32 weeks: the computer science default for grades 6
  to 12 (docs/courses/computer-science/STANDARD.md section 2, Cory, Desk q-fix-cs-1), so course days 2w-1 and 2w fall
  in week w. The 45 minutes hold set-up, clean-up and collecting work: a lesson opens with a retrieval trace or a
  predict task of three to ten minutes (APPROACH.md, "How a day opens"), and device lessons keep three minutes at the
  end to save or print work and close devices, so a lesson teaches for about 35 minutes. Each unit's days include its
  end-of-unit assessment (no unit runs over 25 days, so there are no mid-unit assessments), with one shape for a unit
  a course-level check follows directly: units 3 and 6 are assessed by the check that follows them, and the check's
  respond day is the unit's respond day (the pattern of the kindergarten pilot,
  docs/reviews/frame-computer-science-kindergarten-fixes-2026-11-25.md), so no week holds an end-of-unit assessment
  and a respond day just before a check. Days follow the load of the rows: unit 1 owns two device-only programming
  rows (HS-PRO-RD-17 and HS-PRO-PD-13, the second met in full only on a device) and gets 12; unit 5 is a team product
  with a draft day, a written feedback day and a revision day before its score, and gets 11; units 3 and 6 each own
  three unplugged rows assessed in the check that follows, and get 8 teaching days each. 64 days for 15 rows (12
  that own an id, 3 that contribute) is about four lessons a row, counted with checks. Each check
  takes two lessons, since a 45-minute lesson holds one full performance (lesson 19): the first scores the unit just
  ended, the second samples the earlier units.
- **Check weeks.** The grade 10 core checks take weeks 8 to 11, 18 to 21 and 32 (English language arts 9, 18, 32;
  geometry 10, 21, 32; chemistry 11, 20 to 21, 32; world history II 8 to 9, 18 to 19, 32; docs/courses/CALENDAR.md).
  This course's mid-year check sits on course days 30 and 31 (weeks 15 and 16), with its respond day 32 in week 16;
  its year-end check sits on days 62 and 63 (weeks 31 and 32, week 32 the finals week, CALENDAR.md stagger rule 4),
  with its respond day 64 in week 32. Overlaps with other after-core subjects' check weeks are the lead's calendar
  pass across the after-core frames (For the lead 1).
- **Standard.** The 12 HS Foundational ids the progression gives grade 10 (STANDARD.md "Ownership of MS and HS ids"):
  HS-ALG-PS-03, HS-ALG-ML-06, HS-ALG-IM-09, HS-DAT-DC-23, HS-DAT-DC-24, HS-PRO-RD-17, HS-PRO-PD-13, HS-SOC-ET-41,
  HS-SOC-HU-43, HS-SYS-NT-34, HS-SYS-NT-35, HS-SYS-SE-32, every concept in the year (ALG 3, DAT 2, PRO 2, SOC 2,
  SYS 3). Five ids owned in other grades are used here as contributing (`~`), by two owning rows and three
  contributing rows, and named in "What students learn" with their owner: HS-PRO-RD-18 (grade 11), HS-PRO-PD-14 (grade 12), HS-SOC-HI-39 (grade 11), HS-DAT-DI-25
  (grade 11) and HS-SOC-CE-46 (grade 12). Each owned id is taught at the depth its owner row's notes set in our own
  words, read again against its boundary statement in the source store (S:\CurioClass-sources\computer-science\
  csta-2026-11-21, read 2026-11-25, never copied or quoted; STANDARD.md "Depth"), and "What students learn" says what
  is out. Plans cite ids and state each action in a short phrase of our own (STANDARD.md "Quoting"); the credit line
  "Standards: 2026 CSTA PK-12 Computer Science Standards (CC BY-NC-SA 4.0)" goes on any day that leans on a
  statement. Check set: each unit plan checks itself against the computer science bar (docs/ADOPTION-BAR-SUBJECTS.md
  part 5, items 1 to 9) and the lens (docs/agents/lenses/computer-science.md); the "Check set adds" column names
  what the writer expects that to add. Values rule (DESK-ANSWERS 2026-11-12) holds. No Specialty id is claimed
  (the eight S1 ids belong to grades 11 and 12, STANDARD.md section 2), and no X + CS id.
- **Practices and concept areas.** The Units table's fifth column (the C3 column of the core frames) names, for
  computer science, the concept area each unit teaches and the CSTA practices it teaches inside the content, by code
  and our label (STANDARD.md section 3), as bar items 1 and 2 ask. Each unit plan names the practice's day and task.
  Across the year: CT6 define the problem (units 1, 3, 4), CT7 abstract and model (units 1, 2, 3, 4), CT8 build and
  plan (units 3, 5), CT9 test, debug and refine (units 1, 2, 4), IC3 explain and give feedback (units 2, 5, 6), IC4
  run a project (unit 5), IC5 be a reliable teammate (units 1, 2, 5, pair roles that switch at the halfway signal),
  HCD10 include different users (units 5, 6), HCD11 prototype and test for use and access (units 4, 5), HCD12 keep
  users informed and in control (unit 6), ESR1 weigh who gains and who is harmed (unit 6), ESR2 credit others and
  protect users' data (units 1, 3). Dispositions are named in the unit plans, not here.
- **Base text.** None. The partial base (the archived Teach Computing Curriculum) covers grades K to 8 only
  (STANDARD.md section 2), so this course has no Source map. Curio Class writes every worked program, trace table,
  data set, documentation page and case card itself, in Python for the code (STANDARD.md "Our own editor"). Real
  cases follow STANDARD.md "Real cases in society days": told by what happened, with no company or product named,
  two views and a dated source each, government bodies and courts named where needed; each unit's picks and sources
  are in its row. Invented data and invented cases say "invented for practice" on the teacher page.
- **Day kinds.** As docs/GLOSSARY.md (row "teaching day") defines them, in computer science's words (APPROACH.md):
  Understanding is an unplugged or trace lesson, the first teaching of a construct or idea (a procedure call traced
  on a trace table, two searches stepped through on cards, a network drawn from a description). Fluency is a modify
  lesson: change a working program, algorithm or cleaning step in small, checked steps (unit 1 lesson 5, unit 2
  lessons 4 and 5, unit 4 lesson 4); the course has little of it beyond those and the retrieval openings, and no
  speed target. Application is a make, design or society lesson: add a feature with a library, run the team design
  project, or write an evaluation of a case with evidence. Check is the end-of-unit assessment or a course-level
  check; Respond acts on it by error letter. Inside a unit: understanding before modify before make, and no make
  lesson before a trace or modify lesson on the same construct.
- **Evidence.** Grade 10 writes: trace and predict lessons end in an exit ticket with a short program and "what
  happens?", wrong answers by error letter; modify and make lessons are checked against two or three stated look-fors
  plus the student's line "what I tested and what I changed"; society lessons end in a short claim with two views
  and a dated source (APPROACH.md, "The form of daily evidence"). Every end-of-unit assessment is either a sitting
  with unseen items, never the unit's own anchor (units 1, 2 and 4, and the two checks), or a product whose draft,
  written feedback and revision days come before its score (unit 5). Each owned id has its own look-for, and a
  "design", "diagram", "justify" or "evaluate" id is met by the student's own product or written reasoning, never by
  recognizing a supplied answer. No score comes from a lesson that first teaches a row.
- **Devices.** One device per pair is the default on a device day, never needed per student; students switch driver
  and navigator at the halfway signal. Device days: unit 1 lessons 3, 5, 6, 8, 9 and 10 (the editor's step-through
  trace and the library), unit 2 lesson 3 (both searches run with a step counter), unit 4 lessons 2 to 4 and 7 (the
  cleaning functions and the chart tool), unit 5 lessons 5 and 6 (the prototype and its access tests). Units 3 and 6
  are unplugged. That leaves about half the year's time away from a device, and every unit has at least one unplugged
  lesson (bar item 5; APPROACH.md, Pacing). Every device day is written four ways (STANDARD.md "Devices and rooms"):
  one device per pair, a few devices at stations with the other pairs on the paper version of the same idea, one
  screen with the class predicting and voting before each run, or no device. Two owned ids need a device to be met in
  full (STANDARD.md lists them): HS-DAT-DC-23 (a computational tool cleans the data) and HS-PRO-PD-13 (documentation,
  a library and the editor's debugger used in development). On the no-device path those days teach the idea in full
  (a printed short list cleaned by hand with the same named steps; a printed documentation page used to write the
  call, checked by a partner as "be the computer"), and the course record marks those ids "part met without a
  device", never met. The rest of the year's ids are met in full on paper.
- **Paper path.** Every lesson has one: trace tables, printed programs and documentation pages, card sorts, paper
  network diagrams, hand-plotted charts on printed squares with colored pencils, and paper prototypes. No tool asks
  for a student account, stores a student's name or sends anything off the device (STANDARD.md "Privacy and
  safety").
- **Reading level and vocabulary.** Code read at most twenty lines at a time (APPROACH.md, Supports); error messages
  in plain words we write; each unit names five to eight words taught in depth with a traced example, and the
  everyday words with a computing meaning are taught as two meanings (return, library, call, clean, client,
  breach). Sentence frames: "First the program ___, then it ___", "I predict ___ because line ___ says ___", and for
  society lessons "One view says ___ (source, date); another says ___ (source, date)". A student may answer a trace
  in numbers, arrows or the home language.
- **Swap or leave out.** STANDARD.md section 3 lets a school swap or leave out a named unit for its community's
  reasons. Units 3 and 6 may swap their cases (another breach told by what happened; another emerging technology or
  another case of human choices with a government or court record) and keep their ids. No unit is left out: units 1
  and 2 carry the programming and algorithm ids grade 11 builds on, unit 4 is the year's data and unit 6 its society
  (the bar part 5 fails a course with nothing on data or society), unit 3 holds every systems id, and unit 5 is the
  only owner of HS-ALG-IM-09.
- **Safety.** No lab or field work, so no laboratory or field safety guide applies. Device cords stay behind the
  table; devices are carried with two hands. Security lessons use case cards and toy systems built into the page:
  no scanning, no attack steps and no test of a real school or home system, ever (STANDARD.md "Privacy and safety").
  The scope and sequence copies these lines into each device and security day.
- **Costs.** Provisional, for a class of 30, beyond the school's own devices: printing only. Unit 1 $3 (trace tables,
  the printed programs and documentation page), unit 2 $3 (search cards, test-table sheets, AI task cards), unit 3 $4
  (network description cards, packet strips, breach case cards), unit 4 $3 (messy lists, dictionaries, printed
  squares for hand plotting; colored pencils the class has), unit 5 $5 (persona cards, sketch sheets, paper prototype
  sheets, chart paper for the design wall), unit 6 $3 (case cards, the class timeline strip, benefit-risk charts),
  about $21 in all.
- **Sensitivity reads.** Every unit gets the fresh sensitivity agent's read (docs/pipeline/briefs/sensitivity-read.md);
  no outside reader is planned (Cory, 2026-11-14). Unit 5 has disability content (accessible design, user stand-ins
  with differing abilities, the accessibility laws). Before it reads, the agent studies a starting pack: the
  Autistic Self Advocacy Network's "Identity-First Language" page
  (autisticadvocacy.org/about-asan/identity-first-language/), one community's own account, not taken as every
  community's; the Disability Rights Education and Defense Fund's site (dredf.org), a disability-led group; the
  National Center on Disability and Journalism's Disability Language Style Guide (ncdj.org/style-guide/); and, as
  background on the law only, Section508.gov and ada.gov. It checks no classmate plays a disability as a costume:
  user stand-ins are written persona cards a student reads from, never acted. Unit 6's human-choices case touches
  families who lost benefits and work (APPROACH.md, Sensitive ground, "Work and automation"): the agent studies the
  court record named in the unit and one account by the claimants' own advocates, which it finds and records. Unit
  3's breach and scam cases and unit 6's case carry health's "If a student tells you something" steps word for word
  on their teacher pages (docs/courses/health/APPROACH.md). Unit 4's data is invented, never about students. The
  course's checks get the answer-key agent's read. No unit is hands-on in the laboratory sense, so no safety agent
  read is planned beyond the Safety lines above, which the sensitivity read confirms are on each day.

## Seams

### Picked up from Grade 9 computer science

The rows are from data/progressions/computer-science.csv; each grade 9 row's unit and course days are those of
docs/courses/computer-science-grade-9/frame.md and data/plans/calendar.csv, and grade 8's those of
docs/courses/computer-science-grade-8/frame.md.

| Row picked up (grade 9, or earlier) | What it handed on | Unit here | How it opens here |
|---|---|---|---|
| g9-modular (HS-PRO-PD-12), grade 9 unit 2 (days 14 to 25) | A program split into procedures, a library function and a small object | 1 | Retrieval trace on lesson 1 (grade 9 is the year before): what does this procedure hide? |
| g9-structures-program (HS-PRO-VD-16), grade 9 unit 1 (days 1 to 13) | Lists and key-value records traced with a list-diagram | 1 | Retrieval inside lesson 3, before a list is passed to a procedure |
| g8-evaluate-ai-code (MS-PRO-RD-18), grade 8 unit 4 (days 43 to 54) | Saved code samples judged for accuracy against tests | 1 | Readiness check, last ten minutes of lesson 1 after the hook: last used in computer science grade 8, two grades back, and grade 9 has no row that reads generated code |
| g8-attribution (MS-PRO-PD-14), grade 8 unit 2 (days 14 to 28) | A credit line for others' code | 1 | The same readiness check (grade 8, two grades back); its results shape lesson 9's credit comment |
| g9-design-with-structures (HS-ALG-PS-01), grade 9 unit 1; g9-optimize-procedures (HS-ALG-PS-02), grade 9 unit 2 | Pseudocode and flowcharts for a problem solved two ways; a long program rewritten with procedures and checked by the same tests | 2 | Retrieval trace on lesson 1 of unit 2: which of two given pseudocode versions is the procedure version? |
| g9-ai-tour (~HS-ALG-ML-06), grade 9 unit 3 (days 26 to 32) | AI algorithm types met by name and first matches to task cards | 2 | Retrieval inside lesson 6, before students justify a choice |
| g9-network-sketch (~HS-SYS-NT-34), grade 9 unit 5 (days 44 to 55) | A given school network diagram read and one request traced; nothing drawn | 3 | Retrieval inside lesson 1; drawing from a description is first taught here (lesson 3) |
| g9-security-measures (HS-SYS-SE-31), grade 9 unit 5 | Security measures compared by their cost to users, on toy systems | 3 | Retrieval inside lesson 6, before breaches are classified by cause |
| g9-data-dictionary (HS-DAT-DC-22), grade 9 unit 4 (days 35 to 43) | A data dictionary: each field's type and allowed values, a rule between fields | 4 | Retrieval inside lesson 1; the dictionary is what lessons 5 and 6 verify against |
| g9-simulate-data (HS-DAT-DC-21), grade 9 unit 4 | A simulated data set checked for a stated range; its chart | 4 | Retrieval inside lesson 5 (range checks) and lesson 7 (the chart) |
| g9-algorithm-impacts (~HS-ALG-IM-10), grade 9 unit 3 | A rule-based algorithm audited for where it could discriminate, on a benefit-risk-chart | 5 | Retrieval inside lesson 1, before user research |
| g9-career-interests (~HS-SOC-CE-46), grade 9 unit 6 (days 56 to 62) | A private goal, the skills it needs and one next step | 5 | Retrieval inside lesson 11, the portfolio lesson |
| g9-emerging-differences (HS-SOC-ET-40; ~HS-SOC-HU-43), grade 9 unit 6 | An emerging technology set against the one it may replace, by technical differences | 6 | Retrieval inside lesson 1, before effects on society and the environment |
| g9-computing-history (HS-SOC-HI-38), grade 9 unit 6 | One technology followed on a timeline with the factors that pushed or slowed it | 6 | Retrieval inside lesson 4, where a policy is placed on the same kind of timeline |

Two more threads from grade 9 come back here as review, as its frame hands them on: the operating system layer of
grade 9's system-diagram (g9-operating-systems, unit 5) is drawn on each device in unit 3's network diagrams, and the
probabilistic algorithms of g9-det-vs-prob (unit 3) return where unit 1's game library rolls dice. The packet-strip
model of unit 3 lesson 4 was last used in grade 8 (g8-network-failure, grade 8 unit 1, days 1 to 13) and is not used
in grade 9:
it gets a readiness item in the last ten minutes of unit 2's respond day (course day 21), and the row link is a Row
change (For the lead 3).

### Handed on to Grade 11 computer science

| This course hands on | Unit here | Row that picks it up | What it does with it |
|---|---|---|---|
| g10-evaluate-algorithms: two algorithms compared by step counts on growing inputs, test cases and clarity | 2 | g11-build-ml-model | The test-case habit used on a model: one claim about the model tested against the test-table and a metric |
| g10-choose-ai-type: an AI type justified for a task by its data, interpretability and cost of an error | 2 | g11-training-data-review; g11-build-ml-model | The training set for the chosen task reviewed, then a small model built and tested |
| g10-design-hcd: a technology designed with the human-centered steps, accessibility laws named as a constraint | 5 | g11-algorithm-ethics | Who a design helps and harms becomes a full ethical audit of a rule-based and a data-driven algorithm |
| g10-clean-text: text data cleaned and organized with a tool | 4 | g11-build-ml-model; g11-multivariate-viz | Clean data trains a model and feeds a several-variable chart |
| g10-verify-consistency: approaches to checking data against a dictionary judged | 4 | g11-training-data-review | A training set checked for source, quality and who is missing |
| g10-analyze-code: a procedure with a parameter, a return value and a list explained and traced; one saved sample read | 1 | g11-evaluate-vs-spec; g11-evaluate-generated-code | A program checked against a written specification; saved generated samples judged and their flaws named (HS-PRO-RD-18 owned there) |
| g10-apis-docs: a library used from its documentation, credited in a comment | 1 | g11-evaluate-generated-code | Each generated sample gets an ownership note, the next look at HS-PRO-PD-14 |
| g10-emerging-impacts: an emerging technology's effects on society, environment and access evaluated | 6 | g11-emerging-solution | A conceptual solution to a local problem with an emerging technology, its benefits and harms argued |
| g10-human-choices: risks, benefits and long-term effects at the use, design, deploy and regulate points of one case | 6 | g11-emerging-solution | The human choices in that solution named and weighed |
| g10-history-policy: a past policy's effect on a technology, at a first look | 6 | g11-policy-change | A change to an existing policy proposed and defended (HS-SOC-HI-39 owned there) |
| g10-network-diagram: a small office network diagrammed with hardware and software, a request traced | 3 | g11-infrastructure-impact | The diagram widened to infrastructure (cables, data centers, power) and who it serves |
| g10-breach-causes: breaches and social engineering classified by cause and by impact on four kinds of group | 3 | g11-fix-security-flaw | A flaw found and fixed in a toy system, rated on the cia-triangle |
| g10-visual-data: a three-variable chart read and made | 4 | g11-multivariate-viz; g11-evaluate-simulation | A several-variable visualization built to answer a question (HS-DAT-DI-25 owned there); a simulation judged |
| g10-career-skills: skills from the year's work matched to jobs, one to build next | 5 | g11-career-plan | A team role plan: each role's skill and what a different perspective changes |

g10-network-of-networks (HS-SYS-NT-35) ends its thread here: no grade 11 row takes it on (the progression read
names this as fine, docs/reviews/progression-computer-science-2026-11-19.md). Each pick-up row's grade 11 unit is named in
docs/courses/computer-science-grade-11/frame.md, Seams. Every hand-on above is answered by that
row's assumes in data/progressions/computer-science.csv, and each grade 11 row opens as a retrieval task inside its
first day, since grade 10 is the year before (lesson 16).

## Models carried

| Model | Where it comes from | Introduced or first used here | Used again here |
|---|---|---|---|
| text-program | Grade 6 (g6-variable-types); grade 9 g9-modular | Unit 1 lesson 1: a working twenty-line guessing-game program | Unit 1 throughout; unit 2 (both searches in Python); unit 4 (the cleaning steps); unit 5 (an optional prototype screen); both checks |
| trace-table | Grade 3 (g3-variable-trace); grade 9 g9-structures-program | Unit 1 lesson 2: a procedure call traced, parameter and return value in their own columns | Unit 2 (both searches traced on growing lists); both checks |
| list-diagram | Grade 7 (g7-lists); grade 9 g9-structures-program, g9-modular | Unit 1 lesson 3: a list passed into a procedure, drawn before and after the call | Unit 2 (the halving search drawn on a sorted list) |
| pseudocode | Grade 6 (g6-model-algorithm); grade 9 g9-design-with-structures | Unit 2 lesson 1: the two searches as pseudocode before code | Unit 2 lessons 2 to 5 |
| test-table | Grade 4 (g4-debug-increment); last used grade 8 (g8-evaluate-ai-code) | Unit 1 lesson 6: tests run on a saved code sample (after the day 1 readiness check) | Unit 2 lesson 4 (test cases for correctness); unit 5 lesson 6 (access tests) |
| training-set | Grade 2 (g2-ai-training-data); grade 9 g9-ai-tour | Unit 2 lesson 6: the data each task card has, as a short training-set description | Unit 2 lesson 7; on to grade 11 |
| network-diagram | Grade 3 (g3-reach-internet); grade 9 g9-network-sketch | Unit 3 lesson 2: a small office network, hardware and software on each device | Unit 3 lessons 3 to 5 (drawn from a description, several networks joined); the mid-year check |
| packet-strip | Grade 6 (g6-packets); last used grade 8 (g8-network-failure) | Unit 3 lesson 4: a packet strip traced between two joined networks (readiness item on course day 21) | Unit 3 lesson 5 (the layers a message passes through); the thread ends here |
| cia-triangle | Grade 5 (g5-cia-triad); grade 9 g9-security-measures | Unit 3 lesson 6: each breach card placed by what it broke | Unit 3 lessons 7 and 8; on to grade 11 |
| data-table | Grade 2 (g2-data-types); grade 9 g9-data-dictionary | Unit 4 lesson 1: a messy invented sign-up table beside its dictionary | Unit 4 throughout |
| data-visualization | Grade 4 (g4-data-explain); grade 9 g9-simulate-data | Unit 4 lesson 7: a three-variable chart (x, y and color) | Unit 4 lesson 8; the year-end check |
| benefit-risk-chart | Grade 2 (g2-benefits-harms); grade 9 g9-algorithm-impacts, g9-emerging-differences | Unit 5 lesson 4: the design options' benefits and risks for different users | Unit 6 lessons 1 to 3 (the emerging technology) and 5 to 7 (the four-column chart at the four decision points); the year-end check |
| timeline | Kindergarten (k-then-now); grade 9 g9-computing-history | Unit 6 lesson 4: a policy placed on the class timeline with its effect | On to grade 11 (g11-policy-change) |

## Units

| # | Unit and compelling question | Days | Skills | Owned standards | Practices and concept areas | What students learn | Why this unit, here | Check set adds | Sensitive topics and teacher notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Reading code closely. *How does each part of a program do its job, and how do we use code other people wrote?* Anchor: a working twenty-line guessing game, run once, then read line by line | 12 | g10-analyze-code; g10-apis-docs | HS-PRO-RD-17; HS-PRO-PD-13 | Concept area: programming. Practices: CT6 (say what each part is for); CT7 (see a procedure as a reusable part); CT9 (use the debugger to test and refine); ESR2 (credit the library and its documentation); IC5 (driver and navigator switch at the halfway signal) | Lesson 1: the anchor run once; hook question; retrieval trace of g9-modular; readiness check (last ten minutes) on reading a saved code sample against tests (g8-evaluate-ai-code) and writing a credit line (g8-attribution). Lesson 2 (unplugged): a procedure call traced on a trace-table, the parameter and the return value each in a column; the computer does exactly what is written, in order. Lesson 3 (device): a list passed into a procedure, the list-diagram drawn before and after, stepped through in the editor. Lesson 4: the whole anchor explained part by part, earlier years' parts (sequence, loop, condition, variable, procedure) and this year's (parameter, return value, list) and how they work together: the variable holds the secret number, the while loop runs until the guess is right, the if and else give the feedback. Lesson 5 (modify): change one argument or one return line and predict, run, compare. Lesson 6 (device): one saved code sample read, traced and run against a test-table, a first look at HS-PRO-RD-18 (owned in grade 11, g11-evaluate-generated-code); no live tool. Lesson 7 (unplugged): reading a documentation page: what a function takes, what it returns, its example; a library's interface (its API: the functions it offers and how each is called) as the promise the documentation makes. Lesson 8 (device): a feature added to a program with a supplied offline game library (its dice roll is a probabilistic step, reviewed from grade 9) from its documentation (paper path: the call written from the printed page, part met without a device). Lesson 9 (device): the editor's step-through debugger and its highlighting used as development tools to find a bug; the library and its page credited in a comment above the call, a first look at HS-PRO-PD-14 (owned in grade 12, g12-attribution). Lesson 10 (make): each pair adds a second feature using the library, tests it and writes what they tested and what they changed. Out: no program with many connected data structures, no complex algorithm analysis, no writing a library or an API, no live generated-code tool. End-of-unit (lesson 11): a sitting with unseen items: explain the parts of a new fifteen-line program and trace one call with a list (HS-PRO-RD-17), and from a new printed documentation page write and run one library call in a given program, with its credit comment (HS-PRO-PD-13; paper version marked part met without a device); respond lesson 12. Tools: our own editor (Python text view and step-through trace, job: run, trace and debug the programs); a small offline game library (dice rolls, shuffled decks, a score board) with its one-page documentation (job: the library students read and use). Curio Class writes: the anchor program and its tested solution key, the trace-table and list-diagram sheets, the saved code sample with its test-table, the library and its documentation page, the readiness check items | First because every later code reading in the year (unit 2's searches, unit 4's cleaning steps) asks students to explain a call with parameters and a return value, and it builds directly on grade 9's procedures and lists (g9-modular, g9-structures-program) while they are fresh. Reading comes before using a library, since the documentation describes a call in the same terms. The readiness check sits here because the two grade 8 rows it covers return in this unit | Candidate: kept, a one-page "if you are stuck" sheet for the teacher on the three commonest bugs of the anchor, zero added days | Pair work: roles named and switched, no student at the keyboard all lesson. The guessing game uses numbers only, no names. Agent reads: sensitivity. |
| 2 | Which algorithm is better? *When two algorithms solve the same task, how do we decide which is better, and which kind of AI suits a task?* Anchor: finding one name in a sorted list of a thousand made-up names, once by checking every name and once by halving the list | 9 | g10-evaluate-algorithms; g10-choose-ai-type | HS-ALG-PS-03; HS-ALG-ML-06 | Concept area: algorithms and design (with AI inside it). Practices: CT9 (test cases for correctness); CT7 (see what grows with the input); IC3 (justify a choice to a partner); IC5 (pair roles) | Lesson 1: the anchor as two pseudocode versions; retrieval trace of g9's pseudocode. Lesson 2 (unplugged): both searches stepped through on number cards, steps counted for lists of 8, 16 and 32. Lesson 3 (device): both run in the editor with a step counter on lists of 10, 100, 1,000 and 10,000 and the counts put in a table; the halving search's count grows far more slowly. Lesson 4 (modify): correctness by test cases (the first item, the last, a missing item, an empty list): a halving search with a bug is fixed and retested. Lesson 5 (modify): clarity: two correct versions compared for how easily a reader follows them, and one rewritten with clearer names; memory use named as a second cost. Lesson 6 (unplugged): retrieval of g9-ai-tour; for task cards (sort messages, group shoppers by habit, predict a bus's arrival, caption a photo), the data each task has and what an error costs. Lesson 7 (application): students justify an AI type for a new task in two sentences, naming its strengths and limits for the task: the data's size and type, whether a person can follow how it decides, the outcome wanted; a choice that suits a different task is the wrong example. Out: no Big O notation, no proofs, no analysis of all inputs, no logarithms (the halving is counted, never written as a formula), and no mathematics or building of the AI types (built in grade 11). End-of-unit (lesson 8): a sitting with unseen items: for a new pair of algorithms (two ways to find the largest number in a list), count steps on given sizes, find the test case one version fails and say which is clearer and why (HS-ALG-PS-03); justify an AI type for a new task card in two sentences (HS-ALG-ML-06); respond lesson 9, whose last ten minutes hold the packet-strip readiness item for unit 3. Tools: our own editor with a step counter (job: run both searches on growing lists and count). Curio Class writes: the two searches and their tested keys, the number cards, the buggy halving search, the AI task cards with their keys | After unit 1 because comparing the searches needs a call with a list read and traced. Before units 4 and 6 because the test-case habit and the AI types return there (the cleaning steps are tested; the human-choices case is partly a data-driven system). Comparing algorithms and choosing an AI type sit together as one question: which way of solving suits the task | Candidate: kept, a step-count table template so pairs record counts the same way, zero added days | Made-up names only. Number work stays inside earlier math: counting and comparing counts as a list doubles, no logarithm. Agent reads: sensitivity. |
| 3 | Networks and breaches. *How does a message cross the internet, and what happens to people when a system is broken into?* Anchor: what happens, step by step, when a student in a small office loads one page from a server across town | 8 | g10-network-diagram; g10-network-of-networks; g10-breach-causes | HS-SYS-NT-34; HS-SYS-NT-35; HS-SYS-SE-32 | Concept area: systems and security. Practices: CT7 (a network as a model of parts and roles); CT8 (plan a diagram before drawing it); CT6 (classify a breach by cause); ESR2 (whose data is exposed) | Lesson 1: the anchor; retrieval of g9-network-sketch (read a given diagram). Lesson 2 (unplugged): a small office network diagrammed with its hardware (devices, a router, a server, storage) and its software (the operating system layer of grade 9's system-diagram and the programs on each), and one request traced through it, each part's role named. Lesson 3 (application): a network drawn from a written description, then checked by a partner who traces a request through it. Lesson 4: several small networks joined on the map; a packet strip traced between two of them through routers; addresses. Lesson 5: the internet as a network of networks: nobody runs the whole, many networks agree on shared rules (TCP/IP named), clients and servers, and the layers a message passes through at a high level; a school network and the internet compared on structure, size, addressing and how data moves. Lesson 6 (unplugged): retrieval of g9-security-measures; breach and scam case cards sorted by cause (a weak password, a trick that fooled a person, an unpatched system), each placed on the cia-triangle. Lesson 7: one breach, many groups: an invented hospital breach (invented for practice) classified by its impact on individuals (patients), an industry (the hospital), a community (the local health system) and a government (the rules that apply), and by kind (money, trust, legal, the work that stops). Lesson 8: a second case classified from supplied government pages (see the last column's sources), then review. Out: no building or configuring a network, no packet analysis, no protocol writing, no attack steps or forensic detail, no professional security tools. End-of-unit: the mid-year course-level check (lessons 30 and 31 of the course) stands for it. Tools: none (paper diagrams; a toy network page shown on one screen at most). Curio Class writes: the office network description cards, the packet strips, the breach and scam case cards with their keys, the invented hospital case | After units 1 and 2 because the client and server roles are read as programs talking (unit 1's calls), and before the mid-year check so the check scores a whole unit. Diagram before network of networks (one network, then many), and networks before breaches (a breach needs the parts it broke into). Placed in weeks 11 to 15, after the core check weeks 8 to 11 except its first lesson | Candidate: kept, a one-page diagram key of symbols (device, router, server, link) so every diagram reads the same, zero added days | Scams can touch a student's family: no student is asked whether anyone they know was scammed; a student's own offer is welcome and the teacher page carries health's "If a student tells you something" steps word for word. Cases are told by what happened, no company named. Sources for the teacher line: the U.S. Department of Health and Human Services Office for Civil Rights breach report page (ocrportal.hhs.gov/ocr/breach), counts by breach type as of the day the unit is written; the Cybersecurity and Infrastructure Security Agency's "Avoiding Social Engineering and Phishing Attacks" page (cisa.gov); the Federal Trade Commission's phishing page (consumer.ftc.gov). No attack is run. Agent reads: sensitivity. |
| 4 | Clean data, checked data. *How do we make messy data ready to use, and how do we know it follows the rules?* Anchor: an invented community garden's volunteer sign-up list where the same person appears three ways and one birthdate is in the year 2099 | 10 | g10-clean-text; g10-verify-consistency; g10-visual-data | HS-DAT-DC-23; HS-DAT-DC-24 | Concept area: data and analysis. Practices: CT9 (clean, check and clean again); HCD11 (data ready for the people who use it); CT6 (state the rule data must follow); CT7 (find the pattern in an error) | Lesson 1: the anchor beside its data dictionary; retrieval of g9-data-dictionary. Lesson 2 (device): inconsistencies handled with a tool (supplied cleaning functions in the editor and a table view): capital letters and spaces made the same (trim, change case). Lesson 3 (device): errors corrected: misspellings found by sorting, invalid entries flagged, duplicates removed. Lesson 4 (modify, device): structure: one combined name column split into two, dates put into one format, by changing a supplied cleaning step; students say where a pattern rule (a regular expression) could find every case at once, without writing one. Lesson 5 (unplugged): three ways to verify data against the dictionary (check each entry as it is typed, check the whole table after, check against a second source) judged on cost and the errors each catches; expected types, values and ranges (a birthdate in a sensible range, a grade from 9 to 12). Lesson 6 (application): the three ways applied to a new invented table; students write which they would use and why. Lesson 7 (device): the cleaned table plotted with three variables in one chart (x, y and color) in a chart tool (paper path: hand-plotted on printed squares with colored pencils). Lesson 8: what the pattern is and what the chart cannot show, a first look at HS-DAT-DI-25 (owned in grade 11, g11-multivariate-viz). Out: no cleaning tool built from scratch, no large unstructured data, no regular expression written, no validation script written, no statistics beyond reading a visible trend. End-of-unit (lesson 9): a sitting with unseen items: clean a new short messy list with the named functions and say each step (HS-DAT-DC-23; paper version marked part met without a device); judge two verification approaches for a new invented table on the errors each would miss (HS-DAT-DC-24); respond lesson 10. Tools: our own editor with supplied cleaning functions and a table view (job: clean and organize the text data); a browser chart tool (job: plot three variables, color with a shape or label too). Curio Class writes: the invented volunteer lists and their dictionaries, the cleaning functions, the verification task cards, the chart data | After the mid-year check, with unit 2's test-case habit in place (cleaning steps are tested). Clean before verify (the dictionary checks a table that is already tidy), and verify before charting (a chart of unchecked data misleads). Before unit 5, whose user research is recorded in a small table | Candidate: kept, an error-letter key for the five commonest cleaning mistakes (a trim missed, a duplicate kept, a split on the wrong mark), zero added days | All data is invented for practice and about made-up people; no student's name, birthdate or detail enters any table (STANDARD.md "Privacy and safety"). Agent reads: sensitivity. |
| 5 | Design for every user. *How do we design a technology that works for the people who will really use it?* Anchor: a school sign-up kiosk screen that a user with a screen reader, a user who cannot use a mouse and a user reading in a second language each try and cannot finish | 11 | g10-design-hcd; g10-career-skills | HS-ALG-IM-09 | Concept area: algorithms and design (impacts of design), with computing and society (careers). Practices: HCD10 (learn from different users); HCD11 (prototype, test and refine for access); CT8 (compare options, then build); IC4 (team goals, tasks and milestones); IC3 (written feedback given and used); IC5 (team roles) | Lesson 1: the anchor; retrieval of g9-algorithm-impacts; the human-centered steps named (research the users, write needs, explore options, prototype, test, change). Lesson 2: user research: each team interviews classmates who read from written persona cards (never acted), writes needs and records them in a small table. Lesson 3 (unplugged): accessibility as a design constraint: color contrast, keyboard use, clear language, text that enlarges; the laws that set requirements, named by their government names (the Americans with Disabilities Act, Section 508 of the Rehabilitation Act, the Individuals with Disabilities Education Act). Lesson 4: options sketched and compared on a benefit-risk-chart, including the social and ethical effects of each on different users. Lesson 5 (device or paper): a prototype of the chosen option (paper screens, or a short screen built in the editor). Lesson 6 (device): the prototype tested with users and with access checks (keyboard only, contrast, plain words) on a test-table. Lesson 7: written feedback from another team on the prototype and draft design record. Lesson 8: revision from the feedback and the tests. Lesson 9: each team presents; the product is scored. Lesson 10: respond by error letter. Lesson 11 (portfolio, not scored): each student lists the skills in the work they built this year (reading code, testing, cleaning data, designing with users), matches each to two kinds of job and names one to build next, a contributing use of HS-SOC-CE-46 (owned in grade 12, g12-career-goals); private by default. Out: no large user study, no meeting every point of formal accessibility guidelines, no legal reading of the laws, no certificates or pathways (grade 12). End-of-unit (lesson 9): a product: the team's prototype, test-table and design record, scored on look-fors for each human-centered step, plus each student's own one-page explanation of one design change, the user need behind it and the law or access rule it meets (HS-ALG-IM-09), so every student is scored on their own reasoning; draft (lesson 7), written feedback (lesson 7) and revision (lesson 8) come before the score. Tools: our own editor (optional, job: a short prototype screen); a contrast checker built into the page (job: test color contrast). Curio Class writes: the anchor kiosk, the persona cards, the access checklist, the design record template, the feedback form, the portfolio sheet | After unit 4 so user research is recorded and checked as data, and after units 1 and 2 so a prototype screen can be built and tested. The design project comes before the society unit so unit 6's human choices (design, deploy) are read by students who have just made design choices themselves. The portfolio lesson closes the unit because by then students have built most of the year's work | Candidate: kept, a team role card (researcher, designer, tester, writer) switched halfway, zero added days | Disability content: persona cards are written with the wording the sensitivity read settles from its pack; no student acts a disability or is asked about their own; a student who uses an assistive tool is never singled out. Laws named by government name only, sources ada.gov, section508.gov and sites.ed.gov/idea, as of the day the unit is written. Portfolio: private by default, no family job asked about. Agent reads: sensitivity (the starting pack in Sensitivity reads first). |
| 6 | Who decides? *When a new technology arrives, who makes the choices that shape it, and who gains or loses?* Anchor: a case card: tutoring tools that write answers for students are offered to every school in a district, and some students have no internet at home | 8 | g10-emerging-impacts; g10-human-choices; g10-history-policy | HS-SOC-ET-41; HS-SOC-HU-43 | Concept area: computing and society. Practices: HCD10 (who is included and who is not); HCD12 (users informed and in control); ESR1 (weigh who gains and who is harmed); IC3 (two views, each with a source) | Lesson 1: the anchor; retrieval of g9-emerging-differences; the emerging technology (generated-text tutoring tools in schools) evaluated for its effects on learning and fairness, on a benefit-risk-chart. Lesson 2: its effects on the environment (the energy the computing behind it uses) and on access and outcomes (students with and without home internet), each claim with two views and a dated source. Lesson 3 (application): a written evaluation that names the claim with the weakest evidence. Lesson 4: retrieval of g9-computing-history; a past law placed on the class timeline with what it did to the technology it touched: the 1998 federal law on children's online privacy, which led many sites to bar users under 13, read with two views and a dated source, a first look at HS-SOC-HI-39 (owned in grade 11, g11-policy-change); cause and effect only, no statute reading. Lesson 5: human choices: a state unemployment agency's automated fraud system (Michigan, 2013 to 2015, told from the court record) laid out at four decision points (use, design, deploy, regulate); at each a risk, a benefit and a long-term effect, each from a different person affected. Lesson 6: a short second case card on a data-driven choice (which data a model was trained on, where its cut-off was set) at the same four points, so data selection and tuning are seen as human choices. Lesson 7 (application): students write which decision mattered most in the Michigan case and why, with evidence. Lesson 8: review across the three cases. Out: predicting how a technology will develop, deciding who was right, a formal study, any code or model mathematics, reading a statute. End-of-unit: the year-end course-level check (lessons 62 and 63 of the course) stands for it. Tools: none (case cards, timeline, benefit-risk-chart on paper). Curio Class writes: the three case cards and their teacher source lines, the timeline strip, the four-column chart, the evaluation prompts | Last because it gathers the year: unit 2's AI types, unit 4's data and unit 5's design choices are what the cases' decisions are made of. Its rows hand on only to grade 11 and need nothing after them, so it can be assessed by the year-end check in weeks 31 and 32 | Candidate: kept, a source-line template (title, publisher, date) so every claim's source reads the same, zero added days | Work and benefits: the Michigan case touches families who lost benefits; no student is asked about a family member's work or benefits, and the teacher page carries health's "If a student tells you something" steps word for word. Home internet: no student is asked what they have at home. Cases name government bodies and courts, never companies. Teacher source lines, facts checked there when the unit is written: Michigan Supreme Court, Bauserman v. Unemployment Insurance Agency (2022 opinion, courts.michigan.gov); Federal Trade Commission, Children's Online Privacy Protection Rule page (ftc.gov); U.S. Department of Education Office of Educational Technology, "Artificial Intelligence and the Future of Teaching and Learning" (May 2023); International Energy Agency, "Energy and AI" (2025, iea.org); National Telecommunications and Information Administration, Internet Use Survey (ntia.gov), as of the day the unit is written. The data-driven case card is invented for practice. Agent reads: sensitivity (the court record and the claimants' advocates' account first). |

## Course-level checks

| Check | After unit | Check days | Respond days | What it checks |
|---|---|---|---|---|
| Course-level check, mid-year (weeks 15 and 16; it stands for unit 3's end-of-unit assessment) | 3 | 2 | 1 | Course day 30 scores unit 3 in full with unseen items: draw a network for a new written description with its hardware and software and trace one request through it (HS-SYS-NT-34); compare a new local network with the internet on structure, size, addressing and how data moves, naming the shared rules and the client and server roles (HS-SYS-NT-35); classify a new breach case by cause and by its impacts on an individual, an industry, a community and a government, by kind (HS-SYS-SE-32). Course day 31 samples units 1 and 2 with short new items: trace a new procedure call with a list (HS-PRO-RD-17), count steps for two new algorithms on given sizes (HS-ALG-PS-03), justify an AI type for a new task (HS-ALG-ML-06); unit 1's end-of-unit record for HS-PRO-PD-13 is carried unscored. Written, on paper. Day 32, the respond day for unit 3 and the check, reteaches by error letter and gathers fresh evidence on the missed items |
| Course-level check, year-end (weeks 31 and 32, week 32 the finals week; it stands for unit 6's end-of-unit assessment) | 6 | 2 | 1 | Course day 62 scores unit 6 in full with unseen items: a written evaluation of a new emerging-technology case card for its effects on society, the environment and access, from supplied sources with two views (HS-SOC-ET-41); a new case laid out at the four decision points with a risk, a benefit and a long-term effect at each and the decision that mattered most (HS-SOC-HU-43). Course day 63 samples units 1, 2, 4 and 5 with short new items: explain one part of a new program (HS-PRO-RD-17), find the failing test case of a new algorithm (HS-ALG-PS-03), choose the verification approach for a new table (HS-DAT-DC-24), read a new three-variable chart, and name the access fix a new screen needs (HS-ALG-IM-09); unit 5's scored product and unit 4's end-of-unit record for HS-DAT-DC-23 are carried unscored. Day 64, the respond day for unit 6 and the check, reteaches and records each student's gains for grade 11 |

## Cross-subject

No grade 10 row carries a cross_subject lean in data/progressions/computer-science.csv, so this course sets no
availability calendar for another subject. Two kinds of work touch other subjects, and each is taught inside its own
lesson so the course stands whatever the other courses' order:

- **Mathematics.** Unit 2 counts steps and compares counts as a list doubles; no logarithm or formula is used (no
  math ahead of math, lesson 13). Unit 4's three-variable chart reads a trend by eye, using the scatter plots of math
  grade 8; lesson 7 shows one worked chart first, so a student who has not read a scatter plot since grade 8 can
  follow.
- **English language arts and social studies.** Unit 6's written evaluations and unit 5's design record are writing
  practiced here, not owned; unit 6's law and court cases are a first look at policy, with no assumption of a
  government course (taught in grade 12).

## For the lead

1. **After-core check weeks (calendar pass).** This course's checks sit in weeks 15 and 16 (mid-year) and 31 and 32
   (year-end), off the grade 10 core check weeks 8 to 11 and 18 to 21; week 32 is the finals week. CALENDAR.md shows
   grade 10 week 15 with library's mid-year check, week 16 with physical education's, and week 31 with library's
   year-end check; they stay for the lead's one calendar pass across the after-core frames.
2. **Two-lesson checks (pattern for grades 6 to 12).** Pick: in a two-a-week course of 45-minute lessons, a
   course-level check that stands for a unit takes two lessons, the first scoring the unit, the second sampling the
   earlier units, since one lesson holds one full performance (lesson 19). Grades 6 to 9, 11 and 12 copy it; the
   kindergarten pilot's one-session check stays right for a 30-minute K to 2 session.
3. **Row changes needed** (listed in full in the writer's report): the packet-strip link (g10-network-of-networks
   assumes g8-network-failure), the boundary's structuring parts in g10-clean-text, the named and sourced cases in
   g10-breach-causes, g10-human-choices and g10-history-policy (the rows say "from memory"), the industry wording in
   g10-breach-causes, and the UK spelling "human-centred" in g10-design-hcd.
4. **Source list.** docs/APPROACH-SOURCES.md could add the course's case sources: HHS Office for Civil Rights breach
   report page, CISA's social engineering page, the FTC's phishing and children's online privacy pages, Bauserman v.
   Unemployment Insurance Agency (Michigan Supreme Court, 2022), the Office of Educational Technology's 2023 AI report,
   the IEA's "Energy and AI" (2025), NTIA's Internet Use Survey, and the Disability Rights Education and Defense Fund.
   None was opened for this frame (no downloads); each fact is checked at its source when the unit is written, and a
   page that refuses an automated read is kept as "browser check".
5. **Tool asks.** Three tools for the editor's build list or TOOL-ASKS.md: a step counter in our own editor (unit 2),
   supplied cleaning functions with a table view (unit 4), and a contrast checker built into the page (unit 5); plus
   a browser chart tool that plots three variables with color and a shape or label (unit 4).
