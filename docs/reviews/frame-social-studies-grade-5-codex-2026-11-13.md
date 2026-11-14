# Independent expert cold read: social studies grade 5

**Date:** 2026-11-13  
**Intended report:** `docs/reviews/frame-social-studies-grade-5-2026-11-13.md`  
**Delivery:** Report supplied here. No file was written.

## Verdict

The frame has a coherent sequence, complete structural placement, and a workable provisional year budget, but needs revision before it guides unit writing. Its greatest risk is that a listed standard can appear covered while required learning remains unspecified, including the origins of colonial slavery and part of the inquiry work. Complete those requirements within the existing units and resolve the amendment-process prerequisite before proceeding.

## What I read and checked

I read:

- `docs/agents/EXPERT.md`, the social studies lens, FOUNDATION, GLOSSARY, BASELINE rules 20 to 24, and relevant ROADMAP sections.
- The shared core and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`.
- `docs/courses/social-studies/STANDARD.md`, APPROACH, relevant APPROACH-SOURCES material, and BASE-TEXTS.
- The complete grade 5 frame, its `frames.csv` row, all 21 grade 5 progression rows, and relevant neighboring-grade and earlier prerequisite rows.
- The grade 4 and World Geography and Ancient Civilizations I frames.
- Relevant social studies progression reviews and fixes, cross-subject reviews and fixes, and earlier content-standard and source reviews.
- The grade 5 ELA, mathematics, and science progression entries supporting the named cross-subject connections.
- Relevant official Massachusetts and C3 wording, plus the outside sources listed below.

There is no grade 5 social studies source map because this course has no base text. That is consistent with BASE-TEXTS.

### Gate results

| Check | Result |
|---|---|
| Requested `python -X utf8 scripts/plan.py check` | Stopped with `ModuleNotFoundError: No module named 'markdown'` |
| Separate frame check | 0 failures |
| Separate social studies progression check | 384 rows, 0 failures |
| Requested stale-note check | 0 failures |

The full plan gate did **not** pass. Its dependency failure does not establish a curriculum defect. I continued the requested substantive review using the successful separate checks, without installing anything.

The structural checks establish that all 21 owned progression rows sit in exactly one unit and that their recorded standards are placed consistently. They do not establish full semantic coverage.

## Findings, most serious first

### 1. Several anchor requirements remain only partly specified

**LAYER:** standard  
**REPEAT:** yes, the same kind as finding 2 in the earlier independent social studies progression review  
**Confidence:** likely that these omissions would reach instruction; firm about the required components

The following requirements are missing from the teaching descriptions, even though their codes are present. The official [Massachusetts framework, printed pages 72 to 75](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf) distinguishes these components.

| Unit and standard | What is wrong | Exact fix |
|---|---|---|
| Unit 2, `MA.5.T1.5` | Legal status and prevalence are taught, but the **origins** of colonial slavery are absent. The Virginia example is only a candidate addition. | Make the development of colonial slavery required content: Atlantic connections, forced arrival, and colonial laws establishing racial and inherited bondage. Keep it in unit 2 and update `ss5-slavery-colonies` accordingly. |
| Unit 3, `MA.5.T2.2` | A historic map and named people appear, but analyzing their roles and significance is not specified. | Require students to explain how two selected people influenced an event located on the map, using sources. |
| Unit 4, `MA.5.T2.8` | Failure of the Articles is explicit; reasons for their adoption in 1781 are not. | Add why the states adopted the Articles and what that arrangement initially offered, before explaining its weaknesses. |
| Unit 5, `MA.5.T3.6` | Reading the Bill of Rights and arguing for one amendment appear; explaining its guaranteed freedoms is not explicit. | Require students to explain the freedoms protected by the Bill of Rights before researching one amendment. |

**Why it matters:** a writer can follow the present descriptions faithfully and still omit part of each claimed standard.

For the slavery-origin repair, distinguish forced arrival from the later development of hereditary legal status. The [National Park Service account](https://www.nps.gov/articles/000/arrival-of-the-first-africans-in-1619.htm) and [National Museum of African American History and Culture account](https://www.searchablemuseum.com/colonial-slave-laws/) support that distinction. Do not describe 1619 as the beginning of slavery throughout the Americas.

These repairs complete existing standards in their existing units. They do not require moving a standard or enlarging the course.

### 2. Unit 10 still narrows two claimed C3 requirements

**LAYER:** progression and standard  
**REPEAT:** yes, the same kind as finding 1 in the earlier independent progression review  
**Confidence:** firm on the wording mismatch

Two requirements remain unsecured:

| Indicator | Problem | Exact fix |
|---|---|---|
| `D1.3.3-5` | The progression repair asks students to list facts and ideas needed for each supporting question. That does not preserve the requirement to identify associated concepts open to interpretation. | Add to `ss5-civil-rights-research` and unit 10: “For each supporting question, identify a related idea that people could interpret differently, and explain two possible readings.” |
| `D2.His.13.3-5` | Source usefulness is judged from maker, date and purpose. Intended audience and place of origin are not secured in this research routine. | Require the source log to record maker, date, origin, audience and purpose, then explain the source’s usefulness for the particular question. |

The [C3 Framework, printed pages 24 and 48](https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf) supports these distinctions.

**Why it matters:** collecting facts for a question is different from recognizing an interpretive concept. Naming source features is also insufficient unless students use them to judge relevance.

**Disagreement with the earlier repair:** the fixes report treats the grade 5 `D1.3` repair as complete. I disagree narrowly: adding facts and ideas does not complete the grade 3 to 5 wording. Preserve the earlier additions and add the interpretive requirement.

### 3. Unit 8 depends on an amendment process that unit 5 treats as optional

**LAYER:** frame  
**REPEAT:** yes, the same prerequisite-contract problem identified in earlier progression and cross-subject reads  
**Confidence:** firm

Unit 8 says it needs “unit 5’s branches and amendment process.” Unit 5 places the amendment process only under “Check set adds” as a candidate.

**Why it matters:** a unit writer may legitimately omit the candidate, leaving the later prerequisite untaught.

**Exact fix:** replace unit 8’s prerequisite wording with:

> Needs unit 5’s branches and constitutional provisions. Before studying the Reconstruction amendments, teach a brief model of proposal by Congress and ratification by the states.

Keep the fuller amendment-process candidate in unit 5 optional. This supplies the minimum bridge where it is needed without moving a standard.

### 4. The frame names sensitivity reads but omits the required qualified-person read

**LAYER:** frame  
**REPEAT:** new  
**Confidence:** likely

Several units are flagged for a sensitivity read. The frame does not carry forward FOUNDATION section 7’s separate requirement for a reader from the community concerned to examine Native and hard-history content. The neighboring grade 6 frame explicitly distinguishes the two reads.

**Why it matters:** a later workflow could treat an agent sensitivity read as the entire review requirement.

**Exact fix:** add a course-wide statement:

> Every unit receives the required fresh-agent sensitivity read. Native and hard-history content also requires the qualified-person read specified in FOUNDATION section 7 before publication. The review record identifies the material examined and the resulting corrections.

Carry this into the unit plans, including hard-history material in units 4, 6 and 8 and relevant research selections in unit 10. Cory assigns people and any budget.

### 5. The load justification miscounts anchor standards

**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

The opening says 21 rows hold “about 80 anchor codes and parts.” They actually name **55 distinct Massachusetts codes and parts**, plus **29 distinct C3 indicators**.

**Why it matters:** the mistaken count is offered as evidence that this course requires the entire time allocation.

**Exact fix:** replace that sentence with:

> The course places 21 progression rows containing 55 Massachusetts content codes and parts and 29 C3 indicators. The broad historical span, source work, research and informed action support a provisional 160-day allocation.

Remove “and nothing less.” A shorter-path decision belongs to the eventual scope and sequence and Cory’s time assumptions.

### 6. Grade 5 still instructs the caller to synchronize an already synchronized row

**LAYER:** process  
**REPEAT:** yes, stale work-status notes recur in the earlier progression review  
**Confidence:** firm

`social-studies-grade-5/frame.md`, “For the lead,” item 4, says to run synchronization. `frames.csv` already records 10 units and 160 days, and the frame check passes.

**Why it matters:** it presents completed maintenance as outstanding work.

**Exact replacement:**

> `frames.csv` records 10 units and 160 days for this course; the frame check confirms agreement.

### 7. The neighboring grade 4 frame has the same stale synchronization instruction

**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

`social-studies-grade-4/frame.md`, “For the lead,” item 4, still directs synchronization. Its row already records 7 units and 160 days.

**Why it matters:** the seam-reading pack carries a false outstanding task.

**Exact replacement:**

> `frames.csv` records 7 units and 160 days for this course.

### 8. ROADMAP still says the social studies content standard awaits Cory’s decision

**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

`docs/ROADMAP.md:95` to 96 says social studies waits on an open content-standard decision. STANDARD, the decision record, and the completed P1 flow nodes show that the decision has landed.

**Why it matters:** this incorrectly blocks work whose prerequisite is complete.

**Exact replacement:**

> Social studies uses C3 skills and the Massachusetts 2018 content anchor in the adopted course order, checked against California, Tennessee and New York. The standard decision and P1 preparation are complete; subsequent work follows PRODUCTION-PATH.

### 9. ROADMAP still describes the existing ELA approach page as future work

**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

The layer 3 status row says “Science and ELA pages when those courses open.” `docs/APPROACH-ELA.md` exists. A social studies approach page does not.

**Why it matters:** the status row does not distinguish completed documents from genuine prerequisites.

**Exact replacement for that sentence:**

> The ELA approach page exists at `docs/APPROACH-ELA.md`. Separate science and social studies approach pages remain to be completed before their scopes and sequences.

Do not imply that an existing draft has received approval merely because it exists.

### 10. ROADMAP still calls the existing lesson-day template unwritten

**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

The layer 7 home column calls `docs/courses/LESSON-DAY.md` “to be written before the pilot is built.” That file exists and is used by the lesson checker.

**Why it matters:** it misidentifies a finished prerequisite as a pending task.

**Exact replacement:**

> The shelves and tools; the lesson-day template `docs/courses/LESSON-DAY.md`.

### 11. The progression fixes report still says cross-subject ownership checking awaits the other progressions

**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

`docs/reviews/progression-social-studies-fixes-2026-11-13.md:43` says this waits on the other progressions. Those files exist, and the subsequent cross-subject fixes report documents the ownership-grade check added to `scripts/progression.py`.

**Why it matters:** it obscures the difference between completed grade-level checking and still-unverified within-year timing.

**Exact replacement:**

> Resolved subsequently by the cross-subject progression pass and the ownership-grade check in `scripts/progression.py`. Within-year availability remains for the course frames and calendars.

### 12. The cross-subject fixes report still leaves the now-decided water topic with Cory

**LAYER:** process  
**REPEAT:** yes  
**Confidence:** firm

The expert-finding-7 row and “Not done, and why” section of `docs/reviews/progression-cross-fixes-2026-11-13.md` say the grade 5 ELA topic change remains with Cory. The decision record at `DESK-ANSWERS.md:941` onward records his yes. Current `e5-research` and `e6-reading-range` notes reflect the water thread.

**Why it matters:** the report presents a resolved scope decision as pending.

**Exact fix:** retain the historical account of what that pass omitted, then replace its current outstanding-status statements with:

> Subsequently resolved: Cory approved water for grade 5 ELA unit 4 on 2026-11-13. The progression now carries the water topic and its research and grade 6 handoff.

## Ownership, sequence and days

All owned rows are placed once. Earlier-grade content is identified through retrieval, maintained skills or content revisits. I found no additional unlabelled takeover of another grade’s owned row.

| Unit | Days | Owned rows | Massachusetts codes and parts | Load judgment |
|---|---:|---:|---:|---|
| 1 | 14 | 2 | 4 | Reasonable for encounters, founding comparisons and regional mapping |
| 2 | 12 | 1 | 7 | Justified by the substantial comparison and hard-history work |
| 3 | 17 | 2 | 7 | Reasonable for the event chain and sourcing step up |
| 4 | 16 | 1 | 9 | Dense bundle, but defensible at this introductory depth |
| 5 | 16 | 1 | 6 | Reasonable for constitutional reading and an evidence-based argument |
| 6 | 17 | 4 | 6 | Several short rows; retain the allocation provisionally |
| 7 | 16 | 3 | 7 | Coherent resistance theme; substantial source and context work |
| 8 | 14 | 2 | 4 | Reasonable if military coverage stays introductory |
| 9 | 14 | 3 | 4 | Dense, but research is correctly reserved for unit 10 |
| 10 | 16 | 2 | 1 | Defensible as approximately 11 research days and 5 action days |
| Course checks and respond days | 8 | | | Explicitly reserved |
| **Total** | **160** | **21** | **55** | Fits the stated yardstick |

No unit is demonstrably far over or under its share. Row counts alone would mislead: unit 2’s single row contains considerably more work than several shorter rows elsewhere.

The chronological overlaps are reasonable topic recaps. Unit 7 returns to Tecumseh and slavery’s expansion after unit 6 establishes the early republic. Unit 9 connects Reconstruction-era disputes with later movements. These do not require rearrangement.

The 160-day budget assumes approximately **6,400 minutes**, including course checks and respond days. That is a plausible design allocation, not evidence that ordinary classrooms can always supply it.

## Seams and cross-subject availability

The grade 4 and grade 5 handoffs agree on mapping, prompted sourcing, regional reasoning, forced migration and research. Grade 3 founding ideas, trade and deliberation are explicitly retrieved across the gap.

The grade 6 frame picks up grade 5 research, sourcing, regional reasoning, mapping and economic models. Historical content returning much later is identified as a revisit. I found no additional substantive seam defect.

The other subjects’ grade 5 **frames do not yet exist**, so their within-year ordering cannot be certified.

| Connection | Current evidence | Judgment |
|---|---|---|
| `RI.5.6` before social studies unit 3 | ELA progression places several-account work in ELA unit 3 | Earlier availability is unproved. Preserve the social studies comparison model. |
| `RI.5.3` before social studies unit 3 | ELA progression uses it in units 2 and 3 | Potentially available, but calendar confirmation is needed. |
| `W.5.1` before social studies unit 5 | ELA opinion work appears in units 3 and 4 | Plausible; confirm against the ELA frame. |
| `RI.5.8` before social studies unit 7 | ELA work appears in units 3 and 4 | Plausible; preserve the local Douglass model. |
| `W.5.7` before social studies unit 10 | ELA research recurs from unit 2 | Plausible; actual timing remains unverified. |
| Mathematics coordinate grid | Frame explicitly relies on earlier latitude and longitude instead | No same-year prerequisite defect |
| Science resource protection | Connection is supplementary; industrial costs are taught locally | No same-year prerequisite defect |

This is a verification limit, not a reason to invent unit numbers for unwritten frames.

## Lens checklist

The lens has three explicit course-frame checks. Each is addressed below.

| Course-frame check | Status | Evidence |
|---|---|---|
| Every anchor standard in the topic range has a unit | **Met structurally; missed semantically in part** | All codes are placed; finding 1 identifies incomplete teaching descriptions. |
| Replaced grade 3 or grade 8 own-state content is generalized appropriately | **Not applicable** | This is grade 5. Its named Massachusetts events are part of the adopted national-history anchor. |
| Every unit records check-set additions and their sources | **Met at candidate level** | Every unit names candidates and a check state. Full comparisons remain unit-plan work. |

The broader lens commitments also receive the following frame-level dispositions.

| Commitment | Status |
|---|---|
| Inquiry arc in every unit | Met as a design commitment; finding 2 completes part of the research demand |
| Content taught before inquiry depends on it | Met, apart from finding 3 |
| Primary and secondary sources, multiple accounts | Met as planned; actual selections await unit plans |
| Claims with evidence and reasoning | Met |
| Named historical thinking | Met |
| Geography and economics as reasoning | Met |
| Civic knowledge, deliberation and student-chosen action | Met |
| Values rule | Met in the stated design |
| Plain, age-suited hard history and living Native nations | Met in the stated design |
| Required sensitivity and qualified-person workflow | Missed in part, finding 4 |
| Scope-and-sequence, unit and day execution checks | Not applicable to finished execution at this layer |

The California candidates checked here are credible examples, including colonial institutions and the Northwest Ordinance. Tennessee and New York candidates remain **writer-reported and not independently verified in this read**. That limitation must remain visible until the unit comparison tables are completed.

## Settled by the expert

| Choice | Reason | File touched by the caller |
|---|---|---|
| Keep ten units and the current order provisionally | The divisions have instructional reasons and protect research time | Grade 5 frame |
| Complete the four anchor requirements in their existing units | Completes current ownership without moving standards | Grade 5 frame and social studies progression |
| Add the interpretive supporting-question task and fuller source-utility log | Completes claimed inquiry work | `ss5-civil-rights-research` and unit 10 |
| Teach the minimum amendment bridge inside unit 8 | Resolves the dependency without making an optional unit 5 addition mandatory | Grade 5 frame |
| Keep research and informed action assessed inside unit 10 | Another course-level check would duplicate the final performance | Grade 5 frame |
| Retain the named civil rights core already specified under “For the lead” | Unit 9 needs that content before students research it | `ss5-civil-rights-movements` notes |
| Correct the load count to 55 anchor codes and 29 C3 indicators | Separates content standards from skills | Grade 5 frame |
| Apply findings 6 to 12 as status corrections | They report completed work accurately | Files identified above |

These are recommendations for the caller to apply. No changes were made.

## What is right and should be preserved

- Slavery has enough space for a substantive comparison of enslaved and free lives.
- Unit 9 teaches movement history before unit 10 asks students to investigate it.
- Grade 5 sourcing grows explicitly from grade 4’s prompted work.
- Native nations appear as living governments and communities.
- Hard facts, resistance, family life and institutional action appear together.
- The frame prohibits harmful simulations and leaves civic action to students.
- The repaired women’s roles, Revolutionary War events, postwar economics and contemporary-change comparisons should remain.

## For Cory

- Confirm whether **160 lessons of approximately 40 minutes** is the intended classroom time assumption. The eventual scope and sequence needs a shorter path for classrooms with less time.
- Arrange the qualified-person review required by FOUNDATION, including any compensation. This report assigns no person and authorizes no spending.

## What I could not judge

- A successful full plan gate, because the available runtime lacks `markdown`.
- Confirmed cross-subject calendars before the other grade 5 frames exist.
- Actual reading difficulty, source rights, assessment quality and classroom timing before sources and unit plans are written.
- Final Native and hard-history accuracy, which requires the designated human and sensitivity reads.

No substantive finding rests solely on model memory. Pacing judgments are explicitly reviewer judgments rather than measured classroom results.

## Outside sources and source-list notes

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): grade 5 requirements and introductory depth.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf): inquiry and source-utility requirements.
- [California content standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): targeted checks of candidate additions.
- [National Park Service: arrival in 1619](https://www.nps.gov/articles/000/arrival-of-the-first-africans-in-1619.htm): forced arrival and legal-status distinctions.
- [National Museum of African American History and Culture: colonial slave laws](https://www.searchablemuseum.com/colonial-slave-laws/): legal construction of inherited bondage.
- [Investigating History grade 5 overview, June 2026](https://www.doe.mass.edu/investigatinghistory/curriculum/g5-course-overview.pdf): reference-only comparison of broad sequencing and pacing. Its year-at-a-glance page inconsistently states 97 lessons while listing 101, so I did not use its total as a precise pacing benchmark.

For APPROACH-SOURCES, retain the two slavery-history links and the current grade 5 overview with its count discrepancy. Nothing from the reference curriculum was copied into proposed student material.

**Verdict:** revise before unit writing. **Finding count:** 12. **Intended report path:** `docs/reviews/frame-social-studies-grade-5-2026-11-13.md`, supplied here only.