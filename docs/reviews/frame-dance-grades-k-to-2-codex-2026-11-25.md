# Independent frame review: Dance, grades K to 2

Date: 2026-11-25  
Course: `dance-grades-k-to-2`  
Read-only review. No files changed or report file created.

## Verdict

**Revise before writing the scope and sequence.** The band structure, ownership, unit order and annual totals are sound, but several owned standards lose required actions, and the participation alternatives can award performance marks without evidence of the child’s performance. Restore those actions and their evidence first, while preserving the existing units and allocations.

**Finding count: 6.**

This differs from the earlier combined dance review’s “light fix pass” verdict. That review expressly opened no outside standards pages; the live standards comparison below identifies substantive omissions that an id-count check cannot detect.

## What I read and checked

- The complete course frame, its `course-list.csv` selector and `frames.csv` entry.
- All 24 arts progression rows selected by `grade:K|1|2&strand:da`, and the eight receiving grade 3 rows.
- The relevant national dance standards and repository words-file lines.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts `STANDARD.md` and `APPROACH.md`, and the arts adoption bar.
- Applicable foundation, production-path, shared approach and decision guidance.
- The following dance frame’s seams, models and unit arrangements; relevant physical education and core-course unit contacts.
- The course’s calendar rows and other courses’ check weeks.
- Earlier arts pre-work and progression reviews, the visual arts K to 2 review and fixes, and `frame-dance-grades-k-to-12-2026-11-25.md`.

There is no preceding dance course. No base text is used, so a base-text source map is not applicable.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check dance-grades-k-to-2` | Failed because the plan-stage assessment files do not exist yet. Review continued. |
| `python -X utf8 scripts/frame.py check dance-grades-k-to-2` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures across 121 files.** Unmarked stale statements remain. |
| Independent ownership comparison | All 24 selected rows placed exactly once; all 63 owned ids placed exactly once, 21 per year. |
| Annual allocation | Each year has 60 unit sessions plus two check and two respond sessions: 64 total. |
| Calendar comparison | All six course checks avoid the corresponding core check weeks. |

The aggregate repository gate was not run because it writes result files and baselines, contrary to this review’s read-only restriction.

## Findings, most serious first

### 1. Seven owned standards lose required actions

**Severity:** Major  
**LAYER:** standard, propagated into progression and frame  
**REPEAT:** yes, incomplete own-words standards and assessment coverage recur in the earlier arts reviews.  
**Confidence:** firm.

**Location:** Frame units 1, 5 and 9, lines 266, 270 and 274; words-file lines 84, 87, 88, 90, 91, 122 and 128; corresponding elements and technique progression rows.

The frame’s instruction and evidence follow shortened descriptions that omit parts of the national standards. Naming every id therefore overstates coverage. The following corrections come from the [NCAS dance handout, PDF pages 4 to 6](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance%20-%20new%20copyright%20info_1.pdf).

**Exact fix:** Add each task below to both teaching and the named id’s scored evidence, within its present unit.

| Unit and id | Required addition |
|---|---|
| **1, DA:Pr4.1.Ka** | Children enlarge and shrink their shared circle, rather than only forming it. |
| **1, DA:Pr5.1.Kc** | Children retrieve a previously learned movement after the demonstration stops; immediate repetition alone is insufficient. |
| **5, DA:Pr4.1.1a** | Add straight travel and leaving, locating and returning to a marked position. |
| **5, DA:Pr4.1.1b** | Compare how long contrasting-speed movements take, alongside keeping the beat. |
| **9, DA:Pr4.1.2a** | Include changing orientation and examining how body-part positions relate within the shapes. |
| **9, DA:Pr4.1.2b** | Match the boundaries of a movement phrase to a musical grouping, beyond identifying its first strong beat. |
| **9, DA:Pr5.1.2c** | Observe an unprompted spacing correction as well as a correction requested by the teacher. |

Carry these additions into the corresponding progression notes and words-file summaries, retaining the latter’s 14-word limit. No id needs to move between units.

**Why it matters:** A writer can currently teach and assess exactly what the frame specifies while leaving these actions untaught. The omissions also weaken the preparation handed to grade 3.

### 2. Caller and drummer roles do not establish all the promised performance evidence

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, access and assessment equivalence were raised in the arts pre-work reviews; this particular role substitution is unresolved.  
**Confidence:** firm for the evidence gap.

**Location:** “Taking part without dancing alone,” lines 122 to 125; performance look-fors in units 1, 5 and 9.

The frame offers seated or one-limb movement, or a caller’s or drummer’s role, and says the child receives the same look-for marks. Calling a pattern or supplying its beat does not, by itself, show that child performing the specified body pattern, spatial relationship or movement adjustment.

The [national dance inclusion guidance](https://nationalartsstandards.org/sites/default/files/Dance_resources/Dance%20Inclusion%20Guidelines.pdf) supports individualized goals, accommodations and multiple ways to express learning. It does not make every participation role interchangeable evidence for every outcome.

**Exact fix:** Replace the blanket marking sentence with:

> Each unit names the child’s accessible movement version and the evidence it provides for each performance look-for. Caller and drummer roles remain valid participation choices, but establish only the outcomes directly demonstrated. Where a role supplies no evidence for an owned performance action, the teacher collects an accessible individual movement demonstration with the child’s usual supports and records the accommodation.

Add that evidence mapping to each unit’s assessment directions. Preserve the seated, supported, partner and live-observation options.

**Why it matters:** Otherwise, participation can be recorded as mastery of an action the teacher has not observed.

### 3. Whole-unit leave-outs lack replacement material for dependent units

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the arts pre-work reviews raised whether leave-outs leave the remaining course usable.  
**Confidence:** firm.

**Location:** “Leave-out,” lines 140 to 146; units 3, 4, 7, 8, 11 and 12.

The frame says each unit stands alone, but several later units require a particular dance produced earlier. Unit 7 changes unit 6’s remembered sequence, unit 8 builds its final dance from units 6 and 7, and the same dependency appears in the other years.

The existing ten-minute retrieval provision addresses earlier-year skills. It does not supply missing same-year dance material after a family or school omits a unit.

**Exact fix:** Add this rule to Leave-out and the affected unit rows:

> When an earlier unit was omitted, the receiving unit supplies a short Curio Class original phrase or a fresh, neutral starting point. Students learn or make that material before revising or staging it. The receiving unit assesses only its own ids; omitted-unit ids remain unclaimed.

Name the fallback explicitly:

- Units **3 and 7** receive a short original sequence to change.
- Unit **11** receives a short original phrase to revise.
- Units **4, 8 and 12** provide a fresh dance-making start that does not require the omitted work or sensitive subject.

**Why it matters:** A family exercising the settled leave-out choice should not discover that the next unit requires the work they omitted.

### 4. Unit 12’s question-and-movement task needs an explicit boundary

**Severity:** Moderate  
**LAYER:** frame, with a corresponding progression clarification  
**REPEAT:** yes, finding 5 of the earlier combined dance review.  
**Confidence:** likely.

**Location:** Unit 12, line 277; `da-g2-connect`; words-file line 233.

The unit declares hoop dance watch-only and prohibits imitation, but its assessment asks children to make movement from answers about that dance. Original abstract movement could respect that boundary, but the frame does not distinguish it from reproducing the observed movement.

The task also names only factual observation questions. The national id calls for inquiry leading to movement and explanation, rather than a factual quiz followed by a move. [NCAS dance handout, PDF page 10](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance%20-%20new%20copyright%20info_1.pdf).

**Exact fix:** Keep hoop dance for watch-and-talk cultural study. Use an age-suitable, nonceremonial excerpt of the already included Kpanlogo for the question-and-movement task, after the promised source and sensitivity check. Ask children what they notice, what an observed choice might suggest and what they still wonder; then have them create an original movement idea and explain its connection to one response.

Update the assessment, set-question cards and `da-g2-connect` accordingly. Do not require children to copy cultural steps.

The [University of Ghana’s account](https://ias.ug.edu.gh/content/dances) supports Kpanlogo’s Ga and Accra setting, but also describes adult expressive content. The chosen excerpt therefore needs checking; the form’s name alone does not establish suitability.

**Why it matters:** The next writer needs one clear task that preserves both the cultural boundary and the inquiry demand.

### 5. Kindergarten’s five-session final unit needs its actual merge stated

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** likely.

**Location:** Once-a-week path, lines 34 to 45; Day kinds, lines 95 to 96; unit 4, line 269.

The short path gives unit 4 five sessions. That can accommodate its demonstration, critique and revised rehearsal, two assessment sessions and respond session only if critique and revised rehearsal share a session. The general sequence instead places rehearsal of the change on the next day.

This is a missing timing instruction, not evidence that the entire 32-session path is impossible.

**Exact fix:** State this five-session map for unit 4:

| Session | Work |
|---|---|
| 1 | Study the works, demonstrate the technique and begin making the dance. |
| 2 | Continue making, give critique and rehearse the resulting change within this session. |
| 3 | Connecting assessment at the teacher’s spot. |
| 4 | Family or classroom showing and performance assessment. |
| 5 | Respond to the assessment. |

Add: “On this merged path, revised rehearsal follows critique within session 2; the next-day rehearsal statement describes the full path.”

**Why it matters:** Without that instruction, a scope writer must silently drop, combine or add a session.

### 6. Unmarked notes still describe completed work as unfinished

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, finding 1 of the earlier combined dance review and earlier arts stale-note findings.  
**Confidence:** firm.

**Exact fixes:**

| Location | Replacement or action |
|---|---|
| Frame line 229 | Replace “The grade 3 to 5 frame is not written yet” with: **“The grade 3 to 5 frame is written; its receiving units match the handoffs below.”** |
| Standard bullet, lines 53 to 55; units 1 and 9 | Remove the historical statements that the rows still omit body-part relationships, circling and turning, or requested adjustment. Those earlier corrections are present. Retain the new omissions identified in finding 1. |
| For the lead, item 2 | Delete the requested replacement for physical education’s pending cross-subject cell. That cell already contains the replacement. |
| For the lead, item 3 | Replace with: **“The five previously requested progression corrections are present. Additional standards-coverage corrections are identified in this independent review.”** |
| Physical education K to 2 frame, line 287 | Replace its statement that the dance frame is unwritten with a reference to the existing frame and connections table. |
| Arts row in `ADOPTION-BAR-SUBJECTS.md` | Replace the outstanding standards-gate and music-strand loading tasks with their completed status, already documented in arts `STANDARD.md`. |

**Why it matters:** These notes send the next worker back to completed tasks and conceal what actually remains. The dated earlier reports should remain unchanged as records.

## Lens checklist

Statuses judge the frame’s commitments, not unwritten lessons.

| Lens requirement or error check | Status |
|---|---|
| Correct grade ids in each band year | **Met.** 21 per year, no cross-year ownership. |
| All four artistic processes each year | **Met.** |
| Technique taught directly and increasing in difficulty | **Partly met.** Strong progression; finding 1 restores omitted actions. |
| Discipline words taught and used in making and response | **Met.** |
| Student choice, original work and showing in every unit | **Met.** |
| Describe, ask, suggest critique; revision afterward | **Partly met.** Present throughout; short-path timing needs finding 5. |
| Works from several regions and periods, including living makers | **Met as a frame commitment.** Specific selections and context still need unit-level verification. |
| Context includes maker, time, place and purpose | **Met as a unit-plan requirement.** |
| Assessment uses performance, response, guides, self-check and kept work | **Partly met.** Findings 1 and 2 concern validity of the evidence. |
| End-of-unit assessment is substantive arts work rather than vocabulary alone | **Met.** |
| Realistic session frequency, materials, free alternatives and room arrangements | **Met**, with finding 5’s timing clarification. |
| Performing happens with people; software supports the work | **Met.** |
| Dance remains distinct from physical education | **Met in the stated division.** Basic movement is used without assuming later PE dance units. |
| Five arts disciplines are not collapsed into one | **Met.** |
| No copied cornerstone tasks or coalition explanatory text | No such copying identified in the frame. |
| No compulsory solo performance | **Met.** |
| Setup, cleanup, hazards and controls named | **Met at frame level.** Detailed safety verification remains a later read. |
| “Respond day” distinguished from responding to art | **Met.** |
| Software does not judge finished work or performance | **Met.** |

Detailed daily equipment use, actual lesson timings and execution of access arrangements are **not yet applicable** because the lessons are unwritten.

## Calendar, allocation and seams

- **Full path:** K units total 20 + 14 + 14 + 12 = 60 sessions. Years 1 and 2 each total 18 + 14 + 14 + 14 = 60. The longer opening units have a reasonable routine-building and technique load.
- **Short path:** Unit allocations total 28 sessions per year, plus four course check and respond sessions. Check weeks calculate correctly: K weeks 18 and 26; years 1 and 2 weeks 17 and 25.
- **Core timing:** No core check overlaps were found. Counting and the story-retelling contact are suitable; symmetry is introduced through the dance task rather than assumed from grade 4 mathematics.
- **Seams:** All eight grade 2 handoffs match the receiving grade 3 rows and units. The next band provides a fallback for students who did not take this optional course.
- **After-core clashes:** The existing list is accurate: K week 18 overlaps ELD, PE and visual arts; K week 26 overlaps SEL and visual arts; grade 1 weeks 17 and 25 overlap music; grade 2 week 17 overlaps ELD, music, PE, theater and visual arts, and week 25 overlaps music. These remain for the lead’s cross-course calendar pass, as the after-core brief directs.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Keep all 12 units and existing id ownership | The structural placement and unit reasons hold. | Course frame |
| Add the seven missing actions inside their existing units | Restores the owned standards without moving scope. | Frame, progression notes, words file |
| Keep participation roles, but map evidence by outcome | Participation and demonstrated performance need distinct records. | Frame and later assessment directions |
| Supply neutral replacement phrases after leave-outs | Keeps receiving units usable without claiming omitted ids. | Frame and later unit plans |
| Keep hoop dance watch-and-talk; clarify the separate inquiry task | Gives the writer an explicit cultural boundary. | Unit 12 and connecting notes |
| Merge critique and revised rehearsal in short-path unit 4, session 2 | Preserves five sessions and both assessment sessions. | Frame |

## What is right and should not be touched

Preserve the annual band-year structure, four recurring threads of units, increasing technique demands, all four artistic processes, individual id evidence labels, live teacher judgment, portfolio growth record, no-forced-solo provision, free paper path and explicit cultural setting. The check and respond allocations add up, and the course checks avoid core check weeks.

## What I could not judge

This review does not establish the suitability, permissions or accuracy of every proposed work card, recording or cultural description. It also does not certify safety or establish that one teacher can collect the proposed evidence from 30 children in practice.

No finding relies on personal memory. The frame’s footwear and other safety prescriptions remain explicitly **from memory** pending their promised source-based safety read.

## Sources

- [NCAS dance performance standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance%20-%20new%20copyright%20info_1.pdf): checked the owned actions against teaching and evidence.
- [NCAS dance introduction](https://www.nationalartsstandards.org/content/dance-introduction): checked the relationship among artistic processes and performance outcomes.
- [Dance inclusion guidelines](https://nationalartsstandards.org/sites/default/files/Dance_resources/Dance%20Inclusion%20Guidelines.pdf): checked the basis for individualized access and evidence.
- [Dance opportunity-to-learn standards, 2017 revision](https://nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf): verified the published K to 2 weekly figures of 60 minutes basic and 90 minutes quality. The frame correctly states its 80-minute full path and 40-minute short path gaps.
- [University of Ghana, dance repertoire](https://ias.ug.edu.gh/content/dances): checked Kpanlogo’s setting and the need to select a suitable excerpt.

**For the source list:** Add or cross-reference the inclusion guidance and University of Ghana page if absent. The latter supplies cultural context, not blanket permission or age suitability.

## For Cory

- The existing optional filming proposal remains a people and money decision; this review does not require filmed materials.
- The proposed supplies ceiling of $50 per class per year remains a money decision. Preserve the free alternatives.

No new course-scope or audience decision is needed for these fixes.