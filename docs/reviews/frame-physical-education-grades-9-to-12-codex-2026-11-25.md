# Second independent frame read: Physical Education, grades 9 to 12

Date: 2026-11-25  
Report supplied in chat. No files changed.

## Verdict

The band structure is sound, but the frame needs correction before the scope and sequence is written. Its biggest risk is that placing all 43 indicators once conceals narrower teaching and assessment tasks in the required years. Preserve the four-year structure and calendar while making the required outcomes, assessment evidence and shortened ending explicit.

## What I read

- [Course frame](S:/CurioClass/docs/courses/physical-education-grades-9-to-12/frame.md), its `frames.csv` entry and all its `calendar.csv` rows.
- `frame-read.md`, `frame-write.md`, EXPERT, the PE lens, the PE adoption bar, STANDARD and APPROACH.
- The course-list selector, all 48 selected progression rows, the span-12 standards and the PE handoff notes.
- The preceding PE frame’s seams and relevant units. There is no subsequent PE course.
- The cited math grade 6, science grade 8 and social studies grade 6 units; health, dance and available SEL coordination material.
- Relevant PE decisions, pre-work and progression reviews, the K to 2 fix report, and the earlier grades 3 to 12 frame review.
- Outside sources linked below.

Memory supplied procedural review guidance only. No content finding rests on model memory.

## Gates and calendar

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check physical-education-grades-9-to-12` | One failure: day-level plan files do not exist. This is a frame-stage limitation. |
| `python -X utf8 scripts/frame.py check physical-education-grades-9-to-12` | Two failures, both file-only Pending markers for dance and SEL. See finding 6. |
| `python -X utf8 scripts/stale.py check` | Six failures: two here and four in other courses. Those other-course failures do not affect this verdict. |

The plan check was course-filtered because AGENTS.md prohibits an unfiltered run. `gate.py` was not run because it writes output and baseline files, contrary to this read-only assignment.

Independent counting confirms:

- All 48 selected skills appear exactly once.
- All 43 owned indicators appear once, in grades 9 and 10.
- Each year has 74 unit days plus six course-level check and respond days.
- The calendar agrees with the frame: mid-year checks in week 16; year-end checks in week 32 for grades 9 to 11 and week 28 for grade 12.
- The three cited core-course day ranges agree with the calendar.

## Findings, most serious first

### 1. Exercise principles are applied to only one activity

**Severity:** Serious  
**LAYER:** progression and frame  
**REPEAT:** yes, standards narrowed despite correct code placement, as in the pilot reads  
**Confidence:** firm

**Where:** Unit 6, line 307; progression row `g9-exercise-principles`.

The unit teaches and checks the principles through one chosen activity. The published indicator requires application across several self-selected activities. Elective work cannot complete a required-year omission. [2024 PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/)

**Exact fix:** In the progression note, unit 6 teaching statement and knowledge task, replace the single-activity requirement with two contrasting activities already taught, such as brisk walking and band strength training. Students apply overload, progression, specificity and reversibility to both and explain how their application differs. Keep the row in unit 6 and retain its 13 days.

### 2. Unit 9 lists broader outcomes than its concrete tasks deliver

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, standards-in-full findings in earlier PE reads  
**Confidence:** likely

**Where:** Unit 9, line 310.

The concrete historical case concerns sport, with no corresponding treatment of dance’s societal role. Leadership evaluation occurs in one game segment, while the owned indicator spans different activity settings. Individual problem-solving evidence is also unnamed. [2024 PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/)

This leaves the scope writer to invent missing content inside an already busy 11-day unit.

**Exact fix:** Within unit 9:

- Add a short historical social-dance case connecting unit 5’s dance to social gatherings, using the historical descriptions linked by [Library of Dance](https://www.libraryofdance.org/dances/sir-roger/).
- Have students evaluate leadership in both a warm-up and a game segment.
- Extend the existing assessment card with a historical-role explanation, an individual movement problem and a group problem with the adjustment tried.

Name these tasks in `What students learn` and `Ends`. Use existing case-work and leadership sessions rather than adding another performance day.

### 3. Grade 10 does not provide an activity choice in each term

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Where:** Unit 12, line 313; For the lead item 4.

The progression requires a different activity chosen and tried each term. Both choice blocks occur in unit 12, weeks 25 to 31. Grade 9’s log belongs to another year, and unit 10 also occurs after grade 10’s mid-year check. Neither supplies grade 10’s first-term choice.

**Exact fix:** Make one of unit 8’s existing aerobic sessions a student-selected activity block, with a private record of the choice, reason and experience. Label this preparation for `g10-choose-active-apply`, owned and completed in unit 12. Unit 12 retrieves that first-term entry and supplies a different second-term choice. Remove the claim that grade 9 or unit 10 stands for grade 10’s first term.

This preserves ownership, unit days and check weeks.

### 4. The senior short form drops a protected respond day

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, shortened-path arithmetic and protected assessment time  
**Confidence:** firm

**Where:** Grade 12 calendar, lines 163 to 167; unit 24, line 325.

The three-day short form keeps first teaching, drafting with feedback and the scored reflection. It omits unit 24’s respond day and does not explicitly place revision before scoring. The frame otherwise promises a respond day after every unit assessment.

**Exact fix:** Replace the three-day form with four sessions:

1. First teaching and baseline evidence.
2. Draft and written feedback.
3. Revision before scoring, plus the brief skill check.
4. Response to the assessment.

State that six of the ten days fold. For a student without grade 11, place the readiness check on grade 10’s reflection in the last ten minutes of the year-end respond day, before unit 24 opens.

### 5. Unit 12’s assessment does not explicitly cover its case, analysis and S3 conduct

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier review finding 6 on unit 12’s load, and the pilot’s assessment findings  
**Confidence:** likely

**Where:** Unit 12, line 313; Assessment bullet, lines 89 to 98.

Unit 12 owns 11 indicators in 16 days. Its assessment names the choice log, future plan, reflection and emotion strategy, but does not explicitly check the quality-of-life case or explain why an emotion strategy was selected. Its conduct mark concerns self-management rather than an S3 behavior, contrary to the stated course pattern.

**Exact fix:** Keep the rows and ownership in unit 12. Add to its existing knowledge task:

- A short case response explaining how activity could affect the person’s quality of life and early adulthood.
- A comparison of two emotion strategies, the reason for choosing one, and a brief judgment after using it.

Keep the observed emotion strategy as S4 evidence. Add a separate S3 review mark for supporting a partner’s chosen activity without ranking that choice. Identify these components in the draft, feedback and revision cycle already budgeted.

I would not move an owned row to another unit solely because this unit has many codes.

### 6. Dance is available, while SEL is only partly available

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, stale dependency notes in the pilot and earlier frame reads  
**Confidence:** firm

**Where:** Cross-subject introduction and rows, lines 373 to 387; unit 21’s teacher note.

The dance frame now explicitly names PE unit 5 and distinguishes motor learning from artistic performance and rehearsal. Its Pending marker is stale.

SEL needs different treatment. At inspection, its frame had 142 lines, an empty Units table and no calendar rows. Its models and planned handoffs existed, but its teaching weeks did not. The gate resolves a file-only marker as soon as the file exists.

**Exact fix:**

- Replace the dance Pending cell with its Level 1 unit 2 connection: days 13 to 50, weeks 3 to 10. State that dance supplies its own phrase and counts because it precedes PE unit 5, weeks 22 to 26.
- Replace “the dance and SEL frames are not written” with separate, accurate statements.
- For SEL, name the coping-plan model already defined, retain PE’s independent bridge, and use `Pending(docs/courses/social-and-emotional-learning-grades-9-to-12/frame.md#Course-level checks): confirm unit timing when the year plans are complete.`
- Remove unit 21’s blanket claim that the SEL frame is unwritten.

Do not invent SEL weeks from its seam table.

### 7. “Browser check” substitutes for source work that was not attempted

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, earlier frame review finding 7  
**Confidence:** firm

**Where:** Sensitivity reads, lines 178 to 184; units 5 and 9; For the lead item 3.

The frame says no page was opened, then assigns every cultural pick and historical fact to the lead as a browser check. AGENTS.md reserves that status for unsuccessful automated reads after an alternative source has been tried.

Several usable sources opened during this review.

**Exact fix:** Replace the blanket browser-check list with dated source lines:

- Dance formation and historical descriptions: [Library of Dance](https://www.libraryofdance.org/dances/sir-roger/).
- The 1896 revival and women’s later participation: [IOC history](https://www.olympics.com/ioc/history).
- The 1863 association rules: [National Football Museum](https://nationalfootballmuseum.com/items/the-laws-of-the-game-1863/). Say “the association’s rules were codified in 1863,” avoiding an unrestricted “first common rules” claim.
- Sepak takraw’s basic play: [ActiveSG](https://www.activesgcircle.gov.sg/learn/sepak-takraw/rules-and-regulations-of-sepak-takraw?tab=how_to_play). Label the classroom version as modified.

Retain the fresh sensitivity read. The Singapore heritage page presented a bot check and was not pursued another way; the ActiveSG alternative opened. The football association page timed out; the museum alternative opened.

### 8. Loaded-lift wording conflicts with the course’s stated exclusion

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier frame review finding 12  
**Confidence:** firm

**Where:** Unit 2, line 303; unit 14, line 315; course equipment rules.

Unit 2 excludes loaded lifts from the course, while unit 14 provides a spotter rule for them. A later writer could reasonably include loaded lifting in the elective.

**Exact fix:** Add one course-wide statement: “Curio Class sessions use body weight and resistance bands. Loaded lifting belongs to a school’s separately supervised weight-room program.”

In unit 14, replace the loaded-lift clause with that boundary. Keep equipment inspection, appropriate progression and medical adaptations. The linked [Nova Scotia safety guide](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf) supports adapting fitness activities to students, facilities and equipment.

### 9. Students are not offered a choice of competitive setting

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier frame review finding 10  
**Confidence:** firm

**Where:** Supports, lines 142 to 147; game units.

The frame prohibits public team picking and elimination but omits the subject rule allowing students to choose a more or less competitive setting.

**Exact fix:** Add: “Where competition fits the activity, students choose a cooperative practice setting or a more competitive small-sided setting; both teach and check the same cue.” Carry the choice into the game units’ settings.

### 10. The equipment totals do not match the unit cells

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, earlier frame review finding 11  
**Confidence:** firm

**Where:** Supplies and cost, lines 121 to 125; For the lead item 5.

The listed unit costs sum to:

| Year | Listed costs |
|---|---:|
| 9 | $535 |
| 10 | $185 |
| 11 | $0 |
| 12 | $20 |
| **Band** | **$740** |

The narrative instead gives $555, $205 and $780.

**Exact fix:** Replace those narrative totals with $535, $185 and $740. State separately that optional compasses add $120 and that the estimates remain provisional. If the missing $40 represents actual purchases, identify and cost them in the appropriate unit cells before retaining $780.

### 11. The Units header retains the core-subject label

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Where:** Lines 87 to 88 and Units header, line 300.

The after-core brief explicitly names this column `Cues and settings`; the frame retains `C3`.

**Exact fix:** Rename the table header and its explanatory bullet to `Cues and settings`. Keep the existing contents.

## Lens checklist

| Frame-layer lens line | Mark |
|---|---|
| Outcomes rather than a year of games | Met |
| Outcome for all four standards in every grade | Met |
| Every span indicator placed | Met mechanically; fullness needs findings 1, 2 and 5 |
| Skills precede complex application | Met |
| Dance and fitness return | Met through later choices and programs |
| Few cues at a time; skills before games | Met as a planning rule |
| Most students moving, without lines | Met as a subject rule; implementation remains untested |
| No punishment, elimination, human targets or public picks | Met |
| Choice of competitive setting | Missed, finding 9 |
| Disability, injury and skill adaptations | Met as a planning rule |
| Gender-neutral participation | Met |
| Cultural range and sourced claims | Partial, finding 7 |
| Private fitness measures, never grades or rank | Met |
| Skill, knowledge, conduct and growth evidence | Partial, finding 5 |
| Real space, weather and equipment alternatives | Met in outline |
| PE and health responsibilities distinguished | Met |
| PE dance and arts dance coordinated | Partial, finding 6 |
| Individual adapted plans and medical clearance | Not applicable; correctly assigned to the school |

## What is right and should not be touched

- The required grades 9 and 10, followed by two electives.
- Every selected progression row placed once, with later carries distinguished from ownership.
- Four self-contained years, each with its own checks and respond days.
- The grade 12 week-28 year-end check.
- Private fitness records, cue-based growth assessment, paper access and no student accounts.
- The preceding-band handoffs and the verified core-course calendar citations.
- Dry-land water safety, with in-water instruction assigned to the school’s aquatics program.

## Settled by the expert

| Choice | Reason | Location |
|---|---|---|
| Two contrasting exercise-principle applications | Completes the required indicator without moving ownership | Unit 6 and progression note |
| First-term choice inside existing unit 8 sessions | Meets the progression’s term requirement without moving checks | Units 8 and 12 |
| Explicit case and strategy evidence in the existing product | Makes unit 12 assessable without relocating its standards | Unit 12 |
| Four-session senior ending | Preserves revision and response | Grade 12 calendar; unit 24 |
| Different dependency treatment for dance and SEL | Their current completion states differ | Cross-subject |
| Body weight and bands as the course’s resistance path | Removes contradictory lifting instructions | Equipment rules; unit 14 |
| $740 as the sum of listed purchases | Arithmetic correction, pending any identified omitted purchases | Supplies; For the lead |
| `Cues and settings` header | Follows the after-core brief | Units table |

The earlier review’s claim that the grade 9 log is simply “never scored” overstates the present wording, which says it is never scored **on what was chosen**. An unscored teacher reading can also supply assessment evidence, so I have not repeated that claim as a separate finding.

## What I could not judge

- Whether actual lessons maintain the required activity time or whether students master the cues.
- Whether the 64-session route preserves sufficient practice. Its exact day selections do not exist yet.
- SEL unit timing while its Units table remains empty.
- Every activity-specific safety section. This was a frame read, not the later safety-agent read.
- Current purchase prices. The cost finding checks arithmetic, not quotations.

The PECAT grade tables were not reread in full. Their detailed placement claims remain repository-reported evidence; CDC’s current explanation of the outcome, content and assessment method was checked live.

## For Cory

- **Money:** Set the equipment ceiling and its basis, per year, band or building. The presently listed band purchases total $740 before optional compasses and any omitted required purchases.

## Sources

- [2024 national PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/): checked the required actions and breadth of the high school indicators.
- [CDC PECAT](https://www.cdc.gov/assessing-improving-school-health/pecat/index.html): checked the outcome, content and assessment review method.
- [Professional guidelines](https://shapeamerica.org/standards/guidelines/): checked the frame’s stated weekly-minutes recommendation.
- [CDC youth activity guidance](https://www.cdc.gov/physical-activity-education/guidelines/index.html): checked the distinction between PE provision and daily activity.
- [Nova Scotia PE safety guidelines](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf): checked relevant fitness progression and adaptation guidance.
- [CDC drowning prevention](https://www.cdc.gov/drowning/prevention/index.html): checked the linked page and its prevention context; it is not a complete rescue-teaching manual.
- [Library of Dance](https://www.libraryofdance.org/dances/sir-roger/), [IOC history](https://www.olympics.com/ioc/history), [National Football Museum](https://nationalfootballmuseum.com/items/the-laws-of-the-game-1863/) and [ActiveSG](https://www.activesgcircle.gov.sg/learn/sepak-takraw/rules-and-regulations-of-sepak-takraw?tab=how_to_play): opened for the named cultural and historical examples.

## For the source list

Add the historical dance descriptions, National Football Museum object page and ActiveSG introduction as accessible references if they are not already listed. Their accessibility does not establish permission to reproduce their text or images.

