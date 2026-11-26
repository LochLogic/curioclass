# Independent frame review: Social and Emotional Learning, Grades K to 2

Date: 2026-11-25  
Course: `social-and-emotional-learning-grades-k-to-2`  
Read only. No files were changed.

## Verdict

The frame has a sound instructional foundation: all 120 selected progression rows are placed exactly once, the three years differ in depth, and rehearsal, invented cases and family activities are built into every year. It needs revision before scope writing because its fall and spring checks replace the required mid-year and year-end checks, several owned standards remain partial, and the leave-out rule lacks a workable kindergarten fallback. The most important change is to settle a calendar that preserves complete annual teaching and genuine course-level checks.

**Eight findings:** three serious, three moderate and two minor.

## What I read

- The frame-read brief and the after-core provisions of frame-write; EXPERT.md; the SEL lens; FOUNDATION.md; relevant APPROACH, PRODUCTION-PATH and BASELINE provisions.
- ADOPTION-BAR-SUBJECTS.md: shared requirements, part 9 and the SEL status row; SEL STANDARD.md and APPROACH.md.
- The complete course frame; its course-list selector, frames.csv entry and calendar.csv rows; CALENDAR.md.
- The 120 selected SEL progression rows, grade 3 receiving rows, sel-edges.md and the 40 standard statements.
- Relevant Units-table rows in the K to 2 ELA, mathematics and social studies frames; the health frame’s relevant units and cross-subject table; health’s disclosure instructions.
- Earlier SEL pre-work and progression reviews and their recorded fixes. Earlier frame reports were consulted for repeated finding types.
- Outside sources linked below.

Kindergarten has no preceding course. The grades 3 to 5 SEL frame does not yet exist, so the outgoing seam was checked against its progression rows.

## Checks and counts

The brief’s plan check was course-filtered to honor the repository instruction against unfiltered runs.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check social-and-emotional-learning-grades-k-to-2` | Failed because the course has no day-plan files yet; review proceeded |
| `python -X utf8 scripts/frame.py check social-and-emotional-learning-grades-k-to-2` | Passed, zero failures |
| `python -X utf8 scripts/stale.py check` | Passed, 70 files, zero failures |
| Targeted stale check on the frame, SEL standard, SEL approach and subject bar | Passed, zero failures |
| Independent placement count | 120 selected rows, 120 distinct placements, no missing or extra rows |
| Ownership | 40 owner rows in grade 2; kindergarten and grade 1 carry begun codes |
| Stored calendar | Matches 60 unit sessions plus two check and two respond sessions per year |
| SEL check weeks against same-grade core check weeks | No current clashes |

The structural pass establishes placement and arithmetic. It does not settle the findings below.

## Findings, most serious first

### 1. The frame replaces the required annual checks with earlier checks

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Frame, Days bullet, Course-level checks and For the lead 2.

Each year’s first check follows its second unit, in weeks 9 to 11. Its second follows its fifth unit, in week 26. The final unit then runs through week 32 without a course-level check afterward. Calling these “fall” and “spring” checks accurately describes them, but does not satisfy the after-core requirement for each year’s own mid-year and year-end checks.

This affects eight sub-skills in each final unit. Their unit assessments remain useful, but cannot substitute for the required annual assessment structure. Avoiding core check weeks is necessary; it does not authorize removing the year-end check.

**Exact fix:** Put the first check after units **3, 9 and 15**, and the second after **6, 12 and 18**, retaining a respond session for each. Rewrite the sampling cells around the revised positions without retesting just-taught material.

The lead must then resolve the calendar constraint explicitly. One feasible proposal preserves 64 sessions but finishes SEL in week 28 for K and grade 1 and week 27 for grade 2: eight weeks with three meetings in K and grade 1, ten in grade 2, and two meetings in the other teaching weeks. Mid-year checks can fall in week 13 and year-end checks in weeks 28, 28 and 27, respectively, without current core-check clashes. This changes the settled weekly pattern and belongs with Cory. Apply the same calendar reasoning to the 32-session path.

### 2. Complete placement masks partial treatment of owned standards

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, incomplete standard components recur in earlier frame reads, including the grade 3 to 5 fixes of 2026-11-13  
**Confidence:** firm for SA2 and SA5; likely for the RS3 owner-year concern

**Location:** Units 14, 17 and 18; progression rows `g2-sa-feel-think-link`, `g2-sa-my-strengths` and `g2-rel-different-ways`.

Three components need attention:

- **SA2, cultural and linguistic strengths:** strengths are generic. Welcoming a child’s voluntary contribution does not ensure that cultural or language strengths are taught.
- **SA5, feelings, values and thoughts:** the three-box strip links thoughts, feelings and actions, but omits what the character cares about.
- **RS3, working across cultures:** kindergarten and grade 1 introduce games from different places, but the grade 2 owner task substitutes picture lists versus word lists. That demonstrates different planning preferences without establishing cultural competence at the declared owner depth.

These distinctions appear in both the repository’s standard statements and the published [CASEL framework](https://casel.org/what-is-sel/). The concern is the planned teaching, not a requirement to collect children’s personal information.

**Exact fix:**

1. In unit 17, model an invented teammate whose language or culturally learned skill helps the group. Have students identify the contribution and explain how it helps.
2. In unit 14, add what matters to the character, such as fairness or belonging, to the thought-feeling-action case. Include an unseen item connecting that value to the character’s thought and feeling.
3. In unit 18, make the invented partner’s different approach explicitly grounded in a sourced cultural context. Students try or combine the approaches and explain the contribution. Keep personal sharing optional.
4. Amend the corresponding progression notes and evidence descriptions while retaining their current unit placements.

### 3. Kindergarten units cannot reliably survive an earlier unit being left out

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Days and Carry it out bullets; Inside the band; units 4 and 5.

The frame relies on a “Given:” readiness item when a school leaves out an earlier unit. That does not supply the missing teaching or model. In kindergarten there is also no previous-year SEL row to fall back on.

For example, leaving out unit 2 removes the feelings chart needed by unit 4 and the calm-down routine required by unit 5. Leaving out unit 1 removes the talk routine used in later partner work. A check can reveal these gaps, but cannot make the later unit runnable.

**Exact fix:** Add a leave-out bridge table identifying each later unit’s required incoming model and its fallback.

At minimum:

- Unit 4 supplies and models the pictured feeling clues it needs when unit 2 was omitted.
- Unit 5 supplies and rehearses “stop, breathe” before disagreement work when unit 2 was omitted.
- Later partner units supply the two pictured talk steps when unit 1 was omitted.
- Each receiving unit places its bridge within a named Understanding session and states what practice it replaces.
- Kindergarten readiness wording distinguishes new teaching from retrieval. Later grades use an earlier taught row only when that row was actually taught.

Keep the omitted unit’s coverage disclaimer. A brief bridge does not establish full coverage of that unit’s standards.

### 4. The three standards transferred from library remain outside the ownership record

**Severity:** Moderate  
**LAYER:** progression, frame  
**REPEAT:** yes, ownership and cross-subject coverage tracing recur in the earlier SEL reviews  
**Confidence:** firm

**Location:** Standard bullet, Library subsection and For the lead 4; the three grade 2 rows named below.

Library explicitly places three AASL standards in SEL. The frame acknowledges them, but their codes appear in neither the SEL progression’s standard cells nor the Units table’s Owned standards cells:

| Standard | Receiving owner row | Unit |
|---|---|---:|
| `AASL.V.D.1` | `g2-sm-stay-on-task` | 14 |
| `AASL.V.D.2` | `g2-sa-skills-grow` | 17 |
| `AASL.III.D.2` | `g2-rel-teamwork` | 18 |

Consequently, the clean placement check cannot verify this agreed responsibility. Simply adding the codes will also require validator support: SEL currently accepts only casel-5.txt.

**Exact fix:** Record these three codes on the stated owner rows and units, with their teaching and evidence. The lead should add narrowly scoped validator recognition and the agreed band ownership treatment for these transferred codes, without making SEL responsible for the rest of the AASL framework. Replace For the lead 4 with the resulting ownership statement after that work lands.

### 5. The health seam needs actual unit references and an agreed model

**Severity:** Moderate  
**LAYER:** frame, process  
**REPEAT:** yes, unresolved cross-subject seams and stale dependency notes recur in earlier frame reads  
**Confidence:** firm

**Location:** Health subsection, units 8 and 9, and For the lead 5.

The frame says no health unit numbers can be cited because those frames are being written. A health K to 2 frame and calendar now exist. They expose ordering differences:

| Health teaching | Current placement | Related SEL teaching |
|---|---|---|
| Kindergarten feeling words and calm routine | Health unit 3, weeks 14 to 18 | SEL unit 2, weeks 5 to 10 |
| Grade 1 choosing and asking for help | Health unit 7, weeks 5 to 10 | SEL unit 9, weeks 10 to 15 |
| Grade 1 goal setting | Health unit 9, weeks 18 to 22 | SEL unit 12, weeks 27 to 32 |
| Grade 2 limits and refusal | Health unit 14, weeks 13 to 18 | SEL unit 16, weeks 17 to 20 |

Thus, “health builds on SEL” is not a sufficient same-year rule. The I-statement wording and calm-tool menus also differ.

**Exact fix:** Replace the pending paragraph with these actual receiving units, course days and weeks. For each seam, state whether it uses an earlier-year routine, follows current-year SEL, or supplies its own introduction. Agree and record the exact shared pictured routine and wording before scope writing. Preserve health’s additional health-specific steps and ensure either optional course can run independently.

### 6. Carrying old unit records conflicts with the subject’s disposal rule

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Evidence bullet and every Course-level checks sampling cell; SEL APPROACH.md, Daily evidence.

The approach requires the teacher’s working class sheet to be discarded at the end of its unit. The frame repeatedly says a completed unit’s record is “carried unchanged” into a subsequent course check.

A teacher cannot follow both instructions. This is a record-handling contradiction, not evidence that a tracking system has been built.

**Exact fix:** Replace the carry-forward instructions with:

> The recent unit keeps its own assessment and response process. This course-level check records only its newly sampled evidence. Unit working sheets are discarded at the end of the unit, as SEL APPROACH requires.

Add the same disposal sentence to the Evidence bullet. If a course-level teaching summary is needed, define it as coverage and next teaching steps without individual children’s results.

### 7. The cultural-game choices need sources now, and the ritual claim is unsupported

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Base text bullet, units 5 and 11, Sensitivity reads and For the lead 10.

The frame names Ampe and jan-ken but postpones choosing sources. It also asserts that both have “no ritual meaning” without evidence. Frame-write requires named cultural cases to carry sources.

The basic choices are supportable: a [Ghanaian school’s firsthand account](https://www.tis.edu.gh/2017/05/19/service-in-action-myp-grade-7-8-engagement-with-calvary-presby-school/) describes Ampe, and [Web Japan’s account of traditional games](https://web-japan.org/nipponia/nipponia26/en/topic/) identifies jan-ken in children’s play. Neither establishes the absolute ritual claim.

**Exact fix:** Attach those sources to the respective units, identify the particular version the later page will describe, and delete “with no ritual meaning.” Retain the sensitivity read for context, representation and adaptation choices. Do not copy source wording or images without permitted reuse.

### 8. Living status notes still describe completed or superseded work as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier SEL progression finding 11 and multiple frame reads identify this type  
**Confidence:** firm

**Location:** ADOPTION-BAR-SUBJECTS.md SEL status row; SEL STANDARD.md introduction and section 2; frame For the lead 3 and 8.

The stale checker passes, but these unmarked notes remain:

- The subject bar still owes the progression, validator support and session-arithmetic decision, all completed in November.
- STANDARD still prohibits starting a frame, despite Cory’s 2026-11-25 authorization.
- STANDARD still describes separate grade-year frame files, although the current rule uses one band file with a Year column.
- The frame presents that band-file shape as needing reconciliation even though the governing brief and decision log already settle it.

**Exact fix:**

- Replace the bar’s owed clause with: “Progression and validator support completed 2026-11-21; session arithmetic settled in q-fix-sel-1. Pilot frame written 2026-11-25; frame reviews and reconciliation remain.”
- Replace STANDARD’s frame prohibition with the authorized distinction: frames proceed now; later production follows COURSE-RUN.
- Replace its frame-file description with one band frame, a Year column and a complete annual plan for each grade; scopes are written one year at a time.
- Remove the corresponding pending items from the frame after the living documents are corrected.

Do not rewrite dated review reports.

## Coverage, pacing and seams

| Year | Unit sessions | Course checks and responses | Total | Unit skill counts |
|---|---:|---:|---:|---|
| K | 60 | 4 | 64 | 5, 8, 5, 6, 8, 8 |
| 1 | 60 | 4 | 64 | 4, 6, 7, 8, 7, 8 |
| 2 | 60 | 4 | 64 | 6, 7, 6, 5, 8, 8 |

The heavier kindergarten units 2, 5 and 6 receive 12 sessions each. That follows the progression review’s load warning. No unit is clearly disproportionate merely by its row count.

The shorter paths add to 32 and retain all units. Their classroom feasibility remains to be demonstrated in the scopes, especially the single 20-minute sessions joining Check and Respond.

The cited core-course links either occur early enough or have an explicit SEL bridge. In particular, unit 15 correctly supplies its own oral perspective work before ELA’s later point-of-view unit. Grade 2 outgoing links match the grade 3 progression rows; the receiving frame remains unavailable.

## Lens checklist, frame layer

| Lens requirement | Judgment |
|---|---|
| Distinct cases and depth in each grade year | Met |
| Every selected sub-skill placed | Met structurally; full treatment needs finding 2 |
| Sub-skills return in practice | Partly specified through models, cues and checks; scopes must complete the return schedule |
| Minutes and shorter path stated; no units dropped | Met arithmetically |
| Carry-out cue and family activity per unit | Met |
| Units remain runnable after another unit is omitted | Missed, finding 3 |
| Self-management and relationships rehearsed | Met in the planned activities |
| Stable skill names and steps | Internal model progression is clear; health alignment needs finding 5 |
| Invented cases and optional personal sharing | Met |
| Checks score skills rather than feelings or traits | Met in the planned forms |
| Safe refusal and upstander roles | Met |
| Health topics handed to health | Met |
| Disclosure route and sensitive-topic notes | Met at frame level |
| Growth taught through practice and help | Met |
| Calming routines have plain physical framing | Met |
| No student identity sorting or compelled disclosure | Met |
| Cultural examples sourced | Missed, finding 7 |
| No public product names or unsupported effect claims | Required by the subject pages; public pages are not yet available |

## What is right and should not be touched

- Six distinct units per year and the complete 40-sub-skill annual sequence.
- Grouping related skills while preserving active rehearsal.
- Invented characters, optional sharing and private interest pages.
- Teacher or card roles for pressure, exclusion and unkind acts.
- Concrete school-day cues and family activities in every unit.
- The explicit bridge for ELA content taught later.
- Additional kindergarten practice time in the three heaviest units.

These choices align with the design principles in the [CASEL criteria paper, printed pages 23 to 25](https://files.casel.org/11_CASEL-Program-Criteria-Rationale.pdf) and the [EEF recommendations](https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/primary-sel/EEF_SEL_Summary_of_recommendations_poster.pdf): explicit instruction, active practice, connected sequencing and use beyond the dedicated session. That supports the design choices, not a claim of effectiveness for Curio Class.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Teach cultural and linguistic strengths through invented characters | Completes SA2 without requesting personal disclosure | Frame unit 17; corresponding progression note |
| Include what matters to the character in the feelings-thoughts case | Completes SA5 within its present unit | Frame unit 14; corresponding progression note |
| Keep unit working sheets temporary | Follows the approved SEL evidence rule | Frame Evidence and Course-level checks |
| Keep the later-ELA bridge in unit 15 | SEL’s oral task can stand independently | No change needed |
| Remove the absolute ritual claim | The sources establish play, not that universal assertion | Frame For the lead 10 |

## For Cory

1. **Calendar and instructional time:** choose a meeting-pattern adjustment that permits actual mid-year and year-end checks, or explicitly change the annual-check requirement. The current fixed weekly pattern cannot simply be retained while labeling the existing early checks as year-end checks.
2. **Money:** the provisional supply figures still need any intended ceiling for a class of 30. No spending decision was made in this review.

No new audience or outside-person decision is needed.

## What I could not judge

- Actual session timing, assessment throughput and combined Check/Respond feasibility before scopes and items exist.
- The receiving grades 3 to 5 frame, which is absent.
- Final Spanish accuracy, cultural illustrations, safety implementation and accessibility of unpublished pages.
- Effectiveness of this course. No study of it was reviewed.

## Outside sources and source-list follow-up

All sources below were checked live. No curricular finding rests on model memory.

| Source | Use and limit |
|---|---|
| [CASEL framework](https://casel.org/what-is-sel/) | Competency components, cultural and linguistic assets, and values |
| [CASEL criteria paper](https://files.casel.org/11_CASEL-Program-Criteria-Rationale.pdf) | Design provisions on grade sequences, practice and stated sessions; relevant pages consulted |
| [EEF recommendations poster](https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/primary-sel/EEF_SEL_Summary_of_recommendations_poster.pdf) | Explicit instruction, rehearsal, sequencing and everyday reinforcement |
| [Tema International School account](https://www.tis.edu.gh/2017/05/19/service-in-action-myp-grade-7-8-engagement-with-calvary-presby-school/) | Firsthand Ghanaian school description of Ampe; not a complete teaching guide |
| [Web Japan: Traditional Japanese Games](https://web-japan.org/nipponia/nipponia26/en/topic/) | Jan-ken in children’s games; no universal claim about ritual meaning |

For the source list: record these usable addresses and the CASEL framework redirect. The [Ghana curriculum teacher manual](https://curriculumresources.edu.gh/wp-content/uploads/2026/06/PEH-CORE-Teacher-manual.pdf) appeared in search, but its full fetch exceeded the tool’s size limit; it was not used as fully read evidence.

Prior workspace memory was consulted only for the report’s finding format.

