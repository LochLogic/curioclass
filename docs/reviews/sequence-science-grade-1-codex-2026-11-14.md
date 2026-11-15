# Independent sequence review: Science, Grade 1

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-science-grade-1-2026-11-14.md`  
**Delivery:** Report supplied here. No file was created or edited.

## Verdict

Revise before unit planning: the teaching order, prerequisite bridges and unit allocations are sound, but the assessment summaries do not yet secure every claimed performance and content element. The largest instructional risk is treating a plan and an explanation of supplied results as sufficient evidence of conducting an investigation. Make the missing assessment evidence explicit within the existing days, and obtain Cory’s decision on the timetable that requires ten three-meeting weeks.

## What I read

- `docs/agents/EXPERT.md`, the science lens and `docs/RUBRIC-SCIENCE.md`.
- FOUNDATION, the required ROADMAP sections, BASELINE rules 20 to 24, GLOSSARY, APPROACH and relevant APPROACH-SOURCES entries.
- The complete science-grade-1 scope and sequence, all 68 `days.csv` rows and the complete course frame.
- Kindergarten and grade 1 science progression rows, including every assumed row’s grade of use.
- The owned expectations and dimension elements in the local science standards files, checked against the official sources linked below.
- CALENDAR.md and the grade 1 calendar rows for all four subjects; relevant same-year frame passages establishing the leans.
- Both earlier grade 1 science frame reviews, the K to 2 science fix record, the sequence writer’s handoff, and relevant earlier sequence and structure reviews.
- The base-text record and outside sources listed below.

The prohibited files were not opened. Prior-run memory informed the review method only; the findings rest on current files and live sources.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: importing `lesson.py` raised `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule break reported. |
| `python -X utf8 scripts/frame.py check science-grade-1` | Passed, zero failures. |
| `python -B -X utf8 scripts/sequence.py check science-grade-1` | Passed, zero failures. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files, zero failures. |

The interrupted global gate does not prevent the substantive verdict.

## Findings, most serious first

### 1. Investigation assessments do not explicitly require collecting and recording data under the child’s plan

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, incomplete assessment performances were identified in the earlier grade 1 social studies sequence read, finding 1  
**Confidence:** firm on the requirement; likely on the omission permitted by the wording

**Location:** Scope and sequence, units 4 and 5, Course-level checks and Materials; `days.csv`, days 33, 36, 46 and 66.

**What is wrong:** Day 46 names “planning and interpreting” a material test. Day 66 names an evidence account and peer test plan. The sound assessment descriptions likewise emphasize plans and causal evidence without explicitly reserving observation of children collecting and recording results according to those plans.

The general fallback says children propose a test, read evidence and revise an account. That can support explanation, but a writer could implement it entirely with completed results and never assess the investigation’s execution.

Both [1-PS4-1](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1-PS4-1%20Evidence%20Statements%20June%202015%20asterisks.pdf) and [1-PS4-3](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1-PS4-3%20Evidence%20Statements%20June%202015%20asterisks.pdf) require collaborative collection and recording of observations according to the investigation plan. Their evidence statements distinguish this from planning.

**Why it matters:** A child could receive a complete record for explaining supplied evidence while the teacher has no evidence that the child can carry out the planned observation procedure.

**Exact fix:** Amend the four assessment reservations and corresponding prose:

| Days | Required assessment evidence |
|---|---|
| 33 and 36 | Each child contributes to a peer plan, follows its observation procedure, records observations for both causal directions, and uses those observations to support or revise the account. |
| 46 and 66 | Each child contributes to the material-test plan, participates in carrying it out, records the four material effects, and explains what the observations establish. |

Keep adult operation of electrical equipment and all existing controls. For a recorded-media route, specify how children select the comparisons under their plan and collect their own observations; handing out a completed results chart is supplementary evidence. Keep the current day counts.

### 2. The delivery timetable exceeds the settled weekly frequency

**Severity:** Major  
**LAYER:** sequence, frame  
**REPEAT:** yes, the same timetable-feasibility problem appears in the earlier grade 1 social studies sequence read, finding 4  
**Confidence:** firm

**Location:** Frame, Days bullet and For the lead item 1; scope and sequence introduction and For the lead item 1; `days.csv.school_day`.

**What is wrong:** The frame records Cory’s settled choice of two weekly meetings. The sequence finishes 68 meetings in 29 weeks, requiring:

- Two meetings in 19 weeks.
- Three meetings in weeks **3, 4, 6, 9, 12, 15, 18, 21, 24 and 29**.

Two meetings weekly supply only 58 meetings by week 29. The writer correctly discloses this conflict, but disclosure does not settle the audience’s time requirement.

**Why it matters:** A teacher reserving the agreed two weekly slots cannot follow the reference schedule. The ten additional meetings require approximately 300 to 350 additional minutes before the endpoint.

**Exact fix:** Put this concrete timetable to Cory:

> Sixty-eight meetings across 29 weeks, each lasting 30 to 35 minutes: two meetings in 19 weeks and three in weeks 3, 4, 6, 9, 12, 15, 18, 21, 24 and 29.

If accepted, align the frame’s Days, Cross-subject timing and For the lead wording. If two meetings is a firm ceiling, Cory must authorize the calendar or delivery change. The existing 58-meeting shorter path is a possible basis for that decision, but it is not currently the reference schedule.

### 3. Unit 7 omits the plant-offspring element attached to its standard

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, omission of a core-idea element was identified in the earlier grade 1 science frame read, finding 2; this is a different element  
**Confidence:** firm

**Location:** Scope and sequence, unit 7 and standards table; `days.csv`, days 56 to 60 and 67; local dimension row `1-LS1-2 / LS1.B`.

**What is wrong:** Unit 7 teaches and assesses animal signals, adult responses and survival. Its “animal cases only” direction leaves no named retrieval or assessment of the associated idea that adult **plants and animals** can produce young.

Unit 3 supplies plant parent-and-young evidence, so this does not need a new investigation. However, neither the day 60 observation nor the day 67 course-level check names that evidence under `1-LS1-2`. The [official life-science evidence statement, PDF page 3](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1%20LS%20Evidence%20Statements%20June%202015%20asterisks.pdf#page=3) explicitly includes obtaining information about offspring in both plants and animals.

**Why it matters:** The claim that these tasks cover every part of the code exceeds their stated coverage.

**Exact fix:**

- On day 56, retrieve unit 3’s documented parent-plant and seed-grown-young record.
- On day 57, include one short read-aloud caption establishing that adult plants, as well as animals, can have young.
- On days 60 and 67, reserve a brief unfamiliar plant-and-young information prompt alongside the animal behaviour task.
- Replace “animal cases only” with wording that excludes personal family comparisons while allowing this required plant example.

Retain the robin and deer cases and all six unit days. Do not imply that plants provide animal-style parental care.

### 4. The stored shared calendar still represents the pre-split sequence

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, stale generated calendar data required regeneration in the earlier sequence structure-fix pass  
**Confidence:** firm

**Location:** `data/plans/calendar.csv`, science-grade-1 rows 390 to 401.

**What is wrong:** The stored calendar does not reflect the written day map:

| Item | Stored calendar | Current `days.csv` |
|---|---|---|
| Unit 8 fall launch | Absent | Day 9, school day 19 |
| Unit 2 | Days 9 to 20 | Days 10 to 21 |
| Mid-year check | Days 34 and 35 | Days 35 and 36 |
| Mid-year response | Day 36 | Day 37 |
| Unit 8 spring block | Days 61 to 65, starting school day 131 | Days 62 to 65, starting school day 133 |

The calendar command computes from current inputs, which explains why it can report correct check weeks while the stored CSV remains stale.

**Why it matters:** Another subject’s writer using the required shared calendar sees the daylight launch only in spring and receives incorrect course-day references.

**Exact fix:** The repository owner should run `python -X utf8 scripts/frame.py sync` during the authorized shared turn, then verify that the stored calendar contains separate unit 8 fall and spring runs and the corrected intervening course-day ranges. Regenerate the calendar table through that command, not by hand. This does not require changing the sequence’s dates or check weeks.

### 5. The frame retains obsolete readiness wording

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, readiness-versus-retrieval wording was corrected across the earlier sequence structure pass  
**Confidence:** firm

**Location:** Frame, Days bullet and unit 2 and unit 4 “Why this unit, here” cells.

**What is wrong:** The frame still describes kindergarten retrieval as a “readiness review” or “readiness look” and says an older assumed row opens with a readiness check inside the unit’s days. The current sequence correctly uses retrieval, and the current brief places dormant-skill readiness before the unit opens.

**Why it matters:** A later unit writer could reintroduce a first-day readiness check from the active frame.

**Exact fix:** Replace the unit 2 and unit 4 phrases with “retrieves kindergarten’s …”. Replace the general sentence with:

> A row used in the previous grade or earlier this year receives retrieval inside a day. An assumed row last used two or more grades back receives readiness before the unit opens, at the location required by the sequence-writing rule.

No readiness assessment should be added to this grade 1 sequence.

## Order, standards and assessment coverage

The prerequisite order holds: parts precede nature-inspired design and resemblance accounts; planned sketches precede message-device work; sound and light precede communication; the daylight launch precedes seasonal comparison.

| Owned code | Teaching days | Unit assessment | Course-level check | Judgment |
|---|---|---|---|---|
| 1-ESS1-1 | 1 to 6 | 7 | 35 | Sun, moon and bounded star patterns carried. |
| 1-LS1-1 | 10 to 19 | 20 to 21 | 35 | Parts, plant response and material solution carried. |
| K-2-ETS1-2 | 16 to 19 | 20 to 21 | 35 | Shape-function representation and communication carried. |
| 1-LS3-1 | 22 to 25 | 26 | 36 | Plants, animals and variation carried. |
| 1-PS4-1 | 28 to 32 | 33 | 36 | Both causal directions carried; finding 1 applies. |
| 1-PS4-2 | 38 to 42 | 46 | 66 | Illuminated and self-luminous objects carried. |
| 1-PS4-3 | 43 to 45 | 46 | 66 | All four effects carried; finding 1 applies. |
| 1-PS4-4 | 48 to 53 | 54 | 67 | Built product and receiver trial retained. |
| 1-LS1-2 | 56 to 59 | 60 | 67 | Finding 3 applies. |
| 1-ESS1-2 | 9, routines, 62 to 63 | 64 | 67 | Seasonal comparison and relative-only boundary carried. |

The [official standards](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf) establish these expectations and boundaries. These codes have no lettered suffixes to place separately; their dimension elements still require substantive coverage.

Unit 2 explicitly uses a two-meeting whole-task observation window. Its response occupies the final ten minutes of day 21 once. Other unit responses are separately reserved. No unit exceeds 25 days, so no mid-unit assessment is required.

The immediate course-level checks explicitly change context: sound uses unit 2’s craft context, and daylight uses unit 1’s sky-watch context with fresh seasonal records. At sequence level, this satisfies the non-repetition rule.

## Readiness, retrieval and cross-subject timing

Every assumed earlier-grade science row belongs to kindergarten, the immediately preceding grade.

| Unit | Retrieval placement |
|---|---|
| 1 | Day 1: `sk-weather-watch`. |
| 2 | Day 10: living needs, needs and places, defining a problem. |
| 3 | Day 22: kindergarten evidence accounts and this year’s parts chart. |
| 4 | Day 28: pushes and pulls. |
| 5 | Days 38 and 43: sunlight, evidence accounts, investigations and shade design. |
| 6 | Day 48: defining problems, testing designs and this year’s sketch, sound and light. |
| 7 | Day 56: obtaining information and this year’s sensing-response work. |
| 8 | Day 9 and spring return day 62: recording habits and the fall record. |

**No unit incorrectly checks a year-before row or retrieves a dormant older-grade row. No actual readiness check is misplaced.**

The same-year bridges are adequate:

- W.1.8 arrives after unit 1; days 1 and 2 provide spoken observations and teacher charting.
- RI.1.2 arrives after unit 2; days 10 and 13 provide the topic-and-detail bridge.
- SL.1.5 begins just after day 16; that day provides drawing and dictated labels.
- Length ordering and measurement arrive later in math; days 22 and 50 teach their stated bridges.
- Three-category data work, informative writing and text-detail questions precede their later science uses.
- Science checks remain in weeks 15 and 29, distinct from the other subjects’ target check weeks.

## Days by load and Candidate decisions

| Unit | Total / teaching days | Load judgment | Candidate disposition |
|---|---:|---|---|
| 1 | 8 / 6 | Reasonable for three sky records and predictions. | Daytime moon retained within day 4. |
| 2 | 12 / 10 | Largest allocation justified by biology, modelling and construction. | Live second animal dropped; day 14 uses photographs. |
| 3 | 6 / 4 | Reasonable after parts vocabulary. | Second growing record dropped. |
| 4 | 7 / 5 | Workable; reverse causation has only day 32 and needs careful unit planning. | Second source and stopping test retained on days 30 and 31. |
| 5 | 10 / 8 | Two investigations and supported writing justify the allocation. | Shadow-length extension dropped. |
| 6 | 8 / 6 | Allows construction, measurement, repeated trials and revision. | Comparing groups’ devices dropped. |
| 7 | 6 / 4 | Reasonable for two-source comparisons; finding 3 fits within it. | Live nest dropped. |
| 8 | 5 / 3 | Reasonable because records accumulate outside meetings. | Conditional adult photograph retained within the routine. |

No run is demonstrably far over or under its load. The five-day sound teaching allocation deserves timing attention, but the current evidence does not justify resizing it.

All eight Candidate cells are settled: three retained and five dropped, with costs or reasons. There is no base text, so a base-lesson source map and preservation of another curriculum’s lesson order are **not applicable**.

## Shorter path

The section supplies both a 25-minute period route and ten named fold-ins: **3, 6, 12, 14, 17, 24, 30, 41, 45 and 52**.

All ten are unassessed teaching days. Their work is explicitly retained in neighbouring days; assessment and response slots remain, and unit 8 retains its seasonal placements. No owned part is explicitly cut. Combined-meeting feasibility still needs verification when the activities exist.

## Science lens checklist: scope and sequence

| Checklist line | Result | Evidence |
|---|---|---|
| Anchor is a phenomenon or problem rather than a topic | **Met** | Specific shadow, tower, seedling, sound, light, signal, animal and daylight cases. |
| Models are built before dependent use | **Met** | Kindergarten models are retrieved; structure-function precedes the planned sketch and later device. |
| Engineering design expectations appear in units | **Met** | Units 2 and 6 require designing, making, testing and revision. |
| Equipment has substitutes or a no-kit path | **Met at plan level** | Alternatives and minimum construction supplies are named; finding 1 qualifies assessment evidence. |

The applicable science-bar commitments are substantially present: concrete anchors, revised models, integrated tasks, costs, appropriate source status and a coverage map. Findings 1 and 3 prevent accepting the claim of complete assessment coverage. No finished-course rubric score is warranted from these planning files.

## Settled by the expert

Recommendations for the caller to apply; no files were edited.

| Choice | Reason | Files touched |
|---|---|---|
| Keep the eight units, ownership and day allocations. | Dependencies and relative loads are defensible. | Scope and sequence; `days.csv`. |
| Require explicit data collection and recording in investigation assessments. | Completes the already-owned practice. | Days 33, 36, 46 and 66; corresponding prose. |
| Retrieve plant offspring in unit 7 and check it briefly. | Completes LS1.B without a new unit or day. | Days 56, 57, 60 and 67; unit 7 prose. |
| Keep all ten shorter-path fold-ins. | They preserve assessed work and name the retained evidence. | Shorter path; day notes. |
| Keep optional home observations and essential full-day strips. | Participation remains accessible and fixed-time reports do not substitute for whole-day evidence. | Unit 8. |
| Replace obsolete frame readiness wording with retrieval wording. | Matches the actual prerequisite history. | Frame. |
| Regenerate the shared calendar from the written day map. | Restores the split unit and correct references. | Generated calendar outputs. |

## What is right and should be preserved

The earlier plant-parent comparison, plant-response and mirror-category problems have been addressed. Do not reopen those settled findings.

Preserve the documented parentage fallback, animal examples that avoid personal family disclosure, darkness choices, safety controls, genuine construction requirements, unseen assessment cases and protected response time. The descriptive models stay within the grade’s boundaries.

## What I could not judge

The files do not yet establish assessment-station timing for a whole class, working sound apparatus, complete scoring guidance, media suitability and rights, actual materials costs or local seasonal dates. Those require the unit tasks, selected records and inventory.

The global plan check remains incomplete because of the missing dependency. The EdReports criteria and evidence-guide addresses attempted during this read were inaccessible, so their contents were not independently reverified; the local rubric supplied that part of the review bar.

## Sources

- [Official standards, DCI arrangement](https://www.nextgenscience.org/sites/default/files/AllDCI.pdf): grade expectations, core ideas and assessment boundaries.
- [Grade 1 life-science evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1%20LS%20Evidence%20Statements%20June%202015%20asterisks.pdf): biological content and observation evidence.
- [1-PS4-1 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1-PS4-1%20Evidence%20Statements%20June%202015%20asterisks.pdf): planning and collecting sound-investigation data.
- [1-PS4-3 evidence statement](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1-PS4-3%20Evidence%20Statements%20June%202015%20asterisks.pdf): material tests and recorded observations.
- [Grade 1 Earth-science evidence statements](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/1%20ESS%20Evidence%20Statements%20June%202015%20asterisks.pdf): sky predictions and seasonal daylight.
- [Engineering evidence statements, PDF page 2](https://www.nextgenscience.org/sites/default/files/evidence_statement/black_white/K-5%20ETS%20Evidence%20Statements%20June%202015%20asterisks.pdf#page=2): shape-function models.
- [EQuIP science rubric](https://www.nextgenscience.org/sites/default/files/EQuIPRubricforSciencev3.pdf): coherence and observable three-dimensional assessment.
- [OpenSciEd sky-patterns overview](https://openscied.org/instructional-materials/1-3-space-sky-patterns/) and [sound overview](https://openscied.org/instructional-materials/1-2-waves-sound/): reference comparison of observation-to-explanation and investigation-to-design arcs. These public overviews do not establish a required pacing allocation.
- [Taking Science to School, chapter 3](https://www.nationalacademies.org/read/11625/chapter/5): selected research-summary passages on young children’s scientific reasoning; no lesson-duration claim rests on them.

### For the source list

Record the verified individual physical-science evidence-statement links above. Note that the attempted EdReports criteria and evidence-guide links were inaccessible in this run.

## For Cory

- **Audience and time:** Approve or revise the concrete 29-week timetable in finding 2. It requires ten weeks with three science meetings despite the settled two-meeting frequency.

**Verdict: Revise before unit planning. Finding count: 5. Report path: `docs/reviews/sequence-science-grade-1-2026-11-14.md`, delivered here only.**

