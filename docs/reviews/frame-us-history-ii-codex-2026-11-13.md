# Independent review: US History II course frame

The frame has a coherent historical structure and complete placement of its progression rows, but it needs revision before it becomes the scope and sequence. Its greatest risk is treating a standard’s code as evidence of full coverage when the described work leaves part of that standard untaught. The most useful change is to complete the economics, geography and capstone requirements, then reconcile the shared research calendar with ELA.

**Findings: 8.**  
**Intended report path:** `docs/reviews/frame-us-history-ii-2026-11-13.md`  
**Delivery:** Complete report below. No file was created or edited.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, the shared adoption criteria and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`, and `docs/courses/social-studies/STANDARD.md`.
- `docs/FOUNDATION.md`, the relevant ROADMAP sections, BASELINE rules 20 to 24, `docs/GLOSSARY.md`, `docs/APPROACH.md` and relevant source-register entries. There is no separate social studies approach page.
- The complete US History II frame and its `frames.csv` row.
- All 25 `us2-` progression rows, their prerequisites, relevant earlier-grade rows, Massachusetts USII standards and cited C3 indicators.
- US History I’s frame, the relevant World History II frame material, and Government and Economics coordination statements. There is no subsequent history course.
- ELA 12’s research and presentation progression rows and the earlier mathematics rows cited by this course. No ELA 12 frame was available.
- The source policy, integration guidance and social studies materials report.
- Relevant earlier progression, cross-subject and adoption-bar reviews and their fix records. Earlier report excerpts were used to determine repetition and distinguish completed repairs from remaining defects.

No substantive finding rests solely on memory. The frame’s check-state additions remain explicitly provisional where the writer says their exact references came from knowledge rather than a document comparison.

### Gate results

| Check | Result |
|---|---|
| Requested `python -X utf8 scripts/plan.py check` | Stopped during import: `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternate Python launcher | Could not start its child process |
| `scripts/frame.py check us-history-ii` | **0 failures** |
| Social studies progression checker | **384 rows, 0 failures** |
| Final `scripts/stale.py check` | **19 files, 0 failures** |

The full plan gate therefore remains **unverified**, rather than passed or failed on curriculum content. The independent frame and progression checks establish their narrower structural results.

## Findings, most serious first

### 1. Unit 1 does not fully describe two economics standards it claims

**Severity:** substantial  
**LAYER:** frame  
**REPEAT:** yes, incomplete bundled-standard coverage identified in the earlier social studies reads  
**Confidence:** firm

**What is wrong.** Unit 1 assigns `MA.USII.T1.5`, but its learning description covers moving savings into investment and tracking an investment without explaining how market participants establish asset prices and affect returns. It also reduces `MA.USII.T1.8` to spending and national income. Employment, prices and the interpretation of national measures are not explicit. The corresponding `us2-econ-toolkit` note has the same substantive omissions.

These are requirements of the [Massachusetts framework, PDF pages 130 to 131](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=130), not optional extensions.

**Why it matters.** A writer can follow this frame faithfully and produce a portfolio exercise and a spending explanation that never teach the omitted relationships. Economics cannot be assumed to supply them because the frame correctly permits either course order.

**Exact fix.** Add to Unit 1 and `us2-econ-toolkit`:

> Students explain how buyers and sellers establish financial-asset prices and how a price change affects an investment’s return, using a fictional asset. They trace household and firm spending and production decisions through national income, employment and prices, then interpret supplied national indicators and explain what each measures.

Keep this instruction inside Unit 1. Describe the unit as **review of earlier market reasoning plus new historical economics**, while preserving Cory’s approved review-toolkit purpose.

### 2. The two owned geography indicators are narrower in practice than their wording

**Severity:** substantial  
**LAYER:** frame  
**REPEAT:** yes, the partial C3 coverage kind in the earlier progression reviews  
**Confidence:** firm

**What is wrong.**

- **Unit 3, `D2.Geo.9.9-12`:** Dust Bowl drought, farming practices and migration provide a useful case, but neither the frame nor progression note explicitly requires long-term climate evidence, the full set of spatial consequences, or work extending from local to global scales.
- **Unit 6, `D2.Geo.8.9-12`:** The frame describes city and suburb. The indicator also includes rural regions and relationships among the three. The progression note mentions countryside, but the frame drops it.

The distinctions are visible in the [C3 geography table, PDF page 43](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf#page=43).

**Why it matters.** A migration narrative and a redlining-map exercise could satisfy the current descriptions while leaving the owned geographic reasoning incomplete.

**Exact fix.**

- In Unit 3 and `us2-depression`, require a dated climate record and linked maps or data through which students evaluate migration, settlement, resource use and land use at local, regional and global scales. Distinguish climate variability from farming and policy decisions.
- In Unit 6, explicitly include the rural fringe and require students to evaluate changes **within and among urban, suburban and rural areas**, rather than only identify mapped differences.

Retain the existing units and day totals. These repairs complete already assigned indicators.

### 3. The capstone claims complete C3 coverage but specifies only part of it

**Severity:** substantial  
**LAYER:** frame  
**REPEAT:** yes, earlier C3 completeness findings, including explanation critique and outside audiences  
**Confidence:** firm

**What is wrong.** Unit 12 requires one argument adapted for a chosen audience and a structured peer critique. That leaves two gaps:

- `D4.3.9-12` requires adaptation across a range of audiences and venues, with print, oral and digital communication.
- `D4.5.9-12` concerns critiquing **explanations**. Critiquing an argument does not automatically supply that performance.

The [C3 communication and critique tables, PDF pages 60 to 61](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf#page=60) distinguish these demands.

**Why it matters.** Students could complete every stated capstone requirement without practising or demonstrating the full indicators the course owns.

**Exact fix.** Replace the capstone’s generic presentation and critique requirements with:

> Students adapt their findings into a print briefing, an oral presentation and an offline digital presentation for two contrasting audiences beyond their own classroom. They critique one argument for the credibility of its claims and evidence, and separately critique one historical explanation for reasoning, sequence and supporting detail. They revise after feedback.

Put the same requirements in `us2-research-paper`. One source set can support all formats; three separate research projects are unnecessary.

The earlier repair adding an outside audience is present and should remain. This finding concerns the remaining breadth.

### 4. Disciplinary literacy is still missing from the standards inventory

**Severity:** substantial  
**LAYER:** standard  
**REPEAT:** yes, explicitly carried forward in the earlier cross-subject review  
**Confidence:** firm

**What is wrong.** `STANDARD.md` says the anchor’s literacy standards were not loaded because the ELA file covers them. The loaded ELA records do not contain the corresponding RH and WHST inventory. This frame names general ELA research and presentation codes without closing that documented gap.

The official [history/social studies reading standards](https://www.thecorestandards.org/ELA-Literacy/RH/11-12/) and [disciplinary writing standards](https://www.thecorestandards.org/ELA-Literacy/WHST/11-12/) are distinct from general RI and W codes.

**Why it matters.** Historical reading and writing can appear to be somebody else’s responsibility. A shared essay alone does not establish coverage of disciplinary source comparison, evidence integration and explanation.

**Exact fix.**

1. Correct `STANDARD.md` to identify the inventory gap accurately.
2. Load the applicable disciplinary literacy standards.
3. Record grade 11 contributions and grade 12 completion, then map the grade 12 obligations to this course’s existing source work and writing.
4. State in this frame that historical reading and writing are taught here, including when ELA is not paired.

**For Cory:** approve the ownership allocation between courses before standards are assigned or moved. The inventory correction itself does not require a new scope decision.

### 5. The shared research brief has incompatible starting points

**Severity:** substantial scheduling risk  
**LAYER:** frame  
**REPEAT:** yes, the shared-calendar and research-load requirements of the cross-subject reviews  
**Confidence:** firm on the conflict; judgment call on the proposed calendar

**What is wrong.** The ELA progression specifies an approximately eight-week project with eight sources, an annotated bibliography, a roughly 2,500-word essay and a talk. History’s shared brief adopts that project, but Unit 12 says the question is picked on its first day.

With the stated unit order and assessments, Unit 12 occupies **days 148 to 160**. An eight-week project ending on day 160 would begin around day 121. ELA would already have worked for roughly 27 days before history selects their supposedly shared question.

The table also permits research instruction “before or alongside” Unit 12 without identifying which course first teaches each required move. No ELA 12 frame confirms the arrangement.

**Why it matters.** Teachers cannot implement one shared project from two incompatible briefs. Students may face duplicated research or a rushed restart.

**Exact fix.**

- For the paired route, reserve **days 121 to 160** as the proposed ELA project window. Choose the shared question and agree the source requirements at its opening.
- Change history Unit 12’s first-day task from choosing the question to **confirming or refining it after the final content units**.
- Make history’s final 13 days the historical synthesis, critique, revision, presentation and action phase.
- Specify a separate standalone history route, including its product size, source expectations and instruction time.
- Require the eventual ELA frame to record the matching milestones before the pairing is called verified.

This changes coordination, not ownership of the existing standards.

### 6. The loaded anchor paraphrase omits equity from economic policy goals

**Severity:** moderate  
**LAYER:** standard  
**REPEAT:** yes, the incomplete-standard-record kind found in the earlier social studies review  
**Confidence:** firm

**What is wrong.** `data/standards/ma-hss-2018.txt:527` omits **equity** from `MA.USII.T1.2`. The progression repeats the shortened list. The original includes it. See [Massachusetts, PDF page 130](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=130).

**Why it matters.** A shortened standards record makes an omission invisible to later coverage checks.

**Exact fix.** Add equity to the standard paraphrase and `us2-econ-toolkit` note. In Unit 1, require students to compare two policies by their effects on different groups and explain a trade-off among policy goals. No new standard or unit is needed.

### 7. Unit 8’s compelling question sets up a false choice

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, false either-or framing identified in `bar-subjects-2026-11-11.md`, finding 4  
**Confidence:** likely

**What is wrong.** The question asks whether presidents should be judged by contemporary documents **or** later outcomes. Both are needed for this unit’s stated work: understanding policy choices and evaluating intended and unintended consequences.

**Why it matters.** A writer could turn the unit into choosing a preferred kind of evidence instead of weighing decisions against consequences.

**Exact fix.** Replace the question with:

> How should the choices available at the time and their later consequences shape our judgments of Kennedy, Johnson and Nixon?

Require a response using contemporary evidence and evidence of outcomes. Keep Eisenhower in the Vietnam-policy comparison, as the assigned standard requires.

### 8. Unmarked stale notes survive the successful stale-note gate

**Severity:** moderate process risk  
**LAYER:** process  
**REPEAT:** yes, the stale-dependency kind documented in the day 14 review and later reviews  
**Confidence:** firm

**What is wrong.** The checker does not scan every review or recognize every outdated status phrase. The following statements conflict with current files or recorded decisions.

| Location | Exact replacement or repair |
|---|---|
| `social-studies.csv`, `us2-econ-toolkit`, `us2-civil-rights-laws`, `us2-social-movements` | Replace “government and economics are grade 12 courses” with “government and economics may be taken in grade 11 or 12; their progression rows remain recorded at grade 12.” |
| `progression-social-studies-fixes-2026-11-13.md`, “Skipped, needs Cory,” Codex 3 | Record that `q-ss-progression-1` settled access in grades 11 or 12, with rows retained at grade 12 and prerequisites revised. |
| Same report, Codex 6 | Replace the statement that checking waits on the other progressions with a reference to the completed cross-subject reviews and fix report. Distinguish progression availability from remaining within-year scheduling. |
| `social-studies-open-material-2026-11-13.md`, pending licence verdicts and final Cory questions | Add the subsequent `q-ss-partial-bases` decision and replace pending verdicts: OGL v3.0 was accepted; the named retired CC BY editions were accepted as partial bases. Preserve the original research observations as dated history. |
| `docs/ROADMAP.md:95` | Replace the statement that social studies waits on an undecided content standard with the settled C3 and Massachusetts anchor decision and current frame-planning stage. |
| `docs/GLOSSARY.md:52-53` | Remove “planned” from the existing progression CSV path. Replace the course frame’s “Not built” status with `docs/courses/<course>/frame.md`, tracked in `data/plans/frames.csv`. |

**Why it matters.** These notes can reopen settled decisions, imply completed checks remain undone, and misdirect the next worker.

The frame’s marked topic-page dependency is still pending and is **not** reported as stale.

## Coverage, pacing and seams

### Placement and year fit

All **25 owned progression rows occur exactly once** in the frame. All **43 numbered Massachusetts USII standards have a unit assignment**. Neither result establishes full instructional coverage; findings 1 to 4 and 6 address that distinction.

| Unit | Days | Progression rows | Days before subtracting any separate readiness lesson, but after unit assessment and respond day |
|---|---:|---:|---:|
| 1. Economics toolkit | 13 | 2 | 11 |
| 2. Tradition and modernity | 13 | 2 | 11 |
| 3. Depression and New Deal | 14 | 2 | 12 |
| 4. Isolation, fascism and Holocaust | 15 | 3 | 13 |
| 5. Home front and atomic bombs | 10 | 2 | 8 |
| 6. Cold War and postwar society | 17 | 3 | 15 |
| 7. Civil rights and desegregation | 17 | 3 | 15 |
| 8. Presidencies and Vietnam | 11 | 2 | 9 |
| 9. Rights movements | 10 | 1 | 8 |
| 10. Political change and Cold War’s end | 11 | 2 | 9 |
| 11. Since 1990 | 10 | 2 | 8 |
| 12. Capstone | 13 | 1 | 11 |
| **Units** | **154** | **25** | **130** |
| Course assessments and respond days | **6** | | |

The **160 scheduled days** leave 20 days within a 180-day calendar. Course checks and responses are already included.

Unit 1 is dense: 11 numbered anchor standards in 13 days. Its later applications help justify the allocation, but its missing requirements must be budgeted explicitly. Unit 12’s paired research schedule is the clearest demonstrated pacing problem. Row counts alone do not establish that another unit is substantially overfunded or underfunded.

### Order and handoffs

- US History I’s ending around 1920 connects to Unit 2. Unit 1’s earlier and later economic examples have an explicit toolkit rationale.
- The grade 10 Depression, war, Holocaust, atomic-bomb and Cold War work returns with stated US-focused purposes.
- The earlier research cycle and argument writing support this course’s increasingly independent work.
- Chronological overlaps in the Cold War, civil rights and presidential units are justified by their thematic organization.
- Government and Economics remain usable in either order beside history.
- Earlier mathematics supplies the graph reading and percent-change demands.
- There is no later history frame to receive an outgoing handoff. The endpoint is appropriately research, public communication and civic life.
- Same-year ELA availability remains unverified until its frame exists and resolves finding 5.

### Source map

There is no whole-course base text, so an exhaustive map of an entire textbook is not applicable. The missing `data/plans/us-history-ii/source-map.csv` is not, by itself, a coverage finding for this independently written course.

The nominated partial-source units follow the historical sequence from reorganization through termination, rights movements and contemporary sovereignty. No NonCommercial or reference-only source is presented as adaptable. Actual selected passages, activities, rights exceptions and adaptation time still require unit-level records.

## Lens checklist

| Course-frame checklist line | Result |
|---|---|
| Every anchor standard in the course’s topic range has a unit | **Met for assignment; incomplete in substance**, findings 1 and 6 |
| Replaced grade 3 or “your state” grade 8 retains Massachusetts-only content | **Not applicable**. The high school Boston case is an owned anchor requirement and is contextualized nationally. |
| Units identify check-set additions and their sources | **Met provisionally**. Candidate additions are listed; exact comparisons remain unit-plan work. |

Broader lens commitments:

| Commitment | Frame judgment |
|---|---|
| Inquiry with directly taught content | Met as a design commitment |
| Reasoned chronological order | Met |
| Primary and secondary sources; multiple accounts | Met as a commitment, source sets not yet judged |
| Claims, evidence, reasoning and counterclaims | Met in outline; capstone completion needs finding 3 |
| Geography and economics as reasoning | Partly met, findings 1, 2 and 6 |
| Historical judgment and contextualization | Partly met, finding 7 |
| Annual student-chosen informed action | Placed in Unit 12 |
| Plain hard history and sensitivity flags | Met at frame level; qualified and sensitivity reads remain required before publication |

## What is right and should remain

- Keep the explicit reasons for unit boundaries and chronological overlaps.
- Keep Boston desegregation as a national case rather than deleting an owned standard because the site serves students elsewhere.
- Keep the distinction between review and ownership of earlier C3 work.
- Keep Native nations as contemporary governments, multiple accounts of contested events, and prohibitions on harmful simulations and compelled family disclosure.
- Keep unseen-source assessment commitments and protected respond days.
- Keep the independent routes for schools using history without the paired ELA, Government or Economics courses.

## Settled by the expert

These are proposed implementation choices. Nothing was applied.

| Choice | Reason | File touched |
|---|---|---|
| Retain 160 scheduled days and the current unit order | No demonstrated need to enlarge or reorder the year | US History II frame |
| Complete asset-price/return reasoning and national economic measures inside Unit 1 | These are existing obligations, not new scope | Frame; `us2-econ-toolkit` |
| Include the rural fringe in Unit 6’s geographic evaluation | Completes the assigned indicator within its existing case | Frame |
| Require distinct argument and explanation critiques | Completes existing capstone codes | Frame; `us2-research-paper` |
| Use days 121 to 160 as the proposed paired research window | Makes the eight-week ELA project compatible with history’s final phase | Frame; eventual ELA 12 frame |
| Replace Unit 8’s question with the wording in finding 7 | Requires complementary evidence rather than an artificial choice | Frame |
| Correct the stale statuses listed in finding 8 | Recorded decisions already settle them | Named notes and reports |

## For Cory

- **Standards ownership:** settle the RH/WHST allocation across grades 11 and 12 before assigning or moving standards.
- **People:** identify the qualified readers required for Native and hard-history material before affected units are published.

## What I could not judge

The complete plan gate, the eventual ELA calendar, detailed lesson pacing, actual source difficulty and rights, assessment-item coverage, or the execution of sensitive-content safeguards. This is a frame review, not a finished-course adoption judgment.

## Outside sources and source-list additions

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): checked USII requirements and the economics paraphrase.
- [C3 Framework, revised 2017 PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): checked geography, presentation and critique requirements.
- [Official history/social studies reading standards](https://www.thecorestandards.org/ELA-Literacy/RH/11-12/) and [disciplinary writing standards](https://www.thecorestandards.org/ELA-Literacy/WHST/11-12/): checked the disciplinary-literacy distinction.
- [California history and social science standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf) and [New York grades 9 to 12 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-9-12.pdf): spot-checked candidate content comparisons, not every proposed addition.
- [Historical inquiry curriculum overview](https://www.inquirygroup.org/history-lessons): checked the integration of questions, source reading and corroboration.
- [Washington high school tribal-sovereignty curriculum](https://ospi.k12.wa.us/index.php/student-success/resources-subject-area/john-mccoy-lulilas-time-immemorial-tribal-sovereignty-washington-state/high-school-curriculum): search result accessible; full page returned **403**. Detailed adaptation conditions were not freshly verified.

For the source list: add the directly accessed standards and inquiry links above to `APPROACH-SOURCES.md`, with the portions read and the Washington access limitation. No source-register file was changed.

**Verdict:** revise before scope-and-sequence writing. **Finding count:** 8. **Report path:** `docs/reviews/frame-us-history-ii-2026-11-13.md`, supplied inline only.

