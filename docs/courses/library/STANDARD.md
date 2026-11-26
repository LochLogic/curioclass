# Library and research skills: the standard, made usable

**DRAFT, 2026-11-16. Read cold 2026-11-20 (docs/reviews/prework-library-read-2026-11-20.md) and fixed.**

Written 2026-11-16 as the subject's pre-work (docs/PRODUCTION-PATH.md, "After the core subjects"; the owed row in
docs/ADOPTION-BAR-SUBJECTS.md, "Before a scope and sequence in this subject"). The model is
docs/courses/social-studies/STANDARD.md. Eight courses (section 3), course track `library`.
Decided: separate courses, our own bar, and they may be smaller: fewer minutes a week (one or two sessions, the frame
says which), never fewer units (Cory, 2026-11-11 and 2026-11-15).

## The owed row, and where it stands

| Owed | State | Where |
|---|---|---|
| Relabel the file to the second edition (2025) | Done 2026-11-11 (label in the header); edition confirmed at source 2026-11-16 | data/standards/aasl-2018.txt |
| Open the continuum's grade lists | Done: grades 3 to 5 read in full 2026-11-16 from the web (no copy in the source store); PK to 2, 6 to 8 and 9 to 12 read in full 2026-11-21 (downloaded with Cory's yes, Desk q-fix-library-1) | Section 2 |
| Our own words for the 68 | Done 2026-11-21 against the second edition chart | data/standards/aasl-words.txt |
| Progression gate support | Done 2026-11-21: library entry in scripts/progression.py, data/progressions/library-excluded.csv (five ids), data/progressions/library.csv (98 rows, read cold 2026-11-21, docs/reviews/progression-library-2026-11-21.md) | Sections 3 and 4 |
| Catalog | Done 2026-11-21: eight course rows in data/courses.csv, grade_subjects.csv and modules.csv (Cory, 2026-11-21, Desk q-fix-library-1); scripts/course_status.py counts them | Section 3 |
| Approach page | Approved 2026-11-21 (Cory, Desk q-prework-open-2) | docs/courses/library/APPROACH.md |

## 1. The standard and its terms

- **Which:** American Association of School Librarians, National School Library Standards, second edition,
  learner framework (file dated 2025-09-18; the PDF footer says copyright 2026; ALA lists the edition as 2025). Confirmed 2026-11-16 at standards.aasl.org, which presents the "Second
  Edition". Six Shared Foundations (I Inquire, II Include, III Collaborate, IV Curate, V Explore, VI Engage), each in
  four Domains (A Think, B Create, C Share, D Grow): 68 competencies, ids `AASL.I.A.1` style, unchanged from 2018.
- **Name lags (not this subject's files to change):** the file name aasl-2018.txt and the tag `AASL-2018` in
  scripts/standards.py and data/modules.csv stay as names (the file header says why). data/subjects.csv already
  labels the row with the second edition.
- **Terms** (standards.aasl.org/permissions, read 2026-11-16): one competency may be excerpted into a lesson or unit
  plan for non-commercial education; the whole framework or a substantial part needs ALA permission. So the repo holds
  ids and our own words, never the competency text, and pages never claim AASL alignment approved by anyone.
- **Our own words:** data/standards/aasl-words.txt, the id, a tab, and one skill phrase of 8 to 15 words (an
  action and an object, not a rewording of the sentence), for example `AASL.IV.B.3`, "Question each source's maker
  and purpose before trusting what it says." Written without asking ALA for permission, since a phrase names the
  skill and follows no sentence (Cory, 2026-11-21). All 68 written 2026-11-21 against the second edition chart, read
  once from a copy kept outside the repo (S:\CurioClass-sources\library\aasl-2026-11-21; Cory, 2026-11-21, Desk
  q-fix-library-1).
- **What it lacks:** AASL competencies are not set by grade. The same 68 apply K to 12. The bar's criterion 2 asks for
  named priority skills per grade, so a grade sequence must come from elsewhere.

## 2. The grade sequence: the Empire State Information Fluency Continuum as the check set

- **What it is:** a PK to 12 continuum by Barbara Stripling for New York City and New York State school libraries,
  hosted by Monroe One BOCES School Library System (libguides.monroe.edu/ESIFC; band files dated 2019; continuum page
  last updated 2019-10-23). Four anchor standards: inquiry and design thinking, multiple literacies, social and civic
  responsibility, personal growth and agency (the guide's framework page, read 2026-11-21; no author named there).
  Six phases inside the inquiry standard (connect, wonder, investigate, construct, express, reflect), confirmed in
  all four band files 2026-11-21, followed by a design thinking standard inside the same anchor. Each phase has
  indicators with a cell per grade column, the priority skills marked in bold in the cells and gathered in a
  "priority skills" box per phase for the whole band.
- **Grade columns, by band file** (checked 2026-11-21): PK to 2 has PK, K, 1 and 2 (no Curio Class course uses the
  PK column); 3 to 5 has 3, 4 and 5; 6 to 8 has 6, 7 and 8; 9 to 12 has only two columns, 9-10 and 11-12. So a
  grade 9 or 10 progression row is checked against the 9-10 cell and an 11 or 12 row against the 11-12 cell, and the
  progression says how grade 9 differs from 10 and 11 from 12, since the continuum does not. The four band names the
  pages use (K to 2, 3 to 5, 6 to 8, 9 to 12) match the files, K to 2 being the file's PK to 2 without PK.
- **Read in full:** the grades 3 to 5 band file 2026-11-16; the PK to 2, 6 to 8 and 9 to 12 files 2026-11-21, from
  copies kept outside the repo (S:\CurioClass-sources\library\aasl-2026-11-21, read once, ids and figures only).
  Example of the grain, in our own words: grade 3 uses a teacher-given source for background and simple
  note-making; grade 4 picks an interesting part of a broad topic and compares primary and secondary sources the
  teacher chose; grade 5 judges which questions facts can answer, weighs print, video and online sources for
  relevance and builds a bibliography to a model. In K to 2 the bold skills include finding picture books by their
  labels and shelf order, looking a book up in the catalog by author, title or key word, naming who made a site,
  and crediting authors; in 6 to 8, citing every source in a set style and deciding what fair use allows; in 9 to
  12, reading laterally for background, search filters and operators, and copyright, open licenses and asking a
  maker's permission. The per-grade priority skills, in our words, are the rows of data/progressions/library.csv;
  where a row places a continuum bold skill in a different grade, its note says why.
- **Terms:** no license or copyright line on the guide pages or in the band file. Unclear, so reference only: used to
  place skills in grades and to check our list, never copied.
- **Use (recommended, ours):** each course's progression names priority skills per grade in our own words, tagged
  with the AASL ids they serve, and checked against the continuum's bold skills for that grade. Where the two differ,
  the progression says why.

## 3. How the standard maps to our courses

Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): one course per grade K to 5, then one course for
grades 6 to 8 and one for grades 9 to 12, eight courses. The K to 5 courses each plan one year, so the skills grow
every year. The 6 to 8 and 9 to 12 courses spread across their grades, about one session every two weeks, taught
alongside other classes so research skills come back each year. Settled 2026-11-16 (Cory, Desk card q-later-followups-1).
Course ids: `library-k`, `library-1` to `library-5`, `library-6-8`, `library-9-12`, one row each in data/courses.csv
in the band-split form of health, PE and arts (Cory, 2026-11-21, Desk q-fix-library-1).

**Ownership** (ours, untested). Each of the 68 ids is owned by exactly one grade, the school year where it is first
met at the depth a check can score on its own (not the "with help" level); every other year where a course returns
to it carries `~ID` with a one-line note on how that year differs. Grades 6 to 8 and 9 to 12 get a progression row
per school year (6, 7, 8; 9, 10, 11, 12) even though each is one course: the progression's grades are the school
years, the course is how they are taught. Each row's `assumes` names only the earlier library row it builds on
(empty in kindergarten; each school year's row assumes the library row of the year before, so no grade is skipped),
since the gate accepts only rows of the same file there; an ELA or social studies row it builds on goes in
`cross_subject` (section 5). The gate's library entry in scripts/progression.py uses the standards file, the
anchor, ids with no grade (any grade may own one; the one-owner check does the work) and
data/progressions/library-excluded.csv for the ids section 4 places elsewhere. Settled (Cory, 2026-11-21): own once, at
the school year where the id is first checked alone; `library-6-8` stays one course across grades 6 to 8, with a
row per school year.

| Courses | AASL | Priority skill emphasis (ours; set grade by grade in data/progressions/library.csv) |
|---|---|---|
| K, 1 and 2 (one course each) | All six foundations, mostly at the "with help" level (carried as `~`, owned only where the grade checks an id alone: Ownership, above) | Asking a question, finding a book by its label and shelf order, retelling what a source says, saying who made it and where it came from, sharing with the class (checked against the PK to 2 band file, 2026-11-21) |
| 3, 4 and 5 (one course each) | All six | Key words, searching a catalog and a chosen site, note-making, primary and secondary sources, a simple bibliography, first lateral checks of a site |
| Grades 6 to 8 (one course) | All six | Search strategy, lateral reading, judging evidence and who is behind it, paraphrase and quotation, citation in one style, fair use basics, checking text made by a machine like any other source (who made it, what it cites) |
| Grades 9 to 12 (one course) | All six | Research question design, databases, search operators and filters, and open sources, lateral reading on hard cases, synthesis across sources, full citation, copyright, licenses, fair use and asking a maker's permission (checked against the 9 to 12 band file, 2026-11-21), checking and disclosing the use of machine-made text, sharing a research product |

**Partial bases for 6 to 12.** Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): the CC BY
online-reasoning lessons and the open web-literacy book named in docs/reviews/library-open-material-2026-11-16.md
are partial bases for the 6 to 8 and 9 to 12 courses. Only items under an open license are adapted, in our voice,
with the source in the day's credit, and each item's license is re-read at source when it is first adapted (the
scout's reading of 2026-11-16 is the only one on file); no company or product name appears in student, teacher or family copy.

Every unit names host tasks from the grade's other courses (bar criterion 4): research for a science investigation, a
social studies source question, an ELA research piece. Each also carries a stand-alone host task (APPROACH.md).

## 4. What is left out, and why

- The AASL school librarian and school library frameworks: they describe adults and programs, not learners.
- Reading promotion and literature appreciation (the continuum's multiple literacies standard) beyond what a research
  unit needs: ELA owns reading; library units may use the same books.
- The continuum's design thinking strand: science and computer science own the design cycle; library leans on them
  and keeps only self-chosen making inside a research product (V.B.2, below).
- **By id.** The gate and bar criterion C1 work on ids, not themes. Each of the 68 is either excluded with a reason in
  `data/progressions/library-excluded.csv`, or owned once by a library row and carried as `~` in other years
  (section 3, Ownership); the owner row meets it through a research task (for example II.B.2, weighing
  perspectives, on the day two sources disagree; III.C.1, feedback, on the revise day of a research product).
  Carrying an id as `~` never stands in for its one owner row. Everything not placed below is met through a
  research task (Cory, 2026-11-21).
- **The eight ids checked against the second edition chart** (Cory, 2026-11-21, Desk q-fix-library-1: an id that
  belongs elsewhere goes to its receiving subject and is never dropped). Three stay in library, owned by a library
  row: III.A.1 (choosing to widen and deepen a question by researching with others: a group inquiry day), V.C.2
  (working out with others a new way to find something out, such as a class survey or an observation plan: an
  inquiry day) and V.B.2 (keeping going on a self-chosen making product through trial and error: the made product of
  a research unit). Five are placed in a receiving subject, listed in library-excluded.csv with that subject as the
  reason, and named there by the receiving subject's own page:

| Id | Receiving subject and course band | Why there |
|---|---|---|
| V.B.1 | Science, K to 12: the engineering design rows and the `design-cycle` model (from `sk-define-problem`, K-2-ETS1-1) | The design, test and improve cycle is engineering design, which science teaches every year; computer science uses the same loop |
| V.A.1 | ELA, K to 12: the range of reading and writing rows (RL and RI .10, W.10: `ek-group-reading`, `e3-reading-range` onward, `e3-writing-tasks` onward) | Reading widely in many forms and writing for many purposes is ELA's own range standard |
| V.D.1 | SEL, all four bands (`sel-k-2` to `sel-9-12`): SM3, keeping on task and pushing yourself | Trying again when a task gets hard is self-management, taught on everyday cases |
| V.D.2 | SEL, all four bands: SA8, skill grows with effort, practice and help | The growth view of skill is a self-awareness sub-skill |
| III.D.2 | SEL, all four bands: RS4, working as a team | Treating the group's learning as one's own job is a teamwork skill, taught where SEL teaches teams |

- **What a school may swap or leave out** (Cory, 2026-11-21, Desk q-fix-library-1; the same rule as SEL, PE and
  arts, docs/courses/arts/STANDARD.md section 5): a school or family may swap a case or leave out a unit for its
  community's reasons. Swapping a case for another keeps the unit's ids met; leaving out a unit means the course page
  and the unit's family note name the ids not claimed that year. K to 5 case sets stay neutral: no politics,
  elections, religion, identity groups or conflict (APPROACH.md, "Sensitive ground", item 1).

## 5. Cross-subject leans

**Who teaches what first.** ELA owns the research cycle and the writing of it (the model `research-cycle`; rows
`ek-shared-research` and `e1-shared-research` to `e12-research`), the list of sources in research writing (grade 4,
`e4-research`, which builds on library's grade 2 credit line and grade 3 source list), finding answers quickly across
several print and digital sources (grade 5, `e5-locate-sources`), source credibility in writing (grade 6, `e6-short-research`)
and a standard citation format (grade 7, `e7-research-questions`). Social studies owns sourcing and corroboration
(the models `source-sourcing` and `corroboration`, from the grade 2 rows `ss2-source-maker` and `ss2-two-accounts`)
and news reading (`ss8-news-literacy`, grade 8;
`us1-news-reading`, grade 11). Library owns what neither does: searching as a skill (changing a query, catalogs
and databases, choosing among results), leaving the page to check who is behind it (lateral reading, the first time
it is taught as a method: owned by a library row before grade 8, where `ss8-news-literacy` uses it on news), going upstream to the first source, honest use of others' work across media (not only in
writing), and choosing among tools. Where a library row meets an ELA or social studies skill it names that row's id in
`cross_subject` (for example `ela:e5-locate-sources`; never a model name, and never in `assumes`, section 3); the
progression says which came first in each grade. Re-read against ELA grades 3 to 7 on 2026-11-21
(docs/reviews/progression-library-2026-11-21.md): no conflict in the emphasis cells; two ownership lines above were
corrected and grade 3 note categories moved to grade 4.

- **ELA:** the research writing standards W.7 and W.8 from kindergarten and W.9 from grade 4, and informational
  reading.
- **Social studies:** C3 dimension 3 (sources and evidence) and Massachusetts news and media literacy (NML), from
  grade 8 (`ss8-news-literacy`). Library owns the lateral reading method; social studies uses it on its sources.
- **Science:** science rows obtain and combine information from texts, maps and media (for example `s2-water-where`,
  `s3-climates`, `s4-energy-resources`, `s5-protect-resources`; `s8-human-trait-technology` asks for reliable
  sources), but none teaches judging a source as a method. Library names such rows as host tasks and teaches the
  judging.
- **Computer science:** computer science owns how machine-made text tools work, in its own rows; library owns
  checking what they produce, and assumes no computer science row.
