# Independent frame review: Math Grade 8

Date: 2026-11-14  
Intended report path: `docs/reviews/frame-math-grade-8-2026-11-14.md`  
Delivery: Markdown report supplied here. No files changed.

## Verdict

The frame is broadly sound but needs revision before the scope and sequence is built. Its strongest features are complete skill placement, a coherent geometry-to-algebra progression, and a justified move of the data unit ahead of science’s need for it. The most important change is to adapt the moved lessons and their cumulative practice so they require only mathematics already taught.

## What I read and checked

- `docs/agents/EXPERT.md`, the mathematics lens, `RUBRIC-MATH-K8.md`, the foundation, teaching approaches, relevant roadmap and baseline rules, glossary, source register, and frame-writing brief.
- The complete Grade 8 frame, its `frames.csv` row, all 24 Grade 8 progression rows, and the relevant incoming and outgoing progression links.
- The Grade 7 and Algebra I frames, plus Geometry’s receiving units and seams.
- Same-year science, civics, and relevant ELA frame entries.
- The inline source map against the first-edition base text’s 131 lesson files, lesson metadata, optional designations, dependency diagram, and selected lesson and practice content.
- Earlier Grade 8 reviews, related mathematics frame and progression reviews, and the Grade 4 progression and worked planning pattern.

The requested day-level `source-map.csv` does not exist. The frame-writing brief explicitly assigns that file to the scope and sequence stage, so its absence is not a finding.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py check math-grade-8` | Passed: zero failures; 154 unit days plus 6 course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The incomplete plan gate is an environment limitation. Following the supplied amendment, it does not withhold this verdict.

## Findings, most serious first

### 1. The moved data lessons retain prerequisites that now come later

**Severity:** Major  
**LAYER:** base text  
**REPEAT:** yes, earlier Grade 8 review, finding 1  
**Confidence:** firm

**Location:** [frame.md, unit 4](/S:/CurioClass/docs/courses/math-grade-8/frame.md:107), its source-map row, and `m8-scatter-plots` in `data/progressions/math.csv`.

**What is wrong:** The source map keeps lessons 8.6.1 to 8.6.10 without specifying the prerequisite changes their move requires. Lesson 8.6.1 compares a scatter plot with a function; lesson 8.6.2 asks students to judge whether a relationship is a linear function. Functions are formally taught in this frame’s unit 6. The retained practice also includes systems from base unit 8.4, which now falls later, and material from cut lessons 8.5.17 and 8.5.18. These are actual dependencies in the materials, despite the dependency chart permitting the unit move. See [lesson 8.6.1](https://im.kendallhunt.com/MS/teachers/3/6/1/index.html), [lesson 8.6.2](https://im.kendallhunt.com/MS/teachers/3/6/2/index.html), and [practice 8.6.6](https://im.kendallhunt.com/MS/teachers/3/6/6/practice.html).

**Why it matters:** A writer following “keep” can ask students to use untaught definitions and solving methods. The progression note that this unit practises functions reinforces that mistake.

**Exact fix:**

- Retain unit 4’s position.
- Add to its source-map notes: “Adapt function-dependent prompts and summaries to relationships, lines, equations, slope and intercept already taught in unit 3. Replace cumulative practice requiring base units 8.4 or 8.5, including cut lessons, with review of our units 1 to 3.”
- Add to unit 6: “Return to unit 4’s fitted lines when naming linear functions.”
- Replace the progression note “practises the linear functions of 8.F” with “practises the linear relationships of 8.EE.B; function terminology is connected later.”

### 2. Two full-standard commitments are missing from the unit descriptions

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, earlier Grade 8 review, finding 2  
**Confidence:** firm

**Location:** [unit 1](/S:/CurioClass/docs/courses/math-grade-8/frame.md:104) and [unit 8](/S:/CurioClass/docs/courses/math-grade-8/frame.md:111).

**What is wrong:** Unit 1 names triangle angle sums and alternate interior angles but omits an informal argument for a triangle’s exterior-angle relationship. Unit 8 omits estimating expressions involving irrational numbers. Both performances belong to the owned standards. See the [official mathematics standards, printed pages 54 and 56](https://www.thecorestandards.org/wp-content/uploads/Math_Standards.pdf).

The second omission is a frame-description gap, not absent base instruction: retained [lesson 8.8.10](https://im.kendallhunt.com/MS/teachers/3/8/10/index.html) already includes estimating a sum of square roots. The earlier report’s wording that this is “not taught” is too strong.

**Why it matters:** A unit writer could preserve the headline topics while dropping a required performance during adaptation.

**Exact fix:**

- Unit 1: add “Informally justify the exterior-angle relationship for a triangle and the angle relationships formed by a transversal of parallel lines.” Add an explicit exterior-angle argument to the adaptation notes for 8.1.16.
- Unit 8: add “Use rational approximations to compare irrational numbers and estimate expressions involving them, including a sum of square roots.” Explicitly retain that purpose of 8.8.10’s opening task.

Neither correction moves a standard between units.

### 3. The course-wide promise of additional check and practice days exceeds some units’ allowances

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, related day-allocation findings in the earlier Grade 8 and Grade 6 reads  
**Confidence:** firm

**Location:** [course days](/S:/CurioClass/docs/courses/math-grade-8/frame.md:12) and [source-map allowances](/S:/CurioClass/docs/courses/math-grade-8/frame.md:169).

**What is wrong:** The introduction describes additional mid-unit check, respond and mixed-practice days in major-work units. Units 1 and 2 have only three additional days each. Unit 1 already assigns those to readiness, assessment and response. Units 7 and 8 have four additional days, enough for two check-and-response pairs but no separate mixed-practice day.

**Why it matters:** Writers cannot honor all the stated promises as separate days while retaining the listed lessons and totals.

**Exact fix:** Preserve the totals and distinguish embedded checks from dedicated days:

| Unit | Additional days | Allocation |
|---|---:|---|
| 1 | 3 | Readiness; end-of-unit assessment; respond day. Short mid-unit check and response embedded in retained lessons. |
| 2 | 3 | Readiness; end-of-unit assessment; respond day. Short mid-unit check and response embedded in retained lessons. |
| 3 | 5 | Mid-unit check; respond; mixed practice; end-of-unit assessment; respond. |
| 4 | 4 | Readiness/practice; mid-unit check with targeted response in the same period; end-of-unit assessment; respond. |
| 5 | 5 | As unit 3. |
| 6 | 5 | As unit 3. |
| 7 | 4 | Mid-unit check; respond; end-of-unit assessment; respond. Readiness embedded in the opening lesson. |
| 8 | 4 | As unit 7. |

Rewrite the course-wide statement accordingly. Daily openings carry mixed practice where there is no dedicated practice day.

The earlier report’s proposed unit 4 correction lists five days inside a four-day allowance. Do not apply that wording unchanged.

### 4. “Six wholly major units” is an incorrect focus claim

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 8 review, finding 6  
**Confidence:** firm

**Location:** [major-work bullet](/S:/CurioClass/docs/courses/math-grade-8/frame.md:25).

**What is wrong:** Only units 1, 2, 3, 5 and 7 are wholly major by their owned clusters. Unit 8 includes supporting number-system work; unit 6 includes additional volume work.

**Why it matters:** The inaccurate claim obscures an otherwise strong focus case. The evidence guide permits explicitly connected supporting work in focus calculations; it does not require misclassifying that work as wholly major. See [indicator 1e, PDF pages 13 to 15](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf).

**Exact fix:** Replace the unit count with:

> Five of eight units own only major clusters. Unit 8 connects supporting irrational-number work to the Pythagorean theorem; unit 6 connects volume to functions; unit 4 applies linear relationships to data.

Keep the 129-day figure explicitly provisional until the scope and sequence supplies its allocation calculation.

### 5. The receiving-frame introduction is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, both earlier Grade 8 reads  
**Confidence:** firm

**Location:** [outgoing seams introduction](/S:/CurioClass/docs/courses/math-grade-8/frame.md:66).

**What is wrong:** It says the Algebra I and Geometry frames are unwritten. Both exist and identify receiving units.

**Why it matters:** The note gives a false reason to postpone checking the handoffs.

**Exact fix:** Replace it with:

> Handed on to Algebra I and Geometry. Their frames identify the receiving units.

Add the receiving unit numbers already established there: Algebra I units 2 to 7 as applicable; Geometry units 1 to 7 as applicable. Preserve the explicit unresolved proportional-comparison link in “For the lead.”

### 6. The explanation of the scientific-notation handoff is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier independent Grade 8 review, finding 3  
**Confidence:** firm

**Location:** [scientific-notation seam](/S:/CurioClass/docs/courses/math-grade-8/frame.md:81) and [lead item 6](/S:/CurioClass/docs/courses/math-grade-8/frame.md:156).

**What is wrong:** Both explain the missing handoff by saying N-Q.A.3 has no progression row. It is currently owned by `geo-solving-right-triangles` and begun in `alg1-scatter-linear-models`.

**Why it matters:** A fixer could create unnecessary ownership work instead of examining the actual missing link.

**Exact fix:** Replace both explanations with:

> `m8-scientific-notation` has no outgoing progression link. N-Q.A.3 already has ownership and introductory placements. Decide whether scientific notation has a substantive receiving skill or whether this thread ends here; precision ownership alone does not establish that handoff.

Do not automatically add a link merely because the precision code exists.

### 7. The rubric’s practices gap contradicts existing plans

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale-status class in earlier frame reads  
**Confidence:** firm

**Location:** [rubric, practices row](/S:/CurioClass/docs/RUBRIC-MATH-K8.md:34).

**What is wrong:** It says practices are absent from the plan and no unit names one. The target frame names all eight across its units. The Grade 4 worked plan also names practices and associated tasks.

**Why it matters:** The note confuses the remaining implementation check with work already completed.

**Exact fix:** Replace the gap statement with:

> Practices are named in course frames and existing unit and section plans. Verify that each named practice has a task that develops it and that each completed course covers all eight.

### 8. The rubric still lists writing the sourced approach as unfinished

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, Grade 5 independent rerun review  
**Confidence:** firm

**Location:** [rubric, teacher-supports row](/S:/CurioClass/docs/RUBRIC-MATH-K8.md:35).

**What is wrong:** “The approach written down with sources” remains a gap, although the shared approach, mathematics approach and source register exist.

**Why it matters:** It directs later workers to recreate an existing foundation.

**Exact fix:** Replace that phrase with:

> The shared and mathematics approaches are written with sources. Course materials must explain and demonstrate their implementation.

This correction makes no claim about approval or classroom outcomes.

### 9. The required Grade 4 worked pattern contains stale writing-status statements

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Grade 3 and Grade 4 frame reviews identify this stale-status class  
**Confidence:** firm

**Location:** [math-4-spine.md, “What is missing today”](/S:/CurioClass/docs/courses/math-4-spine.md:340) and [closing paragraph](/S:/CurioClass/docs/courses/math-4-spine.md:363).

**What is wrong:** It says no section is written, all 150 days are gap days, shelves are not matched to sections, and the pilot will be written next. Written days, section plans and linked support materials now exist, including `courses/math-4/u11-1/d089.md` through `d093.md`, its opener, readiness sheet, family note and record.

**Why it matters:** The lens sends writers to this pattern, whose status summary misrepresents the available examples.

**Exact fix:** Replace those statements with:

> Written section plans, lesson days and linked support materials exist for portions of the course, including section 11.1. Use the current plan data and course folders to identify remaining unwritten days and unmatched materials. Written files do not by themselves establish readiness, live coverage or classroom use.

Remove “Then the pilot, section 11.1, is written.” Preserve any separate unfinished-work claim unless current evidence specifically closes it.

## Coverage, sequence, days and seams

| Check | Conclusion |
|---|---|
| Owned skills | All 24 Grade 8 rows are placed exactly once. |
| Owned codes | All 36 codes, including lettered parts, match the units’ ownership lists. |
| Other-grade work | Earlier skills are identified as prerequisites or brief rebuilding. No unjustified ownership transfer found. |
| Standards in full | Finding 2 identifies the remaining explicit commitments. No further substantive omission established. |
| Models | All ten progression models are represented. Finding 1 concerns prerequisite language and practice within moved lessons. |
| Unit order | Transformations support similarity, which supports slope and linear relationships. Equations precede systems. Exponents precede roots. |
| Source completeness | 131 base lessons accounted for: 121 retained and 10 optional cuts. |
| Source rights | The map uses the permitted first edition. No reference-only or non-commercial source is mapped. |
| Incoming seam | Grade 7’s relevant handoffs are picked up. Older symmetry, exponent and coordinate threads have explicit re-entry provisions. |
| Outgoing seam | Receiving units exist and broadly match. Findings 5 and 6 correct the status account; proportional comparison remains an acknowledged link repair. |

The unit allowances are proportionate to their retained base lessons:

| Unit | Retained base lessons | Additional days | Total |
|---|---:|---:|---:|
| 1 | 17 | 3 | 20 |
| 2 | 13 | 3 | 16 |
| 3 | 14 | 5 | 19 |
| 4 | 10 | 4 | 14 |
| 5 | 16 | 5 | 21 |
| 6 | 19 | 5 | 24 |
| 7 | 16 | 4 | 20 |
| 8 | 16 | 4 | 20 |
| **Total** | **121** | **33** | **154** |

Six course-level days produce 160 periods, leaving approximately 20 days in a nominal 180-day school year. No unit is demonstrably far over or under its load. Finding 3 concerns conflicting promises within those allowances.

Cross-subject timing works at frame level:

- Math’s data unit finishes on day 69, before science units 4 and 5, days 78 to 130.
- Science’s early graph work precedes formal functions but provides its own qualitative bridge.
- Science’s space context precedes scientific-notation instruction, with an earlier-grade alternative already stated.
- Civics’ polling work, approximately days 52 to 63, precedes math’s two-way-table work.
- Grade 7 argument writing precedes the congruence arguments.

The current science dates can replace the math frame’s provisional requests. Their availability does not require another unit move.

## Mathematics lens checklist

| Course-frame line | Result |
|---|---|
| Major work meets the focus line by units, lessons and time | **Met provisionally, with finding 4.** Supporting connections are explicit. Of 121 retained lessons, 103 carry some major-work tag; 98 carry an Addressing tag for major work. These are lesson indicators, not minute allocations. |
| Supporting clusters practise major work | **Met.** Data uses linear relationships; irrational numbers support Pythagorean work. |
| Every source-map row has a decision | **Met.** Required adaptation qualifications are finding 1. |
| Prerequisite skills and models precede use | **Missed in the retained moved materials**, finding 1. The frame’s larger sequence holds. |
| Grade ownership and limits respected | **Met**, subject to the full-standard wording correction in finding 2. |
| Detailed task, assessment and daily-instruction checks | **Not applicable at this layer.** They remain obligations of later plans. |

## What is right and should not be touched

Keep the geometry-to-slope progression, the data unit’s fourth position, and volume’s connection to functions. Preserve daily mixed practice, untimed student-facing tools, paper alternatives, neutral data contexts, and the explicit restriction on radius problems before roots.

The second curriculum comparison confirms that a different order can also be coherent. It does not establish a reason to replace this frame’s chosen backbone.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Retain the data unit in fourth place | The dependency chart permits it and science needs it before the original placement would supply it | Grade 8 frame |
| Adapt prerequisite language and cumulative practice | A permitted unit move does not automatically adapt its lessons | Frame source-map notes; progression note |
| Make the two standard commitments explicit | Preserves existing ownership and completes the unit-writing contract | Frame units 1 and 8 |
| Keep the 160-day budget using finding 3’s allocations | Avoids adding a fifth day to a four-day allowance | Frame days and source map |
| Correct the wholly-major count to five | Matches the owned clusters | Frame focus bullet |
| Replace stale status notes | Existing files and progression ownership settle these factual questions | Files named in findings 5 to 9 |

## Relationship to earlier reads

The earlier Grade 8 curriculum findings remain open in the current frame and were independently rechecked here. This report narrows the earlier claim about irrational-expression instruction because retained lesson 8.8.10 already teaches it, and corrects the earlier unit 4 day proposal.

The earlier independent report withheld its curricular verdict over the missing dependency. The supplied amendment now directs a substantive read despite that environment failure; this report provides it.

## What I could not judge

Actual lesson minutes, the quality of unwritten checks, classroom pacing and assessment coverage cannot be established from a frame. The 129-day major-work estimate requires a transparent allocation in the scope and sequence.

The compiled Progressions PDF exceeded the web tool’s size limit, and the linked geometry draft could not be retrieved. I used accessible authors’ progression drafts, the official standards, local progression rows and base-text evidence. No curricular finding rests on memory; prior memory informed only the review format.

## Sources

- [Official mathematics standards](https://www.thecorestandards.org/wp-content/uploads/Math_Standards.pdf): full Grade 8 requirements, printed pages 52 to 56.
- [Authors’ Expressions and Equations progression](https://commoncoretools.files.wordpress.com/2011/04/ccss_progression_ee_2011_04_25.pdf): Grade 8 algebra prerequisites and limits, PDF pages 11 to 13; older draft used alongside current standards.
- [Authors’ Statistics and Probability progression](https://commoncoretools.files.wordpress.com/2011/12/ccss_progression_sp_68_2011_12_26_bis.pdf): bivariate-data progression, PDF pages 11 to 13; older draft.
- [Base-text scope and sequence](https://im.kendallhunt.com/MS/teachers/3/scope_and_sequence.html): pacing and dependency diagram; local lesson files supplied the inventory and adaptation evidence.
- [Second curriculum’s overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_G68_CurriculumOverview.pdf): Grade 8 sequence comparison, printed pages 24 onward; reference only.
- [Grade 8 focus document](https://achievethecore.org/content/upload/SAP_Focus_Math_8.pdf): cluster emphasis.
- [K to 8 publishers’ criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, coherence and rigor.
- [Mathematics evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): focus calculations and connected supporting work.
- [Federal algebra practice-guide summary](https://ies.ed.gov/ncee/WWC/Docs/PracticeGuide/wwc_algebra_summary_072115.pdf): preserving reasoning, representation structure and strategy comparison; not evidence for a particular unit-day count.

## For the source list

Record the working official standards PDF address above. Add the smaller authors’ progression drafts as fallback routes, clearly identifying their dates and draft status, and the grades 6 to 8 curriculum overview used for comparison.

## For Cory

- No new scope decision. The existing question of offering an accelerated Grade 8 pathway remains separate from this standard-path frame.

**Verdict:** Broadly sound; revise before building the scope and sequence. **Finding count:** 9. **Report path:** `docs/reviews/frame-math-grade-8-2026-11-14.md`, supplied here only.

