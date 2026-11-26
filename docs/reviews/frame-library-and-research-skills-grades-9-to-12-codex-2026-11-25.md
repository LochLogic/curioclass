# Second independent frame read: Library and Research Skills, grades 9 to 12

Date: 2026-11-25  
Course: `library-and-research-skills-grades-9-to-12`  
Read-only review. No files were changed.

## Verdict

The frame has a coherent four-year structure, correct skill placement and a calendar that matches its stated annual dose. It needs revision before the scope and sequence: several checks do not establish the complete owned action, recent progression additions lack explicit teaching or assessment, and grade 9 assumes an optional predecessor course. The most important repair is to make the teaching and scored evidence match the progression without increasing the annual session count.

## What I read and checked

- The complete course frame; its `course-list.csv` selector, `frames.csv` row and `calendar.csv` rows.
- All 24 selected progression rows, their grade 8 predecessors, and the grades 6 to 8 library frame. Grade 12 has no successor course.
- The review and writing briefs, EXPERT.md, the library lens, adoption-bar part 11 and shared criteria, library STANDARD.md and APPROACH.md.
- The relevant foundation, production-path, baseline, calendar, source and decision guidance.
- The named ELA and social studies host units.
- Library pre-work, progression and earlier frame reviews.
- The current AASL learner framework, relevant tables in the stored grades 9 to 12 continuum document, and the outside sources linked below.

Independent placement checks found:

| Check | Result |
|---|---|
| Selected progression skills | 24, each placed exactly once |
| Owned standard IDs | 18, matching the progression |
| Annual unit days | 14 in each grade |
| Annual check and respond days | 4 in each grade |
| Band total | 72 sessions |
| Calendar correspondence | Unit, check and respond ranges match |

**Gates:** `plan.py check library-and-research-skills-grades-9-to-12` fails because day-level plan files do not exist; `frame.py check library-and-research-skills-grades-9-to-12` passes with zero failures; `stale.py check` passes across 121 files. The plan-stage failure does not withhold this frame verdict.

## Findings, most serious first

### 1. Two owned outcomes are taught as actions but assessed through incomplete substitutes

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, grades 6 to 8 frame read, finding 1  
**Confidence:** firm  
**Location:** Units 6 and 7, lines 247 to 248; course checks 6 and 7, lines 260 to 261.

Unit 6 teaches publishing research for an audience, but its named scored records are the method note, bibliography and interview report. The unseen item asks students to choose a publishing form. Neither establishes that the published work actually communicates appropriately to its audience.

Unit 7 scores the revised guide, but does not name scored evidence of helping another learner use information. A student could produce an attractive guide without successfully carrying out the teaching already scheduled on day 60.

These distinctions follow the actions in the [AASL learner framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf), particularly VI.C.2 and VI.D.3.

**Why it matters:** The stated evidence can award ownership without demonstrating the complete outcome.

**Exact fix:**

- In Unit 6 and check 6, explicitly score the existing day 52 publication for whether its form, language and presentation serve the named audience. Retain the unseen form-selection item as transfer evidence.
- In Unit 7 and check 7, score the revised guide together with a day 60 teaching record: the move demonstrated, the recipient’s attempt, and how the student clarified or corrected it. Use teacher observation at school or a brief, anonymous account of the home teaching.
- Name these records beside their standard IDs. No additional assessment day is needed.

### 2. Four progression additions have not reached explicit teaching and evidence

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, grades 6 to 8 frame read, finding 2  
**Confidence:** firm  
**Location:** Units 4, 5 and 7; checks 4, 5 and 7; corresponding progression notes.

The progression now specifies:

| Row | Addition missing from the operational outline |
|---|---|
| `g10-label-own-work` | Standard-style credits embedded at the point of use |
| `g11-lateral-news` | Judging degrees of slant and their effect |
| `g11-advanced-search` | Revisiting result ordering and sponsored results |
| `g12-personal-system` | A goal drawn from the student’s strengths |

The frame’s Check set read bullet acknowledges these additions, but the day outlines and check descriptions do not consistently teach or collect evidence of them. General references to credits, lateral checking or a chosen goal do not make these particular moves explicit.

The stored continuum’s Academic Integrity, Perspective / Point of View, source-organization and reflection rows support these distinctions. Its organization and priority-skill purpose are documented in the [official continuum guide](https://slsa-nys.libguides.com/ifc/toc).

**Why it matters:** A scope writer could follow the frame faithfully and omit content already required by the progression.

**Exact fix:**

- **Unit 4, day 33:** model a citation beside a quotation, paraphrase or visual, using the grade 7 style. Day 34 applies it. Check 4 includes one point-of-use credit, rather than checking a label alone.
- **Unit 5, day 38:** include identifying sponsored placement and explaining why result rank does not establish authority. Check 5 samples that distinction.
- **Unit 5, day 39:** model degrees of slant using two captures. Day 40 records the degree and its effect on a claim; check 5 asks for the same judgment on one capture.
- **Unit 7, day 56:** add a private strength-to-goal note that generates the next-step search. Collect evidence of the search process without requiring disclosure of private strengths or plans.

Replace equivalent repetitions within the existing sessions.

### 3. Grade 9 has no entry check for students who did not take the optional predecessor

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier combined library frame read, M3  
**Confidence:** likely  
**Location:** Seams opening, lines 178 to 180; Units 1 and 2.

The frame says every grade 9 prerequisite is one year old, so “none needs a readiness check.” That reasoning assumes students took the grades 6 to 8 library course.

The predecessor frame explicitly recognizes that library is optional and checks its incoming prerequisites for that reason. The same access problem applies at grade 9. A five-minute retrieval from an untaken course cannot establish readiness.

**Why it matters:** Teachers may begin hard lateral cases, license reasoning and collaborative inquiry without knowing which prerequisite moves need teaching.

**Exact fix:** Add a **Readiness and retrieval** bullet:

> Grade 9 samples the grade 8 prerequisites because the preceding library course is optional. Unit 1 uses the last ten minutes of day 1, after the hook, to sample the expectation-and-update move, search perspectives, lateral checking and a traced reference. Unit 2 samples perspective gathering, fair use reasoning and a contribution from another learner in the last ten minutes of day 9’s respond session. Missing moves receive the corresponding grade 8 show-me case before the new work that needs them. Grades 10 to 12 retain their named retrieval tasks.

Rewrite the Seams opening to distinguish prerequisite age from demonstrated readiness.

### 4. New routines need an explicit modeled and rehearsed step before their scored use

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier library findings on first-use scoring and missing fading guidance  
**Confidence:** likely  
**Location:** Unit 3, line 244; Unit 6, line 247.

Unit 3 models seminar ground rules on day 22, then scores the day 24 seminar record without naming an unscored rehearsal of the required say-back and evidence turns.

Unit 6 first names the honesty review on day 51, labeled inquiry: first an invented project, then the student’s own work. No earlier show-me or guided practice explicitly teaches checking quotation context, representation and disclosure together.

This conflicts with the subject approach’s requirement to show a new move before independent inquiry.

**Why it matters:** The writer may turn the first student attempt into assessment, or hide new instruction inside an application day.

**Exact fix:**

- Add two short, unscored seminar turns to day 22: accurately say back a differing view, then add relevant evidence. Keep day 24 as the scored seminar.
- Add a teacher think-aloud and brief paired honesty check to day 49’s show-me session, using the planted-fault project. Day 51 then applies the already taught routine independently to the student’s own work.
- Name when help is withdrawn for these routines.

### 5. The lateral-reading time comparison mixes scheduled periods with available working time

**Severity:** Moderate  
**LAYER:** frame and progression  
**REPEAT:** yes, earlier combined library frame read, M2  
**Confidence:** firm on arithmetic; likely on the required allocation  
**Location:** Lateral reading time, lines 102 to 105; `g9-lateral-method` notes.

Seven 45-minute sessions equal 315 scheduled minutes. The frame itself allows about 39 working minutes per session, so those sessions contain at most **273 working minutes**, before their operator practice, synthesis work, sharing and reflection.

The published study used six 50-minute lessons. Its [university account](https://ed.stanford.edu/news/it-doesn-t-take-long-learn-how-spot-misinformation-online-stanford-study-finds) and [published supplement](https://supp.apa.org/psycarticles/supplemental/edu0000740/EDU_2020_0630_Supplemental_Materials.pdf) do not establish a universally effective 300-minute threshold, or an equivalent net working-time calculation.

**Why it matters:** The frame presents an unverified allocation as satisfying the subject’s explicit time commitment.

**Exact fix:** Replace the bullet’s comparison with:

> Seven sessions in grades 9 and 10 have lateral reading as a main move: 315 scheduled minutes and at most 273 working minutes before other tasks. This does not yet establish the subject’s 300-minute lateral-reading allocation. The scope and sequence must record instructional minutes for modeling, practice and inquiry across named sessions and show where that allocation is met. The study’s six 50-minute lessons are background, not evidence that this course or its paper path produces the same result.

Remove the claim that seven sessions already establish 300 minutes from the progression note. Retain the subject’s allocation requirement. Adding an eighth mixed session alone would not verify it.

### 6. Checks 4 and 8 need a bounded sample that fits one sitting

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** judgment call  
**Location:** Evidence bullet, lines 80 to 85; checks 4 and 8, lines 258 and 262.

Check 4 combines a matrix and connection map from four sources, claim-by-claim summary tracing, a product label, a subject-term search and a fair-sides rewrite.

Check 8 combines lateral checking, two upstream traces, a rewrite, a three-source synthesis map, citation, license interpretation and a personal-system task. Both inherit the approximately 35-minute sitting.

These are several performances, not merely several short questions. The descriptions give no source-length or response limits that make the sitting credible.

**Why it matters:** Later writers must either shorten the intended thinking or exceed the period.

**Exact fix:**

- For check 4, score the student’s revised matrix and map as product evidence. Name day 32 as its draft, teacher feedback before day 34, and revision on day 34. Replace the full unseen matrix and map with one missing matrix entry and one justified connection.
- For check 8, use three compact unseen cases: a source check with one upstream trace; a fair-sides and synthesis response to one short source set; and a citation/license correction. Reuse the already scored capstone and Unit 7 records for the remaining outcomes.
- State source-length, response and minute limits before the scope is accepted.

### 7. Settled partial bases still have no frame-level selection map

**Severity:** Moderate  
**LAYER:** base text  
**REPEAT:** yes, grades 6 to 8 frame read, finding 5  
**Confidence:** firm  
**Location:** Base text, lines 57 to 66; For Cory, lines 333 to 335.

STANDARD.md settles two partial bases. The frame names broad areas where they might fit, but defers any source map until files enter the source store.

The day-level CSV can wait. The frame still needs a finite selection showing what it intends to adapt. Public titles and licenses can be mapped without downloading instructional files. The [publisher’s license inventory](https://cor.inquirygroup.org/creative-commons/) distinguishes permitted and restricted items; the [web-literacy book’s contents and license](https://pressbooks.pub/webliteracy/) are also public.

**Why it matters:** Adaptation choices, duplication and load remain invisible to the frame reader.

**Exact fix:** Add a **Source map** section with one row per selected lesson, level or book chapter:

> Exact title/version | source link | receiving unit | purpose | license/status

Assign selected items to Units 1, 4 or 5 as appropriate. Label teacher-background reading separately. Mark uninspected instructional files as awaiting inspection and exclude restricted items. Keep the download dependency and defer the day-level CSV to the scope stage.

### 8. Several live notes request work that is already complete

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier combined library frame read, M1 and m6  
**Confidence:** firm  
**Location:** Check set read, lines 152 to 173; For the lead items 2, 3 and 5.

Current files contradict these instructions:

- All seven proposed progression-note additions are already present.
- The grades 6 to 8 seam now names this frame and its retrievals.
- The career frame’s Cross-subject table already identifies library Units 1, 3 and 4.
- `aasl-words.txt` already uses “license.”
- The stale checker currently passes.

The linked career frame also retains a paragraph saying these optional frames are unwritten, although the named files exist.

**Why it matters:** The lead could repeat completed edits or overlook the actual remaining reconciliation.

**Exact fix:**

- Change the Check set read’s prospective wording to past tense.
- Replace item 2’s “apply all seven” instruction with: “All seven note additions are present. Record this band’s completed comparison in L103 tracking.”
- Replace item 3 with: “The grades 6 to 8 seam and career frame’s library references are written. No seam-writing task remains here.”
- Delete item 5’s spelling request.
- In the linked career frame, replace “not written” with the current frame status and retain only the specific calendar reconciliation still outstanding.
- Leave dated review reports unchanged.

## Lens checklist at the frame layer

| Lens requirement | Result |
|---|---|
| Spaced instruction across every year | Met |
| Named priority skills with checks | Partly met: findings 1 and 2 |
| Single ownership and explained grade differences | Met |
| Explained differences from continuum placement | Met in notes |
| Library teaches lateral reading before social studies applies it | Met |
| Full inquiry cycles and named core tasks | Met in design |
| Stand-alone alternative when hosts are unavailable | Met |
| Source judgment requires leaving the page | Met |
| Copyright, fair use, permission and honest use | Met in content; finding 4 concerns instruction |
| Products shared with audiences | Met; scoring needs finding 1 |
| No required paid database, library access or account | Met |
| No copied AASL competency text or endorsement claim | Met |
| No unsupported claim of general score improvement | Met |
| Finished captures, swap notes and student-page wording | Not applicable at this layer |

## What is right and should be retained

Keep the four annual parts, two units per year, named handoffs, paper path, invented practice cases, interview alternative and adult-student consent rule. The different annual check weeks match the calendar. No check day falls in a core check week; some respond days do, which the high-school calendar permits.

The stand-alone tasks are legitimate fallbacks when a core project occurs later. Host timing alone is not a prerequisite failure here because the frame teaches the needed move itself. Shared-project use still requires teacher coordination.

Raw row counts do not justify adding sessions or moving standards between units. Unit 5’s two carry-forward rows in five sessions are not inherently underallocated.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Score existing publication and teaching records | Establishes the owned actions without another assessment day | Course frame |
| Carry progression additions into named sessions and checks | Makes the current contract operational | Course frame |
| Check grade 9 entry prerequisites | The predecessor course is optional | Course frame |
| Rehearse seminar turns and model the honesty review | Separates first instruction from independent evidence | Course frame |
| Bound cumulative checks and reuse revised products | Preserves depth within the period | Course frame |
| Keep the annual dose and current standard placement | No demonstrated need to change either | No scope change |
| Treat completed note edits as completed | Verified against current files | Course frame and lead tracking |

## What I could not judge

Finished source sets, rubrics, accommodations and exact lesson timings do not exist at this layer. Detailed partial-base lesson files were not inspected.

The Monroe continuum URL was inaccessible through the web tool, so I used the existing stored grades 9 to 12 document and the accessible official guide. Mark the [Monroe source](https://libguides.monroe.edu/ESIFC) **browser check**.

The web-literacy book’s contents and license opened, but two chapter pages returned 403. I did not fetch those pages another way.

No curriculum finding rests on model memory. A prior memory note was consulted only for report-format convention, which the current brief independently confirms.

## Outside sources

- [AASL learner framework, second edition](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf): checked owned competency actions.
- [Official continuum guide](https://slsa-nys.libguides.com/ifc/toc): checked the framework’s organization and priority-skill purpose; detailed comparison used the stored band document.
- [Lateral-reading study supplement](https://supp.apa.org/psycarticles/supplemental/edu0000740/EDU_2020_0630_Supplemental_Materials.pdf): read the sample instructional sequence and study context.
- [University study account](https://ed.stanford.edu/news/it-doesn-t-take-long-learn-how-spot-misinformation-online-stanford-study-finds): verified the reported six 50-minute lessons and population.
- [Lateral-reading teaching sequence](https://cor.inquirygroup.org/curriculum/collections/teaching-lateral-reading/): checked modeled external investigation and structured practice.
- [Partial-base license inventory](https://cor.inquirygroup.org/creative-commons/): checked item-specific adaptation distinctions.
- [Web-literacy book](https://pressbooks.pub/webliteracy/): checked contents and stated license only.
- [US Copyright Office fair-use explanation](https://www.copyright.gov/fair-use/more-info.html): checked the four-factor approach and its limits.

## For the source list

Record the study supplement as read in part, the accessible continuum guide address, and the web-literacy chapter access failures. Do not record the full study article or blocked chapters as read.

## For Cory

No new scope, audience, money or outside-person decision is required by these fixes. The existing partial-base download request remains before adaptation begins.

