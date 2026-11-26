# Expert read: scope and sequence, Library and Research Skills, grades 6 to 8 (2026-11-26)

Course `library-and-research-skills-grades-6-to-8`. I read it cold, as a middle school librarian and research
teacher, a district adoption reader and a researcher, following docs/pipeline/briefs/sequence-read.md and
build/scope-writes/AFTERCORE-READ.md. A fresh Claude agent wrote the scope. This read changes no file except this
report.

## What I read

- docs/courses/library-and-research-skills-grades-6-to-8/scope-and-sequence.md and
  data/plans/library-and-research-skills-grades-6-to-8/days.csv (all 54 rows), in full.
- The frame docs/courses/library-and-research-skills-grades-6-to-8/frame.md, in full.
- data/progressions/library.csv, every grade 6, 7 and 8 row, and data/standards/aasl-words.txt for the 28 ids the
  days name.
- docs/agents/EXPERT.md, docs/agents/lenses/library.md, docs/ADOPTION-BAR-SUBJECTS.md part 11,
  docs/courses/library/STANDARD.md and APPROACH.md, and build/scope-writes/AFTERCORE-BRIEF.md.
- docs/courses/CALENDAR.md (rule 3, target weeks and the end table) and the grade 6, 7 and 8 check and host-unit
  rows of data/plans/calendar.csv.
- The SEL STANDARD "Shared steps" bullet (section 7), civics days 131 to 138 (the ss8-news-literacy unit) and the
  school_day convention of the other 6 to 8 band courses (health, SEL, PE, visual arts).
- For the REPEAT tags: the grade 5 library sequence read and the list of 2026-11-26 sequence reads that raised
  leave-out bridges (grade 1 library, health K to 2 and 3 to 5, SEL, PE K to 2).
- Outside: the Civic Online Reasoning Creative Commons page (https://cor.inquirygroup.org/creative-commons/), opened
  2026-11-26. It confirms the frame's split: the parallel assessments and most lessons, including the intro and
  lateral reading lessons, are CC BY 4.0, while the curricular assessments, four history lessons and the
  professional learning sessions are CC BY-NC-ND 4.0. The terms-of-use address I tried first returned 404.

**Gates.**
- `scripts/plan.py check`: this course passes. The failures it prints are other courses' (algebra-ii and others).
- `scripts/sequence.py check library-and-research-skills-grades-6-to-8`: 0 failures, one note, "unit 4: standard
  None is on no day". It comes from the frame's literal "None" (the same artifact as the grade 5 read).
- `scripts/frame.py check`: 0 failures. It notes, unit by unit, that the begun codes should be named in What
  students learn. The frame already names each one with its later owner, so there is nothing to change.
- `scripts/frame.py calendar`: no break for grades 6 to 8.
- `scripts/stale.py check`: 0 failures.

**Checked by hand.**
- school_day follows the formula `160y + ceil(160k / 18)` on all 54 rows, and the band-cumulative convention
  matches the other 6 to 8 band courses.
- The weeks are 2, 4, 6, 8, 9, 11, 13, 15, 16, 18, 20, 22, 24, 25, 27, 29, 31 and 32 in every year.
- Every unit falls inside the frame's weeks.
- Checks fall on weeks 20/31, 18/31 and 16/31, as CALENDAR.md's end table gives them.
- Rule 3 holds: no other grade 6, 7 or 8 mid-year check falls on school day 98, 89 or 80. The nearest are grade 8
  SEL on day 78 and grade 7 computer science on days 78 to 80, which is the other grade.
- Every host unit's weeks in calendar.csv match what the days claim: in step for units 1, 2, 3, 5, 6 (days 33 and
  34), 8 and 9, and not in step for units 4 and 7, as the scope says.

## Verdict

The scope is sound and teachable.
- It runs nine full inquiry cycles on paper with invented pages.
- It teaches lateral reading as leaving the page, never as a checklist on the page.
- It names a real host and a stand-alone question for every unit, honestly checked against calendar.csv.
- It keeps every owned id on teaching days and on a scored task.

The biggest risk is in the reduced paths. The 35-minute period and two of the fold-ins do not hold as written. One
grade 8 fold-in drops the day on which the two assessed change lines are written. The leave-out bridges cover four
units of nine.

The change that matters most for the unit writers is in the assessment rows. Unit 2's end-of-unit assessment (day
11) never asks the going-upstream step or the three parts of VI.A.3. Unit 7's sitting drops the "how my first view
shaped what I looked for" line that day 37 teaches. Day 27's scored discussion cannot be heard by one teacher as
written.

## Findings, most serious first

### 1. The reduced paths do not hold as written (serious; LAYER sequence; REPEAT yes, the grade 5 finding 1 kind)

**What is wrong.**
- (a) **A shorter period (35 minutes).** The path says the sittings and checks "drop that day's opening five
  minutes" and "nothing is cut". The sittings have no opening five minutes to drop:
  - Day 5 is a 30-minute sitting plus a 10-minute readiness check (40 of 40).
  - Day 28 is 30 + 8 (38), and day 45 is 30 + 8 (38).
  - The show-me days run a hook or retrieval, a think-aloud, practice and an exit ticket in 40 minutes. The path
    says nothing about where their 5 minutes go.
- (b) **Grade 8 fold-in, day 52 into day 51.**
  - Day 52 is where each student writes the two change lines (II.B.1, III.B.2), and day 53 scores those lines. The
    fold moves only the share, so the assessed lines lose their home.
  - The fold is conditional ("where the audience can come then"), and it takes 15 minutes from day 51's revision
    after teacher feedback.
- (c) **Grade 7 "fold".** Day 21's self-check into day 22 "the day stays", so it saves no session. The total of
  "five sessions folded ... 150 minutes" counts it. Grade 7 has one real fold, which is enough for a year 10 school
  days short at this dose, but the arithmetic should say so.

**Why it matters.** Bar C2 and the brief ask for a reduced path with nothing assessed or owned cut. A writer
following (a) would overrun three sittings. A writer following (b) would leave check 6 scoring lines nobody wrote.

**Fix (settled below).**
- (a) Add three lines to "A shorter period":
  - Day 5 drops its one-answer items (about 5 minutes; the rubric parts stay).
  - Days 28 and 45 cut their earlier-unit sample to one item (about 5 minutes).
  - On show-me days the practice half gives one fewer try (5 minutes); the think-aloud and exit ticket stay.
- (b) Drop the day 52 fold. Grade 8 keeps the day 44 fold, one session, which is enough.
- (c) Restate the total: four sessions folded (two in grade 6, one each in grades 7 and 8), about 115 minutes. Day
  21's self-check move is listed as an optional trim, not a fold.

**Confidence.** Firm (the scope's own minute budgets).

### 2. The leave-out bridges cover four of nine units (moderate; LAYER sequence; REPEAT yes)

**What is wrong.** "A left-out unit" names bridges only for units 2, 5, 6 and 7, and the unit 5 bridge is
incomplete. Later units retrieve or use cards from:
- **Unit 1:** day 20 retrieves g6-search-strategy; day 25 retrieves g6-keep-questioning and g6-quote-paraphrase.
- **Unit 3:** day 32 retrieves g6-team-product and g6-make-and-improve.
- **Unit 4:** day 38 retrieves g7-search-results; day 48 retrieves g7-lateral-hard-cases.
- **Unit 5:** besides unit 8, day 31 retrieves g7-citation-style, and days 38 and 39 retrieve g7-sources-disagree
  and g7-evidence-discussion.
- **Unit 8:** unit 9's product uses images, and day 53 samples a fair use case.

The path also does not say what a course-level check does when it is the left-out unit's end-of-unit assessment
(units 2, 3, 5, 6, 8 and 9), or when it samples a left-out unit.

**Why it matters.** STANDARD.md section 4 lets a school leave out any unit. Without a bridge, the retrieval task on
the next unit's day 2 asks for a move the class never met. A check that samples the unit would then score students
on it.

**Fix (settled below).**
- Add one bridge line per unit whose card is used later:
  - Unit 1 left out: day 20 opens with the search plan's one-step form, and day 25 with the quote-or-paraphrase card.
  - Unit 3 left out: day 32 teaches "mark who added what, log each change".
  - Unit 4 left out: day 38 teaches "filter, pick three", and day 48 "check the photo, the number, the maker".
  - Unit 5 left out: day 31 also teaches the works-cited model, and day 38 "table the claims".
  - Unit 8 left out: day 52's product uses only invented or public domain images, and day 53 drops its fair use
    item.
- Add one rule line: a check that is a left-out unit's end-of-unit assessment keeps only its earlier-unit samples,
  and any check drops the items that sample a left-out unit. In both cases the family note names the ids not
  claimed.
- Each bridge takes the first ten minutes and claims none of the left-out ids, as the scope's rule already says.

**Confidence.** Firm.

### 3. Assessment rows that do not ask the whole of what the unit teaches or the code claims (moderate; LAYER sequence; REPEAT yes, the grade 5 finding 2 kind)

**What is wrong.**
- **Day 11 (unit 2's end-of-unit assessment).** VI.A.3 is "accurate, fair in its context and fit for the task", and
  unit 2's method includes going upstream (days 6, 7 and 9). Day 11 asks for "a lateral check with a verdict and
  reason", one prompt for three parts, and no upstream step. Upstream appears first in day 17's year-end sample,
  which is not unit 2's assessment.
- **Day 40 (unit 7's sitting).** Day 37 teaches, and the row note and the frame's What students learn require, a
  line on how one's own first view shaped what one looked for. Neither day 39's log nor day 40's sitting asks it.
- **Day 53.** It claims AASL.IV.B.2 ("Gather information from sources that see the question in different ways")
  through "a views search plan". A plan gathers nothing.
- **Day 45.** It samples V.A.2 as "an expectation and an honest update" with no marking of which findings test the
  expectation, the "test" half of the id.

**Why it matters.** The unit plan writer copies these rows into items. As written, unit 2 is certified on VI.A.3
without its upstream step or its "fair in context" and "fit for the task" parts, and V.A.2's taught first-view line
is never scored.

**Fix (settled below).**
- Day 11: the lateral item gets three prompts (what was found upstream, so is it accurate; is it fair in its
  context; is it fit for this task), with no minutes added. It is the same page, with three lines in place of one
  verdict.
- Day 40: the sitting's update adds "one line on how what I expected shaped what I looked for" (about 2 minutes),
  and day 39's log adds the same line.
- Day 53: the views sample becomes "a views plan and, from a given short set, one finding for each view" (inside
  the 15 minutes).
- Day 45: the unit 7 sample adds "mark which of four findings test the expectation".

**Confidence.** Firm (aasl-words.txt and the row notes).

### 4. Day 27's scored discussion cannot be heard by one teacher as written, and its only practice is a fishbowl (moderate; LAYER sequence; REPEAT new)

**What is wrong.**
- Day 27 scores II.C.1 from "each student's sourced contributions marked on the record sheet", in groups of five.
  With 30 students that is six discussions at once in about 30 working minutes, so one teacher cannot hear and mark
  every student.
- The only practice is day 25's fishbowl, where only the inner circle speaks. The outer circle's first sourced turn
  is the scored one. The frame's rule, "no score comes from a day a move is first shown", is met by the letter but
  not in practice for half the class.

**Why it matters.** II.C.1 is owned here and checked nowhere else. A score the teacher could not hear is a guess,
and a student marked on a first try is marked on the show-me.

**Fix (settled below).**
- Day 25: the fishbowl rotates. The outer circle takes the inner seats for the second half, so every student makes
  one sourced claim and one "where did that come from?" challenge before day 27. No minutes are added; the citation
  practice stays at 10 minutes.
- Day 27: the record sheet scores two things per student, at least one claim pointed to its source and one source
  challenge. The teacher sits with each group for about five minutes in turn. Each student also hands in a turn slip
  naming the source behind their claim, so the teacher can mark a student not heard live from the slip. This is not
  self-marking: the slip is evidence the teacher judges.

**Confidence.** Likely (classroom arithmetic; APPROACH.md unit field 7 requires teacher judgment).

### 5. The skill card is withdrawn the same session the response log is first shown, and the last-shown move in each unit gets no practice with the card (minor; LAYER frame and sequence; REPEAT new)

**What is wrong.**
- Day 32 shows the response log in ten minutes and withdraws the card in the same session. The log is used on day
  33 without the card, never practiced with it. APPROACH.md section field 5 has the card held by pairs on the first
  practice day and withdrawn on the first inquiry day.
- At this dose, the same thing happens more softly to the move shown on the last show-me day before each inquiry.
  That move gets only an exit ticket before the card is gone:
  - day 2 (note cards) to day 3;
  - day 8 (the group-written article) to day 9;
  - day 38 (the views plan) to day 39;
  - day 42 (fair use) to day 43;
  - day 48 (the question sort) to day 49.

**Why it matters.** Students meet a new move cold on the inquiry day, and the unit plans would inherit the pattern.

**Fix (settled below).** Every inquiry day's note reads "card withdrawn for the moves already practiced; the line
for the move shown last session stays on a one-line strip for this session". On day 32 the response log line stays
on the strip through day 33's first half. The sittings stay without the card, so no assessment changes. For the
lead: the frame's unit 6 Days cell could say the same.

**Confidence.** Judgment call.

### 6. Day 47 says social studies opens with a retrieval task on library's news check, and it does not (minor; LAYER sequence and progression; REPEAT new)

**What is wrong.**
- Day 47's note and the .md's unit 9 Leans line say "social studies opens with a retrieval task on it".
- Civics days 131 to 144 (calendar weeks 27 to 29) teach their own lateral reading day (day 136) and name no library
  retrieval.
- They should not: lesson 32 says no core course assumes library. The g8-news-lateral row note has the same
  either-order line.

**Why it matters.** A teacher reading the library page expects the civics teacher to build on library's news days.
The civics plan cannot assume them.

**Fix (settled below).** Day 47 and the .md say "social studies teaches its own news check (civics unit 9, weeks 27
to 29); a class that has both meets the method twice, and day 51 and 52 share its weeks". For the lead: the
g8-news-lateral row note's "the second course opens with a retrieval task on the first" holds only when library
comes second. It could read "where library comes second, its day opens with a retrieval task".

**Confidence.** Firm (civics days.csv).

### 7. Accuracy points for the answer keys (minor; LAYER sequence; REPEAT new)

- **Day 43:** "period cartoons and photos are public domain and a modern image is not". The first half holds: works
  published in the United States before 1931 are in the public domain as of 2026. The second half is too broad,
  because a modern image may be openly licensed or a United States government work. That is exactly the safer path
  day 42 teaches. Write "a modern image is usually still under copyright, unless its license or maker says
  otherwise." (From memory on the 95-year term; firm on the logic.)
- **Day 9's knees case:** the evidence on weather and joint pain is mixed. A large 2017 study of doctor visits found
  no link with rain. A 2019 smartphone study found a small link with humidity and pressure. Both are from memory
  and marked so. The answer key should reward the lateral and upstream moves and record "evidence mixed", never
  "false". The animal sayings likewise vary saying by saying.
- **Day 11 note:** "its sitting was 13 weeks earlier". Day 5 is week 9 and day 11 is week 20, so 11 weeks.
- **.md, Course-level checks paragraph:** "sat on new cases 8 to 13 weeks after their sittings" holds for the
  mid-year checks only. The year-end checks sample units 1, 4 and 7 about 22 to 23 weeks later. Say "8 to 23 weeks".

**Confidence.** Firm on the arithmetic; likely on the copyright wording; judgment call on the knees key.

### 8. Small fixes (minor; LAYER sequence and process; REPEAT yes for the gate note)

- **For the lead item 3 (the "None" note):** the same artifact as grade 5. One gate fix covers both.
- **Day 47 "sets the team talk rules itself":** students have carried SEL's 6 to 8 talk turn card (SEL STANDARD
  section 7, with its added first step, choose how to talk) since grade 6. The note could say the team talk rules
  start from that card rather than new words, so students meet one set. This is not required for library, so it is
  a judgment call.
- **Teacher written feedback on days 15, 33 and 51:** written "in session" for six to eight teams while they work.
  The note could say "written between sessions and handed back at the start", since a session falls only every two
  weeks.

## What is right and should not be touched

- The paper path on every day, and the stop and privacy rules written out on every open-search day.
- Lateral reading taught by leaving the page, with a polished wrong page that fails and a plain right one that
  passes (day 6).
- Hosts checked week by week against calendar.csv. Units 4 and 7 honestly fall back to stand-alone questions, and
  For the lead item 1 asks only for frame wording.
- The sensitive-ground guards: natural hazards as preparing (unit 3), food as a system (unit 6), sleep with no
  personal questions (unit 7), the smallpox, Banneker and 1906 host notes, teams mixed by first answers only, and
  the viral video described, never shown.
- The candidate cells, each settled with its minutes or a reason. The one drop (copyright in safe use of technology)
  carries a reason and names computer science as owner.
- The checks sit on their target weeks, and rule 3 is checked by school day against calendar.csv.
- The unloaded-source days (6, 8, 20, 47 and 48, with item forms for 11, 22 and 53) are named, and they match the
  frame's Source map and the live license page.

## What I could not judge

- The Civic Online Reasoning lesson texts themselves (not loaded, later.csv L149). Whether days 6, 8, 20, 47 and 48
  fit those lessons' length waits on them.
- The continuum 6 to 8 band file cells (not reopened; the frame's L103 read is taken as given).
- Whether the partner-class exchange is workable in a real school's two-week gap between sessions. The fallback (a
  findings set left by an earlier class) covers it on paper.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Shorter period: day 5 drops its one-answer items; days 28 and 45 cut the earlier-unit sample to one item; show-me days give one fewer practice try | The 35-minute path must cost every day it shortens | scope-and-sequence.md |
| Drop the day 52 fold; grade 8 keeps the day 44 fold; total restated as four sessions, about 115 minutes; day 21's move listed as a trim | The change lines are assessed at day 53; one fold a year is enough | scope-and-sequence.md |
| Bridge lines for units 1, 3, 4 and 8, and the extended unit 5 bridge, plus the check rule for a left-out unit | Every later use of a left-out card needs its ten-minute form | scope-and-sequence.md |
| Day 11's lateral item asks three prompts (upstream and accurate, fair in context, fit for the task) | VI.A.3 in full, on unit 2's end-of-unit assessment | days.csv day 11; .md unit 2 |
| Day 39's log and day 40's update add the "how what I expected shaped what I looked for" line | V.A.2's taught part is scored | days.csv days 39, 40 |
| Day 53's views sample adds one finding per view from a short set; day 45's unit 7 sample adds marking four findings | IV.B.2 and V.A.2 asked whole | days.csv days 45, 53 |
| Day 25's fishbowl rotates; day 27 uses two marks per student, a five-minute teacher visit per group and a turn slip | Every student practices before the score, and the teacher can judge every student | days.csv days 25, 27; .md unit 5 |
| Inquiry days keep a one-line strip for the move shown last session; day 32's response log line stays through day 33's first half | A new move gets one session with its card | days.csv days 3, 9, 32, 33, 39, 43, 49 |
| Day 47 and the .md say social studies teaches its own news check | Civics days 131 to 144 assume no library row (lesson 32) | days.csv day 47; .md unit 9 |
| Day 43's wording on modern images; day 9's key records "evidence mixed"; day 11's "11 weeks"; the checks paragraph's "8 to 23 weeks" | Accuracy | days.csv days 9, 11, 43; .md |
| Teacher written feedback on days 15, 33 and 51 written between sessions | Practicable at one session every two weeks | days.csv days 15, 33, 51 |

## For the lead (not changes to this course's files)

- The frame's unit 6 Days cell: the card stays for the response log through day 4's first half (finding 5).
- The g8-news-lateral row note: its "the second course opens with a retrieval task" line holds only where library
  comes second (finding 6).
- The sequence.py "None" note (finding 8, also raised by the grade 5 read).

## For Cory

Nothing new. The tight days this read found are fixable inside the 18 sessions a year he kept, so the frame's
standing dose option (two more sessions a year, For the lead item 2) is not triggered by this read.

## For the source list

- https://cor.inquirygroup.org/creative-commons/ : the live license split for the Civic Online Reasoning items
  (CC BY 4.0 for the parallel assessments and most lessons; CC BY-NC-ND 4.0 for the curricular assessments, four
  history lessons and the professional learning sessions). Opened 2026-11-26. The /terms-of-use/ address returns 404.

## Sources

- data/plans/calendar.csv, civics-government-and-civic-life/days.csv: host weeks, rule 3 and the news unit.
- data/standards/aasl-words.txt and data/progressions/library.csv: the whole-id and row-part checks.
- Civic Online Reasoning Creative Commons page (above): the source map's license split.
- From memory, marked so: the United States 95-year copyright term for published works, and the 2017 and 2019
  weather and joint pain studies.

Finding count: 8 (1 serious, 3 moderate, 4 minor).
