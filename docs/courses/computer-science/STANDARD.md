# Computer science: the standard, made usable

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

data/courses.csv has one track, `cs-k12`; COURSES-STATUS lists four band courses (K to 2, 3 to 5, 6 to 8, 9 to 12).

| Our course | CSTA band(s) | Ids | Note |
|---|---|---|---|
| Computer Science, grades K to 2 | EK (pre-K and K), E1, E2 | 48 | EK is written for pre-K and K together; Curio Class has no pre-K, so all of EK is taught in K |
| Computer Science, grades 3 to 5 | E3, E4, E5 | 57 | Grade-level standards, one set per grade |
| Computer Science, grades 6 to 8 | MS | 45 | CSTA writes one band for the three years and no grade split |
| Computer Science, grades 9 to 12 | HS Foundational | 46 | Specialty ids claimed only where a unit already goes that far (Cory, 2026-11-11) |

**Open with Cory: what a band course is.** CSTA writes a separate set for each grade from 1 to 5, so a K to 2 or 3 to 5
"course" is really three years. Options: (a) one year per grade in K to 5 (six years), with middle and high school
each one year: the band courses become eight courses; (b) each band course is one year, taught once in the band
(K to 2 teaches 48 standards in one year), which breaks CSTA's grade order; (c) as (a), but middle school spread over
three years at fewer minutes a week. **Pick: (a).** It follows the standard's own grade order, it is how most
elementary schools run computer science (a weekly special, every year), and middle and high school stay the single
course most schools offer. Minutes per week go in each frame (recommend one session a week in K to 5, as library and
SEL do; daily or near daily for the middle and high school course).

**Specialty standards.** The high school course teaches all 46 Foundational ids. A unit may also claim an S1 id when
its task already does what the S1 statement and boundary ask (for example a unit that trains and tests a classifier
may claim an AI S1 id). No unit is lengthened to reach a Specialty id, and no S2 id is claimed in the Foundational
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
