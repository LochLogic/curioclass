# Independent frame review: English Language Arts Grade 10

**Date:** 2026-11-14  
**Requested report path:** `docs/reviews/frame-english-language-arts-grade-10-2026-11-14.md`  
**Delivery:** Complete report below. No files were changed.

## Verdict

The frame has a defensible sequence, places all 26 Grade 10 progression skills exactly once, and accounts for 160 days with protected assessment and respond time. It needs revision before the scope and sequence is built because the shared research project has incompatible product requirements, several standards are incompletely specified, and one sensitive-text instruction conflicts with the repository’s language rule. Preserve the whole-work reading and grade-to-grade handoffs, but resolve the capstone brief and the incomplete instructional requirements first.

**Finding count: 12.**

## What I read and checked

- `docs/agents/EXPERT.md`, the ELA lens, `docs/RUBRIC-ELA.md`, `docs/FOUNDATION.md`, the relevant baseline rules, glossary, roadmap planning requirements, shared approach, ELA approach, and ELA source-access and evidence notes.
- The complete Grade 10 frame, its `frames.csv` row, and all 26 Grade 10 progression rows, including their notes, prerequisites, handoffs, models and cross-subject references.
- The Grade 9 and Grade 11 frames, with the adjacent progression dependencies needed to check both seams.
- The full grades 9 to 10 ELA standards, including lettered parts.
- The relevant World History II and Chemistry frame sections.
- `docs/sources/BASE-TEXTS.md`. Grade 10 ELA has no base text, so a base-text source map is not applicable.
- The earlier Grade 10 report, relevant ELA progression reports and reconciliation records, and the Grade 11 and Grade 12 review and fix records.
- Outside sources listed below, including the actual federal cloning pages and relevant literary passages.

No substantive finding rests solely on memory. Saved memory informed report-format conventions only.

### Gates

`plan.py check` could not complete because the environment lacks the `markdown` module; the required structural fallback passed, so the content verdict follows.

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped with `ModuleNotFoundError: No module named 'markdown'` |
| `python -X utf8 scripts/frame.py check english-language-arts-grade-10` | 0 failures; 7 units, 160 days |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |

Additional read-only inspection confirmed 26 skills placed once, no other grade’s skill in an ownership cell, and all 41 applicable band-level standard codes represented. These checks establish placement and totals, not full instructional coverage.

No turn, synchronization, defect-logging or other writing command was run.

## Findings, most serious first

### 1. The shared capstone lacks one compatible product and a workable time budget

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 10 report, findings 1 and 5  
**Confidence:** firm on the incompatible requirements; likely on classroom capacity

**Location:** Unit 7; writing calendar; Cross-subject research agreement; For the lead 1; World History II unit 11.

**What is wrong:** ELA requires a 1,200 to 1,800 word explanatory report with a student-made figure. History requires a research argument and explanation adapted for audiences. Agreeing that history supplies questions and sources while ELA supplies process and citation does not define how one product preserves both performances.

The presentation budget is also missing. Thirty students giving eight to ten minute talks, plus two minutes of questions each, require approximately 300 to 360 minutes before transitions. That consumes six to eight 50-minute periods inside a 28-day unit that also contains source analysis, research, drafting, revision and assessment.

**Why it matters:** A shared school could lose ELA’s only full explanatory process piece or quietly add a second paper. A unit writer could also budget one presentation day for work requiring substantially more time.

**Exact fix:** Add the same shared-brief block to both frames:

- One dossier containing a separately scored explanatory report, including its figure, and an argued recommendation with counterclaims.
- ELA scores explanatory writing, research, citation and presentation. History scores historical reasoning, explanation, argument and audience adaptation.
- History supplies the paired-school question set before ELA’s research begins.
- One common milestone calendar identifies the question, source list, draft, revision, presentation and history adaptation deadlines.
- Reserve eight presentation periods for a class of thirty, allowing four students per period and a final partial group.

A feasible **ELA-only planning budget** is four days for two short inquiries, fourteen for the sustained inquiry and writing, eight for presentations, and two for the unit assessment and response: 28 total. The paired-school calendar must be reconciled with that budget. The present promise of a wholly shared project in weeks 29 to 32 cannot simply remain unchanged alongside ELA’s week 31 completion.

The joint product and calendar proposal go to Cory because they change the workload agreement between courses.

### 2. The sensitive-text instructions permit prohibited language and omit material content

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, Grade 11 independent report, finding 1; earlier Grade 10 report, finding 11  
**Confidence:** firm

**Location:** Unit 6 sensitive-topics cell; course-wide text policy; unit 5 sensitive-topics cell.

**What is wrong:** Unit 6 reproduces the Declaration’s dehumanizing description of Native peoples and directs discussion of it without the omission boundary now present in Grade 11 and US History I. BASELINE rule 6 prohibits slurs.

Unit 5’s content note names war deaths but omits sexual encounters, nudity, amputation and suicidal distress in the whole novel. These are present in Wheen’s text, including chapters 1 to 2, 7 and 10. [*All Quiet on the Western Front*, Wheen translation](https://www.gutenberg.org/cache/epub/75011/pg75011-images.html).

**Why it matters:** A writer following the frame could reproduce prohibited language and prepare teachers inadequately for passages students are required to read.

**Exact fix:** Adopt Grade 11’s existing presentation rule: omit prohibited language with a visible omission mark and a short editorial explanation, preserve the surrounding argument, and disclose the omissions. Replace unit 6’s wording with:

> Analyze the Declaration’s dehumanizing description of Native peoples and its political purpose without printing the slur or requiring students to speak it. Pair the analysis with Native-authored accounts.

Expand unit 5’s content note to identify the omitted categories above and require the qualified reader to check the relevant passages before use. Retain the whole novel with disclosed language omissions.

### 3. W.9-10.7 loses its short-project requirement

**Severity:** Major  
**LAYER:** standard  
**REPEAT:** yes, incomplete standard components were identified in the earlier Grade 10 report, finding 4  
**Confidence:** firm

**Location:** Unit 7; `e10-w-research.notes`; writing calendar.

**What is wrong:** The progression explicitly requires short projects and one sustained project. The frame specifies only the sustained project. Reading a supplied source set and evaluating arguments do not automatically constitute additional research projects.

The requirement for both durations is explicit in W.9-10.7. [Official ELA standards, printed page 46](https://corestandards.org/wp-content/uploads/2023/09/ELA_Standards1.pdf). The high-school research indicator also expects repeated applications. [ELA evidence guide, PDF pages 80 to 82](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Evidence-Guide.pdf).

**Why it matters:** Grade 9’s earlier projects cannot complete a standard that Grade 10 claims to own in full.

**Exact fix:** Within unit 7, name two two-day inquiries before the sustained project. Each answers a bounded question, includes a student search, evaluates at least two sources, and produces a brief cited synthesis. Use different aspects of the unit topic. Count the four days explicitly, as in finding 1, while keeping ownership in unit 7.

### 4. Unit 2 substitutes comparison of outlines for detailed development analysis

**Severity:** Major  
**LAYER:** standard  
**REPEAT:** yes, earlier Grade 10 report, finding 9, with a newly verified source distinction  
**Confidence:** firm on the missing instruction; likely on selection suitability

**Location:** Unit 2, anchors and What students learn.

**What is wrong:** The planned outcome is two outlines showing how authors order material. That addresses part of RI.9-10.3 but does not secure RI.9-10.5’s analysis of how particular sentences, paragraphs and sections develop and refine ideas.

The anchor description is also inaccurate. The actual federal texts explain cloning generally. The genome institute’s fact sheet discusses Dolly within a broader account; the FDA primer explains livestock reproduction, cloning, risks and uses. They are useful contrasting explanations, but not two accounts devoted to Dolly’s experiment. [Cloning Fact Sheet](https://www.genome.gov/about-genomics/fact-sheets/Cloning-Fact-Sheet), [FDA cloning primer](https://www.fda.gov/animal-veterinary/animal-cloning/primer-cloning-and-its-use-livestock-operations).

**Why it matters:** A writer could deliver successful outline comparison while never teaching the finer analysis the course owns.

**Exact fix:** Name those exact pages and describe them as explanations of the same cloning process for different audiences. Add:

> Students trace how one explanation introduces, develops and connects its ideas, then analyze how selected sentences and paragraphs add, qualify or refine a claim. They explain what would change if one passage were removed or moved, before comparing the two authors’ organization.

Retain Huxley as the extended nonfiction study. Confirm the selected passages’ lengths and complexity in their text records.

### 5. Unit 3’s reading load and longer-work responsibility remain undefined

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 10 report, finding 2  
**Confidence:** firm on the ambiguity; judgment call on the eventual reading budget

**Location:** Units 3 and 5; `e10-rl-world-literature.notes`.

**What is wrong:** Fifteen days cover two stories, a poem, unspecified chapters of *Noli Me Tángere*, *Mhudi* “in large parts,” nonfiction background, comparison writing, punctuation, seminars and assessment. “Large parts” supplies no upper bound.

The frame then says the row’s longer-work study is finished in unit 5, where it is called review. That makes the place of first teaching unclear.

**Why it matters:** Different writers could produce substantially different reading loads or each assume the other unit completes the progression requirement.

**Exact fix:** Replace “large parts” with a bounded chapter selection and a reading budget before the scope and sequence is built. A workable starting selection is *Mhudi* chapters 1 to 4, printed pages 1 to 32, with a small, explicitly named *Noli* selection; use *Native Life* chapter 1 as teacher background unless student reading time is separately allocated. [Digitized 1930 *Mhudi*, chapter index](https://fynbosch.com/digitised-book-mhudi).

State explicitly whether that extended *Mhudi* study completes unit 3’s longer-work responsibility. If it does, unit 5 applies the already taught cultural-analysis method to the whole novel. If it does not, propose a placement or day change for Cory instead of assigning first teaching through a “review” sentence.

The longer-work requirement here belongs to the progression’s course design. RL.9-10.6 itself does not mandate a whole novel.

### 6. The claimed anchor record does not exist

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 10 report, finding 12; Grade 11 independent report, finding 7  
**Confidence:** firm

**Location:** Base text bullet; reading-level claims; course-frame lens requirement.

**What is wrong:** The frame says `texts.csv` gives every anchor its measure, qualitative analysis, task and placement reason. `data/plans/english-language-arts-grade-10/texts.csv` does not exist.

The frame supplies useful placement reasons, but no auditable anchor-by-anchor complexity record. A course-wide numerical range cannot establish the demand of individual selections. The three-part model requires text-specific analysis. [Appendix A, text-complexity section](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf).

**Why it matters:** The frame’s central claim about band-end reading demand cannot yet be verified.

**Exact fix:** Replace the present-tense claim with:

> Pending(data/plans/english-language-arts-grade-10/texts.csv): record each required anchor’s exact edition and selection, source location, quantitative measure where usable, four-part qualitative analysis, reader and task considerations, supports, and reason for placement.

Provide that inventory before confirming the text-complexity lens line. Identify original texts separately as unwritten selections requiring later review.

### 7. Speaking and listening are narrowed to seminars and formal presentations

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, earlier Grade 10 report, finding 4, for incomplete speaking requirements  
**Confidence:** firm

**Location:** Unit 1 seminar instruction; unit 7 speaker evaluation; presentation row.

**What is wrong:** Student-led seminars are well established, but the frame does not secure the full discussion range, including one-on-one and teacher-led settings. Its speaker judgment also leaves point of view, rhetoric and distorted evidence implicit. The formal talk and performed speech do not explicitly teach adapting speech between contexts.

These are distinct requirements within the speaking and listening standards. [Official ELA standards, printed page 50](https://corestandards.org/wp-content/uploads/2023/09/ELA_Standards1.pdf).

**Why it matters:** Frequent talk can still leave part of the owned standards untaught.

**Exact fix:**

- Unit 1: add a paired evidence exchange before a seminar and a teacher-led discussion of a difficult passage. Include decision-making rules, deadlines, inviting others in, and revising a view after hearing evidence.
- Unit 7: require a written evaluation of the recorded speaker’s stance, reasoning, rhetoric, evidence and any exaggeration or distortion.
- Unit 7: have students explain the same finding briefly to a peer and formally to the presentation audience, then explain their changes in language and organization.

These fit existing talk time and require no ownership move.

### 8. The device boundary covers publishing but leaves presentation evidence unresolved

**Severity:** Moderate  
**LAYER:** standard  
**REPEAT:** yes, earlier Grade 10 report, finding 11; Grade 11 independent report, finding 2  
**Confidence:** firm

**Location:** Devices bullet; unit 7; `e10-sl-presentation.notes`.

**What is wrong:** The frame honestly distinguishes paper publishing from W.9-10.6. It does not apply the same completion boundary to SL.9-10.5’s digital-media performance. A printed figure or handout supports a presentation but does not demonstrate strategic digital-media use.

**Why it matters:** The offered paper route could be recorded as completing a digital requirement.

**Exact fix:** Extend the Devices bullet:

> W.9-10.6 and SL.9-10.5 have separate recorded digital components, completed through a school-day shared-device route without student accounts. Paper alternatives preserve the writing and presentation work and leave the digital component unfinished until demonstrated.

In unit 7, name the actual linked publishing and update task and the student’s purposeful digital presentation choice. Supply a teacher-read transcript for listening tasks when recordings are unavailable, without treating it as digital-media production.

### 9. The final check does not clearly establish both reading endpoints

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 10 report, finding 4  
**Confidence:** firm

**Location:** Year-end course-level check; ownership of RL.9-10.10 and RI.9-10.10.

**What is wrong:** The final check names a translated story, an argument essay and an analytic essay “at the high end.” That wording does not clearly attach the complexity and independence conditions to both reading selections.

**Why it matters:** The outgoing seam promises band-end independent proficiency in literature and literary nonfiction. The assessment description could generate evidence for only one.

**Exact fix:** State that the year-end check includes documented high-end literary and literary-nonfiction selections, read independently without routine before-reading explanations or answer-supplying support. Record access accommodations separately. Add one earlier independent checkpoint for each strand during the second half of the course.

This strengthens the evidence for the existing endpoint without moving its ownership.

### 10. Unit 3’s question overdetermines Tagore, and its edition reference is wrong

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier Grade 10 report, finding 8  
**Confidence:** firm on the citation; likely on the question

**Location:** Unit 3 question and anchor citation.

**What is wrong:** The question asks what colonial rule did to people in every story. Tagore supplies colonial context, but the selected stories centrally develop separation, affection, work and unequal relationships. Requiring a direct colonial-cause answer encourages students to import an explanation the narrative may not establish.

The earlier reader’s proposed citation correction is insufficient. *The Postmaster* appears in *Mashi and Other Stories* (1918); *The Cabuliwallah* appears in *The Hungry Stones and Other Stories* (1916). [*Mashi*, text and contents](https://www.gutenberg.org/files/34757/34757-h/34757-h.htm), [*Hungry Stones*, text and contents](https://www.gutenberg.org/cache/epub/2518/pg2518-images.html).

**Exact fix:** Use:

> How do work, status and separation shape people’s lives in these societies, and where does each text make colonial power visible?

Correct the two edition references separately. Retain the colonial-history context while allowing students to distinguish direct evidence from contextual inference.

### 11. The cross-subject calendar contains a stale dependency and unresolved collisions

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier Grade 10 report, findings 6 and 7; Grade 11 independent report, finding 9  
**Confidence:** firm

**Location:** Cross-subject introduction; Chemistry availability row; hard-content and writing-load paragraphs.

**What is wrong:** Chemistry’s frame is described as written later, although it exists. Its climate unit runs in weeks 23 to 26, making that learning available for later ELA explanation.

The same calendar places Chemistry’s forecast near ELA’s week 26 issue argument without resolving the due week. It also calls week 18 “after” history’s Holocaust weeks, although those run through week 18, and does not acknowledge *Mhudi*’s week 11 overlap with the Armenian-genocide window.

**Exact fix:** Replace the dependency sentence with:

> Chemistry’s frame is on file. Its climate-forecast work is in unit 9, weeks 23 to 26, available by week 26 for ELA’s later explanatory work. Earlier technical writing uses Grade 9 skills and Chemistry’s model explanation.

Retain the if-later bridge. Name separate due weeks for Chemistry’s forecast and ELA’s issue argument. Replace the hard-content assurances with accurate overlap statements and require the scope and sequence to separate the relevant lessons by day. Do not claim separation from approximate week ranges alone.

### 12. Earlier review and progression notes still present completed decisions as open

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, Grade 11 and Grade 12 independent reports’ stale-note findings  
**Confidence:** firm

**Location:** Earlier Grade 10 report; ELA stitch and reconciliation reports; Grade 10 frame’s unresolved row pointers.

**What is wrong:** The marked-note checker passes, but it does not establish that these unmarked historical instructions remain current.

| Note | Repository evidence | Exact update |
|---|---|---|
| Earlier Grade 10 report, finding 3 and its Harper replacement decision | Grade 12 now uses Walker’s *Appeal* instead of the Declaration of Sentiments, in both frame and progression | Append: “Updated 2026-11-14: the duplicate pairing was resolved on the Grade 12 side. Grade 10 retains the Declaration of Sentiments. The Harper replacement is not needed to resolve this duplication.” |
| `progression-ela-stitch-2026-11-13.md`, Douglass row under Settled in the stitch, says “Not changed; for the lead” | Reconciliation and current Grade 10 row already replace Douglass with Anthony | Append: “Resolved in the reconciliation: Grade 11 keeps Douglass; Grade 10 uses Anthony.” |
| `progression-ela-reconcile-2026-11-13.md`, Rework for the old files, still instructs Grade 12 to distinguish or replace Sentiments | Grade 12’s replacement is complete | Append: “Resolved by the 2026-11-14 fix pass: Grade 12 uses Walker’s Appeal.” |
| Grade 10 world-literature and seminal-document rows say “see the lead list” | The frame gives no direct answer to those two pointers | Replace each pointer with its actual disposition: the chosen world-literature range, and the existing decision that the copyrighted example is not a required anchor |
| Frame and earlier Grade 10 report refer to 27 progression rows | Current CSV and the stitch both contain 26 | Correct the frame count; annotate the historical report with the verified count |

Preserve dated reports as history and append status corrections rather than silently rewriting their original judgments.

## Data-check conclusions

| Required check | Result |
|---|---|
| Owned skills | All 26 Grade 10 skills appear exactly once in ownership cells |
| Other grades’ ownership | No other grade’s skill is assigned as owned here |
| Standard codes | All 41 applicable band codes are represented |
| Standards in full | Not yet secure: findings 3, 4, 7 and 8; endpoint evidence needs finding 9 |
| Units and reasons | Overall order is defensible; units 3 and 7 need the clarifications above |
| Base-text source map | Not applicable |
| Grade 9 seam | Prerequisites are picked up; no missing incoming skill link found |
| Grade 11 seam | Outgoing skills match current receiving rows; proficiency evidence remains the concern |
| Cross-subject order | History’s imperialism, interpretation and propaganda work precedes its ELA uses; Chemistry timing is available but inaccurately recorded |
| Stale notes | Marked-note check passes; unmarked problems remain in findings 11 and 12 |

I do **not** repeat the earlier claim that W.9-10.9b lacks teaching solely because its code is not repeated in unit 7. The written judgment of an argument already supplies a relevant performance. Add the cross-reference for clarity, but absence of a second label is not itself missing instruction.

### Days and load

| Unit | Days | Owned skills | Judgment |
|---|---:|---:|---|
| 1 | 28 | 9 | Defensible for a whole novel, process essay and establishment of routines |
| 2 | 14 | 3 | Plausible after its source descriptions and analysis task are corrected |
| 3 | 15 | 2 | Load cannot be judged reliably while novel selections remain unbounded |
| 4 | 25 | 4 | Defensible for the whole play, source comparison, poetry and process argument |
| 5 | 22 | 1 | Defensible because it carries a whole novel, not merely one standards row |
| 6 | 16 | 2 | Plausible for the document set and process argument |
| 7 | 28 | 5 | Requires an explicit budget and shared-product decision |
| Course-level checks and response | 12 | — | Properly reserved |

**148 + 12 = 160 days.** This fits a conventional school year with approximately twenty additional days outside the course allocation. There is no reason to enlarge the year merely to preserve an unbudgeted activity.

## Lens checklist: course-frame layer

| Lens line | Status | Evidence |
|---|---|---|
| Units organized around specific topics and texts | Met with a correction | Concrete sets throughout; unit 3’s question needs finding 10 |
| Anchors on file with measure, qualitative analysis and placement reason | Missed | Placement reasons exist; the claimed text record does not |
| Year avoids excessive concentration in one tradition or text kind | Met within the established historical-text policy | Multiple regions and forms; both literature and informational reading |
| A long text is read whole | Met | *Frankenstein*, *Julius Caesar* and *All Quiet on the Western Front* |

K to 2 phonics requirements are not applicable. Question percentages, daily scaffolds, model writing and scoring guidance require later-layer materials and were not treated as demonstrated by this frame.

## What is right and should remain

Keep *Frankenstein* first, its connection to the two-narrator narrative, *Julius Caesar* beside North’s Plutarch, and the movement from rhetorical analysis to the liberty documents and research. Keep the three whole works, recurring vocabulary and seminars, readiness checks at first use, and course-level respond days.

Keep the distinction already made for W.9-10.6 between an accessible paper route and an unfinished digital component. Extend that honesty consistently.

## Settled by the expert

These are recommended item-level decisions for the caller to apply.

| Choice | Reason | File touched |
|---|---|---|
| Keep all seven units and the 160-day total | Structure and overall allocation are sound | Grade 10 frame |
| Keep Grade 10’s Declaration of Sentiments | Grade 12 has already removed the duplicate pairing | Frame and earlier review status note |
| Use the named genome fact sheet and FDA primer as contrasting general cloning explanations | Their actual content supports that comparison | Unit 2 |
| Add passage-level development analysis before comparing outlines | Preserves the full informational-analysis demand | Unit 2 |
| Reserve eight presentation periods for thirty students | Allows every student to present with questions and teacher observation | Unit 7 |
| Add two short inquiries within unit 7 | Completes the existing research requirement without moving ownership | Unit 7 |
| Use separate Tagore edition references | The stories are in different named collections | Unit 3 |
| Apply the existing disclosed-omission language policy | Consistency with the baseline and current neighboring frames | Course brief and unit 6 |

## For Cory

- **Scope:** Decide the proposed joint research dossier and common ELA/history calendar. The product must preserve a full explanatory performance and a full historical argument.
- **People and money:** Assign the community and qualified readers already required for units 3, 5 and 6. Unit 3’s coverage should include the Southern African communities represented; unit 5’s reader needs the complete content list.
- **Scope, only if needed:** If unit 3’s bounded selections cannot fulfill its progression responsibility in fifteen days, approve a specific day or ownership change.

## Sources and limits

- [Official Common Core ELA standards](https://corestandards.org/wp-content/uploads/2023/09/ELA_Standards1.pdf): checked the grades 9 to 10 requirements against the repository text.
- [Appendix A](https://www.oregon.gov/ode/educator-resources/standards/ELA/Documents/ela-appendix-a.pdf): read the text-complexity discussion and three-part model.
- [Current ELA criteria](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Review-Criteria.pdf) and [evidence guide](https://cdn.edreports.org/reviewtools/ela/2.0/ELA-Grades-6-12-v2.0-Tools_Evidence-Guide.pdf): checked complexity, pacing and research expectations; not a full rubric scoring.
- [Secondary-writing practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/22): checked its recommendations for explicit writing instruction and reading-writing integration.
- [New York Grade 10 curriculum map](https://unbounded-uploads.s3.amazonaws.com/attachments/15612/ela-grade-10-curriculum-map.pdf): compared its research stages and separate writing outcomes. Reference only; no material copied.
- [Louisiana unit progressions](https://doe.louisiana.gov/docs/default-source/teacher-toolbox-resources/ela-guidebooks-unit-progressions.pdf): compared high-school course organization. Not evidence that a particular Curio Class day allocation is sufficient.
- [Genome fact sheet](https://www.genome.gov/about-genomics/fact-sheets/Cloning-Fact-Sheet) and [FDA primer](https://www.fda.gov/animal-veterinary/animal-cloning/primer-cloning-and-its-use-livestock-operations): read to test the frame’s anchor descriptions.
- [Tagore’s *Mashi*](https://www.gutenberg.org/files/34757/34757-h/34757-h.htm) and [*Hungry Stones*](https://www.gutenberg.org/cache/epub/2518/pg2518-images.html): checked contents, editions and the two selected stories.
- [Digitized *Mhudi*](https://fynbosch.com/digitised-book-mhudi): checked edition provenance, chapter boundaries and opening passages. The complete novel was not reread.
- [Wheen’s *All Quiet*](https://www.gutenberg.org/cache/epub/75011/pg75011-images.html): checked edition information and the relevant sensitive passages. The complete novel was not reread.

The original Curio Class texts, exact anchor complexity, complete classroom reading load and lesson-level assessment quality remain unverified. This review does not certify every text’s rights.

**For the source list:** Add the working criteria and evidence-guide addresses above, the two exact cloning pages, the corrected Tagore editions, and the digitized *Mhudi* chapter index. The hashed criteria address in the repository did not open during this run; the direct document address did.

**Final disposition:** Revise before scope and sequence. **12 findings.** Requested report path: `docs/reviews/frame-english-language-arts-grade-10-2026-11-14.md`. Report delivered here; no file written.

