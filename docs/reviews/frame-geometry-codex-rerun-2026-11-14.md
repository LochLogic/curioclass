# Geometry course frame: independent expert review

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-geometry-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files edited or created.

## Verdict

The frame has a coherent course structure and a credible 160-day budget, but it needs revision before unit writers build from it. Its main risk is that the promise of complete standards coverage exceeds the explicit teaching contract, with required details omitted and one theorem attributed to the wrong unit. Restore those details and correct the high school focus rationale while preserving the base unit order.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, teaching approaches, source register, glossary, relevant ROADMAP sections, and BASELINE rules 20 to 24.
- The complete Geometry frame, its `frames.csv` entry, all 28 grade 10 mathematics progression rows, related prerequisite and receiving rows, and the full text of its 52 owned standard codes, including parent and lettered codes.
- The Algebra I and Algebra II frames; relevant grade 8, Biology and Chemistry handoffs.
- The base-text policy, frame-writing brief, relevant progression reviews, both existing Geometry reviews, and related mathematics frame reviews.
- The local first-edition Geometry lesson inventory, lesson-standard table, modeling-prompt index, and targeted lesson and prompt texts.
- Outside sources linked below, including the high school review criteria, publishers’ criteria, Geometry progression, three curriculum sequences, and a federal research guide.

`data/plans/geometry/source-map.csv` does not exist. The frame-writing brief assigns that day-level file to the later scope and sequence stage, so its absence is not a frame defect.

**Gate limitation:** `python -X utf8 scripts/plan.py check` could not complete because importing `lesson.py` raises `ModuleNotFoundError: No module named 'markdown'`.

`python -X utf8 scripts/frame.py check geometry` passed with zero failures. `python -X utf8 scripts/stale.py check` passed across 56 files with zero failures.

## Findings, most serious first

### 1. Several required parts disappear from the explicit completion promise

**Severity:** Serious  
**LAYER:** frame, standard  
**REPEAT:** yes, incomplete standards wording was identified in the earlier Geometry review, finding 5  
**Confidence:** firm

**Location:** Geometry frame, units 2, 5 and 8.

**What is wrong:** These units claim completion without naming the following required content:

| Standard | Missing from the frame’s teaching contract | Exact fix |
|---|---|---|
| G-CO.C.11, unit 2 | The converse concerning bisected diagonals | Add: “Prove conversely that a quadrilateral whose diagonals bisect each other is a parallelogram.” |
| N-Q.A.1, unit 5 | Choosing and interpreting the origin in graphs and data displays | Replace “Units guide multi-step work and graph scales” with “Use units to guide multi-step work and interpret formulas; choose and interpret scales and origins in graphs and data displays.” |
| S-CP.A.3, unit 8 | Independence interpreted in both conditioning directions | Add \(P(B\mid A)=P(B)\), alongside the existing \(P(A\mid B)=P(A)\), with nonzero conditioning probabilities. |
| S-CP.B.8, unit 8, if retained | Both factorizations and interpretation of their result | State and apply \(P(A\cap B)=P(A)P(B\mid A)=P(B)P(A\mid B)\) in a uniform model, interpreting the answer in context. |

These requirements appear in the official [congruence standards](https://www.thecorestandards.org/Math/Content/HSG/CO/), [quantity standards](https://www.thecorestandards.org/Math/Content/HSN/Q/) and [conditional probability standards](https://www.thecorestandards.org/Math/Content/HSS/CP/). The parallelogram converse is also explicitly taught in [base lesson Geo.2.13](https://im.kendallhunt.com/HS/teachers/2/2/13/index.html).

**Why it matters:** A writer following the frame can omit these parts from instruction and assessment while still believing the unit completes its standards. Source lessons containing the material do not repair an explicit planning contract that leaves it out.

**Exact fix:** Apply the wording above within the existing units and days. Update the corresponding progression notes where they carry the same omissions, especially `geo-modeling-objects-density` and `geo-conditional-independence`. Keep current ownership unchanged.

### 2. The midsegment proof is attributed to unit 6 instead of unit 3

**Severity:** Serious  
**LAYER:** frame, base text  
**REPEAT:** yes, earlier Geometry review, finding 2  
**Confidence:** firm

**Location:** Units 3 and 6; `geo-coordinate-proofs` notes.

**What is wrong:** Unit 6 identifies the midsegment theorem among the triangle theorems completed there, without naming its earlier proof. Unit 3 does not name that contribution to G-CO.C.10. However, [Geo.3.5](https://im.kendallhunt.com/HS/teachers/2/3/5/index.html) proves the midsegment relationship using dilation. Geo.6.16 supplies the later median-concurrence work.

**Why it matters:** Unit 3’s assessment contract can miss a theorem actually taught there, while a unit 6 writer can plan its initial proof unnecessarily.

**Exact fix:**

- Unit 3: add “Prove that the segment joining two side midpoints is parallel to the third side and half its length, using dilation (G-CO.C.10 contribution; base lesson 5).”
- Unit 6: identify “midsegment theorem proved in unit 3; median concurrence proved here in base lesson 16.”
- Correct `geo-coordinate-proofs` notes to say unit 6 completes the remaining median theorem, rather than the last two theorems.

This records existing instruction. It does not move ownership of G-CO.C.10.

### 3. The unit 2 modeling prompt needs its volume readiness check earlier

**Severity:** Moderate  
**LAYER:** frame, base text  
**REPEAT:** yes, the earlier-read category is prerequisite checks placed after first use  
**Confidence:** firm

**Location:** Unit 2 readiness description; unit 5 readiness description; Source map, “How Much Water?”

**What is wrong:** The frame keeps “How Much Water?” in unit 2 but names the readiness check for `m8-volume-curved` in unit 5. The prompt’s structured version asks students to calculate a cylindrical glass’s capacity and design containers. Its open version also requires students to choose and calculate container volumes. See the [public task](https://im.kendallhunt.com/HS/teachers/2/modeling_prompts/4/modeling_tasks.html).

**Why it matters:** The course deliberately rebuilds knowledge after intervening years, but this task can expose a volume gap several units before the promised check and reminder.

**Exact fix:** Add a short cylinder-volume item to unit 2’s existing readiness day, followed by a brief formula-and-units reminder for students who miss it. Name the prompt as an application of earlier volume work that begins the later modeling thread. Retain unit 5’s readiness check before explaining volume formulas in greater depth.

No additional day or ownership change is needed.

### 4. The high school focus rationale uses the wrong measure and an unsupported exception

**Severity:** Moderate  
**LAYER:** frame, progression, process  
**REPEAT:** yes, earlier Geometry review, finding 1, with a substantive disagreement  
**Confidence:** firm

**Location:** “The bar, applied by analogy”; For the lead, item 2; progression prerequisite tags.

**What is wrong:** Multiplying unit days by the fraction of tagged skill rows does not measure instructional time. It also omits explicitly listed geometry prerequisites: G-CO.A.1, G-CO.C.9 and G-CO.C.10. The [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf), PDF pages 7 to 8, apply the majority-of-time criterion to each course. They do not authorize replacing Geometry’s result with a sequence average.

The current [high school review criteria](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf), indicator 1b.i, likewise require evidence about students’ instructional time.

**Why it matters:** The 26 percent and 52 percent figures cannot establish either a shortfall or an adequate focus allocation.

**Exact fix:** Remove those figures and the sequence-only exception. Use the high school criteria directly, correct the prerequisite classifications, and require the scope and sequence to document time spent developing the identified prerequisites and their connections.

**Disagreement with the earlier read:** Its endorsement of a sequence-only interpretation rested on memory. The accessible primary source does not support that endorsement. This finding does not establish that Geometry itself lacks sufficient focus.

### 5. Unit 8 confuses retained instruction with an extension and misstates its source evidence

**Severity:** Minor  
**LAYER:** frame, base text  
**REPEAT:** yes, earlier Geometry review, finding 6  
**Confidence:** firm

**Location:** Unit 8 “Check set adds”; For the lead, item 3; `geo-conditional-independence` notes.

**What is wrong:** “Probabilities in Games” is already Geo.8.11, included among the eleven retained lessons. Calling it an extension does not identify additional depth. Its [lesson preparation](https://im.kendallhunt.com/HS/teachers/2/8/11/preparation.html) identifies conditional probability and independence, rather than the general multiplication rule.

The multiplication-rule discussion is present in [Geo.8.9](https://im.kendallhunt.com/HS/teachers/2/8/9/index.html), which the frame’s supporting citation omits. The [lesson-standard table](https://im.kendallhunt.com/HS/teachers/2/lessons_and_standards.html) does not explicitly align a Geometry lesson to S-CP.B.8.

**Why it matters:** Writers can double-count an existing lesson as enrichment and mistake related source instruction for explicit coverage of the complete additional standard.

**Exact fix:** Cite lessons 8 to 10 as related instruction, distinguish that from explicit S-CP.B.8 alignment, and remove lesson 11 as evidence for the multiplication-rule claim. Replace the extension entry with: “Candidate: analyze an additional fictional game using both a two-way table and a tree diagram, explaining how the representations agree.”

### 6. The proposed credit line differs from the repository’s adaptation rule

**Severity:** Minor  
**LAYER:** base text, process  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Base text” bullet.

**What is wrong:** The frame prescribes “Based on IM K-12 Math by Illustrative Mathematics, CC BY 4.0.” The current `docs/sources/BASE-TEXTS.md`, “Credit lines,” requires identification of the adapted lesson, a license link, and an explicit statement that Curio Class changed it.

**Why it matters:** A writer copying the frame’s instruction would produce credits inconsistent with the repository’s current source policy.

**Exact fix:** Replace the prescribed line with the policy’s form, substituting the actual unit and lesson:

> Adapted from Illustrative Mathematics K-12 Math, Geometry, unit N, lesson M, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Changed by Curio Class.

### 7. The stitch report still describes the nonlinear inverse contribution as absent

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, existing independent Geometry review, finding 2  
**Confidence:** firm

**Location:** `docs/reviews/progression-math-stitch-2026-11-13.md`, item 20.

**What is wrong:** The Pick cell says `alg2-rational-exponents` lacks both `~F-BF.B.4a` and the applying-day note. The current progression contains both, and the reconcile report records their addition.

**Why it matters:** Completed work remains presented as an outstanding action.

**Exact fix:** Replace the pending wording with:

> Completed in the reconcile: `alg2-rational-exponents` carries `~F-BF.B.4a`, assumes `alg1-inverse-functions`, and names one applying day on cube roots undoing cubing. Ownership remains with `alg1-inverse-functions`.

### 8. The stitch report still says two repaired Geometry rows assume nothing

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, existing independent Geometry review, finding 3  
**Confidence:** firm

**Location:** `docs/reviews/progression-math-stitch-2026-11-13.md`, final note about three Geometry rows.

**What is wrong:** The note groups `geo-constructions`, `geo-inscribed-circumscribed` and `geo-addition-rule` as having no prerequisites. Current data give the first row `m7-triangle-conditions` and the third `alg1-two-way-tables`. The fix report records both changes.

**Why it matters:** The note contradicts the repaired prerequisite contract.

**Exact fix:** Replace it with:

> Updated after the progression reads: `geo-constructions` assumes `m7-triangle-conditions`, and `geo-addition-rule` assumes `alg1-two-way-tables`. `geo-inscribed-circumscribed` retains an empty earlier-grade `assumes` field; its same-course construction dependencies remain in its notes.

### 9. The older grade 4 scope and sequence incorrectly says nothing is built

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale availability and completion notes recur in earlier frame reviews  
**Confidence:** firm

**Location:** `docs/courses/math-4-spine.md`, opening paragraph.

**What is wrong:** “Nothing here is built or public” conflicts with existing lesson sources and rendered artifacts, including `courses/math-4/u01-1/d001.md` and files under `build/lessons/math-4/u01-1/`.

**Why it matters:** The mathematics lens points reviewers to this worked pattern. Its status statement understates what exists and can cause unnecessary reconstruction.

**Exact fix:** Replace that sentence with:

> Lesson sources and rendered build artifacts exist under `courses/math-4/` and `build/lessons/math-4/`. Their existence does not establish publication or classroom readiness; consult the current course-status record for those decisions.

The separate statement that the complete start-of-year check is unwritten was not disproved: the readiness sheet explicitly remains its fallback.

## Coverage, pacing and what should be preserved

Every grade 10 progression skill is placed exactly once: **28 placed, none missing, none duplicated, no foreign owned skills**. Earlier-grade content is identified as retrieval or rebuilding. Finding 3 corrects the timing of one such check.

| Unit | Owned skill rows | Base lessons | Added days | Total days |
|---|---:|---:|---:|---:|
| 1 | 4 | 22 | 4 | 26 |
| 2 | 3 | 15 | 4 | 19 |
| 3 | 3 | 16 | 3 | 19 |
| 4 | 2 | 11 | 3 | 14 |
| 5 | 4 | 18 | 3 | 21 |
| 6 | 5 | 17 | 4 | 21 |
| 7 | 3 | 14 | 3 | 17 |
| 8 | 4 | 11 | 3 | 14 |
| **Total** | **28** | **124** | **27** | **151** |

The added days comprise eight readiness days, eight modeling days, eight assessment days, and three additional proof or construction practice days. Nine course-level days bring the total to 160, including a respond day after each cumulative check. No unit is demonstrably far over or under its load at frame level.

Preserve:

- Construction and rigid motions before congruence, similarity before trigonometry, and coordinate work before the final circle applications.
- The staged growth of proof and the paper path for constructions and technology.
- The explicitly documented G-CO.C.9 contribution across units 1 and 2.
- The complete inventory of 124 base lessons in their original unit order. All eleven modeling-prompt entries have a decision, including the introduction and two exclusions from separate prompt days.
- The first-edition CC BY source boundary. No NC or reference-only curriculum is mapped.
- The incoming Algebra I handoffs for equations, completing the square, functions and tables, and the outgoing Algebra II handoffs for roots, transformations, trigonometry, radians and sample spaces.
- Biology’s earlier-year inherited-trait context. Chemistry’s early quantity needs have explicit fallback teaching in its own frame; the cross-subject tables do not require Chemistry to wait for Geometry.

The two early course checks and the final check provide reasonable cumulative return points. Actual practice distribution and instructional minutes still require the later scope and sequence.

## Mathematics lens checklist: course frame layer

| Lens line | Result |
|---|---|
| Major work receives the required share by units, days or time | **Missed as evidence:** the current proxy does not establish time allocation. Apply the high school measure, finding 4. The K to 8 numerical threshold is not applicable. |
| Supporting clusters practise major work | **Met at frame level:** algebra, quantity, similarity and proof connections are named. Finding 3 repairs one prerequisite check. |
| Every source-map row has a keep, split, merge, cut or ours decision | **Met:** the inline map records decisions. Finding 5 corrects an extension label. |

The lens’s additional requirement to consult high school criteria is satisfied by this read. The frame’s proposed K to 8 analogy should be replaced. Detailed practice tasks, assessment items, fluency spacing and all eight practice standards remain later-layer checks.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep eight units and 160 days | Base sequence and added-day budget are credible | Geometry frame; `frames.csv` unchanged |
| Add cylinder-volume retrieval to unit 2’s existing readiness day | It precedes the first retained task requiring it | Geometry frame, unit 2 |
| Record the midsegment proof in unit 3; retain G-CO.C.10 ownership in unit 6 | Corrects attribution without moving ownership | Geometry frame; progression notes |
| Add the missing required wording within existing units | Completes existing standards rather than expanding scope | Geometry frame; relevant progression notes |
| Use the additional-game comparison as the unit 8 extension candidate | It adds depth beyond retained lesson 11 | Geometry frame, unit 8 |
| Use the current adaptation-credit form | One consistent source policy | Geometry frame |
| Rewrite the three stale notes as specified | Current files establish completion or availability | Findings 7 to 9 locations |

## For Cory

- **Scope:** Confirm the existing proposal to retain S-CP.B.8 as required Geometry content. Recommendation: retain it only with the complete wording in finding 1; it is an additional (+) standard, so its required status remains your decision. No change to the accelerated audience or course length is proposed.

## Sources and limits

- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): course-level focus and the actual prerequisite list, PDF pages 7 to 8.
- [High school mathematics review criteria v2.0](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf): full standards, modeling, instructional time, coherence and practices.
- [Geometry standards](https://www.thecorestandards.org/Math/Content/HSG/), [quantity standards](https://www.thecorestandards.org/Math/Content/HSN/Q/), and [probability standards](https://www.thecorestandards.org/Math/Content/HSS/CP/): checked against the repository’s full standard text.
- [Geometry Progression, March 2016 draft](https://mathematicalmusings.org/wp-content/uploads/2016/03/ccss_progression_g_7_hs_2016_03_27.pdf): middle-grade foundations, transformations, proof, similarity and analytic geometry.
- [Base course narrative](https://im.kendallhunt.com/HS/teachers/2/narrative.html), [scope and sequence](https://im.kendallhunt.com/HS/teachers/2/scope_and_sequence.html), and [lesson-standard map](https://im.kendallhunt.com/HS/teachers/2/lessons_and_standards.html): source order, dependency rationale and placement.
- [New York’s archived curriculum overview](https://www.nysedregents.org/engageny/a-story-of-functions-curriculum-map-and-overview.pdf), Geometry section: comparison sequence, used as reference only.
- [Mathematics Vision Project Geometry framework](https://www.mathematicsvisionproject.org/uploads/1/1/6/3/11636986/2_geometry_framework_overview_and_scope_and_sequence.pdf): another comparison sequence, including probability.
- [Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/20072004.pdf): spaced return and connections among representations.

The compiled 2023 Progressions exceeded the web tool’s size limit; the accessible 2016 Geometry draft was used instead. This review cannot establish actual lesson timing, assessment completeness or classroom effectiveness from a frame.

No curricular finding rests on memory. Prior session memory informed report structure only.

### For the source list

Record the accessible 2016 Geometry progression and the current high school criteria links above. The publishers’ criteria PDF was readable during this run, including its prerequisite table, resolving the access limitation reported in the earlier Geometry read.

**Verdict:** Coherent structure; revision required before unit writing. **Finding count:** 9. **Report path:** `docs/reviews/frame-geometry-2026-11-14.md`, supplied here only.

