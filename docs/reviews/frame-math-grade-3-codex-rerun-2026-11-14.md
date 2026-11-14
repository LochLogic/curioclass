# Independent frame review: math-grade-3

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-math-grade-3-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The frame has a sound structure, complete skill ownership, and a workable 160-day budget, but needs targeted corrections before the scope and sequence is written. The greatest risk is that writers follow narrower or later instructions in the frame instead of the fuller teaching already present in its base lessons. Restore the full rounding expectation and begin spaced multiplication practice earlier, while keeping the unit order and ownership unchanged.

## What I read and checked

- `docs/agents/EXPERT.md`, the math lens, `docs/RUBRIC-MATH-K8.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, BASELINE rules 20 to 24, and relevant approach, source-list, and roadmap sections.
- The complete Grade 3 frame, its `frames.csv` row, all 24 Grade 3 progression rows, and the full Grade 3 standards, including the official PDF’s footnotes.
- The Grade 2 and Grade 4 frames; relevant handoffs in `math-3-5-progression.md`; the earlier Grade 4 scope and sequence and worked section-plan pattern.
- All eight base-text unit overviews, the lesson inventories and preparation-page standards, and selected activities addressing rounding, arithmetic patterns, multiplication strategies, and measurement.
- Relevant portions of the same-year science, ELA, and social studies frames.
- Earlier Grade 3 frame reports, the Grade 2 frame review, and relevant earlier mathematics reviews for unresolved findings and REPEAT classifications.
- `data/plans/math-grade-3/source-map.csv` is absent. This is appropriate at this layer: `frame-write.md` assigns that CSV to the scope-and-sequence stage. The frame’s source-map table supplies the current contract.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check math-grade-3` | Passed: 0 failures; 8 units, 160 days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, 0 marked-note failures. |

The incomplete whole-plan gate does not prevent this substantive verdict under the current brief.

## Findings, most serious first

### 1. Unit 3 narrows the rounding standard

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete standard descriptions also occurred in the Grade 2 frame review, finding 5  
**Confidence:** firm

**Location:** `frame.md:125`, Unit 3, “What students learn.”

**Problem and evidence:** The frame specifies three-digit numbers rounded to hundreds and two-digit numbers rounded to tens. That leaves three-digit numbers rounded to tens outside its stated teaching contract. The progression row describes the easier cases as an emphasis, not an exclusive limit. The [NBT Progression, PDF page 12](https://mathematicalmusings.org/wp-content/uploads/2015/03/ccss_progression_nbp_k5_2015_03_16.pdf) explicitly illustrates three-digit rounding to both places, and [retained base lesson 3.3.15](https://im.kendallhunt.com/k5/teachers/grade-3/unit-3/lesson-15/preparation.html) teaches both within 1,000.

**Why it matters:** A writer following the frame could remove the harder case from teaching and assessment while claiming full coverage.

**Exact fix:** Replace the rounding description with:

> Round whole numbers within 1,000 to the nearest 10 or 100 using place value and a number line. Emphasize three-digit numbers to hundreds and two-digit numbers to tens, while also teaching and checking three-digit numbers to tens.

Keep the existing unit and day allocation.

### 2. The fluency instructions postpone systematic practice unnecessarily

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, delayed fluency practice was identified in `math-4-spine-2026-11-11.md`, finding 5  
**Confidence:** likely

**Location:** `frame.md:35` and Unit 4 at line 126.

**Problem and evidence:** The frame says fact strategies and daily practice start in Unit 4. Unit 4 begins around day 62, and practice described as beginning after that unit starts around day 78. Yet `m3-mult-fluency` names practice in Units 1 and 3 as well. The [OA Progression, PDF page 27](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf) calls for early work toward fluency with easier facts. [Base lesson 3.1.15](https://im.kendallhunt.com/k5/teachers/grade-3/unit-1/lesson-15/preparation.html) already builds toward this target and offers practice with factors 2, 5, and 10.

**Why it matters:** Students who need more repetitions lose several weeks of spaced practice. The frame also contradicts the progression’s intended year-long development.

**Exact fix:** Rewrite the fluency bullet and Unit 4’s “start” wording:

> Begin short, spaced practice with multiplication facts already understood during Unit 1, continuing through Units 2 and 3. Unit 4 owns the complete strategy work, introduces related division-fact practice after division has meaning, and broadens mixed practice through the rest of the year.

Retain Unit 4 ownership, its added strategy days, and all timer restrictions.

### 3. The science bridges introduce measurement before math teaches it

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the earlier Grade 3 frame review, finding 1  
**Confidence:** firm

**Location:** `frame.md:161` and line 162, Cross-subject supply table.

**Problem and evidence:** The math frame permits science to use half-inch measurements and gram scales before math Unit 7. The current science frame instead specifies whole inches or centimetres for early length work and washer counts for the magnetic latch.

Science’s affected work occurs around school days 1 to 77. Math teaches these measurement skills on days 117 to 133. The [fractions Progression, PDF page 3](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf) also places fractional ruler measurement in Grade 3, rather than among the inherited Grade 2 skills.

**Why it matters:** Writers receive conflicting instructions, and the math frame’s bridge requires the very skill it is supposed to avoid assuming.

**Exact fix:** Replace the two bridge cells:

- **Length:** “Science measures in whole inches or whole centimetres until math Unit 7; half- and quarter-inch measurements follow that teaching.”
- **Mass:** “Science counts equal objects, such as washers held by the latch, with no gram-scale requirement until math Unit 7.”

Add the science unit references: Units 1 and 3 for length, Unit 2 for the latch.

### 4. MP2 has no explicit assignment in the frame

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, incomplete practice coverage was identified in `math-4-spine-2026-11-11.md`, finding 5  
**Confidence:** firm

**Location:** The Practices bullet and all eight unit practice cells.

**Problem and evidence:** The frame names MP1 and MP3 through MP8, but never MP2. This is a planning omission, rather than proof that the retained lessons lack quantitative reasoning. [Base lesson 3.6.12](https://im.kendallhunt.com/k5/teachers/grade-3/unit-6/lesson-12/preparation.html), retained in Curio Class Unit 7, explicitly develops MP2 through interpreting measurement situations and tape diagrams. The [Publishers’ Criteria, PDF page 14](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf) asks for all practices to be meaningfully present across the year.

**Why it matters:** The frame’s practice assignments do not give the next writer a complete course-level contract.

**Exact fix:** Set Unit 7’s named pair to:

> MP2 reason abstractly and quantitatively; MP5 use tools strategically.

Name the retained measurement-representation task as the MP2 anchor. MP6 remains explicitly assigned in Units 2 and 3.

### 5. Addition-table patterns have an unclear contributing unit

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, the earlier Grade 3 frame review, finding 2  
**Confidence:** firm

**Location:** Units 3 and 4, lines 125 to 126.

**Problem and evidence:** Unit 4 claims both addition- and multiplication-table patterns, but the retained addition-table work occurs in base lessons 3.3.2 and 3.3.5, mapped to Unit 3. Unit 3 identifies its contribution to two-step problems but omits this contribution to arithmetic patterns. The base text’s [lesson-to-standard mapping](https://im.kendallhunt.com/k5/teachers/grade-3/course-guide/lessons_and_standards.html) confirms these placements.

**Why it matters:** A writer could trim the early pattern work or add unnecessary replacement work to the crowded Unit 4.

**Exact fix:**

- Add to Unit 3: “Base lessons 2 and 5 begin m3-arithmetic-patterns through addition-table patterns explained with properties; Unit 4 owns and completes the skill.”
- Change Unit 4 to: “Explain multiplication-table patterns using properties, recalling the addition-table patterns from Unit 3.”

No ownership moves.

### 6. The shorter-period estimate is incorrect

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** `frame.md:169`, For the lead, item 1.

**Problem and evidence:** The frame says a 45-minute block requires about 20 percent more days. Its planned instruction totals 9,600 minutes. Delivering that time in 45-minute periods requires 213⅓ periods, or 214 whole periods, approximately one-third more than 160. Increasing days by 20 percent supplies only 8,640 minutes.

**Why it matters:** The audience decision is presented with an alternative that understates the required time.

**Exact fix:** Replace the estimate with:

> Keeping the same instructional minutes in 45-minute periods would require about one-third more periods, or 214 whole periods. A 160-day, 45-minute path would need a separately specified adaptation reducing the planned minutes by 25 percent.

Leave approval of the intended audience and period length with Cory.

### 7. The cross-subject introduction contains an unmarked stale note

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the earlier Grade 3 review, finding 1, and earlier mathematics frame reviews  
**Confidence:** firm

**Location:** `frame.md:155`.

**Problem and evidence:** The introduction says the other subjects’ frames “are written later” and that their unit numbers are not recorded. Those frames now exist, and this table already records a social studies unit and day range.

**Why it matters:** The note tells the next writer to treat available coordination evidence as unfinished.

**Exact fix:** Replace the introductory sentence with:

> This course supplies the following mathematics to other subjects in the same year; use the receiving courses’ frames for their unit references and bridge routines.

The automated stale check passes because it does not catch this wording.

## Coverage, order, days, and sources

### Owned skills and standards

All 24 Grade 3 skills appear in exactly one owning unit. No foreign-grade skill ID appears in the ownership cells.

| Unit | Owned skills | Retained base teaching days | Added days | Assessment and respond days | Total |
|---|---:|---:|---:|---:|---:|
| 1 | 2 | 20 | 0 | 2 | 22 |
| 2 | 2 | 14 | 0 | 2 | 16 |
| 3 | 2 | 19 | 0 | 2 | 21 |
| 4 | 5 | 11 | 3 | 2 | 16 |
| 5 | 3 | 10 | 2 | 2 | 14 |
| 6 | 5 | 18 | 3 | 2 | 23 |
| 7 | 3 | 15 | 0 | 2 | 17 |
| 8 | 2 | 13 | 0 | 2 | 15 |
| **Total** | **24** | **120** | **8** | **16** | **144** |

Every content standard and lettered part has a home. Finding 1 concerns incomplete wording within an assigned standard; findings 2 and 5 concern how assigned work develops across units. No other partial standard emerged from this read.

The larger-number multiplication in Unit 5 follows base lessons that keep those products within 100. It should retain that explicit limit in the scope and sequence.

### Unit reasons and year capacity

The order holds:

- Arrays precede area.
- Area models precede distributive reasoning.
- Division and rounding precede the completed four-operation problems.
- Fractions precede fractional measurement and line plots.
- Perimeter follows area, allowing comparison.

The 144 unit days plus four course-assessment days, four course respond days, and eight review days total 160. This fits 32 five-day weeks, leaving four weeks within the foundation’s 36-week calendar.

No unit is clearly far over or under its load. Unit 3’s 21 days are substantial for additional work, but include four major-work problem lessons and the year’s additive fluency. Unit 4 has five skills in 16 days, supported by earlier contributions and continued practice. Unit 6’s 23 days reasonably protect five closely connected fraction skills.

### Source map

All 143 base lessons are accounted for:

| Disposition | Base lessons |
|---|---:|
| Retained in units | 121, delivered in 120 days after the subtraction merge |
| Course-level review | 8 |
| Reused as warm-up routines | 4 |
| Cut with reasons | 10 |
| **Total** | **143** |

The split of base Unit 4 follows its section boundary. Remaining lesson order is preserved. No non-commercial edition or reference-only curriculum is mapped as teaching material.

The three-lesson subtraction merge needs its activity selections and timings resolved in the day-level source map. At this frame layer, its two-day budget and reason are sufficient; the earlier reader’s suggested activity selection is a candidate, not a uniquely necessary solution.

Likewise, I do not count the earlier objection to the routine-reuse label “split” as a substantive coverage defect. Its destination and treatment as warm-ups are explicit.

### Seams and cross-subject timing

The Grade 2 incoming handoffs and Grade 4 outgoing handoffs align. Named skips to later grades are justified. The standard algorithms remain in their correct fluency grades.

ELA places word-meaning work in Unit 2 before math Unit 5, and discussion routines in Unit 1 before math Unit 6. Social studies explicitly keeps savings calculations within 100 until the larger-number mathematics is taught. The science bridge corrections are finding 3.

## Math lens checklist: course frame layer

| Lens line | Result |
|---|---|
| Major work meets the line by units | **Met:** six of eight units, 75 percent. |
| Major work meets the line by days | **Met:** the budget clears 65 percent when supporting work deliberately connected to major work is counted. |
| Major work meets the line by time | **Met at the frame’s equal-period planning level.** Confirm with activity minutes in the scope and sequence. |
| Supporting work practises major work | **Met:** scaled graphs support multiplication, partitioning supports unit fractions, and fractional line plots support number-line reasoning. |
| Every source-map row has a decision | **Met:** all rows specify keep, split, merge, cut, or ours. |
| No duplicated ownership or unexplained grade skip | **Met.** |
| Models precede their dependent work | **Met.** |
| Standard algorithms remain in their fluency grades | **Met.** |
| Grade limits remain intact | **Met apart from the narrowing in finding 1.** |

The focus judgment follows the [evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf), which counts supporting work connected to major work. I did not independently certify the frame’s precise “109 days” estimate.

## What is right and should not be touched

- Keep the base-text order and the division-unit split.
- Keep fractions as numbers, including fractions greater than one, with strips connected to number lines. This agrees with the [federal fractions guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/15).
- Keep the explicit same-whole condition, full perimeter cases, and both meanings of division.
- Keep assessment and respond time, paper alternatives, and private fluency practice without displayed timers.
- Keep original exit tickets and assessments rather than relying on inaccessible base-text assessment materials.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Include three-digit rounding to tens in Unit 3 | Complete the existing standard | `frame.md`, Unit 3 |
| Begin practice with understood products in Unit 1 | Preserve time for spaced fluency development | `frame.md`, Fluency and Units 1 to 4 |
| Assign MP2 and MP5 to Unit 7 | Use an existing measurement task; MP6 remains elsewhere | `frame.md`, Unit 7 |
| Name Unit 3’s contribution to arithmetic patterns | Match retained lessons while keeping Unit 4 ownership | `frame.md`, Units 3 and 4 |
| Match science’s whole-unit and washer-count bridges | Remove conflicting prerequisite instructions | `frame.md`, Cross-subject |
| Correct the 45-minute arithmetic | Same minutes require about one-third more periods | `frame.md`, For the lead |
| Replace the stale cross-subject introduction | Refer directly to existing coordination documents | `frame.md`, Cross-subject |

## For Cory

- **Audience:** Resolve the existing 60-minute-period assumption. Keeping 160 periods of 45 minutes requires a defined shorter path; the current “20 percent more days” estimate cannot support that decision.

No new money, people, or content-scope decision is required by these findings.

## Earlier-review reconciliation and limits

The earlier substantive Grade 3 review correctly identified the science bridge and arithmetic-pattern handoff problems. This read additionally identifies the rounding restriction, delayed fluency instructions, missing MP2 assignment, and shorter-period arithmetic; these warrant a firmer revision verdict than “minor edits.”

The earlier blocker-only report records an accurate historical runtime failure. This report supplies the substantive review that it left undone.

I could not judge actual classroom duration, final assessment coverage, or the activity balance of the merged subtraction days. Those require the scope and sequence and assessment items.

No curriculum conclusion rests on personal memory. Prior session memory informed report structure only.

## Outside sources and access

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): Grade 3 requirements, practices, and footnotes.
- [NBT Progression, 2015](https://mathematicalmusings.org/wp-content/uploads/2015/03/ccss_progression_nbp_k5_2015_03_16.pdf): rounding and algorithm handoffs.
- [OA Progression, 2011](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf): early fluency development and Grade 3 problem structures.
- [Fractions Progression, 2018](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf): unit fractions, number lines, measurement, and equivalence.
- [Publishers’ Criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf) and [Grade 3 focus document](https://achievethecore.org/content/upload/SAP_Focus_Math_3.pdf): practice coverage, focus, and fluency.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): focus calculation and supporting-work treatment.
- [Base curriculum scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-3/course-guide/scope-and-sequence.html): source order, supplemented by the local lesson store.
- [Second curriculum overview, Grade 3 begins on PDF page 34](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf): comparison of sequencing and emphasis; reference only.
- [Federal fractions practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/15): fractions as numbers and number-line representations.

**Access limit:** The compiled 2023 Progressions PDF exceeded the web reader’s size limit. I used the accessible author-published domain drafts above; the frame’s exact 2023 page pointers were not independently certified.

**For the source list:** Record the accessible NBT draft at the `mathematicalmusings.org` address above as a fallback for the timed-out `commoncoretools.me` address.

**Verdict:** Sound structure; targeted revisions required.  
**Finding count:** 7, comprising 3 moderate and 4 minor findings.  
**Report path:** `docs/reviews/frame-math-grade-3-2026-11-14.md`, supplied here only.

