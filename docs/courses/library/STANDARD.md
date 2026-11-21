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
| Open the continuum's grade lists | Grades 3 to 5 read in full 2026-11-16; PK to 2, 6 to 8 and 9 to 12 owed before the progression | Section 2 |
| Our own words for the 68 | Owed: data/standards/aasl-words.txt, one skill phrase per id | Section 1 |
| Progression gate support | Owed: scripts/progression.py has no library entry yet | Section 3 |
| Approach page | Draft, waiting on Cory's yes | docs/courses/library/APPROACH.md |

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
- **Our own words (owed):** data/standards/aasl-words.txt, the id, a tab, and one skill phrase of 8 to 15 words (an
  action and an object, not a rewording of the sentence), for example `AASL.IV.B.3`, "Question each source's maker
  and purpose before trusting what it says." Written without asking ALA for permission, since a phrase names the
  skill and follows no sentence. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2)
- **What it lacks:** AASL competencies are not set by grade. The same 68 apply K to 12. The bar's criterion 2 asks for
  named priority skills per grade, so a grade sequence must come from elsewhere.

## 2. The grade sequence: the Empire State Information Fluency Continuum as the check set

- **What it is:** a PK to 12 continuum by Barbara Stripling for New York City and New York State school libraries,
  hosted by Monroe One BOCES School Library System (libguides.monroe.edu/ESIFC; band files dated 2019; continuum page
  last updated 2019-10-23). Four anchor standards and six phases inside the inquiry standard (connect, wonder,
  investigate, construct, express, reflect), from memory of the 2019 guide: to be confirmed against the band files
  before this line is used in any public source line. Each
  phase has indicators with a cell per grade, and the priority skills for each grade are marked in bold and gathered
  in a "priority skills" box per phase.
- **Read 2026-11-16:** the grades 3 to 5 band file in full. Example of the grain, in our own words: grade 3 uses a
  teacher-given source for background and simple note-making; grade 4 picks an interesting part of a broad topic and
  compares primary and secondary sources the teacher chose; grade 5 judges which questions facts can answer, weighs
  print, video and online sources for relevance and builds a bibliography to a model. The PK to 2, 6 to 8 and 9 to 12
  files have the same shape (structure seen on the continuum page; not read cell by cell). They are read in full
  before the progression is drafted, and the result goes in a table here: for each grade, the priority skills in our
  words, and a row for each place our list differs.
- **Terms:** no licence or copyright line on the guide pages or in the band file. Unclear, so reference only: used to
  place skills in grades and to check our list, never copied.
- **Use (recommended, ours):** each course's progression names priority skills per grade in our own words, tagged
  with the AASL ids they serve, and checked against the continuum's bold skills for that grade. Where the two differ,
  the progression says why.

## 3. How the standard maps to our courses

Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): one course per grade K to 5, then one course for
grades 6 to 8 and one for grades 9 to 12, eight courses. The K to 5 courses each plan one year, so the skills grow
every year. The 6 to 8 and 9 to 12 courses spread across their grades, about one session every two weeks, taught
alongside other classes so research skills come back each year. Settled 2026-11-16 (Cory, Desk card q-later-followups-1).
Course ids: `library-k`, `library-1` to `library-5`, `library-6-8`, `library-9-12`.

**Ownership** (ours, untested). Each of the 68 ids is owned by exactly one grade, the school year where it is first
met at the depth a check can score on its own (not the "with help" level); every other year where a course returns
to it carries `~ID` with a one-line note on how that year differs. Grades 6 to 8 and 9 to 12 get a progression row
per school year (6, 7, 8; 9, 10, 11, 12) even though each is one course: the progression's grades are the school
years, the course is how they are taught. Each row's `assumes` names the earlier library row or the ELA or social
studies row it builds on (section 5). The gate then needs library in scripts/progression.py: the standards file, the
anchor, an id that carries no grade (any grade may own it, and the one-owner check does the work), and
`data/progressions/library-excluded.csv` for the ids section 4 excludes. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2)

| Courses | AASL | Priority skill emphasis (ours, to be set at the progression) |
|---|---|---|
| K, 1 and 2 (one course each) | All six foundations, at the "with help" level | Asking a question, finding a book by its parts, retelling what a source says, saying where it came from, sharing with the class |
| 3, 4 and 5 (one course each) | All six | Key words, searching a catalogue and a chosen site, note-making, primary and secondary sources, a simple bibliography, first lateral checks of a site |
| Grades 6 to 8 (one course) | All six | Search strategy, lateral reading, judging evidence and who is behind it, paraphrase and quotation, citation in one style, fair use basics, checking text made by a machine like any other source (who made it, what it cites) |
| Grades 9 to 12 (one course) | All six | Research question design, databases and open sources, lateral reading on hard cases, synthesis across sources, full citation, copyright, licences and fair use, checking and disclosing the use of machine-made text, sharing a research product |

**Partial bases for 6 to 12.** Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): the CC BY
online-reasoning lessons and the open web-literacy book named in docs/reviews/library-open-material-2026-11-16.md
are partial bases for the 6 to 8 and 9 to 12 courses. Only items under an open licence are adapted, in our voice,
with the source in the day's credit; no company or product name appears in student, teacher or family copy.

Every unit names host tasks from the grade's other courses (bar criterion 4): research for a science investigation, a
social studies source question, an ELA research piece. Each also carries a stand-alone host task (APPROACH.md).

## 4. What is left out, and why

- The AASL school librarian and school library frameworks: they describe adults and programmes, not learners.
- Reading promotion and literature appreciation (the continuum's multiple literacies standard) beyond what a research
  unit needs: ELA owns reading; library units may use the same books.
- The continuum's design thinking strand: science and computer science own design; library leans on them.
- **By id.** The gate and bar criterion C1 work on ids, not themes. Each of the 68 is either owned by a library row,
  carried as `~` on a research task (for example II.B.2, weighing perspectives, on the day two sources disagree;
  III.C.1, feedback, on the revise day of a research product), or excluded with a reason in
  `data/progressions/library-excluded.csv`. Excluded, each owned instead by the subject named: V.B.1 and V.C.2
  (science and computer science design cycles), V.A.1 (ELA wide reading), V.D.1 and V.D.2 (SEL self-management),
  III.A.1 and III.D.2 (SEL relationship skills). Everything else is met through a research task. Pending(docs/agents/decisions/DESK-ANSWERS.md#q-prework-open-2)

## 5. Cross-subject leans

**Who teaches what first.** ELA owns the research cycle and the writing of it (core skill `research-cycle`; rows
`e1-shared-research` to `e12-research`), the first source list (grade 4, `e4-research`), locating print and digital
sources with key words (grade 5, `e5-locate-sources`), source credibility in writing (grade 6, `e6-short-research`)
and a standard citation format (grade 7, `e7-research-questions`). Social studies owns sourcing and corroboration
(`source-sourcing`, `corroboration`, from grade 2) and news reading (`ss8-news-literacy`, grade 8;
`us1-news-reading`, grade 11). Library owns what neither does: searching as a skill (changing a query, catalogues
and databases, choosing among results), leaving the page to check who is behind it (lateral reading, the first time
it is taught as a method), going upstream to the first source, honest use of others' work across media (not only in
writing), and choosing among tools. Where a library row meets an ELA or social studies skill it names that row in
`cross_subject` (for example `ela:e5-locate-sources`) and either assumes it or is assumed by it; the progression says
which came first in each grade. Before the progression is drafted, the 3 to 5 and 6 to 8 emphasis cells above are
re-read against ELA grades 4 to 7.

- **ELA:** the research writing standards W.7 and W.8 from kindergarten and W.9 from grade 4, and informational
  reading.
- **Social studies:** C3 dimension 3 (sources and evidence) and Massachusetts news and media literacy (NML), from
  grade 8 (`ss8-news-literacy`). Library owns the lateral reading method; social studies uses it on its sources.
- **Science:** no science progression row names judging information, so library names host investigations from the
  grade's science course instead of a skill id.
- **Computer science:** computer science owns how machine-made text tools work, in its own rows; library owns
  checking what they produce, and assumes no computer science row.
