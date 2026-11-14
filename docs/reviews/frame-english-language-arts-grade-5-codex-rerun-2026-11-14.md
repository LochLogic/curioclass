# Independent frame review: English Language Arts, Grade 5

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-english-language-arts-grade-5-2026-11-14.md`  
**Delivery:** Complete report below. No files changed.

## Verdict

The four-unit design has sound topics, useful routines, and coherent grade-to-grade handoffs, but it needs revision before baselining. Its greatest risk is an inaccurate source map that conceals three lessons and contradicts several first-teaching placements. Correct that map and reconcile the placements first, then complete the anchor evidence and explicitly assign the missing standards requirements.

**Finding count: 9.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, foundation, shared and ELA approaches, relevant roadmap sections, glossary, and BASELINE rules 20 to 24 and 29.
- The complete [Grade 5 frame](/S:/CurioClass/docs/courses/english-language-arts-grade-5/frame.md), its `frames.csv` row, all 30 Grade 5 progression rows, and adjacent-grade prerequisite and handoff entries.
- The complete Grade 4 and Grade 6 ELA frames.
- Grade 5 science and social studies units, calendars, and cross-subject bridges.
- The full Grade 5 standards text in `data/standards/ccss-ela-standards-full.txt`.
- The base-text register, frame-writing brief, relevant decision entries, and earlier Grade 5 frame and ELA progression reports. Adjacent-course reports informed repeat classification.
- The stored 2017 base curriculum’s Grade 5 curriculum map and lesson inventories in all 12 standard unit archives.
- Outside standards, review criteria, research guidance, and two curriculum maps linked below.

`data/plans/english-language-arts-grade-5/source-map.csv` does not exist. Its absence is **not a finding**: `docs/pipeline/briefs/frame-write.md` explicitly reserves the lesson-level CSV for the scope and sequence. This review checks the frame’s summary source map.

**Gates:** `plan.py check` could not complete because Python lacks `markdown`; `frame.py check english-language-arts-grade-5` passed with 0 failures; `stale.py check` passed, 56 files and 0 failures.

No substantive curriculum finding rests on memory. Saved memory informed only the review format and read-only boundary.

## Findings, most serious first

### 1. Three base lessons are missing from the inventory and pacing

**Severity:** Major  
**LAYER:** base text  
**REPEAT:** yes, earlier Grade 5 frame reads  
**Confidence:** firm  
**Location:** Frame, “Days” and “Source map,” lines 10 to 16 and 197 onward.

The local lesson archives establish these counts, including combined lesson downloads:

| Base module | Actual lessons by base unit | Actual total | Frame total |
|---|---|---:|---:|
| 1 | 12, 16, 13 | 41 | 41 |
| 2 | 13, 13, 13 | 39 | 38 |
| 3 | 12, 15, 13 | 40 | 39 |
| 4 | 13, 9, 12 | 34 | 33 |
| **Year** | | **154** | **151** |

M2U2, M3U3, and M4U1 each extend through lesson 13. The frame stops each at lesson 12.

**Why it matters:** The statement that every base lesson remains whole cannot support the stated calendar. Keeping all 154 lessons and adding two water-research days requires 156 unit days plus seven course-level days, or **163 days**.

**Exact fix:** Correct the three ranges and the base total. Recommended allocation: **41, 39, 40, 33**, retaining 153 unit days and seven course-level days. In unit 4, explicitly merge M4U1 lessons 12 and 13 into one recording day and replace the existing kit-research sequence with community-water research rather than adding two days. Withdraw the blanket claim that every module lesson remains whole.

The recording merge needs a feasible classroom-device and minute budget before acceptance. The earlier reports proposed this repair, but the frame has not incorporated it.

### 2. “Kept” base sequences conflict with first-teaching placements

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 5 frame reads  
**Confidence:** firm  
**Location:** Units 1 to 4, models table, and source map.

The [base curriculum map, PDF pages 4 to 6](https://el-education-production.s3.amazonaws.com/media/documents/Curriculum_Tools_Curriculum_Map_Grade5_0419.pdf) establishes several sequences that the frame misrepresents:

- M1U3 develops and performs a narrative monologue. The frame omits that product while placing narrative and writing-process teaching in unit 2.
- M2U2 includes literary reading, narrator influence, same-genre comparison, and a literary-analysis essay. The frame labels it “comparing text structures; research” and supplies no corresponding literary set.
- M4U1 includes the recorded announcement. M4U3 contains final research, opinion writing, the leaflet, and presentation.

**Why it matters:** Writers cannot retain these sequences while following the stated rule that a skill’s owning unit is where its Grade 5 step first appears.

**Exact fix:** Correct the source-map descriptions and name the retained products. Recommended ownership changes are narrative and writing process to unit 1, and same-genre comparison and initial RL.5.6 teaching to unit 2. Keep L.5.3b’s completion explicitly in unit 4 if desired. Identify unit 1’s source work as either Grade 4 review or initial Grade 5 W.5.8 instruction, with completion in unit 2.

Alternatively, document deliberate replacements lesson by lesson, including replacement instruction and assessment. Standard-placement changes go to Cory.

### 3. Proposed anchors cannot yet establish complexity, quality, or balance

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 5 and Grade 6 frame reads  
**Confidence:** firm  
**Location:** “Reading level,” anchor descriptions, and deferred `texts.csv`.

The frame supplies commissioning descriptions and target measures, but no linked original anchor drafts or exact agency passages. Individual text records are deferred until unit planning. Thus the proposed staircase and approximately equal literary and informational balance remain unverified.

The course-frame lens requires anchors on file. [Appendix A, PDF page 5, printed page 5](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf) requires quantitative, qualitative, and reader/task considerations together. The [Grades 3 to 5 criteria, indicator 2b](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_3_5_Review_Criteria_2_1_bb1cc2d7c6.pdf) likewise requires documented text analysis.

**Why it matters:** Replacing the base books changes the evidence available for questions, models, vocabulary, pacing, and assessments.

**Exact fix:** Before treating the frame as settled, supply each anchor draft or exact source passage with:

- Identifier and location.
- Rights status.
- Measure where appropriate.
- Qualitative demands and reader/task considerations.
- Placement reason and proposed supports.
- Literary/informational classification and whole-text/excerpt status.

Until then, label the numerical ranges as commissioning targets. Resolve the exact declaration version, newspaper reports, teammate recollection, and any third-party material embedded in agency pages. Count balance from designated anchors rather than topic descriptions.

### 4. Five standards requirements need explicit assignments

**Severity:** Major  
**LAYER:** standard  
**REPEAT:** yes, earlier Grade 5 independent frame read  
**Confidence:** firm  
**Location:** Units 1, 2, and 4; reading-range and device provisions.

| Requirement | Gap in the frame | Exact fix |
|---|---|---|
| **RL.5.10** | Stories and poetry are specified, but independent reading of drama has no home. | Add a suitable dramatic script to unit 1 and a later independent reading of a fresh scene at appropriate demand. Performance alone does not demonstrate independent reading. |
| **W.5.6** | Typing, publishing, and critique are named without assigning technology-supported interaction and collaboration. | In unit 2, specify partners exchanging and responding to feedback through a shared digital document, plus a teacher-managed internet publishing route without student accounts. |
| **SL.5.2** | Unit 1 names a talk or video summary, but quantitative information has no explicit summary task. | Add a unit 4 summary combining the water text and numerical display, identified as review of the unit 1 summary routine. |
| **L.5.2c** | The otherwise detailed conventions list omits tag-question commas. | Add direct teaching and editing of tag-question commas in unit 1. |
| **L.5.3b** | Unit 4 identifies varieties of English and what they reveal, without explicitly comparing them. | Require comparison and contrast of language choices across two speakers or texts, with respectful attention to context and register. |

These requirements are explicit in the official [literature](https://www.thecorestandards.org/ELA-Literacy/RL/5/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/5/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/5/), and [language](https://www.thecorestandards.org/ELA-Literacy/L/5/) standards.

**Why it matters:** Parent codes and general promises allow required actions or media to disappear during writing. These corrections complete existing scope within existing units.

### 5. The shortened skills block does not secure daily independent reading

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 5 frame reads  
**Confidence:** judgment call  
**Location:** “Days,” source-map closing paragraph, and `e5-reading-range.notes`.

The progression promises daily independent reading. The frame instead schedules word study followed by fluency **or** independent-reading conferences on alternate days. It gives no independent-reading floor and leaves the replacement for omitted additional writing and complex-text practice unclear.

**Why it matters:** A busy teacher could reasonably provide independent reading only on alternating days.

**Exact fix:** If Cory retains 90 minutes, provisionally allocate the 30-minute block as ten minutes each for word study/spelling, purposeful oral rereading, and independent reading. Conduct conferences during independent reading. Identify where additional writing and complex-text practice occur inside the unit lesson, then test the allocation in the probe.

The exact minutes are an expert planning judgment. The [WWC intervention guide for Grades 4 to 9](https://ies.ed.gov/ncee/wwc/PracticeGuide/29) supports decoding and purposeful fluency work for intervention populations; it does not validate this compressed whole-class schedule.

### 6. Progression wording contradicts the replacement topic and completion note

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, earlier Grade 5 frame reads  
**Confidence:** firm  
**Location:** Frame, “For the lead,” item 2; Grade 5 progression notes; `DESK-ANSWERS.md`, `q-cross-progression-1`.

The progression still directs writers toward earthquake entrapment, emergency-kit supplies, preparedness, and a safety announcement. The frame lists seven affected rows and then adds an eighth, `e5-genre-compare`. The decision register says nine Grade 5 rows were updated, overstating completion.

Other product descriptions also diverge: `e5-informative`, `e5-integrate-several`, and `e5-opinion` describe essays differently from the frame.

**Why it matters:** These are competing instructions for the next writer.

**Exact fix:** Apply the eight listed corrections after resolving finding 2, and reconcile the three additional writing-product descriptions. Replace “seven rows” with “eight rows.”

Rewrite the decision status as:

> The water topic replacement is approved. Progression wording is partially updated; remaining corrections are listed in the Grade 5 frame, For the lead item 2. Product descriptions and first-teaching placements require reconciliation with the corrected source map.

Replace this status with verified completion details when the changes exist.

### 7. The earlier decision entry still presents six answered questions as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Grade 5 independent frame read  
**Confidence:** firm  
**Location:** `docs/agents/decisions/DESK-ANSWERS.md:529-542`.

The entry says no decision has been made, repeats “Waiting for Cory’s yes,” and says findings are not logged. Later entries record the answers, application, fallback choice, and logging.

**Why it matters:** It reopens settled questions, including whether Grade 5 teaches foundational skills.

**Exact fix:** Replace its live status language with:

> Resolved after this entry: the six questions were answered under q-ela-piece-2 on 2026-11-12. The fallback choice was completed in the subsequent fallback-hero decision, and the ELA findings were logged as recorded under “Sara’s pieces 1 and 2 taken in.” Earlier text choices remain historical and must be read alongside the later course-text decision.

Retain separately verified rights-review work as pending.

### 8. The intake entry also leaves the answered ELA card open

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Grade 5 independent frame read  
**Confidence:** firm  
**Location:** `docs/agents/decisions/DESK-ANSWERS.md:548,554`.

The intake note calls `q-ela-piece-2` unanswered and still open. The following entry records Cory’s answers and their application.

**Why it matters:** Correcting finding 7 alone leaves another false open status.

**Exact fix:** Replace both references with:

> q-ela-piece-2 was answered and applied on 2026-11-12; see the following entry.

Keep unrelated questions separately identified according to their actual status.

### 9. The rubric review still treats foundational-skills scope as undecided

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Grade 5 independent frame read  
**Confidence:** firm  
**Location:** `docs/reviews/rubric-ela-2026-11-11.md:309-317`.

Its “For Cory” section still asks whether Grades 3 to 5 claim foundational skills. The decision register, current rubric, and Grade 5 frame all record yes.

**Why it matters:** The expert’s required reading sends reviewers back to a false scope question about an applicable gateway.

**Exact fix:** Add this resolution and remove the live question:

> Resolved 2026-11-12, q-ela-piece-2: Curio Class Grades 3 to 5 teach foundational skills, and Gateway 1 applies in full. The taught sequence and checks remain implementation requirements.

## Ownership, days, seams, and cross-subject results

| Check | Result |
|---|---|
| Owned skills | All 30 placed exactly once: **16, 6, 5, 3** across units 1 to 4. No foreign-grade skill appears in the owning Skills column. |
| Standards | Parent-code coverage is complete. Findings 2 and 4 address teaching placement and incomplete requirements. |
| Unit reasons | The opening novel establishes routines; rainforest work develops research; athlete accounts support synthesis and opinion; water joins the year’s routines. These reasons hold. |
| Days by load | Unit 1’s 41 days support a long novel and continuing routines. Unit 4’s 35 days support substantial synthesis products despite only three new rows. Equal days per row would be inappropriate. The source-count discrepancy remains finding 1. |
| School year | The stated 160 includes four course-level assessment days and three respond days, leaving about 20 days within a 180-day year. |
| Source eligibility | No prohibited edition or reference curriculum is mapped. State explicitly that the standard rainforest branch is selected and the alternative life-science module is unused. |
| Grade 4 seam | Handoffs are picked up, including higher independent-reading demand, longer words, and increased writing expectations. |
| Grade 6 seam | Skill handoffs agree. Grade 6 explicitly develops the water thread through floods, weather, and warnings. |
| Science | Ecosystem instruction overlaps the rainforest unit. Water instruction runs beside the final ELA unit. ELA supplies its own content bridges where necessary. |
| Social studies | Sourcing precedes ELA unit 3. Civil-rights history comes later, so the segregation explainer is necessary. Earlier social studies demands on ELA have explicit local bridges. |
| Mathematics | Hundredths retrieve Grade 4 work without assuming Grade 6 percent instruction. |

I disagree with the earlier recommendation to remove the flood story solely because Grade 6 also studies floods. The next frame deliberately inherits this knowledge and increases the analytical demand. Preserve that seam while ensuring the texts and tasks differ.

The earlier claim that no social studies lean comes later is too broad. Civil-rights history does come later, but the frame already provides the necessary bridge.

## Lens checklist: course frame layer

| Lens line | Status | Evidence |
|---|---|---|
| Units arise from specific topics and texts | **Met in design** | Concrete people, places, events, and proposed text sets. |
| Anchors are on file with complexity and placement evidence | **Missed** | Finding 3. |
| Texts avoid concentration in one era, tradition, or kind | **Missed as demonstrated evidence** | The proposed range is promising, but exact anchors, authorship, and counts remain unavailable. Finding 3 supplies the remedy. |
| A long text is read whole | **Met as a frame commitment** | The novel and biography; actual delivery remains dependent on the texts. |

Question percentages, finished scaffolds, lesson openings, and scoring materials belong to later layers and cannot be scored from this frame.

## What should be preserved

Keep the topic-based structure, repeated research, two whole long texts, text-dependent writing, named models, regular discussion, school-day device route, sensitivity provisions, and counted respond days.

## Settled by the expert

These are recommendations for the caller, not edits made during this read.

| Choice | Reason | File |
|---|---|---|
| Correct the base inventory to 154 lessons and the three ranges through lesson 13 | Verified directly from the archives | Grade 5 frame, Source map |
| Correct the source-map descriptions | The retained sequences must be identified accurately | Grade 5 frame |
| Retain the flood-to-weather knowledge seam | The next grade explicitly inherits and develops it | Grade 5 and Grade 6 seam notes |
| Add the five explicit requirements in finding 4 | Completes existing standards within existing units | Grade 5 frame |
| Use the provisional 10/10/10 skills allocation if 90 minutes is retained | Makes daily commitments visible for testing | Grade 5 frame, Days |
| Identify the unused alternative life-science branch | Makes source selection explicit | Grade 5 frame, Source map |
| Rewrite the stale completion and decision notes | The repository already establishes their status | Files named in findings 6 to 9 |

## For Cory

- **Scope:** Resolve the first-teaching ownership changes in finding 2 and their associated pacing redistribution.
- **Audience:** Decide the 90-minute assumption, given the base curriculum’s longer design and the proposed skills allocation.
- **People and money:** Identify the qualified ELA, rights, and sensitive-content readers, and any compensation.

## Limits and outside sources

Actual anchor quality, originality, precise reading difficulty, rights clearance, and classroom timing remain unjudged. The missing full gate does not withhold this verdict.

Sources opened during this read:

- [Common Core Grade 5 literature standards](https://www.thecorestandards.org/ELA-Literacy/RL/5/), [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/5/), [foundational skills](https://www.thecorestandards.org/ELA-Literacy/RF/5/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/5/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/5/), and [language](https://www.thecorestandards.org/ELA-Literacy/L/5/): full requirements.
- [2017 Grade 5 base curriculum map](https://el-education-production.s3.amazonaws.com/media/documents/Curriculum_Tools_Curriculum_Map_Grade5_0419.pdf): teaching sequences, products, and block structure.
- [Grades 3 to 5 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_3_5_Review_Criteria_2_1_bb1cc2d7c6.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_3_5_Evidence_Guide_2_1_e302cb51c2.pdf): foundational instruction, text analysis, balance, and pacing. Relevant sections checked, not the entire evidence guide.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): three-part text complexity.
- [Grade 5 comparison scope and sequence](https://www.coreknowledge.org/wp-content/uploads/2017/03/G5_CKLA_Detailed_ScopeSequence.pdf): integrated reading, writing, language, assessment, and response time. Reference only.
- [WWC elementary writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17): writing-process and transcription recommendations.
- [WWC reading interventions, Grades 4 to 9](https://ies.ed.gov/ncee/wwc/PracticeGuide/29): decoding and purposeful fluency, with its intervention-population limit.

**For the source list:** Record the comparison scope and sequence if absent. The hashed review PDFs opened through the [review-tools index](https://edreports.org/process/review-tools/ela) after the initial direct request failed.

**Verdict:** Revise before baselining. **Findings:** 9. **Report path:** `docs/reviews/frame-english-language-arts-grade-5-2026-11-14.md`, delivered here without writing a file.

