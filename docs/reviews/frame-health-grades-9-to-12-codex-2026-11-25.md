# Second-model frame read: Health, grades 9 to 12

**Date:** November 25, 2026  
**Course:** `health-grades-9-to-12`  
**Delivery:** Read-only review. No report file written.

## Verdict

**Revise before scope-and-sequence writing.** The semester structure, indicator placement, day arithmetic, and goal thread are sound, but several instructions would produce incomplete standards coverage or inappropriate use of conflict-resolution steps in abuse scenarios. Correct those instructions within the existing units, then finish the calendar-specific PE and SEL handoffs.

**Finding count: 10, ordered most serious first.**

## What I read and checked

I read the complete [course frame](S:/CurioClass/docs/courses/health-grades-9-to-12/frame.md), `frame-read.md`, the after-core provisions in `frame-write.md`, `EXPERT.md`, the health lens, the shared adoption criteria and health subject criteria, and health `STANDARD.md` and `APPROACH.md`.

Comparisons included:

- The `course-list.csv` selector, `frames.csv` entry, all 28 selected progression rows, local NHES descriptions, and HECAT outcome descriptions.
- The preceding health frame’s handoffs, models, and relevant units. There is no subsequent health course.
- Current PE and SEL units, their calendar positions, and SEL’s shared-step rules.
- The cited grade 8 ELA unit and relevant earlier mathematics progression rows.
- Earlier health pre-work, progression, and frame reviews, including recorded fixes, to distinguish recurring defects from settled choices.
- The outside sources linked below.

There is no base text, so a base-text source map is not applicable.

### Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check health-grades-9-to-12` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** |
| Selected progression rows | **28**, each placed once. |
| Indicator ownership | **54 distinct owned indicators**, carried by 25 non-sensitive rows. |
| Days | **76 unit days plus four course-level check/respond days = 80.** |
| Calendar | All **25 stored rows match** the calendar calculated from the current frame. |
| Course-level checks | Days **35 and 79**, school weeks **7 and 16**; respond days **36 and 80**. |
| Printing arithmetic | **$61 + $7 = $68**; optional food demonstration raises the estimate to **$113**. |

`plan.py check` stopped while checking another course because the environment lacks the Python `markdown` dependency; this does not withhold the health-frame verdict.

## Findings, most serious first

### 1. Unit 20 carries negotiation steps into abuse scenarios without a safety boundary

**Location:** Models carried, conflict-steps row; unit 20, Skill/C3 and learning cells.  
**Severity:** Serious. **LAYER:** frame. **REPEAT:** yes, the same inappropriate transfer of conflict-resolution steps appears in the grades 6-to-8 second-model read, finding 1. **Confidence:** firm.

**Problem:** Unit 20 explicitly practices the conflict card, whose steps include listening and negotiating. It does not distinguish an ordinary disagreement from coercion or abuse before choosing that response.

**Why it matters:** A writer could ask a character experiencing abuse to negotiate with the person harming them. Specialist guidance distinguishes ordinary conflict from abuse and its unequal power structure. [Love is respect: conflict resolution](https://www.loveisrespect.org/resources/conflict-resolution/), [National Domestic Violence Hotline guidance](https://www.thehotline.org/resources/should-i-go-to-couples-therapy-with-my-abusive-partner/).

**Exact fix:** Replace unit 20’s skill description with:

> Boundary, help, and safe bystander steps. Retrieve calming and help-seeking from unit 10; do not apply negotiation or compromise to abuse.

Add to day 1 and the teacher notes:

> Distinguish ordinary disagreement from coercion and abuse. In an abuse scenario, prioritize safety, trusted-adult or specialist help, and the school’s reporting process. Never require confronting, mediating with, or negotiating with the person causing harm.

Make the unseen check require students to select the appropriate response route. Retain written scripts and the prohibition on students playing a person who harms.

### 2. Several indicator descriptions and tasks omit part of the published demand

**Location:** Units 2, 3, 4, 6, and 13; corresponding progression notes and local standards descriptions.  
**Severity:** Serious. **LAYER:** standard, progression, frame. **REPEAT:** yes, partial indicator coverage appears in the pre-work second-model read, finding 5, and earlier band reads. **Confidence:** firm on the explicit omissions; likely on the resource breadth.

**Problem:** All codes are placed, but the following demands are not protected. Comparison used the [published 2024 indicators](https://shapeamerica.org/standards/health/new-he-standards/).

| Location | Gap | Exact fix |
|---|---|---|
| Unit 2, `S1.12.6`; unit 3, `S2.12.3`; unit 13, `S5.12.5` and `S5.12.7` | The four-level model and unspecified “several levels” can omit societal or environmental analysis. | Expand the carried map to personal, interpersonal, community, societal, and environmental levels. Give each level a distinct example and preserve all five in relevant checks. |
| Unit 2, `S1.12.7` | “What helps” substitutes supports for benefits. | Analyze a behavior’s expected benefits separately from supports and barriers. Check both benefits and barriers across contrasting behaviors. |
| Unit 2, `S1.12.8` | “Sense of risk” merges perceived likelihood with perceived seriousness. | Use three separate prompts: confidence in carrying out the behavior, perceived likelihood of harm, and perceived seriousness of harm. Ask how each changes the character’s choice. |
| Units 4 and 6, `S3.12.2` through `S3.12.4` | Information dominates; product and service resources are not consistently represented. | Add an unbranded product-resource card and a service-directory card to existing packets. Students analyze access, judge credibility, and use the selected resources to answer a case. |

Correct the corresponding own-words entries in `nhes-2024.txt` and progression notes where they erase these distinctions. Keep ownership in the current units and update cumulative-check descriptions accordingly.

### 3. Two “doing” records still permit planning to substitute for performance

**Location:** End-of-unit evidence; units 14 and 15.  
**Severity:** Serious. **LAYER:** frame. **REPEAT:** yes, descriptions replacing demonstrated action recur in the grades 6-to-8 second-model read, finding 2. **Confidence:** firm for unit 14; likely for unit 15.

**Problem:** Unit 14 explicitly requires each student to carry out **one** habit, although `S7.12.4` requires a variety. Unit 15 records a revised goal step, but does not require the student to enact the adapted behavior for `S7.12.3`. The distinction is visible in both the local descriptions and the [published indicators](https://shapeamerica.org/standards/health/new-he-standards/).

**Why it matters:** A complete meal plan or revised log can receive a doing judgment without enough observed performance. CDC’s assessment guidance calls for measures that represent the intended skill. [HECAT Appendix 7, PDF page 1](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf).

**Exact fix:**

- **Unit 14:** Require each student to demonstrate multiple distinct practices during existing day 2 stations. A no-purchase route can include hand washing, preparing a clean shared serving area, and demonstrating safe serving with reusable classroom materials. Record each practice individually; eating remains optional.
- **Unit 15:** After revising the school-day routine on day 3, have each student enact the adapted step once in class. Record the action and its reason, including how it accommodates a personal or group need. Carry that record into the unit judgment.
- Keep written cases as additional evidence and retain the prohibition on scoring health results or home behavior.

### 4. Unit 20 names another independently removable sensitive unit as a prerequisite

**Location:** Unit 20, Why this unit, here.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** yes, cross-topic sensitive dependencies were identified in the health progression read, finding 10. **Confidence:** firm.

**Problem:** Unit 20 says it follows unit 10 “and unit 19.” Unit 19 is sexual health; unit 20 is violence prevention. `STANDARD.md` section 5 permits sensitive prerequisites only for later sensitive units on the same topic.

**Why it matters:** A school retaining abuse-prevention instruction while omitting sexual health receives an ambiguous prerequisite.

**Exact fix:** Replace that part of the reason with:

> After non-sensitive units 8 and 10, whose help and boundary steps it retrieves. Unit 19 is not a prerequisite. Day 1 supplies the consent facts needed here whether or not unit 19 was taught.

Retain the existing fallback for omitted grade 8 sensitive instruction.

### 5. The shared-course handoffs remain unresolved despite current neighboring frames

**Location:** Seams; Cross-subject PE and SEL tables; For the lead 4; unit 8’s opening.  
**Severity:** Moderate. **LAYER:** frame, process. **REPEAT:** yes, combined health-frame review S3 and earlier pilot seam findings. **Confidence:** firm.

**Problem:** The frame defers neighboring unit numbers and says SEL uses the same words without establishing which course teaches first. Current frames and calendar rows already settle much of this.

**Why it matters:** Writers can duplicate instruction or miss an available prerequisite.

**Exact fix:** Replace the deferred references with these current placements:

| Connection | Placement to record |
|---|---|
| PE activity choice and exercise principles | PE **unit 6**, grade 9 weeks **26 to 31**. Health units 2 and 15 teach first. |
| PE mixed fitness plan | PE **unit 8**, grade 10 weeks **5 to 11**, retrieves health unit 15. |
| PE food and supplement information | PE **unit 10**, grade 10 weeks **17 to 22**, retrieves health units 6 and 14. |
| PE activity after school | PE **unit 12**, grade 10 weeks **25 to 31**, retrieves health unit 2. |
| SEL asking/offering help | SEL **unit 1**, weeks **1 to 5**, precedes health unit 8 in week **6**. Health retrieves its support map. |
| SEL coping | SEL **unit 2**, weeks **6 to 11**, follows health unit 7 in weeks **5 to 6**. |
| SEL conflict and refusal | SEL **unit 4**, weeks **16 to 21**, retrieves health units 10 and 12. |
| SEL systems and norms | SEL **unit 5**, weeks **22 to 27**, retrieves health unit 2. |
| SEL goals and teamwork | SEL **unit 6**, weeks **27 to 31**, retrieves health units 1 and 9. |
| Later SEL boundary/help work | SEL **unit 10**, grade 10, and **unit 17**, grade 11, retrieve health units 10 and 8 respectively. |

Name the actual shared card wording or its canonical location in each connection. Add the preceding health unit numbers from that frame’s Handed on table, and replace For the lead 4 with any remaining unresolved choice only.

### 6. The week 8 goal slot crowds the respond day

**Location:** Days bullet; mid-course respond day.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** yes, combined health-frame review m4. **Confidence:** likely.

**Problem:** “First lesson of each week” places week 8’s ten-minute goal slot on day 36. That day already contains the respond work and a ten-minute readiness check, leaving 25 minutes for responding to a broad cumulative assessment.

**Exact fix:** State the ten goal-slot days explicitly:

> Days 6, 11, 16, 21, 26, 31, 37, 41, 46, and 51.

Say that week 8’s slot moves to day 37 and that each host day reserves 35 minutes for its unit. This preserves ten weekly entries before unit 15 measures the log.

### 7. The source-packet reading expectation exceeds the health approach’s stated support

**Location:** Reading level bullet; unit 6 source packets.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** new. **Confidence:** likely.

**Problem:** The frame assigns two to four agency pages to pairs. The health approach limits independent reading to a short scenario and says the remaining material is read aloud or pictured. Pairing alone does not supply that support.

**Why it matters:** Writers could retain dense agency prose and mistake difficulty reading it for difficulty evaluating evidence.

**Exact fix:** Replace the packet instruction with:

> Students read a short case independently. Source packets contain short, clearly labeled excerpts or original summaries, with the source and date retained. The teacher reads these aloud or provides pictured and chunked versions; the complete agency pages remain available as references. Students compare the same evidence under every access option.

Keep source evaluation demanding and extensions on the same standard.

### 8. Unit 2 presents an activity gap as a majority norm

**Location:** Health unit shape bullet; unit 2, day 1.  
**Severity:** Moderate. **LAYER:** frame. **REPEAT:** yes, combined health-frame review M4. **Confidence:** likely.

**Problem:** Unit 2’s survey figure is labeled a norm about “what most peers really do.” CDC’s current 2025 results report that **25%** of high school students met the daily 60-minute measure. It is a useful gap to explain, but does not show a healthy behavior practiced by most peers. [CDC physical activity results, September 2026](https://www.cdc.gov/yrbs/youth-health-in-focus/physical-activity.html).

**Exact fix:** Label unit 2’s opening:

> An activity gap to explain: what barriers help account for this survey result?

Remove unit 2 from the list of majority-norm corrections. Retain units 11 and 12 as the named norm lessons, with their latest figures checked when planned. Preserve the activity figure and its source year as evidence for the unit’s question.

### 9. The semester-term instruction is stale

**Location:** For the lead 1.  
**Severity:** Minor. **LAYER:** process. **REPEAT:** yes, combined health-frame review M2. **Confidence:** firm.

**Problem:** The note says `term` is `year` and asks for a change to `fall`. Both `course-list.csv` and `frames.csv` already say `fall`; the stored calendar already places the course in weeks 1 to 16.

**Exact fix:** Replace item 1 with:

> Semester calendar verified: term is fall, and the 80 course days occupy school weeks 1 to 16. Course-level checks are on days 35 and 79, with respond days 36 and 80.

No data change or sync is needed for this correction.

### 10. The Units table retains the older core headings and implicit year

**Location:** Units table header; Standard bullet; sensitive units’ Owned standards cells.  
**Severity:** Minor. **LAYER:** frame. **REPEAT:** new. **Confidence:** likely.

**Problem:** The requested after-core format calls for a Year column and the health heading “Skill steps.” This table retains `C3`, omits Year, and leaves sensitive ownership cells empty.

**Exact fix:** Add **Year** immediately after `#`, with **9** in every row; rename **C3** to **Skill steps**; replace the Standard bullet’s “C3 column” reference accordingly; write **None** in units 19 to 21’s ownership cells.

Keep this a single semester. Do not create four annual courses or additional checks.

## Lens checklist, course-frame layer

“Met” below means specified adequately for this layer, not verified in unwritten lessons.

| Lens requirement | Result |
|---|---|
| Named behavior outcomes and useful facts | Met as a frame specification. |
| All eight standards represented | Met. |
| Skill standards practiced across at least two non-sensitive topics | Placement met; performance qualifications in findings 2 and 3. |
| Explicit modeling, practice, fading support, and feedback | Met as specified. |
| Norms and pressure addressed | Missed in part: finding 8. |
| Topics recur with greater depth | Met through preceding-band retrieval and current applications. |
| Coverage traceable to units | Met through the unit outcome tags; full module expectations remain a later check. |
| Sensitive units independently removable | Missed in part: finding 4. |
| Getting help taught outside sensitive units | Met in units 4 and 8. |
| Correct grade-span indicators | Met. |
| Inclusive scenarios, privacy, and no shaming | Met as specified, subject to finding 1’s response distinction. |
| Family and trusted-adult links | Met as specified, including the 18-or-over choice rule. |
| Safe messaging and disclosure procedures | Specified; lesson-level accuracy and implementation remain later reads. |
| Science models used without unnecessary reteaching | Met at frame level. |
| Health and PE responsibilities distinguished | Met conceptually; calendar-specific handoffs need finding 5. |
| No collection of health information or medical advice by tools | Met as specified. |

## What is right and should not be touched

- The accepted **80-day, 45-minute semester** and short-unit structure.
- The sustained goal thread, private alternatives, and scoring of process rather than health outcomes.
- Non-sensitive ownership of every indicator practiced by removable units.
- Unseen cases, individual written evidence, cumulative checks, and carried performance records.
- Paper access, no required accounts or devices, and no product promotion.
- Sensitive-unit family notices, disclosure procedures, prohibition on harmful role play, and adult students’ own leave-out choice.

The three older prerequisite rows are correctly identified for readiness checks. The grade 8 ELA prerequisites precede this course, and the mathematics used stays within earlier learning.

## Settled by the expert

These are recommendations for the caller to apply; no files were changed.

| Choice | Reason | File touched |
|---|---|---|
| Retain current unit owners and day totals while restoring omitted indicator demands | The fixes fit existing cases, cards, and checks | Frame; affected health progression notes and local indicator descriptions |
| Separate ordinary disagreement from abuse before selecting a response | Prevents unsafe transfer of negotiation steps | Frame, unit 20 |
| Remove unit 19 as unit 20’s prerequisite | Preserves independent removal | Frame, unit 20 |
| Move week 8’s goal slot to day 37 | Protects respond time while preserving the thread | Frame |
| Treat the activity percentage as a gap, not a majority norm | Matches the opened survey evidence | Frame, unit 2 |
| Use current PE/SEL units and calendar positions | Resolves deferred handoffs without moving standards | Frame |
| Retain one semester despite adding Year 9 to the table | Makes the band format explicit without expanding scope | Frame |

## For Cory

- **Money only:** The frame’s proposed printing ceiling remains **$70 per semester for 30 students**, with the optional approximately **$45** food demonstration outside that ceiling. The arithmetic supports the estimate; setting the ceiling remains Cory’s decision.
- No new scope, audience, staffing, or outside-reader decision is required by these fixes.

## What I could not judge

This is a frame read, not the required medical-accuracy read of every lesson. Complete HECAT topic-module span tables, lesson keys, reading adaptations, observation timing, safety implementation, and local legal details remain unverified.

Two module-PDF attempts returned tool access errors; the complete HECAT PDF exceeded the tool’s size limit. The appendices opened successfully. The frame’s other memory-derived medical and research references, including the historical hour recommendation, were not treated as newly verified evidence.

No curricular finding in this report rests on memory alone.

## Outside sources and reading extent

- [SHAPE America, 2024 health standards](https://shapeamerica.org/standards/health/new-he-standards/): compared the published high-school indicators with the frame and local descriptions.
- [CDC HECAT Appendix 3](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_03.pdf): checked behavior-outcome meanings.
- [CDC HECAT Appendix 5](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_05.pdf): read scope-and-sequence guidance on coordination, reinforcement, and coverage.
- [CDC HECAT Appendix 7](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf): read assessment guidance on matching evidence to intended knowledge and skills.
- [CDC physical activity results](https://www.cdc.gov/yrbs/youth-health-in-focus/physical-activity.html): checked the current daily-activity percentage and survey year.
- [Love is respect, conflict resolution](https://www.loveisrespect.org/resources/conflict-resolution/): checked the distinction between ordinary disagreement and abuse.
- [National Domestic Violence Hotline guidance](https://www.thehotline.org/resources/should-i-go-to-couples-therapy-with-my-abusive-partner/): checked why shared conflict-solving assumptions do not transfer safely to abuse.
- [CDC HECAT 2021 edition](https://www.cdc.gov/healthy-youth/hecat/2021-edition.html): opened the official edition and module index; complete topic-module reading was not completed.

## For the source list

Add the working CDC 2025 activity-results page and the two relationship-safety pages above, with their uses and reading limits. The activity finding can now replace the earlier report’s memory-only support.

