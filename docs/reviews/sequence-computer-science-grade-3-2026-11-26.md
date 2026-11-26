# Expert read: scope and sequence of computer-science-grade-3 (2026-11-26)

Job: docs/pipeline/briefs/sequence-read.md through build/scope-writes/CS-READ.md, {subject} = computer science.
Read cold; this reader did not write the scope.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/computer-science.md, docs/ADOPTION-BAR-SUBJECTS.md section 5,
  build/scope-writes/CS-BRIEF.md; STANDARD.md and APPROACH.md where the frame and brief point (devices, pairs, pacing).
- docs/courses/computer-science-grade-3/scope-and-sequence.md and data/plans/computer-science-grade-3/days.csv (32 rows).
- docs/courses/computer-science-grade-3/frame.md in full; the 16 g3 rows of data/progressions/computer-science.csv;
  the 19 E3 statements in data/standards/csta-2026-statements.txt; grade 2's days 24 and 25 (the sorter it hands on).
- Lean checks in the partner courses' days.csv: m3-two-step-problems from math day 54 (week 11), m3-scaled-graphs from
  math day 1, s3-design-problem from science day 25, e3-writing-process from ELA day 20, s3-weather-data from science
  day 98. The scope's lean lines match.
- Earlier reads: frame-computer-science-grades-1-to-5-2026-11-25.md, frame-computer-science-grades-1-to-12-fixes-2026-11-26.md,
  sequence-computer-science-grade-6-2026-11-26.md, sequence-computer-science-grade-11-2026-11-26.md (for REPEAT tags).
- Gates: `plan.py check` and `sequence.py check computer-science-grade-3` 0 failures (the 2026-11-26 lead fix accepts
  the check-as-end shape for units 2 and 4); `frame.py calendar` places grade 3 computer science in weeks 11 and 26;
  `stale.py check` names nothing in this course. school_day = 5n checked on every row; checks fall in weeks 11 and 26,
  unit ends in weeks 5, 20 and 31, all inside the frame's weeks. All 19 owned ids sit on taught days; no other id is
  claimed.
- No outside source was opened for this read; accuracy points in findings 5 and 6 rest on memory and say so.

## Verdict

The scope is sound: it follows the frame closely, trace comes before modify before make in units 2 and 3, debugging
follows the trace-table it uses, every grade 2 row opens as retrieval, and the calendar and leans are right. The biggest
risk is the unit 3 end-of-unit assessment: as written the solo build may code an algorithm Curio Class supplies, which
is not the "student-created" algorithm E3-PRO-PD-04 names, and the session does not fit a room with few devices. The
one change that matters most is finding 1 (code the child's own day 11 algorithm, or a credited classmate pair's day 9
card set, never a supplied one).

## Findings, most serious first

**1. Day 20's solo build may use an algorithm Curio Class supplies; E3-PRO-PD-04 asks for code from a
student-created algorithm.** LAYER sequence (frame-set). REPEAT yes (an end task misses a part of its code, as grade
11 finding 3).
What is wrong: the frame's Evidence bullet lets the day 20 four-card algorithm be "a classmate pair's from unit 2 with
its authors named, or one Curio Class supplies"; the day 20 goal says only "a new four-card algorithm". A busy writer
will supply one, because that is easiest to key. A supplied algorithm is not student-created, so the score would not
meet the statement. This differs from the 2026-11-25 frame read (M3), which offered "builds one given four-card
algorithm alone"; the classmate option is right, the supplied one is not.
Why it matters: the only individual evidence for the course's one device-only id would not meet the id.
Fix: day 20 goal and note: "each child codes a student-created algorithm: the child's own day 11 field-day algorithm,
returned with its marks on day 12, or a classmate pair's day 9 card set with its authors named"; drop "or one Curio
Class supplies". The teacher picks a four-card version where a card set is longer. Frame fix under the scope's For
the lead.

**2. Day 20 does not fit a few-device or one-screen room.** LAYER sequence. REPEAT new.
What is wrong: 30 solo turns of five minutes are 150 device minutes. With 15 devices they fit as two turns per pair;
with 5 devices at stations they need 30 minutes of station time, and on one screen 150 minutes. The note names only
the no-device path ("part met without a device").
Why it matters: the frame says every device day is written four ways; a teacher with five devices cannot run this
session as planned and has no rule for who builds when.
Fix: add to day 20's note: "Few devices: solo turns run at the stations through the day 20 sitting and the first half
of day 21, five at a time; children not at a station work on paper. One screen: one child at a time through days 20
and 21 as time allows; those who do not reach it are recorded on the no-device path." Day 21's respond work for those
children runs on printouts.

**3. Day 25's class sorter has no rule that makes it err.** LAYER sequence. REPEAT new.
What is wrong: the class "acts as a sorter trained on insect and spider cards with few side-view spiders", but nothing
says what the sorter may use to decide. Grade 3 children know a spider when they see one, so the "before" tally may
show no mistakes and the lesson fails. Grade 2 (days 24 and 25) gave its sorter yes or no feature questions from the
labeled examples; grade 3 drops that.
Why it matters: the only teaching day for E3-ALG-ML-02 depends on the sorter making the predicted mistakes; it also
feeds the misconception that a model "knows" what it is looking at.
Fix: day 25 note: "The sorter decides only by the yes or no feature questions the class writes from the training cards
(for one: can you see eight legs? are there two body parts?); a child who knows the answer another way keeps it for the
tally. Side-view spiders show fewer legs, so the first questions miss them." The day 26 item keeps a new sorter's
tallies, so nothing there changes.

**4. Days 13 to 16, 20 and 2 do not name their paper path, though the scope says every device day does.** LAYER
sequence. REPEAT new.
What is wrong: days 13 to 16 and 20 say only "the few-device stations, one-screen and no-device versions the unit plan
writes"; day 2's teacher-led search on one screen has no paper version. Days 1, 17, 18, 19, 21 and 23 do name theirs.
Why it matters: CS-READ asks that every device day carry a paper path meeting the same ids, and a unit plan writer
reads the note, not the frame.
Fix: add to each note: days 13 to 16, "Paper path: paper block cards with if and else cards and the printed
block-and-text-view; a partner runs the cards as the computer"; day 20, "Paper path: the solo build laid in paper block
cards, run by the teacher, recorded part met without a device"; day 2, "Paper path: a printed strip of the search,
step by step".

**5. Day 30 lists four tools for "three", and the society days' sources are thin.** LAYER sequence. REPEAT yes (two
views and dated sources not named, as grade 11 finding 4).
What is wrong: day 30's goal reads "three computing tools (a computer weather forecast, a route finder, a voice helper
that answers spoken questions, an AI system)": the frame's voice helper is the AI system, and the comma makes it a
fourth tool. Day 30 names a source for the forecast only; the voice helper's "for a person who cannot easily see a
screen" is a claim with no source. Day 29 says "two brief views with one dated source each" and names one source. Day
4 names no source for its map case.
Why it matters: a writer would build four tool cards in 33 minutes, and unsourced claims break the frame's society
rule (two views, one dated source each).
Fix: day 30 goal: "three computing tools (a computer weather forecast, a route finder, and a voice helper that answers
spoken questions, which is an AI system)"; notes on days 4, 29 and 30 name the second view's source type and say
"sources picked and dated when the cards are written" where none is named yet, with the voice helper's access claim
kept only if a dated source supports it (from memory: voice assistants were sold mainly for hands-free use, and their
use by blind and low-vision people is documented by disability organizations; check before use).

**6. Day 29's "paying at a shop" steps are not about paying, and the "now" step is not current.** LAYER sequence
(frame-set). REPEAT new. Confidence: likely (from memory).
What is wrong: "a written bill, a cash register, a scanned bar code" moves from paying to ringing up a price; bar code
scanning at checkouts dates from the 1970s, older than most of the children's parents, and is shown as the newest way.
Why it matters: E3-SOC-HI-16 asks how innovations changed how people live over time; an inaccurate "now" teaches the
wrong change.
Fix: "paying at a shop: cash counted out with a written bill, a card run through a reader, a card or phone tapped to
pay" (no product names); keep "written bills are still in use, shown with respect".

**7. The year-end check (day 26) is overloaded.** LAYER sequence. REPEAT yes (grade 4 frame read M4, an overloaded
year-end sitting).
What is wrong: seven items in about 25 minutes, with "about 15 for the four unit 4 items"; the collection plan alone
asks what, whom, how, how everyone can answer, the opt-out box and one group a different plan leaves out, which is
several minutes of writing for a grade 3 child. The pretend-post sample repeats E3-SYS-SE-13, already scored on day 5
and sampled on day 11.
Why it matters: the plan item is the only individual evidence for E3-DAT-IM-11; rushed, it reads as a missing part.
Fix (settled below): drop the pretend-post sample from day 26 (and from days 26 and 27's codes and skills), give the
plan item a half-filled planning sheet (the topic and question given; the child fills whom, how, how everyone can
answer, the opt-out box and one group left out), and add E3-SYS-SE-13 to the scope's "owned codes not sampled on a
check day" with "scored on day 5, sampled on day 11".

**8. E3-PRO-PD-05 is scored only from day 16, the session that first teaches it, and day 21 cannot regather it.**
LAYER sequence (frame-set). REPEAT new. Confidence: a judgment call.
What is wrong: day 20 scores PD-05 from "each child's day 16 line"; day 16 is the only feedback session. The frame's
"no score comes from a session that first teaches a row" is met for the row (day 16 is its fourth session), but not for
the id. Day 21's "rerun and fix the missed item's new form" has no form for PD-05.
Fix: add one short paper item to day 20 (about two minutes): a new short program and a partner's look-for form with
one suggestion; the child writes the change they would make and what they would test. The day 16 line stays as
supporting evidence; day 21 gives a missed PD-05 a new suggestion on the child's own solo build.

**9. Pair roles are named on days 14 and 15 only.** LAYER sequence. REPEAT yes (grade 11 finding 10, grade 6 finding 7).
What is wrong: the frame's unit 3 practices put IC5 driver and navigator, switching at the halfway signal, across the
unit; days 13, 16 to 19, 21 and 23 are pair device days with no roles.
Fix: add "Driver and navigator switch at the halfway signal" to those notes (day 20's solo turns excepted).

**10. Day 23 is full, and its graph form is not named.** LAYER sequence. REPEAT new.
What is wrong: a two-week table, a scaled picture graph by hand, the same graph in a tool and a written finding in
about 29 minutes; and a picture graph shows counts, so a relationship between two attributes needs a named layout.
Fix (settled below): the picture graph has two rows, windy days and calm days, each counting cold and warm days, one
picture for two days; the graph tool opens with the table already entered and pairs only pick the graph and compare it
with their own (about 8 minutes).

**11. The shorter path does not say what day 13 gives up or that the check weeks move.** LAYER sequence. REPEAT new.
What is wrong: folding day 14 takes "the last 10 minutes of day 13", which already holds the anchor, the retrieval, the
trace and predict and the shuffled reorder. Folding day 8 moves the mid-year check to session 10 (week 10), and both
folds move the year-end check to week 24.
Fix: say day 13 drops its second predict program and keeps the reorder; add one line: "with both folds the checks sit
in weeks 10 and 24; the lead's calendar pass confirms them."

**12. Stale and small notes.** LAYER sequence. REPEAT yes (grade 6 finding 12, retrieval labels).
- "For the lead 1" and the unit 2 and unit 4 lines "See For the lead 1 on the gate" are stale: sequence.py accepts the
  check-as-end shape since the 2026-11-26 lead fix. Remove item 1 and the two pointers.
- Day 2's retrieval traces day 1's system-diagram with software (g3-software) but `retrieves` says g2-io-parts; set it
  to g3-software and drop day 2 from the g2-io-parts row of the retrieval table.
- Bar item 8 asks for rubrics on projects and code: day 20's note names no rubric for the solo build. Add "scored on a
  short rubric: each structure present, it runs, it matches the algorithm, credit line present".

## What is right and should not be touched

- Trace, modify, make in order (days 7, 8, 9 and 13, 14, 15); read, variables, then debugging with the trace-table, in
  the progression's in-grade order; no typed text code; assignment worded as "gets", never "equals".
- The check-as-end shape for units 2 and 4, each check sampling earlier units with new items, not the day 5 or 20 ones.
- The retrieval table: every assumed row is grade 2, so no readiness check is owed, and none sits on a unit's first day.
- The sensitivity guards on days 3, 4, 10, 24, 28 to 30, copied from the frame.
- school_day = 5n and every check inside the frame's weeks; the leans and their bridges.

## Lens checklist (scope and sequence layer)

| Line | Status |
|---|---|
| All five concept areas taught, AI inside data | Met (unit 4 day 25 on unit 4's data; day 30 ties back) |
| Read before write, then modify, then make | Met |
| Unplugged teaches, plugged tests | Met; paper paths need naming (finding 4) |
| Notional machine taught (trace-table, be the computer) | Met (days 13, 18, 19) |
| Debugging as a method | Met (day 19) |
| Practices inside content, pair roles | Part met (finding 9) |
| Society with evidence, dated, more than one view | Part met (findings 5, 6) |
| Id below boundary or claimed by a mention only | Met; no Specialty or other-grade id claimed |
| End-of-unit reads, traces or writes code | Met (day 20); rubric to name (finding 12) |
| Unplugged path in every unit | Met |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 20 solo build codes the child's own day 11 algorithm or a credited classmate pair's day 9 card set; no supplied algorithm | E3-PRO-PD-04 says student-created | days.csv day 20; frame For the lead |
| Few-device day 20: stations through day 20 and the first half of day 21 | 30 five-minute turns fit only that way | days.csv days 20, 21 |
| Day 25 sorter decides only by the class's yes or no feature questions | The sorter must make the predicted mistakes | days.csv day 25 |
| Day 29 paying steps: cash and written bill, card reader, tap to pay | Accurate and current | days.csv day 29 (frame text for the lead) |
| Day 26 drops the pretend-post sample; plan item on a half-filled sheet | Load; SE-13 scored day 5 and sampled day 11 | days.csv days 26, 27; scope check tables |
| Day 20 adds a two-minute feedback item for E3-PRO-PD-05 | An individual unseen item for the id | days.csv day 20 |
| Day 23 picture graph in two rows (windy, calm), tool opens pre-filled | Shows a relationship; fits the time | days.csv day 23 |
| Day 2 retrieves g3-software | Matches its retrieval task | days.csv day 2; retrieval table |

## For Cory

None. Every finding is an item-level or wording fix inside the frame's units and ids.

## For the source list

None new; no outside source was opened. Before day 30's cards are written, a dated source on voice helpers used by
blind and low-vision people (a disability organization's page) would carry the access claim.
