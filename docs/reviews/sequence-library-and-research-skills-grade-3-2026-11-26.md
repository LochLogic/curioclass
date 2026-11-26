# Expert read: scope and sequence, Library and Research Skills, grade 3 (2026-11-26)

Course `library-and-research-skills-grade-3`. Read cold as a grade 3 teacher and school librarian, a district
adoption reader and a researcher, per docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md.
The scope was written by a fresh Claude agent; this read edits nothing but this report.

## What I read

- docs/courses/library-and-research-skills-grade-3/scope-and-sequence.md and
  data/plans/library-and-research-skills-grade-3/days.csv (all 30 rows), in full.
- The frame (docs/courses/library-and-research-skills-grade-3/frame.md), in full, and its Codex read
  (docs/reviews/frame-library-and-research-skills-grade-3-codex-2026-11-25.md, finding headings; all five are applied
  in the frame).
- data/progressions/library.csv, every grade 3 row and the grade 2 rows it assumes; library-edges.md;
  data/standards/aasl-words.txt for the 14 ids the course names.
- docs/agents/EXPERT.md, docs/agents/lenses/library.md, docs/ADOPTION-BAR-SUBJECTS.md (shared core C1 to C16 and part
  11); docs/courses/library/STANDARD.md and APPROACH.md (the parts the frame cites).
- build/scope-writes/AFTERCORE-BRIEF.md; DESK-ANSWERS entries "after-core frame calls" and "arts scope lead calls"
  (the 10-days-short definition); SEL STANDARD section 7 and the SEL grades 3 to 5 frame (the talk turn card).
- docs/courses/CALENDAR.md and data/plans/calendar.csv rows for grade 3 ELA, science, social studies, health and
  library.
- Earlier reads for the REPEAT tag: sequence-library-and-research-skills-kindergarten-2026-11-26.md and
  sequence-library-and-research-skills-grade-1-2026-11-26.md (with their fixes files).

Gates first: `scripts/plan.py check` (this course: 0 failures), `scripts/frame.py calendar` (library grade 3 checks
in weeks 13 and 29), `scripts/sequence.py check` (0 failures; notes that unit 3 owns no id, which is the frame's
design), `scripts/frame.py check` (0 failures), `scripts/stale.py check` (0 failures). Day numbers, totals, unit day
counts, kinds, an assessment per unit, respond days and owned-skill placement are settled by them and not re-checked.

## Verdict

The scope is sound: four full inquiry cycles in the frame's order, hosts that really are in step on calendar.csv,
every grade 2 row retrieved inside a day, the stop rule and privacy on the right days, and checks in weeks 13 and 29,
clear of every grade 3 core check week. The biggest risk is the same as the grade 1 read: the Shorter path does not
hold in minutes, since its fold-ins push work into days that are already full and the 30-minute session leaves days
26 and 30 at 29 minutes with nothing to cut. The change that matters most for students is finding 2: six assessment
items claim an id but ask only part of it, so a unit plan writer copying them will build checks that miss the
"choose and say why", "check what it says", "more than one kind" and "respect their rights" parts.

## Findings, most serious first

### 1. The Shorter path does not hold in minutes (serious; LAYER sequence; REPEAT yes)

**What is wrong.**
- (a) Thirty-minute session: the path saves time only by trimming the opening retrieval and the exit ticket. Day 26
  (5 + 6 + 12 + 6 = 29 minutes) and day 30 (12 + 12 + 5 = 29) have neither, so each runs 3 minutes over the 26
  working minutes. Day 29's 25-minute sitting fits with 1 minute to spare, which is no room for handing out a catalog
  page.
- (b) Fold-in 1 moves an 8-minute sort round into day 1's last minutes and the look-it-up sort plus the grade 2
  retrieval into day 3, and names nothing either day sheds. Day 1 already holds the hook, the six-step cycle card,
  the think-aloud to three questions, both sorts and a 5-minute exit ticket; day 3 already holds the background read,
  the judge minute, the predict line, three questions, the pick, finding the answer, the say-back and the self-check.
- (c) Fold-in 2 puts two pair scenario cards each at the end of days 6 and 8 (day 8 is a full practice day) and loses
  the only practice of the turn routine, an owned part of AASL.VI.A.1; "stays on day 6" means modeled only.
- (d) The lead's call (DESK-ANSWERS, "arts scope lead calls") counts 10 school days short as lost sessions: for a
  once-a-week course about 2. Three are named, which is fine, but the first two must hold.

**Why it matters.** Bar C2 asks for a short path that holds with nothing assessed or owned cut. A teacher who loses
two library days follows this path into an inquiry day that cannot finish.

**Fix (no day added; settled below).**
- 30-minute session: day 26 runs 5, 4, 12, 5 (pair practice on one note pair; the self-check's written line drops,
  the faces stay); day 30 runs 10, 11, 5. State day 29 as "hand out the catalog page before the session".
- 10 days short = 2 sessions: use fold-ins 3 (day 12 into day 14, as written) and a rebuilt fold-in 1. Day 2 into day
  3: the g2-question-to-research retrieval becomes the first of the student's three questions (write it with a
  question word); the three questions are then sorted both ways on the same sheet (thin or thick, then know it, look
  it up or nobody can, about 3 minutes); the say-back stays. Budget: background 5, judge 1, predict 1, three
  questions 5, both sorts 3, pick and find 7, say-back 3, self-check 3 = 28. Day 1 is unchanged.
- Fold-in 2 stays as a third, only if a third session is lost: the turn routine is practiced live on day 10, where
  pairs take turns at the closed catalog by the routine; day 8's exit ticket becomes one scenario card; day 6 keeps its
  own exit ticket.

**Confidence.** Firm (the scope's and frame's own minute budgets).

### 2. Six assessment items ask only part of the id they claim (moderate; LAYER sequence; REPEAT yes)

**What is wrong.** Against data/standards/aasl-words.txt and the row notes:
- Days 11 and 29 claim ~AASL.IV.B.1 ("search more than one kind of source"), but both items search one printed
  catalog only.
- Day 19 claims ~AASL.IV.A.3 ("choose which sources to use, and say why each one earns its place"); no item asks a
  choice or a reason.
- Day 29 claims ~AASL.IV.B.3 ("question each source's maker and purpose, and check what it says"); it asks the
  labels, maker and purpose, but no check in a second source.
- Days 19 and 29 claim ~AASL.IV.B.4 ("a plan you can explain"); the row says the student says why each note goes in
  its box, but neither rubric asks it.
- Day 28 claims ~AASL.VI.B.2 ("name who made each work you use and respect their rights"); the source list asks the
  first half only.
- Day 11 claims AASL.VI.A.1 on four scenario cards, but the row names five parts (stop rule, turns, private
  information, the password, care of books and devices) and the cards' parts are not named; the row's library-map
  part of g3-key-words is not asked at all.

**Why it matters.** The unit plan writer copies these rows into items. A class can pass days 11, 19, 28 and 29 having
never chosen a source, checked a claim, explained a note's box or said why copying is wrong.

**Fix (settled below; about 1 to 3 minutes each, all inside 29 minutes).**
- Day 11: the search plan's "where to look" line asks two places, the catalog and one other kind (the reference
  shelf on the map); add one map item, "which area holds this book?". Name the four cards' parts: stop rule; private
  information; the two invented passwords; turns and care of a shared device. Sitting about 26 minutes.
- Day 29: the two-try search plan's second try is in another kind of source; add one second-source item (does the
  second source agree?) and one "why this box" line. Sitting about 27 minutes; drop one of the three source labels to
  hold 25 if needed.
- Day 19: add "circle the two sources you would use for this question and say why each earns its place" (about 3
  minutes) and one "why this box" line. Sitting about 27 minutes.
- Day 28: add one one-answer item, "A classmate copied a sentence from a book into their poster. What should they
  do?" (put it in own words and credit it; about 2 minutes). Sitting about 22 minutes.

**Confidence.** Firm (the words file against the day rows).

### 3. Days 15 and 17 are overloaded while day 16 is light (moderate; LAYER sequence; REPEAT new)

**What is wrong.** Day 15 carries the hook and compelling question, primary or secondary, maker and purpose, a
checkable statement beside an opinion, the second-source check and a 5-minute exit ticket: five moves in one
show-me. Day 16 carries one move (notes in boxes) plus a retrieval. Day 17 carries a retrieval, a six-source sort with
maker and purpose, the caption card, two accounts for statement and opinion, a second-source check, notes from a
passage and an exit ticket: well over 29 minutes for grade 3 pairs.

**Why it matters.** The checkable statement and the second-source check are the grade 3 form of leaving the page
(bar item 3). Squeezed into the end of a crowded show-me, they become the step that gets skipped.

**Fix (a day swap inside the unit; settled below).** Day 15: hook, compelling question, primary or secondary, maker
and purpose, exit ticket. Day 16: retrieval (5), notes in boxes model (about 10), then the checkable statement and
second-source think-aloud (about 7), with g2-two-books-differ retrieved here as its opening question, exit ticket (5).
Day 17: fact-sort retrieval (3), six-source sort with the caption card (8), two accounts (6), second-source check (3),
notes from one passage (7), collected as the day's exit evidence in place of a separate ticket: 27 minutes. Move
g2-two-books-differ from day 17's `retrieves` to day 16's.

**Confidence.** Likely (minute counts are ours; the frame gives none for these days).

### 4. Day 23's waiting teams have about 18 minutes and a 5-minute card (moderate; LAYER sequence; REPEAT new)

**What is wrong.** Seven teams are observed one at a time for about 3 minutes each, so each team waits about 18
minutes. The only waiting task named is the retrieval card (a credit line and a say-back), about 5 minutes.

**Why it matters.** Twenty-five unoccupied eight-year-olds make the observation unrunnable by one adult, and noise
spoils the very talk being scored.

**Fix (settled below).** The waiting card has two parts: the retrieval (about 5 minutes), then "finish your
subquestion notes from day 22 and star the one fact you will report, with its source" (about 10 minutes), then the
exit ticket. The starred fact also readies the product on day 24.

**Confidence.** Likely (classroom management, from memory).

### 5. Facts and guards the source sets must get right (moderate; LAYER sequence and frame; REPEAT new)

**What is wrong.**
- **Passwords (days 6, 9, 11).** The "easily guessed versus harder" pair is not defined. Current federal guidance
  (CISA, "Use strong passwords", opened 2026-11-26) puts length first: at least 16 characters, or a passphrase of 4
  to 7 unrelated words. A card that makes "harder" mean a short word with a symbol swapped in teaches the old rule.
- **Predation guard.** Units 3 and 4 bar predation pictures, but unit 1's stand-alone question is "How do spiders
  catch their food?" and unit 4's is "how do they depend on each other", which invites food chains. The guard is not
  carried to unit 1 at all.
- **The far side of the moon (unit 2).** The common slip is "the dark side"; the far side gets as much sunlight as
  the near side and is simply the side always turned away from Earth.
- **Storms (unit 3).** Indoor safety should follow the National Weather Service's "When thunder roars, go indoors"
  (from memory, not opened: browser check).
- **One-answer labels (days 17, 19).** A diagram and a photo with a caption written by someone else can be read as
  either primary or secondary; as one-answer items they will be marked wrong for a defensible answer.

**Fix (settled below).** Day 6 and 9 notes: the harder invented password is a long string of four unrelated words;
the easy one is a name or a short word; no symbol-swap example. Days 1 and 3: spider pictures show webs and silk, no
prey being eaten. Day 22: dependence shown as shelter, plants and clean water, no eating pictures. Day 10 note: the
moon source set says the far side gets sunlight. Day 15 note: storm safety follows the weather service's indoor rule,
checked at the days. Days 17 and 19: one-answer label items use only a photo the maker took, a log, a letter and a book
passage; the diagram and captioned photo stay in the practice sort, discussed, not marked.

**Confidence.** Firm on passwords (CISA page, also NIST's current digital identity guidance from memory); firm on the
moon (from memory, a standard fact); likely on the rest.

### 6. Day 21's team turn does not start from SEL's talk turn card (minor; LAYER sequence; REPEAT yes)

**What is wrong.** Day 21 models a team turn on a new skill card. SEL grades 3 to 5 grows the talk turn card to four
steps (listen, say back, ask a question, add your idea; SEL 3 to 5 frame, from STANDARD section 7). Library is not
bound by the shared-card rule, but a grade 3 student then meets two turn cards for one move (the kindergarten read made
the same call).

**Fix (settled below).** Day 21's note: the team meeting opens with SEL's four talk turn steps in SEL's words; library
adds "report one finding, name what a teammate added, the recorder writes it". Where the school runs SEL, it is a
reminder; where it does not, this day teaches it. No time added.

**Confidence.** Likely.

### 7. Small data fixes (minor; LAYER sequence; REPEAT yes)

- Day 14: "a group whose class count on unit 2 shows a missed step" cannot place a student, since a class count has
  no names. Groups for unit 2 come from day 11's class record sheet by name.
- Day 19's pond-life set and unit 4's team pond set must not share sources, or unit 4 teaches from the assessment's
  passages; say so on day 19.
- With finding 3, day 17's exit ticket becomes the collected notes; with finding 2, the .md's unit 2, unit 3, unit 4
  and check 2 bullets take the new items and minutes.

## Checked and right (do not touch)

- Calendar: `school_day` = 5n gives week n for every day; units in weeks 1 to 5, 6 to 12, 15 to 20, 21 to 28; checks in
  weeks 13 and 29 as frame.py and CALENDAR.md give; library is a special outside rule 1, and neither week is a grade 3
  core check week (ELA 16, 32; math 12, 23, 31; science 9, 20, 30; social studies 14, 25, 28). Week 29 shares with
  health 3 to 5's grade 3 year-end check, which the rule allows.
- Hosts on calendar.csv: social studies unit 1 weeks 1 to 5; science unit 2 weeks 5 to 9 and ELA unit 2 weeks 8 to 16
  beside unit 2; science unit 4 weeks 15 to 20 and social studies unit 4 weeks 15 to 18 beside unit 3; ELA unit 3
  weeks 17 to 24 and unit 4 weeks 24 to 32 beside unit 4. All as stated.
- Retrieval: every assumed row is grade 2 (checked against `assumes`), so no readiness check is owed; each opens
  inside a day, never on a unit's day 1. Day 15 models source kinds the day before g2-kinds-of-sources is retrieved,
  which the frame's day-2 rule causes; g2-who-made-it was already retrieved on days 3 and 10, so it holds.
- Owned ids: AASL.I.A.1 and AASL.VI.A.1 on teaching days and both on a course-level check; unit 4's five owned ids on
  days 21 to 28 with observation (day 23), the revised product (day 27) and the sitting (day 28), each asked of every
  student. No id is claimed outside the frame's rows; carried ids are marked `~`. Unit 3 owns none, by the frame.
- Course-level checks draw on earlier units and say so; units 2 and 4 are carried as class counts; no form repeats
  within two weeks. Unit 4's codes on no check are named with the reason and sent to the lead (scope item 3); agreed.
- Every Candidate cell is settled with its cost. Show-me days model every move a practice day uses. Sensitive ground
  items 1 to 4 sit on the right days in the frame's words; social studies' Native nations content is not borrowed;
  no organization is named on a student page.
- Lens checklist (scope and sequence layer): host task named, met; source judging as a page checklist, not present
  (the second-source check is the grade 3 move off the page); citation with research to cite, met (unit 4 cites its
  own notes); end-of-unit assessment as recall of terms, not present; AASL text copied or alignment claimed, not
  present; live web page without capture, not applicable (closed paper sets); paid database, none; product or search
  company names, none; claims of effect, none.
- Stale notes: none found beyond the stale check; the scope's "For the lead" item 1 is right that the calendar pass
  settled frame item 3.

## What I could not judge

- The NetSmartz grades 3 to 5 presentation: the listing (https://www.missingkids.org/netsmartz/resources, opened
  2026-11-26) shows "Being a Good Digital Citizen: Grades 3-5" and says to log in or register to download; not
  opened. The scope rests nothing on it, rightly.
- The continuum 3 to 5 band file's cells are taken from the frame's reading (L149 not yet loaded into the store).
- The source sets are not written yet, so their accuracy and voices (C12) wait for the days.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| 30-minute session: day 26 at 5, 4, 12, 5; day 30 at 10, 11, 5; day 29 page handed out before | Fit 26 working minutes | scope-and-sequence.md (Shorter path) |
| 10 days short = 2 sessions: fold-ins 3 and a rebuilt 1 (day 2 into day 3 at 28 minutes); fold-in 2 only as a third, turn routine practiced live on day 10 | Receiving days must hold 29 minutes; no owned part loses its practice | scope-and-sequence.md (Shorter path) |
| Day 11: two places on "where to look", one map item, the four cards' parts named | ~IV.B.1, VI.A.1 and the row's map part asked in full | days.csv day 11; .md unit 2 |
| Day 19: choose two sources and say why; one "why this box" line | ~IV.A.3 and ~IV.B.4 asked in full | days.csv day 19; .md unit 3 |
| Day 28: one copied-sentence item | ~VI.B.2 "respect their rights" | days.csv day 28; .md unit 4 |
| Day 29: second try in another kind; one second-source item; one "why this box" line | ~IV.B.1, ~IV.B.3, ~IV.B.4 asked in full | days.csv day 29; .md check 2 |
| Unit 3 day swap: statement-and-opinion and second-source think-aloud to day 16; day 17 budget, notes collected as exit evidence; g2-two-books-differ retrieved on day 16 | Load by day | days.csv days 15 to 17; .md unit 3 |
| Day 23 waiting card: retrieval, then finish notes and star the fact to report | One adult can observe seven teams | days.csv day 23 |
| Password pair: four unrelated words versus a name or short word | Current federal guidance puts length first | days.csv days 6, 9, 11 |
| Predation guard on units 1 and 4; far side gets sunlight; weather service indoor rule; marked labels only on clear-cut kinds | Accuracy and the frame's guard applied evenly | days.csv days 1, 3, 10, 15, 17, 19, 22 |
| Day 21 opens with SEL's four talk turn steps | One card across courses | days.csv day 21 |
| Day 14 groups from day 11's record sheet; day 19's pond set distinct from unit 4's | Data consistency | days.csv days 14, 19 |

## For Cory

Nothing. Every finding is item-level or a day change inside the frame.

## For the source list

- CISA, "Use strong passwords", https://www.cisa.gov/secure-our-world/use-strong-passwords: opened 2026-11-26; at
  least 16 characters, random or a passphrase of 4 to 7 unrelated words, one per account. Use for any password card,
  K to 12.
- NetSmartz resources listing (above): grades 3 to 5 titles listed; download needs a log-in or registration.

## Sources

- data/progressions/library.csv, data/standards/aasl-words.txt, data/plans/calendar.csv, docs/courses/CALENDAR.md:
  ids, assumes, weeks.
- CISA page (above): finding 5.
- From memory: NIST digital identity guidance on length over composition; the far side of the moon; the National
  Weather Service lightning rule (browser check); classroom management for staggered observation.
