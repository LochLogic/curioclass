# Frame read: Media Arts, grades 3 to 5

2026-11-25. Independent second read of [the course frame](S:/CurioClass/docs/courses/media-arts-grades-3-to-5/frame.md). No files were changed.

## Verdict

**Sound course structure, with revisions needed before the scope and sequence is written.** Grade ownership, annual totals, unit order and neighboring seams agree, but several assessment descriptions do not establish the full actions claimed, and the compressed assessment schedule cannot run as stated. The most important change is to make the assessment windows feasible while preserving revision and a subsequent respond session.

**Eight findings follow, most serious first.**

## What I read and checked

- `frame-read.md`, the after-core provisions and relevant lessons in `frame-write.md`, `EXPERT.md`, the arts lens, foundation and shared approach.
- The arts adoption bar, `docs/courses/arts/STANDARD.md` and `APPROACH.md`, and relevant recorded decisions.
- The target frame in full; its course-list, frame and calendar records; all 24 selected progression rows and their standards action lines.
- The neighboring media arts frames, focusing on the grade 2 and grade 6 units, models and reciprocal seams; the grade 3 ELA unit supporting collaborative discussion.
- Earlier arts pre-work, progression and media arts reviews, including the independent K to 2 read, for repeat findings and resolved issues.
- Outside sources linked below, checked through web search and direct opening.

Checks:

| Command | Result |
|---|---|
| `python -X utf8 scripts/frame.py check media-arts-grades-3-to-5` | 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |
| `python -X utf8 scripts/plan.py check media-arts-grades-3-to-5` | 1 failure: expects later-stage plan files |

The plan check was course-filtered because repository instructions prohibit an unfiltered run; its missing-later-stage-files result does not prevent this frame review.

## Findings

### 1. Several evidence descriptions allow incomplete standards to receive “met”

**Severity:** Major  
**LAYER:** frame, with related progression and standard action-line corrections  
**REPEAT:** yes, incomplete evidence coverage in earlier arts reads  
**Confidence:** firm

**Location:** Units 1, 2, 3, 5, 7, 9 and 11, frame lines 282 to 292.

Naming every ID is valuable, but the evidence must establish its required actions. These gaps remain against the [national performance standards](https://www.nationalartsstandards.org/sites/default/files/2021-11/Media%20Arts%20at%20a%20Glance%20-%20new%20copyright%20info.pdf) and [New Mexico’s official K to 5 standards listing](https://web.ped.nm.gov/wp-content/uploads/2024/12/2022_F.21-Media-Arts-Grades-K-5.pdf).

| Unit and ID | Gap | Exact fix |
|---|---|---|
| **1: MA:Cn11.1.3a** | Daily life, values and online behavior are present; cultural life is absent from the teaching and evidence descriptions. | Add an individual explanation connecting one studied work to its cultural setting, using its work card. Retain the existing values and online examples. |
| **1, 5, 9: MA:Cn11.1.3b, 4b, 5b** | Selecting a rule or sorting a case can show knowledge without showing appropriate interaction. | Add an observed use of the relevant tools or classroom media space during production, recorded individually. Keep the case task for explanation and discussion. |
| **2: MA:Pr5.1.3a** | The evidence accepts one role and two jobs, while the standard requires developing ability across varied roles. | Record each student performing at least two different production roles within this unit, with observed skill in each. |
| **9: MA:Cn11.1.5a** | An invented advertisement and one historical fact do not necessarily demonstrate research into media’s relationship with life or community. | Add a short investigation record: question, evidence from the supplied sources, and a conclusion connecting advertising to a public or invented community. |
| **3, 7, 11: MA:Re9.1.3, 4, 5** | Unit 3’s item omits context. Unit 7 checks a production step alone. Unit 11 accepts criteria and feedback without explicitly evaluating both work and production process in context. | Require context in each evaluation. In units 7 and 11, collect judgments of both a finished work and a production step; retain improvement in grade 4 and constructive feedback in grade 5. |

These are corrections within existing ownership. Collect practical observations during production so they do not further crowd check sessions.

Also restore cultural life in the `ma-g3-society` progression note and its words-file action. Restore context in the grade 4 and grade 5 Re9 words-file actions, within the existing 14-word limit. Otherwise the shortened upstream descriptions will reproduce these omissions.

### 2. The talk-and-table timetable leaves inadequate time for individual evidence

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, combined media arts read S1 and K to 2 independent read  
**Confidence:** likely for classroom feasibility; firm for the arithmetic

**Location:** “Scored evidence,” lines 102 to 107; course-level checks, lines 299 to 307.

Five students receive three minutes for a talk item and, in units 1, 5 and 9, a practical or ethics item. That permits approximately 18 seconds per response before transitions, thinking time and recording marks. The complete timetable uses all 40 minutes.

The year-end course checks also add fresh planning or proposal tasks, but the common timetable assigns no separate time to them. Teachers following it must shorten the evidence, rush students or consume response time.

**Exact fix:**

- Record practical tool use and role enactment across the last three production sessions, observing ten students per session.
- Divide individual talk evidence into two windows of at most 15 students, allowing 18 minutes per window. Use the two reserved check days where available; otherwise name a late production window with independent paper work for the other students.
- Give year-end planning and partner testing an explicit ten-minute block.
- Replace the common check-day timetable with separate schedules for response checks, production checks and course-level checks. Count every task and transition within 40 minutes.
- Keep each student’s evidence collected once and available before the relevant respond session.

The suggested timings are planning judgments, not classroom-tested results.

### 3. The short path completes assessment during the session meant to respond to it

**Severity:** Major  
**LAYER:** frame  
**REPEAT:** yes, arts pre-work finding 18 and the K to 2 independent read  
**Confidence:** firm

**Location:** “The once-a-week path,” lines 33 to 45; units 4, 8, 11 and 12.

The short-path totals and promised check weeks **do add up correctly**. The problem is instructional time within those totals.

The frame moves written and talk items into the respond session’s first 20 minutes. Its own routine requires ten minutes for writing and 18 for interviews, before setup or scoring. Students cannot receive a response to evidence that is still being collected.

Year 3 unit 4 has only five sessions. Demonstration, making with critique, revision, screening, remaining assessment and response require six distinct stages under the stated design. Unit 11’s five-session path also needs clarification because its evidence line promises two check days.

**Exact fix:**

1. Remove the provision for completing checks in the respond session.
2. Give screening units a separate response-assessment session after the screening and before response.
3. Change year 3’s short-path allocations from **7, 9, 7, 5** to **7, 9, 6, 6**. Keep the checks in weeks 17 and 26 by scheduling unit 3 in weeks 19 to 24, unit 4’s opening session in week 25, the course check/respond pair in weeks 26 and 27, and unit 4’s remaining five sessions in weeks 28 to 32. State explicitly that the short path pauses unit 4 for that course check.
4. Keep year 4’s **7, 9, 6, 6** and year 5’s **8, 9, 5, 6**, but name the separate screening, response-assessment and respond sessions.
5. For unit 11’s short path, specify one check session for its written item and kept evidence, following demonstration, making with critique and revision. Do not carry the full path’s two-check-day label into that five-session version.
6. Apply finding 2’s observation windows without replacing revision or response.

This preserves 32 sessions, all units and existing ownership.

### 4. The first critiques assume an optional course’s routine before its local fallback

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, earlier arts findings on explicit modeling and entry without prior arts study  
**Confidence:** likely

**Location:** “Readiness and retrieval,” lines 116 to 123; “Models carried,” line 272; units 1 and 2.

The frame correctly says students cannot be assumed to have taken K to 2 media arts. Yet units 1 and 2 use the grade 2 critique card “as review,” while the retrieval and reteach for that thread sit in unit 3. A newcomer reaches two required critiques before the explicitly placed fallback.

**Exact fix:** Add to unit 1 and the critique-protocol model row:

> Before the first critique, the teacher models describe, ask, suggest with a Curio Class example and the unit’s look-for. Students practice the routine with the card. Unit 2 retrieves it; unit 3 extends it through explicitly named evaluation criteria.

Keep the `ma-g3-judge` row and its owned standards in unit 3. This changes the placement of a supporting routine, not standards ownership.

### 5. Year-end checks immediately repeat the preceding unit’s interpretation assessment

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, K to 2 independent read finding 5  
**Confidence:** firm against frame-write lesson 20

**Location:** Course-level checks, lines 300, 302 and 304.

Each year-end check carries the recent unit’s product unscored but immediately gives another interpretation task on its Re8 standard:

- Unit 3: `MA:Re8.1.3`.
- Unit 7: `MA:Re8.1.4`.
- Unit 11: `MA:Re8.1.5`.

Changing the unseen work does not make this a spaced sample of earlier learning.

**Exact fix:** Keep the recent records unscored. Replace those written items with earlier-unit reading samples:

| Year | Replacement |
|---|---|
| 3 | Unit 1: describe how components build a new piece’s message, `MA:Re7.1.3a`. |
| 4 | Unit 5: explain how components build a new piece’s message, `MA:Re7.1.4a`. |
| 5 | Unit 9: compare how two new pieces’ components build different messages, `MA:Re7.1.5a`. |

Retain the earlier planning samples, with finding 2’s explicit time allowance.

### 6. Named works and safety references lack direct source links

**Severity:** Moderate  
**LAYER:** frame  
**REPEAT:** yes, K to 2 independent read finding 6  
**Confidence:** firm

**Location:** Works throughout the Units table; “Safety read,” lines 173 to 177.

The frame repeatedly promises that a work is “described and linked,” but supplies no direct work links. Generic museum, archive and domain names leave the next writer to locate evidence for dates, settings and summaries. Several selections, including the zoetrope strip, Ōfuji film, trade cards, broadside and winter count, remain unidentified.

**Exact fix:**

- Add a direct, freely readable contextual or item-record link beside every named work.
- Replace generic selections with identified items and records.
- Distinguish contextual evidence from the item page used to check reproduction rights.
- Replace the three safety domains with direct links to the specific guides.

Two available starting points are [the maker’s account of The Lost Thing](https://www.shauntan.net/lost-thing-film) and [the film board’s Sigwan record](https://www.nfb.ca/film/sigwan_en/). These support identification and description; they do not establish permission to reproduce the works.

### 7. The weekly-time note promises a media arts figure the checked documents do not supply

**Severity:** Minor  
**LAYER:** process, with a standard-page correction  
**REPEAT:** yes, combined media arts read m5 and K to 2 independent read finding 7  
**Confidence:** firm within the sources checked

**Location:** Days bullet, lines 29 to 32; “For the lead,” item 3, lines 361 to 364; arts `STANDARD.md` section 3.4.

The elementary checklist is explicitly about visual arts. Its 50-minute recommendation should not become a separate media arts minimum because the filename includes “Media.” The general visual and media arts document gives scheduling requirements without a numerical media arts weekly minimum in its scheduling section. [Elementary checklist](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-Elementary_Visual_Media_Arts_Program.pdf), [general program standards, PDF page 12](https://www.arteducators.org/wp-content/uploads/2025/09/OTL-PreK-12_Visual_Media_Arts_Programs.pdf).

**Exact fix:** Replace the Pending promise and lead item with:

> No separate media arts weekly minimum was identified in the association’s elementary visual arts checklist or general PreK to 12 visual and media arts program standards, checked 2026-11-25. This course provides 80 minutes weekly, or 40 on the short path; no numerical comparison is claimed.

Record that bounded result in `STANDARD.md`, separately from unfinished middle school visual arts source work.

### 8. Shared adoption-bar notes still describe completed arts work as unfinished

**Severity:** Minor  
**LAYER:** process  
**REPEAT:** yes, stale implementation notes in arts pre-work reviews  
**Confidence:** firm

**Location:** `docs/ADOPTION-BAR-SUBJECTS.md`, lines 20 to 21 and the Arts row at line 568.

The introduction says no subject approach exists. The Arts row still owes the standards gate and loading 63 high school music strand IDs. The arts approach is approved, L83 is marked done, and the ID file contains those 63 strand IDs. `stale.py` does not catch these unmarked prose claims.

**Exact fix:**

- Replace the introduction’s “none exists” sentence with:  
  **“Subject approach pages live under docs/courses/<subject>/APPROACH.md; this page sets the adoption criteria.”**
- Replace the Arts row’s obsolete “Owed” sentence with:  
  **“The NCAS ID-existence gate and the 63 high school composition and theory IDs, words lines and progression rows were completed 2026-11-21.”**

Leave dated review records unchanged.

## Coverage, days, calendar and seams

| Year | Units | Selected skills | Owned IDs | Unit sessions | Course checks/respond | Total |
|---|---|---:|---:|---:|---:|---:|
| 3 | 1 to 4 | 8 | 18 | 60 | 4 | 64 |
| 4 | 5 to 8 | 8 | 18 | 60 | 4 | 64 |
| 5 | 9 to 12 | 8 | 18 | 60 | 4 | 64 |

All 24 selected skills and 54 owned IDs occur exactly once. No wrong-year ownership was found. Structural placement passes; substantive completeness needs finding 1.

The full-path unit allocations have defensible reasons. Longer planning-and-crew units establish production methods; later units reuse material. The full-path calendar matches all unit ranges and course checks. Those checks avoid the current core check weeks.

The short-path allocations total 32 sessions and produce the stated check weeks. Finding 3 concerns what happens within those sessions.

Both neighboring seams agree with the progression. The grade 3 ELA discussion lean is available from ELA unit 1, before media arts unit 3. Other core contacts carry local support or topic-selection provisions. Computer science is explicitly not a prerequisite.

There is no base text, so a base-lesson source map is not applicable. Existing after-core clashes remain assigned to the lead’s shared calendar pass.

## Arts lens checklist

| Frame-level check | Result |
|---|---|
| Grade IDs placed in their own year | Met |
| Four artistic processes in every year | Met |
| Technique taught directly and grows harder | Met |
| Discipline words used in making and responding | Met in the design |
| Choice and showing in every unit | Met |
| Works span periods and cultures, including living makers | Present; direct sourcing needs finding 6 |
| Critique taught before use; revision before scoring | Needs findings 3 and 4 |
| Making, response, self-assessment and portfolio evidence | Present; completeness and feasibility need findings 1 to 3 |
| Ordinary room, supplies, setup and cleanup planned | Met as frame commitments |
| Schedule avoids a daily K to 8 period | Met |
| Screens support physical making | Met |
| Media arts retains its disciplinary purpose | Met |
| Detailed access, safe execution and final work excerpts | Not yet judgeable at frame level |

## What should be preserved

Preserve the three complete years, reciprocal seams, increasingly demanding techniques, portfolios, individual consent protections, local storage and public or invented alternatives to personal disclosure.

Keep the paper path. The [national media arts introduction](https://www.nationalartsstandards.org/node/763) deliberately leaves particular technologies unspecified. Actual use still needs to be observed where an ID requires interaction.

The corrected Cn10/Cn11 placement agrees with the current national handout and [California’s grade 3 Cn10 record](https://www2.cde.ca.gov/cacs/id/web/30477). Do not reverse that correction.

I do not carry forward the combined review’s suggestion that sharing an artist with another arts discipline is itself a defect. Different disciplinary teaching can justify a revisit.

## Settled by the expert

| Choice | Reason | Files affected |
|---|---|---|
| Collect practical evidence during production | Establishes action without crowding interviews | Target frame and later unit plans |
| Split individual interviews into named windows | Allows credible individual evidence | Target frame |
| Preserve assessment before response on the short path | Response must follow available marks | Target frame and later scope |
| Transfer one year 3 short-path session from unit 3 to unit 4 | Gives the screening unit six sessions while retaining 32 | Target frame |
| Model critique in unit 1 for newcomers | Optional earlier arts study cannot be assumed | Target frame |
| Expand evidence within current ownership | Restores omitted actions without moving standards | Target frame, relevant progression and words lines |
| Sample earlier reading in year-end checks | Avoids immediate repetition | Target frame |
| State the bounded weekly-time source result | Prevents importing a visual arts figure | Target frame and arts STANDARD.md |

## For Cory

- **Money:** The proposed $50 annual class supply ceiling remains a proposal. Current optional estimates are $45, $50 and $50 by year, with free alternatives retained.
- No new audience, outside-person or standards-ownership decision is needed for these corrections.

## Confidence, limits and source-list additions

No finding rests on model memory. Arithmetic and repository contradictions are firm; classroom timing judgments remain untested.

The frame’s detailed safety rules remain explicitly **“from memory”** pending its specified safety read. This review does not establish every work’s reproduction rights, verify every eventual excerpt, or certify final assessment items.

**For the source list:** Add the current national handout, the official state standards cross-check, and the two opportunity-to-learn documents linked above. Record that the elementary numerical recommendation concerns visual arts and that no separate media arts weekly minimum was identified in the two scheduling documents checked.