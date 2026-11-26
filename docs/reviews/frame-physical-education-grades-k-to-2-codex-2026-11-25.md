# Second independent frame read: Physical Education, grades K to 2

Date: 2026-11-25  
Course: `physical-education-grades-k-to-2`  
Read-only report. No files were edited, created or deleted.  
**Finding count: 8**

## Verdict

The frame has a coherent developmental order, complete row placement and a workable full-length session budget, but it needs revision before scope and sequence writing. The largest risk is that complete code coverage hides incomplete teaching or assessment of several indicators. Preserve the unit structure and ownership, repair the coverage and assessment descriptions, and resolve the shared calendar and equipment conditions.

## What I read and checked

- The frame-read brief, `EXPERT.md`, the PE lens, the PE adoption bar, and the subject’s `STANDARD.md` and `APPROACH.md`.
- The complete course frame, its `frames.csv` record, and the 48 progression rows selected by `file:physical-education&grade:K|1|2`.
- All 49 span-2 indicator paraphrases, checked against the publisher’s current standards page.
- `calendar.csv`, `CALENDAR.md`, the after-core frame-writing rules, the PE band-edge file, and relevant settled decisions.
- The PE pre-work and progression reviews. Earlier findings are used to identify repeated defect types, not to treat historical reports as current instructions.
- The cited mathematics and social studies Units rows, plus the relevant Units rows of the existing health K to 2 frame.
- Foundation, approach and production guidance, applicable baseline rules, and the approach source registry.

There is no preceding PE course. The grades 3 to 5 PE frame does not exist yet, so its actual pickup of this band’s handoffs cannot be verified. No base text is claimed, so a source map is not applicable.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check physical-education-grades-k-to-2` | One failure: no scope-stage `days.csv` with `parts.csv` or `items.csv`. This is a frame-stage artifact; the read continued. |
| `python -X utf8 scripts/frame.py check physical-education-grades-k-to-2` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **70 files, 0 failures.** An unmarked stale statement remains, finding 8. |
| Independent placement count | **48 rows placed exactly once; 49 distinct owned indicators.** |
| Independent day count | **74 unit sessions plus 6 course-level sessions in each year: 240 total.** |
| Calendar comparison | All six PE check windows avoid core checks. Each overlaps another after-core subject, finding 3. |

## Findings, most serious first

### 1. Three owned indicators are narrowed in their teaching descriptions

**Severity:** Serious  
**LAYER:** frame, with standard and progression corrections  
**REPEAT:** yes, incomplete-indicator coverage was identified in the PE second-model pre-work read, finding 2  
**Confidence:** firm

**Location:** Units 7, 21 and 22; progression rows `k-express-feel`, `g2-show-ideas` and `g2-water-skills`; the `SHAPE.S4.2.3` paraphrase.

The descriptions do not securely carry the complete outcomes. The differences are visible against both the current indicator text and the repository’s full-coverage rule. [SHAPE America’s 2024 standards](https://shapeamerica.org/standards/pe/new-pe-standards/).

| Indicator and problem | Exact fix |
|---|---|
| **S4.2.3, unit 7:** Naming one feeling does not clearly establish ways movement benefits personal health. | Teach and check two benefits, drawing on unit 6: for example, helping the heart and helping the child feel calm. Broaden the standard paraphrase and row note accordingly. |
| **S2.2.4, unit 21:** The examples cover traveling and in-place movement but omit object handling. | Add a scarf-handling action to the sequence and check the child’s understanding across all three movement types. |
| **S2.2.12, unit 22:** The compulsory knowledge task covers safety rules, while swimming appears only as an optional in-water performance. | Add dry-land picture teaching and questions about floating and kicking for every school. Keep actual swimming within the school’s aquatics program. |

These changes complete existing ownership. They do not require moving indicators between units or adding a pool requirement.

### 2. The unit assessment descriptions do not consistently implement the promised assessment contract

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, the PE second-model pre-work read, finding 1, required explicit skill, knowledge and conduct evidence  
**Confidence:** firm

**Location:** Assessment bullet, grade outcomes, and Units table “Ends” descriptions.

The subject approach requires a skill task, a knowledge task and conduct evidence in every unit. Units 6, 7, 14 and 20 name no assessed motor cue. Units 2, 3, 4, 5, 9, 10 and 11 name no distinct knowledge task. Many units also leave their conduct behavior unnamed.

Some owned outcomes are taught but disappear from the named evidence. Unit 12 checks that the heart is a muscle, but not its strengthening through activity or the health benefit of regular activity. Unit 22 checks a difficulty and what helped, but not why a movement experience mattered. A scope writer could faithfully build the listed checks and leave these outcomes unverified.

This is also contrary to PECAT’s separate treatment of outcomes, teaching content and assessment, and Oregon’s requirement for aligned assessment evidence. [CDC PECAT, PDF page 35, printed page 31](https://www.cdc.gov/physical-activity-education/media/pdfs/2025/04/18_300595-A_PECAT_042619_508tagged_CR2025-04-07_revised-clean.pdf), [Oregon PE criteria, page 7](https://www.oregon.gov/ode/educator-resources/teachingcontent/instructional-materials/Documents/2025PhysicalEducationIMCriteria.pdf).

**Exact fix:**

- In units **6, 7, 14 and 20**, name a reviewed motor cue, observe it at the unit’s start, and repeat it at the check. Suitable choices are travel-and-freeze, soft landing, underhand tossing, and controlled direction changes, respectively.
- Add these brief knowledge prompts to the existing check sessions:

| Unit | Knowledge evidence to add |
|---|---|
| 2 | Identify the body parts supporting a pictured or demonstrated balance. |
| 3 | Show the ready-hands position and explain its job. |
| 4 | Show where the non-kicking foot goes. |
| 5 | Identify the safe swing space before striking. |
| 9 | Name the body parts receiving weight in the demonstrated transition. |
| 10 | Show which foot steps forward for the toss. |
| 11 | Identify the push-down action and choose a calming step after a miss. |

- In **unit 12**, ask how activity changes the heart over time and why regular activity helps health.
- In **unit 19**, observe an actual teacher-guided fair choice, such as sharing turns, rather than recording rule-following alone.
- In **unit 22**, add: “Choose a PE experience and say why it mattered to you.”
- Name one already-taught S3 behavior in every unit’s assessment description. Record it during practice, without adding a separate testing rotation.
- Append relevant indicator IDs to each grade’s S1 to S4 outcome statements, as `STANDARD.md` section 3 requires.

Keep the current session totals. These are short prompts and observations within existing assessment arrangements.

### 3. All six check windows collide with other after-core checks

**Severity:** Moderate, shared integration issue  
**LAYER:** process  
**REPEAT:** new  
**Confidence:** firm

**Location:** Course-level checks; `calendar.csv`; `CALENDAR.md`, stagger rule 1.

The frame satisfies the after-core brief’s explicit requirement to avoid core checks. However, the calendar’s broader K to 5 rule says that two subjects’ course-level checks cannot share a week. The current calendar contains these overlaps:

| Grade | PE window | Other subjects |
|---|---|---|
| K | Mid-year, week 18 | ELD, visual arts |
| K | Year-end, week 28 | ELD, library |
| 1 | Mid-year, week 18 | ELD, visual arts |
| 1 | Year-end, week 28 | ELD |
| 2 | Mid-year, week 17 | ELD, visual arts |
| 2 | Year-end, week 27 | ELD, health |

This is a shared scheduling conflict, not a PE row-placement failure. Leaving it invisible would reproduce the assessment load the calendar rule is intended to prevent.

**Exact fix:** Replace the speculative calendar discussion in “For the lead,” item 7, with the overlap table above and this statement:

> These PE windows avoid core checks but are provisional against the calendar’s all-subject stagger rule. The lead must coordinate the affected after-core frames before the calendar is finalized. Retain each course’s annual session total and assessment provision during that joint pass.

The broader rule’s intended scope needs the decision listed under “For Cory.” Do not independently move another worker’s checks.

### 4. The unconditional zero-cost, ordinary-room claim is not supported by the unit requirements

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, equipment, cost and ordinary-room completeness were raised in the PE pre-work read, finding 3  
**Confidence:** firm

**Location:** Space and equipment, supplies and cost, and paper-path bullets; units 9, 15, 18, 19 and 22.

The frame promises a complete path costing nothing, yet:

- Units 9 and 15 require suitable soft surfaces for weight shifts. Unit 9’s alternatives include grass, which does not solve the wet-weather indoor case.
- The low-equipment options explicitly include $20 for rope and $10 for striking substitutes.
- Unit 22 requires access to real life jackets for fastening practice and assessment. Borrowing is possible but not assured.

A teacher with a hard-floor classroom and no equipment cannot yet run the complete claimed path.

**Exact fix:** Replace “the low-equipment path costs nothing” with:

> Most activities use common materials. Complete delivery also requires access to the specified safe surface and real life jackets. Borrowed equipment may avoid purchases; availability must be confirmed. The listed low-equipment purchases are provisional, not a guaranteed zero-cost path.

Add a small unit-level list of **required access**, **safe substitute**, and **purchase needed if unavailable**. Explicitly identify the unresolved indoor surface and life-jacket conditions. Keep the required safety equipment rather than substituting pretend fastening for the practical task.

The spending or audience decision belongs to Cory.

### 5. Kindergarten omits the two early attempts that the settled rule expressly retains

**Severity:** Moderate  
**LAYER:** frame, progression  
**REPEAT:** yes, progression PE finding 1 and the subsequent settled exception  
**Confidence:** firm

**Location:** Unit 5; `k-bounce-throw-tries`; `STANDARD.md` section 3, rule 3.

The settled rule retains kindergarten attempts at continuous hand dribbling and a self-turned rope, with growth marked and ownership later. Unit 5 instead specifies bounce-and-catch and externally placed or turned ropes, then puts a self-turned rope out of scope. The progression note mentions the attempts but its concrete activity and assessment list does not secure them.

This repeats a gap already settled rather than reopening the owner grades.

**Exact fix:** Add to both the row’s concrete activity list and unit 5:

> Attempt repeated hand bounces and a self-turned rope with teacher support. Observe one cue at the first attempt and again later, recording growth without a required number of successful repetitions. Continuous bouncing is owned in unit 11; the rope pattern is owned in unit 18.

Replace unit 5’s exclusion with:

> Out: mastery of continuous hand dribbling and the self-turned rope pattern.

### 6. The stated 64-session path actually contains 70 sessions

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the same scheduling arithmetic defect appears in the grade 3 science frame reread, finding 5  
**Confidence:** firm

**Location:** “Shorter path,” lines 101 to 103.

Removing 10 sessions from 80 leaves **70**, not 64. The scope writer cannot produce the promised schedule from this instruction.

**Exact fix:** Replace the bullet with:

> **Shorter path.** The 64-session path removes 16 Fluency sessions from each year’s 80-session plan. It retains all first teaching, baselines, end-of-unit assessments, respond sessions and both course-level check windows. The scope and sequence identifies the 16 removable sessions by year and unit and verifies that every owned outcome remains taught and checked.

Delete “one or two a unit,” which cannot produce 16 removals across seven units. The removals must be allocated by actual practice load.

### 7. One named safety guide link does not provide a safety guide

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** new  
**Confidence:** firm

**Location:** Safety-read bullet and “For the lead,” item 5.

The Alberta URL currently opens a one-page relocation notice, not the cited 2014 guide. The Nova Scotia URL opens the actual 2021 guide. A later safety reader following the frame therefore receives only one usable guide. [Alberta link as opened](https://education.alberta.ca/media/160206/sg_pa_final_2014.pdf), [Nova Scotia guide](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf).

**Exact fix:** Remove Alberta from the usable-guide list and replace the corresponding lead note with:

> Nova Scotia’s 2021 guide is accessible. The listed Alberta address returns a relocation notice; it is not a verified safety source. Use the accessible guide for the required activity-specific read unless a replacement Alberta document is opened and checked.

Do not describe either guide as fully read by this review.

### 8. The cross-subject section incorrectly says the health frame has not been written

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, progression PE finding 8 and second-model pre-work finding 9  
**Confidence:** firm

**Location:** Cross-subject, line 257 and the following table.

“Their frames are not written” is false for `health-grades-k-to-2`. Its frame now supplies actual unit locations. The blanket statement hides a seam that can already be checked and updated.

**Exact fix:** Replace the sentence with:

> The health K to 2 frame exists. The links below name its current units. Dance and SEL frame locations remain unverified and are not assumed prerequisites.

Add these health locations to the table:

| PE link | Existing health location |
|---|---|
| Kindergarten movement, water and food habits | Unit 2 |
| Kindergarten calming | Unit 3 |
| Grade 1 food and water | Unit 8 |
| Grade 1 safe play | Unit 9 |
| Grade 2 outdoor and water safety | Unit 13 |
| Grade 2 inviting others to move | Unit 15 |

Retain the distinction between health’s habits and decisions and PE’s movement practice. Do not rewrite the dated historical reviews.

## Lens checklist, frame layer

| Lens line | Mark |
|---|---|
| Outcomes rather than a year of games | **Met.** Units have identifiable learning purposes. |
| Every standard represented in every grade | **Met in placement; evidence needs repair**, findings 1 and 2. |
| Every span indicator placed | **Met:** 49 owned once. |
| Developmental order, parts before combinations | **Met overall; kindergarten attempts need restoration**, finding 5. |
| Dance and fitness return | **Met.** Dance or expressive movement appears each year; fitness ideas recur. |
| Most students moving most of the time | **Met as a planning requirement.** Actual activity time awaits day plans. |
| Safe place to try; no elimination, punishment or public picking | **Met in the stated rules.** |
| Disability, injury and skill-range adaptations | **Met as a requirement.** Individual task adaptations await lower layers. |
| Gender-neutral participation and cultural breadth | **Met in intent.** Named cultural candidates still require their promised source checks. |
| Fitness learned privately, never ranked | **Met.** |
| Assessment shows growth | **Partly met**, finding 2. |
| Real space, weather and little equipment | **Partly met**, finding 4. |
| Health boundary and reciprocal links | **Partly met**, finding 8. |
| Dance boundary and reciprocal links | **Not yet verifiable:** dance frame unavailable. |
| Lesson-level cues, warm-up order, closure and waiting time | Requirements are stated; actual delivery is **not applicable to verification at this layer**. |

## What is right and should not be touched

- The 22-unit structure and annual 74-plus-6 budget.
- Fixed-setting skills before more complex combinations.
- Explicit cue-word and model introductions, including teaching jump-and-land cues before traveling uses them.
- Retrieval from the preceding grade, with no invented earlier-course prerequisite for kindergarten.
- Private growth records, picture-led materials, oral responses and separation of language proficiency from movement evidence.
- Dry-land water teaching for every school, with actual swimming reserved for the school’s aquatics program.
- The longer allocations for introductory routines and the final water-and-reflection unit. I found no unit so over- or under-allocated that a day transfer is justified from this frame alone.

## Settled by the expert

| Choice | Reason | File touched by the later fix |
|---|---|---|
| Keep current unit ownership and full-course day totals | Placement and totals are correct | Course frame |
| Complete swimming knowledge through dry-land pictures and oral responses | Completes existing knowledge ownership without requiring swimming participation | Unit 22; `g2-water-skills` |
| Use reviewed motor cues in concept and choice units | Supplies growth evidence without introducing later-grade ownership | Units 6, 7, 14, 20 |
| Retain later ownership of bouncing and rope patterns | Cory already settled it; kindergarten needs attempts | Unit 5; `k-bounce-throw-tries` |
| Correct the short-path reduction to 16 | Arithmetic required by the already chosen 64-session target | Shorter-path bullet |
| Remove the unusable Alberta citation pending verification | The linked document is a relocation notice | Safety-read bullet |

## For Cory

1. **Audience and money:** Must the complete course remain runnable with no purchases in a hard-floor room, or may it require confirmed access to borrowed mats and life jackets? The present unconditional zero-cost claim cannot stand.
2. **Scheduling scope:** Confirm whether the calendar’s one-subject-per-week rule covers all after-core subjects. The current calendar says it does, while the after-core writing brief explicitly checks only against core subjects. The lead needs one consistent rule before coordinating the overlapping windows.

## What I could not judge

- The next PE band’s actual pickup of these handoffs, because its frame is absent.
- Real 30-minute feasibility, activity intensity, observation capacity and complete wet-weather adaptations, because day plans do not exist.
- Cultural provenance and permission for the candidate dances and games. Those selections remain **from memory**, as the frame acknowledges.
- Current equipment prices or a guaranteed borrowing arrangement. The frame’s amounts remain provisional estimates.
- Activity-specific safety compliance. This was a frame read, not the required safety-agent read.

Saved memory informed report organization and the habit of independently checking counts. No substantive PE finding rests on unverified model memory.

## Sources and reading limits

- [SHAPE America, 2024 PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/): checked all span-2 indicators against the frame.
- [CDC, PECAT 2019](https://www.cdc.gov/physical-activity-education/media/pdfs/2025/04/18_300595-A_PECAT_042619_508tagged_CR2025-04-07_revised-clean.pdf): read the standards-analysis directions and relevant K to 2 motor tables, PDF pages 34 to 37. Its older five-standard structure was kept distinct.
- [Oregon, 2025 PE adoption criteria](https://www.oregon.gov/ode/educator-resources/teachingcontent/instructional-materials/Documents/2025PhysicalEducationIMCriteria.pdf): examined alignment, progression and assessment sections.
- [Appropriate instructional practices comparison](https://www.shapeamerica.org/Common/Uploaded%20files/uploads/pdfs/Appropriate-Instructional-Practices-Grid.pdf): consulted relevant learning-environment and participation guidance.
- [SHAPE America national guidelines](https://shapeamerica.org/standards/guidelines/): verified the elementary weekly recommendation. The frame correctly discloses its lower dose.
- [CDC, drowning prevention](https://www.cdc.gov/drowning/prevention/index.html): read the prevention guidance.
- [American Red Cross, water safety](https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/water-safety.html): read the distinction between swimming skills, water knowledge and helping others.
- [Nova Scotia, 2021 safety guide](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf): verified document identity and accessibility; not read in full.
- [Listed Alberta safety URL](https://education.alberta.ca/media/160206/sg_pa_final_2014.pdf): opened and found a relocation notice.

## For the source list

Record the Alberta address as a relocation notice rather than a usable guide. Add the Red Cross water-safety page if it is not already recorded, with its use limited here to water knowledge and the distinction from actual swimming performance.

