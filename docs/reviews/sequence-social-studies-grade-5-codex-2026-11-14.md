# Independent expert read: social-studies-grade-5 scope and sequence

**Date:** 2026-11-14  
**Intended report:** `docs/reviews/sequence-social-studies-grade-5-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were changed.

## Verdict

Revise before unit planning: the course has a coherent overall arc, sound calendar placement, and a defensible allocation of days. Its biggest risk is apparent coverage, because assessment descriptions and several day goals do less than their attached standards require. Complete the assessment blueprints and the remaining teaching requirements inside the existing units before they become contracts for unit writers.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, FOUNDATION, relevant ROADMAP sections, BASELINE rules 20 to 24, and GLOSSARY.
- The shared core and social studies section of ADOPTION-BAR-SUBJECTS, plus `docs/courses/social-studies/STANDARD.md`.
- The complete grade 5 scope and sequence, all 160 rows of `days.csv`, and the complete course frame.
- All 21 owned grade 5 progression rows, grade 4 and grade 6 handoff records, and the relevant earlier prerequisite rows.
- CALENDAR and grade 5 calendar records for all four subjects, plus the ELA frame’s relevant standards and bridges.
- APPROACH, the social studies source notes in APPROACH-SOURCES, BASE-TEXTS, and the scope-stage planning instructions.
- Both earlier grade 5 frame reports, the grades 3 to 5 fixes report, the independent social studies progression report, and relevant subsequent cleanup records.
- The official Massachusetts and C3 passages and outside references linked below.

Historical memory supplied a checklist only. No substantive finding below rests solely on memory.

## Gates

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Incomplete: reported a missing civics sequence file, then stopped on missing Python dependency `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Passed; no stagger-rule breaks reported. |
| `python -X utf8 scripts/frame.py check social-studies-grade-5` | Passed: 10 units, 160 days, 152 inside units and 8 at course level. |
| `python -X utf8 scripts/plan.py check social-studies-grade-5` | Passed: 0 failures. |
| `python -X utf8 scripts/stale.py check` | Incomplete: crashed with `KeyError: 'node'`. |

The unrelated failure and unavailable checks do not withhold this curriculum verdict.

## Findings, most serious first

### 1. The assessment blueprints do not secure full coverage

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** yes, the standard-to-task mismatch identified in the earlier progression and grade 5 frame reads  
**Confidence:** firm about the written blueprint gaps; actual items do not exist yet

Every unit has an assessment slot and an unseen-source task. Those strengths do not establish that its assessment covers every required part. Several rows attach codes for work the task description never directs a writer to assess.

The following are the minimum repairs identified in this read:

| Unit, assessment day | Coverage not secured by the current description | Exact repair |
|---|---|---|
| 1, day 13 | Founding comparisons and English influence | Add a short founding comparison and an explanation of English influence, alongside the encounter and map tasks. |
| 2, day 25 | Origins, legal prevalence, Atlantic trade, and the full comparison across 7a to 7d | Specify a compact source-and-map set covering these components. Replace “a way” of seeking freedom with a comparison that distinguishes the required routes and legal statuses. |
| 3, day 42 | Boston-map analysis, women’s roles, and colonial government development | Add explicit prompts for these, rather than expecting the generic causal chain to carry them. |
| 4, day 58 | Allegiances, leadership comparison, Shays’ Rebellion, and the full economics demand | Add these to the blueprint. Require the adoption rationale for the Articles and the victory explanation as well as their existing tasks. |
| 5, day 74 | Government levels, women’s exclusion, and the Convention compromise | Name a task for each. A provision explanation and checks-and-balances case do not automatically assess them. |
| 6, day 95 | The War of 1812, the Purchase’s importance, and industrial geography | Add explicit tasks. The War of 1812 code is present, but the stated assessment contains no war task. Include the economic distinctions in finding 2. |
| 7, day 111 | The removal cases, the import ban and internal trade, source perspective, and tactics then and now | Expand the blueprint beyond a perspective response, map reading, and one resistance example. |
| 8, day 125 | Military identification, Lincoln’s role, historical-summary skill, and the different legal changes | Specify these. “What one amendment changed” cannot establish the full amendment requirement. |
| 9, day 141 | Advocacy around the 14th and 15th Amendments | Add that relationship explicitly. The 19th Amendment prompt alone does not cover it. |
| 10, day 159 | The inquiry process, critique, and informed action | Assess the portfolio: questions, source selection and usefulness, evidence notes, revised claim, peer critique, strategy predictions, decision record, and reflection. Retain the unseen-source transfer task. |

**Why it matters:** writers can faithfully build the current task descriptions while leaving required learning unchecked. Codes alone would conceal that gap.

**Exact course-wide fix:** revise these ten assessment rows and their prose summaries into coverage blueprints before writing items. Map each required component to a task or assessable portfolio element. Keep response time counted once. If the resulting blueprint cannot fit its reserved time, identify that conflict before unit writing.

These are blueprint requirements, not a demand for ten long examinations. Several components can share a short source set. The underlying content requirements were checked against the [Massachusetts framework, printed pages 72 to 78](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

### 2. Unit 6 confuses economic indicators and loses the time dimension of industrial costs

**Severity:** serious  
**LAYER:** sequence and standard  
**REPEAT:** yes, semantic code mismatches in the independent progression read  
**Confidence:** firm

There are three connected problems:

- Day 90 teaches machines, skills, productivity, and pay. It is the natural location for both `D2.Eco.6.3-5` and `D2.Eco.13.3-5`.
- Day 91 carries `D2.Eco.13.3-5`, but its goal concerns changes in regional work through trade. That fits its geography indicator; it does not describe the economic indicator attached to it.
- Day 92 identifies only external costs, while grouping dangerous working conditions with costs to people outside the transaction. Workers’ conditions and effects on downstream residents need to be distinguished.
- The progression explicitly preserves short- and long-term industrial benefits and costs. The day goals and assessment reduce these to unspecified benefits and costs.

**Why it matters:** a writer could teach trade as productivity, treat every harmful working condition as an external cost, and omit the comparison across time.

**Exact fix:**

1. Put both productivity indicators on day 90. Explicitly connect investment in workers’ learning with productivity and later income.
2. Remove the productivity indicator from day 91 unless that goal is rewritten to teach it.
3. On day 92, distinguish costs within employment from spillovers to others. Include an external benefit as well as a cost, using a clearly labelled hypothetical example if necessary.
4. Across days 89 to 94, require a short-term/long-term comparison. Carry that distinction into day 95.

No additional day is necessary. These distinctions follow the [C3 economics tables, printed pages 36 to 37](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

### 3. Unit 10 substitutes research activities for some required explanations and teaching

**Severity:** serious  
**LAYER:** sequence and standard  
**REPEAT:** yes, the inquiry-requirement and prerequisite problems in the earlier progression and grade 5 frame reads  
**Confidence:** firm on the missing explanations; likely on the teaching risk

The earlier repairs to interpretive concepts and source logs are substantially present. Three remaining demands are unsecured:

| Location | Problem | Exact fix |
|---|---|---|
| Day 147, `D1.1.3-5` | Opening the question and choosing a topic do not explain its importance to other people. | Add a brief explanation of why the inquiry matters to a named audience beyond the researcher. |
| Day 148, `D1.4.3-5` | Writing supporting questions does not explain how they help answer the compelling question. | Require students to explain that relationship for each proposed supporting question. |
| Days 155 to 156, `D4.7.3-5` | The work specifies a local problem and collective action only. | Include brief comparisons of individual and collective strategies across local, regional, and global problems, drawing on supplied cases. The action students actually undertake can remain local. |

These distinctions were checked against the [C3 inquiry and action tables, printed pages 23 to 24 and 61](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

The unit also owns new inquiry demands, yet days 148 to 154 proceed directly through application. Its goals do not reserve an explicit model for the question explanations, source-usefulness judgment, or critique of an argument.

**Why it matters:** grade 4 research and ELA preparation supply useful foundations, but they do not establish these particular grade 5 explanations.

**Exact teaching fix:** begin day 148 with a model and guided question revision, day 151 with a model of source usefulness, and day 154 with a model critique before peer work. Name the supported attempt and later independent evidence. Keep these within the existing days.

Change “No new content is taught” to “No new historical survey content is introduced; the unit teaches and applies the remaining inquiry skills.”

### 4. Unit 2 implies a misleading ladder from skilled work to freedom

**Severity:** serious  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** firm

The unit’s explanation calls days 21 to 23 “the ways out of slavery in rising order,” beginning with skilled work. Day 21 actually describes hired-out labor whose pay owners retained. That is not itself a route to emancipation.

Day 22’s “freedom after service” also needs to distinguish Africans completing indentures or maritime service from people held in racial slavery. The official anchor makes that distinction in its discussion of 7c. See the [Massachusetts framework, printed page 73](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Why it matters:** the present arc could suggest that skilled labor or completing a term normally released an enslaved person.

**Exact fix:** replace the “rising order” sentence with:

> Days 21 to 23 distinguish labor arrangements and legal status, then examine different ways people sought or obtained freedom. Skilled work and being hired out did not themselves end enslavement.

Rewrite day 22 to contrast completed indentures or service with manumission and freedom suits. Keep Prince Hall’s petitions distinct from the Freeman and Walker court cases. Preserve all three days.

### 5. The claimed chronological order does not match the actual sequence

**Severity:** moderate  
**LAYER:** sequence  
**REPEAT:** new  
**Confidence:** firm

The plan allows some justified thematic recaps, but describes other reversals as chronological:

- Unit 3 reaches the Intolerable Acts on day 30, returns to 1770 on days 33 to 34, then introduces the earlier Stamp Act Congress and Sons of Liberty on day 35.
- Unit 7 calls its removal sequence chronological, but places the 1838 Trail of Tears before the 1833 Mashpee Revolt.
- Unit 9 groups movements, moving from disability events in 1977 and 1990 back to earlier farmworker organizing and Stonewall in 1969.

**Why it matters:** students building causal explanations need to distinguish an overview, a return to an earlier event, and subsequent developments.

**Exact fix:**

- Keep unit 3’s overview followed by source investigations, but name that two-pass design explicitly. Mark each return on a shared timeline. Remove “the year’s first contested event,” since unit 1 already treats contested encounters through different accounts.
- Swap the present day 102 and day 103 goals, placing Mashpee before the Trail of Tears.
- Describe unit 9 as movement-based after its chronological core. Use a parallel timeline to show overlap, rather than implying that one movement ended before another began.

The earlier frame read reasonably accepted broad thematic recaps. This finding concerns the inaccurate day-level explanation, not those accepted unit divisions.

### 6. The required shorter path is still absent

**Severity:** moderate  
**LAYER:** sequence  
**REPEAT:** yes, explicitly left for the eventual scope and sequence by the independent grade 5 frame read  
**Confidence:** firm

The course specifies 160 daily lessons of about 40 minutes, approximately 6,400 minutes. It gives no shorter path.

FOUNDATION section 5 and adoption criterion C2 require this at the scope-and-sequence layer. The earlier grades 3 to 5 fixes report also says the shorter route will be marked here.

**Why it matters:** a teacher with less instructional time has no principled way to shorten the course while retaining its standards and inquiry work.

**Exact fix:** add a concrete pacing alternative identifying essential tasks, shorter source selections, and extensions that can be omitted, with a stated time budget. Preserve required coverage, readiness, assessment evidence, and response. If a less-than-daily version is intended, Cory must settle that audience and time assumption before a reduced calendar is specified.

Do not describe the existing full schedule as a shorter path merely because its year has 160 teaching days.

### 7. Sensitivity and readiness notes disagree across the planning documents

**Severity:** moderate  
**LAYER:** process and frame  
**REPEAT:** yes, incomplete sensitivity flags and stale instructions in earlier grade 5 frame reads  
**Confidence:** firm

The overview says every relevant day contains “sensitivity read” in its note. Several plainly relevant rows do not, including days 21 to 24, day 101, and days 118 to 121. Unit 3 is omitted from the overview’s sensitive-unit list despite its Native alliances and violent encounters. Unit 10 needs conditional coverage for its selected research materials.

The scope also correctly identifies frame corrections for readiness, but those conflicting frame statements remain in place.

**Why it matters:** a day writer using the CSV alone can miss a required review route, while another writer can mistake retrieval for the required readiness check.

**Exact fix:**

- Include units 3 and 10 in the sensitivity overview.
- Add explicit sensitivity notes to affected day rows, including source-dependent research and assessment tasks. Keep the planned fresh-agent review for every unit.
- Apply the scope’s already-written corrections to the frame’s Days bullet and trade/money seam entries.
- Preserve the current readiness placements on days 15, 44, 60, and 147.

The former requirement for an outside community reader was superseded by the current FOUNDATION decision dated 2026-11-14. It is not reopened here.

## Coverage, order, and days by load

All 55 owned Massachusetts codes and parts have a recorded placement. All 19 lettered parts have identifiable teaching days:

| Parts | Days |
|---|---|
| T1.7a to d | 19 to 23 |
| T2.1a to d | 29 to 31, 35 to 38 |
| T2.5a to c | 47 to 48 |
| T4.3a to b | 87 to 88 |
| T4.5a to d | 98, 100, 103, 102 |
| T5.6a to b | 131 to 132 |

Placement is structurally complete. Findings 1 to 4 address the difference between placement and full teaching or assessment.

One additional completion belongs in the day-writing contract: day 31 should explicitly explain how colonial government developed and contributed to revolution. Listing legislatures, town meetings, and charters does not secure that relationship.

| Unit | Total days | Days excluding its assessment and respond day | Load judgment |
|---|---:|---:|---|
| 1 | 14 | 12 | Defensible for encounters, founding research, and regional mapping. |
| 2 | 12 | 10 | Appropriate protection for a substantial hard-history comparison. |
| 3 | 17 | 15 | Defensible for content plus the sourcing step up. |
| 4 | 16 | 14 | Dense. Day 51’s eight named leaders need short profiles and a focused comparison. |
| 5 | 16 | 14 | Reasonable for introductory constitutional reading. |
| 6 | 17 | 15 | Sufficient to repair the economic distinctions without another day. |
| 7 | 16 | 14 | Reasonable across removal, slavery’s expansion, and abolition. |
| 8 | 14 | 12 | Tight but defensible at the anchor’s introductory depth. |
| 9 | 16 | 14 | Retain the extra two days provided by the frame repair. |
| 10 | 14 | 12 | Eight research days and four action days; modelling must fit within them. |

No unit is demonstrably far over or under its load. The principal allocation risk is the assessment demand exposed by finding 1, not unequal numbers of progression rows.

No unit exceeds 25 days, so none requires the additional mid-unit assessment under the stated rule. Unit response occupies ten distinct days; course-level response occupies four more. Those allocations are counted once.

## Calendar and same-year leans

The course-level checks occur on school days 76 to 77 and 143 to 144, meeting target weeks 16 and 29. The final response day falls in week 30, which does not break the rule governing check days.

| Lean | Other subject’s availability | Disposition |
|---|---|---|
| RI.5.3 for unit 3 | ELA unit 2, days 42 to 80 | Later; day 29 supplies the organizer. |
| RI.5.6 for unit 3 | ELA unit 3, days 84 to 123 | Later; day 33 supplies the comparison model. |
| W.5.1 for unit 5 | ELA unit 3 | Later; day 72 supplies the writing frame. |
| RI.5.8 for unit 7 | ELA unit 3 overlaps | Exact earlier availability is unproved; day 108 retains its local model. |
| RI.5.3 for unit 8 | ELA unit 2 ends by day 80 | Available beforehand. |
| W.5.7 and W.5.1 for unit 10 | ELA units 2 and 3 end before day 147 | Available beforehand. |
| Coordinate grid for unit 6 | Math unit 10, days 135 to 149 | Not needed; the task uses inherited latitude and longitude. |
| Resource protection for unit 6 | Science unit 6, school days 125 to 147 | Later; day 92 supplies the industrial-cost context. |

These connections are sound at the available calendar’s resolution. A unit range alone cannot establish the exact day a particular ELA skill is taught, which is why the overlapping RI.5.8 bridge should remain.

## Candidate cells and source map

Every candidate has an explicit disposition.

| Unit | Decision and day cost |
|---|---|
| 1 | Religion and religious freedom retained within day 7. |
| 2 | Southern colonial resistance retained within day 20. |
| 3 | First Continental Congress retained within day 36. |
| 4 | Spain and Netherlands within day 49; Northwest Ordinance within day 52. |
| 5 | Additional amendment case dropped with a reason; later units supply cases. |
| 6 | Cotton gin retained within day 93. |
| 7 | Sequoyah and the newspaper retained within day 99. |
| 8 | Freedmen’s Bureau and schools within day 121; Reconstruction’s end within day 122. |
| 9 | Great Migration retained within day 130. |
| 10 | Starter topic list retained within existing research preparation, no separate day. |

These are settled planning dispositions. They are not evidence that every comparison-state attribution has been independently verified. California was checked selectively; the Tennessee PDF returned 403, and this read did not establish the New York attributions.

**Source map: not applicable.** This grade 5 course explicitly adopts no base text. A lesson-by-lesson base-text placement or cut ledger is therefore not owed.

## Lens checklist for this layer

| Scope-and-sequence check | Status | Reason |
|---|---|---|
| Unit questions require the unit’s sources and allow defensible answers | Met in design | Questions support explanation and judgment; actual source sufficiency awaits unit plans. |
| History follows time order or explains departures | Missed in part | Finding 5. |
| Contested events carry more than one account | Met in design | English and Native accounts, the King Street comparison, and later perspective work are specified. |
| Writing from sources recurs and grows | Met | Early supported claims lead to weighed accounts and several-source research; finding 3 secures the remaining teaching steps. |

The broader lens commitments are present: geographical and economic reasoning, historical perspective, student-chosen action, living Native nations, and plain treatment of hard history. Economic precision and review routing need the repairs above. Actual reading difficulty, source rights, and teacher-note quality remain unit- and day-level judgments.

## Settled by the expert

These are recommendations for the caller to apply. Nothing was edited.

| Choice | Reason | Files touched |
|---|---|---|
| Retain ten units and their present day totals | No demonstrated gross allocation defect | Scope and sequence; days CSV |
| Expand all ten assessment blueprints | Codes must correspond to assessable work | Scope and sequence; days CSV |
| Place both productivity indicators on day 90 | Its task teaches their shared content | Days CSV |
| Distinguish external effects and time horizons in unit 6 | Completes existing economic ownership | Days CSV; later unit plan |
| Add question explanations and models within unit 10 | Supplies the owned inquiry demands before independent use | Days CSV; scope and sequence |
| Replace the unit 2 freedom ladder with legal-status distinctions | Prevents a misleading historical generalization | Scope and sequence; day 22 |
| Swap Mashpee and Trail of Tears days | Repairs an unnecessary chronological reversal | Days CSV |
| Explain thematic recaps and retain parallel timelines | Preserves useful unit groupings while making chronology visible | Scope and sequence; frame |
| Make day 31’s government-development relationship explicit | Completes its existing standard | Days CSV |
| Use brief profiles for the eight day 51 leaders, with one focused comparison | Keeps the lesson plausible within 40 minutes | Later unit plan |
| Reconcile readiness and sensitivity instructions | Gives writers one consistent contract | Frame; scope and sequence; days CSV |

## What should be preserved

- Slavery in the colonies has its own substantial unit.
- The amendment process is now taught before later units use it.
- Civil rights history precedes independent civil rights research.
- Unit 3 supplies its own models before ELA reaches the related work.
- Native nations appear as present-day peoples and governments.
- Harmful simulations are prohibited, and informed action remains students’ choice.
- Calendar placement and distinct response allocations are clear.

## For Cory

- Set the intended time assumption for the shorter path: daily shorter lessons, fewer weekly meetings, or both. This is an audience and scope decision; the existing daily 40-minute course remains the full path.

## Limits and sources

Actual assessment items, scoring guidance, source selections, reading loads, and classroom timing cannot yet be judged. This is a review of their planning contracts.

Outside sources opened:

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): targeted grade 5 requirements and clarifications.
- [C3 Framework, revised June 2017 PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned indicator distinctions and elementary inquiry guidance.
- [Investigating History grade 5 course overview, June 2026](https://www.doe.mass.edu/investigatinghistory/curriculum/g5-course-overview.pdf): reference-only comparison of the historical arc and inquiry progression. Its conflicting lesson totals were not used as a pacing benchmark.
- [California history and social science standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): selective candidate checks, not a complete comparison.

**For the source list:** retain the California PDF address if it is not already recorded. The other working references are already represented in APPROACH-SOURCES.

**Verdict:** revise before unit planning. **Finding count:** 7. **Report path:** `docs/reviews/sequence-social-studies-grade-5-2026-11-14.md`, supplied here only.

