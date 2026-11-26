# Expert read: scope and sequence, Library and Research Skills, grade 5 (2026-11-26)

Course `library-and-research-skills-grade-5`. Read cold as a grade 5 teacher and school librarian, a district
adoption reader and a researcher, per docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md.
A fresh Claude agent wrote the scope. This read changes no file except this report.

## What I read

- docs/courses/library-and-research-skills-grade-5/scope-and-sequence.md and
  data/plans/library-and-research-skills-grade-5/days.csv (all 30 rows), in full.
- The frame docs/courses/library-and-research-skills-grade-5/frame.md, in full.
- data/progressions/library.csv: every grade 5 row, every grade 4 row's ids and assumes, g3-safe-searching and
  g3-research-questions. data/standards/aasl-words.txt for the 18 ids the course names.
- The grade 3 and grade 4 library days.csv files, to see where g3-safe-searching, g3-make-product,
  g3-research-questions and g2-credit-line were last used.
- docs/agents/EXPERT.md, docs/agents/lenses/library.md, build/scope-writes/AFTERCORE-BRIEF.md,
  docs/pipeline/briefs/sequence-write.md, docs/GLOSSARY.md (teaching, assessment and respond day; readiness check;
  end-of-unit assessment), DESK-ANSWERS "10 days short" entry.
- docs/courses/CALENDAR.md (rule 1, the grade 5 table row) and the grade 5 rows of data/plans/calendar.csv (ELA,
  science, social studies, health, library).
- The health grades 3 to 5 frame's unit 11 and 16 rows and days 65 and 66 of its days.csv (the health source check).
- For the REPEAT tag: docs/reviews/sequence-library-and-research-skills-grade-1-2026-11-26.md and the kindergarten read.
- Outside: the NetSmartz resources listing (https://www.missingkids.org/netsmartz/resources), opened 2026-11-26.

Gates run first. `scripts/plan.py check`: library grade 5 passes. `scripts/sequence.py check
library-and-research-skills-grade-5`: 0 failures, and one note, "unit 3: standard None is on no day". The frame's
unit 3 owns no id, so the note is an artifact of the literal "None". `scripts/frame.py calendar`: library grade 5
checks fall in weeks 13 and 28, which matches CALENDAR.md. Library is a special, so week 28 next to health's check
is no break. `scripts/stale.py check`: nothing for this course. The gates settle day numbers, totals, unit day
counts, kinds, an assessment per unit, respond days and owned-skill placement, so this read does not re-check them.

## Verdict

The scope is sound. It is four full inquiry cycles in the frame's order, taught on paper with invented pages. Lateral
reading is taught properly by leaving the page and checking a statement against a second source, not by a
checklist. Every assumed grade 4 row comes back as retrieval. Both course-level checks sit on CALENDAR.md's weeks,
and the hosts were honestly checked against calendar.csv. The biggest risk is the Shorter path. Fold-in 1 removes
unit 1's only practice day: the site-menu case is first practiced there before day 5 assesses it, and the day's work
is pushed into three days that are already full. The 30-minute session also does not hold day 11's 27-minute
sitting. The second most important change is to the check rows: they claim carried codes they do not ask about, or
ask only half of. A unit plan writer would copy them into items.

## Findings, most serious first

### 1. The Shorter path's first fold-in removes unit 1's only practice day and overfills three days (serious; LAYER sequence; REPEAT yes)

**What is wrong.**
- (a) Fold-in 1 folds day 3 into its neighbors. Day 3 is the only day on which students practice the sort, the
  query fixes and the site-menu case before day 5's end-of-unit assessment asks for all three. The moves also land
  on full days:
  - "One round of the question sort" goes into day 1's last 8 minutes. Day 1 already holds the hook, the cycle card,
    the think-aloud sort and rewrite, and a 5-minute exit ticket.
  - "Two of the three search fixes" go into day 4's opening 10 minutes. Day 4 is budgeted at 15 + 8 + 6 = 29 of its
    29 working minutes.
  - Day 3's two retrievals join day 2's opening. Day 2 already spends its 29 minutes on a retrieval, six modeled
    moves and an exit ticket (see finding 6).
  - About 26 minutes are pushed into days with no room, and the receiving days shed nothing.
- (b) The 30-minute session leaves about 26 working minutes. The path says "every sitting (20 to 27 minutes) still
  fits", but day 11 is 27 minutes. Day 28 fits only because it drops its 2 minutes of rereading.

**Why it matters.** Bar C2 and rule 10 ask for a reduced path that holds with nothing assessed cut. A class that
loses two library weeks would sit an assessment on a move it never practiced alone. This is the same kind of fault
as grade 1 finding 1.

**Fix (settled below).**
- Keep fold-in 2 (day 12 into day 14). Day 14 already works from unit 2's class count.
- Replace fold-in 1 with day 30 folded into day 29. Day 29 becomes: unit 4 regrouped reteach 10 minutes, the
  year-end check's gaps 10 minutes, and the year's look-back 9 minutes (the search logs reread and a written
  next-step line, plus the question carried to grade 6). The 5-minute fresh try is dropped, because the look-back
  line is itself a new written try at g5-search-log-look-back.
- Day 30 holds no assessment and no owned part that is not also on day 29. About 29 minutes are saved, so the total
  is still about 58 minutes and 28 days, and day 3 stays.
- On the 30-minute session, day 11 runs its reason lines in 11 minutes (three lines, about 3.5 minutes each) and its
  lateral part in 15, for 26.

**Confidence.** Firm (the scope's own minute budgets).

### 2. Check and end days claim carried codes they do not ask about, or ask only half of (moderate; LAYER sequence; REPEAT yes)

**What is wrong.** Checked against data/standards/aasl-words.txt:
- **Day 13 (mid-year check)** lists ~AASL.I.A.1 ("turn a topic ... into questions") and ~AASL.IV.B.1 ("search more
  than one kind of source"). Its items are a sort, a rewrite, a query changed twice and a next-step line. None turns
  a topic into questions or searches a second kind.
- **Day 28 (year-end check)** lists ~AASL.IV.B.1 for "one query changed", which is one kind of source only.
- **Day 5 (end of unit 1)** gives ~AASL.I.A.1 as "the plan question at the top of the page" and ~AASL.IV.B.1 as
  "the two kinds named on the results page". Neither is a task a student does, and a busy writer cannot build an
  item from either line.
- **Day 19 (end of unit 3)** claims ~AASL.IV.B.4 ("sort notes by ... a plan you can explain") through "notes under
  the question's headings". The explain half is not asked, although days 15, 17 and 18 teach choosing a layout with
  a reason.
- **Days 19 and 28** claim ~AASL.II.B.2 ("compare how several sources with different views treat the same
  question"). The scope and the K to 5 neutral rule both say grade 5 compares facts only, so the code is begun here,
  not met. Listing it on an assessment day makes the item look like it checks views.

**Why it matters.** sequence-write rule 2 ("checks claim only what they sample"; "each part of each code"). The unit
plan writer copies the codes column, and each of these becomes an item that marks a student on half a code or on
nothing. This is the same kind of fault as grade 1 finding 3.

**Fix (settled below).**
- Day 13: drop ~AASL.I.A.1 and ~AASL.IV.B.1 from codes.
- Day 28: drop ~AASL.IV.B.1.
- Day 5: drop ~AASL.IV.B.1. Day 3's g4-search-more-kinds retrieval holds it as practice. Keep ~AASL.I.A.1 with a
  real prompt inside the sort's 8 minutes: after the rewrite, "write one more question research could answer on the
  same topic". Change the note's "each part of each code" line to match.
- Day 19: add one line inside the 13-minute notes part: "say which plan your notes are sorted by and why".
- Days 19 and 28: drop ~AASL.II.B.2 from codes. Keep it on teaching days 15, 17 and 18. The .md's unit 3 line says
  "begun here, not assessed".
- Update the .md's end-of-unit and check lines for units 1 and 3 to match.

**Confidence.** Firm.

### 3. Health grade 5's source-check card runs in weeks 5 to 9 and the scope does not meet it (moderate; LAYER frame; REPEAT new)

**What is wrong.** Health grades 3 to 5, unit 16 (grade 5, weeks 5 to 9 in calendar.csv; days 65 and 66) brings
back health's "source check" card: who made it, what they want, is there evidence, does an adult I trust agree. It
runs that card on three invented claims, the week before library day 7 and two weeks before day 8's lateral check.
Neither the frame's Cross-subject section nor the scope names it.

The lens warns against two subjects teaching source judging without a line on how they relate. The two cards
overlap: both ask who made it and why. They differ in one way: library sends the student off the page, while
health's card is read mostly on the page.

**Why it matters.** Grade 5 students meet two source-judging cards a few weeks apart from the same classroom day.
Without a bridge sentence, the lateral check looks like a rival method, or the health card's on-page reading passes
for the whole of judging.

**Fix.**
- Scope (settled below): day 8's note adds a bridge. It names health's source check (health grade 5 unit 16, weeks 5
  to 9), says the lateral check begins from its "who made it, what do they want", and adds leaving the page and the
  second source. The .md's unit 2 Leans line names it.
- Frame (For the lead): add a health row to the Cross-subject section of the grade 5 library frame. The health frame
  may want a matching line that library grade 5 adds "leave the page".

**Confidence.** Likely (calendar.csv and the health days, read for this report).

### 4. Day 25, the revision day, is typed Respond, and unit 4's response time is named twice (moderate; LAYER sequence; REPEAT new)

**What is wrong.** In GLOSSARY "teaching day", a respond day acts on an assessment, and "every day that drafts,
revises or edits a piece of writing is Application". Day 25 revises the group product from teacher and peer advice
before the product is scored on day 26, so it acts on no assessment. The .md and day 27 also name unit 4's response
time as "day 25 (revision) and day 29". The frame calls the revision "unit 4's respond step", but that is the
frame's word for its place in the cycle, not a day kind.

**Why it matters.** The kind column drives the unit plan's day template. A Respond template regroups students by a
rubric step missed, which is wrong for a group revision. Response time is counted once (sequence-read), and day 29 is
the only day that responds to unit 4's assessment.

**Fix (settled below).** Make day 25 Application. Its goal reads "Inquiry: revise the product from advice ...".
Response time for unit 4 is day 29 alone (12 minutes) in the .md unit 4 section and in day 27's note.

**Confidence.** Firm.

### 5. Day 11 asks a privacy item that nothing this year teaches or retrieves (minor; LAYER sequence; REPEAT new)

**What is wrong.** Day 11 holds an item on what a student does if a page asks for a name or a photo
(~AASL.VI.A.1). Days 2 to 10 carry only the stop rule (close it, tell the adult). The name-and-photo rule is part of
g3-safe-searching, last used in library grade 4 (two grade 4 days carry it), so by rule 2 it needs a retrieval
before it is assessed. None is placed.

**Why it matters.** A student who has not met the rule since grade 4 is marked on it cold. It is a small item, but it
sits on an owned unit's end-of-unit assessment.

**Fix (settled below).** Day 8's show-me adds one modeled case under the stop rule, about 1 minute: a page asks for
your name and a photo, so close it and tell the adult. Day 9's opening retrieval adds the same as one scenario card
inside its 5 minutes, and day 9's retrieves adds g3-safe-searching.

**Confidence.** Firm (grade 3 and grade 4 days.csv).

### 6. Day 2 models six moves in about 19 minutes with no split written (minor; LAYER sequence; REPEAT yes, kindergarten finding 4's kind)

**What is wrong.** Day 2 opens with a 5-minute retrieval and ends with a 5-minute exit ticket. That leaves about 19
minutes to model:
- a key-word and synonym list
- four kinds of query change
- reading source names
- skipping the ad
- the site menu
- keeping a log and looking back at it

The unit's load is genuinely two moves (questions, then searching and logging), and two show-me days is right.
However, nothing tells the unit plan writer the work fits.

**Why it matters.** If day 2 runs long, the menu case or the look-back slips to day 3. Day 3 is a Fluency day, so
the move would then be first taught on a practice day, which the scope itself rules out.

**Fix (settled below).** Day 2's note gets the split: retrieval 5, key words and the four query changes with source
names and the ad on one results page 9, the menu case 3, the log and its look-back 7, exit 5. If the unit plan's
dry run cannot hold it, the menu case is modeled in the first minute of day 3 before pairs start, with day 3 typed
Understanding for that minute's sake. Raise that at the unit plan, not now.

**Confidence.** Judgment call.

### 7. Small fixes (minor; LAYER sequence and process; REPEAT yes)

- **Stale For the lead item 5** (and the frame's item 5). data/standards/aasl-words.txt already reads "Question each
  source's maker and purpose, and check what it says, before trusting it." The gloss was widened, so drop the item
  or say it is done.
- **The gate's "standard None" note** on unit 3 comes from the frame's literal "None". For the lead: frame.py or the
  frame's cell should read empty, so the note stops firing.
- **Bat source set accuracy.** The stand-alone question "How do bats find their way in the dark?" invites "bats use
  echolocation". Many fruit bats find their way mainly by sight and smell (from memory). Day 1's note or the unit 1
  source-set line says the set states this as "most bats", so the sourced answer is true.
- **NetSmartz.** The listing was opened 2026-11-26. "Being a Good Digital Citizen: Grades 3-5" is listed there, and
  the page asks visitors to log in or register to download. The scope's line ("not opened") is accurate. The kit
  itself is a browser check for the sensitivity read.

## Checked and right; do not touch

- **Readiness and retrieval.** Every assumed row is a grade 4 row, used the year before, so retrieval is right and no
  readiness check is owed. The carried codes owned by grade 2 and 3 rows reach grade 5 through grade 4 rows used last
  year (one hop), so nothing is two grades idle except the finding 5 item.
- **Order inside units.** Each Fluency day practices only what the show-me days modeled. Day 8 teaches the statement
  check before day 9 practices it. Day 15 teaches the layout choice before days 17 and 18 ask for it. Each arc ends
  in the unit's product and share.
- **Lateral reading.** Leaving the page, who is behind it, why it was made and a second source are taught on printed
  "what others say" cards, so a paper-path student meets AASL.IV.B.3 in full. Social studies' revolution sources are
  not borrowed. This is the lens's central point, and it is done well.
- **Calendar.**
  - school_day = 5n puts every unit in the frame's weeks.
  - The checks are in weeks 13 and 28, as CALENDAR.md gives.
  - The hosts were checked against calendar.csv: ELA unit 2 weeks 9 to 16, science unit 1 weeks 1 to 4, science
    unit 6 weeks 25 to 30. The two out-of-step hosts are honestly sent to the lead.
- **Course-level checks** draw only from earlier units, and the .md says so. Unit 4's owned ids are named as being on
  no check, with the reason (rule 3, L107).
- **Unit 4's two-part end.** Day 27 reuses day 26's record, so evidence is collected once.
- **Candidate cells** are all settled, with minutes inside the unit's days.
- **Sensitive ground.** The neutral rule, groups mixed by the teacher, the audience kept inside school, the home
  route and honest use without shaming are all on the days they apply.

## What I could not judge

- The online-reasoning lessons, the web-literacy book and the continuum's 3 to 5 band file are not loaded (L149).
  The lateral-check days rest on the frame and on memory of the method.
- The minutes of each day stay provisional until pages are tried.

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| Shorter path: replace fold-in 1 (day 3) with day 30 folded into day 29 (reteach 10, gaps 10, year look-back 9); keep fold-in 2 | Day 3 is unit 1's only practice day, and its work overfilled days 1, 2 and 4 | scope-and-sequence.md Shorter path |
| 30-minute session: day 11 reason lines 11 minutes, lateral part 15 | 27 minutes does not fit 26 working minutes | scope-and-sequence.md Shorter path |
| Drop ~AASL.I.A.1 and ~AASL.IV.B.1 from day 13; ~AASL.IV.B.1 from days 5 and 28; ~AASL.II.B.2 from days 19 and 28 | Checks claim only what they sample | days.csv codes; .md unit 1, unit 3, checks |
| Day 5: "write one more question research could answer on the same topic" inside the sort's 8 minutes, as the ~AASL.I.A.1 prompt | Gives the carried code a real task | days.csv day 5 goal and note; .md unit 1 |
| Day 19: "say which plan your notes are sorted by and why" inside the 13-minute notes part | Asks the explain half of ~AASL.IV.B.4 | days.csv day 19; .md unit 3 |
| Day 8 note: bridge to health grade 5 unit 16's source check (weeks 5 to 9) | Two source-judging cards in one grade need one sentence on how they relate | days.csv day 8 note; .md unit 2 Leans |
| Day 25 kind Application, goal "Inquiry: revise ..."; unit 4 response time = day 29 alone | A revision from advice acts on no assessment; response time counted once | days.csv day 25 and day 27 note; .md unit 4 |
| Day 8 models the name-and-photo case (1 minute); day 9 retrieval adds it, retrieves adds g3-safe-searching | Day 11 assesses it; last used in grade 4 | days.csv days 8 and 9 |
| Day 2 note gets the minute split 5 / 9 / 3 / 7 / 5 | Shows the six modeled moves fit before the unit plan | days.csv day 2 note |
| Bat set says "most bats" echolocate | Keeps the sourced answer true | days.csv day 1 note or .md unit 1 |
| Drop For the lead item 5 as done | The words file already carries the widened gloss | scope-and-sequence.md For the lead |

## For the lead (frame and process)

- Add a health grade 5 unit 16 row to the library grade 5 frame's Cross-subject section (finding 3).
- Unit 3's owned-standards cell "None" makes sequence.py print "standard None is on no day". Make the cell empty, or
  have the gate skip "None".
- The frame's item 5 (AASL.IV.B.3 gloss) is done and can be closed.

## For Cory

None. Nothing here changes scope, money, people or audience.

## Sources

- NetSmartz resources listing, https://www.missingkids.org/netsmartz/resources: confirms the grades 3 to 5
  presentation's title and that a download asks for log-in or registration.
- data/standards/aasl-words.txt: our own words for each id, used for the part-of-code checks.
- Bat navigation by sight and smell in many fruit bats: from memory, not re-read.

## For the source list

Nothing new. The NetSmartz listing is already named in the frame. The log-in note is new information for its row if
it is listed in docs/APPROACH-SOURCES.md.

Note: EXPERT.md asks for findings to be logged with `scripts/plan.py defect`. The brief limits this read to its
report, so the caller logs them.
