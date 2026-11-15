# Independent read: kindergarten ELA scope and sequence

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/sequence-english-language-arts-kindergarten-2026-11-14.md`  
**Delivery:** Complete report here. No files changed.

## Verdict

The four-unit sequence is coherent, but it needs revision before it becomes the settled reference for unit planning. The largest risk is that replacement texts and anchor complexity records remain unavailable, while assessment instructions do not consistently establish completion for every child. Complete the text evidence and repair the assessment records while preserving the topic order and day allocations.

**Finding count: 4.**

## What I read and checked

- The complete kindergarten scope and sequence, all 160 `days.csv` rows, the frame, and the source map.
- All 29 kindergarten ELA progression rows, the kindergarten standards and lettered parts, `CALENDAR.md`, and the kindergarten rows of `calendar.csv`.
- The kindergarten entries in `ela-texts.csv`.
- `EXPERT.md`, the ELA lens, `RUBRIC-ELA.md`, and relevant foundation, approach, glossary, roadmap, baseline, source-register and sequence-writing provisions.
- Relevant earlier kindergarten frame reviews, their fix record, the ELA progression review, and permitted kindergarten sequence reviews for recurring findings.
- Stored source ZIP inventories and mapped member paths. I did not read every source lesson PDF.

The blind file exclusions were respected.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Kindergarten ELA reported 0 sequence failures; the global run reported an unrelated grade 2 failure, then stopped because `markdown` was unavailable. |
| `python -X utf8 scripts/frame.py calendar` | Passed; kindergarten ELA checks occupy weeks 16 and 32. |
| `python -X utf8 scripts/frame.py check english-language-arts-kindergarten` | 0 failures; 160 days, including 154 unit days. |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures. |

The unavailable global gate does not withhold this verdict.

## Findings, most serious first

### 1. The sequence still lacks the actual texts and records needed to judge its reading demand

**Severity:** High  
**LAYER:** sequence  
**REPEAT:** yes, kindergarten independent frame review, finding 1  
**Confidence:** firm

**Location:** Scope and sequence, “Text placement and remaining text work,” “Shorter path,” and “For the lead,” item 2; kindergarten entries in `data/plans/ela-texts.csv`.

**What is wrong:** The inventory contains 21 text-set rows: eight marked on file, twelve to write and one to choose. None of the eight anchor rows has a completed complexity record. Several rows represent multiple prospective selections. Consequently, the claimed increase in demand, five-day snowstorm reading, passage-specific supports and shorter-period reading budget cannot yet be checked against actual texts.

The earlier fix explicitly assigned replacement text records to the scope-and-sequence stage. This finding concerns that now-due work, not the previously rejected proposal to require the inventory before fixing the frame.

The [K-to-2 review criteria, indicators 2b and 2c](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf#page=11) connect complexity and supports to the actual anchor and its task.

**Why it matters:** A unit writer could follow the day map faithfully and discover that the replacement story lacks the needed event, language, illustration or stated reason. Reading length could also invalidate the shorter-period budget.

**Exact fix:** Complete the replacement manuscripts and select the poems before closing this sequence review. Give each constituent text its own identifier and manuscript location. Complete records covering length, rights, qualitative demands, reader and task, placement reason, and matched supports. Supply quantitative analysis where meaningful, without inventing a kindergarten numerical placement threshold. Then verify the five snowstorm sections and shorter-period passage selections against those manuscripts.

Keep the existing topic order. Word-level verification of the adapted decodables remains necessary before their independent use.

### 2. Ownership and assessment completion give competing instructions

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, ownership-to-assessment mismatch recurs in the earlier kindergarten frame review, finding 1  
**Confidence:** firm

**Location:** Frame, “Where a row sits”; scope and sequence, unit assessment descriptions and “For the lead,” item 1; days 33, 74 to 76, 111, 117 and 156.

**What is wrong:** The frame defines ownership as teaching and checking a row to the kindergarten standard, then places foundations rows where their first element appears. The sequence correctly acknowledges that several owned standards finish later. Those two meanings remain unreconciled.

There are also two specific gaps in the closing assessment record:

| Target | Current evidence | Required repair |
|---|---|---|
| Unit 1 letter names and consonant correspondences | Eight letters taught there; completion observed on day 76 | Distinguish the initial unit record from later completion. |
| Unit 2 W.K.6 | Typing on day 75; second tool kind on day 155 | Record completion on day 156 using both contributions. |
| Unit 3 RF.K.3b and parent RF.K.3 | Short-vowel work there; final vowel associations in unit 4 | Identify day 156 as the completion point. |
| Unit 2 RL.K.3 | Explicitly assessed on day 63, absent from its closing assessment rows | Name the retained day 63 story-elements evidence in the closing record. |
| Parent L.K.2 | Parts assessed across units 2 and 3; parent appears on no assessment row | Add an explicit combined completion record on day 117. |

These distinctions follow the complete requirements in the [kindergarten standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf), especially the alphabet, vowel and conventions provisions.

**Why it matters:** A writer can interpret an owning unit as complete while its record contains only a sample. Conversely, another writer may repeat assessments because the plan never identifies which retained evidence closes the standard.

**Exact fix:** Resolve the frame’s definition through the lead and Cory, since the present brief forbids silently changing ownership. The recommended resolution is to retain the teaching order and record both the initial placement and the completion placement for distributed strands.

Add one explicit completion table to the sequence. On day 75, retain and name day 63’s character, setting and major-event observations for RL.K.3. On day 117, add L.K.2 and name its combined evidence: day 75 capitals and punctuation, day 76 sound-to-letter writing, and day 111 or 117 phonetic spelling. Preserve the existing assessment and response days.

The earlier W.K.1 move is settled and should remain unchanged.

### 3. Course-check roster instructions can give different children different assessment coverage

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, incomplete assessment directions recur in the kindergarten social studies sequence review, finding 1  
**Confidence:** likely

**Location:** `days.csv`, days 77 and 78, and days 158 and 159; scope and sequence, “Course-level checks and the calendar.”

**What is wrong:** Day 77 identifies the “first of two roster halves” and describes letters, sounds, phonology and detail questions. Day 78 identifies the remaining roster but describes additional phoneme operations and retelling. The year-end pair similarly places decoding and spelling with the first half, then informational reading and writing with the remaining roster.

The prose intends every child to receive the complete check. The operational row notes can instead be followed as two different batteries assigned to different halves of the class.

**Why it matters:** Some children could receive no direct reading or spelling check, while others receive no retell or writing check. The resulting response groups and grade 1 handoff would rest on unequal evidence.

**Exact fix:** Keep two roster halves, but state on **both days of each pair** that every child in that half completes the same full battery across both target lists. Give both rows the combined assessed codes, including named retained evidence where appropriate. Distinguish whole-group passage work from individual conferences, and verify the six-minute individual budget with the finished tasks.

Alternatively dividing tasks across days would require every child to participate on both days. Do not retain roster-half language with that arrangement.

### 4. The source map contains a stale day description and an unexplained order change

**Severity:** Minor  
**LAYER:** base text  
**REPEAT:** yes, conflicting planning records recur in the kindergarten social studies sequence review, finding 6  
**Confidence:** firm on the discrepancies; judgment call on the preferred vowel spacing

**Location:** `source-map.csv`, row `topic-d64`, physical line 128; cycle 24 and 25 entries and notes; scope and sequence, “Source decisions.”

**What is wrong:** The added topic block for day 64 says to read the final section and assess story elements. That is now day 63’s work. Day 64 is the response day.

Also, the published foundations sequence introduces spoken long e in cycle 24. This plan postpones it to cycle 25 while stating that base order is kept, without recording the postponement’s reason. See the [base kindergarten sequence, PDF page 2](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_GradeK.pdf#page=2).

**Why it matters:** Someone building from the source map could repeat the story assessment instead of responding to it, or overlook a deliberate phonics adaptation.

**Exact fix:** Replace `topic-d64`’s reason with the actual response: 15 minutes of targeted story-map reteaching and a fresh retell using a familiar short weather story, followed by familiar reading.

Keep long e on day 151 as a deliberate one-cycle postponement to separate its introduction from the new long o/u contrasts. Record that reason in the cycle 24 and 25 source-map entries, and qualify the blanket claim that source order is unchanged. No day or ownership move is needed.

## Order, coverage and days by load

The instructional arcs generally build correctly:

- Unit 1 establishes listening, book handling and topic/detail work before independent contributions to opinions and informative products.
- Unit 2 models story elements and retelling before narrative planning, drafting and revision.
- Unit 3 supplies needs facts and models gathering notes before research writing and the collage.
- Unit 4 makes both stories familiar before literary comparison, and distinguishes author reasons from children’s preferences before the final card.

| Unit | Days | Owned rows | Base topic lessons | Base foundations lessons | Load judgment |
|---|---:|---:|---:|---:|---|
| Toys and play | 34 | 14 | 30 | 25 | Broad launch of routines justifies the allocation. |
| Weather wonders | 42 | 9 | 40 | 35 | Largest new language and narrative load justifies the longest unit. |
| Trees are alive | 39 | 4 | 35 | 35 | Decoding and research require substantial repeated work. |
| Enjoying and appreciating trees | 39 | 2 | 34 | 35 | Continued foundations and process writing explain the days. |

No unit is demonstrably far over or under its load. Assessment-marked rows number 9, 5, 11 and 9 respectively, but these are observation windows alongside continuing instruction, not that many full-day tests.

All owned lettered parts have instructional placements. Explicit assessment directions preserve important distinctions, including all four L.K.5 parts, both kinds of comparison, sentence expansion, recognized and named punctuation, sound changes, and meaningful decodable reading. Finding 2 concerns completion records rather than an instruction to add advanced content.

## Other required checks

| Requirement | Judgment |
|---|---|
| Readiness versus retrieval | Met. All 29 kindergarten `assumes` cells are empty. There are no earlier-grade rows whose last-use grade requires classification. |
| Same-year retrieval | Appropriate on days 35, 80 and 119. These retrieve earlier story details, topic/details, tree needs and opinion work. No misplaced readiness check was found. |
| Mid-unit assessments | Present in all four units, each longer than 25 days. |
| Response counted once | Topic response and foundations response occupy separate named blocks. No duplicate day charge found. |
| Checks avoid immediate repetition | Explicitly met: mid-year tasks use earlier toy content; year-end tasks use earlier skills and a new non-tree informational topic. |
| Calendar | Met. ELA weeks 16 and 32 match the targets. Nearest ELA/math check gaps are six and five school days. |
| Same-year leans | Covered by timed bridges on days 1, 11, 15, 35, 80 and 82 where another subject’s exact skill timing is later or uncertain. |
| Candidate cells | All four kept, with assessment and performance slots inside their unit allocations. |
| Shorter period | A concrete 100-minute route preserves foundations and purposeful reading. Actual text lengths and conference throughput remain unverified. |
| Shorter year | Ten named folds produce 150 meetings. Every folded row has blank `assess`; no assessment is removed. A coordinated shorter grade calendar remains necessary, as the sequence acknowledges. |
| Source-map completeness | All 139 topic lesson identifiers and 130 foundations lesson identifiers accounted for once. Combined source PDFs were expanded correctly. All mapped source paths and ZIP members resolved. |
| Stale notes beyond the gate | Finding 4 identifies a stale source-map description that the passing stale check did not detect. |

The four Candidate dispositions retain the topic assessments and performance tasks in these windows:

| Unit | Reserved topic assessment windows |
|---|---|
| 1 | Day 5; days 17 to 18; days 28 to 33 |
| 2 | Days 46 and 63; days 74 to 76 |
| 3 | Days 86 to 87 and 97 to 99; closing observations across days 107 to 117 |
| 4 | Days 126 to 127, 132 and 138; closing observations across days 142 to 156 |

Foundations cycle checks remain inside their own block.

## ELA lens checklist: scope and sequence

| Checklist line | Status | Evidence |
|---|---|---|
| Text demand climbs, or its order is justified | **Missed as demonstrated evidence** | Increasing task demand is explained, but actual anchors and records are missing. |
| Research and full-process writing recur | **Met at planning level** | Multiple shared inquiries and narrative, informative and opinion process pieces are scheduled. |
| Discussion occurs frequently | **Met** | Daily text talk, modelled routines, interviews, science talks and sharing are explicit. |
| K-to-2 phonics sequence is connected to decodable reading | **Met at planning level** | Cycles, reader placements and taught-pattern boundaries are specified. Actual adapted word eligibility remains unverified. |

Unit-level question counts, finished scoring guidance and day-level execution are not applicable to scoring this layer.

## Settled by the expert

These are item-level recommendations for the caller to apply.

| Choice | Reason | File affected |
|---|---|---|
| Keep four units and their current days | The source structure and unequal instructional loads support them. | Frame and sequence |
| Keep same-year opening retrieval without readiness labels | Kindergarten has no earlier-grade assumed rows. | Sequence and days |
| Preserve the six local bridges | They avoid depending on uncertain cross-subject timing. | Days 1, 11, 15, 35, 80 and 82 |
| Retain day 63 evidence at the unit 2 close | Completes the named story-elements record without another test. | Day 75 |
| Close L.K.2 explicitly from its distributed evidence | All four parts need one identifiable completion record. | Day 117 |
| Give both roster halves the complete course-check battery | Every child needs comparable evidence. | Days 77 to 78 and 158 to 159 |
| Keep long e on day 151, documenting the postponement | Makes the adaptation explicit without moving a unit or adding time. | Source map and source decisions |
| Correct the day 64 source-map description | Preserves the intended response instead of repeating assessment. | Source map |

## What should remain

Preserve rich read-alouds alongside explicit foundations, sound-based word mapping, the prohibition on guessing, daily meaningful decodable reading once introduced, kindergarten writing boundaries, and the two digital tool kinds with individual participation records.

These foundations broadly accord with the [federal foundational-reading guide’s recommendations](https://ies.ed.gov/ncee/wwc/PracticeGuide/21) on sound-letter connections, decoding, word recognition and connected reading. That evidence does not establish one mandatory calendar date for beginning decoding.

## Sources and limits

Outside sources opened during this read:

- [Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): kindergarten requirements and lettered parts.
- [K-to-2 review criteria](https://cdn.edreports.org/reviewtools/ela/2.1/ELA-Grades-K-2-v2.1-Tools_Review-Criteria.pdf): relevant foundations, text, discussion, writing, research and assessment indicators.
- [Base kindergarten foundations sequence](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_GradeK.pdf): cycle order and oral versus printed pattern boundaries.
- [Federal foundational-reading guide](https://ies.ed.gov/ncee/wwc/Docs/PracticeGuide/wwc_foundationalreading_040717.pdf): relevant recommendations, consulted in part.
- [K-to-2 publishers’ criteria](https://achievethecore.org/content/upload/2._Publishers_Criteria_for_Literacy_for_Grades_K-2.pdf): read-aloud access and foundational-reading guidance, consulted in part.
- [Core Knowledge kindergarten skills unit 3](https://www.coreknowledge.org/free-resource/ckla-unit-03-kindergarten-skills/): limited comparison of explicit blending, formation and segmented 60-minute instruction. Its full kindergarten sequence was not reviewed.

I could not judge finished text quality, cultural representation, adapted decodable word inventories, final assessment items, scoring consistency or classroom timing. No substantive finding rests solely on memory. Memory was used only for review-format and scope guidance.

**For the source list:** The current K-to-2 criteria PDF above opened successfully. The Core Knowledge unit page is an additional limited comparison source, not a proposed replacement base.

## For Cory

- Resolve the ownership policy for standards taught and completed across different units, including W.K.6. Preserve the instructional order while the completion convention is settled.
- Decide whether the 150-meeting version is an offered course option. Offering it requires a coordinated kindergarten calendar across all four subjects.

**Verdict: Revise before treating the sequence as settled. Findings: 4. Intended report path: `docs/reviews/sequence-english-language-arts-kindergarten-2026-11-14.md`, delivered here, not written.**

