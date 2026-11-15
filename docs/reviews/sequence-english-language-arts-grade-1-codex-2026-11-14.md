# Independent scope and sequence review: English Language Arts, Grade 1

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-english-language-arts-grade-1-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were created, edited or deleted.

## Verdict

Revise before unit planning: the four-unit architecture, teaching arcs and day allocations are defensible, but several assessment claims exceed their named evidence. The biggest risk is apparent completeness, compounded by text records that remain provisional after their agreed completion point. Repair the assessment descriptions, complete the text records, remove the unsupported readiness exception and specify a usable shorter-period route while preserving the current unit ownership and totals.

## What I read

- `docs/agents/EXPERT.md`, `docs/agents/lenses/ela.md`, `docs/RUBRIC-ELA.md`, the foundation, shared and ELA approaches, source-register evidence notes, glossary, relevant BASELINE rules and requested roadmap sections.
- The complete grade 1 scope and sequence and all 160 day records.
- The complete grade 1 frame, its source map, all 31 grade 1 progression rows, kindergarten prerequisites and grade 2 handoff rows.
- Grade 1 standards, including every lettered part, in `data/standards/ccss-ela-standards-full.txt`.
- `docs/courses/CALENDAR.md` and every grade 1 subject’s calendar rows.
- All 17 grade 1 catalogue entries in `data/plans/ela-texts.csv`.
- Earlier grade 1 frame findings, their K to 2 fix disposition, and relevant assessment and retrieval findings in the grade 1 social studies sequence review.
- The sequence-writing rules and base-text register.
- The base source-map lesson inventory and referenced archive members. All referenced archive members exist. I did not reread every source lesson body.
- Outside sources linked below.

The prohibited files were not opened. Prior-session memory informed the review method only; no course-specific finding rests on unaided memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Grade 1 sequence reported 0 failures; the repository-wide run subsequently reported the missing grade 2 sequence and stopped with `ModuleNotFoundError: No module named 'markdown'`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; grade 1 ELA checks fall in weeks 16 and 32, with no reported stagger-rule break. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-1` | Passed: four units, 160 days, including 154 unit days and six course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed: 56 files checked, 0 failures. |

The interrupted repository-wide gate does not determine this curriculum verdict.

## Findings, most serious first

### 1. Some assessment codes lack the performances needed to support them

**Severity:** High  
**LAYER:** sequence  
**REPEAT:** yes, the same assessment-to-standard mismatch appears in `sequence-social-studies-grade-1-codex-2026-11-14.md`, finding 1  
**Confidence:** firm on the explicit omissions; likely on the unit 2 evidence-record repair

**Locations:** `days.csv`, days 70 to 75, 129 and 158; corresponding assessment paragraphs.

The assessment contract correctly requires evidence for every listed code, but these rows do not consistently supply it:

| Location | What is wrong | Exact fix |
|---|---|---|
| **Day 129** | Codes include both `RL.1.9` and `RI.1.9`. The named task compares characters’ experiences in two stories and explicitly checks only `RL.1.9`. The informational comparison begins on day 131. | Remove `RI.1.9` from day 129. Retain its teaching on days 131 and 135 and its complete assessment on day 156. This changes no ownership or allocation. |
| **Unit 2 closing observations, days 70 to 75** | Unit 2 completes the continued short-vowel, digraph and cluster teaching, but its closing foundations performance names inflections only. The cumulative short-vowel evidence appears in the separate course-level check on day 76. The unit record does not identify which cycle observations complete `RF.1.3a/b`. | Explicitly incorporate the relevant cumulative cycle evidence into the unit 2 closing record. Use day 72 to confirm any missing short-vowel, digraph or cluster performance, alongside the existing endings check. Name the evidence and codes in both CSV and prose. |
| **Day 158** | Codes include all four phonemic-awareness parts and all-letter printing. The task names reading, spelling and passage performances, but no oral vowel discrimination, blending, isolation or segmentation, and no printing sample or dated-sample reference. It also lists full fluency without naming successive readings or context-confirmed correction. | Add the four brief oral phoneme performances to the two-day conference rotation. Explicitly reference dated evidence for all 52 letter forms and confirm missing forms. Name purpose/understanding, a successive reading for accuracy/rate/expression, and monitoring or correction after decoding. |

These distinctions are substantive: spoken phoneme work, printing, informational comparison and successive oral readings cannot automatically be inferred from a phonics list or story comparison. The [Common Core standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf) distinguish those performances.

**Why it matters:** A unit writer could build exactly the described tasks and still record complete codes without collecting the required evidence.

Preserve the existing assessment windows and respond allocations. The repair is clearer evidence placement, not a larger final-day test.

### 2. Text records remain deferred beyond the agreed scope and sequence stage

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, grade 1 frame independent finding 2, accepted in part in `frame-ela-k-2-fixes-2026-11-14.md`  
**Confidence:** firm

**Locations:** Scope and sequence introduction, assessment contract and For the lead item 2; `data/plans/ela-texts.csv`.

The earlier disposition placed text records **with the scope and sequence**. This draft instead leaves their completion to unit planning.

The catalogue currently contains:

- Eleven entries marked `to write`.
- Three marked `to choose`.
- Two marked `on file`.
- One marked `to confirm`.
- Blank rights-basis and rights-check fields for all 17 entries.

The catalogue is an inventory, not a completed set of text records. Its general demands do not establish the actual reading load, text difficulty, matched supports or suitability for the assigned tasks. `g1-u1-04` still leaves even the classroom-tool model selection unresolved.

The sequence makes useful choices, including original sky and bird poems and a five-chapter story, but those choices have not reached the catalogue. The [K to 2 review criteria, indicators 2b and 2c](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf), require documented complexity and supports matched to the text.

**Why it matters:** Replacing the base books changes the material on which its teaching and assessments depend. Plausible descriptions cannot establish that the replacement supports the planned work.

**Exact fix:**

1. Complete an inspectable record for each selected text, with a stable file/source pointer, reading role, actual length, qualitative demands, reader/task judgment, placement reason, matched supports and rights status.
2. Name the exact classroom-tool models used on days 7 and 22 onward.
3. Record the settled original-poem choices, five-chapter structure and located human-helpers source in the catalogue.
4. Complete the replacement texts needed to substantiate those records before treating the sequence’s text-dependent claims as settled.
5. For poetry and beginning-reader texts, state why a quantitative measure is unsuitable where appropriate. Do not invent a grade 1 numerical threshold.
6. Keep the required text and sensitivity reads as explicit prerequisites before use.

This follows the accepted record-completion timing. It does not reopen the earlier rejected demand for a finished inventory before the frame.

### 3. Unit 1 claims a readiness exception that the current rule expressly overrides

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, stale frame readiness wording was also identified in the grade 1 social studies sequence read  
**Confidence:** firm

**Locations:** Unit 1 Readiness and retrieval paragraph; day 1; frame Days and Seams wording; For the lead item 1.

All **29 distinct assumed progression rows** were last taught or assessed in kindergarten. They therefore require retrieval in grade 1. The kindergarten day records contain assessment placements for all 29.

Nevertheless, day 1 carries `assess=readiness` and a marked baseline on kindergarten letters, sounds, CVC decoding and high-frequency words. The sequence calls this a frame exception. Sequence-write rule 2 expressly says the current rule wins over frame wording.

**Why it matters:** The sequence preserves an obsolete assessment requirement and presents it as authorized. This invites later writers to retain or expand the same exception.

**Exact fix:** Clear day 1’s readiness marker and remove the claimed exception. Use the existing foundations retrieval and days 2 to 5 small-group observations to identify and respond to gaps. Update the frame’s baseline and later-unit readiness wording to retrieval, and close the lead item as an editorial correction.

No new day, pre-unit slot or unit move is needed.

Unit 1 is the only unit that checks a year-before row as readiness. Units 2 to 4 correctly retrieve kindergarten prerequisites. No older prerequisite is incorrectly retrieved, and no readiness check is scheduled weeks ahead.

### 4. The shorter-period route has no stated duration or workable time budget

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the earlier K to 2 frame disposition required the shorter route to identify retained work and show that its minutes fit  
**Confidence:** firm on the missing specification; judgment call on the eventual minimum period

**Location:** Shorter path, first paragraph.

The paragraph identifies sensible priorities, but supplies neither a shorter period length nor minutes for its components. It explicitly limits its claim to occasional shorter days. It therefore does not establish how the course runs with a recurring shorter allocation.

The ten-day-shorter-year route is substantially more concrete and should be retained.

**Why it matters:** A teacher cannot determine whether the shorter-period route fits an available timetable or how deferred work avoids accumulating.

**Exact fix:** Name a proposed shorter daily allocation and budget both blocks within it. Identify the explicit teaching, matched reading, text encounter, response, small-group time and any practice moved to another day. Show a representative ordinary day and assessment day, including where displaced work fits.

Put any sustained change to the course’s supported daily allocation to Cory as a scope decision. Until settled, describe this honestly as an occasional-short-day contingency and mark the recurring shorter-period requirement unresolved.

## Order, load, assessments and candidates

The main instructional dependencies hold:

- Tool facts and paragraph models precede the designed-tool explanation.
- Tale reading and narrative models precede independent sun poems.
- Main-topic and feature teaching precede sustained bird research.
- Both bird stories are complete before the final story comparison.
- Author reasons precede the nest opinion.
- Context and word-part work precede the human-helpers transfer.
- Silent-e, r-controlled and vowel-team instruction precede the complete foundations observation.

| Unit | Days | Owned rows | Topic allocation | Judgment |
|---|---:|---:|---|---|
| Tools and work | 33 | 12 | 8 introductory, 10 story, 13 design/writing, 2 response | Defensible for launching routines and first informative writing. |
| Sun, moon and stars | 42 | 10 | 15 reading, 12 research/talk, 13 writing/publication, 2 response | Heavy writing, language and research load supports the allocation. |
| Birds’ amazing bodies | 41 | 4 | 10 introductory, 17 research/writing, 12 riddle/drawing, 2 response | Four owning rows understate the load because foundations and earlier writing continue. |
| Caring for birds | 38 | 5 | 10 story, 1 story response, 10 opinion including response, 17 research/publication | Dense but coherent; retain the allocation. |

No run is demonstrably far over or under its load. Unit 4’s nine explicitly scheduled grammar teaching days, followed by repeated application, warrant protection.

All four units exceed 25 days and contain mid-unit assessments. End observations are distributed across several days. Each unit names its final 20-minute response allocation once; dedicated mid-unit and course-level respond days are separately identified.

All candidate cells are settled as kept, with costs inside the units:

| Unit | Topic days carrying assessment evidence | Dedicated mid-unit respond days |
|---|---|---|
| 1 | 8, 19, 31 to 33 | 9, 20 |
| 2 | 47, 48, 61, 70 to 75 | 49, 62 |
| 3 | 86, 104, 105, 115, 118, 119 | 89, 107 |
| 4 | 129, 139, 147, 155 to 157 | 130, 140 |

Foundations progress samples occupy their existing blocks. Finding 1 concerns the evidence attached to these allocations.

## Standards in full

I found no wholly absent owned standard or lettered part at the teaching-placement level. The main multipart placements are:

| Standard parts | Named teaching or performance placement |
|---|---|
| `RF.1.1a` | Sentence-feature routine from day 2; observation on 31. |
| `RF.1.2a–d` | Oral vowel contrast and blending/isolation/segmentation, explicitly elaborated on days 6 and 11; observation on 31 and continued foundations. |
| `RF.1.3a–g` | Cycles 1 to 25, including named continuations; complete parent-standard observation on 155. |
| `RF.1.4a–c` | Matched reading, purposeful rereading and correction after decoding throughout; explicit unit observations. |
| `SL.1.1a–c` | Recurring linked discussion, rules and clarification; explicit observation on 33. |
| `L.1.1a–j` | Printing on days 2 to 27; sentence kinds in unit 2; grammar schedule on days 121 to 133; complete observation on 156. |
| `L.1.2a–e` | Foundations spelling; capitals and commas on days 50 to 60; complete editing performance on 72. |
| `L.1.4a–c` and parent | Context on 121, multiple meanings on 124, full strategy work on 135 and transfer on 147/157. |
| `L.1.5a–d` and `L.1.6` | Categories, definitions, real-life connections, shades and relational vocabulary on days 3 to 6; observation on 33. |

Teaching placement does not resolve the assessment gaps in finding 1 or demonstrate the quality of unwritten texts.

## Readiness and retrieval audit

Every prerequisite below has **last-use grade K**.

| Grade 1 unit | Prerequisites first needed here |
|---|---|
| 1 | Print concepts, letter names, phonemes, letter sounds, CVC decoding, high-frequency words, emergent reading, group reading, story elements, pictures/words, key details, informative writing, discussion, sentences, word relationships. |
| 2 | Retelling, books/authors, connections, narrative, revision/publication, shared research, oral description, unknown-word work. |
| 3 | Main topic and early phonological awareness. |
| 4 | Author reasons, opinion, comparison and oral grammar. |

Repeated prerequisites and same-year models return within the later units. Retrieval is the correct treatment throughout; finding 3 repairs the sole readiness exception.

## Calendar and nonrepeating checks

The checks match the grade 1 targets:

- Mid-year: days 76 and 77, week 16; respond on 78.
- Year-end: days 158 and 159, week 32; respond on 160.
- Nearest math one-to-one check gaps are 16 and 10 school days, exceeding the five-day minimum.

| Lean | Other subject’s availability | ELA use | Judgment |
|---|---|---|---|
| Sky patterns, `1-ESS1-1` | Science school days 3 to 18 | ELA day 34 onward | Available first; day 34 carries a bridge if delayed. |
| Body parts, `1-LS1-1`, for informative writing and research | Science school days 20 to 43 | ELA day 79 onward | Available first; day 79 carries the factual bridge. |
| Claim/reason writing | Social studies school days 33 to 51 | ELA unit 4 | Earlier context; ELA still explicitly teaches its opinion standard. |

The course-level checks explicitly transfer recently assessed skills to earlier content. Mid-year uses tools and the bicycle story; year-end uses earlier tools, sky and bird-body content. This satisfies the nonrepetition requirement at sequence level.

## Shorter year and source map

The ten fold-in pairs are explicitly named: **14→15, 17→18, 27→28, 45→46, 60→59, 69→68, 102→101, 111→110, 127→128 and 153→154**.

None removes a reserved assessment or cycle-end progress sample. The sequence addresses concurrent foundations lessons, preserves new mappings and protects the receiving day’s sample. These are plausible planning choices, with classroom feasibility still untested.

The source map accounts for:

- All 146 topic lessons, including one split across days 127 and 128.
- All 130 foundations lessons.
- Seven added topic response days and 24 foundations consolidation days.
- Twenty-four decodable readers and one poem.
- Twenty-six handwriting pairs.
- Six course-level days.
- Explicit exclusions for Labs and source media.

Mapped topic and foundations lessons preserve source order. The broad foundations order agrees with the [base text’s grade 1 year-at-a-glance](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_Grade1.pdf). The declared pattern delays and exclusions require the promised checks of each adapted reader; their actual execution cannot yet be judged.

## Lens checklist: scope and sequence

| Lens line | Result |
|---|---|
| Text demand climbs, or its order is explained | **Met provisionally:** the rationale grows from concrete tool texts to connections, searchable information and a sustained chapter plot. Actual demand remains unverified under finding 2. |
| Research recurs | **Met:** sky research and both bird units. |
| Full-process writing recurs | **Met:** all four units name planning, drafting, revision and editing. |
| Discussion occurs often | **Met in the sequence:** frequent linked exchanges and at least two routines weekly are promised. |
| K to 2 phonics sequence exists and aligns with decodables | **Met as a plan:** cycles and reader placements are mapped. Actual alignment awaits adapted texts and their pattern checks. |

The grades 3 to 12 numerical writing-share targets are appropriately not imposed on grade 1.

## Stale notes and earlier findings

The stale-note script passed, but semantic inconsistencies remain:

- The frame’s readiness wording conflicts with the current rule, addressed in finding 3.
- The catalogue still leaves poem authorship undecided despite the sequence’s original-text choice.
- The catalogue still says to locate the human-helpers source, while day 147 identifies its held title and location.
- The catalogue retains a four-to-five-chapter description after the sequence chooses five chapters.

The catalogue corrections belong with finding 2. They are not additional findings.

Earlier repairs to foundations order, later-unit continuations, multiple meanings, paragraph-frame origin, the second tale and cross-subject bridges are present. Those decisions should remain.

## What is right and should remain

- Four coherent topic units with explicit performance tasks.
- Concurrent topic and foundations blocks.
- Rich read-alouds alongside matched student decoding.
- Repeated research, writing and text-based discussion.
- Recorded individual contributions to two kinds of digital publication.
- Fresh earlier-content transfer on course-level checks.
- Explicit response allocations and a continuing catch-up routine.
- Respectful cultural framing and practical alternatives to home or outdoor observations.

## Settled by the expert

These are recommendations for the caller to apply. No files were changed.

| Choice | Reason | Files affected |
|---|---|---|
| Preserve all four unit allocations and ownership. | No demonstrated load imbalance warrants resizing. | Scope and sequence; days CSV |
| Remove `RI.1.9` from day 129. | That day assesses stories; informational comparison is taught and assessed later. | Days CSV |
| Complete unit 2 foundations evidence within its closing record. | Its continued short-vowel teaching needs an explicit completion record. | Scope and sequence; days CSV |
| Specify day 158’s missing performances and dated evidence. | The listed codes require distinct evidence. | Days CSV |
| Replace day 1 readiness with retrieval and responsive observation. | All assumed rows were used in kindergarten. | Frame; scope and sequence; days CSV |
| Retain the ten named shorter-year folds as provisional. | They preserve assessed work and identify concurrent foundations handling. | Shorter path |
| Complete and synchronize the text records at this layer. | This is the accepted timing and supports the proposed text-dependent work. | Text catalogue; text records; scope and sequence |

## For Cory

- **Scope/time:** Set the recurring shorter-period allocation the course is expected to support, or explicitly retain 120 minutes as its minimum. The current paragraph supports occasional shortened days only.

No new money, audience or outside-person decision is needed for the other repairs.

## Sources and limits

- [Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): checked grade 1 requirements and distinctions between assessment performances.
- [K to 2 review criteria, v2.1](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf): consulted foundational-skills sequencing, assessment, decodable alignment and text-record indicators. No rubric score is claimed.
- [Revised Publishers’ Criteria, K to 2](https://www.thecorestandards.org/assets/Publishers_Criteria_for_K-2.pdf): consulted cumulative foundations instruction and rich listening alongside beginning reading.
- [WWC foundational-reading guide summary](https://ies.ed.gov/ncee/wwc/Docs/practiceguide/wwc_found_reading_summary_051517.pdf): consulted taught-pattern practice, daily connected reading and corrective feedback. The full guide fetch timed out; the summary was accessible.
- [Base grade 1 foundations year-at-a-glance](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_Grade1.pdf): checked broad cycle order.
- [Core Knowledge grade 1 assessment/remediation guide](https://www.coreknowledge.org/wp-content/uploads/2017/01/CKLA_G1_ARG_U1_web.pdf): consulted its scope and sequence and introduction as a comparison for cumulative instruction and targeted response. It was used as reference only.

**For the source list:** Add or refresh the accessible K to 2 criteria, publishers’ criteria and WWC summary links where absent.

I could not judge finished assessment items, scoring guidance, final text quality, completed reader alignment or classroom timing. Those limitations do not prevent the sequence verdict.

**Verdict:** Revise before unit planning. **Finding count:** 4. **Report path:** `docs/reviews/sequence-english-language-arts-grade-1-2026-11-14.md`, supplied here only.

