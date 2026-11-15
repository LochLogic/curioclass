# Independent sequence read: English Language Arts Grade 10

**Date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-english-language-arts-grade-10-2026-11-15.md`  
**Delivery:** Complete report supplied inline. No files changed.  
**Finding count:** 7.

## Verdict

The seven-unit sequence has a coherent instructional order, preserves three whole literary works, and coordinates its main cross-subject dependencies. It needs revision before unit planning because reading loads remain unbudgeted, several assessment descriptions do not secure their stated requirements, and the shorter-period route retains incompatible timings. Preserve the unit structure and repair those contracts within the existing days.

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the foundation, shared and ELA approaches, source-access notes, relevant roadmap passages, BASELINE rules 20 to 24, glossary, and sequence-writing rules.
- The complete Grade 10 scope and sequence, all 160 day rows, the frame, and the Grade 10 entries in `data/plans/ela-texts.csv`.
- All 26 Grade 10 ELA progression rows, adjacent-grade prerequisites and handoffs, and actual Grade 9 ELA day placements.
- The local grades 9 to 10 ELA standards, including lettered parts, beside the official standards.
- `docs/courses/CALENDAR.md`, Grade 10 calendar rows, and relevant Chemistry, World History II, Grade 7 history, Grade 8 civics, and Grade 9 history day rows.
- Earlier Grade 10 frame reports and the Grade 9 independent sequence report for repeat classification.
- Outside standards, review criteria, writing guidance, two curriculum comparisons, and the two federal cloning explanations linked below.

The blind-read exclusions were respected. Saved memory informed review boundaries and report format only. No curricular finding rests on memory.

### Gates

The repository-wide plan check reported zero Grade 10 ELA sequence failures, then stopped on another course path because `markdown` is unavailable; the structural fallback passed, and the verdict proceeds.

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Grade 10 ELA: zero sequence failures; full run subsequently stopped with `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; no stagger violation reported. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-10` | Passed: zero failures, seven units, 148 unit days plus 12 course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

No turn, synchronization, defect-logging, installation, or writing command was run.

## Findings, most serious first

### 1. Reading demand and completion time remain unresolved at the layer that allocates the days

**Severity:** Serious  
**LAYER:** sequence  
**REPEAT:** yes, Grade 10 independent frame finding 6 and Grade 9 sequence finding 1  
**Confidence:** Firm on missing records and budgets; likely on classroom fit

**Location:** “Reading, writing and evidence across the year”; “Shorter path”; “For the lead” item 2; the text catalogue.

**What is wrong:** The sequence defers exact editions, complexity records, independent-book choices and reading-minute budgets to unit planning. The course-specific `texts.csv` is absent. The shared catalogue contains useful titles and approximate lengths, but most prose measures remain “not on file,” several sources remain unselected, and original texts remain unwritten.

The catalogue estimates approximately 75,000 words for *Frankenstein* and 60,000 for *All Quiet*. The sequence also requires a long independent book in every unit, sharing existing reading and workshop blocks. It never supplies the required unit-by-unit totals for reading in class and at home.

These estimates do not prove that either novel is overlong. They do show why day counts alone cannot establish capacity, especially alongside seminars, vocabulary, conferencing and process writing. Text suitability also requires quantitative, qualitative, and reader/task evidence together. [Common Core Appendix A, printed pages 4 to 6](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf).

**Why it matters:** Unit writers could preserve the nominal schedule only by rushing reading, reducing writing instruction, or introducing unstated homework.

**Exact fix:** Before treating the sequence as ready for unit planning:

- Complete the anchor records with exact editions, selection boundaries, source locations, word counts, complexity analyses, supports and placement reasons.
- Name a free independent-book offer and completion expectation for each unit.
- Add a load table separating first reading, rereading, independent reading, writing, conferencing and any home reading.
- Give unwritten texts explicit length and complexity limits now, then replace estimates with actual records.
- Budget unit 7’s sustained work as eleven full allocations plus the fifteen-minute preparation block on day 140, rather than treating all twelve allocations as full periods.

Keep the present unit lengths provisionally. Any necessary transfer of days between units belongs to Cory. The sequence writer’s restricted file boundary explains the deferred records, but does not complete them.

### 2. Three units omit the cold end assessment required by the ELA approach

**Severity:** Serious  
**LAYER:** sequence  
**REPEAT:** yes, Grade 9 sequence finding 2  
**Confidence:** Firm

**Location:** Unit 2, days 39 to 41; unit 3, days 58 to 59; unit 7, day 155.

**What is wrong:** These end windows assess taught texts, retained products and existing dossiers. The sequence explicitly drops their cold science essay, translated story and source set.

`APPROACH-ELA.md`, under daily evidence and unit field 5, requires an end-of-unit assessment using a text not read in the unit. A later course-level check does not replace that local requirement. Retained process products and an unfamiliar reading can coexist; the Louisiana implementation guide provides a useful comparison by distinguishing culminating writing from cold reading. [Guidebooks implementation guide, PDF page 2](https://doe.louisiana.gov/docs/default-source/teacher-toolbox-resources/ela-guidebooks-overview-guide.pdf).

**Why it matters:** Writers following the sequence and writers following the approach would build different assessment systems.

**Exact fix:** Restore bounded cold reading within the existing windows:

| Unit | Day | Repair |
|---|---:|---|
| 2 | 40 | Use an unfamiliar science passage for the brief evidence, central-idea and development analysis. Retain the existing Huxley summary as whole-essay evidence. |
| 3 | 59 | Use an unfamiliar world-story passage beside a taught comparator. Retain day 58’s regional seminar and the punctuation strip. |
| 7 | 155 | Reserve ten minutes for a short unfamiliar source and graph comparison. Use existing products for the remaining criteria, then retain the fifteen-minute response. |

Reserve these passages from instruction. Keep the following course checks on earlier-unit content with different response forms. Reopen the corresponding candidate decisions.

This is a conflict with Curio Class’s written approach, not a claim that national standards require every unit assessment to be cold.

### 3. Several check descriptions leave required standard components unnamed

**Severity:** Serious  
**LAYER:** sequence  
**REPEAT:** yes, task-to-standard alignment faults in earlier ELA reads, including Grade 9 sequence finding 4  
**Confidence:** Firm on the incomplete descriptions

**Location:** Days 14, 82 and 136; unit 2’s end-window evidence.

**What is wrong:** The brief requires each check to name a prompt or retained performance for every component of its listed codes. A general promise that “all parts” receive evidence does not resolve these concrete gaps:

| Location | Listed requirement | Missing named evidence |
|---|---|---|
| Day 14 | `RL.9-10.2` | Emerging-theme responses are named, but an objective summary is not. |
| Day 82 | `L.9-10.5a`, `L.9-10.5b` | “Brief annotation” does not specify interpreting a figure’s role and analysing near-synonym nuance. |
| Day 136 | `RI.9-10.8` | Identifying reasoning is named; evaluating validity, relevance, sufficiency, false statements and fallacies is not. |
| Unit 2 end window | Seminar and word-strategy teaching on days 30, 32, 35 and 38 | No end row names reuse of the seminar observation or vocabulary-strategy record. |

The official standards distinguish these components. [Common Core ELA standards, printed pages 38, 40 and 55](https://corestandards.org/wp-content/uploads/2023/09/ELA_Standards1.pdf).

**Why it matters:** Successful completion of the named task could still leave a claimed assessment component unobserved.

**Exact fix:**

- Day 14: add a short objective summary of the novel so far.
- Day 82: specify one figure-in-context explanation and one near-synonym comparison; select a passage that supports both.
- Day 136: retain the independent-reading checkpoint under `RI.9-10.10`. Treat the reasoning identification as diagnostic, with full `RI.9-10.8` evaluation secured on days 140 and 155.
- Day 41: explicitly retain the existing seminar observation and word-log strategy evidence. Identify their criteria without collecting another full performance.

Apply the same component check to the final assessment blueprints. Missing repeated labels alone are not missing instruction; the issue here is an absent task or an absent retained-evidence reference.

### 4. The shorter-period route still contains fifty-minute days

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 9 sequence finding 5  
**Confidence:** Firm

**Location:** “Shorter path,” with days 60, 111, 140, 156 and 157.

**What is wrong:** The route offers forty-minute periods, but several specifications remain unchanged:

- Days 60 and 111: forty minutes of response plus ten minutes of readiness.
- Day 140: 25-minute check, ten-minute response and fifteen-minute preparation.
- Day 156: 35-minute literary reading/tasks plus fifteen-minute argument reading.
- Day 157: fifteen-minute nonfiction tasks plus 35-minute essay.

The ten named folds preserve assessed days, which is appropriate, but their receiving days also lack revised minute budgets.

**Why it matters:** Teachers cannot follow both the shorter route and the authoritative day notes.

**Exact fix:** Add explicit shorter-period exceptions. Provisional allocations to test are:

| Day | Forty-minute allocation |
|---|---|
| 60, 111 | Thirty minutes response, ten minutes readiness |
| 140 | Twenty minutes check, eight minutes response, twelve minutes preparation |
| 156 | Twenty-five minutes literary reading/tasks, fifteen minutes argument reading |
| 157 | Ten minutes brief nonfiction tasks, thirty minutes integrated analytic writing |
| 155 | Ten minutes cold comparison, fifteen minutes retained-evidence audit, fifteen minutes response |

Set passage lengths and response demands to these windows while retaining every assessed component. Give each fold destination a corresponding budget. Keep the shorter route provisional until the actual materials have been timed.

### 5. Two prerequisite retrievals occur after the row’s first use

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 9 sequence finding 6  
**Confidence:** Firm

**Location:** Unit 7, days 129/132 and 136/137.

**What is wrong:** Day 129 carries `e10-w-research` and `W.9-10.8` while students judge sources, but retrieval of `e9-w-short-research` is scheduled on day 132. Day 136 carries `e10-ri-argument-evaluate`, while retrieval of `e9-ri-argument-evaluate` occurs on day 137.

Both prerequisites were taught in Grade 9. Retrieval is the right treatment, but it should open their use.

**Why it matters:** The prerequisite table and first-use day map disagree, and a writer could assume that the earlier routine has already been reactivated.

**Exact fix:** Put the source-usefulness retrieval immediately before day 129’s source judgment. Put argument-evaluation retrieval into day 135 using an earlier source, preserving day 136’s unpreviewed reading. Keep day 132’s research-cycle retrieval as a later return.

Do not add readiness checks or move either unit.

### 6. The planned performed passage from the play has become a different speech

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Day 69; frame unit 4; progression row `e10-sl-presentation`.

**What is wrong:** The frame and progression require performing a speech from *Julius Caesar*. Day 69 instead names a short speech presenting the student’s claim about the play and painting. That is useful evidence-based speaking, but it does not name performance of the play’s language. No other day secures the omitted performance.

**Why it matters:** A requirement carried from the progression into the frame disappears during sequencing.

**Exact fix:** Keep the medium-comparison claim and add a brief performed excerpt from the already-read act III, scene 1, followed by an explanation of one delivery choice. Use paired rehearsal and the existing look-for sheet.

In the shorter-year route, explicitly carry this excerpt performance into day 70 alongside the existing speech-feedback fold. Do not claim that passage performance alone completes `SL.9-10.4`; retain the student’s evidence-based claim and the later research talk for that standard.

### 7. The handoff notes and frame retain obsolete instructions

**Severity:** Low  
**LAYER:** process  
**REPEAT:** yes, Grade 9 sequence finding 7 and earlier Grade 10 stale-note findings  
**Confidence:** Firm

**Location:** Prerequisite table and following paragraph; “For the lead” item 1; frame opening and Grade 9 seam paragraph.

**What is wrong:** During this read, Grade 9 ELA’s day map exists and provides teaching or assessment placements for all 24 incoming ELA rows. The sequence still describes that map as absent and every last-use claim as provisional.

The frame also continues to require first-day readiness on Grade 9 rows and calls the older cross-subject leans retrieval. The sequence correctly overrides those instructions, but the contradictory directions remain available to downstream writers.

**Why it matters:** A writer could reopen resolved handoffs or reintroduce readiness on the wrong days.

**Exact fix:** Replace the absent-map statements with current Grade 9 day references. At the next authorized frame update, align its wording with the implemented rule:

- Grade 9 ELA rows receive retrieval.
- The older history, civics and scatter-plot assumptions receive readiness immediately before their receiving units.
- Retain the genuine absence of the Grade 8 mathematics and Algebra I day maps as a separate limitation.

The stale-note gate does not detect these unmarked contradictions.

## Other required checks

### Order and days by load

| Unit | Days | Owned rows | Judgment |
|---|---:|---:|---|
| 1 | 28 | 9 | Coherent progression from evidence, character and structure into whole-novel writing. Reading and independent-book minutes remain unbudgeted. |
| 2 | 14 | 3 | Explanation development precedes comparison; narrative features precede final revision. Both reading and a 1,500 to 2,000 word narrative compete for ten teaching days. |
| 3 | 15 | 2 | Bounded selections improve the earlier frame. Cultural comparison precedes final writing and punctuation evidence. |
| 4 | 25 | 4 | Source comparisons and language instruction precede the full argument. No mid-unit assessment is required at exactly 25 days. |
| 5 | 22 | 1 | The whole novel and completion of the world-literature row justify the allocation. It is not excessive merely because ownership lists one row. |
| 6 | 16 | 2 | Document comparison precedes the issue argument; its process stages are named. |
| 7 | 28 | 5 | Four source days, four short-inquiry days, four argument days, twelve project allocations, three talk days and one closure day are accounted for. Day 140 is a partial project allocation. |

No defensible case for transferring days between units can be made without the missing reading budgets.

### Prerequisites and readiness

All 24 declared incoming ELA rows have Grade 9 teaching or assessment placements. They therefore receive retrieval, not readiness. This includes the literary rows, informational rows, analysis, three writing types, process, research, discussion, presentation, phrases/clauses, punctuation and word strategies.

| Older assumption | Last confirmed teaching | Treatment here |
|---|---|---|
| `ss7-republic-to-empire` | Grade 7, days 125 to 128; assessment day 132 | Day 60 readiness before unit 4 |
| `ss8-constitution-text` | Grade 8, days 31 to 35; assessment day 46 | Day 111 readiness before unit 6 |
| `m8-scatter-plots` | Grade 8 progression placement; later teaching unverified | Day 127 readiness before unit 7 |

Grade 9 history’s brief Constitution retrieval does not establish fresh teaching or assessment of the complete earlier row. The conservative readiness placement remains defensible. No readiness is placed on a receiving unit’s first day or weeks ahead.

### Assessment and calendar

- Units 1 and 7 exceed 25 days and have mid-unit assessments on days 14 and 140.
- Response time is counted once per window.
- The immediate course checks explicitly draw recently assessed skills from earlier-unit content.
- Check weeks 9, 18 and 32 match the frame and calendar. High school has no additional stagger restriction.
- History’s imperialism, interpretation and propaganda units precede their ELA uses.
- Chemistry’s forecast overlap is bridged on days 128 to 130. Its actual forecast deadline is day 129, after ELA’s day 126 argument.
- The paired research milestones match current history rows: draft day 148, report day 151, and ELA panels replacing history’s standalone talk.
- All fourteen candidate additions are dispositioned: two kept within existing days, twelve dropped. Finding 2 requires reopening three cold-reading decisions.
- No base curriculum is used. A base-lesson source map is not applicable.

## Lens checklist: scope and sequence

| Lens line | Status | Evidence |
|---|---|---|
| Reading demand develops across the year, with reasons | **Missed as demonstrated evidence** | Fading support and independent checkpoints are planned, but text-specific complexity records remain incomplete. |
| Research occurs more than once | **Met in the plan** | Two short inquiries and one sustained inquiry, all in unit 7. |
| Full-process writing occurs more than once | **Met** | Five process pieces, with modelling, feedback and revision. |
| Formal discussion occurs often | **Met** | At least two student-led seminars per unit, plus partner and teacher-led discussion. |
| K to 2 phonics and decodable alignment | **Not applicable** | Grade 10. |

The anchor and writing distributions are reported honestly. Their comparison figures are descriptive guidance, not automatic pass thresholds. [ELA evidence guide, indicators 2a and 2o](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Evidence-Guide.pdf).

## What is right and should remain

Keep the whole-work reading, *Frankenstein* before the two-narrator narrative, North beside the play, the trial/news comparison, and the movement from rhetoric through liberty documents into research.

Keep the independent-reading checkpoints separate from subsequent supported teaching. Preserve the explicit distinction between paper participation and unfinished digital standards, the reused conference records, and the single shared research product.

The named planning, drafting, feedback and revision stages are consistent with the secondary-writing guide’s explicit instructional cycle. [WWC secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22).

## Settled by the expert

These are recommendations for the caller to apply, not edits made during this read.

| Choice | Reason | File affected |
|---|---|---|
| Keep seven units and 160 days | Overall order and allocation are defensible | Scope and sequence |
| Keep the two federal cloning explanations | Both explain donor-cell nuclear transfer, providing comparable process material within different explanatory contexts | Text records; days 33 to 34 |
| Retain portfolios while restoring bounded cold reading | Preserves process evidence and the written assessment contract | Days 40, 59 and 155 |
| Move the two retrievals earlier | Aligns prerequisites with first use without adding days | Days 129 and 135 |
| Restore a brief performed play excerpt | Preserves the progression requirement within existing speaking time | Days 69 and 70 |
| Keep the ten named folds provisionally | None is an assessed day; destination budgets still need repair | Shorter path |

The cloning comparison is supported by the actual process passages in the [genome institute fact sheet](https://www.genome.gov/about-genomics/fact-sheets/Cloning-Fact-Sheet) and [federal livestock primer](https://www.fda.gov/animal-veterinary/animal-cloning/primer-cloning-and-its-use-livestock-operations). This settles comparability, not their rights records or grade-level complexity.

## What I could not judge

- Actual reading and writing capacity without finished text records and timed materials.
- Question-set percentages, scoring guidance and student supports that belong to later layers.
- Reliable assessment of every panel speaker. Three parallel panels fit the student presentation minutes, but the teacher’s observation rotation and supporting evidence remain unwritten.
- The finished originals, exact media selections, and pending rights and sensitivity reads.
- The full New York research-module PDF, which exceeded the web fetch size limit. No finding rests on its unread contents.

## Sources and comparison limits

- [Official ELA standards](https://corestandards.org/wp-content/uploads/2023/09/ELA_Standards1.pdf): checked the grades 9 to 10 requirements and lettered components.
- [Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): three-part complexity model, read in part.
- [ELA evidence guide](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Evidence-Guide.pdf): selected text, writing-distribution and research indicators.
- [WWC secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): recommendation summaries and evidence ratings.
- [Grade 10 course comparison](https://odell-uploads-staging.s3.amazonaws.com/release/materials/g10_courseataglance.pdf) and [research diagnostic lesson](https://access.openupresources.org/curricula/odell-hs-literacy/grade-10/application-unit/section-2/lesson-7/student.html): compared inquiry, process products and retained research evidence.
- [Louisiana high school overview](https://doe.louisiana.gov/docs/default-source/year-long-planning/ela-hs-gb-one-pager_july2020.pdf) and [implementation guide](https://doe.louisiana.gov/docs/default-source/teacher-toolbox-resources/ela-guidebooks-overview-guide.pdf): compared text-set coherence, culminating work, cold reading and time allocation. These historical documents were used as design comparisons.

### For the source list

Add or cross-reference the two curriculum comparisons and the working ELA evidence-guide address above. Record the oversized New York module as unread rather than treating its search excerpt as a completed source read.

## For Cory

- Confirm the joint research product only if that cross-course scope decision remains open.
- Any transfer of days between units, or reduction of the seven independent-book completion requirements, would change scope and needs Cory’s decision after the load budget is completed.

**Verdict: revision required. Findings: 7. Intended report path: `docs/reviews/sequence-english-language-arts-grade-10-2026-11-15.md`, supplied inline only.**

