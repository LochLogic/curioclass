# Expert cold read: Math Grade 4 course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-math-grade-4-2026-11-14.md`  
**Delivery:** Complete report supplied inline. No files changed.

## Verdict

The frame is sound in its planned coverage and progression, with all 27 owned skills placed once and no missing Grade 4 standard obligation identified. Its biggest risk is pacing: five pairs of base lessons are compressed without specifying what survives, and the measurement unit’s number restriction conflicts with lessons it keeps. Clarify those teaching directions before using the frame to write the scope and sequence; the unavailable full gate does not prevent this verdict under the updated brief.

## What I read and checked

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, FOUNDATION, the shared and mathematics approaches, and relevant ROADMAP and BASELINE sections.
- The complete Grade 4 frame, its `frames.csv` row, all 27 Grade 4 progression rows, and the Grade 4 standards text.
- The Grade 3 and Grade 5 frames, including their units, models, handoffs and source maps.
- The same-grade ELA, science and social studies frames where dependencies touch mathematics.
- The source policy, the 149-lesson base inventory, and selected source lessons, particularly measurement and the proposed merges.
- Relevant earlier reviews: the Grade 4 spine review, progression reconciliation and stitch, Grade 3 frame review, and earlier Grade 4 frame report.
- Existing Grade 4 planning and lesson files where needed to verify stale statements.

The requested `data/plans/math-grade-4/source-map.csv` does not exist. I reviewed the frame’s complete inline map instead. The older `data/plans/math-4/source-map.csv` contains 23 rows for the earlier course structure; it is not a complete map for this new frame.

| Required command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check math-grade-4` | Passed, zero failures: 9 units, 160 days, 145 within units and 15 at course level. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files checked, zero marked-note failures. |

No turn mutation, installation, defect-ledger write or report-file write was performed.

## Findings, most serious first

### 1. The measurement number rule excludes conversions the unit keeps

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, measurement prerequisites and number restrictions were raised in the earlier Grade 4 spine review, finding 3.  
**Confidence:** firm

**Location:** Grade 4 frame, unit 6, “Why this unit, here.”

**What is wrong:** The unit restricts numbers to facts and multiples of 10, 100 and 1,000. Its retained source lessons include pounds-to-ounces conversions, which require multiples of 16, and customary length work involving 12. The source explicitly supports repeated addition for the pounds-to-ounces table. [Base lesson 5.11](https://im.kendallhunt.com/k5/teachers/grade-4/unit-5/lesson-11/lesson.html)

**Why it matters:** A writer following the restriction literally must discard retained conversion work or introduce a method that the frame has not authorized before unit 7.

**Exact fix:** Replace the restriction with:

> Before unit 7, use known facts, repeated addition and previously learned break-apart strategies. Conversions by 12 and 16 are included, with small whole-number amounts and the method shown explicitly. Multiplication by 10, 100 and 1,000 uses place value. General multi-digit multiplication methods are taught in unit 7.

Keep unit 6 in its present position. This resolves the conflict without moving a standard.

### 2. Five merged lesson pairs have no retained-activity budget

**Severity:** Serious  
**LAYER:** base text  
**REPEAT:** yes, Grade 3 frame review, finding 3.  
**Confidence:** firm on the missing budget; activity selection is a judgment call

**Location:** Source-map rows for base units 4.7 and 4.9.

**What is wrong:** The frame merges 7.1 with 7.2, 7.3 with 7.4, 7.14 with 7.15, 9.1 with 9.2, and 9.7 with 9.8. These are substantial lessons with separate activities and syntheses. For example, 7.1 alone lists a five-minute opening and activities of 25 and 15 minutes, before its lesson synthesis. [Base lesson 7.1](https://im.kendallhunt.com/k5/teachers/grade-4/unit-7/lesson-1/lesson.html)

**Why it matters:** The 21-day geometry allocation and seven-day review depend on these savings. “Merged” without a selection rule can produce overfull days or omit essential drawing and reasoning.

**Exact fix:** Add a retained-activity specification for each pair. Use one opening, selected activities totaling no more than 45 minutes, one synthesis and one exit ticket. The selections under “Settled by the expert” give a concrete starting point. Require the day-level map to identify omitted tasks and preserve every claimed mathematical goal.

Do not add days or move standards at this stage.

### 3. Cross-subject bridges disagree with the frames now available

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, Grade 3 frame review, finding 1.  
**Confidence:** firm

**Location:** Grade 4 frame, Cross-subject introduction and science supply rows.

**What is wrong:** The introduction says the receiving frames “are written later,” although they exist. The mathematics frame supplies a conversion table to science and says science names points and line segments. The science frame instead specifies one measurement unit with no conversion, and wave descriptions using peaks, troughs and distances in whole centimetres.

**Why it matters:** Writers receive two different instructions for the same early-year bridge.

**Exact fix:**

- Replace the introduction with: “The receiving Grade 4 frames are written; the bridges below match their current directions.”
- For weathering and erosion: “Science measures in one unit only, centimetres or millilitres, with no conversion.”
- For wave models: “Science names peaks, troughs and the distance between peaks, measured in whole centimetres; formal point and line-segment terminology waits for mathematics.”
- Replace the science patterns row’s conditional wording with the actual timing: science unit 3 precedes mathematics unit 7, so science states and follows the code rule without requiring explanations of unstated pattern features.

### 4. The major-work time claim contradicts the stated fluency sequence

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, the earlier Grade 4 spine review distinguished prior-grade maintenance from Grade 4 fluency.  
**Confidence:** firm on the wording conflict; the final minute share remains unverified

**Location:** “Major work” and “Fluency” bullets.

**What is wrong:** The frame says the addition and subtraction algorithm is practised “all year” when explaining why the time share is higher. It correctly says elsewhere that the algorithm is taught in unit 5 and maintained afterward. It also calls six units “outright” major work, although unit 7 contains four base lessons on the additional patterns standard.

**Why it matters:** This can direct premature algorithm practice and makes the claimed time calculation difficult to reproduce.

**Exact fix:** Change “outright” to “predominantly.” Replace the time explanation with:

> Grade 3 facts are maintained from the beginning. The Grade 4 addition and subtraction algorithm enters warm-ups after unit 5. The scope and sequence will verify the major-work share in minutes, including documented connections from supporting work.

Retain the approximate day estimate as provisional. The evidence guide permits connected supporting work in the calculation, but requires the perspectives and allocations to be explained. [Mathematics evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf)

### 5. “Split” describes a warm-up reuse outside its defined meaning

**Severity:** Minor  
**LAYER:** base text  
**REPEAT:** yes, Grade 3 frame review, finding 4.  
**Confidence:** firm

**Location:** Source-map row for base lessons 9.10 to 9.12.

**What is wrong:** The frame defines “split” as one base unit becoming two units. This row instead removes standalone lesson days and reuses routines in warm-ups.

**Why it matters:** The map’s decision vocabulary becomes inconsistent just where the future day-level map needs clear instructions.

**Exact fix:** Change the decision to **cut** and the note to:

> Cut as standalone lesson days. Selected estimation, classification and mental-computation routines are reused in warm-ups, with their locations recorded in the day-level map.

### 6. Current planning headers still say nothing has been built

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes are a recurring finding in earlier frame reads.  
**Confidence:** firm

**Locations:**

| Files | Stale statement |
|---|---|
| `docs/courses/math-4-spine.md:4` | “Nothing here is built or public.” |
| `docs/courses/math-4-spine.md:83` | The current-status paragraph says there is “no section” and treats every day as a gap. |
| `docs/courses/math-4/s01.md`, `s02.md`, `s03.md`, `s04.md`, `s10.md`, `s11.md` | Headers say nothing is built. |
| `docs/courses/math-4/u01-1.md`, `u01-2.md`, `u03-1.md`, `u03-2.md`, `u03-3.md`, `u03-4.md`, `u04-1.md`, `u09-1.md`, `u10-1.md`, `u10-2.md`, `u10-3.md` | Headers say nothing is built. |

**What is wrong:** There are 48 draft day files under `courses/math-4/`, alongside section plans and rendered outputs.

**Why it matters:** These notes conceal existing work and can trigger duplicate production. They also blur the distinction between drafted material and material tried with students.

**Exact fix:** Replace the affected headers with:

> Draft lesson files exist for this unit or section. Their readiness and teaching status follow the individual file headers.

For unit 4, specify that day drafts currently cover days 25 to 28. Replace the spine’s “no section” paragraph with:

> Unit and section plans exist for units 1, 2, 3, 4, 9, 10 and 11, with 48 draft day files across parts of the earlier course structure. Remaining days are still gaps. This does not establish classroom use or publication.

The start-of-year check remains unwritten, so its pending notes should stay.

### 7. The rubric’s current-gap descriptions ignore documented pilot work

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale planning status.  
**Confidence:** firm

**Location:** `docs/RUBRIC-MATH-K8.md:33` to its teacher and student support rows.

**What is wrong:** The table says no unit names a practice and nothing checks unit balance. It also lists family notes, supplies and several student supports as absent without acknowledging existing pilot documentation.

The pilot plan names practices and tasks, totals day kinds, includes supplies and a family note, and specifies an extension. Its assessment day includes accommodations and response groups.

**Why it matters:** An expert using the bar as instructed receives an inaccurate account of what remains to be produced.

**Exact fix:** Mark the original gaps as identified on 2026-11-11, then replace the current-status cells with:

> Documented in the Grade 4 pilot planning and draft materials. Whole-course implementation and verification remain open.

Use separate status entries for practices, balance, assessment guidance, family materials and student supports. Do not mark the whole course complete.

### 8. The earlier Grade 4 report retains a superseded gate-blocking instruction

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale review status.  
**Confidence:** firm

**Location:** `docs/reviews/frame-math-grade-4-codex-2026-11-14.md`, Verdict and finding 1.

**What is wrong:** It directs a fresh read only after the full gate passes and withholds all curricular judgment. The updated brief explicitly requires the substantive read despite this environment failure, and that read is now supplied here.

**Why it matters:** The review desk could continue to treat the course as awaiting an independent read.

**Exact fix:** Add a prominent status note:

> Superseded by the completed independent Grade 4 frame review of 2026-11-14. The full plan gate remains unavailable in this sandbox; the structural check passes. Use the completed review for the curricular verdict and findings.

Preserve the earlier runtime error as historical evidence.

## Coverage, sequence and days

| Requirement | Judgment |
|---|---|
| Owned skills | Met. All 27 placed exactly once; no foreign-grade skill appears as an owner. |
| Standards in full | Met at frame level. All 34 leaf obligations, including lettered parts, have a teaching placement. |
| Unit reasons and prerequisites | Sound overall. Equivalence precedes fraction operations; place value precedes multi-digit computation; lines and rays precede angle measurement. Finding 1 concerns the measurement number rule. |
| Source mapping | All 149 base lessons are accounted for inline. Order is preserved, departures are explained, and no prohibited reference source is mapped. Findings 2 and 5 concern execution directions. |
| Grade 3 seam | Picked up, including fractions on number lines, facts, area models and the named Grade 2 re-entry checks. |
| Grade 5 seam | Matches the receiving frame: partial products, partial quotients, fraction operations, decimals, conversion and classification. |
| Cross-subject timing | Local bridges are necessary. ELA opinion writing arrives after mathematics unit 2; the spoken reason and sentence frame are appropriate. Science bridges need the corrections in finding 3. |

| Unit | Days | Lesson days after assessment and response | Owned skills |
|---|---:|---:|---:|
| 1 | 8 | 6 | 1 |
| 2 | 18 | 16 | 2 |
| 3 | 19 | 17 | 4 |
| 4 | 11 | 9 | 2 |
| 5 | 19 | 17 | 4 |
| 6 | 19 | 17 | 3 |
| 7 | 15 | 13 | 2 |
| 8 | 15 | 13 | 3 |
| 9 | 21 | 19 | 6 |

The allocation is reasonable by instructional load. Unit 3’s three added days address distinct needs; units 7 and 8 each add a targeted day. Geometry’s 21 days are defensible if the merges are specified.

The year totals **122 retained base lesson days + 5 original days + 18 unit assessment/respond days + 15 course-level days = 160**. This leaves 20 days within a 180-day calendar. No unit is demonstrably far over or under its share.

## Mathematics lens checklist

| Course-frame checklist line | Result |
|---|---|
| Major work meets the line by units | **Met:** six predominantly major units of nine, about 67 percent. |
| Major work meets the line by days | **Met provisionally:** the approximately 107-day estimate is credible with explicit supporting-work connections. |
| Major work meets the line by time | **Missed:** the higher-time assertion is unsupported; finding 4 supplies the correction. |
| Supporting clusters practise major work | **Met:** factors support equivalence, line plots use fraction operations, and measurement uses multiplicative comparison. |
| Every source-map row has a defined decision | **Missed in meaning:** every row has a label, but the warm-up “split” conflicts with its definition. |
| Practices have course placements | **Met:** all eight are named across units; task-level verification belongs below the frame. |
| High-school bar and beyond-Algebra-2 provisions | **Not applicable.** |

## Settled by the expert

These are recommendations for the caller to apply, not edits made during this read.

| Choice | Reason | File affected |
|---|---|---|
| Keep the nine units and their order | The progression is coherent; no standard move is needed | Grade 4 frame |
| Permit small conversions by 12 and 16 through repeated addition and break-apart reasoning | Resolves the number-rule conflict using earlier learning | Frame, unit 6 |
| For merge 7.1/7.2, retain a shortened describe-and-draw task, the vocabulary sort and selected drawing tasks | Preserve both recognition and construction | Frame source-map note |
| For merge 7.3/7.4, retain the parallel/intersecting-line investigations and selected drawing | Preserve identification and drawing | Frame source-map note |
| For merge 7.14/7.15, retain clock-angle construction, shaded-angle reasoning and selected unknown-angle exchanges | Preserve construction and additive reasoning | Frame source-map note |
| For merge 9.1/9.2, select fraction multiplication, addition and subtraction tasks within the activity cap | Keep all intended operations represented | Frame source-map note |
| For merge 9.7/9.8, retain comparison and remainder-interpretation problems | Preserve the distinct purposes of the pair | Frame source-map note |
| Keep patterns owned by unit 7 | The early counting-pattern warm-up is a preliminary encounter, already acknowledged in the frame | Frame and future source map |
| Keep the inclusive trapezoid convention | Grade 5 explicitly continues it | No change needed |

The proposed activity selections require a timed rehearsal when the actual days are written.

## What is right and should not be touched

Keep the fractions-first order, the explanation of equivalence through partitioning, the separation of decimal notation from decimal computation, and the model-based multiplication and division handoff. These fit the standards and the fraction progression. [Official standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf), [Fractions progression](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf)

Keep the number line across fraction and decimal work. The federal fractions guide supports that instructional choice, with a moderate evidence rating. [Federal fractions guidance](https://ies.ed.gov/ncee/WWC/PracticeGuide/15/Published)

The explicit added days for mixed-number subtraction, incompatible wholes, measured line-plot data and division zeros should remain.

## Limits and outside sources

This review establishes planned coverage and coherence, not delivered lesson quality or classroom feasibility. The new course’s source-map CSV, detailed minute allocation and completed merged lessons remain unavailable.

The compiled 2023 Progressions exceeded the web tool’s size limit. I checked the accessible 2018 fractions progression directly and used repository page references for other compiled-progression details. Those unreopened details are repository-derived, not independently verified against the compiled PDF.

No curricular conclusion rests on unaided memory. Prior-run memory informed only the strict-scope review workflow.

Sources used:

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): Grade 4 obligations and limits.
- [Fractions progression, 2018](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf): equivalence, operations and decimals.
- [K-8 Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus and coherence.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): major-work calculation.
- [Base curriculum scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-4/course-guide/scope-and-sequence.html): order and unit structure.
- [Comparison curriculum map](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum%20Map/EM_GPK5_CurriculumMap.pdf): an alternative Grade 4 sequence, not material for adaptation.
- [Federal fractions guidance](https://ies.ed.gov/ncee/WWC/PracticeGuide/15/Published): number-line instruction.

### For the source list

Add the accessible 2018 fractions-progression address above as a smaller fallback. Label its edition clearly; its page numbers must not be substituted for the compiled edition’s pointers.

## For Cory

- Confirm the existing audience assumption of **160 teaching days with approximately 60-minute mathematics blocks**. A shorter-block path remains work for the scope and sequence.
- No new money, outside-person or standard-placement decision is requested.

**Verdict:** Sound coverage and progression; revise pacing directions before handoff. **Finding count:** 8. **Report path:** `docs/reviews/frame-math-grade-4-2026-11-14.md`, supplied inline, not written.

