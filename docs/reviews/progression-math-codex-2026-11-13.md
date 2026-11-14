# Math progression cold read, 2026-11-13

**Verdict:** The progression is a credible backbone for core mathematics through Algebra II, but it needs corrections before writers treat every row as a complete teaching contract. Its biggest risk is that a valid standard code can conceal an unfinished expectation or an inaccurate mathematical statement. Correct those descriptions and completion claims first, while preserving the broadly sound grade placements.

**12 findings.** This report is supplied here for `docs/reviews/progression-math-codex-2026-11-13.md`. No file was created or changed.

## What I read and checked

| Material | Extent |
|---|---|
| `docs/agents/EXPERT.md`, `docs/agents/lenses/math.md`, `docs/RUBRIC-MATH-K8.md` | Full |
| `docs/FOUNDATION.md`, `docs/APPROACH.md`, `docs/APPROACH-MATH.md` | Foundation and teaching requirements |
| `docs/APPROACH-SOURCES.md` | Relevant source records, access notes and evidence notes |
| `docs/ROADMAP.md`, `docs/PRODUCTION-PATH.md`, `docs/agents/decisions/BASELINE.md`, `docs/GLOSSARY.md` | Applicable scope, review, terminology and production rules |
| `docs/sources/BASE-TEXTS.md` and the external base-text store’s `NOTES.md` | Edition, permissions and available material |
| `data/progressions/math.csv` | All **305 rows**, including every field |
| Four `data/progressions/parts/math-*-edges.md` files | Full |
| `data/progressions/math-excluded.csv` | All **49 exclusions** |
| `data/standards/ccss-math-standards.txt` | All **509 standard and substandard entries** |
| Math focus data | Calculated major-work row counts |
| Other subjects’ progression data | Resolved all **52 cross-subject references** in 48 math rows; read relevant partner descriptions |
| Base text | Unit sequences for all 12 core courses, dependency guidance and targeted lesson narratives |
| `data/courses.csv` | Core route and elective boundary |
| `docs/reviews/progression-math-reconcile-2026-11-13.md` | Read after recording the independent findings |

The assembled rows comprise K to 2: **74**; grades 3 to 5: **76**; grades 6 to 8: **73**; high school: **82**.

Reviewed `math.csv` SHA-256:

`36f1c01c43b2bb46465644b34323a7fd40c22e69df94380426a29030a0ea6e98`

I did not open earlier math course pages or their reviews. Consequently, **REPEAT** below means a precedent of that kind is documented in the permitted reconcile report. **New** means no precedent was identified there, rather than a claim that every prohibited earlier report was searched.

### Gate result

`python -X utf8 scripts/plan.py check` could not complete because `markdown` is unavailable.

The authorized fallback, `python -X utf8 scripts/progression.py check math`, reported:

- **305 rows, zero failures**
- **390 handoffs**, including **67** that skip intervening grades
- **12 model-grade gaps**, across seven models

The full repository gate remains unverified. I did not run turn acquisition, defect logging or other commands that would write.

## Findings, most serious first

### F01. Grade 5 scaling leaves part of its standard unstated

**LAYER: standard · REPEAT: yes · Confidence: firm**

**Skill:** `m5-scaling`, owning `5.NF.B.5b`.

The description explains how multiplication changes size, including multiplication by one. It does not connect that fact explicitly to generating equivalent fractions. The earlier grade 4 row correctly postpones that argument, so its destination must be unmistakable here.

A writer could teach every listed comparison and still omit this required explanation. Both the [standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf) and the [fractions progression](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf) establish the connection.

**Exact fix:** Append to `m5-scaling.notes`:

> Relate fraction equivalence to multiplication by one: for positive whole-number n, n/n = 1, so (a/b) × (n/n) = (na)/(nb), with the same value. Explain this using the fraction multiplication already taught in this grade, contrasting it with grade 4’s partitioning explanation.

### F02. Exponential comparison stops before the standard’s polynomial case

**LAYER: standard · REPEAT: yes · Confidence: likely**

**Skills:** `alg1-linear-vs-exponential`, `alg2-exponential-growth-rational-inputs`, `alg2-factors-zeros-graphs`.

`alg1-linear-vs-exponential` owns `F-LE.A.3`, but its description stops at linear and quadratic comparisons. No later row explicitly finishes the comparison with polynomial growth more generally.

This is a completion gap rather than a reason to teach general polynomials in Algebra I. The [standard](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf) includes that broader case.

**Proposed fix:**

- Change `F-LE.A.3` to `~F-LE.A.3` in `alg1-linear-vs-exponential`.
- Add ownership of `F-LE.A.3` to `alg2-exponential-growth-rational-inputs`.
- Append:

> After polynomial functions have been studied, use graphs and tables to compare an increasing exponential with polynomial functions beyond quadratics and observe eventual exponential dominance. No formal asymptotic proof is required.

This changes the stated completion grade and belongs with Cory.

### F03. Denominator zeros are described as automatic vertical asymptotes

**LAYER: progression · REPEAT: new · Confidence: firm**

**Skill:** `alg2-rational-functions`.

The instruction to graph “vertical asymptotes where the denominator is zero” is too broad. A canceled factor can instead produce a removable discontinuity. The row allows linear and quadratic parts and mentions holes, so the exception lies inside its stated territory.

This would produce incorrect graphs. The base text defines an asymptote using behavior near the excluded input, and the distinction is explicit in [rational-function guidance](https://openstax.org/books/precalculus-2e/pages/3-7-rational-functions). See also the [base lesson](https://im.kendallhunt.com/HS/teachers/3/2/17/preparation.html).

**Exact fix:** Replace the phrase with:

> Identify excluded inputs from the original denominator. Distinguish removable holes caused by canceled factors from vertical asymptotes, using simplification and behavior near the excluded input. Identify zeros only at inputs in the domain.

One contrast example is enough; this need not become an extended study of holes.

### F04. Tangent is swept into the amplitude instruction

**LAYER: progression · REPEAT: new · Confidence: firm**

**Skill:** `alg2-trig-functions-graphs`.

“Graph sine, cosine and tangent ... showing period, midline and amplitude” reads as applying all three features to all three functions. Tangent has no finite amplitude.

The [base tangent lesson](https://im.kendallhunt.com/HS/teachers/3/6/12/preparation.html) instead emphasizes period, domain and asymptotes. [Independent textbook guidance](https://openstax.org/books/precalculus-2e/pages/6-2-graphs-of-the-other-trigonometric-functions) makes the same mathematical distinction.

**Exact fix:** Replace the opening instruction with:

> Graph sine and cosine, showing amplitude, midline and period. Graph tangent, showing its period, zeros, excluded inputs and vertical asymptotes; tangent has no amplitude.

### F05. The no-solution equation form is wrong

**LAYER: standard · REPEAT: new · Confidence: likely**

**Skill:** `m8-linear-equations`.

The notes associate no solution with “x = a, a not b, as 3 = 5.” An equation `x = a` has one solution. The example and the named form contradict each other.

This could corrupt the central distinction students are learning.

**Exact fix:** Replace the classification clause with:

> Transform equations into forms that reveal one solution (x = a), no solution (a = b with a and b different, such as 3 = 5), or infinitely many solutions (a = a).

This follows `8.EE.C.7a` in the [standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf).

### F06. Grade 6 unit conversion does not explicitly finish unit reasoning

**LAYER: standard · REPEAT: yes · Confidence: likely**

**Skills:** `m6-unit-conversion`, `m6-unit-rate`.

The conversion row explains changing measurement units. It does not explicitly require interpreting and transforming units when quantities are multiplied or divided, the other demand of `6.RP.A.3d`.

A writer can satisfy the listed conversion examples without teaching that part.

**Exact fix:** Append to `m6-unit-conversion.notes`:

> Track units when quantities are multiplied or divided: for example, 12 miles ÷ 3 hours gives 4 miles per hour, and 4 miles per hour × 2 hours gives 8 miles. Explain the resulting unit and why it fits the quantity.

Keep the existing limit against complicated area-unit conversions. The additional expectation is ordinary unit reasoning, as required by the [standard](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf).

### F07. Parent codes conceal exclusions and inconsistent completion ownership

**LAYER: process · REPEAT: yes · Confidence: firm**

**Skills:** `alg1-inverse-functions`, `alg1-quadratic-forms-graphs`, `alg2-combining-functions-models`, `alg2-exponential-growth-rational-inputs`.

Four lettered codes have neither an explicit owning row nor an entry in the exclusion file:

| Code | Expectation |
|---|---|
| `F-BF.A.1c` | Function composition |
| `F-BF.B.4b` | Verify inverses by composition |
| `F-BF.B.4c` | Read inverse values from graphs or tables |
| `F-BF.B.4d` | Restrict a domain to obtain an inverse |

The gate accepts their parent codes as coverage, although the notes explicitly exclude these advanced topics.

Separately, `F-IF.C.8` is owned in grade 9 while its exponential part, `F-IF.C.8b`, is completed in grade 11. That conflicts with the reconcile report’s stated rule that ownership identifies completion.

**Exact fixes:**

1. Add the four advanced codes to `math-excluded.csv`, with reasons stating that they are **deferred from the core progression and require elective allocation**.
2. Change `F-IF.C.8` to `~F-IF.C.8` in `alg1-quadratic-forms-graphs`; add ownership of the parent to `alg2-exponential-growth-rational-inputs`. Keep `F-IF.C.8a` in grade 9.
3. Make the gate require an explicit disposition for lettered parts beneath an owned parent.

I disagree with reconcile item 41 only about treating a parent tag as evidence of complete coverage. The quadratic work stays in Algebra I.

### F08. Grade 2 consumes the number-line model before its named introduction

**LAYER: base text · REPEAT: new · Confidence: firm**

**Skills:** `m2-line-plots`, `m2-number-line`, `m2-count-skip-1000`.

`m2-line-plots` takes `number-line` as an incoming model while citing unit 3. The named introduction is unit 4. The gate permits a same-grade introduction anywhere, so it cannot establish this order.

The base text deliberately builds from ruler and line-plot scales toward the abstract number line. Its [unit 3 lesson](https://im.kendallhunt.com/k5/teachers/grade-2/unit-3/lesson-16/preparation.html) explicitly anticipates that later learning; [unit 4 introduces the number line](https://im.kendallhunt.com/k5/teachers/grade-2/unit-4/lesson-1/preparation.html).

**Exact fixes:**

- `m2-line-plots.model_in`: empty.
- `m2-line-plots.model_out`: `dot-plot`.
- Add: “Build the measurement scale from iterated ruler units; this prepares the abstract number-line introduction in unit 4.”
- In `m2-count-skip-1000.notes`, state that number-line representations begin after `m2-number-line`; earlier counting routines remain oral or use objects and place-value representations.

### F09. Some prerequisite fields omit the mathematics they actually need

**LAYER: progression · REPEAT: yes · Confidence: likely**

**Skills:** `alg2-polynomial-arithmetic`, `alg1-quadratic-forms-graphs`, `geo-volume-formulas`, `m7-chance-probability`, `m7-probability-models`, `m7-compound-events`, `m6-percent`.

Two concrete problems remain:

| Row | Problem | Exact correction |
|---|---|---|
| `alg2-polynomial-arithmetic` | Its only earlier-grade prerequisite is volume formulas, a useful context rather than the algebra needed to operate on polynomials | Replace `assumes` with `alg1-quadratic-forms-graphs`. Update both reciprocal handoffs. Retain volume in the notes as an application |
| Three grade 7 probability rows | All have empty `assumes`, although the first row explicitly says earlier fraction, decimal and percent knowledge is required | Add `m6-percent` to each `assumes`; append all three targets to `m6-percent.hands_on` |

Add a note that multiplying binomials and using distributivity in Algebra I are generalized to polynomials. The [base course’s dependency guidance](https://im.kendallhunt.com/MS/teachers/1/scope_and_sequence.html) supports recording mathematical dependencies rather than simply nearby contexts.

### F10. The historical-date cross-link needs its zero-point limit

**LAYER: progression · REPEAT: new · Confidence: likely**

**Skill:** `m6-negative-numbers`; partner: `ss6-timeline-deep-time`.

The math cross-reference describes dates on either side of a zero point. The partner row correctly warns that historical BCE/CE numbering has **no year zero**. Without that qualification in math, a writer may treat historical year labels as ordinary signed coordinates and obtain incorrect elapsed times.

The distinction is verified in [year-dating guidance](https://eclipse.gsfc.nasa.gov/help/dates.html).

**Exact fix:** Change the cross-reference description to:

> social-studies:ss6-timeline-deep-time (ordering earlier and later dates; historical BCE/CE labels have no year zero)

Append to the math notes:

> For signed elapsed time, choose and label a reference event as zero. Do not substitute negative BCE labels into ordinary integer subtraction without explaining the calendar convention.

### F11. Explained gaps still need a consistent re-entry rule

**LAYER: progression · REPEAT: yes · Confidence: likely**

**Skills:** The 67 skipped handoffs reported by the gate, especially `m4-symmetry` → `m8-rigid-motions`, `m7-random-samples` → `alg2-sample-estimates-margin`, and the grade 9 to 11 algebra handoffs.

Most notes explain **why no intervening standard extends the topic**. That does not consistently say whether the returning course assumes fluent recall, supplies a reminder or reteaches the idea. Several grade 4 rows do specify readiness checks; preserve that stronger treatment.

| Source grade → target grade | Skipped handoffs |
|---|---:|
| 2 → 4 | 5 |
| 3 → 5 | 1 |
| 3 → 6 | 1 |
| 4 → 6 | 1 |
| 4 → 7 | 3 |
| 4 → 8 | 1 |
| 5 → 7 | 2 |
| 6 → 8 | 2 |
| 6 → 9 | 1 |
| 7 → 9 | 5 |
| 7 → 10 | 5 |
| 7 → 11 | 1 |
| 8 → 10 | 20 |
| 9 → 11 | 19 |
| **Total** | **67** |

The model gaps are:

| Model | Intervening grades without a recorded use |
|---|---|
| `box-plot` | 8 |
| `dot-plot` | 8, 10 |
| `histogram` | 7, 8, 10 |
| `ratio-table` | 8, 9 |
| `scatter-plot` | 10 |
| `tape-diagram` | 8 |
| `tree-diagram` | 8, 9 |

**Exact fix:** For every returning target lacking a re-entry instruction, append one of these dispositions:

- **Recall required:** identify the earlier skill and a readiness check, with the response to a missed check.
- **Revisited:** state that the returning course rebuilds the idea before using it.

For example, append to `m8-rigid-motions.notes`:

> Revisit line symmetry by folding or reflecting one figure before using the grade 4 handoff; fluent recall after the intervening grades is not assumed.

Append an equivalent sampling re-entry instruction to `alg2-sample-estimates-margin`.

These gaps do **not** justify moving standards or inventing a geometry unit in Algebra I. The [high-school criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf) permit course sequences while requiring their coherence.

### F12. The grade 4 remainder example uses a two-digit divisor

**LAYER: standard · REPEAT: yes · Confidence: likely**

**Skill:** `m4-divide-multidigit`.

The rejected notation example is `84 / 10 = 8 R 4`, although the row’s divisor limit is one digit. The identity preceding it is mathematically correct, but the example gives the writer an unnecessary out-of-limit anchor.

**Exact fix:** Keep `84 = 8 × 10 + 4`, identify the divisor as **8**, and change the rejected form to:

> Do not write 84 / 8 = 10 R 4 as an equality.

This preserves the intended lesson about notation and stays within `4.NBT.B.6`.

## Coverage, ownership, words and cross-subject conclusions

**Coverage:** No K to 8 standard is wholly absent under the gate’s parent-and-child coverage rules. No row has a blank standard field. The semantic omissions are F01, F02 and F06; the four advanced parts lacking explicit disposition are listed in F07.

**Ownership:** K to 8 placements are appropriate. The high-school allocation broadly follows the base text. Preserve polynomial arithmetic, rational exponents, sequences, logarithms, complex solutions and inference in Algebra II. F02 and F07 concern completion claims, rather than a wholesale course rearrangement.

**Prerequisite timing:** Every recorded `assumes` reference names an existing earlier-grade skill. No recorded assumption points to a skill first taught in a later grade. This structural success does not settle whether the prerequisite is sufficient or well chosen, as F09 illustrates.

**Words:** The vocabulary inventory is generally appropriate by grade, including informal language before formal terminology. It cannot by itself prove that a word is taught before its first use within the year. Two minor stitching corrections are settled below; student reading demand requires actual student material.

**Cross-subject links:** All 52 references resolve to a partner skill taught or begun at or before the math grade, including parent-code resolution for the kindergarten language links. No future-grade-only link was found. Same-grade availability is not a calendar guarantee: grade 6 science’s early investigation work and late-year math statistics still need coordination or supplied scaffolds when their course frames are written.

## Pace through the grades

The major-work column counts rows naming a major cluster, including contributing codes. It does not weight time or credit supporting rows that practise major work.

| Grade | Skills | Direct major-work rows |
|---|---:|---:|
| K | 20 | 15 |
| 1 | 26 | 21 |
| 2 | 28 | 19 |
| 3 | 24 | 16 |
| 4 | 27 | 16 |
| 5 | 25 | 19 |
| 6 | 26 | 18 |
| 7 | 23 | 13 |
| 8 | 24 | 19 |
| 9 | 28 | Not the K to 8 measure |
| 10 | 28 | Not the K to 8 measure |
| 11 | 26 | Not the K to 8 measure |
| 12 | 0 | Electives outside this core file |

No grade is demonstrably overloaded from these counts alone. The range is 20 to 28 rows, and the highest grades are not dramatically above both neighbors.

Grades **2, 4 and 7** particularly need weighted checks when days and minutes exist. Their raw major-work row proportions are about 68, 59 and 57 percent. These are **not failures against a time threshold**: the [evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf) requires examination of implemented emphasis from multiple perspectives.

The principal stop-and-return patterns are:

- One-variable data displays pause during grade 8’s bivariate work.
- Probability returns in Geometry after grade 7.
- Sampling inference returns in Algebra II after grade 7.
- Algebra and functions have 22 strand-labelled rows in grade 9, zero in grade 10 and 20 in grade 11. Geometry still uses algebra and functions; the labels must not be read as a year without them.
- Fractions continue into rational-number work despite the strand-name change.

## Progression-layer lens checklist

| Lens line | Status | Evidence or disposition |
|---|---|---|
| Unique ownership at the appropriate depth | **Missed** | Structural ownership passes; completion descriptions need F02 and F07 |
| Handoffs do not silently skip grades | **Missed** | 67 disclosed exceptions; re-entry treatment is inconsistent |
| Models introduced before use | **Missed** | F08 |
| Standard algorithms expected at the proper fluency grade | **Met** | Addition/subtraction 4, multiplication 5, division 6 |
| Number and content limits preserved | **Missed** | F12; broad fraction and operation limits otherwise sound |
| Major-work emphasis | **Not applicable to final judgment here** | Counts supplied; days and time are absent |
| Supporting work practises major work | **Met at progression level** | Graphs, line plots, measurement and geometry connections are usually explicit |
| Every source-map lesson has a disposition | **Not applicable** | Course-frame layer |
| No standard taught only in part | **Missed** | F01, F02, F06 |
| Problems deliberately join units | **Not applicable** | Scope and sequence and task evidence required |
| Fluency receives spaced, mixed practice | **Met as a stated requirement** | Repeated in the relevant fluency rows; delivery unverified |
| Practices tied to actual tasks | **Not applicable** | Unit and day evidence required |
| Balance of understanding, fluency and application | **Not applicable** | Cannot judge balance from skill counts |
| Assessment coverage and item labels | **Not applicable** | Assessment layer |
| Exit ticket matches the goal | **Not applicable** | Day layer |
| Manipulative tied to written method | **Met as a stated requirement** | Strong place-value, fraction and algorithm descriptions |
| No student countdown timer | **Met as a stated requirement** | Explicit throughout fluency notes |
| High-school bar available | **Missed locally** | External high-school criteria consulted; local K to 8 rubric does not cover these courses |
| Handoff work beyond grades 3 to 5 | **Met** | The assembled progression and band notes now supply it |
| Sources and progression past Algebra II | **Not applicable to core file** | Still required before elective planning |
| K to 2 fluency checked without a visible timer | **Not applicable to demonstrated performance** | Practice policy exists; checking procedure remains to be written |

## What is right and should stay

- The progression treats fractions as numbers and carries number-line reasoning into signed numbers.
- Algorithm fluency years and the preceding strategy work are correctly distinguished.
- Grade 3 and 4 fraction limits are unusually explicit.
- The reconciled notes preserve important qualifications about mixed numbers, unlike denominators, comparison language and remainder notation.
- High-school modeling, proof and simulation are substantive expectations.
- The core high-school route follows a coherent base rather than a collection of isolated topic placements.

## Settled by the expert

These are proposed applications for the caller. Nothing was edited.

| Choice | Reason | File or row |
|---|---|---|
| Use divisor 8 and quotient 10 in the remainder example | Preserves the existing identity and grade limit | `math.csv`, `m4-divide-multidigit` |
| Use `a = b`, with different constants, for the no-solution form | Removes a mathematical contradiction | `math.csv`, `m8-linear-equations` |
| Preserve grade 4’s partitioning explanation; add multiplication-by-one equivalence in grade 5 | Respects the fraction progression | `math.csv`, `m5-scaling` |
| Distinguish tangent’s features from sine and cosine | Prevents an amplitude error | `math.csv`, `alg2-trig-functions-graphs` |
| Change “right angle may be new” to “revisit the grade 3 right-angle language” | `m3-quadrilaterals.words` already includes it | `math.csv`, `m4-angle-concepts` |
| Change grade 6 “introduces the function-table” to “extends the grade 5 function-table” | Matches `model_in` and `m5-two-patterns` | `math.csv`, `m6-dependent-variables` |
| Correct the high-school edge note’s Algebra I to Algebra II handoff count from 18 to 19 | Matches the assembled data | `parts/math-hs-edges.md` |
| Preserve the standard core route | Elective and accelerated routes require separate planning | No ownership relocation beyond the identified completion corrections |

## For Cory

- **Content completion:** F01 and F06 restore expectations already required by their standards. F02 proposes finishing exponential-versus-polynomial comparison in grade 11 and changing its completion ownership.
- **Continuity:** Decide any added teaching time or movement between units needed to resolve F11. Readiness checks and brief reminders can usually address it without changing grade ownership.
- **Later scope:** Elective standards need actual allocation and named sources. The existing exclusions should say “deferred,” rather than promise that unplanned electives teach them. Accelerated placement and the high-school review bar also remain course-frame decisions.

## Limits of this read

I could not judge enacted pacing, assessment completeness, student readability or fluency performance from this file. No classroom outcome is claimed.

The 333-page compiled Progressions PDF exceeded the web tool’s fetch limit, and direct network access from the read-only environment was blocked. I used accessible domain drafts and current repository text; I did not independently reverify every compiled-page pointer in the notes.

No finding rests on unverified personal memory.

## Outside sources

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): checked against the local standard text for content demands and boundaries.
- [Fractions progression](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf): equivalence, multiplication and grade handoffs.
- [Counting and operations progression](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf): early number and operation development.
- [Progressions index](https://archive.math.arizona.edu/ime/progressions/): authoritative route to accessible domain documents.
- [K to 8 publishers’ criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): coherence, focus and rigor.
- [High-school publishers’ criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_HS_Spring_2013_FINAL.pdf): course coherence, prerequisite emphasis and modeling.
- [K to 8 evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): major-work measurement and limits of row counting.
- [Base-text scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-5/course-guide/scope-and-sequence.html): grade and unit placement, supplemented by the archived sequences for all core courses.
- [Second curriculum’s overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf): an independent comparison of elementary order and fluency years.
- [Additional grade 5 sequence](https://www.fishtanklearning.org/curriculum/math/5th-grade/) and [Algebra II sequence](https://www.fishtanklearning.org/curriculum/math/algebra-2/): comparison of development across units, without importing their additional scope.
- [Federal mathematics practice-guide summary](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/WWC-PraxGuide-Elementary-Math-Summary-508c.pdf): language, representations and instructional support; its intervention setting limits generalization.
- [Rational functions](https://openstax.org/books/precalculus-2e/pages/3-7-rational-functions), [tangent graphs](https://openstax.org/books/precalculus-2e/pages/6-2-graphs-of-the-other-trigonometric-functions), and [year-dating conventions](https://eclipse.gsfc.nasa.gov/help/dates.html): verification of the specific mathematical and calendar distinctions.

### For the source list

Add the working high-school criteria address, the archived Progressions index and accessible draft addresses, and the three specific verification pages on rational functions, tangent and year dating. Record the compiled PDF’s size limitation for this environment. No source-list file was changed.

**Final verdict: revise before authoritative use. Finding count: 12. Report path: `docs/reviews/progression-math-codex-2026-11-13.md`, supplied here, not written.**