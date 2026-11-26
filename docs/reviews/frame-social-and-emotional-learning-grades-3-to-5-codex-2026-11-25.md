# Independent frame review: Social and Emotional Learning, Grades 3 to 5

Date: 2026-11-25  
Course: `social-and-emotional-learning-grades-3-to-5`  
Read only. No files were created or changed.

## Verdict

The frame has a sound instructional structure: all 120 selected progression rows are placed exactly once, the three grade years differ in depth, and the full calendar provides 64 sessions per year. It needs revision before scope writing because two standards remain partial, some leave-out dependencies are unresolved, and the short path introduces calendar conflicts. The most important change is to complete the required teaching within the existing units while preserving invented cases and optional personal sharing.

**Eight findings: one serious, six moderate and one minor.**

## What I read

- The frame-read brief, the after-core provisions of frame-write, EXPERT.md and the SEL lens.
- FOUNDATION.md; relevant provisions of PRODUCTION-PATH.md, APPROACH.md and BASELINE.md.
- ADOPTION-BAR-SUBJECTS.md, including the shared requirements, part 9 and SEL status row; SEL STANDARD.md and APPROACH.md.
- The complete [course frame](S:/CurioClass/docs/courses/social-and-emotional-learning-grades-3-to-5/frame.md), its course-list selector, frames.csv entry and calendar.csv rows.
- The 120 SEL progression rows selected by `grade:3|4|5`, their incoming and outgoing links, and all 40 standard statements.
- The adjacent SEL frames’ unit placements, seam tables and model descriptions.
- Relevant Units tables in grades 3 to 5 ELA, social studies and mathematics; the health and PE seam provisions; computer science grade 5’s team-project placement.
- Library’s three transfers to SEL and the validators’ current standards recognition.
- Earlier SEL progression, pre-work and frame reviews, including the K to 2 fix report and the combined grades 3 to 12 expert read.
- The outside sources linked below.

No base text is claimed, so a base-lesson source map is not applicable.

## Checks and counts

Commands used `python -B -X utf8` to prevent bytecode-cache writes. The plan check was course-filtered to honor the repository instruction against unfiltered runs.

| Check | Result |
|---|---|
| `scripts/plan.py check social-and-emotional-learning-grades-3-to-5` | Failed because day-plan files do not yet exist; review proceeded |
| `scripts/frame.py check social-and-emotional-learning-grades-3-to-5` | Passed, zero failures |
| `scripts/stale.py check` | Passed, 121 files, zero failures |
| Targeted stale check on the frame, SEL standard, SEL approach and subject bar | Passed, zero failures |
| Independent progression placement count | 120 rows, 120 distinct placements, no missing or extra rows |
| Ownership count | All 40 SEL codes owned in grade 5; grades 3 and 4 begin them |
| Reciprocal progression links | No broken incoming or outgoing links for the selected rows |
| Full-path calendar | 60 unit sessions plus four check and respond sessions per year |

| Grade | Units | Sub-skills per unit | Full-path total | Short-path total |
|---|---|---|---:|---:|
| 3 | 1 to 6 | 6, 5, 7, 6, 8, 8 | 64 | 32 |
| 4 | 7 to 12 | 5, 6, 6, 8, 7, 8 | 64 | 32 |
| 5 | 13 to 18 | 5, 6, 5, 8, 8, 8 | 64 | 32 |

The full-path checks avoid current same-grade core check weeks. That does not establish that the short path does so.

## Findings, most serious first

### 1. Complete placement masks partial treatment of two standards

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, K to 2 second-model finding 2 identified these same missing components  
**Confidence:** firm

**Location:** Frame units 1, 10, 13 and 18; progression rows `g3-sa-feel-think-link`, `g4-sa-feel-think-link`, `g5-sa-feel-think-link` and `g5-sa-my-strengths`.

Two components are not secured by the required teaching:

- **SA5:** The think-feel-do cases connect thoughts, feelings and actions, but do not explicitly connect what the character values to those thoughts and feelings. Naming a value separately in an honesty task does not teach that relationship.
- **SA2:** Grade 5 unit 18 makes a cultural or linguistic strength conditional on the student choosing to include one. Consequently, the owner-year task can be completed without teaching that component.

Both components appear in casel-5.txt and the published [CASEL framework](https://casel.org/what-is-sel/). The [EEF guidance, PDF page 6, printed page 4](https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/primary-sel/EEF_Social_and_Emotional_Learning.pdf) also includes values in self-awareness.

**Why it matters:** A scope writer can follow these rows faithfully and still build incomplete coverage.

**Exact fix:**

1. In units 1, 10 and 13, add what matters to the invented character to the chain task. Students explain how that value helps account for the character’s thought and feeling. Preserve each year’s present depth: one character, two characters, then pressure surrounding change.
2. Add an unseen SA5 item requiring that connection, rather than only a replacement thought.
3. In unit 18, require a fictional example showing how a cultural or linguistic strength helps with a new-school task. Students identify the strength and explain its contribution. Personal examples remain optional.
4. Amend the corresponding progression notes. Keep the standards in their current units.

### 2. The leave-out rule misses a new dependency and several carried models

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, K to 2 second-model finding 3; combined expert finding M3  
**Confidence:** firm for the missing dependency; likely for bridge timing

**Location:** Leave-out bullet, Models carried, and units 7, 8, 11 and 12.

Unit 7 introduces the grade 4 team working agreement. Unit 8 explicitly depends on it, and unit 7 says every later grade 4 team task runs on it. The leave-out list supplies no agreement bridge. Its claim that grade 4 and grade 5 cards are already known from grade 3 cannot cover this new grade 4 product.

The model register also omits the refusal and upstander cards despite their repeated use and onward handoff. Other recurring routines, including the care steps and focus plan, are described in units without a consolidated fallback.

**Why it matters:** A school can exercise the permitted omission and encounter a later unit that assumes the omitted teaching.

**Exact fix:**

- Add a unit 8 bridge: if unit 7 was omitted, use the first Understanding session to establish a minimal agreement about choosing together and sharing jobs. Name the minutes it replaces and claim none of unit 7’s omitted coverage.
- Replace the blanket grade 4 and grade 5 assurance with a check for whether the required model was actually taught.
- Add the refusal card and upstander plan to Models carried: introduced in unit 5, refusal reused in units 11 and 16, upstander options reused in units 11 and 17, then grown in grades 6 to 8.
- Extend the leave-out table to identify the receiving unit and fallback for each required recurring routine, including care steps, focus plan and the working agreement.

Use the subject’s one-step bridge rule. A bridge does not restore the omitted unit’s standards claim.

### 3. The short path places two checks in core check weeks

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** new  
**Confidence:** firm

**Location:** Days bullet and Course-level checks; comparison with calendar.csv.

With one session per week, the final session of each unit falls in its cumulative session-number week. The stated allocations produce:

| Grade | Short-path allocation | Check position | Conflict |
|---|---|---|---|
| 4 | 6, 6, 5, 5, 5, 5 | After unit 11, week 27 | Core course-level check week |
| 5 | 6, 6, 5, 5, 5, 5 | After unit 15, week 17 | Core course-level check week |

The stored calendar describes the full path and therefore does not expose these conflicts.

**Why it matters:** The advertised short path cannot meet the same calendar rule by inheriting full-path check positions.

**Exact fix:** Keep 32 sessions and all groups, but redistribute the additional rehearsals as follows:

| Grade | Revised short-path unit sessions | Mid-year check | Year-end check |
|---|---|---|---|
| 4 | 5, 5, 5, 6, 5, 6 | After unit 9, week 15 | After unit 11, week 26 |
| 5 | 5, 5, 5, 6, 6, 5 | After unit 15, week 15 | After unit 17, week 27 |

A five-session two-group unit retains two combined Understanding/Fluency sessions, one additional rehearsal, Application, and combined Check/Respond. A six-session three-group unit adds one Fluency session to its five-session form.

Write these short-path weeks explicitly. They avoid current core check weeks; coordination with other after-core subjects remains the lead’s calendar task.

### 4. Widened checks exceed their stated sampling limit

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, combined expert finding M2  
**Confidence:** firm on the contradiction; likely on classroom timing

**Location:** Evidence bullet; Course-level checks, especially lines 210 and 215 to 219.

The rule permits one or two sampled items beyond the unit assessment. Several cells specify three sampled demands, and some add another rehearsal, such as coached calm-down work, beside the assessed unit’s rehearsal.

The frame allows about 20 working minutes within the 30-minute session. Its provision to observe pairs during Application helps, but the check cells still promise more than the general rule permits.

**Why it matters:** Writers receive conflicting instructions about page length and observation load.

**Exact fix:**

- Set one cap: at most five written scenario items overall, including at most two sampled items, plus the assessed unit’s rehearsal.
- Keep additional rehearsal sampling in later retrieval openings or Application.
- Use these two written samples per check:

| Check | Samples retained |
|---|---|
| Grade 3 mid-year | Character’s feeling and clue; skipped calm-down step |
| Grade 3 year-end | Snap-judgment check; four-part I-statement |
| Grade 4 mid-year | Club rule from two sides; two paths for two characters |
| Grade 4 year-end | Two characters’ chains; fitting check-in |
| Grade 5 mid-year | Balanced thought; backup plan |
| Grade 5 year-end | Check-in; compromise |

Move the extra grade 3 unit 6 if-then sample into unit 8’s opening, and the grade 4 unit 12 source-check sample into unit 15’s opening. Update the paragraph promising those samples at the next mid-year check.

Require the scope to budget remaining pair observations explicitly, using the existing Application observation provision.

### 5. The library transfers remain outside the ownership record

**Severity:** Moderate  
**LAYER:** progression, frame  
**REPEAT:** yes, K to 2 second-model finding 4, applied only in part  
**Confidence:** firm

**Location:** Standard bullet, Library subsection, For the lead 3, units 14 and 17, and the three grade 5 progression rows.

The frame acknowledges three agreed responsibilities, but their codes remain only in prose:

| Code | Owner row | Unit |
|---|---|---:|
| `AASL.V.D.1` | `g5-sm-stay-on-task` | 14 |
| `AASL.V.D.2` | `g5-sa-skills-grow` | 14 |
| `AASL.III.D.2` | `g5-rel-teamwork` | 17 |

Library STANDARD section 4 and library-excluded.csv place them in SEL. The SEL validator still recognizes only casel-5.txt and gives band ownership treatment only to CASEL codes.

**Why it matters:** The structural pass cannot verify these transferred standards. This is an acknowledged shared-data gap, rather than evidence that the frame omitted their activities.

**Exact fix:** The lead should add narrowly scoped recognition and band ownership treatment for these three codes. Then record them in the stated progression standard cells and Units table ownership cells, with an explicit evidence look-for for each. Replace the pending prose after the change passes.

### 6. The health seam still specifies competing shared cards

**Severity:** Moderate  
**LAYER:** frame, process  
**REPEAT:** yes, combined expert findings M1 and M4  
**Confidence:** firm

**Location:** Shared steps bullet, unit 4, Health subsection and For the lead 4; health frame unit 4 and its SEL table.

SEL and STANDARD section 7 use “I need ___.” Health still uses “Please ___.” The listening routines also differ, and health calls its grade 4 refusal card newly introduced although SEL teaches refusal in grade 3.

Health’s grade 4 and grade 5 SEL references use year-local unit numbers. For example, “SEL unit 4” for grade 4 actually means this frame’s unit 10.

**Why it matters:** Following both frames produces competing wording and misleading retrieval references.

**Exact fix:** Apply the already proposed shared-card reconciliation on the health side:

- Use the four-part “I feel, when, because, I need” frame.
- Identify the common talk-card steps and distinguish any additional health listening practice.
- Treat grade 4 refusal as retrieval and health application of the earlier routine, preserving health’s explicit permission to refuse without giving a reason.
- Cite SEL band unit numbers with the grade beside them throughout health’s seam table.

Retain both courses’ provision to supply the necessary teaching when the other course is absent.

### 7. Friendship rehearsals contradict the stated role restriction

**Severity:** Moderate  
**LAYER:** frame, progression  
**REPEAT:** yes, the earlier progression review addressed safe rehearsal roles  
**Confidence:** firm

**Location:** Unit 4’s friendship rehearsal and teacher notes; corresponding friendship rows, especially `g3-rel-friendships`; unit 16’s two friendship talks.

Unit 4 expressly assigns a partner to play the friend who was hurt, while its teacher notes say the teacher plays any upset or hurt part. Unit 16 asks for both talks to be rehearsed with a partner, including the conditional friend who demands exclusion, while reserving pressure roles for the teacher or a card.

**Why it matters:** The activity wording directs a writer toward roles the accompanying safeguard excludes.

**Exact fix:** Rewrite these rehearsal clauses consistently:

> The teacher or scene card supplies the hurt or pressuring character’s words. The student rehearses the repair, boundary or refusal. A partner serves as a neutral listener or rehearsal coach, using the step card.

Apply the same wording to the corresponding progression notes. Preserve ordinary partner disagreement practice where both roles have legitimate, low-stakes positions.

### 8. Unmarked status notes and one file pointer are stale

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, combined expert finding m1 and K to 2 second-model finding 8  
**Confidence:** firm

**Location:** Frame lines 124, 305, 309 and For the lead 2 and 5; subject-bar SEL status row.

The stale checker passes, but:

- The grades 6 to 8 frame exists.
- Computer science grade 5’s frame exists. Its `g5-team-project` row is in unit 3, weeks 11 to 17.
- PE’s seam now names the SEL units; the claim that its pending notes still fail is outdated.
- `g6-sa-name-feelings` now explicitly grows the earlier strength scale.
- The subject bar still owes the completed SEL progression, validator work and session-arithmetic decision.
- The frame points to `data/plans/library-excluded.csv`; the actual file is `data/progressions/library-excluded.csv`.

**Exact fix:** Replace the affected notes with the current placements and status. Correct the library path. Rewrite For the lead 2 to distinguish the corrected feelings row from the remaining upstander step-up wording, which still understates prior learning. In the subject bar, state that progression and validator support are complete and session arithmetic was settled in q-fix-sel-1.

Do not rewrite dated review reports.

## Lens checklist, frame layer

| Requirement | Judgment |
|---|---|
| Distinct cases and increasing depth by grade | Met |
| Every selected sub-skill placed once | Met |
| Standards taught in full | Missed in the identified components, finding 1 |
| Earlier skills return | Planned through retrieval, Application and carry-out cues |
| Minutes and short path stated | Met arithmetically; short-path calendar needs finding 3 |
| Carry-out cue and family activity per unit | Met |
| A unit can be omitted without breaking later work | Partly met, finding 2 |
| Self-management and relationship skills rehearsed | Met in the planned activities |
| Stable shared names and steps | Incomplete across health, finding 6 |
| Health topics handed to health | Met |
| Checks assess skills rather than feelings or traits | Met in intent; check load needs finding 4 |
| Invented cases and optional personal sharing | Met |
| Safe rehearsal roles | Contradictory in the identified tasks, finding 7 |
| Disclosure route and sensitive-topic notes | Met at frame level through the health reference |
| Growth explained through practice, strategy and help | Met |
| Calming routines use plain physical framing | Met |
| No student identity sorting or required disclosure | Met |
| No unsupported effectiveness claim | Met |
| Day-level language support and accommodations | Specified by APPROACH; implementation awaits later layers |

## What is right and should not be touched

- Six distinct units per grade, complete row placement and reciprocal progression links.
- Grouping related sub-skills while retaining active rehearsal.
- The progression from school-day cases to another person’s view and then social cost or change.
- Invented characters, private interest pages and optional personal sharing.
- Explicit bridges when ELA or social studies teaches a related idea later.
- The paper path, temporary working sheets and concrete family activities.
- Grade 5’s use of counts rather than percentages.
- The choice of Brown v. Board of Education as a settled historical case. The [National Archives source](https://www.archives.gov/milestone-documents/brown-v-board-of-education) confirms the 1954 ruling. The eventual page should distinguish the ruling from subsequent implementation.

The rehearsal, sequencing and transfer provisions are consistent with the design principles in the [CASEL criteria paper, PDF pages 23 to 25](https://files.casel.org/11_CASEL-Program-Criteria-Rationale.pdf) and [EEF guidance](https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/primary-sel/EEF_Social_and_Emotional_Learning.pdf). This supports the design choices, without establishing effectiveness for this course.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Add the character’s value to SA5 cases | Completes the existing standard within its current units | Frame units 1, 10 and 13; matching progression notes |
| Require a fictional cultural or linguistic strength in unit 18 | Completes SA2 without requiring disclosure | Frame unit 18; `g5-sa-my-strengths` |
| Use the short-path allocations in finding 3 | Retains 32 sessions and all groups while avoiding current core check weeks | Frame Days and Course-level checks |
| Cap sampled check items at two | Resolves the frame’s internal contradiction | Frame Evidence and Course-level checks |
| Use neutral rehearsal partners for the identified friendship tasks | Makes the activity agree with its safeguard | Frame and corresponding progression notes |
| Retain the independent core-subject bridges | Later core teaching need not block SEL | No change needed |

These are recommendations for the caller to apply. No edits were made.

## For Cory

1. **Annual check placement, scope:** The K to 2 fix report already leaves this decision with Cory. Here, each “year-end” course check also precedes an entire eight-sub-skill unit, with later sampling partly deferred to another grade. The combined expert read accepts that pattern; it does not remove the outstanding scope decision. Record explicitly whether that annual assessment structure is accepted or whether meeting frequency and check placement must change. This report does not count the previously deferred question as a new defect.
2. **Supply ceiling, money:** The provisional printing and supply figures still have no SEL ceiling. No spending decision was made.

## What I could not judge

- Actual session timing, marking throughput and combined Check/Respond delivery before scopes and items exist.
- Final accessibility, Spanish accuracy, cultural representation and safety implementation.
- Whether the later cultural examples have adequate sources, since their places and specific practices remain to be chosen.
- Effectiveness of the course. No study of these materials was reviewed.
- Final coordination among all after-core courses. Their existing clashes belong to the lead’s calendar pass.

## Outside sources and source-list follow-up

All sources below were checked live. No curricular finding rests on model memory.

| Source | Use and limit |
|---|---|
| [CASEL framework](https://casel.org/what-is-sel/) | Checked competency components, especially values and cultural and linguistic strengths |
| [CASEL criteria paper](https://files.casel.org/11_CASEL-Program-Criteria-Rationale.pdf) | Consulted design passages on grade sequences, active practice, transfer and stated annual sessions |
| [EEF primary SEL guidance](https://d2tic4wvo1iusb.cloudfront.net/production/eef-guidance-reports/primary-sel/EEF_Social_and_Emotional_Learning.pdf) | Consulted self-awareness and SAFE guidance; not read cover to cover |
| [National Archives: Brown v. Board of Education](https://www.archives.gov/milestone-documents/brown-v-board-of-education) | Checked the ruling, date and distinction between decision and implementation |

For the source list: record the working EEF PDF address and the CASEL framework redirect, with the limited reading coverage above. Prior workspace memory was used only for report-format conventions.

