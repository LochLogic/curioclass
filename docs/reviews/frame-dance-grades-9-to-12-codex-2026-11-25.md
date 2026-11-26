# Second independent frame read: Dance, grades 9 to 12

**Date:** 2026-11-26  
**Course:** `dance-grades-9-to-12`  
**Verdict:** Revise before scope and sequence writing. The level structure, ownership counts and calendar are sound, but several assessment descriptions permit incomplete standards coverage, and the room specification does not safely support the planned movement. The most important change is to complete the teaching and evidence requirements inside the existing owning units.

**Findings:** 10. No files changed.

## What I read and checked

- The complete course frame, its `frames.csv` record, course-list selector and 35 calendar rows.
- All 28 selected dance progression rows: eight each for Levels 1 to 3 and four for Level 4, together with the corresponding standards IDs and action summaries.
- The arts lens, adoption bar, `STANDARD.md`, `APPROACH.md`, shared foundation and approach requirements, relevant frame-writing rules and recorded arts decisions.
- The preceding dance frame’s grade 8 units and handoffs, plus the cited PE and health connections. There is no subsequent dance course.
- Earlier dance and arts reviews to identify repeated findings.
- Outside standards, safety guidance and selected work records linked below.

There is no base text or source map to audit.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check dance-grades-9-to-12` | One failure: later-stage plan data is absent; this does not block the frame read. |
| `python -X utf8 scripts/frame.py check dance-grades-9-to-12` | **0 failures.** |
| `python -X utf8 scripts/stale.py check` | **0 failures**, although manual reading found stale prose. |

Independent counting confirms 63 distinct owned IDs, 21 per owning level, with every selected progression row placed once. Each level’s calendar covers school days 1 to 160 exactly once.

## Findings, most serious first

### 1. The floor specification does not support the required jumps and floor work

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, the preceding independent dance read identifies the same floor-control problem.  
**Confidence:** firm.

**Location:** “The ordinary room,” lines 172 to 179; “Safety read,” lines 201 to 215; unit 7 and units inheriting its controls.

A cleared classroom, an arm-span spacing rule and a clean surface do not establish suitability for jumps, leaps, rolls and slides. The frame requires these activities without distinguishing resilient flooring from tile or flooring laid over concrete.

The dance association’s guidance specifies resilient flooring and warns against hard underlying surfaces. Nova Scotia’s guidance also requires safe footing and movement taught in progression. [Dance opportunity-to-learn guidance, printed pages 8 to 9](https://www.nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf), [Nova Scotia safety guidance, PDF page 55, printed page 43](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical_Education_Safety_Guidelines.pdf).

**Why it matters:** A teacher following the present instructions could conduct repeated impact work on an unsuitable classroom floor.

**Exact fix:** Add a course-wide surface check, repeated in unit 7’s controls:

> Before jumps, leaps, rolls or slides, the teacher confirms that the surface and underlying construction are suitable for that activity. Concrete, tile and flooring over those surfaces are not the impact-work path. On an unsuitable surface, use low-impact standing or seated work and defer the affected practical assessment until suitable space is available.

Specify traveling lanes and rotating groups where the room cannot accommodate simultaneous movement. Do not mark an aerial-performance requirement met from a written substitute. Refer any resulting space or resource limitation to Cory.

### 2. Several owned standards have narrower teaching or evidence than their full actions

**Severity:** Major  
**LAYER:** frame, with related progression and standard-summary corrections  
**REPEAT:** yes, incomplete standards and assessment evidence recur in earlier arts reads.  
**Confidence:** firm.

**Location:** Units 2, 5, 7, 8, 12, 14 and 15, lines 325 to 338.

The frame improves substantially on the short action summaries, but some final look-fors still permit “met” without the complete action.

**Exact fixes:** Make these additions within the present owning units.

| Unit and ID | Problem and exact correction |
|---|---|
| **2: `DA:Pr4.1.Ia`, `Ib`** | The balance look-for omits intentional transitions and changing relationships; the rhythm look-for omits breath phrasing. Add these to the performed phrase and scoring guide. [Proficient elements](https://www2.cde.ca.gov/cacs/id/web/30262). |
| **2: `DA:Pr5.1.Ia`, `Ic`** | Recall, spacing and timing alone understate technical control. Name alignment, coordination, balance, support and weight transfer in observation. Require the rehearsal record to show implementation and multiple strategies applied to self and peers. [Proficient technique and rehearsal](https://www2.cde.ca.gov/cacs/id/web/30275). |
| **7: `DA:Pr5.1.IIb`, `IIc`** | Anatomy notes and rehearsal plans do not establish practical application and execution. Add live evidence of anatomical principles applied and independent and collaborative rehearsals carried out, followed by reflection. Keep the invented dancer for food tasks. [Accomplished technique and rehearsal](https://www2.cde.ca.gov/cacs/id/web/30276). |
| **8: `DA:Cr1.1.IIb`, `DA:Cr2.1.IIb`** | Written comparisons and movement selections need performed evidence. Score the blended movement vocabulary and demonstrated choices supporting the aesthetic statement. |
| **12: `DA:Pr4.1.IIIa` to `IIIc`** | Add changing dancer relationships, phrasing both with and without accompaniment, movement with and against its rhythm, and dynamic relationships among dancers. |
| **12: `DA:Pr5.1.IIIa`** | One piece and written self-evaluation do not secure varied genres or analysis with others. Collect practical evidence across contrasting styles and a peer discussion of performance ability. [Advanced technique](https://www2.cde.ca.gov/cacs/id/web/30277). |
| **14: `DA:Cr3.1.IIIa`** | The revision record must also show artistic criteria examined and refined, with reasons. |

The three creating and elements corrections immediately above follow the [national dance standards, PDF pages 1 to 5](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance.pdf).

Two connecting corrections are also required:

- **Unit 5, `DA:Cn10.1.Ib`:** Replace comparison with another team’s process as the sole process comparison. Require oral and written comparison between choreography and another creative, academic or scientific procedure, plus discussion of new understanding. [Proficient connecting](https://www2.cde.ca.gov/cacs/id/web/30340).
- **Unit 15, `DA:Cn11.1.IIIa`:** Add movement characteristics and artistic criteria beside technique, and explain how the analysis expanded dance literacy. General personal growth is insufficient. Carry the correction into unit 19’s reassessment. [Advanced historical and cultural connecting](https://www2.cde.ca.gov/cacs/id/web/30355).

**Why it matters:** A scope writer could faithfully implement the frame and still teach or assess less than the course claims.

Update the corresponding progression notes and short action summaries wherever they preserve these narrower demands. Keep all ownership in its current unit.

### 3. Level 4 cannot provide the general Advanced recovery route promised

**Severity:** Major  
**LAYER:** frame and progression  
**REPEAT:** yes, incomplete Level 4 reassessment recurs in the independent high school arts reads.  
**Confidence:** firm.

**Location:** Standard bullet, lines 50 to 52; units 16 to 19; the four `da-g12-*` rows.

The frame tells a student ending Level 3 at “partly” on an ID that Level 4 offers a route to reach it. Level 4 explicitly reassesses only **11 of the 21 Advanced IDs**.

The ten omitted IDs are:

`DA:Cr1.1.IIIb`, `DA:Cr2.1.IIIb`, `DA:Cr3.1.IIIb`, `DA:Pr4.1.IIIb`, `DA:Pr4.1.IIIc`, `DA:Pr5.1.IIIb`, `DA:Pr5.1.IIIc`, `DA:Pr6.1.IIIb`, `DA:Re7.1.IIIb`, `DA:Cn10.1.IIIb`.

**Why it matters:** Students and teachers could expect recovery of an unmet requirement that the year never explicitly assesses.

**Exact fix:** Replace the blanket assurance with:

> Level 4 reassesses the 11 Advanced IDs listed in its units. An unmet Advanced ID is completed only when new evidence demonstrates its full action; enrollment or completion of Level 4 does not establish this.

Send Cory the scope choice between retaining that limited promise and adding a recovery route for all ten omitted IDs. If expanded, place creating recovery in unit 16, responding in 17, performing in 18 and the career capstone in 19, with matching `~` references and evidence.

### 4. The PE boundary excludes technique the dance course itself requires

**Severity:** Major  
**LAYER:** frame and standard  
**REPEAT:** yes, the combined dance review identifies the unresolved PE boundary.  
**Confidence:** firm on the contradiction; the policy resolution belongs to Cory.

**Location:** Lines 73 to 77 and 374; arts `STANDARD.md` section 6; PE grade 9 unit 5.

The frame says dance teaches “no motor cue.” Yet its own units teach balances, alignment, safe landings, rolls, slides and technical execution. The owned technique standard requires bodily skill, while the cited PE unit occurs later, in weeks 22 to 26. [Proficient dance technique](https://www2.cde.ca.gov/cacs/id/web/30275).

The connection also understates actual overlap: PE unit 5 includes an original phrase, stated idea, motif and transition, connecting directly to dance unit 3.

**Why it matters:** A writer must either omit necessary instruction or contradict the stated boundary.

**Exact fix:** Ask Cory to reconcile the shared rule. Recommended replacement:

> Dance teaches the movement technique required for its owned artistic performance standards. PE develops movement competence, fitness and teamwork in its own contexts. Each connection names shared prior practice and the different purpose of its use here.

After that decision, replace both “no motor cue” statements, add PE unit 5 to dance unit 3’s connections, and reconcile PE’s intent and motif wording. Do not silently remove dance technique.

### 5. Course-level checks sometimes claim actions their tasks cannot demonstrate, and Level 4 repeats scored work

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, assessment validity and duplicate Level 4 checkpoints recur in earlier arts reads.  
**Confidence:** firm.

**Location:** Course-level checks, lines 349 to 359; unit 16.

Examples include an artist’s statement about someone else’s unseen dance labeled as the student’s creating standard, analysis of an unseen composition labeled as designing dances, and evaluation of a described dancer labeled as self-evaluation.

Separately, unit 16 scores the series and revision record at its end. The next day’s course checkpoint collects the same work against the same three IDs, contradicting “no piece is scored twice.”

**Why it matters:** The record overstates what a written sample demonstrates and adds redundant assessment.

**Exact fix:**

- Retain unseen analysis tasks as samples of analysis or interpretation. Remove claims that they independently demonstrate choreography, embodied technique or self-evaluation.
- Carry the corresponding practical evidence unscored from the owning units, as the frame already does elsewhere.
- For Level 3 self-evaluation, use the student’s own earlier performance evidence rather than a described dancer.
- Make days 71 and 72 the single end-of-unit assessment and response for unit 16’s series. Treat the final days within its 70-day allocation as rehearsal and preparation, without a second score.

The last correction keeps the existing 160-day calendar.

### 6. Whole-unit leave-outs do not preserve the claimed independence of later units

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the preceding independent dance read identifies the same dependency problem.  
**Confidence:** firm.

**Location:** Leave-out bullet, lines 166 to 171; units 4, 5, 9, 10, 14 and 16 to 19.

“Each unit stands alone” conflicts with explicit dependencies. Unit 4 revises unit 3’s dance; unit 10 presents work refined in unit 9, which is specifically named as removable; units 17 to 19 depend on unit 16’s series.

**Why it matters:** Omitting a permitted unit can leave the next teacher without the work its tasks require.

**Exact fix:** Add a fallback to each dependent unit:

- Provide an original practice dance and process record when an earlier making or revision unit was omitted.
- In unit 10, allow the unit 8 dance with a short, counted revision and rehearsal sequence.
- For units 17 to 19, identify an existing student series or an original supplied practice series for the relevant tasks.
- Retrieve or teach missing vocabulary and routines before use.

State that supplied work supports the later unit’s requirements and does not recover omitted creating IDs. Retain the notice identifying unclaimed IDs.

### 7. Firm selections lack source links, and two range statements need correction

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, missing links recur in earlier independent dance reads; the repeated Annabelle selection was identified in the combined dance review.  
**Confidence:** firm.

**Location:** Base text bullet; Units table; Safety read; For the lead item 9.

The frame contains **no external URLs**, despite repeatedly saying works are “described and linked.” The frame-writing brief requires free sources for anchors and links for safety guides.

Two specific corrections are supported:

- Unit 16 labels *The Statement* “Canada, 2016.” Its world premiere was in The Hague, and it was created for the Dutch company’s dancers. Identify the Canadian choreographer separately from the work’s production setting. [Original company’s work record](https://www.ndt.nl/en/explore/works/the-statement/).
- The “none repeats” claim overlooks *Annabelle Serpentine Dance*, already named in kindergarten. Whitford and Moore are names associated with the same performer. [Film catalog record](https://catalog.afi.com/Film/28950-SERPENTINE-DANCE--ANNABELLE?cxt=filmography).

**Why it matters:** Writers must repeat source discovery, and the stated cultural range is less precise than it appears.

**Exact fix:** Attach a direct institutional source link to every fixed work and both safety guides. Identify the exact serpentine film used in unit 10. Retain the bridge film as deliberate review, explain its harder high school purpose, standardize the performer’s name, and remove the absolute nonrepetition claim. Correct unit 16 to distinguish the maker’s origin from the production’s setting.

Keep item-level rights checks at unit-plan stage.

### 8. Ten-minute retrieval does not fit inside a seven-minute warm-up

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the same timing conflict appears in the preceding independent dance reads.  
**Confidence:** firm on the conflict; allocation is an item-level judgment.

**Location:** Days bullet, lines 20 to 23; Readiness and retrieval, lines 140 to 150; unit retrieval instructions.

The frame allocates seven minutes to warm-up but repeatedly places a ten-minute retrieval task inside it, sometimes with an additional ten-minute reteach.

**Why it matters:** Teachers must overrun or remove movement preparation or instruction.

**Exact fix:** Replace “inside day 2’s warm-up” with a separate day 2 block:

| Component | Minutes |
|---|---:|
| Setup | 3 |
| Warm-up | 7 |
| Combined retrieval | 10 |
| Teaching, including integrated reteaching when needed | 18 |
| Cool-down and closing evidence | 4 |
| Reset | 3 |
| **Total** | **45** |

State that retrieval combines the unit’s assumed threads, and its reteach replaces part of teaching rather than adding time. Carry the allocation into the short path.

### 9. Adult students’ leave-out choices are not stated

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the independent visual arts high school read identifies the same omission.  
**Confidence:** firm.

**Location:** Leave-out bullet, lines 166 to 171; Grade 12 calendar.

The frame correctly gives adult students control over showing and recording consent, but assigns leave-out decisions only to a school or family. The supplied repository rule explicitly covers adult students’ leave-out choices.

**Why it matters:** The frame gives different decision rights depending on which paragraph a teacher follows.

**Exact fix:** Add to Leave-out:

> A student aged 18 or older receives the family note directly and makes their own leave-out and consent choices; the school’s rules still apply.

Carry that rule into relevant family notes.

### 10. Unmarked stale instructions remain despite the passing stale check

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, the combined dance review and preceding independent read identify these same stale notes.  
**Confidence:** firm.

**Exact fixes:**

| Location | Replacement or action |
|---|---|
| Frame, For the lead item 6 | Delete the request to replace PE’s pending connection. PE’s Cross-subject table already contains that replacement. |
| Grade 8 responding seam, line 258 | Replace “time-stamped evidence” with “time-stamped or moment-named evidence,” matching the current progression. |
| Arts row of `ADOPTION-BAR-SUBJECTS.md`, line 568 | Replace the outstanding standards-gate and music-loading tasks with a statement of completion, consistent with arts `STANDARD.md`. Shared-file change belongs to the lead. |

**Why it matters:** These instructions send later workers back to completed tasks. Preserve dated reviews as historical records.

## Calendar, allocation and seams

| Level | Unit days | Checks and responses | Total | Check days within its year |
|---|---:|---:|---:|---|
| 1 | 156 | 4 | 160 | 85 and 159 |
| 2 | 156 | 4 | 160 | 81 and 159 |
| 3 | 156 | 4 | 160 | 81 and 159 |
| 4 | 156 | 4 | 160 | 71 and 137 |

The calendar agrees with the frame. Level 1’s mid-year response correctly falls on day 86 in week 18. Week 32 year-end checks are permitted by the high school calendar rule.

All three short paths total 76 unit days plus four check and respond days. The bridge uses 7.5 percent of either path. No arithmetic correction is needed.

The longer technique and revision units have reasonable stated reasons. There is insufficient day-level evidence to establish whether the compressed paths provide enough practice for the proposed depth.

The grade 8 handoffs match the receiving Level 1 threads, and the bridge explicitly supports students without prior dance. Models generally precede their use. PE arrives after dance’s first technical unit, making finding 4 consequential. Health and ELA connections have explicit fallbacks, so they need not delay dance.

## Lens checklist

| Frame-layer lens requirement | Status |
|---|---|
| Standards placed by level rather than student grade | Met |
| Four artistic processes in each year | Met in design |
| Direct technique instruction that becomes harder | Partly met: findings 2 and 4 |
| Discipline vocabulary used in making and response | Met in design |
| Student choice and a showing in every unit | Met |
| Describe, ask, suggest critique followed by revision | Met in design |
| Multiple cultures, periods and living makers each year | Met in selection; source precision needs finding 7 |
| Growth, kept work, self-assessment and scoring guides | Partly met: findings 2, 3 and 5 |
| Real schedules and shorter paths | Counts met; opening timing needs finding 8 |
| Equipment and safe use of space | Missed: finding 1 |
| Performing happens with people in the room | Met |
| Alternatives to compulsory solo performance | Met in design; retain each ID’s practical action |
| Dance and PE responsibilities distinguished accurately | Missed: finding 4 |
| Artistic responding distinguished from respond days | Met |
| No adaptation of protected cornerstone tasks | No adaptation identified |
| Finished day-level demonstrations, samples and access adaptations | Not applicable yet; assess at later stages |

## Settled by the expert

These are recommendations for the fixer, not edits made during this read.

| Choice | Reason | File touched |
|---|---|---|
| Keep the 19-unit order and current ownership | Rows and calendar are coherent | Course frame |
| Complete the evidence in finding 2 within existing units | Repairs the claimed standards without moving them | Frame, related progression notes and action summaries |
| Use one score for unit 16’s series at days 71 and 72 | Removes duplication without changing calendar totals | Course frame |
| Use the 45-minute day 2 allocation in finding 8 | Preserves preparation, retrieval and teaching | Course frame |
| Retain Annabelle as explicitly identified review | Reuse can serve a harder purpose without claiming nonrepetition | Course frame |
| Preserve invented-dancer food tasks and no-lifts rule | These are settled course constraints | Frame and later plans |

## What is right and should not be touched

Keep the achievement-level entry rule, bridge, optional fourth year, distinct discipline vocabulary, original student choreography, portfolios and public or invented alternatives to personal disclosure. Keep practical work in the room, teacher judgment of performances, local storage, paper paths and the right to participate without compulsory solo dancing.

## What I could not judge

This frame cannot establish the safety of an actual room, the adequacy of final demonstrations, individual scoring reliability or achievement after 60 or 120 hours. Those require the later plans and evidence from use.

Item-level rights and every work’s cultural account remain unverified. No substantive finding rests solely on memory; prior memory informed review organization and arithmetic checks, which were checked against the current files.

## Sources and source-list follow-up

The finding links identify the outside evidence used. The principal national sources were:

- [National dance performance standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance.pdf): full actions checked against the local summaries.
- [Dance opportunity-to-learn standards, 2017 revision](https://www.nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf): floor, space and high school scheduling guidance.
- [Nova Scotia physical education safety guidelines](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical_Education_Safety_Guidelines.pdf): dance precautions and progression. The currently served document is dated **2026**, rather than the frame’s September 2021 citation.

**For the source list:** Record the working links above. The dance association’s high school scheduling lines are readable: Proficient and Accomplished provision describes 60 to 90 minutes at least three times weekly; Advanced describes a typical 90-minute class. The frame’s 45-minute periods need an explicit comparison, distinguishing period length from weekly totals. This completes the source-reading step requested in For the lead item 2 without changing Cory’s settled dose.

## For Cory

- Resolve the PE and arts boundary so required dance technique can be taught explicitly.
- Decide whether Level 4 offers recovery for all unmet Advanced IDs or only its current selected reassessments.
- Decide any resource implications of suitable movement space and the proposed optional supplies ceiling. This review authorizes no spending or outside involvement.

