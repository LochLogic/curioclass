# Algebra II course frame: independent review

Intended report path: `docs/reviews/frame-algebra-ii-2026-11-14.md`

Supplied here in full. No files were created, edited or deleted.

## Verdict

The frame has a sound course structure, with coherent prerequisites, complete skill placement and a defensible 160-day budget. Its biggest risk is an unfinished handoff for comparing functions across representations, compounded by several completion claims that need more precise teaching commitments. Revise those commitments and replace the unsupported focus calculation before using the frame to direct unit writing.

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, the K to 8 mathematics rubric, the foundation, teaching approaches, source register, glossary and relevant planning rules.
- The complete Algebra II frame, its `frames.csv` entry, all 26 grade 11 mathematics progression rows and the full text of their owned and contributing standards.
- Geometry’s incoming handoffs and course structure, Algebra I’s relevant outgoing handoffs, and prerequisite progression rows.
- Relevant Physics, Chemistry, Economics, Government and ELA frame entries.
- Earlier Algebra II, Algebra I, Geometry and mathematics progression reviews, including the stitch, fixes and reconcile records.
- The base text’s course narrative, lesson inventory, standards alignments, modeling-prompt inventory and selected lesson descriptions.
- The outside sources linked below.

`data/plans/algebra-ii/source-map.csv` does not exist. The frame-writing brief explicitly schedules that CSV for the scope and sequence layer; the inline frame source map is the appropriate artifact here.

No Precalculus, Statistics or Calculus frame exists at the expected paths. Their receiving sides therefore cannot yet be checked.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not finish: importing `lesson.py` raises `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check algebra-ii` | Passed: zero failures; seven units, 151 unit days and nine check and respond days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files checked, zero failures. |

The incomplete full gate is an environment limitation, not a reason to withhold this curriculum verdict.

## Findings, most serious first

### 1. The function-comparison handoff has no receiving commitment

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, unresolved in the earlier Algebra I and Algebra II frame reads  
**Confidence:** firm

**Location:** Algebra II units 2, 4 and 6; Algebra I’s “For the lead” item 3; `alg1-vertex-form-max-min`.

**What is wrong:** Algebra I proposes handing comparisons involving later function families to Algebra II. This frame never names F-IF.C.9, and the progression owner still limits its comparisons to quadratics. Graphing several families and finding graph intersections do not by themselves establish comparison of two functions presented in different representations.

The standard requires that comparison capability, and the Functions Progression explains why students must connect representations rather than merely extract features from expressions. [Mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf), [Functions Progression, PDF pages 9 to 10](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_functions_2013_07_02.pdf).

**Why it matters:** A writer can follow both frames faithfully and never finish the promised transfer beyond Algebra I’s families.

**Exact fix:** Keep ownership with `alg1-vertex-form-max-min`, and explicitly name these contributions within existing days:

- Unit 2: compare a polynomial supplied as a graph with another supplied in factored form.
- Unit 4: compare exponential functions supplied as a table and an equation.
- Unit 6: compare periodic models supplied as a graph and an equation.

Require a justified comparison of relevant properties, rather than graph-to-graph matching alone. Add the receiving contributions and matching outgoing handoff to the progression notes, and include one unfamiliar comparison on the year-end course check. No added day is needed.

### 2. The focus calculation uses the wrong yardstick and does not measure time

**Severity:** Moderate  
**LAYER:** frame, process  
**REPEAT:** yes, earlier Algebra I, Geometry and Algebra II focus findings remain unresolved  
**Confidence:** firm

**Location:** “The bar, applied by analogy,” line 11; “For the lead,” item 5.

**What is wrong:** The 57 percent figure allocates unit days according to the proportion of tagged progression rows. Rows have unequal instructional demands, and the tagging omits relevant content: unit 7 includes S-IC.A.1, which the high school prerequisite table explicitly names.

The applicable high school sources are reachable. They call for a majority of instructional time on widely applicable prerequisites; the Publishers’ Criteria explicitly state this for each course. A sequence-wide total supplements that judgment. The K to 8 65 percent threshold is not the Algebra II threshold. [High School Publishers’ Criteria, PDF pages 7 to 8](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf), [High School Review Criteria, indicator 1b.i](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf).

**Why it matters:** The current figure can justify inappropriate content changes or give false assurance about instructional emphasis.

**Exact fix:** Replace the analogy paragraph with a high school criterion and label the current percentages as withdrawn estimates. At the scope and sequence layer, classify actual lesson tasks against the published prerequisite table and total their instructional time, including relevant portions of added days. Report each course separately, with the series total alongside it. Do not change unit allocations merely to reach the K to 8 percentage.

This corrects the earlier reviews’ memory-based suggestion that a sequence-wide reading alone settles the criterion.

### 3. Unit 2 claims to finish A-CED.A.1 without placing its exponential case

**Severity:** Moderate  
**LAYER:** frame, standard  
**REPEAT:** yes, earlier Algebra II finding 3 remains unresolved  
**Confidence:** firm

**Location:** Unit 2, line 105; `alg2-rational-equations`.

**What is wrong:** The progression row includes creating equations from rational and exponential relationships, but the unit describes its completion through rational equations. The standard includes simple exponential equations, while the mapped base lessons 20 and 21 address rational contexts. [Mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf), [base-text lesson alignments](https://im.kendallhunt.com/HS/teachers/3/lessons_and_standards.html).

**Why it matters:** “Finished here” allows the missing case to disappear from the unit’s teaching and assessment.

**Exact fix:** Keep ownership in `alg2-rational-equations`. Add one explicitly named exponential-context task within an existing unit 2 day, using Algebra I knowledge and a solution accessible through known powers or a graph. For example, students create and solve \(80(2^t)=640\) from a supplied doubling situation. Include an equation-creation item in the end-of-unit assessment.

Unit 4 then extends this work through logarithmic solutions. Moving completion to unit 4 is another possible repair, but logarithms are not necessary to satisfy the simple exponential case.

### 4. The prescribed credit line conflicts with the current lesson rule

**Severity:** Moderate  
**LAYER:** base text, process  
**REPEAT:** yes, source-credit requirements recur in earlier ELA frame reviews  
**Confidence:** firm

**Location:** “Base text,” line 12.

**What is wrong:** The frame instructs adapted days to use “Based on IM K-12 Math by Illustrative Mathematics, CC BY 4.0.” The current requirements in `docs/sources/BASE-TEXTS.md`, “Credit lines,” and `docs/courses/LESSON-DAY.md`, rule 4, specify a source locator, licence link and statement that Curio Class changed the material.

**Why it matters:** A writer following this frame would reproduce an obsolete credit template across the course.

**Exact fix:** Replace that instruction with the current template, substituting the actual unit and lesson:

> Adapted from Illustrative Mathematics K-12 Math, Algebra 2, unit \<n>, lesson \<n>, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Changed by Curio Class.

Keep the single credit in the day’s header and printed foot, repeated once in the teacher page’s Credit section.

### 5. The even-and-odd commitment does not explicitly include equations

**Severity:** Minor  
**LAYER:** frame, standard  
**REPEAT:** yes, the graphical/algebraic omission in earlier Algebra II finding 4 remains unresolved  
**Confidence:** firm

**Location:** Unit 5, line 108.

**What is wrong:** “Even and odd functions from symmetry” does not clearly commit the writer to recognition from algebraic expressions as well as graphs. The standard requires both. The base text already provides both through lessons 5 and 6, including an equation-only justification in lesson 6. [Mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf), [lesson 6 preparation](https://im.kendallhunt.com/HS/teachers/3/5/6/preparation.html).

**Why it matters:** A graphical symmetry activity can become the entire treatment.

**Exact fix:** Replace the phrase with:

> Recognize even, odd and neither functions from graphs and algebraic expressions, justifying the algebraic decision using \(f(-x)\) in base lessons 5 and 6.

Use both representations in the unit assessment. No additional day is needed.

### 6. Two pacing claims disagree with the frame’s own counts

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, prose-calendar arithmetic discrepancies recur in earlier frame reads  
**Confidence:** firm

**Location:** “Days,” line 8; “For the lead,” item 1, line 159.

**What is wrong:**

- The proposed 150-day alternative removes six added days from units 2, 4 and 6, plus two modeling days. That removes eight days, leaving **152**, not 150.
- Unit 4 is described as owning the most codes, ten. Unit 2 lists **13** owned codes.

**Why it matters:** These statements mislead the person selecting a shorter calendar or judging instructional load. The main 160-day total remains correct.

**Exact fix:** Change the alternative’s stated total to **152** for the listed cuts. Replace the code-count claim with:

> Unit 2 owns 13 codes across seven rows; unit 4 owns ten codes across four rows.

Keep 160 as the recommended year. Selecting and validating a shorter course remains a scope decision.

### 7. The progression stitch still requests a completed inverse contribution

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier independent Algebra II finding 2 remains unresolved  
**Confidence:** firm

**Location:** `docs/reviews/progression-math-stitch-2026-11-13.md:62`, item 20.

**What is wrong:** The note says the nonlinear-inverse applying day is not yet recorded in `alg2-rational-exponents`. The current row contains `~F-BF.B.4a` and the applying-day note; the reconcile report records completion, and frame unit 3 allocates the day.

**Why it matters:** The stale instruction can prompt duplicate allocation or unnecessary row edits.

**Exact fix:** Replace the outstanding-work text with:

> Implemented: `alg2-rational-exponents` carries `~F-BF.B.4a`, assumes `alg1-inverse-functions`, and names the cube-root inverse applying day. Algebra II frame unit 3 allocates that day. Ownership remains with `alg1-inverse-functions`.

This records planning completion without claiming a finished lesson exists.

## Coverage, order and days

All **26 owned skills** appear once. The frame lists the progression’s **51 owned codes**, including parent codes and subparts. Earlier-grade work is identified as readiness, retrieval or contribution rather than silently re-owned.

| Unit | Skills | Base lessons | Planned days | Load judgment |
|---|---:|---:|---:|---|
| 1. Sequences | 1 | 11 | 14 | Appropriate introduction and algebra re-entry |
| 2. Polynomials and rational functions | 7 | 26 | 31 | Long but coherent; its internal sections justify the span |
| 3. Exponents and complex numbers | 4 | 19 | 24 | Added rewriting and inverse work have clear purposes |
| 4. Exponentials and logarithms | 4 | 18 | 23 | Plausible for the new representations and equation solving |
| 5. Transformations | 2 | 11 | 14 | Compact but supported by earlier function work |
| 6. Trigonometric functions | 4 | 19 | 24 | Appropriate allowance for unit-circle construction and modeling |
| 7. Inference | 4 | 16 | 21 | Plausible for simulation-based inference with sampling rebuilt |

The budget is **120 base lessons + 21 readiness, modeling and assessment days + ten added days = 151 unit days**. Nine course check and respond days bring it to **160**.

No unit is demonstrably far over or under its share. The prerequisite chain holds: polynomial arithmetic precedes complex arithmetic, rational exponents precede expanded exponential work, and transformations precede transformed trigonometric models. This follows the [base-text course narrative](https://im.kendallhunt.com/HS/teachers/3/narrative.html).

All 120 base lessons are covered by nonoverlapping ranges in their original order. All eight modeling prompts receive a disposition, including the introductory prompt merged into unit 1. No reference-only or noncommercial source is mapped as an adaptation base.

## Seams and cross-subject checks

- Geometry supplies the required roots, coordinate transformations, right-triangle ratios, radians, unit circle and sample spaces.
- Algebra I readiness checks address the intervening Geometry year. Grade 7 random sampling is explicitly rebuilt.
- Physics places waves in weeks 16 to 19, before Algebra II’s trigonometry in weeks 23 to 28. Both frames support a different local order.
- Chemistry teaches the half-life context in the preceding year.
- Economics and Government provide local bridges for students taking them before Algebra II’s relevant units.
- Grade 10 ELA argument evaluation precedes its use here; grade 12 ELA’s report evaluation follows Algebra II.
- The elective handoffs are useful proposed endpoints. Their receiving frames remain unavailable.

## Mathematics lens checklist: course frame layer

| Checklist line | Result |
|---|---|
| Major work judged by units, days or time against the applicable line | **Missed:** the row-weighted percentage does not establish instructional time. Finding 2 supplies the applicable high school criterion. |
| Supporting work practises major work | **Met at frame level:** trigonometry reuses transformations and function interpretation; inference carries its own identified prerequisite content. |
| Every source-map row has a disposition | **Met:** lesson ranges, modeling prompts and added days have explicit decisions. |

Daily practice spacing, practice-specific tasks, assessment items and support quality belong to later layers and cannot yet be certified.

## What is right and should not be touched

Preserve the seven-unit sequence, the named readiness returns, the sampling rebuild and the nine course check and respond days. Preserve the paper routes and the supplied-data alternative to personal pulse measurement.

The nonlinear-inverse applying day is a sound contribution. I do **not** uphold the earlier suggestion that omitting the standard’s particular rational-function example automatically makes F-BF.B.4a incomplete: examples illustrate its demand, and the Functions Progression explicitly supports the planned cubing case. [Functions Progression, PDF page 13](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_functions_2013_07_02.pdf).

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Use existing days for the three function-comparison contributions | Completes the promised transfer without increasing the year | Algebra II frame and matching progression notes |
| Add a simple exponential equation-creation task in unit 2 | Satisfies the current owning row using earlier knowledge | Algebra II unit 2 |
| Make graphical and algebraic symmetry explicit | Both are required and already present in the base lessons | Algebra II unit 5 |
| Retain unit 2 as one unit | Its source sections form a coherent mathematical chain | Algebra II frame |
| Use the current lesson-credit template | Resolves conflicting instructions | Algebra II frame |
| Correct the shorter-option arithmetic to 152 | Those specified cuts remove eight days | Algebra II “For the lead” |
| Rewrite stitch item 20 as implemented | Current data and reconcile evidence agree | Mathematics stitch report |

## For Cory

- **Core scope:** confirm whether F-IF.C.7d remains required core content, as the progression proposes. Recommendation: retain it because the mapped rational-function lessons already support it without additional days.
- **Calendar scope:** retain the proposed 160-day year unless a shorter course is wanted. The listed alternative currently describes 152 days and still needs a content-loss judgment.

## Sources and limits

- [Mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): exact content requirements.
- [Functions Progression, 2013 draft](https://mathematicalmusings.org/wp-content/uploads/2013/07/ccss_progression_functions_2013_07_02.pdf): representations, transformations and the limits of inverse-function expectations.
- [High School Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): focus criterion and prerequisite table.
- [High School Review Criteria v2.0](https://cdn.edreports.org/media/2025/07/Math-HS-Review-Criteria_2.0.pdf): high school focus, full intent and coherence.
- [Base-text narrative](https://im.kendallhunt.com/HS/teachers/3/narrative.html) and [lesson alignments](https://im.kendallhunt.com/HS/teachers/3/lessons_and_standards.html): sequence and source commitments.
- [Fishtank Algebra II](https://www.fishtanklearning.org/curriculum/math/algebra-2/): comparison sequence. Its additional advanced content is not treated as a requirement here.
- [New York’s historical course overview](https://www.nysedregents.org/engageny/a-story-of-functions-curriculum-map-and-overview.pdf): a second comparison sequence, read as reference only.
- [Federal algebra practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/20): the public recommendations and evidence ratings, not a pacing prescription.

The compiled 2023 Progressions exceeded the web retrieval limit; the smaller 2013 Functions draft was read instead. The full federal guide timed out, so only its public recommendation summary was used. Classroom pacing and the quality of unwritten assessments remain untested.

No curricular finding rests on model memory. Prior workflow memory informed report structure only.

### For the source list

Add the reachable high school criteria links and the smaller Functions Progression fallback, with the portions read and the edition distinction.

**Verdict:** Sound structure; revise before unit writing. **Finding count:** 7. **Report path:** `docs/reviews/frame-algebra-ii-2026-11-14.md`, supplied here only.

