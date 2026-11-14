# Independent frame review: Math Grade 7
2026-11-14

Report supplied here only. No files were changed. Intended path: `docs/reviews/frame-math-grade-7-2026-11-14.md`.

## Verdict

Revise before using this frame to write unit plans. The eight-unit sequence, placement of all 23 owned skills and 43 standard codes, and 160-day year are coherent, but several source references, prerequisite placements, and student activities could lead a writer to build incomplete or overloaded instruction. The most valuable correction is to make the source map specify where instruction begins, what students actually do, and which activities survive each merge.

## What I read and checked

- Expert instructions, mathematics lens, mathematics rubric, Foundation, shared and mathematics approaches, relevant Roadmap sections, BASELINE rules 20 to 24, and the base-text record.
- The complete Grade 7 frame, its `frames.csv` row, all Grade 7 progression rows, relevant neighboring progression links, and the Grade 6 and Grade 8 frames.
- Grade 7 standard text and focus classifications.
- Base-text unit and lesson inventories, preparation-page standards and optional markers, and targeted lesson activities, especially decimal expansions, scale drawings, and comparative inference.
- Relevant science and social studies frame rows and calendars.
- Earlier Grade 7 reviews, neighboring mathematics frame reviews, progression reviews and reconciliation records, and the Grade 4 worked example.

`data/plans/math-grade-7/source-map.csv` does not exist. The frame explicitly defers that file to the scope and sequence; its embedded source map was reviewed instead.

**Gates:** `plan.py check` could not complete because `markdown` is unavailable; `frame.py check math-grade-7` passed with zero failures; `stale.py check` passed across 56 files with zero marked-note failures.

The unavailable full gate does not withhold this curricular verdict, as the current brief expressly directs.

## Findings, most serious first

### 1. Decimal-expansion instruction is assigned to a unit whose cited lessons do not teach it

**Severity:** Serious  
**LAYER:** frame, progression, base text  
**REPEAT:** yes, unresolved in the earlier Grade 7 expert report  
**Confidence:** firm

**Location:** Grade 7 frame, units 4 and 5; `data/progressions/math.csv`, `m7-decimal-expansion`.

**Problem and consequence:** The progression cites 7.4.4 and 7.5.12. Those lessons concern proportional relationships and negative rates. The actual long-division lesson is **7.4.5**, retained in unit 4. Unit 5 owns the skill and promises its instruction, but its source allocation identifies no finishing lesson. A writer following the references could omit the intended consolidation or introduce the same content twice without explaining the relationship. [Base lesson 7.4.5](https://im.kendallhunt.com/MS/teachers/2/4/5/index.html)

**Exact fix:** Keep ownership in unit 5. Add to unit 4:

> Long division to terminating and repeating decimals begins in base lesson 7.4.5; 7.NS.A.2d is owned and checked in unit 5.

Name one of unit 5’s six added days:

> Decimal expansions consolidated, including negative rational numbers, terminating or eventually repeating forms, and an independent long-division check.

Correct the progression reference to 7.4.5 and this added unit 5 day. Unit 5’s six added days then comprise decimal consolidation, mixed practice, mid-unit check and response, and end-of-unit assessment and response.

### 2. Teacher demonstration does not complete the technology requirement

**Severity:** Serious  
**LAYER:** standard  
**REPEAT:** yes, the partial-standard type appears in earlier mathematics frame reads  
**Confidence:** firm

**Location:** Frame lines 42 to 45, unit 7, and “For the lead,” item 4.

**Problem and consequence:** The frame accepts a teacher demonstration plus paper construction as completing 7.G.A.2. The standard requires students to draw using technology as well as the other named methods. Watching the teacher operate a drawing environment does not establish that student performance. This differs from the earlier Grade 7 report’s acceptance of the fallback. [Official mathematics standards, printed page 50](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf)

**Exact fix:** Replace the completion claim with:

> Students construct and test shapes using technology. On one shared device, students take turns controlling the construction. Teacher demonstration introduces the task; paper construction provides additional practice and evidence but does not replace the digital construction.

The unit plan must name an available environment and a feasible participation arrangement before claiming full coverage.

### 3. Three merged days lack a feasible retained-activity allocation

**Severity:** Moderate  
**LAYER:** frame, base text  
**REPEAT:** yes, retained-activity budgets were also missing in the Grade 4 and Grade 5 independent reads  
**Confidence:** firm on the time discrepancy; judgment call on the proposed selections

**Location:** Source-map merges 7.1.3–4, 7.1.11–12, and 7.8.18–19.

**Problem and consequence:** Excluding optional activities, synthesis, and exit checks, the source activities and warm-ups total approximately:

| Merge | Source minutes | Available after daily practice |
|---|---:|---:|
| 7.1.3–4 | 50 | 45 |
| 7.1.11–12 | 55 | 45 |
| 7.8.18–19 | 80 | 45 |

The last merge compresses the main comparative-inference instruction and subsequent information-gap practice. Its reason also misdescribes lesson 19 as class-data work. [Lesson 18](https://im.kendallhunt.com/MS/teachers/2/8/18/index.html), [lesson 19](https://im.kendallhunt.com/MS/teachers/2/8/19/index.html)

**Exact fix:** Keep the current unit totals, with these explicit adaptations:

- **3–4:** Five minutes of prior practice, five-minute opening, three ten-minute tasks covering scaled-copy construction, multiplicative reasoning, and corresponding distances and angles, then five-minute synthesis and five-minute exit ticket.
- **11–12:** Five minutes of prior practice, five-minute opening, fifteen minutes redrawing at another scale, fifteen minutes interpreting equivalent scales and units, then five-minute synthesis and five-minute exit ticket.
- **18–19:** Replace the merge with an adapted lesson 18 using mean/MAD and median/IQR comparisons. Allocate five minutes each to prior practice and opening, fifteen minutes to each comparison, and five minutes each to synthesis and exit ticket. List lesson 19 separately as an extension cut because lesson 18 carries the required inference instruction.

The final choice retains 17 base-derived days in unit 8. Record omitted activities explicitly.

### 4. Unit 1 uses angle tools before their planned re-entry

**Severity:** Moderate  
**LAYER:** frame, progression  
**REPEAT:** yes, earlier reads identify prerequisites and threads beginning before their named preparation  
**Confidence:** firm

**Location:** Readiness paragraph, incoming seams, and unit 1.

**Problem and consequence:** The frame places the first rebuilding of angle concepts and protractor use in unit 7. Retained lesson 7.1.4 already asks students to measure corresponding angles with protractors. Its preparation page explicitly requires them. A student can therefore meet a dormant prerequisite in the opening unit without the promised readiness support. [Lesson 7.1.4](https://im.kendallhunt.com/MS/teachers/2/1/4/index.html)

**Exact fix:** Add brief readiness checks and rebuilding of `m4-angle-concepts` and `m4-protractor` before the merged 3–4 day. Name corresponding-angle comparison as earlier-grade review supporting scale drawings. Add protractors and tracing paper to unit 1’s supplies, and change unit 7’s wording to “recheck and refresh.”

### 5. The major-work percentage is not reproducible as written

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the earlier Grade 7 report identified the arithmetic problem  
**Confidence:** firm

**Location:** “Major work” paragraph and “For the lead,” item 2.

**Problem and consequence:** Units 2, 4, 5 and 6 total **94 days**. Adding the assumed four major-work-equivalent course days already produces 98, leaving none of the stated ratio days from unit 1 in that calculation.

Connected supporting work may count, but the frame does not identify the activities and minutes producing its additional 16 days. A lesson containing a short major-work warm-up does not automatically supply a whole period of major-work instruction.

**Exact fix:** Correct the arithmetic and label the connected-work estimate provisional. Add a compact allocation identifying qualifying activities, their Grade 7 standards, and estimated minutes, including practice and assessments without double counting. The year contains **8,000 minutes**; demonstrating 65 percent requires **5,200 qualifying minutes**.

Retain the unit lengths while making this allocation. Do not automatically transfer six geometry or statistics days. The evidence guide includes connected supporting work and asks reviewers to examine units, lessons or activities, and instructional time. [Evidence guide, indicator 1e, PDF pages 13 to 15](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf)

I agree with the earlier report’s counting rule, but do not regard its whole-lesson tag count as sufficient evidence for instructional time.

### 6. Cross-subject availability statements need correction against existing frames

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, unresolved in the earlier Grade 7 report  
**Confidence:** firm

**Location:** Cross-subject rows for science.

**Problem and consequence:**

- MS-PS1-4 is completed in **science Grade 6**, through `s6-state-change`, rather than owned by science Grade 7.
- Science Grade 7’s design unit occupies days **24 to 42**, overlapping mathematics unit 2, days **13 to 33**. Its exact proportionality task is not located.
- Science Grade 7’s population work occupies days **129 to 158**, comfortably after mathematics percentages, days **47 to 68**.

The present wording obscures what is already available and what still needs coordination.

**Exact fix:** Move the thermometer context to the earlier-grade assumptions. Mark population percentages available. For the design task, require supplied comparisons before mathematics day 33, without asking students to classify proportionality; allow the full proportionality test afterward. Mathematics can use supplied engineering data before the science investigation if the problem explains its own context.

Preserve the social studies timing: time zones around days 78 to 86 and Roman economic contexts around days 134 to 144 follow the relevant mathematics.

### 7. Two other progression references point writers to the wrong lesson ranges

**Severity:** Minor  
**LAYER:** progression, base text  
**REPEAT:** yes, the same source-reference error appears in finding 1 and the earlier Grade 7 read  
**Confidence:** firm

**Location:** `m7-percent-problems` and `m7-compare-populations`.

**Problem and consequence:** The percentage row cites lessons 5 to **17**, but base unit 7.4 ends at lesson **16**. The population-comparison row cites 7.8.12 to 15, omitting the principal comparison lessons 11, 18 and 19. Writers cannot reliably retrieve the intended instruction.

**Exact fix:**

| Row | Replacement source reference |
|---|---|
| `m7-percent-problems` | 7.4.6 to 16, drawing on representation work in 7.4.4–5 |
| `m7-compare-populations` | 7.8.11 and 18; lesson 19 as further practice or extension, with sampling preparation in 12 to 16 |

The frame already accounts for these lessons; ownership need not change. [Percentage unit inventory](https://im.kendallhunt.com/MS/teachers/2/4/index.html), [probability and sampling inventory](https://im.kendallhunt.com/MS/teachers/2/8/index.html)

### 8. The rubric’s statement that no plan names practices is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, already identified in the Grade 5 independent reread  
**Confidence:** firm

**Location:** `docs/RUBRIC-MATH-K8.md:34`.

**Problem and consequence:** It says practices are absent from all plans. This frame assigns all eight, and the Grade 4 worked unit names practices and tasks. The note directs attention away from the remaining implementation check.

**Exact replacement:**

> Practices are named in current frames and the Grade 4 worked unit. Each course’s scope and sequence must demonstrate all eight through identified tasks; assignments in a frame alone do not establish complete coverage.

### 9. The rubric still lists the written approach as missing

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, already identified in the Grade 5 independent reread  
**Confidence:** firm

**Location:** `docs/RUBRIC-MATH-K8.md:35`.

**Problem and consequence:** “The approach written down with sources” remains a gap although the shared approach, mathematics approach, and source record exist. It invites duplicate work.

**Exact replacement:**

> The shared and mathematics approaches are written, with source and access records. Course materials must explain and demonstrate how they implement those approaches.

This makes no claim about classroom results or approval.

### 10. The lens confuses missing narrative pages with missing progression work

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, already identified in the kindergarten independent read  
**Confidence:** firm

**Location:** `docs/agents/lenses/math.md:61–62`.

**Problem and consequence:** The separate narrative page may remain specific to grades 3 to 5, but the statement that other bands still need the same handoff work overlooks the assembled K to 11 progression and frame seam tables.

**Exact replacement:**

> The grades 3 to 5 narrative reference remains available. Other bands’ handoffs are recorded in data/progressions/math.csv, progression review records, and course-frame seam tables. Review their completeness and timing against the published Progressions.

### 11. The adjacent Grade 8 frame says existing receiving frames are unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, unresolved in the earlier Grade 8 expert report  
**Confidence:** firm

**Location:** `docs/courses/math-grade-8/frame.md:66–67`.

**Problem and consequence:** Algebra I and Geometry frames now exist. Calling them unwritten discourages checking the receiving end of the progression reviewed here.

**Exact replacement:**

> Handed on to Algebra I and Geometry; their current frames identify the receiving units.

Then replace row-only destinations with the receiving units documented in those frames.

### 12. The earlier blocked independent report needs a superseding status note

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the Grade 4 independent reread identified the same issue  
**Confidence:** firm

**Location:** `docs/reviews/frame-math-grade-7-codex-2026-11-14.md`, verdict and closing instructions.

**Problem and consequence:** It requires a passing full gate before any substantive read and leaves the frame unjudged. The current brief supersedes that instruction, and this report completes the substantive read. Without a status update, the review record can continue to show an outstanding independent review.

**Exact replacement status note:**

> Superseded by the completed independent Grade 7 frame review of 2026-11-14. The full plan gate remains unavailable in this sandbox; the course structural check passes. Use the completed review for the curricular verdict and findings.

Preserve the original runtime evidence.

## Coverage, sequence and days

| Requirement | Result |
|---|---|
| Owned skills | All **23** Grade 7 skills placed exactly once; no foreign-grade skill listed as owned |
| Standard identifiers | All **43** owned codes represented |
| Standards in full | Technology performance is incomplete under the stated fallback; decimal instruction needs an explicit beginning and completion allocation |
| Other standard clauses | No further substantive omission established from the frame and retained source instruction |
| Unit reasons and order | Coherent: scale reasoning leads to proportional relationships; signed arithmetic precedes equations; equations precede angle problems; percentages precede probability and sampling |
| Source coverage | All **145** base lessons accounted for: 126 retained lessons become 123 days through three merges; 19 lessons are cut |
| Licensing | Mapped material is the permitted first edition; no NC or reference-only curriculum is mapped |
| Incoming seams | Grade 6 ratios, arithmetic, equations, geometry and statistics are picked up; earlier angle-tool re-entry needs finding 4 |
| Outgoing seams | Direct Grade 8 receiving uses match; later algebra and probability destinations are named |
| Cross-subject | Finding 6; no need to reorder the mathematics units |

Current day allocation:

| Unit | Base-derived days | Added days | Total |
|---|---:|---:|---:|
| 1 | 10 | 2 | 12 |
| 2 | 15 | 6 | 21 |
| 3 | 9 | 2 | 11 |
| 4 | 16 | 6 | 22 |
| 5 | 17 | 6 | 23 |
| 6 | 23 | 5 | 28 |
| 7 | 16 | 2 | 18 |
| 8 | 17 | 2 | 19 |
| **Units** | **123** | **31** | **154** |
| Course checks and responses | | **6** | **6** |
| **Year** | | | **160** |

The year leaves 20 days within a nominal 180-day calendar. No whole unit is clearly excessive for its responsibilities; the concern is the activity load hidden inside particular merged days.

## Lens checklist: course frame layer

| Checklist line | Judgment |
|---|---|
| Major work meets the required emphasis by units, lessons and time | **Missed as demonstrated evidence.** Connected work is legitimate, but the stated allocation needs correction and a reproducible time estimate |
| Supporting clusters practise major work | **Met in design.** Sampling uses proportional reasoning, circles use proportional relationships, and angle problems use equations; quantify the credited work |
| Every source-map row has a decision | **Met.** Decisions cover every base lesson; merges and several references require findings 1, 3 and 7 |

Related progression checks found no duplicate grade ownership or premature algorithm expectation. Earlier angle-tool preparation is finding 4. Unit-task quality, assessment items, daily exit tickets, and actual classroom timing remain later-layer checks.

## What is right and should be preserved

- The eight-unit sequence and its mathematical dependencies.
- Number-line reasoning for signed arithmetic and comparison of arithmetic and algebraic equation solutions.
- Explicit checks and response time, daily mixed practice, and the absence of student countdown timers.
- Retaining percentage-error instruction and providing extensions from omitted application lessons.
- Neutral financial and survey contexts.

## Settled by the expert

| Choice | Reason | Proposed location |
|---|---|---|
| Keep decimal ownership in unit 5; begin it explicitly in unit 4 | Preserves ownership while matching the source | Frame units 4–5; progression note |
| Require student-controlled digital construction | Preserves the standard’s required performance | Frame unit 7 and technology note |
| Keep current unit totals with the activity selections in finding 3 | Resolves overload without adding days | Embedded source map |
| Bring angle-tool readiness into unit 1 | Preparation belongs before first use | Readiness, seams and unit 1 |
| Count documented connections to major work | Supported by the evidence guide | Focus paragraph and allocation |
| Use actual neighboring-course calendars | Removes avoidable uncertainty | Cross-subject table |

## For Cory

None. These corrections preserve the course’s standards ownership, audience and 160-day allocation.

## Limits and outside sources

This is a frame review, not verification of unwritten assessments or classroom timing. The complete 2023 Progressions PDF exceeded the web tool’s size limit; the Number System and Geometry draft links also failed. No curricular finding rests on memory.

Sources opened and used:

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): Grade 7 requirements and neighboring-grade limits.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): focus counting, connected work, and instructional-time evidence.
- [K–8 publishers’ criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence and rigor.
- [Ratio progression](https://commoncoretools.files.wordpress.com/2012/02/ccss_progression_rp_67_2011_11_12_corrected.pdf), [expression and equation progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf), and [statistics and probability progression](https://commoncoretools.files.wordpress.com/2011/12/ccss_progression_sp_68_2011_12_26_bis.pdf): mathematical dependencies and handoffs.
- [Base-text scope and sequence](https://im.kendallhunt.com/MS/teachers/2/scope_and_sequence.html), plus the linked lessons above: source order, activity requirements and lesson allocations.
- [Second curriculum’s Grade 7 sequence](https://www.fishtanklearning.org/curriculum/math/7th-grade/): comparison of proportional, rational-number, algebra, geometry and statistics organization; not treated as a minimum pacing requirement.
- [Federal problem-solving practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/16): representations, reflection and comparison of strategies.

**For the source list:** Add the accessible draft progression links and Grade 7 comparison page above as fallbacks or course-specific references.

**Verdict:** Revise before unit planning. **Finding count:** 12. **Report path:** `docs/reviews/frame-math-grade-7-2026-11-14.md`, supplied here without writing the file.

