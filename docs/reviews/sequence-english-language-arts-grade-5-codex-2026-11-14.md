# Independent scope and sequence review: English Language Arts, Grade 5

**Review date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-english-language-arts-grade-5-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

Revise before unit planning. The four unit arcs, recurring research, foundational-skills sequence and cumulative-check placement are coherent, but several day rows claim evidence their named tasks do not supply, and the writing and shorter-path provisions remain incomplete. Align the claimed standards with observable work first, then repair the planning records without changing unit ownership or day totals.

**Finding count: 9.**

## What I read and checked

- The complete [scope and sequence](/S:/CurioClass/docs/courses/english-language-arts-grade-5/scope-and-sequence.md), all 160 day rows, the frame, all 154 source-map rows and the 25 central text-catalog records for this course.
- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, foundation, shared and ELA approaches, relevant roadmap sections, glossary, BASELINE rules 20 to 24, source register and sequence-writing rules.
- All grade 5 standards in `data/standards/ccss-ela-standards-full.txt`; grade 4, 5 and 6 ELA progression rows.
- The grade 4 ELA day map, to verify the assumed rows against actual teaching or assessment days.
- `docs/courses/CALENDAR.md` and every grade 5 row in `data/plans/calendar.csv`.
- Permitted earlier grade 5 frame reports, their correction record, ELA baseline reports and the grade 3 independent sequence report, for resolved issues and repeat classification.
- The lesson-file inventories in all twelve selected grade 5 base-unit archives, plus the published base curriculum map.
- Outside standards, review guidance, research guidance and comparison curriculum material linked below.

The blind-file exclusions were respected. Repeat tags refer to the permitted earlier reports inspected.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Reported zero sequence failures for this course, then stopped elsewhere because Python lacks `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; grade 5 ELA checks fall in weeks 17 and 32. |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-5` | Passed, zero failures: 153 unit days plus seven course-level days. |
| `python -X utf8 scripts/stale.py check` | Passed, 56 files and zero failures. Semantic stale notes remain below. |
| `python -X utf8 scripts/sequence.py check english-language-arts-grade-5` | Passed, zero failures. |

The incomplete repository-wide gate does not prevent this verdict.

## Findings, most serious first

### 1. Several assessment rows claim standards without naming matching evidence

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, assessment-to-code mismatches also appear in the earlier grade 3 sequence read  
**Confidence:** firm

**Location:** Days 38, 118, 122 and 156.

| Day | Problem | Exact fix |
|---|---|---|
| 38 | RL.5.5 is assigned to a reading suite naming one fresh scene and a short stanza supplement. Neither, as described, supplies a series of chapters, scenes or stanzas whose relationship establishes a whole text’s structure. | Name a brief independent verification using the completed novel’s chapter map or the complete two-scene play. Ask how the parts fit together. Place it within the existing reading allocation. |
| 118 | SL.5.4, SL.5.5 and SL.5.6 accompany presentation planning, alongside account and argument verification. No assessed presentation or completed media product is specified. | Identify presentation planning as preparation. Reserve the speaking evidence for days 121 and 123, and remove unsupported assessment claims from day 118. |
| 122 | SL.5.4 and SL.5.6 accompany portfolio verification and display creation, with no named spoken performance. | Remove these assessment claims from this row. Keep their evidence on days 121 and 123. Retain SL.5.5 only with an explicit explanation of how the completed display strengthens a presentation’s main idea. |
| 156 | RL.5.7 accompanies water presentations and source checks. Explaining an informational leaflet’s visual does not itself demonstrate analysis of visual contributions to literary meaning, tone or beauty. | Keep the independent literary visual analysis on day 152 as the closing RL.5.7 evidence. Remove the repeated claim from day 156 unless that day explicitly uses and verifies the literary-analysis record. |

The [literature standards](https://www.thecorestandards.org/ELA-Literacy/RL/5/) distinguish whole-text structure and literary visual analysis; the [speaking standards](https://www.thecorestandards.org/ELA-Literacy/SL/5/) require actual reporting, media use and adaptation of speech.

**Why it matters:** A writer could follow these day descriptions faithfully while producing assessment records that overstate what each child demonstrated.

After these corrections, audit every assessment row using the same rule: each listed demand needs a named task, product feature, observed performance or explicitly identified portfolio evidence. Full item wording can remain with unit planning.

### 2. Day 23 claims the complete narrative standard before its new demands are taught

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete task-to-standard coverage is an earlier ELA review finding type  
**Confidence:** likely

**Location:** Day 23, followed by days 29 to 33.

Day 23 asks for a two-voice poem showing contrasting responses to one event, but lists W.5.3a through e and the parent code. The first explicit narrative model comes on day 29; pacing and transition-clause instruction follow on day 31.

A contrast poem need not contain a naturally unfolding event sequence, varied transitions or a conclusion growing from narrated events. The [writing standard](https://www.thecorestandards.org/ELA-Literacy/W/5/) requires those features.

**Why it matters:** This both uses new narrative demands before their explicit instruction and makes a comparison exercise appear to carry the complete narrative standard.

**Exact fix:** Keep day 23 as text-based comparison and poetry composition under RL.5.3, W.5.10 and its applicable language work. Remove the blanket W.5.3a to e and parent-code claim there. Keep full narrative teaching and assessment on days 29 to 33 and 39.

### 3. The twenty-entry writing cycle does not constitute a writing calendar

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, grade 3 sequence finding 4 and ELA baseline writing-accounting concerns  
**Confidence:** firm

**Location:** Scope and sequence, line 71; writing products across all four units.

The proposed six opinion, seven informative and seven narrative entries have no assigned days, products or source texts. Distribution is delegated to future unit plans. Consequently, the sequence cannot establish its writing shares or show how short responses relate to substantial process pieces.

The existing extended products visibly include two sustained narratives, several informative products and two opinion essays. This observation does not establish the final proportions, because the full ledger is missing.

The [grades 3 to 5 evidence guide, PDF pages 109 to 111](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Evidence-Guide.pdf) distinguishes on-demand and process writing. Its 30/35/35 distribution concerns process writing and is reported narratively, rather than scored separately.

**Why it matters:** Short exit responses could be counted to disguise an uneven process-writing distribution, or writers could add unnecessary pieces to satisfy an abstract cycle.

**Exact fix:** Replace the reservation with a complete planned-product ledger giving each substantive piece:

- Type and source texts.
- Drafting, feedback, revision and completion days.
- Process or one-sitting status.
- One identifier retained across revisions.

Report process-writing distribution separately from short-response practice. Adjust existing work where necessary rather than inventing additional products to repair a percentage.

### 4. The shorter-period provision retains all 90 minutes

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, grade 3 sequence finding 5  
**Confidence:** firm on the missing reduced-time route

**Location:** “Shorter path,” line 205.

The offered schedules, 60 plus 30 or 45 plus 45 minutes, split the original allocation into sessions. They are useful scheduling accommodations, but provide no route for a school with one shorter daily literacy allocation. The paragraph acknowledges this limitation.

**Why it matters:** Such a teacher still cannot determine what fits, what becomes less frequent or which work can be combined.

**Exact fix:** Add a provisionally budgeted reduced-time option, with minutes for the unit lesson, word work, reading practice, grammar and assessments. Name the repeated demonstrations, copying or publication work reduced on particular days. Check that option against demanding days such as 38, 78 and 153 while preserving owned instruction and assessment evidence.

If no reduced-time option can preserve the course, label this requirement unresolved and present the demonstrated minimum time for Cory’s scope decision. Do not describe the split-session option as completing that requirement.

### 5. The ten-day-short route folds the wrong work on day 106

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** firm

**Location:** Shorter-path table, line 217; days 105 to 107.

The table calls day 106 an “opinion plan” and moves argument-map completion to day 107. In the authoritative CSV:

- Day 105 plans the opinion on an argument map.
- Day 106 drafts the introduction.
- Day 107 drafts a reason paragraph.

The fold therefore repeats planning while leaving the omitted introduction without a clear home.

**Why it matters:** Following the shortened route can remove the instruction and writing carrying W.5.1a immediately before the independent essay.

**Exact fix:** Retain day 106 as the fold-in day, but rename it “opinion introduction.” Use day 105’s completed plan to draft the introduction in the first fifteen minutes of day 107, then draft the reason paragraph. Preserve the explicit topic, opinion and logical grouping requirements. No assessment day or owned part needs to move.

### 6. Core-text balance is calculated from catalog labels rather than instructional use

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, grade 3 sequence finding 6 and earlier grade 5 anchor-evidence concerns  
**Confidence:** firm

**Location:** “The text and skills path,” line 63; “For the lead,” item 4.

The 60/40 count includes only five records labelled `anchor`. It excludes required core instruction on the declaration, rainforest adventures, athlete accounts, illustrated river story and poems because their catalog label is `paired`.

The [evidence guide, PDF page 55](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Evidence-Guide.pdf) defines anchor/core status through instructional use. A paired relationship does not exclude a text from core instruction.

All 25 scheduled catalog records comprise **10 literary and 15 informational records**, provisionally **40/60**. This is not a final selection count: several records bundle multiple texts, and assessment-only or background selections need separate treatment.

**Why it matters:** The present count can misdirect future text decisions and gives an incomplete account of whole texts, excerpts and genres.

**Exact fix:** Identify core status separately from `paired`, classify each scheduled record by actual use, unpack collections into selections when chosen, and recount. Treat the present figures as provisional. No additional text needs commissioning merely to make five catalog labels divide evenly.

### 7. Days 53 and 54 contradict the stated single-response convention

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** firm

**Location:** Unit 2 assessment description, line 95; response convention, line 143; days 53 and 54.

The prose treats days 53 to 54 as a multi-day research-and-discussion assessment and says response occurs on its last day. Both CSV rows instead reserve a final fifteen-minute feedback-and-retry block: **30 minutes across two days**.

**Why it matters:** The writer receives two incompatible directions about whether these are one assessment with one response or two separately closed assessments.

**Exact fix:** Keep the combined assessment interpretation. Use day 53’s final fifteen minutes to prepare the assessed discussion from completed research notes; place the assessment’s feedback and retry on day 54. Update both day notes and the summary to identify that single response allocation.

The other multi-day response placements inspected are distinguishable and counted once.

### 8. The prerequisite audit can now close, but active notes still describe it as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale readiness and completion guidance appears in the earlier grade 3 sequence read  
**Confidence:** firm

**Location:** Prerequisite introduction and table, lines 9 to 47; “For the lead,” item 2; frame readiness wording; rubric Gateway 1 status cells.

The scope says no grade 4 ELA day map exists. It now exists, and every one of the thirty directly assumed ELA rows has day-level teaching or assessment evidence. Their last-use grade is therefore **4**, supporting retrieval in grade 5.

The conditional correction rule also places a possible unit 1 readiness check after its hook on day 1. The current user brief explicitly requires the start-of-year check instead. No such readiness check is actually scheduled, so this is a faulty future instruction rather than a present first-day assessment.

The frame still calls some grade 4 retrieval work readiness. The rubric still says no grade 3 to 5 scope and sequence exists.

**Why it matters:** These live instructions can reopen settled handoffs or reintroduce unnecessary assessments.

**Exact fix:** Replace the provisional ELA audit with verified grade 4 day references, remove its pending action, and retain retrieval. Correct the conditional unit 1 rule to the start-of-year check specified in this brief. Update frame terminology and rubric evidence-status cells while retaining the limits on unfinished texts and untested timing.

The excluded older math day map remains an explicitly unverified handoff.

### 9. The supposedly absent base lesson 14 is present under an unusual filename

**Severity:** Minor  
**LAYER:** base text  
**REPEAT:** new  
**Confidence:** firm

**Location:** “Source decisions,” line 162; source-map row `G5M3U2L14`.

The archive contains:

`G5M3U2/G5M3U2L14-ModuleLessons-download/G5M3U2L14-ModuleLessons .pdf`

There is a space before `.pdf`. The scope and source-map reason incorrectly say the separate lesson file is absent.

**Why it matters:** The next writer may rely on an overview instead of consulting the available lesson.

**Exact fix:** Replace the absence statement with the exact archive-member location. Keep its placement on day 109. No lesson or day is missing from the map.

## Other required judgments

### Order and days by load

| Unit | Days | Newly owned rows | Assessment-labelled days | Judgment |
|---|---:|---:|---:|---|
| 1 | 41 | 18 | 9 | The whole novel, initial routines, essay and monologue justify the longest allocation. Day 23 needs finding 2’s correction. |
| 2 | 39 | 6 | 12 | Informational reading and research precede literary explanation and narrative transfer. Five closing assessment days also carry revision and device work. |
| 3 | 40 | 5 | 11 | Whole-biography reading precedes account comparison, argument mapping, opinion and presentation. Three substantial products justify the allocation. |
| 4 | 33 | 1 | 11 | The load includes continued language work, research, announcement, essay, leaflet and presentation. One newly owned row does not mean one row’s worth of total work. |

No demonstrated unit-wide excess or shortage warrants resizing a unit. The crowded reading suite on day 38 and the multi-text verification on day 153 require timed scrutiny when texts and items exist.

### Prerequisite last use

Each row below has grade 4 day-level evidence. The examples establish use in the immediately preceding grade; they are not claims that these are the final practice days.

| Earlier row | Grade 4 evidence day |
|---|---:|
| e4-evidence-inference | 9 |
| e4-theme-summary | 9 |
| e4-character-depth | 13 |
| e4-lit-word-meaning | 35 |
| e4-poetry-drama | 34 |
| e4-narration-pov | 8 |
| e4-traditional-tales | 115 |
| e4-reading-range | 35 |
| e4-main-idea-summary | 44 |
| e4-explain-events | 42 |
| e4-text-structure | 48 |
| e4-firsthand-secondhand | 129 |
| e4-visual-info | 48 |
| e4-reasons-evidence | 86 |
| e4-integrate-two | 47 |
| e4-academic-words | 44 |
| e4-word-strategies | 54 |
| e4-long-words | 158 |
| e4-fluency | 35 |
| e4-opinion | 116 |
| e4-informative | 17 |
| e4-narrative | 76 |
| e4-writing-tasks | 158 |
| e4-writing-process | 27 |
| e4-research | 56 |
| e4-discussion | 13 |
| e4-presenting | 38 |
| e4-formal-informal | 151 |
| e4-grammar | 158 |
| e4-conventions | 158 |

**Treatment:** retrieval for all thirty. No older ELA prerequisite was found wrongly retrieved, and no year-before ELA row is actually scheduled as readiness in the grade 5 CSV. No scheduled readiness check occupies a unit’s first day or sits weeks ahead.

### Standards in full

The sequence assigns instructional days across all owned lettered families:

| Family | Principal placements |
|---|---|
| RF.5.3a; RF.5.4a to c | Daily word work, twice-weekly rereading, performance samples and seasonal screens |
| W.5.1a to d | Days 104 to 110; return on 147 to 151 |
| W.5.2a to e | Days 24 to 28; closing verification on 40 |
| W.5.3a to e | Days 29 to 33; closing revision on 39 |
| W.5.9a and b | Days 5, 26, 38 and 82, with later source-based writing |
| SL.5.1a to d | Days 10 to 12 and 41, with recurring formal discussions |
| L.5.1a to e | Days 15, 18, 25 and 29; closing language tasks on 39 |
| L.5.2a to e | Days 17, 19, 23 and 27; closing tasks on 39 |
| L.5.3a and b | Sentence work from day 25; varieties work in units 2 and 4 |
| L.5.4a to c | Days 4 and 7, continued vocabulary work and closing evidence on 38 |
| L.5.5a to c | Days 14, 16 and 21; assessment reservations on 22 and 38 |

These are planning placements, not certification of unwritten items. W.5.6’s completion in unit 2 and L.5.3b’s continued work in unit 4 are explicitly identified. Findings 1 and 2 distinguish valid placement from unsupported claims on individual days.

### Calendar, checks, candidates and source map

| Requirement | Judgment |
|---|---|
| Mid-unit assessments | Present in every unit, all longer than 25 days. |
| Closing response | Once on days 41, 80, 123 and 156. Finding 7 addresses the separate interim contradiction. |
| Checks do not repeat | Met. Days 81 to 82 transfer rainforest-unit skills to earlier farm-related content. Days 157 to 158 use earlier rainforest content for water-unit skills. |
| Target weeks | Met: weeks 17 and 32. |
| Same-year science leans | Ecosystems overlap school days 21 to 48; day 42 supplies a bridge. Water distribution ends on 123; protection runs 125 to 147, with ELA bridges placed. |
| Same-year social studies leans | Sourcing precedes ELA account work. Segregation and research come later, with bridges on days 84 and 45 to 52. |
| Candidate cells | All have explicit keep decisions, locations and zero additional days. Their work is assigned inside existing blocks. |
| Ten-day-short year | Ten unassessed fold-ins are named. Finding 5 repairs the day 106 mismatch. Check meetings 75 to 76 and 147 to 148 calculate correctly. |
| Source-map completeness | 154 unique base lessons: 152 keep decisions and two merge rows landing on day 135. No cuts or order reversals found. |
| Source selection | The unused life-science companion and the treatment of the second base block are explicitly explained. |
| Recording merge | Its prepared script, short recordings and parallel rotation have a stated minute budget. Classroom feasibility remains provisional. |

## Lens checklist: scope and sequence layer

| Lens line | Result |
|---|---|
| Text demand climbs, or departures have a reason | **Met as a commissioning plan.** Support fades toward independent high-band reading. Actual demand remains unverified because the texts are unfinished. |
| Research and full-process writing recur | **Met.** Research is taught and reused; process writing recurs across units. Finding 3 concerns accounting and distribution. |
| Formal discussion occurs often | **Met.** Fourteen named formal discussions, additional assessed discussions and daily partner talk. |
| K to 2 phonics order aligns with decodable texts | **Not applicable.** Grade 5 instead has an explicit long-word, spelling and fluency sequence. |

## What is right and should remain

Preserve the four unit arcs, corrected base-lesson inventory, whole novel and biography, repeated research, decoding-before-context rule, source-based writing, explicit technology collaboration and school-day device route. Preserve the individual speaking evidence, earlier-topic cumulative checks, cross-subject bridges and sensitivity provisions.

The earlier frame’s missing lessons, monologue omission and misplaced literary pair have been corrected. This report does not reopen those settled findings.

## Settled by the expert

Recommendations for the caller to apply; no edits were made.

| Choice | Reason | File or location |
|---|---|---|
| Align assessment claims with named evidence | Prevent unsupported coverage records | `days.csv`, days 38, 118, 122 and 156 |
| Keep day 23 as comparison and poetry practice | Full narrative demands are taught later | `days.csv`, day 23 |
| Replace the abstract writing cycle with a product ledger | Establish actual purposes, process opportunities and distribution | Scope and sequence |
| Correct the day 106 fold to introduction drafting | Preserve W.5.1a on the shorter route | Shorter-path table |
| Classify core texts by instructional use | Catalog relationship labels do not establish core status | Text accounting |
| Keep one response allocation for days 53 to 54 | Match the stated multi-day convention | Unit 2 prose and day notes |
| Close all thirty ELA handoffs as grade 4 retrieval | Day-level evidence now exists | Prerequisite table and pending notes |
| Correct the lesson 14 archive location | The lesson is present | Source-map reason and source notes |
| Retain all four unit lengths and current ownership | No demonstrated need to resize or relocate standards | Frame and sequence |

## For Cory

- If the course is intended to serve schools with a single daily literacy allocation below 90 minutes, settle that time and audience boundary after a concrete reduced-time schedule has been tested. The existing provisional 90-minute decision need not be reopened for the item-level corrections above.

## Limits and outside sources

Most original texts remain unwritten, agency selections remain unchosen and rights work remains incomplete. Final text quality, reading volume, complexity, question percentages, scoring quality and classroom timing cannot yet be established. The missing course-level `texts.csv` remains an inherited production dependency, already acknowledged by the sequence.

I checked archive placement and filenames, not every base lesson’s full instructional content. The older math day map was excluded. **No substantive finding rests solely on memory.**

Sources opened in this run:

- Common Core grade 5 [literature](https://www.thecorestandards.org/ELA-Literacy/RL/5/), [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/5/), [foundational reading](https://www.thecorestandards.org/ELA-Literacy/RF/5/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/5/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/5/) and [language](https://www.thecorestandards.org/ELA-Literacy/L/5/): checked against the repository’s complete standard text.
- [Grades 3 to 5 review criteria](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Review-Criteria.pdf) and [evidence guide](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-3-5-v2.1-Tools_Evidence-Guide.pdf): relevant core-text, pacing and writing provisions, not a full scored course review.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): quantitative, qualitative and reader/task considerations.
- [Federal elementary-writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17): explicit writing-process instruction, varied purposes and sentence-writing support. It does not prescribe the day allocations recommended here.
- [Base curriculum’s grade 5 map](https://el-education-production.s3.amazonaws.com/media/documents/Curriculum_Tools_Curriculum_Map_Grade5_0419.pdf): module arcs, products, assessment purposes and two-block design.
- [Comparison grade 5 scope and sequence](https://www.coreknowledge.org/wp-content/uploads/2017/03/G5_CKLA_Detailed_ScopeSequence.pdf): integration of reading, writing, grammar, morphology, assessment and response. Consulted as reference only.

**For the source list:** The two review-tool CDN addresses above worked. The hashed criteria address recorded in the local rubric was inaccessible through the web tool. The lesson 14 archive note also needs correction as specified in finding 9.

**Verdict:** Revise before unit planning. **Findings:** 9. **Report path:** `docs/reviews/sequence-english-language-arts-grade-5-2026-11-14.md`, supplied here without creating a file.