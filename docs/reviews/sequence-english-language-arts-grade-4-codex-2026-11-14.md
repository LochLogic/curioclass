# Independent scope and sequence review: English Language Arts, Grade 4

**Review date:** 2026-11-15  
**Intended report path:** `docs/reviews/sequence-english-language-arts-grade-4-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files changed. This is the independent first read specified for this run.

## Verdict

Revise before treating this scope and sequence as settled. Its four-unit structure, instructional arcs and day allocations are defensible, but several assessment placements need clearer prior teaching or fuller evidence, and the required text records remain unfinished. Preserve the unit order and calendar while repairing those commitments and updating the prerequisite evidence.

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, the foundation, shared and ELA approaches, relevant source-register notes, glossary, BASELINE rules and roadmap requirements.
- The complete Grade 4 scope and sequence, all 160 rows of `days.csv`, the frame and all 157 source-map rows.
- All Grade 4 progression rows, Grade 3 prerequisite rows and Grade 5 handoffs.
- The Grade 3 ELA day map to verify actual prerequisite placements.
- `docs/courses/CALENDAR.md` and the Grade 4 rows of `data/plans/calendar.csv`.
- Grade 4 entries in `data/plans/ela-texts.csv` and the base-text register.
- The two earlier Grade 4 frame reviews, their disposition report, and permitted ELA progression and sequence reviews for REPEAT classifications.
- Lesson inventories inside the twelve selected Grade 4 base-text archives.
- The linked outside sources listed below.

The blind-rule files were not opened. No curriculum finding rests solely on model memory.

**Gates:** `plan.py check` reported zero Grade 4 sequence failures, then encountered a missing Grade 5 sequence and stopped on missing Python dependency `markdown`; `frame.py calendar` passed, `frame.py check english-language-arts-grade-4` passed with zero failures, and `stale.py check` passed with zero failures.

## Findings, most serious first

### 1. Required text records are deferred beyond their agreed completion point

**Severity:** High  
**LAYER:** sequence  
**REPEAT:** yes, Grade 4 frame review finding 5 and Grade 2 sequence review finding 2  
**Confidence:** firm

**Location:** Scope and sequence, “Text demand and availability” and “For the lead” item 1; frame, “Reading level”; `data/plans/ela-texts.csv`.

**What is wrong:** The frame requires the course’s text records with the scope and sequence, before unit planning. `data/plans/english-language-arts-grade-4/texts.csv` is absent. The shared catalogue supplies useful identifiers and commissioning targets, but the four anchors remain unwritten, individual poems remain unchosen, and several records represent collections rather than inspectable selections.

The sequence instead directs the unit/text stage to supply the records before classroom use. That postpones the dependency beyond the frame’s stated checkpoint.

**Why it matters:** Replacement texts determine whether the planned comparisons, language examples, vocabulary, reading installments and assessments can work. Proposed lengths and complexity targets cannot establish those features. Text-complexity analysis requires the actual text alongside quantitative, qualitative and reader/task considerations. [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf)

**Exact fix:** Keep this sequence explicitly provisional until the text-record owner supplies:

- Identified manuscripts or exact source selections, including individual poems and excerpt boundaries.
- Actual lengths, whole/excerpt status, qualitative demands, reader/task fit and placement reasons.
- Meaningful prose measures where appropriate, matched supports and rights status.
- Confirmation that the texts contain the features and vocabulary their assigned days require.

Complete that checkpoint **before the relevant unit plan**, rather than before classroom use. This does not reopen the earlier rejected demand for finished manuscripts before the frame.

### 2. Some assessments precede an explicit model or sufficient independent practice

**Severity:** High  
**LAYER:** sequence  
**REPEAT:** yes, teaching-onset conflicts in the Grade 4 frame reviews and the Grade 2 sequence’s dictionary finding  
**Confidence:** likely

**Location:** `days.csv`, days 41 to 45, 96 to 104, and 109 to 115.

**What is wrong:** The daily map leaves these teaching steps insufficiently placed:

| Assessment | Missing or late preparation | Exact fix within existing days |
|---|---|---|
| **Day 44: W.4.9b and full RI.4.2** | This is the first W.4.9b-coded task. The explicit main-idea/detail/summary model follows on day 45. Day 41 mentions summarizing, but does not clearly reserve the new source-based writing model and guided handover. | On day 41, model selecting details and writing a short informational summary with an explanation of its evidence. On day 43, include a brief independent application. Keep day 45 as correction and refinement. |
| **Day 99: SL.4.3** | Earlier point/reason/evidence teaching concerns written arguments. The first explicit recorded/read-aloud speaker analysis is day 104, after the listening assessment. | During day 96, model identifying a speaker’s point, reasons and evidence from a short read-aloud excerpt. Add a brief listening application on day 97 before day 99’s assessment. |
| **Day 115: L.4.2c** | The compound-sentence comma is first taught on the same row that collects its end-component evidence. There is no clearly named earlier guided and independent application. | Teach the comma with a sentence model on day 109 and practise it in the student’s draft on day 113. Day 115 then assesses transfer during revision. |

The sequence’s general statement that models precede drafting does not locate these particular models.

**Why it matters:** A writer could build assessments that measure first exposure or supported imitation. Informational evidence writing and identifying a speaker’s support are distinct grade-level performances. [Grade 4 writing standards](https://www.thecorestandards.org/ELA-Literacy/W/4/), [speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/4/)

The recommended repairs follow the elementary writing guide’s emphasis on explicit instruction and a handover through the writing process. [WWC elementary writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17)

### 3. The word-strategy sequence does not explicitly carry every required demand

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete performances under claimed codes recur in the earlier ELA progression and sequence reviews  
**Confidence:** likely

**Location:** `days.csv`, days 43, 44, 54 and 74; progression row `e4-word-strategies`.

**What is wrong:** The plan places context clues, roots and reference use, but never explicitly assigns work distinguishing meanings of a **multiple-meaning word**. It also does not clearly reserve finding **pronunciation and precise meaning** through references before the first L.4.4c assessment on day 44. Pronunciation-reference work is explicitly named much later, in week 28.

Day 74 relies on day 54’s strategy record, whose description names a glossary and word parts without specifying those missing performances. These requirements occur within the standard’s wording, even though they do not each have a separate code. [Grade 4 language standards, L.4.4](https://www.thecorestandards.org/ELA-Literacy/L/4/)

**Why it matters:** Three strategy labels can be present while an important kind of word problem and part of reference use remain untaught or unobserved.

**Exact fix:**

- On day 43, model choosing between two meanings of a word in the animal text and using print/digital references for pronunciation and exact meaning.
- Make day 44 reserve a brief application of both reference purposes.
- Make day 54’s record contain an independent multiple-meaning example and the pronunciation/meaning reference entry.
- Name those entries among the products scored on day 74.

Use words actually present in the selected texts. Add no day or new standard.

### 4. Two later W.4.6 assessment claims exceed their named evidence

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, Grade 4 frame review finding 3 and earlier ELA assessment-evidence findings  
**Confidence:** firm

**Location:** `days.csv`, days 142 and 156.

**What is wrong:** Day 142 lists W.4.6 but names an independent essay written through a school-device route. Day 156 lists the same full code but names revision and publication of the press release. Neither row names evidence for all its digital requirements.

The unit 2 records on days 62 and 75 are much clearer: they explicitly retain exchange, revision, publication and the uninterrupted page-typing sitting. Those records establish a workable model for later completion decisions. [Grade 4 writing standards, W.4.6](https://www.thecorestandards.org/ELA-Literacy/W/4/)

**Why it matters:** A typed essay or published release could be scored as the complete standard without the collaboration and keyboarding evidence.

**Exact fix:** Remove W.4.6 from day 142’s assessment claims while retaining device writing as its delivery route. On day 156, explicitly name the retained digital-process record from days 62/75, together with the current publication, as the evidence used for the full-standard completion decision.

This preserves full coverage without adding another digital assessment.

### 5. The prerequisite evidence note is now stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale prerequisite and placement notes were raised in the earlier Grade 4 frame review  
**Confidence:** firm

**Location:** Scope and sequence, “Earlier-grade assumptions” and “For the lead” item 2.

**What is wrong:** The sequence still treats the Grade 3 ELA day map as absent and marks all 28 direct ELA assumptions “day evidence pending.” That map now exists. Every one of those assumed rows has named assessment placements there.

Examples include `e3-same-author` on days 99/114, `e3-compare-two-texts` on day 131, `e3-short-research` on days 60/75, and `e3-sentences` on day 75.

**Why it matters:** The note sends later writers to resolve an uncertainty that can now be closed, obscuring the remaining uncertainty about Grade 3 mathematics.

**Exact fix:** Replace the blanket ELA caveat with verified Grade 3 day references for all 28 rows. Retain their retrieval treatment. Keep the separate qualification for 3.MD.B.3 because the Grade 3 mathematics day map remains absent.

## Order, assessment coverage and days by load

| Unit | Days | Owned rows | Judgment |
|---|---:|---:|---|
| 1. Poems and becoming a writer | 38 | 16 | The opening reading work, biography essay and poem/presentation process justify the allocation. Prose/drama comparison precedes its assessed use. |
| 2. Animal defenses | 39 | 9 | Initial reading, expert research, informative writing and a developed branching narrative carry substantial load. Repair the early summary/evidence model and word-strategy detail. |
| 3. Erie Canal debate | 39 | 3 | History, research, the play, three traditional tales and the opinion/discussion sequence justify the days despite few newly owned rows. |
| 4. The vote | 37 | 2 | The whole chapter book, continued grammar, account comparison, research and final publications justify the allocation. |
| Course checks and response | 7 | none | Four check days and three respond days are explicit. |
| **Total** | **160** | **30** | No unit is demonstrably far over or under its load. |

The main arcs are coherent. Research precedes the animal narrative, reasons and evidence precede the canal opinion piece, and account comparison precedes its independent assessment.

All four units exceed 25 days and contain mid-unit assessments. Their closing evidence is distributed:

- Unit 1: days 34 to 36 and 38.
- Unit 2: days 74 to 76.
- Unit 3: days 115 to 117 and 119.
- Unit 4: days 151 to 153 and 156.

Portfolio products appropriately stand for extended writing and process evidence. Findings 2 to 4 identify the specific remaining teaching/evidence gaps. The stated response convention counts the main feedback slot once, with later revision and publication applying it.

The grammar continuation is explicit: L.4.1f in unit 1; c/d in unit 2; b/e/g in unit 3; a in unit 4. Narrative parts, informative parts, opinion parts and the later mythological-allusion work have named placements. Generic full-code promises still need the specific repairs above.

## Readiness and retrieval

All 28 direct ELA assumptions have Grade 3 placements, so retrieval is the correct Grade 4 treatment. No unit misclassifies a year-before ELA row as readiness, retrieves an identified older ELA row instead of checking it, or places an older-row readiness check on its hook day.

Earlier Grade 4 learning is retrieved within later lessons. The Grade 3 social studies timeline and claim/evidence assumptions also have day-level evidence. The Grade 3 graph assumption remains provisionally identified, as finding 5 distinguishes.

## Calendar and checks that do not repeat

Both course-level checks meet the target weeks:

| Check | Days | Week | Earlier content used for recently assessed skills |
|---|---|---:|---|
| Check 1 | 78 to 79; response 80 | 16 | Poetry, biography and producing a poet’s collection replace animal-defense content. |
| Check 2 | 157 to 158; response 159 to 160 | 32 | Canal accounts replace vote accounts; the new tale connects to unit 3. |

The scope and sequence explicitly explains both transfers.

The same-year leans are handled correctly against the calendar:

- Science structures/functions arrive on school days 118 to 147, after ELA unit 2. Day 39 supplies the bridge.
- Science hazards arrive on days 97 to 117. Day 43 uses an animal-threat problem/solution text.
- Social studies’ canal unit overlaps ELA on days 80 to 103. Day 81 supplies background without assuming completion.
- Social studies sourcing on days 60 to 79 precedes ELA unit 4.

Grade 4 ELA breaks no course-level-check stagger rule.

## Candidate cells, source map and shorter path

**Candidate cells:** All are settled as kept, with named placements and costs embedded inside the unit allocations. The three tale days are specifically funded by the research merge and two narrative-lesson replacements.

**Source map:** All **153 selected base lessons** appear exactly once as source identifiers, plus four original additions. Archive lesson inventories reveal no omitted or extra selected lesson identifiers. The two cuts, merges and split have reasons; retained lesson order is preserved. The Life Science companion’s exclusion is explained.

This verifies the inventory and disposition, rather than every adapted lesson’s fidelity. Local PDF extraction was unavailable because this Python environment lacks a PDF reader library. The publisher’s old map address returned 404 and its planning page exposed no lesson content, so the overview/lesson discrepancy in module 4 unit 2 remains unconfirmed in this read.

**Shorter path:** The ten named folds yield 150 meetings, preserve assessment days and retain the named reading order. The shorter-period route preserves the 90-minute daily provision through additional in-school time and honestly states the limit of a lone 60-minute allocation. The combined workloads, especially days 100/101 and 131/132, still need timing with the actual texts. The sequence correctly requires a remapped calendar for the shorter year.

## ELA lens checklist: scope and sequence layer

| Checklist line | Result | Evidence |
|---|---|---|
| Text demand climbs, or its order has a stated reason | **Met as a design; actual demand unverified** | The sequence explains the increase in coordinated demands and longer reading. Finding 1 limits confirmation. |
| Research recurs and full-process writing recurs | **Met** | Research in units 2, 3 and 4; model, planning, feedback, revision and publication across units. |
| Formal discussion occurs often | **Met** | Repeated discussions throughout the year, alongside daily partner talk. |
| K to 2 phonics sequence aligns with decodable texts | **Not applicable** | Grade 4 instead supplies a daily multisyllabic-word and spelling sequence. |

The four planned anchors give a two-literary/two-informational balance. Actual quality, complexity and reading volume remain unverified. The writing types recur, but the stated 30/35/35 distribution remains unsubstantiated; daily code counts cannot establish process-writing shares.

## What is right and should be retained

- The four coherent topic sets and their order.
- Explicit daily long-word reading and aligned spelling.
- Fluency focused on understanding, accuracy and expression.
- Whole-book reading completed in class.
- Repeated research, formal discussion and supported writing processes.
- Earlier-topic content in cumulative checks.
- School-day digital evidence and honest recording of unfinished standards.
- Sensitive-history notes, present-day analysis and choice around personal disclosure.

## Settled by the expert

These are item-level dispositions for the eventual fixer. Nothing was edited.

| Choice | Reason | File affected |
|---|---|---|
| Model informational summary/evidence writing on day 41 and apply it on day 43 | Preparation precedes day 44 | `days.csv`; sequence assessment prose |
| Model speaker-support identification on day 96, with practice on day 97 | Preparation precedes day 99 | `days.csv` |
| Teach compound-sentence commas on day 109 and practise on day 113 | Independent transfer precedes day 115 | `days.csv` |
| Specify multiple-meaning and pronunciation/meaning evidence on days 43, 44, 54 and 74 | Completes the word-strategy demands | `days.csv` |
| Remove day 142’s full W.4.6 assessment claim; identify retained evidence on day 156 | Keeps claims proportional to named products | `days.csv` |
| Confirm all 28 ELA prerequisites from the available Grade 3 map | Retrieval is supported | Scope and sequence |
| Retain the four unit allocations and ten named folds, pending timing | Their purposes and reading order are defensible | Scope and sequence |
| Clarify day 116’s “feedback on day 115” wording as applying earlier feedback; completed-essay feedback remains on day 117 | Removes an ambiguous response reference | `days.csv`, day 116 |

## For Cory

None arising from these item-level corrections. Any proposal to change the approved daily time allocation, audience, staffing or device provision remains Cory’s decision.

## Sources and limits

- [Common Core Grade 4 standards: literature](https://www.thecorestandards.org/ELA-Literacy/RL/4/), [information](https://www.thecorestandards.org/ELA-Literacy/RI/4/), [foundations](https://www.thecorestandards.org/ELA-Literacy/RF/4/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/4/), [speaking/listening](https://www.thecorestandards.org/ELA-Literacy/SL/4/) and [language](https://www.thecorestandards.org/ELA-Literacy/L/4/): checked against the local standard text.
- [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): text-complexity framework.
- [Grades 3 to 5 evidence guide](https://cdn.edreports.org/media/2025/07/ELA-3-5-Evidence-Guide_2.1.pdf), indicators 1u, 2f and 2o: fluency assessment, reasonable pacing and writing distribution. Those sections were consulted, not the full guide.
- [WWC elementary writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/17): explicit writing-process instruction and transcription skills.
- [Publisher’s Grade 4 curriculum overview](https://www.eleducation.org/resources/fourth-grade-curriculum-map): base-program structure.
- [Another Grade 4 scope and sequence](https://www.coreknowledge.org/wp-content/uploads/2017/03/G4_CKLA_Detailed_ScopeSequence.pdf): comparison of integrated reading, writing, language and response planning, used as reference only.

This read cannot establish actual text quality, exact reading load, question dependence, scoring quality or classroom timing from unwritten texts and reserved tasks.

**For the source list:** Record the reachable evidence-guide address above and the current publisher overview page; retain the access warning for the old curriculum-map URL.

**Verdict: revise before settling the sequence. Findings: 5. Intended report path: `docs/reviews/sequence-english-language-arts-grade-4-2026-11-14.md`, delivered here without writing a file.**

