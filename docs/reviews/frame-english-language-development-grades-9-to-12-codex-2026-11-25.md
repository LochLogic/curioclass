# Independent frame review: English language development, grades 9 to 12

**Date:** November 25, 2026  
**Course:** `english-language-development-grades-9-to-12`  
**Finding count:** 7  
**Disposition:** Revise before the scope and sequence. No files were changed.

## Verdict

The frame has a sound four-year structure, complete progression-row placement and workable yearly calendars. Its biggest risks are incomplete performances behind the grade 12 ownership claims and assessments that omit their stated social and instructional language goals. Complete those performances and align the assessment instructions before downstream planning.

## What I read and checked

- The complete [course frame](S:/CurioClass/docs/courses/english-language-development-grades-9-to-12/frame.md), its `course-list.csv` selector, `frames.csv` record and calendar rows.
- All 52 selected progression rows, the grade 8 handoffs, and the preceding ELD frame’s overview, models, seams and grade 8 units. There is no subsequent ELD course.
- The frame-read brief, after-core frame-write provisions, EXPERT instructions, ELD lens, adoption bar part 10, ELD STANDARD and APPROACH, and RUBRIC-ELD.
- Relevant foundation, production, baseline, source-register, calendar and recorded decision rules.
- Named core-host placements and calendar windows, with targeted host day rows where availability needed closer checking.
- Earlier ELD progression, pilot and frame reports, used after the initial frame read to distinguish settled decisions from recurring defects.
- The published framework’s 18 grade 9 to 12 content expectations and the carried SI expectations.

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check english-language-development-grades-9-to-12` | **0 failures** |
| `python -X utf8 scripts/progression.py check eld` | **162 rows, 0 failures** |
| Independent placement check | All 52 selected skills placed exactly once |
| Independent calendar calculation | Each year covers school days 1 to 160 without gaps or overlaps: 154 unit days plus 6 check/respond days |
| Mid-year checks against core checks | No conflicting core check weeks |
| Year-end checks | Week 32 overlaps are permitted by the high school finals rule |
| Scoped `plan.py check` | One stage-related failure: lesson-plan tables do not exist yet |
| `python -X utf8 scripts/stale.py check` | One unrelated failure in the PE grades 9 to 12 frame |

The unfiltered plan check was replaced with the scoped check under AGENTS.md; the course gate wrapper was not run because it writes output and baseline files.

## Findings, most serious first

### 1. The owner-year descriptions and assessments do not establish full expectation coverage

**Severity:** Serious  
**LAYER:** frame; progression  
**REPEAT:** yes, pilot coverage finding and combined ELD frame read finding 2  
**Confidence:** Firm

**Location:** “Standard,” lines 46 to 49; Units 28 to 36, lines 296 to 304; corresponding grade 12 progression notes.

The printed expectations require performances beyond the listed tasks. Add the following to both teaching and assessment:

| Unit | Exact addition |
|---|---|
| 28, LA Narrate | Theme development, changing character relationships and viewpoint, supported by word-choice evidence. |
| 29, SS Explain | Compare expert accounts of multiple checks, including disagreements and unintended outcomes. |
| 30, SC Explain | Formulate an investigable question, evaluate source reliability, predict variable changes and refine a remedy. |
| 31, MA Explain | Evaluate alternative methods against mathematical evidence; assess that evaluation. |
| 32, SS Argue | Judge source credibility, accuracy and relevance against an expert reference. |
| 33, LA Inform | Analyze evolving word choices and text-based inferences; teach neutrality and cohesion. |
| 34, MA Argue | Generalize across cases and extend a peer’s argument. |
| 35, SC Argue | Evaluate constraints and ethical issues; establish context and justify stance. |
| 36, LA Argue | Corroborate sources, evaluate reasoning and conclude with recommendations in an objective register. |

These additions come from the [official framework, PDF pages 326 to 330, printed pages 325 to 329](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf).

**Why it matters:** Writers can complete the current tasks while leaving claimed performances untaught.

**Exact fix:** Amend each listed unit’s learning and assessment cells and its progression note. Retain the existing ownership and unit placements. Replace the memory-based coverage statement and For the lead item 2 with the verified page reference and the resulting coverage record.

This changes the earlier combined review’s conclusion: the problem is substantive incomplete coverage, beyond an unfinished source check.

### 2. Units 31 and 33 do not assess their stated SI goals

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Units 31 and 33, lines 299 and 301.

Unit 31 teaches an SI plan statement with goals, steps and reasons, but its assessment asks only for a mathematical method explanation. Unit 33 teaches a formal spoken and written request, but its assessment lists reading, an email and an informative section, with no spoken task.

**Why it matters:** The resulting records cannot establish whether students achieved those SI goals. Unit 33 also contradicts the course-wide promise that every end-of-unit assessment includes teacher-heard talk.

**Exact fix:**

- **Unit 31:** Use a real or invented project plan as the context for the method explanation. Require its goal, next steps, reasons and one alternative in both the spoken and written response. Record SI look-fors separately from mathematical-language look-fors.
- **Unit 33:** On the first assessment day, hear each student make the formal request. On the second day, combine the email and informative section into one purposeful written product: a formal email containing the defined term, source synthesis and request. Judge greeting, purpose, question and close alongside the LA language goals.

These changes preserve the two assessment days and avoid adding another full written performance.

### 3. Several progression scaffolds belong to hosts the frame explicitly excludes

**Severity:** Moderate  
**LAYER:** frame; progression  
**REPEAT:** yes, progression review findings 1 and 5 concerned support and vocabulary fit  
**Confidence:** Firm

**Location:** Units 10, 29 and 30; progression notes for `g10-sc-explain`, `g12-ss-explain` and `g12-sc-explain`.

| Unit | Mismatch |
|---|---|
| 10 | The frame excludes reaction rates, but the progression supplies “When ___ goes up, the rate ___” and “More frequent collisions contribute to ___.” |
| 29 | The frame excludes economics, but the lowest entry point uses “When demand goes up, ___.” |
| 30 | Earth and Space Science students use the earthquake system, and other students may use water quality or orbits, but the lowest entry point supplies “The current is driven by ___.” |

**Why it matters:** A writer following both files would give some learners supports about content their task does not use. The students needing the most support receive the least usable prompt.

**Exact fix:** Keep the selected hosts and withdrawal rules, but supply matching supports in the frame and progression notes:

- Unit 10: “Elements in this column have ___. This helps explain ___.”
- Unit 29: “When one branch ___, another branch can ___.”
- Unit 30: Give a labeled model and a host-specific opening for water quality, the earthquake system and orbits. Use “___ contributes to ___ because ___” as the shared pattern.

Retaining one suitable host is sound. The earlier recommendation to keep these rows unchanged overlooks the incompatible support text.

### 4. Units 28 and 36 mix assessment forms without counting the product stages

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, evidence placement is a recurring frame-read issue  
**Confidence:** Firm

**Location:** “Days,” lines 24 to 26; Units 28 and 36.

The summary describes every end-of-unit assessment as a two-day sitting with unseen items. Unit 28 also requires a narrative revised after feedback on day 12. Unit 36 requires an argument revised after written feedback, without placing its draft, feedback and revision days.

**Why it matters:** The writer cannot tell which response is the independent sitting evidence and which is the revised product. Frame-write rule 19 requires those product stages to be counted.

**Exact fix:** State that these two units combine a revised writing product with an unseen interpretive and talk sitting. Count the stages explicitly:

| Unit | Product schedule | Sitting and response |
|---|---|---|
| 28 | Draft day 11; written feedback day 12; revision day 13 | Interpretive and talk tasks days 14 and 15; respond day 16 |
| 36 | Draft day 150; written feedback day 151; revision day 152 | Interpretive and talk tasks days 155 and 156; respond day 157 |

Identify the revised product as the writing evidence. Preserve feedback and revision when applying the senior shorter path.

### 5. “Unseen” selections lack the required check against existing teaching materials

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, pilot pattern note and combined ELD frame read finding 1  
**Confidence:** Firm

**Location:** Base text bullet and assessment selections in Units 9, 14, 17, 20, 22, 24, 28, 33 and 36.

The frame repeatedly calls for new public-domain or government selections without requiring a search across existing lessons and assessment items. Several selections come from subjects and periods already heavily represented in ELA and history.

**Why it matters:** A selection can be new to ELD while already familiar from another course, weakening the intended transfer evidence.

**Exact fix:** Add this rule to the Base text bullet and apply it to every assessment selection:

> Before designating a text or source set as unseen, search docs/ and data/, including section plans and items.csv, for the passage and its distinctive wording. Record the selection and the search result in the unit’s sources. Replace any passage already taught or assessed.

Retain the distinction between supplied records used during teaching and unseen assessment material.

### 6. Living notes still describe completed or changed work as pending

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, combined ELD frame read finding 7 and pilot stale-note findings  
**Confidence:** Firm

The stale checker does not detect these unmarked status claims.

| Location | Exact fix |
|---|---|
| Frame, For the lead item 7 | Replace the claim that the preceding frame is still being written. State that it exists and remove the reference to a nonexistent Pending marker. |
| Frame, Picked up table | Add the preceding unit numbers: Inform rows 18; MA Argue 19; LA/SI Argue 20; SC Argue and SI Explain 21; MA Explain 22; LA/SI Narrate 23; SS Explain 24; SS Argue 25; SC Explain 26. |
| ELD lens opening | Replace the blanket building restriction with: “Frames are authorized now. The scope and sequence, unit plans, days and newcomer strand wait until the C11 condition in STANDARD section 6 is met.” |
| ADOPTION-BAR-SUBJECTS, ELD prework status row | Remove the owed progression-check entry and four calls. State that progression support and the four decisions were applied November 21; retain the later-stage C11 condition. |

**Why it matters:** These notes can trigger duplicate work or incorrectly stop authorized frame work.

Preserve dated review reports as historical records.

### 7. Some language-goal references are incomplete codes

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, combined ELD frame read findings 15 and 16  
**Confidence:** Firm

**Location:** Newcomer strand, lines 115 to 121; SI review references in Units 6, 8 to 12, 16, 18, 21, 24 to 27, 29, 30 and 34 to 36.

`WIDA.ELD-LA.9-12.Inform` is a family of expectations, not a complete id. Numerous SI references name the use without its full id and owner.

**Why it matters:** The subject bar requires each unit’s language goals to name the expectation ids it plans to.

**Exact fix:**

- In the newcomer strand, name both `WIDA.ELD-LA.9-12.Inform.Interpretive` and `WIDA.ELD-LA.9-12.Inform.Expressive`.
- At every abbreviated SI reference, write `WIDA.ELD-SI.4-12.<use>, carried; owned in grade 4`, using the actual use.
- Keep the existing primary Skills placements and carry-only ownership.

## Lens checklist

| Frame-layer lens line | Result |
|---|---|
| Content behind units, rather than isolated word lists or grammar drills | **Met** |
| Multiple levels preserve content and thinking demand | **Met in the stated design; support fit needs finding 3** |
| Correct standard, cluster and key-language-use ids | **Owned codes met; prose references need finding 7** |
| Entry and exit points stated; ELD distinct from ELA | **Met** |
| ELA pairings and named core hosts | **Met at frame level** |

Both modes are planned throughout. The assessment exceptions in findings 1 and 2 need repair. Unit- and day-layer execution cannot yet be verified against unwritten materials.

## What is right and should remain

- Four complete grade years, each with its own units, assessments and two course-level checks.
- All 52 progression rows placed once, with the 18 content ids owned in grade 12 and SI ownership retained in grade 4.
- Explicit within-year returns for all four key language uses.
- The host-first calendar, retrieved alternatives and grade 12 elective fallbacks.
- Paper access, teacher-held evidence, learner-specific notes and home-language support.
- Invented applicants and stories, private handling of drafts, and the rule for students 18 or over.
- The distinction between ELD language instruction and host-course content teaching.

The emphasis on academic language through content and integrated oral and written work is consistent with the promising high school practices discussed by the [National Academies, chapter 8](https://www.nationalacademies.org/read/24677/chapter/10). That evidence does not establish the effectiveness of this course or its particular schedule.

## Settled by the expert

Recommendations for the caller to apply; this read changed nothing.

| Choice | Reason | Files affected |
|---|---|---|
| Complete expectations within their current owning units | Preserves ownership and course structure | Frame; grade 12 progression notes |
| Integrate SI evidence into existing assessment performances | Tests the stated goals within the allotted days | Frame, Units 31 and 33 |
| Match scaffolds to the selected host | Makes support usable without lowering the task | Frame; three progression notes |
| Distinguish revised products from unseen sittings | Makes evidence and time allocations explicit | Frame, Units 28 and 36 |
| Require an unused-passage search | Protects the intended transfer evidence | Frame |
| Correct living status notes and code references | Removes contradictory instructions | Named living documents |

## For Cory

- **Newcomer delivery remains a people and time decision.** Settle who teaches the 20-day strand and how newcomers receive the regular-unit language instruction during that period. The existing decision keeps the strand beside the 160-day frame; this review selects no staffing or delivery model.

## Limits, sources and memory

Actual assessment items, scoring examples, accommodations, host-passage selections, classroom timing and the newcomer strand remain unverified. The C11 evidence was not audited here.

- [Official English language development framework](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf): opened successfully; expectation lists checked directly.
- [National Academies, chapter 8](https://www.nationalacademies.org/read/24677/chapter/10): targeted reading of high school instruction and the limits of its research evidence.
- **For the source list:** Add the precise expectation-page check to the existing framework entry. No new source is required.

No substantive finding rests on memory. Prior memory was used only for report-workflow guidance.

