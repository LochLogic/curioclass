# Expert read: scope and sequence of Dance, grades 3 to 5 (2026-11-26)

Course `dance-grades-3-to-5`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write
the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9
  and "Fails if"), docs/courses/arts/STANDARD.md (3.4 pacing in full) and docs/courses/arts/APPROACH.md (kinds of
  day, readiness, scoring, critique, pacing), build/scope-writes/ARTS-BRIEF.md.
- docs/courses/dance-grades-3-to-5/scope-and-sequence.md and data/plans/dance-grades-3-to-5/days.csv (all 192 rows),
  read cold.
- Beside them: the frame (docs/courses/dance-grades-3-to-5/frame.md: the brief, the Units table rows for units 1, 3,
  5 and 9, Course-level checks, Seams), the 24 da-g3 to da-g5 rows of data/progressions/arts.csv, CALENDAR.md's
  grade 3 to 5 rows, data/plans/calendar.csv for this course and for the courses its leans name (science grades 4
  and 5, ELA grades 3 and 5, physical education 3 to 5), the 63 dance lines of
  data/standards/ncas-performance-standards-words.txt, the frame reads
  (frame-dance-grades-3-to-5-codex-2026-11-25.md, frame-dance-grades-k-to-12-2026-11-25.md,
  frame-visual-arts-dance-fixes-2026-11-26.md), later.csv L107, and the media arts 3 to 5 sequence read of today
  for house form.
- Gates: `scripts/plan.py check` (0 failures for this course), `scripts/sequence.py check dance-grades-3-to-5`
  (0 failures), `scripts/frame.py calendar` (frame 0 failures; 60 unit days a year), `scripts/stale.py check`
  (0 failures). I also ran two short scripts over days.csv: all 63 ids sit in their own year, and every id has a
  teaching day before its end-of-unit row, except that DA:Re7.1.5b has no check row at all (finding 5).
- No new outside source was opened. Two part readings in finding 2 rest on memory of the full NCAS performance
  standard text (2014) beside our own-words file, and are marked so.

## Verdict

Sound: the band-year rule holds id by id, every unit has all four processes on named days, technique days come
before the making that needs them, every unit has one critique, a rehearsal of the change and a showing, the works
range over five regions and 1922 to today with their settings and sensitivity flags, and the leans meet the other
courses' weeks. The biggest risk is in the checks: all six course-level checks, and unit 5's end-of-unit showing,
list codes whose items ask about only part of them, so a met mark would claim more than was seen. The one change that
matters most is to bring each check item to the whole code or stop listing the code (finding 1, most of it settled
below); second is the year 5 shorter-year fold-ins, which take away unit 10's last rehearsal and a scored line
(finding 3).

## Findings, most serious first

### 1. Course-level check items ask about only part of the codes they list

LAYER sequence (and frame, for the checks table). REPEAT yes (a check that names a code and samples part of it, as in
earlier reads). Confidence: firm (days.csv against the words file).

- **What is wrong.** Rule: every check task asks about each part of each code it lists. Against the words-file
  lines:
  - Day 33 (year 3 mid-year): DA:Pr5.1.3c is "recall, apply coaching and your own checks to improve"; the look-for
    is the recall with no cue only. DA:Pr4.1.3b's "stay with the music's timing" is not in the look-for either
    (the item is "fills a new set count with two energy qualities").
  - Day 51 (year 3 year-end): DA:Cr1.1.3a is moves from starting points "you picked yourself"; the item gives "a new
    starting point".
  - Day 97 (year 4 mid-year): DA:Pr5.1.4c's goal part and DA:Pr4.1.4b's percussion and steady and uneven rhythm
    parts are not sampled (the note says so).
  - Day 115 (year 4 year-end): DA:Pr4.1.4c ends "then refine phrases"; the written item has no refinement.
    DA:Cr1.1.4b is "invent a movement challenge and change elements to solve it"; the item has the student solve "a
    partner new challenge", so the student invents nothing.
  - Day 163 (year 5 mid-year): DA:Pr5.1.5c's goal part is not sampled.
  - Day 179 (year 5 year-end): DA:Pr4.1.5c is contrast tight and flowing, start moves from torso or limbs, analyze
    energy; the item is written only, on the teacher's phrase, so the student does none of the moving parts.
    DA:Cr1.1.5a asks for "several inspirations"; the item gives one new source.
  The scope's For the lead item 3 names the year 4 and 5 mid-year gaps but misses the rest. Its For the lead item 1
  also offers "one written item on a unit-2, 6 or 10 id" at the mid-year check: those are the units assessed two or
  three days before, which the no-repeat rule forbids.
- **Why it matters.** A met mark on the check is read as the whole code met again; a teacher building the check from
  this row writes items that cannot show it.
- **The fix.** Settled below for the items that can be made whole inside the minutes (days 51, 115, 179 for
  DA:Cr1.1.5a, and the goal parts on days 97 and 163, using the 10 minutes the mid-year checks do not spend on a
  written part). For the lead, as frame table changes: on day 33 either add "one coach comment, then the sequence
  again" to the group turn or list DA:Pr5.1.3c as practice, not a sample, and name DA:Pr4.1.3b's timing part in the
  look-for; on day 97 list DA:Pr4.1.4b as practice or add the drum part to a group turn; on day 179 sample
  DA:Cn10.1.5a (fully answerable in writing, unit 10) in place of DA:Pr4.1.5c. Replace For the lead item 1's first
  option with one that samples a unit-1, 5 or 9 id in writing, such as DA:Pr5.1.5b's "discuss how habits and
  nutrition prevent injury" from a new invented dancer card at the year 5 mid-year check, its practice part seen in
  the showing.

### 2. Unit 5's end-of-unit showing leaves out a part of two codes

LAYER frame (the frame's evidence line), carried into sequence. REPEAT yes (an owned part not assessed).
Confidence: likely (words file plus the full NCAS text from memory).

- **What is wrong.** Day 78 scores DA:Pr5.1.4c as "the group starting and changing on a dancer cue". The words-file
  line is "sync phrases with fellow dancers using music or lighting cues"; the full standard (from memory) has both
  cueing off each other and responding to stimulus cues such as music or lighting. Day 73 teaches all three cues
  (music, the held card, a dancer's cue), but the check sees only the dancer's cue, the one the words line does not
  name. DA:Pr4.1.4b is "play percussion for dancers, move to steady and irregular rhythms, react to tempo shifts";
  the look-for is "plays the part on two sounds once and dances once through a tempo change", so the steady and
  uneven rhythm part is never looked at.
- **Why it matters.** Both are owned grade 4 parts scored only here; the unit plan will copy the look-for as written.
- **The fix.** Settled below for day 78. For the lead: the frame's unit 5 "End-of-unit evidence" line needs the same
  two changes.

### 3. The year 5 shorter-year fold-ins take away unit 10's last rehearsal and a scored line

LAYER sequence. REPEAT new. Confidence: firm.

- **What is wrong.** Year 5's fold-in days are 142, 150, 158 and 159. Day 158 is the only rehearsal of the whole
  showing after making cycle 2, and it is where each group writes the two comparison lines that day 160 scores for
  DA:Cn10.1.5b ("the matter dance with its notes and three lines"). Day 159 is the run-through; its frames go "into
  the warm-up of day 160", a check day. With both folded, the matter dance finished on day 157 goes to the showing
  with no rehearsal, and a scored part is made inside another day's minutes. The scope's own "What was hard to
  settle" says run-throughs before showings are kept, which days 142 and 159 contradict. (Day 142's full run folds
  into day 141, which already runs the dance against the goals, so that one holds.)
- **Why it matters.** The rule for the short year is nothing assessed and no owned part cut; here the making of a
  scored line and the rehearsal before a showing are cut.
- **The fix (settled below).** Keep day 158 on the short path. Fold 159's frames into the warm-ups of days 157 and
  158, not of check day 160. Take the fourth fold-in from day 167 (paired-tool rounds into the warm-ups of days 168
  and 169), its baseline look moved to those two warm-ups by rotating groups. Correct the "What was hard to settle"
  sentence: run-throughs before showings are kept, except day 142, whose run sits inside day 141.

### 4. The once-a-week path packs four owned ids' first teaching into one session in four units

LAYER frame (the session counts per unit). REPEAT yes (today's media arts 3 to 5 read found the same in its frame).
Confidence: judgment call.

- **What is wrong.** The path keeps every id nominally, but in units 4, 8, 11 and 12 the merged sessions cannot
  teach in steps. Unit 12 session 1 (days 181 to 186) holds the hook watch, the run of the unit 11 study, the
  ten-minute retrieval, the change log, the frevo watch with the venue plan, staging trials and the suggestion card:
  four owned ids' first teaching in about 15 minutes after set-up, warm-up, retrieval and cool-down. Unit 11 session
  2 (days 168 to 171) teaches four responding ids with two dance watches. Units 4 and 8 sessions 1 and 2 teach four
  ids and a dance watch in two sessions. Unit 9, by contrast, merges only two days in most of its early sessions.
- **Why it matters.** The bar's "Fails if" names prompts to make with no technique taught; on this path a group
  makes the unit 12 adaptation in the session after a single pass at four techniques.
- **The fix.** For the lead (frame): in year 5 move one session from unit 9 to unit 11 (8 and 7 sessions; unit 9's
  sessions 1 to 4 can merge three days each as unit 10's do), so unit 11 teaches two responding ids a session. Units
  4, 8 and 12 stay at five sessions (two showing or check sessions and respond are fixed); the scope's unit 12 split
  is settled below so the suggestion card is taught in the session that uses it.

### 5. DA:Re7.1.5b sits on no check row, and unit 11's responding ids get no practice before the written day

LAYER sequence. REPEAT new. Confidence: firm.

- **What is wrong.** The style card (DA:Re7.1.5b) is finished on day 175 and "scored beside" day 177, but day 177's
  codes do not list it, so no row with assess=end carries the id (units 4 and 8 list their kept cards on the check
  row). Separately, DA:Re7.1.5a, DA:Re8.1.5a and DA:Re9.1.5a each have one teaching day (168, 169, 170) and no
  practice before the written day 177; units 3 and 7 give the same kind of ids a frames run (days 47, 111).
- **Why it matters.** The gates and the unit plan read the codes column; an id with no check row looks unassessed.
  A written item answered on frames met once, a week before, rests on recall alone.
- **The fix (settled below).** Add DA:Re7.1.5b to day 177's codes. Put a five-minute frames run (purpose from
  pattern, two moves that carry the idea, opinion with two traits) in the warm-ups of days 174 and 175.

### 6. The mid-year check notes carry a written part the checks do not have

LAYER sequence. REPEAT new. Confidence: firm. Minor.

- **What is wrong.** Days 33, 97 and 163 copy the course-check budget "written part first ... (10)" and 38 minutes,
  while day 33 says "no written part needed" and none of the three has a written item.
- **The fix (settled below).** State each mid-year budget as it runs (see the table), with the freed minutes used as
  finding 1 sets.

### 7. school_day is one less than scripts/frame.py's spread, and calendar.csv still shows the frame's numbers

LAYER process. REPEAT new. Confidence: firm. Minor.

- **What is wrong.** The scope counts course day n on school day ceil(2.5 n) minus 1 (day 1 on school day 2, day 33
  on 82), band-long (year 4 from 161). frame.py's even spread, and data/plans/calendar.csv as it stands, put day 1
  on school day 3 and day 33 on 83, per year. Every week agrees, so no check moves. Dance K to 2 and visual arts 3 to
  5 use this scope's convention; music 3 to 5 and dance 6 to 8 use frame.py's.
- **The fix.** For the lead: pick one convention for every K to 8 band course and regenerate calendar.csv; nothing to
  change in this scope until then.

## Checked and right; do not touch

- **Which grade in which year:** stated once on the first page; every one of the 63 codes is on days of its own year.
- **Readiness and retrieval:** every unit assumes only the row one grade back (progression `assumes` column agrees),
  so each opens with day 2 retrieval and none has a readiness check; day 1 stays clean; the year 3 "by course order"
  reteach is carried in each year 3 retrieval note.
- **Order inside units:** each model starts on the day the progression says (phrase-recall day 10, choreographic
  tools day 36, feedback-loop modeled day 12 and owned day 56, energy words day 74, research notes day 88,
  dance-reason-because day 106, rehearsal goals day 137, change log day 182). Technique and watch days precede the
  making; the critique is the second application day and the next day rehearses the change.
- **Four processes:** the table names days for each process in every unit; in units 1, 5 and 9 connecting is light
  (the works' settings on days 1 and 4), which meets the bar and the frame.
- **Works:** Africa, the Americas, Asia, Europe and the Pacific, 1922 to today, living makers each year; every
  sensitivity flag in the frame is in the day note (kathak, legong, Les Ballets Africains leave-out lines; gumboot,
  bomba, Hard Time Blues one-sentence settings).
- **Calendar:** checks on CALENDAR.md's weeks (17 and 26; 18 and 26 in year 5); the science grade 4 waves bridge,
  science grade 5 unit 1 before day 153, ELA SL.3.1 and W.5.1 bridges and physical education's later dance units
  all match calendar.csv.
- **No repeat after a unit's end:** each check draws from the units before the one just assessed, and says so.
- **Rule 3:** the 41 unsampled ids are named with a reason (finding 1 changes only the lead's option).
- **Task form inside two weeks** (For the lead 2): rightly raised; I would accept the repeat in writing for
  performing ids, since the content is new each time.
- **Once-a-week arithmetic:** 32 sessions a year, check sessions on the full path's weeks, respond a week later, as
  the frame sets.
- **Shorter period (30 minutes):** the split of a written day's show items into the respond day keeps every item.

## The lens checklist (scope and sequence layer)

| Line | Result |
|---|---|
| A grade's ids in the wrong year | Met: none |
| A year with one artistic process missing | Met |
| Works from one tradition or one century | Met |
| Technique that does not get harder | Met: the frame's ladder is followed day by day |
| A plan that needs a daily period | Met: two 40-minute sessions, a 32-session path |
| No showing in a unit | Met: every unit shows; three family showings |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 51: the student picks one of three new starting-point cards for the showing look-for (DA:Cr1.1.3a) | The code asks for starting points the student picked | days.csv day 51 |
| Day 115: the written item adds one line refining the new phrase (DA:Pr4.1.4c); each student draws a challenge card in the written part that the partner solves in the showing, both scored (DA:Cr1.1.4b) | Brings both codes whole inside the minutes | days.csv day 115 |
| Day 179: material from two new sources (a story card and a nature card), a source line for each (DA:Cr1.1.5a) | "Several inspirations" | days.csv day 179 |
| Days 97 and 163: after the group turns, each student writes one goal from the teacher's comment on the goal card (kept, scored) | Brings the goal parts of DA:Pr5.1.4c and DA:Pr5.1.5c into the check, in the minutes no written part uses | days.csv days 97, 163 |
| Day 97: the new cue is a dancer's cue to start and the drum or held card to change | Both cue parts of DA:Pr5.1.4c | days.csv day 97 |
| Day 78: the cue look-for reads "starts together on a dancer's cue and changes on the drum or the held card"; the DA:Pr4.1.4b look-for adds "dances a steady and an uneven pattern" | Each part of each code on the end-of-unit showing | days.csv day 78, scope unit 5 Assessments |
| Mid-year budgets (days 33, 97, 163): set-up 3, warm-up 5, six groups at about 4 minutes (24), goal lines 4 (days 97 and 163; day 33 cool-down instead), cool-down and room back 4: 40 | Matches what the day does | days.csv notes |
| Year 5 fold-ins: 142, 150, 159 (frames into the warm-ups of 157 and 158) and 167 (into the warm-ups of 168 and 169, baseline look moved there); day 158 kept | Keeps unit 10's rehearsal and its scored lines | days.csv notes, scope Shorter path table and "What was hard to settle" |
| Day 177 codes add DA:Re7.1.5b | The kept style card is scored with that day | days.csv day 177 |
| Five-minute responding frames run in the warm-ups of days 174 and 175 | Practice before the written day, as units 3 and 7 | days.csv notes |
| Unit 12 once-a-week sessions: 1 = days 181 to 185, 2 = days 186 to 189 | The suggestion card is taught in the session that uses it | scope once-a-week table, days.csv notes |

## For Cory

Nothing. Every finding is inside the standards' limits, the frame or the scope; none changes scope, audience, money
or people.

## What I could not judge

- Whether 40 minutes holds six groups at about four minutes with a class of 30 in a real gym; it needs a trial.
- The full NCAS wording behind findings 1 and 2 was not reopened; the words file is the evidence, memory the support.

## Sources

- data/standards/ncas-performance-standards-words.txt: the part-by-part reading of every code.
- National Core Arts Standards, dance, grades 3 to 5 (2014), from memory: the cueing and rhythm parts in finding 2.

Report: docs/reviews/sequence-dance-grades-3-to-5-2026-11-26.md
