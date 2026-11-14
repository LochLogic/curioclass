# Expert cold read: Kindergarten Math course frame

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/frame-math-kindergarten-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files written.

## Verdict

The frame has a sound mathematical sequence, places all 20 kindergarten progression skills, and provides a coherent handoff to Grade 1. Its biggest risk is the claim that major-work emphasis has been established, although its lesson classifications do not establish instructional time. Revise that calculation and the inaccurate measurement rationale before using the frame to commission unit plans.

**Finding count: 7.**

## What I read and checked

- The kindergarten frame in full, its `frames.csv` entry, and all kindergarten math progression rows.
- The Grade 1 math frame and receiving progression rows. Kindergarten has no preceding course.
- The expert instructions, math lens, rubric, foundation, teaching approaches, source register, base-text rules, glossary, and relevant roadmap and baseline provisions.
- Relevant earlier progression, cross-subject, frame, and math planning reviews, including their fix reports.
- Kindergarten science and social studies frames, plus the relevant portions of the kindergarten ELA frame, which appeared during this review.
- The base text’s course sequence, all eight lesson inventories, preparation-file standards classifications, and selected lesson narratives and activities.

`data/plans/math-kindergarten/source-map.csv` does not exist. This is appropriate at this layer: the frame-writing contract explicitly postpones that file until the scope and sequence. The inline source map was reviewed instead.

| Required check | Result |
|---|---|
| Repository-wide `plan.py check` | Latest completed run: exit 0 |
| Kindergarten frame | 0 failures |
| Math progression | 305 rows, 0 failures |
| `stale.py check` | Latest run: 56 files, 0 failures |

The ordinary plan command initially stopped because the installed Python lacks `markdown`. The completed run supplied an in-memory import placeholder that would raise an exception if rendering were requested. No checking function was changed, no rendering occurred, and no dependency was installed.

Two unrelated frame failures appeared during the session and were corrected in the repository before verification. They are not current findings.

## Findings, most serious first

### 1. The major-work claim is not yet supported by an instructional-time calculation

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the earlier math progression and Grade 4 frame reviews distinguish content counts from instructional emphasis  
**Confidence:** firm

**Location:** Frame, “Major work” bullet and “For the lead,” item 5.

**What is wrong:** The frame counts every day outside units 3 and 7 and the two sorting lessons as major work. That credits all 18 days of unit 1, although its retained opening lessons include exploration of shapes and materials. Conversely, it excludes whole geometry units that deliberately include counting and number work.

The base-lesson count also uses the presence of a major-work standard as its test. A standard tag does not establish how much of a mixed lesson serves that standard. For example, the retained geoblock exploration addresses geometry while building toward counting; a later shape-building lesson explicitly reinforces counting. [Opening geoblock lesson](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-1/lesson-4/preparation.html), [later shape-building lesson](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-7/lesson-1/preparation.html).

The evidence guide asks for instructional minutes when a lesson equals a day, alongside unit and lesson perspectives. It also permits credit for supporting work connected to major work. [Evidence guide, indicator 1e](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf).

**Why it matters:** The stated margin is only four 60-minute day equivalents: 124 credited days against the 120 needed for 75 percent. Classification choices could materially change that result.

**Exact fix:** Replace the assertion of established compliance with a provisional allocation. Add a minute estimate covering retained lessons, centers, counting routines, added lessons, and assessments. Identify the mathematical work earning each allocation. At the stated 9,600-minute annual budget, demonstrate at least 7,200 minutes devoted to major work and connected supporting work. Reconcile the unit and lesson counts with that calculation before declaring the margin secure.

This finding does **not** establish that the course falls below 75 percent.

### 2. Two added lessons are justified by a base-text omission that does not exist

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** new  
**Confidence:** firm

**Location:** Unit 3 rationale, inline source map’s two added lessons, and “For the lead,” item 5.

**What is wrong:** The frame says the base text has no lesson on comparing lengths directly. Retained lesson K.3.6 compares lengths of rectangles; retained lesson K.3.7 explicitly teaches comparison by aligning endpoints. [Lesson 6 preparation](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-6/preparation.html), [lesson 7 preparation](https://im.kendallhunt.com/k5/teachers/kindergarten/unit-3/lesson-7/preparation.html).

**Why it matters:** The writer is being directed to fill a nonexistent gap, while the frame presents the resulting allocation as evidence-based necessity.

**Exact fix:** Correct all three references. Keep unit 3 at 19 days, but describe the two added lessons as deliberate consolidation:

1. Describe several measurable attributes of one familiar object, then select the attribute being compared.
2. Compare lengths and heights using varied objects, including misleading arrangements that require aligning endpoints.

The first emphasis explicitly protects the single-object requirement of K.MD.A.1. Both stay within the standards already assigned to unit 3. [Official kindergarten standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf).

### 3. Moving centers into tomorrow’s warm-up does not establish a 45-minute path

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier frame reviews require explicit and workable time assumptions  
**Confidence:** firm on the budget; judgment call on the eventual shorter path

**Location:** “For the lead,” item 1.

**What is wrong:** The proposed arrangement moves each day’s centers into the following morning’s warm-up without budgeting their duration or preserving that morning’s counting and review. Kindergarten centers commonly occupy 15 to 25 minutes, while established warm-ups generally take 5 to 10 minutes. [Base-text lesson structure](https://im.kendallhunt.com/k5/teachers/teacher-guide/a-typical-im-lesson.html).

Across 160 days, reducing a 60-minute allocation to 45 minutes removes 2,400 minutes. Those minutes need an explicit disposition.

**Why it matters:** A teacher could accept the apparent accommodation and then lose sustained practice or accumulate unfinished activities.

**Exact fix:** Replace the sentence with:

> The standard classroom path budgets 60 minutes daily, including centers. Scheduling centers separately requires an explicitly budgeted additional block. A 45-minute total daily path requires a separate pacing allocation that preserves counting, fluency practice, instruction, synthesis and daily evidence.

The audience decision belongs to Cory, listed below.

### 4. The cross-subject introduction still treats existing frames as future work

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale-status findings recur in earlier frame reviews  
**Confidence:** firm

**Location:** Kindergarten math frame, lines 124 to 126.

**What is wrong:** The introduction says the other subjects’ frames are written later. Kindergarten ELA, science and social studies frames now exist.

**Why it matters:** The sentence leaves a completed coordination opportunity described as a future dependency.

**Exact fix:** Replace the introduction with:

> Kindergarten ELA, science and social studies frames now exist. Their teaching points and bridges have been compared below. Exact first-use dates remain to be coordinated in the scopes and sequences.

Update the availability tables from those current frames.

### 5. The lens’s missing fluency-check page claim is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, already identified in this frame’s “For the lead,” item 4, but unapplied  
**Confidence:** firm

**Location:** `docs/agents/lenses/math.md`, lines 65 to 66.

**What is wrong:** The lens says no page explains checking kindergarten to Grade 2 counting and fluency without a timer. The kindergarten and Grade 1 frames now describe observation in games and individual checks, with recorded strategy categories.

**Why it matters:** Every subsequent reviewer is instructed to investigate an already documented procedure as an absent one.

**Exact fix:** Replace the gap with:

> The K to 2 frames describe counting and fluency checks through observation, games and individual listening. Unit plans must turn these procedures into tasks, recording guidance and instructional responses.

### 6. The lens’s missing handoff-work statement is outdated

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same stale-status type  
**Confidence:** firm

**Location:** `docs/agents/lenses/math.md`, lines 61 to 62.

**What is wrong:** The lens says progression pages exist only for grades 3 to 5 and that other bands still need the same handoff work. The assembled math progression now records K to 11 handoffs, band-edge notes exist, and course frames provide receiving-unit tables.

**Why it matters:** It confuses the absence of another document in the older format with the absence of the underlying progression work.

**Exact fix:** Replace those lines with:

> The grades 3 to 5 reference page remains available. Other bands’ handoffs are recorded in data/progressions/math.csv, the band-edge notes and course-frame seam tables. Reviewers check their completeness and timing against the Progressions.

### 7. The earlier kindergarten social studies review needs a dated status update

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same stale-status type  
**Confidence:** firm

**Location:** `docs/reviews/frame-social-studies-kindergarten-2026-11-13.md`, lines 127 to 128 and 141.

**What is wrong:** The review says no kindergarten ELA, math or science frame exists and retains that absence as a review limitation. All three now exist.

**Why it matters:** A later worker could mistake the historical limitation for the current coordination status.

**Exact fix:** Preserve the original review and append a dated update beside those passages:

> Update, 2026-11-14: kindergarten ELA, math and science frames now exist. The earlier absence limitation is superseded. Compare their first-use teaching points and bridges during scope and sequence coordination.

## Coverage and coherence conclusions

**Owned skills:** All 20 kindergarten rows appear exactly once in the Skills column. Larger-number work is labelled as extension. No unlabelled ownership transfer to another grade was found.

**Standards in full:** Reading the frame together with its progression notes, I found no definite missing kindergarten standard or lettered part. Counting arrangements and limits, zero, category ordering, the kindergarten story-problem types, decompositions, partners of ten, teen structure, direct comparison, and geometry are represented. This establishes planned coverage, not completed lesson or assessment coverage.

**Units and order:** Counting precedes operations; decomposition precedes teen-number work; the ten-frame is introduced before its later applications. Unit 7 revisits composition and operations explicitly. Preserve the distinction between kindergarten’s ten individual ones and Grade 1’s ten as a unit. The standards’ counting and operations progression supports these foundations and handoffs. [Counting and operations progression](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf).

**Days:** The allocations are 18, 26, 19, 20, 17, 16, 15 and 23 days: 154 unit days plus four course-check days and two respond days. This fits the repository’s 160-day yardstick. No unit is clearly excessive or inadequate solely from its skill count: unit 1 establishes classroom routines, unit 2 carries substantial number work, and unit 8 consolidates learning. Findings 1 to 3 qualify the claimed allocation evidence.

**Source map:** The base inventories contain 137 lessons. The inline map places 136 and cuts one with a reason; its additions and assessment days reconcile with the unit totals. The measurement move and earlier ten-frame introduction have stated reasons. No reference-only or noncommercial source is mapped for adaptation.

**Seams:** There is no incoming course. The recorded kindergarten handoffs match Grade 1 assumptions and its receiving units. The acknowledged proposal to connect `mk-one-to-one` directly to `m1-count-to-120` is a useful documentation refinement.

**Cross-subject:** ELA unit 1 supplies sorting language and read-aloud questioning before the stated math uses. Science begins some comparisons and weather recording earlier, but its frame supplies direct-comparison and teacher-counting bridges. Social studies teaches position words locally and uses unit-value tokens. No unbridged future prerequisite was found. Exact dates still require coordinated scopes and sequences.

## Math lens checklist: course-frame layer

| Lens line | Result |
|---|---|
| Major work meets the required emphasis | **Missed as demonstrated evidence:** nominal unit/day counts pass; instructional-time verification remains open, finding 1 |
| Supporting clusters practise major work | **Met at frame level:** sorting counts and compares; composition counts pieces; later shape work revisits number and operations |
| Every mapped source lesson has a disposition | **Met at frame level:** all base lessons kept, moved or cut; added lessons identified; rationale correction required by finding 2 |

All eight mathematical practices appear among the candidates. Actual tasks, rigor balance, assessment coverage and daily exits remain later-layer judgments.

## What is right and should remain

- Daily counting and spaced fluency practice, with individual observation.
- Explicit counting limits and arrangements.
- Objects, drawings and written representations connected together.
- Kindergarten story-problem boundaries and the Grade 1 handoff.
- A complete paper route and practical alternatives for participation.
- Reasons for adapting the base sequence instead of silently changing it.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep unit 3 at 19 days; redefine its two added lessons as specified in finding 2 | Preserves consolidation while correcting the source claim | Kindergarten frame |
| Include several attributes of one object in the first added measurement lesson | Protects the full K.MD.A.1 requirement | Kindergarten frame, unit 3 and source map |
| Retain the early ten-frame introduction | Later units explicitly use it | Kindergarten frame |
| Add the reciprocal one-to-one counting link already proposed by the frame | Makes the Grade 1 counting dependency explicit | `math.csv`, `mk-one-to-one` and `m1-count-to-120` |
| Treat major-work percentages as provisional until minutes are reconciled | Prevents an unsupported completion claim | Kindergarten frame |

## For Cory

- **Audience and time:** Confirm whether the classroom audience assumes 60 minutes daily or must also be served within 45 total minutes. The current sentence does not provide the latter path.

## Sources and limits

Sources were read for sequence, standards, emphasis and instructional design, without importing reference-only wording or problems.

- [Official mathematics standards](https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf): kindergarten requirements and Grade 1 boundaries.
- [Counting and operations progression](https://commoncoretools.files.wordpress.com/2011/05/ccss_progression_cc_oa_k5_2011_05_302.pdf): cardinality, operations, problem types and handoffs.
- [Kindergarten focus document](https://achievethecore.org/content/upload/SAP_Focus_Math_K.pdf): major work and required fluency.
- [K to 8 publishers’ criteria](https://achievethecore.org/content/upload/Math_Publishers_Criteria_K-8_Spring_2013_FINAL.pdf): focus, supporting work, rigor and progression.
- [Math evidence guide](https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf): the 75 percent threshold and multiple measurement perspectives.
- [Base-text kindergarten sequence](https://im.kendallhunt.com/k5/teachers/kindergarten/course-guide/scope-and-sequence.html): unit structure, purposes and review.
- [Second curriculum’s overview](https://greatminds.org/hubfs/knowledge/resources/math/EM_Basic_Curriculum_Files/Curriculum_Overview/EM_GPK5_CurriculumOverview.pdf): independent comparison of kindergarten sequence, comparison language and teen-number development.
- [Teaching Math to Young Children](https://ies.ed.gov/ncee/wwc/PracticeGuide/18): developmental progressions and progress monitoring; these recommendations do not validate this course’s exact pacing.

The compiled Progressions PDF could not be retrieved successfully; the accessible counting and operations draft was used. Classroom pacing, actual assessment coverage and instructional outcomes could not be judged from a frame. Prior memory informed report organization only; no curriculum finding rests on personal memory.

**For the source list:** Retain the direct lesson 6 and lesson 7 preparation links above as evidence that the base text already teaches direct length comparison.

**Final verdict:** Revise before unit planning. **Finding count:** 7. **Report path:** `docs/reviews/frame-math-kindergarten-2026-11-14.md`, supplied here, not written.

