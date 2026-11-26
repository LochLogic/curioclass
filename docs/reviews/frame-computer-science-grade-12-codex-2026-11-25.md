# Frame read: computer-science-grade-12

2026-11-26 | Independent second reader | Read-only report

## Verdict

The five-unit structure is sound: all 11 selected progression rows are placed once, the 14 owned standards match their units, and the calendar accounts for all 64 course days. The biggest risk is claiming full coverage where the fallback or assessment does less than the standard requires. Seven findings need correction before scope and sequence, especially the AI-model fallback and the assessment of actual program refinement.

## What was read and checked

- The frame-read brief, applicable frame-write rules and after-core changes, EXPERT.md, and the computer science lens.
- The subject adoption bar, STANDARD.md and APPROACH.md; relevant shared foundation, approach, production and decision rules.
- The grade 12 frame in full, its selected progression rows, frames.csv entry and calendar rows.
- The adjacent grade 11 frame, including its outgoing handoffs. There is no following course.
- The grade 12 ELA Units table and calendar rows; targeted earlier computer science frames for repeated cases.
- Relevant pre-work, progression and earlier frame reviews.
- All 14 claimed standards’ boundary statements in the stored CSTA PDF, beside the published source.

No files were changed.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check computer-science-grade-12` | One stage-related failure: days.csv with parts.csv or items.csv is absent. Course-filtered to honor repository instructions. |
| `python -X utf8 scripts/frame.py check computer-science-grade-12` | 0 failures; 60 unit days and four course-level check/respond days. |
| `python -X utf8 scripts/stale.py check` | 121 files checked, 0 failures. An unmarked stale statement remains. |
| Independent placement check | All 11 selected skills placed exactly once; 10 Foundational and four Specialty standards accounted for. |
| Calendar comparison | Units occupy days 1–11, 12–22, 25–46, 47–54 and 57–64. Checks on days 23 and 55 match weeks 12 and 28. |

The plan-stage failure does not block this frame verdict. This is a single-grade course, so the band-course Year column requirement does not apply.

## Findings

### 1. Serious: the supplied-model fallback does not meet S1-AIN-HR-09 in full

**LAYER:** progression  
**REPEAT:** yes, boundary-depth coverage is an established review pattern; this particular fallback is new  
**Confidence:** firm

**Location:** Frame, Course order and Standard bullets; unit 1, day 4; progression row `g12-evaluate-ai-output`.

S1-AIN-HR-09 includes analysis of systems students created themselves and systems created by others. Replacing the grade 11 class model with a supplied model covers only the latter. Even students who took grade 11 need evidence that they helped create the model being analyzed. [CSTA standards, PDF page 112, printed page 107](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf)

The fallback is useful teaching material, but the frame currently promises full coverage for students whose own-model evidence is missing.

**Exact fix:** Keep the supplied-model fallback and add this qualification to the progression note, unit 1, Evidence and Devices:

> Students analyze a model they helped create and a model created by others. A student without a model they helped create uses the supplied model for this lesson; S1-AIN-HR-09 is recorded as part met until the student also analyzes a model they helped create. HS-ALG-PS-05 remains fully claimed.

Carry that qualification into the eventual course record. Do not add model-building days silently: the frame explicitly excludes building models.

### 2. Serious: the year-end assessment does not score the refinement students actually made

**LAYER:** frame  
**REPEAT:** yes, assessment below the standard’s action is an established review pattern  
**Confidence:** firm

**Location:** Unit 4, days 4–8; Course-level check 2; Evidence bullet.

Students make and test changes during unit 4, but day 8 explicitly records the program and refinement record without scoring them. The year-end sitting instead asks students to choose and explain a proposed change.

That checks reasoning about refinement, while HS-PRO-TR-20 requires students to make meaningful refinements using feedback, test results and design values. [CSTA standards, PDF page 67, printed page 62](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf)

**Exact fix:** Replace unit 4’s day 8 assessment sentence with:

> The final program and refinement record are handed in. The teacher scores each student’s contribution to one implemented refinement, using the user-feedback note, before-and-after evidence, test results and explanation of the design value served. This product score forms the performance part of the year-end assessment.

Keep the unseen sitting as individual transfer evidence. Name the rubric, two sample refinement records and individual evidence in the unit-plan requirements. This uses existing work and adds no day.

### 3. Moderate: the four-day senior short form drops explicit portfolio and field research

**LAYER:** frame  
**REPEAT:** new in the computer science reviews consulted  
**Confidence:** likely

**Location:** Grade 12 calendar bullet, lines 39–45; unit 5 short form.

The full unit gives day 4 to examining portfolio evidence and researching two computing-related fields. The short form names the hook, log study, published accounts, plan draft, feedback, revision and hand-in, but never places that day 4 work.

A writer could follow the short form exactly and produce a career plan without the research and reflection the progression requires.

**Exact fix:** Replace the four-day description with this bounded allocation:

| Short-form day | Work retained |
|---|---|
| 1 | Hook, 3 minutes; team-log analysis, 7; two short published narratives, 20; analysis draft, 7 |
| 2 | Portfolio evidence for two skills, 7 minutes; two supplied field cards, 12; plan draft connecting interests, skills, fields, pathway and next step, 18 |
| 3 | Written feedback and revision of both pieces |
| 4 | Scored analysis and plan, plus the short unseen log item |

These are task minutes within the existing lesson arrangements. Keep the explicit statement that both standards are unclaimed when students leave before this unit can be taught.

### 4. Moderate: the course-level checks need task limits and a usable time budget

**LAYER:** frame  
**REPEAT:** yes, combined grades 6–12 review S3 and grade 11 second-reader finding 4  
**Confidence:** likely

**Location:** Course-level checks, frame lines 251–252.

The first sitting contains values analysis, law evaluation, policy evaluation, a community-impact judgment, a collection proposal and an earlier-unit output judgment. The second contains attribution, refinement reasoning, heuristic review and three earlier-unit samples.

These can become several substantial performances. “A 45-minute sitting” does not constrain the amount of reading, evidence or writing a later author may assign.

**Exact fix:** Retain the dates and specify a maximum of 35 task minutes, with ten minutes for directions, transitions and collection:

| Check | Task budget |
|---|---|
| After unit 2 | Values trace, 5; law evaluation, 8; one linked data-policy/community-impact case, 12; saved-output judgment, 5; review, 5 |
| Year-end | Attribution, 7; individual refinement explanation, 8; heuristic review, 8; three brief retrieval samples, 9; review, 3 |

Require supplied evidence, response limits and look-fors for each task. Score finding 2’s existing product outside the sitting.

I agree with the earlier review’s workload concern. The evidence does not require a uniform two-lesson assessment rule across every computer science grade.

### 5. Moderate: course day 24 double-books its final ten minutes

**LAYER:** frame  
**REPEAT:** yes, combined review M7  
**Confidence:** likely

**Location:** Course order, lines 49–57; incoming Seams; unit 3 opening.

Day 24 is the mid-year respond day. Its final ten minutes are assigned both the grade 11 prerequisite check and the grade 9 check on flowcharts, modules and data structures.

These prerequisites determine whether students can enter the capstone, so the overlap should be resolved before daily planning.

**Exact fix:** Keep the grade 11 prerequisite check on day 24. Move the grade 9 check to the final ten minutes of course day 22, unit 2’s feedback-and-revision day.

Update all three references: Course order, the paragraph below incoming Seams, and Models carried. Unit 3 day 3 should name the worked example and supported practice used for each flagged gap.

### 6. Minor: the Specialty percentage uses all course days as its denominator

**LAYER:** frame  
**REPEAT:** yes, combined review S2  
**Confidence:** firm

**Location:** Specialty days under C1, lines 72–77.

The stated allocation totals five day-equivalents, but the frame divides by 64 course days. C1 and STANDARD.md specify teaching days.

Removing the ten dedicated assessment/respond days gives 54 teaching days: five of 54 is approximately **9.3 percent**, rather than eight percent. The present allocation still passes, but has little headroom.

**Exact fix:** Replace the percentage sentence with:

> The five Specialty day-equivalents occupy about 9.3 percent of the 54 teaching days, excluding dedicated assessment and respond days. The scope and sequence counts all outside-content minutes, including shared lessons, against the same teaching-time denominator.

List the excluded days: unit 1 days 10–11, course days 23–24, unit 3 days 21–22, course days 55–56, and unit 5 days 7–8. Recalculate if the later plan changes those classifications.

### 7. Minor: the adoption-bar introduction incorrectly says no subject approach exists

**LAYER:** process  
**REPEAT:** yes, stale-note pattern in the combined review and earlier reads  
**Confidence:** firm

**Location:** `docs/ADOPTION-BAR-SUBJECTS.md`, lines 20–21.

The introduction says layer 3 requires an approach page and “none exists.” The computer science approach is present, records Cory’s approval on 2026-11-20, and is acknowledged in the same adoption-bar file’s computer science status row.

This sends readers toward completed work, despite the stale checker passing.

**Exact fix:** Replace that sentence with:

> This page sets the adoption bar. Subject approach pages describe teaching methods; their current completion and approval status is recorded under “Before a scope and sequence in this subject.”

## Lens checklist, course-frame layer

| Lens line | Result |
|---|---|
| All five concepts receive taught time | Met: ALG in units 1–2, DAT and SYS in unit 2, PRO in units 3–4, SOC in units 1 and 5. |
| Read and predict, then modify, then make | Met explicitly in the capstone sequence. |
| Unplugged work teaches an idea; device work tests it | Met at frame level in every unit. |
| The notional machine is taught | Carried through module tracing, pseudocode, flowcharts and the editor’s step-through view. |
| Debugging and testing are explicit methods | Met through test-tables, review steps, integration tests and revision. |
| Practices sit inside content | Met; practices have tasks and pair roles switch. |
| Society uses evidence and multiple views | Planned; actual packs still need source and sensitivity checks. |
| A non-specialist teacher can teach it | Required by APPROACH.md; actual explanations and solutions belong to later layers. |
| Constructs are taught before independent use | Planned, with finding 5’s readiness allocation needing correction. |
| Standards reach their boundary depth | Mostly met in design; findings 1–3 identify gaps in claims, assessment or the short route. |
| Specialty claims fit; no S2 claims | Named S1 list is permitted. Retain the existing version-control qualification and add finding 1’s qualification. |
| AI has underlying algorithm/data work | Met; output judgments lead into system bias and policy work. |
| No unit lacks unplugged work | Met. |
| Doing is assessed through programs and products | Strong in unit 3; unit 4 needs finding 2. |
| Tools have named jobs and need no accounts or installation | Met in the proposed specification. |
| No unsupported general-thinking claim | Met. |

The block-to-text transition is not a new teaching responsibility at this grade. The elective entry route remains responsible for checking the code knowledge it actually uses.

## Settled by the expert

| Choice | Decision | Reason | Files affected |
|---|---|---|---|
| Structure and calendar | Keep five units and 64 days | Ownership, dependency order and calendar arithmetic hold | Grade 12 frame |
| Supplied AI model | Retain it with an explicit partial-coverage record | Useful fallback without overstating evidence | Frame and `g12-evaluate-ai-output` |
| Refinement assessment | Score the existing implemented change | Preserves the standard’s action without adding days | Frame; later unit 4 assessment |
| Senior short form | Retain portfolio and two-field research explicitly | Keeps both career rows represented | Frame |
| Course-level checks | Keep dates and bound tasks | Resolves workload ambiguity locally | Frame |
| Readiness timing | Move the older-prerequisite check to day 22 | Removes the day 24 overlap | Frame |
| Repeated people and CARE sources | Treat them as deliberate revisits with a new analytical purpose | Repetition alone does not justify changing other courses | Frame’s case and coordination notes |
| US spelling | Change “catalogue id” to “catalog id” | Applies the repository’s wording rule | Frame header |

No standard is moved between grades or units.

## What is right and should not be touched

- The sequence from evaluating outputs, to evaluating rules, to building and refining software.
- The substantial capstone allocation: 22 days, including design, review, feedback and revision.
- The distinction between owned standards and the two grade 9 standards revisited in the capstone.
- The honest partial-coverage statement for version control until the editor supports it.
- Saved-output evaluation without student use of live generated-text tools.
- Private career plans, invented project data, consent for peer users, and the rule for students 18 or over.
- The ELA bridges. Seminar teaching precedes its computer science use; explanatory writing comes later and has an explicit local bridge.

## What could not be judged

Actual tools, assessment items, rubrics, case packs and teacher solutions are not available at this layer. Their correctness, accessibility and completion time remain later checks.

The proposed historical and legal sources are viable directions, but finding a source does not establish that its eventual excerpt supports every planned claim. No finding above rests solely on subject-matter memory. Historical Codex memory was consulted only for review-workflow guidance; substantive conclusions were checked against current files or sources.

## Sources and source-list corrections

- [2026 CSTA PK–12 Computer Science Standards](https://csteachers.org/wp-content/uploads/2026/07/2026-CSTA-PK%E2%80%9312-Computer-Science-Standards.pdf): checked the 14 claimed standards’ boundaries, including required actions and excluded depth.
- [Computing pedagogy](https://www.raspberrypi.org/teach/pedagogy): checked modeling, program comprehension and the progression toward independent construction.
- [W3C: Involving Users in Evaluating Web Accessibility](https://www.w3.org/WAI/test-evaluate/involving-users/): checked the distinction between user evaluation and standards-based accessibility review.
- [Census Bureau disclosure-avoidance announcement, June 2021](https://www.census.gov/newsroom/press-releases/2021/2020-census-key-parameters.html) and [NCAI’s May 2021 research update](https://archive.ncai.org/policy-research-center/research-data/prc-publications/NCAI_PRC_2020_Census_Guide_to_Data_and_Impacts_5_17_2021_FINAL.pdf): verified a concrete pair of institutional and community sources for unit 2.
- [CARE Principles](https://www.gida-global.org/careprinciples): working community-authored source. Replace the frame’s `/care` address, which returned 404.
- [DOJ Title II web-rule summary](https://www.ada.gov/title-ii-web-rule/): confirms the 2024 rule and records the April 2026 deadline extension. Date the eventual summary and include the update when discussing implementation.
- [FTC’s January 2025 COPPA announcement](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data): confirms the proposed amendment source.
- [NIST AI 600-1 publication record](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence): verified title and July 2024 publication date; the record alone was not used as evidence for particular harms.
- [Copyright Office report, Part 2](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf): verified the January 2025 copyrightability source.
- [NASA’s Katherine Johnson biography](https://www.nasa.gov/history/katherine-johnson-biography/): accessible candidate background source. The unit still needs a specific first-person account.
- [Smithsonian Hopper interview, July 1968](https://www.si.edu/media/NMAH/NMAH-AC0196_hopp680700.pdf): **browser check**, automated opening returned 403. It was not fetched another way. The November 1968 URL tried returned 404. Keep claims about the chosen interview’s contents unverified until the lead checks it.

Add the specific working links and access statuses to the source handoff. Keep “from memory” labels on remaining unverified facts until checked.

## For Cory

- If every entrant must receive a full S1-AIN-HR-09 claim, decide whether to authorize model creation within grade 12. That changes the present scope, which excludes building models. Until then, use finding 1’s partial-coverage record.
- The other corrections require no new spending, audience change or outside-person arrangement.

