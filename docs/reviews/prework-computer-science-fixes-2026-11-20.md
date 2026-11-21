# Computer science pre-work: stage 1 fix pass, 2026-11-20 (run 2026-11-21)

Read: the second-model read (docs/reviews/prework-computer-science-gemini-2026-11-20.md, findings 1 to 9 and its five
questions, the main list); the real-page findings of the two calibration reads (docs/reviews/calibration-computer-science-2026-11-20.md,
expert #6 and #8; calibration-computer-science-gemini-2026-11-20.md, Gemini cal #10, #12 to #15 and the g5-who-included
finding inside #10); the computer science parts of data/plans/later.csv L96; and the first read
(docs/reviews/prework-computer-science-read-2026-11-19.md) only to avoid reopening settled points and to catch what is
still wrong. Settled calls read first: DESK-ANSWERS entries for q-later-cs-career-library, q-later-followups-1,
q-prework-cs-1, q-prework-open-1 and -2, q-fix-pe-1 and q-fix-health-1. Every row claim was checked against the
statement in data/standards/csta-2026-statements.txt and the row in data/progressions/computer-science.csv; the HS
ownership split was counted from the csv (12, 12, 12, 10). `python -X utf8 scripts/progression.py check computer-science`:
0 failures after the fixes.

| # | Source | What | Decision | Where |
|---|---|---|---|---|
| 1 | gemini #1.1 | Unit field 1 (header) gives no sessions or period length | Not a fault: the shared header stands and the frame holds sessions and minutes; the page now says in one line that unnamed fields are filled as UNIT-PLAN.md says | APPROACH.md, plan fields opening |
| 2 | gemini #1.2 | Unit field 2 drops the limits | Fixed: field 2 names the limits (depth taught to and what is left out) and points to STANDARD.md "Depth" | APPROACH.md, unit field 2 |
| 3 | gemini #1.3 | Unit field 3 (where it sits) absent | Not a fault: shared field; strong or weak handoff is already UNIT-PLAN's, and the weak K to 1 handoff is in STANDARD.md section 2 | |
| 4 | gemini #1.4 | Unit field 4 (readiness check) absent; proposes a K to 5 reteach in the next session | Not a fault: the shared rule and timing stand; the proposed reteach timing would be new policy | |
| 5 | gemini #1.5 | End-of-unit assessment sits in the kinds-of-day table, not unit field 5 | Fixed: moved to unit field 5; the Check row points there | APPROACH.md, kinds of day and unit field 5 |
| 6 | gemini #1.6 and #1.10, gemini cal #14 | Section field 1 carries "the common bug and what it shows", which belongs to the error register (unit field 6) | Fixed: removed from section field 1; unit field 6 now letters common bugs and notional-machine errors, one mistake per letter, with what each shows | APPROACH.md, unit field 6, section field 1 |
| 7 | gemini #1.7 | Unit field 7 (response allocation) absent | Not a fault: the shared marking step fits (trace items marked on the key, the build or debug task teacher-judged after class); Gemini's group cap and no-hands-up rule would be new policy | |
| 8 | gemini #1.8, gemini cal #14 | Unit field 8 holds the few-device and one-screen versions (STANDARD.md sends them to section fields 5 and 10), and lacks the TOOL-ASKS.md link, supplies list and notes for technical staff (bar item 7) | Fixed: device versions moved to section field 5 (few-device, no-device) and 10 (one screen); field 8 has the TOOL-ASKS.md link, the supplies list with the optional board's cost, and one line for technical staff | APPROACH.md, unit field 8, section fields 5 and 10 |
| 9 | gemini #1.9 | Family note (in English and Spanish) and sources have no slot | Family note: not a fault, the shared field stands, and Spanish across the site is parked (later.csv L60). Sources: fixed, unit field 10 points to the partial base's third-party check and each society case's dated source | APPROACH.md, unit field 10 |
| 10 | gemini #1.10 | Section field 2 dropped; section field 10 has no one-child pair answer | Section field 2: not a fault (shared). Field 10: fixed, at home the parent takes the other pair role and they switch when field 7 says (item-level choice, ours) | APPROACH.md, section field 10 |
| 11 | gemini #1.11 | No "What a tool may and may not do" | Fixed: one line in unit field 8 says what a tool may do and points to STANDARD.md section 5 and the daily evidence for what it may not (each rule kept once) | APPROACH.md, unit field 8 |
| 12 | gemini #1.10 (section field 11) | Section field 11 restated the shared field | Fixed: dropped from the list, now named among the fields with nothing added | APPROACH.md |
| 13 | gemini #2, gemini cal #10, L96 | No sensitive ground: no sensitivity-read trigger, teacher note, disclosure steps or leave-out rule | Fixed: new "Sensitive ground" section gathers what the pages already say (bias, exclusion and access; data about people and communities, data sovereignty; online safety; work and automation), the teacher note in section field 1, the sensitivity agent for cultural, Native and disability content (FOUNDATION section 7), and health's disclosure steps on online safety and personal information pages as PE's (q-fix-pe-1). Leave-out: question for Cory 2 | APPROACH.md, "Sensitive ground"; section field 1 |
| 14 | gemini cal #10, L96 | g5-who-included owns E5-SOC-HI-16 ("inclusion or exclusion") but teaches exclusion only, with no two views | Fixed: inclusion cases added, two views and a dated source each, task lists who was included or left out; "from memory, to be checked" kept | computer-science.csv, g5-who-included |
| 15 | gemini #3, gemini cal #13 | Line labelled "Minutes:" gives no minutes; 6 to 12 is a range; no period length | "Minutes:" relabelled "Sessions a week:" with a line that minutes and sessions a year are not yet set. Defaults: question for Cory 1 (a dose choice) | STANDARD.md section 2; APPROACH.md "Open for Cory" |
| 16 | gemini #4.1 | g7-personal-data drops sovereignty from MS-DAT-IM-28 | Fixed: sovereignty added to words and notes (checked against the statement) | computer-science.csv, g7-personal-data |
| 17 | gemini #4.2 | g9-operating-systems drops peripherals from HS-SYS-HW-29 | Fixed: peripheral added to words; notes add peripherals reached through a driver card | computer-science.csv, g9-operating-systems |
| 18 | gemini #4.3 | g9-simulate-data never uses the data "for use in a simulation" (HS-DAT-DC-21) | Fixed: the generated set is fed into a short supplied simulation and a parameter is changed | computer-science.csv, g9-simulate-data |
| 19 | gemini #4.4 | g10-analyze-code reads a thirty-line program; APPROACH caps 6 to 12 at twenty | Fixed: twenty-line | computer-science.csv, g10-analyze-code |
| 20 | gemini #4.5 | g1-code-sequence words include repeat; E1-PRO-PD-04 asks sequence only, iteration is E2 | Fixed: repeat removed (no E1 or EK statement names iteration) | computer-science.csv, g1-code-sequence |
| 21 | gemini #4.6 | g9-data-and-people says "Owned in grade 12" then names grade 11 | Fixed: stale clause removed (HS-DAT-IM-27 is grade 11's, q-prework-cs-1) | computer-science.csv, g9-data-and-people |
| 22 | gemini #4.6 | g7-impact-history says "unplugged side effects" | Fixed: "unintended side effects" (MS-SOC-HI-39) | computer-science.csv, g7-impact-history |
| 23 | gemini cal #15 | g5-visual-algorithm never names events, which E5-ALG-PS-01 asks for | Fixed: event added to words; the flowchart starts on an event and repeats a step | computer-science.csv, g5-visual-algorithm |
| 24 | expert cal #8 | "A rotating third each day, so every student is read at least once a week" does not add up at one to three sessions a week | Fixed: the arithmetic is stated honestly (once in every three sessions, once in three weeks in K to 5) | APPROACH.md, "The form of daily evidence" |
| 25 | expert cal #6, L96, gemini #9, first read #6 | The boundary statement sets the depth but is stored nowhere, so depth comes from the one-line statement | Fixed on the page: "Depth" says plainly the store is owed and the progression's owner rows are checked again when it lands; the owed table lists the store, the sub-concept key and the practices table. The store itself: follow-up 4 | STANDARD.md section 1 "Depth"; owed table |
| 26 | gemini #9, first read #17 and #18 | Sub-concept key, practices table and an approach source still owed | Owed row added (as 25); the extraction and one read pedagogy source: follow-up 4 | STANDARD.md owed table |
| 27 | gemini #5.1, gemini cal #12 | courses.csv cs-k12 notes give the 2017 bands | Question for Cory 4 (a catalogue row) | |
| 28 | gemini #5.2, first read #21 | subjects.csv line 8 says "CSTA K-12" | Follow-up 1 (shared file) | |
| 29 | gemini #5.3 | APPROACH.md header still a draft and "Still open: our own editor" | Fixed: header gives the approval (q-prework-cs-1) and the fix dates; Settled lists the approval and the editor (q-prework-open-1); "Open for Cory" lists what is really open | APPROACH.md header, Settled, Open for Cory |
| 30 | gemini #5.4 | STANDARD.md owed table says the approach page waits on Cory; "Each HS year owns 11 or 12 ids" while grade 12 owns 10 | Fixed: table row says approved; HS split stated as 12, 12, 12, 10 (counted from the csv) with the IM-27 move; the page header no longer says "a draft for Cory's yes" | STANDARD.md header, owed table, section 2 |
| 31 | gemini #5.5 | ADOPTION-BAR-SUBJECTS.md part 5 says "The high school course" and the owed row still lists the S1 list and the editor | Follow-up 2 (file not editable here) | |
| 32 | gemini #5.6, first read #21 | csta-2026-specialty-ids.txt header says the checkers do not read it, "the high school course", "module" | Fixed: header line names the four courses, the eight S1 ids, S2 and X + CS left out, and that both scripts read the file (checked) | data/standards/csta-2026-specialty-ids.txt, header |
| 33 | gemini #5.7, first read #23 | Four hyphen-space breaks in the statements file body | Follow-up 3 (standards file body) | |
| 34 | gemini #6 | The editor decision is said to settle the text language, but no language is named (the Desk entry names none) | Fixed: the page no longer claims it is settled; it says the language is the editor's and not yet named. The pick: question for Cory 3 | STANDARD.md "Our own editor" |
| 35 | gemini #7, gemini Q5 | progression.py accepts any S1 id, X + CS included, in grades 11 and 12 | Follow-up 5 (gate tightening to a settled rule, not a new call) | |
| 36 | gemini #8 | STANDARD.md section 4 names no core skill ids; the csv has no social studies, library or career leans | Not a fault for the ids: they live in the csv's cross_subject column where the check tests them, and the page now says so. Library and career are not core subjects (COURSE-RUN: leans name a core skill), and the page now says they are not leans. Social studies: no grade 9 to 12 row in data/progressions/social-studies.csv teaches government or technology policy, so no lean can point yet: follow-up 6 | STANDARD.md section 4 |
| 37 | first read #21 | docs/APPROACH.md opening still lists only math, ELA, science and social studies approach pages | Follow-up 7 (file not editable here) | |
| 38 | first read #21 | ADOPTION-BAR-SUBJECTS.md part 5 "Standards" paragraph argued with itself | Not a fault now: it reads "Loaded" | |
| 39 | gemini Q1 to Q4 | Questions on minutes, catalogue grain, text language, leave-out | Carried as questions for Cory 1 to 4 | |

Counts: fixed 27 (rows 2, 5, 6, 8, 9 sources, 10 field 10, 11 to 14, 15 label, 16 to 26, 29, 30, 32, 34, 36 wording);
not a fault 8 (rows 1, 3, 4, 7, 9 family note, 10 section field 2, 36 ids, 38); questions 4 (from rows 13, 15, 27,
34); follow-ups 7. Rows 9, 10, 13, 15, 25, 34 and 36 carry two decisions each.

Not added (new policy in the second read's proposed text): a K to 5 reteach slot, a four-group respond cap, family
notes in Spanish, a "no opt-out unit" default, the national hotline line (health's steps are pointed to instead), and
a ban on tools grading open explanations beyond what the daily evidence already says.

## Questions for Cory

1. **Default minutes a session and sessions a year.** Sessions a week are settled (one in K to 5, two to three in 6 to
   12); minutes and sessions a year are not, so a frame cannot test C2 or the S1 10 percent cap. Recommended (ours,
   untested, as PE's defaults were set): K to 2, 32 sessions of 30 minutes; 3 to 5, 32 of 40; 6 to 12, 64 a year (two a
   week) of 45 minutes, a frame may change them with a reason. Why two a week in 6 to 12: each high school year owns
   10 to 12 ids, and three a week (96 sessions) would put more days outside the standards than C1 allows.
2. **What a school may leave out.** The bar asks each course page to say it; health and PE have rules (PE: a named unit
   may be swapped or left out, and the course then claims no standard no remaining unit teaches). Recommended: the
   same as PE: a school may leave out a named society or AI unit for its community's reasons, later units do not
   assume it, and the course page then claims none of its ids.
3. **The text language for grades 7 to 12** (and grade 6's side-by-side view). Recommended: Python, because the K to 8
   partial base teaches Python in its middle years, so units adapt directly, and it is the most common first text
   language in high school courses; the alternative is JavaScript, which a browser runs with no added runtime.
4. **The cs-k12 catalogue row** (data/courses.csv line 41 notes "CSTA bands K-2 3-5 6-8 9-10 11-12", the 2017 bands).
   Recommended: keep one cs-k12 row (13 grade courses under the track are settled) and change its notes to "One course
   per grade K to 12; 2026 CSTA PK-12 bands EK, E1 to E5, MS, HS, plus eight named S1 ids in grades 11 and 12".
   Alternative: four band rows as health, PE, SEL and ELD.

## Follow-ups for the lead

1. data/subjects.csv line 8: "CSTA K-12" to "2026 CSTA PK-12".
2. docs/ADOPTION-BAR-SUBJECTS.md: part 5 "Standards", "The high school course teaches" to "The four high school
   courses teach", with the eight named S1 ids (q-prework-cs-1); line 566, move the S1 list (L84 done) and our own
   editor (q-prework-open-1) out of "Owed".
3. data/standards/csta-2026-statements.txt body lines 129, 255, 270, 308: join "large-scale", "device-to-device",
   "human-centered", "large-scale", and add the repair to the header's fetch note.
4. From the CSTA PDF (it can only be read by downloading it): a boundary-statement store in data/standards/ (planning
   only, under the statements' licence), the sub-concept key, and the practices table (STANDARD.md section 3); then
   re-check every owner row in computer-science.csv against its boundary statement. Also read one open pedagogy
   source (for example a published PRIMM summary) into APPROACH.md "Honest limits" and docs/APPROACH-SOURCES.md.
5. scripts/progression.py `code_grades`, computer science: return `[], []` for `S1-XCS-*`, and accept only the eight
   named S1 ids (four in grade 11, four in grade 12, STANDARD.md section 2).
6. When the social studies government course (data/courses.csv `government`) has progression rows, add
   `social-studies:` leans to g11-policy-change, g12-data-policy-debate and g12-law-policy.
7. docs/APPROACH.md opening paragraph: list the after-core subject approach pages (computer science among them).

Lead, 2026-11-21: follow-ups 1 to 3 done (subjects.csv standards name, the bar lines, the four rejoined words in the statements file). Follow-up 4 needs a download of the standards PDF and waits for Cory; 5 to 7 are on the lead's list. The four questions are on the Desk (q-fix-cs-1).

## Cory's answers applied (2026-11-21, Desk q-fix-cs-1)

1. Default minutes and sessions: STANDARD.md section 2, the sessions line (K to 2, 32 of 30; 3 to 5, 32 of 40; 6 to 12, 64 of 45; a frame may change them with its reason; each band's scope and sequence names its short path); APPROACH.md "Pacing" points there.
2. Swap and leave-out: STANDARD.md section 3, new bullet in PE's and the arts' wording; APPROACH.md "Sensitive ground" points there.
3. Text language: STANDARD.md "Our own editor" names Python for grades 6 to 12, "Blocks to text" names Python at each grade step.
4. Catalogue: STANDARD.md section 2 says the one `cs-k12` row stays, with the lead's corrected notes; no page described the old notes.

APPROACH.md "Settled" lists all four; "Open for Cory" now says nothing is open.

## CSTA standards PDF read (2026-11-21, Desk q-fix-downloads-1)

Follow-up 4, the parts that wait on the PDF. The PDF was downloaded from csteachers.org into
S:\CurioClass-sources\computer-science\csta-2026-11-21\ (README there: read once, ids and structure only, not for the
public site), and its text taken by script. Licence printed in the PDF: CC BY-NC-SA 4.0, reuse and adaptation allowed
with credit, non-commercial, same licence; nothing from it was copied into a page.

- Ids and statements: the PDF holds the same 331 ids as csta-2026-ids.txt and csta-2026-specialty-ids.txt, and every
  statement in csta-2026-statements.txt matches it apart from whitespace, quote marks and hyphen forms (checked line added
  to the statements file header).
- Sub-concept key: done, STANDARD.md section 1 (codes and names from the PDF's naming tables, our one-line meanings).
- Practices table: done, STANDARD.md section 3 (codes ESR1 to HCD12, our labels, the bar item each serves).
- Boundary statements against the progression: every owner row of data/progressions/computer-science.csv read against
  its boundary statement; 34 rows fixed. Past the limit: g4-written-algorithm taught the flowchart, which E4-ALG-PS-01
  says is not expected (now numbered sentences; the flowchart moves to g5-visual-algorithm, which E5-ALG-PS-01 allows);
  g2-algorithm-peers and g4-algorithm-groups asked students to design a fairer rule (not expected in E2 or E4;
  removed); g6-procedures listed parameter (not expected in MS-PRO-PD-12; removed). Below the depth the boundary sets,
  one clause added each: g1-data-questions, g2-explain-build, g2-data-questions, g3-make-improve, g3-data-groups,
  g4-data-people, g5-use-or-not, g6-precision-metadata, g6-packets, g7-viz-choices, g7-personal-data (the cross-border
  sense of sovereignty), g8-ml-evaluate (model card), g8-evaluate-ai-code, g9-computing-history, g10-design-hcd,
  g10-clean-text, g10-network-of-networks, g10-apis-docs, g10-breach-causes, g11-infrastructure-impact,
  g11-data-scale-ethics, g12-data-policy-debate, g12-law-policy, g12-diverse-teams (published accounts of
  professionals). Specialty I rows brought to their S1 boundary: g11-multivariate-viz, g11-evaluate-vs-spec,
  g11-fix-security-flaw, g12-evaluate-ai-output, g12-refine-with-users. `progression.py check computer-science`: 0
  failures.
- Boundary-statement store: not made (the README limits the PDF to ids and structure). Depth now sits in each owner
  row's notes; STANDARD.md "Depth" says so. Whether to store the boundary text: question for Cory 5.
- STANDARD.md owed row closed; lens and APPROACH.md unit field 2 point to the owner row's notes and the practice codes.

Questions for Cory (new): 5, store the boundary statements and each standard's practice and disposition pairing in
data/standards/ under CSTA's licence, planning only (recommended yes); 6, S1-SWD-PP-08 asks for a version-control
workflow (branching, review, merging) that g12-team-workflow leaves out (recommended: a small offline version history
with branch and merge in our own editor, the id marked part met until it exists); 7, g7-lists and g8-text-project
teach lists, which MS-PRO-VD-16 and MS-ALG-PS-01 say are not expected in middle school (recommended: keep them and count
the list days as days outside the standards under C1, since Python's list is the natural first structure and the HS
rows build on it).

Still open from follow-up 4: one open pedagogy source for APPROACH.md "Honest limits" and docs/APPROACH-SOURCES.md
(not a PDF task; lead's list).
