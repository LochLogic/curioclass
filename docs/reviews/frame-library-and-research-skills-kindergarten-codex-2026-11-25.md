# Independent cold read: kindergarten library course frame

**Date:** November 25, 2026  
**Course:** `library-and-research-skills-kindergarten`  
**Finding count:** 3  
**Delivery:** Complete report here. No files changed.

## Verdict

The frame has a sound sequence, complete placement of its seven progression skills, and a defensible kindergarten interpretation of its owned standard, but it needs revision before the scope and sequence copies its allocations. The largest risk is assessment administration that exceeds the course’s own usable session time and consumes time reserved for response. Fix that allocation, make Unit 2’s complete inquiry cycle concrete, and remove the stale gate limitation.

## What I read and checked

- The complete course frame, its `course-list.csv` selector, its `frames.csv` row and its calendar rows.
- `frame-read.md`, the relevant frame-writing instructions, EXPERT, the library lens, library STANDARD and APPROACH, and the library adoption bar.
- FOUNDATION, relevant production-path and BASELINE provisions, the shared approach, source-access guidance and relevant library decisions.
- All seven kindergarten library progression rows, the receiving grade 1 rows, the later owners of carried standards, and the standards registry and own-words phrases.
- The kindergarten Units tables for ELA, science and social studies, checked against `calendar.csv`.
- Earlier library pre-work, progression and fix reports, plus relevant earlier frame findings concerning assessment time and stale notes.
- The stored continuum file named in the frame, including its kindergarten column and priority-skill boxes, read directly from the document’s tables.
- The outside sources linked below.

Kindergarten has no preceding course. The grade 1 library frame does not yet exist, so the outgoing seam was checked against the progression rather than a neighboring frame.

| Required check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check library-and-research-skills-kindergarten` | One failure: the plan stage needs lesson-plan CSVs that do not yet exist. The command was course-filtered under the repository rule. |
| `python -X utf8 scripts/frame.py check library-and-research-skills-kindergarten` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 70 files checked, 0 failures |

The unavailable lesson-plan layer does not withhold this frame verdict. The aggregate gate was not run because it writes output and baseline files.

## Findings, most serious first

### 1. The assessment schedule exceeds the usable session

**Severity:** High  
**LAYER:** frame  
**REPEAT:** yes, assessment overload and missing operational minutes recur in `frame-unit-lessons-2026-11-16.md`, lessons 3 and 5.  
**Confidence:** firm

**Location:** [Days and Evidence](/S:/CurioClass/docs/courses/library-and-research-skills-kindergarten/frame.md:11), the unit assessment descriptions, and [the mid-year check](/S:/CurioClass/docs/courses/library-and-research-skills-kindergarten/frame.md:123).

**Problem:** The frame budgets about three minutes at each end of a 25-minute session, leaving 19 minutes. Its assessment method takes about four minutes per group of four.

- Twenty-four children require six groups and 24 assessment minutes.
- The class of 30 used in the supplies estimate requires eight groups and 32 minutes.
- Four groups, at most 16 children, take 16 minutes and leave three usable minutes for transitions and variation.

The claim that 24 children fit in one session is therefore incorrect. For 30 children, spilling the remaining 13 assessment minutes into the mid-year respond session leaves only six usable minutes for regrouping, reteaching and a fresh try. The same blanket administration rule also overfills the single end-of-unit assessment sessions.

**Why it matters:** A writer following these allocations must rush individual evidence, omit children or spend the protected response time finishing assessment.

**Exact fix:**

1. Give the mid-year check two sessions, in weeks 12 and 13, followed by its respond session in week 14. Take the additional session from Unit 1: use six sessions consisting of show-me, practice, inquiry, inquiry, assessment and respond. Introduce the pictured cycle with the initial wonder model.
2. Update Unit 1 to days 1 to 6 and Unit 2 to days 7 to 11. Units 3 and 4 retain their current positions. The course remains 30 sessions: **23 unit sessions, four course-level check sessions and three respond sessions**.
3. Replace the blanket promise that an entire class fits into one unit assessment session. Name two observation windows where necessary, after practice: one during inquiry and one on the assessment day, with no more than four four-minute groups in either window. Preserve the inquiry product, sharing and reflection through the other pupils’ independent tasks.
4. Require each unit plan to demonstrate its complete 19-minute administration budget. Remove permission for unplanned assessment overflow into the respond session.

The lead should regenerate the calendar after applying the allocation.

### 2. Unit 2 does not specify the complete inquiry it promises

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** likely

**Location:** [Unit 2, What students learn](/S:/CurioClass/docs/courses/library-and-research-skills-kindergarten/frame.md:115).

**Problem:** The course brief and library APPROACH require a complete inquiry cycle and a shared product in every unit. Unit 2’s concrete inquiry task is to fetch a fact book and share it. Its stand-alone question asks which bin holds a rain book. Neither instruction requires children to obtain information from that book or make a product showing what they learned.

The course-wide drawing and reflection promises help, but the unit’s explicit five-session outline leaves the writer to invent the missing research task. The [continuum’s inquiry guidance](https://slsa-nys.libguides.com/ifc/intro) connects investigation to constructing and communicating new understanding.

**Why it matters:** Unit 2 can become an orientation and retrieval exercise while being counted as a complete research cycle.

**Exact fix:** Retain book care, labels and sorting as the unit’s priority skills. Replace its inquiry description with:

> For the host’s weather question, or the stand-alone question “What happens when rain falls?”, children find the labeled bin and select a fact book with help. The teacher reads a short passage from the rain book. Children identify a picture or fact that helps answer the question, draw that fact, share it with a partner and complete the pictured reflection. “Which bin holds the rain book?” is the find-step prompt within this inquiry.

Keep the independent unit assessment focused on fetching and classifying a book. The supported inquiry contribution does not transfer ownership of later-grade standards.

### 3. The fortnightly-session gate warning is stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale implementation notes recur in earlier frame reads, including the kindergarten science rerun.  
**Confidence:** firm

**Location:** [For the lead, item 2](/S:/CurioClass/docs/courses/library-and-research-skills-kindergarten/frame.md:174).

**Problem:** The note says `frame.py` cannot read “about one session every two weeks” and asks the lead to resolve that limitation before writing the band frames. Current [parser code](/S:/CurioClass/scripts/frame.py:245) already recognizes fortnightly wording and assigns `per_week = 0.5`.

**Why it matters:** The note presents completed implementation as outstanding work and encourages an unnecessary wording workaround.

**Exact fix:** Replace item 2 with:

> **The band courses’ time and the gate.** `frame.py` recognizes “about one session every two weeks” as 0.5 sessions a week. Use the subject page’s true dose. The band frames need the brief’s Year column and 18 sessions per year: 54 across grades 6 to 8 and 72 across grades 9 to 12.

The stale checker’s clean result does not settle this unmarked factual note.

## Coverage, order and calendar

| Requirement | Result |
|---|---|
| Owned skills | All seven kindergarten rows appear exactly once in Skills. |
| Owned standard | AASL.V.C.1 is taught and checked through expressing a question about the topic. This fits the [second-edition learner framework](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf). |
| Carried standards | Nine distinct carried ids are explained with their later owners. No unsupported ownership transfer found. |
| Unit order | Wonder and cycle, book location, answering information, then collaborative sharing and crediting form a coherent sequence. |
| Current totals | 7 + 5 + 5 + 7 = 24 unit sessions; three check and three respond sessions bring the total to 30. Finding 1 concerns administration capacity. |
| Current calendar | Matches the frame. Checks in week 13 and weeks 27 to 28 avoid core checks in weeks 14 to 17 and 29 to 32. |
| Cross-subject timing | Named units and course-day ranges agree with the calendar. Later or overlapping hosts have explicit independent alternatives. |
| Outgoing seam | All eight outgoing links from the seven kindergarten rows are reciprocated in grade 1 `assumes`. |
| Base text | None. A source map is not applicable. |
| Band Year column | Not applicable to this single-grade course. |

## Library lens checklist

| Lens requirement | Judgment |
|---|---|
| Spaced instruction across the year | Met |
| Named grade priority skills and checks | Met in design; assessment capacity needs finding 1’s repair |
| Complete inquiry cycle | Explicit in Units 1, 3 and 4; Unit 2 needs finding 2 |
| Named host tasks from other courses | Met, with stand-alone alternatives |
| Questions leading to finding information | Met |
| Honest use at kindergarten depth | Met through maker credit and distinguishing found information from one’s own ideas |
| Product, audience and reflection | Explicit in Units 1, 3 and 4; incomplete in Unit 2 |
| No duplicate ownership at the same depth | Met |
| Later-grade work introduced with a reason | Met through supported, pictured contributions |
| Lateral reading ownership and website-checklist risk | Not applicable to kindergarten’s closed, adult-read sources |
| Free access and no assumed library or device | Met |

## What is right and should be preserved

Preserve the spoken and pictured entry points, the meaningful sequence, the standalone paper path, the non-shaming treatment of borrowing and credit, and the explicit fallbacks when another course’s task arrives later. The distinction between owning an id and contributing to it with help is particularly useful.

The direct continuum comparison supports the frame’s account of the kindergarten skills. Its proposed difference notes make the choices about alphabetical shelving and online privacy visible rather than silently claiming identical placement.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Keep four units, the current skill placements and the 30-session total | Coverage and sequence hold | Course frame |
| Move one Unit 1 session to the mid-year check | Provides two check windows before the core cluster and protects response | Course frame; regenerated calendar |
| Make rain information the Unit 2 inquiry product | Completes the existing inquiry requirement without changing ownership | Course frame, Unit 2 |
| Replace the fortnightly-parser warning | Current code already handles the dose | Course frame, For the lead |

These are recommendations for the caller to apply. Nothing was edited.

## For Cory

None arising from these findings. No change of audience, spending or outside-person requirement is needed.

## What I could not judge

The absent grade 1 frame prevents a frame-to-frame seam comparison. The actual read-alouds, assessment cases, accommodations and classroom administration times remain later-stage work.

## Sources and evidence limits

- [AASL learner framework, second edition](https://standards.aasl.org/wp-content/uploads/2026/07/250918-AASL-framework-for-learners.pdf): checked the owned competency and the meanings of carried contributions.
- [AASL second-edition explanation](https://standards.aasl.org/2edition/): confirmed the edition and continuing framework structure.
- [School Library Systems Association inquiry introduction](https://slsa-nys.libguides.com/ifc/intro): checked the relationship between inquiry, new understanding and communication.
- [Continuum contents and grade-band organization](https://slsa-nys.libguides.com/ifc/toc): checked the distinction between the full continuum and priority-skill summaries.
- The stored `esifc-priority-pk-2.docx` named by the frame: directly checked kindergarten cells and priority boxes. No reference wording or tasks were copied.

The [Monroe continuum address](https://libguides.monroe.edu/ESIFC) was inaccessible through the web tool, status **browser check**. The alternative association source opened; the grade-specific comparison used the existing local document.

No curricular finding rests on memory. Prior-run memory informed report organization only.

**For the source list:** The association’s [continuum guide](https://slsa-nys.libguides.com/ifc) is an accessible alternative entry point.

