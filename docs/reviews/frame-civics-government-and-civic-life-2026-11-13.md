# Frame read: Civics: Government and Civic Life (grade 8), 2026-11-13

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Brief: docs/pipeline/briefs/frame-read.md.

## What I read

- docs/courses/civics-government-and-civic-life/frame.md, in full; its row in data/plans/frames.csv (10 units,
  160 days). No base text, so no source map.
- The 27 grade 8 rows of data/progressions/social-studies.csv, every column; the grade 5 and 7 rows they take from
  and the wh1, us1, us2, gov and econ rows they hand to (assumes and hands_on checked both ways by script: no broken
  pair).
- The neighbour frames: world-geography-and-ancient-civilizations-ii (before), social-studies-grade-5 (the founding,
  last taught there) and us-government-and-politics (grade 12, builds on this course). No World History I frame
  exists yet.
- The bar: docs/agents/lenses/social-studies.md, docs/ADOPTION-BAR-SUBJECTS.md (shared core and section 1, items 11
  and 13 in particular), docs/courses/social-studies/STANDARD.md, docs/FOUNDATION.md section 7, the MA.8 lines of
  data/standards/ma-hss-2018.txt, the C3 ids, docs/agents/decisions/DESK-ANSWERS.md (card q-ss-progression-1).
- Every cross-subject row named in the frame, and every ELA, math and science row that names an ss8 row. No grade 8
  ELA or math frame exists yet.
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md; no earlier frame read.
- Gates: `python -X utf8 scripts/plan.py check` (this frame: 0 failures, 10 units, 148 days in units, 12 for
  checks); `python -X utf8 scripts/stale.py check` (0 failures). I counted the MA.8 codes by hand: 56, as the frame
  says. The cross-subject day windows match the unit days.

## Verdict

The frame is sound: all 56 anchor codes and the grade 8 C3 civics, economics and action indicators sit in units
with reasons, "your state" is taught as a method with several states, the values rule is applied where it bites
(Barnette over Gobitis, secession from the seceding states' own words, the 2015 ruling), and party and family
neutrality is written in. The biggest gap is one Cory already decided: Native nations as present-day governments in
grade 8 (DESK-ANSWERS 2026-11-13, q-ss-progression-1) is carried by no row, the frame only proposes it, and grade
12's gov-federalism and an earlier review both assume it is there. The one change that matters most is to put it
in ss8-federal-state-powers and unit 7 before the scope and sequence; next, the human reads and the timing of the
action unit.

## Findings

### 1. Cory's call "Native nations as present-day governments in grade 8" is carried by no row

- **What is wrong.** Cory kept the writers' call 7 (DESK-ANSWERS 2026-11-13, q-ss-progression-1). No grade 8 row
  names tribal governments: ss8-haudenosaunee-influence is an influence inquiry, ss8-federal-state-powers names
  "state and national governments" only. The frame sees it ("For the lead" 1) and leaves the row unedited. Grade 12
  gov-federalism teaches "tribal nations as a third sovereign" with a readiness check on ss8-federal-state-powers,
  and docs/reviews/progression-social-studies-2026-11-13.md ("What is right") lists "8 (tribal sovereignty)" as
  present, which the data does not show.
- **Why it matters.** A decided scope item would be lost at the scope and sequence, which builds from the rows; the
  grade 12 readiness check would test what grade 8 never taught; and the review's claim tells the next reader the
  gap is closed. D2.Civ.5.6-8, owned by ss8-federal-state-powers, asks for "selected other systems of government"
  (C3 wording from memory), which is the natural home.
- **Fix.** Add to ss8-federal-state-powers's notes: "Tribal nations as governments today: more than 570 federally
  recognized nations with their own constitutions, councils, courts and services, and treaty rights; one worked
  example from the nation's own materials (the Medicine Creek Treaty nations, through Since Time Immemorial unit
  1C), in the present tense. Grade 12 (gov-federalism) builds the third-sovereign law on it." Add "tribal nations as
  governments, with one worked example" to unit 7's "What students learn", inside its 20 days, and "community
  reader" to unit 7's last column. Replace "For the lead" 1 with a line saying it is done. The caller corrects the
  review's "8 (tribal sovereignty)" line or notes beside it that it was true only after this fix.
- LAYER progression and process (stale review result). REPEAT new. Confidence: firm.

### 2. The human reads are fewer than the bar and FOUNDATION require

- **What is wrong.** "Units 1, 2, 6 and 7 need the fresh-agent sensitivity read, and unit 1 a qualified person's
  read." Bar item 12 asks the read of every unit. FOUNDATION section 7 asks a reader from the community concerned
  for hard-history content: unit 2 (how the Constitution protected slavery) and unit 6 (secession, Dred Scott, the
  persecution of Jehovah's Witness families) are hard history with no such reader; unit 7, with finding 1, carries
  Native governments.
- **Why it matters.** The reads, and the people Cory is asked to find, are planned from this sentence.
- **Fix.** "Every unit gets the fresh-agent sensitivity read (bar item 12). A reader from the community concerned
  reads units 1 and 7 (Native nations) and units 2 and 6 (slavery and its law)." Add the reads to the last column
  of each unit.
- LAYER frame. REPEAT new (same kind as the grade 6 and 7 frame reads of the same day). Confidence: firm.

### 3. The action unit falls in the year's last twelve days with no time to see a result

- **What is wrong.** Unit 10 runs days 149 to 160: deliberate, choose, present "to an audience beyond the class",
  then look back. School boards and officials book weeks ahead and the last two weeks of a school year are its
  most crowded; an action presented on day 158 has no answer by day 160. The frame allows the deliberation to
  "start earlier ... if an audience's calendar needs it" but sets no date.
- **Why it matters.** The grade 8 action is the one that leaves the school (D4.3: audiences outside the classroom);
  if the audience cannot be booked, the writer falls back to presenting to the class, and the look-back has nothing
  to look at.
- **Fix.** Add to "Informed action": "The teacher books the audience by the end of unit 8 (about day 130); the
  presentation falls by about day 157; the last day is the look-back, which records the answer received or what is
  still pending and what the class would do next." Same in ss8-civic-action's notes.
- LAYER frame. REPEAT new. Confidence: judgment call.

### 4. The counterclaim seam from grade 7 is in prose but not in the data

- **What is wrong.** Seams: "A multi-cause argument naming the opposing claim | ss7-rome-fall | Unit 1
  (ss8-haudenosaunee-influence answers counterclaims in full)", and Models carried lists claim-evidence-reasoning
  from ss7-rome-fall. But ss8-haudenosaunee-influence's assumes is empty and ss7-rome-fall's hands_on lists only wh1
  rows; the grade 7 frame's "Handed on" table omits it.
- **Why it matters.** Unit 1's readiness check is built from assumes; with it empty, nothing checks that students
  can name an opposing claim before they are asked to answer one in full on day 1 to 15.
- **Fix.** Add ss7-rome-fall to ss8-haudenosaunee-influence's assumes (and ss8-haudenosaunee-influence to
  ss7-rome-fall's hands_on); the grade 7 frame adds the row (its own read, finding 6).
- LAYER progression. REPEAT new. Confidence: firm.

### 5. Unit 4's reason for its place does not hold in most calendars

- **What is wrong.** "Falls near the November elections in most years, so current information is at hand." Unit 4
  is days 52 to 63; Election Day (the first Tuesday after November 1) falls near school day 45 to 50 in most
  calendars, and a 160-day course runs behind a 180-day school calendar, so the unit falls after the election.
- **Why it matters.** Minor: the placement still works (results, turnout and spending data are fresh), but a writer
  who trusts "near" may build days on a live campaign that has ended.
- **Fix.** "Falls just after the November elections in most years, so results, turnout and campaign finance data
  are fresh; in years with no federal election, the unit uses the latest state or local election."
- LAYER frame. REPEAT new. Confidence: likely.

### 6. One cross-subject lean is missing from the table

- **What is wrong.** e8-reading-range (ELA 8) thread 1 reads beside ss8-greek-roman-roots, ss8-declaration and
  ss8-press-freedom, and thread 2 beside ss8-news-literacy. The table lists the ss8-declaration lean only.
- **Why it matters.** The ELA 8 frame will not know that the free-press and news half of its threads needs unit 9
  (days 131 to 144), late in the year.
- **Fix.** In the e8-reading-range line add: "its Greek and Roman roots texts after unit 1 (days 1 to 15); its free
  press and news-claims texts during or after unit 9 (days 131 to 144)".
- LAYER frame. REPEAT yes (cross-subject timing, progression-cross-2026-11-13). Confidence: firm.

### 7. Stale notes

- **What is wrong.** (a) "For the lead" 6 says frames.csv is "Not edited here; `frame.py sync` writes the row"; the
  row is there (10, 160). (b) ss8-civic-action's notes say "the handoff skips 2 grades because grades 6 and 7 are
  world geography and ancient civilizations" and, two sentences on, that the skill is "kept in use between by
  ss6-mena-settlement and ss7-athenian-democracy", which it assumes. Neither is marked, so stale.py passed them.
- **Why it matters.** (b) tells a writer the action skill has lain unused for two years and invites a reteach of
  what grades 6 and 7 practised.
- **Fix.** (a) "frames.csv carries the row (10 units, 160 days), written by `scripts/frame.py sync`; rerun it if the
  unit count changes." (b) Delete "the handoff skips 2 grades because grades 6 and 7 are world geography and
  ancient civilizations; grade 8 is the civics year" from ss8-civic-action; the "maintained skill" sentence says it.
- LAYER process and progression. REPEAT yes (the progression fixes of 2026-11-13, item 9, rewrote this very
  sentence in ss8-civic-action). Confidence: firm.

## The lens checklist (course frame layer)

| Line | Met, missed or not applicable |
|---|---|
| An anchor standard in the course's topic range has no unit | Met (gate; 56 of 56 counted by hand) |
| "Your state" in grade 8 keeps Massachusetts-only content | Met: unit 7 and unit 9 teach the student's own state with several worked examples; Massachusetts (8.T6, Article 16) is one example |
| No unit lists what the check set adds, or an addition has no recorded source | Met: the column is filled; candidates name California's government course or Tennessee |
| History in time order, or a reason | Met: the two moves from the anchor's order (8.T5.1 and 8.T5.5 to unit 3; 8.T4.12 and 8.T4.13 to unit 8) carry reasons |
| A contested question has more than one telling | Met: the Haudenosaunee influence claim against historians' counterclaims; Federalist and Anti-Federalist; editorials from more than one side |
| Writing from sources builds short to long | Met: unit 1 claim and counterclaim, units 2 to 5 short pieces, unit 6 the longest, units 9 and 10 |
| Values rule applied | Met: (a) Barnette over Gobitis; (b) secession from its own declarations; (c) the 2015 ruling; (d) grade 8 depth |
| Sensitive topics and the reads | Missed in part (findings 1 and 2) |
| Informed action once a year, chosen by students | Met, with finding 3 on its timing |

## What is right and should not be touched

- Party and family neutrality, and no question about anyone's citizenship status.
- The founding documents read for claims, structure and what they left out, with rhetoric left to ELA, and the
  same-month warning with ELA 8.
- Judicial review and implied powers taught with the branches (unit 3), where most civics courses teach them.
- The Haudenosaunee Confederacy in the present tense and the influence claim weighed, not asserted.
- The economics row placed in a real state or town budget, with spillovers, bonds and one state chart.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 7 split: federalism and tribal governments 5 days, state rights documents 3, state and local government 6, public budget and economics 6 | Keeps the year's only economics row (four C3 economics codes) from being squeezed in the longest unit | frame unit 7 |
| The two moves from the anchor's order stand | Each has a reason that holds; no standard leaves the course | frame "For the lead" 2 |
| The ratification excerpts: Federalist No. 51 and Brutus No. 1, short and glossed | MA.8.T2.4 compares the two sides, which needs one excerpt from each; grade 12 (gov-founding-documents) reads Federalist against Brutus at depth | frame unit 2 "Check set adds" (moves from candidate to placed) |
| Unit 4's reason reworded as in finding 5 | Matches the calendar | frame unit 4 |
| 45 minutes a lesson | Agree with the pick; C2 needs a stated length | scope and sequence |

## For Cory

- People: with findings 1 and 2, grade 8 needs readers from the community concerned for units 1 and 7 (Native
  nations) and units 2 and 6 (slavery and its law), not unit 1 alone.

## What I could not judge

- No grade 8 ELA or math frame exists, so the leans are checked against the progression rows only.
- No World History I frame exists; the hand-ons to wh1 rows are checked against the rows only.
- C3 wording (D2.Civ.5.6-8 in finding 1) rests on memory: the repo holds ids only.
- Whether a given school board can hear eighth graders in May: finding 3 is a judgment from how school calendars
  usually run.

## Sources

- data/standards/ma-hss-2018.txt: MA.8 codes counted and traced.
- data/standards/c3-indicators.txt: C3 ids; wording from memory.
- docs/agents/decisions/DESK-ANSWERS.md, 2026-11-13, card q-ss-progression-1: Cory's call 7 (finding 1).
- docs/ADOPTION-BAR-SUBJECTS.md (C1, C12, section 1 items 8, 11, 12, 13) and docs/FOUNDATION.md section 7.
- docs/agents/lenses/social-studies.md: the checklist above.
- No outside source was fetched this run; nothing new for the source list.

Defects were not logged with `scripts/plan.py defect`: the caller asked that only this report be written.
