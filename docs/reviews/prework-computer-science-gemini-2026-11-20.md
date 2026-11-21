# Computer science pre-work: second-model cold read, 2026-11-20

> Filed by the lead 2026-11-20. Gemini 4 Neon (medium effort) in Antigravity, pasted by Cory from S:/CurioClass-gemini/ (prompt 10 to 18 for this subject), after it passed calibration (docs/reviews/calibration-*-gemini-2026-11-20.md). Its saved report is S:/CurioClass-gemini/reports/prework-computer-science-read.md; text unchanged here except wording the repository checks flag.

Independent second-model cold read as the curriculum expert (docs/agents/EXPERT.md) with the computer science lens
(docs/agents/lenses/computer-science.md), following docs/pipeline/briefs/prework-codex-read.md. I did not write these
drafts. Nothing in S:\CurioClass was edited. Confidence is Firm, Likely or Judgment call on each finding. Outside
sources were checked by web search and are linked under Sources; anything resting on memory is marked "from memory".
The earlier Claude read (docs/reviews/prework-computer-science-read-2026-11-19.md) was opened only after all findings
below were written; see "Against the first read" at the end.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md; docs/FOUNDATION.md; docs/COURSE-RUN.md
(stage 1); docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, part 5, computer science row of "Before a scope and
sequence", sources table); docs/courses/UNIT-PLAN.md; docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md
(finished examples for comparison); docs/courses/computer-science/STANDARD.md and APPROACH.md;
docs/reviews/computer-science-open-material-2026-11-16.md; docs/pipeline/briefs/sensitivity-read.md;
docs/reviews/prework-sel-read-2026-11-19.md (format model); data/standards/csta-2026-ids.txt,
csta-2026-specialty-ids.txt, csta-2026-statements.txt and cte-career-clusters-2024.txt; data/courses.csv (computer
science row, line 35) and data/subjects.csv (line 8); scripts/standards.py (CSTA and LISTED checks);
scripts/progression.py (STD_FILES, ANCHOR and code_grades); data/progressions/computer-science.csv (all 202 skill
rows, for ownership, handoff and full-standard checks). Opened last, after findings were fixed:
docs/reviews/prework-computer-science-read-2026-11-19.md.

## Verdict

The standards list is sound: all 196 Foundational ids and 135 Specialty ids are real, unique and matched one for one
in the statements file, counts agree everywhere they are stated, and the draft pages respect the CC BY-NC-SA 4.0 terms
without copying statement text. The biggest risks are that APPROACH.md still drops or misplaces half the UNIT-PLAN
fields (including every unit field except 2 and 8, section field 2, and a "What a tool may and may not do" rule),
sensitive ground has no sensitivity-read triggers, reporting route or leave-out rule, dose by band states no period
length, and three owned standards in data/progressions/computer-science.csv are met only in part. The one change that
matters most is completing APPROACH.md to a full, accurately placed UNIT-PLAN block (with tool rules and sensitive
ground) alongside fixed default minutes per band and the three progression coverage fixes before any course frame is
written.

## What I counted

| Check | Result |
|---|---|
| Foundational ids (csta-2026-ids.txt) | 196, unique; EK 16, E1 16, E2 16, E3 19, E4 19, E5 19, MS 45, HS 46 (matches header and STANDARD.md) |
| Foundational by concept | ALG 40, PRO 45, DAT 35, SYS 38, SOC 38; sum 196 (matches STANDARD.md) |
| Specialty ids (csta-2026-specialty-ids.txt) | 135, unique; S1 73 (AIN 14, CYB 15, DSC 14, GMD 9, PHY 8, SWD 8, XCS 5), S2 62 (AIN 10, CYB 12, DSC 15, GMD 8, PHY 8, SWD 9, XCS 0) (matches header and STANDARD.md) |
| Statements (csta-2026-statements.txt) | 331 lines, unique, exact 1-to-1 match with the 196 Foundational + 135 Specialty ids; 4 hyphen-space artifacts remain (lines 129, 255, 270, 308) |
| Named S1 ids in STANDARD.md section 2 | 8 ids (4 in grade 11: S1-AIN-DD-02, S1-DSC-VZ-11, S1-CYB-TS-08, S1-SWD-TR-07; 4 in grade 12: S1-AIN-HR-09, S1-DSC-PP-13, S1-SWD-PP-08, S1-SWD-UX-05); all 8 exist in both Specialty and statements files |
| Progression ownership (computer-science.csv) | 202 skill rows; all 45 MS ids owned once (G6 17, G7 15, G8 13; matches STANDARD.md); all 46 HS Foundational ids owned once (G9 12, G10 12, G11 12, G12 10; mismatches STANDARD.md line 76 "11 or 12"); all 8 named S1 ids owned once (4 in G11, 4 in G12) |
| Progression handoffs | 4 grade-skipping handoffs (g8->g10 x2, g8->g11 x1, g9->g11 x1), each explained in the receiving row's notes; 1 stale owner note in g9-data-and-people (line 156) |
| Validators | scripts/standards.py reads both id files (lines 92 to 93); scripts/progression.py includes computer-science in STD_FILES, ANCHOR and code_grades (lines 60, 70, 102 to 117), but allows S1-XCS-* and any S1 id in grades 11 and 12 |
| Cross-subject code in STANDARD.md section 4 | CTE.Career Clusters.Digital Technology verified in data/standards/cte-career-clusters-2024.txt line 23; AASL.Curate and AASL.Engage verified in scripts/standards.py line 117 |

## Findings, most serious first

### 1. APPROACH.md drops seven unit fields and one section field, misplaces two items, and lacks a "What a tool may and may not do" section

- **Where:** docs/courses/computer-science/APPROACH.md ("What computer science adds to the plan fields", lines 50 to 83; "The kinds of day", line 18); docs/courses/UNIT-PLAN.md (unit fields 1 to 10 and section fields 1 to 11); docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md (comparison).
- **What is wrong:** Field-by-field placement against UNIT-PLAN.md shows ten placement and omission faults:
  1. **Unit field 1 (Header):** Dropped. Unlike sel/APPROACH.md, nothing states that the header carries sessions by kind, sessions a week and period length.
  2. **Unit field 2 (Standards, limits, and what is carried):** Drops **limits** (the depth taught to and what is left out, required by UNIT-PLAN field 2 and STANDARD.md section 1 "Depth").
  3. **Unit field 3 (Where it sits):** Dropped. No rule for builds-on, handoff strength (such as the weak K to 1 handoff in STANDARD.md line 84), leads-to or comes-back (bar criterion 3 and C4).
  4. **Unit field 4 (Readiness check, whole):** Dropped. No rule for what a computer science readiness check looks like (e.g. a short trace item) or how the ten-minute reteach runs in a once-a-week K to 5 rotation.
  5. **Unit field 5 (End-of-unit assessment, whole):** Merged into the "Kinds of day" table (line 18) instead of sitting under Unit plan field 5. Nothing under Unit plan specifies code/project rubrics (bar criterion 8) or accommodations.
  6. **Unit field 6 (Error register):** Dropped. Both code misconceptions and systems/data/society misconceptions need one mistake per letter with source or "from memory".
  7. **Unit field 7 (Response allocation):** Dropped. UNIT-PLAN field 7 defaults to hands-up self-marking on short items; APPROACH.md never says whether trace items are self-marked while build/debug tasks are teacher-judged by look-fors, how respond-day groups are capped, or how marking time is counted.
  8. **Unit field 8 (Tools and supplies across the unit):** Misplaces "the few-device and one-screen versions" into Unit field 8, whereas STANDARD.md line 143 places the four device-day rooms in section fields 5 and 10. Also drops the link to TOOL-ASKS.md, the supplies list (including optional microcontroller cost per STANDARD.md section 5), and technical-staff notes (bar criterion 7).
  9. **Unit field 9 (Family note) and Unit field 10 (Sources and what is still to make):** Both dropped. Neither English/Spanish family notes nor the sources table, UK base third-party check, dated society sources and logic-model pointer have a slot.
  10. **Section field 2 (Where it sits):** Dropped (the list jumps from Field 1 to Field 3). **Section field 1** duplicates "the common bug and what it shows", which UNIT-PLAN places in Unit field 6 (and explicitly excludes from section field 4). **Section field 10** omits how pair programming (driver/navigator) runs for one child at home (FOUNDATION section 2) and the last-day-of-unit home line.
  11. **What a tool may and may not do:** Absent as a section (compare health/APPROACH.md lines 132 to 136). Rules are scattered across STANDARD.md section 5 and APPROACH.md lines 41 to 42 and 92 to 95, leaving no single statement of what a tool may check and what it may never do.
- **Cost:** Writers will invent different structures for unit fields 1, 3, 4, 6, 7, 9 and 10, put few-device rotations in the wrong plan, omit technical-staff notes (bar criterion 7), and have no clear boundary on automated grading or live external tools (C7, C8, C9, C13, C14, C15).
- **Fix:** Replace "What computer science adds to the plan fields" in docs/courses/computer-science/APPROACH.md with a complete block covering Unit fields 1 to 10 and Section fields 1 to 11, and add a "What a tool may and may not do" section:

> ## What computer science adds to the plan fields
>
> **Unit plan.**
> - Field 1 (Header): sessions by kind, sessions a week and period length, matching the course frame.
> - Field 2 (Standards, limits, and what is carried): each standard's parts by verb (the id and our own words, STANDARD.md "Quoting"); the depth taught to and what is left out (limits, STANDARD.md "Depth"); the practice the unit teaches, named by its group; what is carried through the unit: the anchor program, algorithm or dataset (its name, the day it is shown whole, the day it is withdrawn, the day students first build alone); the unit's unplugged days, counted.
> - Field 3 (Where it sits): builds on (with handoff marked strong or weak, including the weak K to 1 handoff), leads to, and where it comes back.
> - Field 4 (Readiness check, whole): when given (UNIT-PLAN timing); one short trace or concept item per earlier-grade row assumed, with key and ten-minute reteach. In K to 5 once-a-week classes, the reteach runs in the next session's first ten minutes.
> - Field 5 (End-of-unit assessment, whole): read and trace items plus a short build, debug or audit task with look-fors and two sample pieces (one that meets them, one that does not), a paper version for rooms without devices (marked as in STANDARD.md "Devices and rooms"), and accommodations.
> - Field 6 (Error register): one mistake per letter (notional-machine errors, code bugs, or systems, data and society misconceptions), what each shows, and its source or "from memory".
> - Field 7 (Response allocation): marking time and response time stated separately. Short trace items may be marked against the key on screen (five minutes); build, debug and society tasks are teacher-judged against look-fors (no hands-up self-marking). Respond-day groups come from the class record sheet by error letter, capped at four groups; others work in pairs on an extension case.
> - Field 8 (Tools and supplies across the unit): each tool with its day, mark (key or light), job, verdict and link to TOOL-ASKS.md; devices needed per pair; supplies list (cards, paper, optional microcontroller cost if used); and one line of notes for school technical staff (common browser, single offline file, no install, no account, nothing sent off the device).
> - Field 9 (Family note): once per unit in English and Spanish (what the class is building or auditing, key words, and a note that no student account or personal data is used).
> - Field 10 (Sources and what is still to make): standards file, progression page, dated sources for every society case, third-party check record for any adapted UK base unit, what is still to make, and a pointer to the course logic model (C16).
>
> **Section plan.**
> - Field 1 (Standards and practices): this section's share of each standard (id and our own words), limits that bite here, connections, the notional-machine point (what the computer does with each line, in order) or adult-level background for non-code units, the practice with its day and task, and any sensitive-ground teacher note and reporting route.
> - Field 2 (Where it sits): what comes just before and after inside the unit, which readiness items it uses, and where its results go.
> - Field 3 (Checks, written first): the unit assessment item numbers this section owns, then each day's evidence in the form set under "The form of daily evidence".
> - Field 4 (Expected errors and first ideas): each error letter this section meets as a wrong example beside a right one (a wrong program for code; a wrong statement for systems, data or society), the day shown, and the five to ten minute action if many made it.
> - Field 5 (What is carried, and instruments): the anchor program, algorithm or dataset and how it fades (whole worked program, blanks or shuffled lines, modified, withdrawn); each key moment with ideal instrument and spec verdict; the few-device rotation (three or four stations with paper stations for waiting pairs) and the no-device paper stand-in (STANDARD.md "Devices and rooms").
> - Field 6 (Days): one row a day with goal in student words, kind in this page's words, opening and minutes, who holds what is carried (teacher, pair, student), tool part, mark, job and minutes (or "None"), work away from the device, and evidence number.
> - Field 7 (Talk and writing): two or three planned questions (at least one of the form "what will happen if"), one written or spoken task ("what I tested and what I changed"), its look-fors, and pair roles (driver, navigator) with the switch time.
> - Field 8 (Practice that returns): a three-minute trace or debug of an earlier unit's construct, the unit named. No fluency target.
> - Field 9 (Supports and extension): English learners, access, check accommodations, reading load and extension, as set under "Supports".
> - Field 10 (Two rooms): one child at home (the parent plays navigator while the child drives, or trades roles each task, plus one line on the unit's last day); one screen in the room (whole-class predict, vote, and one student at the device per step).
> - Field 11 (Not in this section, and still to make): what is left to another section or course, what is still to make, spec-only marks, and "from memory" marks.
>
> ## What a tool may and may not do
>
> A tool may show a notional machine step by step, run automated test cases against a student program and report "yes" or "not yet", switch between blocks and text, or simulate a toy network, classifier or security system offline in a single file. A tool may not require an install, an account or a network connection, send student work or data off the device, connect a student to a live generated-text service, grade open explanations or design rationale, collect personal data, or replace the unit's unplugged teaching days.

- **Confidence:** Firm.

### 2. Sensitive ground is unnamed: no sensitivity-read triggers, no teacher-note or reporting-route rule, and no leave-out rule

- **Where:** docs/courses/computer-science/STANDARD.md ("Privacy and safety", lines 174 to 182; "Real cases in society days", lines 184 to 192); docs/courses/computer-science/APPROACH.md (absent); docs/pipeline/briefs/sensitivity-read.md; docs/ADOPTION-BAR-SUBJECTS.md (line 91, "each course page says what a school may leave out").
- **What is wrong:** Neither STANDARD.md nor APPROACH.md mentions `docs/pipeline/briefs/sensitivity-read.md` or defines what counts as sensitive ground in computer science. Multiple CSTA 2026 standards touch sensitive ground directly:
  - Algorithmic bias, exclusion, and disparate impact on demographic or marginalized groups (E4-ALG-IM-03, E5-SOC-HI-16, MS-ALG-IM-10, MS-ALG-IM-11, MS-SYS-IM-37, MS-SOC-ET-41, MS-SOC-ET-42, HS-ALG-IM-10, HS-SOC-ET-41, S1-DSC-PP-13, S1-SWD-PP-08).
  - Data sovereignty, surveillance, and personal data about communities (MS-DAT-IM-28, HS-DAT-IM-27, HS-DAT-IM-28).
  - Online safety, unkind messages, personal information, and social consequences (E1-SYS-SE-12, E2-SYS-SE-12, E3-SYS-SE-13, MS-SOC-HU-43).
  - Automation and job displacement (MS-SOC-CE-45) and ethics of AI versus human responsibility (HS-SOC-HU-44).
  Privacy and safety rules exist in STANDARD.md, but there is no rule requiring a teacher note on sensitive topics in Section field 1, no reporting route if a child discloses online harm, bullying or unsafe contact during an online-safety day, no list of which units require a sensitivity read, and no leave-out rule stating what a school or family may omit and what the course page then reports.
- **Cost:** Units on algorithmic bias, data sovereignty and online safety would be written without the required sensitivity read (C12, FOUNDATION promise 7), teachers will lack a reporting route if an elementary online-safety lesson triggers a disclosure, and schools will have no clear leave-out guidance.
- **Fix:** Add a "Sensitive ground" section to docs/courses/computer-science/APPROACH.md (and point to it from Section field 1 and STANDARD.md):

> ## Sensitive ground
>
> Every computer science unit gets a fresh-agent sensitivity read (docs/pipeline/briefs/sensitivity-read.md) before days ship, with heightened study of community voices on units covering algorithmic bias and disparate impact, exclusion in computing history and design, data sovereignty, digital access barriers, automation and work, and online safety.
>
> - **Teacher note (section field 1):** Every section touching bias, exclusion, online harm, surveillance or job loss carries a short teacher note stating what may come up in the room, how to keep discussion on evidence and systems rather than blaming any group or classmate, and the two views with dated sources.
> - **Online safety and disclosures:** Every online-safety or privacy section (grades K to 8) carries a reporting-route line on the teacher page: listen, do not promise secrecy, follow the school's duty to report, and name the next trusted adult (at home, a parent does not handle a disclosure of harm alone; list the national child abuse hotline by purpose). No student is asked to share a real online incident or account.
> - **Leave-out rule (pending Cory):** Computer science has no opt-out unit by default, because every concept is part of the standards and society cases follow the values rule with two views and dated sources. If a school chooses to leave out a society or AI unit, later units do not assume it, and the school is told which CSTA ids that year no longer claims.

- **Confidence:** Firm (for the missing sensitivity-read, teacher-note and reporting-route rules); Judgment call on the leave-out default (see Questions for Cory 4).

### 3. Dose by band states no period length, gives a range for grades 6 to 12, and does not cite what CSTA says about instructional time

- **Where:** docs/courses/computer-science/STANDARD.md section 2 (line 68: `Minutes: one session a week in K to 5 (a specials rotation), two to three a week in 6 to 12 (a real elective)`); docs/courses/computer-science/APPROACH.md ("Pacing", lines 102 to 108).
- **What is wrong:** Three gaps block C2 (a stated year and period length) and C1 (keeping S1 days under 10 percent of teaching days):
  1. Line 68 is labelled "Minutes:" but states **zero minute figures** and zero annual session counts.
  2. "Two to three a week in 6 to 12" is a range, not one default number per band, so day budgets cannot be computed.
  3. Neither STANDARD.md nor APPROACH.md cites whether a national or professional body publishes a time figure. Web search confirms that CSTA (2026 PK-12 Computer Science Standards, https://csteachers.org/pk12standards/) and the K-12 Computer Science Framework do not publish a mandatory weekly minutes figure, leaving scheduling to states and districts.
- **Cost:** Frame writers in grades K to 12 have no default period length or annual session count, cannot verify C2 arithmetic or the 10 percent S1 cap in grades 11 and 12, and may budget incompatible session lengths across grades.
- **Fix:** Update STANDARD.md section 2 line 68 and APPROACH.md "Pacing" once Cory confirms the default minutes (see Questions for Cory 1):

> **Dose by band.** CSTA publishes no required minutes per week (2026 CSTA PK-12 Computer Science Standards; scheduling is left to states and districts). Settled sessions a week (Cory, 2026-11-16, Desk card q-later-followups-1): one session a week in K to 5, two to three a week in 6 to 12. Default calendar (ours, untested, pending Cory): K to 2, 32 sessions a year of 30 minutes (16 hours); grades 3 to 5, 32 sessions a year of 40 minutes (about 21 hours); grades 6 to 8, 64 sessions a year (2 a week) of 45 minutes (48 hours); grades 9 to 12, 96 sessions a year (3 a week) of 45 minutes (72 hours). A course frame may adjust these with a stated reason, and gives a shorter path.

- **Confidence:** Firm.

### 4. Progression coverage and consistency faults in data/progressions/computer-science.csv: three ids met only in part, a grade-1 vocabulary leak, and a 30-line vs 20-line reading-load contradiction

- **Where:** data/progressions/computer-science.csv lines 21, 116, 120, 154, 156, 160, 170; data/standards/csta-2026-statements.txt lines 13, 123, 149, 176; docs/courses/computer-science/APPROACH.md line 96 to 97.
- **What is wrong:** Checking owned rows in data/progressions/computer-science.csv against the full CSTA statements and APPROACH.md surfaces five concrete faults:
  1. **MS-DAT-IM-28 met only in part (line 116, `g7-personal-data`):** The statement asks students to explain benefits and risks of personal data and metadata, "including issues of data ownership, privacy, and **sovereignty**." Both `words` and `notes` omit **sovereignty** (data sovereignty: a community's or nation's right to govern collection, ownership and use of its own data).
  2. **HS-SYS-HW-29 met only in part (line 160, `g9-operating-systems`):** The statement specifies that an operating system manages hardware and other software, "including handling memory and **peripherals**." Both `words` and `notes` omit **peripherals**.
  3. **HS-DAT-DC-21 met only in part (line 154, `g9-simulate-data`):** The statement asks students to generate simulated data that fits certain parameters "**for use in a simulation**." The row generates and checks a simulated dataset, but never uses it inside a simulation.
  4. **Reading-load contradiction (line 170, `g10-analyze-code` vs APPROACH.md line 96 to 97):** APPROACH.md caps Grades 6 to 12 code reading load at "up to twenty lines (ours, untested)". `g10-analyze-code` specifies "Given a **thirty-line** text program".
  5. **Grade-1 construct leak (line 21, `g1-code-sequence`, E1-PRO-PD-04):** `words` includes `repeat`, even though iteration/loops are not taught until grade 2 (E2-ALG-PS-01, E2-PRO-PD-04) and STANDARD.md line 49 forbids teaching a K to 5 id at the next grade's depth.
  6. **Two text defects in `computer-science.csv`:** Line 156 (`g9-data-and-people`) contradicts itself in two adjacent sentences ("Owned in grade 12; here the first look. Hands on to g11-data-scale-ethics, which owns the id."); line 120 (`g7-impact-history`, MS-SOC-HI-39) says "unplugged side effects" instead of "unintended side effects".
- **Cost:** Three standards fail C1 and UNIT-PLAN rule 19 ("always cover the whole standard"), a grade 1 writer may pull loops a year early, and a grade 10 writer faces two opposite reading-load caps.
- **Fix:**
  - `g7-personal-data` (line 116): add `sovereignty` to `words` and add to `notes`: `They also examine data sovereignty: why a community or nation (including Indigenous nations) claims the right to govern how data about its people and land is collected and used.`
  - `g9-operating-systems` (line 160): add `peripheral` to `words` and add to `notes`: `and how the OS manages peripherals (keyboard, printer, sensor, storage drive) through device drivers.`
  - `g9-simulate-data` (line 154): add to `notes`: `Then students feed the generated dataset into a short supplied simulation (such as a queue or weather model) and observe how changing a parameter changes the simulation's outcome.`
  - `g10-analyze-code` (line 170): change `thirty-line` to `twenty-line` (or raise APPROACH.md's grades 9 to 12 reading-load cap to 30 lines; keeping 20 lines is simpler and fits a single page).
  - `g1-code-sequence` (line 21): remove `repeat` from `words`.
  - `g9-data-and-people` (line 156): delete `Owned in grade 12; ` so it reads `Here the first look. Hands on to g11-data-scale-ethics, which owns the id.`
  - `g7-impact-history` (line 120): change `unplugged side effects` to `unintended side effects`.
- **Confidence:** Firm.

### 5. Course list, catalogue and status contradictions across five files

- **Where:** data/courses.csv line 35; data/subjects.csv line 8; docs/courses/computer-science/STANDARD.md lines 19 and 76; docs/courses/computer-science/APPROACH.md lines 3 to 4 and 125 to 126; docs/ADOPTION-BAR-SUBJECTS.md lines 334 to 335 and 566; data/standards/csta-2026-specialty-ids.txt line 9; data/standards/csta-2026-statements.txt lines 129, 255, 270 and 308.
- **What is wrong:** Seven concrete contradictions and stale lines remain after the 2026-11-19/20 updates:
  1. `data/courses.csv` line 35 reads `cs-k12,computer-science,Computer Science,k-12,,n,CSTA bands K-2 3-5 6-8 9-10 11-12`. Those are the superseded **2017** CSTA bands (1A, 1B, 2, 3A, 3B), not the 2026 bands (EK, E1 to E5, MS, HS), and the note does not reflect the settled 13 grade courses (STANDARD.md line 58).
  2. `data/subjects.csv` line 8 says `CSTA K-12` instead of `2026 CSTA PK-12`.
  3. `APPROACH.md` lines 3 to 4 still read `**DRAFT, 2026-11-16, fixed 2026-11-19..., for Cory's yes.** Nothing here is decided until he says so.` and line 126 reads `Still open: our own editor (STANDARD.md).` Both directly contradict line 125 (Cory approved APPROACH.md on 2026-11-20, Desk q-prework-cs-1) and STANDARD.md line 164 (our own editor settled 2026-11-21, Desk q-prework-open-1).
  4. `STANDARD.md` line 19 still says `Approach page | Draft, fixed 2026-11-19, waiting on Cory's yes`, and line 76 says `Each HS year owns 11 or 12 ids`, contradicting `computer-science.csv` line 203 (Cory, 2026-11-20: grade 12 owns 10 Foundational ids plus 4 S1 ids, so the Foundational split is 12 / 12 / 12 / 10).
  5. `ADOPTION-BAR-SUBJECTS.md` part 5 line 334 still says `The high school course` (singular) and omits the 2026-11-20 decision naming 8 S1 ids in grades 11 and 12; line 566 still lists `Owed: the Specialty level 1 list (later.csv L84); our own editor (Desk q-prework-open-1)` even though both are settled.
  6. `data/standards/csta-2026-specialty-ids.txt` line 9 still says `the checkers do not read this file yet` and `the high school course` (singular) and `module` (non-glossary word), although both `scripts/standards.py` (line 92) and `scripts/progression.py` (line 60) already read it.
  7. `data/standards/csta-2026-statements.txt` still has four PDF hyphen-space artifacts: line 129 (`large- scale`), line 255 (`device- to-device`), line 270 (`human- centered`), and line 308 (`large- scale`).
- **Cost:** Writers and downstream scripts get conflicting facts about whether APPROACH.md is approved, whether the editor is settled, how many ids grade 12 owns, and which CSTA edition and bands `data/courses.csv` tracks.
- **Fix:**
  - `data/courses.csv` line 35: update `notes` (pending Cory on catalogue grain, Questions for Cory 2) to `One course per grade K to 12; 2026 CSTA PK-12 (EK, E1 to E5, MS, HS Foundational plus eight named S1 ids in grades 11 and 12)`.
  - `data/subjects.csv` line 8: change `CSTA K-12` to `2026 CSTA PK-12`.
  - `APPROACH.md` lines 3 to 4: replace the DRAFT header with `**Approved by Cory 2026-11-20 (Desk q-prework-cs-1), with fixes applied 2026-11-19 (docs/reviews/prework-computer-science-read-2026-11-19.md); updated after second-model read.**` Delete `Still open: our own editor (STANDARD.md).` at line 126.
  - `STANDARD.md` line 19: change to `Approved 2026-11-20 (Desk q-prework-cs-1); updated after second-model read`. Line 76: change `Each HS year owns 11 or 12 ids` to `HS Foundational split is 12, 12, 12 and 10 ids across grades 9 to 12 (grade 12 owns 10 Foundational ids for the capstone plus 4 S1 ids; grade 11 owns 12 Foundational plus 4 S1 ids; Cory, 2026-11-20)`.
  - `ADOPTION-BAR-SUBJECTS.md` line 334: change `The high school course teaches` to `The four high school courses (grades 9 to 12) teach`, and add the 2026-11-20 eight-S1 decision; line 566: move the S1 list and editor to Done.
  - `csta-2026-specialty-ids.txt` line 9: replace with `# note: scripts/standards.py and scripts/progression.py read this file. Grades 11 and 12 claim the eight named S1 ids in STANDARD.md section 2; S2 and XCS ids stay out of computer science courses.`
  - `csta-2026-statements.txt` lines 129, 255, 270, 308: join `large-scale`, `device-to-device`, `human-centered`, `large-scale`.
- **Confidence:** Firm.

### 6. The text programming language for grades 7 to 12 is stated as settled but never named

- **Where:** docs/courses/computer-science/STANDARD.md ("Our own editor", lines 162 to 166; "Blocks to text", lines 168 to 172).
- **What is wrong:** Line 166 says Cory's decision to build our own browser editor "also settles the text language for grades 7 to 12", and line 171 says "One text language for grades 7 to 12, named as a subject term on teacher pages, chosen so it runs in a common browser with nothing installed." Neither paragraph names the language (for example Python or JavaScript).
- **Cost:** Grade 6 to 12 frame, unit and day writers cannot write worked code examples, trace tables, syntax error messages, or offline reference documentation (MS-PRO-PD-13, HS-PRO-PD-13) until one language is named.
- **Fix:** Add one sentence to STANDARD.md "Blocks to text" naming the settled language (see Questions for Cory 3):

> The text language for grades 6 (side by side) and 7 to 12 is [Python / JavaScript], named as a subject term on teacher pages and run offline in our single-file browser editor.

- **Confidence:** Firm.

### 7. The progression gate allows S1-XCS-* (and any of the 73 S1 ids) in computer science grades 11 and 12

- **Where:** scripts/progression.py lines 110 to 113 (`code_grades`); docs/courses/computer-science/STANDARD.md section 2 (lines 96 to 99) and section 3 (lines 108 to 109).
- **What is wrong:** STANDARD.md section 3 explicitly excludes the five X + CS standards (`S1-XCS-XC-01` to `S1-XCS-XC-05`) from computer science courses, and section 2 restricts S1 claims in grades 11 and 12 to eight named ids (four in grade 11, four in grade 12). In `scripts/progression.py`, `code_grades` checks only `if b == 'S1': return ['11', '12'], ['11', '12']`, which accepts `S1-XCS-*` and any other S1 id in either grade 11 or 12.
- **Cost:** An XCS standard or an unapproved S1 id can slip into `data/progressions/computer-science.csv` or a grade 11/12 frame without failing the gate.
- **Fix:** In `scripts/progression.py` `code_grades` for `computer-science`, reject `S1-XCS-*` (return `[], []`, like `S2`), and optionally check S1 codes against the eight-id allowlist (four in grade 11, four in grade 12) from STANDARD.md section 2:

> In `code_grades`: if `code.startswith('S1-XCS-')`, return `[], []` (excluded from computer science). For other `S1` codes, accept only the four grade-11 ids in `['11']` and the four grade-12 ids in `['12']` (or warn on any S1 id outside the named eight).

- **Confidence:** Firm.

### 8. Cross-subject leans in STANDARD.md name no core progression ids, and computer-science.csv omits social studies, library and career leans

- **Where:** docs/courses/computer-science/STANDARD.md section 4 (lines 116 to 132); data/progressions/computer-science.csv (`cross_subject` column).
- **What is wrong:** STANDARD.md section 4 describes math, science, ELA, social studies, library and career leans in general prose only (naming only one code, `CTE.Career Clusters.Digital Technology`, and two AASL domain names, Curate and Engage). Meanwhile, `data/progressions/computer-science.csv` includes 29 `math:`, `science:` and `ela:` skill ids, but **zero** `social-studies:`, `library:` or `career:` leans, even on rows that explicitly debate law, policy, history, online sources and careers (`g9-computing-history`, `g11-policy-change`, `g12-data-policy-debate`, `g12-law-policy`, `g12-career-goals`).
- **Cost:** Stage 2/3 cross-subject timing checks cannot verify whether computer science's policy/law days lean on high school government or whether its source-checking days lean on library skills.
- **Fix:** Add a short table or bulleted list of verified core progression ids to STANDARD.md section 4 (matching the `math:`, `science:` and `ela:` ids already used in `computer-science.csv`), and add the matching `social-studies:` ids (such as government/policy rows) to `g11-policy-change`, `g12-data-policy-debate` and `g12-law-policy` in `computer-science.csv`.
- **Confidence:** Likely.

### 9. Three pre-work PDF extractions remain owed, and APPROACH.md still cites no read sources

- **Where:** docs/courses/computer-science/STANDARD.md section 1 ("Depth", lines 47 to 49; "Sub-concept codes", lines 50 to 52) and section 3 ("Practices", lines 111 to 114); docs/courses/computer-science/APPROACH.md ("Honest limits", lines 110 to 115); docs/ADOPTION-BAR-SUBJECTS.md C13.
- **What is wrong:** Three items needed by frame and unit writers are still owed from whoever holds the 2026 CSTA PDF: (a) boundary statements (needed to judge depth under C1), (b) the sub-concept code key (`PD, RD, TR, VD, PS, ML, IM, DC, DI, HW, SE, NT, HI, HU, CE, ET`), and (c) the table of twelve practices mapped to bar part 5 item 2. In addition, APPROACH.md line 115 still says `Sources read for this page: none yet`, while relying on PRIMM / use-modify-create / notional-machine order from memory.
- **Cost:** Unit writers cannot check CSTA boundary statements, must guess sub-concept meanings and practice names, and C13 flags an approach page whose pedagogy rests on unread sources.
- **Fix:** Keep these four items explicitly tracked in a single "Owed before frames" block at the top of STANDARD.md (or in ADOPTION-BAR-SUBJECTS.md's computer science row), and read at least one open primary pedagogy source (such as the Teach Computing Curriculum pedagogy guide or a published PRIMM summary) into APPROACH.md "Honest limits" before stage 3 opens.
- **Confidence:** Likely.

## What is right and should not be touched

- All 196 Foundational ids, 135 Specialty ids and 331 statements in `data/standards/csta-2026-*.txt`: counts, uniqueness, band structure and CC BY-NC-SA 4.0 licence headers are clean and accurate.
- The "Order inside a unit: understanding before modify before make" rule and the five-row kinds-of-day table in APPROACH.md.
- The separation of unplugged teaching days, device days and four-way device stand-ins (plus "part met without a device") in STANDARD.md section 5.
- The privacy and safety rules (no student data, pretend accounts, offline toy security systems, no live student generated-text tools) and the real-cases rule (what happened, no company names, two views with dated sources).
- The non-specialist teacher page block (APPROACH.md lines 80 to 83) and the Supports section (lines 85 to 100), aside from the 20-vs-30-line cap alignment in Finding 4.
- The ownership structure in `data/progressions/computer-science.csv` (all 45 MS ids and 46 HS Foundational ids owned once, ordering constraints respected, grade skips explained in notes).
- The base-text scout (`docs/reviews/computer-science-open-material-2026-11-16.md`): clear OGL v3.0 vs CC BY-NC-SA 4.0 separation and unit-by-unit third-party check rule.

## Not checked

- **Existence of the 29 cross-subject skill ids in `data/progressions/math.csv`, `ela.csv` and `science.csv`:** The brief asks for a one-line grep per id without dumping whole files. Shell commands could not run in this environment because the configured command working directory (`s:\CurioClass-agy`) does not exist, so I did not dump those three files and did not verify those 29 ids. Run `python -X utf8 scripts/progression.py check computer-science` to verify them mechanically.
- **The 2026 CSTA PDF itself (218 pages):** Not opened locally; standard codes, structure, concepts, practices, dispositions, Specialty tiers, licence (CC BY-NC-SA 4.0), DOI (`10.1145/3820482`) and five sample standard statements were verified via web search against `csteachers.org`.
- **`scripts/unitplan.py` and `scripts/plan.py`:** Not read.
- **`docs/APPROACH.md` and `docs/APPROACH-SOURCES.md`:** Not read in this pass.

## Sources

- CSTA, 2026 CSTA PK-12 Computer Science Standards (`https://csteachers.org/pk12standards/`, DOI `https://doi.org/10.1145/3820482`): verified publication, DOI, ISBN (979-8-4007-2780-1), CC BY-NC-SA 4.0 licence, five concepts, twelve practices in four groups, seven dispositions, Foundational vs Specialty I and II tiers, and exact wording of sample codes `EK-ALG-PS-01`, `MS-ALG-ML-07`, `HS-SYS-SE-33`, `S1-AIN-DD-02` and `S1-XCS-XC-01`.
- CSTA Washington overview of the 2026 CSTA Standards (`https://cstawa.org/` via web search): corroborated the four practice groups (Computational Thinking, Inclusive Collaboration, Human-Centered Design, Ethics and Social Responsibility) and seven dispositions.
- CSTA and state guidance on K-12 computer science instructional time (web search across `csteachers.org`, `ospi.k12.wa.us`, `brookings.edu`, `nm.gov`): confirmed that neither CSTA nor the K-12 Computer Science Framework publishes a mandatory weekly minute figure, leaving scheduling to states and districts.
- Any remark on typical district scheduling or pedagogy not opened in full (PRIMM, use-modify-create, notional machine) rests on memory ("from memory").

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Complete Unit fields 1 to 10 and Section fields 1 to 11 in APPROACH.md, move few-device/one-screen stand-ins to Section fields 5 and 10, and add "What a tool may and may not do" | Matches UNIT-PLAN.md placement and closes C7, C8, C9, C13, C14 and C15 gaps | docs/courses/computer-science/APPROACH.md |
| Add data sovereignty to `g7-personal-data`, peripherals to `g9-operating-systems`, and using generated data in a simulation to `g9-simulate-data` | Closes C1 and UNIT-PLAN rule 19 ("always cover the whole standard") | data/progressions/computer-science.csv |
| Remove `repeat` from grade 1 `g1-code-sequence` words; align `g10-analyze-code` to 20 lines; fix stale grade-12 note on `g9-data-and-people` and typo on `g7-impact-history` | Removes grade-1 construct leak, reading-load conflict and copy errors | data/progressions/computer-science.csv |
| Fix stale status, checker, band-label and hyphen-space lines | Removes direct contradictions across pre-work files | docs/courses/computer-science/APPROACH.md, STANDARD.md, docs/ADOPTION-BAR-SUBJECTS.md, data/subjects.csv, data/standards/csta-2026-specialty-ids.txt, csta-2026-statements.txt |
| Reject `S1-XCS-*` in `scripts/progression.py` `code_grades` for computer science | Enforces STANDARD.md section 3 exclusion mechanically | scripts/progression.py |

## Questions for Cory

1. **Default period length and annual sessions by band (Finding 3).** Sessions a week are settled (1 in K to 5, 2 to 3 in 6 to 12), but no minutes per session or single 6 to 12 default is set. Recommended: K to 2, 32 sessions of 30 minutes; grades 3 to 5, 32 sessions of 40 minutes; grades 6 to 8, 64 sessions (2 a week) of 45 minutes; grades 9 to 12, 96 sessions (3 a week) of 45 minutes, with frames free to adjust with a reason. Yes, or different defaults?
2. **Catalogue grain in `data/courses.csv` (Finding 5).** Line 35 has one row (`cs-k12`) with stale 2017 band notes (`K-2 3-5 6-8 9-10 11-12`), while STANDARD.md sets 13 grade courses. Recommended: keep the one `cs-k12` row (matching `math-k8` and `ela-k12`) and update its notes to "One course per grade K to 12; 2026 CSTA PK-12 (EK, E1 to E5, MS, HS Foundational plus eight named S1 ids in grades 11 and 12)". Or split into per-band or per-grade rows?
3. **Text programming language for grades 6 to 12 (Finding 6).** STANDARD.md says the browser-editor decision settles the text language, but no page names it. Recommended: Python (matches the UK Teach Computing Curriculum key stage 3 partial base and fits grades 9 to 12 data and AI tasks, run offline in our single-file browser editor), or JavaScript (zero runtime overhead in any browser). Which?
4. **Leave-out rule for computer science units (Finding 2).** ADOPTION-BAR-SUBJECTS.md says each course page states what a school may leave out. Recommended: no computer science unit is opt-out by default (all five concepts are required and society cases follow the values rule with two views and dated sources), and if a school drops a society or AI unit, later units do not assume it and the course page states which CSTA ids are no longer claimed that year. Yes or no?
5. **Enforcing the 8-id S1 allowlist in `scripts/progression.py` (Finding 7).** Recommended: reject `S1-XCS-*` in computer science and restrict `S1` ownership in `code_grades` to the four named grade-11 ids and four named grade-12 ids (STANDARD.md section 2). Yes, or reject only `S1-XCS-*`?

## Against the first read

Comparing this independent read with `docs/reviews/prework-computer-science-read-2026-11-19.md` (which was run before the 2026-11-19/20 fixes and before `data/progressions/computer-science.csv` was written):

- **Already in the first read (and still open or only partly fixed):**
  - Finding 1 (part): the first read caught the broken section fields 7 to 10 in APPROACH.md, and its fix was applied, but its own replacement block still omitted unit fields 1, 3, 4, 5, 6, 7, 9 and 10, section field 2, and "What a tool may and may not do", and misplaced few-device/one-screen into unit field 8.
  - Finding 3 (part): the first read caught missing session length and weeks a year (first read Finding 14); the fix deferred them to course frames without setting default minutes per band or citing CSTA's lack of a published time figure.
  - Finding 5 (part): the first read caught the stale note in `csta-2026-specialty-ids.txt` line 9, `data/subjects.csv` line 8 (first read Finding 21), and the four hyphen-space breaks in `csta-2026-statements.txt` (first read Finding 23); none of those three edits were applied.
  - Finding 9: the first read already flagged the missing boundary statements, sub-concept key, twelve-practices table and unread APPROACH.md sources (first read Findings 6, 17, 18); all four remain owed.
- **New in this second-model read:**
  - **Finding 1 (new parts):** full unit-field placement audit (unit fields 1, 3, 4, 5, 6, 7, 9, 10 and section field 2 missing; few-device/one-screen misplaced in unit field 8; common bug duplicated in section field 1; "What a tool may and may not do" section missing; one-child home pair-programming adaptation missing in section field 10).
  - **Finding 2:** sensitive ground unnamed (no `sensitivity-read.md` triggers, no sensitive-topic teacher-note rule, no reporting route for online-safety disclosures, no leave-out rule).
  - **Finding 4:** progression coverage and consistency faults in `data/progressions/computer-science.csv` (`MS-DAT-IM-28` missing data sovereignty, `HS-SYS-HW-29` missing peripherals, `HS-DAT-DC-21` missing use in a simulation, grade-1 `repeat` leak in `E1-PRO-PD-04`, 30-line vs 20-line reading-load contradiction in `g10-analyze-code`, stale grade-12 note in `g9-data-and-people`, typo in `g7-impact-history`).
  - **Finding 5 (new parts):** stale 2017 CSTA bands in `data/courses.csv` line 35, and post-fix status contradictions across `APPROACH.md` (lines 3 to 4 and 126), `STANDARD.md` (lines 19 and 76) and `ADOPTION-BAR-SUBJECTS.md` (lines 334 and 566).
  - **Finding 6:** text programming language stated as settled by the editor decision but never named.
  - **Finding 7:** `scripts/progression.py` `code_grades` allows `S1-XCS-*` and any of the 73 S1 ids in computer science grades 11 and 12.
  - **Finding 8:** cross-subject leans in STANDARD.md section 4 name no core progression skill ids, and `computer-science.csv` omits social studies, library and career leans.
  - **Outside verification:** web-search verification of the 2026 CSTA PK-12 Computer Science Standards (DOI, licence, structure and sample codes) and CSTA's lack of a published instructional-time figure.
