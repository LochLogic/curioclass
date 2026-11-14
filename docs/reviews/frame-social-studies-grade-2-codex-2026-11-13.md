# Independent expert read: grade 2 social studies course frame

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-social-studies-grade-2-2026-11-13.md`  
**Delivery:** Complete report supplied here. No files were changed or created.

## Verdict

The frame has a sound overall structure, sensible handoffs and a plausible 96-day budget, but needs revision before it directs detailed planning. Its biggest risk is incomplete teaching hidden behind complete standard-code coverage, particularly countries and government, and regional change. Complete those requirements within their existing units, correct the source claims and map prerequisites, and retain the present unit sequence.

**Finding count: 12: five curriculum or planning findings and seven stale-note findings.**

## What I read and checked

- `docs/agents/EXPERT.md` and `docs/agents/lenses/social-studies.md`.
- `docs/FOUNDATION.md`, the requested ROADMAP sections, BASELINE rules 20 to 24, `docs/GLOSSARY.md`, `docs/APPROACH.md` and relevant source-access and evidence notes in `docs/APPROACH-SOURCES.md`.
- Section 1 and the relevant shared criteria of `docs/ADOPTION-BAR-SUBJECTS.md`.
- `docs/courses/social-studies/STANDARD.md`.
- The complete grade 2 frame, its `frames.csv` row, grade 1 and grade 3 frames, and the grade 3 outline.
- Grade 1 to 3 social studies progression rows, the exclusions, the local Massachusetts standard descriptions and C3 code inventory.
- Relevant grade 2 ELA, mathematics and science progression rows.
- `docs/sources/BASE-TEXTS.md` and relevant portions of the social studies open-material review.
- Earlier social studies progression reviews and their fix report, cross-subject reviews and fixes, the earlier social studies content review, and relevant review-history and digest instructions.

There is no grade 2 social studies base text or source map. I found no same-grade ELA, mathematics or science course frame, and no social studies approach page.

### Checks

| Check | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check`, run first | Stopped with `ModuleNotFoundError: No module named 'markdown'`. No complete gate result was obtained. |
| Direct frame checks for grades 1, 2 and 3 | All returned **0 failures**. |
| Social studies progression check | **384 rows, 0 failures**, with depth and skipped-grade notes. |
| `scripts/stale.py check` | **0 failures** on both runs. It inspected 11 files initially and 19 on the later run. |

The dependency error is an environment limitation, not evidence that this frame fails the plan gate. The full frame check also reported CSV disagreements for other courses. Those are outside this review.

No finding rests solely on model memory. Recommendations about question quality and workload are professional judgments, identified below.

## Findings, most serious first

### F1. Unit 4 teaches only part of the country standard

**LAYER:** standard, frame  
**REPEAT:** yes, incomplete standard-to-task mappings recur in the earlier social studies progression reads  
**Severity:** serious  
**Confidence:** firm

**What is wrong.** Unit 4 lists land, borders, people, government, laws, capital and flag. It does not secure the purposes of government or how history, culture, language and type of government distinguish countries. The official clarification to `MA.2.T4.2` includes these requirements. The local standard paraphrase also omits them. [Massachusetts framework, PDF page 47, printed page 47](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

Its reason also describes grade 1’s “elected government as what every country has.” A busy writer could reasonably turn that into the false claim that all countries have elected governments.

**Why it matters.** Students could finish the unit able to identify flags and borders without explaining what governments do or how countries differ. The shortened standard record makes the omission harder for later writers to detect.

**Exact fix.**

In unit 4 and `ss2-countries`, add:

> Explain purposes of government, including helping provide safety and education. Compare two countries using their history, culture, language and ways of governing. Countries have governments, but governments are not all chosen through elections.

Replace the unit’s election wording with:

> Uses grade 1’s idea of government, then distinguishes that idea from the different ways countries choose leaders and govern.

Expand the own-word entry for `MA.2.T4.2` in `data/standards/ma-hss-2018.txt` to retain those clarification requirements. Keep the standard in unit 4 and retain its 10 days.

### F2. The regional-change repair still leaves part of its C3 indicator untaught

**LAYER:** progression, frame  
**REPEAT:** yes, `progression-social-studies-codex-2026-11-13.md`, finding 1, and its subsequent fix  
**Severity:** serious  
**Confidence:** firm

**What is wrong.** `ss2-climate-regions` and unit 2 now compare **one region at two dates**, using environmental examples. `D2.Geo.10.K-2` requires change in both physical and cultural characteristics across various world regions. [C3 Framework, PDF page 44, printed page 43](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

Unit 6’s migration content does not explicitly complete that regional comparison. The earlier repair was useful but too narrow.

**Why it matters.** A writer can follow the repaired row faithfully and still build only a glacier or lake comparison.

**Exact fix.** In unit 2 and the progression note, replace the single-region requirement with:

> Compare two world regions at two dates. Use selected maps, photographs and captions to describe changes in physical features and in homes, work or everyday customs. Identify what changed and what stayed, using the sources.

Replace a repeated climate example within the existing 13 days. Use familiar grade 1 ways-of-living vocabulary before introducing new terms.

### F3. The frame overstates its source comparisons and anchor order

**LAYER:** frame  
**REPEAT:** yes, inaccurate source-to-course mappings were identified in `social-studies-expert-read-2026-11-12.md`  
**Severity:** moderate  
**Confidence:** firm

**What is wrong.**

- The opening claims Massachusetts topic order, but resources and countries precede migration here. The unit reasons justify those changes, so the sequence itself is defensible.
- Every check-set entry says “confirmed in the unit plan’s comparison table,” although those unit plans do not exist.
- New York grade 2 is cited for world-continent comparisons and country reports. Its grade 2 focus is community comparison; its explicit world-community course is grade 3. [New York framework, grades 2 and 3](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf).
- No unit identifies a Tennessee contribution or corroborating code.
- The Ellis Island and Angel Island pairing is presented as a check-state addition without a source establishing that specific pairing.

**Why it matters.** Later writers cannot distinguish a checked requirement from an illustrative choice or proposed extension.

**Exact fix.**

Replace the opening order claim with:

> Seven units organized from the Massachusetts grade 2 topics. Resources and countries precede migration so students can explain movement using places, resources and borders. The country report gathers the year’s learning.

Replace each “confirmed” sentence with:

> Candidate comparison, to be verified in the unit plan.

Use these precise starting references:

| Unit | Correct comparison record |
|---|---|
| 1 | California `2.2.2`, map labeling; Tennessee `2.10`, maps and globes |
| 2 | Identify continent-wide photographs as a Curio Class illustration of its anchor content, rather than a New York grade 2 requirement |
| 3 | California `2.4.1` for food production; New York `2.1` for community types; Tennessee `2.04` for industries |
| 4 | California `2.3.2` for interaction among nations; Tennessee `2.11` and `2.07` to `2.08` for maps and trade |
| 5 | Label the island pairing as a Curio Class example requiring item-level sources |
| 6 | California `2.1.1` for family-history evidence; Tennessee `2.01` to `2.02` for cultural comparison |
| 7 | Retain the country report under `MA.2.T4.3`; identify any additional comparison separately |

The California references support several existing choices. [California grade 2 standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf). Tennessee references were checked against the official crosswalk’s **new 2024** column. [Tennessee crosswalk](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf).

### F4. Unit 6’s question invites a list instead of a conclusion from evidence

**LAYER:** frame  
**REPEAT:** yes, the need for defensible competing answers appears in `ela-6-spine-2026-11-11.md`, finding 4  
**Severity:** moderate  
**Confidence:** likely

**What is wrong.** “What do people bring with them when they move?” can be answered by listing belongings, languages, foods and customs. Students need not use the unit’s interviews or evidence about changes to newcomers and communities.

**Why it matters.** The unit can become a cultural inventory while appearing to run the inquiry arc. Sustained inquiry and conclusions drawn from coherent sources are also emphasized by the external instructional-material criteria. [Social studies materials criteria, criterion 2](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf).

**Exact fix.** Use:

> When people move, do they change their new community more, or does it change them?

Keep the present question as a supporting question. Add supporting questions about changes to newcomers and changes to the receiving community. Close with a modeled claim using the supplied sources. Do not ask students to rank cultures or disclose private family experiences.

### F5. The map prerequisites still name ruler measurement instead of repeated units

**LAYER:** progression  
**REPEAT:** yes, wrong code-to-task mappings recur in the social studies and cross-subject progression reads  
**Severity:** moderate  
**Confidence:** firm

**What is wrong.** `ss2-map-parts` and `ss2-make-map` still lean on `2.MD.A.1`, although both count repeated whole units and explicitly avoid ruler measurement. The frame already identifies the correction, but the data remains unchanged.

The mathematics progression places repeated-unit measurement in `m1-measure-length-units`, owning `1.MD.A.2`. Ruler measurement belongs to grade 2’s later unit 3.

**Why it matters.** The recorded dependency suggests an unavailable prerequisite and invites a writer to introduce measurement beyond the stated map-scale boundary.

**Exact fix.** Change both `cross_subject` cells to:

> `math:1.MD.A.2 (length as a whole number of equal units laid end to end)`

Move the frame’s mathematics entry into an earlier-grade prerequisites table. Rewrite its lead note as a completed correction once applied.

### F6 to F12. Unmarked stale notes remain

Each row below is a separate finding. All are **minor**, **LAYER process**, **REPEAT yes**, and **confidence firm**. Earlier social studies and cross-subject reviews already identified this kind of stale status wording.

| ID | What is wrong and evidence | Why it matters | Exact rewritten note |
|---|---|---|---|
| **F6** | Grade 2 frame, “For the lead” item 4, says the CSV disagrees. Its row is already `social-studies-grade-2,7,96`; the direct check passes. | Sends the next worker to repair an agreement. | “The grade 2 CSV row agrees with this frame: 7 units, 96 days. The direct frame check passes.” |
| **F7** | Grade 1 frame, final note, makes the same disagreement claim. Its row and direct check agree: 8 units, 96 days. | Leaves the incoming seam attached to a false blocking note. | “The grade 1 CSV row agrees with this frame: 8 units, 96 days. The direct frame check passes.” |
| **F8** | `docs/GLOSSARY.md`, “course frame,” says “Not built.” Multiple frames exist, including this one. | Misstates the location and maturity of a core planning artifact. | “`docs/courses/<course>/frame.md`; totals in `data/plans/frames.csv`; PRODUCTION-PATH step 2.” |
| **F9** | `docs/ROADMAP.md`, social studies status near lines 95 to 96, says its content standard remains open for Cory. `STANDARD.md` records the decision and implementation. | Can reopen an already settled scope decision. | “Social studies uses C3 skills and the Massachusetts 2018 content anchor under the recorded check-set and values rules. Planning follows PRODUCTION-PATH.” |
| **F10** | `docs/APPROACH.md`, opening paragraph, places the English language arts subject page in the future. `docs/APPROACH-ELA.md` exists. | Obscures an existing source of literacy guidance. | “Mathematics and English language arts have subject pages: APPROACH-MATH.md and APPROACH-ELA.md. Science and social studies subject pages remain to be written.” |
| **F11** | ROADMAP layer 3 status likewise says the ELA page will follow when its course opens. | Duplicates the incorrect prerequisite status. | “The shared approach, mathematics page and English language arts page exist. Science and social studies subject pages remain to be written; review status is recorded on the relevant pages.” |
| **F12** | The social studies progression fix report’s “Not done” section says cross-subject verification waits for the other progressions. Those files and the later cross-subject read and fix report now exist. | Makes completed follow-up look unassigned. | “Superseded by progression-cross-fixes-2026-11-13.md: the other progressions now exist and received the cross-subject read and fix pass. Same-year timing still requires course frames. The grade 2 map prerequisite correction remains identified in this frame review.” |

For F12, preserve the dated report as history and carry the replacement disposition in the current follow-up record. The stale checker’s clean result does not settle these unmarked notes.

## Ownership, standards and days

The frame places **all 18 owned skills exactly once**. It names **17 owned Massachusetts codes and 25 C3 indicators**. Six shared economics standards are excluded here with explicit grade 1 ownership, rather than silently dropped.

| Unit | Days | Owned skills | Content standards | Judgment |
|---|---:|---|---|---|
| 1. Maps | 16 | map-parts, projections, make-map, source-maker | `MA.2.T1.1` to `.3` | Appropriate foundation and time allocation |
| 2. Land, water and climate | 13 | continents-features, climate-regions, claim-sources | `MA.2.T2.1` to `.3` | Plausible; complete F2 |
| 3. Living with the land | 16 | people-environment, resources-industries, people-resource | `MA.2.T2.4`; `MA.2.T5.1` to `.3` | Larger allocation justified by economics and action |
| 4. Countries and trade | 10 | countries, trade-world | `MA.2.T4.1` to `.2` | Plausible; complete F1 |
| 5. People on the move | 14 | why-people-move, nation-of-immigrants, two-accounts | `MA.2.T3.1` to `.2` | Sources and hard-history care justify the allocation |
| 6. Family stories and culture | 10 | family-interviews, culture-migration | `MA.2.T3.3` to `.4` | Plausible; revise the inquiry question |
| 7. Country report | 12 | country-report | `MA.2.T4.3` | One substantial integrated skill justifies 12 days |
| **Units** | **91** | **18 skills** | | |
| Course-level assessment and response | **5** | Three assessment days, two respond days | | Explicitly budgeted |
| **Course** | **96** | **32 weeks at three lessons weekly** | | Internally coherent |

No unit is demonstrably far over or under its share. These are frame-level judgments, not observed teaching times.

For `MA.2.T2.1`, the progression explicitly requires physical features on **each** continent. Preserve that wording when expanding unit 2: the frame’s illustrative list currently names features from only four continents. I have not treated an illustrative list as an exclusion of the other three.

## Sequence, seams and cross-subject dependencies

The actual unit order has defensible reasons. Maps precede their use; regions precede adaptation and resources; resources precede trade; countries precede mapped migration; migration precedes interviews and cultural effects; the report comes last. Timeline and continuity-change work already exist in earlier grades, so their review before grade 2’s later elaboration is not a sequencing fault.

Grade 1’s incoming skills are picked up. Grade 2’s outgoing skills are answered by grade 3’s frame, including map scale, sourcing, independent accounts, claims, migration, interviews and the action cycle. The later-recorded interview is correctly preserved as possible primary evidence. Those earlier repairs should remain closed.

| Dependency | Current evidence | Conclusion |
|---|---|---|
| Map scale | Grade 1 mathematics owns repeated-unit measurement | Correct the recorded lean under F5 |
| Written claims | Grade 2 ELA practices opinion writing in its later module 4 | The early shared-writing bridge is necessary; independent writing must wait for demonstrated readiness |
| Text comparison | Grade 2 ELA owns `RI.2.9` | The supplied comparison chart is a reasonable bridge |
| Interviews | Grade 2 ELA’s discussion row owns `SL.2.3` | Class practice before the interview is appropriate |
| Research | ELA research occurs in modules 2 and 3 | The late country report is plausibly placed |
| Land and water modeling | Grade 2 science owns `2-ESS2-2` and itself uses earlier social studies vocabulary | Social studies can teach naming and locating first; it must not assume science modeling is already complete |
| Earlier science | Relevant kindergarten rows exist | Retrieval is appropriate; resources and industries still need direct social studies instruction |

The same-year bridges are credible. **Teaching dates are not verified**, because the other grade 2 course frames do not yet exist.

## Course-frame lens checklist

| Checklist line | Status | Evidence |
|---|---|---|
| Every anchor standard in the topic range has a unit | **Met for placement; missed for full teaching** | All codes are placed; F1 identifies incomplete content |
| Replaced grade 3 or grade 8 own-state content avoids Massachusetts-only teaching | **Not applicable** | This is grade 2; its interview localization is appropriate |
| Every unit names check-set additions with a recorded source | **Missed** | F3: broad attributions, premature confirmation and no Tennessee unit references |

Relevant commitments from the broader lens:

| Commitment | Status at this layer |
|---|---|
| Inquiry arc in every unit | **Missed** until F4 is repaired |
| Content and models taught before use | **Met**, subject to F5’s prerequisite correction |
| Sources used as evidence, including more than one account | **Met as a design commitment** |
| Claims supported with named sources | **Met** |
| Chronology, causation, continuity and perspective | **Met**, except F2’s incomplete regional-change requirement |
| Geography and economics as reasoning | **Met** |
| Informed action once yearly, with student choice | **Met** |
| Values rule and plain, age-suited hard history | **Met as a design commitment** |
| Sensitive-topic notes and prohibited harmful simulations | **Met as a design commitment** |
| Actual source difficulty, rights, assessment quality and daily execution | **Not applicable to final judgment at frame level** |

## Settled by the expert

These are corrections within existing ownership. No standard moves between units or grades.

| Choice | Reason | File touched |
|---|---|---|
| Complete government purposes and country distinctions in unit 4 | Finishes the owned standard | Grade 2 frame; social studies progression; Massachusetts standard description |
| Use two regional comparisons covering physical and cultural change | Completes the existing indicator | Grade 2 frame; `ss2-climate-regions` |
| Replace unit 6’s compelling question; retain its current question as supporting | Requires a conclusion from the unit’s evidence | Grade 2 frame |
| Use `1.MD.A.2` for the two map-scale leans | Matches the actual repeated-unit task | Social studies progression and frame |
| Preserve the current unit order and day totals | Reasons and workload are plausible | Grade 2 frame |
| Mark check-set entries as candidates until verified | Separates evidence from planning intentions | Grade 2 frame |
| Apply the seven status replacements above | Removes obsolete instructions without reopening decisions | Files identified in F6 to F12 |

## What is right and should not be touched

- Maps first and the report last.
- Explicit division of the shared economics topic between grades 1 and 2.
- Concrete whole-unit scale before later measurement sophistication.
- Source independence checks.
- A country report ending in an argument.
- Native nations presented as living peoples and governments.
- Plain treatment of forced movement, with no victim or perpetrator simulations.
- Alternatives to personal family disclosure.
- A safe action cycle checked against published advice.
- Assessment and respond days counted within the course total.

## What I could not judge

- The complete repository-wide plan gate.
- Actual reading difficulty, item-level reuse rights or historical accuracy of unselected excerpts.
- Whether end-of-unit assessments include suitable unseen sources.
- Observed lesson duration or final section pacing.
- Confirmed teaching dates in the other grade 2 subjects.
- A complete numbered home calendar and shorter path.
- A social studies subject approach that has not yet been written.

External curriculum benchmarking was limited. I inspected the [Louisiana grade 2 unit sequence](https://doe.louisiana.gov/docs/default-source/teacher-toolbox-resources/bayou-bridges-unit-progressions.pdf) and [grade 2 course description](https://www.coreknowledge.org/free-resource/louisiana-bayou-bridges-grade-2/). They offer structural comparison, not evidence that Curio Class should adopt their different content order. The Michigan Open Book grade 2 route was inaccessible. No finding relies on its contents.

## For Cory

- Confirm the audience’s time assumption: three 30 to 40 minute lessons weekly.
- Set the still-open K to 2 device assumption before presentation and tool requirements become fixed.
- Arrange the required qualified community read of Native and hard-history content before publication.

No outreach or spending occurred.

## Sources and source-list follow-up

Sources were reopened for this review unless an access limitation is stated above.

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): grade 2 content, clarifications and shared economics.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned indicator meanings and grade-band depth.
- [California standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): precise check-set references.
- [New York framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): distinction between grade 2 community study and grade 3 world communities.
- [Tennessee 2024 crosswalk](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf): accessible official comparison route; use the new-standard column. The main department page returned 403.
- [Social studies instructional-material criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): inquiry, coherent sources and evidence-based conclusions.
- Louisiana sequence and course-description links above: limited structural benchmarking only, reference use.

**For the source list:** record the working Tennessee crosswalk route, the inaccessible Michigan route, and the precise uses above. Nothing was copied into course materials.

**Verdict: revise before detailed planning. Finding count: 12. Report path: `docs/reviews/frame-social-studies-grade-2-2026-11-13.md`, supplied here only.**