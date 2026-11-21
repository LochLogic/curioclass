# World languages pre-work: second-model cold read, 2026-11-20

> Filed by the lead 2026-11-20. Gemini 4 Neon (medium effort) in Antigravity, pasted by Cory from S:/CurioClass-gemini/ (prompt 10 to 18 for this subject), after it passed calibration (docs/reviews/calibration-*-gemini-2026-11-20.md). Its saved report is S:/CurioClass-gemini/reports/prework-world-languages-read.md; text unchanged here except wording the repository checks flag.

Read as the curriculum expert (docs/agents/EXPERT.md) with the world languages lens
(docs/agents/lenses/world-languages.md). World languages are SHELVED; this read covers the stage 1 pre-work only and
does not propose unshelving, frames or scopes and sequences. I did not write these drafts. Nothing in the repository
was edited; this report is saved to S:\CurioClass-gemini\reports\prework-world-languages-read.md. Confidence is Firm,
Likely or Judgment call on each finding. Anything resting on memory is marked "from memory". I did not open the earlier
first read (docs/reviews/prework-world-languages-read-2026-11-20.md) until my own findings were complete; the comparison
sits at the end under "Against the first read".

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/prework-codex-read.md; docs/agents/lenses/world-languages.md;
docs/courses/world-languages/STANDARD.md; docs/courses/world-languages/APPROACH.md; data/standards/actfl-wrs.txt;
docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, part 6, "Before a scope and sequence in this subject", Decided
item 2, Sources table); docs/COURSE-RUN.md (stage 1); docs/FOUNDATION.md; docs/courses/UNIT-PLAN.md;
docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md (finished examples);
docs/reviews/prework-sel-read-2026-11-19.md (report shape); docs/reviews/world-languages-open-material-2026-11-20.md
and docs/reviews/world-languages-asl-material-2026-11-21.md (base-text scouts;
docs/reviews/world-languages-open-material-2026-11-16.md does not exist); docs/pipeline/briefs/sensitivity-read.md;
data/courses.csv (world-languages rows 36, 37 and 45); scripts/progression.py (lines 1 to 140, including STD_FILES,
ANCHOR and code_grades); scripts/standards.py (lines 80 to 142, LISTED, CLOSED and validate). After my own findings
were fixed: docs/reviews/prework-world-languages-read-2026-11-20.md.

Web search, run today: ACTFL World-Readiness Standards (2015) titles and structure; ACTFL Proficiency Guidelines 2024
(Superior and Distinguished); NCSSFL-ACTFL Can-Do Statements 2026 edition; ACTFL Early Language Learning position
statement (29 July 2012); ACTFL target-language (90 percent) and heritage-speaker position statements (21 May 2010);
ACTFL, LTI and FSI hours-to-proficiency norms for Category I languages (Spanish).

## Verdict

The standards list is real and honest about reuse terms: all 11 World-Readiness standard ids and all 11 ACTFL
proficiency level ids are unique, match the published frameworks, and copy no standard text. The biggest risk is that
the pre-work is not yet runnable by the gates or a planner: STANDARD.md falsely states that scripts/standards.py
accepts actfl-wrs.txt (all 11 WRS ids and 2 ACTFL ids currently fail validation), Cory's 2026-11-21 Option D decision
left direct contradictions in both STANDARD.md and APPROACH.md, and APPROACH.md places two plan fields in the wrong
UNIT-PLAN.md slots while omitting required parts of five others. The one change that matters most is reconciling the
gate specs and post-decision Option D rules (findings 1, 2 and 4) alongside a clean field-by-field fix of APPROACH.md
against UNIT-PLAN.md (finding 3).

## What I counted

| Check | Result |
|---|---|
| Ids in data/standards/actfl-wrs.txt | 22 non-comment lines, all unique: 11 WRS standard ids (`WRS.Communication.1.1` to `WRS.Communities.5.2`) across 5 goal areas, plus 11 ACTFL level ids (`ACTFL.Novice Low` to `ACTFL.Distinguished`) |
| Published framework check (web search) | All 11 WRS titles match ACTFL (2015, 4th ed.); ACTFL Proficiency Guidelines 2024 retain Superior and Distinguished without sublevels; NCSSFL-ACTFL 2026 Can-Do Statements edition confirmed |
| Validator (scripts/standards.py) | `actfl-wrs.txt` is NOT in `LISTED`; `CLOSED` regexes accept only 9 of 22 ids (`ACTFL.Novice/Intermediate/Advanced Low/Mid/High`) and reject all 11 `WRS.*` ids plus `ACTFL.Superior` and `ACTFL.Distinguished` |
| Own-words statement file | None exists for the 11 WRS standards, Spanish sounds/spelling, or the 7 ASL parameters (`actfl-wrs.txt` holds ids only) |
| data/courses.csv world-languages rows | 3 rows (`spanish` k-12, `french` 6-12, `asl` k-12; all `core=n`); `ADOPTION-BAR-SUBJECTS.md` still says 2 shelved courses |
| Option D course count | 12 courses for Spanish and ASL (4 levels plus 2 early-years companions each); French adds 4 courses if kept 6-12 |
| Dose vs ACTFL floor | Default 3 x 35 min/week x 36 weeks = 105 min/week (~63 hours/level, 252 hours across 4 levels); clears ACTFL's 2012 elementary/middle floor (more than twice a week, at least 90 min/week), but no dose is stated for Option D early-years companions |
| Cross-subject leans (13 ids) | Not re-verified by shell grep in this session (see "Not checked"); `scripts/progression.py` lean-timing check will reject level-based rows leaning to grade 5+ core skills unless exempted |
| Progression gate (scripts/progression.py) | No `world-languages`, `spanish`, or `asl` entry in `STD_FILES`, `ANCHOR`, or `code_grades` |

## Findings, most serious first

### 1. STANDARD.md falsely states that scripts/standards.py validates actfl-wrs.txt; 13 of 22 ids currently fail

- **Where:** STANDARD.md section 1 ("Validator", lines 47 to 48); scripts/standards.py lines 97 to 111 and 137 to 142;
  data/standards/actfl-wrs.txt.
- **What is wrong:** STANDARD.md says: "scripts/standards.py reads actfl-wrs.txt as an id list, so every full id is
  valid as listed (the file was loaded 2026-10-27; this pre-work did not re-run the gate)." In scripts/standards.py,
  `actfl-wrs.txt` is not in `LISTED` (lines 97 to 104). Instead, `CLOSED` (lines 110 to 111) defines
  `'ACTFL': re.compile(r'ACTFL\.(Novice|Intermediate|Advanced) (Low|Mid|High)')` and
  `'World-Readiness': re.compile(r'WRS\.(Communication|Cultures|Connections|Comparisons|Communities)')`. As a result,
  `validate()` rejects all 11 numbered `WRS.<goal area>.<n.n>` ids (such as `WRS.Communication.1.1`) and rejects
  `ACTFL.Superior` and `ACTFL.Distinguished`. Only 9 of the 22 ids in `actfl-wrs.txt` currently pass.
- **Cost:** Every world-languages progression row, frame, unit plan and day citing any of the 11 standard ids will fail
  the standards gate as soon as the pass opens, and a writer reading STANDARD.md will assume the gate is already wired.
- **Fix (replace the "Validator" bullet in STANDARD.md section 1; ours, untested):**

> - **Validator.** `scripts/standards.py` does not yet read `data/standards/actfl-wrs.txt` in `LISTED`. Its `CLOSED`
>   patterns accept only bare goal-area names (`WRS.Communication`, etc.) and the nine Novice to Advanced sublevels;
>   all 11 numbered `WRS.*` ids plus `ACTFL.Superior` and `ACTFL.Distinguished` currently fail `validate()`. Before any
>   world-languages progression or frame runs, add `('World-Readiness', 'actfl-wrs.txt')` to `LISTED` in
>   `scripts/standards.py` (keeping the `CLOSED` patterns only if `data/modules.csv` still uses bare goal-area codes).

- **Confidence:** Firm.

### 2. Cory's 2026-11-21 Option D decision left direct contradictions across STANDARD.md and APPROACH.md

- **Where:** STANDARD.md header table (lines 11, 16), section 5 (lines 107 to 108, 123 to 132), section 6 (lines 151
  to 158), and "Questions for Cory" (lines 217 to 240); APPROACH.md "Pacing and dose" (lines 180, 191 to 192).
- **What is wrong:** On 2026-11-21 (Desk `q-prework-open-2`), Cory chose **Option D** (four levels per language plus an
  early-years companion for Levels 1 and 2, 12 courses for Spanish and ASL) and approved APPROACH.md as pre-work.
  Several older lines were left in place and now contradict that decision:
  - APPROACH.md line 180 says "Settled by no one yet (question 7 in STANDARD.md)" right above line 191 "**Dose by
    level** (Cory, 2026-11-21)".
  - APPROACH.md line 192 says "a K to 5 learner has the same course at the same dose", directly contradicting Option D's
    early-years companion for Levels 1 and 2.
  - STANDARD.md section 5 lines 107 to 108 still say "a grade 3 learner and a grade 9 learner at the same level use the
    same course, with age-tuned topics and tasks".
  - STANDARD.md section 5 lines 123 to 125 only specify Option B's course ids (`spanish-1` to `spanish-4`, `asl-1` to
    `asl-4`) and never name the four early-years companion course ids, their grade range (`k-5` vs `6-12` for the main
    track), or whether French (`6-12` in `data/courses.csv`) gets four courses only.
  - STANDARD.md header table lines 11 and 16 still mark the level split and APPROACH.md as waiting on Cory, and
    "Questions for Cory (as asked)" lists all 11 questions without marking questions 1 to 3 and 5 to 11 closed (only
    question 4 stays open, alongside the new ASL questions in `docs/reviews/world-languages-asl-material-2026-11-21.md`).
- **Cost:** A future writer opening the pass will not know whether K to 5 learners take the same course or an
  early-years companion, what course ids to create in `data/courses.csv`, or what dose the early-years companions use.
- **Fix (apply in STANDARD.md and APPROACH.md; ours, untested):**
  In STANDARD.md header table, update row 1 to `Option D chosen (Cory, 2026-11-21): 4 levels plus early-years
  companions for Levels 1 and 2` and row 6 to `APPROACH.md approved as pre-work (2026-11-21); lens and two scouts
  written`. Replace STANDARD.md section 5 lines 107 to 108 and 123 to 132 with:

> **Levels, not grades, with an early-years companion (Option D, Cory 2026-11-21).** Learners in grades 6 to 12 take
> Levels 1 to 4 (`spanish-1` to `spanish-4`, `asl-1` to `asl-4`, grades `6-12`), targeting Novice Mid, Novice High,
> Intermediate Mid and Intermediate High. Learners in K to 5 start in the early-years companions (`spanish-k5-1`,
> `spanish-k5-2`, `asl-k5-1`, `asl-k5-2`, grades `k-5`), targeting the same Level 1 and Level 2 proficiency goals
> through play, song, movement and short pictured texts; K to 5 learners who finish both companions move to Level 3.
> That gives 12 courses for Spanish and ASL. French (`6-12` in `data/courses.csv`) stays four courses (`french-1` to
> `french-4`) behind Spanish and ASL when the pass opens, with no early-years companion unless Cory adds K to 5 French.

  In APPROACH.md "Pacing and dose", delete "Settled by no one yet (question 7 in STANDARD.md)." on line 180, and
  replace "a K to 5 learner has the same course at the same dose" on line 192 with "The early-years companions (Option
  D, K to 5 Levels 1 and 2) use a stated K to 5 dose (pending Cory's pick, Question 2 below)."
- **Confidence:** Firm.

### 3. APPROACH.md puts two plan elements in the wrong UNIT-PLAN.md fields and drops required parts of five others

- **Where:** APPROACH.md "What world languages add to the unit and section plan fields" (lines 47 to 86) and "Error
  register in this subject" (lines 148 to 154), checked field by field against `docs/courses/UNIT-PLAN.md` ("The unit
  plan: fields, in order", lines 151 to 224; "The section plan: fields, in order", lines 230 to 280).
- **What is wrong:** Checked field by field:
  - **Unit field 2 (Standards, limits, what is carried):** omits **limits** (what grammar and text types stay out of
    the level), omits the **withdrawal day** of what is carried (which was placed in Unit field 7 instead), omits the
    rule-15 no-quote override (ACTFL standard text is all rights reserved, so plans state each standard in our own
    words rather than quoting verbs), and writes "the World-Readiness standards" on a teacher-facing unit plan when
    STANDARD.md lines 42 to 43 say public pages say "world language standards" and give the id.
  - **Unit field 4 (Readiness check):** omits the required `UNIT-PLAN.md` first-line gate token (`Given:`,
    `Retrieval only:`, or `Start-of-year check:`, which `scripts/unitplan.py` requires) and does not state that Level 1
    Unit 1 assumes no prior target-language rows.
  - **Unit field 6 (Error register):** line 153 puts "and a remedy" in Unit field 6. In `UNIT-PLAN.md`, Unit field 6
    holds the error, what it shows, and its source; the wrong-beside-right example and five-to-ten-minute remedy sit in
    **Section field 4** (except in a merged one-section unit).
  - **Unit field 7 (Response allocation):** **wrong placement** for the frame withdrawal day ("The withdrawal day for a
    frame is the unit's second Application day at Level 1 and 2, its first at Level 3 and 4" belongs in Unit field 2
    and Section field 5, not Response allocation). Also omits **response time** (separate from marking time) and how
    the **interpretive (understand) task** is marked. In addition, "about one minute a learner for each judged task"
    for both exchange and presentation tasks equals 50 minutes for a 25-student class, exceeding a 35-minute session
    without saying how marking fits (e.g. rotating pairs across two days or scoring during partner rounds).
  - **Unit field 8 (Tools and supplies):** **wrong placement** for "the room (a class, a small group, a home table)",
    which belongs in **Section field 10** (Two rooms). Also **drops** the unit's **tools list** (each tool with day,
    mark, job, spec verdict, and link to `TOOL-ASKS.md`).
  - **Section field 1 (Standards and practices):** **drops** the section's **standard codes, share of each standard,
    and limits that bite here** (lists only "before you teach" and sensitive ground).
  - **Section field 3 (Checks, written first):** **drops** the **numbers of the unit assessment items this section
    owns**.
  - **Section field 5 (What is carried, and instruments):** **drops** the **instruments** block (each key moment, ideal
    instrument, spec verdict, link to `TOOL-ASKS.md`) and **what a room with nothing does** (the paper path, C14), and
    lacks the withdrawal-day rule currently misplaced in Unit field 7.
  - **Section field 6 (Days):** omits the "who holds what is carried" column from the day-row list.
- **Cost:** Every unit plan and section plan written from APPROACH.md will place withdrawal days and room notes in the
  wrong fields, fail `scripts/unitplan.py` checks on field 4, and omit tools, paper fallbacks, standard limits and
  owned assessment item numbers.
- **Fix (replace the corresponding bullets in APPROACH.md lines 52 to 86; ours, untested):**

> - Unit field 2: the world language standard ids the unit teaches, stated in our own words (never quoting ACTFL
>   wording; rule 15 override); the level's limits (structures and text lengths kept out of this level); the theme and
>   real-world task; the structures, words and (ASL) parameters taught; what is carried (frame, word cards, sign set),
>   tied on day 1 and withdrawn on the unit's second Application day at Level 1 and 2, or its first Application day at
>   Level 3 and 4.
> - Unit field 4: `Given:`, `Retrieval only:` or (in Level 1 Unit 1, which assumes no prior target-language rows)
>   `Start-of-year check:` on the first line; a short understand-and-reply task on the words and structures the unit
>   builds on; the ten-minute reteach models the earlier structure again.
> - Unit field 6: the error register (lettered once per unit, one mistake per letter, what it shows, and source or
>   "from memory"; the wrong-beside-right example and five-to-ten-minute response sit in Section field 4).
> - Unit field 7: marking time and response time stated separately, and whether response sits inside the Check day or
>   on a separate Respond day. Short interpretive items are marked against a key (five minutes); exchange and
>   presentation tasks are teacher-judged against look-fors (no hands-up self-marking), scheduled across partner rounds
>   or two Check days so marking fits the 35-minute period (about one minute a learner per judged task). Respond-day
>   groups come from the sheet's "not yet" cells by structure, capped at four groups; the rest rehearse in pairs.
> - Unit field 8: each tool with its day, mark (key or light), job, spec verdict and link to `TOOL-ASKS.md`; supplies
>   (word cards, frames, model text by title and record, or printed sign chart; no product or program names).
> - Section field 1: the standard ids and this section's share in our own words; limits that bite here; connections;
>   before you teach (the structure, sound or parameter explained at adult level; any sensitive ground and reporting
>   route).
> - Section field 3: the numbers of the unit assessment items this section owns, then the day's evidence as above, with
>   look-fors per level.
> - Section field 5: what is carried (the model, frame, word cards or sign set), who holds it each day, and the named
>   withdrawal day (second Application day at Level 1 and 2; first at Level 3 and 4); each key moment with ideal
>   instrument, spec verdict and link to `TOOL-ASKS.md`; what a room with nothing does (printed chart, partner cards).
> - Section field 6: days: goal in student words, kind, opening (see "How a day opens"), who holds what is carried,
>   tool by part (mark, job, minutes) or "None", work by hand, evidence by its number in field 3.

- **Confidence:** Firm.

### 4. The ownership and gate spec in STANDARD.md section 6 has four gaps that would block a progression writer

- **Where:** STANDARD.md section 6 ("Ownership for the gate", "What scripts/progression.py would need", and
  "Cross-subject leans", lines 151 to 173); `scripts/progression.py` lines 30 to 34, 47 to 75, 87 to 140.
- **What is wrong:** Four concrete gaps remain in section 6:
  1. **No ownership rule for Option D early-years companions.** Section 6 maps "Level 1 to Level 4 map to positions 1
     to 4" for `spanish` and `asl`, but says nothing about the four early-years companion courses (`k-5` Levels 1 and
     2). A writer will not know whether the companions share the Level 1 and Level 2 progression rows or own separate
     rows.
  2. **Contradictory `STD_FILES` / `ANCHOR` keys.** Line 152 says each language is its own subject key (`spanish`,
     `asl`), while line 159 asks for "a `world-languages` entry in STD_FILES and ANCHOR". In `scripts/progression.py`,
     every progression file `data/progressions/<subject>.csv` looks up its own key in `STD_FILES` and `ANCHOR` (as
     `'health'` and `'physical-education'` do). The keys must be `'spanish'` and `'asl'` (and `'french'` later), not
     `'world-languages'`.
  3. **Cross-subject lean timing will fail the gate.** `scripts/progression.py` lines 30 to 34 fail any `cross_subject`
     lean whose target core skill sits at a later grade than the leaning row's grade (unless marked `Just in time:`).
     If Level 1 to Level 4 map to positions 1 to 4, then leaning from Level 1 to `e3-word-strategies` (grade 3) or
     `ss4-regional-cultures` (grade 4), or from Level 3 to `e6-word-strategies` (grade 6), `e9-sl-presentation` (grade
     9), `us1-immigration` (grade 11) or `wh1-geography-shapes-contact` (grade 9), will fail the gate as forward leans.
     Section 6 does not list this gate change.
  4. **Missing strand id files in the owed list.** Line 155 to 156 says Spanish sounds/spelling and the seven ASL
     parameters "get their own id file, one id each", yet neither file exists and neither is listed in STANDARD.md's
     header "Owed" table.
- **Cost:** Stage 2 (`progression.py check`) will fail on every cross-subject lean and on subject-key lookup, and two
  writers will handle Option D early-years companions differently.
- **Fix (update STANDARD.md section 6 lines 151 to 162; ours, untested):**

> - **Ownership for the gate** (ours, untested). Each language is its own subject key in the progression (`spanish`,
>   `asl`, and `french` later), so each owns the 11 `WRS` ids once. A WRS id is owned by Level 1 of that language as
>   "met at Novice Mid depth"; Levels 2 to 4 carry it as `~ID` with a one-line note naming the harder function, context,
>   text type and control (see the depth ladder). Option D's early-years companions (K to 5 Levels 1 and 2) are
>   age-tuned course frames for the same Level 1 and Level 2 progression rows, not separate owners. The 11 `ACTFL.*`
>   level ids are excluded with the reason "a proficiency scale used to name each level's exit target, not a skill".
>   Strands (Spanish sounds and spelling; the seven ASL parameters) each get their own id file before stage 2 opens,
>   one id each, owned by the level that first teaches them. For the gate, `L1` to `L4` replace `K` to `12` as the
>   ordered level list for these subjects, with handoffs checked between adjacent levels (`L1` to `L2` to `L3` to `L4`).
> - **What `scripts/progression.py` needs:** entries for `spanish` and `asl` (not one `world-languages` key) in
>   `STD_FILES` and `ANCHOR` (reading `actfl-wrs.txt` with `ACTFL.*` ids in `ANCHOR_SKIP` or `<subject>-excluded.csv`,
>   plus each language's strand id file once created); a per-subject level list `['L1', 'L2', 'L3', 'L4']` in place of
>   `GRADES`; a `code_grades` rule returning `(['L1'], ['L1', 'L2', 'L3', 'L4'])` for WRS ids; and an exemption from
>   grade-order `cross_subject` lean timing for level-based subjects (so teacher-pointer leans to K to 12 core skills
>   verify that the target id exists without comparing level position to grade number).

  Add "Create strand id files (Spanish sounds/spelling; 7 ASL parameters) and own-words WRS file" to STANDARD.md's
  header "Owed" table.
- **Confidence:** Firm.

### 5. No depth ladder, no own-words statement file for the 11 WRS standards, and no stated text-length ceiling per level

- **Where:** STANDARD.md sections 1, 5 and 6; APPROACH.md "Supports" (line 95: "a text of at most the level's stated
  length, with a picture for every line at Level 1").
- **What is wrong:** Three linked planning pieces are missing:
  1. **No depth ladder.** Section 6 says Levels 2 to 4 carry each `WRS` id as `~ID` with "the harder function, context,
     text type and control (the depth ladder, which is the real progression)", yet no depth ladder is written in
     STANDARD.md or APPROACH.md. A writer cannot tell what function, context, text type or control separates Level 1
     from Level 2, 3 or 4.
  2. **No stated text-length ceiling per level.** APPROACH.md line 95 sets reading load to "a text of at most the
     level's stated length", but neither page states a length for any level.
  3. **No own-words statement file for the 11 WRS standards, and no check rule for Communities 5.1 and 5.2.** Unlike
     CASEL, NHES and NCAS, `actfl-wrs.txt` holds ids only. Without our own-words statements breaking out each
     standard's parts (for example, Interpretive covering listening/reading/viewing; Presentational covering informing,
     explaining, persuading and narrating; Communities 5.1 school and global communities; 5.2 goal-setting and
     reflection), a progression writer cannot verify C1 (every part of each owned id taught and checked). STANDARD.md
     lines 136 to 137 rightly flag that Communities 5.1 and 5.2 are hard for a free site, but give no concrete rule for
     how Level 1 owns and checks them without failing C1.
- **Cost:** C1 (every part of every standard taught at depth), C4 (progression across levels) and C10 (reading load)
  cannot be checked consistently across units.
- **Fix (add to STANDARD.md section 6; ours, untested, to be checked against the full 2015 standards and 2024
  guidelines when the pass opens):**

> **Depth ladder and text-length ceiling by level (ours, untested):**
> - **Level 1 (exit Novice Mid):** memorized words, chunks and formulaic phrases on familiar self, family, school and
>   daily topics; short captions or 3 to 5 simple sentences with a picture per line; intelligible to a sympathetic
>   listener.
> - **Level 2 (exit Novice High):** phrases and simple sentences with emerging original combinations on everyday
>   routines, community and short cultural texts; short paragraphs of 5 to 8 sentences with picture and gloss support.
> - **Level 3 (exit Intermediate Mid):** strings of sentences and connected paragraphs, asking and answering original
>   questions in familiar and some new contexts (present, past and future time frames emerging); authentic texts of 1 to
>   3 short paragraphs (about 100 to 200 words).
> - **Level 4 (exit Intermediate High):** connected paragraphs with narration, explanation and supported opinion across
>   time frames on wider cultural and global topics; authentic texts of 200 to 400 words.
>
> **Communities 5.1 and 5.2 (C1 check rule):** 5.1 is taught and checked inside the classroom and school community
> (using the target language for a real class or school product or exchange, plus reading or viewing authentic community
> media); 5.2 is taught and checked through the learner's unit self-check against our can-do paraphrases and a one-line
> goal for the next unit. Write an own-words statement file (`data/standards/actfl-wrs-words.txt`) listing each of the
> 11 standards' parts before stage 2 opens.

- **Confidence:** Firm that the three pieces are missing; the specific word counts are a Judgment call.

### 6. The Level 4 exit target (Intermediate High) does not fit the default dose (252 cumulative hours)

- **Where:** STANDARD.md section 5 (lines 130 to 132); APPROACH.md "Pacing and dose" (lines 191 to 196).
- **What is wrong:** Default dose is 3 sessions of 35 minutes a week for 36 weeks = 63 hours per level, or **252
  cumulative hours** across Levels 1 to 4. Published intensive-study estimates citing ACTFL, Language Testing
  International (LTI) and FSI norms for Category I languages (Spanish) put **Intermediate Mid** at roughly **240
  intensive class hours** and **Intermediate High** at roughly **480 intensive class hours** (and non-intensive school
  classes generally accumulate proficiency more slowly per hour). APPROACH.md honestly notes that "the hours are not
  shown to reach the exit sublevels", which protects C16, but setting Level 4's stated exit target at Intermediate High
  on 252 hours builds a structural mismatch into the course frame before stage 3 begins. In addition, Option D's
  early-years companions have no stated dose.
- **Cost:** A school running the default 63 hours/level schedule will fall far short of Intermediate High by Level 4,
  and a state reviewer checking feasibility (C14) and target alignment (bar part 6, item 1) will flag the mismatch.
- **Fix:** Read the CASLS hours-to-proficiency paper (`TBQHoursToReachIH.pdf`) before stage 3 opens, and bring the
  dose-versus-target choice to Cory (Question 3 below): either adjust the 63-hour-per-level exit ladder to Novice Low,
  Novice Mid, Novice High and Intermediate Mid (noting that Intermediate High requires a daily-period high school
  track), or set high school Levels 1 to 4 to a daily-period default (about 135 hours a level). Add a stated dose for
  Option D's early-years companions (Question 2 below).
- **Confidence:** Likely.

### 7. Sensitive ground and read rules contain one contradiction and three gaps

- **Where:** APPROACH.md "Sensitive ground and which reads it needs" (lines 156 to 176) and Section field 1 (lines 71
  to 72); docs/FOUNDATION.md section 7 item 3 (lines 124 to 141); docs/pipeline/briefs/sensitivity-read.md.
- **What is wrong:**
  1. **Contradiction on Spanish human reader:** APPROACH.md lines 174 to 175 say: "A person (a Deaf ASL teacher; a
     Spanish-speaking teacher) reads before anything ASL becomes public (question 4), as the brief itself can only stand
     in for outside readers." `FOUNDATION.md` line 136 already settled that Spanish is an **agent read** (the `spanish`
     agent), and STANDARD.md Question 4 asks only about a Deaf ASL teacher for ASL. Listing a Spanish-speaking teacher
     as a required human reader contradicts FOUNDATION.md and does not match the sentence's own scope ("before anything
     ASL becomes public").
  2. **Missing `rights` read:** APPROACH.md lines 172 to 174 name `sensitivity`, `spanish` and `text` reads, but omit
     the `rights` read from `docs/pipeline/briefs/sensitivity-read.md`. Both base-text scouts establish that authentic
     Spanish texts, audio and any open ASL graphics come from outside sources item by item and need licence
     verification on the day of use.
  3. **Missing reporting route and leave-out rule:** APPROACH.md names sensitive ground (immigration status, family
     privacy, colonial history, religious holidays, contested Deaf history including oralism and cochlear implants) and
     points Section field 1 to sensitive ground, but never states the teacher's **reporting route** if a learner
     discloses unsafe home or immigration distress (compare `health/APPROACH.md` and `sel/APPROACH.md`), nor states
     whether a **leave-out note** applies to units touching contested Deaf history, colonial history or religious
     holidays (per `ADOPTION-BAR-SUBJECTS.md`, "each course page says what a school may leave out").
- **Cost:** A writer following APPROACH.md will stall Spanish units waiting for an unplanned human reader, skip the
  `rights` check on authentic texts and audio, and leave teachers without a reporting route or clear leave-out rule.
- **Fix (replace APPROACH.md lines 172 to 176; ours, untested):**

> - **Teacher note, reporting route and leave-out.** Every unit touching sensitive ground carries a Section field 1
>   teacher note naming what may come up and how to handle it, plus the school's duty-to-report route (and, for a
>   parent at home, the national child-help and crisis lines by purpose) if a learner discloses harm. Cultural and
>   historical units are not opt-out units, and no learner is asked to share personal or family status; each course page
>   states what a school may adapt or leave out, and the Unit field 9 family note previews any unit covering colonial
>   history, religious holidays or contested Deaf history.
> - **Reads** (docs/pipeline/briefs/sensitivity-read.md): a `sensitivity` read for each unit's cultural texts
>   (community: the speakers of the variety or the Deaf community); a `spanish` read for all Spanish text, audio scripts
>   and family notes (agent read per FOUNDATION.md section 7); a `text` read and a `rights` read for every authentic
>   text, audio clip and outside image. For ASL drawings and Deaf cultural text, a Deaf ASL educator reads before
>   anything becomes public (STANDARD.md Question 4, still open); the agent `sensitivity` read checks wording only.

- **Confidence:** Firm.

### 8. Supports (C11) omits how to tell a language gap from a content gap, and Spanish home-table exchange needs the same caveat as ASL

- **Where:** APPROACH.md "Supports" (lines 93 to 99) and Section field 10 (lines 82 to 85); `ADOPTION-BAR-SUBJECTS.md`
  C11.
- **What is wrong:**
  1. C11 fails if "Nothing helps the teacher tell a language gap from a content gap." APPROACH.md's Supports section
     names 6 to 8 words in depth, reading load, check accommodations and extension, and correctly directs learners
     without English or Spanish home support to the picture-and-model route, but includes no key line helping the
     teacher separate a **target-language form gap** (or an **English-instruction gap** for an English learner) from a
     **task or cultural-content gap**.
  2. Section field 10 says a parent who does not know Spanish can "do the exchange together even if the parent does not
     know the language, using the page's model". If the parent only reads scripted lines from the page, that is a
     scripted dialogue, which bar part 6 item 7 says does not count as an interpersonal exchange. APPROACH.md already
     states the honest caveat for ASL ("no exchange is claimed when no one in the room signs"); Spanish needs the same
     honest line (or a picture-based information-gap card paired with the audio model).
- **Cost:** C11 could lose a mark at review, and a home-table Spanish lesson could claim an unrehearsed exchange where
  only a script occurred.
- **Fix (add to APPROACH.md "Supports" and Section field 10; ours, untested):**
  In "Supports", add:

> **Key line (C11):** An answer that completes the communicative task or shows the cultural understanding with target
> language errors that do not block meaning (or through a picture/gesture clue when checking comprehension) is a
> language-form gap, not a task failure; a missed cultural idea or wrong information-gap answer is a content gap.

  In Section field 10, replace "(read the model together, say or sign it back, do the exchange together even if the
  parent does not know the language, using the page's model; or a mixed class)" with:

> (read or play the model together, practise the phrases back and forth using picture-based information-gap cards so
> each side holds unseen picture details; where the adult does not speak Spanish, no unrehearsed interpersonal exchange
> is claimed; last day of the unit: review the learner's self-check and sample work together).

- **Confidence:** Likely.

### 9. Stale notes and minor mismatches across files

- **Where:** `docs/ADOPTION-BAR-SUBJECTS.md` part 6 item 9 (line 361) and owed row (lines 575 to 577); `STANDARD.md`
  lines 29 and 52; `data/standards/actfl-wrs.txt` line 9; `APPROACH.md` line 208.
- **What is wrong:**
  1. `ADOPTION-BAR-SUBJECTS.md` part 6 item 9 still says `[O] Materials are video` and the owed row (lines 575 to 577)
     still says "Decide the video source for American Sign Language, which may mean people on camera", contradicting
     Cory's 2026-10-27 graphics-only decision (no video, no photos of people).
  2. `STANDARD.md` line 52 refers to `data/courses.csv`'s `subject` column as `track`.
  3. `STANDARD.md` line 29 and `data/standards/actfl-wrs.txt` line 9 mark `ACTFL.Distinguished` as "not checked" / "not
     confirmed in 2024 text". Web search today confirms ACTFL Proficiency Guidelines 2024 retain both Superior and
     Distinguished without sublevels.
  4. `APPROACH.md` "Evidence and sources" (line 208) lists only the first scout
     (`docs/reviews/world-languages-open-material-2026-11-20.md`) and omits the second ASL scout
     (`docs/reviews/world-languages-asl-material-2026-11-21.md`).
- **Cost:** Low individually, but the video line in `ADOPTION-BAR-SUBJECTS.md` directly contradicts a standing owner
  decision and could confuse a future writer.
- **Fix:** Update `STANDARD.md` line 52 (`track` to `subject`), update `STANDARD.md` line 29 and `actfl-wrs.txt` line
  9 to note Distinguished is confirmed in the 2024 Guidelines (by web search summary, 2026-11-20), add
  `docs/reviews/world-languages-asl-material-2026-11-21.md` to `APPROACH.md` line 208, and update
  `ADOPTION-BAR-SUBJECTS.md` part 6 item 9 and its owed row when Cory approves (Question 5 below).
- **Confidence:** Firm.

## What is right and should not be touched

- The reuse-terms discipline across STANDARD.md, APPROACH.md and `actfl-wrs.txt`: ids, titles and our own words only,
  can-do statements as paraphrases with the non-endorsement note, and zero copied ACTFL wording.
- The pedagogical core in APPROACH.md and the lens: task-based communicative goals, 90 percent target language with
  learner-facing target-language instructions separated from English/Spanish adult notes, three modes in every unit
  ending in a linked task, real information gaps (no scripted dialogues), chunks before rules, and culture as
  practices, products and perspectives.
- The heritage-speaker stance (a path inside each Spanish level, home and school registers treated as registers rather
  than right/wrong, regional varieties never corrected as errors, learners never asked to translate for class or
  family, `vosotros` off by default).
- The ASL-specific rules: graphics only (drawings, labelled parameter charts, movement storyboards), all seven
  parameters taught directly each unit, voice-off norm during signing practice, Deaf community voice first, and
  insistence on Deaf educator verification before any ASL page becomes public.
- Both base-text scouts (`world-languages-open-material-2026-11-20.md` and `world-languages-asl-material-2026-11-21.md`):
  thorough, licence-accurate, honest about 403/404 blocks, and clear that Curio Class must write its own K to 12
  courses.
- The tool boundaries (no recording or storing voice/signing/writing, no automated pronunciation or sign-form scoring,
  no proficiency placement, screens never replacing a partner).

## Not checked

- **Cross-subject lean id existence in `data/progressions/*.csv`:** The 13 ids named in STANDARD.md section 6
  (`ek-discussion`, `e3-word-strategies`, `e5-figurative`, `e6-word-strategies`, `e9-sl-presentation`, `e2-sentences`,
  `ss2-culture-migration`, `ss3-home-region`, `ss4-regional-cultures`, `ss2-nation-of-immigrants`, `us1-immigration`,
  `wh1-geography-shapes-contact`, `psy-language`) could not be grepped via shell in this session because the shell
  tool's default working directory (`s:\CurioClass-agy`) does not exist on disk, and the brief forbids dumping whole
  progression files. (Note: the first read checked all 13 on 2026-11-20 and reported all 13 exist.)
- **Full primary texts of paid or blocked frameworks:** The full 2015 ACTFL World-Readiness volume, the full 2024 ACTFL
  Proficiency Guidelines PDF, the 2026 NCSSFL-ACTFL Can-Do Statements text, the CASLS `TBQHoursToReachIH.pdf` paper,
  the Clerc Center K-12 ASL standards, ASLTA 2014 standards, and the Texas LOTE 2026 rubric were not opened in full;
  web checks above used published summaries.
- **No progression CSV, frame or unit plan exists yet** (world languages are shelved), so row-level `assumes` /
  `hands_on` / `~` handoffs and per-unit standard coverage could be checked only at the rule level.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Option D early-years companions share Level 1 and Level 2 progression rows as age-tuned course frames, not separate owners | Keeps ownership clean at 4 levels (`L1` to `L4`) per language without duplicating WRS owners | docs/courses/world-languages/STANDARD.md section 6 |
| `scripts/progression.py` uses per-language keys (`spanish`, `asl`), level list `L1` to `L4`, and exempts level-based subjects from grade-order lean timing | Matches how `progression.py` resolves `STD_FILES`/`ANCHOR` and prevents false forward-lean failures | docs/courses/world-languages/STANDARD.md section 6 |
| Move frame withdrawal day from Unit field 7 to Unit field 2 and Section field 5; move room setup from Unit field 8 to Section field 10 | Matches `docs/courses/UNIT-PLAN.md` field placement | docs/courses/world-languages/APPROACH.md |
| Add `rights` read, reporting route, and C11 language-vs-content key line; remove human Spanish-speaking teacher requirement | Aligns with `docs/FOUNDATION.md` section 7, `docs/pipeline/briefs/sensitivity-read.md`, and C11 | docs/courses/world-languages/APPROACH.md |
| Add Communities 5.1/5.2 C1 check rule and draft depth ladder / text-length ceiling per level (to be verified against full ACTFL docs when pass opens) | Gives stage 2 writers an unambiguous rule for `~ID` depth notes and C10 reading load | docs/courses/world-languages/STANDARD.md section 6 |

## Questions for Cory

Only open scope, audience, money and people questions are listed here (questions already settled on 2026-11-21 in
STANDARD.md are not re-asked):

1. **Who checks ASL pages, and whether to build ASL without a Deaf co-author (STANDARD.md Question 4; ASL scout
   Question 1).** Recommended: keep ASL in pre-work (no public ASL page) until a Deaf ASL educator/artist is paid or
   credited to write or verify every sign drawing and Deaf cultural page; do not ship ASL on an agent read alone.
2. **Option D early-years companion dose, course ids and French scope.** Recommended: early-years companions
   (`spanish-k5-1`, `spanish-k5-2`, `asl-k5-1`, `asl-k5-2`, grades `k-5`) run 3 sessions of 30 minutes a week (~54
   hours/level, meeting ACTFL's 90 min/week floor); main courses (`spanish-1` to `spanish-4`, `asl-1` to `asl-4`) are
   grades `6-12`; French stays 4 courses (`6-12`, no early-years companion) when the pass opens.
3. **Level 4 exit target (Intermediate High) versus default dose (63 hours/level, 252 hours total).** Recommended:
   after reading the CASLS hours paper at pass open, either adjust the 63-hour-per-level exit ladder to Novice Low,
   Novice Mid, Novice High and Intermediate Mid (noting Intermediate High needs a daily-period high school track of
   about 135 hours/level), or raise the high school Levels 1 to 4 default to 5 sessions of 45 minutes a week (~135
   hours/level).
4. **ASL fingerspelling-only start and CC BY 3.0 eligibility (from `world-languages-asl-material-2026-11-21.md`).**
   Recommended: wait to ship ASL until a Deaf artist/signer can draw and verify signs rather than shipping a
   fingerspelling-only course under the ASL course slot; confirm whether Open Course Library's CC BY 3.0 licence
   qualifies under `BASE-TEXTS.md` before inspecting its course files when the pass opens.
5. **Updating `ADOPTION-BAR-SUBJECTS.md` part 6.** Part 6 item 9 still says `[O] Materials are video` and the owed row
   still says "Decide the video source... people on camera", contradicting the 2026-10-27 graphics-only rule.
   Recommended: update those two lines to graphics-only (drawings and storyboards, no video) now so no later writer is
   misled, while leaving the "2 courses" wording until the pass opens as already decided.

## Against the first read

Compared with `docs/reviews/prework-world-languages-read-2026-11-20.md` (run on 2026-11-20, before its fixes and
before Cory's 2026-11-21 Option D answers and the 2026-11-21 ASL second scout):

- **Already caught by the first read (and mostly applied before this read):** initial ownership gaps for `ACTFL.*`
  level ids and two languages sharing one file (first read finding 1); Level-1-only dose and 30-to-45-minute range
  (finding 2); unanchored cross-subject leans (finding 3); unlabelled `(+n)` table counts and course-id grain (finding
  4); 90 percent target-language collision with home-table adult notes (finding 5); missing "How a day opens", thin
  Supports and missing "never does" list (finding 6); missing sensitive-ground items for Hispanic/Latino/Latine,
  colonial history, religious holidays, contested Deaf history and hearing status (finding 7); stale `actfl-wrs.txt`
  header note on numbering and PDF URL mismatch (finding 8).
- **Partly overlapping, extended here:**
  - Finding 5 (missing depth ladder, missing own-words WRS statement file, missing per-level text-length ceiling, and
    Communities 5.1/5.2 C1 check rule): the first read noted the depth ladder was missing in finding 1c, but the fix
    pasted into STANDARD.md never actually wrote a depth ladder or addressed the other three gaps.
  - Finding 6 (Level 4 Intermediate High target vs 252 cumulative hours): the first read noted the exit targets were
    from memory and untied to hours; this read checked published Category I intensive hours (~240 for Intermediate Mid,
    ~480 for Intermediate High) and added the missing Option D early-years dose.
- **New in this second read:**
  - **Finding 1:** `STANDARD.md`'s claim that `scripts/standards.py` reads `actfl-wrs.txt` is false (all 11 `WRS.*`
    ids and 2 `ACTFL.*` ids currently fail `validate()`). The first read did not open `scripts/standards.py`.
  - **Finding 2:** Post-decision Option D contradictions left across STANDARD.md and APPROACH.md after Cory's
    2026-11-21 answers.
  - **Finding 3:** Full field-by-field audit of APPROACH.md against `docs/courses/UNIT-PLAN.md` (which the first read
    did not open): frame withdrawal day misplaced in Unit field 7, room setup misplaced in Unit field 8, missing tools
    list/verdicts in Unit field 8, missing standard share/limits in Section field 1, missing owned assessment item
    numbers in Section field 3, missing instruments and paper fallback in Section field 5, missing response time and
    interpretive marking in Unit field 7, 50-minute marking overflow in a 35-minute period, rule-15 no-quote override
    and "World-Readiness" public-copy label in Unit field 2, and remedies duplicated in Unit field 6.
  - **Finding 4:** `scripts/progression.py` key mismatch (`world-languages` vs `spanish`/`asl`), `progression.py`
    forward-lean failure on level-based rows leaning to grade 5+ core skills, missing Option D early-years ownership
    rule, and strand id files missing from the header "Owed" table.
  - **Finding 7:** Contradictory human "Spanish-speaking teacher" reader in APPROACH.md line 174 (against
    `FOUNDATION.md` line 136), missing `rights` read for authentic texts/audio, and missing reporting route and
    leave-out rule on sensitive ground.
  - **Finding 8:** Missing C11 language-gap vs content-gap key line in Supports, and missing non-scripted caveat for
    Spanish home-table exchanges when the adult does not speak Spanish.
  - **Finding 9:** Stale `[O] Materials are video` and "people on camera" lines in `ADOPTION-BAR-SUBJECTS.md`,
    `track` vs `subject` column name in STANDARD.md, confirmation that ACTFL 2024 retains Distinguished, and omission
    of the 2026-11-21 ASL second scout in APPROACH.md's sources paragraph.

## Sources

- ACTFL, *World-Readiness Standards for Learning Languages* (4th ed., 2015), summary page:
  https://www.actfl.org/educator-resources/world-readiness-standards-for-learning-languages/standards-summary (verified
  the 5 goal areas, 11 standard titles, and absence of printed 1.1 to 5.2 numbers, via web search).
- ACTFL, *ACTFL Proficiency Guidelines 2024*:
  https://www.actfl.org/educator-resources/actfl-proficiency-guidelines (verified that Superior and Distinguished
  remain the top two undivided levels in the 2024 edition, via web search).
- NCSSFL and ACTFL, *NCSSFL-ACTFL Can-Do Statements* (2026 edition):
  https://www.actfl.org/educator-resources/ncssfl-actfl-can-do-statements (verified that the 2026 edition is current
  and aligned with the 2024 Proficiency Guidelines, via web search).
- ACTFL, *Early Language Learning* position statement (29 July 2012):
  https://www.actfl.org/news/early-language-learning (verified the "more frequent than twice per week, adding up to at
  least 90 minutes per week" elementary and middle school floor, via web search).
- ACTFL, *Use of the Target Language in the Classroom* and *Language Learning for Heritage and Native Speakers*
  position statements (21 May 2010): https://www.actfl.org/educator-resources/position-statements (verified the 90
  percent target-language recommendation and asset-based heritage-learner guidance, via web search).
- Language Testing International (LTI) / ACTFL / Foreign Service Institute (FSI) hours-to-proficiency estimates for
  Category I languages (Spanish): https://www.languagetesting.com/ and https://www.state.gov/foreign-language-training/
  (checked intensive class-hour estimates of ~240 hours for Intermediate Mid and ~480 hours for Intermediate High, via
  web search).
