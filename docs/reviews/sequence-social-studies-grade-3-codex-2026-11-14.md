# Independent expert cold read: social-studies-grade-3

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-social-studies-grade-3-2026-11-14.md`  
**Delivery:** Complete report supplied here. No files were changed.

## Verdict

The seven-unit structure is sound, but the scope and sequence needs revision before it guides unit writing. Its biggest risk is apparent completeness: the day rows name the standards, while several required demands disappear from teaching or assessment descriptions. The most important change is to specify assessment tasks against every unit’s actual requirements, then repair the omissions below without changing the year’s unit allocations.

## What I read

- `docs/agents/EXPERT.md`, the social studies lens, `FOUNDATION.md`, the relevant ROADMAP path and gaps, BASELINE rules 20 to 24, and `GLOSSARY.md`.
- The shared adoption criteria and social studies section of `ADOPTION-BAR-SUBJECTS.md`; `docs/courses/social-studies/STANDARD.md`.
- The complete grade 3 scope and sequence, all 160 rows of `days.csv`, and the complete course frame.
- All 27 grade 3 progression rows, relevant incoming grade 1 and grade 2 rows, and the recorded exclusions.
- `docs/courses/CALENDAR.md` and grade 3 entries in `data/plans/calendar.csv`.
- `APPROACH.md`, relevant source-access notes in `APPROACH-SOURCES.md`, `BASE-TEXTS.md`, and the grade 3 outline. No social studies approach page exists.
- Both earlier grade 3 frame reports, relevant progression reports, the grade 3 frame fix record, and the social studies baseline review and fixes.
- Outside standards, curriculum references and historical sources linked below. Reference material was read only.

### Checks

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped after an unrelated missing civics sequence and a missing `markdown` dependency. |
| `python -X utf8 scripts/frame.py calendar` | Completed; no stagger-rule breaks reported. |
| `python -X utf8 scripts/frame.py check social-studies-grade-3` | Passed, 0 failures. |
| `python -B -X utf8 scripts/plan.py check social-studies-grade-3` | Passed, 0 failures. |
| `python -X utf8 scripts/stale.py check` | Crashed with `KeyError: 'node'`; no global stale-note clearance established. |
| Targeted stale check on this sequence, frame and days CSV | Passed, 3 files, 0 failures. |

The unit 1 reading-pack command also stopped because sequence-stage rows lack `check_min`; I read the source files directly.

## Findings, most serious first

### 1. End-of-unit assessments do not secure the full taught requirements

**LAYER:** sequence  
**REPEAT:** yes, incomplete semantic coverage identified in the earlier progression and grade 3 frame reads  
**Severity:** serious  
**Confidence:** firm

The assessment descriptions are narrower than the teaching they close. A skill ID in an assessment row does not establish that the task elicits that skill.

| Assessment | Unsecured demand | Exact repair |
|---|---|---|
| Unit 1, day 23 | Map construction; inquiry-question work; explanations connecting region, culture and environmental change | Require a small constructed map, a geographic explanation, and a supporting-question response alongside the source-based claim. Name the corresponding codes. |
| Unit 2, day 47 | Taxes and services, participation, cooperation’s benefits and difficulties, deliberation, and constitutional comparison | Specify an integrated town-decision case covering these demands, including an oral deliberation component and a constitutional comparison. |
| Unit 3, day 67 | Incentives, profit, money’s exchange function, nonbank institutions and interest rates | Add short tasks using the unit’s business and savings cases. The present resources and opportunity-cost tasks do not secure these requirements. |
| Unit 4, day 88 | Generating questions about multiple sources; contributions and sovereignty | Add student-generated questions about the unseen source set and a contribution/government explanation. A primary-or-secondary sort does not assess question generation. |
| Unit 5, day 120 | Explorer accounts and maps, the Mayflower Compact, hardships, relationships and leader comparisons | Specify these within the assessment blueprint, including the lettered parts. The mid-unit assessment does not replace the required complete end-of-unit assessment. |
| Unit 6, day 135 | Constitutional purpose and origins, the Bill of Rights, and the completed government comparison | Name these tasks explicitly rather than leaving them inside an unspecified claim. |
| Unit 7, day 159 | The biography, external presentation and informed-action reasoning | Identify the biography, presentation and action record as scored components of the end-of-unit assessment, alongside the unseen-source task. |

**Why it matters:** a writer can follow these rows faithfully and produce assessments that overlook substantial teaching. Response days would then act on incomplete evidence.

**Fix:** replace each brief assessment label with a code-to-task blueprint covering every taught requirement. Preserve the unseen-source task and the existing response time. Use existing project products for performance evidence, with explicit individual scoring, and establish feasibility within the current unit days before claiming complete coverage.

The distinction between source classification, source questioning, explanation and argument is supported by the [official C3 indicator tables](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

### 2. Several requirements present above this layer are lost in the day goals

**LAYER:** sequence, with frame clarification  
**REPEAT:** yes, missing parts of owned standards in the earlier grade 3 frame reports  
**Severity:** serious  
**Confidence:** firm

| Location | What is missing | Exact fix |
|---|---|---|
| Day 20, `D1.3.3-5` | It lists facts needed for supporting questions, but omits an idea open to interpretation. The current progression and frame explicitly require that work. | Add: “For each supporting question, identify one idea people could interpret differently and explain two readings.” Model one example before students supply another. |
| Day 100, `MA.3.T4.1c` and its parent | The retained Plymouth case includes Massasoit but not Samoset or the Abenaki/Wabanaki relationship. No substitution is recorded. | Include Samoset and the distinct Abenaki/Wabanaki connection in the existing first-contact account. |
| Days 113 to 116, `MA.3.T5.5` | Colonial maritime trade is taught, but colonial bartering disappears. Day 53 teaches barter generally, without applying it to colonial economies. | Add a brief retrieval and colonial barter example on day 113, then connect it to the maritime economy. |
| Day 83, `MA.3.T2.3d` | Contributions are attributed broadly to “the nations,” without requiring the local nation’s contribution. | Require one contribution from a nation connected to the school’s area, supported by that nation’s public materials, before comparing worked cases. |

**Why it matters:** these are substantive omissions, not missing code labels. The own-place adaptation changes locations and examples; it needs to preserve or explicitly dispose of the work attached to the retained codes.

**Evidence:** the current progression and frame, the [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf), and the [Massachusetts framework, PDF pages 54 to 56, printed pages 54 to 56](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

### 3. The transition to writing from two sources is assigned without a named model

**LAYER:** sequence  
**REPEAT:** yes, prerequisite and modelling gaps in the earlier grade 3 frame reads  
**Severity:** moderate  
**Confidence:** likely

Day 19 explicitly models a claim from a named source. Early assessments likewise permit one source. Day 118 then requires evidence from two named sources, but no preceding day explicitly models combining their evidence into one argument.

**Why it matters:** students may write two disconnected facts or name two sources while relying on only one. ELA’s opinion-writing calendar does not itself supply this disciplinary move.

**Fix:** extend day 19’s model using two very short sources, such as a map and a photograph. Keep the spoken and sentence-frame bridge. On days 20 to 21, rehearse naming both sources and explaining how their evidence supports the same claim; revisit this on day 117 before the more demanding colonial argument.

Multiple-source argument is part of [D4.1.3-5](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf). Explicit modelling and guided practice are also consistent with [Rosenshine’s research summary](https://www.aft.org/sites/default/files/Rosenshine.pdf); it does not establish a required number of lessons.

### 4. Day 28 turns a government comparison into an inaccurate universal structure

**LAYER:** sequence and frame  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** firm

Day 28 asks students to name “the three branches at each level.” The frame’s California candidate makes the same generalization. Local governments do not uniformly reproduce the national three-branch arrangement, and tribal governments require their own descriptions.

California’s [HSS-3.4.4](https://www2.cde.ca.gov/cacs/history?c0=12,0,4&dl=0&maxgrade=12&mingrade=0&order=0&perpage=100) does not justify teaching identical structures everywhere. For example, [Arlington’s own government description](https://www.arlingtonma.gov/town-governance) identifies its particular executive and legislative arrangements.

**Why it matters:** students could learn a false template and apply it to their town, school board or a tribal nation.

**Fix:** change day 28 to name national and state branches and the leaders at the three levels. Use days 29 to 32 to examine the actual local arrangement. On day 43, describe the selected tribal government from its own constitution without assuming three branches. Correct the candidate wording in the frame and sequence accordingly.

### 5. Unit 5 claims chronological order but follows colony case studies

**LAYER:** sequence  
**REPEAT:** new  
**Severity:** moderate  
**Confidence:** firm

The sequence says “Time order,” then teaches Plymouth on days 97 to 100, Jamestown on days 101 to 102, and St. Augustine on day 105. Their founding dates run in the opposite direction: 1620, 1607 and 1565. See the [National Park Service account](https://www.nps.gov/places/st-augustine-town-plan-historic-district-st-augustine-florida.htm) and [Florida’s historical overview](https://dos.fl.gov/florida-facts/florida-history/a-brief-history/european-exploration-and-colonization/).

**Why it matters:** this is the unit that introduces the timeline. Unexplained jumps can make teaching order look like historical order.

**Fix:** retain the case-study order, but replace “Time order” with its actual pedagogical reason: Plymouth provides the extended worked case, followed by shorter comparisons. At the opening of each colony case, locate its founding date on the same timeline and explicitly identify the backward or forward jump. Apply the same explanation to the frame.

This is an allowed departure from chronology once its reason is stated.

### 6. Operational notes still contradict the current plan

**LAYER:** process  
**REPEAT:** yes, stale-note findings in the earlier grade 3 frame reports  
**Severity:** minor  
**Confidence:** firm

| Location | Problem | Exact fix |
|---|---|---|
| Days 25, 49 and 125 notes | Reteaching is assigned to “day 2,” although the CSV uses course-day numbering. | Replace with days 26, 50 and 126 respectively. |
| Frame, Cross-subject table | Unit 7 still occupies about days 137 to 156. | Replace with days 141 to 160, as the sequence already requests. |
| Frame, sensitivity preparation | Unit 2’s Native-government content is omitted from the preparation list. | Apply the sequence’s existing correction naming the local nation’s government pages and selected constitution. |
| Grade 3 outline, final settled list | Mashpee Wampanoag remains the Northeast worked case after the recorded change to Penobscot. | Replace that current settled entry with Penobscot and cite the November 14 baseline fix. Preserve historical review records. |
| Sequence, compressible-days explanation | It treats repeated codes on days 7 and 23 as protection for day 10’s construction demand, although those goals specify reading rather than constructing a map. | State explicitly which adjacent day receives the construction task when day 10 is folded. Do not describe code repetition as equivalent task coverage. |

**Why it matters:** these notes guide implementation and the shorter route. They can send writers to the wrong day or preserve a label while losing the intended work.

## Coverage, order and load

### Lettered parts

All ten separately loaded lettered codes have teaching placements. Their assessment coverage remains subject to finding 1.

| Parts | Teaching days | Judgment |
|---|---|---|
| `MA.3.T2.3a` | 75, 77 to 81 | Named nations secured. |
| `MA.3.T2.3b` | 75, 78 | Homelands and present lands secured. |
| `MA.3.T2.3c` | 76, 77, 79 to 82 | Settlement explanations secured. |
| `MA.3.T2.3d` | 83 | Local contribution needs finding 2’s clarification. |
| `MA.3.T4.1a` | 98 | Compact and self-government secured. |
| `MA.3.T4.1b` | 99 | Hardships secured. |
| `MA.3.T4.1c` | 100 | Partial, finding 2. |
| `MA.3.T5.5a` | 113 | Fishing and shipbuilding secured. |
| `MA.3.T5.5b` | 114 | Atlantic, Caribbean and forced-labor trade secured. |
| `MA.3.T5.5c` | 115 | Authorized general-form port comparison secured. |

The official framework’s additional subparts under `3.T1.3` are substantively placed across days 26 to 40: school decisions, local services, government forms, participation, volunteering and property taxes. The loaded paraphrase does not expose those as separate codes.

`MA.3.T6.2` is deliberately excluded with its grade 5 destination recorded. I do not reopen that settled scope decision.

### Load and internal order

“Teaching days” below includes understanding, fluency and application days.

| Unit | Total | Teaching | Assessment/respond | Load judgment |
|---|---:|---:|---:|---|
| 1 | 24 | 22 | 2 | Defensible for geography plus the first inquiry model. |
| 2 | 24 | 22 | 2 | Defensible for five owned rows and dormant civics retrieval. Day 28 needs correction. |
| 3 | 20 | 18 | 2 | Defensible for four rows, with savings revisited across several days. |
| 4 | 18 | 16 | 2 | Substantial but defensible: two local-content days, five worked-case days, source work and synthesis. |
| 5 | 32 | 29 | 3 | The largest allocation fits six rows and extensive historical content. Chronological departures need explanation. |
| 6 | 12 | 10 | 2 | Defensible because Revolution events remain in grade 5. |
| 7 | 20 | 18 | 2 | Tight: seven project-content days, three biography days, one presentation day and five action days precede review and assessment. |

No whole-unit allocation is demonstrably far over or under its load. The two tightest individual slots are day 28 and day 105, which combines mid-unit response with the third colony. Protect day 105’s response time explicitly when producing the shorter route.

Readiness is correctly placed at the first relevant use: days 1, 25, 49 and 125. Unit 5 has its required mid-unit assessment on day 104. Response time is counted once: seven unit respond days, four course respond days, and the embedded mid-unit response on day 105.

## Calendar and same-year leans

Course-level checks fall on school days 69 to 70, 122 to 123 and 137 to 138: weeks **14, 25 and 28**. These match the target calendar. The year-end check deliberately precedes unit 7 and excludes its content; unit 7 has its own assessment.

| Lean | Calendar evidence | Judgment |
|---|---|---|
| ELA opinion writing | Unit 3, days 81 to 119 | Early spoken and sentence-frame bridge is present. Finding 3 supplies the separate two-source model. |
| ELA discussion | Unit 1, days 1 to 39 | Social studies independently teaches norms on day 38. |
| ELA maps and illustrations | Unit 1, days 1 to 39 | Available before social studies day 73; a local model is also named. |
| ELA research, informative writing and reporting | Units 1 to 3, completed before unit 7 | Calendar supports the late project. |
| Math addition/subtraction within 1,000 | Unit 3, days 39 to 59 | Savings stay within 100 until day 60. |
| Science climate | Unit 6, school days 123 to 147 | Social studies day 6 supplies its own bridge. |

The calendar establishes unit availability, not the exact first teaching day of every peer-subject standard. Where that remains uncertain, the local bridges protect this sequence.

## Candidate dispositions and source map

| Candidate | Disposition and cost |
|---|---|
| New York location vocabulary/world communities | Kept on day 4; no additional day. |
| California branches and local tribal governments | Kept within unit 2; wording and placement corrected by finding 4. |
| California specialization/division of labor | Kept on day 52; economic change on day 145. |
| California tribal-government relationships | Kept on day 84. |
| Tennessee French and Dutch colonies | Kept on day 94; no additional day. Attribution could not be independently rechecked because the official PDF returned 403. |
| California landmarks/documents | Kept on day 132. |
| California community history/economic change | Kept within unit 7, especially day 145. |

The general promise to read Tennessee civics during unit planning is not a separately defined addition. Retain that comparison obligation without implying that additional content has already been selected.

King Philip’s War is explicitly not placed here, with its grade 5 destination stated.

**Source map:** not applicable. This course has no adopted base text.

## Scope and sequence lens checklist

| Checklist line | Status | Evidence |
|---|---|---|
| Compelling questions require sources and allow defensible answers | Met at sequence depth | The place, government, economy, Native-nation and community questions support evidence-based explanations. Actual prompts and source sets still require unit review. |
| History runs in time order, or a reason is given | Missed | Finding 5. |
| Contested events carry more than one telling | Met at sequence depth | Explorer/Native accounts, Wampanoag accounts, the 1622 conflict and colonial/Native evidence are explicitly paired. |
| Writing from sources recurs and grows | Partly met | Claims recur every unit and grow to two-source work, but the transition lacks an explicit model, finding 3. |

## Settled by the expert

These are recommendations for the caller to apply.

| Choice | Reason | Files affected |
|---|---|---|
| Keep seven units and their current totals | No demonstrated whole-unit load defect warrants reshaping | Frame and sequence |
| Restore the missing requirements on their existing days | Completes existing ownership without adding scope | Days CSV and sequence |
| Model two-source argument within days 19 to 21 | Preserves the early literacy bridge while teaching the disciplinary move | Days CSV and sequence |
| Compare actual local and tribal structures | Avoids an inaccurate universal template | Frame, sequence and day 28 |
| Keep colony case-study order with an explicit reason and timeline resets | Repairs chronology without moving standards between units | Frame and sequence |
| Preserve map construction and mid-unit response in the shorter route | Compression must preserve the work, not just the codes | Sequence and day notes |
| Count project products explicitly within unit 7’s assessment | Makes its performance requirements assessable | Day 159 and later assessment blueprint |

## What is right and should not be touched

- Place, government and economics prepare students for the later historical and community inquiries.
- Native nations appear before European arrival and remain present-day peoples and governments.
- The current citizenship, voting and equal-rights distinction repairs the earlier inaccurate generalization.
- The own-place method, privacy protections, paper path and prohibition on harmful simulations are appropriate.
- State constitutional purpose is taught before constitutional comparison.
- Calendar staggering, readiness placement and reserved response time are sound.
- Informed action remains a class choice grounded in its project.

## Limits and sources

This is a sequence review, not certification of unwritten lessons, assessment items, source difficulty, rights clearance or sensitivity. Actual 40-minute feasibility remains untested.

The New York framework was checked from the stored official PDF using read-only extraction after the web request timed out. Tennessee’s official PDF and the Library of Congress guide returned 403. No substantive finding rests solely on memory; saved memory was used only for review workflow.

Sources used:

- [C3 Framework, revised 2017](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): targeted indicator meanings.
- [Massachusetts History and Social Science Framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): grade 3 requirements, including lettered parts.
- [California official standards](https://www2.cde.ca.gov/cacs/history?c0=12,0,4&dl=0&maxgrade=12&mingrade=0&order=0&perpage=100): candidate wording.
- [New York K to 8 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): stored copy, PDF page 42, printed page 41, for location work.
- [Investigating History, grade 3 unit 2](https://www.doe.mass.edu/investigatinghistory/curriculum/units.aspx?grade=3&unit=2): limited comparison of historical inquiry structure and perspectives.
- [Leadership and Government inquiry](https://c3teachers.org/inquiries/leadership-and-government/): limited comparison of supporting questions, evidence and culminating argument.
- [Rosenshine, Principles of Instruction](https://www.aft.org/sites/default/files/Rosenshine.pdf): modelling and guided practice.
- [Arlington government description](https://www.arlingtonma.gov/town-governance): municipal structural variation; search-visible official text, full page blocked.
- [National Park Service, St. Augustine](https://www.nps.gov/places/st-augustine-town-plan-historic-district-st-augustine-florida.htm): colony chronology.

**For the source list:** add the municipal-government and St. Augustine routes with these limited uses and access notes.

## For Cory

None. The recommendations complete existing requirements and make item-level choices within the agreed course scope. The daily block and agent sensitivity-read arrangements are already recorded decisions.

**Verdict:** revise before unit writing. **Finding count:** 6. **Report path:** `docs/reviews/sequence-social-studies-grade-3-2026-11-14.md`, delivered here only.

