# Health pre-work: second-model cold read, 2026-11-20

> Filed by the lead 2026-11-20. Gemini 4 Neon (medium effort) in Antigravity, pasted by Cory from S:/CurioClass-gemini/ (prompt 10 to 18 for this subject), after it passed calibration (docs/reviews/calibration-*-gemini-2026-11-20.md). Its saved report is S:/CurioClass-gemini/reports/prework-health-read.md; text unchanged here except wording the repository checks flag.

Independent second-model read as the curriculum expert (`docs/agents/EXPERT.md`) with the health lens (`docs/agents/lenses/health.md`), following `docs/pipeline/briefs/prework-codex-read.md` (stage 1 pre-work read). I did not write these drafts. Nothing in the repository was edited; only this report was written. Outside sources were checked via web search and linked below; anything resting on memory is marked "from memory". The first read (`docs/reviews/prework-health-read-2026-11-19.md`) was not opened until all findings below were completed, then compared in "Against the first read".

## What I read

`AGENTS.md`; `docs/agents/EXPERT.md`; `docs/agents/lenses/health.md`; `docs/COURSE-RUN.md`; `docs/FOUNDATION.md`; `docs/APPROACH.md`; `docs/ADOPTION-BAR-SUBJECTS.md` (pass rule, shared core C1 to C16, part 3 Health, the health row of "Before a scope and sequence", sources table); `docs/courses/UNIT-PLAN.md`; `docs/courses/health/STANDARD.md`; `docs/courses/health/APPROACH.md`; `docs/courses/sel/APPROACH.md` (finished comparison page); `docs/standards-notes/health-2007-to-2024.md`; `docs/reviews/health-open-material-2026-11-16.md`; `docs/pipeline/briefs/sensitivity-read.md`; `docs/reviews/prework-sel-read-2026-11-19.md` (report shape); `data/standards/nhes-2024.txt`; `data/standards/hecat-topics.txt`; `data/progressions/health.csv`; `data/courses.csv` (health row, line 33, plus SEL and ELD rows for comparison); `scripts/standards.py`; `scripts/progression.py` (`STD_FILES`, `ANCHOR`, `SPAN`, `code_grades`, lines 1 to 140); targeted slices of `data/progressions/science.csv` (lines 70 to 134, to verify `MS-LS1-1` and `MS-LS1-3` grade placement). Opened only after writing all findings: `docs/reviews/prework-health-read-2026-11-19.md`.

## Verdict

The two standards files (`nhes-2024.txt` and `hecat-topics.txt`) are sound: all 172 SHAPE America 2024 indicators and all 81 CDC HECAT 2021 Healthy Behavior Outcomes are real, unique, and written in Curio Class's own words, and every one of the 172 NHES indicators is owned exactly once in `data/progressions/health.csv`. The biggest risk is that `docs/courses/health/STANDARD.md` cites five nonexistent HECAT outcome numbers in its coverage map while `docs/courses/health/APPROACH.md` drops eleven named `UNIT-PLAN.md` fields and misplaces four others (including family notes, teacher bias, and disclosure reporting inside Section field 9), which would send unit and section writers to the wrong fields and invalid outcomes. The one change that matters most is fixing the coverage map numbers and adding the complete, correctly placed `UNIT-PLAN.md` unit and section field block to `APPROACH.md` before health course frames or unit plans begin.

## What I counted (so nobody has to again)

| Check | Result |
|---|---|
| NHES 2024 IDs in `data/standards/nhes-2024.txt` | 172, all unique, sequentially numbered; per standard (PreK-2 / 3-5 / 6-8 / 9-12): S1 7/7/7/9 (30), S2 3/4/4/5 (16), S3 3/4/5/5 (17), S4 5/7/10/10 (32), S5 4/5/6/8 (23), S6 6/6/6/6 (24), S7 2/2/3/4 (11), S8 3/4/5/7 (19). By span: PreK-2 = 33, 3-5 = 39, 6-8 = 46, 9-12 = 54. Matches header and spot-checks against SHAPE America 2024. |
| HECAT 2021 IDs in `data/standards/hecat-topics.txt` | 10 topic IDs (9 topics plus CHE) and 81 HBO IDs, all unique: AOD 8, FN 12, MEH 9, PHW 12, PA 7, S 8, SH 10, T 5, V 10. Matches header and CDC HECAT 2021 Appendix 3. |
| Nonexistent HECAT HBO numbers in `STANDARD.md` section 4 map | 5 invalid HBO IDs across 6 cells: PHW 13 (9 to 12), FN 13 (9 to 12), PA 8 (6 to 8 and 9 to 12), S 9 (9 to 12), T 6 (9 to 12). |
| NHES ownership in `data/progressions/health.csv` | 172 owned, 0 missing, 0 owned twice: K = 10, G1 = 14, G2 = 9 (span 2 = 33); G3 = 11, G4 = 14, G5 = 14 (span 5 = 39); G6 = 13, G7 = 17, G8 = 16 (span 8 = 46); G9 = 54 (span 12 = 54). |
| All 8 NHES standards touched per grade year (`STANDARD.md` section 4 rule) | Grades 1 to 9 touch all 8 standards; Kindergarten touches 7 (Standard 8 is missing, neither owned nor `~`). |
| Cross-subject leans in `data/progressions/health.csv` | 15 entries covering 12 distinct core codes: ELA `RI.4.8`, `W.4.1`, `RI.7.8`, `W.7.1`, `RI.8.8`, `W.8.1`, `SL.8.4`; Math `6.RP.A.3`, `6.SP.B.5`, `7.SP.B.3`; Science `MS-LS1-1` (grade 6), `MS-LS1-3` (grade 7). All 12 are real codes at or before the leaning grade. |
| Skipped-grade handoffs in `data/progressions/health.csv` | 7 skipped-grade `assumes`/`hands_on` pairs (`g4-phw-prevent-illness-injury` to `g6`, `g4-meh-calm-stress` to `g6`, `g5-phw-surroundings-community` to `g8`, `g6-phw-adult-or-professional` to `g8`, `g6-fn-eating-patterns` to `g9`, `g7-phw-living-with-conditions` to `g9`, `g7-s-online-boundaries` to `g9`); all 7 state a skip reason in `notes`. |
| Sensitive rows in `data/progressions/health.csv` | 22 sensitive rows (plus 1 eased non-sensitive row `k-phw-body-names`); 17 of the 22 omit at least one required element (leave-out note, family note, what the course still meets, or disclosure reporting route). |
| `scripts/standards.py` and `scripts/progression.py` | `standards.py` checks NHES by regex (`NHES.S[1-8](.(2|5|8|12).\d{1,2})?`) and does not check HECAT (matches `STANDARD.md` section 1). `progression.py` lists `health` in `STD_FILES`, `ANCHOR` (`nhes-2024.txt`), and `code_grades` (spans 2, 5, 8, 12). |

## Findings, most serious first

### 1. Five nonexistent HECAT outcome numbers sit in the `STANDARD.md` coverage map, plus four map-to-progression mismatches

- **Where:** `docs/courses/health/STANDARD.md` section 4 table (lines 74 to 80) and Key (lines 86 to 87); `data/standards/hecat-topics.txt` (lines 10 and 24 to 104); `data/progressions/health.csv` (lines 43, 102, 103, 185, 202).
- **What is wrong:** CDC's HECAT 2021 Appendix 3 has exactly 81 Healthy Behavior Outcomes: AOD 8, FN 12, MEH 9, PHW 12, PA 7, S 8, SH 10, T 5, V 10 (confirmed in `hecat-topics.txt` and on CDC's HECAT 2021 pages). Five rows of the coverage map in `STANDARD.md` section 4 cite HBO numbers one past the real maximum:
  - PHW (9 to 12): `9 to 13` (PHW stops at 12; there is no PHW 13).
  - FN (9 to 12): `10 to 13` (FN stops at 12; there is no FN 13).
  - PA (6 to 8 and 9 to 12): `1, 2, 5, 7, 8` and `1, 2, 5 to 8` (PA stops at 7; there is no PA 8).
  - S (9 to 12): `1 to 6, 8, 9` (S stops at 8; there is no S 9).
  - T (9 to 12): `1, 3 to 6` (T stops at 5; there is no T 6).
  In addition, four real outcomes disagree between the map, its Key, and `data/progressions/health.csv`:
  - **PHW 10 in K to 2:** Key line 86 says `Care-seeking (PHW 10 and 11) starts in K to 2`, but the K to 2 cell (line 74) lists `1, 2, 3, 4, 5, 11` (not 10) and `health.csv` starts PHW 10 in grade 5 (`g5-phw-when-to-get-care`).
  - **PHW 12 in 3 to 5:** The 3 to 5 cell (line 74) lists `1 to 11` and Key line 87 says `PHW 12 (fads) is judged in grade 7`, yet `health.csv` line 102 (`g5-fn-claims-that-hurt`) still tags `Serves HECAT.PHW.HBO12`.
  - **MEH 3 in 3 to 5:** The 3 to 5 cell (line 76) lists `1 to 5, 7 to 9` (including MEH 3, handling conflict), yet no grade 3 to 5 row in `health.csv` serves `HECAT.MEH.HBO3` (`g5-v-conflict-steps`, line 103, cites only `HECAT.V.HBO1, HECAT.V.HBO2`).
  - **FN 12 in 9 to 12:** The 9 to 12 cell (line 75) lists `10 to 13` (including FN 12), yet no grade 9 row in `health.csv` serves `HECAT.FN.HBO12`.
- **Cost:** Because `STANDARD.md` notes that the coverage map cells are not machine-checked, frame and unit writers copying from the map will build units around five nonexistent HECAT codes (failing C1) and will misplace or omit four real outcomes.
- **Fix (replace lines 74 to 80 and lines 86 to 87 of `docs/courses/health/STANDARD.md`):**

```markdown
| Personal health and wellness (PHW) | 1, 2, 3, 4, 5, 11 | 1 to 11 | All | 1, 2, 5 to 7, 9 to 12 (3, 4, 8 met in 6 to 8) |
| Food and nutrition (FN) | 1, 2, 3, 6, 7 | 1 to 8, 10, 12 | 1 to 9, 11, 12 | 1, 8, 10, 11 (2 to 7, 9, 12 met in 6 to 8) |
| Mental and emotional health (MEH) | 1, 2, 3, 4, 5, 7 | 1 to 5, 7 to 9 | All; 6 in a sensitive unit (s) | All; 6 in a sensitive unit (s) |
| Physical activity (PA) | 1, 4, 6 (with PE) | 1 to 7 (with PE) | 1, 2, 5, 7; 3, 4, 6 taught in PE | 1, 2, 5 to 7 (with PE; 3, 4 met in 6 to 8) |
| Safety (S) | 1, 3 to 8 | 1, 3 to 8 | All | 1 to 6, 8 (7 met in 6 to 8) |
| Violence prevention (V) | 1, 3, 7; 8 in body safety (s) | 1, 2, 3, 5, 7; 8, 9 in body safety (s) | 1 to 3, 5 to 7; 4, 8, 9, 10 in a sensitive unit (s) | All; 4, 8, 9, 10 in a sensitive unit (s) |
| Tobacco (T) | 1, 2 | 1, 2, 3, 4 | All | 1, 3 to 5 (2 met in 6 to 8) |
```

  In Key line 86, replace `Care-seeking (PHW 10 and 11) starts in K to 2` with `Checkup care-seeking (PHW 11) starts in K to 2 because NHES.S1.2.7 does; treatment care-seeking (PHW 10) starts in 3 to 5.` In `data/progressions/health.csv`, remove `HECAT.PHW.HBO12` from `g5-fn-claims-that-hurt` (line 102) and add `HECAT.MEH.HBO3` to `g5-v-conflict-steps` (line 103); confirm FN 12 placement with Cory (Question 3).
- **Confidence:** Firm.

### 2. `APPROACH.md` drops eleven `UNIT-PLAN.md` fields and misplaces four others across unit and section plans

- **Where:** `docs/courses/health/APPROACH.md` (whole page) checked field by field against `docs/courses/UNIT-PLAN.md` ("The unit plan: fields, in order", lines 145 to 226, and "The section plan: fields, in order", lines 228 to 279) and compared with `docs/courses/sel/APPROACH.md`.
- **What is wrong:** `health/APPROACH.md` names only 6 of the 21 unit and section fields explicitly, drops 11, merges 2 into an unnumbered heading, and sends 4 items to the wrong field:

| `UNIT-PLAN.md` field | Status in `health/APPROACH.md` | Fault |
|---|---|---|
| Unit 1 Header | Dropped | Not named anywhere on the page (contrast `sel/APPROACH.md`). |
| Unit 2 Standards, limits, what is carried | Part | Lists HECAT outcomes, 3 objectives, skill steps, dated facts, scenarios. Drops NHES codes, limits, what is carried through the unit, and the all-rights-reserved rule (health cannot quote indicator verbs under `UNIT-PLAN.md` rule 15). |
| Unit 3 Where it sits | Dropped | No builds-on, handoff strength, leads-to, comes-back, or PE/science/SEL links. |
| Unit 4 Readiness check, whole | Dropped | Not named anywhere. |
| Unit 5 End-of-unit assessment, whole | Merged / sent elsewhere | Described under "Kinds of day" and "The daily evidence", not Unit field 5; drops the two sample answers per teacher-judged item (C9) and accommodations line. |
| Unit 6 Error register | Dropped | Not named anywhere. |
| Unit 7 Response allocation | Merged / sent elsewhere | The override to `UNIT-PLAN.md` field 7 ("no hands-up self-marking; respond-day groups come from the class record sheet") sits inside "The daily evidence" (lines 77 to 78), omitting marking time, response time, and the group cap. |
| Unit 8 Tools and supplies | Dropped as a field | Tool rules sit in "What a tool may and may not do", with no Unit field 8 slot for supplies, verdicts, or `TOOL-ASKS.md`. |
| Unit 9 Family note | Wrong field | Placed inside `## Supports (field 9)` (lines 115 to 118), merging Unit field 9 (Family note) into Section field 9 (Supports and extension). |
| Unit 10 Sources and what is still to make | Dropped as a field | "Evidence and sources" describes the approach page, not what each unit plan puts in Unit field 10 (dated figure sources, criterion 7 accuracy read record, logic model link). |
| Section Header | Dropped | Not named. |
| Section 1 Standards and practices | Part / split | Named as `## Practices (section field 1)` (lines 61 to 64), but "what the teacher page must explain, at an adult's level" (teacher bias note, disclosure reporting route, and "what a health day never does" for the unit) is split across lines 59 and 101 to 106 inside `## Supports (field 9)`. |
| Section 2 Where it sits | Dropped | Not named. |
| Section 3 Checks, written first | Unnumbered / merged | Titled `## The daily evidence (principle 8)` (lines 66 to 82), mixing daily evidence (Section field 3) with the unit check and respond groups (Unit fields 5 and 7), and omitting unit assessment items owned. |
| Section 4 Expected errors | Dropped | Not named. |
| Section 5 What is carried, and instruments | Part | Step card and withdrawal well stated, but drops instruments/verdict and "a room with nothing" (paper path). |
| Section 6 Days | Part | Titled `## How a day opens (section field 6)`, filling opening only and dropping day kind, who holds the card, tool line, by-hand work, and exit number. |
| Section 7 Talk and writing | Dropped / misplaced | Not named; the sensitive-unit rehearsal rule ("written scripts of the refusal line only; teacher or card plays the pressure") sits inside `## Supports (field 9)` (lines 99 to 100) instead of Section field 7. |
| Section 8 Practice that returns | Named ambiguously | Says `(field 8)` instead of `(section field 8)`. |
| Section 9 Supports and extension | Part / overloaded | Drops **check accommodations** for exit questions (`UNIT-PLAN.md` line 270); overloaded with Unit field 9 (family notes), Section field 1 (teacher bias, disclosure reporting), and Section field 7 (rehearsal rule). |
| Section 10 Two rooms | Dropped | Not named anywhere, even though `FOUNDATION.md` section 2 requires a parent-at-home path and a one-projector path. |
| Section 11 Not in this section | Dropped | Not named (important in health for handing moving to PE and science models to science). |

- **Cost:** Unit and section writers will either invent inconsistent placements, leave out C8/C9/C10/C14/C15/C16 required slots (two sample answers, error register, check accommodations, two rooms), or fail `scripts/unitplan.py` and cold-read checks.
- **Fix (add a clean "What health adds to the unit and section plan fields" section to `docs/courses/health/APPROACH.md`, moving misplaced items out of `## Supports (field 9)` and `## The daily evidence` into their exact `UNIT-PLAN.md` numbers):**

```markdown
## What health adds to the unit and section plan fields

- **Unit field 1 (Header):** days by kind summed from sections; sessions a year and period length as the band frame states; for a sensitive unit, the leave-out note on its first page (STANDARD.md section 5.5).
- **Unit field 2 (Standards, limits, and what is carried):** the NHES indicator ids in Curio Class's own words (never quoting SHAPE America's indicator sentences or verbs; exception to UNIT-PLAN.md rule 15), the HECAT 2021 behaviour outcomes in our own words, limits, three objectives (one knowing, one valuing, one doing), the unit's skill with its steps written out, the short dated facts with source and year, three to five realistic age-matched scenarios, and what is carried (the skill's step card, with the day the model is withdrawn).
- **Unit field 3 (Where it sits):** builds on (earlier health rows, handoff strong or weak; never assuming a sensitive unit except an earlier sensitive unit on the same topic), leads to, comes back, and links to PE, science, math, ELA or SEL by row id where used.
- **Unit field 4 (Readiness check, whole):** retrieval tasks or a ten-minute readiness check on assumed earlier health rows, using character scenarios only (no personal disclosure); ten-minute reteach models the earlier skill again.
- **Unit field 5 (End-of-unit assessment, whole):** a teacher-judged performance task on an unseen scenario (or a finished plan or advocacy piece) scored on the skill steps, plus one short facts-in-use item per fact the unit lists and a valuing scenario item scored on whether the reason uses a unit fact. Never a fact-recall test. Each teacher-judged item carries look-fors and two sample answers (one that meets them, one that does not), plus one line on accommodations.
- **Unit field 6 (Error register):** lettered misconceptions and skill-step errors (for example confusing a refusal with an insult, or treating a norm myth as fact), each with what it shows and its source or "from memory".
- **Unit field 7 (Response allocation):** marking time and response time stated separately. The unit check is teacher-judged on the skill steps (no hands-up self-marking). Respond-day groups come from the class record sheet's "not yet" cells by skill step, capped at four groups; others practise on a new scenario in pairs.
- **Unit field 8 (Tools and supplies across the unit):** each tool with its day, mark, job, verdict and link to TOOL-ASKS.md, following "What a tool may and may not do" below; supplies list with low-cost stand-ins.
- **Unit field 9 (Family note):** in English and Spanish, written when the unit is finished. Every unit gives a home task (a talk with a trusted adult the student chooses, or a short list to read together; a student with no adult at home may use a school adult). A sensitive unit (and k-phw-body-names) carries the longer form: what the unit covers, the dates, and how to opt out (in a school through the school; at home the parent decides).
- **Unit field 10 (Sources and what is still to make):** the standards files, progression page, dated public health sources for every figure, the criterion 7 health expert agent read record (reader, date, sources checked, findings, fixes), the sensitivity read record where required, and a pointer to the course's one-page logic model (C16).
- **Section field 1 (Standards and practices):** the NHES standard and indicator ids (our words), the HECAT behaviour outcome, the decision each fact serves, which lines of "What a health day never does" bite here, the teacher's own views note (assumptions the topic may touch and one way to keep them out of the room), and for every sensitive unit the disclosure reporting route (listen, do not promise secrecy, follow the school's duty to report, tell the student who the next adult is; for a parent teaching at home, name the national child abuse hotline and the 988 crisis line by purpose and state that a child's disclosure is not handled alone).
- **Section field 2 (Where it sits):** what comes just before and just after in the unit, which readiness items this section uses, and where its results go.
- **Section field 3 (Checks, written first):** the unit assessment item numbers owned by this section, plus the daily evidence written out (fluency/application solo scenario line; understanding choice-plus-fact question; twice-a-unit student self-check on the skill steps).
- **Section field 4 (Expected errors and first ideas):** for each error letter met here, a wrong example beside a right one, the day shown, and the five to ten minute response if many made it.
- **Section field 5 (What is carried, and instruments):** the skill's step card (teacher holds the model on the first fluency day, pairs hold the card on the second, card withdrawn on a named application day, unit check taken without it; K to 2 use three or four pictured words said aloud), plus each key moment's ideal instrument, spec verdict and paper path.
- **Section field 6 (Days):** one row a day with goal in student words, kind, how it opens (a short scenario or peer-norm question, five minutes at most; in K to 5 new content and fluency steps are taught before pairs try them), who holds the step card, tool line or "None", work by hand, and exit number.
- **Section field 7 (Talk and writing):** two or three planned questions with their days, the written task and look-fors, and the rehearsal rule (varied character scenarios; in sensitive units and any pressure refusal, written scripts of the refusal line only, with the teacher or a card playing any pressure and no student playing a person who pressures, abuses or threatens).
- **Section field 8 (Practice that returns):** which earlier skill or topic returns on each day (skills return across topics; getting help from a trusted adult returns every year).
- **Section field 9 (Supports and extension):** English learners (six to ten health words in depth, correct body part names from the start, sentence frames for each skill step, language gap vs content gap key line), access (no student must speak aloud; rehearsal in writing, by pointing, by tool or with an adult), check accommodations for exit questions (read aloud, oral answer, scribe, extra time), reading load (at most a short scenario read alone; the rest read aloud or pictured), safe personal goal list (never weight, body shape, food restriction or calories; a character's goal is always an option), non-disclosure rule, local scenario swaps, and extension on the same standard (a harder or less familiar scenario, never the next grade's standard).
- **Section field 10 (Two rooms):** a parent teaching one child at the table (the parent plays the scenario card or neutral partner role; a personal plan stays private; for disclosure at home, use the Section field 1 help lines); one projector (scenario and step card shown on one screen, pairs rehearse at desks or on paper).
- **Section field 11 (Not in this section, and still to make):** what is left to PE (movement practice), science (body-system and biology models), SEL (shared routines) or a sensitive unit, plus what is still to make and any "from memory" marks.
```

  Also add Health to `UNIT-PLAN.md` rule 15 alongside Arts and Computer Science so no unit check fails for not quoting SHAPE America's indicator verb.
- **Confidence:** Firm.

### 3. Kindergarten never touches Standard 8 (`NHES.S8`), breaking `STANDARD.md`'s every-year rule

- **Where:** `docs/courses/health/STANDARD.md` section 4 (line 98: `Each year touches all eight standards.`) and `data/progressions/health.csv` (lines 2 to 20, all Kindergarten rows).
- **What is wrong:** Every grade from 1 through 9 touches all eight NHES standards (either owning an indicator or contributing via `~CODE`), but Kindergarten has zero rows touching Standard 8 (`NHES.S8.2.1`, `NHES.S8.2.2`, or `NHES.S8.2.3`).
- **Cost:** A Kindergarten scope and sequence built from `data/progressions/health.csv` will violate `STANDARD.md` section 4 and leave advocacy untouched until grade 1.
- **Fix (in `data/progressions/health.csv`):** Add `~NHES.S8.2.1` to `k-s-trusted-helpers` (line 10, which already teaches knowing trusted adults and asking them for help, matching `NHES.S8.2.1`: "Students ask other people for help that supports their wellness") or add `~NHES.S8.2.2` to `k-v-kind-words-and-hands` (line 16). Both are non-sensitive rows in span 2, so `scripts/progression.py` accepts them cleanly and Kindergarten touches all eight standards.
- **Confidence:** Firm.

### 4. Sensitive ground: `sensitivity-read.md` is never named in `STANDARD.md` or `APPROACH.md`, and 17 of 22 sensitive rows in `health.csv` omit required safeguards

- **Where:** `docs/courses/health/STANDARD.md` sections 5 and 6; `docs/courses/health/APPROACH.md`; `docs/FOUNDATION.md` section 7.3 (line 137); `docs/pipeline/briefs/sensitivity-read.md`; `data/progressions/health.csv` (lines 40, 56, 57, 78, 97, 116, 117, 138, 156 to 159, 178 to 180, 206 to 208).
- **What is wrong:**
  1. **No sensitivity-read gate named on the pre-work pages:** `FOUNDATION.md` section 7.3 requires the sensitivity agent (`docs/pipeline/briefs/sensitivity-read.md`) to read sensitive health topics before those units go live, and `COURSE-RUN.md` stage 1 requires sensitive ground to name what needs a sensitivity read. `STANDARD.md` section 6 defines only the criterion 7 medical/scientific accuracy read ("Curio Class health expert agent") and never mentions `docs/pipeline/briefs/sensitivity-read.md` or says whether every sensitive unit (sexual health, body safety, sexual/dating violence, suicide/self-harm) and C12 topics (bodies, family structures, food cultures) get a sensitivity read.
  2. **Incomplete safeguards on 17 of 22 sensitive rows in `health.csv`:** `STANDARD.md` section 5.5 and `APPROACH.md` require every sensitive unit to carry a leave-out note (including what the course still meets without it), a family note before it, and the disclosure reporting route (listen, no secrecy promise, duty to report, parent-at-home hotlines). While `g6-v-unwanted-touch-and-help` (line 137) carries all four cleanly:
     - All three suicide/self-harm rows (`g7-meh-self-harm-help` line 156, `g8-meh-suicide-help` line 179, `g9-meh-suicide-and-self-harm-help` line 208) omit the leave-out note, the family note, and the disclosure reporting route (and lines 179 and 208 also omit what the course still meets without them).
     - All nine sexual health rows (`g1-sh-families-and-respect` line 40, `g2-sh-bodies-grow-respect` line 57, `g3-sh-respect-all-people` line 78, `g4-sh-body-changes` line 97, `g5-sh-consent-and-health` line 117, `g6-sh-puberty-and-health` line 138, `g7-sh-relationships-consent` line 158, `g8-sh-prevention-and-health` line 180, `g9-sh-health-and-consent` line 206) omit the family note and disclosure reporting route, and 6 of them omit the leave-out note and what the course still meets without it.
     - Five violence/body-safety rows (`g2-v-body-safety` line 56, `g5-v-body-safety` line 116, `g7-v-dating-and-sexual-harassment` line 157, `g8-v-dating-and-assault` line 178, `g9-v-abuse-and-dating-violence` line 207) omit the full duty-to-report/no-secrecy reporting route and/or what the course still meets without them.
  3. **Pressure role-play on a non-sensitive row:** `g7-s-ride-gear-places` (line 159) says `Students role-play turning down a ride and calling for another one` without the safeguard used on `g4-t-saying-no` and `g7-aod-turn-down-requests` ("written scripts; a card plays the offer; no student plays an impaired driver or pressurer").
- **Cost:** A unit planner working from a single row's notes can drop a leave-out note, family note, or disclosure reporting route on the highest-stakes units (suicide, abuse, sexual health), and no workflow trigger exists on `STANDARD.md` to run `sensitivity-read.md`.
- **Fix (add rule 8 to `docs/courses/health/STANDARD.md` section 5):**

```markdown
8. **Sensitivity read.** Every sensitive unit (sexual health, body safety, sexual violence and dating violence, suicide and self-harm) and any non-sensitive unit touching bodies, food culture, family structure or disability gets a fresh-agent sensitivity read (`docs/pipeline/briefs/sensitivity-read.md`) at unit plan and day stages, in addition to the criterion 7 medical and scientific accuracy read (section 6).
```

  Add a standard boilerplate line to the 17 incomplete sensitive rows in `data/progressions/health.csv` naming: (a) leave-out note and family note (English and Spanish), (b) the exact non-sensitive row(s) that still meet the unit's `~` skills, and (c) the disclosure reporting route (listen, no secrecy promise, duty to report; parent at home uses the national child abuse hotline and 988). On `g7-s-ride-gear-places` (line 159), add: `Written refusal scripts only; a card plays the offer, and no student plays an impaired driver.`
- **Confidence:** Firm.

### 5. Three owner rows in `data/progressions/health.csv` meet their NHES indicator only in part

- **Where:** `data/standards/nhes-2024.txt` against `data/progressions/health.csv` lines 141, 143, and 195 (plus minor example gaps on lines 83 and 204); `UNIT-PLAN.md` rule 19 ("Always cover the whole standard").
- **What is wrong:**
  - **`NHES.S2.8.2`** (`nhes-2024.txt` line 51): `"Students examine personal, group, community, society and environment factors behind behaviors, results and fair health."` Owner row `g7-fn-influences-on-eating` (line 141) says: `"Examine personal, group, community and society factors behind eating choices (culture, price, nearby stores, ads) without ranking any food culture. Influence check at three levels."` It drops **environment** factors, drops **results** and **fair health** (health equity), and narrows five named levels to "three levels".
  - **`NHES.S5.12.2`** (`nhes-2024.txt` line 124): `"Students determine when and why a health situation needs a careful decision process."` Owner row `g9-t-decision-views-process` (line 195) says: `"decide when a situation needs a careful decision process"` and drops **and why**.
  - **`NHES.S3.8.3`** (`nhes-2024.txt` line 68): `"Students get health information, products and services from credible sources."` Owner row `g7-phw-credible-sources` (line 143) ends with `"Students trace a claim to its source"`, which checks **information** only and leaves out finding credible **products** and **services**. (Similarly, `NHES.S3.5.3` on line 83 lists only food/drink ad and label examples with no health service example, and `NHES.S8.12.5` on line 204 lists a bystander plan and a school policy ask with no environment example.)
- **Cost:** Downstream unit plans and end-of-unit assessments built from these rows will leave parts of three owned standards untaught and untested, failing C1 and `UNIT-PLAN.md` rule 19.
- **Fix (update the three owner rows' `notes` in `data/progressions/health.csv`):**
  - Line 141 (`g7-fn-influences-on-eating`): replace `Examine personal, group, community and society factors behind eating choices (culture, price, nearby stores, ads) without ranking any food culture. Influence check at three levels.` with `Examine personal, group, community, society and environment factors (culture, price, nearby stores, ads, local food-growing and transport conditions) behind eating choices, health results and fair health, without ranking any food culture. Influence check across all five levels.`
  - Line 195 (`g9-t-decision-views-process`): replace `decide when a situation needs a careful decision process` with `determine when and why a situation needs a careful decision process`.
  - Line 143 (`g7-phw-credible-sources`): replace `Students trace a claim to its source.` with `Students locate one credible source of health information, one safe health product source and one local or school health service, and trace a claim to its source.` (Also add one health-service example to line 83 and one environmental-advocacy example to line 204.)
- **Confidence:** Firm on `S2.8.2` and `S5.12.2`; Likely on `S3.8.3` (and minor examples on `S3.5.3`, `S8.12.5`).

### 6. Course list in `data/courses.csv` does not match the four-course band shape in `STANDARD.md` and `ADOPTION-BAR-SUBJECTS.md`

- **Where:** `data/courses.csv` line 33 (`health,health-pe,Health,k-12,,y,`) vs `docs/courses/health/STANDARD.md` line 5 (`four courses, one per band`) and `docs/ADOPTION-BAR-SUBJECTS.md` line 564 (`Health (4)`).
- **What is wrong:** `data/courses.csv` holds a single `k-12` row (`health`) with blank `notes` and `core = y`. By contrast, `sel` (lines 41 to 44) and `eld` (lines 46 to 49) were already split into four band rows (`sel-k-2`, `sel-3-5`, `sel-6-8`, `sel-9-12`) on 2026-11-21 with notes naming the grade-year frame grain. Neither `STANDARD.md` nor `APPROACH.md` states the course IDs that `data/plans/<course>/` and `scripts/plan.py` will use (four band IDs `health-k-2` to `health-9-12`, or ten grade-year IDs).
- **Cost:** Stage 3 frame writers and `scripts/plan.py` have no settled course IDs for health, and the catalogue count disagrees with `ADOPTION-BAR-SUBJECTS.md`.
- **Fix (pending Cory's yes, Question 1):** Replace line 33 of `data/courses.csv` with four band rows matching `sel` and `eld`:

```csv
health-k-2,health-pe,"Health, grades K to 2",k-2,,y,"SHAPE America 2024 and HECAT 2021; one frame per grade year"
health-3-5,health-pe,"Health, grades 3 to 5",3-5,,y,"SHAPE America 2024 and HECAT 2021; one frame per grade year"
health-6-8,health-pe,"Health, grades 6 to 8",6-8,,y,"SHAPE America 2024 and HECAT 2021; one frame per grade year"
health-9-12,health-pe,"Health, grades 9 to 12",9-12,9,y,"SHAPE America 2024 and HECAT 2021; one semester in grade 9"
```

  Add one line to `STANDARD.md` section 4 stating those four course IDs and noting that K to 8 hold one frame per grade year while 9 to 12 is one semester frame.
- **Confidence:** Firm.

### 7. No shorter path is stated for K to 8 or 9 to 12, and default session counts say "about"

- **Where:** `docs/courses/health/APPROACH.md` "Pacing" (lines 122 to 130); `docs/ADOPTION-BAR-SUBJECTS.md` C2 (`a shorter path`, `days add up`); `docs/FOUNDATION.md` section 5.5 (`gives a shorter path where ordinary schools have less time`).
- **What is wrong:** `APPROACH.md` gives the default session counts as `"about 30 sessions a year of 30 minutes; 6 to 8 about 45 sessions a year of 45 minutes; 9 to 12 about 80 days of 45 minutes"`, cites the 2007 NHES national figure (40 hours PreK-2, 80 hours 3 to 12) and notes Cory's approval of the gap, but never states a **shorter path** (which sessions a school with fewer minutes cuts without losing any standard) and uses "about" instead of an exact default count for C2 arithmetic.
- **Cost:** C2 fails any course with no short path or non-exact day counts.
- **Fix (in `docs/courses/health/APPROACH.md` "Pacing", pending Cory on the short-path rule, Question 2):** Drop "about" so the defaults are exact (`K to 5: 30 sessions a year of 30 minutes; 6 to 8: 45 sessions a year of 45 minutes; 9 to 12: 80 days of 45 minutes; each band frame may change these with a reason`). Add: `Short path (C2): each band frame names the sessions to drop when a school has less time (typically the second Application day in multi-day non-sensitive units), never dropping a skill's first Fluency rehearsal or Check; sensitive units remain separately removable under STANDARD.md section 5.`
- **Confidence:** Likely.

### 8. `STANDARD.md` section 8 cross-subject leans are unkeyed and overstate the life science leans compared with `health.csv`

- **Where:** `docs/courses/health/STANDARD.md` section 8 (lines 170 to 181) vs `data/progressions/health.csv` (`cross_subject` column and lines 3, 22, 79, 119, 139).
- **What is wrong:** `STANDARD.md` section 8 names no specific core skill IDs (so a pre-work reader cannot verify leans from `STANDARD.md` alone) and claims `"body systems, puberty, germs and disease, nutrition chemistry lean on the life science progression; a health unit does not reteach the science model, it uses it."` In `data/progressions/health.csv`, however, only two rows lean on science (`g6-phw-habits-for-each-part` on `science:MS-LS1-1` and `g7-phw-living-with-conditions` on `science:MS-LS1-3`), and three health rows explicitly state body organs, germs, and vaccines as health's own plain facts because NGSS does not cover germs/vaccines and reaches body organs only in grade 4 (`k-phw-body-names` line 3, `g1-phw-stop-germs` line 22, `g4-phw-prevent-illness-injury` line 79). All 15 `cross_subject` entries in `health.csv` (12 distinct codes across ELA, Math, and Science) are real codes taught at or before the leaning grade; note only that `MS-LS1-1` sits in science unit 6.6 (late grade 6) and `6.SP.B.5` sits in late grade 6 math, so the grade 6 health frame must sequence `g6-phw-habits-for-each-part` and `g6-pa-habits-supports-barriers` after those units or supply a just-in-time note.
- **Cost:** A writer reading `STANDARD.md` section 8 will assume science teaches germs, puberty, and nutrition chemistry and leave those facts out of health lessons.
- **Fix (replace the Science bullet in `docs/courses/health/STANDARD.md` section 8, lines 174 to 175):**

```markdown
- **Science:** body systems lean on the life science progression (`MS-LS1-1` in grade 6, `MS-LS1-3` in grade 7); a health unit uses those models rather than reteaching them. Because NGSS does not cover germs, vaccines, or puberty, health states those plain facts directly with dated public health sources.
```

  Also list the core codes used in `health.csv` in the Math (`6.RP.A.3`, `6.SP.B.5`, `7.SP.B.3`) and ELA (`RI.4.8`, `W.4.1`, `RI.7.8`, `W.7.1`, `RI.8.8`, `W.8.1`, `SL.8.4`) bullets of section 8.
- **Confidence:** Firm.

### 9. Stale notes across five files

- **Where:**
  - `docs/courses/health/STANDARD.md` line 3 (`DRAFT`), line 7 (`APPROACH.md (draft)`), and line 22 (`Loaded in data/standards/nhes-2024.txt: 172 indicators, ids only`, contradicting line 33 right below it).
  - `docs/agents/lenses/health.md` line 7 (`docs/courses/health/APPROACH.md (draft)`).
  - `docs/ADOPTION-BAR-SUBJECTS.md` line 564 (`Owed: ... the approach page's yes (Desk q-prework-open-1)`).
  - `data/standards/nhes-2024.txt` line 11 (`so ids only`, contradicting line 12 right below it, which added Curio Class's own words on 2026-11-19).
  - `data/progressions/health.csv` line 120 (`g6-phw-prevent-illness-injury`): says `"Returns to g4-phw-prevent-illness-injury after a skip: the idea is not taught in between, on purpose"`, even though grade 5 `g5-s-choose-safe-option` (line 106) carries `~NHES.S1.5.3` ("Includes the injury-prevention link back to ~S1.5.3").
- **What is wrong:** `APPROACH.md` line 3 records Cory's approval on 2026-11-21 (`Desk q-prework-open-1`), and `nhes-2024.txt` has carried Curio Class's own words since 2026-11-19, so the draft and ids-only notes are stale and contradict adjacent lines.
- **Cost:** Minor; creates confusion about whether `APPROACH.md` is approved and whether NHES own-words exist.
- **Fix:** Update the status lines in `STANDARD.md` (lines 3, 7, 22), `docs/agents/lenses/health.md` (line 7), `docs/ADOPTION-BAR-SUBJECTS.md` (line 564), and `data/standards/nhes-2024.txt` (line 11: change `so ids only` to `so ids and our own words only`). On `health.csv` line 120, change `the idea is not taught in between, on purpose` to `illness prevention is not taught as its own row in grade 5, on purpose (injury prevention returns in g5-s-choose-safe-option)`.
- **Confidence:** Firm.

## What is right and should not be touched

- Both standards files (`nhes-2024.txt` and `hecat-topics.txt`): every ID is real and unique, all counts match the published frameworks, and all 172 NHES lines and 81 HECAT lines are genuinely written in Curio Class's own words with no copied runs.
- The 2007-to-2024 mapping note (`docs/standards-notes/health-2007-to-2024.md`), including the Standard 1 shift-to-use caution and the plain "this mapping is ours" statement.
- The ownership rule in `STANDARD.md` section 4 and its wiring in `scripts/progression.py` (`STD_FILES`, `ANCHOR`, `code_grades`): unambiguous, machine-checked, and cleanly satisfied across all 172 NHES indicators in `data/progressions/health.csv`.
- The sensitive-unit removability design (`STANDARD.md` section 5 rules 1 to 7): no skill lives only in a sensitive unit, getting help is taught twice in non-sensitive units, no later non-sensitive unit assumes a sensitive unit, and the narrowly bounded `k-phw-body-names` rule preserves correct body part names when sexual health is left out.
- The "What a health day never does" list, the safe personal goal list, the non-disclosure rule, and the step-card fading model in `APPROACH.md`.
- Pacing honesty: citing the 2007 NHES 40-hour and 80-hour national recommendation alongside Curio Class's lower defaults and naming the gap on the course page.

## What I could not judge

- Individual HECAT module span tables for the eight unread modules (AOD, FN, MEH, PHW, PA, S, T, V): `STANDARD.md` section 3 records that only the Sexual Health module was read in part, and the other eight are read by each band's unit planner.
- Medical and scientific accuracy of future lessons and dated figures: no unit plans or days exist yet; that is the criterion 7 read.
- Whether `scripts/progression.py check health` passes today without runtime warnings: I could not run shell commands in this read-only workspace, so `health.csv` was audited by full line-by-line inspection.

## Sources

- SHAPE America, National Health Education Standards (3rd edition, 2024): [https://shapeamerica.org/standards/health/new-he-standards/](https://shapeamerica.org/standards/health/new-he-standards/) (used via web search to verify NHES 2024 indicator codes `1.2.1`, `1.8.7`, `1.12.9`, `2.12.5`, `3.12.5`, `4.8.10`, `4.12.10`, `5.8.6`, `5.12.8`, `6.12.6`, `7.8.3`, `7.12.4`, `8.8.5`, `8.12.7` and confirm Curio Class's own-words rewrites do not copy published wording).
- CDC, Health Education Curriculum Analysis Tool (HECAT), 2021 Edition Portal and Appendix 3 (Healthy Behavior Outcomes): [https://www.cdc.gov/healthy-youth/hecat/2021-edition.html](https://www.cdc.gov/healthy-youth/hecat/2021-edition.html) and [https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_03.pdf](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_03.pdf) (used via web search to verify HECAT 2021 HBO totals: PA = 7, T = 5, S = 8, FN = 12, PHW = 12, confirming that PHW 13, FN 13, PA 8, S 9, and T 6 in `STANDARD.md` do not exist, and confirming `hecat-topics.txt` is in Curio Class's own words).
- National Health Education Standards (2nd edition, 2007) instructional time recommendation (via ETR and state guidance summaries): [https://www.etr.org](https://www.etr.org) and [https://portal.ct.gov](https://portal.ct.gov) (used via web search to confirm the 40 hours/year for PreK to grade 2 and 80 hours/year for grades 3 to 12 figures cited in `APPROACH.md`).
- No finding above rests on memory.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Remove the 5 nonexistent HBO numbers (PHW 13, FN 13, PA 8, S 9, T 6) and fix Key line 86 ("PHW 11" in K to 2, not "PHW 10 and 11") | Checked against CDC HECAT 2021 Appendix 3 and `hecat-topics.txt` | `docs/courses/health/STANDARD.md` section 4 |
| Add `~NHES.S8.2.1` to `k-s-trusted-helpers` in `health.csv` | Keeps `STANDARD.md`'s rule that every grade year touches all eight standards | `data/progressions/health.csv` line 10 |
| Expand `APPROACH.md` with the complete `UNIT-PLAN.md` unit (1 to 10) and section (1 to 11) field mapping, moving family notes to Unit 9, bias/disclosure to Section 1, and rehearsal role-play to Section 7; add Health to `UNIT-PLAN.md` rule 15 | Matches `UNIT-PLAN.md` placement rules and protects all-rights-reserved NHES wording | `docs/courses/health/APPROACH.md`; `docs/courses/UNIT-PLAN.md` |
| Add `docs/pipeline/briefs/sensitivity-read.md` as rule 8 in `STANDARD.md` section 5, and complete the missing leave-out, family note, non-sensitive fallback, and disclosure reporting lines on the 17 incomplete sensitive rows in `health.csv` (plus the card-plays-pressure line on `g7-s-ride-gear-places`) | Aligns pre-work with `FOUNDATION.md` section 7.3 and `STANDARD.md` section 5 | `docs/courses/health/STANDARD.md`; `data/progressions/health.csv` |
| Complete partial owner rows for `NHES.S2.8.2` (add environment, results, fair health, five levels), `NHES.S5.12.2` (add "and why"), and `NHES.S3.8.3` (add products and services) | Required by `UNIT-PLAN.md` rule 19 and C1 | `data/progressions/health.csv` lines 141, 143, 195 |
| Update `STANDARD.md` section 8 to list the real core codes from `health.csv` and drop the claim that science teaches germs, vaccines, and puberty | Matches `health.csv` and `data/progressions/science.csv` | `docs/courses/health/STANDARD.md` section 8 |
| Clean up stale draft, ids-only, and skip-note lines | Removes contradictions after 2026-11-19 and 2026-11-21 updates | `docs/courses/health/STANDARD.md`; `docs/agents/lenses/health.md`; `docs/ADOPTION-BAR-SUBJECTS.md`; `data/standards/nhes-2024.txt`; `data/progressions/health.csv` |

## Questions for Cory

1. **Catalogue grain in `data/courses.csv` (Finding 6).** `data/courses.csv` still has one `health` row (`k-12`), while `STANDARD.md` and `ADOPTION-BAR-SUBJECTS.md` define four band courses, and `sel` and `eld` were already split into four band rows on 2026-11-21. **Recommended:** split `health` into four band rows (`health-k-2`, `health-3-5`, `health-6-8`, `health-9-12`) with notes naming the grade-year frame grain (K to 8) and one-semester grade 9 shape.
2. **Short path for health courses (Finding 7).** Neither `STANDARD.md` nor `APPROACH.md` defines the shorter path required by C2 and `FOUNDATION.md` section 5.5. **Recommended:** state in `APPROACH.md` that each band frame names the short path by dropping the second Application day in multi-day non-sensitive units (never dropping a skill's first Fluency rehearsal or Check), while sensitive units remain separately removable.
3. **Three outcome placements between the coverage map and `health.csv` (Finding 1).** Moving an outcome in or out of a band changes scope. **Recommended:** (a) mark `HECAT.FN.HBO12` as "met in 6 to 8" in the 9 to 12 coverage map (matching `health.csv`, where grade 9 does not teach it) rather than adding another grade 9 task; (b) add `HECAT.MEH.HBO3` to `g5-v-conflict-steps` so grades 3 to 5 match the map; (c) remove `HECAT.PHW.HBO12` from `g5-fn-claims-that-hurt` so PHW 12 stays in grade 7 as the map and Key state.

## Against the first read

Opened `docs/reviews/prework-health-read-2026-11-19.md` after writing all findings above. Every one of the first read's 16 findings (C7 fading model, "What a health day never does", MEH 6 and V 4 map clashes, 9 to 12 semester pacing, safe personal goals and sensitive-unit rehearsal rule, teacher bias and disclosure route, C10/C11 supports, C13/C16 sources and evidence, criterion 7 reader wording, 81 HECAT outcomes in our own words, valuing objective and marking step, home task and longer family note, stale notes as of 2026-11-19, 21 module stubs, body-part names in PHW K to 2, and how a day opens) had already been applied to `STANDARD.md` and `APPROACH.md` before this read.

**All nine findings in this report are new** relative to the first read:
- **Finding 1** (five nonexistent HECAT HBO numbers PHW 13, FN 13, PA 8, S 9, T 6, plus four map-to-progression mismatches): new; introduced during the post-first-read map edits and progression write.
- **Finding 2** (field-by-field `UNIT-PLAN.md` placement audit of `APPROACH.md`: 11 dropped fields, 4 misplaced items, missing check accommodations, missing rule 15 exception): new; the first read added content to `APPROACH.md` under its existing headings without checking every `UNIT-PLAN.md` field number.
- **Finding 3** (Kindergarten missing Standard 8 in `health.csv`): new; `health.csv` did not exist during the first read.
- **Finding 4** (missing `sensitivity-read.md` trigger on `STANDARD.md` and incomplete safeguards on 17 of 22 sensitive rows in `health.csv` plus `g7-s-ride-gear-places`): new.
- **Finding 5** (partial owner rows for `NHES.S2.8.2`, `NHES.S5.12.2`, `NHES.S3.8.3` in `health.csv`): new.
- **Finding 6** (`data/courses.csv` single `health` row vs four band courses): new.
- **Finding 7** (no C2 short path stated; "about" session counts): new.
- **Finding 8** (`STANDARD.md` section 8 unkeyed leans and overstated life-science leans vs `health.csv`): new.
- **Finding 9** (post-approval stale draft, ids-only, and skip-note lines): new (superseding the first read's 2026-11-19 stale notes).
