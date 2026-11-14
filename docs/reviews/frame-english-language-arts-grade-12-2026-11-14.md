# Expert cold read: course frame, English Language Arts Grade 12 (2026-11-14)

Reader: the curriculum expert (fresh agent, docs/agents/EXPERT.md), on docs/pipeline/briefs/frame-read.md with
{course} = english-language-arts-grade-12, {subject} = ela. I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/ela.md, docs/RUBRIC-ELA.md, docs/pipeline/briefs/frame-read.md and
  frame-write.md (with its "Lessons from the social studies frames" list).
- The frame, docs/courses/english-language-arts-grade-12/frame.md, and its row in data/plans/frames.csv (8 units,
  160 days). No base text, so no source map.
- Every grade 12 row of data/progressions/ela.csv, notes in full, and the grade 11 rows it picks up.
- The neighbouring frame, english-language-arts-grade-11 (read first, reviewed the same day), and for repeats every
  other ELA frame (grades 4, 5, 8, 9 and 10 matter below) searched for this year's titles and authors.
- The partner frames: us-history-ii (whole, its senior calendar and capstone), us-history-i (Plessy), and
  us-government-and-politics (units 2, 4, 5 and 8, ELA lean table).
- The 11-12 band text in data/standards/ccss-ela-standards-full.txt, every lettered part, against the frame's "Where
  each thread ends" table.
- docs/agents/decisions/DESK-ANSWERS.md, the 2026-11-12 and 2026-11-13 ELA entries.
- Gates: `python -X utf8 scripts/frame.py check english-language-arts-grade-12` (0 failures: 8 units, 160 days, 149
  in units, 11 for checks), `python -X utf8 scripts/stale.py check` (0 failures). I spent the read on what they cannot
  see.

Not opened, as instructed: docs/courses/ela-6/, docs/ela-6-spine.md, docs/NEXT-SPINES.md, the ela-6 and reconcile
reviews, and S:\CurioClass-sources\_calibration.

## Verdict

The frame is well built: every grade 12 row sits in one unit, the "where each thread ends" table names a last unit
and a final product for every band standard but one, Hamlet and Gatsby are read whole, and the three proposed row
changes are sound. The biggest risks are repeated anchors (Keller chapter 4 and the Hurston essay are grade 9's, the
Hughes poem grade 5's, the Four Freedoms grade 10's) and load: unit 1 and unit 5 carry more than their days, and the
senior research unit has no milestone calendar against US History II's capstone although history asks for one. The
one change that matters most is to replace unit 1's two repeated essays (settled below), because a student who came
up through Curio Class would open the senior year on texts already studied.

## Findings, most serious first

### 1. Repeated anchor texts (LAYER frame; REPEAT yes)

**What is wrong.**
- Unit 1 reads Keller's The Story of My Life chapter 4 and Hurston's 'How It Feels to Be Colored Me'. Grade 9 reads
  Keller chapters 3 and 4 and the Hurston essay as anchors; US History II unit 2 reads Hurston as well.
- Unit 4 reads Hughes's 'The Negro Speaks of Rivers', a grade 5 anchor; the row e12-lit-american-modern names it.
- Unit 6 lists FDR's Four Freedoms as a candidate; grade 10 unit 6 reads it.
- The independent shelf lists The Age of Innocence, also on grade 11's shelf.
- Unit 7 rereads Gettysburg (grade 9) beside the Second Inaugural (grade 11) without saying it is a reread; grade 9's
  frame says Gettysburg "is read again in grade 12", so the reread is planned, but this frame should name it as one.
**Why it matters.** Lesson 11 (no repeats of other grades' picks); rubric 2a counts range across the years. A reread
is fine when it is named and the task is new; an anchor read twice for the same purpose is not.
**Fix.** Unit 1: replace Keller and Hurston with Mark Twain, 'Two Views of the Mississippi' (Life on the Mississippi,
chapter 9, 1883) and Jane Addams, Twenty Years at Hull-House, chapter 4 (1910); keep Frost and the model essay (settled
below; both public domain, both reflective, both short). Unit 4: 'I, Too' (1926) in place of 'The Negro Speaks of
Rivers', and the same swap in e12-lit-american-modern's notes. Unit 6: drop the Four Freedoms candidate. Shelf: keep
The Age of Innocence here (grade 11 drops it, see that report). Unit 7: "Gettysburg (grade 9) and the Second
Inaugural (grade 11), reread for RI.11-12.9's theme across documents". Confidence: firm.

### 2. Days by load: units 1, 3 and 5 hold more than their days (LAYER frame; REPEAT yes)

**What is wrong.**
- Unit 1 (13 days) carries 7 rows and 12 standard codes and a full process essay with a rewrite "taking a new
  approach" (W.11-12.5), plus the year's opening routines. Grade 11's opening unit had 17 days for less.
- Unit 3 (12 days) reads Swift, the opening chapters of Pride and Prejudice and all of Earnest, and writes.
- Unit 5 (11 days) reads The Souls of Black Folk (the frame's chapters run to about 20,000 words) and A Room of One's
  Own chapters (about 13,000), about 33,000 words of hard argument in 11 days, while the rubric's 80 percent
  text-dependent rule needs time on each.
**Fix.** Unit 1: 13 to 15 days; unit 8: 38 to 36 (it still opens on the shared question day, now about day 125, see
finding 3). Unit 3: the Pride and Prejudice chapters move to home reading with one class day, or are cut. Unit 5: Du
Bois chapters 1 and 3 only ('Of Our Spiritual Strivings' and 'Of Mr. Booker T. Washington and Others'). Confidence:
likely.

### 3. Senior research against US History II: no milestone calendar, and three joints left open (LAYER frame; REPEAT yes)

**What is wrong.** US History II says "The ELA 12 frame sets its milestones against this before the pairing is called
settled." Its capstone: a question "from the 1920s to today" chosen about day 123, a standalone 1,500 to 2,000 word
product, six sources with three primary, two forms for two contrasting audiences (one beyond the classroom), unit 12
on days 148 to 160, and a cut order ("grade 12 may end early"; unit 12 can run in 10 days). The frame's unit 8 (days
123 to 160) gives no dates for the question, the source set, the draft or the talk; asks for 8 sources with no primary
count; lets the question be any; gives one audience; and has no cut order for senior early release.
**Why it matters.** A student in both courses does the work twice or misses one course's rule; the pairing cannot be
called settled.
**Fix.** Unit 8: add a milestone line: "question chosen with history about day 125 (history day 123); annotated source
list of 8, at least 3 primary, due about day 135 (history unit 10's end), one list serving both courses; full draft
about day 147 (before history's check); talk days 150 to 156 in two forms for two audiences, one beyond the classroom,
serving history's unit 12; final paper day 158." Add "in a paired school the question falls inside 1920 to today".
Add a cut order: "if seniors leave early, the paper's revision days go first, then the second form of the talk; the
source list and the draft never". Confidence: firm (US History II's text).

### 4. W.11-12.6 and SL.11-12.5: the paper path and where the threads end (LAYER standard; REPEAT yes)

**What is wrong.** As in grade 11, the paper path (posted copy, handout) is written as if it met "use technology,
including the Internet" and "strategic use of digital media". The "Where each thread ends" table names an end for
every standard except W.11-12.6.
**Fix.** Brief, "Paper path and accounts": the grade 10 and 11 wording (a shared device or lab session with the
school's tools, posted by the teacher, no student account; without it the plan records the two codes unfinished). Add
W.11-12.6 to the threads table: "ends in unit 8: the research paper published and updated with the talk's media".
Confidence: firm.

### 5. Unit 6: licensing of the housing set, and a speech picked by date (LAYER frame; REPEAT yes)

**What is wrong.**
- The housing and zoning set names "a news report, an op-ed". Both are copyrighted and often paywalled, and the rule
  is no paid copy.
- "The most recent presidential inaugural" is picked by date, not by RI.11-12.6's "rhetoric ... particularly
  effective"; with FDR 1933 and JFK it also puts three speeches from one party's presidents together if the current
  one shares it.
- The question names "our town ... rents" while the cell names "a city's zoning".
**Fix.** The housing set from US government works (a Census Bureau housing release, a HUD or GAO report, a city
council's public minutes) and two short original Curio Class pieces written as a report and an op-ed, as grade 10 does.
Add Reagan's address on the Challenger disaster (1986, a US government work) as the year's effective-rhetoric pick
beside FDR and JFK; the current speech stays as a reading under the balance rule, not as an exemplar. One wording for
the question: "Should our town change its zoning to bring rents down?" Confidence: likely.

### 6. References and the library rule (LAYER frame; REPEAT yes)

**What is wrong.** As in grade 11: research "through the library's databases", an unnamed historical dictionary and
usage guide (L.11-12.1b's own examples are paid), Tufte's Artful Sentences (L.11-12.3a's example, a paid book) as the
style model, and Hamlet's words with no named free glossary. "No student is sent to a library or a paid copy."
**Fix.** Open archives only (the Library of Congress, Chronicling America, HathiTrust full view, the Internet Archive,
government sites), school databases an extra. References as grade 11 (Webster's 1828, the Online Etymology
Dictionary, Fowler 1926, the Curio Class style sheet and the GPO Style Manual), plus C. T. Onions, A Shakespeare
Glossary (1911) and Alexander Schmidt's Shakespeare Lexicon (both public domain) for Hamlet. L.11-12.3a's syntax study
uses the year's own texts (Woolf, Du Bois, King) as models. Confidence: firm.

### 7. RI.11-12.5 on a court opinion is "judged again" but never judged first (LAYER frame; REPEAT new)

**What is wrong.** Unit 5 says the structure row is "judged again in unit 7 as review" on Tinker. The row
e12-info-structure names court-opinion structure (syllabus, holding, reasoning, dissent) as its second text; unit 5
judges structure on Woolf only.
**Fix.** Unit 7 teaches court-opinion structure as the row's second text (one day, Tinker), judged there; unit 5's line
reads "Woolf; court opinions in unit 7". Confidence: firm.

### 8. Plessy and Brown met three or four times across social studies (LAYER frame; REPEAT new)

**What is wrong.** Unit 7 reads Plessy and Brown. US History I (Jim Crow) reads Plessy, US History II unit 7 reads
Brown, and US Government unit 5 picks "one rights pair from four", including Plessy and Brown. A senior could meet
them four times.
**Fix.** Keep them here (RI.11-12.9's legal reasoning needs a pair, and the ELA lens is new); add to the cross-subject
lean: "US Government picks another of its four pairs in a school that runs ELA 12 beside it". The other course's
choice is the Government frame's; this frame only says it. Confidence: likely.

### 9. SL.11-12.1 and SL.11-12.4 taught to their headlines (LAYER standard; REPEAT yes)

**What is wrong.** SL.11-12.1 asks for discussions "one-on-one, in groups, and teacher-led"; the frame names
seminars and groups. SL.11-12.4 asks for "a range of formal and informal tasks"; every talk named is formal.
**Fix.** Unit 2: one teacher-led discussion on a Hamlet scene and one one-on-one conference on the essay draft, named.
Unit 6: an informal two-minute talk (a reaction to one speech) beside the formal policy talk. Confidence: firm.

### 10. Hard-content days and readers (LAYER frame; REPEAT yes)

**What is wrong.** Unit 4 (days 52 to 69) overlaps US History II's Holocaust unit (days 42 to 56 by its unit days); the
frame's own cross-subject line puts the overlap at days 46 to 60, two to four days off. Gatsby's Meyer Wolfsheim is an
antisemitic portrait, and no Jewish community reader is named. The sensitivity line names units 1 and 7, not 4.
**Fix.** Correct the day ranges to history's days 42 to 56, and say Gatsby's Wolfsheim chapters (4 and 9) fall after
day 56 if the calendar allows, or are taught with the "if later" line. Add unit 4 to the sensitivity reads: a Jewish
community reader and the Black community reader for McKay, Cullen and Toomer. Confidence: likely.

### 11. Who wrote the texts (LAYER frame; REPEAT new)

**What is wrong.** Rubric 2e. The year's authors are British and white American writers, Black American writers, and
no Native, Latino or Asian American author, although grade 12's span (to the early twentieth century and beyond)
includes public domain works by them.
**Fix.** Shelf adds: Mourning Dove, Cogewea, the Half-Blood (1927) and Sui Sin Far, Mrs. Spring Fragrance (1912) (grade
11's shelf takes Ruiz de Burton; if grade 11 keeps Sui Sin Far, grade 12 takes Zitkala-Sa's American Indian Stories,
1921, instead). Settled below. Confidence: likely.

### 12. Unit 3 is named by a mode (LAYER frame; REPEAT new; judgment call)

**What is wrong.** "Satire and comedy" names a mode; rubric 2d counts specific topics. Swift, Austen and Wilde share
one: money, marriage and class in Britain, 1729 to 1895.
**Fix.** Retitle "Money, marriage and class: Swift, Austen and Wilde"; question: "What do these writers show about how
money decides who marries whom, and how does laughing at it make the point?" Confidence: judgment call.

## The writers' proposed row changes

| Change | Expert view |
|---|---|
| e12-seminar: grade 11 rotating roles text made consistent with grade 10's student-set roles | Endorse, with grade 11's tweak (students choose from a named set or make their own, and set the goal). See the grade 11 report, finding 10 |
| e12-info-founding-documents: Walker's Appeal (1829) in place of the Declaration of Sentiments | Endorse: grade 10 reads Seneca Falls, so the swap removes a repeat, and Walker answers the Declaration directly. Two follow-ons: the row's words column drops "sentiments"; grade 8's frame (lines 167 to 168, "the Seneca Falls Declaration of Sentiments (grades 10 and 12)") becomes stale and needs "(grade 10)" (LAYER process) |
| RL.11-12.7's American play: grade 11's Trifles retrieved in unit 2 beside Hamlet | Endorse. Add: the lesson supplies the Trifles scene and both versions for students new to Curio Class, so nothing assumes grade 11 was taken here |

## What is right and should not be touched

- The "where each thread ends" table: every band standard has a last unit and a product, checked against the full
  text, with W.11-12.6 the one gap (finding 4).
- Hamlet read whole with two versions compared; Gatsby read whole; the independent book.
- The law unit's mock opinion on Mahanoy (2021) written by students from the public opinions, not a copied text.
- Respond days after each check, "Candidate:" cells, the stated day, "if later" lines against US History II.
- The cross-subject math lean (reading a chart in the policy unit; nothing computed ahead of math).

## Lessons from the social studies frames (frame-write.md)

| # | Lesson | Result |
|---|---|---|
| 1 | Respond day after each check | Met |
| 2 | Check-set cells start "Candidate:" | Met |
| 3 | Time a day stated | Met |
| 4 | Standards in full | Missed: SL.11-12.1 and SL.11-12.4 ranges (finding 9) |
| 5 | Each thread starts where first used | Met |
| 6 | "First" claims and one wording | Missed: "judged again" with no first (finding 7) |
| 7 | Both ends of every handoff | Met for grade 11; missed against US History II's milestone request (finding 3) |
| 8 | "If later" lines | Met, day ranges off (finding 10) |
| 9 | Days by load | Missed: units 1, 3, 5 (finding 2) |
| 10 | Questions answerable from the unit | Met, unit 6's wording fixed (finding 5) |
| 11 | Picks named, no repeats | Missed: four repeats (finding 1); news pieces unnamed (finding 5) |
| 12 | Sensitivity reads | Missed for unit 4 (finding 10) |
| 13 | No math ahead of math | Met |
| 14 | Paper path, no account | Met for access; the limits on W.6 and SL.5 not said (finding 4) |
| 15 | No status lines about other files | Met |

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 1 essays: Twain, 'Two Views of the Mississippi' (1883), and Addams, Twenty Years at Hull-House ch. 4 (1910), with Frost and the model essay | Removes two grade 9 repeats; both reflective, short, public domain | Frame unit 1 |
| 'I, Too' (1926) in place of 'The Negro Speaks of Rivers' | Removes a grade 5 repeat; public domain; answers Whitman, read in grade 11 | Frame unit 4; e12-lit-american-modern notes |
| Drop the Four Freedoms candidate; Reagan's Challenger address (1986) as the effective-rhetoric pick | Removes a grade 10 repeat; a US government work; balances the speeches | Frame unit 6 |
| Housing set from US government works and two original Curio Class pieces | No paid or paywalled copy | Frame unit 6 |
| Hamlet versions: the LibriVox full-cast recording and the 1921 silent film (public domain), plus a class staging of one scene | RL.11-12.7 met without making a recording; For the lead 6 becomes optional | Frame unit 2, For the lead |
| References: Onions's A Shakespeare Glossary (1911) and Schmidt's Shakespeare Lexicon, plus grade 11's set | Free, no account | Frame brief, unit 2 |
| Du Bois cut to chapters 1 and 3 | Fits unit 5's days | Frame unit 5 |
| Shelf: Mourning Dove, Cogewea (1927); Sui Sin Far, Mrs. Spring Fragrance (1912); The Age of Innocence kept here only | Wider authorship, no shelf repeat | Frame brief |
| Unit 1 to 15 days, unit 8 to 36 | Load; the shared question day still holds | Frame Units table |

## For Cory

- **People.** Unit 4 adds a Jewish community reader beside the Black community reader, and units 1 and 7 keep the
  readers already named (Irish for Swift if unit 3 is read, and a counselor for unit 1's reflective writing). Who, and
  any pay, is yours.
- **The panel** for the senior talk's audience beyond the classroom comes through the school, never through Curio
  Class.
- **Senior early release.** If a school's seniors leave before day 160, the cut order (finding 3) covers it; changing
  the course's length instead would be a scope call.
- **ELA check set:** as grade 11.

## What I could not judge

The computed measures (no texts.csv yet); whether the LibriVox Hamlet is a full cast (from memory, not fetched today);
the community readers' view of the picks.

## Sources

- data/standards/ccss-ela-standards-full.txt: the 11-12 band, every lettered part (findings 4, 6, 9).
- docs/courses/us-history-ii/frame.md: senior calendar and capstone (finding 3).
- LibriVox catalogue API, https://librivox.org/api/feed/audiobooks/?title=Trifles&format=json : read 2026-11-14
  (the Trifles retrieval).
- From memory, to check before a unit rests on them: the LibriVox Hamlet cast, the 1921 Hamlet film's status, the
  public-domain status of Onions and Schmidt.

## For the source list

- The LibriVox catalogue API (also in the grade 11 report).

## Confidence

Finding 1 firm; 2 likely; 3 firm; 4 firm; 5 likely; 6 firm; 7 firm; 8 likely; 9 firm; 10 likely; 11 likely; 12
judgment call.
