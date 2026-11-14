# Independent expert cold read: Civics: Government and Civic Life

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-civics-government-and-civic-life-2026-11-13.md`  
**Delivery:** Complete report below. No report file was created.

## Verdict

The frame has a coherent sequence, credible handoffs and a workable year, but it should not guide course writing unchanged. Its biggest risk is apparent completeness: every owned skill and standard code has a unit, while some required content remains unspecified. Complete the requirements within their existing units, implement the accepted tribal-government addition, and correct the review requirements before accepting the frame.

## What I read and checked

I read:

- `docs/agents/EXPERT.md`, the social studies lens, `docs/FOUNDATION.md`, the relevant roadmap sections, and BASELINE rules 20 to 24.
- The shared core and social studies section of `docs/ADOPTION-BAR-SUBJECTS.md`, `docs/courses/social-studies/STANDARD.md`, `docs/APPROACH.md`, and the source registry.
- The complete civics frame, its `frames.csv` row, all 27 grade 8 progression rows, their relevant prerequisites and receiving rows, and the loaded standards.
- The complete preceding frame, World Geography and Ancient Civilizations II, and following frame, World History I.
- Relevant ELA and mathematics progression rows, the base-text record, the glossary, earlier social studies and cross-subject reviews, their fix reports, and the relevant decisions in `DESK-ANSWERS.md`.

Outside checking covered the official Massachusetts and C3 frameworks, California’s government standards, the Educating for American Democracy Roadmap, and the Washington tribal-sovereignty curriculum index. Tennessee and New York searches located official documents, but opening them failed. No curricular finding below rests on model memory.

### Gates

| Command | Observed result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| `python -B -X utf8 scripts/frame.py check civics-government-and-civic-life` | 0 failures |
| `python -B -X utf8 scripts/progression.py check social-studies` | 384 rows, 0 failures, with advisory notes |
| `python -B -X utf8 scripts/stale.py check` | Final run: 19 files, 0 failures |

The full plan gate is **unverified**, rather than passed. I installed nothing and did not bypass its missing dependency. The separate checks support this provisional content review, but the full gate must complete before acceptance.

## Findings, most serious first

### 1. Government standards lose required detail between the official anchor and the frame

**LAYER:** standard  
**REPEAT:** yes, bundled-standard omissions were identified in `progression-social-studies-codex-2026-11-13.md`, finding 2  
**Severity:** substantial  
**Confidence:** firm

The local summary of `MA.8.T3.2` omits the legislative process, named congressional leadership functions, and executive structures specified in the official anchor. Neither the progression notes nor unit 3 restore committees, hearings, legislative procedures, the Cabinet or the armed services. Unit 4 likewise leaves the office terms specified under `8.T3.4` unsecured. See the [Massachusetts framework, PDF pages 106 to 107, printed pages 106 to 107](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf).

**Why it matters:** A writer following the local records could teach checks and balances completely as summarized while omitting how governing institutions actually conduct their work.

**Exact fix:** Expand the existing standards paraphrases and corresponding progression notes. In unit 3, explicitly require students to trace legislation through committees, hearings and votes; explain congressional leadership functions; and distinguish the Cabinet, agencies and armed services. In unit 4, explicitly compare office terms and constitutional term limits. Keep both standards in their existing units and days.

### 2. Unit 7 still specifies only part of two economics indicators

**LAYER:** progression  
**REPEAT:** yes, `progression-social-studies-2026-11-13.md`, finding 1  
**Severity:** substantial  
**Confidence:** firm

`ss8-public-budget` carries `D2.Eco.10.6-8` and `D2.Eco.11.6-8`. Its notes address borrowing costs but do not explicitly address investing. They include employment, growth, inflation and GDP, but leave unemployment and income data unspecified. The earlier repair added inflation and GDP without completing the indicator. See the [C3 Framework, printed page 37](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters:** The course would hand on incomplete economic reasoning while claiming both codes.

**Exact fix:** Add to the progression notes and unit 7:

> Compare how changing interest rates affect borrowing and investing. Use public data on employment, unemployment, inflation, output, income and growth to evaluate the economy and explain consequences for the public budget.

Use a supplied public-data panel and one investment example within the existing 20 days. Check both requirements in the unit’s assessment.

### 3. The accepted tribal-government content remains outside unit 7’s actual specification

**LAYER:** frame  
**REPEAT:** new  
**Severity:** substantial  
**Confidence:** firm

“For the lead,” item 1, correctly identifies the problem. Cory accepted present-day Native nations as governments in grade 8, but unit 7 and `ss8-federal-state-powers` still specify federal and state government without that addition. Listing a possible source in the introduction does not place the learning in the unit.

**Why it matters:** A writer could omit an accepted part of the course. The later Government course expects that foundation.

**Exact fix:** Apply the frame’s proposed addition to `ss8-federal-state-powers` and unit 7: teach a named nation’s present-day government, governing institutions and treaty relationship through one worked example. Distinguish tribal sovereignty from state and municipal government. Replace the pending lead note with the implemented placement.

The [Washington curriculum index](https://ospi.k12.wa.us/student-success/resources-subject-area/time-immemorial-tribal-sovereignty-washington-state/middle-school-curriculum) confirms the named middle-school treaty unit exists; I could not open its individual unit page.

This disagrees with the earlier progression review’s positive summary that grade 8 already secures tribal sovereignty. The current row secures an influence inquiry, which is a different task.

### 4. The frame understates the required sensitivity and qualified-person reads

**LAYER:** frame  
**REPEAT:** yes, the review requirement for tribal material appears in `social-studies-open-material-2026-11-13.md`, trap 4  
**Severity:** substantial process risk  
**Confidence:** firm

Lines 58 to 59 name sensitivity reads for units 1, 2, 6 and 7, and a qualified-person read only for unit 1. The social studies bar requires a sensitivity read for every unit. FOUNDATION section 7 also requires a community reader for Native and hard-history content, which extends beyond unit 1.

**Why it matters:** A production worker could treat the shorter list as the complete review obligation.

**Exact fix:** Rewrite the paragraph to state:

> Every unit receives the fresh-agent sensitivity read. Units 1 and 7 require the qualified community read for Native content; units 2 and 6 require the qualified read for their hard-history content. The unit plans identify the passages and record completion before publication.

Cory supplies the people and any budget. This report does not appoint or contact anyone.

### 5. Two unit questions permit answers that bypass their source investigations

**LAYER:** frame  
**REPEAT:** new among the relevant earlier reads  
**Severity:** moderate  
**Confidence:** likely

Unit 1’s “Where did the ideas behind American government come from?” invites an origins list. Unit 9’s “How can citizens tell what is true in the news?” permits a generic checking checklist. Neither question requires the comparative judgments that the units’ stronger content descriptions promise.

**Why it matters:** Writers may organize recall or general advice around questions intended to sustain inquiry. The [Educating for American Democracy Roadmap](https://www.educatingforamericandemocracy.org/the-roadmap/) illustrates questions grounded in substantive civic and historical dilemmas.

**Exact fix:** Use:

- **Unit 1:** “Which traditions most shaped the founders’ plan, and where does the evidence of influence fall short?”
- **Unit 9:** “Which claims about one public policy issue are best supported, and what does comparing its coverage reveal about a free press?”

Retain the existing content and days. Each unit plan must supply sources supporting more than one defensible conclusion.

### 6. An earlier review still says partial bases are unloaded

**LAYER:** process  
**REPEAT:** yes, stale-status findings appear in `progression-cross-codex-2026-11-13.md`, finding 1  
**Severity:** minor  
**Confidence:** firm

`progression-social-studies-codex-2026-11-13.md:73` says candidate partial bases are “not yet loaded.” `docs/sources/BASE-TEXTS.md` now records all but Oak as loaded.

**Why it matters:** A later worker may repeat completed acquisition work or disregard available material.

**Exact fix:** Replace that status sentence with:

> No whole-course social studies base text is adopted. The partial-base record now lists loaded material, with Oak obtained per unit when needed; this course’s frame maps no base lessons.

Preserve the original review date and add a dated status update.

### 7. Earlier review notes still say the other progressions are absent

**LAYER:** process  
**REPEAT:** yes, the same stale-status category as finding 6  
**Severity:** minor  
**Confidence:** firm

The progression review’s finding 6 and limitations section still describe the other subject progressions as absent. The progression fix report also says ownership checking “waits on those progressions.” Mathematics, ELA and science progressions now exist, and the later cross-subject fix report records ownership and grade checks.

**Why it matters:** These notes confuse completed ownership checking with the genuinely unfinished within-year scheduling check.

**Exact fix:** Update those repeated status statements to:

> The other subject progressions now exist, and cross-subject ownership and grade checking were completed in the cross-subject pass. Within-year availability still requires comparison of the course frames.

Link `progression-cross-fixes-2026-11-13.md`.

### 8. The source review still presents the OpenStax decision as pending

**LAYER:** process  
**REPEAT:** yes, stale-status category  
**Severity:** minor  
**Confidence:** firm

`social-studies-open-material-2026-11-13.md` still directs Cory to decide the AI-clause question, including its opening summary, recommendations and “Open items.” `DESK-ANSWERS.md`, card `q-ss-partial-bases`, records his decision, and BASE-TEXTS incorporates it.

**Why it matters:** A settled repository decision appears to remain an approval requirement.

**Exact fix:** Add a dated resolution and replace the pending instructions:

> Cory accepted use of the retired CC BY editions as partial bases on 2026-11-13. Follow BASE-TEXTS and its item-level restrictions; current NC-SA editions remain reference only.

This records the repository decision without making a new legal determination.

### 9. The source review still presents acceptance of OGL v3.0 as pending

**LAYER:** process  
**REPEAT:** yes, stale-status category  
**Severity:** minor  
**Confidence:** firm

The same review’s Oak entry, trap 5, recommendation and “Open items” still condition use on Cory accepting OGL v3.0. The same decision card records acceptance.

**Why it matters:** It creates another obsolete approval request.

**Exact fix:** Replace the pending condition with:

> Cory accepted OGL v3.0 on 2026-11-13. Use eligible current material under BASE-TEXTS, checking third-party items separately.

Keep genuine unit-selection and rights-checking work open.

### 10. The glossary still labels progression CSVs as planned

**LAYER:** process  
**REPEAT:** yes, stale-status category  
**Severity:** minor  
**Confidence:** firm

`docs/GLOSSARY.md:52` labels `data/progressions/<subject>.csv` “planned,” although the four core progression files exist.

**Exact fix:** Replace “planned” with “current records for the four core subjects.” Preserve the definition and historical mathematics-page pointer.

**Why it matters:** The glossary should direct workers to the existing source of course ownership.

### 11. The glossary still says course frames are not built

**LAYER:** process  
**REPEAT:** yes, stale-status category  
**Severity:** minor  
**Confidence:** firm

`docs/GLOSSARY.md:53` says “Not built; PRODUCTION-PATH step 2.” Multiple frames, including this course and both neighbors, now exist.

**Exact fix:** Replace the status cell with:

> `docs/courses/<course>/frame.md`; totals in `data/plans/frames.csv`; PRODUCTION-PATH step 2. Frames are being written and reviewed.

**Why it matters:** This distinguishes existing drafts from completed reviews without falsely declaring the layer finished.

## Ownership, sequence and days

All **27 grade 8 skills appear exactly once**. No foreign-grade skill is silently claimed as a new owner. Earlier content is explicitly revisited, and the repeated deliberation indicator distinguishes grade 7’s single procedure from grade 8’s comparison of procedures.

The frame places all **50 Massachusetts parent standards**, structurally carrying the six loaded lettered parts, and **26 distinct C3 indicators**. Findings 1 and 2 concern semantic completeness, which those counts cannot establish.

| Unit | Days | Owned skills | Massachusetts parent codes | C3 indicators | Scheduled days |
|---|---:|---:|---:|---:|---|
| 1 | 15 | 3 | 5 | 1 | 1 to 15 |
| 2 | 15 | 3 | 4 | 1 | 16 to 30 |
| 3 | 17 | 3 | 6 | 2 | 31 to 47 |
| 4 | 12 | 2 | 4 | 1 | 52 to 63 |
| 5 | 13 | 3 | 9 | 2 | 64 to 76 |
| 6 | 19 | 3 | 4 | 2 | 77 to 95 |
| 7 | 20 | 4 | 10 | 6 | 100 to 119 |
| 8 | 11 | 2 | 2 | 4 | 120 to 130 |
| 9 | 14 | 3 | 6 | 1 | 131 to 144 |
| 10 | 12 | 1 | 0 | 6 | 149 to 160 |

Checks and respond days occupy **48 to 51, 96 to 99, and 145 to 148**. Thus 148 unit days plus 12 course-level days equals 160, leaving 20 other days in a 180-day calendar.

No unit is demonstrably far over or under its share. Unit 7 is the tightest because four rows include substantial economics; unit 6 reserves nine of nineteen days for research. Their unit plans must allocate assessment and response within those totals. Unit 10’s twelve days are justified by its deliberation, investigation, action and reflection, despite its single progression row.

The order is sound: branches precede court research, rights precede state-rights comparison, and government levers precede policy change and action. The departures from anchor order have explicit reasons.

## Seams and cross-subject checks

The preceding frame supplies the named democracy, republic, sourcing, argument and economics foundations. World History I picks up this course’s inquiry and sourcing in unit 1, interpretation in unit 3, and constitutional ideas and longer argument in unit 10. Those handoffs align.

Earlier mathematics ownership is confirmed for percentages and sampling. Same-year ELA timing is **not verified**: no grade 8 ELA frame was present at the final inventory. The civics dates are requests to the ELA planner, rather than evidence of an agreed calendar.

Before acceptance, reconcile argument and research before day 77, conflicting-viewpoint work before day 131, and discussion preparation before day 149. Where unavailable, specify the complete local bridge. The existing research fallback names only counterclaim modelling and should also name the needed research routine.

There is no adopted whole-course base text and no course source map. Base-lesson completeness and ordering are therefore **not applicable**. No NC or reference-only lesson is mapped.

## Lens checklist

| Course-frame checklist line | Result | Evidence |
|---|---|---|
| Every anchor standard has a unit | **Met structurally; missed in part semantically** | All codes placed; findings 1 and 2 |
| Grade 8 uses “your state,” rather than Massachusetts-only content | **Met** | Unit 7 uses the student’s state, multiple worked examples and state links |
| Check-set additions are named and sourced | **Met provisionally** | Candidate additions identify their check-set member; exact comparison belongs to unit plans |

The broader lens principles are visible in the design: direct content teaching, source-based argument, chronology with reasons, economic reasoning, deliberation and student-chosen action. Findings 3 to 5 identify weaknesses in government coverage, review requirements and inquiry framing.

Unit and day checklist lines are **not applicable to this frame-only judgment**. Actual source difficulty, contextualization, contrasting accounts, modelling, exit tickets and assessment quality require the later artifacts.

## What is right and should be preserved

- The 160-day structure and explicit respond time.
- Retrieval when grade 5 content returns.
- The distinct civic purpose for rereading founding documents.
- Repeated writing from sources and unseen-source assessment commitments.
- Student-chosen action, political neutrality and protection of family privacy.
- Plain treatment of slavery and exclusion, without harmful role play.

## Settled by the expert

| Choice | Decision and reason | File touched by the caller |
|---|---|---|
| Existing unit placement | Keep the current ten units and totals; the order has defensible prerequisites | Course frame |
| Unit 1 question | Use finding 5’s comparative influence question | Course frame |
| Unit 9 question | Use finding 5’s policy-claim question | Course frame |
| Economics completion | Use one public-data panel and an interest-rate investment comparison | Progression and unit 7 |
| Tribal-government placement | Implement the already accepted addition in unit 7 | Progression and course frame |
| Period assumption | Carry 45 minutes into the scope and sequence | Scope and sequence |
| Stale notes | Apply findings 6 to 11 as dated status corrections | Named records |

No proposed repair moves a standard between units or grades.

## For Cory

- Identify the qualified community readers required for the Native and hard-history material, and settle any associated cost before those units publish.

No new scope or audience decision is required. The tribal-government and partial-base decisions are already recorded.

## Sources and limits

- [Massachusetts History and Social Science Framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): grade 8 content requirements and institutional detail.
- [C3 Framework, revised 2017 PDF](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): owned indicators, particularly economics.
- [California standards, Appendix C](https://www.cde.ca.gov/ci/hs/cf/documents/hssappendixc.pdf): checked the Blackstone and Federalist candidate references.
- [Educating for American Democracy Roadmap](https://www.educatingforamericandemocracy.org/the-roadmap/): substantive inquiry framing.
- [Washington middle-school curriculum index](https://ospi.k12.wa.us/student-success/resources-subject-area/time-immemorial-tribal-sovereignty-washington-state/middle-school-curriculum): confirmed the named treaty-unit listing; individual unit access failed.
- [Tennessee standards](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Academic%20Standards%20for%20Social%20Studies%206.24.pdf) and [New York framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-9-12.pdf): official search results only; opening failed, so no complete comparison is claimed.

**For the source list:** Add the successful official framework, Roadmap and curriculum-index routes to `APPROACH-SOURCES.md` where absent. Record the failed routes and reading limits.

Actual classroom timing, excerpt accessibility, completed sensitivity reads and assessment coverage remain unjudged. The full plan gate and same-year ELA calendar also remain unverified.

**Final verdict:** Revise before acceptance. **Findings: 11**, comprising five curriculum or review-design findings and six stale-status findings. **Report path:** `docs/reviews/frame-civics-government-and-civic-life-2026-11-13.md`, delivered here only.

