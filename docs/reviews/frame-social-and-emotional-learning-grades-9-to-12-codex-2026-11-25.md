# Second-model cold read: Social and Emotional Learning, Grades 9 to 12

**Date:** 2026-11-25  
**Course:** `social-and-emotional-learning-grades-9-to-12`  
**Findings:** 8  
**Mode:** Read only. No files created, edited or deleted.

## Verdict

The frame has a sound annual structure: all 160 assigned progression rows appear exactly once, each year has six units and its own assessments, and the calendar agrees with 64 sessions per year. It needs targeted repairs before scope writing, chiefly to preserve shared routine wording and make the authorized leave-out route work without reteaching omitted content. Fix those instructions first, then close the narrower coverage, evidence and source-preparation gaps below.

## What I read

- `docs/pipeline/briefs/frame-read.md`, the after-core provisions in `frame-write.md`, `docs/agents/EXPERT.md`, the SEL lens, FOUNDATION, relevant production-path and BASELINE rules, and the shared approach.
- The [complete course frame](S:/CurioClass/docs/courses/social-and-emotional-learning-grades-9-to-12/frame.md), its `course-list.csv` selector, `frames.csv` entry and calendar rows.
- SEL STANDARD and APPROACH, adoption-bar part 9 and shared criteria, `casel-5.txt`, and all 160 selected progression rows.
- The preceding band’s outgoing seam and carried models, corresponding grade 8 rows, and reciprocal links within this band. There is no subsequent SEL course.
- Referenced core-course Units tables and relevant mathematics, health, PE, library and computer science placements.
- SEL pre-work, progression and earlier frame reviews, including the combined grades 3 to 12 expert report and the adjacent-band second-model reports.
- The outside sources linked below.

No base text is claimed. A base-lesson source map is therefore not applicable.

## Checks and counts

Commands used bytecode suppression. The plan check was course-filtered to honor AGENTS.md’s prohibition on unfiltered runs.

| Check | Result |
|---|---|
| `scripts/plan.py check social-and-emotional-learning-grades-9-to-12` | Failed because the frame-stage course lacks `days.csv` with `parts.csv` or `items.csv`; review proceeded |
| `scripts/frame.py check social-and-emotional-learning-grades-9-to-12` | Passed, zero failures |
| `scripts/stale.py check` | Passed, 121 files, zero failures |
| Targeted stale check on the frame, SEL standard, approach and progression | Passed, zero failures |
| `scripts/progression.py check sel` | Passed, 520 rows, zero failures |
| Independent row-placement count | 160 distinct assigned rows, each placed once; no missing or extra rows |
| Reciprocal progression links | No broken incoming links among the selected rows |
| Ownership | All 40 SEL codes owned in grade 12; grades 9 to 11 begin them |

| Grade | Units | Sub-skills per unit | Sessions in Units table | Check/respond sessions | Total |
|---|---|---|---:|---:|---:|
| 9 | 1 to 6 | 6, 6, 5, 7, 8, 8 | 60 | 4 | 64 |
| 10 | 7 to 12 | 5, 6, 7, 6, 8, 8 | 60 | 4 | 64 |
| 11 | 13 to 18 | 5, 8, 5, 7, 7, 8 | 60 | 4 | 64 |
| 12 | 19 to 24 | 5, 6, 6, 8, 7, 8 | 60 | 4 | 64 |

The calendar places each mid-year check on school day 75 and its respond session on day 78. Year-end checks occupy days 158 and 160 in the permitted week 32 finals period. The 32-session short path retains all six units in each year.

## Findings, most serious first

### 1. The high school I-statement replaces the shared wording

**Severity:** Serious  
**LAYER:** frame, progression  
**REPEAT:** yes, combined expert finding S1 remains unresolved  
**Confidence:** firm

**Location:** Frame lines 13, 14, 137 and unit 4; progression row `g9-rel-friendships`.

STANDARD section 7 requires one set of words across SEL, health and PE. The preceding band hands on:

> I feel ___ when ___ because ___. I need ___.

The frame says it adds a request and check-back, but instead changes the order and substitutes “I would like” for “I need,” while dropping “because.” The Leave-out bullet still calls this a four-part frame.

**Why it matters:** Writers following these instructions will produce competing cards for a routine meant to remain familiar across courses.

**Exact fix:** Use this wording consistently:

> I feel ___ when ___ because ___. I need ___. Does that work for you?

Apply it in Shared steps, Models carried, unit 4 and `g9-rel-friendships`. Describe the request as already present in “I need,” and the check-back as the added fifth part. Update the Leave-out description and downstream references accordingly. This implements the earlier settled repair without moving a standard.

### 2. Leave-out bridges teach the wrong depth and miss an immediate receiver

**Severity:** Serious  
**LAYER:** frame  
**REPEAT:** yes, incomplete leave-out dependencies recur in the earlier SEL second-model reads  
**Confidence:** firm

**Location:** Days and Leave-out bullets, lines 8 and 14; units 1 and 2; Models carried.

STANDARD section 5.6 requires a later unit to bridge an omitted card through its **one-step form** in the first ten minutes. The frame instead instructs it to teach the card’s full “9 to 12 form.”

The bridge list also sends unit 1’s six-step decision routine first to units 3 and 5. Unit 2 already uses its look-back step to judge the stressor pilot. Omitting unit 1 therefore breaks the next unit’s stated work.

Late entry is also described as a `Given:` case followed by teaching during the first Understanding session, without separating the readiness evidence from the response to it.

**Why it matters:** A school exercising the permitted omission can encounter an unprepared dependency immediately. The full high school bridge also claims more teaching than the settled ten-minute provision permits.

**Exact fix:**

- Replace “the card’s 9 to 12 form” with “the card’s one-step form.”
- Name unit 2 as the first receiving unit for unit 1’s look-back routine and support-map use.
- In unit 2, specify the minimal bridge: model identifying the problem, choosing a next step and checking what happened. State which opening and rehearsal minutes it replaces.
- Check every later receiver against Models carried, including the inherited refusal, fairness and upstander cards.
- Separate late-entry readiness evidence from reteaching. Use the subject’s `Given:` provision only when the earlier form was not used in the preceding year; otherwise use retrieval.
- Retain the statement that these bridges claim none of the omitted unit’s sub-skills.

### 3. Some annual teaching narrows a sub-skill before its owner year

**Severity:** Moderate  
**LAYER:** frame, progression  
**REPEAT:** yes, partial treatment despite complete placement recurs in earlier SEL reads  
**Confidence:** firm for the omissions; likely for their effect on later writing

**Location:** Units 1, 3, 11, 14 and 16; corresponding progression notes.

The owner year explicitly includes materials organization and cultural strengths. Earlier years still promise full teaching rows at their own depth, but two components are not secured:

| Sub-skill | Gap | Exact fix |
|---|---|---|
| SM5, planning and organization | Units 1, 11 and 14 emphasize calendars, commitments and handoffs without explicitly teaching how to keep materials organized. | Add a materials system to each existing planning task: a ninth grader’s assignment folder, a team’s shared files and handoff records, and an overloaded student’s project materials. Students explain how that system supports the plan. |
| RS3, working across cultures | Units 3 and 16 can be satisfied by differences between schools or individual work habits, without a cultural difference. | Require one culturally situated invented case in each unit, with individual preferences stated and respectful adaptation practiced. Keep personal cultural disclosure optional. |

The [published framework](https://casel.org/what-is-sel/) includes cultural competence and organizational skills; the repository’s own standard statements retain those components.

For a concrete RS3 case, an invented Deaf and hearing team could negotiate communication preferences and turn-taking. The [Deaf-Hearing Communication Centre’s guidance](https://www.dhcc.org/resources/communication-tips) supports asking individual preferences. Use case cards, with no simulation of hearing loss or requirement to perform another identity.

Also align `g9-sa-feel-think-link` and `g10-sa-feel-think-link` with the frame’s improved wording: their progression notes still omit the explicit connection to what the characters value.

Keep all existing unit placements and session totals.

### 4. The evidence plan does not secure checks of several owner-year skills

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, the adjacent-band second-model read identified the same evidence-placement problem  
**Confidence:** likely

**Location:** Evidence bullet, unit 20 and Course-level checks.

Unit 20 owns SA3, SA8, SM1, SM2, SM3 and SM5. Its named end evidence is a coping-plan page and correction-response rehearsal. Those forms clearly address coping and managing a strong feeling, but do not identify where growth through practice and help, self-directed focus, or materials organization are checked. The subsequent course-level sample again names a coping plan.

The generic class sheet could hold that evidence, but the frame does not assign those skills to a particular evidence opportunity. Similar uncertainty remains in the wider project units.

**Why it matters:** A scope writer may preserve every teaching activity while checking only the most visible part of a unit.

**Exact fix:**

- In unit 20, assign SA8 to a new invented practice-log response, SM3 to a focus-plan revision, and SM5 to a changed-month planning task that includes organizing materials.
- Place those checks in the relevant Application sessions after teaching and practice. Keep the coping page and response rehearsal as the closing evidence.
- Add the same brief allocation to every owner-year unit: which skills are checked during Application and which during Check.
- Require an individual look-for within pair work.
- Keep cumulative sampling to two brief written items. Set a timed limit on unfinished rehearsals entering Check, and give the shared short-path Check/Respond session its own minute budget.
- Preserve APPROACH’s writing, card-supported and teacher-supported response alternatives.

This is an evidence-design risk, not a demonstrated timing failure. A timed unit-plan probe must settle feasibility.

### 5. Three transferred library standards remain outside ownership checking

**Severity:** Moderate  
**LAYER:** progression, frame  
**REPEAT:** yes, earlier SEL second-model finding on library transfers  
**Confidence:** firm

**Location:** Standard bullet; Library subsection; For the lead 3; units 20 and 21.

The frame names the agreed transfers, but they remain in prose rather than the progression’s standard cells and the Units table’s Owned standards cells.

| Transferred code | Receiving owner row | Unit |
|---|---|---:|
| `AASL.V.D.1` | `g12-sm-stay-on-task` | 20 |
| `AASL.V.D.2` | `g12-sa-skills-grow` | 20 |
| `AASL.III.D.2` | `g12-rel-teamwork` | 21 |

The current SEL validator recognizes CASEL codes only. Its passing result therefore does not verify these responsibilities.

**Why it matters:** The standards have been removed from library ownership without reaching an equally checkable receiving record.

**Exact fix:** The lead should add narrowly scoped validator recognition and band ownership handling for these three transfers, then enter them on the stated rows and units with their teaching and evidence. Do not expand SEL ownership to the rest of the library framework.

Correct the file pointer from `data/plans/library-excluded.csv` to `data/progressions/library-excluded.csv`.

### 6. Required preparation sources are deferred rather than named

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier SEL reads identified incomplete historical and cultural preparation sources  
**Confidence:** firm

**Location:** Base text, Safety and Sensitivity reads bullets; units 5, 9, 18 and 22.

The frame gives court and museum categories for later agents to search, rather than a complete preparation pack. It also directs the safety agent to find an unnamed state guide. Frame-write requires named sources and a titled, linked safety guide.

**Why it matters:** Different writers can build materially different historical accounts or safety assumptions from the same frame.

**Exact fix:** Replace the search instructions with a source table containing the exact page, community concerned and purpose:

| Unit | Concrete source repair |
|---|---|
| 5, Mendez | Add the [U.S. Courts account containing Sylvia Mendez’s own words](https://www.uscourts.gov/data-news/judiciary-news/2024/09/26/mendez-v-westminster-how-a-young-girls-courage-transformed-schools). Name Mexican American families and the Mendez family’s Mexican and Puerto Rican heritage in the preparation note. |
| 9, Brown | Add the [National Archives opinion page](https://www.archives.gov/milestone-documents/brown-v-board-of-education) and [Cheryl Brown Henderson’s account](https://www.brownvboard.org/brown-foundation-story). Name Black American plaintiffs and families. Distinguish the constitutional ruling from subsequent implementation. |
| 18, Morgan | Replace the unread Oyez dependency with the [Library of Virginia account](https://www.lva.virginia.gov/collections/educator-resources/changemakers/items/show/44). Name Black American interstate passengers and require a separately identified community account before teaching specific personal costs. |
| 22, Heart of Atlanta | Add the [Library of Congress exhibition section](https://www.loc.gov/exhibits/civil-rights-act/immediate-impact.html#obj204). Say “covered public accommodations” rather than the broader “public places.” Its linked civil-rights testimony supplies a concrete community-source route for the sensitivity reader. |
| Pilot and service units | Name and link [Colorado’s Field Trips and Extracurricular Activities: School Nurse Checklist](https://ed.cde.state.co.us/shs/fieldtrips), alongside local policy. Carry its relevant accessibility, health-support, emergency-response and environmental considerations into the activity plan. It does not replace a cleanup-specific hazard check. |

The Morgan Oyez URL was inaccessible through the tool; the Heart of Atlanta URL returned no readable case text. They were not fetched another way. Mark those original references **browser check**, with the readable alternatives above.

### 7. Living notes still describe completed work as absent

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, combined expert finding m1 remains unresolved  
**Confidence:** firm

**Location:** Cross-subject lines 187, 238, 256 and 272 to 281; For the lead 5, 8 and 12; adoption-bar SEL status row.

The stale checker passes, but manual inspection finds completed work still described as pending:

- Computer science grades 11 and 12 have frames.
- PE’s SEL seam now cites this frame and its relevant units.
- The two band-edge seam tables agree on all 40 links.
- The adoption-bar status row still owes the completed progression and settled session arithmetic.
- Several calendar references name nonexistent `docs/plans/calendar.csv`.

**Exact fix:**

| Note | Replacement |
|---|---|
| Computer science grade 11 | `g11-algorithm-ethics` is in unit 5, course days 49 to 55, weeks 25 to 28. SEL teaches its own trip-date case. |
| Computer science grade 12 | `g12-team-workflow` is in unit 3, days 25 to 46, weeks 13 to 23. `g12-career-goals` and `g12-diverse-teams` are in unit 5, days 57 to 64, weeks 29 to 32. Each course teaches its own needed routine; a team may adopt the SEL charter once available. |
| For the lead 5 | “PE now names SEL’s goal plan, response plan, team charter and balanced week, with its own fallback where SEL is unavailable.” |
| For the lead 12 | “The grade 8 outgoing and grade 9 incoming seam tables agree on all 40 rows.” |
| Adoption-bar SEL status | State that the progression and validator support are complete and session arithmetic was settled through `q-fix-sel-1`. |
| Calendar pointers | Replace `docs/plans/calendar.csv` with `data/plans/calendar.csv`. |

Do not rewrite the dated review reports.

### 8. “Every unit … sampled twice” overstates the assessment design

**Severity:** Minor  
**LAYER:** frame  
**REPEAT:** yes, combined expert finding m4 remains unresolved  
**Confidence:** firm

**Location:** Course-level checks, line 172.

Each year’s third and sixth units receive their own assessment through the course-level check. They are not sampled again within that year. Earlier units receive their own assessment and one later sample.

**Why it matters:** The claim overstates cumulative coverage and can mislead later assessment planning.

**Exact fix:** Replace the sentence with:

> Every unit receives its own end-of-unit assessment. The first, second, fourth and fifth units of each year are sampled once more in that year’s course-level checks. The third and sixth units are assessed through those checks.

Do not imply that every code is sampled.

## Lens checklist, frame layer

| Lens requirement | Result |
|---|---|
| Distinct years with growing depth | Met: school-day plans, another person’s view, costs and pressures, then settings past school |
| Every sub-skill placed, with return practice | Placement met; annual breadth needs finding 3’s repairs; carried routines provide return practice |
| Minutes stated; short path retains units | Met |
| Carry-out cue and family activity for every unit | Met |
| A school can leave out a unit without breaking later units | Missed, finding 2 |

The wider lens supports the concerns about shared wording and evidence placement. Health boundaries, invented cases, private personal pages, nonclinical language and safe upstander roles are otherwise explicitly protected.

## What is right and should not be touched

- The Year column, continuous unit numbering and complete annual structure.
- All 160 row placements and reciprocal progression links.
- Six units and 64 sessions per year, with assessment and Respond time included.
- The distinct grade-year depth and grade 12 transition emphasis.
- Paper delivery, no student accounts, and disposal of teacher working sheets after their stated purpose.
- The 18-and-over family-note and leave-out provision.
- Grade 12 civic voice through an invented graduate’s case, and RS9 through a school case with written transfer to work.
- The statement that no study has tested this course.

No whole unit is clearly far overallocated. The main pacing uncertainty concerns collecting individual evidence within closing sessions.

I do not adopt the earlier combined report’s claim that revisiting Brown necessarily prevents growth. Grade 10 can revisit it through affected people’s perspectives and a redesigned norm. Identify that as a deliberate return with a new question and evidence demand.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Preserve the inherited I-statement and add only the check-back | Maintains the shared routine | Frame; `g9-rel-friendships` |
| Use one-step leave-out bridges and name unit 2 as an immediate receiver | Implements STANDARD section 5.6 | Frame |
| Add materials organization and culturally situated collaboration within existing tasks | Restores breadth without moving standards | Frame; affected progression notes |
| Allocate owner-year evidence between Application and Check | Prevents broad teaching from receiving narrow checks | Frame; later scope and unit plans |
| Retain Brown as an explicit revisit at new depth | Repetition of a case does not require repetition of the learning | Frame |
| Correct current status notes and the sampling claim | Aligns living instructions with repository evidence | Frame; adoption-bar status row |

## For Cory

- **Money:** The supply ceiling remains unset. The frame estimates about $60 per year in printing, plus up to $20 per pilot or service task. Retain provisional figures until unit plans establish quantities.
- **Scope:** The existing grading-or-credit question remains open. This read makes no decision about credit for the advisory course.

## What I could not judge

- Actual completion time for written checks and individual rehearsal observations, especially on the short path.
- Finished historical adaptations, cultural cases, translations and accessibility supports.
- Specific off-site activities without a site, local policy and activity plan.

These require unit plans, finished materials or a timed probe. No curriculum finding rests on unverified memory.

## Outside sources and source-list follow-up

- [CASEL framework](https://casel.org/what-is-sel/): checked competency breadth and the cultural and organizational components.
- [CASEL criteria, December 2020, pages 23 to 25](https://files.casel.org/11_CASEL-Program-Criteria-Rationale.pdf): checked grade-by-grade programming, active practice and stated annual sessions.
- [Education Endowment Foundation SEL toolkit](https://educationendowmentfoundation.org.uk/education-evidence/teaching-learning-toolkit/social-and-emotional-learning): checked the dose rationale. Its synthesis describes sessions up to 45 minutes twice weekly; it does not establish effects for this course.
- Historical, community, communication and safety sources are linked beside their uses in findings 3 and 6.

**For the source list:** Record the newly identified historical, community, communication and safety pages as references, with their access results and no assumed adaptation permission. Record that the older CASEL framework address redirects to the current page above.