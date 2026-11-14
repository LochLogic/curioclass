# Expert cold read: English Language Arts Grade 7

The frame has a coherent six-unit structure, complete skill placement and a workable annual day budget, but it needs revision before its coverage claims are accepted. The largest risk is treating proposed texts and shortened standards descriptions as evidence that the planned instruction is complete. Preserve the unit structure while restoring the missing performances, reconciling the knowledge thread and documenting the actual anchors.

**Finding count:** 10.  
**Intended report path:** `docs/reviews/frame-english-language-arts-grade-7-2026-11-14.md`  
**Delivery:** Complete report here. No file was written or edited.

## What I read and checked

I read the Grade 7 frame, its `frames.csv` row, all 28 Grade 7 ELA progression rows, the relevant Grade 6 and Grade 8 progression rows, and both neighboring ELA frames. I compared these with the full Grade 7 standards, the Grade 7 science frame and the relevant units and availability calendar of the Grade 7 social studies frame.

I also consulted:

- `docs/agents/EXPERT.md`, the ELA lens, `RUBRIC-ELA.md`, `FOUNDATION.md`, the glossary and relevant baseline rules.
- The roadmap planning requirements, shared and ELA approaches, source-access notes and `BASE-TEXTS.md`.
- The earlier ELA progression reads, stitch, reconcile and fix reports.
- Relevant earlier ELA scope and sequence, rubric and rights findings, plus the Grade 6 to 8 frame fix report.
- Outside standards, review criteria, research guidance and two published curriculum designs, linked below.

No substantive curriculum finding rests on memory. Saved memory was used only for report-format preferences.

### Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Crashed before completing: `ModuleNotFoundError: No module named 'markdown'` |
| `python -B -X utf8 scripts/plan.py check ela-k12` | 0 failures, but checked 0 items; not evidence of frame coverage |
| `python -B -X utf8 scripts/frame.py check english-language-arts-grade-7` | 0 failures |
| `python -B -X utf8 scripts/progression.py check ela` | 374 rows, 0 failures |
| `python -B -X utf8 scripts/stale.py check` | 56 files, 0 failures |

The full gate remains **unverified**, rather than failed on curriculum content. The passing constituent checks support this review but do not replace a completed global run. No dependencies were installed and no defect-ledger entries were written.

## Coverage, units and days

All **28 owned skills appear exactly once** in the Skills column. No foreign-grade skill ID is assigned as an owner. The rows cover **41 applicable parent standards**; `L.7.5b` is separately assigned within the split ownership of `L.7.5`. Code coverage is complete, but the performances in findings 2, 4 and 5 are incomplete.

| Unit | Days | Owned skill rows | Load judgment |
|---|---:|---:|---|
| 1. Drought year | 30 | 10 | Reasonable for the whole novella, narrative process piece and recurring routines |
| 2. Dust Bowl | 26 | 5 | Reasonable for fiction against history, film, informative writing and sentence work |
| 3. Smallpox | 26 | 6 | Substantial load: research, publication, presentation, author comparison and vocabulary |
| 4. Athens | 22 | 3 | Reasonable for the process argument and two text/audio comparisons |
| 5. Marathon and Games | 22 | 2 | Not demonstrably excessive: poetry, form, allusions, staging and narrative reuse require time |
| 6. Elwha River | 22 | 2 | Reasonable; can accommodate the missing research and presentation reuse |
| Course checks and responses | 12 | — | Three two-day checks, each followed by two respond days |
| **Total** | **160** | **28** | **148 unit days plus 12 course-level days** |

At 50 minutes daily, this provides about **133 hours in class**, with 20 days remaining against the rubric’s approximate 180-day school-year yardstick. No unit is clearly far over or under its share on the available evidence. Actual reading and writing minutes remain untestable without the texts and lesson schedule.

There is **no base text** for this course. The absence of a source map is correct, and base-lesson placement, omissions and source-order checks are not applicable.

## Findings, most serious first

### 1. The text staircase is proposed, not documented

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, the missing-text and complexity-record problems recur from `ela-6-spine-2026-11-11.md`, findings 1 and 6  
**Confidence:** firm on the missing evidence

**Location:** Reading level; Units, text column; For the lead 4.

The Grade 7 course folder contains only `frame.md`, and there is no Grade 7 plan-data folder. The novella, features, poems, play and recordings are descriptions of future works. Federal sources are generally named by agency and topic rather than by exact page or report. No anchor has an accessible text record showing its measure, qualitative demand, reader/task considerations and placement reason.

The [text-complexity model](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf) requires those dimensions together. The [review criteria, indicators 2b and 2c](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Review_Criteria_2_0_a3fc2b49ab.pdf) also connect documented complexity with matched supports.

**Why it matters:** A writer cannot establish that the chosen texts carry the intended analysis, fit the grade or justify their position merely from their proposed plots and lengths.

**Exact fix:** Identify every anchor by stable text ID and local path or exact source URL. Supply its text record, rights record and matched supports before section writing. Until that evidence exists, label the selections and complexity placements explicitly as proposed, rather than settled.

### 2. W.7.6 stops at publication and links

**Severity:** High  
**LAYER:** standard  
**REPEAT:** yes, digital-performance gaps recur from the earlier ELA progression read, finding 3  
**Confidence:** firm

**Location:** Paper path and no accounts; Unit 3; `e7-produce-publish`.

Unit 3 specifies publishing an article with live links, but does not place technology-supported interaction and collaboration. The paper alternative acknowledges the missing links but omits the progression’s school-day device route or explicit unfinished-status rule.

[W.7.6](https://www.thecorestandards.org/ELA-Literacy/W/7/) includes interaction and collaboration as well as production, publication and source links.

**Why it matters:** A student could complete the entire stated task without demonstrating the collaborative part of the claimed standard.

**Exact fix:** Add to Unit 3:

> Students use a shared document or local digital exchange to comment on a partner’s draft, respond to feedback and revise. The final article includes working source links. A shared classroom device or school-day lab session provides access; if unavailable, record W.7.6 as unfinished. The handwritten route supports the other writing goals.

This requires no Curio Class account or hosting.

### 3. The frame does not deliver its research and talk counts

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, insufficient repeated opportunities are the same kind of problem identified in earlier ELA rubric and progression reads  
**Confidence:** firm

**Location:** Days; Writing calendar; Units 3 and 6; `e7-research-questions` and `e7-present-salient`.

The progression requires **two or three research projects** and **two or three talks**. The frame explicitly offers one research project and one prepared findings talk, both in Unit 3, despite promising “two rounds of talks” in the brief. Unit 6’s supplied-source writing does not explicitly require another research cycle.

[Evidence-guide indicator 2t](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf), PDF page 81, asks for repeated research application. The [published Grade 7 curriculum map](https://el-education-production.s3.amazonaws.com/media/documents/CurriculumTools_CurriculumMap-Grade7_0220.pdf) provides a useful comparison: research returns on different topics across the year.

**Why it matters:** Students get one supported attempt and no clearly planned later transfer.

**Exact fix:** Keep Unit 3 as the teaching home. In Unit 6, make the existing explanation a second short research product: answer a focused question, search within the fenced set, assess several sources, cite them and generate a further question. Add a brief findings talk using that product. Mark both skills as **used again**, keeping their owners in Unit 3 and retaining the eight-piece writing calendar.

### 4. The speaking and listening plan drops required performances

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, partial-standard descriptions recur in the Grade 6 to 8 frame reads and fixes  
**Confidence:** firm

**Location:** Unit 1 discussion description; Unit 3 presentation description.

Unit 1 names rules and roles but omits tracking progress toward goals and deadlines. Its questions return discussion to the topic but do not explicitly elicit elaboration and responses to peers. Unit 3 specifies a clarifying display but leaves multimedia and adaptation across contexts unspecified.

These are explicit elements of [SL.7.1b, SL.7.1c, SL.7.5 and SL.7.6](https://www.thecorestandards.org/ELA-Literacy/SL/7/).

**Why it matters:** The planned routines can look complete while omitting the distinctive Grade 7 demands.

**Exact fix:** Add a discussion goal, deadline and progress check; require students to ask for elaboration and respond to a peer’s contribution. For the findings presentation, specify a purposeful multimedia component and visual display. Include a rehearsal explanation to a partner and a formal presentation, with students adapting language and delivery between them.

### 5. L.7.4c is reduced to using a dictionary

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, narrowing a standard to its headline recurs in the earlier frame reads  
**Confidence:** firm

**Location:** Unit 3, “a dictionary (c)”; `e7-word-strategies`.

The progression specifies general and specialized references. The frame reduces this to a dictionary and does not name the pronunciation, precise-meaning or part-of-speech purposes of reference use.

[L.7.4c](https://www.thecorestandards.org/ELA-Literacy/L/7/) specifies general and specialized materials, in print and digital forms.

**Why it matters:** Students can complete the stated word work without learning the reference choices this grade requires.

**Exact fix:** Replace “a dictionary (c)” with:

> General and specialized references, in print and digital forms, used to check pronunciation, precise meaning or part of speech. Compare a general dictionary with a medical glossary on words from the unit.

Retain context, roots and verification as the other strategies.

### 6. The citizenship thread is not reconciled with the progression

**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** yes, this reopens the knowledge-thread seam addressed in the progression read, finding 5, and its fix report  
**Confidence:** firm on the mismatch; judgment call on the scope choice

**Location:** Knowledge threads; For the lead 3; `e7-reading-range`; neighboring reading-range notes; social studies cross-subject calendar.

The progression commits Grade 7 to democracy, the republic and citizenship in Greece and Rome. The frame deliberately supplies Athens only. It correctly flags the proposed deletion, but that proposal has not changed the contract. Grade 8’s progression still says it inherits Greece and Rome, and the social studies frame still expects Grade 7 ELA Rome texts.

**Why it matters:** Different writers receive different instructions about what Grade 8 may assume.

**Exact fix:** Obtain Cory’s scope decision. If Athens-only is accepted, revise the Grade 7 note, the Grade 6 outgoing description, the Grade 8 inherited-knowledge description and the social studies reference to ELA Rome texts together. State where Grade 8 obtains the republic concept. Otherwise, retain the existing thread and place its Roman reading explicitly. Do not mark the seam reconciled while the proposal remains pending.

### 7. The drought-map rights line is inaccurate

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, source-specific rights attribution recurs from the earlier ELA rights read  
**Confidence:** firm

**Location:** Unit 1, text and rights column; Unit 2’s repeated drought-map source.

The frame groups U.S. Drought Monitor maps with federal works under a public-domain label. The map is jointly produced with a university center. Its [permission page](https://droughtmonitor.unl.edu/About/Permission.aspx) authorizes commercial and noncommercial reuse with specified attribution.

**Why it matters:** A broad federal-work label can cause the required credit to disappear when the map is reproduced.

**Exact fix:** Separate the map’s rights entry from the agriculture pages. Record the selected map’s date and URL, cite the permission page, and reproduce the attribution it specifies. Keep the federal-work description only for verified federal-authored material.

### 8. Athens is described as following a unit that is still running

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, inaccurate within-year availability claims recur in earlier cross-subject reads  
**Confidence:** firm

**Location:** Unit 4, Why this unit, here; Cross-subject table.

ELA Unit 4 runs on days **91 to 112**. Social studies’ Athens unit runs about days **87 to 101**. The statement “After social studies grade 7’s Athens unit” is therefore incorrect for ELA’s first eleven days.

The existing local-background bridge is useful and prevents this from being an unaddressed prerequisite failure.

**Why it matters:** A unit writer following the reason column could omit background that the cross-subject table says ELA must supply.

**Exact fix:** Replace the opening reason with:

> Begins alongside social studies’ Athens unit and continues after it. ELA’s opening feature teaches the assembly and citizenship background before either the story or primary excerpts require it.

Keep the current unit days.

### 9. The first progression review still says the mathematics progression is absent

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale status notes recur in earlier frame reads  
**Confidence:** firm

**Location:** `docs/reviews/progression-ela-2026-11-13.md`, What I could not judge, line 214.

The note defers mathematics leans “until data/progressions/math.csv exists.” That file exists, and `progression-ela-fixes-2026-11-13.md` records the resulting ownership checks.

**Why it matters:** A later reader may repeat completed work or treat a resolved dependency as open.

**Exact fix:** Replace that note with:

> Unverified at the original read. Subsequently checked against data/progressions/math.csv; the resulting changes are recorded in progression-ela-fixes-2026-11-13.md. Within-year availability remains a course-frame check.

### 10. The independent progression review also retains the resolved ownership hold

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same stale-status type as finding 9  
**Confidence:** firm

**Location:** `docs/reviews/progression-ela-codex-2026-11-13.md`, F7 and What I could not judge.

F7 still instructs a future writer to wait for mathematics ownership. Its limits section repeats that hold. Current mathematics rows assign the relevant owners, and the ELA fix report records the completed reconciliation.

**Why it matters:** Its proposed pending-status text would now reintroduce obsolete guidance into corrected rows.

**Exact fix:** Preserve the original finding as history, but add:

> Resolved after this read by progression-ela-fixes-2026-11-13.md. S-ID.C.9 and S-ID.B.5 have Grade 9 owners; S-IC.B.6 has a Grade 11 owner. The Grade 10 ELA lean was replaced with Grade 8 scatter-plot work. Annual ownership is settled; same-year timing still requires the course frames.

Replace the corresponding limits bullet with a link to this resolution.

## Seams and cross-subject availability

The principal skill seams are sound: several pieces of evidence develop toward strongest evidence; contrasting narrators prepares for dramatic irony; informative writing, sentence work and fiction against history have identified receiving units.

| Dependency | Judgment |
|---|---|
| Athens knowledge | Overlaps rather than precedes ELA; retain the local bridge and correct the reason, finding 8 |
| Greek myths before allusions | Timing works: the last-week allusion work follows social studies’ myth unit |
| ELA research before Greek research | Timing works: Unit 3 ends before social studies begins its Greek research |
| ELA roots before Latin legacy | Timing works |
| ELA argument before social studies’ final argument | Timing works |
| Ecosystems before early drought/soil reading | Science comes later; ELA explicitly supplies its own background |
| Ecosystems before Elwha | Science’s ecosystem unit precedes the Elwha unit |
| Climate reasoning | Science and ELA overlap; both provide a local route, so neither must assume the other has finished |

No additional unbridged same-year prerequisite failure was established.

## Lens checklist: course frame

| Checklist line | Status | Evidence |
|---|---|---|
| Units use specific topics and texts rather than skill labels or broad themes | **Met** | Six identifiable topics with related reading, writing and talk |
| Anchors are on file, with measures, qualitative reasons and placement reasons | **Missed** | Proposed works and source families do not supply those records, finding 1 |
| Texts avoid dependence on one era, tradition or kind | **Missed in demonstrable evidence** | Forms and periods vary, but actual original texts and the final anchor inventory are unavailable; cultural and authorial range cannot yet be established |
| A long text is read whole | **Met in the frame** | The approximately 20,000-word novella is explicitly read whole; delivery remains subject to finding 1 |

The progression, scope and sequence, unit and day checklists are not separately scored at this layer. Their frame-level implications, including repeated research and process writing, were considered above.

## Settled by the expert

These are recommendations for the caller to apply. No edits were made.

| Choice | Reason | File affected |
|---|---|---|
| Keep the six units and 160-day total | No demonstrated annual overload or unit imbalance | Grade 7 frame |
| Keep Unit 3 as the research and presentation owner; reuse both in Unit 6 | Restores the progression’s counts without duplicate ownership or another major written piece | Grade 7 frame |
| Use digital peer feedback and a school-day access route | Completes the existing publication requirement | Grade 7 frame |
| Add discussion progress tracking and elaboration explicitly | Restores the Grade 7 performances | Grade 7 frame |
| Compare a general dictionary and a medical glossary | Fits the existing disease topic and reference standard | Grade 7 frame |
| Describe Athens as concurrent, with ELA background taught first | Matches both calendars without moving units | Grade 7 frame |
| Retain relevance judgments in Unit 6 | Judging evidence relevance belongs within Grade 7; naming irrelevant evidence does not itself require a Grade 8 extension | Grade 7 frame |
| Use source-specific drought-map attribution | The source supplies a usable permission route | Grade 7 frame and later text record |

## What is right and should remain

- The whole novella gives evidence, theme, interaction and point-of-view work a shared foundation.
- The Dust Bowl unit makes fiction against history concrete.
- All three writing types have process or shorter applications.
- Formal discussion recurs at least every two weeks.
- The source-based units include arguments, reports, visual information and recorded speech.
- Sensitive-content notes avoid requiring personal disclosures and identify relevant qualified readers.
- Checks have explicit respond days, and the paper route acknowledges a digital completion boundary.

## What I could not judge

Actual text quality, measures, cultural range, informational-anchor share, reading volume, question quality, scoring guidance and classroom minutes cannot be verified from proposed texts. The full global plan gate also remains uncompleted because of the environment dependency.

The published comparisons were used to examine design, not to require their texts, purchases or formats. [EL Education’s Grade 7 map](https://el-education-production.s3.amazonaws.com/media/documents/CurriculumTools_CurriculumMap-Grade7_0220.pdf) documents recurring research and named texts. [Great Minds’ implementation guide](https://greatminds.org/hubfs/WW%20Uploads/Great%20Minds%20Wit%20%26%20Wisdom%20Sample%20Teacher%20Resource%20Pack.pdf) shows how text sets, complexity records and writing purposes accompany a year plan. Neither comparison establishes that this course needs more units.

## Sources and access notes

- Official Grade 7 [literature](https://www.thecorestandards.org/ELA-Literacy/RL/7/), [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/7/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/7/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/7/), and [language](https://www.thecorestandards.org/ELA-Literacy/L/7/) standards: ownership and full performances.
- [Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf) and [2012 supplement](https://achievethecore.org/file/5): complexity dimensions and band measures.
- [Review-tools index](https://edreports.org/process/review-tools/ela): accessed the linked criteria and relevant evidence-guide sections after the initial direct criteria request failed.
- [WWC secondary writing guidance](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): supports explicit writing instruction, reading-writing connections and feedback. It does not establish a required number of major pieces.
- [Drought Monitor permission](https://droughtmonitor.unl.edu/About/Permission.aspx): reuse and attribution.

**For the source list:** Add the current Grade 7 curriculum-map URL and the drought-map permission page if absent. Preserve the review-tools index as the fallback route for its linked PDFs.

## For Cory

- **Scope:** Resolve the Athens-only proposal against the existing Greece-and-Rome knowledge thread. Reconcile all affected handoffs together.
- **Audience:** Confirm the assumed 50-minute daily lesson plus four nights of home reading.
- **People and money:** Assign the qualified ELA text reader and Lower Elwha Klallam community reader already required by the frame, including any compensation.

**Verdict:** Revise before accepting the frame’s coverage claims. **Findings:** 10. **Report path:** `docs/reviews/frame-english-language-arts-grade-7-2026-11-14.md`, delivered here, not written.

