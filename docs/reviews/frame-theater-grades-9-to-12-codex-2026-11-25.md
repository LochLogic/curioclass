# Second-model frame read: Theater, grades 9 to 12

**Course:** `theater-grades-9-to-12`  
**Date:** 2026-11-25  
**Mode:** Read only. No files created, changed or deleted.

## Verdict

**Requires changes before scope and sequence writing.** Ownership, unit order and the full-year calendar are coherent, but several teaching and assessment instructions would produce incomplete standards coverage. Correct the meaning of “sustainable,” complete the evidence requirements, and repair placement and assessment delivery before handing this frame to writers.

**Findings: 7**, most serious first.

This differs from the “sound and buildable” verdict in `docs/reviews/frame-theater-grades-k-to-12-2026-11-25.md`: correct placement and arithmetic do not establish that each standard is taught and assessed in full.

## What was read and checked

- The complete target frame, its `course-list.csv` selector, its `frames.csv` entry and all 36 calendar rows.
- All 29 selected progression rows: `grade:9|10|11|12&strand:th`, including prerequisites, handoffs, models and notes.
- The theater ids and their corresponding words-file actions.
- The preceding theater frame’s relevant units, models and handoff tables. There is no subsequent theater course.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts adoption bar, arts `STANDARD.md` and `APPROACH.md`.
- Relevant foundation, shared approach, production-path, baseline, calendar, source and decision provisions.
- Earlier arts pre-work, progression and theater frame reviews.
- The outside sources linked below.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check theater-grades-9-to-12` | One failure: this frame-stage course lacks the day-plan files the command requires; review continued |
| `python -X utf8 scripts/frame.py check theater-grades-9-to-12` | Passed: 0 failures |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |
| Independent skill count | 29 selected skills, each placed exactly once |
| Independent owned-standard count | 72 ids, each placed exactly once: 24 per level in Levels 1 to 3 |
| Level 4 ownership | No new ids; all 24 Level 3 ids return |
| Independent day count | Each level: 156 unit days plus four course check/respond days, totaling 160 |
| Short-path arithmetic | Each level: 76 unit days plus four course check/respond days, totaling 80 |
| Stored calendar | Each level occupies school days 1 to 160 without gaps or overlaps |

Commands used `-B` to prevent bytecode writes. The plan check was course-filtered because repository instructions prohibit an unfiltered run; the gate wrapper was not run because it writes outputs and baselines.

## Findings

### 1. Unit 7 mistakes sustained performance for a play’s survival over centuries

**Severity:** Serious  
**LAYER:** standard, with progression and frame consequences  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Target frame, unit 7; `th-g10-story`; words-file entries for `TH:Pr4.1.IIa`, `TH:Pr5.1.IIa` and `TH:Pr5.1.IIIa`.

**Problem:** Unit 7 teaches what makes *Hagoromo* “lasting after six centuries” and checks what keeps a classic “alive.” The assigned performing standard concerns choices that sustain believable theater. The [South Dakota standards glossary](https://doe.sd.gov/contentstandards/documents/FineArts-051822.pdf), printed page 69, defines sustainable as consistency throughout the work. The [national high school standards](https://www.nationalartsstandards.org/sites/default/files/handbook_pdfs/handbook_1686070572.pdf), PDF pages 7 and 8, place this concept within performing and preparation.

**Why it matters:** A student could explain historical longevity without investigating whether performance choices remain consistent through a scene. The words-file substitution “lasting” encourages that error elsewhere.

**Exact fix:**

- Retain the historical question as context, but replace unit 7’s performing task with two contrasting stagings of the same excerpt. Students identify which distinctive choices remain believable and consistent throughout, and explain why.
- Replace its `TH:Pr4.1.IIa` evidence with an annotated observation record covering those choices across the excerpt.
- Replace that words-file line with: “Test distinctive choices that keep a drama believable and consistent throughout its performance.”
- Replace ambiguous “lasting” language in the two acting-preparation entries with “sustained throughout the performance.”
- Align `th-g10-story` and the relevant acting notes with this meaning. Keep all ownership unchanged.

### 2. Several evidence lines allow a partial performance of the standard to earn “met”

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete evidence requirements recur in the earlier theater band reads  
**Confidence:** Firm

**Location:** Units 4, 8, 10, 13 and 15, especially “End-of-unit evidence.”

The following omissions are confirmed against the [national theater standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance%20-%20new%20copyright%20info.pdf), particularly PDF pages 1, 3, 6, 7 and 8.

| Location | Problem | Exact fix |
|---|---|---|
| Unit 4, `TH:Re9.1.Ia` | “One tie to history **or** another art” permits the critique to omit culture and other disciplines. | Require evidence and criteria, with explicit consideration of another art, history, culture and another discipline. These may be concise connections within the existing critique. |
| Unit 8, `TH:Cr3.1.IIb` | The evidence accepts revision traced to research **or** script study, and omits bodily-response choices. | Require both sources of reasoning and observable revision of body, voice and bodily response, explained in the existing rehearsal log. |
| Unit 10, `TH:Cr3.1.IIa` | A concept **or** design change does not establish analysis of both. | Score separate rehearsal-log entries analyzing the concept and technical design, including a reason to change or retain each. |
| Unit 13, `TH:Cr1.1.IIIc` | The log accepts a historical **or** cultural choice. | Require historical and cultural context joined with the permitted personal or invented experience in the character choices. |
| Unit 13, `TH:Re8.1.IIIa` | The named evidence checks revision of the student’s work only. | Score the revision note and an interpretation of another person’s work, both supported by evidence and criteria. |
| Unit 15, `TH:Cr3.1.IIIa` | “Style, genre and form chosen and kept” omits conventions and evidence of transformation through rehearsal. | Add conventions and a before/after rehearsal note showing how the work was transformed or reimagined. |
| Unit 15, `TH:Pr6.1.IIIa` | Research from two roles is sufficient under the proposed look-for. | Require the production’s research and analysis to represent playwright, director, designer and dramaturg perspectives. Students need not personally hold all four jobs. |

**Why it matters:** These are explicit marking instructions. Writers could follow them faithfully and award complete coverage for incomplete evidence.

Apply the corrected requirements to their Level 4 returns as well. Keep the current units and ids.

### 3. The placement bar samples writing and response while leaving practical prerequisites untested

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm on the omission; likely on its placement consequences

**Location:** “Entry and placement,” units 6 and 11, and the Level 1 and Level 2 year-end checks.

**Problem:** Placement uses the previous level’s year-end check. Level 1’s sitting samples four ids; Level 2’s samples three. Neither checks acting technique, rehearsal revision or technical implementation. Unit 6 explicitly describes placement marks on the sampled ids, although subsequent units assume all eight preceding threads.

**Why it matters:** A student entering from outside could pass the written sample and immediately face practical work whose prerequisites have never been demonstrated.

**Exact fix:** Keep the year-end sitting as the written component. In the existing six-day placement units, add a practical component consisting of:

1. A short performed scene and character explanation.
2. A design solution demonstrated in a cued run.
3. A rehearsal record showing feedback and revision.
4. A source note supporting a production choice.

Use the preceding level’s existing guides, record readiness by thread, and provide the named reteach where evidence is missing. Replace “placement bar” with “written component of placement” in both year-end check rows. Preserve the three-day short-path placement unit by combining these components into one rehearsed scene and its accompanying record.

### 4. The showing timetable does not cover the promised participation and recording choices

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the grades 6 to 8 read identifies the same individual-evidence and recording-refusal problems  
**Confidence:** Firm

**Location:** “Scored evidence,” “Leave-out,” and units 3, 5, 8, 13 and 18.

**Problem:**

- The common timetable allows six groups of five, but unit 3 specifies paired character studies. Fifteen five-minute paired studies require 75 performance minutes, before the other 15 minutes already budgeted.
- Director, designer and stage-manager roles cannot by themselves establish owned acting evidence. The stated seated or recorded alternative addresses character units but does not explicitly preserve unit 5’s scripted-performance evidence.
- A group the teacher cannot observe live “is recorded.” Arts `APPROACH.md`, “Kept work,” expressly permits recording refusal and requires live observation instead.

**Why it matters:** Some students could receive a group mark without individually demonstrating the owned skill, or face recording as the only feasible completion route.

**Exact fix:**

- Add a student-by-id observation roster.
- Schedule final live observation rounds within the last rehearsal days, before response, for paired studies and any missing individual evidence.
- Keep the common showing day for the ensemble presentation; specify shorter excerpts or additional observation rounds where the unit uses pairs or individual roles.
- Require an individually observed scripted acting contribution for unit 5, with seated and supported ensemble versions available.
- Replace the compulsory-recording sentence with: “Recording is optional. A student who declines is observed live during a scheduled final observation round; the teacher’s mark is the evidence.”

These rounds must be counted on both full and short paths.

### 5. The early-departure path removes six days when it needs to remove ten

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** “Grade 12 calendar,” units 5, 10, 15 and 20, and the year-end checks.

**Problem:** Seniors leaving two weeks early finish on school day 150. The frame finishes on day 160 but permits only six fluency days to fold. That leaves four days unscheduled.

**Why it matters:** The promised senior path cannot deliver its remaining teaching, assessment and response within the stated attendance window.

**Exact fix:** State a ten-day consolidation path for affected seniors:

| Level | Final unit’s senior-path length | Final unit ends | Year-end check | Respond |
|---|---:|---:|---:|---:|
| 1 | 32 days instead of 42 | 148 | 149 | 150 |
| 2 | 35 days instead of 45 | 148 | 149 | 150 |
| 3 | 35 days instead of 45 | 148 | 149 | 150 |
| 4 | 23 days instead of 33 | 148 | 149 | 150 |

Replace “up to 6 days” with this allocation. Require the scope and sequence to identify ten consolidation days using the existing short-path principles, while preserving instruction, feedback, critique, revision, checks and response. This allocation is a planning judgment, not a tested delivery claim.

### 6. Required source links are absent from the frame

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier theater reads request exact safety-guide links  
**Confidence:** Firm

**Location:** “Base text,” “Safety read,” the Units table and “For the lead” item 3.

**Problem:** The frame contains no full source URLs. Named works point to unspecified company, university or archive pages; safety guides have bare domains. `frame-write.md` rules 22 and 23 require free source links at this layer.

**Why it matters:** Writers cannot reproduce the frame’s factual checks or reliably locate the intended production, cultural account or safety guidance.

**Exact fix:**

- Add a source appendix keyed to unit and work, recording the exact page, supported claim, access date and extent read.
- Replace the three bare safety domains with the exact links listed below.
- For unit 2’s Abbey history, use the [Abbey Theatre’s own history page](https://www.abbeytheatre.ie/about/history/), which confirms the 1904 opening and *Spreading the News*.
- Give other fixed selections equally specific primary-source links before they become writing inputs. If a source refuses automated access, follow the repository’s alternate-source and “browser check” rule.
- Update the live safety-source note to distinguish sources located or partly read here from the later specialist safety review.

This finding concerns traceability. It does not certify the proposed movement or technical exercises.

### 7. Living guidance retains obsolete status claims and a false no-repeat assurance

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, both issues appear in earlier arts or theater reviews  
**Confidence:** Firm

| Location | Problem | Exact fix |
|---|---|---|
| `ADOPTION-BAR-SUBJECTS.md`, arts row under “Before a scope and sequence” | It still owes the standards gate and loading 63 music strand ids. L83 is done and the ids are loaded. | Replace both owed clauses with: “NCAS membership checking and the 63 high school music strand ids were completed 2026-11-21.” |
| Target frame, “For the lead” item 2 | It says no lower-band maker repeats. Shakespeare appears in grades 3 to 5; Arena Stage appears in grades 6 to 8. | Replace the assurance with explicit revisit purposes: Shakespeare moves from character speech and stage directions to directing concepts; Arena Stage moves from venue design to the researched choices of *Sovereignty*. Name the earlier units in units 12 and 14. |

**Why it matters:** The first note can trigger duplicate work. The second presents a selection check as successful when it was incomplete. Neither requires removing the current works.

Preserve dated reviews as records.

## Lens checklist at frame level

| Lens requirement | Result |
|---|---|
| Levels separated from grade numbers | Met |
| Correct ids in each level | Met |
| All four artistic processes each year | Met |
| Technique taught directly and made harder | Present; sustainable-performance meaning needs finding 1 |
| Discipline words used in making and response | Met in the planned sequence |
| Student choice and a showing in every unit | Present |
| Critique follows a protocol and leads to revision | Met in the full-path design |
| Works span cultures, periods and living makers | Met in planned selections; source traceability needs finding 6 |
| Growth, self-assessment and kept work | Present; complete individual evidence needs findings 2 and 4 |
| Realistic sessions and assessment delivery | Needs finding 4 |
| Full and shorter schedules | Arithmetic holds; delivery changes must reach both paths |
| Equipment and safe-space controls | Named; specialist validation remains outstanding |
| Performing takes place with people | Met |
| Participation without compulsory solo performance | Present; evidence and recording choices need finding 4 |
| Tools support practice and do not judge performances | Met |
| Original assessment tasks rather than copied cornerstone tasks | No contrary provision found |
| Distinct theater learning | Met |
| Dance/PE and music/math duplication | Not applicable |
| Artistic responding distinguished from respond days | Met |
| Work suitability, detailed pedagogy and rights clearance | Later specialist checks; not established by this frame read |

## Calendar, seams and load

- **Full path:** Every level has a complete 160-day year. Stored calendar rows match the frame.
- **Checks:** Level 1 uses days 81/82 and 159/160. Levels 2 to 4 use local days 77/78 and 159/160. Week 32 is permitted for high school finals.
- **Load:** Level 1’s 12-day bridge and Levels 2 and 3’s six-day reviews meet the subject limits. The longer production units are defensible because they carry rehearsal and presentation work.
- **Short path:** All four 80-day totals add correctly. Arithmetic alone does not establish feasible individual observation or placement.
- **Incoming seam:** All eight grade 8 handoffs are answered. The bridge preserves entry without prior optional theater.
- **Outgoing seam:** Level 4 is terminal. Its five rows have no outgoing handoffs.
- **Cross-subject:** Selected rows contain no formal `cross_subject` lean. The frame supplies theater-specific research, writing and discussion supports, so no missing prerequisite ordering was established.
- **Base text:** None is claimed; a base-lesson source map is not applicable.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Retain unit order, ownership and full-year allocations | Placement, prerequisites and load support them | Target frame |
| Correct “sustainable” throughout the affected chain | Restores the performing action | Words file, progression notes, target frame |
| Complete evidence within existing units | No standard needs moving | Target frame and corresponding summaries |
| Add practical placement evidence within existing review days | Checks assumed readiness without extending the course | Target frame |
| Require individual observation and optional recording | Makes marking and access provisions executable | Target frame |
| Use the ten-day senior consolidation allocation | Fits the stated two-week absence | Target frame |
| Retain Shakespeare and Arena Stage as explicit revisits | Their later analytical purposes differ | Target frame |

## What is right and should not be touched

- Levels are determined by prior learning, with a complete entry course at Level 1.
- All selected skills and owned ids are placed once.
- Research, acting, design, response and production form a coherent recurring sequence.
- Cultural study restrictions, invented alternatives for personal disclosure, paper access and adult-student consent are explicit.
- Course-level checks sample earlier work and carry recent production records unscored.

## What could not be judged

No scope, unit plans, task cards, scoring samples or day materials yet establish actual delivery. The complete rights status and suitability of every selected work, the Suzuki-based exercise, and the feasibility of compressed paths need their later specified reads.

No substantive finding rests on model memory. Existing safety controls remain marked “from memory” pending the dedicated safety read; proposed timing arrangements are reviewer judgments.

## Sources and use

- [National theater standards, at a glance](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance%20-%20new%20copyright%20info.pdf): full actions and level distinctions.
- [National high school theater handbook](https://www.nationalartsstandards.org/sites/default/files/handbook_pdfs/handbook_1686070572.pdf): cross-check of performing and assessment requirements.
- [South Dakota fine arts standards glossary](https://doe.sd.gov/contentstandards/documents/FineArts-051822.pdf): the technical meaning of sustainable.
- [Educational Theatre Association opportunity-to-learn standards](https://schooltheatre.org/wp-content/uploads/2022/02/Opportunity-to-Learn-Standards-EdTA_2022.pdf): high school scheduling and rehearsal guidance, especially PDF page 19.
- [Montgomery County school theater safety handbook](https://www.montgomeryschoolsmd.org/siteassets/district/departments/facilities/safety/drama-and-theater-safety-handbook.pdf): source located and introductory supervision, training and housekeeping provisions read.
- [Play It Safe school theater manual](https://actsafe.ca/department/live-events/play-safe-safety-school-theatre-studios-manual/): landing page and manual scope checked; full manual not reviewed.
- [Art and Craft Safety Guide](https://www.cpsc.gov/Safety-Education/Safety-Guides/hobbies/art-and-craft-safety-guide): official guide location checked; guide contents not reviewed.
- [Abbey Theatre history](https://www.abbeytheatre.ie/about/history/): unit 2’s founding and opening-production facts.

### For the source list

Record the exact links above, their uses and their reading limits in `docs/APPROACH-SOURCES.md`. The theater association’s high school scheduling section gives an academic-class comparison rather than a numeric weekly target.

## For Cory

- The frame proposes an optional supplies ceiling of **$150 per class of 30 per level**, with free alternatives retained. This remains the frame’s unresolved money decision.

