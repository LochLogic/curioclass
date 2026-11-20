# Expert read: the computer science progression draft, K to 12 (2026-11-19)

Read cold, as a draft that is not yet in data/progressions/. Edited nothing but this report.

## What I read

- data/progressions/parts/computer-science.csv: 202 rows (K 14, 1 15, 2 14, 3 15, 4 16, 5 16, 6 18, 7 19, 8 18, 9 17, 10 15, 11 13, 12 12).
- data/progressions/parts/computer-science-edges.md: the band-crossing handoffs and the 11 placement choices.
- Gate: `gate_part.py computer-science ...` gave 0 failures on 202 rows. plan.py not run, as told. `scripts/stale.py check`: 62 files, 0 failures.
- The bar: docs/agents/EXPERT.md, docs/agents/lenses/computer-science.md, the computer science part of docs/ADOPTION-BAR-SUBJECTS.md (section 5), docs/courses/computer-science/STANDARD.md in full. APPROACH.md only skimmed (opening and plan-field sections).
- Standards: data/standards/csta-2026-ids.txt (196 ids) and csta-2026-statements.txt (read for about 90 ids to judge placement; no wording copied below).
- To check leans (read only, outside the draft): data/progressions/math.csv, science.csv and ela.csv, looked up by id only. Titles of earlier reviews in docs/reviews/ (health and physical education 2026-11-19, math 2026-11-13) read for the kinds of finding that repeat.
- Checked by script: every one of the 196 ids is owned exactly once, none is missing or invented; every E-band id sits in the matching grade; every assumes and hands_on points at a real row exactly one grade away (the only gaps are rows with no hands_on, in finding 4); no model_in is used before the grade that introduces it. Counts by grade and concept for MS (17/15/13) and HS (12/12/11/11) match the edges file.
- Not read: the reconcile report (there is none yet for this subject), any earlier course page.

## Verdict

Sound and close to adoptable. Ownership is right (the ordering constraints in STANDARD.md all hold, the MS and HS splits are defensible, and the rows are real teaching days, not padding), the five concepts run in every grade, unplugged work is in nearly every row, and no company, product, language or editor name appears. The biggest risk is not the placements the writer asked about but the layer around them: seven of the cross-subject leans name a math standard that does not match the day, three strands (generated-code evaluation, attribution, data-and-people) skip two to four grades, and the HS rows from grade 10 on carry one-sentence notes that a writer cannot build a unit from. The one change that matters most is to repair the handoffs and leans (findings 2 and 4), then thicken the grade 10 to 12 notes (finding 7).

Findings: 13 (3 moderate-to-serious, 7 moderate, 3 minor; none blocks the draft). Placements judged: the writer's choices 1, 2, 4, 6, 7, 8, 9, 11 stand as written; choice 3 stands with one move proposed (finding 1); choice 5 stands with one merge (finding 9); choice 10 needs the ELA leans in finding 2.

## Findings, most serious first

### 1. Grade 12 owns 11 ids but two rows are multi-week projects; the data-and-people strand stops for two years (moderate; judgment call; LAYER progression; REPEAT new)

Rows: g12-capstone-build, g12-team-workflow, g12-refine-with-users, g12-data-scale-ethics, g12-data-policy-debate, g11-evaluate-simulation.
Grade 12 has 12 rows, but the capstone and the team workflow are written as "several weeks" each and the refine-with-users day follows them, so three of the 12 rows take most of the year; the other nine are single unplugged society and policy days. Meanwhile HS-DAT-IM-27 and HS-DAT-IM-28 both land in grade 12 and the data-and-people strand (MS-DAT-IM-28, -29, then g9-data-and-people) has no row in grades 10 and 11. The two grade 12 rows assume g11-evaluate-simulation and g11-policy-change, which are not their real prerequisites (a simulation review is not large-scale data ethics); the real prerequisite is g9-data-and-people, three years before.
Fix: move HS-DAT-IM-27 to grade 11 (own it in a new row g11-data-scale-ethics, the row now called g12-data-scale-ethics, assumes g9-data-and-people; hands_on g12-data-policy-debate), and keep IM-28 in grade 12 (assumes g11-data-scale-ethics). HS split becomes 12/12/12/10 and grade 11 gains one DAT id. This fixes both the strand gap and the "debate follows the review in the same year" worry in choice 4, and it lightens the year that holds a capstone. It breaks the "each HS year owns 11 or 12 ids" line in STANDARD.md, so that line changes with it (finding 12). Confidence: judgment call; a reviewer who wants every grade at 11 or 12 can keep the writer's split and accept the capstone squeeze.

### 2. Cross-subject leans: seven name a math standard that does not fit the day, they are standard codes not skill ids, and ELA has none (moderate; firm; LAYER progression; REPEAT yes, same kind as the health and physical education reads and the math read)

Checked each `math:` code against the skill that owns it in data/progressions/math.csv.
Wrong or too thin, remove the lean:
- k-follow-steps (math:K.G.A.1, owned by mk-shapes-positions: shapes and positions; the day is ordering routine steps). Keep K.G.A.1 on k-sequence-commands only (position and direction words, a true fit).
- g1-split-task (math:1.OA.B.3, m1-properties-strategies: properties of operations; the day is breaking a task into parts).
- g2-name-and-label (math:2.MD.D.10, m2-picture-bar-graphs: drawing graphs; the day is naming a stored value).
- g3-algorithm-combo (math:3.OA.D.8, m3-two-step-problems; the day is if and else on a made-up route). Keep the lean on g3-read-code, where a letter stands for an unknown and the fit is real.
- g5-variables-use (math:5.OA.B.3, m5-two-patterns). Keep on g5-visual-algorithm (a counter that adds the same amount each time round).
- g6-verify-algorithm (math:6.SP.B.5, m6-summarize-data: summarizing a data set; the day is test inputs and expected output).
- g6-data-quality (math:6.SP.B.5) and g6-precision-metadata (math:6.SP.A.2, m6-statistical-questions): thin. Remove, or replace with a lean the math progression can actually back; I could not find one.
Format: the lean column names standard codes for math and skill ids for science. The lens and the brief ask for a skill. The ones I could resolve: m2-arrays-equal-addends (2.OA.C.4), m4-patterns (4.OA.C.5), m7-chance-probability (7.SP.C.5), m3-two-step-problems (3.OA.D.8). The rest (K.MD.B.3, 1.MD.C.4, 3.MD.B.3, 6.EE.A.2, 7.RP.A.2, 7.SP.A.1, 8.F.A.1, 8.SP.A.1) the writer should convert with the same lookup. Science leans (s3-weather-data, s3-design-problem, s4-information-codes, s5-design-test, s6-digital-signals, s7-design-optimize) all exist and are owned at or before the grade that leans: met.
Timing: most leans name the math skill of the same grade, which is allowed ("at or before") but the math skill may come later in the year than the computer science day. STANDARD.md already says frame "if later" lines bridge; each such row should say so in its note (for example g3-check-data and g6-sort-filter-tool).
ELA (choice 10): add leans; STANDARD.md section 4 already names explaining an algorithm in writing and feedback. All ids below exist at that grade in ela.csv. Proposed: g2-explain-build -> ela:e2-tell-and-record; g3-make-improve (feedback step) -> ela:e3-writing-process; g4-team-document (documenting for a reader) -> ela:e4-explain-events; g8-investigation-summary -> ela:e8-produce-publish; g8-emerging-debate -> ela:e8-collab-discussion; g12-data-policy-debate and g12-human-vs-ai -> ela:e12-seminar; g12-values-in-design (a written paragraph) -> ela:e12-informative. The answer to "should there be any" is yes, these seven; more is padding.

### 3. Grade 3 packs four first-times into two rows (moderate; likely; LAYER progression; REPEAT new)

Rows: g3-read-code, g3-make-improve, g3-debug-combo.
g3-read-code teaches a variable in running code, introduces the trace-table, and teaches "what is this part for" (E3-PRO-RD-07), all in one device-and-unplugged day, with the assignment-is-not-equality misconception. g3-make-improve introduces selection in blocks, the block-and-text-view, and a feedback loop with a look-for list. For a once-a-week course with eight-year-olds that is two rows doing the work of four, and the row count (15 of a 14 to 16 range) has room.
Fix: split g3-read-code into g3-read-code (E3-PRO-RD-07: what a part of a block program is for, no variable, trace by pointing; hands_on g4-team-document) and g3-variable-trace (E3-PRO-VD-06, named-box to trace-table; assumes g2-name-and-label; hands_on g4-trace-values; model_out trace-table, named-box). Grade 3 becomes 16 rows; g3-debug-combo assumes both. Keep the block-and-text-view in g3-make-improve.

### 4. Handoffs: one orphan, two strands that skip years, three weak assumes (moderate; firm; LAYER progression; REPEAT yes, same kind as the health and physical education reads)

- g7-lists teaches lists and hands on to nothing, but g8-text-project is built on "variables, a list and a procedure" and assumes only g7-design-with-variables and g7-analyze-code. Fix: g7-lists hands_on g8-text-project; g8-text-project assumes add g7-lists.
- g6-precision-metadata has no hands_on, but metadata is the first idea in g7-personal-data. Fix: hands_on g7-personal-data (and g7-personal-data assumes g6-precision-metadata beside g6-data-about-people).
- Generated-code evaluation: g8-evaluate-ai-code (MS-PRO-RD-18) has no hands_on; its HS match g11-evaluate-generated-code assumes g10 rows only; nothing in grades 9 and 10 touches it. Fix: in g10-analyze-code add one saved sample read and traced (a note, and a lean ~HS-PRO-RD-18); g11-evaluate-generated-code assumes add g8-evaluate-ai-code only if the writer wants the long link visible, otherwise leave.
- Attribution: g8-attribution (MS-PRO-PD-14) has no hands_on, and HS-PRO-PD-14 is not met until g12, though grades 9 to 11 use library functions (g9-modular, g10-apis-docs) and generated code (g11). Fix: add `~HS-PRO-PD-14` to g10-apis-docs ("credit the library and the documentation page in a comment") and to g11-evaluate-generated-code (note ownership of a generated sample); g12-attribution stays the owner. Choice 3 (PD-14 in grade 12) stands on this condition.
- g9-det-vs-prob assumes g8-ai-tool-day, which is the one-screen generated-text day and not a prerequisite for deterministic against probabilistic. Real prerequisite: g8-ml-evaluate (an output that differs and errs) plus the math lean. Fix: assumes g8-ml-evaluate; g8-ai-tool-day hands_on g9-det-vs-prob is dropped (it then has none; that is acceptable, see next point).
- g11-infrastructure-impact assumes g10-network-diagram, but the id is an impacts id; the real earlier row is g8-design-for-all (access and design for different users) and g7-access-differences. Fix: assumes g8-design-for-all; keep g10-network-diagram as a second assume only if infrastructure means networks in the day.
- g12-data-scale-ethics: see finding 1.
Rows that end a strand without a handoff and are fine: g8-refine-for-users, g8-design-for-all (after the fix above it hands to g11), g9-det-vs-prob, g9-operating-systems, g9-device-limits, g10-network-of-networks, g11-training-data-review (hands to g11-build-ml-model, same grade: add that), g11-fix-security-flaw.

### 5. Order inside a grade is written only in notes, and one note contradicts its own order (moderate; firm; LAYER progression; REPEAT yes, same kind as science read finding 9 and the physical education read finding 12)

The gate does not see in-grade order. Dependencies that the scope and sequence must keep, none yet recorded in one place:
- Grade 3: g3-make-improve (block-and-text-view) before g3-read-code (assumes it) before g3-debug-combo (trace-table).
- Grade 6: g6-variable-types (introduces the text-program) before g6-procedures and g6-inclusive-collab (both use it); g6-model-algorithm (introduces pseudocode) before g6-careers-ct (writes pseudocode lines).
- Grade 6 contradiction: g6-model-algorithm asks for "a call to a named procedure" in a flowchart, and its note says students write their own procedures in g6-procedures, which owns MS-PRO-PD-12. MS-PRO-PD-12 is owned in grade 6 so g6-procedures can run first. Fix: add to both notes "g6-procedures runs before g6-model-algorithm" (or reword the model row to name a procedure given, not written).
- Grade 9: g9-structures-program before g9-design-with-structures (constraint, written); g9-modular after both.
- Grade 11: g11-training-data-review before g11-build-ml-model (written); g12-diverse-teams after g12-team-workflow (it reads a log from it; written).
Fix: add a short "order in the grade" line to the note of the first row of each grade named above, so a scope and sequence writer sees it.

### 6. Two near-duplicate days and one overlap (moderate; firm for the first, judgment call for the second; LAYER progression; REPEAT new)

- g9-network-sketch (~HS-SYS-NT-34: sketch a school network, label hardware and software) and g10-network-diagram (HS-SYS-NT-34: diagram a small office network with hardware and software, trace one request) are the same task. Fix: make g9-network-sketch a read-and-trace day (students read a given school network diagram and trace one request through it, read before write), and keep drawing in g10. This also keeps the g8-network-failure to g10 chain honest.
- g7-system-requirements (write requirements, compare two options, name a tradeoff, add environmental effect) and g8-choose-a-system (choose between two systems against class-written requirements, energy and ethics note) overlap. Fix: grade 7 writes requirements for a given family or shop; grade 8 chooses between two systems against requirements written by a different group, with the written justification checked against them. Say so in the g8 note.
- g8-network-failure after g7-internet-resilience: both trace packets around a failure. Keep (the task does change from "find another path" to "redraw and add a backup link"), but state the new task in the g8 note.

### 7. High school notes are one line from grade 10 on (moderate; firm; LAYER progression; REPEAT new for this subject)

K to 9 notes run three to five sentences and say the depth, the device and paper path, the common misconception, and the case type. These rows have one sentence or less: g10-history-policy, g10-visual-data, g10-career-skills, g10-emerging-impacts, g10-human-choices, g10-breach-causes, g11-algorithm-ethics, g11-test-ml-claims, g11-career-plan, g11-emerging-solution, g11-policy-change, g11-infrastructure-impact, g11-fix-security-flaw, and all of grade 12 (g12-evaluate-ai-output, g12-values-in-design, g12-team-workflow, g12-refine-with-users, g12-attribution, g12-diverse-teams, g12-career-goals, g12-human-vs-ai, g12-law-policy). They are the rows with the most class time per row (grade 12 has 12 rows against 70 or more sessions), so they need the most to say.
Fix: each note names (a) the depth in our own words and what is left out, (b) the kind of evidence or case, with "two views and a dated source" for society rows, (c) the device or paper path, and (d) the model carried. Two single-sentence examples of what is missing: g12-team-workflow says nothing about how the weeks are divided or what the "review step" checks; g12-law-policy names no kind of law or case.

### 8. "From memory" marks are on nine rows; thirteen more carry real cases or facts with no mark (minor; firm; LAYER process; REPEAT yes, same kind as the stale-note findings in the social studies read)

Marked: g1-then-and-now, g2-people-solve, g4-history-limits, g6-computing-eras, g7-impact-history, g7-automation-work, g8-relationships, g8-attribution, g9-computing-history. Unmarked rows that tell a history, law or breach case or rely on a dated source: g3-why-build, g3-computing-at-work, g8-history-case, g8-biased-decisions, g9-data-and-people, g10-history-policy, g10-breach-causes, g11-policy-change, g11-infrastructure-impact, g12-law-policy, g12-data-policy-debate, g7-cia-effects, g5-who-included. STANDARD.md says case examples are "from memory, to be checked before use". Fix: add the same words to those notes, and give no date or fact as settled. The writer's marks on dated sources ("each with a dated source in the teacher line") are good practice and should stay.

### 9. Filler rows and the thin career and human-versus-machine threads (choice 5 and 6; minor; judgment call; LAYER progression; REPEAT new)

Judged, row by row:
- Keep as real teaching (each adds a task the owner needs): g9-ai-tour, g9-algorithm-impacts, g9-data-and-people, g10-visual-data, g10-history-policy, g9-computing-history is owner. ML-06 is rightly owned in grade 10 (the verb is justify; grade 9 meets the types).
- Merge: g11-test-ml-claims (~HS-ALG-PS-03 used on a model) is the weakest. Fold it into g11-build-ml-model as the closing session (test a claim against the test-table), delete the row, and set g10-evaluate-algorithms hands_on g11-build-ml-model. Grade 11 drops to 12 rows.
- Career thread (g8 to g12): keep g9-career-interests and g10-career-skills as short portfolio sessions, but g11-career-plan is mislabelled: its note describes a team role plan (that is HS-SOC-CE-45 content) while the row leans ~HS-SOC-CE-45 and sits in a career thread. Rewrite it as a role-and-team plan that feeds g12-diverse-teams, or move the career half into g12-career-goals. The thread overlaps the separate career courses on the course list (CTE section of the bar); that overlap is Cory's, see For Cory.
- Human-versus-machine thread: the ~ lines inside other rows are enough. Do not add rows.

### 10. The blocks-to-text bridge never names the day a student first reads a loop and a choice in text (minor; likely; LAYER progression; REPEAT new)

Grade 6 introduces the text-program only for variables (g6-variable-types) and procedures (g6-procedures); g7-analyze-code is the first row that asks for iteration and selection in a twenty-line text program. The lens flags "text code with no bridge". Fix: one clause in the g6-variable-types or g6-procedures note: the short programs include one loop and one choice shown in blocks beside the text. No new row.

### 11. Words (minor; firm; LAYER progression; REPEAT yes, same kind as the science and ELA reads)

- "dictionary" is a word in g9-structures-program (a key-value store) and in g9-data-dictionary (a field catalogue) in the same grade. Fix: g9-data-dictionary words keep "data dictionary" whole, and the g9-structures-program note says "dictionary here is a different thing".
- "regression" in g7-test-refine (a bug that returns after a fix) collides with regression as a statistics word in grade 8 math. Fix: use "recheck" and keep the idea.
- g4-authn-authz carries "authentication; authorization" as student words in grade 4. The standard names the pair, so keep, but teach them as login and permission first and give the long words last.
- Pass: K and grade 1 lists are spoken and pictured words; the pre-taught order is right everywhere I checked (event, repeat, variable, procedure, pseudocode, packet).

### 12. Process: the starting split in STANDARD.md contradicts its own ordering constraint, and one note's cost line is unclear (minor; firm; LAYER process; REPEAT new)

- STANDARD.md says the MS split is about 16/16/13 with DAT 3/3/3, and also says MS-DAT-DC-21 to 24 come before MS-ALG-ML-07. Both cannot hold: four DAT ids must precede ML-07, and ML-07 is in grade 7, so DAT is 4/2/3 and the split 17/15/13 or the same with ML-07 later. The writer's 17/15/13 is forced, not a taste. Fix: STANDARD.md "Starting split" becomes 17/15/13 with DAT 4/2/3, and ALG 4/4/3, PRO 3/3/3, SOC 3/3/2, SYS 3/3/2 stay; if finding 1 is taken, HS becomes 12/12/12/10 with the "11 or 12" line changed.
- computer-science-edges.md choice 1 says the cost is "one extra DAT id in grade 6 and two in grade 7". The counts show grade 6 has four DAT ids (one more than 3) and grade 7 has two (one fewer). Reword to "one more DAT id in grade 6, one fewer in grade 7".
- The edges note says K to 5 rows run "a little over the 8 to 14 guide". I could not find that guide in the files I read. If it lives elsewhere, it should be cited; see "Settled" for the judgment.

### 13. Device and paper paths: all twelve device-only ids are marked; two rows lack the path the rule asks for (minor; firm; LAYER progression; REPEAT new)

Marked "part met without a device" correctly on all twelve device-only ids in STANDARD.md (g4-table-tool, g5-collect-tools, g5-train-model, g6-sort-filter-tool, g7-reference-docs, g8-relationships, g9-simulate-data, g9-modular, g9-device-limits, g10-clean-text, g10-apis-docs, g11-build-ml-model) and extras (g7-sort-filter-groups, g11-multivariate-viz, g6-ml-hypothesis). Missing: g7-improve-training-data names a paper stand-in (sorting cards as the model) but not the "part met without a device" mark for MS-ALG-ML-07; g11-fix-security-flaw is a "device day on a toy system" with no paper path (a written flaw and fix on a printed toy system works). History and policy rows carry no device claims, which is right.
Specific-things check: "part met without a device" wording is correct on the rows that use it; no row says an id was met without one.

## Settled by the expert

| Choice | Decision | Reason | File |
|---|---|---|---|
| K to 5 at 14 to 16 rows against 30 to 36 sessions | Stand; do not merge | About two sessions a row; most device rows are already unplugged then device, and merging ids would hide a standard | computer-science.csv |
| MS split 17/15/13 and MS-DAT-DC-24 in grade 6 | Stand | Forced by the ordering constraint (DC-21 to 24 before ML-07); only STANDARD.md needs updating | STANDARD.md |
| MS-DAT-DI-25 in grade 8 | Stand | Math owns scatter and association in grade 8 (checked: 8.SP.A.1 in math.csv grade 8) | none |
| HS-PRO-PD-14 in grade 12 | Stand | Applying attribution fits the team program; add `~` leans in g10 and g11 | g10-apis-docs, g11-evaluate-generated-code |
| HS-SOC-HU-44 in grade 12 | Stand | Debating human and machine intelligence suits the last year; HU-43 and the ~ lines carry the thread | none |
| HS-ALG-ML-07 in grade 11 | Stand | Same grade as ML-08 is fine with the written order; moving it to 10 makes ALG 4/2 | none |
| HS-ALG-ML-06 owned in grade 10 | Stand | The verb is justify; grade 9 meets the types | none |
| Society ids sharing rows | Stand | g4-ml-learning, g3-benefits-risks, g3-why-build, g5-who-included, g5-use-or-not, g4-history-limits are single themes; each is two sessions in practice; the strand labels differ from the id concept only in six rows and read right | none |
| Two or three `~` ids as first looks (g9-ai-tour, g9-algorithm-impacts, g9-data-and-people) | Stand as teaching rows | See finding 9 | none |
| g11-test-ml-claims | Merge into g11-build-ml-model | Weakest filler | computer-science.csv |
| "from memory" marks | Add to 13 rows | Finding 8 | computer-science.csv |
| Math leans g1-split-task, k-follow-steps (K.G.A.1), g2-name-and-label, g3-algorithm-combo, g5-variables-use, g6-verify-algorithm, g6-data-quality, g6-precision-metadata | Remove | Finding 2 | computer-science.csv |
| ELA leans, seven | Add | Finding 2 | computer-science.csv |
| Row split g3-read-code into two | Do it | Finding 3 | computer-science.csv |
| Row IM-27 to grade 11 | Proposed; judgment call | Finding 1; the caller may keep 12/12/11/11 | computer-science.csv, STANDARD.md |
| Models | Stand | step-card, picture-graph, block-program, and the rest enter before use; the pseudocode and text-program rows need the in-grade order of finding 5 | none |

## For Cory

- Finding 1: whether grade 12 owns 10 ids (12/12/12/10) so the capstone year is lighter; it changes what grades 11 and 12 teach.
- Finding 9: the career thread (a short row each year, grades 8 to 12) overlaps the separate career exploration and pathways courses on the course list; keep it inside computer science or hand it to those courses. Scope.
- Finding 12: the starting split and the "11 or 12 ids a year" line in STANDARD.md change; it is Cory's draft rule.
- Finding 4: the generated-text thread (MS-ALG-PS-05 on one screen, then supplied saved outputs only, no live tool) stands as the Pending decision describes; no change, but the long gap between grade 8 and grade 11 is filled only by one saved sample in g10-analyze-code, which is a smaller dose than the standard's text suggests.
- Specialty ids are out by design (they wait on Cory); nothing here claims one.

## Pace through the grades

Rows per grade: K 14, 1 15, 2 14, 3 15, 4 16, 5 16, 6 18, 7 19, 8 18, 9 17, 10 15, 11 13, 12 12. By concept (owned ids, counts): MS ALG 4/4/3, DAT 4/2/3, PRO 3/3/3, SOC 3/3/2, SYS 3/3/2; HS ALG 3/3/3/2, DAT 2/2/2/2, PRO 2/2/2/3, SOC 2/2/2/3, SYS 3/3/2/1. The row count falls through high school while the sessions stay level, so rows get longer: that is why the thin notes in finding 7 matter. No grade carries far more than its neighbours; grade 7 at 19 rows is the largest and is explained by its three `~` and one orphan row. Strands that stop: SOC-CE after g12 (end); DAT-IM stops in grades 10 and 11 (finding 1); SYS-HW has no row after grade 9 (fine, both ids are owned there); SYS-IM has none in grades 9 and 10 (see finding 4, infrastructure assume).

## Lens checklist, progression layer (docs/agents/lenses/computer-science.md)

| Line | Result |
|---|---|
| All five concepts in every band; AI inside the concepts, not one late unit | Met. AI runs ALG-ML from grade K to 12 (attribute cards, training set, model, evaluate, choose type, build) with society beside it. |
| A concept owned by no band, or programming taking most rows | Met. Programming is about a third of rows in every band. |
| A construct used before it is taught | Met on ownership. Order inside a grade is only in notes (finding 5). |
| Middle school assumes text code with no bridge | Met in outline (g3 text view, g6 side by side, g7 text); one clause missing (finding 10). |
| Read before write, then modify, then make | Met in the notes that carry it (worked example first, trace before build); not checkable in the thin HS rows (finding 7). |
| Unplugged work in every unit | Met; nearly every row has an unplugged day or paper stand-in. |
| Notional machine and debugging as a method | Met (g1-fix-sequence to g5-systematic-debug, g10-analyze-code). |
| A Specialty id claimed in the Foundational course | Met: none claimed. |
| Society with evidence, two views, dated source | Met in the rows that say it; marks missing on thirteen (finding 8). |
| Claims that coding improves general thinking | Met: none. |
| No product, company, language or editor name | Met: none found anywhere in the 202 rows or the edges note (searched for the common ones; none). |
| A claim that students "meet" an id without a device | Met: none; all 12 device-only ids are marked (finding 13). |
| ELA leans | Missed, now proposed (finding 2). |
| Cross-subject leans real and at or before | Mixed: science met; math seven wrong or thin (finding 2). |

## What is right and should not be touched

- The ownership map: the ordering constraints of STANDARD.md all hold (VD-16 before PS-01 and RD-17; PD-12 before RD-17; RD-17 before RD-18; DC-21 to 24 before ML-07; ML-06 before ML-07 and 08; NT-34 before 35; PS-03 after PS-01 and 02; SE-31, 32, 33 in order; ET-40, 41, 42 in order; IM-27 before IM-28).
- The model chain (step-card, block-program, training-set, named-box, trace-table, flowchart, pseudocode, test-table, text-program, list-diagram) with no model used before its grade.
- The K to 5 row counts, the unplugged-first rule on device rows, and the "part met without a device" marks.
- The names of real cases told by what happened and the rule for no company names; the two-view, dated-source rule on society days.
- The band-crossing handoffs listed in the edges note (the nineteen it lists all resolve to real rows).

## What I could not judge

- Whether the math skill each lean names falls before or after the computer science day inside the year (needs the math scope and sequence).
- The depth of any boundary statement: it is not stored in the repository, so the depth read is from the one-line statements only; every depth call here is likely, not firm.
- The "8 to 14 guide" for rows per grade in the edges note (not found).
- Whether HS-ALG-IM-10 and HS-ALG-ML-07 fit as written against the printed boundary statements.
- Facts in history, law and breach rows (all from memory in the draft; none of them checked here).

## Sources

- The standards files and STANDARD.md, ADOPTION-BAR-SUBJECTS.md section 5, the computer science lens: used for the bar, ids and placement.
- data/progressions/math.csv, science.csv, ela.csv: used to check leans by id only.
- docs/reviews/progression-health-2026-11-19.md, progression-physical-education-2026-11-19.md, progression-math-2026-11-13.md: headings only, to set REPEAT. Nothing outside the repository was read; the pedagogy points (use-modify-create, tracing first) come from the lens, "from memory" otherwise.

## For the source list

None new.
