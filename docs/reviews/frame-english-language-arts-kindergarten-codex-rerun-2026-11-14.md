# Independent expert read: kindergarten ELA course frame

**Date:** 2026-11-14  
**Requested report path:** `docs/reviews/frame-english-language-arts-kindergarten-2026-11-14.md`  
**Delivery:** Complete report below. No files changed.

## Verdict

The four-unit structure, foundational sequence, day allocations and kindergarten-to-grade-1 handoffs are broadly sound, but the frame needs revision before further planning treats it as settled. Its largest weakness is that replacement anchor texts and their complexity records remain promises, leaving the actual reading year unreviewable. Establish that text inventory, then correct the digital-writing requirement, assessment mismatches and shortened-path guidance.

**Finding count: 9.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `RUBRIC-ELA.md`, FOUNDATION, APPROACH, APPROACH-ELA, relevant ROADMAP and BASELINE provisions, source-access notes and the base-text register.
- The complete kindergarten frame, its `frames.csv` row, all 29 kindergarten progression rows, and the receiving grade 1 links and frame. Kindergarten has no preceding ELA course.
- Kindergarten science, social studies and mathematics frames for prerequisite timing.
- Earlier kindergarten and grade 1 ELA frame reports, ELA progression reports, reconciliation, stitch and fix records, and the earlier open-materials report.
- The stored 2017 source inventory, topic-lesson ZIP member lists, foundations lesson lists, module 4 foundations overview, Resource Manual copyright page, NOTES and stored terms excerpt.
- Outside sources linked below, including the official standards, kindergarten foundations sequence, K-to-2 review criteria, publishers’ criteria and federal foundational-reading recommendations.

The day-level `source-map.csv` does not exist. This is **not a finding**: the frame-writing brief assigns that CSV to the scope-and-sequence stage and requires the inline lesson-range map here.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not finish: missing Python dependency `markdown` |
| `python -X utf8 scripts/frame.py check english-language-arts-kindergarten` | 0 failures |
| Initial `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |
| Final stale check | One unrelated failure: grade 7 ELA frame, line 32, unmarked work-status wording |
| Independent ownership and seam check | 29 skills placed once; all 38 outgoing links reciprocated |

The unrelated stale failure and unavailable global gate do not withhold this verdict.

## Findings, most serious first

### 1. Replacement anchors and their complexity records are unavailable

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, earlier kindergarten independent report, finding 1  
**Confidence:** firm

**Location:** “Texts and the reading level,” all four unit descriptions, and “For the lead,” item 4.

**Problem and consequence:** The frame describes prospective stories and informational texts, then defers their records to unit planning. No inspectable replacement manuscripts or text records accompany it. The base books’ measures cannot establish the replacements’ complexity, and the proposed longer weather story cannot yet demonstrate sustained whole-text reading. The lens requires anchors on file; the [K-to-2 criteria, indicator 2b](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_20_K_2_20_Review_20_Criteria_2_1_44660ca52d.pdf) require analysis of the actual texts.

**Exact fix:** Establish an anchor inventory before treating the text plan as settled. For every anchor, provide its identifier, manuscript path, genre, rights status, length, quantitative analysis or explanation of its limitations, qualitative analysis, associated task and placement reason. Include the complete longer weather story and count the actual literary/informational, whole/excerpt and cultural range. Preserve the four topics.

### 2. W.K.6 loses the requirement to explore a variety of digital tools

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, earlier kindergarten independent report, finding 2  
**Confidence:** firm

**Location:** “Paper path and devices,” units 2 and 4, and progression row `ek-revise-publish`.

**Problem and consequence:** Making a class digital product does not establish exploration of varied tools. The progression describes children’s contributions, which is useful, but neither document specifies the required variety. A teacher could repeat one workflow and record completion. See [W.K.6, printed page 19](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf#page=19).

**Exact fix:** Retain shared devices. Specify guided exploration of at least two digital tools, such as a text composer and drawing tool, with peer collaboration and a record of each child’s contribution. Two is an operational choice, not a numeric quota stated by the standard. Update both documents without moving ownership.

### 3. Unit 1’s candidate assessment conflicts with its ownership of writing

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier kindergarten expert report, finding 1  
**Confidence:** firm

**Location:** Unit 1, “Check set adds”; “Where a row sits”; “For the lead,” item 3.

**Problem and consequence:** Unit 1 names “toy preference writing” as an assessment candidate, while W.K.1 belongs to unit 4 and early opinion work is explicitly informal preview. The frame acknowledges the conflict but leaves competing instructions in place. A unit writer could assess completion before the owning unit or silently move the standard.

**Exact fix:** Until Cory decides the proposed ownership move, replace the candidate with:

> An informative drawing and dictated or written statement about a classmate’s classroom toy, assessed for W.K.2. Toy-preference talk and drawing remain supported previews of W.K.1, assessed for completion in unit 4.

Keep the proposed ownership change under “For Cory.” Do not require a written reason for kindergarten opinion completion.

### 4. The mid-year retell check uses an unfamiliar story

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier kindergarten independent report, finding 3  
**Confidence:** firm

**Location:** Course-level check after unit 2.

**Problem and consequence:** The check combines detail questions and retelling on a previously unheard read-aloud. RL.K.2 specifies familiar stories, and `ek-retell` describes repeated hearings. The check therefore adds an immediate listening-memory demand. See [RL.K.2, printed page 11](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf#page=11).

**Exact fix:** Keep the unfamiliar text for detail questions. Assess retelling separately on a familiar unit 2 story, allowing prompting and story-map cards, and record inclusion of key details. Retain the existing assessment and respond days.

### 5. The shortened path removes every second reading

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier kindergarten independent report, finding 4  
**Confidence:** firm on the conflict; likely on the instructional cost

**Location:** “For the lead,” item 1.

**Problem and consequence:** The half-day proposal shortens the topic block by dropping the second read of every read-aloud. APPROACH-ELA instead requires purposeful returns to anchors. The blanket cut removes opportunities to revisit difficult language and check interpretations. The [K-to-2 publishers’ criteria, PDF page 6](https://achievethecore.org/content/upload/2._Publishers_Criteria_for_Literacy_for_Grades_K-2.pdf#page=6) also emphasize texts worth rereading.

**Exact fix:** Replace the blanket deletion with:

> The shorter topic block retains the complete initial reading and purposeful returns to selected passages. The scope and sequence names the passages, vocabulary and questions retained, identifies activities shortened, and demonstrates coverage within the available minutes before this route is offered.

Keep the foundations block intact.

### 6. Grade 1 undercounts the models inherited from kindergarten

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier kindergarten independent report, finding 5; grade 1 independent report, finding 6  
**Confidence:** firm

**Location:** Grade 1 frame, sentence after “Models carried.”

**Problem and consequence:** The summary says eight models come from kindergarten. Its table carries eleven, agreeing with the kindergarten frame. The handoff itself exists, but the summary gives the receiving writer an incorrect inventory.

**Exact fix:** Replace the sentence with:

> Eleven models come from kindergarten; grade 1 adds syllable-types, figurative-language, context-clues and paragraph-frame. All go on to grade 2.

Change no progression link or model column.

### 7. The frame presents established edition evidence as an unresolved licence question

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier kindergarten expert report, finding 3  
**Confidence:** firm

**Location:** Kindergarten frame, “For the lead,” item 2.

**Problem and consequence:** The item still proposes replacing the foundations base if the lead rejects its licence. The current base-text register, stored terms excerpt and printed first-edition Resource Manual already document CC BY 4.0 with third-party exclusions. The note invites unnecessary rebuilding.

**Exact fix:** Move this settled statement into “Base text”:

> The held 2017 Reading Foundations Skills Block is documented as CC BY 4.0 by the stored terms excerpt and printed first-edition notices. The 2024 edition is excluded. Third-party material remains subject to item-level replacement or clearance.

Delete the conditional branch about rebuilding the foundations base because its edition licence is unresolved.

### 8. The earlier materials report leaves that completed investigation open

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier kindergarten independent report, finding 6  
**Confidence:** firm

**Location:** `docs/reviews/ela-open-material-2026-11-12.md`: summary, 2017 Skills Block licence row, planning recommendation and open items 1 to 2.

**Problem and consequence:** These passages still describe opening a 2017 file and establishing its licence as unfinished. The source store now contains the investigation and printed evidence. A later reader could mistake historical uncertainty for a current dependency.

**Exact fix:** Preserve the dated observations and add this prominent closure annotation:

> Closed 2026-11-13: the stored 2017 Skills Block evidence and printed first-edition notices establish CC BY 4.0, subject to third-party exclusions. The conditional need to replace the foundations base no longer applies. The 2024 edition remains excluded.

Point the affected recommendation and open items to that annotation. Keep unfinished image checks distinct.

### 9. The ELA lens still says the K-to-2 criteria have not been read

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier kindergarten independent report, finding 8  
**Confidence:** firm

**Location:** `docs/agents/lenses/ela.md`, “What this lens does not cover.”

**Problem and consequence:** Its unqualified “not yet read” statement conflicts with the progression report’s recorded consultation of those criteria. The kindergarten frame already relies on that consultation. Readers cannot distinguish an unread source from a source absent from the grades-3-to-12 rubric summary.

**Exact fix:** Replace the parenthesis with:

> RUBRIC-ELA.md summarizes grades 3 to 12. Separate K-to-2 criteria were consulted in progression-ela-codex-2026-11-13.md, including phonemic awareness, phonics order and aligned decodables. That report states the reading limits.

Do not imply that the complete evidence guide was read.

## Ownership, standards, order and days

All 29 owned skills appear exactly once. All 41 kindergarten parent standards are represented; their lettered requirements were checked beside the progression notes. Finding 2 identifies a substantive narrowing that code coverage cannot detect.

Continued foundations teaching is explicitly named after its owning unit. Kindergarten’s oral long-vowel and `-ank`/`-ink` work remains distinguished from grade 1 decoding patterns. That boundary agrees with the [publisher’s kindergarten sequence](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_GradeK.pdf).

| Unit | Days | Owned skills | Base topic lessons | Base foundations lessons | Judgment |
|---|---:|---:|---:|---:|---|
| Toys and play | 34 | 13 | 30 | 25 | Appropriate launch of routines and letters |
| Weather wonders | 42 | 9 | 40 | 35 | Largest topic allocation is justified |
| Trees are alive | 39 | 4 | 35 | 35 | Decoding and research make these rows substantial |
| Enjoying and appreciating trees | 39 | 3 | 34 | 35 | Continued foundations and culminating writing justify the allocation |
| **Total** | **154** | **29** | **139** | **130** | No demonstrably disproportionate unit |

The two blocks run alongside each other. Four assessment days and two respond days bring the course to 160, leaving 20 days within a 180-day school year. Classroom timing remains untested.

The inline source map places every topic lesson and foundations lesson in order. ZIP member ranges confirm the counts, including combined topic-lesson files. Labs are explicitly omitted with a time rationale; no excluded edition or reference-only curriculum is mapped as the base.

I do not adopt the earlier report’s demand to map every overview or reference document as a separate lesson. The present requirement concerns base lessons. Decodable adaptation decisions should nevertheless be recorded explicitly when the day-level map is built.

## Seams and cross-subject timing

The kindergarten starting assumptions require no reading or letter knowledge. All 38 outgoing progression links are reciprocated, and grade 1 opens with a readiness check and review.

| Dependency | Current disposition |
|---|---|
| Weather knowledge | Science’s chart begins in week 1; its weather unit overlaps ELA unit 2. ELA supplies the facts needed immediately |
| Living things’ needs | Science and ELA introduce this near week 16; ELA’s supplied-text bridge covers later science teaching |
| Discussion rules | Both courses teach them at the outset |
| Spoken opinion | Social studies teaches its spoken routine before ELA unit 4 |
| Sequencing | Social studies can follow ELA’s first use; ELA teaches its own sequencing language |
| Sorting toys | Mathematics’ sorting-and-counting work comes later; ELA directly teaches its non-counting sort |

These are workable bridges, rather than evidence that every other course finishes the prerequisite first. Science’s week-20 opinion use also precedes ELA unit 4, but science explicitly supplies a spoken, teacher-scribed bridge.

The earlier mathematics stale-note finding is closed: its current introduction acknowledges that neighboring frames exist.

## Lens checklist: course-frame layer

| Checklist line | Status | Evidence |
|---|---|---|
| Units have specific topics and text sets | **Met at topic level** | Toys, weather and connected tree topics have coherent purposes |
| Anchors are on file with complexity and placement reasons | **Missed** | Finding 1 |
| Texts avoid unjustified concentration in one era, tradition or kind | **Missed as demonstrated evidence** | Mixed genres and Kenyan content are planned; actual texts and counts are absent |
| A longer text is read whole | **Missed as demonstrated evidence** | The weather story is proposed but unavailable |

The lens’s progression, scope-and-sequence, unit and day checklists are not scored as frame requirements. Actual decodable alignment, question dependence and lesson supports require the later materials.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep four units and existing allocations | Source order and instructional load support them | Kindergarten frame |
| Require two digital tools with guided child participation | Makes W.K.6 breadth explicit within shared-device access | Kindergarten frame; `ela.csv` |
| Keep unit 1 opinion work formative pending the ownership decision | Resolves the assessment contradiction without moving a standard | Kindergarten frame |
| Use a familiar story for the retell check | Matches the taught target | Kindergarten frame |
| Preserve purposeful passage revisits in a shorter route | Retains the stated reading approach | Kindergarten frame |
| Correct eight inherited models to eleven | Both frames’ tables establish the count | Grade 1 frame |
| Close the edition investigation in both outstanding notes | Current local evidence resolves the historical uncertainty | Kindergarten frame; materials report |
| Accept the inline source map at this layer | The day-level CSV belongs to the next stage | Review disposition |

## What should remain

Preserve rich read-alouds alongside systematic foundations, decodables restricted to taught patterns, rejection of picture-based guessing, all three writing types, repeated research and discussion, respond days, and the specific privacy and sensitivity provisions. The foundational design is consistent with the [federal guide’s recommendations](https://ies.ed.gov/ncee/wwc/PracticeGuide/21) on sound-to-letter connections, decoding and connected-text practice.

## Sources and limits

| Source | Use in this read |
|---|---|
| [Official Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf) | Kindergarten requirements and grade 1 growth |
| [K-to-2 review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_20_K_2_20_Review_20_Criteria_2_1_44660ca52d.pdf) | Foundations sequence, aligned decodables and actual-anchor analysis |
| [Kindergarten foundations sequence](https://files.eleducation.org/web/resources/Section-5_CurriculumTools_SkillsBlock-Year-at-a-Glance_GradeK.pdf) | Cycle order and oral versus printed patterns |
| [K-to-2 publishers’ criteria](https://achievethecore.org/content/upload/2._Publishers_Criteria_for_Literacy_for_Grades_K-2.pdf) | Rich texts, rereading and text balance |
| [Common Core Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf) | Text-complexity framework |
| [Federal foundational-reading guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/21) | Recommendations and evidence ratings |
| [Core Knowledge language-arts overview](https://www.coreknowledge.org/language-arts/) | Limited comparison of knowledge and skills strands; reference only |

The live publisher terms page exposed navigation without substantive terms. Edition findings therefore rely on the current local register, stored dated excerpt and printed Resource Manual notice.

Actual anchor quality, cultural range, decodable eligibility, scoring guidance and classroom timing remain unjudged. No substantive finding rests solely on memory. Saved memory supplied review-format guidance only.

**For the source list:** The K-to-2 criteria opened through the review-tools index after the direct request failed.

## For Cory

- Confirm the full-day, 120-minute audience assumption and whether half-day provision belongs in scope.
- Decide the existing proposal to move W.K.1 ownership from unit 4 to unit 1.
- Assign the qualified ELA teacher and qualified reader for the Kenyan account, including any pay.

**Verdict:** Revise before treating the frame as settled. **Findings:** 9. **Report path:** `docs/reviews/frame-english-language-arts-kindergarten-2026-11-14.md`, delivered here only; existing files unchanged.

