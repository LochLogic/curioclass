# Library and research skills: the standard, made usable

**DRAFT, 2026-11-16.**

Written 2026-11-16 as the subject's pre-work (docs/PRODUCTION-PATH.md, "After the core subjects"; the owed row in
docs/ADOPTION-BAR-SUBJECTS.md, "Before a scope and sequence in this subject"). The model is
docs/courses/social-studies/STANDARD.md. Eight courses (section 3), course track `library`.
Decided: separate courses, our own bar, and they may be smaller: fewer minutes a week (one or two sessions, the frame
says which), never fewer units (Cory, 2026-11-11 and 2026-11-15).

## The owed row, and where it stands

| Owed | State | Where |
|---|---|---|
| Relabel the file to the second edition (2025) | Done 2026-11-11 (label in the header); edition confirmed at source 2026-11-16 | data/standards/aasl-2018.txt |
| Open the continuum's grade lists | Done 2026-11-16: the grades 3 to 5 list read in full; the other bands' structure seen | Section 2 |
| Name lags left in other files | Reported to the lead, not changed here | Section 1 |
| Approach page | Draft, waiting on Cory's yes | docs/courses/library/APPROACH.md |

## 1. The standard and its terms

- **Which:** American Association of School Librarians, National School Library Standards, second edition,
  learner framework (PDF dated 2025-09-18). Confirmed 2026-11-16 at standards.aasl.org, which presents the "Second
  Edition". Six Shared Foundations (I Inquire, II Include, III Collaborate, IV Curate, V Explore, VI Engage), each in
  four Domains (A Think, B Create, C Share, D Grow): 68 competencies, ids `AASL.I.A.1` style, unchanged from 2018.
- **Name lags (not this subject's files to change):** the file name aasl-2018.txt and the tag `AASL-2018` in
  scripts/standards.py and data/modules.csv stay as names (the file header says why). data/subjects.csv still labels
  the library row "AASL National School Library Standards (2018)": a label-only fix for the lead.
- **Terms** (standards.aasl.org/permissions, read 2026-11-16): one competency may be excerpted into a lesson or unit
  plan for non-commercial education; the whole framework or a substantial part needs ALA permission. So the repo holds
  ids and our own words, never the competency text, and pages never claim AASL alignment approved by anyone.
- **What it lacks:** AASL competencies are not set by grade. The same 68 apply K to 12. The bar's criterion 2 asks for
  named priority skills per grade, so a grade sequence must come from elsewhere.

## 2. The grade sequence: the Empire State Information Fluency Continuum as the check set

- **What it is:** a PK to 12 continuum by Barbara Stripling for New York City and New York State school libraries,
  hosted by Monroe One BOCES School Library System (libguides.monroe.edu/ESIFC; band files dated 2019). Four anchor
  standards (inquiry and design thinking; multiple literacies; social and civic responsibility; personal growth and
  agency). Inside the inquiry standard, six phases: connect, wonder, investigate, construct, express, reflect. Each
  phase has indicators with a cell per grade, and the priority skills for each grade are marked in bold and gathered
  in a "priority skills" box per phase.
- **Read 2026-11-16:** the grades 3 to 5 band file in full. Example of the grain, in our own words: grade 3 uses a
  teacher-given source for background and simple note-making; grade 4 picks an interesting part of a broad topic and
  compares primary and secondary sources the teacher chose; grade 5 judges which questions facts can answer, weighs
  print, video and online sources for relevance and builds a bibliography to a model. The PK to 2, 6 to 8 and 9 to 12
  files have the same shape (structure seen on the continuum page; not read cell by cell).
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

| Courses | AASL | Priority skill emphasis (ours, to be set at the progression) |
|---|---|---|
| K, 1 and 2 (one course each) | All six foundations, at the "with help" level | Asking a question, finding a book by its parts, retelling what a source says, saying where it came from, sharing with the class |
| 3, 4 and 5 (one course each) | All six | Key words, searching a catalogue and a chosen site, note-making, primary and secondary sources, a simple bibliography, first lateral checks of a site |
| Grades 6 to 8 (one course) | All six | Search strategy, lateral reading, judging evidence and who is behind it, paraphrase and quotation, citation in one style, fair use basics |
| Grades 9 to 12 (one course) | All six | Research question design, databases and open sources, lateral reading on hard cases, synthesis across sources, full citation, copyright, licences and fair use, sharing a research product |

**Partial bases for 6 to 12.** Settled 2026-11-16 (Cory, Desk card q-later-cs-career-library): the CC BY
online-reasoning lessons and the open web-literacy book named in docs/reviews/library-open-material-2026-11-16.md
are partial bases for the 6 to 8 and 9 to 12 courses. Only items under an open licence are adapted, in our voice,
with the source in the day's credit; no company or product name appears in student, teacher or family copy.

Every unit names host tasks from the grade's other courses (bar criterion 4): research for a science investigation, a
social studies source question, an ELA research piece.

## 4. What is left out, and why

- The AASL school librarian and school library frameworks: they describe adults and programmes, not learners.
- Reading promotion and literature appreciation (the continuum's multiple literacies standard) beyond what a research
  unit needs: ELA owns reading; library units may use the same books.
- The continuum's design thinking strand: science and computer science own design; library leans on them.

## 5. Cross-subject leans

- **ELA:** the research writing standards (W.7, W.8, W.9 at each grade) and informational reading. ELA owns the
  writing; library owns finding, judging and citing.
- **Social studies:** C3 dimension 3 (sources and evidence) and Massachusetts news and media literacy (NML) in high
  school. Library owns the lateral reading method; social studies uses it on its sources. Plans name who teaches it
  first so it is not owned twice.
- **Science:** gathering and judging information (NGSS practice 8).
- **Computer science:** SOC standards on privacy, data and AI-made content; AI output is a source to be checked.
