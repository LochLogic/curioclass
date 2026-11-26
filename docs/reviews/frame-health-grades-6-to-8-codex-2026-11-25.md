# Second-model frame read: Health, grades 6 to 8

**Date:** November 25, 2026  
**Course:** `health-grades-6-to-8`  
**Delivery:** Complete report supplied here. No report file written.

## Verdict

**Revise before scope-and-sequence writing.** The band structure, skill placement, annual arithmetic, and removable sensitive units are sound. The biggest risks are treating bullying through conflict-resolution steps and awarding skill judgments from written descriptions alone; correct those instructions before writers build lessons from them.

**Finding count: 9.**

## What I read and checked

I read the complete [course frame](S:/CurioClass/docs/courses/health-grades-6-to-8/frame.md), the review brief and after-core writing provisions, `EXPERT.md`, the health lens, the health adoption bar, `STANDARD.md`, and `APPROACH.md`.

The comparison included:

- The `course-list.csv` selector, `frames.csv` entry, and all 63 selected health progression rows.
- Local NHES indicator descriptions and HECAT outcome descriptions.
- The neighboring health frames’ course descriptions, seams, models, and relevant units.
- The cited core units, their owned standards, and calendar positions.
- Current PE and SEL unit placements, shared cards, and calendar positions.
- Earlier health progression, pre-work, and frame reviews for repeated finding types.
- The outside sources linked below.

There is no base text, so a base-text source map is not applicable.

### Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check health-grades-6-to-8` | One failure: lesson-stage `days.csv` with `parts.csv` or `items.csv` is absent. Course-filtered to honor AGENTS.md. |
| `python -X utf8 scripts/frame.py check health-grades-6-to-8` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** |
| Selected skills | **63 selected and placed once.** |
| Indicator ownership | **46 distinct indicators:** grade 6 owns 13, grade 7 owns 17, grade 8 owns 16. |
| Annual allocation | Each year has **44 unit sessions plus four check/respond sessions**. |
| Stored calendar | All **42 rows match** the calendar calculated from the current frame. |
| Annual standards | All eight appear in each year’s non-sensitive progression rows. |
| Two-topic rule | Standards 2 through 8 each appear in at least two non-sensitive topics across the band. |

The plan-stage failure does not prevent this frame review. The structural pass establishes placement and arithmetic, not complete teaching or assessment.

## Findings, most serious first

### 1. The bullying unit carries conflict-resolution steps without defining their limit

**Location:** Seams, line 192; Models carried, line 301; unit 7, line 318.  
**Severity:** Serious. **LAYER:** frame. **REPEAT:** yes, the same transfer problem appears in the grades 3-to-5 second-model read, finding 2. **Confidence:** firm.

**Problem:** Unit 7 names “boundary and conflict steps” as its communication model. The carried conflict card includes each person stating their side and finding a fair way. Nothing in this unit explicitly prevents applying that sequence to bullying.

**Why it matters:** A writer could build a joint negotiation task between a student being bullied and the person bullying them. Federal guidance distinguishes bullying from conflict between people with equal power and warns against peer mediation for bullying. [Federal response guidance](https://www.stopbullying.gov/prevention/support-the-children-involved).

**Exact fix:** Add this direction to unit 7’s learning and teacher-note cells:

> Distinguish ordinary disagreement from bullying before choosing a response. In bullying, prioritize safety, supporting the person targeted, reporting, and adult follow-through. Do not require negotiation, compromise, or a joint problem-solving conversation with the person bullying.

Change unit 7’s skill description to:

> Boundary, reporting, and help steps; calming and listening retrieved from the conflict card.

Give day 1 two contrasting cases and require students to choose the appropriate response route. Retain the prohibition on students acting the person who bullies.

### 2. Written answers can substitute for demonstrated skills

**Location:** End-of-unit evidence, lines 74 to 86; units 3, 11, 12, 14, 23, and 24; corresponding course-level checks.  
**Severity:** Serious. **LAYER:** frame. **REPEAT:** yes, demonstrated action replaced by descriptions was identified in both earlier health band reads. **Confidence:** firm.

**Problem:** The default assessment is a written account of what a character would do. Unit 3 specifically checks written listening steps. Other communication units also finish with written lines, while unit 23 judges tool selection without naming assessed evidence of applying the tool.

Practice is present, but the frame does not require an individual performance record for these judgments. The explicit doing-record safeguard currently names only selected indicators in units 26 and 27.

**Why it matters:** Knowing a script does not establish active listening, responsive communication, or application of an influence-management strategy. The live indicators and HECAT assessment guidance require evidence matching the intended skill. [2024 indicators](https://shapeamerica.org/standards/health/new-he-standards/), [HECAT Appendix 7, PDF page 1](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf).

**Exact fix:**

- In units 3, 11, 12, 14, and 24, reserve part of existing practice/application time for a teacher-recorded individual response to an unfamiliar prompt. Unit 3 must include receiving a message, asking a relevant question, and accurately reflecting its meaning.
- Permit speech, AAC, or responsive written exchange with an adult or partner. A prewritten description of somebody else’s response cannot stand alone.
- In unit 23, record each student applying a taught strategy to an invented message during class. Keep personal logs private.
- Carry these records into unit judgments and cumulative checks without rescoring them. Retain written scenarios as additional evidence.

### 3. Several owned indicators are narrowed by their tasks

**Location:** Units 1, 13, 16, and 25; related course-level check cells.  
**Severity:** Serious. **LAYER:** frame. **REPEAT:** yes, partial indicator coverage recurred in the K-to-2 frame read. **Confidence:** likely.

**Problem:** All codes are placed, but these tasks leave part of their demand unprotected. Comparison used the local descriptions and the [live 2024 indicators](https://shapeamerica.org/standards/health/new-he-standards/).

| Indicator and location | Gap | Exact fix within the existing unit |
|---|---|---|
| `S1.8.1`, unit 1 | Maps what strengths contribute, without analyzing ways to build on them. | Add a practice/helper strategy to each strengths map and assess its health contribution. |
| `S1.8.5`, unit 13 | Decoding an instruction can replace analyzing the connection with health outcomes. | Add a paired-character case requiring an explanation of that connection. |
| `S3.8.3` and `S3.8.4`, unit 13 | Claim tracing and rating dominate; product and service access/evaluation are less complete. | Include printed information, product-source, and service-directory cases; assess locating and evaluating each. |
| `S5.8.4`, unit 16; `S5.8.5`, unit 25 | “Personal and wider” or unspecified levels can omit required levels. | Use an explicit five-level matrix in teaching and checks, including the environmental level. |

Update the corresponding cumulative-check descriptions to preserve these demands. Keep current owners and unit allocations.

### 4. The proposed nine-week route cannot hold the stated course unchanged

**Location:** Days bullet, lines 27 to 28; unit 26, line 337; unit 27, line 338.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** new. **Confidence:** firm.

**Problem:** Nine weeks of daily teaching provide 45 meetings. Each year requires 48. The claim that this route keeps the same order and checks therefore leaves three sessions unexplained.

Compression also changes elapsed time. Unit 26 relies on a five-week habit project, and unit 27 relies on time between delivery and evaluation. Seven consecutive daily sessions cannot reproduce unit 26’s stated duration.

**Why it matters:** A scope writer would have to remove teaching, checks, or performance time without a settled rule. HECAT distinguishes pacing from scope and calls for time to develop and reinforce skills. [HECAT Appendix 5](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_05.pdf).

**Exact fix:** Delete the promise that an unchanged course fits a daily nine-week quarter. Replace it with:

> The planned route is 48 sessions across 32 weeks. A daily nine-week route requires a separately specified 45-session short path. That path must identify three session reductions, retain every owned indicator and check/respond cycle, and explicitly schedule the multiweek habit and advocacy evidence.

Do not label that route available until its session table exists. If a nine-week delivery limit is required, bring the time constraint to Cory.

### 5. The SEL bridge assumes an unavailable card and cites obsolete unit numbers

**Location:** Unit 3; Cross-subject, lines 403 to 425; Models carried and shared-wording claims.  
**Severity:** Moderate. **LAYER:** frame and process. **REPEAT:** yes, obsolete neighbor references and conflicting shared cards were identified in earlier health frame reads. **Confidence:** firm.

**Problem:** Health unit 3 runs in grade 6 weeks 7 to 10. SEL unit 3 introduces its expanded calm-down card in weeks 11 to 15. Health says it uses SEL’s card without specifying the earlier form or a bridge.

The SEL table also uses year-relative numbers for grades 7 and 8, rather than the current band’s continuous numbering. Health’s I-statement ends “Please ___”; SEL’s current model ends “I need ___,” despite the claim of one wording.

**Why it matters:** Writers can use a model before its introduction or produce competing cards.

**Exact fix:**

1. State that health unit 3 retrieves the **grade 5 four-step calm-down card: stop, breathe, name it, choose**. SEL unit 3 later grows it to five steps.
2. Replace SEL references with current band units:

| Health connection | Current SEL unit and weeks |
|---|---|
| Grade 7 refusal | Unit 8, weeks 6 to 11 |
| Grade 7 support, conflict, and standing up | Unit 11, weeks 22 to 27 |
| Grade 7 goals | Unit 12, weeks 27 to 31 |
| Grade 8 checking facts and thinking ahead | Unit 13, weeks 1 to 5 |
| Grade 8 refusal | Unit 14, weeks 6 to 11 |
| Grade 8 perspectives and concern | Unit 16, weeks 17 to 22 |
| Grade 8 negotiation | Unit 17, weeks 22 to 27 |
| Grade 8 goals and teamwork | Unit 18, weeks 27 to 31 |

3. Keep health’s established “Please ___” request slot and list the reciprocal SEL wording correction for the lead.
4. Add the existing PE unit references: unit 7 for `g6-ways-active`, unit 13 for `g7-challenges`, unit 14 for `g7-eat-move-well`, and units 18 and 15 for `g8-leading` and `g8-goals-obstacles`.

### 6. Two readiness checks ignore documented use in grade 5

**Location:** Readiness bullet, lines 87 to 97; seam introduction; units 2 to 5.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** new in the health reports examined. **Confidence:** firm.

**Problem:** The frame treats two grade 4 rows as unused since grade 4. The preceding frame documents otherwise:

- Grade 5 unit 15 explicitly retrieves `g4-meh-calm-stress`; unit 18 retrieves it again.
- Grade 5 unit 17 explicitly retrieves `g4-phw-prevent-illness-injury` and practices its injury-prevention contribution.

**Why it matters:** The frame’s rule counts last use, not simply the owner grade. The current wording also falsely describes prevention as skipped in grade 5.

**Exact fix:**

- Replace the reserved ten-minute readiness checks before units 3 and 5 with opening retrieval tasks inside those units.
- Cite grade 5 units 15/18 and 17 as the last-use evidence.
- Remove “after a skip” and “skipped in grade 5” for these links.
- Return the reserved minutes in units 2 and 4 to their assessment work.
- Retain the two older-row checks in grade 8 unit 22 unless later scope evidence changes their count.

### 7. Assessment-day instructions conflict with the after-core brief and product schedule

**Location:** Days and evidence bullets; units 5, 15, 18, 25, and 26; mid-year check rows.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** new for the explicit after-core check rule. **Confidence:** firm.

**Problem:** Units 5, 15, and 25 each finish with an assessment, immediately followed by a cumulative check covering their content. The after-core brief says that the course-level check serves as the preceding unit’s assessment when it covers that unit.

The product schedule is also ambiguous: unit 26 puts drafting, written feedback, and revision together on day 6, despite promising counted draft and revision days.

**Why it matters:** Writers receive conflicting instructions about both assessment load and feedback time.

**Exact fix:**

- Make each mid-year check the end-of-unit assessment for unit 5, 15, or 25.
- Convert those units’ current final assessment sessions to application and feedback. Keep annual totals unchanged.
- Replace “end-of-unit record carried” in those check rows with explicit first-scored evidence from the immediately preceding unit.
- In unit 26, draft the write-up on day 5, provide written feedback before day 6, and revise on day 6.
- In unit 18, explicitly identify day 1’s ask as the first draft, day 3 as revision after feedback, and day 4 as scoring.

### 8. Unmarked process statements and template instructions need correction

**Location:** Days bullet; Day kinds; Units header and blank ownership cells; Cross-subject introduction; For the lead item 2.  
**Severity:** Moderate. **LAYER:** process. **REPEAT:** yes, stale status and template wording recur in earlier health frame reads. **Confidence:** firm.

**Problem:** The marked stale-note check passes, but several unmarked instructions are inaccurate:

- The frame claims both checks avoid every core check day. School day 157 overlaps ELA year-end checks, and grades 6 and 7 social studies checks. Finals-week sharing is permitted.
- For the lead item 2 says there are no after-core clashes. Current PE mid-year check ranges include health’s school day 84 in all three grades.
- The course allows at most one whole Fluency day per unit, but units 3 and 12 list two.
- The current after-core brief requires **Skill steps**, rather than **C3**, and **None** in ownership cells without owned codes.

**Exact fix:**

Replace the check-separation claim with:

> Mid-year checks avoid core check days. Year-end checks share the permitted week 32 finals period.

Replace For the lead item 2 with:

> Health’s mid-year check is school day 84 in each grade. Current PE check ranges overlap that day. Retain this placement pending the lead’s shared calendar pass; week 32 year-end sharing is permitted.

Change the Fluency statement to allow the one or two sessions explicitly listed, while retaining Understanding for first teaching. Rename the seventh Units column **Skill steps** and fill blank ownership cells with **None**.

Do not move shared calendar entries in this review.

### 9. Grade 6’s printing total is overstated by two dollars

**Location:** Annual cost summary, lines 343 to 345; For the lead item 9.  
**Severity:** Minor. **LAYER:** frame. **REPEAT:** yes, cost arithmetic was identified in both earlier health band reads. **Confidence:** firm.

**Problem:** The grade 6 unit costs sum to **$30**, rather than $32.

**Exact fix:** Change both grade 6 summary amounts to **$30**. Keep grade 7 at **$31**, or **$46** with the helmet, and grade 8 at **$39** including poster supplies. These are arithmetic corrections, not verification of purchasing prices.

## Coverage, sequence, days, and seams

The progression placement is complete. Every owned indicator remains in a non-sensitive unit, sensitive units name replacement uses for their optional days, and non-sensitive rows do not depend on sensitive rows.

The main sequence holds: help precedes sensitive applications, influence work precedes later decisions, and goal planning precedes monitoring. The grade 9 handoffs match the neighboring frame’s pickup table.

The science, mathematics, and ELA calendar relationships are generally handled correctly. In particular, the frame supplies alternatives when science or statistics comes later. The two grade 5 dead ends already identified under For the lead item 4 should remain explicit paired-row repairs.

No unit is demonstrably far over its allocation. Unit 30 remains particularly tight: three sessions contain two sessions of new content and an assessment across six sexual-health outcome tags. Its module read must test actual content, practice, and assessment time before those tags become a coverage claim. HECAT’s middle-school sexual-health expectations are substantially more detailed than the outcome headings. [Sexual Health module, PDF pages 6 to 8, printed SH-6 to SH-8](https://www.cdc.gov/healthy-youth/hecat/pdfs/hecat_module_sh.pdf).

The accepted lower annual dose is not reopened here.

## Health lens checklist

“Met” means adequately specified at frame level, not demonstrated in finished lessons.

| Lens requirement | Result |
|---|---|
| Named behavior outcomes; useful facts | Met in design |
| Skills explained, modeled, practiced, and given feedback | Part met: findings 2 and 7 |
| Norms and social pressure addressed | Met in design; figures remain due |
| No fear, shame, or blame | Met as an explicit constraint |
| Families, trusted adults, and help routes | Met |
| Inclusive participation without required disclosure | Met |
| Sufficient time and spaced return | Part met: finding 4; unit 30 needs timing confirmation |
| All eight standards reached | Met each year |
| Skill standards practiced across two topics | Met with sensitive rows excluded |
| Coverage map locations | Outcome tags present; full matrices remain due at scope stage |
| Topics return across the band | Met at frame level |
| Sensitive units removable | Met for ownership and dependencies |
| Help taught outside sensitive units | Met every year |
| Indicators used within the correct span | Met |
| Performance assessments rather than recall alone | Part met: finding 2 |
| Skills have steps, models, and practice | Met in intent; bridge correction in finding 5 |
| Current, dated figures | Required, not yet demonstrated |
| Age-matched content | Provisionally met; module reads remain necessary |
| Home links and advance sensitive-unit notes | Met |
| Indicator meaning preserved | Part met: finding 3 |
| No required personal health or family disclosure | Met |
| No weighing, calorie counting, or food moralizing | Met |
| Suicide/self-harm safeguards | Specified: no methods, help line, adult plan, counselor preparation |
| Tools collect no health information or give advice | Met as a constraint |
| Science models used without unnecessary reteaching | Met |
| Health and PE divide planning from movement | Met in principle; references need updating |

## What is right and should remain

- The Year column, continuous numbering, and complete annual check/respond structures.
- Non-sensitive ownership of every unique indicator.
- Removable sensitive units with advance notes and disclosure directions.
- Paper access, communication accommodations, and private personal records.
- Real-audience advocacy and the explicit doing records in units 26 and 27.
- The mathematical fallbacks when statistics comes later.

## Settled by the expert

| Choice | Reason | Files affected by a later fix |
|---|---|---|
| Preserve 30 units, 144 sessions, and current ownership | Placement and arithmetic hold | Health frame |
| Separate bullying response from ordinary conflict resolution | Prevents an unsafe instructional transfer | Health frame |
| Require individual performance evidence during existing sessions | Matches evidence to the skill | Health frame |
| Restore omitted indicator demands within current owners | Completes existing scope | Health frame |
| Use the grade 5 calm-down card in health unit 3 | The expanded SEL card comes later | Health frame |
| Treat the two documented grade 5 uses as retrieval | Last-use evidence governs | Health frame |
| Use mid-year checks as the preceding units’ assessments | Follows the after-core rule | Health frame |
| Correct grade 6 printing to $30 | Sum of listed costs | Health frame |

## What I could not judge

- Finished lesson timing, scoring guides, accessibility implementation, or classroom effectiveness.
- Complete medical and scientific accuracy, which requires the separate dated unit/day read.
- Full coverage of all nine HECAT modules’ span expectations.
- Final survey figures, current purchasing prices, or the historical 2007 national-hours citation.
- A workable 45-session quarter route, because none is specified.

## Outside sources and memory

- [2024 NHES indicators](https://shapeamerica.org/standards/health/new-he-standards/): checked indicator demands.
- [HECAT Appendix 7](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf): checked assessment alignment and evidence.
- [HECAT Appendix 5](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_05.pdf): checked scope, sequence, and pacing distinctions.
- [CDC curriculum characteristics](https://www.cdc.gov/assessing-improving-school-health/health-education-curriculum/): checked skill instruction, reinforcement, and adequate practice time.
- [Federal bullying response guidance](https://www.stopbullying.gov/prevention/support-the-children-involved): checked the boundary between bullying response and conflict resolution.
- [HECAT Sexual Health module](https://www.cdc.gov/healthy-youth/hecat/pdfs/hecat_module_sh.pdf): selectively checked middle-school expectations and unit 30’s load.

No substantive finding rests on memory. The frame’s safety links and inherited browser-check entries remain unverified in this read. The historical national-hours comparison was not independently reverified.

**For the source list:** Add the federal bullying response page to unit 7’s required source pack if it is not already listed.

## For Cory

- **Money:** The proposed $40 annual supplies ceiling remains a decision. Corrected listed totals are grade 6 **$30**, grade 7 **$31** or **$46** with the helmet, and grade 8 **$39**.
- **Time and scope:** If a daily nine-week route is required, settle that delivery constraint before a writer removes three sessions or compresses multiweek performance evidence.