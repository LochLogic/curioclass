# Independent cold read: social-studies-grade-2 scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-social-studies-grade-2-2026-11-14.md`  
**Delivery:** Report supplied here only. No files were changed.

## Verdict

Revise before writing the unit plans: the overall order, 96-day budget and calendar placement are sound. The biggest risk is apparent completeness, because every owned code appears while some required teaching and assessment evidence remain unspecified. Complete those requirements and preserve the early writing support, keeping the existing units and day totals.

**Finding count: 7.**

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, the shared and social studies adoption criteria, and `docs/courses/social-studies/STANDARD.md`.
- `FOUNDATION.md`, the relevant ROADMAP sections, BASELINE rules 20 to 24, `GLOSSARY.md`, `APPROACH.md`, and relevant source and evidence notes in `APPROACH-SOURCES.md`.
- The complete grade 2 scope and sequence, all 96 rows of its `days.csv`, and the complete course frame.
- All grade 2 social studies progression rows and the connected grade 1 and grade 3 rows; the recorded exclusions.
- The Massachusetts grade 2 standard descriptions and the official framework’s standards and clarifications; relevant official C3 indicators.
- `CALENDAR.md`, every grade 2 subject’s calendar rows, and relevant ELA and science frame entries.
- The sequence-writing and frame-writing rules, including the current readiness rule.
- Earlier grade 2 frame reviews, their fix record, relevant progression reviews and fixes, and the social studies baseline review and fixes.
- `BASE-TEXTS.md`. This course has no base text, so a base-lesson source map is not applicable.

Outside sources were opened during this read and are linked below. No finding rests solely on memory.

### Gates

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Reported an unrelated missing civics sequence, then stopped with `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule breaks reported. |
| `python -X utf8 scripts/frame.py check social-studies-grade-2` | **0 failures**; seven units, 96 days. |
| `python -X utf8 scripts/sequence.py check social-studies-grade-2` | **0 failures**. |
| `python -X utf8 scripts/stale.py check` | Stopped with `KeyError: 'node'`. |
| Scoped stale check on this sequence, day file and frame | **Three files, 0 failures**. Manual status review still found finding 7. |

The incomplete global gates do not withhold this verdict.

## Findings, most serious first

### 1. The assessment descriptions leave required evidence uncovered

**LAYER:** sequence  
**REPEAT:** yes, incomplete standard-to-task alignment recurs in the earlier social studies progression and grade 2 frame reads  
**Severity:** serious  
**Confidence:** firm

**What is wrong.** Several assessments attach codes to a narrower task. The general promise of teacher observation does not identify the missing performance, and the expressly named observations sometimes cover different work.

The following are concrete omissions, rather than a request to write assessment items prematurely:

| Location | Evidence not secured | Exact fix within the existing days |
|---|---|---|
| Unit 1, day 15 | Source origin is omitted; the human-environment map example is not checked. | Add origin to the sourcing response and ask what relationship the supplied map shows. Retain scoring of the maps made on days 13 and 14. |
| Unit 2, day 28 and its observation note | Two continents, two oceans and one feature do not establish the full placement requirement. Ocean importance, vegetation and effects on people are also unsecured. | Name a brief observation record across days 24 to 27 covering complete placement on map and globe, a feature per continent, and the missing explanations. Preserve the already specified physical and cultural change observations. |
| Unit 3, day 44 | Naming a resource and one tool **or** skill omits production costs, both resource categories represented by tools and skills, and several relationships taught earlier. | Specify separate recorded evidence for costs, tools and learned skills, community comparisons, and disaster effects. Add the teaching repairs in finding 2 before assessing them. |
| Unit 4, day 56 | Naming country characteristics and tracing one good do not check government purposes, country comparison, reasons for trade or both trade directions. | Use the day 55 closing task as a named assessment component for explanations and comparison. Make day 56 trace one incoming and one outgoing good. |
| Unit 5, day 70 | The arrival comparison does not establish the “nation of immigrants” explanation or the past-present comparison. The attached movement indicator also extends beyond people. | Name a short closing observation for the explanation and past-present comparison. Record goods evidence in unit 4 and ideas evidence in unit 6; do not imply day 70 completes the whole movement indicator. |
| Unit 6, day 80 | Source limitations are checked, but generating a question about the source is not. Culture’s elements and contributions across the community remain implicit. | Add a student-generated source question and explicitly score the relevant evidence from days 78 and 79 alongside the unseen-source task. |
| Unit 7, day 92 | Finding facts and matching them to supporting questions does not establish source-selection reasoning or the connection to the compelling question. | Score a short source-choice record from the research and ask how one supporting answer helps answer the big question. Preserve scoring of the report’s argument. |

**Why it matters.** A writer could follow these descriptions faithfully and produce a record that cannot show whether students learned everything claimed. This is especially consequential in unit 3, immediately before the already crowded week 14.

**Evidence.** The assessment goals and notes were compared with the local standards and the official [Massachusetts framework, grade 2 content and clarifications](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), and the relevant [C3 indicator tables](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Exact overall fix.** Revise the seven assessment summaries and corresponding CSV goals or notes to identify each missing performance and its collection day. Use bounded observations and existing products, keeping the current assessment and respond days.

### 2. Three owned requirements have no explicit teaching task

**LAYER:** sequence, progression, standard  
**REPEAT:** yes, the earlier progression review and grade 2 frame findings F1 and F2 identified this kind of narrowing  
**Severity:** serious  
**Confidence:** firm

**What is wrong.**

1. **Services disappear from `D2.Eco.4.K-2`.** Days 39 and 40 teach food and other goods. Neither explicitly compares services produced locally and elsewhere. The owning progression note and frame repeat this narrowing. Earlier teaching of the goods-services distinction does not complete this year’s geographic comparison. [C3 economics indicators, PDF page 37, printed page 36](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

2. **Settlement reasons remain an example rather than an explanation.** Day 30 names cities by rivers, but never requires students to explain why people settle near particular water bodies or landforms. That requirement appears in the clarification to `MA.2.T2.4`, but is absent from the local shortened description. [Massachusetts framework, PDF page 46, printed page 46](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

3. **The country argument has no digital presentation.** Days 89 to 91 reserve a printed report and an oral presentation. The owned `D4.3.K-2` also includes a digital medium. The earlier repair successfully added an argument, but did not settle this remaining mode. [C3 communication indicators, PDF page 60, printed page 59](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters.** These omissions survive a code-presence check and would be inherited by the unit writers.

**Exact fix.**

- Expand day 40 to compare a locally produced good and service with examples from another community, retaining the production-cost task. Update the owning progression note and frame to match.
- Expand day 30 to explain one river settlement and one contrasting landform settlement using supplied maps and captions. Restore this clarification in the standard description.
- Reserve part of days 90 and 91 for an adult-assisted digital version of the student’s argument on one shared device, with no account, network or upload. Preserve the printed presentation path. If a learner uses only that path, record the digital component as unobserved rather than claiming it was demonstrated.

The last point exposes the audience decision listed under “For Cory”; it does not justify changing ownership silently.

### 3. The writing bridge ends before the calendar dependency is met

**LAYER:** sequence, frame  
**REPEAT:** yes, the earlier grade 2 frame read explicitly required support before independent writing  
**Severity:** serious  
**Confidence:** likely

**What is wrong.** Shared writing is specified on day 26, with the bridge named for days 26 and 27. The next day asks for a written assessment claim, and later closing claims continue before ELA’s opinion-writing unit.

Day 28 is school day **42**. ELA unit 4 begins on school day **119**, with opinion instruction somewhere inside it. The social studies frame itself says independent writing waits until ELA has taught it. The ELA frame likewise describes the early social studies bridge as keeping the claim short and spoken.

**Why it matters.** A busy writer could remove support after one shared-writing lesson and measure writing independence instead of geographic reasoning.

**Exact fix.** Add a continuing bridge rule to the sequence and the affected day notes:

> Before ELA opinion instruction is complete, students rehearse claims aloud and record their own chosen reason and source using a supplied sentence frame, with transcription support where needed. Teaching may use shared composition; assessment responses retain each student’s own reasoning.

Apply it explicitly to days 27, 28, 43, 44, 46, 55, 56 and 69. Name a local demonstration of readiness before withdrawing the frame, rather than treating the start of ELA unit 4 as automatic completion.

This is a calendar and implementation judgment. The broader recommendation to teach writing processes explicitly is supported by the [elementary writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17); that guide does not establish a mandatory waiting week.

### 4. Unit 1’s compelling question has one intended answer

**LAYER:** frame, sequence  
**REPEAT:** yes, the earlier grade 2 frame read identified a similar inquiry-question weakness in unit 6  
**Severity:** moderate  
**Confidence:** judgment call

**What is wrong.** “Can a map ever show the world just as it is?” is settled by the unit’s instruction that every map selects or distorts something. Students can supply the expected “no” without weighing which representation serves a particular purpose.

**Why it matters.** The question functions as a concept check while being presented as the year’s first sustained inquiry. The sequence-layer lens requires room for more than one defensible conclusion.

**Exact fix.** Use:

> Which map would we choose to answer a question about our world, and why?

Retain the present question as a supporting question. On days 11, 14 and 15, have students choose between representations for a stated purpose and justify the choice from what each shows or leaves out. Change the frame question to match, without moving standards or days.

This is a new application of the earlier question-quality finding. The repaired unit 6 question should remain. The distinction between inquiry and explanatory supporting questions is discussed in the [C3 inquiry arc](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

### 5. Some candidate dispositions overstate what the cited comparison actually contributes

**LAYER:** sequence, process  
**REPEAT:** yes, grade 2 frame finding F3 concerned inaccurate or premature source-to-course claims  
**Severity:** moderate  
**Confidence:** firm

**What is wrong.** Unit 6 and day 77 say Tennessee `2.01` and `2.02` are met by the row. Day 77 lists cultural contributions; it does not explicitly compare customs or examine shared principles and goals. Unit 3 similarly treats Tennessee `2.04` as fully met by resource-industry examples, although its named industries extend further. These distinctions are visible in the official crosswalk’s **new 2024 column**. [Tennessee crosswalk, PDF page 6](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf).

California `2.4.1` also includes a historical comparison, whereas day 39 keeps a present-day food chain. Keeping a selected contribution is defensible, but its disposition should distinguish that choice from completing the cited standard. [California grade 2 standards, PDF page 15](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf).

**Why it matters.** The next comparison table could inherit a false “already met” result.

**Exact fix.**

- Day 77: explicitly compare two supplied cultural examples. Day 78: identify one shared community goal. Keep both inside their existing days.
- Unit 3: replace the full-completion claim with “resource-industry examples informed by Tennessee `2.04`; the wider industry survey is not adopted here.”
- Day 39: record “kept, present-day production and consumption chain, one day; the historical comparison is not added because this contribution serves the unit’s existing resources-and-work question.”

Keep the other candidate decisions. The word-bank adaptation of California map labeling is an explicit choice, not an error.

### 6. The required shorter path is absent

**LAYER:** sequence  
**REPEAT:** yes, the earlier grade 2 frame read recorded this unresolved limitation  
**Severity:** moderate  
**Confidence:** firm about the omission; judgment call about the remedy

**What is wrong.** The sequence states 30 to 40 minutes and a full 96-day route, but identifies no shorter path. The shared adoption criterion C2 and FOUNDATION section 5 require one.

**Why it matters.** A teacher with the shorter period still has to decide what can safely be omitted.

**Exact fix.** Add a named **30-minute core path**, keeping all 96 meetings and all required performances. Specify that additional illustrative examples, extended discussion and display preparation occupy the optional ten minutes. Require each later unit plan to identify its core source set and optional elaborations explicitly.

Do not call any owned standard, cultural-change comparison, assessment or respond day optional. A route with fewer meetings would require a separate feasibility judgment; none is established by this review.

### 7. The frame still gives obsolete readiness instructions

**LAYER:** frame, process  
**REPEAT:** yes, stale status and prerequisite wording recur in the earlier frame and baseline reads  
**Severity:** minor  
**Confidence:** firm

**What is wrong.** The frame’s Days bullet requires a readiness check for an assumed grade 1 row, while the current rule calls for retrieval when that row was used the preceding year. Its opening also still says the scope and sequence will set the days later.

The sequence already identifies the readiness conflict correctly. The scoped stale check does not detect either sentence.

**Why it matters.** Unit writers following the frame could add unnecessary assessment time or reopen completed day allocation.

**Exact fix.**

- Replace the readiness clause with the sequence’s proposed retrieval wording.
- Replace the future-tense opening with a reference to the existing scope and sequence and day file.
- Close the sequence’s corresponding lead note once the frame is corrected.

No additional readiness day is warranted by the connected grade 1 rows.

## Order, load, calendar and coverage

All **18 owned skills** and **42 distinct owned codes** appear. The owned Massachusetts set has no lettered subcodes; the substantive completeness issues concern clauses, clarifications and indicator requirements.

| Unit | Teaching days | Assessment + response | Load judgment |
|---|---:|---:|---|
| 1. Maps | 14 | 2 | Appropriate foundation for subsequent source and map use. |
| 2. Land, water and climate | 11 | 2 | Plausible total, with a concentrated day 19: eight named features across five continents, compared with four across two on day 18. Redistribute examples across days 17 to 20 and preserve repeated locating. |
| 3. Living with the land | 14 | 2 | Larger allocation justified by environmental reasoning, economics and the action cycle. |
| 4. Countries and trade | 8 | 2 | Tight but plausible if country comparison and trade remain concrete. |
| 5. People on the move | 12 | 2 | Plain historical teaching and source comparison justify the allocation. |
| 6. Family stories and culture | 8 | 2 | Practice before interviewing is well placed. |
| 7. Country report | 10 | 2 | Appropriate for gathering, constructing an argument and presenting. |
| **Total** | **77** | **14** | **91 unit days, plus five course-level assessment and response days.** |

No whole unit is demonstrably far over or under its load. These are planning judgments, not measured teaching times.

The internal arcs generally build correctly: map components precede construction; countries and resources precede migration; interview practice precedes interviewing; research gathering precedes the argument. The thematic organization of unit 5 explains its historical groupings adequately.

No unit exceeds 25 days, so no mid-unit assessment is required. Response time is counted once: seven unit respond days and two course-level respond days.

### Calendar and leans

| Requirement | Verified placement |
|---|---|
| Mid-year check | Course day 46, school day 68, **week 14**; response on school day 70. |
| Year-end check | Course days 94 and 95, school days 152 and 154, **week 31**; response on school day 155. |
| Science land-and-water lean | Science unit 1 ends school day 21; social studies unit 2 begins school day 26. Available. |
| ELA purpose and text-comparison leans | Later ELA placement is acknowledged and bridges are supplied. |
| ELA opinion-writing lean | Later placement is correctly identified; continuation of support needs finding 3. |
| ELA speaking and research leans | Their calendar units precede the interviews and country report. Exact lesson completion remains a later planning check. |

Week 14 holds four social studies meetings: the unit assessment, its response, the course-level check and its response. This concentration is disclosed and breaks no stagger rule. Keep observations distributed so finding 1 does not turn day 44 into an oversized written test.

## Scope and sequence lens checklist

| Checklist line | Status |
|---|---|
| Compelling questions require sources and permit defensible conclusions | **Missed in unit 1**, finding 4. The remaining questions are workable at this layer. |
| History follows time order, or a reason explains departure | **Met.** The thematic order and local chronological groupings are explained. |
| A contested event receives more than one telling | **Not yet judgeable for final source selection.** Days 68 and 69 explicitly reserve account comparison; the unit plans must establish the voices used for the separate hard-history cases. |
| Writing from sources recurs and develops | **Met for recurrence; missed for support continuity**, finding 3. |

## What is right and should not be touched

- Maps first, resources and countries before migration, and the report last.
- Physical and cultural change in two regions, preserving the earlier repair.
- The bounded country menu and supplied printed source sets.
- Explicit treatment of forced movement, living Native nations and source independence.
- Interview alternatives that avoid compulsory family disclosure.
- The safe, school-mediated action cycle and its later reflection.
- The existing assessment and respond-day allocations.

The earlier government-content, scale-prerequisite, regional-change and unit 6 question repairs remain substantially intact. This read identifies remaining requirements and implementation gaps, rather than reopening those settled choices.

## Settled by the expert

These are recommendations for the caller to apply. Nothing was edited.

| Choice | Reason | Files affected |
|---|---|---|
| Retain seven units and 96 days | Order and overall allocation are defensible. | Sequence and day file |
| Make missing assessment performances explicit | Codes alone cannot establish coverage. | Assessment summaries and CSV notes |
| Complete services and settlement explanations inside unit 3 | Finishes existing ownership. | Day file, frame, progression notes and standard description |
| Continue supported individual claims until readiness is demonstrated | Aligns the early work with the ELA calendar. | Sequence, affected day notes and frame |
| Replace unit 1’s compelling question | Creates a choice justified from representations. | Frame, sequence and days 1, 11, 14 and 15 |
| Distinguish selected check-set contributions from full completion | Prevents inherited coverage claims. | Candidate dispositions and day notes |
| Use a 30-minute core route with optional elaboration | Supplies a shorter time path without removing standards. | Sequence and later unit plans |
| Correct readiness and future-tense status wording | Removes conflicting instructions. | Frame and sequence lead note |

## What I could not judge

Actual source difficulty, reuse rights, final historical wording, assessment scoring, presentation duration and classroom feasibility require the source sets, unit plans and items. This is a scope and sequence verdict, not a finished-course adoption review.

## For Cory

- **Audience:** settle whether the K to 2 audience can access one adult-operated shared device for the digital presentation component. The all-paper route remains useful, but cannot document that particular performance.

No money or outside-person decision is needed for the other recommendations.

## Sources and source-list follow-up

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): grade 2 standards, clarifications and shared economics.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned indicator requirements and inquiry framing.
- [Social studies instructional-material criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): coherent knowledge, inquiry and evidence expectations.
- [Elementary writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17): explicit writing instruction; no inference that a particular calendar week ensures independence.
- [California standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): candidate contributions and their limits.
- [Tennessee 2024 crosswalk](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf): new-column comparison requirements.
- [New York K to 8 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf?v=2024100929): community comparison. The unparameterized address timed out; this address opened.
- [Louisiana grade 2 curriculum overview](https://www.coreknowledge.org/free-resource/louisiana-bayou-bridges-grade-2/): limited comparison of knowledge sequence and assessment organization.
- [Primary geography unit overview](https://www.thenational.academy/teachers/programmes/geography-primary-ks1/units/continents-and-oceans-what-can-we-find-out-about-the-world/lessons): limited comparison of local-to-global prerequisites. Its year group and standards differ, so it is not a pacing minimum.

**For the source list:** record the working parameterized New York address and the current primary geography route. Neither comparison curriculum was read in full or used as a base text.

**Verdict: revise before unit planning. Finding count: 7. Report path: `docs/reviews/sequence-social-studies-grade-2-2026-11-14.md`, supplied here only.**

