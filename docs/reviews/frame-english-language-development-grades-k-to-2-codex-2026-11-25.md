# Independent frame review: English language development, grades K to 2

**Date:** November 25, 2026  
**Verdict:** Revise before downstream planning. The band structure, row placement and yearly calendars are sound, but the frame does not yet establish full coverage of several owned expectations or the required SI goals and language-use recurrence across every year. Complete those language goals first, then correct the host dependencies and contradictory assessment instructions below.

**Finding count: 7.** No files were changed.

## What I read and checked

- [The complete course frame](S:/CurioClass/docs/courses/english-language-development-grades-k-to-2/frame.md), its `frames.csv` record, course-list selector and calendar rows.
- All 33 selected ELD progression rows for K, 1 and 2, plus grade 3’s receiving rows and `eld-edges.md`.
- The frame-read brief, after-core frame-write provisions, EXPERT instructions, ELD lens, subject bar part 10, ELD STANDARD and APPROACH, and RUBRIC-ELD.
- FOUNDATION, relevant production and baseline rules, calendar rules, source-register entries and ELD decisions.
- Relevant core-course Units tables for all three grades, ELD prework and progression reviews, and comparable earlier frame findings.

There is no preceding ELD course. The grades 3 to 5 frame does not yet exist, so its side of the seam was checked against grade 3’s progression rows.

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check english-language-development-grades-k-to-2` | **0 failures** |
| Independent row placement | All 33 selected skills placed exactly once; no foreign skills |
| Independent calendar calculation | Each year covers days 1 to 160 without gaps or overlaps: 154 unit days plus 6 check/respond days |
| ELD course-level checks against core checks | No conflicting core check weeks in K, 1 or 2 |
| `python -X utf8 scripts/stale.py check` | 70 files, **0 failures** |

The scoped `plan.py check english-language-development-grades-k-to-2` reported one failure because lesson-plan tables do not exist yet; the structural frame check passed, and the review proceeded.

## Findings, most serious first

### 1. Several owned expectations are represented only in part

**Severity:** Serious  
**LAYER:** frame; progression  
**REPEAT:** yes, incomplete required performances recur in earlier ELA frame reads  
**Confidence:** Firm

**Location:** Units 4, 9 and 10; progression rows `k-sc-explain`, `g1-ss-argue` and `g1-sc-explain`.

The descriptions and checks support narrower performances than their owned expectations:

| Unit | Missing performance | Exact fix |
|---|---|---|
| 9 | Source evidence, distinguishing fact from opinion, and connecting evidence to the claim | Add a short pictured source about the school problem. Students distinguish a checkable statement from a preference, select supporting information, and explain how it supports their choice. Assess this with a new source. |
| 4 | Formulating an investigable question or design problem and comparing solutions | Use the host’s existing push or shade records. Students formulate the question and compare two recorded solutions, explaining their choice. |
| 10 | Formulating the question, selecting supporting observations and comparing solutions | Use existing sound or light records for these language tasks, including a comparison of two ways to solve the recorded problem. |

These requirements appear in the [official framework, PDF pages 54, 74 and 76, printed pages 53, 73 and 75](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf).

Keep the investigations in science. Amend the three progression notes and the frame’s learning and assessment cells without moving their owned standards. Otherwise, writers can complete the listed tasks while leaving parts of the claimed expectations untaught.

The earlier ELD progression review explicitly left expectation wording unjudged. Its code-coverage result does not settle this finding.

### 2. Eight units lack an explicit social and instructional language goal

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** “Units and reasons” summary and Units **3, 6, 11, 12, 13, 16, 17 and 18**.

The frame places each year’s four SI rows in four units. The remaining eight units have partner talk but no named SI expectation, function or evidence. Bar item 1 and STANDARD section 3 require SI beside content-area language in **every unit**. A recurring talk routine alone does not specify what social language students learn.

**Exact fix:** Add a carried SI id, its owner year, a concrete partner-language goal and an observable look-for to each missing unit’s “What students learn” cell:

| Unit | SI goal to add |
|---|---|
| 3 | Inform: describe and sort observations, then summarize a partner’s report |
| 6 | Argue: give a reason for a sorting choice and respond to another choice |
| 11 | Inform: give and follow directions using the place cards |
| 12 | Inform: summarize a partner’s animal observation |
| 13 | Inform: give and follow directions for reading the chart |
| 16 | Explain: describe how the partners arranged their resource-to-use chain |
| 17 | Explain: explain how the group selected its evidence cards |
| 18 | Argue: support a comparison and answer a partner’s reason |

Keep the existing Skills cells as primary placements. Label subsequent SI work as practice or review, so the 33-row placement remains intact.

### 3. The yearly recurrence claim is not supported by the unit map

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, ELD prework read finding 9 required later-unit returns  
**Confidence:** Firm

**Location:** “Key language uses as the spine,” Units table and “For the lead,” item 2.

Kindergarten Narrate, Explain and Argue each occupy only one unit. Grade 1 has the same problem. Grade 2 Inform and Narrate each occupy only one unit, with Narrate arriving in the final unit. Returning in the next grade does not establish the within-year recurrence required by bar item 13 and APPROACH’s “Across the unit.”

**Exact fix:** Add an explicit recurrence map and the corresponding tasks to the named units:

| Year | Returns to plan |
|---|---|
| K | Narrate: unit 2 to unit 4, recounting a recorded test. Explain: supported introduction in unit 3’s chart routine, then the harder cause explanation in unit 4. Argue: unit 5 to unit 6, defending a sort to a partner. |
| 1 | Narrate: unit 8 to unit 11, recounting how a map was made. Explain: unit 10 to unit 12, explaining the report-making routine. Argue: unit 9 to unit 13, defending a chart-based class choice. |
| 2 | Retrieve and extend SI Narrate in unit 14, then return with the fuller recount in unit 20. Return to Inform in unit 16 by summarizing the resource information before explaining its connections. |

Name what becomes harder at each return. Keep primary row placements, existing unit days and the limit of one or two key language uses per unit.

### 4. Three host dependencies need correction

**Severity:** Serious  
**LAYER:** frame; progression  
**REPEAT:** yes, unsuitable hosts and incomplete availability records recur in earlier progression and frame reads  
**Confidence:** Firm

**Location:** Units 2, 12 and 16 and their cross-subject entries.

| Location | Problem and student cost | Exact fix |
|---|---|---|
| Unit 2 | Its bridge ends on day 34, but the kindergarten ELA frame explicitly places weather information on days 35 to 48 and story elements from day 49. ELD assumes the weather story is available too early. | Extend the bridge through day 48 using an already-read toy story and class events. Begin weather-story analysis from day 49, after ELA reads it. Correct both the host cell and cross-subject row. |
| Unit 12 | It names science unit 7, `s1-parent-offspring`, as the host for likenesses between parents and young. Science unit 3 teaches those likenesses; unit 7 teaches behavior that helps young survive. | Name unit 3, `s1-like-parents`, as retrieved content. Use unit 7’s current records for descriptions of young animals signaling and adults responding. Add that descriptive task to the learning cell and add the retrieved host to `g1-sc-inform`’s cross-subject field. |
| Unit 16 | Its bridge covers days 39 to 42, but the calendar places the first social studies unit 3 meeting on school day 45. Days 43 and 44 remain unbridged. | Change the bridge to **days 39 to 44** and begin the new resource-to-use work after the host introduces it. |

These changes preserve the units and calendar while making the content available when ELD uses it.

### 5. Unit 9’s assessment contradicts the withdrawal rule

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, progression review finding 3 concerned scaffold withdrawal  
**Confidence:** Likely

**Location:** Unit 9’s end-of-unit assessment, “draw and write the claim with the frame.”

The course-wide rule removes the cloze frame for levels 1 and 2 before the check and removes sentence frames for levels 3 and 4 before the end-of-unit task. The local assessment instruction tells the writer to retain “the frame,” making the intended evidence ambiguous.

**Exact fix:** Replace that phrase with:

> Draw and write the claim using the permitted picture supports and word bank. Remove the task-specific cloze and sentence frames before this assessment, following the course withdrawal rule; retain individually required access accommodations.

Keep framed rehearsal before the assessment.

### 6. Living notes describe work that has already changed

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, stale availability and validator notes recur in earlier ELD and frame reads  
**Confidence:** Firm

The stale checker passes, but it does not detect these claims.

| Location | Exact fix |
|---|---|
| Frame, “For the lead,” item 9 | Replace the claim that `frame.py` cannot handle band years with: “Band-year calendar handling is implemented. The calendar places this course under grades K, 1 and 2, and its structural check passes. Recheck clashes after calendar changes.” |
| Frame, item 1’s proposed replacement | Replace “The four band frames are written” with “Band frames are authorized by Cory’s November 25 decision; this K to 2 draft exists.” The other three frame files do not yet exist. |
| ELD STANDARD opening and section 6; APPROACH opening; lens opening | State the current exception once in each applicable rule: frames are authorized now; the C11 condition continues to hold the later stages. Remove the contrary prohibition on starting a frame. |
| ADOPTION-BAR-SUBJECTS, ELD prework status row | Replace the owed progression-check entry and four calls with: “Progression support and the four q-fix-eld-1 decisions were applied November 21. Later stages remain subject to the C11 gate.” |

Preserve dated review reports as historical records.

### 7. The mid-unit assessment summary incorrectly includes unit 20

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** “Days,” lines 20 to 21.

The summary says units 1, 2, 19 and 20 exceed 25 days. Their lengths are **30, 31, 27 and 25** respectively. Unit 20’s own row correctly contains no mid-unit assessment.

**Exact fix:** Change the list to **“units 1, 2 and 19”**. Keep unit 20 at 25 days and retain the current yearly totals.

## Lens checklist

| Frame-layer lens line | Result |
|---|---|
| Content behind the units, rather than isolated word lists or grammar drills | **Met**, with host corrections in finding 4 |
| Multiple levels preserving content and thinking demand | **Met in the stated design**; assessment withdrawal needs finding 5 |
| Valid standard, cluster and key-language-use ids | **Met** |
| Entry and exit points stated; ELD distinct from ELA | **Met** |
| ELA pairing for LA and core hosts for MA, SC and SS | **Met for named pairings**; availability and fit need finding 4 |

The unit- and day-layer checklist cannot yet be verified against unwritten materials. The frame appropriately requires structured talk, learner-specific notes, home-language support and language-versus-learning-need guidance.

## What is right and should remain

- The three complete grade years, continuous unit numbering and separate yearly checks.
- The 154 plus 6 allocation and the check weeks: K and grade 1 weeks 18 and 28; grade 2 weeks 17 and 27.
- Primary placement of all 33 progression rows and ownership of the 26 K and grade 1 ids.
- Both modes, direct teaching of forms, paper access and teacher-held evidence.
- The distinction between ELD language teaching and the host course’s content instruction.
- Invented-story options, family-topic protections and the planned sensitivity and Spanish reads.
- Grade 2’s reasoned pairing of its science Explain and Argue rows. No separate ELD base-course source map is required for the stated design.

## Settled by the expert

These are recommendations for the caller to apply; this read changed nothing.

| Choice | Reason | Files affected |
|---|---|---|
| Complete expectations inside their current units | Preserves ownership while correcting incomplete coverage | Frame; three progression notes |
| Record SI recurrence outside primary Skills placements | Meets the subject bar without duplicate primary placements | Frame |
| Use the host’s actual content availability | Prevents premature or mismatched tasks | Frame; `g1-sc-inform` host record |
| Remove sentence frames from unit 9’s independent assessment | Makes its evidence consistent with the stated rule | Frame |
| Remove unit 20 from the over-25-day list | Correct arithmetic; no day change | Frame |

## For Cory

- **Newcomer delivery remains a staffing and time decision.** Item 8 proposes either added time or a side table during the regular period. Before adopting the latter, settle who teaches the strand and how newcomers recover the regular-unit language work they miss. The existing decision keeps the strand beside the 160-day frame; this review does not authorize additional staffing or select a delivery model.

## Limits, sources and memory

The next band’s frame, actual host texts, newcomer strand, assessment items, accommodations and classroom timing remain unverified. The C11 evidence was not audited here; the November 25 decision authorizes this frame while retaining the later-stage condition.

- [Official English language development framework](https://wida.wisc.edu/sites/default/files/resource/WIDA-ELD-Standards-Framework-2020.pdf): checked expectation wording behind the owned codes, rather than relying on code presence.
- [Institute of Education Sciences practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/19): supports retaining language instruction through content and planned oral and written work. It does not validate this course’s particular schedule.

**For the source list:** Add the precise expectation-page checks above to the existing framework entry. No new source is needed.

No substantive finding rests on memory. Prior memory was used only for review-workflow guidance; repository and outside-source evidence were checked during this read.

