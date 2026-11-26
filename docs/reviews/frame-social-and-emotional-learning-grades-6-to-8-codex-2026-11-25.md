# Independent frame review: Social and Emotional Learning, Grades 6 to 8

Date: 2026-11-25  
Course: `social-and-emotional-learning-grades-6-to-8`  
Read only. No files were created, edited or deleted.

## Verdict

The frame has a sound structure: all 120 selected progression rows are placed exactly once, each grade has a distinct six-unit year, and the full calendar provides 64 sessions per year. It needs revision before scope writing because some standards remain partial, one rehearsal conflicts with the safe-role rule, and a permitted unit omission leaves an immediate dependency unsupported. The most important change is to complete the teaching within the existing units while preserving invented cases and optional personal sharing.

**Eight findings: three serious, four moderate and one minor.**

## What I read

- The frame-read brief, after-core provisions of frame-write, EXPERT.md and the SEL lens.
- FOUNDATION.md; relevant provisions of PRODUCTION-PATH.md, APPROACH.md and BASELINE.md.
- ADOPTION-BAR-SUBJECTS.md, including part 9 and the SEL status row; SEL STANDARD.md and APPROACH.md.
- The complete [course frame](S:/CurioClass/docs/courses/social-and-emotional-learning-grades-6-to-8/frame.md), its course-list selector, frames.csv entry and calendar.csv rows.
- All 120 SEL progression rows selected by `grade:6|7|8`, their incoming and outgoing links, and the 40 standard statements.
- Adjacent SEL frames’ unit placements, seam tables and model descriptions.
- Relevant Units-table entries in ELA, mathematics and social studies; health, PE, computer science and career exploration seam provisions.
- Library’s three standards transfers and the validators’ current recognition.
- SEL pre-work, progression and earlier frame reviews, including the K to 2 fix report, the grades 3 to 5 second-model report and the combined grades 3 to 12 expert report.
- The outside sources linked below.

No base text is claimed, so a base-lesson source map is not applicable.

## Checks and counts

Python commands used bytecode suppression. The plan check was course-filtered to honor AGENTS.md’s prohibition on unfiltered runs.

| Check | Result |
|---|---|
| `scripts/plan.py check social-and-emotional-learning-grades-6-to-8` | Failed because the later day-plan files do not exist; review proceeded |
| `scripts/frame.py check social-and-emotional-learning-grades-6-to-8` | Passed, zero failures |
| `scripts/stale.py check` | Passed, 121 files, zero failures |
| Targeted stale check on the frame, SEL standard, SEL approach and progression | Passed, zero failures |
| Independent placement count | 120 rows, 120 distinct placements, no missing or extra rows |
| Reciprocal progression links | No broken incoming or outgoing links among the selected rows |
| Ownership | All 40 SEL codes owned in grade 8; grades 6 and 7 begin them |

| Grade | Units | Sub-skills per unit | Unit sessions | Check/respond sessions | Total |
|---|---|---|---:|---:|---:|
| 6 | 1 to 6 | 5, 6, 5, 8, 8, 8 | 60 | 4 | 64 |
| 7 | 7 to 12 | 7, 5, 5, 7, 8, 8 | 60 | 4 | 64 |
| 8 | 13 to 18 | 6, 8, 6, 7, 5, 8 | 60 | 4 | 64 |

The stored calendar agrees with these allocations. Mid-year checks fall on school day 75 in grades 6 and 7 and day 78 in grade 8, avoiding core check days. Year-end checks on day 158 overlap core checks within the permitted week 32 finals exception.

## Findings, most serious first

### 1. The hallway rehearsal assigns the student a prohibited role

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, safe-role contradictions recur in the grades 3 to 5 second-model finding 7  
**Confidence:** firm

**Location:** Unit 3, Group 1; progression row `g6-sm-big-feelings`.

The frame rehearses responses for a character laughed at in a hallway. The progression makes the assignment explicit: the student speaks as that character while the teacher reads the hallway moment.

Having the teacher supply the mockery prevents a student from playing the aggressor, but still casts another student as the person being mistreated. STANDARD section 5.3 prohibits both roles.

**Why it matters:** A writer following the progression would build a rehearsal that contradicts the course’s safety rule.

**Exact fix:** Replace the rehearsal’s trigger with an ordinary setback that preserves strong feelings and audience pressure without targeted mistreatment:

> An invented character’s model falls apart just before a class display. Students compare three responses, rehearse the calm-down steps and a chosen response, and explain how concern about onlookers affected the choice. No character mocks or humiliates another.

Apply the replacement to unit 3 and `g6-sm-big-feelings`. Keep any discussion of targeted mockery as third-person case analysis rather than a student’s acted role.

### 2. Complete placement masks partial treatment of owned standards

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, K to 2 second-model finding 2 and grades 3 to 5 second-model finding 1 identified the same coverage problem  
**Confidence:** firm

**Location:** Units 2, 6, 7, 10 and 13 to 16; corresponding progression notes.

Four components are not secured by the required teaching:

| Standard | Gap | Exact fix within the existing placement |
|---|---|---|
| SA5, linking feelings, values and thoughts | Units 2, 10 and 13 use thought-feeling-action chains without explicitly connecting what matters to the character to their thought and feeling. | Add the character’s value, such as belonging or fairness, to each case. Students explain how it helps account for the thought and feeling. Include that connection in unseen evidence. |
| SA2, cultural and linguistic strengths | Grade 8 unit 14 uses a generic strength. The progression welcomes culture and language when offered, which makes that component optional. | Require an invented example containing a cultural or linguistic strength, then have students explain its contribution to the task despite the social cost. Keep personal examples optional. |
| RS3, working across cultures | Units 6, 7 and 16 deliberately reduce differences to individual work habits. The Base text bullet expressly says they are never a culture’s way. | Retain individual variation, but require culturally situated cases and respectful adaptation across cultures. Unit 16 must demonstrate this at owner-year depth, with sourced context and an unseen application. |
| SM5, planning and organization | Grade 8 unit 15 covers competing commitments and time, but omits keeping materials organized. | Add an invented project’s papers or materials to the planning task. Students choose an organization system and explain how it supports the revised schedule. |

The cultural, linguistic and values components are explicit in the published [CASEL framework](https://casel.org/what-is-sel/) as well as the repository’s standard statements.

**Why it matters:** A scope writer can follow the frame faithfully and still build incomplete owner-year coverage.

For a concrete RS3 replacement, unit 16 could use written cases about an invented Deaf and hearing project team negotiating communication preferences under a deadline. The [Deaf-Hearing Communication Centre’s guidance](https://www.dhcc.org/resources/communication-tips) supports asking individual preferences and adapting group communication. Students would analyze and negotiate from case cards, with no simulation of hearing loss or requirement to perform another identity.

Amend the affected progression notes and evidence descriptions. Keep every standard in its current unit.

### 3. Leaving out unit 2 breaks unit 3’s stated prerequisite

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, missing leave-out dependencies recur in the K to 2 and grades 3 to 5 second-model reads  
**Confidence:** firm

**Location:** Leave-out bullet; units 2 and 3; Models carried.

The leave-out list says unit 2’s feelings scale is first needed by unit 4. Unit 3’s reason explicitly depends on the scale grown in unit 2, and its retrieval names that scale. Unit 2 also says its think-feel-do chain supports unit 3, but the bridge list omits that routine.

**Why it matters:** A school can exercise the authorized omission and immediately encounter a unit whose opening assumes the omitted teaching.

**Exact fix:**

- Change the feelings-scale entry to identify **unit 3** as its first receiving unit.
- In unit 3’s first Understanding session, provide the subject’s ten-minute, one-step bridge when unit 2 was omitted: model identifying a character’s feeling from a clue and distinguishing mild from strong.
- State which opening and rehearsal minutes the bridge replaces.
- Either supply the minimal think-feel-do bridge where unit 3 actually uses it, or remove unit 2’s claim that unit 3 depends on that chain.
- Check later receivers against the complete model list, including the problem size meter and goal steps inherited from the preceding band.

The bridge claims none of unit 2’s omitted standards.

### 4. The widened checks lack a bounded workload and complete evidence placement

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, combined expert finding M2 identified the widened-check workload  
**Confidence:** likely for timing; firm for the missing evidence assignments

**Location:** Evidence bullet; Course-level checks; units 14 and 18.

The frame combines a unit assessment, several sampled earlier skills and a watched rehearsal per pair in a 30-minute session with about 20 working minutes. It permits rehearsal observations in the last Application session, but does not cap how many remain for Check.

There is also an evidence-placement gap. For example, unit 18’s check names upstander choice, covering a team gap and well-being. It does not identify where the owner-year goal monitoring, initiative, agency, leadership and problem-solving performances are judged. The project is expressly unscored. Unit 14 similarly leaves several owned skills outside its named end evidence.

**Why it matters:** A writer may build an overlong page while leaving some owned skills evidenced only by unspecified daily observation.

**Exact fix:**

1. Cap cumulative sampling at **two brief written items per course-level check**, with no additional sampled rehearsal.
2. Identify the owned skills judged during each unit’s last Application sessions and those judged during Check. Every owned skill needs a named evidence opportunity.
3. For unit 18, place goal adjustment, initiative, answering objections, leading/following and evaluating a solution in named Application evidence. Judge the demonstrated steps, never character or willingness.
4. Require an individual look-for for each student within pair rehearsals.
5. Set a maximum number of unfinished pair observations entering Check, based on a timed unit-plan probe.
6. Give the shared short-path Check/Respond session its own minute budget.

Retain the existing session totals and end-of-unit evidence forms.

### 5. The three transferred library standards remain outside ownership checking

**Severity:** Moderate  
**LAYER:** progression, frame  
**REPEAT:** yes, K to 2 second-model finding 4  
**Confidence:** firm

**Location:** Standard bullet; Library subsection; For the lead 3; units 15 and 18.

The frame acknowledges the transfers and names their teaching, but the codes remain outside the progression’s standard cells and the Units table’s Owned standards cells.

| Transferred code | Receiving owner row | Unit |
|---|---|---:|
| `AASL.V.D.1` | `g8-sm-stay-on-task` | 15 |
| `AASL.V.D.2` | `g8-sa-skills-grow` | 15 |
| `AASL.III.D.2` | `g8-rel-teamwork` | 18 |

The current SEL validator recognizes the CASEL standard file only. A passing placement check therefore cannot verify these agreed responsibilities.

**Exact fix:** The lead should add narrowly scoped recognition and band ownership treatment for these three transferred codes, then place them on the stated owner rows and units with their evidence. Do not make SEL responsible for the rest of the library framework.

Also correct both references to `data/plans/library-excluded.csv` to the actual file, `data/progressions/library-excluded.csv`.

### 6. The model register misstates inheritance and changes shared wording

**Severity:** Moderate  
**LAYER:** frame, progression  
**REPEAT:** yes, combined expert findings M3 and m3  
**Confidence:** firm

**Location:** Models carried; unit 3; seam descriptions; progression rows `g6-sm-calm-down`, `g6-rel-stand-up` and `g6-rel-ask-offer-help`.

The paragraph headed “New in this band” includes refusal, fairness and upstander cards already taught in grades 3 to 5. The upstander row’s step-up still describes a move from one planned response to choosing among options, although the earlier band already offers options.

The calm-down card also changes “choose” to “pick a tool” while claiming simply to add “go on.”

**Why it matters:** Writers can mistake retrieval for first teaching and produce inconsistent cards across subjects.

**Exact fix:**

- Move the inherited cards into explicit model rows.
- Describe grade 6 refusal as choosing an inherited option to fit the setting.
- Describe the upstander extension as adding online reporting and choosing safely for a team-chat case.
- Rewrite the help-seeking step-up as choosing a helper by setting, channel and available adults, building on the earlier size-based choice.
- Keep the shared calm-down wording **“stop, breathe, name it, choose, go on.”** Explain “choose” as choosing a tool.
- Have the lead align the matching PE and next-band wording.

### 7. The historical sensitivity pack lacks the community’s own published voice

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, source sufficiency was raised in the K to 2 second-model read  
**Confidence:** firm

**Location:** Base text and Sensitivity reads bullets; units 9 and 16; For the lead 11.

The frame names only the National Archives opinion page for the sensitivity agent’s historical preparation. FOUNDATION section 7 also requires the community’s own published voice.

The [National Archives page](https://www.archives.gov/milestone-documents/brown-v-board-of-education) supports the constitutional ruling and distinguishes it from later implementation. It does not replace a community account.

**Exact fix:** Name Black American families and plaintiffs as the community concerned, and add [Cheryl Brown Henderson’s account of preserving the Brown history](https://www.brownvboard.org/brown-foundation-story) to the required preparation pack. Require separate sourcing for any specific personal costs taught in unit 16.

Use the precise historical statement:

> In 1954, the Supreme Court held racial segregation in public schools unconstitutional. Implementation followed and met resistance.

I disagree with the combined expert report’s claim that using Brown twice necessarily prevents growth. Unit 9 asks students to consider excluded people’s perspectives; unit 16 asks about the costs of change. Keep Brown as an explicitly identified revisit, with different evidence and questions.

### 8. Living status notes still describe completed work as pending

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, combined expert finding m1 and earlier second-model stale-note findings  
**Confidence:** firm

**Location:** For the lead 4, 6, 7 and 8; adjacent-band handoff note; SEL status row in ADOPTION-BAR-SUBJECTS.md.

The stale checker passes, but manual inspection finds:

- Computer science grades 6 and 7 frames exist. Their relevant rows are in units 1 and 6, already cited in this frame’s Cross-subject table.
- PE’s seam now cites the written SEL frame.
- Career’s table now names SEL units 13 to 18, although its separate Pending paragraph remains stale.
- `g6-sa-name-feelings` already says it grows the earlier strength scale.
- The subject-bar status row still owes the completed progression and settled session-arithmetic call.

**Exact fix:** Replace the affected living notes with current statements:

- **For the lead 6:** “PE 6 to 8 now cites the SEL calm-down, conflict and teamwork placements.”
- **For the lead 7:** “Career’s Cross-subject table names SEL units 13 to 18 and retains its own bridges; remove the obsolete Pending paragraph.”
- **For the lead 8:** “Computer science grade 6 unit 1 and grade 7 unit 6 provide the links cited in Cross-subject.”
- **For the lead 4 and the preceding-band handoff:** distinguish the corrected feelings row from the remaining upstander step-up correction.
- **Subject-bar SEL status:** state that the progression and its validator support are complete and session arithmetic was settled in q-fix-sel-1.

Do not rewrite dated review reports.

## Lens checklist, frame layer

| Lens requirement | Result |
|---|---|
| Distinct grade-year cases and growing depth | Met overall: options, another person’s view, then costs |
| Every sub-skill placed, with return practice | Placement met; recurring practice is specified through openings and carried routines |
| Minutes stated; short path retains units | Met |
| Carry-out cue and family activity in every unit | Met |
| A unit can be left out without breaking later units | Missed, finding 3 |

The wider lens also exposes findings 1 and 2. The frame otherwise preserves the health boundary, invented cases, nonclinical language, private pages and skill-based checks.

## What is right and should not be touched

- The Year column, continuous unit numbering and complete annual structure.
- All 120 row placements and reciprocal seams.
- The 64-session dose and inclusion of Respond time.
- The paper-first route and absence of student accounts.
- Mandatory rehearsal for refusal, help-seeking and upstander work.
- Disposal of teacher working sheets after their stated purpose.
- Explicit core-course bridges where mathematics or ELA comes later.
- The statement that no study has tested these courses.

No whole unit appears substantially overallocated. The main pacing risk is concentrated in assessment sessions rather than the overall distribution.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Replace the hallway mockery rehearsal with an ordinary public setback | Preserves SM1 while respecting the safe-role rule | Frame; `g6-sm-big-feelings` |
| Restore the missing standard components in their existing units | Completes coverage without moving ownership | Frame; affected progression notes |
| Bridge the feelings scale in unit 3 when unit 2 was omitted | Repairs the first actual dependency | Frame |
| Limit cumulative check sampling to two brief written items | Bounds the widened assessment | Frame |
| Preserve “choose” in the shared calm-down card | Keeps the inherited cue while adding one step | Frame; progression; neighboring references |
| Retain Brown as a deliberate revisit with different questions and stronger preparation sources | The planned depth differs between years | Frame |

## For Cory

- **Money:** The supply ceiling remains unset. The frame estimates about $55 to $60 per year for printing, small project costs and a one-time timer purchase. Recommendation: retain provisional figures until unit plans establish actual quantities.

No additional scope, audience or outside-person decision is needed for these fixes.

## What I could not judge

- Actual completion time for the widened checks or shared short-path Check/Respond sessions. These need a timed unit-plan probe.
- Finished cases, translations and historical adaptations, which do not yet exist.
- Accessibility and scoring consistency of finished rehearsal guides.

Prior memory supplied only a report-format reminder. No curriculum finding rests on unverified memory.

## Outside sources and source-list follow-up

- [CASEL framework](https://casel.org/what-is-sel/): checked the missing cultural, linguistic and values components.
- [CASEL design criteria, December 2020, pages 23 to 25](https://files.casel.org/11_CASEL-Program-Criteria-Rationale.pdf): checked grade-by-grade sequence and active-practice expectations.
- [National Archives, Brown v. Board of Education](https://www.archives.gov/milestone-documents/brown-v-board-of-education): checked the ruling and implementation distinction.
- [Brown Foundation Story, Cheryl Brown Henderson](https://www.brownvboard.org/brown-foundation-story): community-authored preparation source for the sensitivity read.
- [Deaf-Hearing Communication Centre, communication guidance](https://www.dhcc.org/resources/communication-tips): source for the proposed culturally situated collaboration case.

For the source list: record the Brown Foundation and communication-guidance pages as references only, with no assumed adaptation permission. The older CASEL framework address redirects to the current page linked above.

