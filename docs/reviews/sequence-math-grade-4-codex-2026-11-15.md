# Independent sequence review: Math Grade 4

**Date:** 2026-11-15  
**Role:** Independent first reader, before the expert  
**Intended report path:** `docs/reviews/sequence-math-grade-4-2026-11-15.md`  
**Delivery:** Complete report supplied inline. No files changed.

## Verdict

The sequence has a sound mathematical order and carries the owned standards through appropriate teaching arcs. It needs revision before unit-plan production because the measurement assessment leaves a required context to a conditional catch-up prompt, the major-work minute claim credits more than the named tasks establish, and day 100 exceeds its period budget. Repair those directions and the stale contract notes while retaining the nine units and their order.

**Finding count: 4.**

## What I read

- `docs/agents/EXPERT.md`, the mathematics lens, `docs/RUBRIC-MATH-K8.md`, the foundation, shared and mathematics approaches, relevant source-register entries, roadmap provisions, and BASELINE rules 20 to 24.
- The complete Math Grade 4 scope and sequence, all 160 day rows, its frame, and the source map.
- The 27 Grade 4 progression rows, their earlier-grade prerequisites, Grade 5 handoffs, and relevant Grade 2 and Grade 3 day records.
- `CALENDAR.md`, all Grade 4 calendar rows, and relevant same-year frame passages.
- Sequence-writing and readiness-timing rules; permitted earlier Grade 4 frame reports and the Grade 3 independent sequence report for repeat classification.
- The outside sources linked below.

The prohibited files were not opened. Session memory informed the review workflow only. No curriculum conclusion rests on memory.

## Gates

The repository-wide plan check stopped before this course because Python lacks `markdown`; the course-specific checks passed, so the environment failure does not withhold this verdict.

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Incomplete: `ModuleNotFoundError: No module named 'markdown'` |
| `python -X utf8 scripts/frame.py calendar` | Passed; Grade 4 mathematics checks in weeks 12, 23 and 31 |
| `python -X utf8 scripts/frame.py check math-grade-4` | 0 failures |
| `python -X utf8 scripts/plan.py check math-grade-4` | 0 failures |
| `python -X utf8 scripts/sequence.py check math-grade-4` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

No turn, build, synchronization, defect-writing or Git mutation command was run.

## Findings, most serious first

### 1. Unit 6 does not reserve its mass-problem assessment evidence

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete evidence for a claimed standard also appears in the Grade 3 sequence review, finding 3  
**Confidence:** Firm on the missing placement; likely on the resulting implementation risk

**Location:** Scope and sequence, unit 6, assessment paragraph; `days.csv`, days 90 and 93.

**What is wrong:** Day 93 assembles evidence from days **84, 86, 88, 89 and 91**, claiming all of `4.MD.A.2`. Day **90**, which explicitly teaches mass and capacity problems, is absent.

The retained base lesson behind day 89 concerns time intervals. Its added money problem does not supply the missing mass context. The base lesson behind day 90 supplies weight and capacity problems. [Base lesson 5.13](https://im.kendallhunt.com/k5/teachers/grade-4/unit-5/lesson-13/lesson.html), [base lesson 5.14](https://im.kendallhunt.com/k5/teachers/grade-4/unit-5/lesson-14/lesson.html).

The conditional “short missing-part prompt if needed” leaves a predictable omission to the ten-minute assembly slot. Mass is an explicit component of the standard. [Official standards, printed page 31](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf#page=31).

**Why it matters:** A writer can follow the named archive exactly and still lack a planned mass-problem performance. The teacher then has to identify and repair the omission while assembling records.

**Exact fix:**

- Reserve a brief independent mass-problem product inside day 90, replacing repeated practice.
- Add day 90 to day 93’s archive list in both files.
- Identify which retained day 86 task supplies liquid-volume evidence after the money substitution.
- Give the record five explicit context entries: distance, time, liquid volume, mass and money. Also identify where its operations, fraction/decimal notation, conversion and measurement-scale representation are evidenced.
- Keep day 93 for record completion and genuinely unexpected missing evidence. Keep one response on day 95.

### 2. The major-work minute claim gives blanket credit to prerequisite preparation

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, major-work accounting was finding 1 in the earlier Grade 4 frame report  
**Confidence:** Firm that the blanket allocation is unsupported; judgment call on individual borderline minutes

**Location:** Scope and sequence, “Cross-subject timing and practice over the year,” the 6,430-minute calculation.

**What is wrong:** The calculation credits 50 minutes on every unit 1 day because factors and multiples prepare later equivalence. The named unit 1 tasks develop factor structure and maintain Grade 3 multiplication and area. They do not identify the Grade 4 major-work tasks occupying those credited minutes.

Supporting work can count when it engages students in the grade’s major work. A useful prerequisite relationship alone does not establish that every minute of the earlier unit does so. [K-8 Publishers’ Criteria, criterion 3](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf), [mathematics evidence guide, indicators 1e and 1f](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf).

Removing unit 1’s **net 390 credited minutes**, including restoration of its already-deducted ten-minute facts sample, changes this stated allocation from **6,430 to 6,040 minutes**, or **62.9 percent**. This is a sensitivity calculation, not proof that the actual course falls below 65 percent. Other currently uncounted work may restore the margin.

I disagree with the earlier frame report’s treatment of “factors feed equivalence” as sufficient justification for crediting the entire unit.

**Why it matters:** The draft presents 67 percent as a conservative reservation, but its margin depends on a classification the daily tasks do not substantiate.

**Exact fix:** Replace blanket unit credit with a task-based minute ledger naming the Grade 4 major standard being practised. Retain justified supporting-work minutes and count previously excluded Grade 4 warm-up, synthesis or exit-ticket minutes once each. If no unit 1 minutes qualify, document at least **200 additional qualifying minutes** elsewhere to reach 6,240 of 9,600 minutes. Keep the current unit order; seek a frame decision only if a defensible allocation cannot fit.

### 3. Day 100 contains 70 minutes of directions in a 60-minute period

**Severity:** Minor  
**LAYER:** sequence  
**REPEAT:** yes, unreconciled activity budgets were finding 2 in the earlier Grade 4 frame rerun  
**Confidence:** Firm

**Location:** `days.csv`, day 100; corresponding original source-map row.

**What is wrong:** The row allocates:

| Component | Minutes |
|---|---:|
| Facts sample | 10 |
| Targeted response | 20 |
| Area retrieval | 20 |
| Synthesis | 10 |
| Listed warm-up | 5 |
| Required original exit ticket | 5 |
| **Total** | **70** |

The row does not say that its facts sample replaces the listed warm-up, and its four specifically timed components already consume the whole period.

**Why it matters:** This day protects a multiplication prerequisite. An overfull budget makes the area retrieval or independent evidence the likely casualty.

**Exact fix:** Use **5 minutes warm-up, 10 facts sample, 15 targeted response, 20 area retrieval, 5 synthesis and 5 exit**, totaling 60 minutes. Update the source-map note to match.

For the 45-minute route, specify **5 minutes warm-up, 5 facts sample, 8 response, 12 area retrieval, 10 synthesis and 5 exit**. Select fewer facts and examples; retain all four named prerequisite purposes.

### 4. Higher-layer notes still contradict the corrected sequence

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale planning directions recur in the earlier Grade 4 frame rerun  
**Confidence:** Firm

**Locations:**

- `frame.md`, Readiness, Seams, unit descriptions and source-map notes.
- `data/progressions/math.csv`, `m4-decimal-notation`.
- `docs/APPROACH-MATH.md`, “Students who are behind.”

**What is wrong:**

- The frame still calls Grade 3 facts and fraction retrieval “readiness,” and requires another money readiness check in unit 6.
- The frame and decimal progression note attribute cents-as-hundredths instruction to public base lesson 3.18. Its public activity concerns coin thickness; the sequence correctly identifies the dollar representation as an adaptation. [Public base lesson 3.18](https://im.kendallhunt.com/k5/teachers/grade-4/unit-3/lesson-18/lesson.html).
- The mathematics approach says Grade 4 has no reteaching beyond four respond days. This sequence contains nine unit respond days, four course-level respond days and in-day reminders.

**Why it matters:** Writers are instructed to consult these files. They can reintroduce duplicate readiness checks, omit the explicit money adaptation or underestimate available response time.

**Exact fix:** Synchronize these statements with the sequence:

- Facts and Grade 3 fractions receive retrieval.
- Money receives readiness on day 44, explicit teaching on day 48 and retrieval in unit 6.
- The dollar representation is a Curio Class adaptation, not a claim about the public base lesson.
- Describe the nine unit and four course-level respond days, plus the named in-day reminders.

These corrections change no ownership or day count.

## Coverage and sequence judgments

| Requirement | Judgment |
|---|---|
| Order within units | Sound. Equivalence supports operations; place value supports larger computation; multiplication precedes division; rays and turns precede protractor work and angle equations. |
| Standards in full | All 27 owned rows and 34 leaf obligations have planned teaching placements. Lettered fraction and angle parts are carried by named work. |
| End-of-unit assessments | Generally explicit and appropriately distributed. Finding 1 concerns unit 6’s evidence placement. |
| Mid-unit assessments | Not applicable. No unit exceeds 25 days. |
| Response counted once | Met in the schedule. Saved products feed one combined unit response. |
| Course checks avoid repetition | Met at planning level. Checks 1 and 2 use earlier-unit contexts; check 3 reuses recent geometry products and changes the new task form. |
| Candidate cells | Met. Nine progression checks retained within existing days; nine optional extensions dropped with reasons. |
| Source map | Met. All 149 base lessons have unique dispositions: 60 keep, 64 split, 10 merge and 15 cut, plus 31 original slots. Retained source order is preserved. |
| Shorter year | Met. Ten named fold-ins preserve first teaching, owned parts, assessments and responses. |
| Shorter period | Present and generally actionable; day 100 needs the explicit correction in finding 3. |
| Stale notes | Automated check passed; finding 4 identifies semantic contradictions outside its coverage. |

The teaching/application allocations are **6, 15, 17, 9, 17, 17, 13, 13 and 20 days** across units 1 to 9, before their dedicated check and respond days. Their differing loads justify the distribution. I found no other unit clearly far over or under its load.

## Readiness and calendar

The sequence-writing rule counts explicit teaching or assessment as last use, excluding passing retrieval. On that basis, the prerequisite records support the planned distinction; I found no firm year-before readiness error requiring another finding.

| Receiving unit | Treatment |
|---|---|
| 1 | Grade 3 facts retrieved inside day 1 |
| 2 | Grade 3 fractions and partitions retrieved inside lessons |
| 3 | Grade 3 and same-year fraction work retrieved |
| 4 | Grade 2 money readiness on day 44 |
| 5 | Grade 2 representation/comparison readiness on day 57 |
| 6 | Grade 2 unit-size readiness on day 76; money retrieved after day 48 teaching |
| 7 | Grade 3 patterns, facts, properties and area reasoning retrieved |
| 8 | Grade 3 and same-year prerequisites retrieved |
| 9 | Grade 2 circle readiness on day 127; Grade 3 shape/fraction work retrieved inside lessons |

All four readiness slots immediately precede their receiving units. None occupies a unit opener.

Checks fall in target weeks **12, 23 and 31**, with no Grade 4 stagger conflict. The incoming writing and vocabulary leans have bridges on days 19/21 and 77. The outgoing science and social studies timing statements agree with the calendar, including the early scale-bar, wave, measurement and light-path bridges.

## Mathematics lens checklist

| Scope and sequence checklist line | Result |
|---|---|
| Every standard completed beyond merely naming it | Met for teaching; assessment placement needs finding 1 |
| Problems deliberately join units | Met: mixed-number exchanges, measurement/comparison, rectangle formulas and fractional lengths |
| Fluency receives spaced, mixed practice | Met: facts from the start, Grade 4 algorithms after teaching, then fractions/decimals and explained products/quotients |

All eight practices have named task placements and planned assessment connections. The major-work time claim needs finding 2. High-school and beyond-Algebra-2 provisions are not applicable.

## Settled by the expert

Recommendations for the caller to apply, with no edits made during this read.

| Choice | Reason | File affected |
|---|---|---|
| Keep all nine units and their order | The mathematical dependencies are sound | Scope and sequence |
| Save a brief mass-problem product on day 90 | Supplies the predictable gap in the unit 6 archive | Scope and sequence; days.csv |
| Identify the retained liquid-volume evidence explicitly | The money substitution must preserve that context | days.csv; source-map.csv |
| Replace blanket major-work credit with named task minutes | Makes the focus claim reproducible | Scope and sequence |
| Use the revised 60- and 45-minute day 100 budgets | Preserves prerequisites and an exit ticket within the period | days.csv; source-map.csv |
| Synchronize readiness, money-source and response notes | Prevents superseded directions from returning | Frame; progression; mathematics approach |

## What is right and should remain

Keep the fractions-first structure, one number line across fractions and decimals, partitioning explanations for equivalence, explicit mixed-number exchanges, and the separation of decimal notation from decimal computation. These choices fit the [fractions progression](https://mathematicalmusings.org/wp-content/uploads/2018/08/ccss_progression_nf_35_2018_08_10.pdf). The number-line emphasis is also consistent with the [federal fractions guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/15/Published).

Keep the full angle-equation days, explicit division-zero day, distributed geometry evidence and protections against reusing answer-bearing examples.

## Sources and limits

Additional sources consulted:

- [Base curriculum scope and sequence](https://im.kendallhunt.com/k5/teachers/grade-4/course-guide/scope-and-sequence.html): base order and unit dependencies.
- [Comparison curriculum map](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum%20Map/EM_GPK5_CurriculumMap.pdf): alternative allocation and order, used as reference only.
- [Grade 4 focus document](https://achievethecore.org/content/upload/SAP_Focus_Math_4.pdf): major, supporting and additional cluster classifications.
- [Mathematics review criteria](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Review%20Criteria_2.0.pdf): focus, assessment and rigor expectations.

The compiled 2023 Progressions exceeded the web tool’s size limit. I used the accessible 2018 fractions document for direct fraction verification; unreopened compiled-page references remain repository-derived.

Items, keys and detailed scoring guides are intentionally unwritten at this layer. This review therefore judges planned coverage and directions, not item correctness, classroom timing or delivered learning.

**For the source list:** Add the public base lesson 5.14 link as a specific pointer for mass and capacity evidence.

## For Cory

- No new scope, money, people or audience decision is required for these fixes.

**Verdict:** Sound mathematical order; revise assessment evidence, minute accounting and conflicting directions before unit-plan production.  
**Finding count:** 4.  
**Report path:** `docs/reviews/sequence-math-grade-4-2026-11-15.md`, supplied inline, not written.

