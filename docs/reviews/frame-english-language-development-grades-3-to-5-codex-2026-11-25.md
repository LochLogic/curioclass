# Second independent frame read: English Language Development, grades 3 to 5

**Date:** November 25, 2026  
**Course:** `english-language-development-grades-3-to-5`  
**Findings:** 5  
**Disposition:** Revise before the scope and sequence.

## Verdict

The frame has a sound structure: three complete years, purposeful content hosts, explicit language instruction, and all progression rows and owned codes placed once. Its biggest risk is substantive coverage: the units do not yet teach every function behind their claimed standards, and two grade 5 content promises lack workable placements. Complete the expectation check and repair those placements while preserving the three 160-day years.

## What was read and checked

- The complete [course frame](S:/CurioClass/docs/courses/english-language-development-grades-3-to-5/frame.md), its `frames.csv` record, its `course-list.csv` selector, and its calendar rows.
- All 38 selected progression rows: grades 3, 4 and 5 in `data/progressions/eld.csv`.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the ELD lens, STANDARD and APPROACH, adoption bar part 10, and `RUBRIC-ELD.md`.
- FOUNDATION, relevant production and baseline rules, APPROACH, the source registry, and applicable recorded decisions.
- The adjacent ELD frames’ seams and relevant models and placements; the named core hosts’ Units tables.
- Earlier ELD prework, progression and K to 2 frame reviews and fixes, for settled decisions and REPEAT classification.
- The official framework’s expectation lists for SI K-3, SI 4-12, and content clusters 2-3 and 4-5. These were opened successfully during this read.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check english-language-development-grades-3-to-5` | One stage-related failure: no `days.csv` with `parts.csv` or `items.csv`; this is a frame-stage course |
| `python -X utf8 scripts/frame.py check english-language-development-grades-3-to-5` | **0 failures** |
| `python -X utf8 scripts/stale.py check` | Three failures, all in other courses: two music frames and the physical education grades 6 to 8 frame |
| `python -X utf8 scripts/progression.py check eld` | **162 rows, 0 failures** |
| Independent placement count | **38 rows placed once; 42 owned codes placed once; no omissions or extras** |
| Independent calendar count | **160 days per year, no gaps or overlaps** |
| Check weeks against core courses | **No core check-week collisions:** grade 3 weeks 19 and 27; grade 4 weeks 15 and 29; grade 5 weeks 18 and 28 |

The plan-stage failure and unrelated stale-note failures do not prevent this verdict. No files were changed.

## Findings, most serious first

### 1. Code coverage conceals incomplete expectation coverage

**Severity:** Serious  
**LAYER:** frame; progression  
**REPEAT:** yes, K to 2 second-model finding 1  
**Confidence:** Firm

**Location:** “Standard” bullet, Units table, and “For the lead” item 7.

The frame infers functions from codes. The official lists show omissions. Representative additions follow, in our own words. [Official framework, Appendix C, PDF pages 304 to 316, printed pages 303 to 315](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf).

| Unit | Functions to add explicitly |
|---|---|
| 1 | Describe relationships; define, compare and classify; summarize others’ information |
| 2 | Select suitable source types and evaluate explanations |
| 3 | Judge credibility through fact and opinion |
| 4 | Frame investigable questions; compare designs against requirements and limits; revise explanations |
| 5, 22 | Evaluate mathematical patterns or structures |
| 6 | Test evidence relevance; distinguish opinion; use an impartial voice |
| 7 | Form conjectures and generalize across cases |
| 8, 18 | Interpret nonliteral meanings; connect character actions with events |
| 9, 11, 12, 13 | Address inference, missing information, changing variables, trade-offs and revision |
| 19 | Compare design solutions; distinguish fact, reasoned judgment and speculation |
| 20 | Evaluate word choice; summarize ideas; maintain an objective voice |
| 21 | Compare different source interpretations |
| 23 | Compare perspectives; use a formal style |
| 25 | Evaluate source credibility and purpose; establish perspective |

**Student cost:** Writers could build complete-looking units that leave claimed functions untaught.

**Exact fix:** Add instruction and assessment look-fors within the existing placements. Complete a function-by-function check of all 42 owned codes; correct equally narrow progression notes. Replace the coverage assertion only after that check passes.

### 2. Unit 24 reaches its hierarchy host after its assessment begins

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, premature host dependencies occurred in the K to 2 second-model finding 4  
**Confidence:** Firm

**Location:** Unit 24, line 271, and the `m5-shape-hierarchy` cross-subject entry.

Unit 24 occupies grade 5 days **123 to 137**. Its final two assessment days therefore fall on **135 and 136**, followed by response on **137**.

The cross-subject entry says the hierarchy work arrives in the unit’s last days and includes a placement assessment item. However, the math frame explicitly places hierarchy diagrams and arguments on **days 138 to 142**. Math unit 10 opening on day 135 does not make its hierarchy content available that day. See [math grade 5 frame, unit 10](S:/CurioClass/docs/courses/math-grade-5/frame.md:140).

**Student cost:** Students could be assessed on classification reasoning before the host teaches it, or ELD could become the first math lesson despite excluding math teaching.

**Exact fix:** Keep unit 24’s teaching and assessment on scaling. Reserve grade 5 days **146 and 147 within unit 25** for the hierarchy application and critique, explicitly revisiting `g5-ma-argue` after math days 138 to 142. Include an unseen hierarchy justification in unit 25’s end-of-unit assessment, with its own language look-fors.

Keep `g5-ma-argue` primarily placed in unit 24, update both units and the cross-subject table, and retain the existing year total and check weeks. Obtain Cory’s decision on this distribution of required instruction across units.

### 3. The gravity task required by the progression remains optional

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete progression-task coverage is the same kind as earlier ELD coverage findings  
**Confidence:** Firm

**Location:** Units 19 and 21; `s5-gravity-down` cross-subject entry; “For the lead” item 3.

`g5-sc-argue` requires arguments about both gravity and plant matter. Unit 19 teaches plant matter and expressly excludes gravity. The later cross-subject entry says gravity **may** be added, while the lead note offers leaving it to science.

That does not fulfill the current progression contract. Science teaching the content does not supply ELD’s planned language instruction and evidence.

The calendar makes a later application possible: science unit 4 runs on school days **75 to 100**, overlapping ELD unit 21’s days **66 to 85**.

**Exact fix:** Make the gravity application required in unit 21. Allocate days **79 to 81** to interpreting and constructing an evidence-based gravity claim from the host’s records, including the meaning of down toward Earth’s center. Replace that unit’s SI Inform review with SI Argue review, keeping two key language uses, Explain and Argue.

Add an unseen gravity argument to the two-day assessment, on a separate day from the history performance. Keep primary placement of `g5-sc-argue` in unit 19, update the recurrence and cross-subject records, and remove the optional wording. This distribution of required instruction also belongs in Cory’s decision.

### 4. Several living notes no longer describe the repository

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, K to 2 second-model finding 6 and earlier ELD prework findings  
**Confidence:** Firm

The stale checker does not detect these statements.

| Location | Evidence and exact fix |
|---|---|
| Frame, “For the lead” item 2 | All six named cognate corrections already appear in the current progression. Replace the outstanding-change claim with: “The six cognate notes already contain the corrected wording; no further cognate edit is requested here.” |
| Frame, item 7 and “Standard” bullet | The framework opened successfully in this read. Replace the deferred browser task with: “The expectation lists were opened during the second independent read. Apply finding 1 and complete the coverage check before claiming full coverage.” |
| Frame, item 9 | The grades 6 to 8 seam no longer contains the cited Pending marker, and the current stale output does not flag it. Remove item 9. |
| Frame, item 5 | Its clash list omits grade 4 week 15 and grade 5 week 18. Replace it with the complete current list below. |
| ELD lens opening | Replace the blanket building restriction with: “Frames are authorized now; the scope and sequence, unit plans, days and newcomer strand remain subject to the C11 condition.” |
| Adoption bar, ELD prework status row | Replace the owed validator and four-call wording with: “Progression check support and the four q-fix-eld-1 decisions are implemented. Frames are authorized; later stages remain subject to the C11 condition.” |

The current additional after-core overlaps are:

- **Grade 3:** week 27, theater.
- **Grade 4:** week 15, music and SEL; week 29, health and library.
- **Grade 5:** week 18, dance, media arts, physical education, theater and visual arts; week 28, health and library.

These overlaps remain for the lead’s coordinated calendar pass. They are not a reason to move this frame’s checks independently.

### 5. The outgoing seam assigns cluster ownership to grade 6 incorrectly

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** “Handed on to English Language Development, grades 6 to 8,” line 215.

The sentence says, “Grade 6 owns the cluster 6-8 ids.” STANDARD section 2 and the progression assign ownership to **grade 8**; grade 6 carries those codes.

**Exact fix:** Replace the sentence with:

> Grade 6 begins carrying the cluster 6-8 ids, owned in grade 8; the SI 4-12 ids, owned here in grade 4, continue as carried work.

The seam’s skill links can remain.

## Lens checklist

| Frame-layer lens line | Result |
|---|---|
| Content behind units, rather than isolated vocabulary or grammar drills | **Met** |
| Multiple proficiency levels preserving content and thinking demand | **Met in the stated design**; actual tasks and look-fors remain to be written |
| Valid standard, cluster and key-language-use codes | **Met**; substantive coverage requires finding 1 |
| Entry and exit points stated; ELD distinct from ELA | **Met** |
| ELA pairings and core hosts named | **Met for identification**; availability and required applications need findings 2 and 3 |

Unit- and day-layer requirements are appropriately specified as future obligations: structured talk, learner-specific notes, home-language resources, direct teaching of forms, withdrawal of supports, and guidance distinguishing language needs from learning needs. Their implementation cannot yet be judged.

## What is right and should remain

- Three complete grade years with continuous unit numbering and separate yearly assessments and checks.
- **154 unit days plus six course-check and response days per year**, at 30 minutes daily.
- Correct primary placement of all 38 rows and ownership placement of all 42 codes.
- SI planned in every unit and an explicit within-year recurrence map.
- Language forms named at text, sentence and word levels, with modeled construction before independent use.
- Grade-level content, paper access, home-language support and teacher-held evidence.
- Clear boundaries between ELD, ELA, host content instruction and school placement decisions.
- Invented-story options and protections against compelled family disclosures.
- Honest identification of the units that receive end-of-unit assessment without later course-check sampling.
- No separate ELD source map is required for the stated design: this course places no base-course lessons.

## Settled by the expert

Recommendations for the caller to apply. This read changed nothing.

| Choice | Reason | Files affected |
|---|---|---|
| Complete functions within existing primary standard placements | Corrects coverage without changing ownership | Frame; corresponding progression notes |
| Preserve the three 160-day totals and existing check weeks | Arithmetic and separation from core checks are correct | Frame; calendar |
| Correct grade 6 to carried status | Matches the established ownership rule | Frame seam |
| Replace or remove the identified stale notes | Prevents duplicate work and contradictory instructions | Frame; ELD lens; adoption bar |
| Retain paper, talk and teacher judgment as the delivery model | Fits the subject approach and access requirements | Frame |

## For Cory

- **Required applications across units:** Approve the concrete distributions in findings 2 and 3: hierarchy work in unit 25 and gravity work in unit 21, retaining their existing primary row placements. Moving required standard instruction across units is reserved to you; neither proposal adds days.
- **Newcomer delivery:** The earlier staffing and time question remains open. The strand stays beside the 160-day frame. Its delivery still needs a decision about who teaches it and how newcomers receive regular-unit instruction they miss.

## What could not be judged

The actual host passages, assessment items, proficiency-level look-fors, accommodations, marking time and classroom operation are not yet available for this frame. Two-day assessment descriptions establish an intention, not demonstrated feasibility.

This read did not verify the C11 probe and guard evidence or certify host-text rights. The existing condition on later ELD stages remains appropriate.

## Sources and memory

- [Official English language development framework](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf): expectation lists behind the selected codes, checked directly rather than inferred from their names.
- [Teaching Academic Content and Literacy to English Learners in Elementary and Middle School](https://ies.ed.gov/ncee/wwc/PracticeGuide/19): supports retaining integrated content, oral language and written language instruction; it does not validate this course’s specific schedule.

**For the source list:** Record the expectation-list reading above under the existing framework entry. Its listed PDF address worked during this review.

No substantive finding rests on memory. Prior memory supplied review-format guidance only; findings rest on current repository evidence and sources opened during this read.

