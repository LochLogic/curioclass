# Computer science: the standard, made usable

**DRAFT, 2026-11-16.**

Written 2026-11-16 as the subject's pre-work (docs/PRODUCTION-PATH.md, "After the core subjects"; the owed row in
docs/ADOPTION-BAR-SUBJECTS.md, "Before a scope and sequence in this subject"). The model is
docs/courses/social-studies/STANDARD.md. Course calls (what a course teaches, the course list, minutes) are Cory's;
where one is needed this page recommends and says so.

## The owed row, and where it stands

| Owed | State | Where |
|---|---|---|
| A header for the ids file | Done 2026-11-11 | data/standards/csta-2026-ids.txt |
| The standards' wording, under its own licence line | Done 2026-11-16: all 331 statements, CC BY-NC-SA 4.0 line in the file header | data/standards/csta-2026-statements.txt |
| Load the 135 Specialty standards | Done 2026-11-11 (ids); wording 2026-11-16 | data/standards/csta-2026-specialty-ids.txt; statements file |
| High school teaches the Foundational set, claims a Specialty id only where a topic already goes that far | Decided (Cory, 2026-11-11); restated in section 3 | This page |
| Approach page | Draft, waiting on Cory's yes | docs/courses/computer-science/APPROACH.md |

One follow-up sits outside this subject's files: LICENSE-CONTENT.md says all Curio Class data is CC BY 4.0, so it needs
a third-party line naming csta-2026-statements.txt as CC BY-NC-SA 4.0 (the lead's file; flagged
docs/reviews/standards-currency-2026-11-11.md, csta section, item 5).

## 1. The standard and its terms

- **Which:** 2026 CSTA PK-12 Computer Science Standards, Computer Science Teachers Association, published summer
  2026, DOI 10.1145/3820482. It replaces the 2017 CSTA standards. Checked at source 2026-11-16: the PDF behind
  csteachers.org/2026-csta-pk-12-computer-science-standards/ (218 pages).
- **Shape:** three parts. Concepts are the content and the organising frame: Algorithms and Design (ALG),
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
- **Terms:** CC BY-NC-SA 4.0, printed on the PDF's licence page and every page footer: free to share and adapt with
  credit, non-commercial, adaptations under the same licence. Curio Class is free, so non-commercial is met, but its
  own pages are CC BY. So: the statement text lives only in data/standards/csta-2026-statements.txt under CSTA's
  licence; every Curio Class page, plan and tool cites ids and says things in our own words, and never copies a
  statement or boundary statement. Credit line where a day leans on a statement: "Standards: 2026 CSTA PK-12
  Computer Science Standards (CC BY-NC-SA 4.0)". Never say a course is aligned to, reviewed by or endorsed by CSTA.

## 2. How the standards map to our courses

Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): one course per grade, K to 12, 13 courses under the
`cs-k12` track.

| Our course | CSTA band | Ids | Note |
|---|---|---|---|
| Computer Science, kindergarten | EK (pre-K and K) | 16 | Curio Class has no pre-K, so all of EK is taught in K |
| Computer Science, grades 1 to 5 (one course each) | E1 to E5 | 16, 16, 19, 19, 19 | CSTA writes one set per grade; each course teaches its own |
| Computer Science, grades 6, 7 and 8 (one course each) | MS | 45 across the three | CSTA writes one band and no grade split; the 6 to 8 scope and sequence places each id in a year (introduced, then built on), and each id is fully met by grade 8 |
| Computer Science, grades 9 to 12 (one course each) | HS Foundational | 46 across the four | Placed by year the same way; Specialty ids claimed only where a unit already goes that far (Cory, 2026-11-11) |

Minutes per week go in each frame (recommend one session a week in K to 5; more in 6 to 12). Still open with Cory.

**Partial base for K to 8.** Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): the UK's open computing
curriculum (scout: docs/reviews/computer-science-open-material-2026-11-16.md) is a partial base for grades K to 8.
Each unit taken from it is checked unit by unit for third-party material (anything not under the base's own licence
is left out), and is rephrased for an American audience when needed (spelling, money, place names, school years).
Its source goes in the day's credit; no company name appears in student, teacher or family copy.

**Specialty standards.** The four high school courses teach all 46 Foundational ids between them. A unit may also claim an S1 id when
its task already does what the S1 statement and boundary ask (for example a unit that trains and tests a classifier
may claim an AI S1 id). No unit is lengthened to reach a Specialty id, and no S2 id is claimed in a Foundational
course. Specialty courses (a pathway of one or two courses per area, as CSTA suggests) are not on the course list;
adding any is Cory's call.

**The 2017 codes** are the superseded set. Tool specs may show them beside 2026 ids as a crosswalk; they never stand
alone.

## 3. What is left out, and why

- Pre-K: no Curio Class course. The EK set is taught whole in kindergarten.
- Specialty II in the Foundational course (see above), and Specialty courses as courses (not on the list).
- The X + CS standards (XCS) as computer science days: they describe computer science inside other subjects, so
  they are leans for those subjects' units, not this course's.
- Boundary statements as text: never copied (licence and our own voice). Plans restate the depth in our own words.
- Practices and dispositions have no ids in data/standards; units name the practice by its group and our own words,
  and every unit names at least one practice it teaches (bar criterion 2).

## 4. Cross-subject leans on the core progressions

CSTA prints interdisciplinary links for each Foundational standard (to CCSS, NGSS, the arts, health, library and
career standards). Our own reading of where the course leans:

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

## 5. Cost and devices

Every unit has an unplugged path (bar criterion 5, ours). Programming units need a device per one or two students
running a common browser; nothing is installed and no account is made (bar criterion 7). Physical computing (a
microcontroller board) is optional and always has a simulator or paper stand-in; its cost is stated where used.
