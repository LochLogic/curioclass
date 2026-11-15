# Independent sequence read: English Language Arts Grade 9

2026-11-15. First-reader report, supplied inline. No files changed.

Requested report path: `docs/reviews/sequence-english-language-arts-grade-9-2026-11-15.md`

## Verdict

The eight-unit sequence has a coherent instructional order, recurring research and writing, and sound calendar coordination. It needs revision before unit planning because reading loads remain unsubstantiated, four units omit the locally required cold assessment text, and several day descriptions promise evidence or production time they do not secure. Preserve the unit structure while repairing those contracts.

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the glossary, and sequence-writing rules.
- The complete Grade 9 scope and sequence, all 160 `days.csv` rows, the frame, and Grade 9 records in `data/plans/ela-texts.csv`.
- All Grade 9 ELA progression rows, their Grade 8 prerequisites, relevant older language rows, and relevant Grade 10 limits.
- Grade 8 day placements, with targeted Grade 5 and Grade 7 language checks, to distinguish teaching and assessment from maintenance.
- `docs/courses/CALENDAR.md`, Grade 9 calendar rows, and Biology’s actual design-report placement.
- The foundation, shared and ELA approaches, BASELINE rules 20 to 24, relevant roadmap passages, and source-access notes.
- The local grades 9 to 10 standards, checked beside the official standards.
- Earlier Grade 9 frame reviews and Grade 8 sequence reviews for REPEAT classification.
- Outside standards, review criteria, writing guidance, two curriculum comparisons, and the assigned Butler epic books, linked below.

The blind-rule exclusions were respected. Saved guidance informed review boundaries and report structure only; no curricular finding rests on memory.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Grade 9 ELA reported zero sequence failures; the full run subsequently stopped because the environment lacks `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Passed, with no reported stagger violation. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-9` | Passed, zero failures: 148 unit days plus 12 course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The incomplete full gate does not withhold the verdict.

## Findings, most serious first

### 1. Reading-load dependencies remain unresolved at the layer that allocates the days

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** yes, Grade 9 independent frame finding 1 and Grade 8 sequence reading-load finding  
**Confidence:** firm on missing records and counts; likely on classroom fit

**Location:** “Reading, writing and recurring time,” unit 2, “Shorter path,” and “For the lead” items 1 and 2.

**What is wrong:** The scope openly defers exact selections, word counts, complexity records, media durations, and seven independent-book choices. That is honest, but it leaves the principal pacing decisions unsubstantiated. The course-specific `texts.csv` remains absent.

A concrete pressure point is days 23 to 31. They assign nine whole Butler books, approximately **43,300 words** in the checked transcription, alongside new phrase/clause work, discussion, and narrative drafting. Nine ordinary 32-minute main-work blocks provide 288 minutes. At an illustrative 150 words per minute, first reading alone takes about 289 minutes. That rate is a budgeting example, not a Grade 9 norm. [Butler translation, books I and V to XII](https://classics.mit.edu/Homer/odyssey.html).

The independent-reading promise also needs a budget. The inventory estimates about 70,000 words for the unit 1 offer. Even granting eight minutes on every day through day 19 gives only 152 minutes, before conferencing. Completion therefore requires an additional stated allowance or a different completion expectation.

**Why it matters:** Writers must otherwise shorten required reading, sacrifice explicit instruction and revision, or introduce unstated homework. General band targets cannot establish particular texts’ suitability; quantitative, qualitative, and reader/task evidence work together. [Common Core Appendix A, printed pages 4 to 6](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf).

**Exact fix:**

- Complete the course text records with exact editions, boundaries, word counts, rights evidence, complexity analysis, placement reasons, and matching supports.
- Add a unit load table separating first reading, rereading, independent reading, and any home reading, with media running times.
- Rebalance reading and concurrent work within unit 2’s existing days before calling the schedule feasible.
- Name the seven remaining free independent-book offers and realistic completion expectations.
- For unwritten texts, supply explicit commissioning limits now, then replace estimates with actual counts.

Keep current unit lengths provisionally. Any required transfer of days between units belongs to Cory.

### 2. Four units drop cold assessment texts despite the ELA approach requiring them

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** yes, the invalid cold-text assessment kind identified in the earlier Grade 9 frame review  
**Confidence:** firm

**Location:** Unit 3, days 61 to 62; unit 5, days 93 to 94; unit 7, day 130; unit 8, days 152 to 154.

**What is wrong:** These units assess taught passages, retained products, or rehearsed performances without a new cold reading. The scope explicitly drops the cold story, speech, explanatory article, and sonnet.

`APPROACH-ELA.md` requires an end-of-unit assessment on a text not read in the unit. Its unit-field instructions repeat that requirement. Avoiding a recent task form does not require abandoning an unfamiliar text: unfamiliarity and response form are separate choices.

**Why it matters:** The sequence silently changes a governing assessment contract. Unit writers following the sequence and those following the approach will build different assessments.

**Exact fix:** Retain portfolios and whole-work evidence, but restore a bounded cold reading within each existing assessment window:

| Unit | Existing day | Distinct response form |
|---|---:|---|
| 3 | 61 | Cold world-story passage, annotated evidence and concise oral explanation |
| 5 | 93 | Cold speech passage, rhetorical map and brief defense |
| 7 | 130 | Cold explanatory passage, two-level outline and short word-choice commentary |
| 8 | 154 | Cold lyric passage, annotations on meaning, figures, tone, and nuance |

Reserve the texts from instruction and independent assignments. Retain the following course checks’ earlier-unit topics and different response forms. Reopen the affected candidate decisions accordingly.

This is a conflict with Curio Class’s written approach, not a claim that national standards require every unit assessment to be cold.

### 3. Unit 7 requires a published final product without scheduling its production

**Severity:** moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 9 frame findings about the fourteen-day writing and presentation load  
**Confidence:** firm on the missing allocation; likely on the proposed repair’s fit

**Location:** Days 124 to 129, particularly days 127 and 128.

**What is wrong:** Day 126 completes the draft. Day 127 combines whole-class discussion, structured peer response, returned teacher annotations, revision, a change log, and independent-reading conferencing. Day 128 then requires an edited, typed, shared, and updated final portfolio.

Unlike the other three process pieces, this piece has no explicit editing and digital-publication window before collection. The required talk also lacks a clearly named preparation window.

**Why it matters:** The explanatory piece is the year’s main process application of W.9-10.2. Its final revision and publishing stages are likely to become homework or disappear. Protecting modelling, practice, and reflection is consistent with the secondary-writing guidance. [WWC secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22).

**Exact fix:**

- Day 124: build the research synthesis and citation trail in the working document.
- Days 125 to 126: draft and complete the explanation; place structured peer response at the end of day 126.
- Move the second whole-class discussion to day 124’s synthesis work.
- Day 127: use returned teacher annotations for significant revision, editing, digital sharing, and an update.
- Name the brief informal explanation before day 129’s panels as rehearsal and adaptation evidence.

Budget these stages explicitly, including device rotations. Keep one research product, the week 26 deadline, and the existing fourteen days.

### 4. Recitation is being credited as an evidence-based findings presentation

**Severity:** moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete task-to-code alignment identified in earlier ELA reviews  
**Confidence:** firm

**Location:** Days 153 and 158.

**What is wrong:** Day 153 lists `SL.9-10.4`, but its named performance is reading or reciting a passage. Its evidence concerns phrasing, understanding, audience, and register. Day 158 reuses that record for the same code.

SL.9-10.4 requires presenting information or findings with supporting evidence and a followable line of reasoning. Expressive recitation alone does not establish that performance. [Official standards, printed page 50](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf).

**Why it matters:** A complete presentation score could be assigned from evidence of a different oral performance.

**Exact fix:** Keep the required passage reading. Identify its applicable oral-reading and register evidence separately. For SL.9-10.4, explicitly retain the research-presentation record from day 129 on days 153 and 158, rather than assigning that code to recitation alone.

Do not collect another full talk. The existing research presentation supplies the relevant findings, evidence, and reasoning.

### 5. The shorter-period path retains several fifty-minute specifications

**Severity:** moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 8 sequence finding 6  
**Confidence:** firm

**Location:** “Shorter path,” with days 20, 50, 116, and 130.

**What is wrong:** The route offers 35 to 40 minutes but retains these allocations:

- Day 20: 20-minute discussion plus 20-minute word task, before transitions.
- Day 50: 40-minute response plus ten-minute readiness.
- Day 116: ten-minute confirmation plus 40-minute response.
- Day 130: 25-minute assessment plus 25-minute response.

Moving independent reading does not resolve these assessment-day totals. The ten folds also relocate conferences, rereading, rehearsal, or device work without replacement minute budgets.

**Why it matters:** Teachers cannot preserve every assessed part by following the shorter route as written.

**Exact fix:** Supply separate 35-minute and 40-minute allocations for the heaviest assessment days. For a provisional 35-minute version:

| Day | Allocation to test |
|---|---|
| 20 | 15 minutes discussion, 15 minutes word evidence, five minutes transitions |
| 50 | 25 minutes response, ten minutes readiness |
| 116 | Five minutes portfolio confirmation, 30 minutes response |
| 130 | 20 minutes bounded assessment, 15 minutes response |

Shorten passages and response length while retaining each demand. Give each folded destination a budget showing displaced practice and retained work. Keep the shorter route provisional until finished texts and assessment items fit those allocations.

### 6. The research row appears before its named retrieval and before a research task

**Severity:** moderate  
**LAYER:** sequence  
**REPEAT:** yes, Grade 8 sequence finding 4 on first-use alignment  
**Confidence:** firm

**Location:** Days 75 and 76.

**What is wrong:** Day 75 carries `e9-w-short-research` and `W.9-10.7`, but its named task integrates a chart, talk, and memoir while judging sources. Student inquiry and the retrieval of `e8-self-generated-research` begin on day 76.

The chart/talk/text synthesis supports SL.9-10.2. It does not, as described, constitute the research project claimed by W.9-10.7.

**Why it matters:** The first-use map and prerequisite table disagree, and a writer could infer that research has already been introduced.

**Exact fix:** Remove `e9-w-short-research` and `W.9-10.7` from day 75. Keep its media integration and source judgment. Let day 76 remain the explicit research opening, with retrieval immediately before question formulation and searching.

No day or owned requirement is lost.

### 7. The frame and lead notes retain obsolete instructions

**Severity:** low  
**LAYER:** process  
**REPEAT:** yes, stale frame instructions identified in earlier sequence reviews  
**Confidence:** firm

**Location:** Frame opening and Grade 8 seam paragraph; scope “For the lead” item 3.

**What is wrong:** The frame still directs readiness checks on Grade 8 pickups and says each unit opens with one. The sequence correctly implements retrieval and places its older-language readiness before unit 3.

The Biology deadline is also presented as work still requiring coordination. Biology’s current day map fixes its report on **day 139, week 28**, clear of ELA’s day 128, week 26.

**Why it matters:** A downstream writer can reintroduce prohibited readiness placement or reopen a resolved workload issue.

**Exact fix:** At the next authorized frame update, replace blanket Grade 8 readiness wording with retrieval and name the genuine older-row check before unit 3. Update the scope’s Biology note to record the verified day 139 deadline and mark this coordination resolved.

## Other required checks

| Check | Result |
|---|---|
| Order within units | Generally sound: evidence and structure precede epic analysis; rhetoric precedes validity; issue argument precedes literary argument; whole-play conclusions remain provisional until the ending. |
| Declared prerequisites | All declared Grade 8 ELA prerequisites have explicit teaching or assessment placements. Retrieval is appropriate. The research mapping exception is finding 6. |
| Older readiness | Fragment/run-on and pronoun-reference readiness on day 50 precedes unit 3 by one day. Later maintenance references do not establish new teaching. No readiness task is placed on a unit’s first day. |
| Myth background | Grade 8’s explicit Persephone source reading supports retrieval of the inherited myth background. Day 23 teaches unfamiliar epic names. |
| Assessments | End assessments exist in every unit. Unit 2’s mid-unit assessment satisfies the over-25-day requirement. Response time is counted once. Findings 2 and 4 concern assessment validity. |
| Lettered parts | Narrative a to e, argument a to e at the stated Grade 9 limit, explanation a to f, discussion a to d, word strategies a to d, and assigned language parts have mapped teaching and evidence. Named Grade 10 extensions remain distinguishable. |
| Course checks | Earlier-content transfers are explicit: unit 1/2 content after unit 3, unit 4 content after unit 5, and unit 2/6 content after unit 8. |
| Calendar | Checks occupy weeks 13, 20, and 32. Grade 9 permits shared finals. History, Algebra I, and Biology dependencies arrive first or have named bridges. |
| Candidates | All sixteen receive keep/drop decisions and stated costs or reasons. Four cold-text drops need reopening under finding 2. |
| Source map | Not applicable: no adaptable base curriculum. |
| Stale notes | Automated check passes; unmarked contradictions remain in finding 7. |

### Days by load

“Teaching days” below excludes Check and Respond rows; some response time is embedded in Check days.

| Unit | Total days | Teaching days | Judgment |
|---|---:|---:|---|
| 1 | 22 | 19 | Generous for four short stories, justified partly by starting annual routines |
| 2 | 28 | 22 | Whole-book reading plus syntax and narrative work remains unproved |
| 3 | 13 | 10 | Reasonable outline for four short stories and focused editing |
| 4 | 18 | 14 | Plausible, conditional on excerpt and media limits |
| 5 | 11 | 8 | Reasonable for the narrow rhetorical set |
| 6 | 17 | 15 | Writing receives an appropriate sustained run |
| 7 | 14 | 11 | Five opening reading days and three research days leave only three teaching days for drafting through publication |
| 8 | 25 | 20 | Coherent whole-play and poetry arc, subject to timed scene budgets |

No unit’s days should be moved merely to equalize row counts.

## Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Text demand climbs, or its ordering has a reason | **Met in rationale; verification incomplete.** Increasing independence and integration are explained. Text records remain missing. |
| Research and full-process writing recur | **Met in frequency.** Two research cycles and four process pieces; unit 7’s production allocation needs repair. |
| Formal discussion occurs often | **Met in the plan.** At least twice per unit, with daily partner talk and explicit discussion parts. |
| K to 2 phonics aligns with decodables | **Not applicable.** Grade 9. |

This is a sequence review, not a completed rubric score.

## What should be preserved

Keep the unit order, substantial epic reading, every scene of the play, and interleaved poems. Preserve integrated research, distinct process pieces, significant-change logs, explicit Grade 10 limits, earlier-content course checks, and reuse of recent individual evidence.

The sensitive-content notes, distinction between support and replacement, and honest recording of unfinished digital components should remain.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Retain the eight units and current allocations provisionally | The instructional order is coherent | Scope and sequence; day map |
| Restore cold readings with different response forms | Satisfies both assessment contracts | Days 61, 93, 130, 154; candidate decisions |
| Reuse day 129 for SL.9-10.4 | Research findings supply the required reasoning evidence | Days 153 and 158 |
| Make day 76 the research opening | Matches the actual inquiry and prerequisite retrieval | Day 75; prerequisite description |
| Protect unit 7’s revision and publishing window | Final production needs scheduled time | Days 124 to 129 |
| Retain day 50’s readiness placement | It is immediately before the receiving unit | Day 50 |
| Mark Biology coordination resolved | Report due day 139, week 28 | Scope lead note |

## For Cory

- **Scope, only if timing requires it:** If the measured reading and production loads cannot fit within existing unit days, decide whether to transfer days between units or revise a specified reading commitment. This report makes neither change.

## Limits and outside sources

I could not establish actual classroom timings, all texts’ rights and complexity, media usability, question quality, scoring reliability, or sensitivity-read completion. No new classroom-effectiveness claim is made.

- [Official Common Core standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): band requirements and oral-performance distinctions.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): text-complexity model.
- [ELA review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): selected complexity, pacing, writing, and balance provisions. The high-school informational comparison is reported without scoring; the sequence appropriately distinguishes anchor counts from day counts.
- [WWC secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): model, practice, and reflection.
- [Fishtank Grade 9 pacing guide](https://www.fishtanklearning.org/curriculum/ela/9th-grade/pacing-guide/): comparison only. Its 60-minute lessons and additional reading allowance prevent direct day-count equivalence.
- [Louisiana Grade 9 play unit](https://doe.louisiana.gov/docs/default-source/teacher-toolbox-resources/ela-grade-9---romeo-and-juliet-1-0-unit.pdf): comparison of integrated reading, writing, and culminating work, not copied tasks.
- [Butler’s epic translation](https://classics.mit.edu/Homer/odyssey.html): approximate word counts for the nine assigned whole books.

For the source list: add the literary archive and Louisiana comparison if absent. The review PDFs opened successfully through links on their official tools page after an initial direct-open failure.

**Verdict:** Revise before unit planning.  
**Finding count:** 7.  
**Report path:** `docs/reviews/sequence-english-language-arts-grade-9-2026-11-15.md`, delivered inline, not written.

