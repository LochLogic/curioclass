# Independent expert read: kindergarten ELA course frame

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/frame-english-language-arts-kindergarten-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files written or changed.

## Verdict

The four-unit structure, foundational sequence, day allocations and kindergarten-to-grade-1 handoffs are broadly sound, but the frame needs revision before it becomes the reference for further planning. The largest risk is that its replacement anchor texts and complexity records are promises rather than inspectable materials, so the proposed reading year cannot yet be judged. Establish that text inventory first, then correct the digital-writing requirement, retell assessment and shortened-path guidance below.

## What I read and checked

I read the kindergarten frame, its `frames.csv` row, all 29 kindergarten progression rows, the receiving grade 1 rows and frame, and the kindergarten mathematics, science and social studies frames for availability comparisons. Kindergarten has no preceding ELA course.

Supporting reading included EXPERT.md, the ELA lens and rubric, FOUNDATION, relevant ROADMAP and BASELINE provisions, APPROACH and APPROACH-ELA, the source register, glossary, frame-writing brief, base-text record, and earlier ELA progression reviews, reconciliation and fix reports. Earlier ELA and course-frame reports informed the REPEAT tags.

Outside reading covered the official ELA standards, kindergarten foundational sequence, K-to-2 review criteria, publishers’ criteria and federal foundational-reading recommendations. The stored 2017 source inventory and ZIP member names were checked without extraction to disk. The Resource Manual’s printed licence page and module 4 foundations overview were read directly.

| Check | Result |
|---|---|
| Requested repository-wide `plan.py check` | Initially stopped because Python lacks `markdown` |
| Repository-wide checks with an in-memory renderer placeholder | Exit 0, no failures; rendering was configured to raise if called and was never called |
| `frame.py check english-language-arts-kindergarten` | 0 failures |
| `progression.py check ela` | 374 rows, 0 failures |
| Course-specific `plan.py check` | 0 failures; 0 assessment items checked |
| Latest `stale.py check` | 56 files, 0 failures |
| Kindergarten ownership and outgoing links | 29 skills placed once; all 38 outgoing links reciprocated |

The ordinary global command still needs its dependency environment repaired. The workaround changed no checking function, installed nothing and wrote nothing.

The absent `data/plans/english-language-arts-kindergarten/source-map.csv` is **not a finding**. The frame-writing brief explicitly assigns that day-level file to the scope-and-sequence stage; this layer requires the inline lesson-range map.

## Findings, most serious first

### 1. The replacement anchor texts and their records are not available for inspection

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, missing anchor sets and complexity evidence recur in `ela-6-spine-2026-11-11.md`, findings 1 and 6  
**Confidence:** firm on the missing evidence

**Location:** “Texts and the reading level,” all four unit descriptions, and “For the lead,” item 4.

**What is wrong:** The frame supplies story premises, informational-text descriptions and future commitments to text records. It does not identify inspectable replacement manuscripts and records in the course directory or course plan data. The longer weather story likewise has no manuscript, length or complexity analysis establishing the promised whole-text experience.

The base texts’ measures cannot establish the difficulty of replacement texts. The [K-to-2 review criteria, indicator 2b](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_20_K_2_20_Review_20_Criteria_2_1_44660ca52d.pdf) require analysis of the actual anchors.

**Why it matters:** A writer cannot reliably adapt questions, vocabulary, supports or writing tasks before knowing what the replacement text actually says. Genre balance, cultural range and the year’s sustained reading also remain unverified.

**Exact fix:** Before treating the text plan as settled, attach an anchor inventory for all four units. Give every anchor a stable identifier and manuscript path, genre, original/adapted status, rights record, length, quantitative analysis or reason it is unsuitable, qualitative analysis, associated task and placement reason. Include the complete longer weather story and count the actual literary/informational and whole/excerpt balance. Preserve the four topics while this evidence is assembled.

### 2. W.K.6 is narrowed to making a class digital product

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete digital-standard completion claims recur in `progression-ela-codex-2026-11-13.md`, finding 3  
**Confidence:** firm on the requirement; likely on the instructional omission

**Location:** “Paper path and devices,” units 2 and 4, and progression row `ek-revise-publish`.

**What is wrong:** The frame declares W.K.6 met when the class makes a digital piece on a shared device. Neither the frame nor the progression note explicitly preserves exploration of a **variety** of digital tools. Two products made through the same unspecified workflow do not establish that breadth. The [official standard, printed page 19](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf#page=19) includes both exploration and variety.

**Why it matters:** A teacher could operate one tool while children supply content, then record the whole standard complete.

**Exact fix:** Retain the shared-device route and existing unit ownership. Require children, with adult guidance, to explore at least two distinct digital functions used to produce and publish writing, such as composing text and adding a digital drawing or recorded narration. State what each child or small group chooses, tries and contributes, and what the teacher records. Carry this wording into `ek-revise-publish`. Additional student accounts or individual devices are unnecessary.

### 3. The mid-year retell check uses an unfamiliar story

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, assessment-to-target mismatches recur in `frame-social-studies-kindergarten-codex-2026-11-13.md`, finding 3  
**Confidence:** firm on the wording mismatch

**Location:** Course-level check after unit 2.

**What is wrong:** The check combines key-detail questions and retelling on a read-aloud “not heard before.” RL.K.2 concerns familiar stories, and `ek-retell` explicitly describes stories heard several times. See the [official standard, printed page 11](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf#page=11).

**Why it matters:** The result can confound immediate listening memory with the familiar-story retelling taught during the course.

**Exact fix:** Keep the unfamiliar read-aloud for key-detail questions. Assess retelling separately using a familiar unit 2 story, with the permitted prompting and story-map cards. Record inclusion of key details. Keep the existing two assessment days and following respond day.

### 4. The shortened path removes purposeful rereading

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, preserving text access and instructional support is an earlier ELA finding type, including `ela-6-spine-2026-11-11.md`, finding 6  
**Confidence:** firm on the internal conflict; likely on the learning cost

**Location:** “For the lead,” item 1.

**What is wrong:** The proposed half-day path saves time by dropping the second reading of every read-aloud. APPROACH-ELA instead requires returning to an anchor for a named purpose. The cut removes a central instructional opportunity rather than identifying which activities can be shortened.

**Why it matters:** Children would lose planned opportunities to revisit difficult language, verify answers and consolidate knowledge. Those opportunities are especially useful while independent decoding is developing.

**Exact fix:** Replace the blanket deletion with:

> The shorter topic block retains a complete initial reading and a purposeful return to selected passages, with questions and vocabulary work. The scope and sequence identifies the passages and activities shortened and demonstrates coverage within the available minutes before this path is offered.

Keep the foundations block intact. Whether the course serves half-day kindergarten remains an audience and scope decision for Cory.

### 5. The grade 1 frame undercounts the models inherited from kindergarten

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, inconsistent model descriptions recur in `progression-ela-codex-2026-11-13.md`, finding 8  
**Confidence:** firm

**Location:** Grade 1 frame, sentence following “Models carried.”

**What is wrong:** The sentence says eight models come from kindergarten. Its own table carries eleven, matching the kindergarten frame. Grade 1 then adds four.

**Why it matters:** The tables preserve the handoff, but the summary gives the next writer an incorrect inventory.

**Exact fix:** Replace the sentence with:

> Eleven models come from kindergarten; grade 1 adds syllable-types, figurative-language, context-clues and paragraph-frame. All go on to grade 2.

Change no model column or progression link.

### 6. The earlier materials report still leaves the 2017 foundations licence unresolved

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, unclosed source-scouting decisions recur in `frame-social-studies-grade-1-codex-2026-11-13.md`, finding 14  
**Confidence:** firm

**Location:** `docs/reviews/ela-open-material-2026-11-12.md`, summary, 2017 Skills Block licence row, planning recommendation and open items 1 to 2.

**What is wrong:** These passages still describe the 2017 foundations licence as unverified and condition the phonics base on opening a file. The source store now documents that work. The stored First Edition Resource Manual’s copyright page prints CC BY 4.0, with third-party exclusions.

**Why it matters:** A later reader could reopen the base-text choice or unnecessarily commission a replacement sequence.

**Exact fix:** Preserve the original dated observations and add a prominent closure annotation:

> Closed 2026-11-13 for the 2017 Reading Foundations Skills Block: the stored licence evidence and printed file notices establish CC BY 4.0, subject to item-level third-party exclusions. The 2024 edition remains excluded. The conditional need to replace the foundations base no longer applies.

Update the recommendation and relevant open-item status to point to that annotation. Keep any distinct, unfinished image or Additional Language and Literacy Block check separately identified.

### 7. The kindergarten mathematics frame still describes existing neighboring frames as future work

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same availability-note defect appears in `frame-science-grade-1-codex-2026-11-14.md`, stale-note findings  
**Confidence:** firm

**Location:** Kindergarten mathematics frame, Cross-subject introduction.

**What is wrong:** It says the other subjects’ frames “are written later.” The kindergarten ELA, science and social studies frames now exist.

**Why it matters:** This presents a timing comparison that can be performed now as an outstanding dependency.

**Exact fix:** Replace the introduction with:

> All leans are to kindergarten in the same year. The ELA, science and social studies frames are available for the timing comparison. The tables record mathematics’ first needs and the bridges used when another subject teaches a skill later.

### 8. The ELA lens still says the K-to-2 criteria have not been read

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, completed work presented as pending is an established progression and frame-review finding type  
**Confidence:** firm

**Location:** `docs/agents/lenses/ela.md`, “What this lens does not cover.”

**What is wrong:** Its blanket “not yet read” statement is overtaken by the ELA progression review, which records reading the K-to-2 criteria. The kindergarten frame already cites that read.

**Why it matters:** A reviewer cannot tell whether the source is unread, partly read or simply absent from the grades-3-to-12 rubric summary.

**Exact fix:** Replace the parenthesis with:

> RUBRIC-ELA.md summarizes grades 3 to 12. Separate K-to-2 criteria were consulted in the ELA progression read, including phonemic awareness, phonics order and aligned decodables; see progression-ela-codex-2026-11-13.md for its reading limits.

Do not imply that the complete evidence guide was read.

## Ownership, standards, order and days

All 29 kindergarten skills appear in exactly one owning unit. The frame represents all 41 kindergarten parent standards; lettered requirements were checked alongside the progression notes. Finding 2 identifies a substantive narrowing that code coverage does not catch.

The later completion of letter knowledge and phonics is explicitly marked “continued,” so placing their owning rows in unit 1 does not silently require mastery of all letters there. I found no unjustified transfer of grade 1 phonics into kindergarten.

| Unit | Days | Owned skills | Base topic lessons | Base foundations lessons | Judgment |
|---|---:|---:|---:|---:|---|
| Toys and play | 34 | 13 | 30 | 25 | Appropriate launch of routines and letter work |
| Weather wonders | 42 | 9 | 40 | 35 | Heaviest topic allocation is justified |
| Trees are alive | 39 | 4 | 35 | 35 | Decoding and research make four rows substantial |
| Enjoying and appreciating trees | 39 | 3 | 34 | 35 | Continued foundations and culminating writing justify the time |
| **Total** | **154** | **29** | **139** | **130** | No unit demonstrably far over or under its share |

The blocks run alongside each other, so their lesson counts should not be added into separate days. Four course assessment days and two respond days bring the total to 160, leaving 20 days within a 180-day year.

The inline source map covers the topic lesson ranges and foundations lessons 1 to 130 in order. Labs are explicitly omitted with a time rationale. No excluded edition or reference-only source is mapped as an instructional base.

## Seams and cross-subject availability

The 29 kindergarten rows’ 38 outgoing links are reciprocated in grade 1. The receiving frame retains review before new short-vowel, cluster, fluency and writing demands. Finding 5 concerns its summary count, not a missing handoff.

| Lean | Timing judgment |
|---|---|
| Weather knowledge | Science begins weather before ELA unit 2; ELA also supplies the facts its texts require |
| Living things’ needs | Instruction occurs near ELA unit 3; retain ELA’s explicit supplied-text bridge |
| Discussion rules | Both subjects teach them at the outset; ELA models its own routine |
| Spoken opinion | Social studies supplies it before ELA unit 4 |
| Sequencing language | Social studies can follow ELA’s first use; retain ELA’s own sequencing instruction |
| Sorting toys | Mathematics’ full sorting-and-counting work comes later; ELA’s direct, non-counting sort is an adequate bridge |

No additional prerequisite-order finding is warranted.

## Lens checklist: course-frame layer

| Checklist line | Status | Evidence |
|---|---|---|
| Units use specific topics and texts rather than isolated skills or broad themes | **Met at topic level** | Toys, weather and the two connected tree units have coherent purposes |
| Anchors are on file with complexity and placement reasons | **Missed** | Finding 1 |
| The year avoids an unjustified concentration in one era, tradition or text kind | **Missed as demonstrated evidence** | Mixed genres and Kenyan content are planned, but actual anchors and a counted inventory are absent |
| A longer text is read whole | **Missed as demonstrated evidence** | The weather story is proposed but unavailable; finding 1 |

The lens’s progression, scope-and-sequence, unit and day checklists are **not applicable to scoring this frame**. Actual decodable alignment, question counts and lesson-level supports require the later materials.

## Settled by the expert

These choices require no movement of standards between units.

| Choice | Reason | File affected |
|---|---|---|
| Keep the four units and existing day allocations | Source order and instructional load support them | Kindergarten frame |
| Use a familiar story for the RL.K.2 check | Matches the target and taught routine | Kindergarten frame |
| Specify two distinct digital functions with child participation | Restores W.K.6 breadth using the existing shared-device route | Kindergarten frame; `ela.csv` |
| Retain purposeful passage revisits in the shorter path | Preserves the stated reading approach | Kindergarten frame |
| Correct eight inherited models to eleven | Both frames’ tables establish the inventory | Grade 1 frame |
| Accept the inline source map at this layer | The CSV is explicitly due with the scope and sequence | Review disposition |
| Preserve the repaired kindergarten phonics boundaries | The earlier fix report and source sequence agree | No change |

## What is right and should remain

- Rich read-alouds alongside systematic foundational instruction.
- Decodables constrained by taught correspondences and high-frequency words.
- Explicit rejection of picture-based word guessing.
- Oral long-vowel work distinguished from grade 1 spelling-pattern decoding.
- Three writing types, repeated revision, research and frequent text discussion.
- A respond day after each course check.
- Classroom-toy examples, privacy protections and specific sensitivity notes.
- The honest statement that paper alone does not complete digital writing.

The foundational design is consistent with the [federal practice guide’s recommendations](https://ies.ed.gov/ncee/wwc/PracticeGuide/21) on sound-to-letter connections, decoding and connected-text practice.

## Sources and limits

| Source | Used for |
|---|---|
| [Official Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf) | Kindergarten requirements and grade 1 growth |
| [Kindergarten foundations year-at-a-glance](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_GradeK.pdf) | Cycle order and oral versus printed patterns |
| [K-to-2 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_20_K_2_20_Review_20_Criteria_2_1_44660ca52d.pdf) | Text records, intentional phonics sequence and aligned decodables |
| [K-to-2 publishers’ criteria](https://achievethecore.org/content/upload/2._Publishers_Criteria_for_Literacy_for_Grades_K-2.pdf) | Rich read-alouds and coherent knowledge building |
| [Federal foundational-reading guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21) | Research recommendations and their evidence levels |
| [Core Knowledge language-arts overview](https://www.coreknowledge.org/language-arts/) | Limited comparison of knowledge and skills strands; reference only |

The live 2017 planning and terms pages returned navigation without substantive text. Edition, inventory and licence judgments therefore use the current local source records and printed materials, not those empty responses.

Actual text quality, cultural range, decodable-word eligibility, assessment scoring and classroom timing remain unjudged. Pacing and shortened-path recommendations are professional judgments. No substantive finding rests solely on memory; prior memory was used only for review-format guidance.

**For the source list:** Record that the K-to-2 criteria opened successfully through the review-tools index after the direct request failed. Preserve the working kindergarten foundations sequence address.

## For Cory

- Confirm the full-day, 120-minute audience assumption and whether a half-day offering belongs in scope.
- Assign the qualified ELA teacher and the qualified reader for the Kenyan account, including any pay.
- Resolve the frame’s existing proposal to move W.K.1 ownership from unit 4 to unit 1. Until then, retain current ownership and distinguish early supported previews from summative assessment.

**Verdict:** Revise before fixing the frame. **Finding count:** 8. **Report path:** `docs/reviews/frame-english-language-arts-kindergarten-2026-11-14.md`, delivered here only.

