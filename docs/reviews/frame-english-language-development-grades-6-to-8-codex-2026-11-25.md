# Second independent frame read: English Language Development, grades 6 to 8

**Date:** November 25, 2026  
**Course:** `english-language-development-grades-6-to-8`  
**Findings:** 5  
**Disposition:** Revise before the scope and sequence.

## Verdict

The frame has a sound structure: three complete years, purposeful language instruction, and correct placement of every selected progression row and owned code. Its biggest risks are incomplete coverage behind those codes and host applications scheduled before the host teaches the required content. Complete the expectation coverage and repair those dependencies while preserving the three 160-day years.

## What was read and checked

- The complete course frame, its `frames.csv` record, `course-list.csv` selector and calendar rows.
- All 39 selected progression rows in `data/progressions/eld.csv`, plus the grade 5 and grade 9 handoffs.
- The frame-read brief, after-core frame-write provisions, EXPERT instructions, ELD lens, STANDARD, APPROACH, adoption bar part 10 and RUBRIC-ELD.
- Relevant foundation, approach, production, baseline, calendar and recorded decision rules.
- Adjacent ELD frames’ seams and relevant placements; named core-host Units tables and targeted host calendar and day rows.
- Earlier ELD progression, prework and frame reviews, for settled decisions and REPEAT classification.
- The official framework’s grades 6 to 8 expectation lists, opened successfully during this read.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check english-language-development-grades-6-to-8` | One stage-related failure: the course has no lesson-plan `days.csv` with `parts.csv` or `items.csv` |
| `python -X utf8 scripts/frame.py check english-language-development-grades-6-to-8` | **0 failures** |
| `python -X utf8 scripts/stale.py check` | Nine failures, all in other courses |
| `python -X utf8 scripts/progression.py check eld` | **162 rows, 0 failures** |
| Independent placement count | **39 rows placed once; 18 owned codes placed once; no missing or foreign skills** |
| Independent calendar count | **154 unit days plus six check/respond days per year** |
| ELD mid-year checks against core checks | **No school-day collisions** |
| Additional after-core overlap | Grade 6 ELD and physical education share **school day 82** |

The plan-stage failure and unrelated stale-note failures do not prevent this verdict. Commands used `-B` to suppress bytecode creation. No files were changed.

## Findings, most serious first

### 1. The owned codes cover more language functions than the units currently teach

**Severity:** Serious  
**LAYER:** frame; progression  
**REPEAT:** yes, K to 2 and grades 3 to 5 second-model coverage findings  
**Confidence:** Firm

**Location:** Frame lines 47 to 49, grade 8 Units 18 to 26, and “For the lead” item 2.

The frame says every part was checked against the framework’s lists. Item 2 instead explains that the descriptions came from the short local code glosses. Those glosses do not establish full expectation coverage.

The official lists identify these additions, paraphrased here. [Official grades 6 to 8 framework, PDF pages 32 to 48](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020-Edition-Grades-6-8.pdf).

| Unit | Required work to add explicitly |
|---|---|
| 18, LA Inform | Define the topic; analyze descriptive evidence; maintain an impartial stance. |
| 19, MA Argue | Compare strategies, form conjectures and generalize across cases. |
| 20, LA Argue | Separate textual summary from personal opinion; judge evidence sufficiency and reasoning; conclude. |
| 21, SC Argue | Compare two same-topic arguments and their evidence choices; maintain an objective stance. |
| 22, MA Explain | Compare representations and solution approaches; evaluate the selected model’s rationale. |
| 23, LA Narrate | Trace theme, evaluate word choice, and develop a narrative’s complication and resolution. |
| 24, SS Explain | Compare experts’ explanations and limitations; explain interacting causes and effects. |
| 25, SS Argue | Evaluate source purpose and credibility; contextualize a position using multiple sources. |
| 26, SC Explain | Frame an investigable question; evaluate reasoning; explain variable relationships; revise and retest. |

**Why it matters:** Writers can complete the listed scenes, paragraphs and cause chains while leaving claimed functions untaught.

**Exact fix:** Add the table’s work to the existing units’ learning descriptions and assessment look-fors, with the same thinking demand at all three entry points. Complete a function-by-function comparison of all 18 owned codes and amend corresponding progression notes. Keep investigations in science: language tasks can use supplied questions, records and revised models.

Replace the full-coverage assertion with an accurate account of what was checked and what remains until these additions are complete. Ownership need not move.

### 2. Three applications use the host unit’s opening date as though its required content were already available

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, premature host dependencies in the earlier ELD frame reads  
**Confidence:** Firm for the mismatches; proposed allocations are judgment calls

**Location:** Units 16, 21 and 22, and their cross-subject entries.

| ELD placement | Current host evidence | Problem |
|---|---|---|
| Unit 16, grade 7 days **132 to 144** | Math introduces distribution comparison on day **148**, population/sample distinctions on **149**, and comparison from two populations’ random samples on **154** | The sampling application and its assessment occur too early. Math unit 8 opening on day 139 does not supply that content. |
| Unit 21, grade 8 days **59 to 81** | Science begins its mass-and-orbit gravity model on day **99** and argues gravity’s dependence on mass on **100** | Gravity cannot be the unit’s second host argument. Science unit 4 opening on day 77 does not make this argument available. |
| Unit 22, grade 8 days **82 to 97** | Math’s named `m8-function-model` application occurs on day **101** | The function-model application comes after ELD’s assessment and response. Earlier input-output work does not settle this specific lean. |

Evidence: [math grade 7 day rows](S:/CurioClass/data/plans/math-grade-7/days.csv:149), [science grade 8 gravity rows](S:/CurioClass/data/plans/science-grade-8/days.csv:100), and [math grade 8 modeling row](S:/CurioClass/data/plans/math-grade-8/days.csv:102).

**Why it matters:** ELD would become first instruction in the host content, assess students prematurely, or silently omit required progression applications.

**Exact fix proposed for Cory:**

- **Grade 7 sampling:** Keep Unit 16’s primary placement and triangle argument. Require the sample-comparison language application on **days 155 and 156 in Unit 17**, after math day 154, and sample it in the year-end check. Place Unit 17’s history assessment on **151 and 152**, its response on **153**, and use **157** for response to the later application’s exit evidence. Replace Unit 17’s SI Narrate review with SI Argue review, keeping two key language uses.
- **Grade 8 gravity:** Keep Unit 21’s teaching and assessment on energy-transfer arguments. Require the gravity-language return on **days 102 to 104 in Unit 23**, using science’s completed mass-and-orbit records. Collect separate language evidence on the final application day. Label this SC Argue review, preserving the primary placement in Unit 21.
- **Grade 8 function modeling:** Keep Unit 22 on already-taught equation methods and linear relationships. Require its function-model return on **days 118 and 119 in Unit 24**, after math unit 6 finishes, and include that application in the year-end MA Explain sample.

Update the affected units, recurrence map, cross-subject table and check descriptions together. These proposals preserve the yearly totals and existing course-check dates, but distribute required instruction across units, so they require Cory’s decision.

### 3. The progression’s two-step equation explanation is reduced to an optional aside

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, required progression applications left optional in the grades 3 to 5 read  
**Confidence:** Firm

**Location:** Unit 11, Unit 16, the `m7-two-step-equations` cross-subject entry, and “For the lead” item 5.

[`g7-ma-explain`](S:/CurioClass/data/progressions/eld.csv:93) requires explaining proportional and two-step equations, including what their parts mean. Unit 11 excludes two-step equations because its host arrives later. Unit 16 mentions them only within SI procedure review, “where it fits.”

That leaves no required mathematical explanation or evidence for this part of the row. Explaining a sampling procedure does not itself fulfill it.

**Exact fix:** Make Unit 16’s later MA Explain return mandatory. Allocate **day 133** to unpacking the language of a previously taught two-step solution and **day 134** to explaining both operations, their reasons and the symbols’ meanings in talk and writing. Use an unseen worked equation for the exit evidence.

Keep `g7-ma-explain` primarily placed in Unit 11. Update its seam, recurrence and cross-subject descriptions, and replace “where it fits” and “may revisit” with the required return. This distribution also belongs in Cory’s decision.

### 4. Three home-language notes confuse translations with cognates

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, inaccurate cognate notes in earlier ELD reads  
**Confidence:** Firm

**Location:** Unit 3, Unit 16 and Unit 22 home-language notes.

The notes identify *inundación/flood* as cognates and describe *muestra/sample* and *pendiente/slope* as hidden cognates. The dictionary histories do not support these pairings.

- *Inundación* derives from Latin *inundatio*; *flood* has an Old English history. [RAE-ASALE](https://dle.rae.es/inundaci%C3%B3n), [Merriam-Webster](https://www.merriam-webster.com/dictionary/flood).
- *Muestra* derives from *mostrar*, from Latin *monstrare*; *sample* derives through French from Latin *exemplum*. [RAE-ASALE: muestra](https://dle.rae.es/muestra), [mostrar](https://dle.rae.es/mostrar), [Merriam-Webster: sample](https://www.merriam-webster.com/dictionary/sample).
- *Pendiente* derives from *pender*; *slope* has a different recorded history. [RAE-ASALE](https://dle.rae.es/pendiente), [Merriam-Webster](https://www.merriam-webster.com/dictionary/slope).

**Why it matters:** These notes would teach an incorrect word-learning strategy.

**Exact fix:** Use these sentences:

| Unit | Replacement |
|---|---|
| 3 | “*Inundación* means *flood*. *Especialización* and *specialization* are cognates.” |
| 16 | “*Muestra* means *sample*. *Condición* and *condition*, and *triángulo* and *triangle*, are cognates.” |
| 22 | “*Pendiente* means *slope*. *Función* and *function* are cognates.” |

Retain the useful translations and remove the unsupported shared-root claims.

### 5. Living notes contradict completed work and current authorization

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, earlier ELD prework and grades 3 to 5 stale-note findings  
**Confidence:** Firm

The stale checker does not detect these statements.

| Location | Problem | Exact fix |
|---|---|---|
| Frame, “For the lead” item 2 | Defers the expectation-list check to a future download | Record that the lists opened during this independent read, and point to finding 1’s remaining coverage work. No local download is required for that reading. |
| Frame, item 3 | Describes an applied row change while still offering a choice based on the old row; “below” points to no handoff | Replace with: “`g8-ma-argue` now uses congruence and the transformation argument for the triangle angle sum. Keep Unit 19 in its current position.” Remove the obsolete swap alternative. |
| Frame, item 5 | Lists the Pythagorean theorem as an unused lean although the current progression replaced it; calls two-step work optional | Remove the obsolete lean and record the mandatory later applications established by findings 2 and 3. Retain accurate explanations of directly taught language on earlier host texts. |
| ELD lens opening | Says building waits for C11 without the frame exception | Replace with: “Frames are authorized now. The scope and sequence, unit plans, days and newcomer strand remain subject to the C11 condition.” |
| Adoption bar, ELD prework status row | Still owes progression-check support and four decisions already implemented | Replace that outstanding-work wording with: “Progression-check support and the four q-fix-eld-1 decisions are implemented. Frames are authorized; later stages remain subject to the C11 condition.” |

**Why it matters:** A later worker could repeat completed work, undo the corrected math pairing, or misread which stage is authorized.

Keep dated review reports unchanged. Correct living documents in place; any new decision belongs in the existing decision log.

## Lens checklist

| Frame-layer lens line | Result |
|---|---|
| Content behind units, rather than isolated vocabulary or grammar drills | **Met** |
| Multiple proficiency levels preserving content and thinking demand | **Met in the stated design** |
| Valid standard, cluster and key-language-use codes | **Met**; full coverage needs finding 1 |
| Entry and exit points stated; protected ELD distinct from ELA | **Met** |
| ELA pairings and other core hosts named | **Met for identification**; timing and required applications need findings 2 and 3 |

Structured talk, direct teaching of forms, scaffold withdrawal, learner-specific notes and student self-checks are specified appropriately for later layers. Actual lesson implementation remains unjudged.

## What is right and should remain

- Three whole grade years, continuous unit numbering and separate yearly checks.
- Correct placement of all 39 progression rows and 18 owned codes.
- SI goals in every unit and explicit within-year recurrence.
- Named language forms at text, sentence and word levels.
- Model analysis, joint construction, talk and independent writing.
- Paper access, teacher-held evidence and protections against compelled family disclosures.
- Honest identification of final units assessed through their own end-of-unit records.

The content, oral-language and writing emphasis is consistent with the [federal practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/19). That evidence does not validate this course’s particular schedule.

No separate ELD source map is needed for the stated design because it places no base-course lessons.

## Settled by the expert

Recommendations for the caller to apply; this read changed nothing.

| Choice | Reason | Files affected |
|---|---|---|
| Complete functions within existing owned-code placements | Repairs coverage without changing ownership | Frame; progression notes |
| Preserve three 160-day years and existing course-check dates | Arithmetic and separation from core checks are correct | Frame; calendar |
| Correct the three translation/cognate notes | Preserves useful Spanish support accurately | Frame |
| Retain congruence and angle-sum work in Unit 19 | Matches the current progression and available host | Frame |
| Rewrite the identified living notes | Prevents contradictory instructions and duplicate work | Frame; lens; adoption bar |

## For Cory

- **Required instruction across units:** Decide on the concrete later applications in findings 2 and 3. They retain primary row placements and yearly totals.
- **Newcomer delivery:** The existing question remains: who teaches the separate 20-day strand, and how newcomers receive regular-unit instruction they miss.
- **People and scheduling:** Include the grade 6 day **82** physical education overlap in the lead’s coordinated after-core calendar pass.

## What could not be judged

Actual passages, assessment items, proficiency-level look-fors, accommodations and marking time are not yet available. The two-day assessment descriptions establish an intention, not demonstrated classroom feasibility.

This read did not verify C11 probe and guard evidence or certify host-text rights.

The preceding frame’s incorrect statement that grade 6 owns cluster 6 to 8 remains an already reported seam defect. The target frame correctly assigns ownership to grade 8; that earlier finding is not counted again here.

## Sources and memory

Outside sources are linked beside their uses above. The official expectation lists and dictionary entries opened successfully.

**For the source list:** Add the working [grades 6 to 8 framework booklet](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020-Edition-Grades-6-8.pdf) to the existing framework entry and record the expectation-list reading.

No substantive finding rests on memory. Prior memory supplied review-method guidance only; findings rest on current repository evidence and sources opened during this read.

