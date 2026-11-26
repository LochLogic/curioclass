# Independent frame review: Visual Arts, grades 9 to 12

Date: 2026-11-25  
Course: `visual-arts-grades-9-to-12`  
Read-only review. No files changed or report file created.

## Verdict

**Revise before writing the scope and sequence.** The four-level structure, progression ownership and annual allocations are sound, but placement and several Level 4 assessments do not establish the achievement they claim. Repair those evidence requirements first, then reconcile the safety instructions, alternate paths and calendar descriptions.

**Finding count: 9.**

## What I read and checked

I read the complete frame, its course-list selector, `frames.csv` entry, calendar rows, all 28 selected progression rows, the eight incoming grade 8 rows, and the relevant standards and words-file lines.

The governing reading included `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, the arts adoption bar, and relevant foundation, production-path, approach and decision guidance. I compared the preceding visual arts frame and the cited English language arts contacts. There is no following visual arts course and no base text, so a source map is not applicable.

Earlier arts reviews were consulted for repeat classification, particularly `frame-visual-arts-grades-3-to-12-2026-11-25.md`.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check visual-arts-grades-9-to-12` | One failure: later-stage `days.csv` and assessment tables are absent. This frame-stage limitation did not block the review. |
| `python -X utf8 scripts/frame.py check visual-arts-grades-9-to-12` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** Unmarked stale statements remain below. |
| Ownership comparison | All 28 selected progression rows occur exactly once. The 45 owned IDs are assigned to their correct levels. |
| Annual allocation | Each level has 156 unit days plus four course-level check/respond days. |
| Calendar comparison | Full-path calendar rows match the unit allocations. Several prose descriptions and short-path placements need correction. |

## Findings, most serious first

### 1. Level 4 names Advanced reassessment without requiring several of the assessed actions

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, incomplete assessment evidence recurs in the earlier arts reads; these Level 4 omissions were not identified there.  
**Confidence:** firm.

**Location:** Units 16 to 19, frame lines 272 to 275.

The tasks permit successful completion without demonstrating several IDs they explicitly reassess. Referring generally to the Level 3 guide does not resolve that mismatch: the proposal, essay, ethical account and exhibit must actually elicit the required evidence. The relevant actions are confirmed by the [national visual arts standards, PDF pages 1 to 8](https://www.nationalartsstandards.org/sites/default/files/2021-11/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

**Why it matters:** Level 4 is expressly the opportunity for a student who finished Level 3 at “partly” to demonstrate Advanced achievement. A generic independent project cannot establish the missing actions.

**Exact fix:** Add these mandatory requirements to the existing tasks and their evidence lines:

| Unit | Required addition |
|---|---|
| 16 | A social-change hypothesis; justified material/method and convention choices; revision using traditional and contemporary criteria alongside personal vision. |
| 17 | A comparison of shared features across a relevant group of works, even when the essay centers on one work. |
| 18 | Evidence of how cultural images or objects affect lives, and how social, cultural, historical and personal knowledge informs making. |
| 19 | Comparison of preservation methods; an intended social, cultural or political understanding for viewers; an evidence-based appraisal of an artist’s societal impact. |

Name the corresponding IDs beside these requirements. Keep the four units and existing ownership.

### 2. Placement can admit students without evidence of the practical prerequisites

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the earlier arts reads identify incomplete links between assessment and claimed achievement.  
**Confidence:** likely.

**Location:** “Levels, entry and placement”; units 6 and 11; course-level year-end checks.

Placement uses the preceding level’s year-end sitting. Those checks deliberately sample a few written/planning demands and carry product records **unscored**. For example, Level 2’s placement can establish start routes, a revision plan and interpretation without establishing the incoming student’s making, handling, collaboration or presenting skills.

**Why it matters:** A cumulative check can sample because a continuing student already has unit records. A new placement student may have no such record.

**Exact fix:** Keep the parallel sitting, but require a placement evidence checklist covering the preceding level’s creating, presenting, responding and connecting prerequisites. Accept existing work with a brief explanation; use targeted practical demonstrations where evidence is missing. Score that evidence against the preceding level’s guides during the review unit. State that the sitting alone does not authorize advancement.

This strengthens the existing placement rule without adding units or changing entry by level.

### 3. Unit 4’s solo alternative removes a required collaborative action

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the same general problem of an alternate task losing part of a standard occurs in earlier assessment findings.  
**Confidence:** firm.

**Location:** “The ordinary room,” lines 136 to 140; unit 4, line 260.

The ordinary-room rule offers a solo version with the same look-fors. Unit 4 repeats that promise, but its owned `VA:Cr2.3.Ia` requires collaborative proposal development. Working alone and naming one’s contribution cannot establish collaboration. [National visual arts standards, PDF page 2](https://www.nationalartsstandards.org/sites/default/files/2021-11/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

**Exact fix:** Specify that independent fabrication is allowed, while proposal development remains collaborative. A classroom partner or the existing home adult co-develops design choices; the log records both contributors’ ideas and one jointly resolved decision. Add that look-for to the guide. Remove the claim that a wholly solo proposal meets this ID in full.

### 4. The ventilation instruction accepts a control the named safety source rejects

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm.

**Location:** “Safety read,” approximately lines 161 to 169; dependent unit hazard instructions.

“Windows or a fan on for ink and acrylic” treats a fan as sufficient ventilation. The named federal guide expressly distinguishes fresh-air ventilation from simply circulating room air, which can increase exposure. [Art and Craft Safety Guide, PDF page 7, printed page 7](https://www.cpsc.gov/s3fs-public/blk_media_5015.pdf).

**Why it matters:** The frame says these controls will be copied into lesson data. Marking them “from memory” appropriately identifies uncertainty but does not prevent an unsafe instruction from propagating.

**Exact fix:** Replace the sentence with:

> Follow each material’s label and safety data sheet. Where ventilation is required, provide fresh air with contaminated air carried away from users. A circulating fan alone is insufficient. If the room cannot provide the required conditions, use the unit’s pencil or other suitable alternative.

Carry that wording into affected hazard cards. Retain the planned safety read.

### 5. Calendar descriptions conflict with both the full and short paths

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the full-path show-week discrepancy was identified in the earlier combined frame review; the short-path and prerequisite details below are additional.  
**Confidence:** firm.

**Location:** Short-path bullet; course-level checks and grade 12 bullets; Cross-subject table.

| Problem | Exact fix |
|---|---|
| The prose places curating units and shows in weeks 25 to 31. Units 5 and 19 actually end on day 158; units 10 and 15 span days 119 to 158. All extend into week 32. | State the actual spans: weeks 25 to 32, or 24 to 32. Give the showing’s exact day separately from the unit’s final day. |
| Level 4’s short-path units 16 and 17 total 39 days. Its check is day 40 and respond day 41, crossing into week 9 despite the promise that both fall in week 8. | Keep those allocations and explicitly state: “Level 4 checks on day 40, week 8, and responds on day 41, week 9.” Correct both short-path descriptions. |
| The senior rule promises a week 30 or 31 finish by folding at most five days. Five days shorten 160 to 155, which reaches week 31, not week 30. | State that a day-155 finish requires five merged days and a day-150 finish requires ten. Require the scope to number the senior calendar and retain showing, critique, revision, checks and response before claiming either finish. |
| The English contact says both cited units precede unit 17. Grade 11 English unit 3 ends on day 55, while art unit 17 begins on day 51. On the short path art begins still earlier. | Replace “Both units come before” with the actual overlap. Apply the existing essay-planner teaching fallback whenever the necessary English instruction has not occurred, on either path. |

No standards need to move.

### 6. The Level 1 mid-year check contradicts the dry-medium check rule

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, check-day materials and operating contradictions recur in the earlier combined review.  
**Confidence:** firm.

**Location:** Level 1 mid-year check, line 281; check-day operating paragraph, lines 290 to 294.

The check requires a “fresh unplanned ink task.” The operating paragraph prohibits ink and allows pencil or dry media. These are incompatible instructions for the writer and teacher.

**Exact fix:** Replace the task with:

> A fresh unplanned pencil drawing, with a short log of decisions made during drawing (`VA:Cr2.1.Ia`).

Keep the hazard-card and image-response items. This preserves the assessed action and the existing dry check-day arrangement.

### 7. The adult-student rule covers showing consent but omits leave-out decisions

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, adult-student consent wording was raised in the arts progression review; this remaining omission concerns leave-out choices.  
**Confidence:** firm.

**Location:** “Leave-out,” lines 131 to 135; “Grade 12 calendar.”

The showing provisions correctly recognize an adult student’s own consent. The leave-out provision assigns the choice only to “a school or family.” The supplied repository rule expressly gives students aged 18 or older their own family note and leave-out choice, subject to school rules.

**Exact fix:** Add to the Leave-out bullet:

> A student aged 18 or older receives the family note directly and makes their own leave-out and consent choices; the school’s rules still apply.

Keep the requirement to identify any IDs not claimed after a unit is omitted.

### 8. Unmarked stale notes still describe completed work as outstanding

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, the same notes were identified in the earlier combined frame review.  
**Confidence:** firm.

**Location:** Seams introduction, line 192; For the lead items 6 and 8; adoption-bar arts pre-work row, line 568.

| Stale statement | Current evidence | Exact fix |
|---|---|---|
| The grades 6 to 8 frame is unwritten. | That frame exists; its outgoing table matches the eight incoming threads. | Replace with: “These rows match the preceding frame’s handed-on table and the Level 1 progression rows’ assumptions.” |
| `va-g8-craft` still says “open licence.” | Its words cell now says “open license.” | Delete For the lead item 8. |
| The shared arts row still owes the standards gate and 63 music strand IDs. | `L83` is marked done; the standard documentation records the IDs as loaded. | Remove those two obligations from the living adoption-bar row, then remove the resolved lead reminder. |

The passing stale checker does not cover these unmarked statements.

### 9. The suggested day-kind template cannot fit the shortest paired unit

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, identified as minor finding m3 in the earlier combined review.  
**Confidence:** firm.

**Location:** “Day kinds,” approximately lines 88 to 94.

The minimum suggested allocation is 34 days: nine understanding, six fluency, fourteen application and five check/respond days. Unit 2 has 32 days. “Roughly” does not identify which category a scope writer should reduce.

**Exact fix:** Give a fitting 32-day example:

> Eight understanding days, five fluency days, fourteen application days, one mid-unit check and one respond day, two end-of-unit check days and one respond day. Longer units add days according to their making and research demands.

Keep critique and revision inside application.

## Lens checklist

| Frame-layer lens line | Result |
|---|---|
| Levels represent achievement, not student grade | Met |
| Four artistic processes in every level | Met in placement; Level 4 evidence needs finding 1 |
| Technique taught directly and made harder | Met |
| Discipline words support making and response | Met |
| Student choice and a showing in every unit | Met; collaboration alternative needs finding 3 |
| Critique routine followed by revision | Met |
| Works span cultures, periods and living makers, with settings | Met as a planned selection |
| Kept work, self-assessment and scoring guides | Met structurally; findings 1 and 2 address sufficiency |
| Feasible room, materials and session routines | Partly met; findings 4, 6 and 9 |
| Shorter schedule available | Met structurally; timing corrections in finding 5 |
| No forced solo performance | Met through group, wall and family showings |
| Artistic responding distinguished from respond days | Met, including the approved Level 4 checkpoint arrangement |
| Visual arts remains a distinct discipline | Met |
| Sacred works studied without imitation | Met as a planning rule |
| No copied coalition questions or cornerstone tasks identified | Met at this layer |

## What is right and should not be touched

- The paired threads, consistent level structure and increasingly independent work.
- The 12-day readiness bridge and six-day review units.
- The complete ownership mapping and separate annual checks.
- The id-by-id evidence lines, portfolio routine and distinction between scored evidence and carried records.
- The paper path, invented/public alternatives and contextual treatment of sensitive works.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Require the missing Level 4 evidence within existing units | Makes the stated reassessment demonstrable | Course frame |
| Supplement placement sittings with practical evidence | New entrants lack continuing students’ cumulative records | Course frame |
| Preserve collaboration while allowing independent fabrication | Retains access and the owned action | Course frame, unit 4 |
| Replace fan-only ventilation wording | Matches the named safety source | Course frame |
| Use pencil for the unplanned mid-year task | Fits the existing check-day rule | Course frame |
| Correct calendar prose, adult choice and stale notes | Aligns instructions with current data and rules | Course frame; shared adoption-bar row |
| Use the explicit 32-day template above | Fits the shortest paired unit | Course frame |

## For Cory

- **Money:** The proposed $150 ceiling per class per level remains a decision for Cory. The frame’s current estimates are $120, $125, $125 and $110, alongside free alternatives.
- **Scope:** Whether to support two levels taught in one period remains open. Keep the current separate level requirements until that decision.
- **Scope:** Any change permitting student blade use belongs in the governing arts approach after the safety read. This review does not request that change.

## Sources, limits and source-list follow-up

- [National visual arts performance standards, 2014](https://www.nationalartsstandards.org/sites/default/files/2021-11/Visual%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf): checked the high school actions behind ownership and assessment.
- [National high school achievement-level descriptions](https://www.nationalartsstandards.org/content/visual-arts-high-school-student-work): checked the achievement-based progression.
- [High school visual arts opportunity-to-learn standards](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-High_School_Visual_Media_Arts_Program.pdf): checked the pending scheduling source. It recommends regular instruction comparable to other academic subjects, with semester and other scheduling options; it supplies no universal weekly-minute minimum. Replace For the lead item 5’s request for a numeric gap with that verified description. Curio Class provides 225 minutes per meeting week and 120 or 60 total hours.
- [Federal Art and Craft Safety Guide](https://www.cpsc.gov/s3fs-public/blk_media_5015.pdf): checked ventilation, particularly PDF page 7.

**Could not judge:** Finished scoring guides, actual 45-minute task loads, individual artwork rights, every work fact, complete material safety, and the numbered senior schedules require the later plans and item-specific sources.

**Memory:** No finding depends on unverified subject-matter memory. Prior workspace memory informed review method only. Work facts and rights not independently checked here remain unverified.

**For the source list:** Record the directly accessible high school scheduling checklist and the federal guide’s ventilation page. The checklist’s lack of a numeric minimum resolves the frame’s pending source question without inventing a figure.

