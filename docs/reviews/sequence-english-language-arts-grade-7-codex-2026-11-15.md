# Independent read: Grade 7 English language arts scope and sequence

**Intended report path:** `docs/reviews/sequence-english-language-arts-grade-7-2026-11-15.md`  
**Delivery:** Complete report below. No file was written or edited.

## Verdict

The six-unit sequence is coherent and conditionally sound, with sensible teaching order, repeated research, sustained writing and well-placed cross-subject bridges. The clearest coverage gap is that Unit 3 lists L.7.6 on assessments without naming evidence of accurate vocabulary use and vocabulary gathering; the shorter-period route also remains dependent on unresolved workload budgets. Preserve the units and ownership, make that assessment evidence explicit, and settle the timing and stale instructions before treating the sequence as final.

**Finding count: 4.**

## What I read

- The complete Grade 7 scope and sequence, all 160 rows of `days.csv`, and the course frame.
- All 28 Grade 7 ELA progression rows, the Grade 6 prerequisite rows and relevant Grade 8 handoffs.
- The current Grade 6 day map to verify actual prerequisite use.
- All 33 Grade 7 rows in `data/plans/ela-texts.csv`.
- `CALENDAR.md` and the Grade 7 rows of `data/plans/calendar.csv`.
- The expert instructions, ELA lens, ELA rubric, glossary, sequence-writing rules, foundation, shared and ELA approaches, and relevant roadmap, baseline and source-access guidance.
- Both earlier Grade 7 frame reports, the Grade 5 sequence report, and targeted finding passages from the Grade 3 and Grade 4 sequence reports for REPEAT classification.
- Outside standards, review guidance, writing research and two curriculum designs, linked below.

The prohibited files were not opened. No substantive curriculum conclusion rests on memory. Saved memory informed report organization only.

### Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Grade 7 sequence reported 0 failures; global run failed on the missing Grade 8 sequence, then stopped because `markdown` was unavailable |
| `python -X utf8 scripts/frame.py calendar` | Passed; no stagger-rule breaks |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-7` | 0 failures |
| `python -B -X utf8 scripts/sequence.py check english-language-arts-grade-7` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

The incomplete global gate does not withhold this verdict.

## Findings, most serious first

### 1. L.7.6 is named on assessments without its complete performance

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, partial-standard assessment descriptions recur in the earlier Grade 7 frame reads  
**Confidence:** Firm

**Location:** `days.csv`, days 73 and 84; scope and sequence, Unit 3 assessment paragraph.

Both assessment rows list L.7.6. Their named tasks concern word meanings, tone, context, roots, reference entries, verification and word relationships. Those tasks demonstrate substantial vocabulary analysis, but neither row names a product showing accurate use of academic and domain vocabulary or the gathering of vocabulary knowledge when a word matters to comprehension or expression.

The prose promises “accurate academic/domain language,” but the CSV does not reserve that evidence. These are explicit demands of [L.7.6](https://www.thecorestandards.org/ELA-Literacy/L/7/).

**Why it matters:** A unit writer could build every named assessment task and still omit part of the listed standard.

**Exact fix:** Add to both assessment notes:

> The existing analytical response accurately uses selected academic and domain words. A brief vocabulary note identifies an important unfamiliar word or phrase, records the knowledge gathered about it and explains its contribution to comprehension or expression.

Day 84 uses fresh words and evidence. Keep the work within the existing response rather than adding another composition. Add the vocabulary-gathering expectation to the progression row’s abbreviated description when that layer is next maintained.

### 2. Reading volume and crowded-day budgets do not yet establish the shorter-period route

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, unresolved shorter-period feasibility recurs in the Grade 3 and Grade 4 sequence reads  
**Confidence:** Firm on missing budgets; judgment call on eventual feasibility

**Location:** Reading, writing and time; Text records; Shorter path; days 61, 86 and 96.

The draft budgets the novella in tenths and gives some individual text lengths, but it does not state each unit’s total reading volume divided between class and home. `APPROACH-ELA.md`, “Volume of reading,” requires that accounting.

Several days particularly need bounded commissions and a minute allocation:

- Day 61 reads both smallpox articles whole and begins comparison in a period containing 15 minutes of independent reading.
- Day 86 combines independent reading, an eight-minute formal discussion, ten-minute next-unit retrieval and response to research, talk and reading evidence.
- Day 96 combines independent reading, formal discussion, a mini-model and the first five-part argument.

Under the stated standard-period routine, day 96 leaves approximately **17 minutes for modelling and composition**, after independent reading, word work, discussion and the written response. Day 86 leaves approximately **seven minutes outside those reserved activities for other response work**, although its discussion can itself carry feedback.

The shorter-period section candidly says its route cannot yet be called runnable. That is an honest limitation, but it leaves the requested alternative unfinished. The [pacing evidence guide, indicator 2f](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf) asks for realistically completable schedules.

**Why it matters:** Unbounded text and product lengths can consume the minutes reserved for instruction, feedback or access support.

**Exact fix:** Add a six-unit reading-budget table with commissioned word totals, class/home allocation and the in-class catch-up provision. For days 61, 86 and 96, specify text or product limits, minutes and which activity supplies feedback evidence. Carry those allocations into the 40-minute route and the ten proposed folds. Retain its conditional status until selected texts and representative tasks have been timed.

### 3. The prerequisite verification hold is now obsolete

**Severity:** Low  
**LAYER:** sequence  
**REPEAT:** yes, Grade 5 sequence finding 5 identifies the same obsolete handoff hold  
**Confidence:** Firm

**Location:** Decisions that govern the days, prerequisite table and following paragraph; For the lead, first bullet.

The sequence says the Grade 6 day map is absent and assigns provisional last-use grades. That file now exists. All **29 distinct assumed Grade 6 rows** have Grade 6 teaching or assessment days.

Examples include narrator viewpoint on day 119, reading versus performance on day 124, media integration on day 140, research assessment on days 83 to 84, and section structure assessment on day 106. The resulting treatment is correct for every receiving unit: retrieval.

**Why it matters:** The obsolete hold sends the next reader back to completed work and makes a verified handoff appear unresolved.

**Exact fix:** Mark every listed prerequisite “last used in Grade 6, confirmed against its day map,” with a supporting day reference. Remove the absent-file statement, provisional conversion instructions and lead-verification request. Remove the hypothetical Unit 1 first-day readiness fallback as unnecessary; the run’s instruction places any genuine older prerequisite in the start-of-year check.

No unit was found checking a year-before row, retrieving a confirmed older row, or placing an actual readiness check on its first day.

### 4. The frame still gives contradictory assessment and readiness instructions

**Severity:** Low  
**LAYER:** frame  
**REPEAT:** yes, stale readiness wording recurs in the Grade 3 to Grade 5 sequence reads  
**Confidence:** Firm

**Location:** Frame, Days; Seams; Models carried; Course-level checks.

The sequence correctly applies the newer rules, but the frame still:

- Requires readiness checks on Grade 6 foundations at unit openings.
- Says the following course-level check substitutes for a unit’s end-of-unit assessment.
- Claims the longest run between course-level checks is 48 unit days, although Units 1 and 2 total **56**.
- Describes Unit 1’s story-map work as “how the drought acts on the family,” while the current river-family plan explicitly avoids that inherited drought plot.

**Why it matters:** A later writer starting from the frame can restore superseded assessment practices or commission the wrong story.

**Exact fix:** Replace the readiness wording with confirmed Grade 6 retrieval. State that every unit retains its own assessment and response, while following course-level checks use earlier-unit content for newly taught skills. Correct the three run lengths to **56, 48 and 44 unit days**. Replace the drought example with the effects of river conditions and fishing-season closure on family choices.

These are caller maintenance changes outside this read-only assignment.

## Order, assessments and days by load

| Unit | Days | Owned rows | Teaching / assessment / respond days | Judgment |
|---|---:|---:|---:|---|
| 1. Salmon year | 30 | 10 | 24 / 4 / 2 | Sustained reading precedes narrative composition; mid-unit evidence has response time |
| 2. Dust Bowl | 26 | 5 | 20 / 4 / 2 | History precedes fiction comparison; sentence models precede informative drafting |
| 3. Smallpox | 26 | 6 | 20 / 4 / 2 | Source comparison precedes research; publication precedes presentation and product assessment |
| 4. Athens | 22 | 3 | 18 / 3 / 1 | Background precedes primary rhetoric; written texts precede media versions |
| 5. Marathon and Games | 22 | 2 | 19 / 2 / 1 | Form and sound precede interpretation; allusions follow the history knowledge or receive glosses |
| 6. Klamath recovery | 22 | 2 | 19 / 2 / 1 | Reports precede evaluation and research application; writing precedes findings talks |

No whole unit is demonstrably far over or under its load. Units 5 and 6 also carry substantial reuse of writing, research, discussion and presentation skills, so their two owned rows do not imply two small instructional loads.

All 35 lettered Grade 7 parts have day placements. Apart from finding 1, the named assessment products and short tasks provide a plausible route to full coverage at this planning layer. Units over 25 days have mid-unit assessments on days 15, 43 and 73, followed by distinct response blocks. Final unit response and course-level response address separate evidence.

The checks explicitly protect against content repetition:

| Check | Days | Newly taught skills use |
|---|---|---|
| 1 | 57 to 58 | Earlier river content for Unit 2 informational skills |
| 2 | 109 to 110 | Earlier smallpox content for Unit 4 position analysis |
| 3 | 157 to 158 | Earlier health content for Unit 6 argument evaluation |

## Calendar, Candidate cells and shorter path

Checks occupy target weeks **12, 22 and 32**. The Grade 7 stagger rule is satisfied.

The calendar supports the stated dependencies: Athens overlaps and receives an ELA bridge; myths finish before the late allusion work; ELA research, roots and argument precede their social studies uses. Ecosystems come after early river and soil reading, which therefore supply their own background. Climate instruction overlaps Unit 6, whose day 139 supplies the needed factual account.

Every Candidate cell has a decision and cost:

| Unit | Settled allocation |
|---|---|
| 1 | Text record and discussion look-for, no added days; integrated task, existing day 27 |
| 2 | Question count, no added days; informative model, existing day 46 |
| 3 | Research instruction/application, existing days 70 to 72 and 75 to 81; vocabulary recurrence embedded |
| 4 | Argument guide, existing days 97 to 98; speaking look-for embedded |
| 5 | Text record, no added days; oral-reading look-for, existing day 117 |
| 6 | Cold task, existing days 153 to 154; anchor inventory, no added days |

The ten folds name unassessed days: **8, 10, 14, 34, 41, 65, 80, 103, 117 and 130**. Each has a receiving neighbour and retained work. Assessment and response days survive; implementation minutes remain subject to finding 2.

There is no base text. A base-lesson source map and source-order check are not applicable.

## Lens checklist: scope and sequence

| Lens line | Status |
|---|---|
| Text demand develops across the year, or departures have reasons | Met as a commissioning plan; actual complexity remains unverified |
| Research and full-process writing recur | Met: two research projects and process writing in Units 1, 2 and 4 |
| Formal discussion occurs often | Met: named discussions have no gap exceeding ten school days |
| K to 2 phonics sequence aligns with decodable texts | Not applicable |

## What is right and should remain

- The whole novella finishes before students use its craft in their narratives.
- Original and contemporary anchors prepare students for supported older texts.
- Process products and revision trails supply assessment evidence without requiring another full essay.
- Digital collaboration, multimedia and listening remain explicitly unfinished when their necessary experience is unavailable.
- The river knowledge returns with greater analytical demand in Unit 6.
- Sensitivity notes preserve factual content and avoid forced personal disclosure.

Earlier frame concerns about repeated research and talks, digital collaboration, discussion demands, specialized references and cross-subject bridges have been addressed. They are not reopened here.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Use the existing analytical response and a vocabulary note for L.7.6 | Completes the standard without another composition | Grade 7 `days.csv`, days 73 and 84; scope and sequence |
| Confirm Grade 6 as the last-use grade for all 29 prerequisites | Actual teaching and assessment placements exist | Scope and sequence |
| Retain current retrieval placements and unit lengths | No older prerequisite or unit-level load failure was established | Scope and sequence; `days.csv` |
| Require bounded reading and task budgets before accepting the 40-minute route | Preserves the existing instructional commitments | Scope and sequence |
| Reconcile frame wording with the current assessment arrangement | Prevents superseded instructions returning | Grade 7 frame |

## What I could not judge

Actual text quality, measured complexity, final authorial range, classroom timings, question quality and scoring reliability remain unverified. The draft correctly distinguishes its bundled **58% informational catalogue-row count** from an unfinished count of individual anchors.

The original texts, federal selections, media, rights checks and sensitivity reads remain production conditions. The unresolved paper access to linked Tribal texts also remains visible. These acknowledged conditions should stay explicit.

## Sources

- [Official Grade 7 language standards](https://www.thecorestandards.org/ELA-Literacy/L/7/): vocabulary performance and language parts.
- [Official Grade 7 speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/7/): discussion, presentation and media requirements.
- [Grades 6 to 12 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): selected text, pacing and inventory provisions.
- [WWC secondary writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): explicit modelling, reading-writing connections and feedback.
- [EL Education Grade 7 curriculum map](https://el-education-production.s3.amazonaws.com/media/documents/CurriculumTools_CurriculumMap-Grade7_0220.pdf): comparison of recurring research, writing and topic-based units.
- [Louisiana Grades 6 to 8 overview](https://doe.louisiana.gov/docs/default-source/academic-curriculum/ela-guidebooks-6-8-%282024%29-overview.pdf): comparison of text sets, developmental writing and later application.
- [Publishers’ Criteria, Grades 3 to 12](https://www.thecorestandards.org/wp-content/uploads/Publishers_Criteria_for_Literacy_for_Grades_3-12.pdf): reading range and sustained engagement with texts.

**For the source list:** The older Louisiana Grade 7 unit-overviews address returned 404. Its current Grades 6 to 8 overview was accessible and supplied the comparison.

## For Cory

None.

**Verdict:** Conditionally sound; revise assessment evidence and workload budgets before final acceptance. **Findings:** 4. **Report path:** `docs/reviews/sequence-english-language-arts-grade-7-2026-11-15.md`, delivered here without writing a file.

