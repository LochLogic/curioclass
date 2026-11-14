# Independent expert read: World Geography and Ancient Civilizations I

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-world-geography-and-ancient-civilizations-i-2026-11-13.md`  
**Delivery:** Report supplied here. No file was created or edited.

## Verdict

The frame has a sound regional structure, complete placement of its 29 progression skills, and a plausible annual time budget, but it needs revision before it guides the scope and sequence. Its biggest risk is that complete code placement conceals several incomplete standards and conflicting instructions about when skills are taught. Complete the required student work and repair those instructions while keeping the present unit structure and 160-day total.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, FOUNDATION, the relevant ROADMAP guidance, BASELINE rules 20 to 24, and GLOSSARY.
- The shared adoption criteria and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`; `docs/courses/social-studies/STANDARD.md`.
- The complete target frame, its `frames.csv` row, all 29 grade 6 social studies progression rows, and the referenced earlier and later handoff rows.
- The complete grade 5 and World Geography and Ancient Civilizations II frames.
- Relevant grade 6 math, science and ELA progression rows. Corresponding course frames were not present.
- BASE-TEXTS, the plan-data guidance, relevant APPROACH and APPROACH-SOURCES material, existing topic records, and the earlier social studies progression reviews and correction reports.
- External standards and curriculum references listed below.

### Check results

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Alternate installed Python launcher | Could not launch its child interpreter: permission denied |
| Direct target `frame.py check` | **0 failures** |
| Direct social studies `progression.py check` | **384 rows, 0 failures**, with advisory notes |
| `python -X utf8 scripts/stale.py check` | **16 files, 0 failures** |

The full plan gate remains **unverified**. Its interruption was an environment error, not a reported curriculum failure. The direct checks support this limited frame review but do not replace the full gate.

## Findings, most serious first

### 1. Three anchor requirements remain unspecified

**LAYER:** standard  
**REPEAT:** yes, incomplete requirements inside claimed codes recur in the earlier progression reads  
**Severity:** serious  
**Confidence:** firm

Both the frame and its owning progression rows omit the work below.

| Location | Missing work | Exact fix |
|---|---|---|
| Unit 1, `ss6-social-science-lenses`, `MA.6.T1.3` | Cooperation among disciplines, beyond sorting their questions | Add a worked investigation showing specialists combining evidence, testing a hypothesis and reaching a joint interpretation. |
| Unit 5, `ss6-egypt-society`, `MA.6.T3c.6` | Religious beliefs about proper behavior | Add an age-suited source task connecting expected conduct with Egyptian religious beliefs. |
| Unit 7, `ss6-islam-origins`, `MA.6.T3f.3` | Muhammad’s teachings, beyond biography and the Qur’an’s importance | Name and teach representative beliefs and ethical obligations, attributed to Islamic sources. |

These are required components, not optional enrichment. Add them to the existing units and progression notes, with an explicit check for each. The requirements are confirmed in the [Massachusetts framework, printed pages 86, 89 and 90](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

### 2. Five C3 indicators are only partly secured

**LAYER:** progression  
**REPEAT:** yes, especially finding 1 of `progression-social-studies-codex-2026-11-13.md`  
**Severity:** serious  
**Confidence:** firm on the requirements; likely on the resulting lesson omissions

The earlier correction report records the research-row repairs as applied, but the current notes still leave parts missing.

| Unit and indicator | Exact remaining repair |
|---|---|
| 8: `D1.3.6-8` | Explain expert agreement about a supporting question. |
| 8: `D1.5.6-8` | Choose sources to represent differing viewpoints. Primary/secondary classification alone is insufficient. |
| 8: `D3.1.6-8` | Add structure, context and corroborative value to source-selection checks. |
| 4: `D2.Civ.12.6-8` | Assess an actual law and a proposed revision against the same public problem. |
| 11: `D4.2.6-8` | State a strength and weakness of the explanation itself. |

Apply these changes to the owning progression notes and corresponding frame rows. Without them, writers can complete the described tasks while leaving claimed indicators unfinished. See the [C3 indicator tables](https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf).

This reopens only the unresolved portions. The added expert-agreement work in unit 2, electronic mapping in unit 9, and market work in unit 6 should remain.

### 3. The final check asks for a move assigned to grade 7

**LAYER:** frame  
**REPEAT:** yes, the cross-subject reviews already identified opposing-claim timing problems  
**Severity:** moderate  
**Confidence:** firm

Course check 3 requires “a counterpoint named.” No grade 6 unit explicitly teaches that move. The ELA progression limits grade 6 argument to a claim and its reasons, while the grade 7 social studies frame explicitly teaches naming the opposing claim in its final unit.

**Why it matters:** the final assessment can mark students down for work that this frame neither teaches nor securely receives.

**Exact fix:** replace the check phrase with:

> A short written argument supported by evidence, with a limitation of the evidence identified.

Keep opposing-claim instruction in its recorded grade 7 location. This repairs the assessment without moving a standard.

### 4. The sensitivity-review list excludes units containing hard history

**LAYER:** process  
**REPEAT:** yes, earlier social studies reviews identify incomplete sensitivity safeguards  
**Severity:** moderate  
**Confidence:** firm

The course introduction flags units 2, 7, 10 and 11 for a fresh-agent sensitivity read, and only units 10 and 11 for a qualified person’s read. Units 4, 5, 6 and 9 also explicitly teach enslavement or trade in enslaved people.

FOUNDATION section 7 requires a community reader for Native and hard-history content. The social studies adoption bar also says the fresh-agent sensitivity read covers every unit.

**Why it matters:** writers could treat the introduction’s list as the complete review requirement.

**Exact fix:** replace the selective statement with:

> Every unit receives the fresh-agent sensitivity read. Units 4, 5, 6 and 9 to 11 contain hard-history or Indigenous content requiring the qualified-person review specified by FOUNDATION section 7. Other sensitive material is flagged in its unit plan.

Cory retains responsibility for identifying and arranging outside readers.

### 5. “First full sourcing” in unit 4 weakens the grade 5 handoff

**LAYER:** frame  
**REPEAT:** yes, prerequisite and model-continuity problems recur in the progression reviews  
**Severity:** moderate  
**Confidence:** likely

The introduction, seam table, model table and unit 4 repeatedly describe Hammurabi as the year’s first full sourcing step. Yet grade 5 hands on unprompted sourcing before evidence is used, and unit 2 already asks students to compare historical interpretations and write claims.

**Why it matters:** a literal reading permits early source work without maintaining the routine students previously learned.

**Exact fix:** in all affected frame locations, distinguish maintenance from the new application:

> From unit 1, students retrieve and use grade 5’s sourcing routine before using evidence. Unit 4 applies it closely to a ruler’s law code and prologue.

Make the corresponding correction to `ss6-hammurabi-code`. Unit 2 should source its secondary accounts before comparing them. This preserves the grade 5 handoff and the distinctive work of unit 4. It is also consistent with the routines described by [Digital Inquiry Group](https://www.inquirygroup.org/history-lessons).

### 6. The unit 11 research options contradict its stated boundary

**LAYER:** progression  
**REPEAT:** yes, course-boundary mismatches are an established finding type in earlier social studies reads  
**Severity:** moderate  
**Confidence:** firm

The frame says the Inca empire belongs to grade 9, but `ss6-maya-andes-research` offers Inca as an ordinary research option and names Inca khipu. The frame carries that record-keeping example into unit 11.

**Why it matters:** the default research route can expand into content explicitly reserved for another course.

**Exact fix:** use Maya or an early Andean society such as Moche as the supported research choices. Remove Inca from the default option list; label any retained Inca comparison **extension**, with grade 9 retaining ownership. This follows the distinction in the [anchor’s Americas section, printed pages 93 to 94](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

### 7. Two compelling questions need tighter boundaries

**LAYER:** frame  
**REPEAT:** yes, question-to-content mismatch appears in earlier social studies review criteria  
**Severity:** moderate  
**Confidence:** judgment call

Unit 7 asks how the three faiths came to shape so much of the world, while its content concentrates on their origins and reserves later spread for other courses. Unit 11’s question assumes widespread destruction of records across every permitted research society, although the specified destruction example concerns Maya books.

**Why it matters:** the first question invites an unsupported global survey; the second supplies a conclusion that may not fit the selected case.

**Exact fixes:**

- Unit 7: **“How much did these three faiths share at their beginnings, and where did they differ?”**
- Unit 11: **“What can surviving evidence tell us about Maya or early Andean life, and what remains uncertain?”**

These wording changes fit the existing content and days.

### 8. The frame’s registration note is stale

**LAYER:** process  
**REPEAT:** yes, stale notes recur in the progression reviews  
**Severity:** minor  
**Confidence:** firm

“For the lead,” item 5, leaves an instruction to synchronize the frame row. `data/plans/frames.csv` already contains the correct 11-unit, 160-day entry.

**Why it matters:** the handoff presents completed registration as remaining work.

**Exact replacement:**

> `data/plans/frames.csv` records this course as 11 units and 160 days. Re-run synchronization only if those totals change.

### 9. A correction report still waits on progressions that now exist

**LAYER:** process  
**REPEAT:** yes  
**Severity:** minor  
**Confidence:** firm

Under “Skipped, needs Cory,” `progression-social-studies-fixes-2026-11-13.md` says cross-subject ownership checks wait on the other progressions. Those files exist, and the later cross-subject correction report documents the ownership and timing repairs.

**Why it matters:** a caller can reopen completed work or misunderstand what remains unverified.

**Exact current-status replacement:**

> Resolved subsequently in `progression-cross-fixes-2026-11-13.md`: the other progressions are present and cross-subject ownership checks were applied. Within-year availability still requires the corresponding course frames.

For the dated review record, retain the original history and attach this as a dated resolution note.

### 10. GLOSSARY still describes progression CSVs as planned

**LAYER:** process  
**REPEAT:** yes  
**Severity:** minor  
**Confidence:** firm

The progression row in `docs/GLOSSARY.md` labels `data/progressions/<subject>.csv` “planned,” although the four core-subject progression files exist.

**Why it matters:** the terminology guide misstates where current planning evidence lives.

**Exact replacement for that cell:**

> `data/progressions/<subject>.csv`; earlier narrative guidance includes `docs/courses/math-3-5-progression.md`.

### 11. GLOSSARY still says course frames are not built

**LAYER:** process  
**REPEAT:** yes  
**Severity:** minor  
**Confidence:** firm

The course-frame row in `docs/GLOSSARY.md` says “Not built,” although this course and its neighboring courses have frame files.

**Why it matters:** the guide directs readers away from artifacts that are now available.

**Exact replacement for that cell:**

> `docs/courses/<course>/frame.md`; totals in `data/plans/frames.csv`; PRODUCTION-PATH step 2.

## Ownership, order and time

Every grade 6 progression skill appears in exactly one unit’s Skills cell. There are no missing, duplicated or foreign skill IDs.

| Unit | Days | Owned progression skills |
|---|---:|---|
| 1 | 10 | `ss6-social-science-lenses`; `ss6-timeline-deep-time` |
| 2 | 15 | `ss6-changing-interpretations`; `ss6-paleolithic-neolithic`; `ss6-complex-societies` |
| 3 | 15 | `ss6-mena-maps`; `ss6-mena-settlement` |
| 4 | 16 | `ss6-mesopotamia-states`; `ss6-surplus-specialization`; `ss6-mesopotamia-society`; `ss6-hammurabi-code` |
| 5 | 16 | `ss6-egypt-nile`; `ss6-egypt-society`; `ss6-egypt-achievements`; `ss6-nubia-kush` |
| 6 | 10 | `ss6-phoenician-trade`; `ss6-writing-systems` |
| 7 | 13 | `ss6-ancient-israel`; `ss6-christianity-origins`; `ss6-islam-origins` |
| 8 | 12 | `ss6-silk-roads-exchange`; `ss6-research-contribution` |
| 9 | 16 | `ss6-africa-geography`; `ss6-axum-swahili`; `ss6-west-africa-trade` |
| 10 | 11 | `ss6-caribbean-central-geo`; `ss6-caribbean-peoples` |
| 11 | 14 | `ss6-south-america-geo`; `ss6-maya-andes-research` |

The 148 unit days plus 12 course-level check/respond days total 160. This fits a 180-day calendar with 20 days outside the course allocation.

No unit is demonstrably far over or under its share at this layer. Two budgets need particular care during daily planning:

- Unit 8 assigns about **9 of 12 days** to research, leaving **3 days** for connections and other work.
- Unit 11 assigns **14 days** to regional geography and a longer report. Its scope and sequence must preserve both components.

As a comparison, the [Investigating History guidebook](https://www.doe.mass.edu/investigatinghistory/curriculum/g6-course-guidebook.pdf), PDF page 7, budgets 123 lessons across four larger units. Different grouping and lesson design prevent treating that count as a required allocation for Curio Class.

The order generally holds: timeline before dated comparisons, complex-society traits before their repeated use, regional map tools before later regional applications, and a first research project before the final report. The faith grouping explains its deliberate chronological departure.

## Seams and cross-subject availability

The grade 5 and grade 7 frame handoffs largely agree with this frame. Geography, economic reasoning, continuity and change, research, and the annual action cycle all have identifiable receiving work. Finding 5 addresses the main backward seam problem.

Earlier-grade math and science prerequisites are identifiable in their progressions. Same-year availability cannot be confirmed against grade 6 math, science or ELA frames because those frames were absent. The target frame mostly handles this responsibly through local teaching: unsigned coordinates, separately explained graph axes, a supplied dating-evidence pack, and research or author-purpose modeling when ELA comes later.

Those arrangements are **proposed coordination**, not verified calendar alignment.

## Source map

**Not applicable at present.** The course adopts no whole-course base text, and no source-map file exists for it. The frame maps no base lessons and correctly distinguishes possible partial bases from reference-only material.

If a later unit adopts base lessons, its source map must then record the lessons, exclusions, order changes and reasons. The current absence is not a finding.

## Course-frame lens checklist

| Checklist line | Status | Reason |
|---|---|---|
| Every anchor standard in the topic range has a unit | **Met for placement; missed for full specification** | Findings 1 and 2 identify unfinished requirements. |
| Replaced grade 3 or grade 8 own-state content is generalized | **Not applicable** | This is grade 6. |
| Units record check-set additions and their sources | **Met at frame level** | Every unit has a column; candidates remain explicitly provisional. |
| Questions can be answered from the planned content and sources | **Missed** | Finding 7. |
| Content precedes independent inquiry | **Met in design** | Direct teaching and ordered research preparation are stated. |
| Chronology has reasons for departures | **Met** | Regional grouping and the faith grouping are explained. |
| Sources receive sourcing, context and corroboration | **Missed in the early-year instructions** | Finding 5. Actual source packs remain unjudged. |
| Claims and source writing develop across the year | **Met in design** | Short claims lead to two reports; finding 3 removes an untaught assessment demand. |
| Historical thinking has named parts | **Met** | Chronology, interpretation, perspective, continuity/change and causation are visible. |
| Geography and economics function as reasoning | **Met in design** | Maps, settlement explanations, trade costs and productivity recur. |
| Civic dispositions and annual informed action | **Met in design** | Unit 3 includes choice, evidence, action and reflection. |
| Values and hard-history safeguards | **Missed in review coverage** | The instructional stance is sound; finding 4 repairs the review list. |
| Unit and day requirements | **Not applicable to this read** | Excerpts, supporting questions, daily tasks and final assessments are later-layer artifacts. |

## Settled by the expert

These are recommendations for the caller to apply. No changes were made.

| Choice | Reason | File touched |
|---|---|---|
| Complete the components in finding 1 inside their existing units | Preserves current ownership and days | Target frame; `social-studies.csv` |
| Add the five explicit tasks in finding 2 | Makes the claimed work buildable | Same files |
| Replace the final-check counterpoint with an evidence limitation | Matches taught work | Target frame |
| Maintain sourcing from unit 1; describe Hammurabi as a close application | Preserves the grade 5 handoff | Target frame; `ss6-hammurabi-code` |
| Support Maya or early Andean research; label retained Inca comparison extension | Enforces the stated boundary | Target frame; `ss6-maya-andes-research` |
| Use the revised questions in finding 7 | Fits the planned content | Target frame |
| Apply the four current-status note repairs | Removes completed work from the pending picture | Files named in findings 8 to 11 |
| Keep 11 units and 160 days | No demonstrated need for a structural change | Target frame; `frames.csv` |

## What is right and should stay

- The complete, single-unit placement of progression skills.
- The cumulative timeline, including the absence of year zero.
- The repeated regional reasoning frame.
- Explicit retrieval or reteaching for dormant prerequisites.
- Living Indigenous peoples represented through their own materials.
- Clear boundaries between historical study of religion and devotional practice.
- Student-chosen informed action with a delayed reflection.
- Unseen-source assessment tasks and protected respond days.

## What I could not judge

- A complete plan-gate result.
- Actual reading difficulty, translations, rights clearance, source balance or assessment quality before materials exist.
- Minute-level feasibility before the scope and sequence is written.
- Same-year cross-subject frame alignment.
- Final accuracy and sensitivity of Native and hard-history materials.
- The full New York comparison: its official PDF timed out twice. The early-town candidate remains unconfirmed in this read.

No substantive finding rests solely on memory. Question wording and pacing judgments are professional judgments. Earlier memory guidance was used only for review procedure, not as evidence about this course.

## Sources and source-list additions

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): required content and course boundaries.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/C3-Framework-for-Social-Studies.pdf): indicator requirements.
- [California standards](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf): confirmed the unit 7 candidate concerning Judaism after 70 CE.
- [Investigating History grade 6 guidebook](https://www.doe.mass.edu/investigatinghistory/curriculum/g6-course-guidebook.pdf): comparative course structure and pacing.
- [Investigating History regional unit overview](https://www.doe.mass.edu/investigatinghistory/curriculum/units.aspx?grade=6&unit=2): limited regional-sequence comparison.
- [Digital Inquiry Group curriculum description](https://www.inquirygroup.org/history-lessons): sourcing and evidence routines.
- [Oak early-civilizations comparison lesson](https://www.thenational.academy/teachers/lessons/comparing-the-earliest-civilisations): limited inspection of the proposed younger-pupil material. It does not establish grade 6 sufficiency.
- [New York K to 8 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): attempted, not successfully opened.

**For the source list:** add the accessible Investigating History guidebook and regional-unit routes, the direct C3 PDF route, and the inspected Oak lesson. Record the limited extent of each inspection and the New York access failure.

## For Cory

- Confirm the audience assumption of **160 daily periods of about 45 minutes**.
- Arrange the qualified readers required for the course’s Indigenous and hard-history material. No outreach or spending was undertaken.

**Verdict:** revise before the scope and sequence. **Finding count:** 11. **Intended report path:** `docs/reviews/frame-world-geography-and-ancient-civilizations-i-2026-11-13.md`. Delivered here only.

