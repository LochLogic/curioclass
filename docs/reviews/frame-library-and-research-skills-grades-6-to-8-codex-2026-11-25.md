# Independent frame review: Library and Research Skills, grades 6 to 8

Date: 2026-11-25  
Course: `library-and-research-skills-grades-6-to-8`  
Read only. No files changed.

## Verdict

Revise before writing the scope and sequence. The frame has a sound three-year structure, complete skill placement, coherent handoffs and a workable calendar, but some assessments establish a plan or an individual answer where the owned standard requires actual collection or collaboration. The most important change is to identify the existing student work that supplies that missing scored evidence.

**Seven findings:** one major, four moderate and two minor.

## What I read

- The frame-read brief, the after-core provisions of frame-write, EXPERT.md, the library lens, and applicable repository rules.
- ADOPTION-BAR-SUBJECTS.md, including its shared requirements and library part; library STANDARD.md and APPROACH.md.
- The [course frame](S:/CurioClass/docs/courses/library-and-research-skills-grades-6-to-8/frame.md), its course-list selector, frames.csv entry and calendar.csv rows.
- All 23 selected progression rows, the neighboring grade 5 and grade 9 rows, and the adjacent frames’ handoff and model provisions.
- The cited core Units tables for ELA, science, social studies and civics.
- Library prework and progression reviews, their fix records, applicable decisions, the base-material scout, and earlier library frame findings.
- The stored grades 6 to 8 continuum document, including its grade columns and priority boxes.
- Outside sources linked below.

## Checks

| Check | Result |
|---|---|
| `python -X utf8 scripts/frame.py check library-and-research-skills-grades-6-to-8` | **0 failures.** Nine units, 54 days: 42 unit days and 12 check/respond days. |
| Independent placement count | All 23 selected skills appear exactly once; 19 distinct owned standards. |
| Annual totals | Each year has 14 unit days, two check days and two respond days. |
| Calendar rows | Match the frame’s unit and check placements. Checks avoid the core check weeks. |
| Course-filtered `plan.py check` | Stops because day-level plan files do not exist yet. This does not block a frame verdict. |
| `stale.py check` | One failure, in the physical education grades 9 to 12 frame, outside this course. |

The gate wrapper was not run because it writes output files; the course-filtered plan check replaced the brief’s unfiltered command under the repository rule.

## Findings, most serious first

### 1. Some owned standards lack scored evidence of the action they require

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the earlier library reads identified incomplete evidence for owned outcomes  
**Confidence:** firm

**Location:** Units 6, 7 and 8, lines 231 to 233; course-level checks 4 and 5, lines 243 to 244.

Three assessment descriptions stop short of their owned outcomes:

- **Unit 7, IV.B.2:** the sitting scores a search plan naming three perspectives and source kinds. It does not require students to collect information representing those perspectives.
- **Unit 6, V.C.3:** the group generates and evaluates solutions during the unit, but the named scored evidence is an individual answer about an unseen problem. The page rubric is described as scoring sources and credit, rather than collaborative solution development.
- **Unit 8, IV.C.3:** students compare sites with classmates during inquiry, but its named assessment is an individual comparison of two entries. No scored record establishes each student’s contribution to the collaborative comparison.

The distinction follows the actions in the [AASL learner framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf), rather than a requirement for longer tests.

**Why it matters:** A student could pass the stated assessment without demonstrating the complete owned outcome.

**Exact fix:** Use work already scheduled:

1. In Unit 7, score each student’s inquiry log for information actually collected from three perspectives, with a source and relevant finding for each. Retain the unseen search-plan item as transfer evidence.
2. In Unit 6 and check 4, explicitly score the existing group solution list and each student’s contribution: ideas generated before selection, findings supporting the retained ideas, and how another member’s contribution changed an idea.
3. In Unit 8 and check 5, score the existing pair comparison chart, with each student’s contribution identified. Retain the individual unseen comparison.
4. Name these records in the unit rows and check cells. No additional assessment day is needed.

### 2. Unit 4 names navigation and subject headings but does not allocate their teaching or check

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, coverage stated without a corresponding teaching/check allocation  
**Confidence:** firm

**Location:** Unit 4, line 229; `g7-search-results`.

The current progression note and What students learn include navigating a site’s menus/search box and following subject headings or category labels. However, the four-day outline names filters, reference works and result selection, and its sitting tests those same moves. Neither added navigation skill has an explicit practice or assessment task.

These are identifiable skills in the stored continuum’s Navigation and Search Strategies row, not interchangeable names for filtering results.

**Why it matters:** The scope writer could follow the day outline faithfully and omit the additions that the frame says it teaches.

**Exact fix:** Add the following within the existing four days:

- Day 1: model finding an answering page through an invented reference site’s menu/search box and following its subject heading to related records.
- Day 2: include both moves in the printed search practice.
- Day 4: make one of the three selected results require a navigation route and one require following a subject heading; students record the route and resulting record.

Replace equivalent result-selection repetitions rather than extending the sitting.

### 3. Several assumed predecessor rows have no named retrieval task

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, frame-write lesson 16  
**Confidence:** firm

**Location:** Readiness and retrieval, lines 69 to 77; Units 5, 6, 7 and 9.

The frame promises that each assumed earlier row is retrieved, but the unit entries omit:

| Unit | Assumed rows missing from its named retrieval |
|---|---|
| 5 | `g6-keep-questioning`, `g6-quote-paraphrase` |
| 6 | `g6-group-wiki`, `g6-team-product`, `g6-make-and-improve` |
| 7 | `g7-evidence-discussion` |
| 9 | `g7-group-solutions`, `g7-feedback-loop` |

For example, Unit 6 retrieves citation from Unit 5, but its progression rows assume the previous year’s encyclopedia, teamwork and version-log skills.

**Why it matters:** These units begin new work on foundations the teacher has not checked, despite the frame’s explicit retrieval promise.

**Exact fix:** Retain the existing retrievals and add short opening tasks on later days:

- Unit 5, day 3: write a follow-up question from a finding and distinguish a quotation card from a paraphrase card.
- Unit 6, day 3: use a compact prior-work packet to identify an article reference, explain a team contribution and interpret a version-log change.
- Unit 7, day 3: give one source-backed discussion turn and ask another speaker for its source.
- Unit 9, day 3: connect a proposed group solution to a finding and complete a keep/change response to feedback.

Limit each opening to five minutes and keep day 1 for its hook and question.

### 4. Sensitivity directions do not consistently follow the optional host content

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, frame-write lessons 12 and 30  
**Confidence:** likely

**Location:** Sensitivity reads, lines 103 to 114; Units 5, 7 and 8.

The frame identifies several communities and sensitive cases, but its host choices introduce additional content:

- Unit 5 can use ELA’s smallpox and credit inquiry, whose frame names death, enslavement, Onesimus and Native nations’ losses.
- Unit 7 can use ELA’s conflicting-viewpoints work on Banneker, Jefferson and the Declaration’s exclusions.
- Unit 8 can use ELA’s 1906 food and medicine inquiry, whose frame names injury, immigrant workers and human testing.

The corresponding library notes are generic. Unlike the grade 9 to 12 library frame, this frame does not establish that every adopted host carries its own sensitivity boundaries and source requirements into library.

**Why it matters:** A writer could import the host’s sources while applying only the library stand-alone case’s lighter notes.

**Exact fix:** Add this course-wide rule:

> When a unit uses a core host’s content, its sensitivity read also applies the host frame’s last-column boundaries and studies the host’s named sources first. The unit plan records which host texts and communities its source set actually includes.

Then add explicit host-content notes to Units 5, 7 and 8 naming the sensitive content above. Keep their stand-alone alternatives and prohibit personal health or family disclosures.

### 5. The source map does not identify a finite set of base items

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** new  
**Confidence:** firm

**Location:** Source map, lines 325 to 341.

The table maps categories such as “Intro lessons” and “The parallel assessments,” with assessments assigned collectively to three units. It does not identify which individual lessons, levels or assessment versions are selected. Consequently, a reader cannot verify that every selected base item is placed once or distinguish selected items from unused ones.

Version identification matters: the publisher’s [Creative Commons inventory](https://cor.inquirygroup.org/creative-commons/) lists parallel assessments under both permitted and restricted licenses.

**Why it matters:** The scope writer must make the actual base selection and resolve its licensing and load, decisions the frame should make reviewable.

**Exact fix:** Replace the category table with one row per selected item, giving:

> Exact title and level/version | publisher link | receiving unit | adaptation purpose | license status

Assign every selected assessment to one receiving unit. If an item is intentionally reused, identify its first placement and label subsequent use as review. List unused eligible items as outside this partial selection. Keep the existing exclusion of restricted items and the requirement to inspect each selected file before adaptation.

The day-level CSV can still wait for the scope stage.

### 6. Unit 7’s compelling question fits only its stand-alone case

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, kindergarten frame finding 11  
**Confidence:** firm

**Location:** Unit 7, line 232.

“Should our school start later” cannot be answered from the unit’s alternative ELA host about historical authors answering conflicting viewpoints, or its science host about a technology.

**Why it matters:** A host-path teacher would need to replace the published compelling question.

**Exact fix:** Use:

> How do we test what we expect against evidence and views different from our own?

Retain the school-start-time question as the stand-alone inquiry’s case question.

### 7. The frame still requests six progression edits already present

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier combined library frame read, M1  
**Confidence:** firm

**Location:** For the lead items 1 and 5, lines 345 to 352 and 364 to 365; Check set read bullet.

All six proposed additions are already present in the current progression notes. Nevertheless, item 1 says to append them, and item 5 conditions completion on applying them. The Check set read bullet also describes them as forthcoming row changes.

**Why it matters:** Following the instructions would duplicate notes and obscure what remains unfinished.

**Exact fix:**

- Replace item 1’s instructions with:

  > The six L103 note additions are present in data/progressions/library.csv. No further append is required.

- Replace item 5 with:

  > The grades 6 to 8 comparison is complete and its six note additions are present. Record this band’s completion in the lead’s L103 tracking.

- Change prospective wording in Check set read to past tense.
- Leave the dated earlier review unchanged.

## Lens checklist at the frame layer

| Lens requirement | Mark |
|---|---|
| Spaced instruction across each year, rather than orientation week | Met |
| Named priority skills and checks | Partly met: findings 1 and 2 |
| Single ownership and explained grade differences | Met |
| Library teaches lateral reading before social studies applies it to news | Met |
| Full inquiry cycles with named core hosts and stand-alone alternatives | Met in design; day-level completion remains to be verified |
| Source judgment requires leaving the page | Met |
| Honest use at grades 6 to 8 depth | Met |
| Research products shared with an audience | Met |
| No assumed paid database, library access or student account | Met |
| Appropriate sensitivity directions | Partly met: finding 4 |
| No unsupported claim of general score improvement | Met |
| Actual day captures, teacher swap notes and finished student-page wording | Not applicable yet |

## What is right and should be retained

The annual separation, skill placement and year-to-year handoffs are coherent. Preserve the paper path, invented practice cases, explicit source ownership, four-factor fair use reasoning, feedback before product scoring, and course-level checks serving as the immediately preceding unit’s assessment.

Keep the existing 18-session annual structure while making the local repairs above. Row counts alone do not establish that additional sessions are necessary.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Score existing collection and collaboration records | Establishes the owned actions without another test day | Course frame |
| Place missing retrievals on later-day openings | Preserves day 1 and the existing annual calendar | Course frame |
| Make Unit 7’s main question independent of its case | Supports both named hosts and the stand-alone path | Course frame |
| Treat the six L103 additions as completed | Verified against current progression notes | Course frame; lead tracking |
| Retain the current dose pending scope-level timing | No demonstrated need to change course scope or staffing | No dose change |

## What I could not judge

The partial-base lesson files are not in the source store, so their detailed adaptation load remains unverified. Finished source sets, rubrics, accessibility supports and lesson timings do not exist at this layer.

The continuum website was inaccessible through the web tool. I read the existing stored grades 6 to 8 document instead; its public URL remains **browser check**. No curriculum finding above rests on recalled source content.

## Sources

- [AASL learner framework, second edition](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf): checked owned competency actions.
- [Empire State continuum, grades 6 to 8](https://libguides.monroe.edu/ld.php?content_id=49990830): read the stored document; checked grade expectations and priority skills. Website status: browser check.
- [Civic Online Reasoning license inventory](https://cor.inquirygroup.org/creative-commons/): checked item-specific license distinctions.
- [Civic Online Reasoning middle school module](https://cor.inquirygroup.org/blog/module-for-middle-school/): checked the publisher’s staged modeling and practice sequence.
- [Teaching lateral reading](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/): checked the method’s emphasis on external investigation.
- [US Copyright Office fair use explanation](https://www.copyright.gov/fair-use/more-info.html): checked the four-factor approach; no legal conclusion about an individual use is made.

## For the source list

Add the publisher’s middle school module as planning background. Its sequence supports separating introductory questions, modeled lateral reading and practice; it does not establish this course’s dose.

## For Cory

None newly required. The proposed fixes preserve the current course scope, audience and dose. The existing partial-base download dependency remains before adaptation begins.

