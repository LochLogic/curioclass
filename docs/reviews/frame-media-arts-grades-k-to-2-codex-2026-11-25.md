# Independent frame read: Media Arts, grades K to 2

**Course:** `media-arts-grades-k-to-2`  
**Date:** 2026-11-25  
**Findings:** 7  
**Read-only review:** No files changed.

## Verdict

**Revise before scope writing.** The three-year structure is sound: every selected progression row appears once, each year owns its 18 IDs, and the full-path calendar adds up. The largest risk is assessment feasibility, especially the short path, which places unfinished assessment inside respond time and does not visibly reserve revision before scoring.

## What I read and checked

- The frame-read brief, the after-core provisions of frame-write, EXPERT.md, the arts lens, the arts adoption bar, and arts STANDARD.md and APPROACH.md.
- FOUNDATION.md, relevant production-path and baseline rules, and arts decisions and earlier arts reviews.
- The target frame in full; its course-list selector, progression rows, standards IDs and own-words lines, frames.csv entry, and calendar rows.
- Grade 3 progression handoffs and the adjacent media arts frame’s receiving seams; the cited kindergarten mathematics and grade 2 social studies units.
- Outside primary sources linked below.

**Checks:** `frame.py check media-arts-grades-k-to-2` passed with 0 failures; `stale.py check` passed with 0 failures across 121 files.

**Plan check:** The course-filtered `plan.py check` failed because the course has no `days.csv` with parts or items yet; review continued using the passing frame structural check.

## Findings, most serious first

### 1. The interview schedule does not provide credible time for individual evidence

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, combined media arts read S1 and the visual arts pilot  
**Confidence:** likely.

**Location:** “Scored evidence,” lines 94 to 103; units 1, 5 and 9; course-level check procedure, lines 272 to 274.

Six groups of five receive four minutes each. In units 1, 5 and 9, each child answers two talk items and performs a table task. That is 15 responses in 240 seconds, averaging **16 seconds per response**, before presenting stimuli, handling materials, transitions or recording judgments. Even the two-item checks allow only 24 seconds per response.

The frame supplies a waiting task, which is useful, but saying the teacher watches only the table does not remove responsibility for the other 25 children. The likely result is rushed evidence or missing individual marks.

**Exact fix:**

- Move safe-use and tool demonstrations into scheduled, rotating observations during the last making days. Keep an individual class-list mark.
- Limit each final interview day to **one oral item per child**. Where two oral items remain necessary, reserve two interview days within the unit’s existing allocation.
- Use a 40-minute interview-day budget of 5 minutes for setup, 24 for interviews, 5 for self-check, 4 for cleanup and 2 for transitions.
- Give waiting children a familiar paper task requiring no new instruction or device.
- Course-level checks sample rather than establish every owned action. Keep one oral sample per child and use the fresh paper task and explicitly unscored unit records for the remaining samples.

### 2. The four-session units do not preserve the promised assessment and response sequence

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the short-path and assessment-before-response problems identified in the arts pre-work reviews  
**Confidence:** firm.

**Location:** “The once-a-week path,” lines 30 to 40; “Day kinds,” lines 84 to 88; units 3, 4, 7, 8, 11 and 12.

The short path assigns four sessions to each third and fourth unit. Its four named stages are demonstration, making with critique, showing, and respond. The frame separately requires revision on the next day before scoring, but does not place it in that sequence.

For screening units, the two talk items move into the respond session’s first 20 minutes. The frame’s own interview arrangement takes **24 minutes**, and children whose talk evidence is collected then cannot start targeted response from those marks beforehand. This reintroduces a problem the arts approach’s fix pass expressly resolved.

**Exact fix:** Replace the `9, 11, 4, 4` short-path allocation with a concrete session plan that reserves revision and completes all assessment before respond. One workable allocation to develop is:

| Short-path component, each year | Sessions |
|---|---:|
| First unit | 6 |
| Second unit | 6 |
| Third unit | 6 |
| Final screening unit | 10 |
| Two course checks and their respond sessions | 4 |
| **Total** | **32** |

In the six-session units, combine demonstration and initial drafting in session 1; place the next making and critique in session 2, revision in session 3, necessary check components in sessions 4 and 5, and respond in session 6. The final unit has room for separate screening, two interview sessions and subsequent response.

Under that allocation, place short-path course checks in **weeks 13 and 21**, followed by respond sessions in weeks 14 and 22. Both check weeks avoid the current core check weeks in all three grades. Rewrite the short-path week claims and give it a separate check schedule; retain the full path’s existing dates. This allocation is an instructional judgment, not a tested result.

### 3. Several evidence descriptions omit actions required by their owned IDs

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, incomplete assessment coverage in the earlier arts reads; unit 9 was already identified in the combined media arts read  
**Confidence:** firm.

**Location:** Units 2, 6, 9, 10 and 12, lines 249, 253 and 256 to 259.

The following gaps remain when the evidence sentences are compared with the national statements. These are evidence corrections within existing ownership. [NCAS media arts performance standards, pages 4, 8 and 9](https://www.nationalartsstandards.org/sites/default/files/2021-11/Media%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf).

| Unit and ID | Problem | Exact fix |
|---|---|---|
| **2: MA:Pr5.1.Ka and Kb** | The screening observes skills but does not explicitly collect identification of those skills. | Add a brief naming or pointing response identifying the tool, cooperative or creative skill the child demonstrated. Record it alongside the observation. |
| **6: MA:Pr5.1.1b** | Two flip books demonstrate variation, but the evidence omits describing the creative technique. | Add a dictated or spoken line naming the technique varied and what changed. Keep it with the two versions. |
| **9: MA:Cn11.1.2a** | Naming a message and a location in daily or community life does not establish the cultural connection. | Add an individual explanation connecting a studied work to its cultural setting. Use the supplied work card, without asking children to disclose their own family’s culture. |
| **10: MA:Pr5.1.2a** | Naming a role and its skill does not demonstrate performing that role. | Score observed role enactment during production. Across the project, record each child’s artistic or design choices, tool use and collaboration. Keep the naming item as reflection. |
| **12: MA:Cn10.1.2b** | The item accepts what an experience meant **or** what it was for. | Replace “or” with “and”: collect both its meaning and purpose, using the same class-shared alternative. |

Place added observations and dictated lines during making or revision sessions so they do not worsen finding 1.

### 4. The kindergarten critique card omits the question step

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, arts pre-work finding 10 on an explicit critique protocol  
**Confidence:** firm.

**Location:** Models carried, line 238; unit 3, line 250.

“I notice, I like, I would change” is called the same routine as “describe, ask, suggest.” It contains no question. A writer following the child-facing card can therefore omit the required inquiry into the maker’s choice.

**Exact fix:** Replace the card with:

> I notice ___. Why did you choose ___? You could try ___ because ___.

Tie the suggestion to a unit look-for. Keep “what appeals to you?” as the separate response-assessment question. State that the teacher models this same three-step routine in units 1 and 2 before children use the card.

### 5. The year-end checks repeat the immediately preceding unit’s response task

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm against frame-write lesson 20.

**Location:** Year-end check rows, lines 266, 268 and 270.

The checks say the recent unit’s record is carried unscored, but also immediately reassess that unit through another unseen-work interpretation item:

- Kindergarten: unit 3’s `MA:Re9.1.K`.
- Grade 1: unit 7’s `MA:Re8.1.1`.
- Grade 2: unit 11’s `MA:Re8.1.2`.

A different stimulus does not make this a spaced sample of earlier learning. The frame-writing rule directs checks immediately after a unit to use earlier-unit items and carry the recent record.

**Exact fix:** Retain the recent unit records unscored and replace those fresh questions with earlier-unit samples:

| Year | Replacement sample |
|---|---|
| K | Unit 1: compare the experiences offered by a new picture and sound, `MA:Re7.1.Kb`. |
| 1 | Unit 5: explain a media connection between people in an invented or public example, `MA:Cn11.1.1a`. |
| 2 | Unit 9: describe how two new pieces shape different experiences, `MA:Re7.1.2b`. |

Apply finding 1’s one-oral-item limit when combining these with the remaining check tasks.

### 6. Named works and safety references lack the promised direct source links

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm.

**Location:** Works throughout the Units table; “Safety read,” lines 158 to 162.

The frame names archives, museums and domains, then repeatedly says a work will be “described and linked.” It supplies no direct work links. This falls short of frame-write lesson 23’s source requirement and leaves the next writer to locate the evidence behind dates, settings and descriptions.

**Exact fix:**

- Add a direct, freely readable source link beside every named work or series, supporting its identification and setting.
- Distinguish a contextual source from the item page used for its eventual rights check.
- Replace generic collection placeholders, especially the unit 3 kamishibai story set and unit 9 poster choices, with identified study selections and their item records.
- Turn the three safety-guide names into direct links to the specific guides.

For example, unit 9 can cite the [Library of Congress WPA collection record](https://www.loc.gov/item/2005682800/) and [Wendy Red Star’s own site](https://www.wendyredstar.com/). The flashing reference can link directly to [the explanation of success criterion 2.3.1](https://www.w3.org/TR/UNDERSTANDING-WCAG/seizure-does-not-violate.html). These links do not establish permission to reproduce every image.

### 7. Process notes describe completed checker work and an unresolved source search inaccurately

**Severity:** Minor  
**LAYER:** process, with a related standard-page correction  
**REPEAT:** yes, stale implementation notes in earlier arts reviews  
**Confidence:** firm.

**Locations and exact fixes:**

| Location | Correction |
|---|---|
| **For the lead, item 4** | Replace the claim that arts courses are grouped together with: **“frame.py already counts each after-core course separately through stagger_key; the lead’s remaining task is resolving the reported clashes.”** |
| **For the lead, item 3** | Add **library-and-research-skills-grade-2** to the current grade 2 week 27 conflicts. Retain the lead’s calendar-pass assignment. |
| **Days bullet and For the lead, item 2** | Replace the implied promise of a media arts figure in the elementary checklist with: **“No separate media arts weekly minimum was identified in the association’s elementary visual arts checklist or general PreK–12 visual and media arts program standards, checked 2026-11-25. This course provides 80 minutes weekly, or 40 on the short path; no numerical comparison is claimed.”** |
| **Arts STANDARD.md, section 3.4** | Separate the completed media arts source check from the still-pending middle school visual arts work. Do not transfer the elementary visual arts figure to media arts. |

The elementary document explicitly addresses visual arts; its 50-minute figure is not a verified separate media arts minimum. The general document’s scheduling section gives qualitative requirements without a numerical weekly figure. [Elementary checklist](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Elementary_Visual_Media_Arts_Program.pdf), [general program standards](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-PreK-12_Visual_Media_Arts_Programs.pdf).

## Coverage, days and seams

| Year | Units | Selected rows | Owned IDs | Unit sessions | Course checks and response | Total |
|---|---|---:|---:|---:|---:|---:|
| K | 1 to 4 | 8 | 18 | 60 | 4 | 64 |
| 1 | 5 to 8 | 8 | 18 | 60 | 4 | 64 |
| 2 | 9 to 12 | 8 | 18 | 60 | 4 | 64 |

All 24 selected skills appear exactly once. No wrong-year ownership was found. The eight grade 2 handoffs match grade 3’s receiving rows and units.

The full-path allocation of 18, 22, 10 and 10 sessions has a defensible instructional rationale. The longer opening units establish routines and production techniques; later units reuse material. The short-path allocation needs finding 2’s repair.

Calendar rows agree with the full-path unit ranges and checks in weeks 21 and 27. Neither check week overlaps a core check. Week 27’s after-core clashes belong to the lead’s shared calendar pass.

Cross-subject contacts have local teaching or fallback provisions. The mathematics citation matches kindergarten unit 1, days 1 to 18. The social studies contact is explicitly not a prerequisite.

There is no base text, so lesson-by-lesson source-map coverage is not applicable.

## Arts lens checklist

| Frame-level lens check | Result |
|---|---|
| Grade IDs placed in their own year | Met |
| Four artistic processes in every year | Met |
| Technique taught explicitly and grows harder | Met |
| Discipline words used in making and responding | Met in the design |
| Student choice and a showing in every unit | Met |
| Works span cultures and periods, including living makers | Met in the annual design; sourcing needs finding 6 |
| Critique followed by revision | Needs findings 2 and 4 |
| Performance, response, self-assessment and portfolio evidence | Present; feasibility and completeness need findings 1 to 3 |
| Ordinary room, setup, cleanup and supplies planned | Met as frame commitments |
| K to 8 course avoids daily periods | Met |
| Screens support physical making | Met |
| Five arts retain distinct disciplinary purposes | Met |
| Detailed day execution, access and safety | Not yet judgeable from the frame |

## What should be preserved

Preserve the three complete years, reciprocal progression seams, increasingly demanding techniques, portfolios, public or invented alternatives to personal disclosure, local storage, and consent protections.

Keep the paper path. The national introduction deliberately avoids prescribing particular technologies, so this read found no basis for requiring electronic devices throughout. [NCAS media arts introduction](https://www.nationalartsstandards.org/node/763).

I do not carry forward the earlier combined review’s suggestion that sharing a work with another arts discipline is itself a defect. A repeated work can support different disciplinary learning; duplicated teaching would require separate evidence.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Observe practical skills during planned production sessions | Collects the action without crowding interviews | Target frame |
| Limit each interview day to one oral item per child | Makes individual evidence more credible | Target frame |
| Develop the short path as 6, 6, 6 and 10 unit sessions, with separate check weeks | Preserves 32 sessions while reserving revision, assessment and response | Target frame and later scope |
| Expand evidence within existing ID ownership | Restores omitted actions without moving standards | Target frame |
| Restore “describe, ask, suggest” on the kindergarten card | Matches the approved critique routine | Target frame |
| Sample earlier units in year-end checks | Avoids immediate repetition of recent assessment | Target frame |
| Publish the bounded result of the weekly-time source check | Avoids borrowing a visual arts figure | Target frame and arts STANDARD.md |

## For Cory

- **Money:** The proposed $75 annual class supply ceiling remains a proposal. Current optional estimates are $35, $30 and $40 by year, with free alternatives retained.
- No new audience, outside-person or standards-ownership decision is needed for these corrections.

## Sources, confidence and limits

Outside sources were checked through web search and direct opening. No finding rests on model memory.

The frame’s detailed safety rules remain marked **“from memory”** pending its specified safety read. This review does not certify every artwork’s reuse rights, suitability of the eventual excerpts, or the final assessment items.

**For the source list:** Add the specific elementary and general opportunity-to-learn documents linked in finding 7, recording that the elementary numerical figure concerns visual arts and that no separate media arts weekly figure was identified in the two documents checked.