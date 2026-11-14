# Independent expert read: social studies kindergarten course frame

**Date:** 2026-11-13  
**Intended report path:** `docs/reviews/frame-social-studies-kindergarten-2026-11-13.md`  
**Delivery:** Complete report below. No file written.

## Verdict

The six-unit structure is coherent, with all 19 kindergarten progression skills placed once and their grade 1 handoffs preserved. Revise before approving the frame: the largest risk is that compressed standards language permits incomplete teaching, alongside weaknesses in the final assessment and the evidence expected for one inquiry question. Restore the missing standard requirements first, then make the assessment, calendar and source corrections below.

## What I read and checked

Read the expert instructions, social studies lens, FOUNDATION, relevant ROADMAP and BASELINE provisions, shared approach, approach-source evidence notes, glossary, social studies adoption bar and STANDARD page. No social studies approach page exists yet.

Read the kindergarten frame in full, its `frames.csv` row, all kindergarten progression rows, the grade 1 frame and receiving progression rows, the local Massachusetts standards and C3 indicator inventory, the base-text record, and relevant earlier social studies and cross-subject reviews and fix reports. Consulted earlier scope and sequence reviews to classify repeated findings.

Outside reading covered the official Massachusetts kindergarten standards and clarifications, relevant C3 indicators, California and New York kindergarten requirements, the Tennessee 2024 kindergarten crosswalk, the social studies materials criteria, two published kindergarten inquiries and a district course overview. Links and reading limits appear below.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Could not complete: `ModuleNotFoundError: No module named 'markdown'` |
| Course-specific `plan.py check social-studies-kindergarten` | 0 failures; 0 items checked |
| `frame.py check social-studies-kindergarten` | 0 failures |
| `progression.py check social-studies` | 384 rows, 0 failures; informational notes remain |
| `stale.py check` | 11 files, 0 failures |
| Independent placement and seam check | All 19 skills placed once; every kindergarten handoff reciprocated |

The global gate’s environment error is not evidence of a plan defect. It also cannot be reported as a successful global gate. No package installation, synchronization, defect logging or repository mutation was attempted.

## Findings

### 1. The full anchor requires time language and map exposure absent from the planning record

**Severity:** Major  
**LAYER:** standard  
**REPEAT:** yes, incomplete requirements inside claimed standards recur in `progression-social-studies-codex-2026-11-13.md`, finding 2  
**Confidence:** Firm on the source requirements; likely on the resulting teaching omission

**What is wrong.** The frame promises every part of `MA.K.T3.3`, but unit 4 and `ssk-sequence-time` omit morning, afternoon, night, and last or next week, month and year. The local paraphrase of `MA.K.T3.3b` omits them too. Unit 3 also omits the `K.T2.2` clarification’s initial exposure to differently designed maps and their purposes. These appear in the [official framework, printed pages 34 to 35](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=34).

**Why it matters.** A writer following these records can satisfy every listed code while teaching a narrower standard.

**Exact fix.**

- Restore the omitted time expressions in the local standard paraphrase, progression row and unit 4 description. Include sequencing from an informational read-aloud as well as personal experience, nature and stories.
- In unit 3, specify a brief comparison of two differently designed world maps and a globe, with teacher-led talk about what each helps someone see. Keep this as introductory exposure. Grade 2 retains formal work on projections.
- Keep the current unit ownership and day totals.

This is a new instance of the earlier defect type. The previously repaired national-symbol requirements remain intact.

### 2. Unit 4 asks students to rank whole eras using evidence about selected objects

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, question and source alignment was also a concern in `ela-6-spine-2026-11-11.md`, finding 4  
**Confidence:** Likely

**What is wrong.** “Was life better long ago, or is it better today?” exceeds what comparisons of washboards, school materials and transport can establish. The teacher note’s suggestion that earlier life was “slower” does not supply evidence about whose life, which place or which period.

**Why it matters.** Children can learn to turn a few technological comparisons into a judgment about an entire era. The required conclusion should stay within the evidence examined, consistent with the [materials criteria’s emphasis on source-based reasoning](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf).

**Exact fix.** Replace the question with:

> Which changes mattered most in the daily work we studied?

Require children to choose a change, point to evidence from a named photograph or object, explain their reason, and identify something that stayed the same. Keep the seven days and both owned skills.

### 3. The final course check omits earlier inquiry and geography, and has no response time

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, assessment scheduling and ending with a response recur in `ela-6-spine-2026-11-11.md`, finding 3  
**Confidence:** Firm

**What is wrong.** The final check samples units 4 to 6 through ordering, sorting and holiday recall. It does not revisit the map work or spoken claim and reason developed earlier. Both respond days follow the mid-year check, so the course ends with assessment and handoff alone.

**Why it matters.** The final record provides weak evidence about two important grade 1 prerequisites. ROADMAP’s assessment rule also requires a response after cumulative checks.

**Exact fix.**

- Keep four course assessment days and two respond days.
- Place one respond day after each course check.
- Add a representative unfamiliar picture-map task and a source-based spoken claim with a reason to the final check.
- State that the final response addresses the observed gaps before the record goes to grade 1.

The total remains **58 unit days + 4 assessment days + 2 respond days = 64**.

### 4. Unit 3 attributes its proposed addition to the wrong grades

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**What is wrong.** Its check-set cell says California and New York kindergarten both widen map work to the country, supporting placement of the child’s state on a United States map. California’s explicit community, state and country location requirement is **grade 1, 1.2.1**. New York’s kindergarten `K.6` emphasizes representations and familiar community locations. See the [California standards, printed pages 4 to 5](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf#page=10) and [New York framework, printed pages 17 to 18](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf).

**Why it matters.** The attribution makes an extension look like a verified kindergarten requirement.

**Exact fix.** Replace that cell with:

> California K.4.3 reinforces interpreting map symbols; New York K.6 reinforces familiar-place location. Briefly locating the student’s state on a United States map is a Curio Class extension connecting the address’s state and country, informed by California grade 1, 1.2.1. Confirm the comparison in the unit plan.

Retain the existing activity and eleven-day allocation. Do not claim ownership of the grade 1 standard.

### 5. The holiday-unit rationale is unsupported by the stated pace

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm on lesson positions; likely on calendar fit

**What is wrong.** Under the current allocation, unit 4 occupies course lessons 35 to 41 and unit 5 lessons 42 to 52. At two lessons a week, unit 5 begins in teaching week 21. The claim that both Martin Luther King Jr. Day and Presidents’ Day fall inside it is therefore not secured. The cross-subject table gives earlier approximate first-use weeks. Two lessons of 20 to 30 minutes also yield **40 to 60**, rather than 50 to 60, minutes weekly.

**Why it matters.** A writer could organize instruction around a holiday coincidence the actual calendar does not provide.

**Exact fix.** Base unit 5’s position on its timeline and perspective prerequisites. State that holidays are named when they occur and investigated retrospectively or prospectively in unit 5. Recalculate first-use weeks after finding 3’s response-day adjustment, and correct the weekly minutes. Leave exact dates to the scope and sequence.

### 6. The frame’s synchronization warning is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale pointers recur in `progression-social-studies-2026-11-13.md`, finding 9  
**Confidence:** Firm

**What is wrong.** “For the lead,” item 2 says the frame gate reports disagreement with `frames.csv`. The CSV now records six units and 64 days, and the frame gate passes.

**Why it matters.** It directs the next worker to resolve an inconsistency that no longer exists.

**Exact fix.** Replace the item with:

> `data/plans/frames.csv` agrees with this frame: 6 units, 64 days. The frame gate passed on 2026-11-13.

### 7. The glossary still labels course frames “Not built”

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same stale-status type as finding 6  
**Confidence:** Firm

**What is wrong.** The course-frame row in `docs/GLOSSARY.md:53` says “Not built,” although this frame and several neighboring frames exist.

**Why it matters.** The glossary gives a false implementation status for the artifact being reviewed.

**Exact fix.** Replace its status cell with:

> `docs/courses/<slug>/frame.md`; counts in `data/plans/frames.csv`; PRODUCTION-PATH step 2.

### 8. The progression fix report still defers an ownership check that now exists

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the same stale-status type as finding 6  
**Confidence:** Firm

**What is wrong.** `progression-social-studies-fixes-2026-11-13.md:43` says checking cross-subject ownership “waits on those progressions.” The other progressions exist. The later cross-subject fix report documents ownership and grade checking, and the current social studies progression gate passes.

**Why it matters.** It leaves a completed dependency presented as pending, while obscuring the remaining task of checking within-year timing.

**Exact fix.** Replace the bullet with:

> Deferred in this pass; subsequently addressed by the cross-subject progression pass and ownership/grade gate. Within-year availability remains for the course frames.

Preserve the link to `progression-cross-fixes-2026-11-13.md`.

## Coverage, units, days and seams

| Unit | Days | Owned skills | Judgment |
|---|---:|---:|---|
| Learning together | 10 | 4 | Appropriate foundation for later discussion and claims |
| Doing our part | 9 | 3 | Sound move from rules to responsibility and collective decisions |
| Where things are | 11 | 4 | Reasonable allowance for language, maps, models and address work |
| Long ago and today | 7 | 2 | Reasonable; repair the standard detail and question |
| Days we remember | 11 | 3 | Justified by its substantial content and sensitive material |
| Work and trade | 10 | 3 | Reasonable for work, scarcity, exchange and the class store |

No unit is demonstrably far over or under its share. Equal days per progression row would be inappropriate.

All **16 Massachusetts parent standards and 17 distinct C3 indicators** attached to the kindergarten rows are placed. Finding 1 concerns depth despite that complete placement. I found no other clear partial-standard omission at this layer.

Kindergarten correctly assumes no earlier Curio Class course. All 19 outgoing skill relationships are answered in grade 1, and the five models have receiving work there. No prerequisite model is clearly used before its introduction.

There is no base text, so a missing `source-map.csv` is appropriate. No reference-only curriculum is mapped as adaptable material.

All eight cross-subject leans resolve to kindergarten work in the other progressions. The local bridges avoid an immediate dependency failure. Kindergarten ELA and mathematics frames do not yet exist, so their teaching order cannot be confirmed.

## Course-frame lens checklist

| Lens line | Status | Evidence |
|---|---|---|
| Every anchor standard in the topic range has a unit | Met for placement; missed for full depth | Finding 1 |
| Replaced grade 3 or grade 8 own-state content is handled correctly | Not applicable | Kindergarten uses the stated own-state address method |
| Units identify check-set additions and their sources | Missed | Every unit has a cell, but unit 3’s attribution is incorrect, finding 4 |

The wider lens expectations are well represented through oral claims, recurring questions, disciplinary models, student-selected classroom action and sensitive-content notes. Source-bounded inquiry needs the repair in finding 2. Detailed source selection, supporting questions and assessment items belong to the later unit layer.

## Settled by the expert

These are recommendations for the caller to apply; no edits were made.

| Choice | Reason | File affected |
|---|---|---|
| Restore the omitted time language and introductory map comparison | Completes already claimed standards | Standards record, progression CSV, kindergarten frame |
| Use the revised unit 4 question and evidence requirement | Keeps conclusions within the studied evidence | Kindergarten frame |
| Allocate one respond day after each course check | Preserves 64 days and provides a final instructional response | Kindergarten frame |
| Make the final check sample earlier map and claim work | Strengthens the cumulative record | Kindergarten frame |
| Label state-on-country-map work as an extension with the correct source | Preserves the activity with an honest attribution | Kindergarten frame |
| Use prerequisite-based holiday placement and corrected pacing language | Removes an unsupported calendar promise | Kindergarten frame |
| Apply the three status rewrites above | Makes current handoff information accurate | Named process files |

## What is right and should remain

Preserve the familiar-classroom starting point, oral and picture-based access, explicit model introductions and reciprocal grade 1 seams. Keep the protections against compulsory family disclosure, the inclusion of unpaid work, student choice in classroom action, and the Native and hard-history review flags.

The early routines fit the kind of bounded classroom inquiry illustrated in the published [Rules inquiry](https://c3teachers.org/inquiries/rules/). The class-store work also has a sound connection to the picture-based scarcity reasoning illustrated in [Needs and Wants](https://c3teachers.org/inquiries/needs-and-wants/). These were comparisons of inquiry structure, not sources to copy.

## What I could not judge

- A successful global plan gate.
- Actual assessment throughput for a class of thirty. Two short assessment periods need a tested administration plan.
- The other kindergarten subjects’ within-year availability.
- Reading difficulty, rights and historical accuracy of sources not yet selected.
- Finished unit assessments, home routes or daily teaching feasibility.

No substantive finding rests solely on memory. Age suitability and the proposed question repair include professional judgment. No classroom trial or effect claim is made.

## Sources and source-list additions

- [Massachusetts 2018 framework](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): kindergarten requirements and clarifications, printed pages 32 to 35.
- [C3 Framework](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): relevant kindergarten-to-grade-2 indicators and inquiry structure.
- [California standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): kindergarten requirements and the grade 1 location requirement.
- [New York framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): kindergarten content, practices and map expectations.
- [Tennessee 2024 crosswalk](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Social%20Studies%20Standards%20Crosswalk%206.24.pdf): kindergarten comparison candidates; not a requirement to import every difference.
- [Social studies materials criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): coherence, evidence-based reasoning and feasible pacing.
- [Rules](https://c3teachers.org/inquiries/rules/) and [Needs and Wants](https://c3teachers.org/inquiries/needs-and-wants/): published inquiry-plan comparisons; embedded source collections were not audited.
- [District kindergarten overview](https://sites.google.com/schools.nyc.gov/social-studies-and-civics/resources-by-grade/elementary/kindergarten): course organization only; linked guides were not reviewed.

**For the source list:** Record these reachable social studies standards, criteria and inquiry examples in `APPROACH-SOURCES.md`, retaining the reading limits above. Their availability does not establish permission to adapt their materials.

## For Cory

- Confirm the proposed course scope of **64 periods across 32 teaching weeks**, at two periods of 20 to 30 minutes weekly.
- Arrange the required qualified community read before Native and hard-history material goes live. No contact or expenditure was undertaken.

**Verdict:** Revise before approval. **Finding count:** 8. **Report path:** `docs/reviews/frame-social-studies-kindergarten-2026-11-13.md`, delivered here only.