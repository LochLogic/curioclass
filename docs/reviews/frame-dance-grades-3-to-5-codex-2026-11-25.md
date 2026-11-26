# Independent frame review: Dance, grades 3 to 5

Date: 2026-11-25  
Course: `dance-grades-3-to-5`  
Read-only review. No files changed or report file created.

## Verdict

**Revise before writing the scope and sequence.** The band structure, ownership, unit reasons and annual totals are sound, but several standards lose required actions, and some participation alternatives can award performance marks without evidence of the student's performance. Restore those actions and their evidence first, then resolve the assessment and shorter-path timing conflicts.

**Finding count: 10.**

This differs from the earlier combined dance review's “light fix pass” verdict. Direct comparison with the national standards identifies substantive omissions that checking code placement cannot detect.

## What I read and checked

- The complete course frame, its `course-list.csv` selector and `frames.csv` entry.
- All 24 progression rows selected by `grade:3|4|5&strand:da`, plus the eight grade 2 and eight grade 6 seam rows.
- The preceding and following dance frames' seams, models, unit arrangements and relevant receiving or sending units.
- The national dance standards and corresponding repository words-file lines.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, and the arts adoption bar.
- Applicable foundation, production-path, baseline and decision guidance; arts pre-work, progression and earlier dance reviews.
- Relevant science, ELA, health and physical education unit contacts.
- The course's calendar rows and other courses' check weeks.

There is no base text, so a base-text source map is not applicable.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check dance-grades-3-to-5` | Failed because the plan-stage assessment files do not exist yet. Review continued. |
| `python -X utf8 scripts/frame.py check dance-grades-3-to-5` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** Unmarked stale statements remain. |
| Independent ownership comparison | All 24 selected rows placed exactly once; unit standards match their rows; 63 ids, 21 per year. |
| Annual allocation | Each year has 60 unit sessions, two course check sessions and two course respond sessions: 64 total. |
| Calendar comparison | All six course checks avoid the corresponding core check weeks. |

The aggregate repository gate was not run because it writes result files and baselines, contrary to the read-only restriction.

## Findings, most serious first

### 1. Several owned standards lose required actions

**Severity:** Major  
**LAYER:** standard, propagated into progression and frame  
**REPEAT:** yes, incomplete standards paraphrases and evidence recur in the earlier arts and dance reads.  
**Confidence:** firm.

**Location:** Units 1, 2, 5, 6, 7, 9, 10 and 12; corresponding progression notes and words-file entries.

Every id appears in its unit's learning cell, but appearance does not establish full coverage. These corrections belong inside the existing ownership and units.

The following omissions were checked against the [national dance performance standards](https://www.nationalartsstandards.org/sites/default/files/Dance%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

| Unit and id | Problem | Exact fix to teaching and evidence |
|---|---|---|
| 1, `DA:Pr4.1.3b` | Timing is reduced to staying with accompaniment. | Add timing with and against accompaniment, plus metric and movement-led phrasing, to the improvisation and its look-fors. |
| 2, `DA:Cr1.1.3a` | One chosen starting point replaces experimentation across sources. | Try movements from at least two self-chosen sources; retain both trials before choosing. |
| 5, `DA:Pr4.1.4a` | Filled and empty space disappear. | Include both in fixed and moving shapes, with an observed look-for. |
| 5, `DA:Pr4.1.4b` | One drum part replaces varied percussion. | Have each child accompany dancers using at least two safe percussion sounds or instruments. |
| 9, `DA:Pr4.1.5a` | Relationships use eyes only. | Add another body part's focus and score the relationship demonstrated. |
| 9, `DA:Pr4.1.5c` | Torso **or** limbs and general energy analysis narrow the action. | Require both origins; demonstrate and explain how initiation changes energy. |
| 7, `DA:Re9.1.4a` | The assessment is written only. | Add a movement demonstration applying the student's artistic criteria. |
| 12, `DA:Pr6.1.5b` | Selection replaces exploration. | Trial two production choices before selecting one for both spaces; retain the trial record. |

Further technique omissions are corroborated in the [California dance standards, PDF page 47, printed page 36](https://www.cde.ca.gov/BE/st/ss/documents/caartsstandards.pdf#page=47).

| Unit and id | Problem | Exact fix |
|---|---|---|
| 1, `DA:Pr5.1.3c` | “Coach” does not establish teacher feedback. | Name a teacher comment and the student's self-check on the recall card; show the resulting improvement. |
| 5, `DA:Pr5.1.4b` | Strengthening replaces the broader technique requirement. | Add movement-range and endurance work to instruction and observed evidence. |
| 5, `DA:Pr5.1.4c` | External cues and a group goal replace part of the action. | Add dancers cueing one another and an individual feedback-linked goal. |
| 9, `DA:Pr5.1.5b` | Explanation stops at injury prevention. | Extend the invented-dancer response to strength, flexibility and endurance; observe safe practice during movement combinations. |
| 9, `DA:Pr5.1.5c` | The ensemble's goal replaces personal goals. | Keep ensemble rehearsal and add one feedback-linked goal for each student. |

The connecting tasks also omit distinct work:

| Unit and id | Problem | Exact fix |
|---|---|---|
| 6, `DA:Cn10.1.4b` | Researching facts replaces developing a question; another expressive form is absent. | Each group writes its research question, investigates it through the existing sources, makes its dance, and explains how the topic could be expressed through another art form. Keep these on the research card. [Grade 4 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30335) |
| 10, `DA:Cn10.1.5b` | Research covers science facts, without studying another art form's treatment of the topic. | Add a sourced example from another art form, record how it expresses the chosen topic, and explain the group's dance choices before comparing learning processes. [Grade 5 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30336) |
| 10, `DA:Cn10.1.5a` | Feelings and viewpoints are named without explicitly relating movement to them. | Add one movement example from each dance explaining its relationship to the theme, viewpoint or experience. [Grade 5 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30336) |

Update the affected words-file lines and progression notes alongside the frame, using original concise wording. Retain all existing owners and unit placements.

**Why it matters:** Otherwise, the scope writer can follow the frame faithfully while teaching and assessing less than the owned standards require.

### 2. Participation roles are treated as interchangeable performance evidence

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, finding 2 of the independent Dance K to 2 review.  
**Confidence:** firm.

**Location:** “Taking part without dancing alone,” lines 130 to 134.

Seated and one-limb versions can provide accessible movement evidence. A caller or stage manager, however, does not automatically demonstrate the movement, timing or spatial action being assessed.

The [dance inclusion guidelines](https://nationalartsstandards.org/sites/default/files/Dance_resources/Dance%20Inclusion%20Guidelines.pdf) support individualized goals, accommodations and multiple ways to express learning. They do not establish blanket equivalence between participation roles and performance outcomes.

**Exact fix:** Replace the blanket marking sentence with:

> Each unit maps the student's accessible movement version to its performance look-fors. Caller, drummer and stage-manager roles establish only the outcomes directly demonstrated. Where a role supplies no evidence for an owned movement action, the teacher collects an accessible movement demonstration with the student's usual supports and records the accommodation.

Preserve partner, seated, supported and live-observation options.

**Why it matters:** The record must distinguish participation from demonstrated mastery.

### 3. Whole-unit leave-outs leave later units without their required material

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, finding 3 of the independent Dance K to 2 review.  
**Confidence:** firm.

**Location:** “Leave-out,” lines 153 to 159; units 3 to 4, 7 to 8, and 10 to 12.

The frame says each unit stands alone, but units 4 and 8 revise and stage the preceding unit's dance. Unit 11 selects material from unit 10, and unit 12 revises unit 11's study. The existing retrieval provision addresses earlier-year learning, rather than missing same-year products.

**Exact fix:** Add to Leave-out and the receiving unit rows:

> If an earlier unit was omitted, the receiving unit supplies a neutral Curio Class original phrase or a fresh making prompt. Learning or making that material is counted inside the receiving unit before feedback, revision and assessment. Omitted-unit ids remain unclaimed.

Name the fallbacks explicitly:

- Units 4 and 8 receive a short original study to revise and stage.
- Unit 11 supplies neutral movement material when unit 10 was omitted.
- Unit 12 supplies a short original study when unit 11 was omitted.

**Why it matters:** Exercising the settled leave-out choice must leave the remaining course usable.

### 4. Course checks immediately reassess newly completed units

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the assessment-sampling problem is already addressed in frame-write lesson 20.  
**Confidence:** firm.

**Location:** Course-level checks table, lines 324 to 329.

The table carries recent unit records unscored, but also gives newly scored tasks from that same recent unit. Examples include unit 2's challenge at the grade 3 mid-year check and unit 11's altered-tools study at the grade 5 year-end check.

**Exact fix:** Keep recent-unit records unscored and make these substitutions:

| Check | Newly scored evidence |
|---|---|
| Grade 3 mid-year | Unit 1 recall and timing; use unit 2's existing records unscored. |
| Grade 4 mid-year | Unit 5 balance and coordinated cue response; use unit 6's records unscored. |
| Grade 5 mid-year | Unit 9 phrase recall and ensemble timing; use unit 10's records unscored. |
| Grade 3 year-end | Replace unit 3's traditions item with unit 2's relationship comparison. |
| Grade 4 year-end | Replace unit 7's altered-tool study with unit 6's movement challenge. |
| Grade 5 year-end | Replace unit 11's altered-tools study with unit 10's source-derived movement material. |

**Why it matters:** The cumulative checks should add evidence about retained learning and inform response, rather than repeat the assessment just completed.

### 5. The course-check session exceeds 40 minutes

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, finding 7 of the earlier combined dance review.  
**Confidence:** firm on the arithmetic; judgment call on the proposed allocation.

**Location:** Days bullet, course-check bullet and lines 331 to 334.

The stated components total **43 minutes**:

`3 setup + 5 warm-up + 10 written + 18 showings + 4 cool-down + 3 reset`.

**Exact fix:** Replace the course-check timing with this 38-minute allocation, leaving two minutes of contingency:

| Component | Minutes |
|---|---:|
| Setup | 3 |
| Warm-up | 5 |
| Written component, including presentation of the prompt | 8 |
| Six group turns, 2.5 minutes each | 15 |
| Cool-down | 4 |
| Reset and collection | 3 |

Limit the showing component to two focused look-fors per student. Mid-year checks without written items may use that eight-minute block for additional observation.

**Why it matters:** A teacher following the current prescription must overrun or silently remove a component.

### 6. Unit 12's five-session shorter path conflicts with its required sequence

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the same merge problem appears in finding 5 of the independent Dance K to 2 review.  
**Confidence:** firm.

**Location:** Once-a-week path, Day kinds, Scored evidence and unit 12.

Unit 12 requires demonstration, critique, next-day revised rehearsal, two showing days and a respond day. That is six sessions under the general sequence, but its shorter path receives five.

**Exact fix:** State this exception explicitly:

| Session | Unit 12 work |
|---|---|
| 1 | Study the works, demonstrate staging adaptations and begin adapting the dance. |
| 2 | Continue adapting, critique, revise and rehearse the changes within this session. |
| 3 | First-venue showing and assessment. |
| 4 | Second-venue showing and assessment. |
| 5 | Respond to the assessment. |

Add:

> On unit 12's merged path, revised rehearsal follows critique within session 2. The next-day rehearsal statement describes the full path.

**Why it matters:** The scope writer otherwise has to drop, combine or add a session without authority from the frame.

### 7. Opening retrieval and feedback routines have inconsistent placements

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, first-use placement is a recurring frame-read finding.  
**Confidence:** firm.

**Location:** Days, Readiness and retrieval, Models carried, and units 1 to 4.

The warm-up receives about five minutes, but retrieval takes ten minutes inside it. Grade 3 unit rows additionally promise each of two assumed threads its own ten-minute reteach. Separately, every unit uses describe, ask, suggest feedback, while the models table first places `feedback-loop` in unit 4.

**Exact fix:**

- Give day 2 a separate ten-minute combined retrieval block.
- Replace separate thread-by-thread reteaches with one ten-minute integrated reteach when needed.
- State day 2's allocation: setup 3, warm-up 5, retrieval 10, teaching or integrated reteach 15, cool-down 4, reset 3.
- Change `feedback-loop` to “first used and modeled in unit 1's critique; applied to the owned revision standard in unit 4.”
- Make the corresponding unit 4 rationale say the model is developed there, rather than first introduced.

**Why it matters:** The next writer needs an executable opening and a consistent account of when students learn the feedback routine.

### 8. Work selections and source links remain unfinished

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, named picks and sourced facts are recurring frame requirements.  
**Confidence:** firm.

**Location:** Base text, Safety read and the Units table's works cells.

The frame contains no direct web links. Several selections remain “the unit plan picks,” including the Acogny solo, Pilobolus piece, Dancing Earth work, kathak solo and several cultural performances. These choices determine whether the proposed comparison, cultural boundary and visible technique actually work.

**Exact fix:** Complete a work register in the frame fix pass, with one row per studied work:

`Unit | Exact work or excerpt | Maker or named practitioner | Place and date | Direct institutional or community source | Feature studied | Watch-only or movement use`

Replace each deferred pick with its identified selection. Link each existing named work's supporting page. Keep item-level rights verification in the unit plan, as APPROACH requires.

For the Safety read, replace bare domains with direct links to the [Nova Scotia safety guide](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf) and [dance opportunity-to-learn standards](https://nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf). The former's dance section is printed page 43.

**Why it matters:** The scope writer should not inherit unresolved anchor choices or have to reconstruct the evidence behind cultural and historical claims.

### 9. Referenced assessment dates consume the unit's respond day

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new.  
**Confidence:** firm.

**Location:** Course-level checks table and lines 335 to 336.

The frame includes a respond day inside each unit, but calls the unit's final two days its assessment records. For example, unit 2 ends on day 32: days 31 and 32 cannot both be check days followed by an included respond day.

**Exact fix:** Correct the cited windows:

| Unit | Check days | Respond day |
|---|---|---|
| 2 | 30 and 31 | 32 |
| 3 | 48 and 49 | 50 |
| 6 | 94 and 95 | 96 |
| 7 | 112 and 113 | 114 |
| 10 | 160 and 161 | 162 |
| 11 | 176 and 177 | 178 |

Replace the closing explanation with:

> For units with two check days, those checks occupy the third-last and second-last unit days; the final unit day responds to their marks.

**Why it matters:** The total is recoverable, but the current instructions assign incompatible jobs to the same day.

### 10. Unmarked notes still describe completed work as outstanding

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier combined dance and arts reviews identified stale notes.  
**Confidence:** firm.

**Exact fixes:**

| Location | Replacement or action |
|---|---|
| Frame For the lead, item 2 | Delete the requested replacement for PE's pending cell. Its If later cell already contains that replacement. Retain only the remaining request to make its middle-cell row ids consistent. |
| Frame Standard bullet and For the lead, item 3 | Replace the historical seven-row correction request with the specific remaining standards corrections in finding 1. Do not leave the actionable changes solely in an earlier writer's chat message. |
| Frame For the lead, item 4 | Replace the unperformed national-text check request with: “The independent national-text comparison was completed 2026-11-25; its remaining corrections are listed in the second-reader report.” |
| Frame Base text, PE dance list | Replace tinikling with PE's current dance choices: Virginia Reel, Alunelul, La Bastringue and its original line dance. Pilolo is listed there as a game. |
| Preceding dance frame, Handed on section | Replace “The grade 3 to 5 frame is not written yet” with “The grade 3 to 5 frame is written; its receiving units match the handoffs below.” |
| Arts row of `ADOPTION-BAR-SUBJECTS.md` | Replace the outstanding standards-gate and music-strand loading tasks with their completed status already documented in arts `STANDARD.md`. |

Shared-file corrections belong to the lead. Preserve dated earlier reports as records.

**Why it matters:** Stale instructions send subsequent workers back to completed tasks and obscure the corrections still needed.

## Lens checklist

Statuses concern the frame's commitments, rather than unwritten lessons.

| Lens requirement or error check | Status |
|---|---|
| Correct grade ids in each band year | **Met:** 21 per year. |
| All four artistic processes each year | **Met.** |
| Technique taught directly and increasing in difficulty | **Partly met:** finding 1 restores missing actions. |
| Discipline words used in making and responding | **Met.** |
| Student choice, original work and showing in every unit | **Met.** |
| Structured critique followed by revision | **Partly met:** findings 6 and 7. |
| Several cultures and periods, including living makers | **Met as planned range;** selections need finding 8. |
| Maker, time, place and purpose supplied | **Partly met:** descriptions are substantial, but source links and some selections are missing. |
| Performance, response, self-assessment and kept work | **Partly met:** findings 1, 2 and 4. |
| Substantive arts assessment rather than vocabulary alone | **Met.** |
| Realistic frequency, session time and shorter path | **Partly met:** findings 5 to 7. |
| Equipment, space and hazards identified | **Met at frame level;** detailed safety read remains required. |
| Performing happens with people | **Met.** |
| Dance remains distinct from PE | **Met in the stated division;** later PE instruction is not assumed. |
| Five disciplines remain distinct | **Met.** |
| No copied cornerstone tasks or coalition explanatory text | No such copying identified in the frame. |
| No compulsory solo performance | **Met.** |
| Respond days distinguished from responding to art | **Met.** |
| Software does not judge finished performance | **Met.** |

Daily execution, exact equipment use and completed safety reads are not yet applicable.

## Calendar, allocation and seams

- Grades 3 and 4 allocate **16 + 16 + 16 + 12 = 60** unit sessions. Grade 5 allocates **17 + 17 + 14 + 12 = 60**. The additional grade 5 time for ensemble rehearsal and source-based making has a defensible reason.
- Each shorter path totals **28 unit sessions plus four course check and respond sessions**. Its arithmetic holds; unit 12 needs the explicit merge in finding 6.
- Course checks occur in weeks **17 and 26** for grades 3 and 4, and **18 and 26** for grade 5. These match the calendar rows and avoid core course checks.
- Science and ELA contacts are available at the stated times, or have a suitable fallback. The maps and beat counts do not assume later mathematics.
- All eight grade 2 handoffs and eight grade 6 pickups match the progression and adjacent frames. Finding 1 concerns the completeness of what is handed on, rather than mismatched row ids.
- After-core collisions are more extensive than the frame's PE-only note. Week 17 overlaps other arts checks in grades 3 and 4; week 18 overlaps several after-core checks in grade 5; week 26 has several overlaps in every grade. These remain for the lead's calendar pass, as the after-core brief directs, and are not counted as course findings.

The frame correctly reports its 80-minute full path and 40-minute shorter path against the published 90-minute weekly recommendation for grades 3 to 5. [Dance opportunity-to-learn standards, PDF page 12](https://nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf#page=12)

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Keep the 12 units, owners and annual totals | Placement and load reasons hold. | Course frame |
| Restore omitted actions inside existing units | Completes current ownership without moving standards. | Frame, progression notes, words file |
| Map accessible evidence by outcome | Participation roles cannot establish every performance action. | Frame and later assessment directions |
| Supply neutral material after leave-outs | Makes receiving units usable while omitted ids remain unclaimed. | Frame and later unit plans |
| Sample earlier learning at course checks | Avoids immediate repeat scoring of the recent unit. | Course-level checks table |
| Keep warm-up time; shorten and focus course-check tasks | Produces a session that fits 40 minutes. | Frame |
| Merge unit 12's critique and revised rehearsal in session 2 | Preserves both venue assessments and response in five sessions. | Frame |

## What is right and should not be touched

Preserve the annual four-unit pattern, pairing of research with ideas, pairing of revision with staging, all four artistic processes, explicit evidence labels, live teacher judgment, portfolio growth record, free paper path, invented alternatives to personal disclosure and the cultural watch-only boundaries.

## What I could not judge

This review does not establish the suitability, rights or accuracy of every proposed excerpt or cultural description. It does not certify safety or demonstrate that the proposed observation schedule works with 30 children in practice.

No finding relies on personal memory. The frame's safety prescriptions remain explicitly **from memory** pending the promised source-based safety read.

## Sources

- [National dance performance standards](https://www.nationalartsstandards.org/sites/default/files/Dance%20at%20a%20Glance%20-%20new%20copyright%20info.pdf): primary comparison for owned actions.
- [California arts standards](https://www.cde.ca.gov/BE/st/ss/documents/caartsstandards.pdf): corroboration of technique requirements.
- [Grade 4 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30335) and [grade 5 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30336): corroboration of omitted research and expression requirements.
- [Dance inclusion guidelines](https://nationalartsstandards.org/sites/default/files/Dance_resources/Dance%20Inclusion%20Guidelines.pdf): individualized access and evidence.
- [Dance opportunity-to-learn standards](https://nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf): weekly-time figure and its stated gap.
- [Nova Scotia physical education safety guide](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf): verified the named guide and located its dance section; detailed safety evaluation remains outstanding.

**For the source list:** Add or cross-reference the inclusion guidance and direct safety-guide address if absent.

## For Cory

- The existing optional filmed-phrase proposal remains a people and money decision. These corrections do not require filming.
- The proposed supplies ceiling of **$50 per class per year** remains a money decision. Preserve every free alternative.

No new course-scope or audience decision is needed for these fixes.