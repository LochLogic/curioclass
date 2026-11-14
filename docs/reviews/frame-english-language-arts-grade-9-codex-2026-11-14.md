# Independent frame review: English Language Arts Grade 9

**Date:** 2026-11-14  
**Requested report path:** `docs/reviews/frame-english-language-arts-grade-9-2026-11-14.md`  
**Delivery:** Complete report below. No files changed.

## Verdict

The frame has a coherent course structure, but it needs revision before it can reliably guide the scope and sequence. Its biggest risk is that the proposed text difficulty and several teaching commitments are asserted without the records or unit instructions needed to verify them. Complete the anchor inventory and make the missing teaching and assessment requirements explicit while preserving the eight-unit structure.

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, `docs/FOUNDATION.md`, `docs/GLOSSARY.md`, BASELINE rules 20 to 24, and ROADMAP through its course requirements and gap table.
- `docs/APPROACH.md`, `docs/APPROACH-ELA.md`, and relevant source and evidence notes in `docs/APPROACH-SOURCES.md`.
- The complete Grade 9 frame, its `frames.csv` row, all 24 Grade 9 progression rows, and the full standards for the grades 9 to 10 band, including lettered parts.
- The complete Grade 8 and Grade 10 frames, their receiving and sending relationships, and relevant Grade 10 progression notes.
- Same-year calendars and dependencies in World History I, Biology, and Algebra I.
- The earlier Grade 9 report, adjacent ELA frame reviews, and relevant progression reviews for resolved findings and REPEAT classifications.
- The base-text record and relevant Reading Room catalogue entries. This course has no base text, so a source map is not applicable.
- Outside standards, review criteria, research guidance, two published curriculum comparisons, and selected primary literary texts, linked below.

**Gates:** `plan.py check` stopped with `ModuleNotFoundError: No module named 'markdown'`; `frame.py check english-language-arts-grade-9` passed with zero failures; `stale.py check` checked 56 files with zero failures.

An independent read-only count confirmed that every Grade 9 skill appears exactly once in the Skills column, with no unexpected skill placements. All incoming Grade 8 and outgoing Grade 10 progression links appear in the relevant seam tables.

## Findings, most serious first

### 1. The anchor inventory does not substantiate the claimed difficulty or reading load

**LAYER:** frame  
**REPEAT:** yes, earlier Grade 9 finding 6 and Grade 8 independent finding 1  
**Severity:** substantial  
**Confidence:** firm

**Location:** “Base text,” “Reading level,” and the Units table.

**What is wrong:** The frame says `texts.csv` gives each anchor its measure and qualitative analysis, but the Grade 9 plan directory and that file do not exist. Several selections also remain unspecified: the Maupassant translation, federal pages and reports, recorded talks, original essays, and exact excerpt boundaries. Catalogue entries establish that some older selections have been identified, but they do not establish the course’s complexity or load.

A band-wide target cannot establish that these particular anchors occupy its lower two thirds. Complexity requires quantitative evidence where usable, qualitative analysis, and reader/task considerations. [Common Core Appendix A, printed pages 5 to 6](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf), [review criteria 2b and 2c](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf).

**Why it matters:** Writers cannot reliably choose supports, confirm suitability, or test the days against the actual reading.

**Exact fix:** Establish the anchor inventory with exact edition or translation, source URL or repository location, excerpt boundaries, word count, rights basis, text kind, complexity analysis, placement reason, and matching supports. Mark unwritten originals and unselected media pending. Rewrite the present-tense `texts.csv` claim accordingly.

### 2. Several Grade 9 teaching commitments are narrower than their progression rows

**LAYER:** standard  
**REPEAT:** yes, the incomplete-standard-description kind in earlier ELA frame reviews  
**Severity:** substantial  
**Confidence:** firm

**Location:** Units 1, 2, 4, 6, and 8.

The following requirements need explicit instructions:

| Requirement | Current gap | Exact fix |
|---|---|---|
| L.9-10.1b, unit 2 | Only participial and absolute phrases are named. The progression says Grade 9 builds the phrase and clause types that Grade 10 then uses for style. | Add varied phrase and clause construction through sentence combining, including noun, relative, and adverbial clauses. Retrieve familiar types and teach the new ones through anchor sentences and drafts. |
| W.9-10.7, unit 4 | Research is on “a question” about a life or setting. Student-generated questions, narrowing or broadening, and synthesis are not secured. | Require students to formulate a question, revise its scope when sources warrant, and combine findings across sources. Repeat that cycle in unit 7. |
| W.9-10.9a and 9b | The year-long row starts on stories, but the first nonfiction application is not identified. | Label unit 1’s literary application 9a. Add an explicit 9b application in unit 4 and written argument evaluation in unit 6. |
| L.9-10.5a, unit 8 | Figures are named, but analysis of their role is not explicit. | Require an explanation of what a selected oxymoron or euphemism contributes to the passage’s meaning or characterization. |

These are requirements in the [writing standards](https://www.thecorestandards.org/ELA-Literacy/W/9-10/) and [language standards](https://www.thecorestandards.org/ELA-Literacy/L/9-10/), consistent with the progression’s stated Grade 9 limits.

**Why it matters:** A writer could implement the listed activities faithfully while omitting parts that Grade 10 assumes were introduced.

### 3. The proposed unit 2 assessment text is already assigned reading

**LAYER:** frame  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** firm

**Location:** Unit 2, “Check set adds.”

**What is wrong:** The candidate assessment uses a “cold passage from book 6 or 7,” but the anchor specification assigns books 5 to 12 whole. Those passages cannot be unfamiliar assessment texts.

**Why it matters:** Rereading a taught passage does not provide the transfer evidence required by APPROACH-ELA’s cold-text assessment rule.

**Exact fix:** Replace that candidate with an otherwise unassigned passage from Book 4, selected for a self-contained guest-and-host episode. Record its exact boundaries and reserve it from instruction and practice. The [Butler text](https://www.gutenberg.org/files/1727/1727-h/1727-h.htm) supplies the source; the unit plan must confirm that the selected passage supports the assessed skills.

### 4. Digital presentation and media-comparison requirements lack completion boundaries

**LAYER:** standard  
**REPEAT:** yes, earlier Grade 9 finding 5 and progression review F3  
**Severity:** moderate  
**Confidence:** firm

**Location:** “Devices,” unit 4, and unit 6.

**What is wrong:** The frame correctly distinguishes handwritten publication from W.9-10.6, but does not apply that distinction to SL.9-10.5. Unit 4 promises only “one visual aid,” which could be entirely on paper. The film comparison also lacks a route for a room without playback equipment.

SL.9-10.5 requires strategic digital media use. A printed aid supports presentation but does not demonstrate that component. [Speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/9-10/).

**Why it matters:** Completing the paper alternative could be recorded as completing a digital performance.

**Exact fix:** Add:

> Students create and use a digital element in a research presentation through a school-day shared-device route, without student accounts. Record SL.9-10.5’s digital component separately until demonstrated. Film comparison uses shared playback; a transcript alone does not complete the planned film-versus-print comparison.

For unit 6’s listening task, a teacher-delivered speech can preserve an oral source. It must still support evaluation of the speaker’s point of view, rhetoric, reasoning, and evidence.

### 5. Unit 7’s fourteen days do not account clearly for its second research presentation

**LAYER:** frame  
**REPEAT:** yes, earlier Grade 9 finding 4 and Grade 10 presentation-load finding  
**Severity:** moderate  
**Confidence:** judgment call on overall pacing; firm on the omitted presentation

**Location:** Writing calendar, unit 7, and `e9-sl-presentation`.

**What is wrong:** Fourteen days contain several readings, structural analysis, a three-day research project, the explanatory process piece, and an end-of-unit assessment. The progression also requires a three to five minute talk from **each** short research project, but unit 7 does not name that second talk.

For thirty students, the talks alone require 90 to 150 minutes before transitions or feedback.

**Why it matters:** A writer is likely to drop the talk or compress revision to accommodate an unbudgeted product.

**Exact fix:** State that the second project supplies the research stage of the existing explanatory piece, producing one cited paper and its accompanying talk. Budget three lessons for three-minute presentations with brief transitions and feedback, or specify an equivalent teacher-assessed recording arrangement. Confirm that the remaining reading and writing fit the fourteen-day allocation after finding 1 supplies actual text lengths.

The secondary-writing guide supports protecting modelling, practice, and reflection, rather than treating revision as expendable. [WWC secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22).

### 6. The cross-subject calendar is stale, and the week 26 deadline remains uncoordinated

**LAYER:** process  
**REPEAT:** yes, earlier Grade 9 finding 1 and Grade 8 independent finding 5  
**Severity:** moderate  
**Confidence:** firm

**Location:** Cross-subject introduction and Biology/Algebra I tables.

**What is wrong:** The introduction says Biology and Algebra I frames will be written later. Both exist:

- Algebra I teaches correlation and causation in unit 3, weeks 10 to 12, before ELA unit 6.
- Biology teaches common ancestry in unit 7, weeks 19 to 23, before ELA unit 7.
- Biology’s human-impact unit runs in weeks 25 to 28. Its current frame accepts ELA’s source-based explanation without requiring a topic change.
- Biology asks that its design report avoid an ELA process-piece due week. ELA currently fixes its explanatory piece in week 26.

**Why it matters:** Writers receive obsolete availability information and an unresolved workload collision.

**Exact fix:** Replace “written later” with the actual units and weeks. Mark the first two dependencies taught first, retaining local bridges for alternate calendars. Keep the honeycreeper explanation: the previously reported topic conflict is resolved. Coordinate Biology’s design-report deadline with ELA’s week 26 deadline in the two scope and sequences, recording the agreed due week in both.

### 7. The informational-text discussion omits the published high school comparison

**LAYER:** frame  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** firm

**Location:** Units introduction and “For the lead,” item 4.

**What is wrong:** The published evidence guide explicitly includes a 70 percent informational and 30 percent literary comparison for grades 9 to 12, reported without affecting scoring. It instructs reviewers to examine anchor texts. The frame instead reports informational **unit days**, 60 of 148, or 40.5 percent.

Those are different denominators. The earlier Grade 9 report’s discussion did not identify the guide’s high school figure. [Evidence guide, PDF pages 5 and 8](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf).

**Why it matters:** The frame cannot fairly assess its balance against the chosen review instrument.

**Exact fix:** Retain the day-share calculation, label it explicitly, and separately count literary and informational anchors once the inventory exists. Report the guide’s high school comparison and explain any difference. Preserve the distinction between that review procedure and the standards’ across-subject reading distribution. Do not replace a unit merely to force the day percentage toward the guide’s anchor-text percentage.

### 8. Unit 1’s question assumes advance knowledge that its twist story withholds

**LAYER:** frame  
**REPEAT:** yes, earlier Grade 9 finding 2  
**Severity:** minor  
**Confidence:** firm

**Location:** Unit 1’s compelling question.

**What is wrong:** Asking what the reader knows “before the characters do” does not fit every story. In “The Open Window,” the reader initially receives Vera’s fabricated account along with Framton and learns its nature through the ending. This is withholding and revelation, not a consistent reader advantage. [Primary text](https://www.gutenberg.org/files/269/269-h/269-h.htm).

**Why it matters:** Students may be pushed toward an interpretation the text does not support.

**Exact fix:**

> In each story, what does the writer let the reader know, and when, and what does that do to us?

Keep the four stories and the structural-analysis purpose.

### 9. The earlier Grade 9 review needs a dated status correction

**LAYER:** process  
**REPEAT:** yes, stale review-result notes recur in the independent ELA reviews  
**Severity:** minor  
**Confidence:** firm

**Location:** Existing `docs/reviews/frame-english-language-arts-grade-9-2026-11-14.md`, “What I read,” verdict, and finding 1.

**What is wrong:** The report says no Grade 8 frame exists. It now exists. Its principal Biology objection also describes a restriction that Biology’s current frame has replaced with an explicit reciprocal arrangement.

**Why it matters:** A later fixer could perform unnecessary work or change an already reconciled topic.

**Exact fix:** Preserve the original review as a dated snapshot and append:

> Status update, 2026-11-14: the Grade 8 frame is now available and its Grade 9 handoffs have been checked. Biology’s current frame accepts ELA unit 7’s source-based human-impact explanation. The topic conflict in finding 1 is resolved; the outdated ELA calendar and writing-deadline coordination remain open.

### 10. Two factual wording errors remain in the frame

**LAYER:** process  
**REPEAT:** yes, earlier Grade 9 finding 7  
**Severity:** minor  
**Confidence:** firm

**Location:** Unit 1’s reason and “For the lead,” item 3.

**What is wrong:** Unit 1 attributes the recency restriction to the standard. It comes from the course’s text-selection and rights policy. Item 3 attributes “Choice of style manual: see the lead list” to both research rows, but the current Grade 10 row already applies the style manual and no longer contains that placeholder.

**Why it matters:** These statements misidentify the governing rule and the remaining work.

**Exact fixes:**

- Replace “the most recent first-read texts that the standard allows” with “older texts selected within the course’s rights and recency policy.”
- Rewrite item 3 to identify only `e9-w-short-research` as retaining the unresolved placeholder. Preserve the four-year style-sheet choice.

## Data checks and lens checklist

| Check | Result |
|---|---|
| Owned skills | Met: all 24 placed exactly once; no unexpected skill rows. |
| Other-grade skills | Earlier learning is identified as retrieval or review. Grade 10 extensions remain distinguishable. |
| Standards in full | Grade 10 owns the band codes, but Grade 9 still has explicit annual obligations. Missing Grade 9 commitments are identified above. |
| Grade 9 reading endpoint | Must be made assessable: identify literary and literary-nonfiction checkpoints within the band, with documented support as needed at its high end. Do not treat the `~` ownership notation as deferring this endpoint. [Standards, printed pages 38 and 40](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf). |
| Unit reasons and order | Generally sound: evidence before the epic, rhetoric before argument evaluation, argument before the literary argument. No confirmed model prerequisite inversion. |
| Days | 22 + 28 + 13 + 18 + 11 + 17 + 14 + 25 = 148; 12 course-level days give 160. Each course-level check has respond time. Unit 7 needs the load repair above. |
| Source map | Not applicable: no base text. |
| Seams | Incoming Grade 8 and outgoing Grade 10 links match. |
| Cross-subject | World History I dependencies are addressed; Algebra I and common ancestry arrive first. Biology deadline coordination remains open. |
| Specific topic and texts | Mostly met. Units 1 and 3 emphasize literary craft and cultural interpretation; their knowledge-building connection is less explicit than the other units. |
| Anchors on file with complexity and placement evidence | Missed: finding 1. |
| Range of eras, traditions, and kinds | Met in the proposed selections. Exact availability and suitability remain unverified. |
| Long text read whole | Met in the plan: every scene of *Romeo and Juliet*. The Odyssey is explicitly a substantial partial reading. |
| Other lens layers | Detailed question percentages, scoring guidance, vocabulary lists, and daily supports are not assessable from this frame alone. |
| Stale notes | Marked-note gate passes; unmarked problems are findings 6, 9, and 10. |

## What is right and should be preserved

The progression links are unusually explicit. Retain the readiness task at each skill’s first point of use, the four process pieces, repeated research, daily text-based writing, vocabulary recurrence, and the distinction between supported reading and independent performance.

Preserve the whole-play commitment, broad world-literature selection, separate literary and informational units, and the existing sensitive-content notes. The 160-day allocation leaves room within a conventional school year; the issue is proving individual unit loads, not increasing the annual total.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep the eight units and current skill placements | Placement and handoffs are coherent | Grade 9 frame |
| Broaden unit 1’s question to knowledge and timing | Fits both suspense and revelation | Grade 9 frame, unit 1 |
| Reserve an unassigned Book 4 passage as the assessment candidate | Books 6 and 7 are already taught | Grade 9 frame, unit 2 |
| Integrate unit 7 research with the explanatory piece and retain its talk | Preserves both progression commitments while reducing duplicate work | Grade 9 frame, unit 7 |
| Retain the honeycreeper explanation | Current Biology frame accepts the source-based route | Grade 9 cross-subject section |
| Report anchor balance separately from day balance | Different denominators answer different questions | Grade 9 frame and later scope and sequence |
| Preserve Grade 9’s supported reading endpoint | Band ownership does not erase its explicit annual requirement | Reading-level and assessment descriptions |

## For Cory

- **Scope:** The existing question about a more recent long Grade 9 anchor remains a scope choice. This review does not require replacing the current long texts.
- **People and money:** Assign the Native reader, counselling-qualified reader, qualified ELA reader for original texts, and second rights reader required by the foundation. Any compensation remains Cory’s decision.

## Sources and limits

Sources were opened during this read unless stated otherwise:

- [Common Core ELA standards](https://learning.ccsso.org/wp-content/uploads/2022/11/ELA_Standards1.pdf): annual reading requirements and band expectations.
- [Writing](https://www.thecorestandards.org/ELA-Literacy/W/9-10/), [language](https://www.thecorestandards.org/ELA-Literacy/L/9-10/), and [speaking/listening](https://www.thecorestandards.org/ELA-Literacy/SL/9-10/) standards: component checks.
- [Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): complexity model.
- [ELA review criteria](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf) and [evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): selected text, support, topic-connection, and balance sections.
- [Publishers’ Criteria](https://achievethecore.org/content/upload/Publishers_Criteria_for_Literacy_for_Grades_3-12.pdf): extended reading and writing guidance.
- [WWC secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): protection of modelled writing, practice, and reflection.
- [Published Grade 9 pacing comparison](https://www.fishtanklearning.org/curriculum/ela/9th-grade/pacing-guide/): its longer periods and additional reading assumptions limit direct day-count comparisons.
- [New York Grade 9 curriculum map](https://unbounded-uploads.s3.amazonaws.com/attachments/15605/ela-grade-9-curriculum-map.pdf): comparison of text-based sequencing and integrated standards. Reference only.
- [Saki](https://www.gutenberg.org/files/269/269-h/269-h.htm) and [Butler’s Odyssey](https://www.gutenberg.org/files/1727/1727-h/1727-h.htm): selected primary-text checks.

No substantive finding rests solely on memory. Pacing estimates are expert judgments, not classroom measurements. This read does not certify every text’s rights, actual complexity, media quality, question set, assessment quality, or classroom effectiveness.

**For the source list:** Add the two Grade 9 curriculum comparisons and the CCSSO-hosted standards address above. Following links from the official review-tools page successfully opened the hashed review PDFs after an initial direct-open failure.

**Verdict:** Revise before proceeding to the scope and sequence.  
**Finding count:** 10.  
**Report path:** `docs/reviews/frame-english-language-arts-grade-9-2026-11-14.md`, delivered inline, not written.

