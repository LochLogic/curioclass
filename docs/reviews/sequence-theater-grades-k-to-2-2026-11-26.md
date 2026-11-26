# Expert read: scope and sequence of Theater, grades K to 2 (2026-11-26)

Course `theater-grades-k-to-2`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), as
docs/pipeline/briefs/sequence-read.md and build/scope-writes/ARTS-READ.md ask. The scope was written by a fresh agent;
this reader did not write it.

## What I read

- The scope and sequence (docs/courses/theater-grades-k-to-2/scope-and-sequence.md) and all 192 rows of
  data/plans/theater-grades-k-to-2/days.csv, read cold.
- Beside them: the frame (docs/courses/theater-grades-k-to-2/frame.md, whole), the theater rows of
  data/progressions/arts.csv (th-k-*, th-g1-*, th-g2-*, th-g3-*), the theater lines of
  data/standards/ncas-performance-standards-words.txt (65 K to 2 ids), docs/courses/CALENDAR.md and the course's rows
  of data/plans/calendar.csv, and the ELA K, 1 and 2 days.csv files for the four leans.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md section 2 (items 1 to 9 and "Fails if"), docs/courses/arts/STANDARD.md (3.1,
  3.4), docs/courses/arts/APPROACH.md (whole), the lens docs/agents/lenses/arts.md, docs/agents/EXPERT.md, the writer's
  brief build/scope-writes/ARTS-BRIEF.md and docs/pipeline/briefs/sequence-write.md (rules 1 to 11).
- Earlier reads: no earlier sequence read of any arts course exists in docs/reviews/. I checked the short-path
  precedent in docs/reviews/sequence-3-5-fixes-2026-11-14.md ("no assessment, respond or sole-code day is
  compressible").
- Gates, run first: `plan.py check` passes for this course (sequence theater-grades-k-to-2: 0 failures);
  `frame.py calendar` reports no theater failure; `sequence.py check theater-grades-k-to-2` 0 failures;
  `stale.py check` 121 files, 0 failures. My own script confirmed: every code sits in its own grade's year; every
  owned id of every unit is on the unit's end-of-unit days and on at least one teaching day before them; no unit
  carries a code it does not own; every year 1 and year 2 row assumes only the row one grade back, so retrieval (never
  readiness) is the right treatment throughout, and day 2 of each unit carries it in `retrieves`.

## Verdict

The scope is sound on the things that matter most: all 65 ids sit on days of the right year, every unit teaches
technique before making, runs one critique and a revision before a two-day end-of-unit assessment that covers every
owned id, and the band's works range across five continents with living makers each year. The biggest risk is the
once-a-week path: as written, unit 3 merges a making day, two studied traditions and both connecting ids into one
40-minute session, and the story units and unit 6 merge three to six teaching days into one, so the path the bar
item 9 leans on does not hold in a real room. The one change that matters most is rebalancing the frame's
once-a-week session counts (year K 8, 8, 7, 5; year 1 7, 9, 7, 5) and splitting each story unit's study session from
its acting session.

Finding count: 12 (2 serious, 4 moderate, 6 minor).

## Findings, most serious first

### 1. The once-a-week path does not hold for unit 3, the story units or unit 6 (serious)

LAYER frame and sequence. REPEAT new.

**What is wrong.** The frame fixes the session counts (year K 9, 9, 5, 5; years 1 and 2 8, 8, 7, 5) and every unit
keeps three check sessions (showing, teacher's table, respond), so a 5-session unit has two sessions for all its
teaching. The scope then writes:
- Unit 3, session 1 = days 39 to 46: the Paper Bag Players study, the prop-sketch and puppet steps, the making day
  (with its 6-minute clean-up), Chinese shadow puppetry and the shadow and cue technique, the two-ties card that
  teaches TH:Cn10.1.Ka and TH:Cn11.1.Ka, the guided puppet scene and a run. That is eight days, one of them a making
  day, in 40 minutes. A kindergarten class cannot make a paper-bag puppet and do any of the rest in one session.
- Unit 4 session 1 (55 to 58), unit 8 session 1 (119 to 122), unit 12 session 1 (183 to 186): two or three tales
  heard, the story map, the acting step card, and a first run of the whole scene, with three owned ids first taught.
- Unit 6 session 3 (87 to 92): six days, five owned ids first taught (Pr5.1.1a's second day, Cr3.1.1b, Re7.1.1a,
  Re8.1.1a, Re8.1.1c, Re9.1.1c).

**Why it matters.** The brief asks that the once-a-week path hold "with no assessed or owned part cut". Nothing is
cut on paper, but an id taught in six minutes inside a crowded session is cut in the room, and a writer building the
once-a-week teacher page from these lines would write impossible sessions. STANDARD.md 3.4 names "one making or
rehearsal day with a critique" as a kept thing; unit 3 keeps no making session at all.

**Fix (for the lead, since the frame's counts change).**
- Year K: 8, 8, 7, 5. Unit 1: 1 (1, 2), 2 (3, 4, 5), 3 (6, 7, 8), 4 (9, 10, 11), 5 (12 to 15), 6 showing, 7 table,
  8 respond. Unit 2: 1 (19, 20, 21), 2 (22, 23, 24), 3 (25, 26, 27), 4 (28, 29, 30), 5 (31, 32, 33), 6 showing,
  7 table, 8 respond. Unit 3: 1 (39, 40), 2 making (41), 3 (42, 43, 44), 4 (45 to 49), 5 showing, 6 table,
  7 respond. The year K once-a-week mid-year check then falls in week 17 (respond week 18), inside the kindergarten
  core weeks; CALENDAR.md rule 1 exempts arts specials, so it may stand, but the frame's "all off the core check
  weeks" line changes.
- Year 1: 7, 9, 7, 5 (unit 6 has 22 days against unit 5's 16). Unit 5: 1 (65, 66, 67), 2 (68, 69, 70),
  3 (71, 72, 73), 4 (74 to 77), 5 showing, 6 table, 7 respond. Unit 6: 1 (81, 82, 83), 2 (84, 85, 86),
  3 (87, 88, 89), 4 (90, 91, 92), 5 (93 to 96, fluency 93 and 95 in the opener), 6 (97, 98, 99), 7 showing, 8 table,
  9 respond. Check weeks unchanged (17 and 26).
- Story units (4, 8, 12): session 1 holds only the study and teaching days (55 to 57; 119 to 121; 183 to 185),
  session 2 the acting, critique and revision with the kept story map (58 to 60; 122 to 124; 186 to 188). If the lead
  judges that two teaching sessions still cannot carry a 10-day story unit, the frame should say plainly that the
  once-a-week story unit compresses its study, rather than claim it holds.
- Year 2 can keep 8, 8, 7, 5 if unit 10's session 2 (147 to 150) and session 3 (151 to 153) are split as
  1 (145, 146, 147), 2 (148, 149, 150), 3 (151, 152, 153); the current 1 (145, 146), 2 (147 to 150) puts four days
  in one.

Confidence: firm on unit 3 (the making day and clean-up minutes are the frame's own); likely on the others (minute
budgets from the frame, the rest from memory of K to 2 session pacing).

### 2. Day 184 holds more than 40 minutes (serious)

LAYER sequence. REPEAT new.

**What is wrong.** Day 184 carries the 10-minute retrieval opener (th-g1-story), the Cherokee story heard from the
nation's source, the kept candidate's 15-minute third race telling, and the compare that teaches TH:Cn11.2.2a. With
set-up 3 and close 4, that leaves about 8 minutes to hear the Cherokee story and compare three tellings.

**Why it matters.** The candidate was settled "15 minutes inside day 184, no day added", but the cost was counted
against an already full day; the unit's only teaching day for Cn11.2.2a, and the day with the most care owed to a
Native nation's story, would be rushed.

**Fix (settled below).** Hear the short third telling inside the retrieval opener: the retrieval task asks what the
character in that telling does and why (th-g1-story's content), so the telling serves both and the 15 minutes come
back to the Cherokee story and the three-way compare. Day 184's note and the .md candidate (b) say so.

Confidence: firm (minute budget is the frame's own).

### 3. The 10-days-short path folds the only teaching day of two owned ids (moderate)

LAYER sequence. REPEAT yes (the grades 3 to 5 fix pass set "no sole-code day is compressible").

**What is wrong.** Day 68 is the only teaching day of TH:Cr1.1.1a (also unit 5's response to a work); day 153 is the
only teaching day of TH:Re8.1.2a. Both are on the fold list (68 into 69, 153 into 152 as 15-minute segments). Day 152
would then teach three ids in one day.

**Why it matters.** Nothing is cut on paper, but an owned, assessed id loses its only day; the precedent in earlier
reads rules this out.

**Fix (settled below).** Replace 68 with 70 (the guided Turnip drama folds into 69 as a 15-minute segment that uses the
gestures just taught; saves 25) and 153 with 171 (the set planning folds into making day 172 as its first 15 minutes;
saves 25). Year totals are unchanged by these two swaps.

Confidence: firm.

### 4. Five baseline looks sit on days where the look-for is not performed (moderate)

LAYER sequence. REPEAT new.

**What is wrong.** The baseline look is named on a day whose activity cannot show the unit's main look-for:
- Unit 1, day 3 (freeze and melt drill): the look-for is "enters the place and acts in it"; the place walk is not
  taught until day 4 and not played until day 7 or 9.
- Unit 2, day 21 (voice warm-up run): the look-for is "the sound or voice at the cue"; there are no story cues until
  day 24 and 25.
- Unit 3, day 41 (making day): the look-for is "own made puppet used in a scene"; no scene is played until day 45.
- Unit 9, day 132 (three-ways line drill): the look-for is "a made-up line said in the scene"; lines are first made
  up on day 134.
- Unit 11, day 168 (object rounds): the look-for is "the effect worked at its cue"; cues are run on day 166.

**Why it matters.** The growth mark (APPROACH "Growth") is the change from baseline to check; a baseline the teacher
cannot observe becomes a guess, and every child's first mark in those units is empty.

**Fix (settled below).** Unit 1 day 9, unit 2 day 25, unit 3 day 45, unit 9 day 134, unit 11 day 166. Day 166 was a
fold-in day and baseline days never fold, so 168 replaces 166 on the year 2 fold list (168 folds into 167 as a
10-minute segment, saving 30, not 35). None of the other four new baseline days is on a fold list.

Confidence: firm (the look-fors are the frame's own).

### 5. Two course-level check days name no prompt for a part they claim (moderate)

LAYER sequence. REPEAT new.

**What is wrong.** Rule 2, "each part of each code": a check asks about each code it lists.
- Day 53 (year K year-end) claims TH:Cr2.1.Kb (share original ideas) as a live look-for, but its goal is "a fresh
  guided drama with voices and sounds"; nothing asks each child to add an idea of their own. In unit 1 this id was a
  talk item, so a teacher has no model for marking it live.
- Day 181 (year 2 year-end) claims TH:Cr3.1.2a (help change the dialogue) live, but the task is "one character in two
  moods"; no line is said, tried and changed. In unit 9 the id was a kept card with old and new lines.

**Fix (settled below).** Day 53 goal adds "each child adds one idea of their own to the scene". Day 181 goal adds "each
group says one line, tries it another way at the teacher's prompt and keeps the change". No minutes added: both fit
inside each group's 4 minutes.

Confidence: likely.

### 6. The kept plan cards are finished after the making they plan (moderate)

LAYER frame and sequence. REPEAT new.

**What is wrong.** TH:Cr1.1.1b (plan costumes and props) and TH:Cr1.1.2b (plan scenery) are scored from a kept
prop-sketch and set plan "finished on the last making day", which the scope puts on the revision days 113 and 177,
after the props were made (110) and the set built (172) and rehearsed. A plan drawn after the thing exists records it;
it does not show planning. The frame says "made on the last making day"; 113 and 177 are revision days, not making days.

**Fix (settled below).** The unit 7 prop-sketch is begun on day 106 and labeled with the teacher on making day 110;
the unit 11 set plan is drawn on day 171 and labeled on making day 172. Both are scored with the showing day. Day 113
and day 177 add only the child's spoken "what we changed" line. The .md's shorter-period sentence then names the making
days 110 and 172 to 173, not 113 and 177.

Confidence: likely.

### 7. Most movement days carry no safe-use line, though the .md says each day's note names it (minor)

LAYER sequence. REPEAT new.

**What is wrong.** The .md says "each day's note names its equipment, safe use of the floor and the free path". About
80 floor days have no safety line, among them every showing day (16, 34, 61, 78, 100, 114, 125, 142, 158, 178, 189)
and the unit 5 rehearsals of the heap freeze (74 to 78), whose control appears only on day 69.

**Fix (settled below).** The .md bullet says once that the unit's hazards line (frame, last Units column) applies on
every floor day and the note names only day-specific controls; the day-specific controls are added where a hazard is
rehearsed: the heap as a slow-motion freeze on 74 to 78, no falls on 95 to 100, no weapons or contact on 112 to 114,
the giant's slow walk and the freeze for "scared" on 155 to 158.

Confidence: firm (count from days.csv).

### 8. Unit 10 runs two critiques (minor)

LAYER sequence. REPEAT new.

Day 155 has "a partner describes, asks and suggests" and day 156 holds "the unit's critique". APPROACH "Critique": one
critique a unit, inside the second application day. **Fix (settled below):** day 155 becomes "rehearse the three moods
and adjust movements and sounds as you go, with the teacher's side-coaching"; the describe, ask, suggest routine stays
on 156, and the TH:Cr3.1.2b look-for (the change kept after the critique) reads from 156. Confidence: firm.

### 9. Day 1 is crowded for a first kindergarten session (minor)

LAYER sequence. REPEAT new.

Day 1 holds the set-up routine "taught slowly", the kamishibai hook, the agreements card, the freeze signal and
entering the imagined place with the teacher in role. The frame's safety rule is "freeze signal practiced before any
movement". **Fix (judgment call, not settled):** the unit plan may run day 1's entering seated (faces and hands only),
so the freeze signal is learned before anyone moves and the full place walk waits for day 4. Confidence: a judgment
call.

### 10. The shorter-period showing does not fit at 30 minutes (minor)

LAYER sequence. REPEAT new.

The .md says a showing fits a 30 to 35 minute period: set-up 2, six groups at 4 (24), self-check 3, close 3 = 32
minutes. **Fix (settled below):** "at 30 minutes, groups run about 3.5 minutes (21)"; the same holds for the
teacher's-table day of units 6 and 10. Confidence: firm.

### 11. Two units respond only to tales and Curio Class originals (minor)

LAYER frame. REPEAT new.

Units 5 and 9 study no theater maker or form beyond the kamishibai frame of a Curio Class story (unit 5) and two
literary tellings (unit 9). The frame counts these as "another artist's work", and the K to 2 responding standards are
about guided drama, so this meets the letter of bar item 5. An adoption reviewer reading for "theater works" could mark
these two units down. **Fix (for the lead, optional):** the unit 5 plan names kamishibai as a real form again (the
collection page from unit 1, a named revisit) on day 68, and the unit 9 plan adds one line on a living storyteller or
company that performs the Panchatantra for children, described and linked, inside day 129. Confidence: a judgment call.

### 12. Stale and process notes (minor)

LAYER process. REPEAT new.

- The .md lists the kindergarten core weeks as 14 to 17 and 29 to 32; the frame says 14 to 18. Moot for an arts
  special (CALENDAR.md rule 1), but the two should match: use the frame's 14 to 18.
- For the lead item 5 (grade 2 once-a-week respond session in week 18 beside the math mid-year check) is already
  answered by CALENDAR.md rule 1, which the .md itself cites: arts specials do not count against the stagger.
- data/plans/calendar.csv still holds the frame's even spread for this course (school days 3, 45 and so on), while
  days.csv gives 2, 44; `frame.py`'s days_calendar reads the new column correctly, so a `frame.py sync` by the lead
  brings the CSV in line. Weeks already agree.
- For the lead item 2 says frame.py's even spread is what puts the days in the same weeks; in fact frame.py reads
  the days.csv school_day column once it is filled (CALENDAR.md "that column wins"). The item can be shortened to
  "school_day filled as the second and fourth school days of each week, counted on across the band".

## What is right and should not be touched

- Every id on a day of its own year, every lettered part on a teaching day and an end-of-unit item, and the .md's
  statement of which grade's ids fall in which year (bar "Scope and sequence states").
- The unit shape: technique days, then rehearsal, the one critique, a revision, a showing day and a separate
  teacher's-table day, then the respond day. Talk items never share a day with live marking.
- Retrieval: every year 1 and 2 unit retrieves its one-grade-back row on day 2, day 1 stays clean, no readiness
  check anywhere (correct for this progression).
- The course-level checks: on the frame's weeks, each right after a unit's assessment and drawing from earlier units,
  with the 44 unsampled ids named and reasoned (rule 3, L107).
- The leans: all four checked against ELA's days (SL.K.6 from ELA K day 36, RL.K.3 day 49, RL.1.3 grade 1 day 10,
  SL.2.4 grade 2 day 104), with the SL.2.4 bridge on days 145 and 158.
- The sensitivity handling of the Cherokee story (heard and compared only, from the nation's own source, with the
  frame's swap), Nyame narrated by the teacher, the troll as the teacher's puppet.
- The school_day arithmetic (checked against frame.py's band offset) and the logic model on one page.

## What I could not judge

- Whether each named work's rights line holds (the unit plans and browser checks, For the lead item 4).
- The safety rules, which stay "from memory" until each unit's safety read.
- Real session timing with 30 kindergarten children; nothing here has been tried with children.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Baseline look moves: unit 1 day 3 to day 9, unit 2 day 21 to day 25, unit 3 day 41 to day 45, unit 9 day 132 to day 134, unit 11 day 168 to day 166 | The new day is the first where the main look-for is performed | days.csv notes; .md unit lines "Baseline look on day" |
| Year 2 fold list: 168 (into 167, a 10-minute segment, saves 30) replaces 166 | 166 is now a baseline day, which never folds | .md Shorter path table and totals (year 2: first four save 135, all ten 305) |
| Year 1 fold list: 70 (into 69, a 15-minute segment, saves 25) replaces 68 | 68 is the only teaching day of TH:Cr1.1.1a | .md Shorter path table |
| Year 2 fold list: 171 (into 172, its first 15 minutes, saves 25) replaces 153 | 153 is the only teaching day of TH:Re8.1.2a | .md Shorter path table |
| Day 184: the third race telling is heard inside the retrieval opener, which asks what its character does and why | Frees 15 minutes for the Cherokee story and the compare | days.csv day 184 note; .md unit 12 candidate (b) |
| Day 53 goal adds "each child adds one idea of their own to the scene" | A prompt for TH:Cr2.1.Kb | days.csv day 53 |
| Day 181 goal adds "each group says one line, tries it another way at the teacher's prompt and keeps the change" | A prompt for TH:Cr3.1.2a | days.csv day 181 |
| Unit 7 prop-sketch begun day 106, labeled day 110; unit 11 set plan drawn day 171, labeled day 172; days 113 and 177 add only the "what we changed" line | A plan is scored as a plan, made before the making | days.csv days 106, 110, 113, 171, 172, 177; .md units 7 and 11; .md Shorter period sentence (making days 110 and 172 to 173) |
| Day 155: teacher side-coaching, no partner describe, ask, suggest | One critique a unit, on day 156 | days.csv day 155 |
| Safe use: one .md sentence that the unit's hazard line holds on every floor day; day-specific controls on 74 to 78, 95 to 100, 112 to 114, 155 to 158 | The .md's claim and the days now agree | .md "Equipment and safe use"; days.csv those notes |
| Shorter period at 30 minutes: groups run about 3.5 minutes | 32 minutes does not fit 30 | .md Shorter path |
| For the lead item 5 closed: no change, CALENDAR.md rule 1 | Arts specials do not count against the stagger | .md For the lead |
| Kindergarten core weeks written 14 to 18 | Match the frame | .md Course-level checks |

Not settled (for the lead, frame layer): the once-a-week session counts and story-unit split (finding 1), and the
optional theater-maker revisits in units 5 and 9 (finding 11).

## For Cory

None. Nothing here changes scope, money, people or audience; the once-a-week rebalance is a frame fix for the lead.

## Sources

- data/standards/ncas-performance-standards-words.txt, lines 730 to 992: the 65 K to 2 theater ids in our own words,
  used for every id-by-id check.
- docs/courses/arts/APPROACH.md and STANDARD.md 3.4: day kinds, critique, growth, the 32-session path's kept parts.
- docs/ADOPTION-BAR-SUBJECTS.md section 2: the nine criteria and "Fails if".
- docs/reviews/sequence-3-5-fixes-2026-11-14.md: the sole-code-day fold precedent.
- From memory, not opened for this read: K to 2 attention and session pacing in drama (how much one 40-minute
  session can hold), the basis of the "likely" confidence in finding 1. No outside source was opened, so nothing
  goes to the source list.

## Defect log

The brief limits this run to its report, so the findings are not logged with `scripts/plan.py defect`; the caller
may log them, found_by `expert`.
