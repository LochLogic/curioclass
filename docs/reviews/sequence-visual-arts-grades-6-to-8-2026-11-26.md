# Expert read: scope and sequence of Visual Arts, grades 6 to 8 (2026-11-26)

Course `visual-arts-grades-6-to-8`. Cold read of a scope and sequence written by a fresh agent; I did not write it.
Brief: docs/pipeline/briefs/sequence-read.md with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md (the shared core and section "2.
  Arts", items 1 to 9 and "Fails if"), docs/courses/arts/STANDARD.md and docs/courses/arts/APPROACH.md in full.
- docs/courses/visual-arts-grades-6-to-8/scope-and-sequence.md and data/plans/visual-arts-grades-6-to-8/days.csv (192
  rows, every goal and note), cold.
- Beside them: the frame (docs/courses/visual-arts-grades-6-to-8/frame.md: course in brief, Seams, Models carried, Units,
  Course-level checks, Cross-subject, For the lead), the 24 va-g6 to va-g8 rows of data/progressions/arts.csv, the 45
  grade 6 to 8 lines of data/standards/ncas-performance-standards-words.txt, data/plans/calendar.csv (this course, the
  other 6 to 8 arts courses, ELA 6 and 8 units 1 and 2, math 7 units 1 and 2, World Geography and Ancient
  Civilizations I units 1 and 2), the grade 6 to 8 lines of `frame.py calendar`, docs/GLOSSARY.md (day kinds,
  readiness check), build/scope-writes/ARTS-BRIEF.md, and the two earlier reports on the same layer and discipline:
  docs/reviews/sequence-media-arts-grades-3-to-5-2026-11-26.md (for repeat tags) and
  docs/reviews/frame-visual-arts-dance-fixes-2026-11-26.md (settled work swaps; not reopened).
- Gates: `plan.py check` (no failure for this course), `frame.py calendar` (visual-arts-grades-6-to-8: 0 failures; unit
  days 60 a year; 192 days), `sequence.py check visual-arts-grades-6-to-8` (0 failures), `stale.py check` (121 files,
  0 failures). I spent the read on what these cannot see.
- My own count from days.csv: all 45 owned codes sit only on days of their own year, each on at least one teaching day
  before its end-of-unit check day, and each in exactly one end-of-unit check (script run in this read).
- No outside source was opened for this read. The NCAS action lines come from the repository's words file; the critique
  routine and studio habits are background from memory, as the lens marks them.

## Verdict

The scope and sequence is sound in its bones: all 45 grade 6 to 8 codes are placed in the right year and assessed, every
unit has technique steps before making, a critique and a revision before its check, a showing, and works from many
times and places with careful sensitivity notes, and the check weeks and cross-subject leans hold on the calendar. The
biggest risk is the once-a-week path: several merged sessions fold a whole day into a check day that has two spare
minutes, or pack a critique, a revision and a showing into one 40-minute session, so the path a writer builds from would
not run. The one change that matters most is to regroup those merges as settled below; the rest are smaller fixes to
practice slots, two check-day budgets, one untaught technique and stale notes.

## Findings, most serious first

### 1. The once-a-week path does not hold in seven units

LAYER sequence. REPEAT yes (media arts 3 to 5, finding 2). Confidence: firm (the minutes are the frame's own).

**What is wrong.** Two kinds of merge do not fit a 40-minute session.

- *A whole day folded into a check day.* The frame budgets every check day at 3 + 5 + 27 + 3 + 2 minutes. The
  scope and sequence still folds days into "the check's opener": unit 5 ("79 and 80 fold into the check's opener";
  day 79 is a teaching day, the kept candidate study), unit 9 ("144 folds into the check's opener"), unit 2 ("the
  practice day folds into the mid-year opener"), and the 10-days-short year (days 30, 80, 144 and 175 "practice into
  the check's opener"). Two spare minutes cannot hold a practice day or a work study.
- *Four days in one session.* Unit 1 merges days 11 to 14 (critique, revision, showing and the candidate study with a
  written-look practice) into one session. Unit 6 merges 91 to 94 (revise, finish, showing, and day 94, the only
  teaching day of VA:Cr3.1.7a before its check). Unit 12 merges 185 to 188 (write the exhibition stories, critique,
  revise and hang, the family show).

**Why it matters.** A school on the 32-session path (and every quarter rotation, which the frame sends to that path)
gets sessions it cannot run, and in unit 6 the reflection formats would be taught in the last minutes of an overloaded
session the day before they are scored. The frame's rule is that a merge never drops a critique, a revision or a
respond day; packing them into one 40-minute session keeps them only on paper.

**Fix (settled below).** A practice day marked "nothing scored" is dropped on the once-a-week path and on the
10-days-short year, never folded into a check (days 30, 80, 144, 158, 175: unscored, owned parts taught elsewhere).
Regroup so no session holds more than three days and the critique and the revision do not share a session with the
showing as well:

| Unit (sessions) | Regrouped merges (check and respond stay whole) |
|---|---|
| 1 (8) | 1-2, 3-4, 5-6, 7-8, 9-11 (day 10's drill is 11's opener), 12-14 (day 14's candidate cut to a ten-minute look after the showing) |
| 2 (8) | as written, with day 30 dropped, not folded: 17-18, 19-20, 21-22, 23-24, 25-26, 27-29 |
| 5 (9) | 65-66, 67-68, 69-70, 71-72, 73-75 (day 74's drill is 75's opener), 76-77, 78-79 (the living maker's two displays studied at the showing); day 80 dropped |
| 6 (7) | 83-84, 85-87 (85's drill is the opener; the two understanding days merge, the frame's rule), 88-89, 90-91, 92-94 |
| 9 (9) | 129-130, 131-132, 133-134, 135-136 (135's drill is the opener), 137-138, 139-140, 141-143 (142's candidate cut to a ten-minute look at the showing); day 144 dropped |
| 10 (7) | as written, with day 158 dropped: 147-148, 149-150, 151-152, 153-154, 155-157 |
| 12 (5) | 179-181, 182-185 (184's drill is the opener), 186-188 |

Unit 11's merge (163-165, 166-168, 169-171, 172-173, 174-175 with 175 dropped, one merged check, respond) and units 3,
4, 7 and 8 stand as written.

### 2. The show units' "create" is a label on presenting days

LAYER sequence. REPEAT new. Confidence: likely.

**What is wrong.** ARTS-READ asks for all four processes in every unit. Units 4, 8 and 12 claim create on one day each
(days 55, 118 and 185), and each of those days is presenting work: drawing the display plan (VA:Pr5.1.6a), preparing
work two ways (VA:Pr5.1.7a), writing exhibition stories (VA:Pr5.1.8a). The note says "Processes: present; create"
but no create look-for, technique or evidence line goes with it.

**Why it matters.** A unit plan writer reads "create 55" and builds nothing new, so a quarter of the band's units make
no art. The year still touches all four processes, so bar criterion 1 holds per course, but the unit-level claim the
scope and sequence makes is not what the days carry.

**Fix (settled below).** Make the create claim real at no day cost, as practice of the same year's design code, never a
new claim: day 55's display plan is drawn as a design for viewers and checked on unit 3's design-brief look-for
(VA:Cr2.3.6a as practice that returns); day 118's catalog page is laid out with unit 7's hierarchy look-for (VA:Cr2.3.7a
as practice); day 185's introduction panel is laid out on unit 11's pictures-and-words grid (VA:Cr2.3.8a as practice).
Each note names the look-for and the daily evidence line ("what technique I used and what I will change").

### 3. Five codes get one teaching day and no practice before the unseen-work item

LAYER sequence. REPEAT new. Confidence: likely (bar C7, APPROACH "What is carried").

**What is wrong.** Units 5, 9 and 11 give their written response codes a partner-marked practice day before the check
(days 80, 144, 175). Five codes in other units are met on one day and then scored on an unseen work: VA:Re8.1.6a (day 41
only, scored day 47), VA:Re8.1.7a (day 104, scored 111), VA:Re9.1.7a (day 107, scored 111), VA:Pr4.1.6a (day 50, scored
61) and VA:Cn11.1.8a (day 182, scored 189, a sort into four ways of serving group identity).

**Why it matters.** The student's first try without the teacher's model is the scored item; a gap in a response code
shows up only on the respond day.

**Fix (settled below).** A ten-minute partner-marked practice on a second work, inside an existing day: day 45 opener
(context sort and idea and mood on a second work card, VA:Re8.1.6a); day 110, last 15 minutes after the maps are hung
(ideas and mood, and two judgments, on a Curio Class card, VA:Re8.1.7a and VA:Re9.1.7a); day 53 (the drill day: the
three-column chart on a second set of a flat, a 3D and a digital work, VA:Pr4.1.6a); day 184 (the drill day: two
works sorted by the way each serves a group's identity, VA:Cn11.1.8a). Practice only, nothing scored.

### 4. Two check-day budgets do not close

LAYER sequence. REPEAT new. Confidence: firm (arithmetic on the frame's minutes).

**What is wrong.** (a) Unit 11 needs two check days because an argued judgment (VA:Re9.1.8a, day 177) fills a whole
27-minute sitting and the analysis (VA:Re8.1.8a, day 176) another. The year 8 year-end check (day 191) then asks, in
one 27-minute sitting, criteria applied to an unfinished work with two changes planned (VA:Cr3.1.8a) and an argued
judgment with the analysis folded in. (b) The 30-minute period keeps check days "by moving the self-check to the session
before": 3 + 27 + 3 is still 33 minutes.

**Why it matters.** A writer sizing the day 191 items to the day 177 model runs out of time, and students lose marks
to the clock; a school with 30-minute periods has no workable check day.

**Fix (settled below).** Day 191: the VA:Cr3.1.8a item takes 10 minutes (two criteria applied, two changes); the
VA:Re9.1.8a item is a short argued paragraph in 17 minutes (a claim, two reasons each with evidence that names the
work's subject, form or media, which carries VA:Re8.1.8a, and one counterclaim answered). The 30-minute check day:
self-check on the session before, set-up 2, sitting 25, collecting 3, every prompt per part kept and sized to 25
minutes.

### 5. Two things are first met in independent work

LAYER sequence. REPEAT yes (media arts 3 to 5, finding 3, a step used before it is taught). Confidence: likely.

**What is wrong.** (a) The joined panel mural is the year 8 form technique in the frame's ladder, but no day shows it in
steps: day 168 (Application) plans the mural and sets the shared grid, and day 169 paints it. Day 164's grid is the
zine layout, a different job. (b) VA:Cn10.1.6a is met only on day 37 (Application), where each student gathers four
ideas, and the collection card from that day is scored on day 47; nothing earlier shows how.

**Why it matters.** The lens's first error for a unit is "a making task with no technique taught first", and the
frame says no score comes from the day a technique is first met.

**Fix (settled below).** Day 168 becomes Understanding: the panel-and-grid method shown in steps with a step card
(squaring a thumbnail onto panels, edge marks where panels join, a shared color plan), then the group plans. Day 37
opens with the teacher gathering four ideas aloud on the card (shown), before students gather their own.

### 6. Rows used earlier the same year are leaned on with no retrieval

LAYER sequence. REPEAT yes (media arts 3 to 5, finding 5). Confidence: likely.

**What is wrong.** Unit 3's "Why here" says it needs unit 2's idea-making (the frame: "a design starts from a planning
page and a user's retelling is an intent check"), so va-g6-ideas and va-g6-revise; unit 7's says it "uses unit 6's
criteria" (va-g7-ideas). Neither unit retrieves those rows (unit 3 retrieves va-g5-design, va-g5-judge, va-g6-look;
unit 7 va-g6-design, va-g6-judge, va-g7-look).

**Why it matters.** Rule 2 asks for a retrieval task wherever a unit assumes a row used earlier the same year.

**Fix (settled below).** Day 38's opener retrieves the planning page and the intent check (va-g6-ideas, va-g6-revise)
before the user interviews; day 105's opener retrieves the criteria card (va-g7-ideas) before the poster-map plan. Add
both to the `retrieves` column and the units' Retrieval lines.

### 7. Respond days are labeled with the artistic process "respond"

LAYER sequence. REPEAT new. Confidence: firm (the lens names this error; GLOSSARY defines a respond day).

**What is wrong.** All 24 respond days carry "Processes: respond; ..." in their notes, and each unit's "Four
processes" line counts the respond day under respond (for example unit 1 "respond ... 13 to 16").

**Why it matters.** It mixes the day kind with the artistic process, and it inflates the responding count a reviewer
reads off the page.

**Fix (settled below).** On a respond day the Processes line names the process of each part being redone (day 16:
create for the test sheet, responding for the written look). The "Four processes" lines list respond days apart
("respond days 16").

### 8. The logic model drops the honesty line

LAYER sequence. REPEAT new. Confidence: firm (bar C16).

**What is wrong.** The frame's logic model ends "Nothing here has been tried with students, and Curio Class makes no
claim that arts study raises any other result"; the scope and sequence's one-page model leaves it out, and its Outcome
cell reads as a result ("A student who leaves grade 8 makes work ...").

**Fix (settled below).** Head the cell "Outcome sought", and add the frame's sentence under the table.

### 9. Some items list a code but ask only part of it

LAYER sequence. REPEAT yes (media arts 3 to 5, finding 4). Confidence: likely.

- The year 6 year-end check (day 63) gives a planning page "for a given question", which drops the "content that
  matters to you" part of VA:Cr1.2.6a. Fix: the student picks one of three given questions or writes their own, marked
  the same.
- VA:Cr2.1.8a is "try, invent and risk"; the risk log and the day 145 look-for name the planned risk only. Fix: the
  risk log adds one line "one thing I invented (a new mark, a new use of the plate)", and the look-for names it.

### 10. Rotations lose the frame's meeting counts

LAYER sequence. REPEAT new. Confidence: firm.

**What is wrong.** The scope and sequence says a rotation "teaches one year's units in order inside its rotation". The
frame says a daily rotation of at least 64 meetings runs the full path and a quarter rotation (about 40 meetings) runs
the 32-session path. A quarter rotation following the scope and sequence would try 64 days in 40 meetings.

**Fix (settled below).** Replace the Rotations bullet with the frame's two sentences.

### 11. Stale notes and counts

LAYER sequence. REPEAT yes (media arts 3 to 5, finding 8). Confidence: firm.

- For the lead 2: STANDARD.md 3.4 already has the visual arts 6 to 8 row (read 2026-11-25). Delete the item.
- For the lead 4: every arts band course's days.csv counts `school_day` band-wide (1 to 480; visual arts 3 to 5,
  music 6 to 8 and theater 6 to 8 checked), and data/plans/calendar.csv agrees (day 33 is school day 83). Delete the item.
- For the lead 5 and the rule 3 table: 27 of 45 owned codes are not sampled on a course-level day (18 are), not 30.
- Day 30's note: unit 1 ended seven weeks before (week 8 to week 15), not four.
- The Calendar bullet's "result in the final report": state the result (0 failures, 2026-11-26).
- For the lead 3: the supplies ceiling is a money pick for Cory (the frame says so), not the lead's to confirm. Move it.
- Each year heading may name its count: "Year 7 (grade 7 standards, 15 ids)", as the frame asks each year to state.

## What is right and should not be touched

- The band-year rule: every grade 6, 7 and 8 code is on days of its own year only, taught before its check and assessed
  once in an end-of-unit check (counted in this read).
- Check placement: week 17 and week 32 in every year, matching CALENDAR.md's grade 6 to 8 arts weeks; each course-level
  check samples only units before the one just assessed and says so, with unscored records carried, and a reasoned
  table of the unsampled codes.
- The technique ladder (value, then perspective, then gesture and figure; collage papers, then layered wash and ink, then
  a two-color edition) and the step-taught days before each making.
- A critique day (describe, ask, suggest) and a revision day before every showing and check; a showing in every unit; a
  baseline look on a practice day in every unit, never day 1.
- Day 1 of every unit stays clean; retrievals sit in day 2's opener with the ten-minute reteach for a student new to the
  band.
- Works: every year reaches Africa, Asia, Europe, Latin America or the Caribbean, the United States and a Native maker or
  community, with living makers each year; every flagged work (Benin plaques, ledger drawing, terracotta burial, Lam,
  Haida pole, treaty exhibition, Baca's hard history, Inuit goggles, Seminole museum) names its flag and its first source
  in the day note.
- Cross-subject leans: days 43, 49, 105 and 172 each fall after the core unit they lean on (calendar.csv checked), and
  each carries its own frame so nothing of the other course is scored.
- The 10-days-short year folds only drill and practice days, none of them a baseline look.

## What I could not judge

- Whether each named work's rights line holds; that is the unit plan's check on each item's own page.
- Real prices against the $100 ceiling.
- Whether 40 minutes is enough for a paint or print set-up with 30 students; STANDARD.md marks the session length ours,
  untested. A classroom trial would settle it.

## Settled by the expert

| Choice | Reason in one line | File it touches |
|---|---|---|
| Practice days 30, 80, 144, 158 and 175 are dropped on the once-a-week path and the short year, not folded into a check | a check day has 2 spare minutes; the days are unscored | scope-and-sequence.md (units 2, 5, 9, 10, 11; Shorter path) |
| Once-a-week regrouping for units 1, 5, 6, 9 and 12 as in finding 1's table | no session over three days; critique, revision and showing not all in one | scope-and-sequence.md (each unit's once-a-week line) |
| Create made real in show units: days 55, 118, 185 checked on the same year's design look-for, as practice | the unit-level four-process claim must be carried by the day | days.csv notes 55, 118, 185; scope-and-sequence.md units 4, 8, 12 |
| Ten-minute practice slots: day 45 (Re8.1.6a), day 110 (Re8.1.7a, Re9.1.7a), day 53 (Pr4.1.6a), day 184 (Cn11.1.8a) | first unaided try should not be the scored one | days.csv goals and notes 45, 53, 110, 184 |
| Day 191 split: Cr3.1.8a 10 minutes, Re9.1.8a 17 minutes with Re8.1.8a in its evidence | the sitting is 27 minutes | days.csv day 191; scope-and-sequence.md year 8 year-end |
| 30-minute check day: self-check the session before, set-up 2, sitting 25, collecting 3 | 3 + 27 + 3 does not fit 30 | scope-and-sequence.md Shorter path |
| Day 168 kind Application to Understanding, with the panel-and-grid step card | the mural technique is not taught in steps | days.csv day 168 |
| Day 37 opens with the teacher gathering four ideas aloud | Cn10.1.6a first met in independent work | days.csv note 37 |
| Retrieval of va-g6-ideas, va-g6-revise in day 38's opener and va-g7-ideas in day 105's | rule 2, rows used earlier the same year | days.csv `retrieves` and notes 38, 105; scope-and-sequence.md units 3, 7 |
| Respond-day Processes lines name the redone part's process; respond days listed apart in "Four processes" | lens error, GLOSSARY | days.csv respond-day notes; scope-and-sequence.md every unit |
| Logic model: "Outcome sought" and the frame's not-tried sentence | bar C16 | scope-and-sequence.md logic model |
| Day 63 planning page: choose one of three questions or write one's own | carries "content that matters to you" | days.csv day 63 |
| Risk log adds "one thing I invented"; day 145 look-for names it | the "invent" part of Cr2.1.8a | days.csv days 134, 140, 145 |
| Rotations bullet copies the frame's meeting counts | a quarter rotation cannot run 64 days | scope-and-sequence.md How the course runs |
| Stale items of finding 11 fixed as listed | counts and notes a writer would copy | scope-and-sequence.md, days.csv note 30 |

## For the lead (not Cory)

- Defects were not logged with `plan.py defect`: this job's brief allows writing only this report. The lead may log
  findings 1 to 11 with found_by `expert`.
- Finding 1 repeats the media arts 3 to 5 read's finding 2; the once-a-week merge kind may be worth a line in
  sequence-write.md (a practice day is dropped, not folded into a check; no session holds more than three days).

## For Cory

- **Supplies ceiling (money).** The frame's pick stands open: $100 a class of 30 a year for visual arts 6 to 8, every
  unit keeping its free path (provisional costs $60, $70 and $100 by year; year 8's print unit carries brayers and block
  ink). The scope and sequence's materials fit inside it.

## Sources

- data/standards/ncas-performance-standards-words.txt and STANDARD.md 3.1 to 3.4: id placement, counts and pacing (repository).
- docs/ADOPTION-BAR-SUBJECTS.md, arts section and C7, C16: the criteria the findings cite (repository).
- docs/agents/lenses/arts.md: the error list (respond-day wording, technique before making).
- docs/reviews/sequence-media-arts-grades-3-to-5-2026-11-26.md: repeat tags.
- From memory, marked so: the describe, ask, suggest critique routine and studio-habits background (the lens's own
  background note). No outside page was opened.

## For the source list

Nothing new.
