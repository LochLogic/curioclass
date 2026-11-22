# World languages: the standard, made usable

**World languages are SHELVED (Cory, 2026-11-11; restated 2026-11-20). This page is pre-work only and does not
unshelve anything.** It writes no frame, scope and sequence, unit, day or tool, and it changes no status anywhere.
DRAFT, 2026-11-20, written for the owed row "World languages (2)" in docs/ADOPTION-BAR-SUBJECTS.md ("Before a scope
and sequence in this subject") and the stage 1 list in docs/COURSE-RUN.md. Shape copied from
docs/courses/eld/STANDARD.md. Web facts below were read on 2026-11-20 unless marked "not checked" or "from memory".

| Owed (ADOPTION-BAR-SUBJECTS, world languages) | State | Where |
|---|---|---|
| Split each language into levels, with a target each | Option D chosen (Cory, 2026-11-21); catalogue rows drawn when the pass opens | Section 5 |
| Load the 2026 can-do statements after a licence check | Licence read; nothing loaded; paraphrase-only plan | Section 3 |
| Load American Sign Language standards | Sources found; nothing loaded | Section 4 |
| Decide the video source for American Sign Language | Already decided: graphics only, no video, no photos of people (Cory 2026-10-27) | APPROACH.md |
| Course count above 105 | Counted for each option | Section 5 |
| Approach page, lens, base-text scout | Approach approved as pre-work (Cory, 2026-11-21); lens and two scouts written | APPROACH.md; docs/agents/lenses/world-languages.md; docs/reviews/world-languages-open-material-2026-11-20.md; docs/reviews/world-languages-asl-material-2026-11-21.md |
| Strand id files (Spanish sounds and spelling; the seven ASL parameters) and the check entries | Spanish: data/standards/spanish-strands.txt, the gate entry and the progression (data/progressions/spanish.csv, 51 rows, written 2026-11-22). ASL: not made; it waits on question 4 (data/plans/later.csv L93) | Sections 1 and 6 |

## 1. The standard and its terms

- **Standards.** *World-Readiness Standards for Learning Languages*, 4th edition, 2015 (ACTFL). Five goal areas, 11
  standards: Communication (interpersonal, interpretive, presentational), Cultures (practices, products), Connections
  (making connections, acquiring information and diverse perspectives), Comparisons (language, culture), Communities
  (school and global communities, lifelong learning). Source: the ACTFL standards summary page and the two-page summary
  PDF, both read in full 2026-11-20 (links in section 7; the extracted text is from the Utah copy of the PDF). The 2015 summary is a framework with sample progress indicators in
  longer volumes; the longer volume was not opened (not checked).
- **Levels.** ACTFL Proficiency Guidelines, 2024 edition: Novice, Intermediate, Advanced, each split Low, Mid, High,
  then Superior and Distinguished (no sublevels). Confirmed in the 2024 proficiency guidelines, read 2026-11-22 (the
  copy Cory saved in S:\CurioClass-sources\world-languages\actfl-guidelines-2024\, read in full by an agent with his
  clearance): five major levels, Distinguished added in the 2012 edition, Low, Mid and High only for the first three.
  Each of listening, speaking, reading and writing is rated on its own. The guidelines' terms allow no copying of
  their text, so the repo holds level ids and our own words only.
- **The file.** data/standards/actfl-wrs.txt holds the 11 standard ids (`WRS.<goal area>.<n.n>`) and the 11 level names
  (`ACTFL.<level>`), ids only. It is unchanged by this pre-work.
- **Do the 2015 pages print the numbers 1.1 to 5.2?** Checked 2026-11-20: **no.** The two-page ACTFL summary PDF
  (text extracted) contains no such number, and the ACTFL standards summary page shows titles with no numbers. The
  numbers come from the 1999 edition (a side-by-side comparison on learner.org lists the 1999 Communication
  standards as 1.1 to 1.3 beside the 2015 modes) and state adaptations: Maryland's adaptation prints "Standards 1.1 -
  1.3" and splits interpretive and presentational into listening, reading, speaking and writing. This confirms the
  file's header note. Consequence: the ids in the file are our own labels in the 2015 order, and every public page
  names a standard by its title, not by "Standard 1.2". The numbered 2015 sub-parts used by states (the "sample
  progress indicators") were not read (not checked).
- **Reuse terms, checked at the source.**
  - ACTFL standards and guidelines pages carry "Copyright 2026 ACTFL" and no reuse licence on the standards summary
    page. So: titles, ids and our own words only. No standard statement or level description is copied. Public pages
    say "world language standards" and give the id; internal docs may name the source.
  - The standards themselves are for sale on ACTFL's site (the summary page links a purchase page).
  - The proficiency levels are a published scale; their descriptions are ACTFL's. We name the levels and write our
    own descriptions.
- **Check.** scripts/standards.py reads actfl-wrs.txt as a listed file (since 2026-11-21): all 22 ids pass, the 11
  numbered `WRS` ids and `ACTFL.Superior` and `ACTFL.Distinguished` included.

## 2. What is in the catalogue, and a mismatch to report

- data/courses.csv has three rows with subject `world-languages`: `spanish` (k-12, "Modules keyed by level not
  grade"), `french` (6-12, "Same level modules as Spanish; language-specific content added in Phase 2") and `asl` (k-12,
  "tools reviewed by Deaf educators before release"). None is core.
- The adoption bar part 6 and the owed row say **two** courses: Spanish and American Sign Language ("2 shelf foreign
  languages", ADOPTION-BAR-SUBJECTS, Decided, item 2; the course count line "120 courses, 2 world languages
  shelved"). The catalogue has **three**. French is the extra row. Cory's answer (question 2, "Cory's answers"):
  French may be added, listed behind Spanish and ASL; the bar's wording is corrected when the pass opens.

## 3. The 2026 can-do statements

- **What they are.** The *NCSSFL-ACTFL Can-Do Statements*, 2026 edition, from the National Council of State
  Supervisors for Languages and ACTFL, a set of learner statements by proficiency level and mode, with a
  self-assessment use. ACTFL's page names the 2026 edition; a 2026 ACTFL document describes the Superior and
  Distinguished statements as updated revisions of the 2017 set (search summary of the ACTFL Can-Do overview PDFs,
  not opened in full).
- **Licence, as stated on the ACTFL page (read 2026-11-20).** "Provided for educational and non-profit use only";
  "commercial use or sale is prohibited"; attribution to both NCSSFL and ACTFL requested. It is not a Creative Commons
  licence. The page does not name American Sign Language in the terms, though it counts signed conversation within
  the interpersonal mode.
- **What that allows us.** Curio Class is free and non-profit, but "non-profit use" is not a licence to republish
  or adapt text, and a planned donation catalog (from memory, docs/funding/) is a money question. So the standing
  call holds (DESK-ANSWERS, "Can-do and ACTFL statements ship as paraphrases with the note"): **our own paraphrases
  only, never the statements' text, each page carrying a note that they are our paraphrase of the NCSSFL-ACTFL
  can-do statements and not endorsed by either body, and a world-language teacher and a Deaf ASL teacher are asked
  to check them when a contact turns one up.** Nothing is loaded now: no copy of the 2026 text sits in the repo, and
  this pre-work did not download any. Cory sends one short note to NCSSFL and ACTFL asking whether paraphrase in a
  free tool set is acceptable (question 5; data/plans/later.csv L92), before any page uses a paraphrase.

## 4. American Sign Language: what standards exist

Search only; nothing downloaded; links in section 7.

- **K-12 ASL Content Standards** (Clerc Center, Gallaudet University; developed 2014 to 2017 with a consortium and
  the California School for the Deaf at Fremont, per the search summary). Written for **students learning ASL as a
  first language** (academic ASL); the search summary describes five anchor standards with grade-level benchmarks.
  The Clerc Center page returned a 403 when fetched, so the licence and the structure are **not checked**. It is the right fit for Deaf children
  who sign from home, not for a hearing child learning ASL as a second language.
- **Standards for Learning American Sign Language** (ASLTA, 2014), cited in the Massachusetts ASL framework guidance.
  Structure and licence not seen (not checked).
- **State ASL second-language standards built on the World-Readiness Standards.** Indiana's 2026 Academic Standards
  for World Languages: ASL (K-12 and secondary versions), Massachusetts's ASL framework quick-reference (both found by
  search; not opened in full). They organise by the five goal areas and grade bands (Indiana K-2, 3-5, 6-8, 9-10, 11-12).
  This shows the World-Readiness frame is the working standard for ASL as a second language in the United States.
- **Our reading.** For ASL as a second language use the same standards file as Spanish (the 2015 interpersonal mode text
  itself says "signed"), the ACTFL level scale (ACTFL has applied its guidelines to ASL; from memory, not checked) and
  our own ASL strand of parameters (handshape, location, movement, palm orientation, non-manual markers, use of
  space, classifiers: bar part 6, item 9). A Deaf first-language path (the Clerc standards) is a separate course
  idea, out of scope (section 8). Cory chose this reading (question 3, "Cory's answers").
- **Culture and people.** Sources agree Deaf culture belongs in ASL teaching; the Illinois Association of the Deaf
  (2018) states a strong position that Deaf and native ASL users should teach ASL and that hearing teachers replacing
  them is cultural appropriation (found by search; position text not read in full). It bears on who reads and
  checks our ASL pages. See APPROACH.md, "Sensitive ground", and question 4 (still open, data/plans/later.csv L93).

## 5. How the standard maps to the courses

**Levels, not grades.** The bar says "Modules keyed by level not grade" (courses.csv) and "each level names a target
proficiency level" (part 6, item 1). A learner of any age starts at the first level. Under Option D (below) a young
learner takes the early-years companion of Level 1 or 2, which targets the same level as the main course in listening
and speaking, and in reading and writing goes only as far as the child reads and writes in any language (copy and
label) (Cory, 2026-11-22, Desk q-prog-spanish-1); which
grades take a companion is set with the catalogue rows when the pass opens (heritage and age notes in APPROACH.md). Hours decide the pace: a student cannot meet an Intermediate target in a year of 90 minutes a week
(the span is large; ACTFL's own time figure and a hours-to-proficiency lead are in APPROACH.md, "Pacing").

**Options for the split. The split is Cory's call when the pass opens; nothing here decides it.**

| Option | Per language | Courses, Spanish plus ASL (net of the 2 shelved rows in brackets) | Notes |
|---|---|---|---|
| A. Three ranges | Novice, Intermediate, Advanced; Low, Mid, High become units inside each course | 6 (+4) | Fewest courses. Each course very large, so it breaks the bar's "one course for all levels" fail only by degree. Advanced is not reachable in a K to 12 setting without immersion, so the third course would be thin. |
| B. Four levels | Level 1 Novice Low to Mid; Level 2 Novice High; Level 3 Intermediate Low to Mid; Level 4 Intermediate High. Advanced is a stated "beyond" | 8 (+6) | Matches what most school programmes reach. Each course states a target sublevel as an exit target. |
| C. Five levels | Novice Low-Mid, Novice High, Intermediate Low-Mid, Intermediate High, Advanced Low | 10 (+8) | Finest. Heaviest build. |
| D. B plus an early-years form | Option B, with an elementary form of Level 1 and 2 (play, song, movement tasks, small texts), both targeting the same level | 8 plus 4 early-years companions (+10 net, 12 in all) | Honest about age. Most work. |

Adding French at the same levels adds 4 (B) courses. The counts above are net of the 2 shelved rows. Which catalogue
total is current (the plan's 105 active, or the bar's own line of 118 active) is not settled on this page; the pass
states it from data/courses.csv when it opens. Under Option D, data/courses.csv gets 12 rows for Spanish and ASL
(four levels and two early-years companions each) in place of the two all-level rows; their ids and grade ranges are
drawn when the pass opens. French is listed behind Spanish and ASL (Cory's answers) and stays one row until then.

**Cory chose Option D** (2026-11-21, Desk q-prework-open-2): four levels per language plus an early-years
companion for Levels 1 and 2, 12 courses for Spanish and ASL, settled for when the pass opens. The recommendation had
been Option B, for a stated target per course, near what a school can staff, with Advanced
left for a later pass; Option D keeps all of that and adds the companions. Each course's exit target is a sublevel (Level 1 exits at Novice Mid, Level 2 at
Novice High, Level 3 at Intermediate Low, Level 4 at Intermediate Mid; writing aims one sublevel lower at Levels 3
and 4). The full preterite and imperfect contrast and the productive subjunctive are beyond Level 4, met at Level 4
only as chunks (Cory, 2026-11-22, Desk q-prog-spanish-1: an aim a school can reach in about 63 hours a level; fewer
lessons are acceptable where rigor and quality hold). These four exits are ours. The 2024
proficiency guidelines (read 2026-11-22) describe each sublevel and fit this order, but give no hours, years or
school program norms, so they neither confirm nor rule out any of the four; the program norms they were first drawn
from are not in the guidelines and stay not checked. The reading supports three limits: a course checks performance
on taught, rehearsed themes, which the guidelines say can run ahead of proficiency in unrehearsed use; the classroom
performance scale has major levels only, so a sublevel exit is the proficiency estimate a course aims toward, never
a rating our checks give; and a learner can sit at different sublevels in listening, speaking, reading and writing,
so the exit is stated per mode.

**Standards by course.** All 11 World-Readiness standards apply at every level: Communication's three modes are taught
and assessed in every unit (bar part 6, item 6). Cultures, Connections, Comparisons and Communities enter through the
unit theme and task. Communities 5.1 (school and global) and 5.2 (lifelong learning) are the least reachable from a
free site without people in the room: bar part 6, "Unsupported": two-way practice happens between people in the room.
Every course page and family note names the part of 5.1 not claimed (use of the language with communities beyond the
school), and Levels 3 and 4 offer an optional, never required activity the school arranges, never through the site (a
class-to-class letter exchange, or a guest the school invites) (Cory, 2026-11-22, Desk q-prog-spanish-1).

## 6. Ownership rule a progression writer could use later

A **level owns** a skill, not a grade. In a progression for this subject (Spanish: data/progressions/spanish.csv, 2026-11-22; ASL: none, waiting on question 4, data/plans/later.csv L93), each row sits at the
level where the learner first does it at its target depth, and later levels carry it as `~` with a one-line note on what
is harder (the ELD pattern, docs/courses/eld/STANDARD.md section 2). Specifically:

- A row is one (language, level, standard, mode or strand) cell. Ids: the 11 `WRS` ids plus the language strand rows
  we add (sounds and spelling for Spanish; the seven ASL parameters for ASL). Level owner: the first level whose
  target sublevel needs it.
- Each mode of Communication is owned by Level 1 and carried to the top, each time with a harder function, context,
  text type and control (bar part 6, item 2).
- The gate "no skipped grade" becomes "no skipped level", and "grade" becomes "level" in the handoff text.
- **Ownership for the gate** (from the cold read, docs/reviews/prework-world-languages-read-2026-11-20.md; ours, untested). Each language is its own subject key in
  the progression (`spanish`, `asl`), so each owns the 11 `WRS` ids once. A WRS id is owned by Level 1 of that
  language as "met at Novice depth"; Levels 2 to 4 carry it as `~ID` with a one-line note naming the harder function,
  context, text type and control (the depth ladder, which is the real progression; the 2024 guidelines were read at
  source 2026-11-22, and the ladder is the "Harder than Level N" note on each row of data/progressions/spanish.csv). An early-years companion targets the same level
  as its Level 1 or 2 course (Option D), so it uses that level's rows. The 11 `ACTFL.*` level ids are
  excluded with the reason "a proficiency scale used to name each level's exit target, not a skill". Strands (sounds
  and spelling; the seven ASL parameters) get their own id file, one id each, owned by the level that first teaches
  them. For the gate, Level 1 to Level 4 map to positions 1 to 4 in a level list that replaces the grade list for
  these two subjects (Cory, 2026-11-21).
- **What scripts/progression.py does** (Spanish entry added 2026-11-22; the rules are in its docstring): subject key
  `spanish`, file data/progressions/spanish.csv (51 rows, with spanish-edges.md beside it), anchors actfl-wrs.txt and
  data/standards/spanish-strands.txt (SPA.Sounds.1 to 11, ours), the 11 `ACTFL.*` ids listed in
  data/progressions/spanish-excluded.csv, the level list L1 to L4 in the grade column with skill ids starting l1- to
  l4-, and the lean rule below in place of the grade comparison. ASL has no entry; it waits on question 4 (data/plans/later.csv L93).
- **Cross-subject leans** (each names a core skill; ids checked 2026-11-20 by a one-line grep for a row whose
  skill_id column matches, in data/progressions/*.csv):
  - ELA: `ek-discussion` and `e3-word-strategies` (a spoken exchange and word-part work), `e5-figurative` (Level 3 and 4
    texts), `e6-word-strategies`, `e9-sl-presentation` (a presentation), `e2-sentences` (what a sentence is).
  - Social studies: `ss2-culture-migration`, `ss3-home-region`, `ss4-regional-cultures`, `ss2-nation-of-immigrants`,
    `us1-immigration` (the Spanish progression uses neither, to keep tasks off immigration; spanish-edges.md lists the leans in use), `wh1-geography-shapes-contact`.
  - Psychology: `psy-language` (language acquisition), an elective, only as a later cross-link.
  The lean is a pointer for the teacher, not an assumption: a language level is not placed behind a grade of any
  of these. A lean names a core skill and the earliest grade at which a typical learner meets it; the unit never
  assumes it. A lean to a skill of grade 6 or later is allowed only from Level 3 or 4 units (the gate checks this for
  Spanish rows). `psy-language` is a later
  cross-link and not part of the gate.

## 7. Sources read (by link)

- ACTFL standards summary: https://www.actfl.org/educator-resources/world-readiness-standards-for-learning-languages/standards-summary
- ACTFL two-page summary PDF (Utah copy): https://www.schools.utah.gov/curr/worldlanguages/utahcorestandards/WorldReadinessStandardsLearningLanguages.pdf
- 1999 and 2015 comparison: https://www.learner.org/wp-content/uploads/2019/10/teaching-foreign-languages-standards-five-cs-standards-comparison.pdf (search snippet only)
- Maryland adaptation: https://marylandpublicschools.org/about/Documents/DCAA/World-Languages/MDWorldReadinessStandardsLearningLanguages.pdf (search snippet only)
- Can-do statements page: https://www.actfl.org/educator-resources/ncssfl-actfl-can-do-statements
- ACTFL Proficiency Guidelines 2024 and the levels chart: read in full 2026-11-22 from Cory's saved copy (S:\CurioClass-sources\world-languages\actfl-guidelines-2024\); the ISBE copy (https://www.isbe.net/Documents/ACTFL-Proficiency-Guidelines-2024.pdf) now returns a 404
- Clerc Center K-12 ASL Content Standards: https://clerccenter.gallaudet.edu/resources/asl-content-standards/ (403 when fetched)
- Indiana ASL standards 2026: https://secure.in.gov/doe/files/2026-Indiana-Academic-Standards-World-Languages-ASL-K-12.pdf (search only)
- Massachusetts ASL guidance: https://www.doe.mass.edu/worldlanguages/framework/qrg-asl.docx (search only)
- Illinois Association of the Deaf position on ASL instructors: https://iadeaf.org/position-statement-on-american-sign-language-instructors (search only)

## 8. Left out, and why

- **French.** In the catalogue but not in the bar (section 2). No French pre-work is written.
- **Languages beyond these** (Mandarin, Arabic and others): not in the catalogue.
- **A Deaf first-language ASL course** (the Clerc standards): a different learner and a different course.
- **Placement and proficiency testing:** the school's, as for ELD. Curio Class gives no oral proficiency interview, keeps
  no recordings and no scores (FOUNDATION promise 2).
- **Two-way live practice:** between people in the room; the site cannot give it (bar part 6, Unsupported).
- **Video for ASL:** decided, not planned (Cory 2026-10-27).
- **Immersion, study abroad, exchanges, pen pals:** out of scope for a free site.

## Cory's answers (2026-11-21, Desk q-prework-open-2)

World languages stay shelved; these answers settle the pre-work pages only.

- Level split: Option D, four levels plus an early-years form (section 5).
- French: it can be added, listed behind Spanish and ASL. The bar's wording is corrected only when the pass opens.
- Ownership: each language its own progression (section 6).
- ASL standard: World-Readiness and the ACTFL scale, plus our parameters strand; Clerc noted only.
- Who checks ASL pages: no answer yet (question 4 stays open).
- Time: three sessions a week of 35 minutes, 36 weeks, about 63 hours a level (APPROACH.md, "Pacing and dose").
- Early start: an early-years companion now, as part of Option D.
- Heritage speakers: a path inside each Spanish level.
- Can-do statements: paraphrase only, with the note; Cory sends one short note to NCSSFL and ACTFL asking whether
  paraphrase in a free tool set is acceptable (data/plans/later.csv).
- Base text: yes for Spanish (open college-level books for reference and sequence); the ASL research is done again
  (docs/reviews/world-languages-asl-material-2026-11-21.md).
- Approach page: yes, as pre-work.

## Questions for Cory (as asked)

Kept as a record. All were answered 2026-11-21 ("Cory's answers", above) except question 4 (later.csv L93); where an
answer differs from the recommendation below (questions 1 and 8: Option D), the answer holds.

1. **Level split.** Recommended: Option B, four levels per language with a sublevel exit target each (Novice Mid,
   Novice High, Intermediate Mid, Intermediate High). Alternatives A, C, D in section 5.
2. **French and the count.** The bar says two language courses and the catalogue has three. Recommended: keep French
   parked behind Spanish in the same level shape, and correct the bar wording to "three" only when the pass opens.
3. **Which ASL standard to load.** Recommended: the World-Readiness standards and the ACTFL scale for ASL as a second
   language, with our own parameters strand, and the Clerc first-language standards noted only (not loaded).
4. **Who checks ASL pages.** Recommended: no public ASL page before a Deaf ASL teacher has read it; until one is found,
   the work stays in the pre-work stage. The self-built agent read alone is not enough for ASL.
5. **Can-do licence.** Recommended: paraphrase only, with the note (the standing call), and one short written request to
   NCSSFL and ACTFL asking whether paraphrase in a free tool set is acceptable, sent by Cory, since the licence is
   non-commercial and the donation catalog is a money matter.
6. **Heritage speakers.** Recommended: a path inside each Spanish level (more reading and writing, less first-word work),
   not a separate course.
7. **Time.** Recommended: 36 weeks a year, three sessions a week of 35 minutes, about 63 hours a level (Levels 1 to
   4), with no claim that the hours reach the exit targets (APPROACH.md, "Pacing and dose").
8. **Early start.** Should children in K to 5 start at Level 1 as the same course, or have an early-years companion
   (Option D)? Recommended: the same course with an age note, and an early-years form later.
9. **Approach page yes.** Recommended: yes to the draft in APPROACH.md, after Questions 4 and 6.
10. **Base text.** Recommended: use the open college-level Spanish books for reference and sequence, adapt item by item
    only where licence and age fit (open-material scout), and for ASL write our own, because no CC BY ASL course was found.
11. **Ownership form.** Recommended: each language its own progression, Level 1 owns the 11 WRS ids, the level
    names excluded as a scale (section 6). Or one shared progression with two owners per id?
