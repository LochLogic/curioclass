# Independent expert read: social studies kindergarten scope and sequence

**Date:** 2026-11-14  
**Intended report path:** `docs/reviews/sequence-social-studies-kindergarten-2026-11-14.md`  
**Delivery:** Complete report here. No files changed.

## Verdict

The sequence has a coherent six-unit arc, appropriate kindergarten access, and a workable placement of its course-level checks. Revise before approval: its greatest risk is that assessment descriptions claim standards whose required performances they do not fully elicit. Preserve the unit allocations, but make the teaching and observation requirements explicit and reconcile the calendar before unit writing proceeds.

## What I read and checked

Read in full:

- [Scope and sequence](/S:/CurioClass/docs/courses/social-studies-kindergarten/scope-and-sequence.md), [days.csv](/S:/CurioClass/data/plans/social-studies-kindergarten/days.csv), and [course frame](/S:/CurioClass/docs/courses/social-studies-kindergarten/frame.md).
- All 19 kindergarten social studies progression rows and their receiving grade 1 rows.
- `docs/agents/EXPERT.md`, the social studies lens, the shared and social studies adoption criteria, and `docs/courses/social-studies/STANDARD.md`.
- The calendar rules and kindergarten entries for all four subjects in `data/plans/calendar.csv`.
- Both earlier kindergarten frame reviews.

Also consulted FOUNDATION, the relevant ROADMAP path and gaps, BASELINE rules 20 to 24, the shared approach, source-list evidence notes, glossary, base-text record, sequence briefs, relevant earlier progression and baseline reports, and the calendar-generation code. Inspected the other kindergarten subjects’ relevant frame entries. Their daily sequence files do not yet exist.

Outside reading included the official Massachusetts and C3 requirements, California’s kindergarten standards, the social studies materials criteria, and two published kindergarten inquiry examples. Sources and access limits appear below.

| Check | Result |
|---|---|
| `python -X utf8 scripts/plan.py check` | Did not complete: another course lacks its sequence file, then checking stopped on missing dependency `markdown`. |
| `python -X utf8 scripts/frame.py calendar` | Completed; kindergarten social studies checks fall in weeks 15 and 30, with no reported stagger break. |
| `python -X utf8 scripts/frame.py check social-studies-kindergarten` | 0 failures. |
| `python -X utf8 scripts/plan.py check social-studies-kindergarten` | 0 failures. |
| `python -X utf8 scripts/stale.py check` | Did not complete: `KeyError: 'node'`. |

These results do not withhold the curriculum verdict. No turn acquisition, defect logging, synchronization, installation or file writing was attempted because this review is read-only.

## Findings, most serious first

### 1. The unit assessments do not secure the full performances their codes claim

**Severity:** Major  
**LAYER:** sequence  
**REPEAT:** yes, semantic coverage and assessment mismatches recur in `progression-social-studies-codex-2026-11-13.md` and the earlier kindergarten frame review.  
**Confidence:** Firm on the direct mismatches; likely on requirements left implicit.

**What is wrong.** The assessment rows attach broad code lists to narrower tasks. The clearest examples are day 29, which substitutes identifying a map or globe for explaining their similarities and differences, and day 50, which samples one symbol while claiming all four symbol parts. These distinctions follow the [Massachusetts framework, printed pages 33 to 35](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf#page=33).

The same problem appears elsewhere:

| Unit and location | Evidence the current assessment does not secure | Exact repair inside existing days |
|---|---|---|
| 1, days 8 and 9 | Following ordinary class rules with little prompting; comparing the child’s own view with another view. Giving a reason and asking a classmate a question do not establish both. | Name routine rule-following observations and add a brief “My view is …; my classmate’s view is …” comparison. Record discussion behavior separately from the spoken answer. |
| 2, days 17 and 18 | Carrying out a responsibility helpfully and respectfully. Saying what a job is does not demonstrate follow-through. The character prompt also samples only fair or caring behavior. | Observe a real job being completed during day 17. Specify how observations across the closing lessons cover the character work taught on days 15 and 16. |
| 3, day 29 and its note | Map/globe comparison and locating the town and school on the two appropriate maps. The note incorporates products from days 25 and 26, but not the location work on day 28. | Add one similarity and one difference, with support. Explicitly retain each child’s day 28 location demonstration as assessment evidence. Preserve the map/model products. |
| 4, day 39 | “Time words” leaves the required time scales and event contexts unspecified. An assessor could use only first, next and last. | Name a small observation matrix covering the taught time language and personal, natural, story and informational sequences. Distribute observations across the closing lessons; day 39 completes missing evidence. |
| 5, day 50 | One symbol cannot establish each child’s understanding of the flag, eagle, anthem and Pledge. | Collect brief individual observations across days 45 to 50, explicitly covering all four parts. Use read-aloud excerpts or records where a photograph cannot carry the task. Day 50 completes gaps and includes the fresh-source task. |
| 6, days 58 to 60 | Sorting and naming do not guarantee an explanation of a constrained choice, questions about exchange, or the earned-money connection. The store note does not specify these look-fors. | Add named observations during day 58 and a short fresh choice/exchange prompt on day 60. Require a reason, rather than treating a successful purchase or sort as sufficient. |

The relevant C3 distinctions include comparing perspectives, explaining scarcity, and describing workers’ skills and knowledge. They require observable reasoning, beyond labels and participation. See the [C3 indicator tables](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf).

**Why it matters.** A unit writer can follow these descriptions exactly and produce an assessment that passes the structural gate while leaving important learning unobserved. The response day then has an incomplete basis for grouping children.

**Exact fix.** Amend the assessment descriptions and observation windows as above. Keep every unit’s current days and its single respond day. The unit plans should turn these named performances into items and a record sheet; this sequence review does not require finished items now.

### 2. Two owned C3 demands lose their explicit teaching between the progression and the day file

**Severity:** Major  
**LAYER:** sequence and progression  
**REPEAT:** yes, the same code-presence versus actual-work problem as progression review finding 1.  
**Confidence:** Firm on the requirements; likely on omission during teaching.

**What is wrong.**

- **D1.1.K-2:** Day 1 generates questions and posts the compelling question, but no day explicitly teaches children to explain why that question matters to them. The progression row includes that demand.
- **D2.Eco.3.K-2:** Day 53 mentions “skills” in its heading, but its task matches workers to work and tools. Neither that task nor day 60 explicitly asks what a worker must know and be able to do.

These are distinct requirements in the [C3 Framework, printed pages 23 and 36](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf). The economics progression row itself emphasizes skills and tools while leaving knowledge implicit.

**Why it matters.** Children can complete both activities without learning the reasoning attached to their codes.

**Exact fix.**

- On day 1, model and invite: “Finding this out matters to me because …”. Revisit it during day 9’s wonder-wall look back.
- On day 53, model one worker’s knowledge, skill and tool, then have children describe another example from photographs or a read-aloud. Add the same distinction to day 60’s observation.
- Clarify `ssk-work` in the progression so future writers retain knowledge as well as skills and tools.

These are completions of existing ownership, with no added days.

### 3. The informed-action sequence schedules a plan and a review, but not implementation

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the earlier kindergarten frame review identified an incomplete informed-action cycle.  
**Confidence:** Likely.

**What is wrong.** Day 14 ends with “plan the action.” Day 17 asks whether it helped. No intervening goal or note says when the class carries out its decision.

The frame and progression explicitly include acting. The daily record drops that step. Both the [C3 Framework’s classroom-action indicator](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf) and the published [Rules inquiry](https://c3teachers.org/inquiries/rules/) distinguish deciding from acting.

**Why it matters.** A busy writer could build a vote followed by hypothetical reflection, leaving the year’s only informed action incomplete.

**Exact fix.** End day 14 with the first practical step of the selected action. Its note should say that the agreed arrangement operates through normal classroom routines until day 17. On day 17, children use a simple before-and-after observation to judge its effect.

Retain the student-selected problem, eight-school-day interval and nine-day unit.

### 4. The shared calendar does not represent the sequence, and the holiday date promise needs a local placement rule

**Severity:** Moderate  
**LAYER:** process and sequence  
**REPEAT:** yes, calendar coordination recurs in the baseline structure review and holiday timing in both kindergarten frame reviews.  
**Confidence:** Firm on the discrepancies; likely on their classroom consequences.

**What is wrong.** The sequence correctly acknowledges that `calendar.csv` still comes from the frame. That unresolved issue affects the required shared planning record:

| Placement | `calendar.csv` | Actual `days.csv` |
|---|---|---|
| Unit 4 | School days 80 to 94 | School days 81 to 99, interrupted by a holiday lesson |
| Unit 5 | One block, school days 97 to 120 | Lessons on school days 34, 58 and 94, then the block on 102 to 120 |
| Unit 6 ending | School day 143 | School day 145 |

Reading `calendar_rows()` confirms that it derives placements from the frame rather than the daily overrides.

Separately, CALENDAR.md defines school days as positions, with each school supplying actual dates. Fixed positions 34, 58 and 94 therefore cannot guarantee the stated holiday dates. Day 42 also calls a combined Veterans Day and Thanksgiving lesson “On the day,” although those observances have different dates.

**Why it matters.** Other course writers cannot reliably coordinate against the shared calendar. Teachers also receive a stronger holiday-timing promise than the portable calendar supplies.

**Exact fix.**

1. Have calendar generation consume populated daily `school_day` values and emit separate unit segments for interrupted units. Taking only unit-wide minimum and maximum dates would still obscure the three early lessons.
2. Regenerate the shared calendar after that repair. Keep the current course-check weeks.
3. Describe the three holiday positions as provisional until a school overlays its dates. Give a short instruction for placing them on or near the local observance while preserving their unit ownership and day cost.
4. Rename day 42 a November holiday study, near Thanksgiving, with Veterans Day recalled retrospectively. Do not promise simultaneous on-date teaching.

The sequence writer has already identified the generator issue. This finding confirms that it remains unresolved, rather than treating the acknowledgment as a completed repair.

### 5. The required shorter path is absent

**Severity:** Moderate  
**LAYER:** sequence  
**REPEAT:** yes, the same feasibility requirement appears in `baseline-1-science-2026-11-14.md`, finding 6.  
**Confidence:** Firm on the omission; judgment call on the proposed route.

**What is wrong.** The sequence states 20 to 30 minutes per meeting but does not identify what is retained or shortened at the lower end. FOUNDATION section 5 and adoption criterion C2 require a shorter path.

**Why it matters.** When time is tight, the teacher must choose what to remove. Source discussion, individual evidence and response are especially vulnerable.

**Exact fix.** Specify a **20-minute route through the same 64 meetings**. Protect the source or model, one supported attempt, the named individual evidence and the closing explanation. Identify additional examples and repeated whole-class sharing as the first reductions. Keep every assessment and respond day.

Require unit plans to budget that route explicitly. This does not authorize fewer meetings or reduced standards.

### 6. Current prose contains stale counts and status statements

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale handoff statements recur in the earlier kindergarten frame review.  
**Confidence:** Firm.

**What is wrong.**

- The sequence opening says **three course-level check days and three respond days**. Its actual course-level allocation is **four check days and two respond days**.
- Unit 5 says every lettered symbol part has its own day. Parts c and d share day 47.
- The frame’s cross-subject introduction says the other subjects’ frames will be written later. They now exist.

**Why it matters.** These statements invite unnecessary rescheduling and make the current planning state harder to identify.

**Exact fix.**

- Replace the opening allocation with “58 unit days, four course-level check days and two course-level respond days.”
- Replace the symbol statement with “All four lettered parts are placed across days 45 to 47; the anthem and Pledge share day 47.”
- Update the frame introduction to identify the existing frames and shared calendar, while stating that exact lesson-level availability awaits their daily sequences.

The six unit respond days are already included in the 58 unit days. They must not be added again.

## Order, load, coverage and calendar conclusions

The main instructional order is sound. Rules and discussion routines precede collective decisions; position language precedes maps; timeline instruction precedes the main holiday block; and work and exchange build on jobs and classroom decisions. The three early holiday lessons do not themselves require the later timeline model.

| Unit | Total days | Teaching days before assessment/respond | Load judgment |
|---|---:|---:|---|
| 1 | 10 | 8 | Reasonable for four foundational rows and establishing routines. |
| 2 | 9 | 7 | Reasonable for jobs, texts and an action cycle; implementation needs finding 3’s repair. |
| 3 | 11 | 9 | Appropriate emphasis on language and constructed maps/models. |
| 4 | 7 | 5 | Compact: three sequence/time days and two comparison days. Protect practice and distribute observations. |
| 5 | 11 | 9 | Substantial content, including three earlier holiday lessons. Day 47 carries two symbol parts; assessment cannot rest on one sampled symbol. |
| 6 | 10 | 8 | Reasonable for work, choice, exchange and the store. Preserve reasoning within the practical activity. |

No whole unit is demonstrably far over or under its load. Equal days per progression row would be inappropriate.

All **19 owned skills, 16 Massachusetts parent standards and 17 C3 indicators** are placed. The six lettered Massachusetts parts also have explicit teaching placements. Findings 1 and 2 concern the performance behind those placements.

No unit exceeds 25 days, so no mid-unit assessment is required. Kindergarten has no earlier-grade course prerequisite requiring a readiness day.

The course checks occupy school days **73 and 75**, then **146 and 148**, matching weeks **15 and 30**. Responses occupy school days **78 and 150**. The other subjects’ reported check weeks preserve the kindergarten stagger.

### Same-year leans

| Lean | Social studies first use | Other subject’s calendar window | Judgment |
|---|---|---|---|
| SL.K.3 | Day 1, school day 3 | ELA unit 1, school days 1 to 34 | Local question model supplies the bridge. |
| SL.K.1 | Day 6, school day 14 | ELA unit 1 | Discussion rules are taught locally. |
| W.K.1 | Day 8, school day 18 | ELA unit 1 | Explicit oral bridge avoids assuming completed writing instruction. |
| RL.K.3 | Day 15, school day 36 | ELA unit 2, school days 35 to 76 | Picture-supported read-aloud bridge is present. |
| RI.K.3 | Day 34, school day 81 | ELA unit 3, school days 80 to 118 | Picture sequencing bridge is present. |
| RI.K.1 | Day 45, school day 104 | ELA unit 1 | Earlier unit window. |
| K.CC.B.5 | Vote on school day 29; store on 135 | Math unit 2, days 19 to 44; unit 6 ends 119 | Teacher-supported vote bridge; store follows both windows. |
| K.G.A.1 | Day 20, school day 47 | Math unit 3, days 45 to 63 | Social studies explicitly teaches the language itself. |

Unit windows do not prove an exact standard has already been taught. The bridges make the overlapping first uses defensible until daily sequences exist.

Every Candidate cell is settled with an in-day placement: day 2, day 16, days 24 to 26, day 38, day 44 and day 53. The state-location extension is correctly identified as unassessed extension work. No addition creates a separate uncounted day.

There is no adopted base text, so a base-lesson source map is **not applicable**.

## Scope and sequence lens checklist

| Lens line | Result |
|---|---|
| Compelling questions require the unit’s evidence and allow defensible answers | **Met at planning level.** Classroom observations, products and source comparisons can support different answers. Unit assessments must retain those links. |
| History follows time order, or a reason explains departures | **Met.** Thematic kindergarten organization and date-based holiday interruptions are explained. |
| Contested events carry more than one telling | **Met as a sequence commitment.** Thanksgiving includes the historical record and present-day Wampanoag perspectives. Actual source selection remains unjudged. |
| Writing from sources recurs and develops | **Not applicable to independent written length at this course’s deliberately oral depth.** Spoken claims recur across units and become explicitly tied to photographs. Grade 1 receives the written explanation progression. No source-writing growth is claimed here. |

## Settled by the expert

These choices are for the caller to apply. No edits were made.

| Choice | Reason | Files affected |
|---|---|---|
| Retain all six unit allocations and 64 total days | No demonstrated whole-unit imbalance | Sequence and day file |
| Expand named observation windows within existing lessons | Full coverage should not become an oversized final interview | Sequence and day file |
| Teach personal importance of questions explicitly | Completes existing D1.1 ownership | Days 1 and 9 |
| Include worker knowledge, skills and tools | Completes existing economics ownership | Days 53 and 60; `ssk-work` progression row |
| Start implementation on day 14 | Closes the action cycle before evaluation | Days 14 and 17 |
| Represent interrupted units as separate calendar segments | Preserves actual lesson ownership and timing | Calendar generator and generated calendar |
| Treat holiday school-day positions as provisional | School-year positions cannot guarantee civil dates | Sequence and holiday notes |
| Define the shorter route as 20 minutes across 64 meetings | Preserves scope and assessment response | Sequence; subsequent unit plans |
| Correct the three stale statements | Removes contradictory handoff information | Sequence and frame |

## What is right and should remain

Keep the classroom starting point, oral and picture-based access, explicit model introductions, and all 19 reciprocal grade 1 handoffs. Preserve the token store, unpaid-work examples, student choice in action, and protections against compulsory disclosure of addresses, family photographs, chores or traditions.

The earlier frame repairs are substantially present: full time-language teaching, introductory map-design exposure, the bounded unit 4 question, cumulative map and claim tasks, final response time, corrected extension attribution, and early holiday instruction. Those settled findings should not be reopened.

The current FOUNDATION and frame assign sensitive-content work to the sensitivity agent. The older report’s request for an outside qualified reader is superseded.

## What I could not judge

- Individual assessment throughput for thirty children within the proposed observation windows.
- Accuracy, rights, reading difficulty and representation of sources not yet selected.
- Exact availability of cross-subject skills before their daily sequences exist.
- The completed unit items, scoring guidance, home routes or classroom feasibility.

No substantive finding rests solely on memory. Prior workflow memory informed the checking method; standards claims were checked against current files and accessible outside sources.

## Sources and reading limits

- [Massachusetts History and Social Science Framework, 2018](https://www.doe.mass.edu/frameworks/hss/2018-12.pdf): kindergarten standards and clarifications, printed pages 32 to 35.
- [C3 Framework, revised 2017](https://www.socialstudies.org/sites/default/files/c3/c3-framework-for-social-studies-rev0617.pdf): relevant K to 2 indicator tables and inquiry expectations.
- [California content standards](https://www.cde.ca.gov/be/st/ss/documents/histsocscistnd.pdf): kindergarten comparison candidates and the grade 1 location distinction.
- [Social studies instructional-materials criteria](https://air.org/sites/default/files/2024-01/23-23505_HQIM_for_SS_Final.pdf): read in full for coherence, inquiry, usability and assessment.
- [Rules inquiry](https://c3teachers.org/inquiries/rules/) and [Needs and Wants inquiry](https://c3teachers.org/inquiries/needs-and-wants/): published kindergarten comparisons of task progression and concluding performance. Embedded source collections were not comprehensively audited.
- [Needs and Wants PDF](https://c3teachers.org/wp-content/uploads/2024/04/NewYork_K_NeedsandWants.pdf): opening planning and instructional discussion, including its three-to-five-period estimate. Used as a comparison, not a pacing prescription or adaptable base.
- [New York K to 8 framework](https://www.nysed.gov/sites/default/files/programs/curriculum-instruction/ss-framework-k-8a2.pdf): retrieval timed out. Its Candidate attributions were not independently reverified.
- [Tennessee 2024 standards](https://www.tn.gov/content/dam/tn/stateboardofeducation/documents/standards/social-studies-2022-2023/TN%20Academic%20Standards%20for%20Social%20Studies%206.24.pdf): direct retrieval returned 403. No finding depends on its unverified contents.

**For the source list:** Add the two reachable kindergarten inquiry pages and their PDF routes if absent, recording their reference-only use and the reading limits above.

## For Cory

None. This read proposes no change to scope, audience, money or outside people.

**Verdict:** Revise before approval. **Finding count:** 6. **Report path:** `docs/reviews/sequence-social-studies-kindergarten-2026-11-14.md`, delivered here only.

