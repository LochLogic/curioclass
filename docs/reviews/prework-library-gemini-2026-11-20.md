# Library and research skills pre-work: second-model cold read, 2026-11-20

> Filed by the lead 2026-11-20. Gemini 4 Neon (medium effort) in Antigravity, pasted by Cory from S:/CurioClass-gemini/ (prompt 10 to 18 for this subject), after it passed calibration (docs/reviews/calibration-*-gemini-2026-11-20.md). Its saved report is S:/CurioClass-gemini/reports/prework-library-read.md; text unchanged here except wording the repository checks flag.

Read as the curriculum expert (docs/agents/EXPERT.md) with the library and research skills lens
(docs/agents/lenses/library.md). I did not write these drafts. Nothing in S:\CurioClass was edited; this report is
saved to S:\CurioClass-gemini\reports\prework-library-read.md. Each finding carries a confidence mark: Firm, Likely
or Judgment call. Anything resting on memory is marked "from memory". I did not open the earlier Claude read
(docs/reviews/prework-library-read-2026-11-20.md) until my own findings were complete; the final section compares the
two reads.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/library.md; docs/FOUNDATION.md; docs/COURSE-RUN.md (stage 1);
docs/courses/library/STANDARD.md; docs/courses/library/APPROACH.md; data/standards/aasl-2018.txt;
docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, part 11, the library row of "Before a scope and sequence",
decisions and sources table); docs/reviews/library-open-material-2026-11-16.md; docs/courses/UNIT-PLAN.md;
docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md (finished examples for comparison);
docs/pipeline/briefs/sensitivity-read.md; docs/reviews/prework-sel-read-2026-11-19.md (report shape). For checks
only: scripts/progression.py (lines 1 to 150, covering STD_FILES, ANCHOR and code_grades); scripts/standards.py
(lines 80 to 142); data/courses.csv (line 50, plus lines 41 to 49 for the SEL and ELD comparison); data/subjects.csv
(line 13); targeted reads of data/progressions/ela.csv and data/progressions/social-studies.csv to verify the exact
cross-subject row ids named in STANDARD.md section 5. Checked that data/standards/aasl-words.txt does not exist.
Opened docs/reviews/prework-library-read-2026-11-20.md only after all findings below were fixed.

Outside sources checked by web search, by link:

- [AASL Standards Web Portal](https://standards.aasl.org): confirmed the Second Edition (published Fall 2025), six
  Shared Foundations (I Inquire, II Include, III Collaborate, IV Curate, V Explore, VI Engage) and four Domains
  (A Think, B Create, C Share, D Grow).
- [AASL Permissions](https://standards.aasl.org/permissions/): confirmed that short non-commercial educational
  excerpts in a lesson or unit plan are allowed, while inserting the whole framework or a substantial part into a
  derivative curriculum guide requires formal permission.
- [AASL Learner Framework competency listings via public district and education mirrors](https://standards.aasl.org)
  (verified across published crosswalks for I.A.1 to I.D.4, III.A.1 to III.A.3, III.D.1 to III.D.2, IV.B.3, V.A.1,
  V.B.1 to V.B.2, V.C.1 to V.C.3, V.D.1 to V.D.2, II.C.2, III.C.2, VI.C.2, VI.D.3): used to verify the meaning of
  the seven excluded AASL ids in STANDARD.md section 4.
- [Empire State Information Fluency Continuum (WeTeachNYC / Stripling model summaries)](https://libguides.monroe.edu/ESIFC):
  confirmed the six inquiry phases (connect, wonder, investigate, construct, express, reflect) and four updated anchor
  standards (Inquiry and Design Thinking, Multiple Literacies, Social and Civic Responsibility, Personal Growth and
  Agency).
- [AASL Position Statements on School Library Scheduling and Instructional Role of the School Librarian](https://www.ala.org/aasl/advocacy/resources/statements/scheduling):
  confirmed that AASL publishes no fixed minute or hour quota and advocates flexible, responsive scheduling
  integrated at the point of need rather than fixed weekly slots.
- [Wineburg, Breakstone, McGrew, Smith and Ortega (2022), Journal of Educational Psychology, 114(5), 893 to 909 (ERIC/ED summary)](https://eric.ed.gov/):
  confirmed the six 50-minute lateral reading lessons in a district high school government/civics course.

## Verdict

The 68 AASL competency ids in data/standards/aasl-2018.txt are real, unique and consistent with the second edition,
and the revised pre-work has already solved several major gaps from the first pass (single-owner rule, host-task
fallbacks, tool limits, dose defaults and a sensitive-ground section). The biggest risk is that stage 1 is still not
ready to hand off to a progression writer: data/standards/aasl-words.txt does not exist, three of the four Empire
State continuum band files remain unread, two of the seven excluded AASL ids (V.C.2 and III.A.1) are misdescribed
against the AASL framework, and STANDARD.md section 3 instructs writers to place ELA and social studies ids in the
`assumes` column, which fails scripts/progression.py. The one change that matters most before stage 2 opens is
completing the own-words file and remaining continuum bands, fixing the excluded-id list and `assumes` rule in
STANDARD.md, and repairing the missing and misplaced plan fields in APPROACH.md.

## What I counted

| Check | Result |
|---|---|
| Ids in data/standards/aasl-2018.txt | 68 ids (`AASL.I.A.1` to `AASL.VI.D.3`), all unique, zero duplicates |
| Per-foundation counts in file | I: 2/3/4/4 (13); II: 3/3/2/3 (11); III: 3/2/2/2 (9); IV: 3/4/3/3 (13); V: 3/2/3/3 (11); VI: 3/3/2/3 (11); total = 68 (matches header and STANDARD.md section 1) |
| Validator (scripts/standards.py) | `aasl-2018.txt` loaded into `LISTED` under `'AASL-2018'` (line 98); `CLOSED['AASL-2018']` (line 117) accepts foundation names; all 68 full ids validate |
| Own-words file (data/standards/aasl-words.txt) | Missing (does not exist); only 1 example phrase (`AASL.IV.B.3`) appears in STANDARD.md |
| ESIFC continuum band files read | 1 of 4 (grades 3 to 5 read; PK to 2, 6 to 8 and 9 to 12 still owed) |
| Excluded AASL ids in STANDARD.md section 4 | 7 ids named (`V.B.1`, `V.C.2`, `V.A.1`, `V.D.1`, `V.D.2`, `III.A.1`, `III.D.2`); 2 are misdescribed (`V.C.2`, `III.A.1`) and `V.B.2` (tinkering/making) is omitted |
| Progression gate (scripts/progression.py) | `library` absent from `STD_FILES`, `ANCHOR` and `code_grades`; `data/progressions/library-excluded.csv` does not exist |
| Courses | STANDARD.md section 3: 8 courses (`library-k`, `library-1` to `library-5`, `library-6-8`, `library-9-12`). `data/courses.csv` line 50: 1 row (`library`, `k-12`). `data/subjects.csv` line 13: 1 row, already labelled second edition 2025 |
| Cross-subject ids named in STANDARD.md section 5 | All 8 named row ids exist (`e1-shared-research`, `e4-research`, `e5-locate-sources`, `e6-short-research`, `e7-research-questions`, `e12-research`, `ss8-news-literacy`, `us1-news-reading`); `ek-shared-research` (K) is omitted; `research-cycle`, `source-sourcing` and `corroboration` exist as model names, not skill ids |
| APPROACH.md plan fields against UNIT-PLAN.md | Unit fields: 1 missing, 3 partial, 5 partial, 7 incomplete, 10 partial; Section fields: 1 missing sensitive note, 4 partial, 5/6 print path misplaced in field 6 and day opening missing, 9 missing language-vs-content gap and check accommodations, 10 missing one-projector path; no C8 student self-check anywhere |
| Dose defaults in APPROACH.md | K to 2: 30 x 25 min (12.5 h/yr); 3 to 5: 30 x 35 min (17.5 h/yr); 6 to 8 and 9 to 12: 18 x 45 min (13.5 h/yr); no short path stated; no multi-year band totals stated |

## Findings, most serious first

### 1. Stage 1 deliverables are still unfinished: no own-words file and three of four grade-band check sets remain unread

- **Where:** docs/courses/library/STANDARD.md (owed table lines 16 to 17, section 1 lines 33 to 36, section 2 lines
  49 to 55); data/standards/aasl-words.txt (missing); docs/COURSE-RUN.md (stage 1: "Make: the standard in our own
  words and the approach").
- **What is wrong:** `data/standards/aasl-2018.txt` contains bare ids only, and `data/standards/aasl-words.txt` does
  not exist. Only one of the 68 competencies (`AASL.IV.B.3`) has an own-words phrase anywhere in the repository.
  Likewise, only the grades 3 to 5 band of the Empire State Information Fluency Continuum has been read in full; PK to
  2, 6 to 8 and 9 to 12 are unread. A progression writer cannot place 61 ungraded competencies into grades K to 12 or
  verify that every owner row teaches every part of each id when neither the skill phrases nor 9 of the 13 grades'
  priority skill lists exist.
- **Cost:** Stage 2 cannot open cleanly. A progression writer would have to invent meanings from memory or reopen the
  AASL PDF mid-draft, risking near-copying and leaving C1 ("taught in full, at the depth its wording asks") and bar
  part 11 criterion 2 ("each grade has named priority skills") untraceable.
- **Fix:** Do not open stage 2 until both items are completed in stage 1: (a) write `data/standards/aasl-words.txt`
  with all 68 ids and one 8 to 15 word action-and-object phrase per id in our own words (checked against the 2025
  second edition PDF, not from memory), and (b) read the PK to 2, 6 to 8 and 9 to 12 ESIFC band files in full and add
  the grade-by-grade priority skill summary table to STANDARD.md section 2. Keep STANDARD.md marked DRAFT until both
  are checked in.
- **Confidence:** Firm.

### 2. Two of the seven excluded AASL ids are misdescribed against the AASL Learner Framework, and V.B.2 is missed

- **Where:** docs/courses/library/STANDARD.md section 4, lines 105 to 107: "Excluded, each owned instead by the
  subject named: V.B.1 and V.C.2 (science and computer science design cycles), V.A.1 (ELA wide reading), V.D.1 and
  V.D.2 (SEL self-management), III.A.1 and III.D.2 (SEL relationship skills)."
- **What is wrong:** Checking the published AASL Learner Framework competencies shows two factual mismatches in the
  exclusion list:
  - `V.C.2` is about co-constructing innovative means of investigation, which is an inquiry and research skill, not a
    design cycle. The design/maker competency beside `V.B.1` (problem solving through cycles of design,
    implementation and reflection) is `V.B.2` (persisting through self-directed pursuits by tinkering and making).
  - `III.A.1` is about demonstrating a desire to broaden and deepen understandings, which is an inquiry disposition
    rather than a relationship skill. (`III.D.2`, recognizing learning as a social responsibility, is closer to SEL
    social awareness than relationship skills.)
- **Cost:** Excluding `V.C.2` drops a genuine collaborative-investigation competency from library on a false premise,
  while leaving `V.B.2` (tinkering and making) inside library forces a progression writer to invent a maker/design
  task that section 4 explicitly says belongs to science and computer science. Any reviewer checking the exclusion
  file against AASL will flag the wrong codes under C1.
- **Fix (pending Cory, since it changes which standards are excluded; replace STANDARD.md section 4 lines 105 to 107):**

> Excluded, each owned instead by the subject named: V.B.1 and V.B.2 (science and computer science design, tinkering
> and making cycles), V.A.1 (ELA wide reading), V.D.1 and V.D.2 (SEL self-management), and III.D.2 (SEL social
> awareness and civic learning). V.C.2 (co-constructing ways to investigate) and III.A.1 (broadening and deepening
> understanding through collaborative inquiry) stay in library and are met through research tasks. Everything else is
> met through a research task.

- **Confidence:** Firm (verified against published AASL Learner Framework competency listings).

### 3. STANDARD.md instructs progression writers to put cross-subject ids in `assumes`, which fails scripts/progression.py, and the gate has no library entry

- **Where:** docs/courses/library/STANDARD.md section 3 lines 74 to 77 ("Each row's `assumes` names the earlier
  library row or the ELA or social studies row it builds on (section 5)"), vs section 5 line 120 ("names that row in
  `cross_subject`"); scripts/progression.py lines 13 to 19, 51 to 70, 87 to 141.
- **What is wrong:** Three gate and handoff problems sit in section 3:
  1. `scripts/progression.py` requires every `assumes` entry to be a same-subject `skill_id` at an earlier grade,
     paired with `hands_on` on the earlier row. Putting an ELA or social studies row id in `assumes` causes an
     immediate FAIL. Cross-subject ids belong only in `cross_subject` (using `ela:...` or `social-studies:...`).
  2. `scripts/progression.py` still has no `library` entry in `STD_FILES` or `ANCHOR`, and
     `data/progressions/library-excluded.csv` does not exist. (`code_grades` already returns `None` for unlisted
     subjects, which matches ungraded AASL ids.)
  3. Section 3 does not state two handoff rules a progression writer needs: Kindergarten rows have empty `assumes`
     (first grade of the sequence), and inside the band courses (`library-6-8` and `library-9-12`), each school-year
     row assumes the previous school year's library row (grade 6 to 7 to 8 to 9 to 10 to 11 to 12) with no grade
     skipped unless the row's notes explain why. Also, because K to 2 are marked "at the 'with help' level" and
     ownership requires "first met at the depth a check can score on its own", K to 2 rows will carry `~ID` only; the
     page should confirm explicitly that K to 2 rows may carry `~ID` only and own zero ids (or state which basic ids
     K to 2 may own).
- **Cost:** The first stage 2 draft will fail `scripts/progression.py check library`, or cannot run the gate at all.
- **Fix (replace STANDARD.md section 3 lines 74 to 77):**

> Each row's `assumes` names the earlier library row it builds on (empty in kindergarten; inside grades 6 to 8 and 9
> to 12, each school year's row assumes the previous school year's library row with no grade skipped unless the row's
> notes explain why). Every earlier ELA or social studies skill a library row builds on goes in `cross_subject`
> (for example `ela:e5-locate-sources`), never in `assumes`. Kindergarten through grade 2 rows carry `~ID` only
> unless a basic competency (such as asking a question, I.A.1) is scored unaided in that grade; all other owned ids
> sit in grades 3 to 12. Before stage 2 opens, add `'library': ['aasl-2018.txt']` to `STD_FILES` and
> `'library': 'aasl-2018.txt'` to `ANCHOR` in `scripts/progression.py` (`code_grades` returns `None`), and create
> `data/progressions/library-excluded.csv` with one reason per excluded id.

- **Confidence:** Firm.

### 4. APPROACH.md drops or misplaces required UNIT-PLAN.md and adoption-bar fields, and omits a student self-check (C8)

- **Where:** docs/courses/library/APPROACH.md lines 26 to 71 ("The form of daily evidence" and "What library adds to
  the plan fields"); checked field by field against docs/courses/UNIT-PLAN.md, docs/FOUNDATION.md section 5.1, and
  docs/ADOPTION-BAR-SUBJECTS.md (C8, C9, C11, C12, C16).
- **What is wrong:** Checking every unit field (1 to 10) and section field (1 to 11) in order shows nine concrete
  placement and coverage faults:

| Field | Status | Fault against UNIT-PLAN.md / adoption bar |
|---|---|---|
| Unit field 1 (Header) | Dropped | Omitted completely; jumps straight to Unit field 2. Needs sessions by kind (in library's words), sessions a week and minutes, as `sel/APPROACH.md` line 47 does. |
| Unit field 2 | Partial | Does not state limits or note that AASL ids use our own-words phrases (never quoted competency text, needing a library exception in UNIT-PLAN.md rule 15 like arts and CS). |
| Unit field 3 | Partial | Drops "with the handoff marked strong or weak" (required by UNIT-PLAN.md field 3). |
| Unit field 5 | Partial | Missing **two sample answers** (one that meets the look-fors, one that does not) for teacher-judged rubric tasks (bar C9 fails at fewer than two levels) and the **accommodations** line. |
| Unit field 7 | Incomplete | Does not state marking time and response time separately, whether response occurs within the assessment day or on a Respond day, how Respond-day groups are formed from the teacher-judged rubric (no hands-up self-marking; cap at four groups from the class sheet), or the one-child at-home path. |
| Unit field 10 | Partial | Missing the pointer to the course-level **logic model** (bar C16 fails if no logic model) and the **C12 record of whose work and voices appear** (promised on line 101, placed in no field). |
| Section field 1 | Partial | Missing the sensitive topics the section touches, the stop rule note when open search is used, and the teacher response if an unsafe result appears (compare `sel/APPROACH.md` line 73). |
| Section field 4 | Partial | Drops "the day it is shown and the five to ten minute response if many made it". |
| Section field 5 and 6 | Misplaced and partial | **Placement fault:** line 62 puts "the print path when no devices are free (printed source sets)" in **Section field 6**, where it belongs in **Section field 5** ("what a room with nothing does", UNIT-PLAN.md line 252). Section field 6 drops **how a day opens and for how long** and the K to 5 rule that new skills are taught before they are tried (UNIT-PLAN.md rule 13). |
| Section field 9 | Partial (bar fail) | Missing **language gap vs content gap** in keys (bar C11 fails if missing) and **check accommodations** (UNIT-PLAN.md field 9 line 270). "The unit's few words" is also vaguer than health/SEL ("six to eight words taught in depth"). |
| Section field 10 | Partial | Drops **one projector** ("how the day runs with one screen"), required by FOUNDATION.md section 5.1 and UNIT-PLAN.md field 10. |
| Daily evidence / C8 | Missing | Bar C8 fails if "Students never judge or track their own work in a unit", and bar part 11 criterion 1 requires **reflect** in every inquiry cycle. APPROACH.md defines no student self-check or process reflection. |

- **Cost:** Every unit plan and section plan built from APPROACH.md will fail C8 (no self-check), C9 (no two-level
  samples or respond-day group rule), C11 (no language-vs-content-gap line), C16 (no logic model pointer), and
  UNIT-PLAN.md field placement (print path in field 6 instead of 5; no one-projector path in field 10).
- **Fix (paste these replacements into APPROACH.md "The form of daily evidence" and "What library adds to the plan
  fields"):**

> Add to **The form of daily evidence**:
> - **Once per unit (reflection, C8):** a short student self-check where the student rates their own use of the unit's
>   skill steps on the inquiry product and names one thing to do differently next time (spoken or pictured in K to 2).
>
> Replace or add the affected bullets in **What library adds to the plan fields**:
> - Unit field 1 (header): sessions by kind (Show-me, Practice, Inquiry, Assessment, Respond), sessions a week and
>   minutes, as the frame states them.
> - Unit field 2: the host task and its course (and the stand-alone host task, above); the AASL ids the unit owns
>   with our own-words phrases (never quoting AASL competency text) and the grade's priority skills; the limits; the
>   product and its audience; the skill card carried and the day it is withdrawn.
> - Unit field 3 (where it sits): builds on (the earlier library row, or the ELA or social studies row it assumes, by
>   id, with the handoff marked strong or weak); leads to; comes back in.
> - Unit field 5 (end-of-unit assessment): a search, a judgement or a citation actually done on a new case, scored on a
>   short rubric with look-fors and two sample answers (one that meets them and one that does not), plus a few items
>   and one line on check accommodations. Never a quiz on the names of the steps alone.
> - Unit field 7 (response allocation): state marking time and response time separately, and whether response runs
>   inside the assessment day or on a Respond day. The rubric is teacher-judged (no hands-up self-marking); groups for
>   the Respond day come from the class record sheet by missed step, capped at four groups, while others revise or try
>   a fresh case in pairs. Items with one answer are checked on the page. For one child at home, go over missed steps
>   together.
> - Unit field 10 (sources): what was read and how much, what is from memory, no claim of effect, a line pointing to
>   the course-level logic model (C16), and the C12 record of whose work and voices appear in the unit's source set.
> - Section field 1: before you teach: the AASL ids and priority skill, the skill as an adult uses it, why the method
>   beats a checklist of a page's looks, and any sensitive ground the section touches (plus the stop rule and teacher
>   response if open search is used).
> - Section field 4: expected slips beside a sound example, the day each is shown, and the five to ten minute response
>   if many made it.
> - Section field 5 (what is carried and instruments): the unit's skill card (held by the teacher on the first Show-me
>   day, by pairs on the first Practice day, withdrawn on the first Inquiry day named in the plan; check taken without
>   it; returns for one day in later units; pictured steps said aloud in K to 2); the ideal instrument and spec verdict;
>   and what a room with nothing does (the print path with printed source sets, assuming no library access).
> - Section field 6 (days): kind of day; how each day opens (a short retrieval check or one-minute source prompt, five
>   minutes at most); in K to 5, new skills are taught before they are tried.
> - Section field 9 (supports): English learners: six to eight words taught in depth per unit with a picture (including
>   research words with everyday meanings such as source, claim, check, host, cite) and sentence frames; a key line
>   saying that a sound check or reason given in the home language or by pointing is a language gap, while a wrong
>   method is a content gap. Access: the print path, read-aloud pages and oral or written options so no student must
>   speak aloud. Check accommodations: read aloud, oral answer, scribe, extra time. Reading load: source texts at grade
>   level or read aloud, with a shorter source set for students who read below it. Extension: the same skill on a
>   harder case, never the next grade's.
> - Section field 10 (two rooms): a parent teaching one child at a table with one device or none, using the printed
>   set (and the stop rule if using a device); one projector: the teacher displays the invented search results or
>   captured page while students record checks on paper or in pairs.

- **Confidence:** Firm.

### 5. `data/courses.csv` lists one `k-12` course, contradicting the settled eight-course list in STANDARD.md

- **Where:** data/courses.csv line 50 (`library,library,Library and Research Skills,k-12,,n,AASL Shared Foundations`);
  docs/courses/library/STANDARD.md section 3 lines 64 to 68 (`library-k`, `library-1` to `library-5`, `library-6-8`,
  `library-9-12`).
- **What is wrong:** `data/courses.csv` still holds a single `k-12` row for library, whereas SEL (lines 41 to 44) and
  ELD (lines 46 to 49) were updated on 2026-11-21 to match their settled course lists. Having one `k-12` row while
  STANDARD.md declares eight course ids creates a catalogue mismatch before frames and `data/plans/<course>/` folders
  are created.
- **Cost:** Downstream scripts and frame writers will disagree on whether the course id is `library` or `library-k`
  through `library-9-12`.
- **Fix (catalogue decision for Cory, question 1):** Replace line 50 of `data/courses.csv` with the eight settled rows
  (`library-k`, `library-1`, `library-2`, `library-3`, `library-4`, `library-5`, `library-6-8`, `library-9-12`), or
  with three rows (`library-k5`, `library-6-8`, `library-9-12`) if K to 5 follows the `science-k5` and `ss-k5`
  catalogue convention, and record the choice in STANDARD.md section 3.
- **Confidence:** Firm.

### 6. Cross-subject leans in STANDARD.md skip Kindergarten (`ek-shared-research`), mislabel models as core skills, and leave lateral reading's owning grade unpinned against grade 8 social studies

- **Where:** docs/courses/library/STANDARD.md section 5 lines 111 to 127; section 3 table lines 84 to 86;
  data/progressions/ela.csv line 25 (`ek-shared-research`), line 56 (`e1-shared-research`), line 202
  (`e6-short-research`), line 230 (`e7-research-questions`); data/progressions/social-studies.csv line 52
  (`ss2-source-maker`), line 53 (`ss2-two-accounts`), line 207 (`ss8-news-literacy`), line 314 (`us1-news-reading`);
  docs/agents/lenses/library.md line 36.
- **What is wrong:** Three precision errors sit in section 5:
  1. Line 112 says `rows e1-shared-research to e12-research`, omitting Kindergarten `ek-shared-research` (ela.csv line
     25, `W.K.7; W.K.8`), even though line 124 states that W.7 and W.8 begin in kindergarten.
  2. `research-cycle`, `source-sourcing` and `corroboration` are **model names** (`model_in`/`model_out`), not skill
     ids; `scripts/progression.py` validates `cross_subject` against `skill_id` or standard codes, never model names.
  3. Social studies `ss8-news-literacy` (grade 8) already teaches lateral reading ("reading across sites", with
     `lateral reading` in its words column). STANDARD.md says library owns lateral reading first and lists "first
     lateral checks" in grades 3 to 5 and "lateral reading" in grades 6 to 8, but does not pin which exact grade in
     `library-6-8` owns the lateral reading method before grade 8. A writer placing it in grade 8 collides with
     `ss8-news-literacy`.
- **Cost:** A writer who puts `ela:research-cycle` in `cross_subject` will fail the progression gate; a writer who
  places lateral reading in grade 8 of `library-6-8` will trigger the lens's own error ("Lateral reading owned by both
  library and social studies with no line saying who teaches it first").
- **Fix (update STANDARD.md section 5 lines 111 to 120):**

> **Who teaches what first.** ELA owns the research cycle and the writing of it (model `research-cycle`; rows
> `ek-shared-research` and `e1-shared-research` to `e12-research`), the first source list (grade 4, `e4-research`),
> locating print and digital sources with key words (grade 5, `e5-locate-sources`), source credibility in writing
> (grade 6, `e6-short-research`) and a standard citation format (grade 7, `e7-research-questions`). Social studies
> owns sourcing and corroboration (models `source-sourcing` and `corroboration`, from grade 2 rows `ss2-source-maker`
> and `ss2-two-accounts`) and news reading (`ss8-news-literacy`, grade 8; `us1-news-reading`, grade 11). Library owns
> what neither does: searching as a skill (changing a query, catalogues and databases, choosing among results),
> leaving the page to check who is behind it (lateral reading: first checks in grade 5, full method owned in grade 6
> or grade 7, before social studies uses it in `ss8-news-literacy` in grade 8), going upstream to the first source,
> honest use of others' work across media (not only in writing), and choosing among tools. Where a library row meets
> an ELA or social studies skill, it names the row id in `cross_subject` (never a model name).

- **Confidence:** Firm.

### 7. Sensitive ground rules in APPROACH.md leave gaps across grade bands, omit a read for copyright/fair use, and lack a leave-out or swap rule

- **Where:** docs/courses/library/APPROACH.md lines 87 to 105 ("Sensitive ground, and the read each needs");
  docs/ADOPTION-BAR-SUBJECTS.md line 91 ("each course page says what a school may leave out").
- **What is wrong:** Four gaps remain in the sensitive-ground block:
  1. Item 4 (honest use taught without shaming) assigns its read to "part of the 9 to 12 read" only, even though
     note-making, paraphrasing, quoting and citing are taught in grades 3 to 5 and 6 to 8.
  2. Item 2 (unsafe or upsetting search results) assigns its read to "the stop rule and the K to 5 plans" only, even
     though grades 6 to 12 are the grades most likely to run guided open-web Inquiry days (lines 75 to 76). Neither
     Item 2 nor Section field 10 says what a parent teaching at home does if an unsafe result appears, nor what
     adult-escalation step a school teacher follows if a student encounters harmful content (such as adult content,
     self-harm or scams).
  3. Item 6 (copyright and fair use as general guidance, never legal advice) names **no read** at all (unlike items 1
     to 5 and 7).
  4. Item 1 covers 6 to 12 cases touching politics, health, elections, religion, identity groups or conflict, but
     neither STANDARD.md nor APPROACH.md states whether a school or family may swap a sensitive case for a neutral
     stand-alone case (bar "Acceptability is local"), nor states plainly that K to 5 cases stay on neutral curriculum
     topics.
- **Cost:** Grades 3 to 8 miss the shaming-free check, grades 6 to 12 miss the stop-rule check, copyright wording
  goes unread for legal-advice slips, and schools have no stated swap rule for contested 6 to 12 cases.
- **Fix (update APPROACH.md lines 91 to 104):**
  - Item 1: add "K to 5 cases stay on neutral curriculum topics (science, local history, everyday facts). For 6 to 12,
    the course page states that a school or family may swap any sensitive case for a neutral stand-alone case without
    losing any AASL id, and the unit's family note names the case topic in advance."
  - Item 2: change "Read: the stop rule and the K to 5 plans" to "Read: the stop rule and every plan that includes
    guided open search, K to 12; the teacher page (Section field 1) and home note (Section field 10) state what the
    adult does if an unsafe result appears (close the page, no blame, follow school reporting or home safety steps)."
  - Item 4: change "Read: part of the 9 to 12 read" to "Read: part of the 3 to 5, 6 to 8 and 9 to 12 reads."
  - Item 6: add "Read: a rights read of the 6 to 12 copyright and fair-use days."
- **Confidence:** Likely.

### 8. Pacing and dose omit a short path (bar C2), leave a minor K to 5 frequency mismatch, and omit multi-year band totals

- **Where:** docs/courses/library/APPROACH.md lines 5 to 7 and 106 to 115 ("Pacing and dose");
  docs/ADOPTION-BAR-SUBJECTS.md C2 ("Fails if: ... No short path").
- **What is wrong:**
  1. No short path is stated for any band, though bar C2 fails a course with no short path.
  2. K to 5 is described as "one or two sessions a week all year", while the default is 30 sessions a year on a
     32-week Curio Class calendar (FOUNDATION.md line 36), which is about one session a week (two sessions a week
     would be about 60 sessions). Clarifying "about one session a week (or two sessions a week during a host-task
     sprint)" removes the mismatch and aligns with AASL's flexible-scheduling position statement.
  3. For the two multi-year band courses, `APPROACH.md` gives the per-year figure (18 sessions of 45 minutes, about
     13.5 hours a year) but omits the total course length across the band: 54 sessions (about 40.5 hours) across three
     years for `library-6-8`, and 72 sessions (about 54 hours) across four years for `library-9-12`.
- **Cost:** Frame writers for `library-6-8` and `library-9-12` have no stated total session budget or short-path rule
  for C2.
- **Fix (add to APPROACH.md "Pacing and dose", lines 108 to 112):**

> Default time, ours and untested: K to 2, 30 sessions a year of 25 minutes (about 12.5 hours, roughly one session a
> week or clustered into two-session sprints alongside a host unit); 3 to 5, 30 sessions a year of 35 minutes (about
> 17.5 hours); 6 to 8, 18 sessions a year of 45 minutes (about 13.5 hours a year, 54 sessions and about 40.5 hours
> across three years); 9 to 12, 18 sessions a year of 45 minutes (about 13.5 hours a year, 72 sessions and about 54
> hours across four years). Short path (C2, ours, untested): trim extra Practice days while keeping at least one full
> inquiry cycle per unit and the 6-lesson lateral reading floor in grades 9 to 12 (20 sessions a year in K to 5; 12
> sessions a year in 6 to 12).

- **Confidence:** Likely.

### 9. Stale and contradictory status notes across STANDARD.md, APPROACH.md and ADOPTION-BAR-SUBJECTS.md

- **Where:** docs/courses/library/STANDARD.md line 19; docs/courses/library/APPROACH.md lines 3 and 7 to 8;
  docs/ADOPTION-BAR-SUBJECTS.md lines 531 to 533, 547 and 571.
- **What is wrong:**
  - `STANDARD.md` line 19 (owed table) still reads `Approach page | Draft, waiting on Cory's yes`, and
    `ADOPTION-BAR-SUBJECTS.md` line 571 still reads `Owed: the approach page's yes | Cory`, even though
    `APPROACH.md` line 3 states `Approved by Cory 2026-11-21 (Desk q-prework-open-2)`.
  - `APPROACH.md` repeats the same sentence twice in its opening paragraph: line 3 ("read cold and fixed 2026-11-20")
    and lines 7 to 8 ("Read cold 2026-11-20 (docs/reviews/prework-library-read-2026-11-20.md) and fixed.").
  - `ADOPTION-BAR-SUBJECTS.md` part 11 line 547 still reads `the label is stale` (corrected 2026-11-11 and confirmed
    2026-11-16), and lines 531 to 532 still read `introduction page only` and `not re-opened` (grades 3 to 5 and
    AASL second edition were both opened on 2026-11-16).
  - `ADOPTION-BAR-SUBJECTS.md` line 571 still omits the owed stage 1 items (`aasl-words.txt`, the three unread ESIFC
    bands, `scripts/progression.py` support, and `library-excluded.csv`).
- **Cost:** Readers and writers get conflicting signals on whether pre-work is approved or still open.
- **Fix:** Update STANDARD.md line 19 to "Approved 2026-11-21 (Desk q-prework-open-2)"; delete the duplicate closing
  sentence on APPROACH.md lines 7 to 8; update ADOPTION-BAR-SUBJECTS.md part 11 lines 531 to 533, 547 and row 571 to
  reflect the current state and the remaining stage 1 owed items.
- **Confidence:** Firm.

## What is right and should not be touched

- All 68 AASL ids in `data/standards/aasl-2018.txt`, their per-foundation counts, and the clean licence stance (ids
  and our own short skill phrases only, never copying competency text or claiming AASL endorsement).
- The five kinds of day in `APPROACH.md` (Show-me, Practice, Inquiry, Assessment, Respond), mapped cleanly to the
  shared kinds.
- Pairing every unit's core host task with a stand-alone host task (invented question + closed source set) so
  biweekly 6 to 12 courses and families at home can run every unit without depending on another course's calendar.
- The "Sites, search and real cases" and "What a tool may and may not do" rules: invented sites and closed search
  sets for practice and checks, generic site kinds, no company or product names, no live web or tracking inside tools.
- The honest evidence posture: citing the AASL scheduling statement as setting no time figure, citing the 2022 six-
  lesson lateral reading study without overclaiming, and claiming no effect for any Curio Class course.
- The K to 2 daily evidence rule (class checklist kept by the teacher and thrown away at unit end, protecting
  FOUNDATION promise 2).

## What I could not judge

- **Full coverage of every part of each AASL id (brief check 7):** No `data/progressions/library.csv` and no
  `data/standards/aasl-words.txt` exist yet, so individual owner rows and handoff pairs cannot be checked against
  full competency statements until stage 2.
- **ESIFC grade-band placement for K to 2, 6 to 8 and 9 to 12:** Only grades 3 to 5 was read by the writer, and I did
  not download the four Monroe One BOCES band PDFs.
- **Civic Online Reasoning CC BY 4.0 item list (47 items) and licence text:** Relies on the 2026-11-16 scout reading
  in `docs/reviews/library-open-material-2026-11-16.md`; the licence page should be re-checked by the rights reader at
  first adaptation.
- **AASL second edition (2025) wording changes vs 2018:** My web search verified the 68-id structure and the core
  meaning of the excluded ids against published AASL Learner Framework listings (chiefly 2018 mirrors); the writer
  must check the exact 2025 second edition PDF when drafting `data/standards/aasl-words.txt`.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Cross-subject rows go in `cross_subject` (never `assumes`); K rows have empty `assumes`; 6 to 12 rows chain year by year | Matches `scripts/progression.py` gate rules and avoids stage 2 FAIL | docs/courses/library/STANDARD.md section 3 |
| Add `ek-shared-research` to the ELA lean; distinguish model names (`research-cycle`, `source-sourcing`, `corroboration`) from row ids; pin lateral reading method ownership to grade 6 or 7 before `ss8-news-literacy` | Prevents gate failure on model names and eliminates grade 8 collision with social studies | docs/courses/library/STANDARD.md section 5 |
| Fill Unit fields 1, 2, 3, 5, 7, 10 and Section fields 1, 4, 5, 6, 9, 10; move print path from Section field 6 to field 5; add C8 student self-check | Fixes placement against `UNIT-PLAN.md` and prevents C8, C9, C11, C12 and C16 fails | docs/courses/library/APPROACH.md |
| Extend shaming-free honest-use read to grades 3 to 12, unsafe-search stop-rule read to 6 to 12, and add a rights read for 6 to 12 copyright/fair use | Closes sensitive-ground blind spots where those skills are actually taught | docs/courses/library/APPROACH.md |
| State total multi-year session counts (54 for 6 to 8; 72 for 9 to 12) and clarify K to 5 as about one session/week or two-session host sprints | Resolves 30-session vs "one or two sessions a week" friction and gives frame writers a band total | docs/courses/library/APPROACH.md |
| Clean up stale status notes and duplicate sentence | Removes contradictory Draft/Approved signals across three docs | STANDARD.md, APPROACH.md, ADOPTION-BAR-SUBJECTS.md |

## Questions for Cory

1. **`data/courses.csv` catalogue grain (finding 5).** `data/courses.csv` still has one `library` (`k-12`) row while
   STANDARD.md settles eight courses (`library-k` to `library-5`, `library-6-8`, `library-9-12`). **Recommended:**
   replace line 50 with the eight settled rows (or three rows `library-k5`, `library-6-8`, `library-9-12` if matching
   `science-k5` and `ss-k5`) so the catalogue matches the settled course list.
2. **Correcting two excluded AASL ids (finding 2).** The 2026-11-21 exclusion list excluded `V.C.2` (actually
   co-constructing means of investigation, not design cycles) and `III.A.1` (desire to broaden and deepen
   understandings, not relationship skills), and omitted `V.B.2` (tinkering and making). **Recommended:** keep
   `V.C.2` and `III.A.1` in library and exclude `V.B.2` alongside `V.B.1` instead of `V.C.2`.
3. **Holding stage 2 until stage 1's remaining files are finished (finding 1).** `data/standards/aasl-words.txt`, the
   three unread ESIFC band files, `scripts/progression.py` library support, and `data/progressions/library-excluded.csv`
   are still owed. **Recommended:** finish all four in stage 1 before opening stage 2 (progression).
4. **Short path per band (finding 8).** Bar C2 requires a short path. **Recommended:** set the default short path at
   20 sessions a year in K to 5 and 12 sessions a year in 6 to 12 (trimming extra Practice days while keeping at least
   one inquiry cycle per unit and the 6-lesson lateral reading floor in 9 to 12).
5. **Leave-out / swap rule for sensitive 6 to 12 cases (finding 7).** **Recommended:** state on the 6 to 12 course
   pages that a school or family may swap any case touching politics, health, elections, religion, identity groups or
   conflict for a neutral stand-alone case without losing any AASL id, and name the case topic in the unit's family
   note.

## Against the first read

Compared against `docs/reviews/prework-library-read-2026-11-20.md` (opened only after the findings above were
complete):

- **Already caught by the first read and still owed (still missing):** missing `data/standards/aasl-words.txt` (first
  read finding 4 -> my finding 1); three unread ESIFC band files (first read finding 8 -> my finding 1); missing
  `library` entry in `scripts/progression.py` and missing `library-excluded.csv` (first read finding 2 -> my finding
  3); single `library` row in `data/courses.csv` (first read finding 12 -> my finding 5, though the first read kept
  the single row as consistent with `cs-k12` while SEL and ELD have since been split in `data/courses.csv`).
- **Already caught by the first read and fixed before this read:** single-owner rule for the 68 ids, stand-alone host
  task fallback, tool limits, invented-sites rule, AI-made content in 6 to 12 emphasis, W.9 grade 4 start, NML grade 8
  start, and dose defaults.
- **New findings in this second read (including faults introduced when the first read's fixes were applied):**
  1. **Two misdescribed excluded AASL ids (`V.C.2` and `III.A.1`) and missed `V.B.2`** (finding 2): came directly from
     the first read's finding 3 proposal and was pasted into `STANDARD.md` section 4.
  2. **`assumes` vs `cross_subject` gate bug** (finding 3): the first read's finding 2 fix told writers to put ELA or
     social studies rows in `assumes`, which fails `scripts/progression.py`; also added the K empty-`assumes` and
     year-by-year 6 to 12 handoff rules.
  3. **Field-by-field `UNIT-PLAN.md` placement and bar gaps left in `APPROACH.md`** (finding 4): Unit field 1
     dropped, print path placed in Section field 6 instead of 5, day-opening rule missing from Section field 6,
     one-projector path missing from Section field 10, two-level samples missing from Unit field 5, response times and
     group cap missing from Unit field 7, logic model and C12 voices record missing from Unit field 10,
     language-gap-vs-content-gap and check accommodations missing from Section field 9, and C8 student self-check
     missing altogether.
  4. **Cross-subject precision gaps** (finding 6): `ek-shared-research` (K) was dropped from the first read's finding 1
     paste-in, model names were called "core skills", and lateral reading ownership was not pinned to grade 6 or 7
     ahead of `ss8-news-literacy`.
  5. **Sensitive-ground blind spots** (finding 7): shaming-free read skipped grades 3 to 8, unsafe-search read skipped
     6 to 12, copyright/fair use lost its read line when pasted into `APPROACH.md`, and no leave-out/swap rule or
     Section field 1 teacher-note slot was wired in.
  6. **Pacing gaps** (finding 8): no C2 short path, K to 5 "one or two sessions a week" vs 30 sessions/year friction,
     and corrected multi-year band totals (54 and 72 sessions; the first read had an arithmetic slip of "40 over
     three" and "54 over four" for 18 sessions/year).
  7. **Stale status notes and duplicate sentence** left after the 2026-11-20 and 2026-11-21 edits (finding 9).
