# Independent frame read: Physical Education, grades 3 to 5

Date: 2026-11-25  
Course: `physical-education-grades-3-to-5`  
Findings: **7**  
Read-only review. No files changed.

## Verdict

The frame has a sound developmental order, complete placement of its progression rows, and three independently runnable years. It needs corrections before scope and sequence writing: the most serious problems are unsafe floor-work substitutions and assessment descriptions that omit owned skills. Preserve the course structure and day allocations while correcting those instructions, completing cultural-source decisions, and refreshing references to work that landed during this review.

## What I read and checked

- The frame-read brief, applicable after-core frame-write rules, EXPERT guidance, PE lens, PE adoption bar, STANDARD and APPROACH.
- Relevant foundation, shared approach, production, glossary, calendar and decision rules.
- The course frame, its `frames.csv` entry, its `course-list.csv` selector, all selected progression rows, span-5 standard paraphrases and 36 calendar rows.
- The neighboring PE frames’ unit and handoff material, the progression edge document, and relevant earlier PE review findings and fix dispositions.
- Referenced core Units tables and relevant health and newly landed SEL units. The dance grades 3 to 5 frame remained absent.
- Outside sources linked below. No substantive finding rests on memory.

## Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check physical-education-grades-3-to-5` | Final run: 3 failures, all stale SEL Pending markers in this frame |
| `python -X utf8 scripts/stale.py check` | Final run: the same 3 failures |
| Course-filtered `plan.py check physical-education-grades-3-to-5` | Reports missing downstream plan-stage files; this frame has no `days.csv` with assessment data yet |
| Course gate | Not run because it writes output and baseline files, contrary to this review’s read-only boundary |

The first structural run passed; the final run detected the SEL frame that landed during the review. Neither result prevents the content verdict.

## Findings, most serious first

### 1. The floor-work fallback permits unsuitable surfaces and contradicts the medical restriction

**Severity:** Major  
**LAYER:** frame, with progression correction  
**REPEAT:** yes, safety and equipment adequacy were raised in earlier PE reads  
**Confidence:** firm

**Location:** Frame, “Required access,” and unit 3’s teacher notes; progression row `g3-body-roll`.

**Problem and cost:** Required access permits “mats from the school’s stock, or carpet” for rolls, weight shifts and routine floor work. Ordinary carpet is not an adequate specification for tumbling protection. Both named safety resources specify suitable gymnastics mats for floor work and tumbling. [SPHEReS gymnastics guidance](https://myspheres.ca/en/fundamental-reading/gymnastics-facilities/), [Nova Scotia safety guidelines, PDF pages 88 to 89, printed pages 76 to 77](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf).

Unit 3 also says no rolling for a child with a neck or back concern, then offers “a log roll or a standing balance task instead.” A log roll remains rolling. The progression contains the same contradiction. A writer could turn either line into an unsafe adaptation.

**Exact fix:**

- Replace the carpet alternative with: “Rolls and tumbling floor work require suitable gymnastics mats, inspected and secured according to the school’s policy and the cited safety guidance. Ordinary carpet alone is not a substitute.”
- Replace unit 3’s medical alternative with: “Where the family’s or nurse’s guidance excludes rolling, no roll is attempted. Use an allowed standing balance or other permitted movement task.”
- Make the same correction in `g3-body-roll`.
- State that a standing substitute preserves participation but does not establish performance of a rolling indicator. Record the adaptation without claiming an unperformed skill.

This tightens the pilot fix’s general “soft surface” wording using the actual safety sections.

### 2. Several owned outcomes disappear from the named assessment evidence

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the K to 2 second-model read identified the same assessment-contract problem  
**Confidence:** firm

**Location:** Units 1, 2, 5, 11, 12 and 23, “Ends.”

**Problem and cost:** The teaching descriptions include the following outcomes, but their specified assessment tasks do not consistently check them. General observation of participation cannot substitute for named evidence of an owned outcome. The repository’s full-standard rule and PECAT’s separate outcome, content and assessment analysis both require that connection. [CDC PECAT](https://www.cdc.gov/assessing-improving-school-health/pecat/index.html).

| Unit | Missing evidence | Exact addition |
|---|---|---|
| 1 | Need for a cool-down, S2.5.11 | Ask the child to select and explain a suitable warm-up **and** cool-down for pictured activities. |
| 2 | Rolling a ball, S1.5.9 | Add a fixed-position roll to a target, with its own cue mark, within the two-day assessment window. |
| 5 | Instep kicking, S1.5.18; stationary hand dribbling within S1.5.19 | Make the foot task a kick-to-target followed by the cone dribble. Extend the carried hand-dribble observation to include stationary control and traveling control, marked separately. |
| 11 | Describing another person’s perspective, S3.5.1 | Add: “Explain how the left-out player sees this pictured game.” Taking a negotiated role checks S3.5.2, not this outcome. |
| 12 | Actual below-waist hand striking, S1.5.14 | Require observed above-waist and below-waist contacts with separate marks. Showing hand positions and naming ball heights checks knowledge, not contact performance. |
| 23 | Reach rescue in the progression’s promised dry-land skill set | Observe and carry the reach-rescue mark from a final practice closure; retain the throw-rescue and life-jacket task on Check day. |

**Exact fix:** Insert these tasks into the relevant Ends cells and name where each mark is collected. Use the existing two-day windows or carried closure evidence after teaching and practice. Retain the existing respond days and do not compress extra tasks into an unchanged three-minute visit without revising its timing.

These additions check actions already taught and claimed. They do not move standards between units.

### 3. S3.5.5 is narrowed from three working arrangements to an optional choice

**Severity:** Moderate  
**LAYER:** frame, progression and standard  
**REPEAT:** yes, incomplete-indicator coverage recurs in earlier PE reads  
**Confidence:** firm

**Location:** Unit 18; progression row `g5-conflict-solve`; local paraphrase of `SHAPE.S3.5.5`.

**Problem and cost:** The published indicator includes solving problems independently, with partners, **and** in small groups. The local paraphrase and progression use “or,” and unit 18’s assessment can be satisfied by one team disagreement. That leaves independent and partner problem solving optional. [2024 PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/).

**Exact fix:** Replace the optional wording with “independently, with a partner, and in a small group.” Name three taught and observed applications inside unit 18:

1. Independently choose and test a safe response to an equipment or space problem.
2. With a partner, agree and test a fair turn-taking solution.
3. In a small group, resolve an invented or naturally occurring game-call problem.

The final conduct judgment may summarize these observations once. Keep the existing protection against making one child act as another child’s aggressor.

### 4. Cultural selections are fixed before the required source decisions are complete

**Severity:** Moderate  
**LAYER:** process, affecting frame  
**REPEAT:** yes, cultural sourcing was raised in the progression and K to 2 reads  
**Confidence:** firm

**Location:** Units 8, 15 and 16; “Sensitivity reads”; For the lead 7.

**Problem and cost:** The units call the activities “Picks,” while For the lead 7 explicitly says the community-source confirmations were not completed. APPROACH requires the cultural claim to be checked before the unit names the activity and requires evidence that it is open to teaching. Deferring that decision leaves the scope writer with apparently settled selections.

This review found useful primary evidence: the Canadian film board’s education notes explicitly suggest teaching a folk dance to La Bastringue, and the Philippine education department publishes Tinikling teaching modules. These support educational use, but do not grant permission to copy recordings, films or instructional text. [La Bastringue education notes](https://www.onf.ca/film/bastringue_madame_bolduc/), [Philippine education department resource](https://lrmds.deped.gov.ph/detail/21899).

**Exact fix:**

- Add those exact links and their supported claims to units 15 and 16.
- Until their required source checks are recorded, label the remaining selections “Candidate,” including Virginia Reel, Alunelul and jianzi.
- State what remains to verify for each: cultural description, suitability for open teaching, and the particular adaptation used.
- Preserve each unit’s outcomes and days while the selection is settled.

The [Library of Congress record](https://www.loc.gov/item/afcreed000072/) returned **403: browser check**. It was not fetched another way. The alternative [museum record](https://www.thehenryford.org/collections/explore/artifact/399894?AssetId=THF119656) supports historical context, not the complete teaching decision.

### 5. Two readiness checks count from ownership rather than the frame’s last use

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, readiness and retrieval classification is an established frame-review issue  
**Confidence:** firm

**Location:** “Readiness and retrieval,” Seams, and units 21 and 22.

**Problem and cost:** The frame calls `g3-strike-tools` and `g3-rope` two-grade gaps. Yet grade 4 unit 12 explicitly retrieves and uses unit 6’s paddle striking, and grade 4 unit 15 revisits a rope pattern. The stated readiness rule counts from last use, not just the owner grade. The frame therefore allocates two formal readiness windows where its own intervening instruction supports retrieval.

**Exact fix:**

- Change unit 21’s `g3-strike-tools` opening to retrieval of grade 4 unit 12’s striking use.
- Change unit 22’s rope opening to retrieval of grade 4 unit 15’s rope pattern.
- Remove the associated mandatory ten-minute readiness allocations on grade 5 days 45 and 54.
- Change “Six assumed rows” to four and retain the four genuinely older prerequisite checks already listed.
- If a separate long-tool diagnostic is desired because grade 4 refreshed only short-tool striking, name that narrower purpose explicitly rather than describing the entire row as unused.

### 6. Unit 17 places its final check on its respond day

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Unit 17, goal-duration sentence and Ends.

**Problem and cost:** The 14-day unit ends with two check days followed by one respond day. Those are days 12, 13 and 14. Its earlier sentence nevertheless places “the check on day 14,” giving the scope writer contradictory instructions.

**Exact fix:** Replace that sentence with:

> The goal runs from the baseline on day 3 through the assessment window on days 12 and 13, about four weeks on the default dose. Day 14 responds to the assessment.

Keep the 14-day allocation.

### 7. Refresh stale reconciliation notes and incorrect summary metadata

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale notes were identified in earlier PE reads  
**Confidence:** firm

**Location:** Cross-subject; For the lead 3, 4, 5 and 6; Course in brief; Units header.

**Problem and cost:** The final structural check identifies three obsolete SEL Pending markers. Other text also sends the lead back to decisions or edits already present. These notes can cause duplicate work or incorrect sequencing.

**Exact fix:**

- Replace the three SEL Pending markers with the landed units:
  - Grade 3 calming: SEL unit 1, weeks 1 to 6.
  - Grade 3 talk and disagreement work: unit 4, weeks 17 to 21.
  - Grade 4 calming: unit 10, weeks 16 to 21; disagreement work: unit 11, weeks 21 to 25.
  - Grade 5 calming: unit 13, weeks 1 to 5; disagreement work: unit 16, weeks 16 to 21.
- Delete the claim that the calming rows occupy SEL’s first unit every year. Where PE precedes the later SEL treatment, specify retrieval of the earlier shared card and PE’s own contextual teaching.
- Replace For the lead 4’s proposed bar-graph note change with “Applied in `g5-goal`.” The progression already contains that fallback. Remove references to the nonexistent “Row changes” section.
- Rename the Units header `C3` to `Cues and settings`, as the current after-core brief already requires; remove the obsolete request to decide that rename.
- Correct “48 rows” to **49**, comprising **18 in grade 3, 17 in grade 4 and 14 in grade 5**. Replace the “17 ... rows a year” pacing justification with those actual counts.
- Update For the lead 5’s clash record: visual arts overlaps PE in grade 3 weeks 18 and 26 and grade 5 weeks 18 and 26. No overlap appeared for grade 4 in the checked calendar. Leave resolution with the lead’s calendar pass.

The dance Pending marker remains accurate.

## Data checks and lens checklist

| Requirement | Result |
|---|---|
| Owned skills | Met: all 49 selected rows placed exactly once |
| Standard ownership | Met structurally: all 57 span-5 indicators have exactly one owner unit |
| Standards taught and checked in full | Missed: findings 2 and 3 |
| Units and developmental order | Met: patterns precede combinations and game applications |
| Days | Met: each year has 74 unit days plus 6 course-level check/respond days |
| Unit allocations | Broadly proportionate; no unit is clearly excessive or insufficient |
| Calendar | All 36 course rows match the stated allocations; check and respond weeks 18 and 26 avoid core check weeks |
| Every year whole | Met: eight units, unit assessments and two course-level checks per year |
| Incoming and outgoing seams | Row and unit handoffs match; readiness classification needs finding 5 |
| Core subject leans | Met: later science and coordinate-graph work have explicit bridges or earlier alternatives |
| Health and SEL overlap | Health roles are distinguished; SEL references need finding 7 |
| Dance overlap | Pending: neighboring dance frame absent |
| Outcomes rather than a year of games | Met |
| Dance and fitness recur | Met across the three years |
| Most students moving | Supported at frame level by stations, pairs and small-sided games; actual lesson timing remains untested |
| Safe place to try | Generally met; floor-work instructions need finding 1 |
| Disability, injury and skill adaptations | Required throughout; medical rolling alternative needs correction |
| Fitness privacy and growth | Met: private records, cue judgments and comparison with the child’s own baseline |
| Real space, weather and equipment | Addressed, subject to the mat requirement correction |
| Base text and source map | Not applicable: no base text |
| Detailed unit/day lens lines | Deferred to unit and lesson reads |

## What is right and should not be touched

- Preserve the three complete grade years and the progression from patterns to changing conditions to combinations.
- Preserve private fitness records, oral or demonstrated knowledge responses, and the separation of language proficiency from movement performance.
- Preserve dry-land water-safety instruction and the school’s control of any in-water program.
- Preserve recurring dance, fitness and skill applications, along with the explicit gap between the planned PE dose and national weekly-minute guidance.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Require suitable gymnastics mats for rolling and tumbling | Two opened safety resources support the requirement | Frame, Required access |
| Use a permitted non-rolling alternative where rolling is excluded | Removes the contradictory medical instruction | Frame unit 3; `g3-body-roll` |
| Add the assessment evidence listed in finding 2 | Checks existing owned outcomes | Frame Ends cells |
| Teach all three S3.5.5 working arrangements | Restores the published indicator’s breadth | Frame, progression, standard paraphrase |
| Put unit 17’s final checks on days 12 and 13 | Keeps response after assessment within 14 days | Frame unit 17 |
| Use the existing bar-graph fallback | Grade 5 coordinate work comes later | Frame reconciliation notes |

## For Cory

- The existing money question remains: confirm the equipment ceiling, given approximately **$220 of new grade 3 supplies** and about **$390 across the band**, before any purchases. This review authorizes no spending.

## What I could not judge

- Actual movement time, observation workload and adaptations before lessons are written or tried.
- Final dance-course coordination before that neighboring frame exists.
- Complete cultural-source confirmation and recording rights for every proposed activity.
- Whether a particular school’s mats, space or medical arrangements are suitable.

## Sources and reading limits

- [2024 PE standards](https://shapeamerica.org/standards/pe/new-pe-standards/): checked relevant span-5 actions and S3.5.5 breadth.
- [CDC PECAT](https://www.cdc.gov/assessing-improving-school-health/pecat/index.html): outcome, content and assessment analysis. The tool uses the earlier standards edition.
- [SPHEReS gymnastics guidance](https://myspheres.ca/en/fundamental-reading/gymnastics-facilities/): floor-work mat requirements and instructional progression.
- [Nova Scotia safety guidelines](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf): targeted gymnastics and mat-work sections, not the entire document.
- [National weekly PE guidance](https://shapeamerica.org/standards/guidelines/): verified the elementary recommendation supporting the frame’s dose disclosure.
- [CDC drowning prevention](https://www.cdc.gov/drowning/prevention/index.html): water-safety context.
- Cultural sources and their limits are linked in finding 4.

## For the source list

Add the direct La Bastringue education page, Philippine education department Tinikling resource, and SPHEReS gymnastics page as targeted references. Record the Library of Congress URL as **403, browser check**.

