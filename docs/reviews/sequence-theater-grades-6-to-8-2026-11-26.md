# Expert read: scope and sequence of Theater, grades 6 to 8 (2026-11-26)

Course `theater-grades-6-to-8`. Cold read by the curriculum expert (PRODUCTION-PATH step 3), as
docs/pipeline/briefs/sequence-read.md and build/scope-writes/ARTS-READ.md ask. The scope was written by a fresh agent;
this reader did not write it.

## What I read

- The scope and sequence (docs/courses/theater-grades-6-to-8/scope-and-sequence.md) and all 192 rows of
  data/plans/theater-grades-6-to-8/days.csv, read cold.
- Beside them: the frame (docs/courses/theater-grades-6-to-8/frame.md, whole), the th-g6, th-g7 and th-g8 rows of
  data/progressions/arts.csv, the 72 grade 6 to 8 theater lines of data/standards/ncas-performance-standards-words.txt,
  docs/courses/CALENDAR.md (rules 1 to 4 and the grade 6 to 8 table) and the course's rows of data/plans/calendar.csv,
  and the ELA grade 6, 7 and 8 days.csv files for the five leans (SL.6.4, W.6.1, RL.7.3, SL.8.4, W.8.1).
- The bar: docs/ADOPTION-BAR-SUBJECTS.md section 2 (items 1 to 9 and "Fails if"), docs/courses/arts/STANDARD.md (3.4),
  the lens docs/agents/lenses/arts.md, docs/agents/EXPERT.md, the writer's brief build/scope-writes/ARTS-BRIEF.md and
  docs/pipeline/briefs/sequence-write.md (rules 2 and 10).
- Earlier reads of the same layer: docs/reviews/sequence-theater-grades-k-to-2-2026-11-26.md and
  docs/reviews/sequence-music-grades-6-to-8-2026-11-26.md, for the REPEAT tags.
- Gates, run first: `plan.py check` reports `sequence theater-grades-6-to-8: 0 failure(s)` (failures elsewhere are other
  courses'); `sequence.py check theater-grades-6-to-8` 0 failures; `frame.py calendar` no failure; `stale.py check`
  121 files, 0 failures. My own script confirmed: every code sits in its own grade's year; every owned id of every unit
  is on the unit's end-of-unit days and on at least one teaching day before them; no unit carries a code it does not
  own. Every grade 6 to 8 row assumes only the row one grade back in its thread, so retrieval (never readiness) is
  right throughout, and day 2 of each unit carries it in `retrieves`. The course's check days (school days 83, 85,
  158, 160 of each year) share school days only with the other arts electives, which CALENDAR.md rule 3 counts as one.
  The ELA leans hold: W.6.1, RL.7.3 and W.8.1 are taught in ELA unit 1 before the theater day that uses them; SL.6.4
  (ELA day 80) and SL.8.4 (ELA day 148) come later, and the theater days carry their bridge lines.

## Verdict

The scope is sound where it matters most: all 72 ids sit on days of the right year, each year carries all four
processes through owned ids, every unit teaches technique in steps before the making, runs one critique and a revision
before a two-day end-of-unit assessment that covers every owned id, and the works range across five continents with
living makers each year. The biggest risk is the once-a-week path: every unit's first session holds both the hook and
the ten-minute retrieval, and the 14-day units put four to six teaching days into one 40-minute session (unit 11's
first session holds six), so the path keeps every id on paper but not in the room. The change that matters most is
moving each retrieval off the hook session and rebalancing the once-a-week sessions (finding 1); after that, give the
responding and connecting ids now taught on a single day a second short touch (finding 5).

Finding count: 10 (1 serious, 4 moderate, 5 minor).

## Findings, most serious first

### 1. The once-a-week path does not hold in the room (serious)

LAYER frame and sequence. REPEAT yes (theater K to 2 read, finding 1).

**What is wrong.** The frame fixes the sessions at 9, 7, 6 and 6 a year, with three check sessions in every unit, so
a 14-day unit of the 6-session kind has three sessions for eleven teaching days. The scope then writes:
- Every unit's S1 merges its day 1 and day 2 (1 and 2, 19 and 20, 35 and 36 ... 163 and 164), so the retrieval task
  with its ten-minute reteach lands on the hook session, which the frame keeps clean for the hook and the compelling
  question ("day 1 stays clean").
- Unit 11 S1 = days 163, 164, 165, 166, 168, 171: the Globe and Arena Stage, the walk of the real space and its venue
  plan, combining elements on the cue sheet, the simple-technology step card, Ilbijerri, and the paired judgment
  paragraph, plus the retrieval. Unit 3 S1 (35, 36, 37, 39, 42), unit 7 S1 (99, 100, 101, 102, 106) and unit 12 S1
  (177 to 180, 182) hold five days each. After set-up 3, warm-up 5, close 4 and the retrieval 10, about 18 minutes
  remain for all of it.
- Unit 3 S2 (38, 40, 41, 43) and unit 7 S2 (103, 104, 105, 107) hold a cue drill, a card-and-tape making day with its
  6-minute clean-up, the first tech rehearsal and the critique in one session.
- Meanwhile unit 1 S5 holds day 12 alone, unit 5 S5 day 76, unit 9 S5 day 140, and unit 11 S3 day 173 alone.

**Why it matters.** ARTS-READ asks that the once-a-week path hold "with no assessed or owned part cut". Nothing is cut
on paper, but a technique step card shown in five minutes inside a six-day session is cut in the room, and a writer
building the once-a-week teacher page from these lines would write sessions that cannot run (bar item 2, technique
taught in steps; item 9, pacing that fits real schedules).

**Fix.**
- In every unit, the retrieval task opens S2 (units with two study sessions) or the first rehearsal session (units
  with one), never S1. State this once in the once-a-week paragraph.
- Even out the sessions inside each unit (settled below): unit 1 day 13 to S5; unit 2 day 25 to S2; unit 3 day 39 to
  S3 (the criteria come before any written judgment, which is still true); unit 5 day 77 to S5; unit 7 day 102 to S3;
  unit 9 day 141 to S5; unit 11 day 168 to S3; unit 12 day 182 to S3.
- For the lead (frame layer): even after the moves, the design units (3, 7, 11) put a making day, a tech rehearsal and
  a critique into one or two sessions. Either change the year's split to 8, 7, 7, 6 (unit 1 gives up its lone
  revision session; the design unit gets a session for the making alone), or have the frame say plainly that on the
  once-a-week path the study days are taught in short form, about ten minutes each, so no reader takes the path for
  the full course.

Confidence: firm on the merged hook and retrieval (the frame's own rule) and on the minute budget (the frame's own
figures); likely on what a grade 6 to 8 class can do in a session (from memory of middle school drama pacing).

### 2. The retrieval and reteach minutes on each unit's day 2 do not add up (moderate)

LAYER sequence. REPEAT yes (music grades 6 to 8 read, finding 3).

**What is wrong.** Day 2's note gives the retrieval task 10 minutes and then "each with its ten-minute reteach" for two
rows, which reads as up to 30 minutes, on a day that also teaches the warm-up routine in steps (28 working minutes in
all). The same wording sits on days 66 and 130 and every other day 2 of a unit. Day 164 adds the walk of the real
space, which may be a hall or a yard down the corridor, to the same ten-minute opener.

**Why it matters.** A teacher cannot tell whether the reteach is in or on top of the 10 minutes, and the day's own
teaching is the part that gets dropped.

**Fix.** One line in the .md and in each day-2 note: the retrieval's 10 minutes cover both rows, and the reteach runs
inside those same 10 minutes for the students new to theater, from a printed reteach card, while the others do the
retrieval task. Day 2's budget then reads set-up 3, retrieval 10, the warm-up routine taught in steps 15 (it replaces
the 5-minute warm-up that day), practice 8, close 4. On day 164, if the performance space is outside the room, the
retrieval moves to day 165's opener.

Confidence: firm (the frame's own minutes).

### 3. Group-made sheets are scored as each student's evidence (moderate)

LAYER sequence. REPEAT new.

**What is wrong.** The frame says every student is marked on their own. But day 40 has "each group draws two design
fixes, chooses one with a written reason", and that sketch is the kept evidence for TH:Cr1.1.6b; day 104's two-minute
presentation of the fix is a group's, and it is the only evidence for TH:Cr1.1.7b ("explain and present fixes"), with
five students sharing two minutes; day 164's venue plan (TH:Cr1.1.8b) and the cue sheets of days 37, 101 and 165
(TH:Pr5.1.6b, 7b, 8b) do not say whose they are.

**Why it matters.** A student who said and drew nothing would be marked met on a group's sheet; the record would not
show which student met the id, which the band-year rule and the student-by-id roster exist to show.

**Fix (settled below).** Each student keeps their own copy: on day 40 each student draws two fixes with a reason on
their own sketch sheet before the group picks one to build; on day 104 each student writes one explain line on their
own sketch and speaks one part of the presentation (a fix or its reason); day 164's venue plan and each cue sheet are
filled per student, with the group's chosen version copied.

Confidence: likely (one rule, the frame's own, read against the days).

### 4. Some check and item prompts miss a part of the code they list (moderate)

LAYER sequence and frame. REPEAT yes (theater K to 2 read, finding 5; music grades 6 to 8 read, finding 1).

**What is wrong.**
- Day 63 lists TH:Pr5.1.6b ("explain how tech elements are woven into a drama work") but marks only a cue "woven in"
  live; nothing asks a student to explain.
- Day 97 lists TH:Cr3.1.7b (body and voice traits) but marks "traits fitting the goal", with no body and voice named.
- Day 161 lists TH:Cr3.1.8b (body, voice and bodily-response traits) but marks only "a bodily response held".
- Day 61's item for TH:Cn10.1.6a asks for a character's action and the view of the community it gives; the code is
  what characters do and want.
- The defense note for TH:Cr2.1.7a (days 89, 91, 94) is framed "claim, analysis, background"; the code asks for
  analysis, background and context.

**Why it matters.** The brief asks that every check task ask about each part of each code it lists; a check that names
a code and marks half of it reports a met mark the student has not shown.

**Fix (settled below).** Day 63: each student writes one line on the card, while the group plans, on how their cue is
woven in (what, when, why). Day 97: "body and voice traits that fit the goal". Day 161: "a physical, a vocal and a
bodily-response choice, each held". Day 61: "one character's action and want, and the view of the community they
give". Defense note frame: "claim, analysis, background, context (the Gupta court)". The frame's check table carries
the same three wordings; the lead may align it.

Confidence: firm (the words file against the days).

### 5. Twenty responding and connecting ids rest on one teaching day (moderate)

LAYER sequence. REPEAT yes (music grades 6 to 8 read, finding 2).

**What is wrong.** These codes appear on one day before the written check: TH:Re8.1.6a (day 8), TH:Re8.1.6c (13),
TH:Cn11.2.6a (21), TH:Re9.1.6a (39), TH:Re9.1.6c (42), TH:Cn10.1.6a (49), TH:Re8.1.6b (54), TH:Re8.1.7a (73),
TH:Re8.1.7c (77), TH:Cn11.2.7a (85), TH:Cn11.2.7b (86), TH:Re9.1.7c (102), TH:Re9.1.7a (106), TH:Re8.1.7b (118),
TH:Re8.1.8c (141), TH:Cn11.2.8a (151), TH:Re9.1.8b (163, the hook only), TH:Re9.1.8c (168), TH:Re9.1.8a (171),
TH:Re8.1.8b (182). Several share their one day with two other codes (13, 42, 102, 141), and TH:Re9.1.8b is met only on a
hook day.

**Why it matters.** The written check is then the student's first try alone after one exposure. The acting ids get a
drill, a rehearsal, a critique and a revision; the written ids get none, though bar item 5 asks that students be
taught to read and judge other artists' work, not only shown it once.

**Fix (settled below).** Give each a second short touch on a later day of its unit, in the close or as the critique's
question, coded on that day: Re8.1.6a on day 10's close; Re8.1.6c on day 15's close; Cn11.2.6a on day 29's close;
Re9.1.6c as day 43's critique question (the .md already says the critique asks who the design is for); Re9.1.6a on
day 45's close; Cn10.1.6a as day 55's critique question; Re8.1.6b on day 59's close; Re8.1.7a on day 74's close;
Re8.1.7c on day 79's close; Cn11.2.7a and Cn11.2.7b on day 89 (the defense note frame already uses both cards);
Re9.1.7c as day 107's critique question; Re9.1.7a on day 109's close; Re8.1.7b on day 122's close; Re8.1.8c on day
143's close; Cn11.2.8a on day 153 (the research cards); Re9.1.8b and Re9.1.8c as day 172's critique questions; Re8.1.8b
on day 186's close. TH:Re9.1.8a sits on a full day of its own (171); its second touch is optional. Each is one written line (5 minutes, taken from the second run or self-check). Where the day folds
on the 10-days-short path, the line goes with the folded work into the neighbor's close.

Confidence: likely (teaching practice, from memory; the bar's item 5).

### 6. Three days use an earlier unit's work with no retrieval (minor)

LAYER sequence. REPEAT new.

**What is wrong.** Rule 2 asks that a row used the year before, or earlier the same year, open as a retrieval task. Day
137 judges a decision by the criteria card "as review from unit 7" (th-g7-judge, last used the year before) with no
`retrieves` cell. Day 171 pairs evidence and criteria with taste (th-g8-notice, unit 9 of the same year). Day 186's
polish drill uses unit 11's venue plan and cue sheets (th-g8-design).

**Why it matters.** Small: the routines are familiar, but a student who missed unit 7 or unit 9 has no reteach, and
the gate cannot see a use that is not in `retrieves`.

**Fix (settled below).** Add a short retrieval in the opener: day 137 `retrieves` th-g7-judge (unit 7, days 99 to
112); day 171 th-g8-notice (unit 9, days 129 to 146); day 186 th-g8-design (unit 11, days 163 to 176). Each takes the
opener's 5 minutes, not 10, since each is a model in use, not a skill being rebuilt.

Confidence: firm (the rule's text).

### 7. The 10-days-short fold minutes are off in seven rows (minor)

LAYER sequence. REPEAT new.

**What is wrong.** Four folds (10 into 11, 74 into 75, 122 into 123, 138 into 139) put an 8-minute drill in place of
"the full warm-up", which the frame gives 5 minutes, so each neighbor day runs 3 minutes over. Three folds (45 into 44,
109 into 108, 157 into 156) put "the final observation round" into 12 minutes, which cannot cover 30 students; unit
10's TH:Pr4.1.8a is an acting id that needs every student's observed turn.

**Why it matters.** A teacher on the short year gets days that do not fit, and in unit 10 may miss acting marks.

**Fix (settled below).** The four drill folds read "5: the drill is that day's warm-up". The three observation folds
read "12: groups run in parallel; the observation round covers only students still without an observed turn, and any
mark still missing is taken live in an observation round before the respond day" (the frame's own rule). Totals stay
480 minutes saved.

Confidence: firm (the frame's minutes).

### 8. The .md says every day names its floor rule; most floor days do not (minor)

LAYER sequence. REPEAT yes (theater K to 2 read, finding 7).

**What is wrong.** "Every day's note names its floor rule" (Equipment, space and the free path). Fifteen notes carry
the floor line; about 74 Fluency, Application and showing days carry no safe-use line at all (for example 5, 15, 23,
55 to 60, 78 to 80, 119 to 124, 139 to 144, 183 to 188).

**Why it matters.** Bar item 9 asks lessons to list safe use of space; the .md's claim and the days disagree.

**Fix (settled below).** One .md sentence: the unit's floor line, set on its first floor day, holds on every floor day
and is printed on every section plan; then the floor line is added to each unit's first Application day where it is
missing (53, 72, 105, 116, 136, 152, 170, 181), and day-specific controls stay where they are.

Confidence: firm.

### 9. "Responding touched" in units 2, 6 and 10 is not a student act (minor)

LAYER sequence. REPEAT yes (music grades 6 to 8 read, finding 7, the same kind for connecting).

**What is wrong.** The process table says responding is touched on days 21 and 26 (unit 2), 90 (unit 6), 151 and 155
(unit 10). Days 21 and 151 compare versions or productions, which is connecting work; only the critique has students
respond, and that is to classmates' work.

**Why it matters.** Small: each year meets bar item 1 through owned ids. But ARTS-READ asks for all four processes in
every unit, and a critique alone leaves the unit's response to other artists' work as a fact on a card.

**Fix (settled below).** Days 21 and 151 each add a one-line audience-journal reaction to one choice in the other
artist's version, in the unit's words; unit 6's touch is day 90's critique plus a one-line reaction on day 85 to how
the first audience may have met the stage manager's opening.

Confidence: a judgment call.

### 10. Stale and process notes (minor)

LAYER process. REPEAT yes (theater K to 2 read, finding 12).

**What is wrong.** For the lead item 3 says the day 83 clashes are "the lead's calendar pass" and that the calendar
result "is in the job's last message". The lead's calendar pass was done 2026-11-26 (CALENDAR.md rule 3 now counts the
arts electives as one) and `frame.py calendar` passes; the .md's Course-level checks paragraph already says so.

**Fix (settled below).** Replace item 3 with: "Calendar: frame.py calendar passes; the check days share school days
only with the other arts electives, which CALENDAR.md rule 3 counts as one. Closed." Drop the job-message line.

## The lens checklist (scope and sequence layer)

| Line | Result |
|---|---|
| A grade's ids in the wrong year of the band | Met: all 72 in their own year (script check) |
| A year with one artistic process missing | Met: each year owns Cr, Pr, Re and Cn ids |
| Works all from one tradition or one century | Met: five continents each year, 1300s to living makers |
| Technique that does not get harder | Met: body choices, then goals, then tactics; one fix, then viewpoints, then research; one design fix, then several elements, then the real venue |
| A plan that needs a daily period | Met: two 40-minute sessions a week; the once-a-week path is the risk (finding 1) |
| No showing in a unit | Met: twelve showings, four for another class or families |

Bar items 1 to 9: 1 met; 2 met on the twice-weekly path, at risk on the once-a-week path (finding 1); 3 met (six
words a unit, taught on the day needed); 4 met (devised units, choice of fix, role and element); 5 met, thin on the
written ids (finding 5); 6 met (one critique and a revision in every unit); 7 met (every work with maker, place, date
and purpose); 8 met (two marks a unit, self-check, portfolio piece a unit); 9 met with findings 1, 7 and 8. "Fails
if": none.

## What is right and should not be touched

- The band-year rule, stated once, with each year's 24 ids and the mixed-class line.
- The retrieval table (rule 2), with each row's last use and the reteach for students new to theater.
- The course checks: each one right after a unit's end-of-unit assessment samples earlier units, and says so; the 54
  unsampled ids are named with the reason.
- The two-day end-of-unit assessment (showing day, written day), the final observation rounds with roles rotated, and
  the baseline look on the first practice day of each unit, never on a folded day.
- The ELA bridges on days 2, 39, 83, 130 and 171, and the candidate cells, each settled with its day cost.
- Sensitivity flags in the notes of every flagged work (Yuyachkani, Taki Rua, Sanskrit drama, kabuki, Spiderwoman
  Theater, Kamiriithu, the Yuan painting, Ilbijerri, Woza Albert!, Native Voices).

## What I could not judge

- The running time of the Safety Last! store scenes on day 1, and the length of each adapted scene; the unit plans set
  them.
- Whether each work's page carries its rights line; no work page was opened (For the lead item 5, rightly left to the
  unit plans).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Once-a-week: retrieval opens S2 (or the first rehearsal session), never S1; one sentence in the once-a-week paragraph | The hook session stays clean | .md Shorter path |
| Once-a-week moves: day 13 to unit 1 S5; 25 to unit 2 S2; 39 to unit 3 S3; 77 to unit 5 S5; 102 to unit 7 S3; 141 to unit 9 S5; 168 to unit 11 S3; 182 to unit 12 S3 | Evens out sessions inside each unit; order kept | .md once-a-week table |
| Day-2 retrieval: 10 minutes for both rows, the reteach inside them from a printed card; day 2 budget written out; day 164's retrieval to day 165 if the space is outside the room | The minutes add up | .md Readiness and retrieval; days.csv notes of each unit's day 2, days 164 and 165 |
| Days 40, 104, 164 and the cue-sheet days 37, 101, 165: each student keeps their own sketch, venue plan or cue sheet; on day 104 each student writes an explain line and speaks one part | Individual evidence for design ids | days.csv goals and notes of those days |
| Day 63 adds a one-line "how my cue is woven in" per student; day 97 "body and voice traits"; day 161 "a physical, a vocal and a bodily-response choice"; day 61 "action and want"; defense note "claim, analysis, background, context" | A prompt for every part of each listed code | days.csv days 61, 63, 89, 91, 97, 161; .md units 5 and 6 assessment lines if worded there |
| Second touches for the single-day ids, as listed in finding 5 | Practice before the written check | days.csv codes and notes of days 10, 15, 29, 43, 45, 55, 59, 74, 79, 89, 107, 109, 122, 143, 153, 172, 186; .md Shorter path rows for folded days |
| `retrieves` added: day 137 th-g7-judge, day 171 th-g8-notice, day 186 th-g8-design, 5 minutes each | Rule 2 for models used from earlier units | days.csv days 137, 171, 186; .md retrieval table note |
| Fold minutes: four drill folds read "5: the drill is that day's warm-up"; three observation folds read as in finding 7 | The neighbor days fit 40 minutes | .md Shorter path table |
| Safe use: one .md sentence; floor line added on days 53, 72, 105, 116, 136, 152, 170, 181 | The .md's claim and the days agree | .md Equipment; days.csv those notes |
| Days 21 and 151 add a one-line audience-journal reaction; day 85 a one-line reaction to the stage manager's opening | Responding as a student act in units 2, 6, 10 | days.csv days 21, 85, 151; .md process table |
| For the lead item 3 closed and the job-message line dropped | Stale | .md For the lead |

Not settled (for the lead, frame layer): the once-a-week split (8, 7, 7, 6, or a plain "short form" line), and the
frame's check-table wordings in finding 4. On the scope's For the lead item 2, my view: 10 school days, four sessions,
is the right reading for a twice-weekly course; one line in ARTS-BRIEF.md or STANDARD.md 3.4 would settle it for all
five disciplines.

## For Cory

None. Nothing here changes scope, money, people or audience; the once-a-week split is a frame fix for the lead.

## Sources

- data/standards/ncas-performance-standards-words.txt: the 72 grade 6 to 8 theater ids in our own words, used for
  every part-by-part check.
- docs/ADOPTION-BAR-SUBJECTS.md section 2 and docs/courses/arts/STANDARD.md 3.4: the nine criteria, "Fails if", and
  the once-a-week rule.
- docs/courses/CALENDAR.md rule 3 and data/plans/calendar.csv: the check days.
- From memory, not opened for this read: middle school drama session pacing (what one 40-minute session holds), the
  basis of the "likely" confidence in findings 1 and 5. No outside source was opened, so nothing goes to the source
  list.

## Defect log

The brief limits this run to its report, so the findings are not logged with `scripts/plan.py defect`; the caller
may log them, found_by `expert`.
