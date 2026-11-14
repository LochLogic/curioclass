# Independent review: Grade 4 social studies course frame

**Date:** 2026-11-13  
**Intended report:** `docs/reviews/frame-social-studies-grade-4-2026-11-13.md`  
**Delivery:** Report supplied here only. No files changed.

## Verdict

The frame has a sound structure, sensible neighboring-grade handoffs, and a workable full-year budget, but it needs revision before scope and sequence writing. Its largest risk is that complete standard-code coverage conceals narrower teaching requirements in several unit descriptions. The most important change is to restore the required student performances while keeping the seven-unit structure.

## What I read and checked

- `docs/agents/EXPERT.md`, the social studies lens, `docs/FOUNDATION.md`, BASELINE rules 20 to 24, and the relevant ROADMAP sections.
- Section 1 of `docs/ADOPTION-BAR-SUBJECTS.md`, `docs/courses/social-studies/STANDARD.md`, `docs/APPROACH.md`, and relevant entries in `docs/APPROACH-SOURCES.md`.
- The Grade 4 frame in full, its `frames.csv` row, all 17 Grade 4 social studies progression rows, and relevant Grade 3 and Grade 5 progression rows.
- The Grade 3 and Grade 5 social studies frames.
- The Massachusetts Grade 4 content standards and the Grade 4 course’s C3 indicators.
- Relevant progression reviews, cross-subject reviews, their fix records, and the social studies source reviews.
- Grade 4 math and science scope and sequence documents and relevant math, science, and ELA progression rows.
- `docs/sources/BASE-TEXTS.md`, the frame-writing brief, and the checks’ documented boundaries.

Outside reading included the Massachusetts course overview and a New York inquiry as limited curriculum comparisons. These were references only, not material for adaptation. No material finding rests solely on memory.

### Gate results

| Command | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Stopped with `ModuleNotFoundError: No module named 'markdown'` |
| Targeted `plan.py check social-studies-grade-4` | 0 failures, but checked 0 items and 0 wrong answers |
| `frame.py check` | Grade 4 passed with 0 failures |
| `progression.py check social-studies` | 384 rows, 0 failures |
| Final `stale.py check` | 19 files, 0 failures |

The full plan gate is **unverified**, not passed. The frame and progression checks establish placement and identifier consistency; they do not establish the full meaning of the standards.

## Ownership, order, and time

All 17 owned skills appear in exactly one unit. Their rows name 39 Massachusetts content standards and 19 distinct C3 indicators.

| Unit | Days | Owned skills |
|---|---:|---|
| 1. North America on the map | 16 | `ss4-map-scale`; `ss4-political-map` |
| 2. Our neighbors | 22 | `ss4-canada-mexico-research`; `ss4-trade-north-america` |
| 3. First peoples | 18 | `ss4-first-peoples-evidence`; `ss4-native-nations-sites` |
| 4. Voyages and conquest | 20 | `ss4-primary-source`; `ss4-exploration` |
| 5. United States growth | 24 | `ss4-westward-growth`; `ss4-mexico-lands`; `ss4-choice-and-force` |
| 6. Regions, states, land and resources | 26 | `ss4-states-and-statehood`; `ss4-state-maps`; `ss4-regions-resources`; `ss4-national-capital` |
| 7. Regions, peoples and hazards | 24 | `ss4-regional-cultures`; `ss4-disasters-response` |
| **Units** | **150** | **17 skills** |
| Course-level checks and respond days | **10** | Six check days and four respond days |
| **Course** | **160** | Matches `frames.csv` |

No unit is demonstrably far over or under its share. Unit 6 has four broad rows and 16 owned codes; Unit 7 has two broad rows and 14 codes. Their 26 and 24 days are defensible despite their different row counts.

The sequence teaches maps before later applications, research before historical inquiry, and sourcing before the second course-level check. Moving Mexican territorial history into Unit 5 has an explicit chronological reason. The thematic division of regional study between Units 6 and 7 is also explained.

For comparison, the Massachusetts reference course budgets 116 lessons of 30 minutes. Curio Class budgets substantially more time, so feasibility should be tested rather than inferred from that reference’s pacing. This comparison does not justify cutting days mechanically. [Massachusetts Grade 4 course overview, printed page 8](https://www.doe.mass.edu/investigatinghistory/curriculum/g4-course-overview.pdf)

## Findings, most serious first

### 1. Unit 6 substitutes a state map for the required Northeast region map

**LAYER:** standard  
**REPEAT:** yes, the same completeness problem as finding 2 of `progression-social-studies-codex-2026-11-13.md`  
**Confidence:** firm

**What is wrong:** Unit 6 and `ss4-state-maps` prescribe one state map per region. `MA.4.T4a.2` instead requires a map of the Northeast region. The single-state pattern fits several later regional standards, but it cannot replace this artifact. [Massachusetts framework, printed page 64](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf)

**Why it matters:** A writer following the frame would build five state-map tasks and still miss a claimed standard.

**Exact fix:** In Unit 6 and the progression row, replace the common recipe with:

> Construct one Northeast region map and one state map for each of the Southeast, Midwest, Southwest and West. Each map includes the features required by its own anchor standard.

Keep the existing title, scale, compass and key requirements. For the Southwest map, explicitly retain historical Native movements alongside present reservation lands; “homelands and reservations” alone narrows the required historical layer.

### 2. Unit 7 narrows its catastrophe indicators to natural hazards

**LAYER:** standard  
**REPEAT:** yes, the same kind as finding 1 of the earlier social studies progression reads  
**Confidence:** firm

**What is wrong:** Unit 7 and `ss4-disasters-response` list natural hazards only. Their C3 claims also require technological or human-made catastrophes, effects on settlement and migration, and problem-solving examples beyond the local and regional scales. [C3 Framework, printed pages 42, 43 and 61](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf)

**Why it matters:** Preparedness advice and a policy history can fill the unit without teaching those missing parts.

**Exact fix:** Add this requirement to both artifacts:

> Compare a natural catastrophe with a technological or human-made catastrophe. Use before-and-after settlement information and a movement map to explain displacement and effects elsewhere. Include an international comparison showing a response challenge and an opportunity created by that response.

Fit the comparison inside the existing 24 days. Keep the students’ action local, safe and chosen by them.

### 3. Unit 3 leaves two archaeological performances implicit

**LAYER:** frame  
**REPEAT:** yes, the same partial-standard problem as the earlier bundled-code finding  
**Confidence:** likely

**What is wrong:** Unit 3 specifies migration theories, archaeological methods, culture-region maps and preserved sites. It does not explicitly require students to identify characteristics of ancient societies from photographic evidence or explain why preserving the sites matters to a fuller account of American life. These are parts of `MA.4.T2.2` and `MA.4.T2.4`. [Massachusetts framework, printed pages 62 to 63](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf)

**Why it matters:** The current description could produce an 18-day migration inquiry with named sites but little teaching about the societies that built them.

**Exact fix:** Add to “What students learn”:

> Use culture-region maps and photographs to identify archaeological characteristics of ancient societies. Explain what the selected preserved sites contribute to the history students can tell.

Make the second sentence explicit in `ss4-native-nations-sites` as well. Retain the present-day nations, origin-account distinction and restrictions on sacred knowledge.

### 4. Two disciplinary step-ups are not secure in the frame

**LAYER:** frame  
**REPEAT:** yes, the same code-to-performance problem as earlier progression finding 1  
**Confidence:** likely

| Location | What is missing | Exact fix |
|---|---|---|
| Unit 4, `D2.His.1.3-5` | A scaled sequence is specified, but comparison of developments occurring at the same time is not | Require a paired timeline and one explicit comparison of simultaneous developments in different places |
| Unit 2, `D3.1.3-5` | Source selection names origin, kind and date, but not how historical or social context affects usefulness | Add: “Students explain how the source’s setting affects its usefulness for this question” |

The progression already names the first step-up. The C3 source specifies both requirements. [C3 Framework, printed pages 45 and 53](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf)

**Why it matters:** Students could repeat chronological ordering and source-label checking without making the intended Grade 4 advance.

For the timeline, select Coronado from the frame’s existing “de Soto or Coronado” option and compare the overlapping 1541 to 1542 period with Cartier’s third voyage. The dates are supported by the [National Park Service](https://www.nps.gov/coro/learn/historyculture/stories.htm) and [Parks Canada](https://www.parcs.canada.ca/lhn-nhs/qc/cartierbrebeuf/culture/histoire-history/evenement-event/cartier/d). Write the student treatment anew and include the affected Native peoples.

### 5. Regional specialization does not fully specify the owned economic performance

**LAYER:** progression  
**REPEAT:** yes, the same kind as earlier progression finding 1  
**Confidence:** likely

**What is wrong:** Unit 6 and `ss4-regions-resources` explain why regions specialize. Their owned `D2.Eco.4.3-5` concerns specialization and trade by individuals and businesses. Regional output alone does not ensure that explanation. [C3 Framework, printed page 36](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf)

**Why it matters:** Students might associate a resource with a region without explaining the choices of producers.

**Exact fix:** Add:

> Follow one worker and one business in the regional case. Explain why each specializes, what each trades for, and how that exchange helps meet needs.

This is a concrete application of existing scope, not a new economics unit.

### 6. Unit 1’s political-geography vocabulary omits two required terms

**LAYER:** standard  
**REPEAT:** yes, the same completeness problem as earlier progression finding 2  
**Confidence:** firm

**What is wrong:** The frame and `ss4-political-map` list continent, country, state, province and county, but omit **nation** and **city** from `MA.4.T1.2`. [Massachusetts framework, printed page 62](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf)

**Why it matters:** “Nation” is particularly consequential in a course that also teaches Native nations.

**Exact fix:** Add both terms to the frame and progression wording. Use a nested-place example for city and county, and explicitly distinguish a nation from a US state. Keep the existing later placement of detailed US regional mapping.

### 7. The frame still requests an already completed synchronization

**LAYER:** process  
**REPEAT:** yes, the same stale-note kind as finding 9 of `progression-social-studies-2026-11-13.md`  
**Confidence:** firm

**What is wrong:** “For the lead,” item 4, instructs someone to run `frame.py sync`. The current `frames.csv` row already records seven units and 160 days, and the frame gate confirms agreement.

**Why it matters:** The note creates unnecessary work and falsely presents reconciliation as outstanding.

**Exact replacement:**

> **frames.csv.** The Grade 4 row records 7 units and 160 days and agrees with this frame. Re-sync only if either count changes.

### 8. The progression fix record still waits for progressions that now exist

**LAYER:** process  
**REPEAT:** yes, the same stale-note kind as earlier progression finding 9  
**Confidence:** firm

**What is wrong:** Under “Skipped, needs Cory,” `progression-social-studies-fixes-2026-11-13.md` says the cross-subject ownership check “waits on those progressions.” All four progressions now exist, and the cross-subject review and fix record document the subsequent check.

**Why it matters:** The note sends the next reader back to a completed prerequisite while obscuring the remaining within-year timing work.

**Exact replacement:**

> **Codex 6 follow-up completed:** cross-subject ownership and grade timing were checked in the cross-progression review and fix pass. Within-year availability remains for the course frames and calendars to reconcile.

Link that sentence to the cross-progression reports and fix record.

### 9. The source review still presents resolved license decisions as open

**LAYER:** process  
**REPEAT:** yes, the same stale-note kind as earlier progression finding 9  
**Confidence:** firm

**What is wrong:** `social-studies-open-material-2026-11-13.md` still contains conditional instructions asking Cory to accept OGL v3.0 and decide the retired OpenStax AI-clause question. `BASE-TEXTS.md` records both decisions as made on November 13. The source review’s later Oak entry also acknowledges acceptance, leaving the file internally inconsistent.

**Why it matters:** A reader could stop authorized work or reopen settled decisions.

**Exact replacement status note, applied beside each affected conditional recommendation:**

> **Resolved 2026-11-13:** Cory accepted OGL v3.0 and authorized the recorded adaptation use of the retired CC BY editions. Follow `docs/sources/BASE-TEXTS.md`; third-party material still requires its own rights check.

Retain the original research observations as dated evidence.

### 10. The source review still says two loaded collections are awaiting download approval

**LAYER:** process  
**REPEAT:** yes, the same stale-note kind as earlier progression finding 9  
**Confidence:** firm

**What is wrong:** The source review’s follow-up table says Since Time Immemorial and CFPB material are “Ready to load on Cory’s yes.” `BASE-TEXTS.md` and completed `later.csv` item L9 record the loads.

**Why it matters:** These are active next-action statements, not merely historical estimates. They can trigger duplicate work.

**Exact replacement for the Since Time Immemorial status:**

> Loaded 2026-11-13: 17 unit pages and 117 files. The earlier 194-file estimate counted shared files more than once. Grade 4 Washington state units remain excluded.

**Exact replacement for the CFPB status:**

> Loaded 2026-11-13: 134 of 135 activities, 262 PDFs. One activity page is a dead link. See `docs/sources/BASE-TEXTS.md` and later.csv L9.

## Seams and cross-subject availability

The Grade 3 and Grade 5 seams match this frame’s intended progression. Earlier-grade work is generally identified as prior learning or practice, with distinct Grade 4 depth. The return to earlier voyages is explained; it is not an unexplained chronology break.

No same-year math, science or ELA frame was available to verify a shared calendar. The existing documents support the following dispositions:

| Dependency | Disposition |
|---|---|
| Early map measurement | Keep Unit 1’s local measuring routine. The older math scope places measurement conversions late |
| Subtracting years | The math progression owns the skill; counting up provides an adequate local bridge |
| Archaeological layers | Science’s rock-layer unit comes later in its existing sequence. Keep the brief local explanation |
| Energy resources | The science scope places this early, supporting Unit 6 |
| Hazard engineering | Science’s hazard work is late. Social studies must remain runnable from official preparedness sources |
| Research and reporting | ELA owns the named skills, but early availability is unconfirmed. Keep Unit 2’s instruction |
| Firsthand and secondhand accounts | Keep social studies’ own introduction. The ELA progression locates practice in later text sets |

These bridges prevent an unsupported prerequisite from becoming compulsory. They do not establish that another subject teaches every dependency first.

## Base text and source map

**Not applicable.** Grade 4 has no whole-course base text, and no source map exists. That agrees with `BASE-TEXTS.md`. Reference curricula must remain references; the frame does not map their lessons into Curio Class units.

## Course-frame lens checklist

| Checklist line | Mark | Evidence |
|---|---|---|
| Every anchor standard in the course’s topic range has a unit | **Met for placement; missed for full teaching** | All 39 codes are placed; findings 1, 3 and 6 identify narrowed requirements |
| Replaced Grade 3 or Grade 8 own-state content avoids Massachusetts-only treatment | **Not applicable** | This is the national Grade 4 geography and history year |
| Units name check-set additions and their sources | **Met at frame depth** | Every unit names candidates with a state and grade; full comparisons remain unit-plan work |
| Progression, scope and sequence, unit and day checklist lines | **Not applicable to this layer’s final judgment** | Their requirements remain binding at the named later layers |

## Settled by the expert

These are recommendations for the caller to apply. No edits were made.

| Choice | Reason | File touched |
|---|---|---|
| Keep seven units and the current day allocations | No demonstrated pacing defect warrants restructuring | Grade 4 frame |
| Use a Northeast region map and four regional state examples | Restores the required artifact without adding a sixth major mapping task | Frame; social studies progression |
| Select Coronado for the existing Spanish entrada option | Enables a concrete simultaneous-events comparison with Cartier | Grade 4 frame |
| State the archaeological evidence and preservation explanations explicitly | Prevents a migration-only reading of Unit 3 | Frame; relevant progression row |
| Add worker and business examples to regional specialization | Makes the existing economic scope teachable | Frame; social studies progression |
| Add nation and city to political-geography vocabulary | Completes the existing standard | Frame; social studies progression |
| Retain local cross-subject bridges | Shared calendars are not yet verified | Grade 4 frame |

No recommendation moves a standard between units or grades.

## What is right and should remain

- Maps and research precede their later applications.
- Grade 4 prompted sourcing connects coherently to Grade 5 independence.
- Native nations appear as living peoples and governments.
- Conquest, slavery and exclusion are named plainly.
- Harmful simulations and demands for private family disclosures are prohibited.
- The informed action is evidence-based and chosen by students.
- Course-level checks include unfamiliar evidence and scheduled respond days.

## What I could not judge

- A successful full plan gate.
- Final cross-subject calendar alignment.
- Actual source difficulty, rights, accessibility or task timing before selections exist.
- Final historical accuracy and sensitivity of unwritten teaching materials.
- Full check-state comparisons. Tennessee’s standards-review page was blocked during direct retrieval, so I make no claim that its substantive content was audited.

## For Cory

- Confirm the audience assumption of a daily 40-minute social studies block. The shorter route should be designed explicitly when the scope and sequence is written.
- Arrange the required qualified community read of Native and hard-history content before the course is called finished. No outreach or spending was undertaken.

## Outside sources and source-list notes

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): Grade 4 content requirements.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned indicator meanings and depth.
- [AIR and EdReports social studies criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): coherent sequencing, inquiry, usability and assessment principles.
- [Massachusetts Grade 4 course overview](https://www.doe.mass.edu/investigatinghistory/curriculum/g4-course-overview.pdf): limited sequence and pacing comparison.
- [New York K-8 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): checks on the frame’s proposed New York connections.
- [New York Complex Societies inquiry](https://c3teachers.org/wp-content/uploads/2024/04/NewYork_5_Complex_Societies.pdf): limited comparison of source-linked tasks and conclusions, reference only.
- [California content standards](https://www2.cde.ca.gov/cacs/id/web/4184): limited check-state verification.
- [Tennessee standards-review page](https://www.tn.gov/sbe/committees-and-initiatives/standards-review/social-studies.html): direct access blocked.

**For the source list:** Record the working [Investigating History curriculum index](https://www.doe.mass.edu/investigatinghistory/curriculum/) and the June 2026 Grade 4 overview. The older Investigating History route attempted during this read was inaccessible.

**Verdict:** Revise before scope and sequence writing. **Finding count:** 10. **Report path:** `docs/reviews/frame-social-studies-grade-4-2026-11-13.md`, delivered here only.