# Independent expert read: Grade 12 English language arts course frame

**Date:** 2026-11-14  
**Requested report path:** `docs/reviews/frame-english-language-arts-grade-12-2026-11-14.md`  
**Delivery:** Complete report supplied here. No file was written.

## Verdict

The course has a defensible unit order, complete skill placement and a plausible year budget, but it needs revision before scope and sequence writing. Its largest risk is claiming complete preparation without the anchor-text records and completion rules needed to substantiate that claim. Complete those records, distinguish paper participation from digital proficiency, and reconcile the frame with its progression and cross-subject calendars.

**Finding count: 11, comprising five curriculum or planning findings and six stale-review findings.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens and `docs/RUBRIC-ELA.md`.
- The foundation, shared and ELA approaches, glossary, relevant baseline rules, roadmap requirements and source register.
- The complete [Grade 12 frame](/S:/CurioClass/docs/courses/english-language-arts-grade-12/frame.md), its `frames.csv` row, all 30 Grade 12 progression rows, and the Grade 11 progression information needed to check its seams.
- The complete Grade 11 frame. There is no subsequent ELA course frame: Grade 12 is the endpoint.
- The grades 11 to 12 standards, including their lettered parts, in `data/standards/ccss-ela-standards-full.txt`.
- The relevant units, checks and coordination passages in the US History II, Government, Economics and Algebra II frames.
- The base-text register, library catalog and source records, and selected local text metadata, openings, endings and word counts.
- Earlier ELA progression, reconcile, stitch, fix and rubric reports; the relevant social studies frame reviews and subsequent fix report. Earlier reports supplied comparison and REPEAT classifications, not proof of current conditions.

Outside reading included the official standards, Appendix A, publishers’ criteria, relevant portions of the ELA evidence guide, the federal secondary-writing guidance, and curriculum comparisons listed below.

**Memory:** No substantive finding rests on memory. Saved guidance was used only to reinforce the requested read-only review boundary.

## Checks and their limits

The first requested command stopped before completing:

```text
python -X utf8 scripts/plan.py check
ModuleNotFoundError: No module named 'markdown'
```

The available interpreter is the Python installation bundled with LibreOffice. No dependency was installed.

Read-only checks subsequently completed:

| Check | Result |
|---|---|
| `scripts/plan.py check english-language-arts-grade-12` | 0 failures; 0 items and wrong answers checked |
| `scripts/frame.py check english-language-arts-grade-12` | 0 failures; 8 units, 160 days |
| `scripts/progression.py check ela` | 374 rows, 0 failures |
| `scripts/stale.py check` | 56 files, 0 failures |

The scoped plan check does not establish lesson or assessment coverage: this course has no populated plan directory. The frame gate settles placement and totals, not the instructional adequacy of the prose.

## Findings, most serious first

### 1. The anchor-text record is promised, but does not exist

**Severity:** Substantial  
**LAYER:** frame  
**REPEAT:** yes, the missing text-record and text-availability problem in the earlier ELA rubric and course reviews  
**Confidence:** firm

**Location:** Frame, “Base text,” “Reading level and supports,” “Anchor text records,” and Units 2, 3, 5 and 6.

There is no `data/plans/english-language-arts-grade-12/texts.csv`, or equivalent course inventory establishing the edition, selected passage, difficulty and availability of every anchor. Some substantial texts are present: the local Hamlet file contains about 31,700 whitespace-separated words and Gatsby about 48,100. However, I found no corresponding library text assets for several required anchors, including *The Importance of Being Earnest* and *A Room of One’s Own*.

The statement that every anchor “has a Curio Class print copy” therefore outruns the demonstrated record. Approximate measures and short qualitative comments cannot substantiate the whole year’s high-end reading demand. Appendix A requires quantitative, qualitative, and reader/task considerations together; the evidence guide also asks for a placement rationale. [Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf), [ELA evidence guide, indicator 2b](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf).

**Why it matters:** Writers could plan from different editions, discover missing texts late, or treat an unsupported band label as evidence of appropriate demand.

**Exact fix:** Before scope and sequence writing, complete an anchor inventory giving:

- Exact title, edition, source link, local asset and required passage boundaries.
- Whole-text or excerpt status, with a reason for excerpting.
- Named quantitative measure and method where usable.
- Qualitative analysis under the four established headings.
- Reader/task demands, placement rationale and matched supports.
- Separate identities and availability records for recordings and film versions.

Replace the present availability claim with:

> Every required anchor must have a checked, locally available print copy before its unit is planned; the course inventory records which assets are complete.

Report anchor counts and reading-day allocations separately. “Half the reading days” is not an anchor-count inventory.

### 2. Paper alternatives can finish the offered course without completing digital requirements

**Severity:** Substantial  
**LAYER:** standard  
**REPEAT:** yes, `progression-ela-codex-2026-11-13.md`, finding 3, and its subsequent fix report  
**Confidence:** firm

**Location:** Frame lines 16, 111 and 119; `e12-process` and `e12-presentation`.

The posted copy and binder substitute for digital production, publication and updating. A printed presentation handout substitutes for strategic digital media use. Neither route states that the corresponding requirement remains unfinished.

W.11-12.6 and SL.11-12.5 explicitly require technology use. The paper path supports substantial learning, but cannot itself demonstrate those performances. [Writing standards](https://www.thecorestandards.org/ELA-Literacy/W/11-12/), [Speaking and listening standards](https://www.thecorestandards.org/ELA-Literacy/SL/11-12/).

**Why it matters:** A teacher could accurately report completion of every assigned task while inaccurately recording full standard completion.

**Exact fix:** Add to the frame and both progression rows:

> The paper path completes the reading, composition and presentation work it supports. Record W.11-12.6 and SL.11-12.5 separately until each student completes the required digital performance.

Specify a school-day or teaching-parent device route, with no student account required: produce, publish and update one writing product after feedback, and create and use digital media purposefully in a presentation. Where access is unavailable, record the digital requirement as unfinished.

### 3. Speech evaluation does not explicitly require judging the speaker’s evidence

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, incomplete treatment behind a valid standard code recurs in the earlier frame reviews  
**Confidence:** likely

**Location:** Unit 6; `e12-info-rhetoric.notes`.

Both descriptions enumerate stance, premises, links, word choice, emphasis and tone. Neither explicitly requires evaluating the speaker’s use of evidence. The housing set separately judges source credibility, but its description does not secure this missing performance on the speeches.

SL.11-12.3 includes evaluation of reasoning and evidence alongside rhetoric. [Official standard](https://www.thecorestandards.org/ELA-Literacy/SL/11-12/).

**Why it matters:** The likely assignment can reward analysis of persuasive delivery without requiring judgment of whether the argument is supported.

**Exact fix:** Add to Unit 6 and the progression note:

> For one recorded address, students identify a consequential claim, distinguish its supporting evidence from assertion or appeal, evaluate whether the reasoning and evidence support the claim, and explain how delivery strengthens or obscures that support.

Carry that requirement into the unit’s assessment brief.

### 4. Three authoritative progression notes still disagree with the frame

**Severity:** Moderate  
**LAYER:** progression  
**REPEAT:** yes, contradictory onset and handoff notes in the earlier ELA progression reads  
**Confidence:** firm

**Location:** `e12-seminar`, `e12-info-founding-documents`, `e12-lit-interpretations`; frame “For the lead,” items 2 to 4.

The frame correctly identifies these discrepancies, but leaves them unresolved:

| Progression row | Current conflict | Exact correction |
|---|---|---|
| `e12-seminar` | Says Grade 11 roles were set by the teacher, although the Grade 11 frame preserves student leadership | Apply the frame’s proposed replacement: Grade 11 used named rotating roles; Grade 12 groups set their own goals, deadlines and roles |
| `e12-info-founding-documents` | Names Seneca Falls, while Unit 7 specifies Walker’s *Appeal* | Replace the named pair with Walker against the Declaration, explicitly distinguishing Grade 10’s Seneca Falls pairing |
| `e12-lit-interpretations` | Leaves the American dramatist component in Grade 11, without recording the Grade 12 retrieval the frame requires | Add the frame’s sentence specifying retrieval of *Trifles* beside Hamlet |

**Why it matters:** A worker using the data as instructed can build a different course from a worker using the frame.

**Exact fix:** Synchronize these three notes without changing their standard owners or unit assignments. Then rewrite the lead notes as completed decisions, rather than continuing to request the same edits.

The seminar correction and retrieval clarification are settled here. The Walker selection is already the frame’s stated pick and needs reconciliation, not a second competing selection.

### 5. Cross-subject day ranges omit assessment days, and the shared project lacks one necessary milestone

**Severity:** Moderate for the presentation handoff; minor for date corrections  
**LAYER:** frame  
**REPEAT:** yes, the shared-calendar problem in the earlier US History II frame reviews  
**Confidence:** firm on dates; likely on the milestone risk

**Location:** Frame “Cross-subject,” especially lines 150 to 170.

The availability table partly counts unit days without inserting the other courses’ course-level checks.

| Reference | Frame says | Current frame arithmetic gives |
|---|---|---|
| Government Unit 5 | Days 36 to 44 | Days **38 to 46**, after its two-day check following Unit 4 |
| Government Unit 8 | Days 62 to 69 | Days **64 to 71** |
| Economics Unit 6 | Half-year days 43 to 49 | Days **45 to 51**, approximately year days **125 to 131** in spring |
| History Holocaust unit | Days 40 to 54 | Days **42 to 56** |
| History bomb unit | Days 55 to 64 | Days **57 to 66** |
| History civil rights unit | Days 82 to 98 | Days **86 to 102** |

These corrections preserve the main dependency conclusions. Government still finishes before ELA’s later uses, and the Economics fallback remains necessary.

History also requests presentation preparation before its Unit 12, which begins on day 148. ELA places presentation somewhere within days 123 to 160 without committing to preparation before that point.

**Why it matters:** Coordination based on these tables can miss actual overlap, particularly ELA’s Plessy work and the end of history’s civil rights unit, or assume presentation instruction has already occurred.

**Exact fix:** Correct the ranges above. Add matching milestones to both shared briefs: agree the shared question around day 123; provide presentation instruction and a formative rehearsal by day 147; use history’s days 148 to 160 for its historical synthesis and final communication. Preserve independent teaching routes.

### 6. The first US History II review still says the Grade 12 frame is absent

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, unmarked stale dependencies in earlier frame reviews  
**Confidence:** firm

**Location:** `frame-us-history-ii-2026-11-13.md:166-168,183`.

The cross-subject conclusion and limitations still describe a missing ELA frame. The current frame exists and names its research window.

**Why it matters:** This can send the next worker back to obtaining a document already available.

**Exact fix:** Add a dated status correction:

> Updated 2026-11-14: the Grade 12 ELA frame now exists and places its research project in days 123 to 160. The missing-frame limitation is closed; cross-subject dates and presentation milestones require the corrections identified in the independent Grade 12 frame review.

Preserve the original observation as dated history.

### 7. The second US History II review retains the same obsolete dependency

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `frame-us-history-ii-codex-2026-11-13.md:135,237`.

The report still makes verification depend on a future ELA frame.

**Why it matters:** It conflates the completed frame-writing step with remaining coordination work.

**Exact fix:** Add the dated correction from finding 6 beside the current coverage and seam conclusion. Mark the future-frame wording as historical; retain the original account of what was available during that read.

### 8. The first Government review still describes three existing frames as absent

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `frame-us-government-and-politics-2026-11-13.md:169-171,185`.

The ELA 11, ELA 12 and Algebra II frames all exist.

**Why it matters:** The note incorrectly identifies document availability as the remaining obstacle.

**Exact fix:**

> Updated 2026-11-14: all three referenced frames exist. Algebra II places S-IC.B.6 in Unit 7; Government retains its local bridge when taken earlier. The ELA frames supply unit timing and independent teaching routes. Remaining checks concern the chosen timetable and corrected day ranges, not missing frames.

### 9. The second Government review retains the absent-frame limitation

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `frame-us-government-and-politics-codex-2026-11-13.md:276`.

Its current limitations list still refers to absent ELA and Algebra II frames.

**Why it matters:** It leaves completed work appearing outstanding.

**Exact fix:** Replace that limitation with the dated current-status statement in finding 8. Keep the original read-history statement at line 17 as historical evidence.

### 10. The first US History I review still says the Grade 11 frame is unwritten

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `frame-us-history-i-2026-11-13.md:140-142,154`.

The Grade 11 frame exists and specifies the founding-document, Douglass and research coordination on which Grade 12’s incoming seam depends.

**Why it matters:** It conceals the available evidence for the preceding course.

**Exact fix:**

> Updated 2026-11-14: the Grade 11 ELA frame now exists. It places founding documents in Unit 3, Douglass in Unit 5 and reform research in Unit 4. The missing-frame limitation is closed; this update does not certify every remaining cross-subject scheduling detail.

### 11. The second US History I review’s proposed replacement note is itself stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

**Location:** `frame-us-history-i-codex-2026-11-13.md:252,308`.

The proposed status correction still says the Grade 11 frame is needed, and the later conclusion still attributes unverified timing to its absence.

**Why it matters:** A fixer could apply an already outdated replacement verbatim.

**Exact fix:** Replace the missing-frame clause and update the later conclusion using the statement in finding 10. Preserve the original finding and clearly date the correction.

## Coverage, units, days and seams

All **30 owned skills occur in exactly one unit**. They collectively name **41 parent standards**: nine literature, ten informational reading, ten writing, six speaking and listening, and six language standards. The absence of RL.11-12.8 is correct.

| Unit | Days | Owned skill rows | Judgment |
|---|---:|---:|---|
| 1. Reflective essays | 13 | 7 | Plausible because most rows establish year-long routines |
| 2. Hamlet | 23 | 7 | Substantial but justified by the whole play, interpretations and process argument |
| 3. Satire and comedy | 12 | 3 | Plausible with the stated home-reading expectation |
| 4. The 1920s | 18 | 2 | Whole-novel reading and comparisons justify the allocation |
| 5. Du Bois and Woolf | 11 | 3 | Dense; exact excerpt boundaries are needed to substantiate pacing |
| 6. Public rhetoric and housing | 16 | 3 | Plausible, subject to fixing speech evaluation |
| 7. Founding documents and law | 18 | 3 | Dense but coherent after structure and source judgment |
| 8. Senior research | 38 | 2 | About eight weeks matches the progression’s sustained project |
| **Units** | **149** | **30** | |
| **Course checks and responses** | **11** | | Three protected check cycles |
| **Total** | **160** | | Leaves 20 days within a 180-day calendar |

No unit is demonstrably overfunded or underfunded solely from these counts.

The Grade 11 to Grade 12 transition is largely coherent: students move from supplied topic areas, named uncertainties and structured support toward finding, selecting and leading. Shakespeare, legal reasoning and early twentieth-century literature complete explicitly identified band contributions. I do not recommend reteaching the entire two-year band in Grade 12.

Earlier-grade models are identified as retrieval. The frame does not require an unexplained new model before teaching it.

The principal cross-subject dependencies are workable. History teaches the 1920s before Unit 4; earlier mathematics supplies the statistics background; Unit 6 supplies an alternative when spring Economics comes later. The remaining calendar corrections are finding 5.

**Source map:** Not applicable. The base-text register identifies ELA 6 to 12 as independently written. No NC or reference-only curriculum is mapped as a base.

## Lens checklist: course frame layer

| Checklist line | Result |
|---|---|
| Units rest on specific topics and texts rather than isolated skills or broad themes | **Met in outline.** Named literary sets and public questions organize the course; the capstone uses approved individual questions and source sets |
| Anchors are on file, with measures, qualitative reasons and placement reasons | **Missed**, finding 1 |
| Texts avoid leaning to one era, tradition or kind | **Partly met.** Eras and genres vary, but the British and American concentration remains. The earlier progression review already records this scope concern; it is not counted again here |
| At least one long text is read whole | **Met as a frame commitment.** Hamlet, Gatsby and Earnest are required whole, with an additional independent book |
| Other progression, scope and sequence, unit and day checklist lines | **Not applicable as execution tests at this layer.** The frame establishes recurring research, process writing, discussion and vocabulary routines; later plans must demonstrate them |

## What is right and should remain

Keep the whole-text commitments, the tragedy and comedy comparison, the literary and legal arguments, and the independent-reading endpoint. Keep the recurring short writing, seminars, sentence work, protected respond days and distinction between access support and independent proficiency.

The research pairing sensibly shares a question and source set while retaining disciplinary teaching. The personal-disclosure protections and explicit sensitivity flags should remain.

The model, practice and revision commitments are consistent with the federal secondary-writing guidance. [WWC secondary-writing guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22/Published).

## Settled by the expert

These are recommendations for the caller. Nothing was applied.

| Choice | Reason | File affected |
|---|---|---|
| Retain 160 days and the existing unit order | No demonstrated need to enlarge or reorder the year | Grade 12 frame |
| Complete the anchor inventory before scope and sequence writing | Text demand and availability are frame-level decisions | Course text inventory and frame |
| Record digital completion separately from paper participation | Preserves the paper path and honest standard claims | Frame; `e12-process`; `e12-presentation` |
| Add explicit evidence evaluation to Unit 6 | Completes an existing standard without moving it | Frame; `e12-info-rhetoric` |
| Correct the seminar note and record the Trifles retrieval | Matches the actual incoming seam | `ela.csv` |
| Correct cross-subject dates and add a presentation rehearsal by day 147 | Makes the existing pairing implementable | ELA and history frames |
| Date the stale-review corrections | Preserves historical evidence while stating current conditions | Six named review files |

## For Cory

- **People and money:** Identify the required qualified or community readers, the recording participants, and the supportable adult-panel arrangement.
- **Scope and audience:** Resolve the already recorded grades 9 to 12 long-text breadth question if it remains open. This report does not independently expand the British and American course scope.

## What I could not judge

The repository-wide plan gate, complete textual integrity and rights clearance of every edition or recording, actual classroom minutes, assessment-item coverage, or the execution of sensitive-content safeguards.

I did not verify every candidate addition against the proposed supplementary frameworks. Those comparisons remain unit-plan work. The unavailable anchor records prevent a defensible whole-year complexity and text-balance judgment.

## Outside sources and source-list notes

- [Official grades 11 to 12 standards](https://www.thecorestandards.org/ELA-Literacy/RL/11-12/), [informational reading](https://www.thecorestandards.org/ELA-Literacy/RI/11-12/), [writing](https://www.thecorestandards.org/ELA-Literacy/W/11-12/), [speaking and listening](https://www.thecorestandards.org/ELA-Literacy/SL/11-12/), and [language](https://www.thecorestandards.org/ELA-Literacy/L/11-12/): checked the course’s claimed performances and band endpoint.
- [Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): checked the three-part complexity model.
- [Publishers’ criteria, grades 3 to 12](https://achievethecore.org/content/upload/Publishers_Criteria_for_Literacy_for_Grades_3-12.pdf): checked text-centered instruction, extended reading and writing expectations.
- [ELA grades 6 to 12 evidence guide](https://cozy-dream-721ab6aab0.media.strapiapp.com/ELA_6_12_Evidence_Guide_2_0_2068cea08f.pdf): consulted text inventory, complexity and knowledge-building guidance.
- [WWC secondary-writing guidance](https://ies.ed.gov/ncee/wwc/PracticeGuide/22/Published): checked explicit strategy instruction, reading-writing connections and formative feedback. The initial direct PDF request timed out; the official landing page and indexed guidance were accessible.
- [Odell program guide](https://odell-uploads-production.s3.amazonaws.com/release/materials/oe_programguide.pdf) and [grades 11 to 12 research unit](https://www.odelleducation.com/wp-content/uploads/2020/08/Research-Unit-Plan-G11-12-1.pdf): sampled research architecture, reference tools and revision supports as comparisons only.
- [New York Grade 12 curriculum archive](https://lessons.unbounded.org/ela/grade-12): the search-indexed overview was available, but the live page did not expose the curriculum materials. No finding depends on a presumed lesson sequence or pacing from it.

For the source list: add the official strand pages, accessible WWC landing page and sampled curriculum-comparison links where absent, recording the access limits above.

**Verdict:** Revise before scope and sequence writing. **Finding count:** 11. **Report path:** `docs/reviews/frame-english-language-arts-grade-12-2026-11-14.md`, supplied inline only.

