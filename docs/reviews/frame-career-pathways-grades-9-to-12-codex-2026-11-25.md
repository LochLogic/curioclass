# Second-model frame review: Career Pathways, grades 9 to 12

Date: 2026-11-25  
Course: `career-pathways-grades-9-to-12`  
Subject: career education, progression code `cte`  
Read-only review. I made no file changes.

## Verdict

The six-unit structure is sound: all 143 selected progression rows are placed once, owned codes match their units, and the grade 8 handoffs are reciprocal. The frame needs a fix pass before the scope and sequence copies its assessment and scheduling rules: one learner-goal task misses its required action, the paper lateral-reading task lacks its supporting sources, and several schedules do not account for their promised time. Preserve the private plan, broad-to-narrow progression, varied routes and required practice evidence while making those repairs.

**Findings: 12, comprising four serious, five moderate and three minor.**

## What was read

- `frame-read.md`, the applicable requirements in `frame-write.md`, EXPERT, FOUNDATION, production-path guidance, shared APPROACH and BASELINE rules.
- ADOPTION-BAR-SUBJECTS, its shared criteria, career education part and pre-work status row.
- Career education STANDARD, APPROACH, lens and relevant decisions.
- The [course frame](S:/CurioClass/docs/courses/career-pathways-grades-9-to-12/frame.md), its course-list selector, frames row and calendar rows.
- All 143 selected grade 10 progression rows, their task requirements and grade 8 handoffs; the local standards files and learner-goal paraphrases; `cte-edges.md`.
- Career Exploration’s frame, relevant pre-work and progression reviews, both Exploration frame reads and their fix report, and the earlier Pathways review.
- Relevant Units tables and calendar placements for ELA grades 9 and 10, Algebra I, grade 8 Civics, computer science grades 9 and 10, library grades 9 to 12 and SEL grades 9 to 12.
- Relevant parsing code and the outside sources linked below.

This is one year offered within a grade range. STANDARD explicitly settles that shape, so the multi-year band requirement for a Year column and separate annual assessment cycles does not apply.

## Checks

| Check | Result |
|---|---|
| `python -B -X utf8 scripts/plan.py check career-pathways-grades-9-to-12` | One failure: lesson-plan CSVs are absent. Continued the frame review as instructed. |
| `python -B -X utf8 scripts/frame.py check career-pathways-grades-9-to-12` | Passed, zero failures. |
| `python -B -X utf8 scripts/stale.py check` | Passed, 121 files, zero failures. Unmarked stale statements remain below. |
| Independent row comparison | All 143 selected rows placed once, with no extras. |
| Independent code comparison | All 122 owned codes match their units; 106 carried codes identified separately. |
| Independent seam comparison | Every incoming grade 8 link is reciprocal. |
| Calendar comparison | Six units total 92 days; four course-level check and respond days bring the total to 96. |

The full gate wrapper was not run because it writes output files; the requested checking commands above ran without writing files.

## Findings, most serious first

### 1. Unit 3 substitutes identifying a stereotyped ad for CD2.A7’s required example

**Severity:** Serious. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, incomplete standard coverage is a recurring review finding.

**Location:** Units table, Unit 3, “What students learn.”

The frame assigns CD2.A7 to finding stereotypes in an invented recruiting ad and rewriting it. Both `ncdg-2024-words.txt` and `g10-cd2-stereotype-check` require an example of a time a stereotype narrowed a career choice. Rewriting an ad does not establish that the student recognizes that effect on a decision.

**Exact fix:** Retain the recruiting task, but precede it with:

> From a public worker profile or an invented worker case, identify a specific choice narrowed by a stereotype. Name the stereotype, the option it closed and the evidence that shows its effect. A personal example is optional.

Record this short piece as CD2.A7 evidence. Keep the next-choice plan as CD2.R7 evidence.

### 2. The paper lateral-reading task lacks the sources needed to perform it

**Severity:** Serious. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier Pathways finding S1 remains unresolved.

**Location:** Unit 6; Models carried; Cross-subject, library row.

Unit 6 supplies three invented sources, but the bridge instructs students to open another tab, investigate the source’s owner and compare other coverage. Paper students cannot open tabs, and invented organizations have no independently discoverable web history. The materials list supplies the claims without the corroborating evidence needed to judge them.

**Exact fix:** Add a paper investigation packet for each invented source: an owner/about page, an original evidence page or table, and two independent accounts with meaningful agreement or disagreement. Explicitly model leaving the original source, comparing these documents and returning to rate accuracy, fairness, date and completeness. Replace the browser-only instruction with this paper routine; retain a browser demonstration where available.

### 3. Downstream readers still break or discard the cluster codes

**Severity:** Serious. **Confidence:** Firm, reproduced.  
**LAYER:** process. **REPEAT:** yes, earlier Pathways finding M5 is partly resolved.

**Location:** For the lead, item 2; `scripts/course_pages.py`, `codes()`; standard-code uses of `split_list()` in `scripts/unit_skeleton.py`.

`frame.py` now uses a semicolon-only standard-code splitter. Its former comma problem is fixed. The other readers remain defective:

- No complete owned sub-cluster code survives `course_pages.codes()` intact. Of 58 codes, 52 return nothing; six return fragments such as `Analytics` or `Entertainment`.
- The unit skeleton still splits standard codes at commas.
- The frame retains six carried `~` codes in Owned standards as an obsolete workaround.

These readers can publish missing standards or seed incorrect skeletons despite the passing frame check.

**Exact fix:** Use a dedicated semicolon-only standard-code parser in both downstream readers. Preserve spaces, commas, ampersands and parentheses that belong to codes; exclude carried codes from owned lists before removing any marker. Then remove the six `~` entries from Unit 2’s Owned standards cell.

Verify that all 58 owned sub-cluster codes survive intact, no fragments appear, and carried codes remain separate. Rewrite For the lead item 2 to distinguish the completed frame-check repair from the remaining downstream work.

### 4. The shorter schedule contains unnamed or duplicated sessions

**Severity:** Serious. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier Pathways M2 and M3 and the Exploration pacing findings.

**Location:** “Shorter path, unit by unit,” Units 1, 4 and 5.

The allocations total 64, but their session descriptions do not form an executable schedule.

**Exact fixes:**

| Unit | Problem | Replacement |
|---|---|---|
| 1 | Sessions 5 to 8 name only three closing days. The plan day also reteaches Unit 2 readiness before the readiness check on the later respond day. | Session 2: values and learner moments. Session 3: study log and school-plan review. Session 4: sorts. Session 5: field task. Sessions 6, 7, 8: plan, assessment, respond. Give the Unit 2 readiness check on the respond day and its targeted reteach when Unit 2 opens. |
| 4 | The plan day appears twice, leaving one of eight sessions unnamed. | Sessions 1 to 3: opening/comparison, job study, routes and school-readiness work. Session 4: full-plan draft. Session 5: trade-offs and fallback. Session 6: feedback and plan revision. Session 7: assessment. Session 8: respond. |
| 5 | The fold list removes separate hook and carry-over days that the 13-session full schedule does not contain. | Replace the five folds with: second resume day; outside-class-learning day into short session 3; second workplace day; self-employment day into short session 2; second interview day. State that the hook opens the first resume day. |

### 5. The shared-device turns require 75 minutes

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier Pathways M1.

**Location:** Devices; Unit 4; shorter-path Unit 4 session 1.

Fifteen pairs taking five minutes each require 75 minutes. The shorter schedule puts these turns alongside the hook, comparison and job choice in one 45-minute session.

**Exact fix:** Spread the turns across Unit 4’s first three sessions on both schedules, with five pairs scheduled each day. Each pair completes its paper table first, then enters the data, makes the chart and names the privacy step at the device. State this rotation in Devices and both Unit 4 schedules.

### 6. Individual checks consume all available teacher time

**Severity:** Moderate. **Confidence:** Firm for interviews and check-ins; likely for panel transitions.  
**LAYER:** frame. **REPEAT:** yes, earlier Pathways M4.

**Location:** Running it with one teacher; Units 5 and 6.

Thirty 90-second interviews or check-ins fill 45 minutes before transitions or collecting work. Ten four-minute panels leave five minutes for every other action, but the frame gives no transition allowance.

**Exact fix:**

- Split each packet check-in round across half the class on days 2/3, 5/6 and 7/8.
- For the interview assessment, specify a 70-second response and follow-up plus a ten-second changeover per student: 40 minutes, leaving five for opening and collection.
- Give each panel a four-minute slot comprising 3½ minutes of presentation/questions and ½ minute of changeover. Reserve the remaining five minutes for opening and collection.

Keep the written feedback and respond-day revisions.

### 7. The early-departing senior calendar does not recover six sessions

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier Pathways m5.

**Location:** Grade 12 calendar.

The panel days are course days 91 to 93, school days 152, 154 and 155, all in week 31. Losing weeks 31 and 32 removes six sessions. Unit 6’s published shorter path saves five, and moving its closing days into two work sessions does not recover six.

**Exact fix:** Remove the unsupported six-session folding instruction. State:

> A senior section ending after week 30 may use the published 64-session path spread over 30 weeks, with its final check on school day 148 and respond day on school day 150. A school retaining the 96-session path must schedule the six otherwise lost meetings before departure.

Retain an actual respond session. Correct the panel timing to week 31.

### 8. The pay-gap unit names no earnings source or earnings-reading task

**Severity:** Moderate. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, the Exploration review also identified insufficiently specified data anchors.

**Location:** Unit 3, teaching sequence and sources.

STANDARD section 6 and the progression require dated pay and job gaps by sex and race. Unit 3 names an employment-composition table and teaches who holds jobs, regional wages and projections, but no earnings-gap comparison. The named [BLS Table 11](https://www.bls.gov/cps/cpsaat11.htm) contains employment counts and demographic shares, not earnings.

**Exact fix:** Add a short comparison to the existing two-day who-holds sequence using [BLS Table 37](https://www.bls.gov/cps/cpsaat37.htm), which supplies median weekly earnings by sex and race/ethnicity. Label the population, year, national geography and 2025 eleven-month limitation. Ask for one supported comparison and one limit on interpretation. State that these group medians do not establish an individual’s pay or equal-work pay differences.

Keep Table 11 for representation. Use [Table 39](https://www.bls.gov/cps/cpsaat39.htm) only where an occupation-by-sex earnings comparison is appropriate.

### 9. Free cluster choice can make the required team composition impossible

**Severity:** Moderate. **Confidence:** Firm, counterexample.  
**LAYER:** progression. **REPEAT:** new.

**Location:** Unit 6 and `g10-prac-4-teamwork`.

The frame guarantees personal cluster and job choice, then requires teams whose members’ clusters and jobs differ. An allowed class in which every student chooses the same own cluster and job cannot meet that requirement without overriding choices.

**Exact fix:** In both places, replace the composition requirement with:

> Teams have different roles and approaches and use every member’s field knowledge. Mix chosen clusters and jobs where choices allow; no student must change their cluster or job to form a team.

Retain the norms, disagreement record and individual contribution evidence. The local practice description requires respect for differing views and skills, not compulsory differences in chosen occupations.

### 10. SEL’s repeated timing explanation is wrong for several later units

**Severity:** Minor. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier Pathways m1.

**Location:** Cross-subject, SEL rows for Units 3, 4 and 6.

“As above” repeats the claim that SEL teaches these skills late and after the career unit. SEL unit 9 runs on school days 53 to 73, before career Units 3 and 4. SEL unit 11 runs on days 108 to 133, before career Unit 6. Other leans remain later or concurrent.

**Exact fix:** Replace the shorthand with row-specific timing:

- Unit 3: snap judgments taught earlier in SEL unit 9.
- Unit 4: interests taught earlier in unit 9; resilience remains later in unit 12.
- Unit 6: teamwork and planning taught earlier in units 9/11; effects taught alongside in unit 12.

Keep every bridge for students who do not take SEL.

### 11. Living notes still describe completed work as pending

**Severity:** Minor. **Confidence:** Firm.  
**LAYER:** process. **REPEAT:** yes, earlier Pathways m3 and previous stale-note findings.

**Location:** Cross-subject opening; For the lead items 2 and 6; career education status row in ADOPTION-BAR-SUBJECTS.

The computer science, library and SEL frames exist and are cited in this frame, yet the opening says they are unwritten and item 6 still waits for them. Item 2 describes the now-fixed frame-code splitter. The adoption-bar row still lists five Cory calls as owed although DESK-ANSWERS records their resolution.

**Exact fix:**

- State that all cited frames are on file and optional-course leans retain independent bridges.
- Replace item 6 with the reconciled timing results, including finding 10.
- Rewrite item 2 as specified in finding 3.
- Remove the five resolved calls from the adoption-bar row’s owed list; retain the second-state-rubric item.

Do not rewrite the dated review records.

### 12. The load explanation misstates its row counts

**Severity:** Minor. **Confidence:** Firm.  
**LAYER:** frame. **REPEAT:** yes, earlier Pathways m4, with a corrected range.

**Location:** “Why 96 fits.”

There are 57 learner-goal and practice rows: 45 plus 12. Six sit in Unit 2, leaving 51 elsewhere. The actual clusters contain four to six sub-clusters, so a full-path student meets **72 to 78 rows**, rather than about 70.

**Exact fix:** Replace the relevant wording with:

> The 51 rows outside Unit 2 are learner goals and practices; six more sit inside Unit 2. A full-path student meets 72 to 78 rows: 57 learner-goal and practice rows, three cluster rows and 12 to 18 sub-cluster rows.

## What is right and should remain

- The six-unit order connects exploration, reflection, a named job, employment tasks and an applied project.
- All selected rows and owned codes are placed correctly; no grade ownership move is needed.
- The incoming seams are reciprocal, with a fallback for students who never took Career Exploration.
- Portfolio choice does not waive practice evidence. Required attachments protect that earlier repair.
- Plans remain private, routes are not ranked, sensitive choices receive alternatives, and adult students make their own leave-out choices.
- The frame distinguishes national from regional figures and correctly notes Table 11’s missing October 2025 data.

## Lens checklist, course-frame layer

| Lens line | Result |
|---|---|
| Self, world of work, plan, action; plan revised | Met. |
| Real jobs and dated figures; conditions and place included | Partly met: finding 8 completes the pay-gap anchor. |
| Applied work from a field, rather than cluster posters | Met. |
| Practices taught through tasks and assessed evidence | Substantially met; findings 5, 6 and 9 repair delivery conditions. |
| Several clusters studied at depth | Met: three on the full path; two on the explicitly authorized shorter path. |
| Many routes without ranking people | Met. |
| Stereotypes countered through evidence and worker accounts | Partly met: finding 1 restores the required decision example. |
| Honest about school additions and paper alternatives | Partly met: finding 2 repairs the lateral-reading alternative. |
| Unit and day checklist details | Later-layer checks; models, rubrics, privacy and feedback requirements are specified here but cannot yet be verified in finished lessons. |

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Keep the one-year structure without a Year column | The grade range describes availability, not four successive years. | Frame |
| Add the CD2.A7 case before the recruiting-ad rewrite | Restores the required action within existing scope. | Frame, Unit 3 |
| Use paper source-investigation packets | Makes the promised lateral check executable. | Frame, Unit 6 |
| Use the explicit short-session numbering in finding 4 | Preserves the stated allocations and closing days. | Frame |
| Spread device turns across three sessions | Fits the existing device assumption without adding days. | Frame |
| Allow different team roles when chosen occupations coincide | Preserves choice and the teamwork practice. | Frame; practice 4 progression note |
| Keep computer science citations labeled as course days | They are accurate as labeled and follow the brief’s citation convention. | No change |

## Earlier-review reconciliation

The earlier Pathways review’s paper-source and scheduling concerns remain supported. Its frame-parser finding is now partly resolved, while downstream parsing remains broken. I do not adopt its suggestion that the correctly labeled computer science course-day citations are erroneous. Its proposed student-row upper bound of 81 should be 78 for the actual progression rows.

The mid-year check and respond days match the calendar. The shared library respond/check overlap and other after-core clustering remain matters for the lead’s calendar pass; they do not invalidate this high school frame’s structure.

## For Cory

- **Existing scope/access question:** whether the final course may record practice 5’s digital operation as unmet for a student with no device access.
- **Existing scope/dose question:** if the corrected 64-session schedule still proves overloaded at the scope read, choose between additional time and reduced breadth or project demand.

No new money, staffing or outside-reader request arises from this review.

## Sources and limits

- [Advance CTE, Career Ready Practices](https://careertech.org/resource/career-ready-practices/): publisher’s page opened; confirms the twelve-practice resource. Its linked PDF supplied no extractable text here, so detailed practice checks used the repository’s documented paraphrases.
- [BLS Table 11](https://www.bls.gov/cps/cpsaat11.htm): employment composition and the 2025 data limitation.
- [BLS Table 37](https://www.bls.gov/cps/cpsaat37.htm) and [Table 39](https://www.bls.gov/cps/cpsaat39.htm): appropriate earnings sources for finding 8.
- [NIOSH Talking Safety](https://www.cdc.gov/niosh/young-workers/talking-safety/) and [OSHA Young Workers](https://www.osha.gov/young-workers): opened as workplace-safety references. This frame review does not replace the later safety read.
- [University of Maryland Extension, FS-1077](https://www.extension.umd.edu/resource/food-safety-your-school-gardens-classrooms-and-greenhouses-fs-1077): live production address opened. **For the source list:** replace the frame’s development-host link with this address.
- [NCDA’s 2024 framework PDF](https://www.ncda.org/aws/NCDA/asset_manager/get_file/896607?ver=0) and [guidelines page](https://www.ncda.org/aws/NCDA/pt/sp/ncdg_home_page): both returned 403, **browser check**. I did not bypass those refusals. Indicator findings compare the frame with the repository’s local codes, paraphrases and progression requirements; the original wording was not independently revalidated.

No substantive curriculum finding rests on model memory. Prior-run memory was used only for review-format conventions. Finished lesson feasibility, actual source selections and complete assessment quality remain for the later layers.

