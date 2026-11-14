# Independent course-frame review: Math Grade 5

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-math-grade-5-2026-11-14.md`  
Supplied here in full. No files were created or changed.

## Verdict

The frame is mathematically sound in its overall coverage, sequence and allocation, with corrections needed before it becomes the writing contract. The biggest instructional risk is compressing four complete review lessons into two days without identifying what survives; MP5 also has no planned home. Specify those selections and the missing practice, then correct the reader requirement, source references and stale notes while retaining the unit order and 160-day total.

## What I read and checked

- The expert instructions, mathematics lens, mathematics rubric, foundation, shared and mathematics approaches, relevant source records and evidence notes, applicable roadmap sections, BASELINE rules 20 to 24, glossary, and plan-data guidance.
- The complete Grade 5 frame, its `frames.csv` row, all 25 Grade 5 progression rows, relevant adjoining progression rows, and the Grade 5 standards including lettered parts.
- The Grade 4 and Grade 6 mathematics frames; Grade 5 science and social studies frames; relevant Grade 5 ELA framing.
- The base text’s lesson inventory, standards alignment, pacing guidance, and targeted lesson narratives, including the proposed review merges.
- Earlier mathematics progression reviews and fixes, the earlier Grade 5 report, neighboring frame reports, and the Grade 4 worked planning pattern.

The requested `data/plans/math-grade-5/source-map.csv` does not exist. The frame supplies an inline map and explicitly defers the day-level CSV to the scope and sequence, consistent with the frame-writing brief. Its absence is not counted as a finding.

**Gates:** `plan.py check` could not finish because Python lacks `markdown`; `frame.py check math-grade-5` passed with zero failures; `stale.py check` passed across 56 files with zero failures.

This substantive verdict follows the caller’s explicit fallback instruction. It supersedes the earlier Grade 5 report’s recommendation to withhold judgment over the missing dependency.

## Findings, most serious first

### 1. The review merges lack a usable selection rule

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** yes, Grade 3 mathematics frame review, finding 3  
**Confidence:** firm

**Location:** Grade 5 frame, source-map row for base unit 5.8, line 215.

**What is wrong:** Lessons 1 and 2 become one day, as do lessons 7 and 8, but the map identifies no retained activities. The published timelines total 120 minutes for the first pair and 115 for the second, before adapting their exit tickets. These become two 60-minute days. [Lesson 1](https://im.kendallhunt.com/k5/teachers/grade-5/unit-8/lesson-1/preparation.html), [lesson 2](https://im.kendallhunt.com/k5/teachers/grade-5/unit-8/lesson-2/preparation.html), [lesson 7](https://im.kendallhunt.com/k5/teachers/grade-5/unit-8/lesson-7/preparation.html), [lesson 8](https://im.kendallhunt.com/k5/teachers/grade-5/unit-8/lesson-8/preparation.html).

**Why it matters:** A writer can preserve the stated count only by making unrecorded cuts or producing overfull days. The multiplication pair contains different work, digit placement and errors involving zeros. The volume pair moves from estimation to calculation.

**Exact fix:** Keep seven review days and add this selection rule to the source-map note:

> Merged multiplication day: retain lesson 1 activity 1 and lesson 2 activity 1, with one warm-up, a shared synthesis and our exit ticket. Merged volume day: retain lesson 7 activity 1, followed by lesson 8 activities 1 and 2, with one brief opening, a shared synthesis and our exit ticket. Omit the other activities and record those omissions in the day-level source map. Each day must fit 60 minutes.

This retains the purposes of both merges without adding days.

### 2. MP5 has no planned home

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the mathematics rubric already identifies intentional practice coverage as a gap  
**Confidence:** firm

**Location:** Grade 5 frame, Practices paragraph and units table.

**What is wrong:** The table assigns MP1, MP2, MP3, MP4, MP6, MP7 and MP8. It never assigns MP5. Listing supplies does not establish that students choose tools strategically.

**Why it matters:** Later unit plans are instructed to develop the practices named here. They could follow this frame faithfully and omit deliberate opportunities to choose and evaluate tools. MP5 requires such choices. [Standards for Mathematical Practice, pages 6 to 8](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf).

**Exact fix:** In unit 1, replace the MP2 designation with MP5, retaining MP7. Add:

> MP5: students choose cubes, a drawing or a numerical expression to find a volume, explain why their choice suits the solid, and check it with another representation.

MP2 remains deliberately developed in several other units. No content standard or day moves.

### 3. The reader note wrongly excludes the required mathematics-content review

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** new  
**Confidence:** firm

**Location:** Grade 5 frame, lines 55 to 56.

**What is wrong:** “No unit needs a community or qualified reader” is broader than a sensitivity judgment. [FOUNDATION.md, section 7.3](/S:/CurioClass/docs/FOUNDATION.md:133) requires a mathematics-content reviewer to read every item and answer key of one whole course’s checks before the course is called finished. The Grade 6 frame preserves this requirement explicitly.

**Why it matters:** The present wording could remove a required review of the assessments that Curio Class must write independently.

**Exact fix:** Replace that sentence with:

> These contexts require no community-specific sensitivity reader. A qualified mathematics-content reviewer must read every assessment item and answer key before the course is called finished, as required by FOUNDATION 7.3. Cory determines the reader and any payment.

### 4. The Progressions references mix incompatible page locations

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, incorrect progression pointers were identified in the earlier grades 3 to 5 progression review  
**Confidence:** likely

**Location:** Units table, “Check set adds,” especially units 7, 8 and 10.

**What is wrong:** Several pointers disagree substantially with the progression rows that the frame calls its contract. For example:

| Topic | Frame pointer | Corresponding progression-row pointer |
|---|---|---|
| Decimal operations | NBT PDF 77 to 79 | NBT PDF 75, printed 69 |
| Measurement conversion | MD PDF 26 to 27 | GM PDF 116, printed 110 |
| Coordinates and hierarchy | GM PDF 103 to 105 | G PDF 134 to 135, printed 128 to 129 |

These are not merely different statements of one page offset. The accessible standalone NBT document places Grade 5 decimal operations on PDF pages 19 to 20; the indexed compiled geometry text places hierarchy work on printed page 129. [Standalone NBT progression](https://mathematicalmusings.org/wp-content/uploads/2015/03/ccss_progression_nbp_k5_2015_03_16.pdf), [compiled Progressions](https://mathematicalmusings.org/wp-content/uploads/2023/05/Progressions.pdf).

**Why it matters:** Unit writers are expressly sent to these locations to check instructional limits. Wrong pointers can send them to another topic or grade.

**Exact fix:** Name the edition and link in the frame. Reconcile every candidate pointer against the matching skill’s `notes` in `math.csv`, using the existing convention “PDF page (printed page).” For the decimal-operations cell, an immediately verifiable replacement is:

> Candidate: NBT progression, standalone March 2015 draft, PDF pages 19 to 20: decimal computation through place-value reasoning, related to written methods.

Do not copy the compiled page numbers into a standalone document citation. The complete compiled PDF could not be reopened in this sandbox, so its replacement pagination still needs verification.

### 5. The cross-subject calendar still describes existing frames as unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, Grade 3 mathematics frame review, finding 1, and earlier mathematics frame reads  
**Confidence:** firm

**Location:** Grade 5 frame, lines 157 to 159 and the following availability table.

**What is wrong:** The introduction says the other subjects’ frames “are written later.” Grade 5 science and social studies frames now exist. Their actual bridges are more specific than several alternatives proposed here.

**Why it matters:** The note invites another planning pass instead of directing writers to the coordination already recorded. Two independently worded bridge plans can drift.

**Exact fix:** Replace the introduction with:

> The Grade 5 science and social studies frames are written. Their current bridges govern the earlier uses below; the scopes and sequences will confirm exact dates.

Align the table with those frames:

- Science units 1 and 2 use one measurement unit without conversion.
- Science unit 4 uses supplied distance representations without exponent computation and bar graphs until coordinate plotting is taught.
- Science unit 6 uses its recorded earlier-grade line-plot bridge if needed.
- Social studies unit 6 uses latitude, longitude and compass directions.

Retain the mathematics availability dates. No unit move is needed.

### 6. “Split” misclassifies the five routine lessons

**Severity:** Minor  
**LAYER:** base text  
**REPEAT:** yes, Grade 3 mathematics frame review, finding 4  
**Confidence:** firm

**Location:** Grade 5 frame, source-map line 219.

**What is wrong:** The frame defines “split” as dividing a base unit between Curio Class units. Lessons 5.8.14 to 18 instead become warm-up routines throughout the year, with no lesson days allocated.

**Why it matters:** A writer transferring this row into the day-level map could treat the lessons as retained instructional days or leave their disposition ambiguous.

**Exact fix:** Change the decision to `cut` and use:

> Not retained as lesson days. The five routines are reused in warm-ups across the year; their adapted activities are assigned in the day-level source map.

The 160-day total stays unchanged.

### 7. The rubric still says no plan names mathematical practices

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale completion notes are documented in the earlier frame reads  
**Confidence:** firm

**Location:** [RUBRIC-MATH-K8.md, Gateway 2 practices row](/S:/CurioClass/docs/RUBRIC-MATH-K8.md:34).

**What is wrong:** The gap statement says practices are absent from every plan. The current Grade 5 frame assigns seven practices, and [the Grade 4 worked unit](/S:/CurioClass/docs/courses/math-4/s11.md:39) names practices and their tasks.

**Why it matters:** The note conceals the actual remaining task, checking completeness and task quality.

**Exact fix:** Replace the gap statement with:

> Practices are named in current frames and the Grade 4 worked unit. Each course’s scope and sequence must demonstrate all eight through identified tasks; frame assignments alone do not establish complete coverage.

### 8. The rubric still lists the written teaching approach as missing

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the earlier frame reads identify the same stale-status class  
**Confidence:** firm

**Location:** [RUBRIC-MATH-K8.md, teacher-supports row](/S:/CurioClass/docs/RUBRIC-MATH-K8.md:35).

**What is wrong:** “The approach written down with sources” remains listed as a gap, although `APPROACH.md`, `APPROACH-MATH.md` and `APPROACH-SOURCES.md` exist.

**Why it matters:** It asks later workers to recreate an existing foundation and obscures the distinction between a written approach and evidence that lessons implement it.

**Exact fix:** Replace that gap entry with:

> The shared and mathematics approaches are written, with source and access records. Course materials must explain and demonstrate how they implement those approaches.

This does not claim approval, classroom validation or demonstrated outcomes.

## Coverage, sequence and days

All **25 owned skills are placed exactly once**, with no foreign-grade skill listed as owned. Earlier-grade work is identified as readiness or review; general fraction division and later algorithm fluency remain in Grade 6.

No additional content-standard omission was established. The frame and mapped lessons together cover the owned standards, including lettered parts, mixed-number problems, fraction equivalence through multiplication by one, volume packing and additivity, and interpreting coordinates in context.

| Unit | Base lesson days | Added teaching days | Assessment and respond days | Total |
|---|---:|---:|---:|---:|
| 1. Volume and expressions | 12 | 0 | 2 | 14 |
| 2. Fractions as quotients | 5 | 0 | 2 | 7 |
| 3. Fraction multiplication | 18 | 0 | 2 | 20 |
| 4. Fraction division and problems | 10 | 1 | 2 | 13 |
| 5. Multi-digit operations | 20 | 0 | 2 | 22 |
| 6. Decimal place value | 10 | 0 | 2 | 12 |
| 7. Decimal operations | 15 | 0 | 2 | 17 |
| 8. Powers and conversion | 7 | 0 | 2 | 9 |
| 9. Unlike fractions, plots and scaling | 13 | 1 | 2 | 16 |
| 10. Coordinates, shapes and patterns | 13 | 0 | 2 | 15 |
| **Within units** | **123** | **2** | **20** | **145** |

Another four course-check days, four respond days and seven review days produce **160 days**. This fits a school year with explicit response time. No unit is clearly disproportionate to its work; unit 2’s short allocation reflects one focused standard, while units 3 and 5 retain substantial instructional sequences.

The inline map accounts for all **148 base lessons**: 123 unit lessons, nine review lessons merged into seven days, five routine lessons reused in warm-ups, and eleven cuts with reasons. No noncommercial or reference-only source is mapped for adaptation.

The ordering holds: quotient meaning precedes fraction multiplication and division; decimal place value precedes decimal operations; coordinates precede graphing patterns. Delaying unlike-denominator addition is defensible because the frame provides a workable mixed-number strategy. Comparison curricula use different orders, so their sequences do not establish a reason to overturn this base-text order. [Base scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-5/course-guide/scope-and-sequence.html), [Fishtank Grade 5](https://www.fishtanklearning.org/curriculum/math/5th-grade/), [Eureka curriculum map](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum%20Map/EM_GPK5_CurriculumMap.pdf).

The Grade 4 handoffs are picked up, and the Grade 6 frame uses the promised fraction, decimal, volume and coordinate foundations. No unbridged external-subject prerequisite for this mathematics course was found.

## Mathematics lens checklist: course-frame layer

| Checklist line | Result |
|---|---|
| Major work meets the line by units, days and time | **Met at frame level.** The allocation is comfortably above 65 percent. The stated 83 percent remains an estimate for the scope and sequence to document through lesson and minute allocations. |
| Supporting clusters practise major work | **Met.** Conversion uses decimal and place-value reasoning; line plots use fraction operations. |
| Every source-map row has a defined disposition | **Missed narrowly.** All lessons are accounted for, but the routine row needs the correction in finding 6. |

The evidence guide includes connected supporting work in focus calculations and asks for multiple perspectives, including instructional time. [Evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf). The Grade 5 focus document also confirms multi-digit multiplication as the required fluency. [Grade 5 focus](https://achievethecore.org/content/upload/SAP_Focus_Math_5.pdf).

## What is right and should not be touched

- Preserve the coherent base-text order and complete ownership placement.
- Preserve strategies and explanations before the later fluency expectations.
- Preserve the explicit response days and spaced multiplication practice.
- Preserve the fraction models, number-line thread and paper paths.
- Preserve the Grade 5 explanation of equivalence through multiplication by one.

The use of number lines and explanations of fraction procedures is consistent with the federal fractions guide. That guidance supports instructional choices, not a claim that this frame has been tested. [Federal fractions practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/15).

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep ten units and 160 days | Coverage, order and allocations reconcile | Grade 5 frame |
| Keep unlike-denominator addition in unit 9 | Earlier products can use the stated fraction strategy | Grade 5 frame |
| Assign MP5 to unit 1 alongside MP7 | Supplies a deliberate tool-choice task without moving content | Grade 5 frame |
| Retain seven review days with the activity selections in finding 1 | Makes the compression concrete and reviewable | Grade 5 frame and future source map |
| Classify the five routine lessons as cut from lesson-day allocation | Separates routine reuse from retained days | Grade 5 frame |
| Retain science’s existing bridges | Avoids moving mathematics standards for contexts already accommodated | Grade 5 frame |

## Limits and sources

This review cannot establish actual lesson duration, assessment quality or student learning from a frame. The full plan gate did not complete, and the complete compiled Progressions PDF exceeded the web tool’s size limit; direct network retrieval was also unavailable in the sandbox.

Accessible progression documents were used for the relevant limits: [operations and algebraic thinking, Grade 5](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf), [fractions, 2018 draft](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf), and [base ten, March 2015 draft](https://mathematicalmusings.org/wp-content/uploads/2015/03/ccss_progression_nbp_k5_2015_03_16.pdf). Focus and coherence were also checked against the [publishers’ criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf).

No substantive finding rests on personal memory. Pacing judgments are identified as reviewer judgments rather than classroom results.

## For the source list

Add the accessible standalone fractions and base-ten progression links above as fallbacks for the oversized compilation, and the Fishtank Grade 5 overview as a sequence comparison.

## For Cory

- **Audience:** Confirm the proposed daily 60-minute classroom allocation and the requirement for a usable shorter path.
- **People and money:** Identify the required mathematics-content reviewer and any payment before the course is called finished.

**Final verdict:** Sound foundation, revise before unit writing. **Finding count:** 8. **Report path:** `docs/reviews/frame-math-grade-5-2026-11-14.md`, supplied here without writing the file.