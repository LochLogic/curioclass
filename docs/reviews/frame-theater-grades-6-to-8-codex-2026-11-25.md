# Second-model frame read: Theater, grades 6 to 8

**Course:** `theater-grades-6-to-8`  
**Date:** 2026-11-25  
**Mode:** Read only. No files created or changed.

## Verdict

**Requires changes before scope and sequence writing.** The annual structure is coherent: all 24 selected progression skills and 72 standard ids are placed once, in their correct years, with workable full-path calendars and reciprocal handoffs. The main risk is that writers could follow the assessment instructions exactly while collecting incomplete evidence; repair those contracts and the once-a-week assessment sequence first.

**Findings: 6**, most serious first.

This differs from the “sound and buildable” verdict in `docs/reviews/frame-theater-grades-k-to-12-2026-11-25.md`. Placement and arithmetic hold, but they do not establish complete teaching and assessment of each standard.

## What was read and checked

- The complete target frame, its `course-list.csv` selector, `frames.csv` entry and `calendar.csv` rows.
- All 24 selected theater progression rows for grades 6, 7 and 8, their prerequisites, handoffs and words-file actions.
- The neighboring theater frames’ relevant units, seams and models.
- Relevant grade 6, 7 and 8 ELA Units tables, plus the grade 12 anchor list.
- `frame-read.md`, the after-core provisions of `frame-write.md`, `EXPERT.md`, the arts lens, arts adoption bar, arts `STANDARD.md` and `APPROACH.md`.
- Relevant foundation, shared approach, production-path, calendar, baseline and decision provisions.
- Earlier arts pre-work, progression and theater frame reviews.
- The outside sources linked below.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check theater-grades-6-to-8` | One failure: this frame-stage course lacks the lesson-plan data the command requires; review continued |
| `python -X utf8 scripts/frame.py check theater-grades-6-to-8` | Passed: 0 failures |
| `python -X utf8 scripts/stale.py check` | Passed: 121 files, 0 failures |
| Independent skill count | 24 selected skills, each placed exactly once |
| Independent standard count | 72 ids, each placed exactly once, 24 per year |
| Independent day count | Each year: 60 unit days, 2 course check days and 2 respond days, totaling 64 |

The plan check was course-filtered because repository instructions prohibit an unfiltered run. The gate wrapper was not run because it writes outputs and baselines.

## Findings

### 1. Unit 10 substitutes adaptation comparison for comparison of productions of the same work

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** Firm

**Location:** Unit 10, works, teaching and evidence for `TH:Cn11.2.8a`.

**Problem:** The unit compares Li Xingdao’s *The Chalk Circle* with Brecht’s *The Caucasian Chalk Circle*. These are different plays connected by adaptation. The assigned standard requires comparison of productions of the same work, a distinction confirmed on PDF page 10 of the [official theater standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf).

**Why it matters:** Students could complete the specified investigation without encountering the intended production comparison.

**Exact fix:**

- Keep the Yuan play and painting as historical context and retain the original-scene task.
- Teach the owned comparison through two named productions of Brecht’s play: the 1997 National Theatre and Complicité production and the 2015 Unicorn production.
- Require a research sheet comparing how those productions communicate two story elements, with a source identified for each production.
- Retain the unseen written comparison as transfer evidence, rather than the sole evidence of research.

The productions are documented by [Complicité](https://www.complicite.org/work/the-caucasian-chalk-circle/), the [National Theatre archive](https://catalogue.nationaltheatre.org.uk/calmview/Record.aspx?id=1582&src=CalmView.Performance) and [Oxford’s Writing Brecht project](https://brecht.mml.ox.ac.uk/caucasian-chalk-circle). Use original descriptions and links under the existing rights policy.

### 2. Several evidence lines permit incomplete standards coverage

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete evidence contracts also appear in the earlier theater K to 2 and grades 3 to 5 reads  
**Confidence:** Firm

**Location:** Units 1, 3, 5 and 9, “What students learn” and “End-of-unit evidence.”

The following repairs preserve existing ownership. They follow the arts approach’s requirement that every owned action have evidence and were checked against the [official standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf), especially PDF pages 3 to 5, 7 and 8.

| Unit and id | Problem | Exact fix |
|---|---|---|
| 1, `TH:Pr4.1.6b` | Teaching tries three physical choices, but the final evidence records only one. | Keep the final showing and score a rehearsal record identifying the alternatives actually tried and the choice retained. |
| 1, `TH:Pr5.1.6a` | The scored note addresses a warm-up, omitting the acting method taught alongside it. | Give the note two fields: exercise and acting technique, each with its application to the scene. |
| 1, `TH:Cr3.1.6b` | “Two effective body or voice traits” allows both answers to omit either body or voice. | Require one physical trait and one vocal trait, each explained through its effect. |
| 3, `TH:Re9.1.6b` | Identifying an element and its aesthetic choice does not require a judgment. | Ask whether the choice works, supported by the production element and its effect. |
| 9, `TH:Pr4.1.8b` | The task fixes one objective and varies tactics. | Have each student test two objectives, then select tactics against the obstacle; record both trials. |
| 9, `TH:Cr3.1.8b` | A bodily response “held” does not establish refinement across physical, vocal and physiological choices. | Add a before-and-after rehearsal record covering all three, corroborated by teacher observation. |
| 1, 5 and 9, `TH:Re8.1.6c`, `.7c`, `.8c` | The evidence accepts taste alone, leaving beliefs unexamined. | Include an artistic preference and a belief about the scene’s meaning or choices, then identify, interpret or apply them at the year’s required level. Preserve the equally scored invented-viewer option. |

**Why it matters:** These instructions currently allow a “met” mark without complete evidence. The belief task need not request religious beliefs or private disclosures.

### 3. The once-a-week path collects new assessment evidence during response

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, earlier theater reads and `prework-arts-fixes-2026-11-20.md` identify the same timing problem  
**Confidence:** Firm

**Location:** “The once-a-week path,” especially the respond session’s first 20 minutes.

**Problem:** Written assessment occurs at the beginning of the respond session. Arts `APPROACH.md`, “Scoring creative work,” requires marks before that session because those marks determine the response.

**Why it matters:** The teacher cannot prepare response groups from evidence not yet collected, and assessment consumes the promised second attempt.

**Exact fix:** Keep the existing **9, 7, 6, 6** unit-session allocations, but reserve separate showing, written-check and respond sessions.

| Unit position in each year | Study and demonstration | Rehearsal, critique and revision | Showing check | Written check | Respond | Total |
|---|---:|---:|---:|---:|---:|---:|
| First | 2 | 4 | 1 | 1 | 1 | 9 |
| Second | 2 | 2 | 1 | 1 | 1 | 7 |
| Third | 1 | 2 | 1 | 1 | 1 | 6 |
| Fourth | 1 | 2 | 1 | 1 | 1 | 6 |

Remove first-time assessment from respond sessions. Complete marking before response. These counts preserve 28 unit sessions plus four course check/respond sessions, including the stated short-path check weeks.

The allocation is a planning judgment, not evidence that the compressed teaching has been tested.

### 4. Group assessment arrangements do not guarantee individual evidence or honor recording refusal

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** new for the individual-evidence gap; assessment feasibility recurs in earlier frame reads  
**Confidence:** Firm on the omissions; judgment call on the delivery arrangement

**Location:** “Scored evidence,” “Reading load,” Units 1, 5, 7, 9 and 10, and Course-level checks.

**Problem:**

- Six groups of five perform scenes that may have only two acting roles. Students may instead choose director, designer or stage-manager jobs, but the frame promises acting evidence for every learner.
- Unit 7 adds a two-minute design presentation without saying whether it fits inside the common four-minute group slot.
- Unit 10 requires two pacing trials and an original scene without dividing that slot.
- A group the teacher cannot watch live “is recorded.” The arts approach explicitly permits recording refusal and requires live observation instead.

**Why it matters:** A group performance can appear complete while leaving some students’ owned acting skills unobserved. The timetable and recording rule can also fail the promised access arrangements.

**Exact fix:**

1. Add a student-by-id observation roster. Every acting id needs an individually attributable mark; a production job alone cannot supply it.
2. For two-character scenes, rotate roles during designated final observation rounds on the last rehearsal days. Collect missing marks live before the respond session. Group course-check cards must likewise give every student an observable acting turn.
3. Define four-minute showing slots explicitly. For unit 7: two minutes presenting the fix, 90 seconds demonstrating it in the scene, 30 seconds changing groups. For unit 10: two one-minute pacing excerpts, a 90-second original scene and 30 seconds changing groups.
4. Replace the compulsory-recording sentence with: “Recording is optional. A student who declines is observed live during a scheduled final observation round; the teacher’s mark is the evidence.”

Keep supported, seated and ensemble participation available.

### 5. Recurring studies and the ELA anchor overlap need an explicit decision

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the combined theater read identifies these overlaps  
**Confidence:** Firm on the overlaps; judgment call on retaining them

**Location:** Base-text selection statement; Units 1, 3, 8 and 9.

**Problem:** Checking only against theater K to 2 misses relevant earlier studies:

- Kyogen already appears in grades 3 to 5, unit 2.
- Appia already appears in that frame’s unit 7.
- Kamiriithu already appears in its unit 11.
- *The Importance of Being Earnest*, used here in unit 9, is a whole-play ELA grade 12 anchor.

**Why it matters:** `frame-write.md`, lesson 11, asks writers to avoid repeated picks. A purposeful return can deepen learning, but the frame must distinguish that return from a fresh introduction.

**Exact fix:**

- Name kyogen, Appia and Kamiriithu as deliberate revisits in their unit rows, with the earlier unit and the new analytical task: artist experience, aesthetic judgment and cultural perspectives respectively.
- Replace unit 9’s performed *Earnest* adaptation with a Curio Class original interview scene about permission to stage a community performance. Give it competing objectives and constraints of time, space and cost. Retain Stanislavski and Spolin as the technique studies.
- Replace the K to 2-only selection assurance with a statement covering the adjacent band and ELA anchor check.

Different Chaplin films are not automatically the same work. Repeated makers need a reason, rather than automatic removal.

### 6. Living notes still describe completed work as missing

**Severity:** Moderate  
**LAYER:** process  
**REPEAT:** yes, earlier arts and theater reviews identify stale status language  
**Confidence:** Firm

**Problem:** The stale-marker check passes, but several unmarked claims are obsolete or contradicted by current evidence.

| Location | Evidence | Exact fix |
|---|---|---|
| Target frame, For the lead item 3 | `scripts/frame.py` already uses `stagger_key`, counting after-core courses separately. | Replace the requested checker change with: “The checker counts arts courses separately. School day 83 still has after-core clashes in grades 6, 7 and 8; the lead’s calendar pass resolves them.” |
| Target frame, For the lead item 4 | The eighteen named progression notes already contain multiple evidence forms. Some remain incomplete, but “one form” is no longer accurate. | Replace with: “The eighteen notes were expanded. Align remaining summaries with the corrected id-by-id evidence, using only the row’s own grade.” |
| `ADOPTION-BAR-SUBJECTS.md`, arts owed row | L83 is done; all 63 high school composition-and-theory ids are loaded. | Remove both owed clauses and record their completed state. |
| `CALENDAR.md`, paragraph before Target weeks | It says the checker shows no break, although current calendar rows contain after-core clashes. | Replace the current-state claim with: “After-core clashes remain in the calendar and require the lead’s calendar pass.” |
| Arts `STANDARD.md` 3.4, arts `APPROACH.md` sources table, and target frame’s time note | The association’s own document contains middle-school scheduling guidance. | Replace “no figure” and the outstanding-read request with the verified source statement below. |

The [2016 Educational Theatre Association opportunity-to-learn document](https://schooltheatre.org/wp-content/uploads/2022/02/Opportunity-to-Learn-Standards-EdTA_2022.pdf), PDF page 10, recommends at least 45 minutes of instruction during the school day for at least one semester each year. That scheduling item does not explicitly say “daily,” so preserve its wording’s meaning and label any daily interpretation.

The frame provides **42 hours 40 minutes annually**, or **21 hours 20 minutes** on the short path. If comparing with 45 minutes daily over the repository’s 80-day semester, label that assumption: the comparator is 60 hours, with gaps of 17 hours 20 minutes and 38 hours 40 minutes respectively. Do not present the existing “about 67” estimate as the repository-calendar comparison.

**Why it matters:** These notes can trigger duplicate work or misstate current readiness and scheduling evidence. Update living guidance in place; preserve dated reviews as records.

## Lens checklist at frame level

| Lens requirement | Result |
|---|---|
| Correct grade ids in each band year | Met |
| All four artistic processes each year | Met |
| Technique taught directly and made harder | Met in the planned sequence |
| Discipline words used in making and response | Met |
| Student choice and a showing in every unit | Met |
| Structured critique followed by revision | Met on the full path; short-path sequence needs finding 3 |
| Works span cultures, periods and living makers | Met in planned selections; revisit purposes need finding 5 |
| Growth, self-assessment and kept work | Present; individual evidence needs finding 4 |
| Realistic sessions, equipment and safe space | Planned; assessment delivery needs finding 4 |
| Performing happens with people in the room | Met |
| Participation without compulsory solo performance | Present; role alternatives must retain individual evidence |
| Distinct theater learning and cross-subject boundaries | Met |
| Tools support rather than judge performance | Met |
| Original assessment tasks rather than copied cornerstone tasks | No contrary provision found |

Detailed day-level execution and safety validation remain later-stage work.

## Calendar, seams and load

- Each year contains units of **18, 14, 14 and 14 days**. The longer character unit has seven ids and establishes routines; the remaining allocations are defensible for their five or six ids.
- Mid-year checks fall on school day **83**, followed by response on **85**. They avoid core check weeks.
- Year-end checks fall on school day **158**, followed by response on **160**. Week 32 is permitted as finals week.
- Day 83 also holds dance, media arts, physical education and visual arts checks in each grade. These are existing clashes for the lead’s combined calendar pass, not grounds to withhold this verdict.
- Grade 5 handoffs and Level 1 pickups match the progression. The Level 1 bridge preserves entry for students without prior theater.
- ELA writing and story-analysis leans are available in time. Earlier speaking demands have bounded theater-specific fallbacks.
- No base text is claimed, so a base-lesson source map is not applicable.

## Settled by the expert

| Choice | Reason | File affected |
|---|---|---|
| Retain the annual unit order and full-path day allocations | Ownership, prerequisites and load support them | Target frame |
| Keep ownership unchanged while repairing evidence | The defects concern completeness, not placement | Target frame; corresponding progression summaries |
| Keep 9, 7, 6, 6 sessions on the short path | Separate checks and response fit within the existing totals | Target frame |
| Use same-play production comparison in unit 10 | Corrects the assigned task without moving a standard | Target frame |
| Require individual observation and optional recording | Makes the assessment and access promises executable | Target frame |
| Retain named earlier studies as explicit revisits; replace the performed *Earnest* scene | Preserves useful progression while avoiding the whole-play ELA anchor | Target frame |

## What is right and should not be touched

- The grade-year ownership and reciprocal seam tables.
- The progression from circumstances to objectives, then tactics and motives.
- The practical materials, paper paths and theater-specific ELA fallbacks.
- The critique routine, portfolios and baseline-to-final growth observations.
- The cultural-context provisions, invented personal-tie options and restrictions on imitating sacred practices.

## What could not be judged

- Actual teaching feasibility of the compressed path without its day sequence.
- Individual work suitability, editions and rights lines, which remain unit-plan checks.
- Final safety and sensitivity clearance. The frame marks inherited safety rules “from memory”; this review does not certify them.

No substantive finding above rests on unverified memory. Prior memory informed review format only.

## For Cory

- **Money:** Decide the proposed optional supplies ceiling of **$45 per class per year**. Preserve every free path.

No new audience, staffing or outside-person decision is needed for the fixes above.

## For the source list

Record the exact links used here:

- [Official theater standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Theatre%20at%20a%20Glance.pdf): checked action completeness and the production-comparison requirement.
- [2016 opportunity-to-learn standards](https://schooltheatre.org/wp-content/uploads/2022/02/Opportunity-to-Learn-Standards-EdTA_2022.pdf): verified middle-school scheduling guidance.
- [Complicité production page](https://www.complicite.org/work/the-caucasian-chalk-circle/) and [National Theatre archive](https://catalogue.nationaltheatre.org.uk/calmview/Record.aspx?id=1582&src=CalmView.Performance): documented the 1997 production.
- [Oxford Writing Brecht production listing](https://brecht.mml.ox.ac.uk/caucasian-chalk-circle): documented the 2015 Unicorn production.

