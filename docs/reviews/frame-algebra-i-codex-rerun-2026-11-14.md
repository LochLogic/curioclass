# Algebra I course frame: independent review

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-algebra-i-2026-11-14.md`  
**Delivery:** Complete report supplied here. No file created, edited or deleted.

## Verdict

The Algebra I frame has a sound overall sequence, complete skill placement and a defensible 160-day allocation, but needs revisions before its scope and sequence is written. Its biggest risk is that the paper alternative can leave the required technology computation in statistics unfinished while the course claims complete coverage. Preserve the seven-unit structure and correct the coverage instructions, prerequisite placement and evidence claims identified below.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, teaching approaches, source register, base-text policy, glossary, relevant roadmap sections and BASELINE rules 20 to 24.
- The complete Algebra I frame and inline source map, its `frames.csv` entry, all 28 Grade 9 progression rows and the full text of their 36 owned standard codes, including parent and lettered codes.
- The Grade 8 and Geometry frames, the Algebra II frame, neighboring progression rows, and the relevant Biology and ELA Grade 9 units and dependency tables.
- Earlier Algebra I, Geometry, Algebra II and mathematics progression reviews, including the progression stitch, plus the earlier ELA technology-alternative finding.
- The stored first-edition base-text lesson inventory, pacing chart, lesson-standard table, modeling-prompt inventory and relevant lesson narratives. Checked the supports-course licence record.
- Outside sources linked below. Previous-session memory informed reporting conventions only. No curriculum finding rests on memory.

The requested `data/plans/algebra-i/source-map.csv` is absent. The frame-writing brief schedules the day-level CSV for the scope and sequence stage, so its absence is not itself a frame defect.

**Gates:** `plan.py check` stopped with `ModuleNotFoundError: No module named 'markdown'`; `frame.py check algebra-i` passed with zero failures; `stale.py check` reported 56 files and zero failures.

## Findings, most serious first

### 1. The paper alternative leaves the technology computation unfinished

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, the same issue appears in the ELA Grade 11 review, finding 4.  
**Confidence:** firm

**Location:** Algebra I frame, “Technology and the paper path” and Unit 3.

**Problem and consequence:** Unit 3 correctly requires students to compute correlation using technology. The course-wide alternative offers printed tables, grid paper, a basic calculator and a displayed fit, without explaining how students on that route complete the computation. Interpreting supplied results does not demonstrate the entire requirement. See [CCSS Mathematics, S-ID.C.8](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf).

**Exact fix:** Add:

> The paper route preserves graphing, fitting and interpretation. For S-ID.C.8, each student also uses a shared or individual device, without a student account, to compute the correlation coefficient from paired data. If that opportunity is unavailable, record the technology computation as unfinished.

Name that opportunity in Unit 3 and check it separately from interpretation.

### 2. Unit 7 omits the symmetry requirement from its specification

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier Algebra I review, finding 7.  
**Confidence:** firm

**Location:** Unit 7, “What students learn.”

**Problem and consequence:** The frame names zeros and maximum or minimum values, but does not instruct the writer to teach symmetry through factoring and completing the square. The progression row already contains this requirement. A writer following the frame alone could omit it. See [CCSS Mathematics, F-IF.C.8a](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf).

**Exact fix:** Replace the maximum/minimum sentence with:

> Use factoring and completing the square to reveal zeros, maximum or minimum values, and the axis of symmetry, and interpret these features in context (A-SSE.B.3b, F-IF.C.8a).

Carry those features into the end-of-unit assessment specification.

### 3. The added growth comparison precedes the course’s teaching of quadratics

**Severity:** Moderate  
**LAYER:** frame, base text  
**REPEAT:** yes, earlier Algebra I review, finding 2.  
**Confidence:** likely

**Location:** Unit 5 and the source-map notes for Units 5 and 6.

**Problem and consequence:** Unit 5 claims the quadratic and general polynomial comparison is completed there. Its added activity precedes Unit 6’s introduction to quadratic change. Grade 8 supplies powers and some nonlinear examples, but the frame gives no bridge explaining this early comparison.

The base text compares linear and exponential growth in [lesson 5.19](https://im.kendallhunt.com/HS/teachers/1/5/19/preparation.html), then quadratic and exponential growth in [lesson 6.4](https://im.kendallhunt.com/HS/teachers/1/6/4/preparation.html).

**Exact fix:** Recommend that Unit 5 complete the linear case and Unit 6 finish F-LE.A.3 after base lesson 6.4, including the short cubic or fourth-power comparison. Replace “as review” in Unit 6’s source-map note with “finishes F-LE.A.3.” Keep day totals unchanged.

Moving the completion responsibility between units goes to Cory.

### 4. The focus percentage uses an incomplete classification and does not measure time

**Severity:** Moderate  
**LAYER:** progression, process  
**REPEAT:** yes, earlier Algebra I review, finding 3, and neighboring high school reviews.  
**Confidence:** firm

**Location:** “The bar, applied by analogy.”

**Problem and consequence:** Multiplying unit days by the fraction of tagged rows assumes equal time per row. The tags also omit qualifying content: Table 1 includes F-LE.1, F-BF.1, S-ID.2 and S-ID.7, among other content. The frame’s exclusion of both statistics units from its calculation therefore misclassifies relevant work.

The [High School Publishers’ Criteria, printed pages 7 to 8](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf) were reachable in this read. They specify majority time and explicitly address individual courses. The [current high school review criteria](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf) provide the appropriate high school reference.

**Exact fix:** Remove the 72 percent claim and the imported 65 percent threshold. State that quantitative focus remains provisional. At the scope and sequence stage, classify actual lesson days against Table 1 and document treatment of mixed-content days. Report course results alongside sequence results.

This corrects the earlier reviews’ memory-based assertion that only the sequence needs a focus reading. It establishes no reason to reorder this course.

### 5. The F-IF.C.9 source trail names the wrong starting lesson

**Severity:** Minor  
**LAYER:** frame, base text  
**REPEAT:** yes, earlier Algebra I review, finding 1.  
**Confidence:** firm

**Location:** Unit 4, Unit 6 and “For the lead,” item 3.

**Problem and consequence:** Base lesson 4.9 compares graphs. The explicit different-representation comparison appears in [lesson 6.14](https://im.kendallhunt.com/HS/teachers/1/6/14/preparation.html), which the frame keeps but does not identify for this purpose. The current trail could encourage a writer to count graph-to-graph comparison as sufficient evidence.

**Exact fix:** Describe lesson 4.9 as preparation. Add to Unit 6:

> Comparing quadratic functions given in different representations starts in base lesson 14; F-IF.C.9 is completed in Unit 7.

Retain Unit 7’s equation-against-graph comparison and broaden the progression row’s “quadratics only” wording to reflect the frame’s planned comparisons.

I disagree with the earlier report’s stronger claim that completion necessarily requires every Algebra II function family. [F-IF.C.9](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf) does not impose that requirement.

### 6. The shorter-year alternative removes five days, not ten

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** “For the lead,” item 1.

**Problem and consequence:** Dropping four modeling days and one respond day changes 160 to 155, not 150. It also removes the promised response opportunity after one course-level check.

**Exact fix:** Replace the alternative with:

> Retain the 160-day plan. A shorter calendar needs a separately counted proposal that preserves a respond day after every course-level check.

Do not present a 150-day option until ten specific days and their instructional consequences are identified.

### 7. The prescribed adaptation credit differs from the repository’s required form

**Severity:** Minor  
**LAYER:** process, base text  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Base text,” credit-line instruction.

**Problem and consequence:** “Based on IM K-12 Math…” omits the specific source lesson and the statement that Curio Class changed it. `docs/sources/BASE-TEXTS.md`, “Credit lines,” supplies the required form. Leaving competing instructions invites inconsistent attribution.

**Exact fix:** Replace the sample with:

> Adapted from Illustrative Mathematics K-12 Math, Algebra 1, unit [number], lesson [number], CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Changed by Curio Class.

Use the corresponding source for supports material and modeling prompts.

### 8. Two unit reasons confuse Biology’s need dates with mathematics availability

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier Algebra I review, finding 6.  
**Confidence:** firm

**Location:** Units 2 and 5, “Why this unit, here.”

**Problem and consequence:** Unit 2 says Biology needs quantities by about week 5; Unit 5 says its population simulation needs a stepping rule by about week 17. Biology places the population unit in weeks 12 to 15 and the biodiversity simulation in weeks 29 to 31. The mathematical work is available sufficiently early, but the stated reasons misrepresent the shared calendar.

**Exact fix:** Use:

- Unit 2: “Available before Biology’s population unit in weeks 12 to 15.”
- Unit 5: “Available before Biology’s biodiversity simulation in weeks 29 to 31.”

Retain Biology’s explicit teaching of its earlier population step rule from Grade 7 percent.

### 9. The Grade 8 seam introduction incorrectly calls the receiving frames unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Algebra I reviews.  
**Confidence:** firm

**Location:** `docs/courses/math-grade-8/frame.md`, outgoing-seam introduction.

**Problem and consequence:** Both receiving frames exist. The note gives a false reason for postponing a two-ended seam check.

**Exact fix:** Replace the introduction with:

> Handed on to Algebra I and Geometry. The receiving frames are `docs/courses/algebra-i/frame.md` and `docs/courses/geometry/frame.md`; the table names their progression rows.

### 10. Two Grade 8 notes incorrectly say N-Q.A.3 has no row

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Algebra I reviews.  
**Confidence:** firm

**Locations:** Grade 8 frame, scientific-notation seam cell and “For the lead,” item 6.

**Problem and consequence:** N-Q.A.3 is owned by `geo-solving-right-triangles` and begun by `alg1-scatter-linear-models`. The missing scientific-notation link is a different issue. The present wording could prompt unnecessary ownership repairs.

**Exact fix:** Replace both explanations with:

> `m8-scientific-notation` has no recorded outgoing progression link. N-Q.A.3 already has an owner, `geo-solving-right-triangles`, and is begun in `alg1-scatter-linear-models`. Missing linkage must be considered separately from ownership.

Do not invent a dependency solely to eliminate an empty handoff.

### 11. The progression stitch still lists an inverse-functions contribution as unapplied

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale unresolved-work notes recur in earlier frame reads.  
**Confidence:** firm

**Location:** `docs/reviews/progression-math-stitch-2026-11-13.md`, item 20.

**Problem and consequence:** Its action cell says `alg2-rational-exponents` lacks `~F-BF.B.4a` and the nonlinear-inverse contribution. Both are now present, and Algebra II Unit 3 explicitly budgets the applying day. The note invites duplicate work.

**Exact fix:** Replace its current action status with:

> Applied, verified 2026-11-14: `alg2-rational-exponents` carries `~F-BF.B.4a` and the inverse contribution; Algebra II Unit 3 includes the nonlinear-inverse applying day. Ownership remains in Algebra I.

## Coverage, days and seams

All 28 owned skills occur exactly once. Earlier-grade returns are identified as readiness, recall or reactivation; later-course contributions are explicitly distinguished from ownership.

| Unit | Owned skill rows | Base lessons | Retained lesson days | Added days | Total |
|---|---:|---:|---:|---:|---:|
| 1 | 2 | 16 | 14 | 3 | 17 |
| 2 | 6 | 26 | 26 | 3 | 29 |
| 3 | 3 | 10 | 10 | 3 | 13 |
| 4 | 5 | 18 | 18 | 3 | 21 |
| 5 | 3 | 21 | 21 | 3 | 24 |
| 6 | 3 | 17 | 17 | 3 | 20 |
| 7 | 6 | 24 | 24 | 3 | 27 |
| **Total** | **28** | **132** | **130** | **21** | **151** |

Nine course-level assessment and respond days produce 160 days. Each course-level check has a respond day. The long linear and quadratic-equation units have defensible loads; the short statistics unit follows ten base lessons. No unit is demonstrably far over or under its share at frame resolution.

All 132 base lessons and nine modeling prompts receive a disposition. The spreadsheet merge is explained, unit order is preserved, and no reference-only or NC edition is mapped. The national-debt replacement is a permissible context choice; its eventual task must preserve the mathematical work of the replaced prompt.

Recorded incoming and outgoing seams generally match. The Grade 8 proposal to add a proportional-comparison link remains unapplied, but Algebra I already teaches the receiving linear work. The inverse contribution in Algebra II is now placed, so that settled progression decision should remain intact.

Same-year dependencies are workable: ELA’s argument unit follows the mathematics causation work; Biology supplies its early step rule and has fallback instruction for early displays. Neither context requires mathematics to wait for Biology.

## Mathematics lens: course frame checklist

| Checklist line | Result |
|---|---|
| Major work satisfies the applicable focus criterion | **Missed as evidence:** the percentage and classification need correction, finding 4. This does not establish inadequate instructional focus. |
| Supporting work practises major work | **Met:** two-variable statistics uses linear equations; one-variable statistics builds the comparison and interpretation work used later. |
| Every source-map row has a keep, split, merge, cut or ours decision | **Met:** every row has a decision, including prompt cuts and replacement. |

All eight mathematical practices are named across the frame. Task-level enactment, fluency spacing and assessment coverage require the later planning layers.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Preserve seven units and 160 days | Skill placement, base sequence and total allocation hold | Algebra I frame |
| Require student computation of correlation on a shared or individual device | Preserves the complete performance while retaining paper access | Algebra I frame, Unit 3 |
| Restore explicit quadratic symmetry | Already required by the owned standard and progression row | Algebra I frame, Unit 7 |
| Identify lesson 6.14 as the different-representation comparison | Verified against the base lesson | Algebra I frame, Units 4 and 6 |
| Preserve the settled Algebra II nonlinear-inverse contribution | It is now explicitly placed | Progression stitch status |
| Use Biology’s current unit windows | Distinguishes demand from availability | Algebra I frame, Units 2 and 5 |
| Remove the uncounted shorter-year alternative | Its arithmetic and respond-day provision fail | Algebra I frame, lead item 1 |
| Use the repository’s adaptation-credit form | Gives writers one consistent instruction | Algebra I frame |

## What should remain

Preserve the statistics opening, linear algebra before fitted lines, functions before exponentials, and quadratic functions before equation-solving methods. Preserve the readiness checks after instructional gaps, supports outside the core day count, anonymous survey restrictions and course-level respond days.

## Limits and outside sources

This is a frame review. It cannot establish actual lesson duration, assessment quality or student performance.

The published combined Progressions PDF exceeded the web reader’s size limit; the linked high school drafts also failed to load. Their detailed page claims were therefore not independently verified, and no finding relies on remembered Progressions content.

Sources opened or inspected:

- [CCSS Mathematics](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): owned standards and modeling requirements.
- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): applicable focus framework and Table 1.
- [High School Review Criteria v2.0](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf): high school coverage, modeling and rigor expectations.
- [Base-text scope and sequence](https://im.kendallhunt.com/HS/teachers/1/scope_and_sequence.html): sequence and stored pacing chart.
- [Base-text lesson-standard table](https://im.kendallhunt.com/HS/teachers/1/lessons_and_standards.html): stored per-lesson alignments.
- [Fishtank Algebra I pacing](https://www.fishtanklearning.org/curriculum/math/algebra-1/pacing-guide/): comparison of year length, flexibility and period assumptions.
- [Eureka high school overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G912_CurriculumOverview.pdf): reference-only comparison of sequence and calendar allowance.
- [WWC algebra practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/20): structure, solved-example analysis and strategy choice. Supports preserving the frame’s method-selection emphasis.
- [Official Progressions index](https://archive.math.arizona.edu/ime/progressions/): source provenance; linked high school documents were inaccessible.

## For the source list

Record the working Publishers’ Criteria PDF and current high school criteria links above. They resolve access limitations recorded in the earlier reviews. Also record the base-text scope-and-sequence route and lesson-standard table.

## For Cory

- Decide whether F-LE.A.3 finishes in Unit 6 as recommended. This moves a standard’s completion responsibility between units.
- Keep the accelerated Grade 8 audience conditional on a compression plan. This frame assumes Grade 8 prerequisites and does not itself supply that plan.

**Verdict:** Sound structure, revisions required before the scope and sequence. **Finding count:** 11. **Report path:** `docs/reviews/frame-algebra-i-2026-11-14.md`, supplied here only.

