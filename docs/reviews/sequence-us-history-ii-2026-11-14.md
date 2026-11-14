# Sequence read: us-history-ii (US History II, the 1920s to today, full year), 2026-11-14

Expert cold read per docs/pipeline/briefs/sequence-read.md. Independent of any other read of this scope and sequence.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/social-studies.md; the social studies part and part 8 (personal
finance) of docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/social-studies/STANDARD.md; docs/courses/us-history-ii/frame.md
(with the grade 12 timetable and the shared research brief); docs/courses/us-history-ii/scope-and-sequence.md;
data/plans/us-history-ii/days.csv (all 160 rows); the us2-* rows and the ss8, wh2 and us1 rows they build on in
data/progressions/social-studies.csv; the MA.USII lines of data/standards/ma-hss-2018.txt; docs/courses/CALENDAR.md and
the grade 12 rows of data/plans/calendar.csv; the English Language Arts grade 12 frame's unit 8 row and leans
(docs/courses/english-language-arts-grade-12/frame.md); docs/pipeline/briefs/sequence-write.md (rule 2);
docs/GLOSSARY.md (readiness check, retrieval task); the earlier frame read docs/reviews/frame-us-history-ii-2026-11-13.md.

Gates: `plan.py check`: sequence us-history-ii 0 failures; frame us-history-ii 1 failure (finding 2). Every unit's first
and last day in days.csv matches data/plans/calendar.csv. CALENDAR rule 4: no rule for grades 9 to 12 outside the
finals week; check 3 sits in week 30 and unit 12's assessment in week 32. None broken.

## Verdict

A strong full year: twelve units in time order with a reason for every break, every MA.USII code and lettered option
on a named day and in its unit's end-of-unit assessment, an unseen task in every assessment, hard history with its
sensitivity reads named, and a capstone that serves both this course and English Language Arts grade 12. The biggest
risk is the last five weeks in a paired school: days 144 to 147 stack the unit 11 assessment, ELA's draft deadline, the
year-end check and ELA's rehearsal, and ELA's draft falls before this course's corroboration and counterclaim days. The
one change that matters most: in the shared brief, move ELA's draft to day 148 and have units 10 and 11 add the
counterclaim source, so one draft serves both courses.

## Findings, most serious first

### 1. The paired calendar crowds days 144 to 147 and splits the draft (moderate; judgment call). LAYER frame. REPEAT new

**What is wrong.** Where a school pairs this course with English Language Arts grade 12, the shared brief (frame,
"Shared research brief with ELA 12") sets ELA's full draft about day 145 and rehearsal by day 147. In this course, day
144 is unit 11's end-of-unit assessment, day 145 its respond day, day 146 the year-end course-level check and day 147
its respond day. Then unit 12 corroborates the sources and finds the strongest counterclaim on day 149 and drafts on
day 150. So a paired student sits four marked or due events in four days, and hands ELA a draft before the history
course has taught the step that changes the argument most.

**Why it matters.** Either the student writes the argument twice (ELA on 145, history on 150), or the history
corroboration never reaches the paper ELA marks. Seniors in late spring are the group most likely to drop the work.

**Fix.** (a) Frame, shared brief: "draft day 145" becomes "draft about day 148, after this course's year-end check".
(b) Days.csv rows 134 and 143 notes (the exit routines of units 10 and 11): add "where paired, add one source that
argues against your capstone claim to the shared set". (c) Days.csv rows 149 and 150 notes: "Paired: corroborate and
answer the counterclaim inside the ELA draft; no second draft." (d) The same change to "draft about day 145" in the
ELA 12 frame's unit 8 row and lean table, for the lead to carry when that course's scope and sequence is written;
rehearsal by day 147 and talks days 150 to 156 stay. Confidence: judgment call (the other order, ELA's draft first,
is defensible if a lead prefers it; the duplicated draft is not).

### 2. The frame fails the gate on a stale Topics note (moderate; firm). LAYER process. REPEAT yes (stale notes appear in most earlier reads)

**What is wrong.** `plan.py check` fails docs/courses/us-history-ii/frame.md:78: "Pending(ss:us-history-ii) has landed;
rewrite the note to say what is now true". The scope and sequence has since named the three new topic pages for units
1, 8 and 9 (For the lead 2).

**Why it matters.** The whole `plan.py check` exits 1 for every course until this line is fixed, which hides real
failures elsewhere.

**Fix.** Accept For the lead 2, and rewrite the frame's Topics bullet: drop "Pending(ss:us-history-ii):" and say "The
course's existing topics cover units 2 to 7, 10 and 11 (as listed) and the source skills; units 1, 8 and 9 use three
new topic pages named in the scope and sequence (The Economic Toolkit, Presidents and the War in Vietnam, Rights
Movements Since the 1960s), to be added to data/modules.csv for course us-hist-hs (later.csv L8)."

### 3. Day 32 holds two or three lessons (moderate; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 32 carries the New Deal's people from primary sources (six named), a survey of all eleven T2.4
case study options, bank runs and deposit insurance today, a retrieval task on progressive reform and Roosevelt's 1937
court plan in brief. The standard's own list of personalities also names Charles Lindbergh, who is missing.

**Why it matters.** Eleven options in one survey with six primary-source voices and a personal finance touch is not one
50-minute lesson; the survey will be a list, and the personal finance touch will be the first cut.

**Fix (days.csv rows 26, 32, 36).** Move bank runs to day 26 (the chain there already runs through spending, money
supply and banks: "the 1930 to 1933 bank runs" joins it). Move "how deposit insurance protects a saver today" to day 36,
where the FDIC is one of the lasting results judged. Day 32 keeps the people, the survey and the court plan; add
Lindbergh to its list ("and Charles Lindbergh, met again in unit 4's America First"). Settled by the expert.

### 4. Day 114 opens a unit and surveys three movements (minor; likely). LAYER sequence. REPEAT new

**What is wrong.** Day 114 holds a readiness check, two retrieval tasks (us1-reform-movements, wh2-decolonization), what
makes a movement succeed, and survey day 1 on women's rights, LGBTQ civil rights and disability rights. Day 119, the
comparison across movements, has no note and room.

**Fix (days.csv rows 114 and 119).** Move both retrieval tasks to day 119, where they serve the comparison (earlier
reform movements and decolonization's tactics set beside the 1960s and after). Day 114 keeps the readiness check and
the survey. Settled by the expert.

### 5. The look back on the action comes two days after it (minor; likely). LAYER sequence. REPEAT yes (same issue in the US Government read of this date)

**What is wrong.** Day 157 plans the action, day 158 takes it, day 160 looks back on "what changed". A letter or
comment sent through the school on day 158 cannot draw a response by day 160.

**Fix (days.csv rows 157, 158, 160; frame unit 12 row).** Day 157 plans and takes the action (the folding the scope and
sequence already uses for a short senior year); day 158 hands in the final argument. Day 160's look back records "the
response or its absence so far, and what the student would do next". Frame unit 12 row: add "no visible change is
needed for the action to count", the wording the Government frame uses. Settled by the expert for the days; the frame
line goes to the lead.

### 6. "Tracked over time" happens inside one day (minor; likely). LAYER sequence. REPEAT yes (Economics read of this date, finding 6)

**What is wrong.** MA.USII.T1.4 asks students to "track gains or losses of an investment over time". Day 5 tracks a
made-up asset "across dated observations" in one lesson; the note does not say how far apart the dates are.

**Fix (days.csv row 5 note).** Add: "Observations dated across several years, from a made-up series built on published
long-run asset-class returns, so the rise and fall shows why values change over time." Settled by the expert, the same
call as Economics.

### 7. Day 1 calls its readiness check a retrieval task (minor; firm). LAYER sequence. REPEAT yes (loose terms appear in most earlier reads)

**What is wrong.** Day 1's note reads "Readiness check (the opening retrieval task) on ss8-public-budget". GLOSSARY keeps
the two apart: a readiness check is on an earlier grade's row before a unit; a retrieval task is a short, unmarked look
back.

**Fix (days.csv row 1 note).** "Readiness check (the opening retrieval task) on" becomes "Readiness check on".

## The readiness versus retrieval call, and the held look-back days

Readiness checks are right where the scope and sequence puts them: units 1, 7 and 9 each assume a grade 8 row
(ss8-public-budget, ss8-civil-rights-laws, ss8-protest-change) idle three grades for a grade 12 student, so rule 2
applies. Every look back on a grade 10 or grade 11 row (wh2-great-depression, us1-progressivism, us1-jim-crow,
us1-reconstruction, us1-research-inquiry and the rest) is rightly a retrieval task. A student who took Economics in the
fall meets day 1's check as retrieval at a higher level, as the note says; that is fine.

No held look-back day shifts a unit. Day 123 (unit 9's respond day and the capstone question) and day 160 (unit 12's
respond day and the look back) sit inside their units' days in calendar.csv, which matches days.csv for all twelve units
and the three checks. Nothing to sync.

## Checked and found right (do not undo)

- Standards in full: every MA.USII code from T1.1 to T5.7, with all lettered options (all eleven of T2.4, all of T4.5
  and T4.7), is on a teaching day and in its unit's end-of-unit assessment; owned C3 indicators (D2.Civ.12, D2.Geo.8 and
  9, D4.3 to D4.5 and the rest the frame names) are on days. Indicators the frame lists as practised, or as owned by
  Economics (D2.Eco.1, D2.Eco.12), need no day here.
- Time order kept; unit 1's toolkit before the 1920s, with the reason given; the capstone last.
- Every end-of-unit assessment opens with an unseen source; unit 12 adds an unseen historical explanation beside the
  capstone. Accept For the lead 1 and its frame line.
- For the lead 3 (day 123 holds both the respond day and the capstone question): right, no change.
- Hard history: the Holocaust, Japanese American incarceration, the bomb, civil rights violence and Coughlin's
  antisemitism each name their sensitivity read and source study; Roe and Dobbs stated as decided; both political
  traditions in unit 10 get their own words.
- English Language Arts grade 12 leans: its unit 4 (Gatsby) follows this course's unit 2 and its antisemitic passages
  follow unit 4's Holocaust days, as the ELA frame needs.
- Informed action once a year (unit 12), the student's choice, with a reasoned choice not to act allowed.
- No timers shown; 50-minute days; paper path on every digital task.

## Lens checklist, scope and sequence layer

| Line | Met? |
|---|---|
| Unit question answerable without the unit's sources, or one defensible answer | Met: all twelve are open |
| History out of time order with no reason | Met: unit 1's toolkit is out of order with its reason stated |
| A contested event with one telling | Met: two accounts of the Depression (day 27), the bomb's reasons beside survivors' accounts (days 61, 62), both traditions in their own terms (day 129), the Cold War's end from inside and outside (day 132) |
| Writing from sources once a year or never builds short to long | Met: unit arguments each term, the year-end essay, then the capstone |

## Candidate cells

| Cell | Settled in the draft | My read |
|---|---|---|
| Indian Reorganization Act (unit 3) | Kept, 1 day, day 35 | Right |
| Roosevelt's 1937 court plan (unit 3) | Kept in brief inside day 32 | Right (Government teaches it in full) |
| Other candidate cells (units 4 to 11) | As the scope and sequence lists them | Right; none overloads a day except day 32 and day 114 (findings 3, 4) |
| Unit 12 | None in the frame | Right |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Bank runs to day 26; deposit insurance today to day 36; Lindbergh added to day 32's list | Day 32 held two or three lessons; the standard names Lindbergh | data/plans/us-history-ii/days.csv rows 26, 32, 36 |
| Day 114's two retrieval tasks moved to day 119 | Day 114 held a unit opening and a survey; day 119 compares movements | days.csv rows 114, 119 |
| Action planned and taken on day 157; argument handed in on day 158 | Gives the look back three days, not two | days.csv rows 157, 158, 160 |
| Day 5 observations dated across several years from a made-up series on published long-run returns | "Over time" in T1.4 | days.csv row 5 |
| Day 1 note wording | Readiness and retrieval kept apart (GLOSSARY) | days.csv row 1 |
| Counterclaim source added in units 10 and 11 where paired; no second draft on day 150 | One draft serves both courses | days.csv rows 134, 143, 149, 150 |

## For Cory

None. (Finding 1 moves an ELA milestone inside the shared brief Cory's timetable already set; no scope, money, people or
audience change.)

## Sources

- data/standards/ma-hss-2018.txt (Massachusetts 2018, ids and our words): every code checked against the days,
  including the T2.4 personalities list.
- C3 Framework (NCSS 2013, rev. 2017): indicator ids from the frame and the progression rows.
- `scripts/plan.py check` output of 2026-11-14 for the frame failure.

Confidence: findings 2 and 7 firm; 3 to 6 likely; 1 a judgment call.
