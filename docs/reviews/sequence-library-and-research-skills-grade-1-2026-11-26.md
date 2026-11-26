# Expert read: scope and sequence, Library and Research Skills, grade 1 (2026-11-26)

Course `library-and-research-skills-grade-1`. Read cold as a grade 1 teacher and school librarian, a district
adoption reader and a researcher, per docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md.
The scope was written by a fresh Claude agent; this read edits nothing but this report.

## What I read

- docs/courses/library-and-research-skills-grade-1/scope-and-sequence.md and data/plans/library-and-research-skills-grade-1/days.csv (all 30 rows), in full.
- The frame (docs/courses/library-and-research-skills-grade-1/frame.md), in full.
- data/progressions/library.csv, every K and grade 1 row; data/standards/aasl-words.txt for the 11 ids the course names.
- docs/agents/EXPERT.md, docs/agents/lenses/library.md, docs/ADOPTION-BAR-SUBJECTS.md (shared core C1 to C16 and part 11),
  docs/courses/library/APPROACH.md in full, docs/courses/library/STANDARD.md section 4.
- build/scope-writes/AFTERCORE-BRIEF.md; docs/agents/decisions/DESK-ANSWERS.md entries "after-core frame fix-pass
  rules", "after-core frame calls", "arts scope lead calls" (the 10-days-short definition) and "computer science
  scope lead calls".
- docs/courses/CALENDAR.md (the 32-week numbering, rule 1, the grade 1 table) and data/plans/calendar.csv rows for
  ELA grade 1 and science grade 1.
- Earlier reads for the REPEAT tag: docs/reviews/sequence-computer-science-grade-1-2026-11-26.md and
  sequence-music-grades-k-to-2-2026-11-26.md (finding headings and the part-of-code findings).

Gates run first: `scripts/plan.py check` (this course: sequence 0 failures, frame 0 failures), `scripts/frame.py
calendar` (library grade 1 checks in weeks 13 and 28), `scripts/sequence.py check` (0 failures; notes that units 2 to
4 own no id, which is correct), `scripts/stale.py check` (0 failures). Day numbers, totals, unit day counts, kinds,
an assessment per unit, respond days and owned-skill placement are settled by them and not re-checked here.

## Verdict

The scope is sound in its spine: four full inquiry cycles on named host tasks that really are in step on the
calendar, the one owned id (AASL.I.A.2) on teaching days and both course-level checks, every kindergarten row picked
up as retrieval, and careful sensitive-ground handling. The biggest risk is the Shorter path: its three fold-ins
push 7 to 8 more minutes into days that already hold 19, and its 20-minute session keeps assessments of 16 to 18
minutes in about 14 working minutes, so neither reduced path holds as written. The one change that matters most for
students is finding 2: the owned id's assessment shows a picture of the topic, so a child can draw what they see and
be marked as giving a prior fact.

## Findings, most serious first

### 1. The Shorter path does not hold: fold-ins and the 20-minute session overfill their days (serious; LAYER sequence; REPEAT yes)

**What is wrong.** (a) Each fold-in moves about 8 minutes of modeling into a receiving day that already fills its 19
working minutes, and names nothing the receiving day sheds. Day 4 already holds a sheet per child, the book choice,
the read-aloud, checking a "know", drawing a fact, a share circle and the self-check; adding the day 3 model (8
minutes) plus the moved k-picture-book-labels retrieval makes about 27 minutes. Day 25 (pairs give a star and a wish,
each maker revises) gains day 24's 8-minute model; day 30 gains day 29's reteach. "Together about 34 working minutes
are folded and three sessions freed" is the arithmetic of the problem: 57 working minutes of sessions are removed and
34 are pushed into three full days. (b) The shorter session (20 minutes) leaves about 14 working minutes after the
frame's 3 minutes at each end, yet the path says "every assessment form keeps its minutes": days 5 (17), 11 (16), 13
(17), 19 (18), 26 (17) and 28 (18) cannot. (c) The "10 days short" bullet says the year loses nothing because weeks
31 and 32 are empty. That is true only if the lost days are the last two weeks. The lead's call (DESK-ANSWERS,
"arts scope lead calls") counts 10 school days short as lost sessions: for a once-a-week course that is about 2
sessions, wherever they fall.

**Why it matters.** The brief and bar C2 ask for a short path that holds with nothing assessed cut. A teacher who
loses library day twice follows this path and runs two days that cannot be finished, one of them an inquiry day.

**Fix (no day added).** Rewrite the Shorter path:
- 10 days short = about 2 lost sessions; use fold-ins 1 and 2 below for them, and fold-in 3 for a third.
- Fold-in 1, day 3 into day 4: day 4 drops its k-wonder retrieval (done on day 2), opens with the story-or-information
  model in 5 minutes on the two sunflower covers, does the bin fetch (k-picture-book-labels) as the act of choosing
  the book, and takes the share circle to three children. Day 4 then holds 19 minutes.
- Fold-in 2, day 24 into day 25: the star and wish modeled on the pretend page in 5 minutes, one star and one wish in
  pairs (6 minutes), revision (8 minutes); k-class-inquiry is pointed at in day 27's self-check, as the scope says.
- Fold-in 3, day 29 into day 30: the reteach in small groups (10 minutes) and the reflect step on the class chart (9
  minutes), without rereading the class book (it was read on day 27).
- 20-minute session: name per check day which item runs alongside the seated sheet item. Days 5, 11, 13 and 26: the
  whisper walk runs as the teacher walks the room while children draw (about 11 to 12 minutes). Day 19: the
  sticky-note copy is the seated task while stations run (see finding 3). Day 28: the four items read once each on
  one sheet (contents 4, sticky note 3, know and wonder 5, stop steps 2: about 14 minutes). Retrieval openings go to
  three minutes, as the scope already says.

**Confidence.** Firm (the scope's and frame's own minute budgets).

### 2. The owned id's assessment can be met by drawing what the picture shows (serious; LAYER sequence; REPEAT new)

**What is wrong.** AASL.I.A.2 ("Say what you already know about a topic before you start looking") is the course's one
owned id, checked alone as "a real prior fact, unprompted". Day 5 shows "a snail picture" and asks each child to
"draw or write one fact already known"; day 13 uses "a topic picture not seen before" and day 28 "a know and wonder
sheet on a new topic", in the same form. A snail picture shows the shell, the feelers and the slime trail. A grade 1
child asked what they know will draw what is in front of them, and the teacher marking the page afterwards cannot
tell a seen fact from a known one. That is the busy-reader reading of the item, and on it the item does not check
prior knowledge. The same picture-first set-up runs on days 1, 2 and 4, so practice builds the habit too.

**Why it matters.** It is the only id the course claims, sampled on all three of its checks. A whole class can pass
it by looking.

**Fix (no day added).** Name the topic by word and a small icon (a snail outline, no detail), with the full picture
held back until the sheet is done; the marking rule on days 5, 13 and 28 becomes "a fact the icon does not show,
true of the topic". On days 1, 2 and 4, the teacher names the topic, the class fills the "know" box, and only then
is the picture or book opened ("before you start looking", in the id's own order). Change the .md unit 1 end-of-unit
line and the check lines to match.

**Confidence.** Likely (reasoning from the item as written; know-and-wonder charts are meant to come before the
source is opened in the common practice, from memory).

### 3. Three assessment items ask only part of the id they claim (moderate; LAYER sequence; REPEAT yes)

**What is wrong.**
- Day 19 claims ~AASL.III.D.1 ("Speak up with ideas and findings when a research group talks") for every child, but
  the station uses the finder, holder and teller jobs, so only the teller says the finding. The .md says "each child
  speaking up with a finding". The station is also costed at 1.4 minutes a group, below the frame's own station
  range of 1.5 to 2.5 minutes, for three six-year-olds to find a fact, tell it and each name a helper.
- Day 11 claims ~AASL.IV.B.1 ("Search more than one kind of source, not just the first site") for a single printed
  contents page and spread. Unit 2 teaches two kinds of place (the book and the page the teacher opened); the check
  asks about one. Day 28 samples ~AASL.IV.B.1 with the same one-source item.
- Day 26 claims ~AASL.I.C.1 ("Read, watch or listen to classmates' work and respond to what it says") for a star
  drawn "by one thing done well", which is about how the page is made (g1-star-and-wish), not what it says. The row's
  I.C.1 move, "one thing a friend's page taught them", happens only on respond day 27.

**Why it matters.** The unit plan writer copies the check row. Each of these becomes an item that marks a child on
half an id (sequence-write rule 2; the same kind of fault as computer science grade 1 finding 2 and music K to 2
finding 1).

**Fix (settled below).**
- Day 19: at the station each child, holding one card of the picture set, says one finding of their own (about 15
  seconds each), then each names what one helper added (about 10 seconds each); the jobs stay for handing and holding
  the cards. That is about 1.7 minutes a group, about 17 minutes for ten groups. The sticky-note copy becomes the
  seated task during the stations: one minute of instructions to the whole class, a new cover card at each seat,
  marked from the note afterwards, so the cover-card sort is not needed. About 18 minutes in all.
- Day 11: add a printed card-frame "teacher's page" on the same question; each child circles the labeled picture
  there that answers it (about 2 minutes, about 18 in all). Day 28: drop ~AASL.IV.B.1 from its codes and name
  g1-find-in-a-book alone (carried, not owned; day 11 holds it), and say so in the .md's check 2 line.
- Day 26: the whisper walk asks two things, "This page taught me ___" and the wish (about 15 seconds a child, about 7
  minutes), and the passage item is held to 9 minutes; about 18 in all. If the lead prefers not to tighten day 26,
  drop ~AASL.I.C.1 from day 26 and name it as begun on day 27's share, not assessed.

**Confidence.** Firm (words file against the day rows).

### 4. Day 22 asks each child to answer their own wonder from a closed source set (moderate; LAYER sequence; REPEAT new)

**What is wrong.** Day 22: "each child picks one wonder and finds the answering page in the class's source set". The
set is a Curio Class animal-parents read-aloud and a few pictures. Thirty grade 1 wonders will include many the set
cannot answer ("Do kangaroos have friends?"), and the unit has already dropped sorting which wonders a book could
answer to grade 2 (unit 1 Candidates). The teacher reaches day 23 with children who have no fact to draft.

**Why it matters.** The whole product, and the unit's end-of-unit claim for g1-class-book, rests on each child having
a found fact by day 23.

**Fix (no day added).** Day 22: after the know and wonder sheet, the teacher shows a picture menu of 6 to 8 wonders
the source set answers, including any class wonders that match; each child picks one, their own where it is on the
menu. The source set is written so each menu wonder has one answering page. Add one line to the note and to the .md
unit 4 arc.

**Confidence.** Likely.

### 5. Day 27 holds the book share, the self-check, the reteach and a fresh try in 19 minutes (minor; LAYER sequence; REPEAT yes)

**What is wrong.** "Book read aloud about ten minutes" for 30 pages, each child then saying "one thing a friend's
page taught them" (30 turns), then the self-check, the regrouped reteach and a fresh try in the remaining 9 minutes.
The 30 spoken turns alone take about 5 minutes at 10 seconds.

**Fix.** The teacher reads each page's sentence (about 6 minutes); each child tells a partner one thing a friend's
page taught them (2 minutes); the self-check by pointing (2 minutes); the reteach and fresh try (9 minutes). Note it
on day 27.

**Confidence.** Likely.

### 6. Leave-out of unit 1 breaks more than the scope names (minor; LAYER sequence; REPEAT new)

**What is wrong.** The leave-out bullet bridges only unit 4. Day 10 (unit 2) retrieves g1-what-i-know, and the
mid-year check (day 13) samples unit 1 only, so with unit 1 left out it has nothing to sample.

**Fix.** Add: day 10 opens with the know and wonder sheet's one-step form (say one thing you know, one thing you
wonder) in place of the retrieval, claiming nothing; day 13 then samples unit 2 on new cases (a contents page item and
the stop steps for a pretend case, about 11 minutes, in forms not given on day 11), and the .md says so.

**Confidence.** Firm.

### 7. The page the teacher opens is not named (minor; LAYER sequence; REPEAT new)

**What is wrong.** Days 9 and 10 use "the page the teacher opened" and "the teacher's page" without saying what page
it is. The lens marks "a live web page relied on with no dated capture or teacher swap note", and APPROACH.md names no
real site.

**Fix.** Days 9 and 10's notes name it as the unit's tree-roots read-aloud on the Curio Class site (the same page
printed in the card frame on the paper path); any other page the teacher picks gets the teacher page's swap note.

**Confidence.** Firm (lens line).

### 8. Small data fixes (minor; LAYER sequence; REPEAT yes)

- Day 4's `retrieves` names k-wonder, but the day has no retrieval task in its goal or note. With fold-in 1 above,
  clear it from day 4 and from the .md table (k-wonder: day 2).
- Day 29's codes drop ~AASL.V.C.1 though day 28 checks it; add it.
- Day 30 lists g1-class-book in `skills` with no ~AASL.I.B.3 in `codes`; add it or drop the skill.
- With finding 3, day 19's note loses the cover-card sort, and day 28's codes lose ~AASL.IV.B.1.

## Checked and right (do not touch)

- Calendar: `school_day` = 5n - 2 gives week n for every day; units in weeks 1 to 6, 7 to 12, 15 to 20, 21 to 27;
  checks in weeks 13 and 28, as CALENDAR.md's table gives; library is a special outside rule 1, and neither week is a
  grade 1 core check week (14, 15, 16, 19, 29 to 32).
- Hosts are in step on data/plans/calendar.csv: science unit 1 (weeks 1 to 4) and unit 2 (4 to 9) for unit 1's day 4;
  science unit 2 just ended for day 10; ELA unit 3, birds' bodies (weeks 16 to 24), for day 18; science unit 7,
  parents and young (weeks 24 to 26), after days 22 and 23, with the frame's bridge stated. ELA leans are dated
  correctly against ELA's units 1 to 3.
- Retrieval: every assumed row is a kindergarten row (checked against `assumes` in library.csv), so no readiness
  check is owed; each opens inside a day, never on a unit's day 1; same-year rows return in later units.
- Owned code AASL.I.A.2 is on days 1, 2, 4 to 6, 10, 13, 14, 22, 28 to 30 and sampled on both checks; no id is claimed
  outside the frame's rows; every carried id is marked `~`.
- Course-level checks draw on earlier units and say so; unit 2's and unit 4's results are carried as class counts, and
  no task form from the last two weeks is reused. Response time is counted once.
- Every candidate cell is settled with its cost. Sensitive ground items 1 to 4 and kind feedback sit on the right days
  with the frame's words; no organization's name reaches a student or family page; neutral K to 5 cases.
- Day 25 as Application (each maker revises a page) follows GLOSSARY; agreed.
- Lens checklist (scope and sequence layer): host task named, met; source judging as a page checklist, not applicable
  in grade 1 (judging sits inside find, as the frame says); citation with research to cite, met (unit 3); end-of-unit
  assessment as recall of terms, not present (every check does the move); AASL text copied or alignment claimed, not
  present; live web page without capture, missed (finding 7); paid database, none; product names, none; claims of
  effect, none.

## What I could not judge

- The NetSmartz K to 2 presentation's content: the listing page (https://www.missingkids.org/netsmartz/resources,
  opened 2026-11-26) shows "Be Safer Online with NetSmartz: Grades K-2" as a free download, but the listing does not
  state the "tell a trusted adult" rule; the presentation file was not opened. The scope rests nothing on it, rightly.
- The read-alouds, mini-books and cards are not written yet, so their accuracy and voices (C12) wait for the days.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Fold-in contents for days 3 to 4, 24 to 25, 29 to 30 as in finding 1; 10 days short = 2 sessions | Receiving days must hold 19 minutes | scope-and-sequence.md (Shorter path) |
| 20-minute session: concurrent whisper walks, day 19 seated copy, day 28 four items about 14 minutes | Assessments must fit about 14 working minutes | scope-and-sequence.md (Shorter path) |
| Topic named by word and plain icon before any picture; mark "a fact the icon does not show" | Owned id must check prior knowledge, not looking | days.csv days 1, 2, 4, 5, 13, 28; .md unit 1 and checks |
| Day 19: each child says a finding at the station (about 1.7 minutes a group); sticky-note copy as the seated task | ~AASL.III.D.1 asked of every child; inside 19 minutes | days.csv day 19; .md unit 3 |
| Day 11 adds a card-frame teacher's page item; day 28 drops ~AASL.IV.B.1 from its codes | IV.B.1 needs more than one kind of source | days.csv days 11, 28; .md unit 2 and check 2 |
| Day 26 whisper walk adds "This page taught me ___"; passage item 9 minutes | ~AASL.I.C.1 asks about what the work says | days.csv day 26; .md unit 4 |
| Day 22 picture menu of 6 to 8 answerable wonders | Every child needs a found fact by day 23 | days.csv day 22; .md unit 4 |
| Day 27 time split (6, 2, 2, 9 minutes) | Fits 19 minutes | days.csv day 27 |
| Unit 1 leave-out: day 10 one-step form; day 13 samples unit 2 | Leave-out bridge rule | scope-and-sequence.md (Leave-out) |
| Teacher's page = the unit's Curio Class read-aloud page, with a swap note | Lens: no live page without capture | days.csv days 9, 10 |
| Day 4 `retrieves` cleared; day 29 adds ~AASL.V.C.1; day 30 codes match skills | Data consistency | days.csv days 4, 29, 30; .md retrieval table |
| Day 25 stays Application | GLOSSARY: a day that revises work is Application | none (agreed) |

## For Cory

Nothing. Every finding is item-level or a day fix inside the frame.

## For the source list

- NetSmartz resources listing, https://www.missingkids.org/netsmartz/resources: opened 2026-11-26; lists "Be Safer
  Online with NetSmartz: Grades K-2" (English and Spanish) and a K to 2 "Into the Cloud" series as free downloads; the
  presentation files themselves were not read.

## Sources

- data/progressions/library.csv, data/standards/aasl-words.txt, data/plans/calendar.csv, docs/courses/CALENDAR.md:
  ids, assumes, weeks.
- NetSmartz listing (above): the frame's sensitivity source exists as named.
- From memory: know-and-wonder (KWL-style) charts filled before a source is opened (finding 2).
