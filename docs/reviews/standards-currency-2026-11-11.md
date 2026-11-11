# Are the loaded standards the current published editions?

Check date: 2026-11-11. Scope: every file in data/standards/, plus the code systems used in data/subjects.csv
(primary_standards) and data/modules.csv (standards and frameworks columns). This is a currency check, not a
quality review. Nothing here says Curio Class was reviewed by, meets, or is endorsed by anyone.

How to read it:

- **Verified** means the publishing body's own page or file was opened today.
- **Search result only** means a web search snippet was read and the page was not opened.
- **From memory, not verified** is said wherever it applies.
- Module counts come from the frameworks column of data/modules.csv (797 modules), counted by script today.
- Short answer: **no loaded file is a superseded edition.** Three are current but incomplete, two carry a wrong or
  stale label, and three review instruments the bar would rest on are keyed to older editions than the ones loaded.

## Summary

| File | Loaded edition | Current edition | Verdict | Modules affected |
|---|---|---|---|---|
| aasl-2018.txt | AASL learner framework, 68 competency ids, counted against both the 2018 and second edition PDFs | Second edition, published September 2025 (verified) | Current ids, stale label ("2018") | 18 (label only) |
| actfl-wrs.txt | World-Readiness Standards 4th ed. (2015), 11 standards; ACTFL proficiency sublevels (2024 Guidelines) | Same (verified). Can-Do Statements moved to a 2026 edition, not loaded. ASL has its own standards, not loaded | Current but incomplete | 28 tags on world language modules (9 World-Readiness, 19 ACTFL) |
| c3-indicators.txt | C3 Framework 2013 (2017 PDF), 283 indicator ids | 2013; no revision found (NCSS page blocked) | Current, not fully verified | 135 (none need change) |
| casel-5.txt | CASEL 5, page as of 2026-10-27, 40 sub-skill ids (numbering is ours) | 2020 update is still the live framework (verified) | Current | 17 (none) |
| ccss-ela-standards-full.txt | CCSS ELA 2010, 868 lines with full text | 2010; no revision (verified) | Current | 163 (none) |
| ccss-ela-standards.txt | CCSS ELA 2010, 455 ids | Same | Current | same 163 |
| ccss-math-clusters.txt | CCSS Math 2010, 147 cluster ids | 2010; no revision (verified) | Current | 137 (none) |
| ccss-math-focus.csv | Student Achievement Partners focus documents, 2013 to 2014 | Not rechecked today | Cannot tell (no sign of change) | 137 (none) |
| ccss-math-standards.txt | CCSS Math 2010, full text | Same | Current | same 137 |
| csta-2026-ids.txt | 196 ids, no header. They are exactly the PK-12 Foundational Standards of the 2026 CSTA standards (verified by matching against the PDF) | 2026 CSTA PK-12 Computer Science Standards, published summer 2026 (verified) | Current but incomplete: no header, no wording, 135 high school Specialty standards absent | 67 (none renumbered; 9-12 is where the gap bites) |
| cte-career-clusters-2024.txt | 2024 modernized framework: 14 clusters, 72 sub-clusters, 12 practices (numbers only) | Same (verified) | Current but incomplete (practice wording never read) | 8 (none) |
| hecat-topics.txt | HECAT 2021 topics and 81 Healthy Behavior Outcomes | 2021 is still the current HECAT (verified) | Current, but keyed to the 2007 health standards, not the loaded 2024 set | 0 (no module carries a HECAT code) |
| ncas-performance-standards.txt | National Core Arts Standards 2014, 1,202 ids | 2014; a national review began February 2025, no revised text yet (verified) | Current; revision in progress | 74 (none yet) |
| ngss-pes.txt | NGSS 2013, 208 performance expectation ids | 2013; no revision announced (verified) | Current | 110 (none) |
| nhes-2024.txt | SHAPE America National Health Education Standards 2024, 172 indicator ids | Same (verified). A second set with the same title exists (2022, a different body) | Current; header credits the wrong body | 21 (none renumbered) |
| nspfe-2021.txt | National Standards for Personal Financial Education 2021, 379 outcome ids | 2021 (verified) | Current | 14 (none) |
| shape-pe-2024.txt | SHAPE America National Physical Education Standards 2024, 210 indicator ids | Same (verified) | Current; the federal analysis tool is keyed to the older five standards | 12 (none renumbered) |
| wida-2020.txt | WIDA ELD Standards Framework 2020, 104 language expectation ids | 2020 (verified) | Current | 22 (none) |

Not in data/standards/ at all: four frameworks used in data/modules.csv have no file (AP Precalculus 7 modules,
AP Statistics 6, AP Calculus 6, APA high school psychology 7). Their currency was not checked. See the end.

## What the modules actually cite

Knowing the grain matters, because it decides whether an edition change would move codes.

- Fine-grained codes (an edition change would hit module rows): CCSS math and ELA, NGSS, C3, CSTA.
- Coarse codes only (standard, anchor, topic or competency level): NCAS anchors (for example VA:Cr1), SHAPE.S1 to
  S4, NHES.S1 to S8, AASL shared foundation names, CASEL competency names, NSPFE topic names, WIDA.ELD-1 to 5 and
  the four key language uses, WRS goal areas, ACTFL proficiency sublevels, CTE.Career Clusters and
  CTE.Career Ready Practices.
- So for every subject outside math, ELA, science, social studies and computer science, a wording change inside an
  edition changes what a course should teach without changing a single code in data/modules.csv. That is why the
  edition label on each file matters more than the ids.

---

## Detail per file

### aasl-2018.txt

1. **Loaded.** 68 learner competency ids (AASL.I.A.1 style), no wording. The header already records that the
   counts were taken from both the 2018 PDF and the second edition PDF and are the same in each cell, and that the
   second edition rewords some competencies (it names I.A.2) but keeps the numbering.
2. **Current.** Verified at standards.aasl.org: the site now presents the second edition ("A New Edition for a
   Changing World") and links a learner framework PDF dated 2025-09-18. The American Library Association press
   release of 2025-09-02 (opened) announces publication and says the core frameworks remain intact, with the
   supporting text sharpened and new material on competency-based learning. Neither page lists the changes line
   by line. I did not recount the second edition PDF myself; the count rests on the file header.
3. **Verdict.** Current ids, stale label. The file name, the frameworks tag "AASL-2018" and the subjects.csv entry
   "AASL National School Library Standards (2018)" all name the first edition.
4. **What updating touches.** Labels only: 18 modules tagged AASL-2018 (library 13, social studies 3, ELA 1,
   computer science 1; course ids library, ss-k5, us-hist-8, government, ela-k12, cs-k12), the library row in
   data/subjects.csv, the "AASL-2018" pattern in scripts/standards.py (line 101) and docs/PHASE1-SCOPE.md. No code
   is renumbered. Meaning: small. Modules cite shared foundations by name (Inquire, Include and so on), which did
   not change. Any tool spec that quotes a competency sentence should be reread against the second edition.
5. **Licence.** (c) American Library Association. The permissions page (opened) allows use, copying and
   distribution for private, non-commercial and educational purposes, allows excerpts that show how the standards
   apply, and requires permission to post the PDF itself or to reproduce the whole framework or a large part of it
   in a derivative work. Ids only, as now, is safe. Do not store the full competency text in the repo without
   asking.

### actfl-wrs.txt

1. **Loaded.** Two short lists: the 11 World-Readiness Standards (4th edition, 2015) by goal area, and the ACTFL
   proficiency sublevels (2024 Guidelines). Ids and titles in the header, no descriptors. The header admits the
   1.1 to 5.2 numbering is convention and is not printed in the 2015 summary.
2. **Current.** Verified at actfl.org: the World-Readiness Standards page still cites the 4th edition (2015), five
   goal areas, 11 standards, no revision announced, and says the standards apply to American Sign Language and to
   classical languages. The Proficiency Guidelines page lists the 2024 Guidelines as the latest. The
   NCSSFL-ACTFL Can-Do Statements page shows a **2026 edition**, aligned to the 2024 Guidelines, with a PDF
   comparing 2017 and 2026 (not opened).
3. **Verdict.** Current but incomplete. Two things are missing rather than out of date:
   - The Can-Do Statements are not loaded in any edition. The source search today names them as the natural
     ladder for unit objectives. If they are loaded, load 2026, not 2017.
   - ASL. The ASLTA site (opened) lists two separate sets: Standards for Learning ASL (K-16, published with ACTFL,
     aligned to the five Cs) and K-12 ASL Content Standards from the Laurent Clerc National Deaf Education Center
     (for ASL as a first or heritage language). Neither is loaded. The page gives no year; search results date the
     first to 2012 or 2014 (search result only, the two sources disagree).
4. **What updating touches.** 28 tags, all in world languages (course ids spanish and asl; grade bands k-12, 6-12,
   9-12). No codes would be renumbered. Meaning could change for ASL: the ASL courses are coded only to the
   general goal areas and proficiency levels, so nothing in the data says what an ASL course must cover that a
   Spanish course does not (handshape and other sign parameters, use of space, Deaf culture). Adding the ASL
   standards would add content expectations, which is a change in what the ASL course teaches.
5. **Licence.** (c) ACTFL; the full World-Readiness Standards are a paid book and the two-page summary is free
   to members. Can-Do Statements: educational and non-profit use only, no commercial use, credit both NCSSFL and
   ACTFL (verified on the page). Ids and titles are safe. Do not store the full Can-Do text without checking the
   terms in the 2026 file itself.

### c3-indicators.txt

1. **Loaded.** 283 indicator ids with grade band suffix, taken mechanically from the NCSS PDF (2013 framework,
   June 2017 revision that added the religious studies supplement). No wording.
2. **Current.** The NCSS page refused the fetch today (403). A web search found no announced revision for 2024 to
   2026, and NCSS marked the tenth anniversary in 2023 without a new edition (search result only). From memory, not
   verified: the 2013 text with the 2017 supplement is still the published framework.
3. **Verdict.** Current, with the caveat that the publisher's page was not opened today.
4. **Nothing to update.** 135 modules (social studies 123, library 6, CTE 4, ELA 1, science 1).
5. **Licence.** The PDF itself says the text and excerpts may be freely reproduced without asking NCSS (read in
   today's source search). Full statements could be stored.

### casel-5.txt

1. **Loaded.** The five competencies with 40 sub-skills. The numbering is ours (CASEL publishes none) and the
   sub-skill phrases are written out in the header notes.
2. **Current.** Verified at casel.org: the framework page refers to the 2020 update, links the PDF labelled
   11-2020, lists the same five competencies, and announces nothing newer.
3. **Verdict.** Current.
4. **Nothing to update.** 17 modules (SEL 10, health 7), all at competency level.
5. **Licence.** (c) CASEL, all rights reserved. The terms of use (opened) allow personal, non-commercial access
   and require prior written permission for other copying, posting or distribution. **Flag:** the header of this
   file holds the sub-skill phrases close to CASEL's own wording, in a public repo. Either shorten them to our own
   words or ask CASEL (info@casel.org).

### ccss-ela-standards-full.txt and ccss-ela-standards.txt

1. **Loaded.** Common Core ELA 2010. The first file is the full text (455 standards plus 413 lettered parts),
   extracted from the official PDF; the second is the 455 ids.
2. **Current.** Verified at corestandards.org: the page hosts the same 2010 PDFs (ELA_Standards1.pdf and an
   accessible copy), says the standards are "temporarily located" there while the old site is repaired, and names
   no revision.
3. **Verdict.** Current. There is no newer national edition; states have their own revised versions.
4. **Nothing to update.** 163 modules (ELA 158, library 3, ELD 2). The literacy strands for history, science and
   technical subjects (RH, RST, WHST) are still not loaded and no module uses them.
5. **Licence.** The file header records the Common Core public licence: copying and publishing allowed for
   purposes that support the initiative, with the copyright notice. The licence page address tried today returned
   404, so the wording was not reread; it rests on the header. Full text in the repo is within the licence as
   described, provided the notice stays.

### ccss-math-clusters.txt, ccss-math-standards.txt, ccss-math-focus.csv

1. **Loaded.** Common Core Math 2010: 147 cluster ids; the full text of every standard; and the major, supporting
   and additional marks from the Student Achievement Partners focus documents (2013 to 2014) plus the high school
   widely applicable prerequisites table (2013).
2. **Current.** Standards: verified as for ELA (Math_Standards1.pdf on corestandards.org, no revision). Focus
   documents: not rechecked today. From memory, not verified: they have not been reissued.
3. **Verdict.** Standards current. Focus file: cannot tell, with no sign of change.
4. **Nothing to update.** 137 modules, all math. Mathematical Practices are still not loaded.
5. **Licence.** Standards: Common Core public licence as above. Focus documents: the header records an archived
   achievethecore.org statement that site content is CC0 unless marked.

### csta-2026-ids.txt

1. **Loaded.** 196 bare ids (EK, E1 to E5, MS, HS; concepts ALG, PRO, DAT, SYS, SOC). **The file has no header at
   all**: no source, no version, no fetch date, no licence. It is the only standards file like this.
2. **Current.** Verified. The CSTA standards page now cites the "2026 CSTA PK-12 computer science standards"
   (DOI 10.1145/3820482). I downloaded the 218-page PDF and matched ids by script:
   - All 196 ids in the file appear in the PDF, and the PDF holds exactly 196 foundational ids. The file is the
     complete set of Foundational Standards.
   - The PDF also holds 135 high school **Specialty** ids (S1 73, S2 62) across artificial intelligence,
     cybersecurity, data science, game development, physical computing and software development, plus X+CS
     standards for teaching computer science inside other subjects. None are in the file.
   - The PDF's own timeline: structure set in fall 2024, three public drafts, finalized spring 2026, published
     summer 2026. It names the 2017 set as the previous standards.
   - Bands: pre-K and K together (EK), each of grades 1 to 5, one middle school band, one foundational high school
     band. Five concepts: Algorithms and Design, Programming, Data and Analysis, Systems and Security, Computing
     and Society. Twelve practices in four groups.
3. **Verdict.** Current but incomplete.
4. **What updating touches.** 67 modules tagged CSTA-2026 (computer science 66, math 1; course id cs-k12 at every
   grade band, and math-k8 at K). All 207 CSTA codes on modules are in the file. No renumbering. What is missing:
   - A header (source, version, fetch date, licence, counts) like every other file.
   - The wording. docs/agents/gapfill/cs/notes.md already notes the repo holds ids only.
   - The Specialty standards. This is the one place meaning is affected: a 9-12 computer science course can only be
     coded to the 46 foundational high school standards, so any advanced course (AI, cybersecurity, data science)
     has nothing to align to in the data.
   - Several tool specs cite 2017 codes beside the 2026 ids as a crosswalk. That is fine, but the 2017 codes are
     now the superseded set and should never stand alone.
5. **Licence.** CC BY-NC-SA 4.0, stated in the PDF and on the page. Full statements may be stored and adapted with
   attribution, for non-commercial use, under the same licence. **Flag:** LICENSE-CONTENT.md puts all Curio Class
   data under CC BY 4.0. CSTA text cannot be relicensed that way, so if the wording is added the file needs its own
   licence line and LICENSE-CONTENT.md needs a third-party note.

### cte-career-clusters-2024.txt

1. **Loaded.** The 14 clusters and 72 sub-clusters by name, and the 12 Career Ready Practices as numbers 1 to 12
   only. The header says the final practices PDF was image-only, so wording and order were never read.
2. **Current.** Verified at careertech.org: the modernized framework was released in 2024, with 14 clusters, 72
   sub-clusters, three cross-cutting clusters and 12 practices; the wheel graphic was redrawn in April 2025; no
   later change. Search result only: the practices were reworded in 2024 from the 2012 list, and a text page now
   exists at careertech.org/career-ready-practices (not opened).
3. **Verdict.** Current but incomplete (practice wording).
4. **What updating touches.** 8 modules (course ids cte-explore 6-8 and cte-pathways 9-12), coded only as
   "CTE.Career Clusters" or "CTE.Career Ready Practices". No renumbering. Reading the 2024 practice wording could
   shift what the two practice modules teach, since the 2024 list reframes some practices around workplace use.
5. **Licence.** (c) Advance CTE, all rights reserved; no reuse terms on the page. Names of clusters are safe;
   ask before storing the practice text.

### hecat-topics.txt

1. **Loaded.** HECAT 2021: ten topic modules and 81 Healthy Behavior Outcomes as ids. No wording.
2. **Current.** Verified at cdc.gov: the 2021 edition is the current HECAT (page dated 2024-11-29), same ten
   modules. The HECAT overview PDF (opened) cites the National Health Education Standards, **second edition,
   2007**, as its standards source.
3. **Verdict.** Current as an edition. **Keyed to a different edition than the loaded standards**: HECAT 2021
   scores knowledge and skill expectations built on the 2007 standards, and data/standards/nhes-2024.txt is the
   2024 set.
4. **What this means.** No module carries a HECAT code, so nothing in data/modules.csv changes. The effect is on
   the bar: a health unit judged with HECAT is being judged against 2007 expectations. The eight standards keep
   the same order and the same skills in both editions (influences, access, communication, decisions, goals,
   practices, advocacy), so the skill side maps one to one. Standard 1 is the part that moved: the 2024 wording is
   about using functional health information; the 2007 wording was about comprehending concepts (2007 wording
   from memory, not verified).
5. **Licence.** US government work; no licence line in the parts read. Storing HECAT text is low risk, though
   only ids are stored now.

### ncas-performance-standards.txt

1. **Loaded.** 1,202 performance standard ids for dance, media arts, music, theatre and visual arts, from the
   "at a glance" handouts (2014 standards, handouts dated 2021-11). No wording.
2. **Current.** Verified at nationalartsstandards.org: the 2014 standards are still the published set. The home
   page carries a section on reviewing and revising them. The March 2026 process update (PDF opened) says the
   review was announced in February 2025, a survey ran to May 2025 with 3,490 responses, the field wants
   "refinement rather than a re-write", and five goals are set (access for all learners, concise language, student
   voice, technology and AI, postsecondary readiness). A project manager is being hired and the work is called
   multi-year. No release date is given; the timeline graphic is an image I could not read.
3. **Verdict.** Current. A revision is coming and has no date.
4. **What a revision would touch.** 74 modules (arts 72, library 1, ELA 1; course ids dance, media-arts, music,
   theater, visual-arts at every band). Modules cite process and anchor only (for example MU:Pr4). If the eleven
   anchors survive, as the survey summary suggests, module codes hold and only this file's 1,202 ids need
   reloading. If anchors are merged or renumbered, all 74 modules change.
5. **Licence.** Not verified: the copyright guidelines page returned 404 at the two addresses tried. The site
   footer names Young Audiences, Inc. Keep to ids until the terms are read.

### ngss-pes.txt

1. **Loaded.** All 208 performance expectation ids (2013 standards, from the 2017 arrangements PDF). No wording.
2. **Current.** Verified at nextgenscience.org: no revision is announced. The trademark and copyright page
   (opened) names WestEd as the trademark holder and contact, and gives 2013 as the copyright date to cite.
3. **Verdict.** Current.
4. **Nothing to update.** 110 modules, all science.
5. **Licence.** The page describes a public licence letting states, districts, schools, teachers and non-profit
   education bodies copy and adapt the standards without asking. Whether a free public website run by an
   individual counts is not spelled out; ask nextgenscience@wested.org before storing full text. Any use of the
   name needs the trademark footnote, which says the lead states and WestEd were not involved in and do not
   endorse the product.

### nhes-2024.txt

1. **Loaded.** 172 indicator ids in four grade spans under eight standards, from SHAPE America's free standards
   page. No wording.
2. **Current.** Verified at shapeamerica.org: the page lists these eight standards, labels them the 2024
   standards, and links the 2007 standards as the older set. There is a second set with the same title: National
   Health Education Standards, 3rd Edition, 2022, from the National Consensus for School Health Education
   (verified at schoolhealtheducation.org; eight standards, free PDF). Both bodies call theirs the third edition.
   Search result only: SHAPE America took over the copyright of the earlier editions in 2020, and at least one
   state committee chose the SHAPE set over the other.
3. **Verdict.** Current. **But the header is wrong**: it credits "SHAPE America / National Consensus for School
   Health Education" as one publisher. They are two bodies with two rival sets. The ids in the file are SHAPE
   America's.
4. **What updating touches.** Header only. 21 modules (health-pe; course id health at all four bands) cite
   NHES.S1 to S8, which carry the same number-to-skill order in the 2007, 2022 and 2024 sets, so no code moves.
   The site should always name the edition as "SHAPE America, 2024".
5. **Licence.** (c) 2024 SHAPE America. The public licence page (opened) allows use, copying, publishing and
   display of the standards, rationale and indicators for non-commercial and educational purposes, with an
   acknowledgement, a (c) 2024 notice and a link; no modification; no revenue from them; other reproduction or
   creating content from the standards needs written permission. Ids are safe. Full indicator text could
   probably be stored unmodified with the notice, but because Curio Class builds teaching tools from them, read
   the licence text itself (not my summary) and consider asking once.

### nspfe-2021.txt

1. **Loaded.** 379 learning outcome ids under 135 standards in six topics, grades 4, 8 and 12. No wording.
2. **Current.** Verified at jumpstart.org: the 2021 edition is the current one, a free PDF, no revision
   mentioned. The live PDF address is
   https://www.jumpstart.org/wp-content/uploads/2023/04/2021_Natl_Standards_Downloadable_final.pdf (the source
   search today could not find a live copy; this one is linked from the Jump$tart page).
3. **Verdict.** Current.
4. **Nothing to update.** 14 modules (CTE 9, social studies 3, math 2; course ids personal-finance, cte-explore,
   ss-k5, math-k8), all at topic level.
5. **Licence.** Free download; the site footer says all rights reserved and no reuse terms are given. Keep to ids.

### shape-pe-2024.txt

1. **Loaded.** 210 grade-span indicator ids under four standards. No wording.
2. **Current.** Verified at shapeamerica.org: four standards, 210 indicators with the same per-span counts as the
   file header, labelled the 2024 standards, with the 2013 standards linked as the older set.
3. **Verdict.** Current.
4. **What to watch.** 12 modules (health-pe 11, arts 1; course id pe at every band, and dance k-2) cite SHAPE.S1
   to S4, which only exist in the 2024 numbering, so the data is consistent. The mismatch is in the instrument:
   CDC's PECAT (2019) scores a curriculum against the earlier **five** standards. From memory, not verified: the
   old five were motor skills; movement concepts; fitness knowledge and skills; responsible personal and social
   behaviour; and valuing physical activity. The 2024 four fold fitness into the knowledge standard and split the
   last two into social skills and personal skills. Any PECAT-style check needs that mapping written down first.
5. **Licence.** Same SHAPE America public licence as health.

### wida-2020.txt

1. **Loaded.** 104 language expectation ids from the 2020 framework PDF. No wording.
2. **Current.** Verified at wida.wisc.edu: the 2020 Edition is presented as the current framework; 2007 and 2012
   appear only in a comparison chart; nothing newer is announced.
3. **Verdict.** Current.
4. **Nothing to update.** 22 modules (course id eld-k12 at every band). WIDA PRIME 2020 is keyed to the same
   edition.
5. **Licence.** (c) Board of Regents of the University of Wisconsin System. The policies page returned 404, so
   reuse terms were not read. Keep to ids.

---

## Review instruments keyed to a different edition than the one loaded

| Instrument (from the source search today) | Keyed to | Loaded in the repo | What to do |
|---|---|---|---|
| CDC HECAT 2021 (health) | National Health Education Standards, 2nd edition, 2007 (verified in the HECAT overview) | SHAPE America 2024 | Name both editions wherever HECAT is used. Skills 2 to 8 map straight across; reread Standard 1. |
| CDC PECAT 2019 (PE) | SHAPE America's earlier five standards | SHAPE America 2024, four standards | Write a five-to-four mapping before any use. Oregon's 2025 PE criteria already use the four. |
| CFPB Youth Financial Education Curriculum Review Tool, 2015 | Content lists older than the 2021 standards | NSPFE 2021 | Use its utility, quality and efficacy parts as they are; redo the content part against 2021. |
| CSTA Standards Alignment Review, 2026 | The 2017 CSTA standards (the 2026 standards PDF cites it as an analysis of the 2017 set) | 2026 foundational ids | Treat its findings about which standards curricula skip as findings about 2017 codes. |
| K-12 Computer Science Framework, 2016 | Its own five concepts, the base of the 2017 standards | 2026 standards with five renamed concepts | Use for practices and progressions; take concept names from the 2026 standards. |
| State computer science rubrics (Ohio, Oklahoma, Massachusetts, Florida) | Each state's own standards, mostly built on CSTA 2017 (from memory, not verified) | 2026 | Use for structure and scoring only. |
| Texas LOTE rubric (approved 2026-09-04) and the Can-Do Statements | Can-do objectives; the current statements are the 2026 edition | No Can-Do Statements loaded | If Can-Do Statements are loaded, load 2026. |
| docs/ADOPTION-BAR.md, line 111 | Notes a source that quotes 2017 CSTA codes | 2026 | Already flagged there; no change. |

Instruments that match what is loaded: WIDA PRIME 2020 (WIDA 2020), the CASEL program criteria (CASEL 5), the
Texas, Oklahoma and California arts criteria (2014 arts standards or state standards built on them), and the
EdReports and EQuIP tools for math, ELA and science.

## What I could not verify

- **C3 Framework**: socialstudies.org returned 403. "No revision" rests on a search and on memory.
- **AASL second edition**: I did not recount the second edition PDF. That the numbering is unchanged rests on the
  file header and on AASL's statement that the core frameworks are intact.
- **National Core Arts Standards**: copyright terms (page 404) and the review timeline (image only).
- **Common Core public licence**: the licence page address returned 404; wording rests on the file headers.
- **WIDA** reuse terms (policies page 404).
- **Student Achievement Partners focus documents**: not rechecked.
- **ASLTA Standards for Learning ASL**: the page exists and names two sets, but gives no year; the files were
  not downloaded.
- **Career Ready Practices 2024 wording**: a text page was found by search and not opened.
- **The 2007 wording of the health standards and the 2014 wording of the five PE standards**: from memory.
- **PECAT**: not reopened; its link to the five standards is taken from today's source search, which opened it.
- **SHAPE America's public licence**: read through a page summary, not the raw text.
- **AP Precalculus, AP Statistics, AP Calculus and APA high school psychology** (26 modules): no file in
  data/standards/, so nothing was checked. From memory, not verified: the APA psychology standards were revised
  in 2022, and module codes such as "APA.Biological" should be checked against that edition.

## Recommended order of fixes

1. **Fix the header of nhes-2024.txt and settle on the name "SHAPE America, 2024".** Reason: the header credits
   two rival bodies as one, and health is the subject with the strongest instrument. A bar that says "aligned to
   the national standards" without a named edition would be ambiguous on day one. Five minutes of work.
2. **Give csta-2026-ids.txt a header, and decide about the Specialty standards.** Reason: it is the only file
   with no source, date or licence, and the only current-edition gap that limits what a course can teach (9-12
   computer science beyond the foundational level). The licence (CC BY-NC-SA 4.0) allows the wording to be stored,
   which would also close the "ids only" complaint in docs/agents/gapfill/cs/notes.md.
3. **Write the PE five-to-four mapping and the health 2007-to-2024 note before the bar for health and PE is
   drafted.** Reason: both federal tools are the best instruments found for any subject and both are keyed to
   the older editions. Without the mapping, the bar would quietly rest on superseded standards.
4. **Relabel AASL from 2018 to the second edition (2025).** Reason: label only, but it appears on 18 modules, in
   data/subjects.csv and in scripts/standards.py, and a public page that says "2018" a year after the second
   edition looks stale. Rename the tag and the file together so the checker keeps passing.
5. **World languages: load the 2026 Can-Do Statements (ids or benchmarks) and the ASL standards, or record a
   decision not to.** Reason: this changes what the ASL course is expected to teach, and it should be settled
   before the world language spines are written, not after.
6. **Read the 2024 Career Ready Practices wording and fill in section 3 of the CTE file.** Reason: small, and the
   two practice modules are currently coded to a list nobody has read.
7. **Licence housekeeping.** Add a licence line to every file header; reword the CASEL sub-skill notes or ask
   CASEL; add a third-party note to LICENSE-CONTENT.md saying the standards text in data/standards/ (Common Core
   now, CSTA if added) is not covered by CC BY 4.0. Reason: the repo is public and the content licence currently
   claims all data.
8. **Put the arts standards review on a watch list and recheck twice a year.** Reason: it is the only loaded set
   with a revision under way, 74 modules depend on it, and no date is published.
9. **Add files for the AP and APA frameworks or drop the tags.** Reason: 26 modules cite frameworks the repo
   cannot check.
