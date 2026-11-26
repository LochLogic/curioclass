# Expert read: scope and sequence of Theater, grades 3 to 5 (2026-11-26)

Course `theater-grades-3-to-5`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), as
docs/pipeline/briefs/sequence-read.md and build/scope-writes/ARTS-READ.md ask. The scope was written by a fresh agent;
this reader did not write it.

## What I read

- The scope and sequence (docs/courses/theater-grades-3-to-5/scope-and-sequence.md, whole) and all 192 rows of
  data/plans/theater-grades-3-to-5/days.csv, read cold.
- Beside them: the frame (docs/courses/theater-grades-3-to-5/frame.md, whole), the th-g3, th-g4 and th-g5 rows of
  data/progressions/arts.csv, the 72 grade 3 to 5 theater lines of data/standards/ncas-performance-standards-words.txt,
  the course's rows in docs/courses/CALENDAR.md, the ELA grade 3, 4 and 5 rows of data/plans/calendar.csv, and the ELA
  grade 3 to 5 days.csv files for the leans (RL.3.3, SL.4.4, RL.5.3, W.3.1, W.4.1, W.5.1).
- The bar: docs/ADOPTION-BAR-SUBJECTS.md section 2 (items 1 to 9 and "Fails if"), docs/courses/arts/STANDARD.md 3.4,
  docs/courses/arts/APPROACH.md (the unit fields, "Ties to the student's own life"), the lens
  docs/agents/lenses/arts.md, docs/agents/EXPERT.md and the writer's brief build/scope-writes/ARTS-BRIEF.md.
- Earlier reads: docs/reviews/sequence-theater-grades-k-to-2-2026-11-26.md (same day, same discipline) and the
  short-path precedent in docs/reviews/sequence-3-5-fixes-2026-11-14.md ("no sole-code day is compressible"). This
  read agrees with the K to 2 read's once-a-week finding and does not reopen anything it settled.
- Gates, run first: `plan.py check` (sequence theater-grades-3-to-5: 0 failures), `frame.py calendar` (frame
  theater-grades-3-to-5: 0 failures; 60 unit days a year), `sequence.py check theater-grades-3-to-5` (0 failures),
  `stale.py check` (121 files, 0 failures). My own scripts confirmed: each of the three years carries exactly its
  grade's 24 ids, every id is on at least one teaching day of its own year, no id sits in the wrong year, every
  progression row assumes only the row one grade back (so retrieval, never readiness, is right throughout), and every
  check week in days.csv matches CALENDAR.md (17 and 27; 17 and 26; 18 and 27).
- No outside source was opened for this read; what rests on memory is marked. Per the brief I edited nothing but this
  report, so no defect was logged with `plan.py defect`; the caller may log them.

## Verdict

The scope is sound on what matters most: all 72 ids sit in the right year, every unit teaches its technique in steps
before the making, runs one critique and a revision before a two-day end-of-unit assessment that names every owned id,
and the works range across five regions with living makers each year. The biggest risk is the once-a-week path: units
3, 4, 7, 8, 11 and 12 merge four or five teaching days, several of them the first teaching of an owned id, into one
40-minute session, so the path holds on paper only; the 10-days-short list also folds the only teaching days of two
year 5 ids. The one change that matters most is the lead's frame fix for the once-a-week sessions (finding 1); the
fold-list swaps are settled below.

Finding count: 9 (2 serious, 4 moderate, 3 minor).

## Findings, most serious first

### 1. The once-a-week path does not hold for the design and story units (serious)

LAYER frame and sequence. REPEAT yes (the same kind as finding 1 of the theater K to 2 read, 2026-11-26).

**What is wrong.** On the once-a-week path every unit keeps three sessions for the showing, the written check and
respond, so a year's 28 unit sessions leave 16 for 48 teaching days. The frame's counts then put the most compression
on the heaviest units:
- Unit 3 session 2 (days 39 to 43): the making steps with their 6-minute clean-up, Roadside Theater and the two-ties
  card (first teaching of TH:Cn11.1.3a), the community piece (first teaching of TH:Cn10.1.3a) and a fluency run.
- Unit 4 session 1 (days 55 to 59): the hook and adaptation (TH:Cn11.2.3a), the 10-minute retrieval and dramatic
  structure (TH:Pr4.1.3a), the past artists and the griot reading (TH:Cn11.2.3b), the baseline run, and judging with
  the criteria card (TH:Re9.1.3a, TH:Re9.1.3c): five first teachings in 40 minutes.
- Unit 7 sessions 1 and 2 (99 to 102; 103 to 105): Appia, the light plan with retrieval, tholu bommalata and cues,
  then FastHorse (a sensitive study), the cultural-view comparison and the local-problem scene.
- Unit 8 session 2 (121 to 124): the baseline run, judging taught, the critique, the revision and two kept cards.
- Unit 11 session 2 (169 to 173): Laedza Batanani, the investigation sheet, cultural views (the only teaching day of
  TH:Re8.1.5b), the scene build and a cue run; session 3 (174 to 177) holds rehearsal, critique, revision, the last run
  and four kept sheets.
- Unit 12 session 1 (183 to 187): three tellings compared, retrieval and the hidden-thought line, the First Folio,
  the baseline run and the judging guide.

Meanwhile units 1, 2, 5, 6, 9 and 10 merge two or three days a session. The scope's own "For the lead" item 3 sees
this and leaves it to the unit plans.

**Why it matters.** The brief asks that the once-a-week path hold with no assessed or owned part cut. An id taught in
six minutes inside a five-day session is cut in the room, and a writer building the once-a-week teacher page from these
lines would write sessions that cannot be taught. Bar item 9 leans on this path.

**Why the counts cannot simply be moved.** The check weeks pin each year: units 1 and 2 must fill weeks 1 to 16
(year 5: 1 to 17, since week 17 is a grade 5 core check week), and the year-end check and respond sessions hold weeks
26 and 27, so units 3 and 4 (7, 11 and 8, 12) share weeks 19 to 25 and 28 to 32 whatever the split.

**Fix (for the lead, since the frame changes).** Preferred: on the once-a-week path only, keep the year-end
course-level check and drop the mid-year one. Every id is already assessed id by id in its own unit, and the mid-year
check samples only 4 or 5 ids. The design unit then starts in week 17: year 3 units 8, 8, 9, 5; year 4 8, 8, 9, 5;
year 5 8, 9, 8, 5 (unit 11 starts week 18). That gives units 3, 7 and 11 six or five teaching sessions instead of four
or three, and the scope then lists them as, for example, unit 3: 1 (35, 36, 37), 2 (38, 39 making), 3 (40, 41, 42),
4 (43, 44, 45), 5 (46, 47, 48), 6 (49 last run with kept sheets), then showing, written, respond. Story units keep 5
sessions but split session 1: study and teaching only (55 to 57; 117 to 119; 183 to 185), with the baseline run and
the judging teaching opening session 2 before its critique and revision. If the lead keeps both checks, the frame and
the scope should instead say plainly that the once-a-week year compresses the teaching of the design and story units,
and the scope must give each merged session of three or more days a minute line naming what each merged day keeps.
Either way the scope's session lists change.

Confidence: firm on the arithmetic (the minute budgets are the frame's own); likely on the preferred fix.

### 2. The 10-days-short list folds the only teaching days of two year 5 ids, and four folds land on full retrieval days (serious)

LAYER sequence. REPEAT yes (the grades 3 to 5 fix pass of 2026-11-14 set "no sole-code day is compressible"; the
theater K to 2 read found the same).

**What is wrong.**
- Day 171 is the only teaching day of TH:Re8.1.5b (cultural views shape a response, a written item on day 179), and it
  folds into day 170. With all ten year 5 folds, TH:Re8.1.5a loses both its teaching days (153 into 152, 158 into
  159). Those two ids would reach the written day with no day of their own.
- Days 18, 66, 82 and 130 each carry the 10-minute retrieval opener, yet each receives a 15-minute fold (19, 67, 83,
  131). With set-up 3, warm-up 5 and close 4, that leaves 3 minutes for the day's own technique (the body set, the
  given-circumstances card, the three-centers walk, the inner-thought line).
- Day 158 (pairs write and defend reactions with the teacher's feedback, the unit's only practice of the skill that
  makes unit 10 the longest) is in year 5's "first four", the case most schools will use.

**Why it matters.** The brief and the precedent rule out an owned, assessed id losing its only teaching; the
receiving-day overload makes four first teachings unworkable on the short path.

**Fix (settled below).** Year 5: replace 171 with 167 (the cue sheet folds into the cue drill on day 168, 15 minutes,
saves 25) and 153 with 149 (picking matched warm-ups folds into the warm-up slot of day 148, 15 minutes, saves 25);
move 158 to the end of the year 5 list and 134 into the first four (year 5 first four then save 130 minutes, all ten
still 285). Receiving days: 19 folds into 20, 67 into 68, 83 into 84, 131 into 132, each as a 15-minute segment of the
fluency day that runs the technique (same savings). The fold notes in days.csv and the table and totals in the .md
change to match.

Confidence: firm.

### 3. The 10-day story units put critique, revision and two kept cards on one day (moderate)

LAYER sequence. REPEAT new.

**What is wrong.** Day 60 (unit 4) holds the teacher-led critique of six groups, the revision and the completion of
the story map and criteria card; day 188 (unit 12) holds the student-run critique, the revision, the script annotation
and the script page. After set-up, warm-up and close there are 28 minutes; six groups shown and critiqued in turn need
about 24 on their own. Day 124 (unit 8, revision with two kept charts) is tight but workable.

**Why it matters.** The revision is the step the bar's item 6 checks, and the kept cards are end-of-unit evidence; on
the day as written one of the three gets squeezed out, and the most likely one to go is the revision.

**Fix.** Settled below: the story map is completed in the last 5 minutes of day 58 (structure was taught on 56, the
map follows the three runs); the script annotation in the last 5 minutes of day 186 (hidden thought taught 184), both
revisable on the critique day before collection. For the lead: if day 60 still cannot hold a whole-class critique of
six groups, the frame's unit 4 should either run the critique on two model groups with the rest applying the three
steps to their own run, or make the showing check the family showing (as the once-a-week path already does) so day 61
becomes the revision day.

Confidence: likely (minutes are the frame's own; the critique pace is from memory of grade 3 classes).

### 4. The connecting process in six units rests on days that do not carry it (moderate)

LAYER sequence. REPEAT new.

**What is wrong.** ARTS-READ asks for all four processes in every unit, and the .md names the days. In units 1, 2, 5,
6, 9 and 10 no connecting id is owned, and the named days do not hold it: day 1 and day 129 ("a tale set beside a
scene of today") and day 135 ("the jobs of a real show") have no such step in their goals; days 24, 88 and 153 are
TH:Re8 days (experiences of watching drama), which is responding, not connecting.

**Why it matters.** A unit plan writer reads the .md line, finds nothing on the day and drops it; the year still has
all four processes, but these units would not.

**Fix (settled below).** Name the connecting step on the study day where the work's setting is taught, inside its
minutes (anchor 11, work in its context): day 1 goal adds "what the 1611 players and the class both do with an
outline"; day 17 "where kyogen sits on a day of noh and why families hand it down"; day 71 stays; day 81 "the Tramp in
1925 and who laughed at him"; day 129 "an 1838 toy and a toy of today"; day 147 "where pansori was sung and for whom".
The .md process lines for units 1, 2, 5, 6, 9 and 10 then cite 1, 17, 71, 81, 129 and 147, and stop calling days 24,
88, 135 and 153 connecting.

Confidence: likely.

### 5. An invented experience is allowed where the standard asks for the student's own (moderate)

LAYER frame. REPEAT new.

**What is wrong.** TH:Re8.1.3a, TH:Re8.1.4a and TH:Re8.1.5a ask for the student's own experiences of joining in or
watching drama (words file lines). The frame and scope accept "an invented one, marked the same" (days 24, 31, 153,
161). APPROACH gives the invented option for ties to the student's own life (Cn10), not for these.

**Why it matters.** Every student has the class's own scenes and the partner-class showings as drama experiences, so
the option is not needed for safety, and a student can meet the id without its part "your own".

**Fix (for the lead, frame wording).** The item asks for at least one experience from this year's theater class (a
class scene, a partner showing), which every student has; an invented or outside-school experience may be the second.
TH:Re8.1.5b (cultural views shaping the student's response) keeps its invented-viewer option as a sensitivity choice,
named in the frame as a deliberate trade.

Confidence: judgment call.

### 6. The shorter-period arithmetic fails at 30 minutes and on two showing days (moderate)

LAYER sequence. REPEAT new.

**What is wrong.** The .md says a showing day fits a 30 to 35 minute period with the warm-up done in the line, and the
written day fits "as it stands (33 minutes)". At 30 minutes the written day is 31 with the shorter set-up and close,
and a showing day is 32 with its self-check. Units 2 and 6 mark the warm-up itself on the showing day (TH:Pr5.1.3a,
TH:Pr5.1.4a), so it cannot be done in the line.

**Fix (settled below).** On a 30 to 35 minute period: the response card time drops from 15 to 12 minutes (still at
most two items), and the self-check on the guide moves from the showing day to the written day; units 2 and 6 keep
their marked 5-minute warm-up on the showing day with groups of about 3.5 minutes. The .md's "A shorter period"
paragraph says so.

Confidence: firm.

### 7. Three course-level check items do not ask for every part of their id (minor)

LAYER sequence. REPEAT yes (same kind as finding 5 of the theater K to 2 read).

- Day 163 marks TH:Cr2.1.5a live, but a performance cannot show that the scene was shaped from the group's questions.
- Day 53's kept reflection line covers reflecting alone, not "with a few classmates" (TH:Pr6.1.3a).
- Day 181's self-review line follows the first run with no rerun, but TH:Cr3.1.5a is revising by repeating and
  self-reviewing.

**Fix (settled below).** Day 163: the 4-minute record card holds two lines, one group question and the
inner-thought line (TH:Cr1.1.5c); TH:Cr2.1.5a is marked from the question line. Day 53: the card has one line alone
and one agreed with the group, as the unit 1 log page does. Day 181: the self-review line is written after the first
rehearsal run inside the 8 planning minutes and names the change made in the rerun.

Confidence: likely.

### 8. Two unit items miss a part of their id (minor)

LAYER sequence. REPEAT new.

TH:Cr1.1.3a names characters, settings and improvised stories; the look-for on days 4, 14 and 33 names a character and
a place only. TH:Re7.1.4a is spotting choices "by joining in and watching"; the kept card on day 94 asks only about
another group's actor. **Fix (settled below):** the look-for adds "and a story the group made up from the card"; the
day 94 card adds one line on a choice the student's own pair made. Confidence: firm.

### 9. Small fixes (minor)

LAYER sequence. REPEAT new.

- The .md's school_day sentence says day n "falls in year (school_day - 1) // 160", which gives 0 to 2; it should read
  year 3 + (school_day - 1) // 160.
- Day 183's hook uses "a fish bone": the frame's props rule (nothing sharp or small enough to swallow) wants a paper
  cutout; the note says so.

Confidence: firm.

## What is right and should not be touched

- The band-year split: each year claims exactly its grade's 24 ids; the .md says so once, on the first page.
- Retrieval inside day 2's opener for every unit, with day 1 kept for the hook; no readiness check is needed, and the
  .md says why.
- One critique and one revision before every end-of-unit assessment; the teacher-led protocol in units 1 to 4 and the
  student-run card from day 73 on.
- The showing day and written day split, the at-most-two written items, and response time counted once.
- The course-level checks draw from earlier units, say so, and list the 49 unsampled ids with reasons (rule 3).
- The ELA leans and bridges: checked against the ELA days.csv files, RL.3.3, SL.4.4 and RL.5.3 are taught before use,
  and W.3.1, W.4.1 and W.5.1 come later with the response card frame as the bridge.
- The works' range and their sensitivity and safety notes on the day rows.

## What it could not judge

- Whether the minute budgets hold in a real room of 30 (untested, as the logic model says).
- The rights lines and community-source checks on the named works (Holder, FastHorse, Mhlophe, Laedza Batanani, the
  Zuni telling); these are the unit plans' browser checks.
- Whether the Re8.1.3b and Re8.1.4b tasks (a costume piece "showing a cultural view") can be done by grade 3 and 4
  students without drifting into dressing as a group; that is the sensitivity agent's read of units 3 and 7.

## Sources

None opened outside the repository for this read; the bar documents, the words file and the frame were the evidence.
Classroom pacing claims (critique minutes for six groups) rest on memory.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Year 5 fold list: 171 replaced by 167 (into 168, 15 minutes, saves 25) | 171 is the only teaching day of TH:Re8.1.5b | data/plans/theater-grades-3-to-5/days.csv; scope-and-sequence.md Shorter path |
| Year 5 fold list: 153 replaced by 149 (into 148, 15 minutes, saves 25) | with 153 and 158 both folded, TH:Re8.1.5a has no teaching day | same |
| Year 5 first four: 134 in, 158 moved to the end of the list | 158 is the only feedback on defended reactions | same |
| Folds 19, 67, 83, 131 go into 20, 68, 84, 132 instead of 18, 66, 82, 130 | receiving days already carry the 10-minute retrieval | same |
| Story map completed at the end of day 58; script annotation at the end of day 186 | days 60 and 188 cannot hold critique, revision and two cards | days.csv; scope-and-sequence.md units 4 and 12 |
| Connecting step named on days 1, 17, 81, 129, 147 (71 stays); .md process lines cite them | named connect days did not carry it, or were responding | days.csv; scope-and-sequence.md units 1, 2, 5, 6, 9, 10 |
| Shorter period: response card 12 minutes, self-check moved to the written day; units 2 and 6 keep the marked warm-up | 30-minute arithmetic | scope-and-sequence.md "A shorter period" |
| Day 163 record card: one group question plus the inner-thought line | TH:Cr2.1.5a cannot be seen live | days.csv; scope-and-sequence.md check table |
| Day 53 reflection card: one line alone, one with the group | TH:Pr6.1.3a part "with classmates" | same |
| Day 181: self-review in the rehearsal minutes, naming the change made in the rerun | TH:Cr3.1.5a part "repeating" | same |
| TH:Cr1.1.3a look-for adds "a story the group made up from the card" (days 4, 14, 33) | part "improvised stories" | days.csv |
| Day 94 audience card adds one choice the student's own pair made | TH:Re7.1.4a part "joining in" | days.csv |
| school_day sentence corrected to year 3 + (school_day - 1) // 160 | formula gave 0 to 2 | scope-and-sequence.md |
| Day 183 hook: a paper fish-bone cutout | props rule | days.csv |

## For Cory

- Supplies ceiling (money): carried from the frame, provisional $35, $40 and $30 a class for years 3, 4 and 5, all
  optional beside a free path; the frame's pick is a $40 ceiling a class a year. Not changed by this read.
