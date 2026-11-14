# Independent frame review: English Language Arts, Grade 5

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-english-language-arts-grade-5-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

The four-unit design is coherent, but the frame needs revision before baselining. Its largest risk is the claim that the base lessons remain whole: three lessons disappear from the map, and several retained teaching sequences conflict with the stated skill placements. Correct the source map and those placements first, then secure the anchors and make the remaining standards requirements explicit.

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the foundation, relevant roadmap sections, shared and ELA approaches, glossary, and BASELINE rules.
- The complete [Grade 5 frame](/S:/CurioClass/docs/courses/english-language-arts-grade-5/frame.md), its `frames.csv` row, all 30 Grade 5 progression rows, and adjacent-grade handoffs.
- The complete Grade 4 and Grade 6 ELA frames.
- Grade 5 science and social studies units, calendars, and bridges.
- The source register, relevant decisions, earlier ELA progression and frame reviews, and relevant approach and rubric reviews.
- The local base curriculum’s Grade 5 curriculum map and lesson-file ranges in all 12 standard unit archives.
- Outside standards, criteria, research guidance, and two curriculum maps linked below.

`data/plans/english-language-arts-grade-5/source-map.csv` does not exist. This is **not a finding**: `frame-write.md` explicitly defers that day-level file to the scope and sequence. The frame’s source-map table is the artifact reviewed here.

**Gates:** `plan.py check` could not complete because Python lacks `markdown`; `stale.py check` passed, 56 files and 0 failures; `frame.py check english-language-arts-grade-5` passed, 153 unit days plus 7 course-level days. The unavailable full gate does not withhold this verdict.

## Findings, most serious first

### 1. Three base lessons disappear, invalidating the stated pacing

**Severity:** Major  
**LAYER:** base text  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** Frame, “Days” and “Source map.”

Expanding combined lesson filenames into their individual lesson numbers gives:

| Base module | Actual unit lesson counts | Actual total | Frame total |
|---|---|---:|---:|
| 1 | 12, 16, 13 | 41 | 41 |
| 2 | 13, 13, 13 | 39 | 38 |
| 3 | 12, 15, 13 | 40 | 39 |
| 4 | 13, 9, 12 | 34 | 33 |
| **Year** | | **154** | **151** |

M2U2, M3U3, and M4U1 each reach lesson 13. The frame maps each only through lesson 12. Thus retaining every base lesson and adding two water-research days requires **156 unit days**, or **163 days including checks and respond days**, rather than 160.

**Why it matters:** Writers would inherit three missing lessons and an apparently balanced calendar that conceals them.

**Exact fix:** Correct those three ranges and the base total to 154. Recommended allocation: **41, 39, 40, 33**, retaining 153 unit days and seven course-level days. Achieve unit 4’s reduction explicitly: replace the original two-day recording sequence with a planned one-day audio task, and use the existing final-unit research sequence for community-water research instead of adding two days. Identify these adaptations in the map and withdraw the claim that every module lesson remains whole. The one-day recording task needs a feasible minute budget before acceptance.

This confirms the earlier Grade 5 review’s count finding through an independent archive count.

### 2. Retained base teaching conflicts with the frame’s first-teaching placements

**Severity:** Major  
**LAYER:** frame; base text  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** Units 1 to 4, models table, source map, and associated progression notes.

The source map labels M1U3 as retained, but unit 1 omits its planned and revised monologue. The progression itself names that monologue under narrative and fluency, while the frame places Grade 5 narrative and writing-process teaching in unit 2.

M2U2 is labelled “comparing text structures; research.” The base map instead identifies literary reading, narrator influence, same-genre comparison, and an informative essay analysing language. M4U1 includes the recorded announcement; M4U3 contains the final research, opinion essay, leaflet, and presentation. The frame puts the announcement in the latter sequence without explaining the move. These distinctions appear in the [base curriculum map, pages 4 to 6](https://el-education-production.s3.amazonaws.com/media/documents/Curriculum_Tools_Curriculum_Map_Grade5_0419.pdf).

**Why it matters:** A writer cannot simultaneously retain those sequences and follow the frame’s stated first-teaching order.

**Exact fix:** Restore and name the monologue in unit 1, the literary analysis and suitable literary texts in unit 2, and the correct announcement and final-product sequence in unit 4. Recommended ownership changes, requiring Cory’s approval: narrative and writing process to unit 1; same-genre comparison and the first RL.5.6 teaching to unit 2. L.5.3b may remain explicitly completed in unit 4. State whether unit 1’s source use remains Grade 4 review or begins Grade 5 W.5.8.

Any departure retained instead must identify the replaced lessons, replacement instruction, assessment changes, and pedagogical reason.

### 3. Anchor descriptions cannot establish text quality, complexity, or placement

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** “Reading level,” all four anchor lists, and deferred `texts.csv`.

The frame specifies proposed novels, biography, stories, articles, and agency pages without linked anchor drafts or exact passages. It defers individual text records until unit planning. Proposed measures and word counts therefore cannot establish whether these texts support the promised staircase, reading load, or approximately equal literary and informational balance.

The course-frame lens expressly asks for anchors on file with complexity and placement evidence. [Appendix A, printed page 4](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf) requires qualitative, quantitative, and reader/task considerations together.

**Why it matters:** Unit planning would depend on texts whose difficulty and instructional possibilities remain unknown.

**Exact fix:** Supply each anchor draft or exact source passage and a record containing its identifier, location, rights status, measure where appropriate, qualitative demands, reader/task considerations, placement reason, and proposed supports. Count text balance from designated anchors. Until then, label the ranges as commissioning targets.

Identify exact rights routes for the declaration version, newspaper reports, teammate recollection, and third-party material embedded in agency pages. Their availability is currently unestablished.

### 4. Several standards are represented only partially in the planned work

**Severity:** Major  
**LAYER:** standard  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** Units 1, 2, and 4; reading-range and device provisions.

| Requirement | What remains unassigned | Exact fix within existing units |
|---|---|---|
| **RL.5.10** | Independent reading of drama. The specified literary texts are stories and poems. | Include a grade-appropriate dramatic script in unit 1 and a later independent reading of a fresh scene. A performance alone does not establish independent reading. |
| **W.5.6** | Technology-supported interaction and collaboration. Typing, publishing, and peer critique are named, but their connection is unspecified. | In unit 2, require partners to exchange and respond to feedback using the shared device, then publish the revised work through a teacher-managed internet route without student accounts. |
| **SL.5.2** | Summarizing quantitative information. Unit 1 names a talk or video, while the water grid has no summary task. | Name a unit 4 summary that integrates the water text and numerical display, returning to unit 1’s summary routine. |
| **L.5.2c** | The tag-question comma is absent from the otherwise explicit list. | Add direct teaching and editing of tag-question commas in unit 1. |
| **L.5.3b** | Unit 4 identifies varieties of English and what they reveal, but does not explicitly compare and contrast them. | Require comparison of language choices across two story or poem speakers, with respectful attention to context and register. |

These requirements follow the official [literature](https://www.thecorestandards.org/ELA-Literacy/RL/5/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/5/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/5/), and [language](https://www.thecorestandards.org/ELA-Literacy/L/5/) standards.

**Why it matters:** Naming a parent code permits a writer to overlook a required medium, action, or subpart. These additions clarify existing scope and require no new unit.

### 5. The shortened skills block does not secure daily independent reading

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes  
**Confidence:** judgment call  
**Location:** “Days,” “Reading level,” source-map closing paragraph, and `e5-reading-range.notes`.

The progression promises a daily independent-reading block. The frame allocates daily word study followed by fluency **or** independent-reading conferences on alternate days. It gives no independent-reading floor and does not explain how the omitted second-block components are replaced.

**Why it matters:** Independent reading could occur only on alternating days, while additional writing and complex-text practice disappear through compression.

**Exact fix:** If Cory retains 90 minutes, use a provisional 30-minute allocation of ten minutes each for word study/spelling, purposeful oral rereading, and independent reading. Hold individual conferences during independent reading. Identify writing and additional complex-text practice inside the 60-minute unit lesson, and test this allocation in the pilot.

Those minute allocations are an expert planning judgment, not a research-established optimum. The [WWC grades 4 to 9 guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/29) supports decoding and purposeful fluency instruction for intervention populations; it does not validate this compressed whole-class schedule.

### 6. Progression notes still direct writers toward the replaced disaster topic

**Severity:** Moderate  
**LAYER:** progression; process  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** Frame, “For the lead,” item 2; eight Grade 5 progression rows; decision register’s `q-cross-progression-1` entry.

The frame correctly identifies replacements, but the progression still names earthquake entrapment, emergency-kit supplies, preparations, preparedness, and a safety announcement. `e5-genre-compare` also leaves unit 2 or unit 4 unresolved. The decision register says nine Grade 5 rows were updated, overstating completion.

**Why it matters:** The progression and frame provide competing writing instructions.

**Exact fix:** Apply the frame’s eight listed row corrections, including the genre placement after finding 2 is resolved. Change “seven rows” to “eight rows.” Rewrite the decision status:

> The water topic replacement is approved. Progression wording is partially updated; the remaining row corrections are listed in the Grade 5 frame, For the lead item 2.

Update that status again when the corrections actually exist. Reconcile the informative and comparison-writing notes with the final decisions under finding 2.

### 7. The earlier decision note still says six ELA decisions await Cory

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** `docs/agents/decisions/DESK-ANSWERS.md:529-542`.

This entry says no decision has been made, repeats “Waiting for Cory’s yes,” and says the findings are not logged. Subsequent entries record the decisions and logging.

**Why it matters:** It reopens settled scope questions, including Grade 3 to 5 foundational skills.

**Exact fix:** Rewrite its status note:

> Resolved after this entry: the six questions were answered under q-ela-piece-2 on 2026-11-12; the fallback choice was completed in the subsequent fallback-hero decision. The ELA findings were logged as recorded in “Sara’s pieces 1 and 2 taken in.” Retain separately verified rights-review work as pending.

Preserve the historical account, but remove its live waiting instructions.

### 8. The following intake note also leaves the answered ELA card open

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** `docs/agents/decisions/DESK-ANSWERS.md:548,554`.

The intake entry says `q-ela-piece-2` is unanswered and still open. The next entry supplies Cory’s answers and records their application.

**Why it matters:** This second unresolved-looking entry survives even if finding 7 is corrected.

**Exact fix:** Replace those two references with:

> q-ela-piece-2 was answered and applied on 2026-11-12; see the following entry.

Keep the other questions in that paragraph separately listed according to their actual status.

### 9. The earlier rubric review still presents foundational-skills scope as undecided

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm  
**Location:** `docs/reviews/rubric-ela-2026-11-11.md:309-317`.

Its “For Cory” section still asks whether Grades 3 to 5 claim foundational skills. The decision register, current rubric, and Grade 5 frame all record yes.

**Why it matters:** A reader following the standing expert guidance back through earlier reports encounters a false open question about an applicable gateway.

**Exact fix:** Replace the question’s live status with:

> Resolved 2026-11-12, q-ela-piece-2: Curio Class Grades 3 to 5 teach foundational skills, and Gateway 1 applies in full. The taught sequence and checks remain implementation requirements.

## Coverage, days, seams, and cross-subject results

| Check | Result |
|---|---|
| Owned progression skills | All 30 placed exactly once: unit counts **16, 6, 5, 3**. No foreign-grade row appears in Skills. |
| Standards | Applicable codes are represented. Full instructional coverage needs finding 4, and first-teaching consistency needs finding 2. |
| Unit reasons | The novel establishes routines; rainforest research supports later source work; athlete accounts prepare synthesis; water joins the year’s routines. These reasons hold. |
| Days by load | A long opening novel and continuous skills justify unit 1’s size. Unit 4’s synthesis products justify substantial time despite only three newly owned rows. Source fidelity, rather than equal days per row, causes the pacing finding. |
| School year | The stated 160 includes four check days and three respond days, leaving approximately 20 days within a 180-day year. |
| Source eligibility | No prohibited edition or reference curriculum is mapped. State explicitly that the standard rainforest module is selected and the alternative life-science module is unused. |
| Grade 4 seam | The handoffs are picked up, including the higher independent-reading demand and longer-word work. |
| Grade 6 seam | Skill handoffs agree. Grade 6 explicitly develops the water thread through floods and storms. |
| Science timing | Ecosystem teaching overlaps or precedes the rainforest work; water teaching runs beside unit 4. Local content bridges are present. |
| Social studies timing | Sourcing precedes ELA unit 3. Civil-rights history comes later, so the segregation explainer is necessary. Earlier social studies demands on ELA have explicit local bridges. |
| Mathematics | Hundredths retrieve Grade 4 work without assuming Grade 6 percent instruction. |

I disagree with the earlier Grade 5 report’s recommendation to remove the flood story solely because Grade 6 also studies floods. The next frame explicitly carries that knowledge forward and increases the analytical demand. Different texts and tasks can make this a productive seam.

The earlier report’s statement that no social studies lean comes later is too broad: civil-rights content does come later. The frame already supplies the needed bridge, so this creates no additional curriculum finding.

## Lens checklist: course frame layer

| Lens line | Status | Evidence |
|---|---|---|
| Units arise from specific topics and texts | **Met in design** | Four identifiable topic sets, with concrete people, places, events, and proposed texts. |
| Anchors are on file with complexity and placement evidence | **Missed** | Finding 3. |
| Texts avoid excessive concentration in one era, tradition, or kind | **Not yet established** | Contemporary originals and varied subjects are promising, but actual texts, authorship, and anchor counts remain unavailable. |
| A long text is read whole | **Met as a frame commitment** | Novel and biography. Delivery depends on finding 3. |

Question percentages, daily lesson openings, finished supports, and scoring materials belong to later layers and cannot be scored from this frame.

## What should be preserved

Keep the topic-based structure, repeated research, two whole long texts, daily text-dependent writing, explicit Grade 4 review, named models, regular discussion, school-day device route, sensitivity provisions, and counted respond days.

## Settled by the expert

These are recommendations for the caller to apply, not edits made during this read.

| Choice | Reason | File touched |
|---|---|---|
| Correct the base count to 154 and the three ranges through lesson 13 | Independently verified lesson inventory | Grade 5 frame, Source map |
| Retain the flood-to-storm knowledge seam | The next grade names the inheritance and raises demand | Grade 5 and Grade 6 seam notes |
| Add the five explicit standards provisions in finding 4 | Completes existing scope within existing units | Grade 5 frame |
| Use the provisional 10/10/10 skills allocation if 90 minutes is retained | Makes all three daily commitments visible | Grade 5 frame, Days |
| Rewrite the three stale status notes | Decisions are already recorded | Files named in findings 7 to 9 |

## For Cory

- **Scope:** Approve the first-teaching ownership changes proposed in finding 2 and the corresponding pacing redistribution.
- **Audience:** Decide the 90-minute assumption, given the base curriculum’s 120-minute design and the proposed skills allocation.
- **People and money:** Name the qualified ELA, rights, and sensitive-content readers, and any compensation. No outreach is authorized by this report.

## Limits and sources

This read establishes planning defects, not instructional effectiveness. Actual anchor quality, originality, precise reading difficulty, complete rights clearance, and classroom timing remain unjudged. No curriculum finding rests solely on memory.

Outside sources opened:

- [Common Core Grade 5 standards](https://www.thecorestandards.org/ELA-Literacy/): the strand pages linked in finding 4, plus informational reading and foundational skills.
- [Grade 5 base curriculum map](https://el-education-production.s3.amazonaws.com/media/documents/Curriculum_Tools_Curriculum_Map_Grade5_0419.pdf): module structure, assessments, products, and two-block design; checked against local lesson inventories.
- [ELA Grades 3 to 5 review criteria v2.1](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_3_5_Review_Criteria_2_1_bb1cc2d7c6.pdf): foundational instruction, fluency, text complexity, and comprehensive-program expectations.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): three-part text complexity.
- [Publishers’ Criteria, Grades 3 to 12](https://achievethecore.org/content/upload/Publishers_Criteria_for_Literacy_for_Grades_3-12.pdf): extended reading and text-based instruction.
- [Grade 5 comparison scope and sequence](https://www.coreknowledge.org/wp-content/uploads/2017/03/G5_CKLA_Detailed_ScopeSequence.pdf): comparison of integrated reading, writing, grammar, morphology, spelling, assessment, and response time. Reference only.
- [WWC reading interventions, Grades 4 to 9](https://ies.ed.gov/ncee/wwc/PracticeGuide/29): decoding and purposeful fluency, with the population limitation stated above.

**For the source list:** Add the comparison scope and sequence if absent, and record that the original Grade 5 curriculum-map address above was reachable during this read.

**Verdict:** Revise before baselining. **Findings:** 9. **Report path:** `docs/reviews/frame-english-language-arts-grade-5-2026-11-14.md`, supplied here without writing a file.

