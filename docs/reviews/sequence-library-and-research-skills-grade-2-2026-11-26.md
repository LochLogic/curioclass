# Expert read: scope and sequence, Library and Research Skills, grade 2 (2026-11-26)

Course `library-and-research-skills-grade-2`. Read cold as a grade 2 teacher and school librarian, a district
adoption reader and a researcher, per docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md.
The scope was written by a fresh Claude agent; this read edits nothing but this report.

## What I read

- docs/courses/library-and-research-skills-grade-2/scope-and-sequence.md and
  data/plans/library-and-research-skills-grade-2/days.csv (all 29 rows), in full.
- The frame (docs/courses/library-and-research-skills-grade-2/frame.md), in full.
- data/progressions/library.csv, the nine grade 2 rows and their `assumes`; data/standards/aasl-words.txt for the 15
  ids the course names.
- docs/agents/EXPERT.md, docs/agents/lenses/library.md, docs/ADOPTION-BAR-SUBJECTS.md (shared core C1 to C16 and part
  11), docs/courses/library/APPROACH.md (kinds of day, evidence, plan fields, sites, sensitive ground, pacing).
- build/scope-writes/AFTERCORE-BRIEF.md; DESK-ANSWERS entries "after-core frame fix-pass rules", "arts scope lead
  calls" (10 days short = 10 school days), "after-core frame calls" and "computer science scope lead calls".
- docs/courses/CALENDAR.md (rule 1, the grade 2 table) and data/plans/calendar.csv rows for ELA, science and social
  studies grade 2; the host and lean rows' days in those courses' days.csv.
- For the REPEAT tag: docs/reviews/sequence-library-and-research-skills-grade-1-2026-11-26.md and
  sequence-library-and-research-skills-kindergarten-2026-11-26.md.

Gates run first: `scripts/plan.py check` (this course: sequence 0 failures, frame 0 failures; 4 units, 29 days),
`scripts/frame.py calendar` (library grade 2 checks in weeks 13 and 27), `scripts/sequence.py check` (0 failures;
notes: day 2 is the first day for ~AASL.I.A.2, which is grade 1 review, correct; units 3 and 4 own no id, correct),
`scripts/stale.py check` (0 failures). What they settle is not re-checked here.

## Verdict

The scope is sound in its spine: four full inquiry cycles on host tasks that are truly in step on the calendar (the
ELA fossil unit, science plant needs, the ELA pollination research), both owned ids taught, practiced and sampled,
every grade 1 row picked up as retrieval, and the interview guards carried word for word. The biggest risk is an
accuracy fault a librarian would catch at once: unit 2 teaches that a call label's "subject letters" tell where a topic
sits, when school libraries shelve nonfiction by a subject number and use letters for the author. The other change
that matters most is the Shorter path, whose two fold-ins add five minutes to inquiry days that have no spare minute,
the same fault the grade 1 read found.

## Findings, most serious first

### 1. Call labels: the subject is a number, not letters (serious; LAYER frame and sequence; REPEAT new)

**What is wrong.** Day 7 says the teacher "says what the subject letters tell about where the topic sits", the
candidate cell is "said aloud from the call label's subject letters", and the skill card reads "find the letter, find
the number". In the classification most school libraries use, the subject is the number (fossils and prehistoric life
560, plants 580, animals 590, cold-blooded vertebrates 597) and the letters under it are the first letters of the
author's surname; fiction is shelved by the author's letters alone. Subject letters belong to the academic library
system, which an elementary child will not meet. "Four spines in order" (days 8, 11) does not say whether the set is
fiction (letters) or nonfiction (number, then letters), and the continuum cell the frame quotes is the fiction shelf
arrangement.

**Why it matters.** C3a (nothing wrong). A child taught "subject letters" walks into the school's own library and
cannot find the frog books; a librarian adopting the course marks it down on sight.

**Fix.** Day 7's goal and note, the .md unit 2 arc and candidates line: "the teacher says what the label's number tells
about where the topic sits (books about animals sit together under one number)". The invented call labels follow the
common school form: nonfiction, a subject number over the author's first three letters; fiction, a fiction mark over
the author's letters. The skill card becomes "look it up, copy the label, find the number, then the letters; title by
author". Days 8 and 11: the mixed-up shelf and the four-spine item are fiction spines put in order by the author's
letters (the continuum's fiction arrangement); one nonfiction lookup keeps the number. No classification system is
named on any student, teacher or family page (its name is a trademark); pages say "call number". The frame's unit 2
cell and candidate line want the same words; that is the frame's fix, filed by the caller.

**Confidence.** Firm (the classification's own summaries, below; continuum cell as the frame reports it).

### 2. The Shorter path does not hold: both fold-ins land on full inquiry days (serious; LAYER sequence; REPEAT yes)

**What is wrong.** (a) Fold-in 1 puts a five-minute lookup and shelf warm-up "in place of a retrieval" on day 10, and
fold-in 2 puts a five-minute sort and maker warm-up "in place of a retrieval" on day 18. Neither day has a retrieval
opening: day 10 runs lookup, shelf, page, fact, credit line, put-back, share and self-check in 19 minutes, and day 18
runs two sources into boxes, the differing fact, a third source, makers, credit lines, share and self-check. "20
minutes saved (25 freed, 5 used)" counts the freed session, not the receiving day, which goes to 24 minutes. The
stop-rule pictures moved to day 9's opening make that opening about 7 minutes. (b) The 20-minute session keeps
"assessment days drop nothing" with the longest at 17 minutes, but 20 minutes less 2 at each end is 16; the path does
not say what teaching days without an opening (4, 10, 18, 22 to 24) shed.

**Why it matters.** C2. A teacher who loses two library sessions follows this path and runs two inquiry days that
cannot finish, the same kind of fault as grade 1 finding 1.

**Fix (no day added; settled below).**
- Fold-in 1: day 10's partner share and self-check move to day 12, which already opens with those shares and the
  self-check; the freed 5 minutes hold the lookup and four-spine warm-up. The stop pictures go into day 9's opening,
  with the grade 1 source line said inside the show-me (finding 6), so day 9's pair tries run 6 minutes on this path.
- Fold-in 2: day 18's box-mat share and self-check move to day 20, which already holds them; the freed minutes hold
  one card sorted and one invented page's maker and purpose.
- 20-minute session: inquiry days 4, 10, 18 and 23 move their share to the unit's respond day; day 22 runs as in
  finding 4 with the member round cut to 1 minute. Check days: day 19's fact cards come pre-cut (about 15 minutes);
  day 25's sheet item is the seated task while stations run (about 15); day 27 reads each item once (about 16, with
  finding 3's items). Days 5, 11 and 13 fit as written (15, 15, 14).

**Confidence.** Firm (the scope's own minute budgets).

### 3. Five assessment items ask only part of the id they claim (moderate; LAYER sequence; REPEAT yes)

**What is wrong.**
- AASL.VI.B.2, owned ("Name who made each work you use and respect their rights"): days 11 and 27 ask only the credit
  line. The rights half is said on day 9 and never asked.
- ~AASL.IV.B.1 ("Search more than one kind of source, not just the first site"): days 11 and 27 ask one catalog lookup,
  one kind of source. Grade 1 finding 3 is the same fault.
- ~AASL.IV.B.4 ("Sort notes by ... another plan you can explain"): day 19 glues cards into boxes; the row's "saying why
  a card belongs" is not asked. Day 27 the same.
- ~AASL.III.D.1 ("Speak up with ideas and findings when a research group talks") and ~AASL.II.D.2 ("Ask others how they
  see a topic and show you want to know"): day 25's station has the group plan two questions together, so one or two
  children speak and nobody asks anyone.

**Why it matters.** The unit plan writer copies these rows; each becomes an item that marks a child on half an id.

**Fix (settled below).**
- Day 11: add a pointing item, two pictured children (one copies a book's sentence as their own, one writes the fact
  with a credit line), "point at the one who respects the maker" (about 1 minute); and after the catalog item,
  "if this book does not answer it, circle one other kind of source to try" from unit 1's pictures (about 1 minute).
  About 15 minutes. Day 10's inquiry ends with the pair pointing at one other source-kind card for its question.
- Day 19: for one glued card the child writes or says (scribe) "It goes here because ___" (about 2 minutes; 17 in all).
- Day 25: each child at the station asks the teacher, standing in as the person, one question (two from the group's
  plan, the third child's a follow-up, "Can you tell us more about ___?"), about 15 seconds each, then each names what
  one member added (about 10 seconds each): about 1.5 minutes a group, 15 for ten groups; the sheet item is held to 3
  minutes; about 18 in all.
- Day 27: credit line with the respect pointing item (about 4 minutes); three fact cards sorted with one "because"
  (about 4); ~AASL.IV.B.1 drops from day 27's codes (the catalog item stays as g2-catalog-lookup evidence, and the
  .md's "not sampled" list names IV.B.1 as asked in full on day 11); about 18 minutes.

**Confidence.** Firm (words file against the day rows).

### 4. Unit 4's interview and poster days are over-full, and the card goes before any try (moderate; LAYER sequence; REPEAT new)

**What is wrong.** Day 22 holds a 5-minute retrieval, ten groups finishing two questions, the teacher checking ten
question frames, a visiting staff member answering each group in turn with a follow-up, and a member-added round, in
19 minutes; ten groups at even a minute each fills the day alone. No day says what happens when no staff member can
come to a 25-minute specials slot, though the stand-alone question ("How do people at our school care for its
plants?") needs one. Day 23 holds two retrievals (class book page, and star and wish), a book fact found, a sort and a
whole poster drafted with picture and credit lines in about 14 minutes; the star and wish belongs before day 24's
feedback, not before drafting. The skill card is withdrawn on day 22, the first try of the questions move and before
the poster is drafted, so unit 4 has no practice with the card (C7).

**Fix (no day added; settled below).** Day 22: retrieval 3 minutes; groups finish their two questions 4 minutes while
the teacher checks each frame in passing; a whole-class interview, each group asking one question and one follow-up,
about 50 seconds a group (8 minutes); the member-added round 3 minutes. If no staff member can visit, the teacher reads
Curio Class's written first-person answer card as "our school's gardener" (APPROACH.md Sensitive ground item 8 allows a
first-person source set). Day 23: the class book retrieval only (2 minutes); the star and wish moves to day 24's
opening as a one-minute frame before the say-back. The card is held on days 22 and 23 and withdrawn on day 24.

**Confidence.** Likely (minute arithmetic; classroom practice from memory).

### 5. The stand-alone inquiry repeats the show-me case in units 2 and 3 (moderate; LAYER sequence; REPEAT yes)

**What is wrong.** Day 7 the teacher looks up and shelves "a fossil book the class needs"; day 10 pairs "look up the
fossil book", the same book. Days 15 and 16 the teacher sorts the turtle facts, finds the two that differ and decides to
check; day 18's stand-alone question is "How long does a turtle live?" with the same read-aloud. On the stand-alone path
the inquiry redoes what the teacher just did (kindergarten finding 1 is the same kind).

**Fix.** Unit 2: the printed catalog holds 6 to 8 fossil and earth books; day 7's teacher finds one title, day 10 gives
each pair a different title or author. Unit 3: the turtle books stay the show-me case; day 18's stand-alone becomes "How
tall does a sunflower grow?" with two passages and a third (plant facts, beside the science host). Change the .md unit 3
host line to match.

**Confidence.** Firm.

### 6. The owned ids get less practice than the "with help" rows (moderate; LAYER sequence; REPEAT new)

**What is wrong.** Unit 1: g2-question-to-research (with help) has days 1, 2 and part of 4; AASL.IV.A.2 (owned) has a
show-me and 6 minutes of pair tries on day 3, one use on day 4, then the alone check with a written "because" on day 5.
Unit 2 is the same: g2-catalog-lookup has days 7, 8 and part of 10; AASL.VI.B.2 has 6 minutes of pair tries on day 9.
The frame's own practice examples are "match three questions to source kinds" and "write credit lines for three covers".

**Fix (settled below).** Day 3: the story-or-information retrieval becomes the show-me's first case (children say
"story or information, and why", about 2 minutes); the pair tries run 9 minutes on three new questions and two more.
Day 9: the children say the grade 1 source line as the show-me's start (about 2 minutes); the pair tries run 9 minutes
on three covers. The retrieves column keeps both rows.

**Confidence.** Likely.

### 7. Day 16 teaches the maker before retrieving the author (minor; LAYER sequence; REPEAT new)

**What is wrong.** Day 16 opens with the find-the-page retrieval, then teaches two moves (the facts that differ and a
third source; the maker and purpose of five sources) and the online candidate in about 14 minutes. The author and
credit line, which the maker question builds on, come back only on day 17, after the maker is taught.

**Fix (settled below).** Day 16's retrieval becomes a credit line said for the two turtle covers (3 minutes,
g2-credit-line), which leads into "who made it"; the teacher finds the differing pages herself. Day 17's opening
becomes finding the answering page by its heading in the two passages (g1-find-in-a-book), the first practice round.
Swap the two `retrieves` cells and the .md retrieval paragraph.

**Confidence.** Likely.

### 8. Day 4's questions may not be answerable from the closed set (minor; LAYER sequence; REPEAT yes)

**What is wrong.** Pairs "take a question from the board", which holds thirty children's wonders; the frog set (a
read-aloud, a dictionary page, a map, a magazine page) cannot answer most of them. On the host path no source set is
named for map or water questions. Grade 1 finding 4 is the same kind.

**Fix.** Day 4: the teacher stars 6 to 8 board questions the set answers (from day 2's sort, children's own where they
fit) and pairs pick a starred one. On a host day the set is the host course's pages for that day, named by the unit plan.

**Confidence.** Likely.

### 9. With unit 1 left out, the mid-year check has nothing to sample (minor; LAYER sequence; REPEAT yes)

**Fix.** Add to the leave-out bullet: with unit 1 left out, day 13 samples unit 2 on new cases in forms not given on day
11 (a catalog entry with a second-kind circle and the respect pointing item, about 10 minutes), and the .md says so.

**Confidence.** Firm.

### 10. Small fixes (minor; LAYER sequence; REPEAT yes)

- Day 5's new picture is "an owl in a tree", but day 2 practiced on "an owl in snow". Use a new animal (a spider on its
  web).
- The turtle books: the third source must explain why the two differ (different kinds of turtle live different
  lengths), so the lesson is "check, and see why", not "one book was wrong"; every figure must be true of a named kind,
  checked at the days' accuracy read. The same holds for sunflower heights (finding 5).
- The .md gives ela:e2-wh-questions as weeks 1 to 9; ELA's days place it on days 1 to 77 (weeks 1 to 16). It is in
  step either way; correct the weeks.

## Checked and right (do not touch)

- Calendar: `school_day` = 5n puts day n in week n; units in weeks 1 to 6, 7 to 12, 15 to 20, 21 to 26; checks in
  weeks 13 and 27 as CALENDAR.md's table gives; library is a special outside rule 1; neither week holds a grade 2 core
  check (14 to 16, 18 to 20, 28, 29, 31, 32).
- Hosts in step on the other courses' days: social studies map parts (weeks 1 to 5) and science water (2 to 4) for day
  4; ELA text features (ELA days 47 to 58, weeks 10 to 12) for day 10, inside ELA's fossil unit; science plant needs
  (16 to 19) for day 18; ELA research (weeks 18 to 24) and science seeds and pollinators (23 to 25) for day 23. Leans
  before unit 3 are right (source maker weeks 2 to 8; author purpose weeks 10 to 12). The scope's For the lead item 1 is
  right: two accounts is taught in weeks 22 to 23, not 18 to 23, and day 16 carries the bridge.
- Retrieval: every assumed row is a grade 1 row (checked against `assumes`), so no readiness check is owed; none sits on
  a unit's first day.
- Owned codes on days 3 to 5, 13, 27 (IV.A.2) and 9 to 11, 18, 23, 27 (VI.B.2); no id outside the frame's rows; every
  carried id marked `~`. Checks draw on earlier units and say so; unit 2's and unit 4's results carried as class counts.
- Candidates all settled at zero added days. Sensitive ground items 1 to 5 and 8 on the right days, in the frame's
  words; neutral K to 5 cases; no product named; the family interview optional; the social studies family-interview
  unit kept apart.
- Lens checklist (scope and sequence layer): host task named, met; source judging as a page checklist, not present
  (the "check a third source" seed and makers on invented paper pages, lateral reading left to grade 5); citation with
  research to cite, met; end-of-unit assessment as recall of terms, not present; AASL text copied or alignment
  claimed, not present; live web page without capture, not present (paper pages only); paid database or library, none
  (the class book corner); claim of effect, none. Bar part 11 items 1, 2, 4, 5, 6 met; item 3 not applicable at grade 2.

## What I could not judge

- The read-alouds, passages, catalog cards and invented pages are not written yet, so their facts and voices (C12) wait
  for the days' accuracy and sensitivity reads.
- The NetSmartz K to 2 presentation itself was not opened (the grade 1 read opened its listing today); nothing here
  rests on it.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Call labels: subject by number, author letters below; fiction spines by letters; skill card "find the number, then the letters"; no system name | The form school libraries use | days.csv days 7, 8, 11; .md unit 2 |
| Fold-ins land by moving days 10 and 18 shares and self-checks to days 12 and 20; stop pictures in day 9's opening | Receiving days must hold 19 minutes | .md Shorter path |
| 20-minute path: shares to respond days; day 19 pre-cut cards; day 25 sheet as seated task; day 27 read once | Fits 16 working minutes | .md Shorter path |
| Day 11 adds respect pointing item and a second-kind circle (15 minutes); day 10 ends with one other kind named | VI.B.2 and IV.B.1 asked in full | days.csv days 10, 11; .md unit 2 |
| Day 19 one "because" for a card (17 minutes) | IV.B.4 asks a plan one can explain | days.csv day 19; .md unit 3 |
| Day 25 station: each child asks the teacher-as-person, names what one member added; sheet 3 minutes (18) | III.D.1 and II.D.2 for every child | days.csv day 25; .md unit 4 |
| Day 27: respect item, three cards with a "because", ~AASL.IV.B.1 dropped from codes (18 minutes) | Whole ids inside 19 minutes | days.csv day 27; .md checks |
| Day 22 whole-class interview timing; written answer card when no visitor | Fits 19 minutes; a path with no visitor | days.csv day 22; .md unit 4 |
| Day 23 one retrieval; star and wish to day 24's opening; unit 4 card withdrawn day 24 | Load and C7 | days.csv days 21 to 24; .md skill card line |
| Day 10 pairs look up different titles; day 18 stand-alone "How tall does a sunflower grow?" | Inquiry not a rerun of the show-me | days.csv days 7, 10, 18; .md units 2, 3 |
| Days 3 and 9: retrieval folded into the show-me, pair tries 9 minutes | More practice of the owned ids | days.csv days 3, 9 |
| Day 16 retrieves the credit line, day 17 the find-the-page | Author before maker | days.csv days 16, 17; .md retrieval paragraph |
| Day 4 starred answerable questions; host source set named by the unit plan | Every pair can find a fact | days.csv day 4 |
| Unit 1 leave-out: day 13 samples unit 2 | Leave-out rule | .md Leave-out |
| Day 5 picture a spider on its web; third source explains the turtle and sunflower differences; e2-wh-questions weeks 1 to 16 | New case; accuracy; data | days.csv day 5, 16, 18; .md unit 1 |

## For Cory

Nothing. Every finding is item-level or a day fix inside the frame. The frame's unit 2 wording on "subject letters"
(finding 1) needs the same correction in the frame; that is the lead's to file.

## For the source list

- Dewey Decimal Classification summaries (OCLC), https://www.oclc.org/content/dam/oclc/dewey/resources/summaries/deweysummaries.pdf:
  opened 2026-11-26, read as text with pymupdf; second summary gives 560 Fossils and prehistoric life, 580 Plants, 590
  Animals, 597 Cold-blooded vertebrates. The summaries page https://www.oclc.org/en/dewey/resources/summaries.html
  says the system is number-based. The system's name is a trademark: teacher and student pages say "call number".

## Sources

- OCLC Dewey summaries (above): subject by number, finding 1.
- data/progressions/library.csv, data/standards/aasl-words.txt, data/plans/calendar.csv and the grade 2 ELA, science and
  social studies days.csv: ids, assumes, weeks.
- From memory: classroom timing of interviews and stations (finding 4); turtle lifespans varying by kind (finding 10).
