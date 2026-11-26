# Computer science: the standard, made usable

**Written 2026-11-16, fixed 2026-11-19 after a cold read (docs/reviews/prework-computer-science-read-2026-11-19.md)
and 2026-11-21 after the second-model read and the reading of the standards PDF
(docs/reviews/prework-computer-science-fixes-2026-11-20.md).** Its calls
are Cory's, logged in docs/agents/decisions/DESK-ANSWERS.md and named where they apply.

Written 2026-11-16 as the subject's pre-work (docs/PRODUCTION-PATH.md, "After the core subjects"; the owed row in
docs/ADOPTION-BAR-SUBJECTS.md, "Before a scope and sequence in this subject"). The model is
docs/courses/social-studies/STANDARD.md. Course calls (what a course teaches, the course list, minutes) are Cory's;
where one is needed this page recommends and says so.

## The owed row, and where it stands

| Owed | State | Where |
|---|---|---|
| A header for the ids file | Done 2026-11-11 | data/standards/csta-2026-ids.txt |
| The standards' wording, under its own license line | Done 2026-11-16: all 331 statements, CC BY-NC-SA 4.0 line in the file header | data/standards/csta-2026-statements.txt |
| Load the 135 Specialty standards | Done 2026-11-11 (ids); wording 2026-11-16 | data/standards/csta-2026-specialty-ids.txt; statements file |
| High school teaches the Foundational set, claims a Specialty id only where a topic already goes that far | Decided (Cory, 2026-11-11); restated in section 3 | This page |
| Approach page | Approved 2026-11-20 (Cory, Desk q-prework-cs-1); fields placed 2026-11-21 | docs/courses/computer-science/APPROACH.md |
| From the PDF: the sub-concept key, the practices table, every owner row checked against its boundary statement | Done 2026-11-21 (PDF read once, Desk q-fix-downloads-1). The boundary statements' text is not stored: the depth lives in our own words in each owner row's notes (Cory, 2026-11-21, Desk q-fix-cs-2; the PDF's CC BY-NC-SA license does not mix with a public CC BY repository) | Section 1 "Depth" and "Sub-concept codes"; section 3; data/progressions/computer-science.csv |

## 1. The standard and its terms

- **Which:** 2026 CSTA PK-12 Computer Science Standards, Computer Science Teachers Association, published summer
  2026, DOI 10.1145/3820482. It replaces the 2017 CSTA standards. Checked at source 2026-11-16: the PDF behind
  csteachers.org/2026-csta-pk-12-computer-science-standards/ (218 pages).
- **Shape:** three parts. Concepts are the content and the organizing frame: Algorithms and Design (ALG),
  Programming (PRO), Data and Analysis (DAT), Systems and Security (SYS), Computing and Society (SOC). Artificial
  intelligence has no concept of its own; it is spread across all five. Twelve practices in four groups (Ethics and
  Social Responsibility, Inclusive Collaboration, Computational Thinking, Human-Centered Design) say what students
  do. Seven dispositions (creativity, critical thinking, curiosity, persistence, reflectiveness, resourcefulness,
  sense of belonging) are habits of mind. Each standard carries a boundary statement saying what is and is not
  expected; the boundary statement, not the one-line statement, sets the depth (C1, "at the depth its wording asks").
- **Counts:** 196 Foundational ids (EK 16, E1 16, E2 16, E3 19, E4 19, E5 19, MS 45, HS 46; by concept ALG 40,
  PRO 45, DAT 35, SYS 38, SOC 38). 135 Specialty ids in two tiers (S1 73, S2 62) over six areas (AI, cybersecurity,
  data science, game development, physical computing, software development) plus five X + CS standards (computer
  science inside another subject).
- **Terms:** CC BY-NC-SA 4.0, printed on the PDF's license page and every page footer: free to share and adapt with
  credit, non-commercial, adaptations under the same license. Curio Class is free and sells nothing, which is the non-commercial test as we read it (not legal advice); if a paid tier
  ever appears, this is rechecked. Its own pages are CC BY. So: the statement text lives only in data/standards/csta-2026-statements.txt under CSTA's
  license; every Curio Class page, plan and tool cites ids and says things in our own words, and never copies a
  statement or boundary statement. A page states what a standard asks in a new sentence built from the plan's own task,
  never reworded line by line from the statement. Credit line where a day leans on a statement: "Standards: 2026 CSTA PK-12
  Computer Science Standards (CC BY-NC-SA 4.0)". Never say a course is aligned to, reviewed by or endorsed by CSTA.
- **Quoting.** A plan cites each standard by its id and states its action as one verb or a short phrase in our own words
  (the computer science form of UNIT-PLAN rule 15); the statement and boundary statement are never quoted. The
  statement lives in data/standards/csta-2026-statements.txt for the planner, not on the page.
- **Depth.** Each standard's boundary statement (in the PDF) says what students do and what is not expected, and so
  sets the depth. The boundary statements are not stored in the repository. The PDF was read once on 2026-11-21 and
  every owner row in data/progressions/computer-science.csv was checked against its boundary statement then, so each
  owner row's notes carry the depth in our own words, including what is left out. Every plan writes the depth it
  teaches to, and what it leaves out, in our own words, from its owner row. A K to 5 course never teaches an id at its
  next band's depth: for example, grade 4 writes an algorithm in words, and the flowchart is grade 5's.
- **Sub-concept codes** are the third part of an id. A code names a strand inside one concept or area: DAT-IM and
  ALG-IM are different strands. The key below (read from the PDF's naming tables, 2026-11-21) gives each code, its name
  and our one-line meaning.
- **The word AI.** Student copy may name artificial intelligence and machine learning as subjects of study. It never says
  how Curio Class was made.

**Sub-concept key, Foundational.**

| Concept | Code | Name | Our meaning |
|---|---|---|---|
| ALG | PS | Algorithmic problem solving | Planning, writing and checking step-by-step solutions |
| ALG | ML | Machine learning | Systems that find patterns in data to classify, predict or make things |
| ALG | IM | Impacts of algorithms and design | Who an algorithm or a design helps, leaves out or harms |
| PRO | PD | Program development | Building, improving and sharing programs, alone and in teams |
| PRO | VD | Variables and data storage | How a program holds, changes and organizes values |
| PRO | RD | Reading and documenting | Reading, explaining and commenting code |
| PRO | TR | Testing and refining | Testing, debugging and improving a program |
| DAT | DC | Data collection and preparation | Gathering, organizing, checking and cleaning data |
| DAT | DI | Data investigation | Asking a question of data, finding patterns, showing results |
| DAT | IM | Impacts of data science | How collecting and using data affects people |
| SYS | HW | Hardware and software | The parts of a computing system and how they work together |
| SYS | SE | Security | Keeping devices, accounts and information safe |
| SYS | NT | Networks | How devices connect and send information |
| SYS | IM | Impacts of computing systems | How systems affect lives, access and the environment |
| SOC | HI | History of computing | How computing came to be and what it changed |
| SOC | ET | Emerging technologies | New technologies, their limits and their effects |
| SOC | HU | Humans and computing | What people and machines each do, and the choices people make |
| SOC | CE | Career exploration | Computing in work and in students' own plans |

**Sub-concept key, Specialty** (high school; tiers S1 and S2). AIN (artificial intelligence): DD design and
development, DS data science for AI, HR human responsibility, PP professional practice. CYB (cybersecurity): ND network
theory and design, NO network operations, TS threats and security measures, CP cybersecurity policies, PP professional
practice. DSC (data science): CC creation and curation, AM analysis and modeling techniques, MI model interpretation and
reasoning, VZ visualization, PP professional practice. GMD (game development): DD design and development, PX player
experience, AR architecture, PP professional practice. PHY (physical computing): HC hardware and circuit design, IO
inputs and outputs, DD design and development, CI connectivity and the internet of things, PP professional practice.
SWD (software development): DD design and development, UX user experience, TR testing and refining, PP professional
practice. XCS (X + CS): XC, computer science inside another subject. In every area PP means the habits and ethics of
working in the field.

## 2. How the standards map to our courses

Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): one course per grade, K to 12, 13 courses under the
`cs-k12` track. The catalogue keeps that one `cs-k12` row, noted "2026 CSTA PK-12 standards; one course per grade
K-12" (Cory, 2026-11-21, Desk q-fix-cs-1).

| Our course | CSTA band | Ids | Note |
|---|---|---|---|
| Computer Science, kindergarten | EK (pre-K and K) | 16 | Curio Class has no pre-K, so all of EK is taught in K |
| Computer Science, grades 1 to 5 (one course each) | E1 to E5 | 16, 16, 19, 19, 19 | CSTA writes one set per grade; each course teaches its own |
| Computer Science, grades 6, 7 and 8 (one course each) | MS | 45 across the three | CSTA writes one band and no grade split; the progression gives each id one owner grade (see "Ownership of MS and HS ids") |
| Computer Science, grades 9 to 12 (one course each) | HS Foundational | 46 across the four | One owner grade each, by the same rule; Specialty ids claimed only where a unit already goes that far (Cory, 2026-11-11) |

Sessions a week: one in K to 5 (a specials rotation), two to three in 6 to 12 (a real elective). Settled 2026-11-16 (Cory, Desk card q-later-followups-1). Defaults (Cory, 2026-11-21, Desk q-fix-cs-1): K to 2, 32 sessions of 30 minutes; 3 to 5, 32 of 40; 6 to 12, 64 of 45 (two a week) for each year. A course frame may change them with its reason, as PE's defaults allow, and each band's scope and sequence names its short path (bar C2). Why two a week in 6 to 12: each high school year owns only 10 to 12 ids, and three a week would push the days outside the standards past the bar's 10 percent limit.

**Ownership of MS and HS ids.** The course progression (layer 4, docs/PRODUCTION-PATH.md), not the scope and sequence,
places each MS and HS id in exactly one grade that owns it: the grade where students are first taught it to the depth
set under "Depth" in section 1, and checked on it. Another grade of the band that uses the id again lists it as
`~ID` (used in a new setting, contributes). Every MS id is owned by grade 8 at the latest, every HS id by grade 12.
Starting split (ours, untested; counted from data/standards/csta-2026-ids.txt, MS 45 and HS 46): grade 6 owns about 17
MS ids, grade 7 about 15, grade 8 about 13, by concept ALG 4/4/3, DAT 4/2/3, PRO 3/3/3, SOC 3/3/2, SYS 3/3/2 (MS
concepts ALG 11, DAT 9, PRO 9, SOC 8, SYS 8; the split is forced, because MS-DAT-DC-21 to 24 must all come before MS-ALG-ML-07 in grade 7, which puts four DAT ids in grade 6). Grades 9, 10 and 11 own 12 HS ids each and grade 12 owns 10 (HS concepts ALG 11, DAT 8, PRO 9, SOC 9,
SYS 9; HS-DAT-IM-27 moved to grade 11, Cory, 2026-11-20, Desk q-prework-cs-1), with every concept in every year. Ordering constraints, ours: MS-PRO-VD-16 before MS-ALG-PS-01 and MS-PRO-RD-17;
MS-PRO-PD-12 before MS-PRO-RD-17; MS-PRO-RD-17 before MS-PRO-RD-18; MS-DAT-DC-23 before MS-DAT-DI-25 to 27; MS-ALG-ML-06
before MS-ALG-ML-07 and 08; MS-DAT-DC-21 to 24 before MS-ALG-ML-07; MS-SYS-NT-34 before NT-35; MS-DAT-DI-25 owned in
grade 8 unless the math frame teaches association earlier (from memory). HS: HS-PRO-VD-16 before HS-ALG-PS-01;
HS-PRO-PD-12 before HS-PRO-RD-17; HS-ALG-ML-07 before ML-08; HS-ALG-PS-03 after PS-01 and 02; HS-SYS-SE-31 and 32
before SE-33; HS-SOC-ET-40 and 41 before ET-42; HS-DAT-IM-27 before IM-28. Stems line up only inside K to 5 (a stem such
as E3-PRO-PD-04 follows E2-PRO-PD-04); MS and HS numbers do not match E5's, so a writer never assumes the same stem
across E5 to MS. EK is taught whole in kindergarten and E1 repeats several of its constructs: the K to 1 handoff is marked
weak in the progression, not re-taught.

**Partial base for K to 8.** Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): the UK's open computing
curriculum (scout: docs/reviews/computer-science-open-material-2026-11-16.md) is a partial base for grades K to 8.
Each unit taken from it is checked unit by unit for third-party material (anything not under the base's own license
is left out), and is rephrased for an American audience when needed (spelling, money, place names, school years).
Its source goes in the day's credit; no company name appears in student, teacher or family copy. The edition the
frames map is the archived Teach Computing Curriculum (raspberrypi.org/curriculum/archived, resources dated 2023, no
longer maintained by its publisher); England's current lessons, on Oak National Academy, differ by unit, so a frame
that adapts a current unit names it as such (docs/sources/BASE-TEXTS.md).

**Specialty standards.** The four high school courses teach all 46 Foundational ids between them. A unit may also claim an S1 id when
its task already does what the S1 statement and boundary ask (for example a unit that trains and tests a classifier
may claim an AI S1 id). No unit is lengthened to reach a Specialty id, and no S2 id is claimed in a Foundational
course. Decided (Cory, 2026-11-20, Desk q-prework-cs-1): grades 11 and 12 claim a short named list of
S1 ids as in-course standards, taught and checked in full and counted so bar criterion C1's 10 percent is not reached;
no new courses; S2 stays out. The list is eight S1 ids, four in grade 11 (S1-AIN-DD-02, S1-DSC-VZ-11, S1-CYB-TS-08, S1-SWD-TR-07) and four in grade 12 (S1-AIN-HR-09, S1-DSC-PP-13, S1-SWD-PP-08, S1-SWD-UX-05), each taught inside a row that already teaches the topic. S1 days count as days outside the course's own standards under C1, so each grade's scope and sequence keeps them, with any other such days, under 10 percent of its teaching days. Specialty courses (a pathway of one or two courses per area, as CSTA suggests) are not on the course list;
adding any is Cory's call.

**The 2017 codes** are the superseded set. Tool specs may show them beside 2026 ids as a crosswalk; they never stand
alone.

## 3. What is left out, and why

- Pre-K: no Curio Class course. The EK set is taught whole in kindergarten.
- What a school may swap or leave out (Cory, 2026-11-21, Desk q-fix-cs-1; the same rule as PE and the arts): a school
  may swap or leave out a named unit for its community's reasons. Each course page names these units, and it claims no
  standard that no remaining unit teaches; leaving out a unit means the course page and the unit's family note name
  the ids not claimed that year.
- Specialty II in the Foundational course (see above), and Specialty courses as courses (not on the list).
- The X + CS standards (XCS) as computer science days: they describe computer science inside other subjects, so
  they are leans for those subjects' units, not this course's.
- Boundary statements as text: never copied (license and our own voice). Plans restate the depth in our own words.
- Practices and dispositions have no ids in data/standards; units name the practice by its code and our own words,
  and every unit names at least one practice it teaches, with its day and task (bar criterion 2). The PDF pairs each
  standard with one or two practices and one or two dispositions; that pairing is not stored. The twelve practices,
  numbered 1 to 12 across four groups (read from the PDF 2026-11-21; labels ours), and which of the bar's four items
  (working together, testing and fixing, abstraction, explaining) each serves:

| Code | Group | Our label | Bar item |
|---|---|---|---|
| ESR1 | Ethics and social responsibility | Use computing for good: weigh who gains and who is harmed | none |
| ESR2 | Ethics and social responsibility | Respect people: credit others' work, protect users' data | none |
| IC3 | Inclusive collaboration | Explain computing ideas, give and take feedback | explaining |
| IC4 | Inclusive collaboration | Run a project: shared goals, tasks, milestones, documented work | working together |
| IC5 | Inclusive collaboration | Be a reliable, respectful teammate and reflect on the team's work | working together |
| CT6 | Computational thinking | Define the problem: criteria, limits, smaller parts | abstraction |
| CT7 | Computational thinking | Abstract: find patterns, make reusable parts, model and simulate | abstraction |
| CT8 | Computational thinking | Build: compare approaches, plan, then code or train | none |
| CT9 | Computational thinking | Test, debug and refine | testing and fixing |
| HCD10 | Human-centered design | Learn from and include different users | none |
| HCD11 | Human-centered design | Prototype, test and refine for use and access | testing and fixing |
| HCD12 | Human-centered design | Keep users informed and in control | none |

## 4. Cross-subject leans on the core progressions

CSTA prints interdisciplinary links for each Foundational standard (to CCSS, NGSS, the arts, health, library and
career standards). Our own reading of where the course leans is below; the skill ids of each lean on a core
progression are in the progression's `cross_subject` column (data/progressions/computer-science.csv), where the
check tests them. Library and career education (the last two lines) are not core subjects, so they are named here
only, not as progression leans.

- **Math:** sequence and pattern (K to 2), coordinate grids and angles for movement tasks (grades 4 to 6), variables
  and expressions (grade 6 on), data displays and statistics (DAT throughout), Boolean conditions as true and false
  statements. Frame "if later" lines bridge where the math grade has not taught it yet.
- **Science:** data collection and analysis, models and simulations, and the engineering design standards (ETS),
  which share the define, test and improve loop with ALG design standards.
- **ELA:** explaining an algorithm in writing, giving and taking feedback, research for SOC topics.
- **Social studies:** SOC standards on the history and effects of computing, privacy, law and policy (high school
  government); the values rule applies to them.
- **Library and research skills:** judging online sources, citing and using others' work (AASL Curate and Engage);
  the library course owns the method, computer science uses it.
- **Career education:** the Digital Technology cluster (CTE.Career Clusters.Digital Technology and its sub-clusters).

## 5. Cost, devices and rooms

Programming units run on a device per one or two students in a common browser; nothing is installed and no account is
made (bar criterion 7). Physical computing (a microcontroller board) is optional and always has a simulator or paper
stand-in; its cost is stated where used.

### Devices and rooms

Three things are kept apart. An unplugged day teaches an idea with cards, paper or movement; every unit has at least
one (kind: understanding; bar item 5). A device day is a day where a tool does a named job. A stand-in is how a device
day runs with fewer devices (C14). Every device day is written four ways (section fields 5 and 10): (1) one device per
pair, the default; (2) a few devices: three or four stations on a rotation, the other pairs at a paper station on the
same idea, every pair taking the keyboard role at least once; (3) one screen: the class runs the program together,
predicts and votes before each run, and a student at the device takes each step; (4) no device: the same idea on paper,
with trace tables, "be the computer", programs written on paper and checked by a partner. An id whose standard asks
students to use a computational tool, train a model, or use documentation and libraries is met only on a device (for
example E4-DAT-DC-09, E5-DAT-DC-09, E5-ALG-ML-02, MS-DAT-DC-23, MS-DAT-DI-25, MS-PRO-PD-13, HS-DAT-DC-21,
HS-DAT-DC-23, HS-ALG-ML-08, HS-PRO-PD-12, HS-PRO-PD-13, HS-SYS-HW-30). On the no-device path that day teaches the
idea and the course record marks the id "part met without a device"; the course never says the id was met.

### Generated-text tools

Evaluating generated output (MS-PRO-RD-18, HS-PRO-RD-18, HS-ALG-PS-05) is met on supplied material: Curio Class supplies
saved outputs and code samples, some right and some flawed, and students judge them for accuracy and use. No tool
asks a student to use a live generated-text tool, make an account or send anything off the device. For MS-ALG-PS-05,
which asks students to use one (Cory, 2026-11-20, Desk q-prework-cs-1): no live tool in Curio
Class; the day is teacher-run on one screen with a tool the school has already approved and no student accounts, and
the course marks the id "part met" where a school has none.

### Our own editor

Settled (Cory, 2026-11-21, Desk q-prework-open-1): build one small browser editor of our own (blocks and a
text view, with a step-through trace), a single file with no account, starting with grades 3 to 5, rather than pointing
teachers to a third-party tool. The text language for grades 6 to 12 is Python, run in this editor (Cory, 2026-11-21,
Desk q-fix-cs-1): the K to 8 partial base teaches Python in its middle years, so its units adapt directly, and it is
the most common first text language in high school.

The editor also keeps a small offline version history with branch, review and merge, so grade 12's team project
meets S1-SWD-PP-08 in full; until that exists, the standard is part met and the course page says so (Cory, 2026-11-21,
Desk q-fix-cs-2). It is an ask for the editor's own build list when the editor is specced.

### Blocks to text

Kindergarten to grade 5: block code with a text view of the same program. Grade 6: blocks and Python text side by
side. Grade 7: written Python for new programs, blocks as a stand-in. Grade 8 on: Python. Python is named as a subject
term on teacher pages and runs in our own editor in a common browser with nothing installed. The language is Cory's
(above); the grade steps are ours, untested.

### Privacy and safety

No student's name, photo, voice, location or family detail goes into a program, a dataset or a tool. Class data is about
things (weather, pets drawn from a list, shapes, snack types), tallied by hand or with counts, never about identifiable
children, health or home. Accounts, passwords and personal information are taught with a pretend page or a paper account;
no student makes an account. Online safety days use paper or an offline pretend site; any real web use is teacher-led on
one screen. Security days use toy systems built into the page; no scanning, no attack and no test of a real school or
home system, ever. A tool stores student work only on the device or in a file the student downloads or prints; it sends
nothing off the device.

### Real cases in society days

A real case is told by what happened, not by the company or product: "a company sold a face-matching system to police;
a 2018 study found it wrong more often for darker-skinned women" (example only, from memory, facts to be checked
before use). The teacher page gives the date and the source's title and publisher in a source line, which is a citation
and not a promotion. If a case cannot be understood without the name, choose another case or use a court or government
record's own description. A society day gives two views and one dated source for each.
Decided (Cory, 2026-11-20, Desk q-prework-cs-1): student and teacher copy may name government bodies and
courts but never companies, with sources only in the teacher source line.
