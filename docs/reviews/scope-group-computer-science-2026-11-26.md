# Scope group read: computer science, K to 12 (2026-11-26)

Brief: build/scope-writes/GROUP-READ.md, group computer-science, 13 courses (computer-science-kindergarten and
computer-science-grade-1 to computer-science-grade-12). This read looks across the courses. It does not repeat what
the 13 single-course reads (docs/reviews/sequence-computer-science-*-2026-11-26.md) and their fix reports settled.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-read.md; build/scope-writes/CS-BRIEF.md.
- docs/agents/lenses/computer-science.md; docs/courses/computer-science/STANDARD.md and APPROACH.md;
  docs/ADOPTION-BAR-SUBJECTS.md section 5 and C1; data/progressions/computer-science.csv and computer-science-edges.md.
- All 13 scope-and-sequence.md files in full; each frame.md by search (Swap or leave out, device minutes, family
  note); all 13 days.csv files by script (scratch: build/scope-writes/scratch/group-computer-science/an.py): ownership
  of every id, progression rows by day, `retrieves` against each row's grade and last use, readiness placement,
  check-day openers, blank `codes`, begun ids, sensitive days, reading load.
- docs/courses/CALENDAR.md (rules 1 to 4 and the check table); DESK-ANSWERS.md, the 2026-11-26 entries "after-core
  frame calls", "after-core frame fix-pass rules", "computer science scope lead calls" and "after-core scope lead calls".

## Findings

### 1. The debugging routine is taught as new three years running, in three wordings

- **Grade 7 day 5** teaches a four-step routine ("predict, run, find the first line where the run differs from the
  trace, change one thing and rerun") and prints it on the day 7 build sheet.
- **Grade 8 day 14** calls its routine "first explicit teaching" and "the year's debugging routine". It has six steps,
  the lens's: predict, run, compare, find the first place it goes wrong, change one thing, test again. Days 17, 23 and
  49 use it by name.
- **Grade 9 day 6** retrieves "grade 8's debugging method" as four steps: predict, run, compare, first wrong line.
- Grade 6 day 5 retrieves grade 5's strategies (g5-systematic-debug, days 13 and 14), which are a different thing:
  ways to find a bug, not a routine.
- **Why it matters.** A student who takes grades 7 to 9 meets one method on three cards with three step lists. Grade
  8 re-teaches as new what grade 7 taught. Debugging is meant to be one method that comes back (lens, "Debugging is
  taught as a method").
- **Fix.** Use the lens's six steps word for word in every course from grade 6 to 12: on grade 7 day 5 (first
  taught), on grade 7 day 7's build sheet, on grade 8 day 14 (reworded as retrieval with the worked bug, plus first
  teaching for a student new to the elective) and on grade 9 day 6. Grade 6 day 5 names grade 5's strategies as tools
  that sit inside the "find the first place it goes wrong" step.
- **Tag: scope.**

### 2. The "add the missing examples, retest, compare" sorter lesson repeats in grades 3, 5 and 7, the same on paper

- **Grade 2 day 25:** an uneven training set gives uneven mistakes.
- **Grade 3 day 25:** the class is the sorter, with few side-view spiders. It is tested, given more examples, tested
  again, and right answers are tallied before and after.
- **Grade 4 day 26:** one property of the training set is changed and the result predicted.
- **Grade 5 days 22 and 23:** add the missing varied examples, retrain, compare counts before and after. Until the
  trainer exists (L148) this runs on paper, with a partner as the model.
- **Grade 7 days 36 to 38:** improve the training set and retest, also on paper until L148.
- The progression notes set much of this (g3-ml-new-data and g5-train-model both say "add examples, compare before and
  after"). The device was meant to be what is new in grade 5. With the device not built, grade 5 day 23 and grade 3
  day 25 are the same lesson, and no scope says what is new.
- **Why it matters.** This is a task form repeated with no reason named. A reviewer reads it as a spiral that does not
  climb, and students lose a session on a game they have already played.
- **Fix.** In grade 5, on days 22 and 23 and on the paper path, students build and split their own training and test
  sets and name the features the partner model may use. In grade 3 the teacher supplies the set. Grade 5 day 22's
  retrieval opener names grade 3 day 25 and says what is new. Grade 7 day 36's note says what grade 7 adds: accuracy as
  a percent, non-examples and misleading backgrounds.
- If the lead would rather fix it at the source, the g3-ml-new-data and g5-train-model notes are a progression change
  (structure). I pick the scope fix.
- **Tag: scope.**

### 3. The sensitivity read is named before case cards on some sensitive days and not on others

- **Days that name it:** grade 2 days 10 and 29, grade 3 days 10 and 24, grade 5 days 8 and 27, grade 6 day 43, grade
  7 days 28 and 49, grade 10 days 42 to 47, grade 11 day 52, grade 12 days 15 and 18.
- **Days with the same kind of content that do not name it:**
  - grade 4 day 28 (Mary Golda Ross of the Cherokee Nation, Annie Easley, Jerry Lawson: Native and Black history);
  - grade 6 days 58 and 59 (Dorothy Vaughan and segregation);
  - grade 7 days 39 to 41 (race, dialect and disability bias);
  - grade 8 days 7 to 10, 22 and 24 (disability needs as test conditions);
  - grade 9 day 31 (a distance rule that can stand in for income, disability);
  - grade 11 day 49 (disability bias);
  - grade 12 day 59 (race and gender barriers in Hopper's and Johnson's accounts).
- **Why it matters.** APPROACH.md "Sensitive ground" and FOUNDATION section 7 send every unit with cultural, Native or
  disability content to the sensitivity agent before it goes live. A unit writer working from a day row that does not
  name the read will skip it. Grade 4 day 28 is Native content with no read named.
- **Fix.** Add "sensitivity read before the case cards (docs/pipeline/briefs/sensitivity-read.md)" to each day listed,
  and to the Sensitivity line of that unit in each scope.
- **Tag: scope.**

### 4. Begun and used-again ids are kept in the `codes` column in grades 9 and 11, but only in notes in 6, 7, 8 and 10

- **Grades 9 and 11** write `~ID` in `codes` (10 ids), as the 2026-11-26 after-core lead call sets ("Begun ids are
  written ~ID in the codes column").
- **Grades 6, 7, 8 and 10** leave `codes` blank on teaching days whose progression row carries a `~ID`, with the id
  in the note only:
  - grade 6 days 30 and 50;
  - grade 7 days 11 to 13, 23 and 51;
  - grade 8 days 1, 2, 6, 13 to 17, 20, 21, 56 and 60;
  - grade 10 days 38, 39, 52 and 57.
- **Grade 8 day 61** (the year look-back) has neither a skill nor a code. The grade 8 scope's C1 paragraph says "No
  other day falls outside the standards", which does not match.
- **Why it matters.** The C1 share (under 10 percent outside the standards) cannot be counted from the CSV the same way
  in every course. A gate that counts blank `codes` would put grade 8 at 13 of 52 teaching days. Grades 7 and 8 also
  count their list days as outside the standards, while their progression rows tie those days to ~MS-PRO-VD-16 and
  ~MS-ALG-PS-01.
- **Fix.**
  - Write each such day's progression `~ID` into `codes` in grades 6, 7, 8 and 10.
  - Grade 8 day 61: give it a skill and a code, or count it under C1 (about 5 of 52 with the list days, still under
    10 percent).
  - Grades 7 and 8: state once whether the list days count as outside the standards (the C1 paragraph) or as `~ID`
    days, not both.
- **Tag: scope.**

### 5. "A year about 10 days short" means two different things in 6 to 12

- **K to 5 and grade 7** read it as 10 school days, two weeks: 2 sessions in K to 5, 4 sessions in grade 7.
- **Grades 6, 8, 9, 10, 11 and 12** fold 10 course days, which at two a week is five weeks and about 16 percent of
  the year. Grade 6, for one, folds its first editor session (day 2).
- **Why it matters.** CALENDAR.md counts in school days. A teacher who loses two weeks in grade 8 meets a plan for
  five. Ten folds also squeeze practice that the single-course reads protected (modify days, worked examples).
- **Fix.** In each grade 6 and 8 to 12 scope, mark the four folds that save the least as the "10 school days" path,
  and keep the other six as a named spare list for a year shorter still. This is the form grade 7's fifth fold and
  the kindergarten spare already take.
- **Tag: scope.**

### 6. The shorter year folds respond days in grades 4 and 5, which K, 2 and 3 forbid; check weeks move in grade 3 only

- **K** says "Never folded: any check or respond day". **Grade 2** says "A school that loses more drops no respond
  day", and that a lost week moves teaching days, "never the check". **Grade 3** says respond and check days are never
  folded.
- **Grade 4** folds respond day 6. **Grade 5** folds respond days 5 and 10.
- **Grade 3** says that with both folds its checks move to weeks 10 and 24. Every other course keeps its check weeks.
- **Why it matters.** The same specials teacher often teaches K to 5. One rule, worded differently every year, reads as
  a different rule each time.
- **Fix, my pick.** A respond day after an end-of-unit sitting may fold into the next day's opener with a self-check,
  as grade 5 writes it. A respond day after a course-level check never folds. Check days keep their weeks (grade 2's
  wording). Edit the shorter-path lines of K and grades 1 to 3 to state that rule, and grade 3's line on weeks 10 and
  24 to keep the checks in weeks 11 and 26. The rule belongs once in APPROACH.md "Pacing" (the lead's file).
- **Tag: scope.**

### 7. Whether a check sitting opens with a retrieval task differs by grade

- **Retrieval filled on check days:** K (days 5, 12, 21, 27, 31), grade 2 (all five), grade 3 (days 5, 20 and 31 but
  not 11 and 26) and grade 4 (all five), plus grade 8 days 27 and 63.
- **No retrieval on check days:** grade 1 (its scope says so), grade 5, and grades 6 to 12 otherwise.
- Grade 1's For the lead 4 already asks for an APPROACH.md line.
- **Why it matters.** APPROACH "How a day opens" says every day opens with one of three openers. No scope or APPROACH
  line settles check days, and grade 3 differs inside one year.
- **Fix, my pick.** Use grade 1's rule: a check sitting opens with settling and instructions, not a retrieval task.
  Kindergarten's spoken "what is this tool's job" warm-up stays as instructions, not scored. Clear `retrieves` on the
  check days of K, grade 2, grade 3 (days 5, 20, 31), grade 4 and grade 8 (days 27, 63), and give the minutes to the
  sitting. The APPROACH line is the lead's.
- **Tag: scope.**

### 8. Who sits the elective readiness check differs in 7 to 12, and grade 10 counts one row as two grades back

- **Grade 9** has every student sit the readiness items, because "a teacher cannot always tell who took grade 8".
- **Grade 8** has the readiness check serve as "a second retrieval" for those who took grade 7.
- **Grades 7, 10, 11 and 12** give it "for a student who did not take" the year before. They do not say what the
  others do during those ten minutes.
- **Grade 10 day 20** gives g8-network-failure as "readiness for every student, two grades back". Grade 9 day 49
  retrieves that row, so it was last used the year before (rule 2 counts last use).
- **Why it matters.** Ten minutes a unit, six times a year, are either the whole class's or half the class's. A
  teacher cannot plan the room from these lines.
- **Fix.**
  - Use grade 9's wording in grades 7, 8, 10, 11 and 12: every student sits the items. For a student who took the
    year before they are the year-before retrieval, and the teacher reads them to find who needs the worked example.
  - Grade 10: move g8-network-failure to the year-before list (retrieval for grade 9 takers, readiness for the rest).
- **Tag: scope.**

### 9. Units a school may leave out are named in the frames of grades 1, 7 and 12 but not in their scopes, and one seam is missing

- **Scopes that carry the frame's leave-out with its day changes:** kindergarten (unit 5), grade 3 (unit 5), grade 6
  (unit 4, with day 63's swap items) and grade 8 (unit 5).
- **Frames that allow a leave-out the scope does not carry:**
  - Grade 1 lets unit 5 be left out (frame lines 131 to 133).
  - Grade 7 lets unit 4 be left out. Its frame says what day 60 and grade 8 then do (frame lines 143 to 146).
  - Grade 12 lets unit 5 be left out (frame lines 183 to 187).
- **Missing seam.** Grade 8's frame (line 60) says g8-ml-evaluate, g8-modify-for-bias and g8-ai-tool-day open with a
  bridge where grade 7's unit 4 was left out. Grade 8's scope readiness table (day 41) does not say so. Grade 7's
  scope does say its day 33 covers a class whose school left out grade 6's unit 4.
- **Why it matters.** STANDARD.md section 3 requires the course page to name the ids not claimed when a unit is left
  out. A school that leaves out grade 7 unit 4 gets no plan for grade 7 day 60 or grade 8 day 41.
- **Fix.**
  - Add a "Swap or leave out" line to the grade 1, 7 and 12 scopes: the unit, the ids not claimed, what replaces its
    check items, and that the calendar does not move (the grade 6 form).
  - Grade 7: name day 60's retrieval of grade 6's training set as the bridge.
  - Grade 8: add the left-out grade 7 unit 4 case to day 41's readiness line.
- **Tag: scope.**

### 10. Days on data about people carry health's steps in grades 6, 7 and 12 but not in 9 and 11

- **Days that carry the steps:** grade 6 day 30, grade 7 days 26 to 30 and grade 12 days 18 to 21 put health's "If a
  student tells you something" steps on personal-data days.
- **Days that do not:**
  - Grade 9 day 41 (fare-card trip records, immigrant families who worry about being tracked).
  - Grade 11 day 51 (large-scale collection from applicant data), and days 49 to 52 more widely.
- **Why it matters.** APPROACH lists personal data (HS-DAT-IM-27) as sensitive ground. Grade 9 day 41 is the most
  likely day of the year for a disclosure about a family's status.
- **Fix.** Add the steps line to grade 9 day 41 and grade 11 days 51 and 52, in the form grade 7 day 28 uses.
- **Tag: scope.**

### 11. Device and pair routines are worded differently in each frame

- **Put-away minutes:** 4 in K to 3, 5 in grades 4 and 6, 4 in grades 5 and 7, 3 at each end in grade 8, 3 to open
  and 4 to save in grades 9 and 11, 3 in grade 10, 3 plus 2 for paper in grade 12.
- **Pair switch:** "at the halfway signal" in most courses, "every eight minutes" in grade 4, "at a stated time" in
  grade 6.
- The frames set these numbers, so they differ at the source.
- **Why it matters.** It is minor for students. A specials teacher with several grades, or a reviewer reading the
  band, sees a routine that changes for no stated reason.
- **Fix.** One device line per band, kept in APPROACH and quoted by each frame:
  - K to 5: four minutes to put away, switch at the halfway signal.
  - 6 to 12: three minutes to open, four to save and close, switch at the halfway signal (grade 4's eight-minute team
    rotation kept as a named exception for teams of four).
- **Tag: frame.**

### 12. Repeated anchors and titles across the elective years, and one stale string

- **Anchors.** Grade 7 day 1 (a printed twenty-line quiz), grade 8 day 13 (a twenty-line word-guess game) and grade 10
  day 1 (a twenty-line guessing game) open their years on the same kind of program. A student who built the grade 8
  word-guess game meets a guessing game again as grade 10's "read closely" anchor.
- **Title.** Grade 7 unit 4 and grade 9 unit 3 are both called "Algorithms that decide".
- **Typo.** Grade 11 For the lead 3 reads "rame.py".
- **Why it matters.** A repeat with no reason named (check 2). It is small, but a family or student sees it.
- **Fix.**
  - Give grade 10 day 1 a different twenty-line program, for one a small inventory or a timetable lookup, with the
    same procedures for the "what does each procedure hide" question.
  - Rename grade 9 unit 3, for example "Rules, chance and AI".
  - Correct "rame.py" to "frame.py".
- **Tag: scope.**

## What holds

- **Ownership.** All 196 Foundational ids are claimed by exactly one course. The eight S1 ids are in grades 11 and 12
  only, as STANDARD.md lists them. Every begun `~ID` is owned by a later grade.
- **Progression coverage.**
  - All 202 progression rows are taught in their own grade, none only begun.
  - Every row's `assumes` cell is taught in full in its grade.
  - Every year-before row is opened as a named retrieval day.
  - Grade 12's grade 9 rows get a readiness check for every student (day 22).
- **Ramps.**
  - Blocks to text: block code with a text view in K to 5, side by side in grade 6, Python text in grade 7, Python
    from grade 8.
  - The variable runs from the named box (grade 2) to the trace-table (grade 3), supplied score logic (grade 4),
    store, compare and change (grade 5) and three types (grade 6).
  - Assignment is worded "becomes" or "set to" in every grade.
  - Reading load stays inside APPROACH's limits.
- **Calendar.**
  - K to 5 is treated as a special in every scope (CALENDAR rule 1).
  - Grades 6 to 8 keep off core check days.
  - Every course's check weeks match CALENDAR.md's table.
  - Grade 12 ends its checks by week 28 for early leavers.
- **Society cases.**
  - Each society case is dated, with two views and no company named.
  - The grade 10 children's online privacy law comes back on grade 12 day 16 as a card.
  - The grade 7 sovereignty case comes back as a card on grade 11 day 52 with a reason.
  - Grade 11's retrieval of grade 8's data center debate is named.

## Sources

- Repository files listed under What I read (opened 2026-11-26).
- https://www.fcc.gov/document/fcc-ends-e-rate-funding-school-bus-wi-fi-and-hotspot-lending: browser check (403,
  2026-11-26). It is for grade 7 day 50's "2025-09-30 federal vote" with its majority and dissent. From memory the
  date and the split vote hold.
- https://www.usmint.gov/coins/coin-medal-programs/native-american-dollar-coins/2019: browser check (403,
  2026-11-26). It is for grade 4 day 28's Mary Golda Ross card (the 2019 Native American dollar). From memory it
  holds.
- https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf: opened 2026-11-26. The text did not extract, so only
  the 2019 publication folder supports grade 7 day 39's "NISTIR 8280 of December 2019".
- Not opened, from memory and consistent with the scopes:
  - the Fair Credit Reporting Act of 1970 (grade 8 day 56);
  - the 1983 airliner and GPS civilian access (grade 9 day 56);
  - the 1998 children's online privacy law (grade 10 day 57);
  - NIST SP 1270, March 2022 (grade 11 day 50).
- The scopes' own browser checks stand as listed there: the CISA phishing page, the ASPE telehealth report, the khipu
  and NFB braille pages, and the Smithsonian Hopper oral history.
