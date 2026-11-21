# Library and research skills pre-work: cold read, 2026-11-20

Read as the curriculum expert (docs/agents/EXPERT.md) with the library and research skills lens
(docs/agents/lenses/library.md). I did not write these drafts. Nothing was edited but this file. Each finding is marked
Firm, Likely or Judgment call. Anything resting on my memory is marked "from memory". This is a stage 1 read
(docs/COURSE-RUN.md); it is one reader, so it is not the second-model read or the calibration the stage also asks for.

## What I read

AGENTS.md; docs/agents/EXPERT.md (named in the brief, skimmed through the lens); docs/agents/lenses/library.md;
docs/courses/library/STANDARD.md and APPROACH.md; data/standards/aasl-2018.txt; docs/ADOPTION-BAR-SUBJECTS.md (pass rule,
C1 to C16, part 11, the library row of "Before a scope and sequence", the decisions list); docs/reviews/library-open-material-2026-11-16.md;
docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md (finished examples); docs/courses/UNIT-PLAN.md (field
lists only); docs/pipeline/briefs/sensitivity-read.md; docs/COURSE-RUN.md stage 1; docs/reviews/prework-sel-read-2026-11-19.md
(format and the ownership precedent). For the checks only: scripts/progression.py (STD_FILES, ANCHOR, code_grades and the
ownership check); data/courses.csv and data/subjects.csv (the library rows only); docs/COURSES-STATUS.md (library rows);
one-line greps in data/progressions/ela.csv, social-studies.csv, science.csv and computer-science.csv.

Outside sources opened, by link:

- [AASL learner framework, second edition, PDF](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf):
  downloaded and counted by position on the page (the footer reads second edition, copyright 2026).
- [AASL learner framework, first edition, PDF hosted by Rhode Island](https://ride.ri.gov/Portals/0/Uploads/Documents/Instruction-and-Assessment-World-Class-Standards/Other-Subjects/180206-AASL-framework-for-learners-2.pdf):
  downloaded and counted the same way (footer: 2018).
- [standards.aasl.org home](https://standards.aasl.org/): shows "Second Edition".
- [AASL permissions page](https://standards.aasl.org/permissions/): an excerpt that shows how the work is applied, such as a
  lesson or unit plan, is permitted; putting the full document or a large share of its text into a derivative work such as
  a curriculum guide needs permission.
- [Monroe One BOCES continuum guide, about page](https://libguides.monroe.edu/ESIFC) and
  [its continuum page](https://libguides.monroe.edu/ESIFC/continuum): four band files (PK-2, 3-5, 6-8, 9-12) with priority
  skills in bold; last updated 2019-10-23; no author, no licence or copyright line on the pages I opened.
- [Stanford news release on the 2022 lateral reading field study](https://ed.stanford.edu/news/it-doesn-t-take-long-learn-how-spot-misinformation-online-stanford-study-finds)
  (by search result only): about 500 high school students, an urban midwestern district, six 50-minute lessons.
- [AASL scheduling position statement, ALA repository](https://alair.ala.org/handle/11213/15901) (by search result only).

## Verdict

The standard list is sound: all 68 AASL ids are real, unique and match both the first and second edition PDFs cell by cell.
But the pre-work is not ready to feed a progression: there is no ownership rule for 68 ungraded competencies (and the gate has
no library support), about 30 of the 68 are outside research and are neither excluded nor assigned, several of the library skills
are already owned by ELA and social studies core skills that the page does not name, and the approach page leaves out the dose,
the sensitive ground, the tool limits and most plan fields. The fixes are all writing and one small gate change; the questions
for Cory are few (ownership form, the 30 outside ids, own-words licence stance, naming real sites).

## What I counted (so nobody has to again)

| Check | Result |
|---|---|
| Ids in data/standards/aasl-2018.txt | 68 lines, no duplicates, form `AASL.<I to VI>.<A to D>.<n>` |
| By cell, file | I 2/3/4/4, II 3/3/2/3, III 3/2/2/2, IV 3/4/3/3, V 3/2/3/3, VI 3/3/2/3 (Think/Create/Share/Grow): matches the header note and STANDARD.md section 1 |
| By cell, first edition PDF (2018) | Counted by page position: identical, 13/11/9/13/11/11 = 68 |
| By cell, second edition PDF (footer 2026, file name 250918) | Counted the same way: identical, 68. The per-id keywords I read match the file's numbering (for example V.B.1 is problem-solving through design cycles, VI.B.2 is acknowledging authorship) |
| Own words | The file holds ids and header notes only; no competency is quoted. No own-words gloss exists for any of the 68 |
| Courses | STANDARD.md: 8 (K, 1, 2, 3, 4, 5, 6 to 8, 9 to 12). COURSES-STATUS.md: 8 rows. data/courses.csv: 1 row (`library`, `k-12`, typical_grade blank, notes "AASL Shared Foundations"). data/subjects.csv: 1 row, label already "second edition 2025" |
| Stale counts | The bar's decision 9 still says "four courses can proceed"; the bar part 11 fails-if and rows say 8 |
| Pacing statements | Three: APPROACH.md header and the bar pass rule say "one or two sessions a week all year"; STANDARD.md section 3 and APPROACH.md "Questions" say 6 to 8 and 9 to 12 are "about one session every two weeks" |
| Dose numbers | Minutes per session: stated nowhere. Sessions per year: stated nowhere. National time figure: none cited, none found (see finding 6) |
| Cross-subject leans | 4 leans in STANDARD.md section 5; 0 name a skill id from data/progressions |
| Progression gate | `library` is absent from STD_FILES, ANCHOR and code_grades in scripts/progression.py |
| Ids outside a research reading | By my sort of the 68 keywords: II (11), III (9) and V.B, V.C, V.D (8) = 28, plus V.A.1 and VI.D.3 as borderline = about 30 |
| Core skills already covering library's grade 3 to 5 and 6 to 8 skills | ELA `research-cycle` core skill in 16 rows; `e4-research`, `e5-locate-sources`, `e5-research`, `e6-short-research`, `e7-research-questions`; social studies `source-sourcing` (75 rows), `corroboration` (28), `ss8-news-literacy` |
| Science rows naming information evaluation | 0 (grep for obtain, evaluat and communicate in the notes and skill columns) |
| Computer science rows naming AI-made content or chatbots as sources | 0 (grep) |

## Findings, most serious first

### 1. Library's skills are already owned by ELA and social studies core skills, and the leans name none of them

- **Where:** STANDARD.md section 3 table (3 to 5: "key words, searching ... note-making ... a simple bibliography, first lateral checks";
  6 to 8: "paraphrase and quotation, citation in one style"); section 5 ("ELA owns the writing; library owns finding, judging and citing");
  the lens ("Lateral reading owned by both library and social studies with no line saying who teaches it first").
- **What is wrong:** The ELA progression already owns the research cycle from kindergarten (`ek-shared-research`, `e1-shared-research`
  to `e12-research`), citation in a first form at grade 4 (`e4-research`: "a source list"), print-versus-digital locating, key words and
  "reliable" at grade 5 (`e5-locate-sources`), credibility at grade 6 (`e6-short-research`) and a standard format at grade 7
  (`e7-research-questions`). Social studies owns `source-sourcing` and `corroboration` from grade 2 and lateral reading in
  `ss8-news-literacy` (grade 8) and `us1-news-reading` and `us1-research-inquiry` (grade 11). So "library owns finding, judging
  and citing" is false as written: ELA's W.x.8 standard is finding, judging and citing. The section 5 leans point at standards
  (W.7 to W.9, C3 dimension 3, a practice) and not at the skill ids a library row must `assumes` or `~`.
- **Cost:** The progression cannot say who teaches a skill first, so the same skill is owned twice at the same depth (a lens error)
  or library repeats what the grade's ELA course just taught. Stage 2's check "every cross-subject lean points to a skill taught by
  then" cannot run.
- **Fix (replace STANDARD.md section 5 opening, ours, untested):**

> **Who teaches what first.** ELA owns the research cycle and the writing of it (core skill `research-cycle`; rows
> `e1-shared-research` to `e12-research`), the first source list (grade 4, `e4-research`), locating print and digital sources with
> key words (grade 5, `e5-locate-sources`), source credibility in writing (grade 6, `e6-short-research`) and a standard citation
> format (grade 7, `e7-research-questions`). Social studies owns sourcing and corroboration (`source-sourcing`, `corroboration`, from
> grade 2) and news reading (`ss8-news-literacy`, grade 8; `us1-news-reading`, grade 11). Library owns what neither does:
> searching as a skill (query changes, catalogues and databases, click restraint), leaving the page to check who is behind it
> (lateral reading, the first time it is taught as a method), going upstream, honest use of others' work across media (not only
> in writing), and choosing among tools. Where a library row meets an ELA or social studies skill it names that row in `cross_subject`
> (`ela:e5-locate-sources`) and either assumes it or is assumed by it; the progression says which came first in each grade.

  The writer must then re-read the 3 to 5 and 6 to 8 emphasis cells against ELA grades 4 to 7 before the progression is drafted.
  Confidence: Firm.

### 2. No rule gives each of 68 ungraded competencies one owning grade, and the gate does not know library

- **Where:** STANDARD.md section 1 ("The same 68 apply K to 12"), section 3 (K to 2 "all six foundations, at the 'with help' level");
  scripts/progression.py (STD_FILES, ANCHOR, code_grades have no library entry; the ownership check reports a code owned by more than one grade
  and an anchor code owned by none, unless it is in `data/progressions/library-excluded.csv` with a reason).
- **What is wrong:** The page implies all 68 are met in every course. The gate wants each id owned once (or excluded with a reason) and
  `~ID` elsewhere. The course shape also makes the grade axis unclear: K to 5 are single-grade courses, 6 to 8 and 9 to 12 are band courses,
  but the progression csv has a `grade` per row, K to 12. A writer has no rule for whether a 6 to 8 course owns at grade 6, 7 or 8.
- **Cost:** Three writers will make three progressions (68 owned rows at K; 68 x 8 duplicate rows the gate rejects; or ids owned at the band
  end only). Criterion 2 ("each grade has named priority skills") has no place to be traced.
- **Fix (add to STANDARD.md section 3, ours, untested, pending Cory):**

> **Ownership.** Each of the 68 ids is owned by exactly one grade, the grade where it is first met at the depth a check can score on its
> own (not the "with help" level); every other grade where the course returns to it carries `~ID` with a one-line note on how that year
> differs. Grades 6 to 8 and 9 to 12 each get a row per grade (6, 7, 8; 9 to 12) even though the course is one: the progression grades are
> the school years, the course is how they are taught. A competency can be owned in K to 5 by the course of that year. Each row's
> `assumes` names the earlier library row or an ELA or social studies core skill (finding 1).

  The gate needs: `'library': ['aasl-2018.txt']` in STD_FILES, `'library': 'aasl-2018.txt'` in ANCHOR, `code_grades('library', code)` returning
  `None` (the id carries no grade, so any grade may own it and the one-owner check does the work), and a `library-excluded.csv` with a reason per
  excluded id (finding 3). Confidence: Firm that a rule and gate entries are missing; the single-owner form is a Judgment call (see question 1).

### 3. About 30 of the 68 competencies are outside research, and section 4 leaves them out by theme, not by id

- **Where:** STANDARD.md section 4 (leaves out reading promotion, the design strand, the librarian frameworks) and the bar's C1 ("every standard
  of the course is named and taught in full").
- **What is wrong:** By id, the Include foundation (II, 11 ids: awareness of contributions of different learners, weighing viewpoints,
  conversation, reflecting on one's place), the Collaborate foundation (III, 9 ids: group work, communication tools, feedback), and the Explore
  domains B, C and D (V.B.1 and V.B.2 design cycles and persistence, V.C.1 to V.C.3 curiosity and innovation, V.D.1 to V.D.3 resilience and feedback)
  are mostly not search, judging or citing. V.A.1 (reading widely and deeply in multiple formats) is reading promotion; VI.D.3 is inspiring others
  to engage. Section 4 excludes the themes "reading promotion" and "design thinking", but the gate and C1 work on ids. As written, either 30 ids are
  taught as library (and overlap SEL, ELA speaking, CS and science), or the gate fails them as unowned, or someone excludes them silently.
- **Cost:** Criterion C1's door ("any standard lacks a lesson, practice or a check item") is the first one a reader tests. A reader tracing II.B.2 or V.B.1 finds nothing.
- **Fix (add to STANDARD.md section 4, ours; the list is a proposal for Cory, question 2):**

> **Ids met through research, not excluded.** Each of the 68 is either owned by a library row, carried as `~` on a research task (for
> example II.B.2, weighing perspectives, on the day two sources disagree; III.C.1, feedback, on the revise day of a research product), or excluded
> with a reason in `data/progressions/library-excluded.csv`. The ids proposed for exclusion, each owned instead by the subject named: V.B.1
> and V.C.2 (science and computer science design cycles), V.A.1 (ELA wide reading), V.D.1 and V.D.2 (SEL self-management), III.A.1 and III.D.2
> (SEL relationship skills). Everything else is met through a research task.

  Confidence: Firm that the gap exists; which ids go where is a Judgment call.

### 4. The standard is not yet in our own words at the competency level

- **Where:** data/standards/aasl-2018.txt (ids only); STANDARD.md section 1 ("the repo holds ids and our own words, never the competency text").
- **What is wrong:** The brief's check is that the standard is "in our own words". The page says the repo holds our own words, but it holds none: no gloss
  for any of the 68. Health, SEL, arts and computer science each have an own-words file (casel-5.txt, nhes-2024.txt, ncas-performance-standards-words.txt,
  csta-2026-statements.txt). Nothing here is copied, which is safe, but a progression writer reading only `AASL.IV.B.3` learns nothing. The 2018 and
  2025 text differs in places (the file says "rewords some competencies (e.g. I.A.2)"), so the writer cannot recover it from memory either.
- **Cost:** The writer will open the framework PDF or paraphrase from memory, and the risk of near-copying grows. Reviewers cannot trace "taught at the depth the wording asks" (C1) without a stated wording.
- **Fix:** Write `data/standards/aasl-words.txt` (id, tab, one skill phrase in our own words, 8 to 15 words, an action and an object, not a rewording of the sentence).
  Example of the grain, ours: `AASL.IV.B.3<TAB>Question each source's maker and purpose before trusting what it says.`
  See question 3 on the licence stance. Confidence: Firm.

### 5. The approach page fills about half of the plan fields, one field number is wrong, and C7 has no rule

Compared with docs/courses/health/APPROACH.md, docs/courses/sel/APPROACH.md and the field lists in docs/courses/UNIT-PLAN.md (unit fields 1 to 10, section fields 1 to 11):

| Slot | Library page | Gap |
|---|---|---|
| Kinds of day | Filled (five, in library's words) | Check kind: "Assessment day" reads fine; none |
| Daily evidence | Filled | K to 2 evidence is a class checklist; say where it lives and that it is thrown away at unit end (sel precedent, promise 2) |
| Unit field 2 | Filled | Add: the day the model is withdrawn; the host task's fallback (finding 9) |
| Unit fields 3 to 10 | Not stated | where it sits, readiness item, end-of-unit assessment form (a search or judgement actually done), error register, response allocation, tools and supplies, family note, sources |
| Section field 1 | "what the teacher page explains" | Field 1 is standards and practices, not the teacher page; move the line to the unit teacher page and write field 1 as: the AASL ids and the priority skill, the skill as an adult uses it |
| Section field 2, 7, 8, 10, 11 | Not stated | where it sits; talk and writing (search-aloud routine, sentence frames); practice that returns; two rooms (a parent at a table, one projector, no devices); not in this section |
| Section field 9 | "free sources only; dated captures" | Field 9 is supports and extension (English learners, access, reading load, extension). Move the free-sources line to field 6 or the tools slot and write field 9 in full |
| What is carried and fading (C7) | "the research notebook, returned to" | No day names who holds the model and when it is withdrawn. A student must first search with the teacher, then in pairs with a step card, then alone, the card withdrawn on a named day |
| What a tool may and may not do | Missing | See below |
| Sensitive ground | Missing | See finding 7 |
| Pacing and dose | Missing | See finding 6 |
| Evidence and sources (C13, C16) | Only the scout and lens mention it | Needs a short section: what was read in full, what is from memory, no claim of effect, logic model pointer |

- **What a tool may and may not do (add, ours):**

> A tool may give practice on an invented set of pages, searches and sources (a closed set, so every result is the same for every student),
> check a citation against a model, sort claims into "checked" and "not yet checked", and keep a private research notebook on the device. It may not
> use the live web or a real search service, record what a student searches for or types, give a verdict on a real site, or write the student's
> notes or product.

- **Fix (the kind-of-day opening and the fade rule, paste into "What library adds to the plan fields", ours):**

> **What is carried and when it fades.** The unit's skill card (the steps of the one search, check or citation move the unit teaches) is held by
> the teacher on the first Show-me day (thinking aloud on an invented case), by pairs on the first Practice day, and withdrawn on the first Inquiry day,
> which the section plan names. The unit check is taken without it. A skill returns in later units with the card for one day, then without it. K to 2
> use the same steps as three or four pictured words said aloud.

  Confidence: Firm.

### 6. The dose is not stated, three pacing statements disagree, and no time figure is cited

- **Where:** APPROACH.md header ("one or two sessions a week all year (Cory, 2026-11-15)"); STANDARD.md section 3 and APPROACH.md "Questions" (6 to 8 and
  9 to 12 about one session every two weeks, 2026-11-16); the bar pass rule ("each SEL and library course runs the whole year at one or two sessions a week").
- **What is wrong:** There is no sessions-per-year or minutes-per-session figure for any band. The sentence in the bar contradicts the later decision: one course
  for 6 to 8 that spreads across three grades at one session every two weeks is about 18 sessions a year and 54 over the course. Whether "the year" in "a unit
  runs at least one full inquiry cycle" is a school year or three of them is not said. I searched for a national or professional figure: the AASL scheduling
  position statement (revised 2019, "responsive scheduling") gives no minutes per week that I found; so none can be cited, and the page must say that.
  One research figure exists for the high school method: the 2022 field study used six 50-minute lessons (Stanford release, by search result; the journal
  article was not re-read), so a 9 to 12 course must reach at least about 5 hours of lateral reading across its four years.
- **Cost:** A frame writer cannot compute days or the short path (C2), and the 6 to 12 courses may not fit a full cycle per unit.
- **Fix (add a "Pacing and dose" section to APPROACH.md, ours and untested; Cory decides raises):**

> **Pacing and dose.** Settled 2026-11-15 and 2026-11-16 (Cory): K to 5 meet one or two sessions a week; 6 to 8 and 9 to 12 about one session every two
> weeks across their grades. Default time, ours and untested: K to 2, 30 sessions a year of 25 minutes (about 12.5 hours); 3 to 5, 30 sessions of 35 minutes
> (about 17.5 hours); 6 to 8, 18 sessions a year of 45 minutes (about 13.5 hours a year, 40 over three); 9 to 12, 18 sessions a year of 45 minutes (about 13.5
> hours a year, 54 over four). A frame may change these with a reason. No national or professional body publishes a time figure for library instruction
> that we found (the AASL scheduling position statement gives none, searched 2026-11-20); the only time figure behind any method here is the 2022 lateral
> reading field study (six 50-minute lessons, high school, from the news release; the article was not re-read), so the 9 to 12 course must hold at least that
> much lateral reading and claims no more.

  Also change the bar's pass-rule sentence to "one or two sessions a week, or about one every two weeks in the two band courses (its frame states which)". Confidence: Firm.

### 7. Sensitive ground is not named anywhere

- **Where:** STANDARD.md and APPROACH.md (no section); the lens (no section on it); the bar C12.
- **What is wrong:** Library research is the subject most likely to put a child in front of live, uncurated content. The pages name no sensitive ground and no read.
- **Cost:** C12 and the pre-work gate ("a sensitivity read where the subject needs one") cannot be met; a later writer has no stop line.
- **Fix (add a "Sensitive ground" section to APPROACH.md, ours):**

> **Sensitive ground, and the read each needs** (fresh-agent read per docs/pipeline/briefs/sensitivity-read.md, kind `sensitivity`, target the unit's case set):
> 1. **Lateral reading cases** about politics, health, elections, religion, identity groups or conflict. Cases are invented or evenly chosen across the political range, and
> hoax or hate pages are described or shown in an invented form, never reproduced. Read: a sensitivity read of every unit's case set (6 to 12).
> 2. **Unsafe or upsetting search results** (adult content, violence, scams). Students use a closed set or a teacher-checked list; the page never sends children into open
> search with no stop rule; the teacher page says what to do if one appears. Read: a sensitivity read of the stop rule and the K to 5 plans.
> 3. **Privacy:** no student gives a name, school, location or photo into a search or a site; a tool stores nothing off the device. Read: an accessibility and privacy check
> by the tools reader.
> 4. **Plagiarism and honest use** taught without shaming (a student who copied is helped to cite, not accused in front of the class). Read: part of the 9 to 12 sensitivity read.
> 5. **Whose voices a source set shows** (C12): the record per unit of whose work and voices appear. Read: the same sensitivity read.
> 6. **Copyright and fair use** as general guidance, never legal advice; no claim that a use is lawful. Read: a rights read.
> 7. **AI-made text and images** as a source (finding 11): no claim that any tool is reliable or unreliable; the method is the same check. Read: a text read of the 9 to 12 plans.

  Confidence: Firm that the section is missing; the list is Likely complete.

### 8. The grade check set covers one of four bands; the "Done" status overstates it, and some claims about the continuum are unverified

- **Where:** STANDARD.md section 2; the bar's library row ("the continuum's grades 3 to 5 list read in full as the grade check set"); the bar part 11 ("To firm it: open the continuum's grade lists").
- **What is wrong:** The progression is to be checked against the continuum's bold skills for every grade. Only 3 to 5 was read cell by cell. PK to 2, 6 to 8 and 9 to 12 were
  only "structure seen", and K to 2 and 9 to 12 are exactly the bands with no other source in the scout. The page also says "four anchor standards" and six phases
  (connect, wonder, investigate, construct, express, reflect). The guide pages I opened (the about, intro and continuum pages) do not list the standards or the phase names, and a
  search summary says the older document had three standards. I could not confirm four. The author line (Stripling) is confirmed by search results for the 2019 reissue, but not on the guide page itself.
- **Cost:** The "check" half of the use rule has no data for most grades. A wrong anchor count would be in a public-facing source line.
- **Fix:** Before the progression, read the other three band files in full and put the result in the table in section 2: for each grade, the priority skills (our words), and a
  row for each place our list differs. Reword section 2 as: "Four anchor standards and six phases, from memory of the 2019 guide, to be confirmed against the band files before this line is used."
  Change the bar and the status row from "Done" to "3 to 5 read; 3 bands owed". Confidence: Firm that three bands are unread; Likely that the count of anchors is right (from memory I recall four in the 2019 version).

### 9. Hosting a unit on another course's task assumes a calendar the library courses do not control

- **Where:** STANDARD.md section 3 (host tasks, bar criterion 4); APPROACH.md ("A unit runs at least one full inquiry cycle on its host task").
- **What is wrong:** A 6 to 8 course that meets about every two weeks, and any course used by one family at home who may not use the other Curio Class courses, cannot count on the science
  investigation or social studies source question happening that week. No fallback is stated.
- **Cost:** A unit with no host task that week is a one-off orientation, the first "fails if" in the bar.
- **Fix (add to APPROACH.md unit field 2, ours):**

> Each unit names the kind of host task and one named example from the grade's core courses (by row id), for the teacher to schedule against. Each unit also carries a stand-alone host
> task of its own (an invented question with a closed source set) so the unit can run when no core task is in step. The scope and sequence records both.

  Confidence: Likely.

### 10. Lateral reading needs real sites, and the house rule forbids company and product names

- **Where:** AGENTS.md ("No company or product names in anything a student, teacher or family reads"); the scout ("named platforms replaced"); APPROACH.md section field 9.
- **What is wrong:** The method names kinds of thing (an encyclopedia site, a fact-checking organisation, a search results page, a social post) and uses real examples. The page says
  captures are "made our own", and the scout says named platforms are replaced, but nothing says whether a student ever searches the real web, and whether an organisation such as a
  public encyclopedia or a fact-checking nonprofit may be named by its own name. The rule as written forbids it.
- **Cost:** The first writer will break either the rule or the method.
- **Fix (add to APPROACH.md, ours; pending Cory, question 4):**

> Practice and check pages use invented sites, invented search results and described captures, with kinds named generically ("an online encyclopedia", "a fact-checking site", "a video site").
> Inquiry days may use the real web under the teacher's guidance and the stop rule (finding 7); the student page then says "your search results" and names no site. A teacher page may say
> "swap in a current case" without naming a product.

  Confidence: Judgment call.

### 11. AI-made content is in the lens and the CS lean, but not in the 6 to 8 and 9 to 12 emphasis, and no CS row teaches it

- **Where:** lens ("copyright, licences, fair use and AI-made text (9 to 12)"); STANDARD.md section 5 ("SOC standards on privacy, data and AI-made content; AI output is a source to be checked"); section 3 table (neither 6 to 8 nor 9 to 12 mentions it).
- **What is wrong:** The CS progression has SOC rows (for example `g3-benefits-risks`, `g4-history-limits`) but none that names AI output as a source (grep: 0 hits for chatbot or AI-made). The lean points to nothing.
- **Cost:** A required modern skill falls between two subjects.
- **Fix:** Add to the 6 to 8 cell "checking text made by a machine like any other source (who made it, what it cites)" and to the 9 to 12 cell the same plus "disclosing its use". Replace the CS lean line with: "CS owns how such tools work in its
  own rows; library owns checking what they produce, and no CS row assumed." Confidence: Likely.

### 12. Course list: one catalogue row for eight courses, no course ids, stale counts

- **Where:** data/courses.csv line 44; STANDARD.md section 3; bar decision 9 ("four courses can proceed"); STANDARD.md section 1 ("data/subjects.csv still labels the library row ... (2018)").
- **What is wrong:** The page lists eight courses but gives them no ids (the plan.py course key). The one catalogue row matches the computer science convention (`cs-k12`), so it is consistent, but the eight course ids that frames will use are unnamed.
  The "four courses" line in the bar is a leftover. The subjects.csv label is already corrected, so the "name lags" note is out of date.
- **Cost:** Frames and the course-status page may use different ids.
- **Fix:** Add to STANDARD.md section 3: "Course ids: `library-k`, `library-1`, `library-2`, `library-3`, `library-4`, `library-5`, `library-6-8`, `library-9-12`." Change the bar's decision 9 to "eight". Strike the subjects.csv lag note.
  Confidence: Likely (the ids are a proposal; the stale lines are Firm).

### 13. Small cross-subject and source accuracy slips

- **Where:** STANDARD.md section 5; the scout; STANDARD.md header.
- **What is wrong:**
  - "W.7, W.8, W.9 at each grade": W.9 (drawing evidence from texts) does not exist before grade 4 (data/progressions/ela.csv notes it at `e3-short-research`; the standards file has no W.K.9 to W.3.9). W.7 and W.8 exist from kindergarten.
  - "Massachusetts news and media literacy (NML) in high school": NML ids are also owned at grade 8 (`ss8-news-literacy`), so the lean can start in 8.
  - "NGSS practice 8" and "science: gathering and judging information": no science progression row names information evaluation (grep, 0), so the lean cannot be tied to a science skill id; name host investigations instead.
  - The header says "PDF dated 2025-09-18": that is the file name's date; the PDF footer says copyright 2026. The ALA store lists the second edition as 2025.
  - The scout's "47 items under CC BY 4.0" and the licence wording were not re-checked by me: the page I guessed at 404, and my one search found the free lesson sets but no licence page. They rest on the scout's own reading of 2026-11-16.
  - The lateral reading study (2022) can now be cited rather than "from memory": the news release confirms about 500 students, six 50-minute lessons, a district-wide study. The journal article itself I did not re-read.
- **Fix:** Edit each line to match; for the scout, add "re-check the licence page at the first adaptation" in its table. Confidence: Firm for the first two bullets and the science lean, Likely for the rest.

## Questions for Cory

1. **Ownership form (finding 2).** The gate wants one owner per id. Recommended: each of the 68 is owned once, at the school year where it is first checked alone, and `~` in other years; the 6 to 8 and 9 to 12 courses get a row per school year. The alternative is to own each id once per course (8 x 68 rows) by changing the gate. Which?
2. **The ids outside research (finding 3).** Recommended: teach every id through a research task except the seven named in the fix (V.B.1, V.C.2, V.A.1, V.D.1, V.D.2, III.A.1, III.D.2), which are excluded with a reason and left to science, computer science, ELA and SEL. The alternative is to exclude all 28 (II, III, V.B to V.D) and name the loss in the part-pass count. Which?
3. **Own-words file and the AASL permission terms (finding 4).** The permissions page allows one competency in a lesson, but says a substantial part of the framework in a derivative work needs permission. Recommended: a gloss of 8 to 15 words per id that names the skill and does not follow the sentence, with no permission request. The alternative is to ask ALA for permission before the file is written. Which?
4. **Naming real sites in student and teacher pages (finding 10).** Recommended: no names; invented sites and generic kinds throughout, with the real web used only on guided inquiry days. The alternative is an exception for public-interest organisations (an encyclopedia, fact-checking nonprofits) named in teacher pages only. Which?
5. **Dose (finding 6).** Recommended: the defaults in the fix (25, 35, 45 and 45 minutes; 30, 30, 18 and 18 sessions a year). Do you want any raised, given that no national figure exists to compare with?
6. **Your yes on the approach page.** It stays a draft until findings 5, 6, 7 and 9 to 11 are in.
