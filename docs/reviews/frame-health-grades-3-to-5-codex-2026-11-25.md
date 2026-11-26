# Second-model frame read: Health, grades 3 to 5

**Date:** November 25, 2026  
**Course:** `health-grades-3-to-5`  
**Delivery:** Complete report supplied here. No files changed.

## Verdict

**Revise before scope-and-sequence writing.** The three-year structure is coherent, every selected progression row is placed once, and sensitive units can be omitted without removing unique indicator ownership. The most important changes are to correct the puberty and bullying statements and ensure assessment evidence matches the actions and explanations the standards require.

**Finding count: 5.**

## What I read and checked

I read the complete [course frame](S:/CurioClass/docs/courses/health-grades-3-to-5/frame.md), its entries in `course-list.csv` and `frames.csv`, all 60 health progression rows selected by `file:health&grade:3|4|5`, the local NHES and HECAT descriptions, and the course’s 33 stored calendar rows.

The review also used:

- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, and the health lens.
- The health adoption bar, `STANDARD.md`, and `APPROACH.md`.
- Foundation, shared approach, production, glossary, calendar, and relevant decision rules.
- The neighboring health frames, including their handoff tables.
- The named PE, SEL, and grade 4 ELA units and their calendar positions.
- Earlier health pre-work, progression, and K-to-2 frame reviews, to identify repeated findings.
- The outside sources linked below.

There is no base text, so a base-text source map is not applicable.

### Checks

Commands used `-B` to prevent Python bytecode writes.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check health-grades-3-to-5` | One failure: lesson-stage `days.csv` with `parts.csv` or `items.csv` is absent. Course-filtered to honor AGENTS.md. |
| `python -X utf8 scripts/frame.py check health-grades-3-to-5` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | One failure in the unrelated PE grades 9-to-12 frame. The health review continued. |
| Selected skills | **60 selected, 60 placements, no duplicates or omissions.** |
| Indicator ownership | **39 indicators, each owned once:** grade 3 owns 11; grades 4 and 5 own 14 each. |
| Annual standards | All eight standards appear in each year’s non-sensitive rows. |
| Annual allocation | Grade 3: 26 unit sessions plus 4 course-level sessions. Grade 4: 26 plus 4. Grade 5: 25 plus 5. |
| Stored calendar | All **33 rows match** the calendar calculated from the current frame. |
| Core-check separation | All six health course-level checks avoid their grade’s core-check weeks. |

The structural pass establishes placement and arithmetic, not full instructional coverage.

## Findings, most serious first

### 1. The puberty unit gives inaccurate reassurance about timing

**Location:** Frame unit 14, line 300; progression row `g4-sh-body-changes`.  
**Severity:** Serious. **LAYER:** frame and progression. **REPEAT:** new. **Confidence:** firm.

**Problem:** Unit 14 promises puberty teaching “before it starts” and says “all timings are normal.” Neither statement is reliable. Puberty can begin within the usual range before grade 4, and unusually early or late development can need professional evaluation. Both NIH and pediatric guidance distinguish normal variation from timing that warrants attention. [NIH puberty guidance](https://www.nichd.nih.gov/health/topics/factsheets/puberty), [pediatric guidance](https://www.healthychildren.org/English/ages-stages/gradeschool/puberty/Pages/Physical-Development-of-School-Age-Children.aspx).

**Why it matters:** A teacher could give false reassurance, while a child whose changes have already begun could hear that the course expected otherwise.

**Exact fix:**

Replace the relevant sentence in the frame and progression notes with:

> Puberty in plain, correct terms: body changes and hygiene, wide variation in when changes begin, privacy, and who to ask. Changes may already have begun for some students. A question or concern about development can be taken privately to a trusted adult or health professional.

Add this teacher direction:

> Do not judge an individual student’s development or reassure them that every timing is normal. Refer individual concerns through the school’s health process.

Retain the early-development line in the leave-out note. The separate question of earlier preparation belongs to Cory, below.

### 2. The bullying definition omits the feature that distinguishes bullying from ordinary conflict

**Location:** Frame unit 4, line 290; seam table line 175; Models carried line 277; progression row `g3-v-bullying`.  
**Severity:** Serious. **LAYER:** frame and progression. **REPEAT:** new. **Confidence:** firm.

**Problem:** “Repeated unkind acts that hurt” omits a real or perceived power imbalance and excludes behavior that is highly likely to recur. The seam also describes applying conflict steps to bullying without explaining the limit of that transfer.

Federal definitions include unequal power and repetition or likely repetition. Federal response guidance cautions against treating bullying as a dispute between equally powerful children who should resolve it together. [Bullying definition](https://www.stopbullying.gov/bullying/what-is-bullying), [CDC definition](https://www.cdc.gov/youth-violence/about/about-bullying.html), [response guidance](https://www.stopbullying.gov/prevention/support-the-children-involved).

**Why it matters:** Students may misclassify bullying or be expected to negotiate with someone who has power over them.

**Exact fix:**

Replace the definition in the frame and progression row with:

> Bullying is unwanted behavior that hurts or threatens someone, involves unequal power, and happens again or is likely to happen again. Power can come from strength, popularity, information, or a group.

Add two short contrasting cases to day 3: an ordinary disagreement and a bullying situation. Require students to identify the difference and choose a safe response.

Replace the seam’s transfer statement with:

> Retrieve listening and calming skills, then distinguish disagreement from bullying. In bullying, prioritize safety, supporting the person targeted, and getting adult help. Do not require compromise or a joint problem-solving conversation.

Keep the existing prohibition on students acting the bullying.

### 3. Two indicator judgments can be made without the required evidence

**Location:** End-of-unit evidence, lines 68 to 80; units 4 and 9, lines 290 and 295; course-level checks, lines 318 and 319; local description of `NHES.S1.5.4`.  
**Severity:** Serious. **LAYER:** standard and frame. **REPEAT:** yes, assessment evidence that substitutes for an indicator’s required action recurred in the K-to-2 second-model read. **Confidence:** likely.

**Problem:** The frame strengthens several performance records, but two gaps remain.

| Indicator | Current gap | Exact fix |
|---|---|---|
| `NHES.S4.5.2` | Unit 4 checks “the listening steps for a scene.” Its named individual observation records the I-statement, not active listening. Naming listening steps does not establish their use. | During days 3 to 5, record each student attending to an unfamiliar short message, asking a relevant question, and accurately saying back its meaning in two settings. Use accessible communication, including text or AAC where appropriate. Carry that record into the unit judgment; keep the written scenario as additional evidence. |
| `NHES.S1.5.4` | The local description substitutes “show” for the standard’s explanatory demand. Unit 9’s carried evidence can be a generic handwashing, water-break, or warm-up demonstration, with no assessed explanation of managing a condition. | Rewrite the local description in original words: “Students explain ways to carry out healthy behaviors, including ways people manage health conditions.” In unit 9, add an unfamiliar character case requiring an explanation of a taught routine and how an adult-supported condition plan helps the character. Keep generic routine demonstrations as useful additional evidence. |

The live indicators distinguish using active listening from explaining health behaviors and condition management. [2024 NHES indicators](https://shapeamerica.org/standards/health/new-he-standards/). HECAT likewise asks whether assessment measures match instructional intent. [HECAT Appendix 7, PDF page 1, printed APX-26](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf).

**Why it matters:** A student can otherwise receive “met” through procedural recall or an unrelated routine while the required learning remains unverified.

These fixes preserve the existing indicator owners and unit allocations.

### 4. Coordination notes still describe absent frames and outdated SEL cards

**Location:** Cross-subject, lines 328 to 360; For the lead, items 5 and 6, lines 393 to 398; Units table header, line 285.  
**Severity:** Moderate. **LAYER:** process. **REPEAT:** yes, stale neighbor-frame availability notes were identified in the K-to-2 frame read. **Confidence:** firm.

**Problem:** The frame says the PE frame is unwritten and postpones work until the SEL frame is written. Both exist. Grade 4 and grade 5 SEL references use year-relative unit numbers rather than the existing frame’s continuous numbering.

The justification for keeping two decision cards also says SEL’s three words lack options and results. Its current grade 3 card explicitly includes listing choices, considering consequences, choosing, and checking.

**Why it matters:** Writers can follow incorrect references, repeat teaching unnecessarily, or miss the actual timing relationship between courses.

**Exact fix:**

Replace the availability statements with current references:

| Health connection | Existing receiving or supporting unit and weeks |
|---|---|
| Grade 3 activity | PE unit 4, weeks 14 to 17; PE unit 7, weeks 27 to 29 |
| Grade 4 activity | PE unit 9, weeks 1 to 4 |
| Grade 5 activity | PE unit 17, weeks 1 to 6 |
| Grade 5 food and drink for activity | PE unit 20, weeks 15 to 17 |
| Grade 4 SEL goals | SEL unit 8, weeks 6 to 10 |
| Grade 4 SEL feelings and calming | SEL unit 10, weeks 16 to 21 |
| Grade 4 SEL help, refusal, and speaking up | SEL unit 11, weeks 21 to 25 |
| Grade 4 SEL decisions and checking claims | SEL unit 12, weeks 27 to 32 |
| Grade 5 SEL calming | SEL unit 13, weeks 1 to 5 |
| Grade 5 SEL goals | SEL unit 14, weeks 6 to 10 |
| Grade 5 SEL relationships and refusal | SEL unit 16, weeks 16 to 21 |
| Grade 5 SEL speaking up | SEL unit 17, weeks 21 to 26 |
| Grade 5 SEL decisions | SEL unit 18, weeks 27 to 32 |

Use these actual positions in the cross-subject table. Retain bridges where health comes first, particularly health’s grade 5 water explanation before PE unit 20.

Replace For the lead item 5’s decision-card rationale with:

> SEL’s current card already includes options, consequences, choice, and checking. Health applies that shared process to health situations and adds the explicit question of whether adult help is needed. Name the shared steps and the health-specific addition in both courses.

As part of the same template refresh, rename the seventh Units column **Skill steps** and replace blank Owned standards cells with **None**, following the after-core brief.

### 5. Grade 4’s materials total is understated by one dollar

**Location:** Unit costs, lines 294 to 300; annual total, line 309; For the lead item 8, line 402.  
**Severity:** Minor. **LAYER:** frame. **REPEAT:** yes, materials arithmetic was also a finding in the K-to-2 second-model read. **Confidence:** firm.

**Problem:** Grade 4’s listed costs are:

`$3 + $3 + $3 + $3 + $3 + $2 + $3 = $20`

The annual summary and supplies-ceiling note say $19.

**Why it matters:** The proposed budget is based on an incorrect total.

**Exact fix:** Change both grade 4 summary amounts to **$20**. Keep grade 3 at **$18** and grade 5 at **$20**, which match their listed unit costs. Prices remain provisional; this finding concerns arithmetic.

## Coverage, sequence, time, and seams

The selected progression skills and indicator owners are complete. Preparation and reuse of indicators owned later in the band are marked as practice. Unique owners remain in non-sensitive units, and each sensitive unit names a non-sensitive use for its optional days.

The main instructional order holds: help precedes sensitive applications, source checking precedes later claims work, and goal planning precedes tracking and reflection. The grade 5 advocacy unit counts drafting, feedback, revision, and delivery. Neighboring health frames pick up the named handoffs.

The annual arithmetic is sound: **30 sessions of 30 minutes equals 15 hours per year**. The lower dose is an existing Cory decision, not a new defect. The historical 80-hour comparison was not independently reverified in this read.

No unit is demonstrably far over its share. The two-session sensitive units remain tight, especially unit 14, but a precise minimum cannot be established without the planned module reads and lesson timings. HECAT asks planners to provide enough time for introduction, reinforcement, and skill development. [Appendix 5, PDF page 2, printed APX-19](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_05.pdf).

The stored calendar has these after-core collisions:

| Grade | Health check week | Other courses |
|---|---:|---|
| 3 | 15 | Music |
| 3 | 29 | Library |
| 4 | 14 | Library |
| 4 | 29 | ELD and library |
| 5 | 15 | Music and SEL |
| 5 | 28 | ELD and library |

These remain for the lead’s shared calendar pass, as the frame already acknowledges. They do not invalidate this frame’s successful separation from core-check weeks.

## Health lens checklist

“Met” means adequately specified at frame level, not demonstrated in finished lessons.

| Lens requirement | Result |
|---|---|
| Named behavior outcomes and useful facts | Met in design; factual corrections in findings 1 and 2 |
| Skills explained, modeled, practiced, and given feedback | Met in intent |
| Norms and social pressure addressed | Met in design; final sources remain due |
| No fear, shame, or blame | Met |
| Families, trusted adults, and help routes included | Met |
| Inclusive participation without required disclosure | Met |
| Sufficient time and spaced return | Provisionally met; short sensitive units require timing checks |
| All eight standards reached | Met each year |
| Skill standards practiced across at least two topics | Met in the specified tasks, including physical activity goal work |
| Coverage locations identified | Unit outcome tags present; full matrices remain due at scope stage |
| Topics recur across the band | Met at frame level |
| Sensitive units removable without losing unique skills | Met |
| Getting help taught outside sensitive units | Met every year |
| Indicators used within the correct span | Met |
| Assessments require more than recall | Part met: finding 3 |
| Skills have steps, models, and practice | Met in design |
| Figures have sources and dates | Required; actual figures remain unjudged |
| Content fits the age and is accurate | Part met: findings 1 and 2 |
| Home links and advance sensitive-unit notes | Met |
| Original indicator wording preserves meaning | Part met: finding 3 |
| No required personal health or family disclosure | Met |
| No weighing, calorie counting, or good/bad food labels | Met |
| Suicide and self-harm safeguards | Not applicable to this band’s planned content |
| Tools collect no health information or give medical advice | Met as an explicit constraint |
| Health states early facts without assuming unavailable science | Met |
| Health and PE divide explanation, planning, and movement | Met in principle; update references under finding 4 |

## What is right and should remain

- The Year column, continuous unit numbering, and complete annual check structures.
- Non-sensitive ownership of every unique indicator.
- Removable sensitive units with advance family notes and disclosure directions.
- Accessible paper tasks, read-aloud options, and communication accommodations.
- Safe school habits and goals, scored without judging bodies, home circumstances, or success.
- The explicit doing records in unit 15 and real-audience delivery in unit 19.

## Settled by the expert

| Choice | Reason | Files affected by a later fix |
|---|---|---|
| Keep 21 units, 90 sessions, and existing indicator owners | Structural placement and annual allocations hold | Health frame |
| Replace absolute puberty reassurance with accurate variation and private referral wording | Corrects a factual error without diagnosing students | Frame and health progression |
| Distinguish bullying from ordinary disagreement | Protects the intended safety response | Frame and health progression |
| Record active listening and assess an explanation of condition management | Evidence must match the indicator | Frame and local indicator description |
| Replace obsolete peer references and card descriptions | Existing frames settle availability and timing | Frame and reciprocal references |
| Correct grade 4’s materials total to $20 | Sum of listed costs | Frame |

## What I could not judge

- Finished lesson timing, scoring guides, or classroom effectiveness.
- Complete medical and scientific accuracy. This was a targeted frame read, not the separate dated unit/day accuracy read.
- Full coverage of all nine HECAT modules’ span expectations. I consulted the food and nutrition and sexual health tables selectively.
- Current purchasing prices, final survey-source choices, or the historical national-hours citation.

The promised module reads remain necessary. Their results should determine additions and time, rather than assuming every addition fits in a single sentence.

## Outside sources and memory

- [2024 NHES indicators](https://shapeamerica.org/standards/health/new-he-standards/): checked indicator meaning and assessment demands.
- [NIH puberty guidance](https://www.nichd.nih.gov/health/topics/factsheets/puberty) and [pediatric puberty guidance](https://www.healthychildren.org/English/ages-stages/gradeschool/puberty/Pages/Physical-Development-of-School-Age-Children.aspx): checked timing and the limits of reassurance.
- [Federal bullying definition](https://www.stopbullying.gov/bullying/what-is-bullying), [CDC bullying definition](https://www.cdc.gov/youth-violence/about/about-bullying.html), and [response guidance](https://www.stopbullying.gov/prevention/support-the-children-involved): checked definition and response distinctions.
- [HECAT Appendix 5](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_05.pdf): checked sequencing and time principles.
- [HECAT Appendix 7](https://www.cdc.gov/healthy-youth/hecat/pdfs/HECAT_Appendix_07.pdf): checked assessment alignment.
- [HECAT food and nutrition module](https://www.cdc.gov/healthy-youth/hecat/pdfs/hecat_module_fn.pdf) and [sexual health module](https://www.cdc.gov/healthy-youth/hecat/pdfs/hecat_module_sh.pdf): consulted selected band expectations.

No substantive finding rests on memory. Saved memory informed report organization only. The frame’s deferred safety links were not independently verified here.

**For the source list:** The federal bullying definition and response pages are useful additions to the grade 3 unit’s named reading sources.

## For Cory

- **Scope:** Grade 4 unit 14 cannot promise preparation before puberty begins. Decide whether to add brief preparation within the existing grade 3 sensitive unit or provide an earlier family-facing preparation route. This report does not move content between units.
- **Money:** The proposed $30 annual supplies ceiling remains a decision. Corrected listed totals are grade 3 **$18**, grade 4 **$20**, and grade 5 **$20**. The optional snack event’s estimated $30 food cost is separate.

