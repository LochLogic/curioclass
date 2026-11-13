# Social studies: the standard, made usable (pre-work P1)

Written 2026-11-13 for docs/PRODUCTION-PATH.md pre-work P1a to P1e. The decision is Cory's (DESK-ANSWERS
2026-11-12 and 2026-11-13): option (d), C3 for skills, Massachusetts 2018 as the content anchor in Massachusetts's
course order, checked unit by unit against a named few, Curio Class's own year in place of the anchor's
own-state year, under the values rule. This page records what was done to make it usable. The paper behind it is
docs/reviews/social-studies-content-standard-2026-11-12.md.

| Piece | State | Where |
|---|---|---|
| P1a. Load the anchor | Done | data/standards/ma-hss-2018.txt (ids and our own words), checked by scripts/standards.py |
| P1b. Redraw the course list | Done 2026-11-13 (Cory's yes on Desk card q-ss-course-list, with the lead's high school pick) | Section 2 below; data/courses.csv |
| P1c. Name the check states | Done (the lead names them, per PRODUCTION-PATH) | Section 3 |
| P1d. Design the replaced year | Draft done, read in its turn | docs/courses/social-studies/grade-3-outline.md |
| P1e. Psychology and electives | Done: psychology after the core | Section 4 |

## 1. The anchor file (P1a)

- data/standards/ma-hss-2018.txt holds every Massachusetts 2018 content standard from kindergarten to the high
  school courses, with its lettered parts, as `MA.<code><TAB>our own words`. Codes follow the framework's own
  topic codes: `MA.3.T2.3b`, `MA.USI.T5.2`, `MA.WHII.T4.10c`, and for the high school standards whose topic codes
  repeat across sections, a section prefix: `MA.GOV.T3.1` (Government and Politics), `MA.ECON.T2.4` (Economics),
  `MA.PFL.T1.2` (Personal Financial Literacy), `MA.NML.T4.1` (News/Media Literacy).
- Topic and sub-topic headings have lines of their own (`MA.6.T3b`), so a course frame can cite a topic.
- Not loaded: pre-kindergarten; the seven practice standards (C3 carries the skills); the literacy standards
  (drawn from the Massachusetts ELA framework, which matches the CCSS ELA file we already hold).
- Terms: the framework permits copying any part for non-commercial educational purposes with credit to the
  Massachusetts Department of Elementary and Secondary Education. Curio Class pages are CC BY, so the file stores
  ids and our own words, never the framework's sentences, as with CCSS. Credit is in the file header.
- Massachusetts's own Investigating History units (grades 3 to 7) are CC BY-NC: reference only, never adapted.
  Copies of both are in S:\CurioClass-sources\reference-only-do-not-copy\massachusetts-hss-2018\.

## 2. The course list, redrawn to Massachusetts's order (P1b, done)

The old list was California's order. Under the anchor it became the list below (in data/courses.csv since 2026-11-13). The elementary
course stays one row by grade (`ss-k5`), as now.

| Grade | Course (proposed title) | Massachusetts source | Core | Change from today | Today's course id |
|---|---|---|---|---|---|
| K | Kindergarten: Living and Learning Together | K.T1 to K.T4 | yes | Content follows the anchor | ss-k5 |
| 1 | Grade 1: Leaders, Helpers and Communities | 1.T1 to 1.T4 | yes | Content follows the anchor | ss-k5 |
| 2 | Grade 2: Places and Peoples of the World | 2.T1 to 2.T5 | yes | Now a world geography year | ss-k5 |
| 3 | Grade 3: Communities Then and Now | Curio Class's own year (grade-3-outline.md); 3.T1 and the skills of 3.T2 kept in general form | yes | Replaces the anchor's Massachusetts year | ss-k5 |
| 4 | Grade 4: North America, Its Land and Peoples | 4.T1 to 4.T4e | yes | Was state history and government | ss-k5 |
| 5 | Grade 5: The United States to the Civil War, and the Fight for Civil Rights | 5.T1 to 5.T5 | yes | Grows past the Constitution | ss-k5 |
| 6 | World Geography and Ancient Civilizations I | 6.T1 to 6.T5c | yes | Becomes the first of two years | world-geo-6 (kept) |
| 7 | World Geography and Ancient Civilizations II | 7.T1 to 7.T4c | yes | Was medieval to early modern | world-hist-7 (id kept) |
| 8 | Civics: Government and Civic Life | 8.T1 to 8.T7 (8.T6, Massachusetts government, taught as "your state") | yes | Was US history to 1877 | us-hist-8 (id kept) |
| 9 | World History I (about 500 to 1800) | WHI.T1 to WHI.T6 | yes | New course | world-hist-hs (id kept) |
| 10 | World History II (about 1800 to today) | WHII.T1 to WHII.T7 | yes | New course | world-hist-2 (new) |
| 11 | US History I (1763 to World War I) | USI.T1 to USI.T7 | yes | New course | us-hist-1 (new) |
| 12 | US History II (the 1920s to today) | USII.T1 to USII.T5 | yes | New course | us-hist-hs (id kept) |
| 11 to 12 | US Government and Politics (half year) | GOV.T1 to GOV.T5 | yes | Little change | government (kept) |
| 11 to 12 | Economics (half year), with personal finance | ECON.T1 to ECON.T7, PFL.T1 to PFL.T4 | yes | Adds the personal finance standards | economics (kept) |
| 11 to 12 | Psychology | APA, after the core (section 4) | no | None | psychology (kept) |

- News/media literacy (NML) has no course of its own: grade 8 carries 8.T7, and NML.T1 to T5 are placed in the
  high school courses' unit plans.
- Core social studies courses go from 13 to 15 (World History and US History each become two). The Desk's plan
  flow counts them from data/courses.csv, so it grows when the list changes.
- The high school grades were the lead's pick, which Cory took (2026-11-13). Massachusetts fixes no high school grade. Pick:
  World History I and II in 9 and 10, so world history runs on from grade 7 (which ends about 500) without a
  gap; US History I and II in 11 and 12, the most common place for US history; Government and Economics as half
  years for grades 11 and 12. Alternative: US History I and II in 9 and 10 (the framework says US History I
  builds on grade 8 civics) and world history in 11 and 12. Either way the content is the same.
- Done after the yes (2026-11-13): data/courses.csv redrawn with every old course id kept (URLs and closet keys
  use them) and two new ids, world-hist-2 and us-hist-1. 46 topics moved to the course and grade where their
  content now sits, rewritten in place, and their D-code grade bands relabelled. Each moved topic keeps its first
  module id (data/modules/kept-ids.csv, read by scripts/build_db.py and scripts/add_codes.py), because word walls,
  media and tool files point at those ids. The 153 worksheets of the moved topics moved with them to new row
  numbers at the end of their new unit (docs/worksheets/social-studies.md; generated.csv follows).
- Some redrawn courses are thin until their scope and sequence is written (us-hist-8 civics 13 worksheets,
  world-hist-hs 17, us-hist-hs 28; grade 2, 4 and 5 topics also need new ones). scripts/check_worksheets.py
  prints these as notes, not problems. Saved for later as L8.

## 3. The check set (P1c)

Each unit plan is read against these, and anything a strong set treats as essential that the anchor leaves out
or teaches thinly is added inside the year's days, with its source recorded.

| Check set member | Why | Edition | Reuse |
|---|---|---|---|
| California | Rated A- in civics and US history (Fordham 2021); fullest grade-by-grade content | Standards 1998, framework 2016 | Read only; ids and our own words if ever cited (CDE needs permission to reproduce) |
| Tennessee | Rated A-; newest revision; has economics, government and psychology standards | 2024 revision (in classrooms 2027-28) | Read only; terms not confirmed |
| New York | A- in US history; its high school order matches the common national pattern | Framework 2014 (K-8 revised 2016, 9-12 2017) | Read only; NYSED terms allow educational use with credit, not commercial use. On disk: S:\CurioClass-sources\reference-only-do-not-copy\new-york-ss-toolkit |
| The college-level course frameworks (grades 9 to 12 only) | The working high mark for high school content | Current editions | Read only; never named in student, teacher or family copy |
| Educating for American Democracy Roadmap | National history and civics guide built by about 300 scholars | 2021 | Read only |
| Subject references | Economics: CEE Voluntary National Content Standards (2010); geography: Geography for Life, 2nd edition (2012) | As named | Read only |

Three states, not more: each added state is another full read per unit, and the paper found these the strongest
sets with the clearest fit. Alabama 2024 and District of Columbia 2023 were strong in their older editions but are
unrated in their new ones; they can join if a unit's check finds a gap the three do not settle.

## 4. Psychology and the other electives (P1e)

- **Psychology** is not core (data/courses.csv) and the core subjects come first (Cory, 2026-11-13). It waits for
  the after-the-core stage. Its standard is the APA National Standards for High School Psychology Curricula,
  third revision, approved by the APA Council in February 2022 (confirmed from secondary sources; apa.org blocks
  automated reading, so the file is loaded by hand when psychology's turn comes: Cory saves the PDF, the lead
  writes ids and our own words).
- **Government and Economics** are core here although Massachusetts calls them electives, because a civics and an
  economics course is what most states require for graduation. Their standards are in the anchor file.
- **Personal finance** sits inside Economics (PFL), and NSPFE 2021 stays cited where topics already use it.
