# Expert read: scope and sequence of Dance, grades 6 to 8 (2026-11-26)

Course `dance-grades-6-to-8`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write
the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9
  and "Fails if") and the shared core, docs/courses/arts/STANDARD.md and docs/courses/arts/APPROACH.md (as cited by
  the frame), build/scope-writes/ARTS-BRIEF.md, docs/pipeline/briefs/sequence-write.md (rules 2, 3 and 10).
- docs/courses/dance-grades-6-to-8/scope-and-sequence.md and data/plans/dance-grades-6-to-8/days.csv (all 192 rows,
  goals and notes), read cold.
- Beside them: the frame (docs/courses/dance-grades-6-to-8/frame.md, all of it), the 24 da-g6 to da-g8 rows of
  data/progressions/arts.csv, the 63 grade 6 to 8 dance lines of data/standards/ncas-performance-standards-words.txt,
  docs/courses/CALENDAR.md (grades 6 to 8 rows) and the course's rows in data/plans/calendar.csv, with the leaned-on
  rows of social studies grade 6 (days 100 and 112, Silk Roads), physical education 6 to 8, health 6 to 8 and ELA
  grades 6 and 8. The earlier arts scope read (docs/reviews/sequence-media-arts-grades-3-to-5-2026-11-26.md) for
  REPEAT tags.
- Gates: `scripts/sequence.py check dance-grades-6-to-8` (0 failures), `scripts/plan.py check` (no failure for this
  course), `scripts/frame.py calendar` (dance weeks 17 and 32 in each of grades 6, 7 and 8, as CALENDAR.md sets),
  `scripts/stale.py check` (0 failures). A short script over days.csv: every one of the 63 ids sits only on days of
  its own year, and every id is on an end-of-unit row or a kept product scored with one. `school_day` follows
  ceil(2.5 x n) and lands each check on week 17 or 32.
- No outside source was opened for this read. The standards' wording rests on our own-words file (checked at source
  by earlier arts reads); the minute and room judgments rest on the frame's own minute budgets and on memory of
  middle school arts electives, marked so.

## Verdict

Sound in shape: the band-year rule is stated once and kept (21 ids a year, each on a day of its own year), every
unit carries all four processes by day, technique is taught on its own day and drilled before the making that uses
it, every unit has one critique by protocol and a rehearsed change before its showing, the three written products
are drafted, given feedback and revised inside their units, and the works range across four continents and 1653 to
today with every flagged tradition named in its day's note. The biggest risk is the once-a-week path: every unit's
written check day is merged into a session with two or three other days, so a 37-minute set of assessed items has
no room, and the performance units' second session carries four teaching days. The one change that matters most is
to give the once-a-week written items a real slot (finding 1); close behind, the waltz context card that scores
DA:Cn11.1.6a is never taught (finding 2).

## Findings, most serious first

### 1. The once-a-week path does not hold the written check days

LAYER frame and sequence. REPEAT yes (the same kind as the media arts 3 to 5 read's finding 2: the frame's session
counts overload sessions). Confidence: likely (from the frame's own minute budgets).

- **What is wrong.** The frame gives each unit one check session (the showing) on the once-a-week path, but every
  unit has two check days. The scope's answer ("For the lead" item 5) merges the written day into the last
  rehearsal session. The written day alone is 37 minutes (set-up 2, phrase 4, items 28, collecting 3). The merged
  sessions are:

  | Units | Session | Days merged into one 40-minute session |
  |---|---|---|
  | 1, 5, 9 | 6 of 8 | 13, 14, 15, 17 (test fixes, run-through, last rehearsal and log, the written day); 77, 78, 79, 81; 141, 142, 143, 145 |
  | 2, 6, 10 | 6 of 8 | 28, 29, 31; 92, 93, 95; 156, 157, 159 |
  | 3, 7, 11 | 4 of 6 | 44, 45, 47 (rehearse the change and collect the notation, revise the critique, three unseen-phrase items); 108, 109, 111; 172, 173, 175 |
  | 4, 8, 12 | 4 of 6 | 58, 59, 61; 122, 123, 125; 186, 187, 189 |

  The same path puts four teaching days into session 2 of every 14-day unit: 38 to 41 (criteria card, critique
  draft, invented notation, its drill), 52 to 55 (research card with two sources, plan, performing in the space,
  production elements), and likewise 102 to 105, 116 to 119, 166 to 169, 180 to 183. Unit 12's two research
  methods (DA:Cn10.1.8b) and unit 4's two sources cannot be done in a quarter of a session.
- **Why it matters.** The brief asks that the once-a-week path hold with no assessed or owned part cut. On a busy
  teacher's reading, three unseen-phrase items in the last minutes of a rehearsal are cut or rushed, and an
  end-of-unit assessment lands on a teaching session, which the frame's "two kinds of check day" rule and APPROACH
  "Kinds of day" do not allow.
- **The fix.**
  - **Settled (units 2, 6 and 10, inside the frame's counts).** These units have a light session (day 25, 89 and
    153 sit alone in session 4). Re-merge: session 1 days 19-20, 2 days 21-22, 3 days 23-25, 4 days 26-27, 5 days
    28-29, 6 day 31 alone with day 29's run-through as its warm-up, 7 day 30 (showing), 8 day 32. Unit 6: 83-84,
    85-86, 87-89, 90-91, 92-93, 95, 94, 96. Unit 10: 147-148, 149-150, 151-153, 154-155, 156-157, 159, 158, 160.
    Each written day then has a session of its own.
  - **For the lead (a frame change), units 1, 3, 4, 5, 7, 8, 9, 11, 12.** These have no light session, and the
    first unit of each year cannot give one up (its 18 days already fill 8 sessions). Recommended: on the
    once-a-week path only, the written items become two short timed blocks of about 12 minutes, each at the close
    of a session after the part it assesses is taught (the unseen phrase danced at the start of the block), scored
    after the session like a kept product; one prompt per part stays, so nothing assessed is cut. The frame's
    once-a-week bullet names this as the path's one exception to "two check days, never mixed". If the lead
    prefers to keep two check days, the only other way is a 33rd and 34th session, which the path does not have.
    Either way, session 2 of the 14-day units moves its research start (days 52, 116, 180) into session 1's last
    ten minutes after the hook, so the research card is not begun and planned in the same quarter session.
  - **Text (settled).** The Shorter path paragraph says "unit days 13 to 15 and 17" and "unit days 10, 11 and 13",
    so no writer reads them as course days.

### 2. The waltz show item for DA:Cn11.1.6a is scored but its setting is never taught

LAYER sequence. REPEAT yes (a part used before it is taught, as in earlier reads). Confidence: firm (days.csv).

- **What is wrong.** Day 60 scores DA:Cn11.1.6a in part by "a short accessible demonstration of the waltz with its
  sourced context card". No day teaches the waltz's setting (day 3 teaches the box step and the counts only) and no
  day writes the context card; it first appears on day 59, the dress run. The scope's own Processes line gives unit
  1's connecting to days 1 and 5 only, so The Blue Danube is also a work studied with no setting (lens, "Unit"
  errors).
- **Why it matters.** The student must interpret what the waltz's movement meant to its people with nothing taught
  about them; the show item cannot be met as written, and a writer building day 3 would leave the setting out.
- **The fix (settled).** Day 3's note adds the work card's setting lines for the waltz (Vienna, the 1860s ballrooms,
  who danced it and what the turning couple meant then, from an open museum or library page), about 5 minutes
  inside the teaching; the Processes line of unit 1 adds day 3 to connect. Day 55 gains a last ten-minute block:
  each student drafts the waltz context card (one movement and the meaning it carried, two sourced lines) from the
  day 3 work card, with DA:Cn11.1.6a added to day 55's codes; day 58 finishes and collects it beside the production
  card; day 59 runs the waltz with it as now. The unit 4 Arc and Assessments lines change to match.

### 3. The mid-year showing checks use new material that no day teaches

LAYER sequence (the frame sets "new material"; the scope must place its learning). REPEAT new. Confidence: likely.

- **What is wrong.** Days 33, 97 and 161 ask groups to dance a new partner section, a new three-beat piece, a new
  floor pattern or a new layered phrase. The showing day's 40 minutes are full (set-up 3, warm-up 5, six groups 24,
  self-check 5, room back 3), and the day before (32, 96, 160) is a respond day with no such block.
- **Why it matters.** Either the groups learn the new material during the check (no time) or the teacher drops the
  check's "new material" and re-dances the unit sections, which the note forbids.
- **The fix (settled).** The last ten minutes of days 32, 96 and 160 teach the check's new material from a Curio
  Class step card (about 16 counts, unscored), as the brief's readiness placement already uses a respond day's last
  ten minutes; day 33, 97 and 161's warm-up runs it once. Each of those days' notes says so. On the once-a-week path
  this block sits in the unit's session 8.

### 4. The shorter year folds the wrong days

LAYER sequence. REPEAT yes in part (the baseline cut is the media arts read's finding 9). Confidence: likely.

- **What is wrong.** The fold days include days 41, 105 and 169, each the only Fluency day of its unit (the only
  notation drill before the scored notation), and days 59, 123 and 187, the only dress run before each family
  showing (187 is the only run in both spaces before a two-space showing that scores DA:Pr6.1.8b). Days 29, 93 and
  157 fold into a showing day's "warm-up and opening", but a showing day has no opening slot. Days 41, 105 and 169
  are also baseline-look days.
- **Why it matters.** The 18-day units and the making units hold three or four Fluency days each; folding there
  costs least, while the chosen days strip the revising and performance units of their only practice.
- **The fix (settled).** Fold days: year 6 days 10 (into 11's warm-up), 14 (15), 22 (23), 29 (30's warm-up only);
  year 7 days 74 (75), 78 (79), 86 (87), 93 (94's warm-up only); year 8 days 139 (140), 150 (151), 157 (158's warm-up
  only), 169 (172), the one revising-unit fold kept in year 8 because units 9 and 10 then keep one Fluency day each.
  Minutes saved stay 160 a year, 480 in all. Add to the table's lead line: "Where a fold day carries the baseline
  look, its last rotating group is observed in the next day's opener." Move the "Shorter year" note text to the new
  days.

### 5. Rows used earlier the same year are leaned on with no retrieval

LAYER sequence. REPEAT yes (as in the media arts read, finding 5). Confidence: firm against sequence-write rule 2.

- **What is wrong.** Retrieval sits only on day 2 of each unit, for the progression `assumes` row. Several units
  lean on a row taught earlier the same year: unit 2 builds from unit 1's spacing, accents and tension (da-g6-elements)
  on day 26; unit 3 revises unit 2's study (da-g6-form) on day 42; unit 4 re-dances unit 1's waltz (da-g6-elements,
  last used in week 2) for a scored show item; unit 6 uses unit 5's borrowed designs (da-g7-elements) on day 90;
  unit 7 revises unit 6's study (da-g7-form) on day 106 and leans on unit 5's quality words on day 101; unit 10 uses
  unit 9's sculpting and layered time (da-g8-elements) on day 154; unit 11 revises unit 10's dance (da-g8-form) on
  day 170 and leans on unit 5's comparing of styles (da-g7-elements, the year before) on day 165.
- **The fix (settled).** A five-minute retrieval warm-up in the named day's opener, in its note and `retrieves`:
  day 26 da-g6-elements; day 42 da-g6-form; day 55 da-g6-elements (the waltz, before finding 2's context card);
  day 90 da-g7-elements; day 101 da-g7-elements; day 106 da-g7-form; day 154 da-g8-elements; day 165 da-g7-elements;
  day 170 da-g8-form. Add a "Same-year retrieval" line to the .md's Readiness and retrieval bullet. No readiness
  check is needed (no row is two grades idle) and no unit's first day changes.

### 6. Course-level check items list codes but ask only some of their parts

LAYER sequence (the wording comes from the frame's checks table). REPEAT yes. Confidence: firm against the words
file.

| Day | Code | Part not asked | Change |
|---|---|---|---|
| 33 | DA:Pr4.1.6b | four-beat measures; abrupt and lingering timing | the new piece has a three-beat and a four-beat part, with one sudden and one sustained change |
| 63 | DA:Re7.1.6a | how the patterns relate | "naming its repeating patterns and how one relates to another" |
| 127 | DA:Pr4.1.7c | plan clear performance | add "and one line on how to perform each clearly" |
| 127 | DA:Re7.1.7a | the links between patterns | "patterns compared, alike and different, and how they link" |
| 161 | DA:Pr4.1.8b | choose beat, movement and breath phrasing | the layered phrase includes one breath phrase, its choice named |
| 191 | DA:Cr2.1.8b | define | "criteria defined, then applied to a described new group dance, and their effect" |
| 191 | DA:Re8.1.8a | how elements create expression | a prompt of its own: "how two elements in the named moments create its expression", apart from the judgment |

All are item wording inside the standards' limits (settled); the frame's checks table changes to match (for the
lead, since it is the frame's text). None moves a code.

### 7. The frame says unit 12 stages unit 11's dance; the scope does not

LAYER frame. REPEAT new. Confidence: firm.

- **What is wrong.** The frame's unit 11 row ends "Before unit 12, which stages the revised dance for two spaces",
  and its Leave-out bullet gives unit 12 a fallback ("stages a staging-ready original study"). The frame's own unit
  12 row, and this scope (days 181 and 184), stage the new research study instead, and the scope has no unit 12
  fallback.
- **Why it matters.** A unit plan writer reading the frame would plan two dances for unit 12 in 14 days.
- **The fix (for the lead).** The scope's reading is the right one (one study carries DA:Cn10.1.8b and DA:Pr6.1.8b
  together). The frame drops "which stages the revised dance for two spaces" from unit 11 and the unit 12 clause
  of the fallback sentence. No scope change.

### 8. Small text a writer would copy wrong

LAYER sequence. REPEAT new. Confidence: firm.

- Physical education grade 6 unit 6 runs weeks 22 to 26 in data/plans/calendar.csv; the scope's lean table and day
  11's note say 22 to 27 (the frame says so too). Change to 22 to 26 in both scope places.
- Day 73 (Dance Theatre of Harlem) has no sensitivity line though the frame's unit 5 list names the company. Add:
  "Sensitivity: a company founded in 1969 to open ballet to Black dancers, said in one plain sentence from its own
  pages, read first by the sensitivity agent."
- The scope's Processes line for unit 1 counts day 3 as responding; day 3 is a step and counts day. With finding 2
  it becomes connect; drop it from respond.

## The writer's "For the lead" items

- Item 1 (added samples): agreed; inside the frame's limits.
- Item 2 (task form within two weeks): my reading is that "task form" means the item's form on its content, not the
  kind of check day. The mid-year showings dance unit 1, 5 or 9 skills on new material with different look-fors from
  the making unit's showing, and the year-end items differ in form from the performance unit's written items, so
  nothing repeats and the frame needs no swap. The lead confirms the reading once for all arts courses.
- Item 3 (Fluency days in the 14-day units): agreed.
- Item 4 ("the unit's waltz"): agreed; finding 2 adds the teaching it needs.
- Item 5 (once-a-week written day): replaced by finding 1.

## What is right and should not be touched

- The band-year statement on the first page, the mixed-class line, and each year's heading naming its grade's ids.
- The day pattern: day 1 clean for the hook, day 2 retrieval with its reteach, technique on its own Understanding
  day before any making, jumps taught on a day of their own before the drill, the critique modeled on the teacher's
  phrase the first time (day 12), and two check days per unit, never mixed, on the full path.
- Draft, written feedback and revision inside units 3, 7 and 11, with the draft early enough for feedback to return.
- Kept products finished on making days and scored with the check marks, so no check day collects a product made
  on it; the "codes not sampled" table with a reason for each.
- The sensitivity notes on the days (stepping, butoh, The Green Table, the Tang figurines, Kaha:wi, capoeira, Weave,
  sabar, khon, the fancy shawl dance), watched-only where the frame says so, and the invented dancer for every
  body, food and habit item.
- The room and safety rules, the floor rule and the groups of five with the director's, counter's and staging roles.
- The calendar: checks on week 17 (school day 83, shared only with the other arts electives) and week 32, family
  showings in weeks 30 and 31, and each same-year lean met or bridged.
- The candidate cells, all settled with reasons.

## What I could not judge

- Whether six groups of five in 24 minutes, with a show item per student, fits a real middle school gym; a trial
  would tell.
- Whether the frame's Pr5.1.6b warm-up look-for on the showing day can be marked while the teacher watches one group
  at a time (the frame's rule); the unit plan should say whether it is marked during each group's turn.
- The rights lines of the works the unit plans pick; not this layer's job.

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| Once-a-week re-merge of units 2, 6 and 10 (finding 1) | each written day gets its own session inside the frame's counts | scope-and-sequence.md Shorter path; days.csv notes of days 19 to 32, 83 to 96, 147 to 160 |
| "Unit days" wording in the Shorter path paragraph | not read as course days | scope-and-sequence.md |
| Waltz setting on day 3; context card drafted on day 55 (DA:Cn11.1.6a added), finished on day 58 | the scored show item needs its teaching | days.csv days 3, 55, 58; scope-and-sequence.md units 1 and 4 |
| New check material taught in the last ten minutes of days 32, 96 and 160 | the mid-year showing cannot teach it in its own minutes | days.csv days 32, 33, 96, 97, 160, 161 |
| Fold days 10, 14, 22, 29, 74, 78, 86, 93, 139, 150, 157, 169, and the baseline line | keeps the revising units' only drill and every dress run | scope-and-sequence.md Shorter path; days.csv notes |
| Same-year retrieval warm-ups on days 26, 42, 55, 90, 101, 106, 154, 165, 170 | rule 2 for rows used earlier the same year | days.csv notes and `retrieves`; scope-and-sequence.md Readiness and retrieval |
| Item wording in finding 6's table | each listed code asks each of its parts | days.csv days 33, 63, 127, 161, 191; scope-and-sequence.md Course-level checks |
| Physical education weeks 22 to 26; day 73 sensitivity line; day 3 out of respond | copy errors a writer would build from | scope-and-sequence.md; days.csv days 11, 73 |

## For the lead (not Cory)

- Finding 1's once-a-week exception for the written items (or a decision to accept the compression) is a frame
  change, as is moving the research start into session 1.
- Finding 6's wording in the frame's Course-level checks table.
- Finding 7's two frame sentences.
- The writer's item 2 reading of "task form", once for all arts courses.

## For Cory

Nothing new on scope, money, people or audience.

## For the source list

None: no outside source was opened for this read.
