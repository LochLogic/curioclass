# Independent frame review: Dance, grades 6 to 8

**Date:** 2026-11-25  
**Course:** `dance-grades-6-to-8`  
**Finding count:** 10  
**Read-only review:** No files changed.

## Verdict

**Revise before writing the scope and sequence.** The band structure, ownership and annual totals are sound, but several teaching and assessment instructions narrow the owned standards, and the floor rule can permit impact work on unsuitable surfaces. Restore the missing actions and their evidence within the existing units, while preserving the course’s cultural range, accessible participation and free alternatives.

## What I read and checked

- [The complete course frame](S:/CurioClass/docs/courses/dance-grades-6-to-8/frame.md).
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, foundation and relevant baseline rules.
- The shared adoption criteria and arts part of `ADOPTION-BAR-SUBJECTS.md`; arts `STANDARD.md` and `APPROACH.md`; relevant Desk decisions and arts pre-work reviews.
- The course-list selector, frame metadata, calendar rows, all 24 selected progression rows and their 63 standards, the corresponding words-file entries and adjoining progression handoffs.
- Adjacent dance frames’ unit and seam tables; the relevant PE, health, ELA and social studies connections.
- Earlier dance reviews to identify repeated findings, checked against current files.
- The national dance standards and the outside sources linked below.

| Check | Result |
|---|---|
| `python -B -X utf8 scripts/frame.py check dance-grades-6-to-8` | **Pass:** 0 failures; 60 unit days in each year, 192 days overall. |
| Independent ownership and arithmetic check | **Pass:** 24 skills and 63 codes placed exactly once; 21 codes per year. |
| `python -B -X utf8 scripts/plan.py check dance-grades-6-to-8` | Cannot validate this frame at plan stage: the required day-plan data does not exist; review continued. |
| `python -B -X utf8 scripts/stale.py check` | **Pass:** 121 files, 0 detected failures; unmarked stale statements remain in finding 10. |

No base-text source map is required: this course has no base text.

## Findings, most serious first

### 1. Several owned standards lose required actions or sufficient scored evidence

**Severity:** Major  
**LAYER:** standard, progression and frame  
**REPEAT:** yes, incomplete standards and evidence recur in the earlier arts and independent dance reads.  
**Confidence:** firm.

**Location:** Units 1, 3 to 5, 7 to 9, 11 and 12, frame lines 317 to 328; corresponding progression notes and words-file entries.

The frame frequently improves on the short words file, but its claim that every id is taught and checked in full remains too strong. These are substantive omissions, rather than requests for more assessment items.

**Exact fixes:** Add the following teaching and evidence inside the existing owning units. Update any corresponding words-file or progression note that preserves the narrower action.

| Unit and id | What is missing | Exact addition |
|---|---|---|
| **1: DA:Pr5.1.6a** | Direction changes, jumps, landings and transitions omit levels, facings, pathways and limb extensions. | Teach and observe those additional actions in the group phrase, with technical control named in the guide. [Grade 6 technique standard](https://www2.cde.ca.gov/cacs/id/web/30272) |
| **1: DA:Pr5.1.6b and 6c** | A written warm-up plan does not demonstrate safe application; a group-growth log need not document each dancer’s improvement. | Add live observation of the warm-up and safe body use. Give each student a dated improvement entry in the rehearsal log. Keep food choices with the invented dancer. [Grade 6 technique standard](https://www2.cde.ca.gov/cacs/id/web/30272) |
| **9: DA:Pr4.1.8b** | Layered tempos omit differing phrase lengths and varied timings within one section. | Teach and assess an unequal-length phrase combination, alongside simultaneous body-part tempos and explained phrasing choices. [Grade 8 elements standard](https://www2.cde.ca.gov/cacs/id/web/30261) |
| **3: DA:Re8.1.6a** | The item permits only two aspects, and omits body use from its choices. | Require explanation connecting elements, body use, technique, structure and context to expression and intent, using appropriate dance terms. [Grade 6 interpretation standard](https://www2.cde.ca.gov/cacs/id/web/30311) |
| **7: DA:Re8.1.7a** | “One element or setting” does not establish the promised interpretation. | Compare both dances’ meanings and explain expression through elements, body use, technique and context, using terms appropriate to each style. [National dance standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance.pdf) |
| **11: DA:Re8.1.8a** | The analysis scores elements and named moments, leaving body use, technique and context unspecified. | Score how those aspects work together to create expression, supported by the selected moments and appropriate terminology. [Grade 8 interpretation standard](https://www2.cde.ca.gov/cacs/id/web/30313) |
| **4: DA:Cn11.1.6a** | Written interpretation **or** showing does not establish both actions. | Collect interpretation plus accessible demonstration. Use the already studied, nonceremonial waltz as review, with a sourced context card; retain Tang objects and Kaha:wi for observation only. [Grade 6 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30350) |
| **8: DA:Cn10.1.7b** | A spirit study and three history lines omit the historical presentation and documentation of research applied to movement. | Make the showing a short lecture demonstration tracing the style’s development, supported by a research-and-application record. [Grade 7 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30338) |
| **12: DA:Cn10.1.8b** | Two separate pieces omit an explicit study exploring their contrasting ideas; research methods and deeper understanding are unspecified. | Organize both topics into one study with contrasting sections. Use at least two suitable research methods and explain both choreographic choices and new understanding. [Grade 8 connecting standard](https://www2.cde.ca.gov/cacs/id/web/30339) |

Four further corrections follow from the national text:

- **Unit 5, DA:Pr5.1.7a:** add copying, remembering and performing spatial and rhythmic phrases using the taught adaptations.
- **Unit 11, DA:Re7.1.8a:** collect description, demonstration and discussion; the current written-or-show choice does not establish all three.
- **Unit 12, DA:Pr6.1.8a:** add the missing plan for continuing improvement.
- **Unit 8, DA:Cn11.1.7a:** address similarities as well as differences, relating explanations to community perspectives.

These remain in their present units. [National dance standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Dance%20at%20a%20Glance.pdf)

**Why it matters:** A scope writer could follow the frame faithfully and still teach or assess less than the course claims.

### 2. “Wood or mats” is not a sufficient floor rule for impact work

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, source-based safety and ordinary-room feasibility recur in earlier arts reviews.  
**Confidence:** likely.

**Location:** Safety read, lines 182 to 194; units 1 and 5; the ordinary-room promise.

The frame permits jumps on “a wooden floor or mats.” That includes possible wood over concrete and treats unspecified mats as sufficient protection. The named dance guidance distinguishes resilient flooring from hard construction and explicitly warns about wood over concrete. [Dance opportunity-to-learn standards, facilities section](https://nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf)

**Exact fix:** Replace the impact-floor sentence with:

> Jumps, landings and repeated stamping use a level, resilient surface confirmed suitable by the safety read and the school. A wooden finish or a loose mat over a hard floor does not by itself establish suitability. On an unsuitable floor, use non-impact marking and arrange the required movement observation in a suitable school space before recording that action as met.

Add a small-space version using stationary work and rotating groups, with waiting students outside the movement area. Link the actual safety guides, rather than their domains. The school guide also requires safe footing, clear surrounding space and progressive instruction. [Nova Scotia safety guide, dance section](https://curriculum.novascotia.ca/sites/default/files/documents/resource-files/Physical%20Education%20Safety%20Guidelines%20%282021%29%20EN.pdf)

**Why it matters:** The ordinary-room alternative must give a teacher an executable decision before students jump or stamp.

### 3. Participation roles are treated as equivalent performance evidence

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, finding 2 in both independent earlier-band dance reviews.  
**Confidence:** firm.

**Location:** Taking part without dancing alone, lines 127 to 131.

A seated or one-limb version can demonstrate movement learning. Directing, counting or leading staging does not automatically demonstrate the performer’s timing, spatial control or technique. The inclusion guidance supports individualized accommodations and varied expression, rather than blanket equivalence between roles. [Dance inclusion guidelines](https://www.nationalartsstandards.org/sites/default/files/Dance_resources/Dance%20Inclusion%20Guidelines.pdf)

**Exact fix:** Replace “marked on the same look-fors in that version” with:

> Each accessible movement version is mapped to the performance look-fors it demonstrates. Director, counter and staging roles establish only outcomes directly demonstrated through that role. Where an owned movement action remains unseen, collect an accessible movement demonstration with the student’s usual supports and record the accommodation.

Preserve group participation, live observation and the choice against recording.

**Why it matters:** Participation must not become a performance mark without evidence of the action claimed.

### 4. Several routines are first placed after units already require them

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, first-use placement recurs in earlier frame reads.  
**Confidence:** firm.

**Location:** Day kinds, Models carried and units 1 to 4.

Every unit studies works, critiques and performs for an audience. Nevertheless, `feedback-loop`, `look-and-say` and `dance-look-describe-interpret` first appear in unit 3; performing-space and performance-etiquette first appear in unit 4. The grade 6 entry route cannot assume students took the optional preceding dance course.

**Exact fix:** Change those Models carried entries to:

> First modeled or retrieved in unit 1 when the routine is first used; developed and assessed under its owned standard in unit 3 or unit 4.

Make unit 1 explicitly teach describe, ask, suggest; the observation routine; and performer/audience space and conduct. Keep formal revision ownership in unit 3 and staging ownership in unit 4.

**Why it matters:** The current table can send a writer into a critique or showing before the class has learned its routine.

### 5. Retrieval and reteaching do not fit the stated opening

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, finding 7 of the independent grades 3 to 5 dance read.  
**Confidence:** firm on the conflict; judgment call on the allocation.

**Location:** Days, Readiness and retrieval, and grade 6 unit openings.

The warm-up receives about five minutes, but retrieval takes ten minutes “inside” it. Grade 6 unit rows additionally promise each of two assumed threads its own ten-minute reteach.

**Exact fix:** Give day 2 a separate combined retrieval block and replace the two separate reteaches with an integrated reteach when needed:

| Component | Minutes |
|---|---:|
| Setup | 3 |
| Warm-up | 5 |
| Combined retrieval | 10 |
| Teaching, including an integrated reteach when needed | 15 |
| Cool-down | 4 |
| Reset | 3 |
| **Total** | **40** |

State that the shorter path carries this block inside its opening session.

**Why it matters:** Otherwise, a teacher must exceed the period or silently remove warm-up or instruction.

### 6. Whole-unit leave-outs lack replacement material for dependent units

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, finding 3 in both independent earlier-band dance reviews.  
**Confidence:** firm.

**Location:** Leave-out, lines 146 to 152; units 3, 7, 11 and 12.

The frame says every unit stands alone, but units 3, 7 and 11 revise the preceding making unit’s product. Unit 12 stages the revised dance from unit 11. Earlier-year retrieval does not replace a missing same-year product.

**Exact fix:** Add to Leave-out and those receiving units:

> If the required earlier product is absent because a unit was omitted, the receiving unit supplies a neutral Curio Class original study or a fresh making prompt. Learning or making that material is counted before feedback, revision and assessment. Omitted-unit ids remain unclaimed.

Specify a short study for units 3 and 7, an original group study for unit 11, and a staging-ready study for unit 12.

**Why it matters:** Exercising the settled leave-out choice must leave the remaining units usable.

### 7. Mid-year checks immediately reassess the unit just completed

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, frame-write lesson 20 and the independent grades 3 to 5 read.  
**Confidence:** firm.

**Location:** Course-level checks, lines 334, 336 and 338.

Each mid-year check carries recent-unit records unscored but also introduces newly scored tasks from that same unit:

- Grade 6 repeats unit 2’s creating standards.
- Grade 7 repeats unit 6’s creating standards.
- Grade 8 repeats unit 10’s creating standards.

**Exact fix:** Keep the recent making-unit records unscored and newly score retained learning from units 1, 5 and 9 respectively. Use a new spacing-and-timing phrase in grade 6, borrowed designs and accented timing in grade 7, and sculpted space, layered timing and phrase recall in grade 8.

Change the three “Samples units…” sentences accordingly. Preserve the year-end checks’ earlier-unit sampling.

**Why it matters:** The additional check should provide retention evidence and useful response, rather than repeat the assessment just completed.

### 8. The PE connection omits a shared tradition and overstates separation

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, findings 3 and 4 of the earlier combined dance review.  
**Confidence:** firm.

**Location:** Dance/PE bullet, Base text bullet, units 2 and 8, Cross-subject table.

The frame still names tinikling among PE’s choices and says none of its dances repeats PE. Current PE unit 6 uses cumbia, while PE unit 22 explicitly retrieves this course’s grade 7 capoeira study.

The absolute “teaches no motor cue” statement also conflicts with this frame’s required instruction in landings, alignment and weight shifts.

**Exact fix:**

- Replace the obsolete PE list with **cumbia, kolo and the original line dance**.
- Add a reciprocal connection: **dance unit 8, grade 7**, studies capoeira’s history and artistic character; **PE unit 22, grade 8 weeks 28 to 31**, teaches the basic ginga and cultural significance, retrieving that history or supplying its own context card.
- Replace the no-repeat claim with this named, deliberate return.
- Replace “teaches no motor cue” with: “Dance teaches the technique required by its artistic standards inside this course; it assumes no earlier PE instruction.”
- Name canon and contrast as shared vocabulary: PE uses them for coordinated movement; dance uses them to shape artistic intent.

**Why it matters:** The current wording misdirects the writer about both available prerequisites and legitimate dance technique instruction.

### 9. Source links and several anchor choices remain unfinished

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, named picks and sourced facts recur in earlier frame and dance reads.  
**Confidence:** firm.

**Location:** Works cells, Safety read and For the lead item 4.

The frame contains no direct web links. The step team, Sankai Juku work, Moiseyev piece and particular museum objects remain deferred choices. Those selections determine whether the promised technique, comparison and cultural boundaries actually work.

**Exact fix:** Complete a frame work register before scope writing:

`Unit | Exact work or excerpt | Maker/practitioner | Place and date | Direct source | Feature studied | Observation only or movement use`

Replace every “the unit plan picks” anchor with the selected work. Retain item-specific rights checks in the unit plan, as the arts approach requires.

For already verifiable entries:

- Label **Weave** as a **2018 to 2020 project, premiered January 2019**, matching the maker’s account. [Weave](https://www.rosysimasdanse.com/weave)
- Link the maker’s account for **Juice**, including its three-installment structure. [Juice](https://www.meredithmonk.org/repertory/juice-2/)
- Link the primary page supporting **Rite of Spring’s** date and source-music relationship. [Rite of Spring](https://www.shenweidancearts.org/rite-of-spring)

Add direct links for the two safety guides already named in finding 2.

**Why it matters:** The scope writer should not inherit unresolved anchors or reconstruct the evidence for cultural and historical statements.

### 10. Unmarked notes describe completed work as outstanding

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, earlier combined dance and arts reviews identified these stale-note patterns.  
**Confidence:** firm.

**Exact fixes:**

| Location | Replacement or action |
|---|---|
| Standard bullet, lines 52 to 54; For the lead item 3 | Remove the historical correction request. The listed progression changes have landed. Replace it with the remaining specific corrections in finding 1, recorded in the report rather than only in a writer’s chat message. |
| For the lead item 2 | Delete the requested replacement for PE’s pending prose: PE lines 367 to 372 already name the dance units and technique rows. Retain only the request to make the PE table’s row-id cell consistent. |
| Handed-on introduction, line 262 | Replace “is being written beside this one” with “is written; its Level 1 bridge and receiving units are named below.” |
| Receiving high school frame, grade 8 responding seam | Replace “time-stamped evidence” with “time-stamped or moment-named evidence.” |
| Arts row of `ADOPTION-BAR-SUBJECTS.md` | Remove the outstanding standards-gate and music-strand loading tasks; arts `STANDARD.md` already records their completion. |
| For the lead item 1 | Update the collision list from the current calendar. PE’s check is school day 82, rather than 84; several other arts checks share dance’s day 83. Explicitly except the permitted week 32 finals overlap from the no-core-clash statement. |

Shared-file corrections belong to the lead. Preserve dated review reports as records.

**Why it matters:** Stale instructions send subsequent workers back to completed tasks and hide the corrections that remain.

## Calendar, allocation and seams

| Year | Unit days | Course check and respond days | Total |
|---|---|---|---:|
| Grade 6 | 18 + 14 + 14 + 14 = 60 | 4 | **64** |
| Grade 7 | 18 + 14 + 14 + 14 = 60 | 4 | **64** |
| Grade 8 | 18 + 14 + 14 + 14 = 60 | 4 | **64** |

The shorter path also adds correctly: **28 unit sessions plus four course check and respond sessions**.

The longer opening units have a defensible technique and routine load. The 14-day revision/response units carry substantial work, but I found no demonstrated need to change their totals before the scope allocates their drafting, feedback and revision days.

Calendar rows agree with the frame: mid-year checks are in week 17, with check day 83 and respond day 85; year-end checks are in week 32, with days 158 and 160. Week 17 avoids the four core subjects’ checks. Other arts courses share day 83, so the lead’s after-core calendar pass remains necessary.

All eight incoming and outgoing progression threads match at both ends. ELA grade 6 discussion, ELA grade 8 argument writing and grade 6 social studies’ Silk Roads material precede their stated uses. Health and PE arrive later but have explicit in-course fallbacks. The remaining PE corrections are in finding 8.

The stated **80-minute weekly full path** and **40-minute shorter path** correctly disclose their gaps against the published **90-minute grades 6 to 8 recommendation**. [Dance opportunity-to-learn standards](https://nationalartsstandards.org/sites/default/files/NDEO%20Opportunity%20to%20Learn%20Standards%202017%20rev.pdf)

## Lens checklist

Statuses concern frame commitments, not completed lessons.

| Lens requirement or error check | Status |
|---|---|
| Correct grade ids in each band year | **Met:** 21 per year. |
| Four artistic processes each year | **Met.** |
| Technique taught directly and increasing in difficulty | **Partly met:** finding 1. |
| Discipline words used in making and responding | **Met as planned.** |
| Student choice, original work and showing in every unit | **Met.** |
| Structured critique followed by revision | **Partly met:** first-use correction in finding 4. |
| Several cultures and periods, with living makers or traditions | **Met as planned range.** |
| Works taught with maker, time, place and purpose | **Partly met:** finding 9. |
| Growth, self-assessment and kept work | **Met as planned.** |
| Performance and response assessed substantively | **Partly met:** findings 1, 3 and 7. |
| Realistic frequency and period length | **Partly met:** finding 5. |
| Equipment, space and safe use | **Partly met:** finding 2. |
| Performing happens with people | **Met.** |
| No compulsory solo performance | **Met.** |
| Respond days distinguished from responding to art | **Met.** |
| Software does not judge finished performance | **Met.** |
| Dance/PE connection avoids unsupported prerequisites | **Partly met:** finding 8. |
| Five arts disciplines remain distinct | **Met.** |
| No copied cornerstone tasks or coalition explanatory text | No such copying identified. |
| Daily modeling, scaffold withdrawal and exact equipment use | **Not yet applicable:** verify in subsequent plans and days. |

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Retain the 12 units, existing ownership and annual totals | Placement and overall arithmetic hold. | Course frame |
| Restore omitted actions within their current owners | Completes existing scope without moving standards. | Frame, progression notes, words file |
| Map accessible evidence by outcome | A participation role establishes only what it demonstrates. | Frame and assessment directions |
| Separate retrieval from warm-up | Produces a 40-minute opening that can be followed. | Frame |
| Model recurring routines at first use | Optional earlier dance learning cannot be assumed. | Models carried and unit 1 |
| Provide neutral material after leave-outs | Keeps receiving units usable without reclaiming omitted ids. | Frame and later unit plans |
| Newly score earlier learning at mid-year | Adds retention evidence. | Course-level checks |
| Retain capoeira as a named cross-year return | The two subjects can build different learning from it. | Dance/PE connections |

## What is right and should not be touched

Preserve the coherent annual four-unit pattern, explicit grade ownership, technique progression, portfolio and baseline records, teacher judgment of performance, free paper path, invented alternatives to personal disclosure, cultural observation-only boundaries and the distinction between artistic responding and respond days.

## What I could not judge

This read does not establish the suitability or rights of every proposed excerpt, certify safety, or demonstrate that the observation schedule works with 30 students. Those require the selected source pages, completed unit plans and the promised content reads.

No finding rests on personal memory. The frame’s unverified safety prescriptions remain explicitly **from memory** until checked in the safety read; this review checked the floor issue and named guidance only.

## Sources and source-list follow-up

The linked national and state standards support finding 1. The inclusion guidance supports individualized access; the two safety guides support finding 2 and the pacing comparison; the maker pages support the work-register corrections.

**For the source list:** Add or cross-reference the direct inclusion and safety-guide links, plus the maker pages used here. California’s wording corroborates selected omissions; the national text remains this course’s governing standard.

## For Cory

- The existing optional filmed-phrase proposal remains a **people and money** decision. These corrections do not require filming.
- The proposed **$50 per class per year** supplies ceiling remains a money decision.
- If the intended audience includes schools with **no suitable movement surface anywhere available**, settle that limitation explicitly. Do not promise full impact-technique coverage on an unsuitable floor or silently require a purchase.