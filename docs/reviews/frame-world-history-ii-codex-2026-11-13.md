# Independent frame review: World History II

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-world-history-ii-2026-11-13.md`  
**Delivery:** Report supplied here only. No files were changed.

## Verdict

The frame has a sound overall structure, but it needs revision before it guides unit writing. Its biggest risk is apparent completeness: all recorded skills and codes are placed, while the official standards contain requirements missing from the local records or the planned work. Restore those requirements, correct the misleading sequencing instructions, and resolve the partial-base mapping before approving the frame.

## What I read and checked

I read:

- `docs/agents/EXPERT.md`, the social studies lens, FOUNDATION, the relevant ROADMAP sections, BASELINE rules 20 to 24, the shared approach and its source notes.
- The shared core and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`, and `docs/courses/social-studies/STANDARD.md`.
- The complete World History II frame, its `frames.csv` row, all 43 grade 10 progression rows, and relevant prerequisite and receiving rows.
- The World History I and US History I frames, including their handoff tables.
- The local Massachusetts standards and exclusions, with targeted comparison against the official framework.
- The relevant math, ELA and science progression rows. No corresponding ELA 10 or Chemistry frame exists.
- `BASE-TEXTS.md`, the social studies source review, the relevant Desk decisions, and the local partial textbook’s copyright page, contents and sample image credits.
- Earlier social studies progression reviews and fixes, cross-subject reviews and fixes, and the existing kindergarten and grade 1 frame reviews.

### Checks

| Check | Result |
|---|---|
| Requested `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Existing alternate Python launcher | Could not start: permission denied |
| `python -B -X utf8 scripts/frame.py check world-history-ii` | **0 failures** |
| `python -B -X utf8 scripts/progression.py check social-studies` | **384 rows, 0 failures**, with advisory notes |
| `python -B -X utf8 scripts/stale.py check` | **19 files, 0 failures** |

The full plan gate remains unverified. Its environment error is not a curriculum failure. The standalone gates settle recorded placement and arithmetic, not whether the records preserve the standards’ full meaning.

## Findings, most serious first

### 1. The local anchor omits required content

**Severity:** serious  
**LAYER:** standard, progression, frame  
**REPEAT:** yes, incomplete requirements inside claimed standards recur in the earlier progression reads  
**Confidence:** firm

The official framework contains requirements absent from both the local paraphrase and the corresponding progression notes:

| Location | Missing requirement | Exact fix |
|---|---|---|
| `MA.WHII.T3.2`, `wh2-imperialism-causes`, unit 3 | Parts **c and d**: integrated political, religious and economic imperial goals; racial theories and Social Darwinism as justifications | Add own-word records for `MA.WHII.T3.2c` and `d`, assign them to this existing row, and explicitly include both in unit 3. |
| `MA.WHII.T5.5`, `wh2-decolonization`, unit 8 | **Central and South America** in the nationalist-movement survey | Restore those regions to the standard paraphrase and survey. Keep one movement in depth. |
| `MA.WHII.T6.2`, `wh2-middle-east-since-1980`, unit 9 | Youth demographics, Kurdish autonomy, and political challenges in the oil-rich Gulf states | Restore these components to the standard record, progression notes and unit description. |

These are omissions from the adopted anchor, not proposed check-set additions. Evidence: [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), PDF pages 152, 158 and 160, matching printed pages.

**Why it matters:** writers following the repository can omit this content while every structural check passes.

**Fix:** make the linked repairs above without moving ownership between units. Then reconsider units 3, 8 and 9 against the restored workload.

### 2. Several C3 endpoints remain only partly specified

**Severity:** serious  
**LAYER:** progression, frame  
**REPEAT:** yes, C3 code-to-task mismatches were finding 1 of the earlier independent progression read  
**Confidence:** firm on the requirements; likely on the resulting omissions

The repaired progression still leaves the following work unsecured:

| Row and code | Exact repair |
|---|---|
| `wh2-historians-interpretations`, `D2.His.17.9-12` | Require related historical interpretations in **multiple media**, rather than print, film **or** a display. |
| `wh2-industrial-cities`, `D2.Geo.8.9-12` | Evaluate political decisions as well as economic activity, including suburban relationships. |
| `wh2-postwar-world`, `D2.Geo.5.9-12` | Evaluate cultural **and environmental** consequences of decisions over time; border changes alone are insufficient. |
| `wh2-globalization`, `D2.Eco.15.9-12` | Explicitly include economic growth and resource and income distribution. |
| `wh2-global-problems`, `D2.Geo.9.9-12` | Evaluate climate effects on resource use and land use at local-to-global scales. |
| `wh2-research-argument`, `D4.3.9-12` | Adapt arguments **and explanations** across audiences and venues, using print/oral and digital forms. |

Evidence: the official [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf), printed pages 39, 42, 43, 48 and 60.

**Why it matters:** a suitable topic or one successful product does not secure the complete endpoint.

**Fix:** add these explicit performances to the named progression notes and preserve them in the corresponding frame cells. Use small tasks within existing work, not six additional projects.

The earlier fixes to supporting-question interpretation, contemporary methods of change, and explanation critique are present. Those settled findings are not reissued.

### 3. Unit 5 gives a false causal reason for its order

**Severity:** serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

Unit 5 says, “the Depression comes before the dictators because it explains their rise.” That instruction invites a common cause to be applied to all three regimes. Mussolini entered government in 1922 and established his dictatorship before the Depression. The unit’s question also asks why democracy survived somewhere, but its named political cases concentrate on dictatorships. The [Holocaust Museum’s Mussolini account](https://encyclopedia.ushmm.org/content/en/article/benito-mussolini-1) establishes the chronology.

**Why it matters:** writers can build an inaccurate explanation into the very unit intended to teach historical causation.

**Exact fix:** replace the ordering reason with:

> Establish the different routes to authoritarian rule on a dated timeline. Mussolini’s dictatorship and Stalin’s consolidation began before the global Depression; the Depression intensified instability and helped the Nazi rise. Compare these developments with one surviving democracy before evaluating the road to war.

Use Britain as the short comparison alongside the existing government-response work. Keep the 14-day allocation and the existing rows.

### 4. The frame turns one Cold War case into two

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, the earlier progression reads warned against multiplying the “one example” requirements  
**Confidence:** firm

The Days bullet explicitly budgets `wh2-cold-war-europe` and `wh2-cold-war-world` as “one case in depth each.” The progression instead says each student selects **one case from either row**. The official anchor also permits one development, as shown in [WHII.T5.3](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf), printed page 157.

**Why it matters:** unit 7 already has five rows in 15 days. The frame adds a second substantial investigation without acknowledging the change.

**Exact fix:** replace every ambiguous formulation with:

> Each student studies one development in depth, selected across the European and wider-world options together. All students receive the short survey of the remaining developments.

Keep both rows in unit 7. Keep 15 days until the corrected workload is allocated.

### 5. Unit 10’s nine-day justification assumes teaching absent from the earlier units

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** yes, unsupported prerequisite assumptions recur in the progression reviews  
**Confidence:** firm on the inconsistency; judgment call on the allocation

“For the lead” item 2 justifies nine days partly because units 4 and 6 have already taught the Convention’s history. Those units name Armenia, the Holocaust, international institutions and several legal instruments, but neither explicitly places the Genocide Convention. The course brief and unit 10 instead put its first teaching here.

**Why it matters:** a writer may omit the introduction or discover that the nine-day budget depends on prior teaching that never occurred.

**Exact fix:** retain first teaching in unit 10 and replace the justification with an explicit provisional allocation:

| Work | Days |
|---|---:|
| Convention definition and distinction from other mass atrocity | 1 |
| Rwanda anchor investigation | 3 |
| Srebrenica comparison and brief survey | 1 |
| Terrorism and evaluation of a response | 2 |
| End-of-unit assessment using unseen sources | 1 |
| Respond day | 1 |
| **Total** | **9** |

State that earlier units supply historical context, not prior mastery of the definition. If selected sources cannot fit this allocation, bring a documented time change to Cory rather than silently moving terrorism.

### 6. The partial base has a chapter guide, but no auditable source map

**Severity:** moderate  
**LAYER:** base text  
**REPEAT:** new  
**Confidence:** likely

The frame identifies a partial base and assigns chapters 6 to 15 to units. However, `data/plans/world-history-ii/source-map.csv` does not exist. Chapters 11, 14 and 15 serve multiple units, with no section-level division.

The [publisher’s record](https://dc.etsu.edu/etsu-oer/13/) and local contents confirm the chapter sequence. The local copyright page also confirms that third-party images retain separate terms.

**Why it matters:** the present guide cannot establish whether selected material is duplicated, omitted deliberately, or rearranged with a reason. Calling the course “our own” does not make its proposed adaptations traceable.

**Exact fix:** supply the requested source map for the selected partial base. Record source section/page span, destination unit, adapted or omitted status, reason, and rights status. Mark chapters 1 to 5 as belonging principally to the preceding course; distinguish text and original maps from third-party assets.

This does not require adopting every textbook section. If these are only unselected candidates, say that explicitly and identify selection and mapping as unfinished work.

### 7. The qualified-reader list leaves out hard-history content

**Severity:** moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

“For the lead” item 4 lists units 3, 4, 6, 8 and 10. Unit 1 also contains slavery and Indigenous content. Units 5, 7 and 9 include persecution, mass death or civilian suffering.

**Why it matters:** the selective list can become a shipping checklist that excludes material covered by FOUNDATION section 7.3.

**Exact fix:** replace the numbered-unit limitation with:

> A qualified community reader must read the Native and hard-history content wherever it appears before those units ship. The present inventory includes relevant content in units 1, 3, 4, 5, 6, 7, 8, 9 and 10. The fresh-agent sensitivity read remains separately required.

Cory arranges the people. This finding does not require outreach during this review.

### 8 to 16. Stale follow-up notes

These are **minor, firm process findings**. Each is **LAYER process; REPEAT yes**, matching the stale-note findings in earlier progression and frame reviews.

They matter because they can reopen settled decisions, repeat completed research, or conceal the work that actually remains. Preserve original dated observations where useful, but add the following dated resolution or replace the active follow-up.

| # | Location and stale note | Evidence and exact replacement |
|---|---|---|
| **8** | `progression-social-studies-fixes-2026-11-13.md:38`: Government and Economics placement remains reserved | Desk card `q-ss-progression-1` decides it. Replace with: “Resolved 2026-11-13: Government and Economics are open to grades 11 or 12. Grade 12 is the data label; neither course requires prior US History I.” |
| **9** | Same file, line 43: cross-subject verification “waits on those progressions” | All four progressions and the cross-subject fix report exist. Replace with: “The cross-subject progression reads and fixes are complete. Remaining availability checks belong to the course frames and their within-year calendars.” |
| **10** | `social-studies-open-material-2026-11-13.md:175`: OGL and the AI-clause decisions remain open | Desk card `q-ss-partial-bases` resolves both. Replace with: “Resolved 2026-11-13: OGL v3.0 is accepted with item-level exceptions checked; the retired attribution-licensed editions are accepted as partial bases. See BASE-TEXTS.md.” |
| **11** | Same report, line 177: open the history/geography unit lists and a licence footer | Its later addendum records this work. Replace with: “Completed in the later addendum: unit lists and a sample licence footer read. Select and check individual lessons when needed.” |
| **12** | Same report, line 179: retry C3 Teachers and Library of Congress | Both are described as loaded in the later addendum. Replace with: “Access recovered in the later addendum. Retain its separate reuse limits and item-level rights checks.” |
| **13** | Same report, line 180: check LibreTexts and Louisiana alongside still-unread organizations | The addendum checks the first two. Replace with: “LibreTexts K12 and Louisiana checked and retained as reference only. Facing History and the Bill of Rights Institute remain unread; consult when a unit needs them.” |
| **14** | Same report, line 225: Since Time Immemorial is “Ready to load on Cory’s yes” | BASE-TEXTS.md and the local manifest establish loading. Replace with: “Loaded 2026-11-13; inventory and locations are in BASE-TEXTS.md and the source manifest. Cultural and item-level rights checks remain.” |
| **15** | Same report, line 226: financial-education activities are “Ready to load on Cory’s yes” | BASE-TEXTS.md and the local manifest establish loading. Replace with: “Loaded 2026-11-13: 134 of 135 activities, with the unavailable activity recorded. See BASE-TEXTS.md and the manifest.” |
| **16** | `docs/ROADMAP.md:95`: social studies waits on an undecided content standard | STANDARD.md, the loaded anchor and subsequent progression work contradict this status. Replace with: “The social studies standard is decided: C3 skills, Massachusetts 2018 content, the named check set and the values rule. Progressions are written and read; course frames are under review.” |

The stale checker does not scan most of these review files by default. Its zero does not settle these findings.

## Coverage, order and days

The gate correctly establishes **43 owned rows placed once**. The recorded ownership contains **50 Massachusetts parent standards** and **25 distinct C3 indicators**. Findings 1 and 2 explain why that inventory is not yet complete semantic coverage.

| Unit | Rows | Days | Workload judgment |
|---|---:|---:|---|
| 1. States, rights and revolutions | 5 | 16 | Reasonable, with England explicitly recalled. Its Latin American thread extends beyond the title’s 1830 endpoint. |
| 2. Industrial Revolution | 3 | 12 | Reasonable for causes, consequences and reform. |
| 3. Nations and empires | 4 | 14 | Recheck after restoring the missing imperialism requirements. |
| 4. First World War and peace | 5 | 16 | Heavy, but interpretation work can use the same peace-settlement evidence. |
| 5. Interwar years | 4 | 14 | Reasonable after correcting the causal sequence and using a concise survival comparison. |
| 6. Second World War and Holocaust | 4 | 16 | Defensible, with one battle in depth and careful source selection. |
| 7. Cold War | 5 | 15 | Defensible for one in-depth development across both case rows. |
| 8. Independence and rights | 4 | 13 | Tight: decolonization, apartheid, eight Israel/Palestine components and social movements. Restore the regional survey before accepting the allocation. |
| 9. Connected world | 5 | 12 | Tightest content survey. Restored Middle East and C3 work needs an explicit allocation before approval. |
| 10. Genocide, atrocity and terror | 2 | 9 | Conditionally workable using finding 5’s bounded allocation. |
| 11. Global problems and research | 2 | 13 | Defensible if research habits recur earlier and the capstone uses a bounded source search. |
| **Units** | **43** | **150** | |
| **Course checks and respond days** | | **10** | Three checkpoints, each including response. |
| **Course total** | | **160** | Fits the repository’s full-year yardstick. |

No unit is demonstrably far overallocated. Row counts alone do not prove that units 8 and 9 are feasible. Their restored requirements should be budgeted before adding days to the course.

The broad sequence holds: revolutions, industry, empire, world wars, Cold War, independence, globalization and current problems. The thematic return after 1945 has a stated reason. No new model is assumed before an earlier grade teaches it.

## Seams and cross-subject checks

**Seams are substantially sound.** World History I’s Enlightenment, constitutional, Atlantic, industrial-preparation and interpretation threads are picked up. US History I’s receiving table matches the World History II handoffs, including the distinction between a historical-content return and the transferable cause-analysis skill.

England’s constitutional history is explicitly review. Existing later-course economic returns deepen earlier work rather than claiming it is new.

**Cross-subject ownership is identifiable, but same-year scheduling remains unverified.** The named ELA and science rows exist. Earlier math and science references precede grade 10, and the nuclear-science bridge is explicit.

The frame records useful proposed deadlines and avoids inventing the other courses’ unit numbers. However, no ELA 10 or Chemistry frame currently establishes that those deadlines will be met. Before approval, reconcile:

- Interpretation and argument teaching before the dependent history work.
- The proposed shared research project in weeks 29 to 32.
- Presentation preparation before its use.
- The hard-content and substantial-writing calendar.

This is an outstanding cross-frame check, not evidence that those courses already teach the skills first.

## Lens checklist: course frame layer

| Checklist line | Result |
|---|---|
| Every anchor requirement in the course’s Massachusetts range has a unit | **Missed.** Recorded parent codes are placed, but finding 1 identifies omitted requirements. |
| The replaced grade 3 year or grade 8 own-state treatment avoids Massachusetts-only content | **Not applicable.** This is grade 10 world history. |
| Units name check-set additions and record their source | **Met provisionally at frame depth.** Every unit names candidates and their origin. The frame openly says these were proposed from knowledge; the unit comparison tables must verify them against named editions. |

## What is right and should not be undone

- Explicit inquiry questions and a growing research and argument arc.
- Primary sources alongside interpretations, with source difficulty and rights requirements.
- Rwanda as the decided anchor, Srebrenica as the comparison, and supported alternatives.
- Present-day communities, human lives, resistance and agency alongside hard history.
- Prohibitions on harmful simulations and demands for students to disclose family experiences.
- Complete solo-student survey routes.
- Unseen-source course checks and protected respond days.

The source care, contextualization and simulation prohibitions are consistent with the [Holocaust Museum’s teaching guidance](https://www.ushmm.org/teach/fundamentals/guidelines-for-teaching-the-holocaust).

## Settled by the expert

These are recommendations for the caller to apply. No edits were made.

| Choice | Reason | File it touches |
|---|---|---|
| One Cold War development in depth across both case rows | Preserves the existing progression contract | World History II frame |
| Keep the Convention introduction in unit 10 and budget it explicitly | Removes the unsupported prerequisite assumption | Same frame |
| Use Britain as unit 5’s concise surviving-democracy comparison | Answers the unit question within its existing scope | Same frame |
| Compare a written interpretation with a captioned documentary segment or display | Makes the existing interpretation task cover multiple media | Frame and `wh2-historians-interpretations` notes |
| Keep the 160-day working budget during repair | The present evidence does not establish a need for 165 days | Frame and subsequent scope and sequence |
| Describe unit 1’s later Latin American material as a thematic continuation through the 19th century | Makes the chronological exception explicit | Frame title/ordering explanation for unit 1 |

## For Cory

- **People:** arrange the qualified community reads required by finding 7.
- **Time and scope:** retain 160 days provisionally. Decide any proposed increase only after units 3, 8 and 9 have allocations that include the restored requirements.

No money, outreach or new audience decision was undertaken.

## Limits, sources and source-list additions

I could not establish a successful full plan gate, confirm the absent cross-subject calendars, or judge final source difficulty, assessment quality and classroom minutes. This is a frame review, not certification of unwritten units.

Outside sources checked:

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): official World History II requirements.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned indicator endpoints.
- [California content standards](https://www.cde.ca.gov/BE/ST/SS/documents/histsocscistnd.pdf): targeted confirmation of the Vienna and industrialization comparisons.
- [College-level world history framework, effective fall 2026](https://apcentral.collegeboard.org/media/pdf/ap-world-history-modern-course-and-exam-description.pdf): targeted check of the migration candidate, not a full comparison.
- [Partial textbook publisher record](https://dc.etsu.edu/etsu-oer/13/): licence and publication record; local PDF inspected for contents and exceptions.
- [Mussolini historical account](https://encyclopedia.ushmm.org/content/en/article/benito-mussolini-1): chronology underlying finding 3.
- [Holocaust teaching guidance](https://www.ushmm.org/teach/fundamentals/guidelines-for-teaching-the-holocaust): responsible source use and methods.

The [New York framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-9-12.pdf) timed out, the [Tennessee review page](https://www.tn.gov/sbe/committees-and-initiatives/standards-review/social-studies.html) returned 403, and the textbook’s online download returned 403. Its existing local PDF supplied the limited checks described above.

No substantive finding rests solely on memory. The frame’s unverified check-set candidates remain knowledge-based proposals. Workload judgments and the proposed allocations are professional judgments, not measured classroom results.

**For the source list:** add the current college-level framework edition and the Mussolini chronology source, recording the limited uses above.

**Verdict:** revise before unit writing. **Finding count:** 16. **Intended report path:** `docs/reviews/frame-world-history-ii-2026-11-13.md`, delivered here only.