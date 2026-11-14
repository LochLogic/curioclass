# Independent frame review: English Language Arts, Grade 4

**Date:** 2026-11-14  
**Report path:** `docs/reviews/frame-english-language-arts-grade-4-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

Revise before using this frame to write the scope and sequence. Its four-unit structure, grade-to-grade handoffs and 160-day total are sound, but the first-teaching placements conflict with the retained base lessons, and the canal replacement map misidentifies the lessons being removed. Correct those two records together so a writer can follow one dependable teaching order.

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, `docs/FOUNDATION.md`, the shared and ELA approach pages, relevant source-list entries, BASELINE rules 20 to 24 and 29, and the frame-writing instructions.
- The complete grade 4 frame and its `frames.csv` row.
- All 30 grade 4 progression rows, with grade 3 and grade 5 ownership and handoff rows beside them.
- The complete grade 3 and grade 5 ELA frames.
- Relevant grade 4 science and social studies units, calendars and local bridges.
- The existing grade 4 frame review, neighboring-grade reviews, and ELA progression stitch and fix reports.
- The 2017 base-text archive’s lesson lists, including combined lesson downloads; relevant unit-overview text and module 3 supporting-material headings.
- The complete grade 4 standards on the [Common Core standards site](https://www.thecorestandards.org/ELA-Literacy/RL/4/), with its separate strand pages linked below.
- Relevant portions of the [grades 3 to 5 evidence guide](https://cdn.edreports.org/media/2025/07/ELA-3-5-Evidence-Guide_2.1.pdf), the [elementary writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17), and a second curriculum’s [grade 4 scope and sequence](https://www.coreknowledge.org/wp-content/uploads/2017/03/G4_CKLA_Detailed_ScopeSequence.pdf), used for comparison only.

`source-map.csv` does not exist. The frame-writing instructions explicitly defer that file to the scope and sequence, so I checked the frame’s lesson-range map instead.

**Gates:** `plan.py check` could not complete because Python lacks `markdown`; `frame.py check english-language-arts-grade-4` passed with zero failures; `stale.py check` passed with zero failures.

No curriculum finding below rests solely on model memory. Earlier reviewers’ source claims were treated as claims to check, not independent evidence.

## Findings, most serious first

### 1. Unit 1 teaches and assesses skills placed later

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 4 review, finding 2  
**Confidence:** firm

**Location:** Frame lines 122, 125 and 133 to 136; base M1U2 overview, printed pages 180 to 186.

**Problem and evidence:** Unit 1 retains the four-paragraph informative essay, but `e4-informative` and `e4-writing-process` belong to unit 2, essay structure is introduced there, and `e4-grammar` belongs to unit 4. The archived M1U2 overview explicitly teaches informative writing and revision, complete sentences, fragments/run-ons, and quotation punctuation. Its assessment checks those features.

Calling the essay’s process “grade 3 form” does not resolve the conflict with the retained grade 4 instruction and assessment. Direct instruction in the writing process is also supported by the [elementary writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17).

**Why it matters:** A writer must either teach these skills before their assigned unit or remove instruction the frame says it keeps.

**Exact fix:** Propose placing `e4-informative`, `e4-writing-process` and `e4-grammar` in unit 1, with a part-by-part continuation showing which grammar features arrive later. Move the essay-structure introduction to unit 1 and teach quotation punctuation there. Preserve later work as development and review. These standard moves require Cory’s decision.

### 2. The canal replacement cuts the wrong source lessons

**Severity:** Major  
**LAYER:** base text  
**REPEAT:** yes, earlier grade 4 review, finding 1  
**Confidence:** firm

**Location:** Frame lines 204 to 212.

**Problem and evidence:** M3U1 lessons 1 to 3 are labelled Declaration of Independence lessons. They actually launch the topic, read a Revolution overview for gist, and reread it closely. Declaration materials occur in M3U2 lessons 5, 8 and 13, whose supporting files identify Parts I, II and III.

The replacement therefore removes the launch and background-reading sequence while leaving the actual Declaration adaptations unspecified.

**Why it matters:** The canal unit could open without the background its play and debate require, while retained close-reading lessons lack assigned replacement passages.

**Exact fix:** Keep M3U1 lessons 1 to 3 as the canal launch, overview and close read. Map M3U2 lessons 5, 8 and 13 explicitly to selected canal memorial or opposition passages. Retain 39 days by replacing M3U2 lessons 11 and 12 with two myth days and combining M3U1 lessons 4 and 5 into one supporters/opponents research day to release the third. Name the remaining first-person narrative work in the map and identify its assessment changes explicitly.

### 3. W.4.6 is only partly specified in the frame

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, digital-standard completeness was raised in the ELA progression review  
**Confidence:** firm

**Location:** Frame lines 43 to 46 and unit 2.

**Problem:** The frame specifies typing and publishing, but does not identify an internet-supported interaction or collaboration task. Those elements appear in the progression row and in [W.4.6](https://www.thecorestandards.org/ELA-Literacy/W/4/); typing an individual essay alone does not establish them.

**Why it matters:** A writer following only the frame could deliver the typed page and still omit part of the standard.

**Exact fix:** Add to unit 2: “Using a teacher-managed internet route without student accounts, partners exchange a draft or comments, revise from the response, and publish the finished writing. Each student also types at least one page in one sitting.” Keep the existing unfinished-standard rule when the device route cannot be provided.

### 4. RL.4.7 begins with the wrong text form

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, earlier grade 4 review, finding 3  
**Confidence:** firm

**Location:** Unit 1 and the proposed `e4-poetry-drama` note change.

**Problem:** The named first teaching compares a poem with its recording. [RL.4.7](https://www.thecorestandards.org/ELA-Literacy/RL/4/) specifies a story or drama and connections to its presentation. Unit 3 supplies a suitable play comparison, but calls it review.

**Why it matters:** The first teaching and ownership claim do not match the standard’s specified text.

**Exact fix:** Use unit 1’s already planned prose story against a recorded reading or short performance. Ask students to identify presentation choices that reflect particular descriptions or directions. Keep the poem recording as additional work and unit 3’s play as review. The earlier review’s proposed “unit 2 drama scene” is not present in this frame.

### 5. Anchor descriptions cannot yet support the text-complexity claims

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, missing anchors and text records were raised in the earlier ELA scope-and-sequence review  
**Confidence:** firm on the missing evidence

**Location:** Frame lines 31 to 36 and all four anchor descriptions.

**Problem:** The original books are specifications rather than identified manuscripts. The frame promises future text records, gives estimated measures, and does not name the individual poems or federal selections. The lens’s requirement for anchors on file with defensible placement is therefore missed.

The [evidence guide’s text-complexity indicator](https://cdn.edreports.org/media/2025/07/ELA-3-5-Evidence-Guide_2.1.pdf) calls for analysis of the actual anchor texts. A projected word count and measure cannot establish their quality or difficulty.

**Why it matters:** Lesson adaptation, reading load and scaffolding could be built around text features that the eventual manuscripts do not contain.

**Exact fix:** Label the current figures as design targets. Give every anchor a stable identifier, select the individual short texts, and establish a manuscript-and-record checkpoint before its sections are planned. For poetry and drama, use qualitative and reader/task analysis rather than asserting a reliable numerical placement below the band.

### 6. The compressed skills block has no workable allocation

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 4 review, finding 6  
**Confidence:** likely

**Location:** Frame lines 9 to 16 and 212 to 214; `e4-reading-range`.

**Problem:** Thirty minutes must carry daily word reading and spelling, plus alternating fluency and independent-reading conferences. The progression promises daily independent reading, but the frame does not reserve it daily. The omitted components of the base’s second block are described only as “its other two parts.”

**Why it matters:** Teachers cannot tell what receives protected time or which source practices have been deliberately removed.

**Exact fix:** Give an explicit provisional allocation within the existing 90 minutes: 10 minutes for word reading and spelling, 10 for guided oral rereading, and 10 for independent reading, with conferences during that reading. Name the omitted additional complex-text and writing practice. State that grammar teaching remains inside the mapped module lessons. This allocation is an expert planning choice, not a research-established minimum; timing must test it.

### 7. Two cross-subject prerequisites are unavailable when requested

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier grade 4 review, finding 7, and earlier cross-subject reviews  
**Confidence:** firm

**Location:** Frame lines 155 to 159.

**Problem:** Science teaches structures/functions in unit 6, late in the year, after ELA unit 2. Social studies teaches `ss4-regional-cultures` in unit 7, after ELA’s myth set. Moreover, that social studies row concerns North American regions, not the Greek, Akan and Japanese traditions selected here.

**Why it matters:** The availability table suggests preparation that the other courses cannot supply. The existing “if later” provisions need to become the planned route.

**Exact fix:** Rewrite the science line: “ELA unit 2 introduces the animal structures and defense relationships through its texts; science unit 6 later investigates and models them.” Remove `ss4-regional-cultures` as the myth set’s prerequisite in both frame and progression. Require ELA to provide each tale’s geographic and cultural context itself.

The earlier-grade graph and timeline dependencies are appropriate. Social studies already supplies local bridges for research and account comparison before ELA teaches them.

### 8. The alternative base module is neither mapped nor excluded

**Severity:** Minor  
**LAYER:** base text  
**REPEAT:** yes, earlier grade 4 review, finding 5  
**Confidence:** firm

**Location:** Source map, lines 190 to 214.

**Problem:** The source store includes grade 4’s alternative Life Science module 2. The map does not acknowledge it.

**Why it matters:** “Every base lesson placed or excluded” remains incomplete even though the chosen four-module sequence is identifiable.

**Exact fix:** Add: “Alternative module 2, Life Science: not selected. The animal-defenses module supplies the year’s research, informative writing and branching narrative sequence; the alternative would duplicate that slot.” Identify the alternative package in the later source-map data.

### 9. A placement note still presents a settled choice as open

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale placement and row/frame wording were raised in earlier reviews  
**Confidence:** firm

**Location:** `data/progressions/ela.csv`, `e4-traditional-tales.notes`, line 126; frame lines 181 to 182.

**Problem:** The progression still offers “unit 1 or unit 3” and directs the reader elsewhere for placement. The stitch and current frame have already selected unit 3 beside the play.

**Why it matters:** A later writer could reopen the choice or create a different placement while believing the record is undecided.

**Exact fix:** Replace that clause with: “Read in unit 3 beside the canal play, with the narrative arc used to line up events.” Apply the frame’s already listed row-text corrections in the same reconciliation pass. No placement decision is needed.

## Coverage, days and seams

| Unit | Days | Owned skills | Judgment |
|---|---:|---:|---|
| 1 | 38 | 13 | Sound opening routines; first-teaching record needs correction |
| 2 | 39 | 11 | Research plus two substantial writing products justify the allocation |
| 3 | 39 | 3 | Replacement map needs repair; reading, debate and review justify substantial time |
| 4 | 37 | 3 | Long book, research, language teaching and final products justify the allocation |
| Course checks/respond days | 7 | — | Four assessment days and three respond days are explicit |
| **Total** | **160** | **30** | Leaves 20 days within a 180-day year |

Every grade 4 skill appears exactly once in the ownership cells. No unit ownership cell imports another grade’s skill. Grade 3 preparation is generally identified as prior learning or review.

All grade 4 parent standards have a named placement. Full teaching remains qualified by findings 1, 3 and 4 and by the absence of actual texts and lessons.

Grade 3’s outgoing skills match grade 4’s assumptions. Grade 5 picks up the stated grade 4 outcomes, including the increase from referring to evidence to quoting accurately and from one account pair to multiple accounts.

I disagree with the earlier review’s claim that W.4.9b has no home: unit 2’s animal research and source-based informative writing provide one. Explicitly label that work W.4.9b during reconciliation.

## ELA lens checklist: course frame layer

| Checklist line | Result | Evidence |
|---|---|---|
| Units use specific topics and texts rather than isolated skills or vague themes | **Met, with qualification** | Four substantive sets; the myths need an explicit connecting rationale within unit 3 |
| Anchors are on file with appropriate complexity analysis and placement reasons | **Missed** | Finding 5 |
| The year avoids dependence on one era, tradition or text kind | **Met at design level** | Contemporary originals, historical accounts, poetry and three cultural traditions; actual balance remains unverified |
| At least one long text is read whole | **Met as a commitment** | Two whole books are specified; manuscripts remain pending |

No course-frame checklist line is not applicable. Question counts, scaffold quality, writing models and assessment scoring require the later materials.

## What is right and should be retained

- Four coherent units and an explicit 160-day budget.
- Daily word-reading instruction, spelling linked to it, and fluency focused on meaning and expression.
- Recurring research, writing through the process, and frequent text-based discussion.
- Two whole long texts.
- School-day device access and honest recording of unfinished digital standards.
- Sensitivity notes, student choice around personal disclosure, and qualified-reader requirements.

## Settled by the expert

| Choice | Reason | File touched by the eventual fix |
|---|---|---|
| Use the existing unit 1 prose story and its presentation for RL.4.7 | Matches the standard without moving ownership | Grade 4 frame; `e4-poetry-drama` |
| Preserve unit 3’s launch and explicitly replace all three Declaration passages | Repairs the source adaptation | Grade 4 frame, Source map |
| Retain 39 unit 3 days using the swaps in finding 2 | Changes days within the unit | Grade 4 frame, Source map |
| Use the provisional 10/10/10 skills allocation for timing | Makes the 30-minute promise testable | Grade 4 frame, Days |
| Make ELA’s science background the planned route | Science arrives later | Grade 4 frame, Cross-subject |
| Remove North American regional cultures as a prerequisite for the world-tale set | Content and calendar do not match | Grade 4 frame; ELA progression |
| Retain units 3 and 4’s day counts | New-skill counts alone do not measure reading and product load | Grade 4 frame |
| Close the myth-placement note | Unit 3 is already selected | ELA progression |

## For Cory

- Decide the proposed moves of informative writing, writing process and initial grammar teaching into unit 1.
- Confirm the assumed 90-minute literacy block, already reserved as an audience/time decision.
- Identify qualified readers for the original texts and sensitive history, including a Haudenosaunee community reader, and decide any payment.

## Limits and source follow-up

This read cannot establish manuscript quality, actual text balance, full lesson-level coverage or classroom timing. The archive checks used text extraction and supporting-material headings, not a visual review of every source page. No finding relies on the earlier review’s memory-based legal claim about land transactions.

Additional live sources used:

- [Grade 4 informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/4/), [foundational reading](https://www.thecorestandards.org/ELA-Literacy/RF/4/), [speaking/listening](https://www.thecorestandards.org/ELA-Literacy/SL/4/) and [language](https://www.thecorestandards.org/ELA-Literacy/L/4/): checked the frame against the full standard wording.
- [2017 base curriculum planning page](https://www.eleducation.org/curriculum/language-arts/planning/grade-4-2017-ed/): old unit URLs redirected here, but the fetched page did not expose their content. Local archives supplied the relevant evidence.

**For the source list:** Record the working `www.thecorestandards.org` strand pages and the reachable evidence-guide CDN address above. Record that the former base-curriculum unit URLs now redirect to the planning page.

**Verdict: revise before scope and sequence. Findings: 9. Report path: `docs/reviews/frame-english-language-arts-grade-4-2026-11-14.md`, delivered here without writing a file.**

