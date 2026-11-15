# Independent sequence read: English Language Arts Grade 12

**Date:** 2026-11-15  
**Report path:** `docs/reviews/sequence-english-language-arts-grade-12-2026-11-15.md`  
**Delivery:** Complete report supplied inline. No file was written.

## Verdict

Revise before unit planning: the overall sequence is coherent, but several assessment and timing claims need correction. The largest risk is treating compressed check descriptions as sufficient evidence of full standards coverage within the available time. Narrow the final reading check, make the remaining assessment demands explicit, and substantiate the reading allocations before treating the daily schedule as settled.

**Finding count: 6.**

## What I read and checked

- The complete Grade 12 scope and sequence, all 160 rows of `days.csv`, and the course frame.
- All 30 Grade 12 ELA progression rows, their declared prerequisites, and the Grade 11 day placements needed to establish last use.
- The applicable standards, including lettered parts, in `data/standards/ccss-ela-standards-full.txt`.
- `EXPERT.md`, the ELA lens, `RUBRIC-ELA.md`, the foundation, shared and ELA approaches, glossary, relevant baseline rules, roadmap requirements, and source-register entries.
- `CALENDAR.md` and the relevant Grade 12 calendar rows, including Government, Economics, and US History II.
- All 35 Grade 12 records in `data/plans/ela-texts.csv`, the base-text register, and relevant earlier Grade 12 frame and Grade 9 to 11 sequence findings and fix records.
- Outside standards, research guidance, review criteria, and two curriculum comparisons linked below.

I respected the blind-file exclusions. Earlier reports were consulted after the cold examination to distinguish recurring problems from resolved findings.

**Memory:** No substantive curriculum finding rests on memory. Saved guidance informed only scope discipline and report structure.

### Gates

The global `plan.py check` reported zero Grade 12 sequence failures, then stopped elsewhere because the Python environment lacks `markdown`.

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check english-language-arts-grade-12` | 0 failures |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule breaks reported |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-12` | 0 failures; 160 days |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

These results establish structural validity, not instructional sufficiency.

## Findings, most serious first

### 1. Day 121 promises too many complete performances for its response window

**Severity:** Serious planning risk  
**LAYER:** sequence  
**REPEAT:** yes, overloaded cumulative checks were also identified in the Grade 11 sequence read  
**Confidence:** likely

**Location:** Day 121; “Course-level checks and calendar”; frame “Where each thread ends.”

Day 121 lists eight skill rows and eleven parent standards. Its 38-minute response window must accommodate evidence and uncertainty in both genres; literary themes and nonfiction central ideas, including development, interaction, and summaries; several dimensions of literary language; interpretation comparisons; refined technical terms; and comprehensive speech evaluation.

The 900-word text limit bounds reading volume, but does not establish that these distinct analyses fit. The scope explicitly defers the timing trial until actual texts and prompts exist. That leaves the final checkpoint’s central design unresolved.

**Why it matters:** Writers could satisfy the code list by producing rushed fragments instead of defensible evidence of independent proficiency. Reasonable pacing is an explicit review consideration. [ELA evidence guide, indicator 2f](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Evidence-Guide.pdf).

**Exact fix:** Retain day 121’s high-band reading, two-version comparison, and refined-key-term task. Remove its additional full-coverage claims for evidence/uncertainty, interacting themes and central ideas, literary word analysis, and speech evaluation; identify their existing unit-end and earlier-check records in the coverage table instead. Keep the speech available for day 122’s source-based reflection without claiming another complete speech evaluation. Trial the reduced assessment before fixing its prompts and response lengths.

This changes sampling within the existing check, without moving an owned standard or resizing a unit.

### 2. Two cumulative-check descriptions omit parts of standards they list

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, incomplete assessment specifications recur in the Grade 10 and Grade 11 sequence reads  
**Confidence:** firm on the omissions

**Location:** Days 51 and 83.

| Day | Listed standard | What the description does not secure |
|---|---|---|
| 51 | `RL.11-12.4` | “Word/tone” does not explicitly require figurative and connotative meanings, multiple meanings, or the effect of particularly fresh, engaging, or beautiful language. |
| 83 | `L.11-12.5a` | “Figures/near-synonyms” does not explicitly require explaining the figure’s role in the text. |

Both distinctions are explicit in the standards. The stronger descriptions on days 35 and 49 show that the plan already recognizes them. [Literature standards](https://www.thecorestandards.org/ELA-Literacy/RL/11-12/), [language standards](https://www.thecorestandards.org/ELA-Literacy/L/11-12/).

**Why it matters:** A writer can follow the named matrix and omit these performances while still recording complete coverage. The introductory promise that later prompts will cover remaining parts does not identify the missing evidence.

**Exact fix:**

- Day 51: specify an integrated response explaining contextual figurative/connotative meaning, a consequential multiple meaning or fresh expression, and its effect on meaning and tone. Select a passage that supports those demands.
- Day 83: require the existing figure response to explain what that figure contributes to the passage’s meaning or argument, alongside the near-synonym comparison.
- Carry these requirements into the check summary. If the selected texts or timing cannot support them, remove those coverage claims and point to their existing complete unit assessments.

### 3. Reading allocations remain plausible rather than demonstrated

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, reading-load documentation was raised in the Grade 12 frame reviews and Grade 9 to 11 sequence reads  
**Confidence:** firm on missing documentation; judgment call on eventual classroom fit

**Location:** Reading rationale; units 2, 4, 5, and 7; shorter-path folds; `data/plans/ela-texts.csv`.

The scope defers exact pages and access time to unit planning. Of 35 text records, 27 contain “not on file” in their measure field, and excerpt boundaries frequently remain broad. All 35 rights-check fields are blank, although the scope correctly acknowledges that limitation.

The tightest allocation is unit 5: **eight teaching days**, two assessment days, and one respond day for Du Bois chapters 1 and 3, approximately 15,000 Woolf words, two seminars, comparative writing, and three demanding reading rows. Distributed home reading may make this workable, but its actual assignments are not mapped. Comparable uncertainties remain around whole-play reading and legal extracts.

**Why it matters:** Day totals cannot establish whether reading, rereading, discussion, and writing fit together. Complexity also requires qualitative and reader/task analysis alongside appropriate quantitative evidence. [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf).

**Exact fix:** Add a provisional load table to the sequence showing exact selections, words or media minutes, first-reading assignments, class/home allocation, in-school access time, and concurrent writing demands. Prioritize unit 5 and the fold destinations. Keep the present unit budgets provisional until that table supports them.

This does not reopen the earlier rejected requirement to complete every text record before fixing the frame. It addresses the current sequence’s responsibility to justify its allocations.

### 4. The shorter-period route retains explicit 50-minute specifications

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same problem appears in the Grade 9 to 11 sequence reads  
**Confidence:** firm

**Location:** “Shorter path”; days 49, 121, and 122.

The proposed 35 to 40 minute route gives sensible priorities but does not reconcile several fixed allocations:

- Day 49 reserves ten minutes for preparation and up to eight five-minute group slots: **50 minutes**.
- Day 121 reserves 12 minutes for reading/listening and 38 for responses: **50 minutes**.
- Day 122 reserves 35 minutes for composition and 15 for reflection/editing: **50 minutes**.

The presentation-panel adjustment is explicit and useful. The other assessment windows need equivalent treatment.

**Why it matters:** A teacher following the shorter route must either exceed the period or silently omit assessed work.

**Exact fix:** Define a provisional **40-minute assessment path**:

- Spread day 49’s oral collection across days 48 and 49, with each learner heard once and the corresponding evidence named on both rows.
- After finding 1’s reduction, budget day 121 at 12 minutes reading/listening and 28 minutes responding.
- Budget day 122 at 28 minutes composition and 12 minutes source-linked reflection/editing, with a correspondingly bounded product.
- Give a separate allocation for 35-minute periods rather than presenting the range as one interchangeable route.

Trial these budgets with the actual materials. Retain every assessed part across the existing windows.

### 5. Interpretations retrieval follows its first application

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, late prerequisite retrieval is identified in the Grade 9 and Grade 10 sequence reads  
**Confidence:** firm

**Location:** Prerequisite table; days 24, 25, and 31.

The first explicit retrieval of `e11-lit-interpretations` occurs on day 31. Students already compare three Hamlet versions on day 24 and refine that judgment on day 25.

The Grade 11 placement is verified, so retrieval is appropriate. Its timing is the problem.

**Why it matters:** The first application does not open by recovering the earlier distinction between describing performance differences and evaluating how a version interprets its source.

**Exact fix:** Add a brief retrieval at the start of day 24 using a supplied familiar script and interpretation contrast, then proceed to Hamlet. Retain day 31’s supplied *Trifles* comparison as the American-dramatist application and evidence record. Update the prerequisite table to identify day 24 as first retrieval.

No readiness check or additional day is needed.

### 6. Current upstream notes still contradict the sequence

**Severity:** Low, except wording that could restore incorrect prerequisite checks  
**LAYER:** process  
**REPEAT:** yes, stale handoff instructions recur in earlier frame and sequence reads  
**Confidence:** firm

**Location:** Frame opening, prerequisite wording, and reading/writing summary; progression rows `e12-info-ideas-events`, `e12-info-founding-documents`, and `e12-research`.

The stale-note gate passes, but these substantive inconsistencies remain:

| Current wording | Required correction |
|---|---|
| The frame says the scope and sequence sets days “later.” | Link the existing sequence and identify it as the current day map. |
| The frame repeatedly directs opening readiness tasks on Grade 11 skills. | Replace these with retrieval inside the first relevant teaching day, consistent with the governing rule. |
| `e12-info-ideas-events` specifies Du Bois chapters 1 to 3. | Synchronize with the settled chapters 1 and 3 selection and revise the historical examples accordingly. |
| `e12-info-founding-documents` says Grade 10 reads Seneca Falls. | Correct the cross-reference to the current Grade 10 document set, which includes Harper. |
| `e12-research` says about eight weeks. | State 36 days, about seven weeks. |
| The frame reports writing as approximately 40/40/20 without a count. | Report the actual process-product distribution and its counting rule. |

The last point needs particular care. As presently taught, the narrative, Hamlet argument, explanation, mock opinion, and claim/counterclaim research paper produce **three argument products, one informative product, and one narrative product**, or **60/20/20 by product count**. The research paper also carries informative work, so its principal purpose must be declared rather than used ambiguously to support the reported ratio. The review guide treats distribution as descriptive reporting. [ELA evidence guide, indicator 2o](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Evidence-Guide.pdf).

**Why it matters:** Later writers can restore superseded instructions, expand reading inadvertently, or repeat an unsupported balance claim.

**Exact fix:** Apply the corrections above, preserve dated review history, and replace the frame’s estimated reading balance with separately counted required-text and reading-day totals. No assignment change is required merely to produce a preferred percentage.

## Other required checks

### Order, standards, assessments, and days by load

The main instructional order is sound: models precede drafting, evidence precedes sustained argument, the novel is completed before its final comparisons, and legal reasoning precedes the mock opinion. The research sequence moves appropriately from questions and searching to source evaluation, synthesis, drafting, revision, and presentation.

| Unit | Total days | Teaching days, excluding Check and Respond | Owned rows | Load judgment |
|---|---:|---:|---:|---|
| 1 | 15 | 11 | 7 | Reasonable for short models, one process piece, and annual routines. |
| 2 | 23 | 19 | 7 | Substantial whole-play and argument load; exact reading distribution needed. |
| 3 | 12 | 9 | 3 | Plausible with the stated reading arrangements. |
| 4 | 18 | 15 | 2 | Whole novel and period comparisons justify the allocation. |
| 5 | 11 | 8 | 3 | Tightest reading allocation; substantiate it. |
| 6 | 16 | 12 | 3 | Plausible for rhetoric, source integration, and explanation. |
| 7 | 18 | 14 | 3 | Dense legal reading and process writing; bound the extracts. |
| 8 | 36 | 24 | 2 | Sustained research and two presentation contexts justify the long allocation. |

No allocation is demonstrably excessive solely from row counts. Underallocation remains an unresolved risk, especially in unit 5, rather than a proved need to transfer days.

All **30 owned rows and 41 parent standards** are placed. The lettered writing, discussion, and language components have identifiable teaching and assessment locations, subject to the cumulative-check omissions in finding 2.

Every unit has an end-of-unit assessment and one final response allocation. Unit 8, the only unit over 25 days, has its midpoint assessment on day 142 and response on day 143. Reused conference, publication, source, and presentation records generally avoid duplicate collection.

### Readiness and retrieval

All **30 declared ELA prerequisites** belong to Grade 11, and their listed latest day placements match the current Grade 11 day map. No declared older ELA row requires a readiness check.

The statistics prerequisite, `S-IC.B.6`, is assigned to Grade 11 in the mathematics progression; day 93’s retrieval is appropriate. Supplied numerical comparisons avoid adding an undeclared older computation prerequisite.

No older-row readiness check is misplaced on a unit’s first day or weeks ahead. Finding 5 concerns delayed retrieval, not misclassification.

### Course checks and calendar

Checks fall in weeks **11, 17, and 25**, matching the live Grade 12 calendar. The week 17 overlap with history is permitted under the high-school calendar rule.

Each check explicitly transfers the immediately preceding unit’s skills to earlier units’ subject matter. The same-year leans arrive before use or have named bridges, including the deliberate supply-and-demand alternative to Economics’ later policy instruction.

The senior-project milestones align with the calendar at question selection, provisional and complete source lists, draft completion, rehearsal, talks, and final publication.

### Candidate cells and shorter year

All candidate cells are settled. Ophelia’s songs remain within the required play; the second Shakespeare selection occupies an existing assessment day. Other additions are dropped with reasons and zero additional days.

All ten named fold-in days are unassessed Fluency days. Their destinations preserve required texts and named skills on paper. Actual destination loads still need finding 3’s verification. The distinction between ten lost meetings and a school year that actually ends ten days earlier is correctly maintained.

**Source map:** Not applicable. The base-text register identifies ELA 6 to 12 as independently written.

## Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Text demand climbs, or its ordering has a stated reason | **Met in rationale; verification incomplete.** Independence and integration increase, but selection-specific evidence remains unfinished. |
| Research and full-process writing recur | **Met.** Short inquiries recur before and during the sustained project; five process pieces are scheduled. |
| Formal discussion occurs often | **Met as a planned routine.** Every unit names two seminars, including student leadership, alongside other discussion settings. |
| K to 2 phonics and decodables align | **Not applicable.** |

This is a sequence judgment, not a completed rubric score.

## What should be preserved

Keep the unit order, three complete shared long works, distinct writing purposes, frequent source-based writing, and movement toward independent reading. Preserve the privacy alternatives, original-text access, explicit unfinished digital components, earlier-content transfer, shared-project milestones, and reuse of individual evidence records.

The model, practice, revision, and reflection structure is consistent with the [secondary-writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22).

## Settled by the expert

| Choice | Reason | Files affected when applied |
|---|---|---|
| Narrow day 121’s full-coverage claims | Existing complete records allow a more credible final sample | Day map, check summary, frame endpoint table |
| Make day 51’s language analysis and day 83’s figure-role explanation explicit | Secure the listed standard components | Day map, check summary |
| Retain current unit budgets provisionally | No demonstrated basis yet for transferring days | Scope and sequence |
| Define a 40-minute assessment path and a separate 35-minute allocation | Make the shorter-period promise reviewable | Shorter path, affected day notes |
| Retrieve interpretations on day 24 | Recover the prerequisite before first application | Day map, prerequisite table |
| Keep Du Bois chapters 1 and 3 | This is the settled frame and sequence selection | Progression note |
| Report writing shares from declared product purposes | Correct the claim without changing assignments | Frame, scope and sequence |
| Synchronize current-status and prerequisite wording | Prevent restoration of superseded instructions | Frame, progression notes |

## For Cory

- **People and audience:** Resolve the school staffing, observers, spaces, adult panels, and younger audiences required by unit 8. The capacity formulas identify the requirement but do not supply those people.
- **Audience:** Resolve the delivery route for a parent teaching one child, since the current audience and device arrangements are written around a school.
- **Scope, only if triggered:** Decide any unit resizing, required-text reduction, or genuinely shorter senior-year calendar that the completed load checks show necessary.

## Sources and limits

- [Common Core literature standards](https://www.thecorestandards.org/ELA-Literacy/RL/11-12/), [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/11-12/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/11-12/), [speaking/listening](https://www.thecorestandards.org/ELA-Literacy/SL/11-12/), and [language](https://www.thecorestandards.org/ELA-Literacy/L/11-12/): checked the applicable performances and lettered parts.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): checked the three-part complexity model.
- [ELA review criteria](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Review-Criteria.pdf) and [evidence guide](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Evidence-Guide.pdf): consulted text analysis, pacing, assessment, and writing-distribution provisions.
- [Federal secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): consulted explicit strategy instruction and integrated reading/writing recommendations.
- [Grade 12 pacing comparison](https://www.fishtanklearning.org/curriculum/ela/12th-grade/pacing-guide/): its 60-minute lessons and additional reading allowance prevent direct day-count equivalence.
- [Grade 12 course-at-a-glance comparison](https://odell-uploads-staging.s3.amazonaws.com/release/materials/g12_courseataglance.pdf): compared reflective opening work, Hamlet analysis, recurring diagnostics, and culminating inquiry. This supports the broad architecture, not the proposed minutes.

The rubric’s hashed criteria link failed to open; the publisher’s direct criteria and evidence-guide links above worked. Actual classroom timing, finished prompts, scoring reliability, complete rights clearance, and completed sensitivity reads remain unverified.

**For the source list:** Add the working direct review-tool links and the two Grade 12 curriculum comparison links above.

**Verdict:** Revise before unit planning.  
**Finding count:** 6.  
**Report path:** `docs/reviews/sequence-english-language-arts-grade-12-2026-11-15.md`, delivered inline, not written.

