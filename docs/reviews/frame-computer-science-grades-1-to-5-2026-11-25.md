# Frame read: computer science, grades 1 to 5 (2026-11-25)

Expert cold read, one combined pass over five frames, to docs/pipeline/briefs/frame-read.md with the after-core
changes in the task. Read only; this file is the one write.

## What I read

- AGENTS.md; docs/pipeline/briefs/frame-read.md; docs/courses/computer-science/STANDARD.md and APPROACH.md;
  docs/agents/lenses/computer-science.md; docs/agents/EXPERT.md (opening).
- docs/courses/computer-science-kindergarten/frame.md and
  docs/reviews/frame-computer-science-kindergarten-fixes-2026-11-25.md (the pilot pattern and its fixes).
- docs/courses/computer-science-grade-1 to -grade-5/frame.md in full; docs/courses/computer-science-grade-6/frame.md
  (header, seams and unit 1) for the grade 5 handoff.
- data/progressions/computer-science.csv, every grade 1 to 5 row, checked against each frame's "For the lead" row
  changes.
- The boundary statements in the source store (S:\CurioClass-sources\computer-science\csta-2026-11-21), read for
  E1-ALG-PS-01, E1-DAT-DI-09, E2-PRO-PD-04, E3-PRO-PD-04, E3-PRO-PD-05, E4-PRO-PD-04, E4-PRO-PD-05, E4-DAT-DC-09,
  E5-PRO-PD-04 and E5-DAT-DC-09. Nothing copied.
- `python -X utf8 scripts/plan.py check`: computer-science progression 202 rows, 0 failures; all five frames
  0 failures, 32 days each (28 in units, 4 for checks and respond days). `scripts/stale.py check`: 0 failures.

## Verdict

All five frames are sound in shape. Each follows the pilot (28 unit days, two course-level checks that stand for a
unit's assessment, two respond days, trace then modify then make, one look-for per owned id), the seams grade to grade
are named and match, and grade 5 hands grade 6 exactly the 16 rows grade 6 picks up. The one serious problem is
outside the frames: the row changes grades 1 and 2 depend on did not land in the progression, while grades 3 and 5
did. Device time is the main design question: K to 3 sit far below APPROACH's share and the band needs one stated
rule.

Per frame:

| Frame | Verdict |
|---|---|
| Grade 1 | Ready after fixes. Strong unplugged design; its row changes are not in the CSV, and the mid-year item for E1-ALG-PS-01 tests ordering, not decomposing. |
| Grade 2 | Ready after fixes. Row changes not in the CSV; its device share drops below grade 1's against grade 1's own handoff line. |
| Grade 3 | Ready after fixes. Row changes landed. E3-PRO-PD-04 is scored from a pair product while its look-for says the child's own; device share a quarter against "about half". |
| Grade 4 | Ready after minor fixes. Meets the device share; the year-end check day carries too much for 40 minutes. |
| Grade 5 | Ready after fixes. Row changes landed; the device-share sentence contradicts the count; unit 3 session 3 is overloaded; the E5-PRO-PD-04 item is thin. |

## Findings

### Serious

**S1. Grade 1 and grade 2 row changes did not land.** LAYER progression. REPEAT new.
What is wrong: grade 1 "For the lead 2" and grade 2 "For the lead 5" list row changes the frames already teach to;
none is in data/progressions/computer-science.csv. Still in the CSV: g1-data-questions keeps its pet questions
("how many pets", "which pet is best", "do you have a pet"); g1-keep-safe keeps "practise" and lacks signing out and
the given password; g1-responsible-use lacks the consequences for self and class; g1-patterns-ai lacks "made by
people" and the suggestion example; g1-two-kinds-data keeps "labelled"; g2-people-solve's notes lack the familiar
machines half (E2-SOC-HU-15); g2-data-questions keeps "which snack"; g2-benefits-harms keeps "one tool a child
uses" (the frame pictures the tool); "labelled" remains in g2-ai-training-data and g2-name-and-label. Grades 3 and 5
landed in full (why-build, share-online, ml-new-data, labeled; grade 5's five).
Why it matters: the scope and sequence and day writers read the rows, not the frames, so the frames' fixes are lost
downstream, and the pet and snack questions cut against the values line (a child with no pet or no snack at home is
singled out).
Fix: apply both lists as written in the frames; then sweep the grade 1 and 2 rows for "labelled" and "practise".

**S2. The pet and snack data questions stand in the rows as the model questions.** LAYER progression. REPEAT new.
What is wrong: a part of S1 that ranks on its own. E1-DAT-DI-09 wants a countable question beside an opinion one; a
class-countable question (shirt colors, the weather chart, the class's book votes) does that without asking about
home.
Fix: in g1-data-questions use a classroom count and a classroom opinion question; in g2-data-questions use a class
choice made in school (a class read-aloud vote, a recess game). Leave health-3's "which snack" worksheet alone (not
this subject).

### Moderate

**M1. Device share in K to 3 is far below APPROACH, and grade 2 goes down from grade 1.** LAYER frame and standard.
REPEAT new.
What is wrong: APPROACH Pacing sets about two thirds away from a device for K to 2 and about half for 3 to 5.
Grade 1 states four fifths away, grade 2 seven eighths away (a lower share than grade 1, against grade 1's line
"grade 2 may raise the share"), grade 3 about a quarter on a device. Grades 4 and 5 meet it.
Why it matters: a frame that drifts from APPROACH without saying so invites each later writer to re-decide it.
The unplugged choices are good teaching; the gap is the missing rule.
Fix: either raise grades 2 and 3 (grade 2's unit 3 sessions 4 and 6 and unit 5's make can run on the editor; grade 3
unit 4's data-table work can) or add one line to APPROACH Pacing: "K to 3 may sit below this share when the
unplugged form teaches the row as well; each frame states its share." Then reword grade 1's handoff line to match
what grade 2 does.

**M2. Grade 1's mid-year item for E1-ALG-PS-01 does not test decomposition.** LAYER frame. REPEAT new.
What is wrong: day 13 asks children to order the step-cards of each part of a new pictured job. The parts are given,
so the child sequences but never breaks the task down; the boundary asks for breaking a familiar multistep task into
smaller ordered steps.
Fix: give the whole job as one picture (or one spoken instruction) and have the child cut it into parts first, by
drawing lines between picture panels or choosing two to four part cards from a set with decoys, then order the steps.

**M3. Grade 3 scores E3-PRO-PD-04 from a pair's program; its look-for says the child's own.** LAYER frame. REPEAT
new.
What is wrong: the Evidence bullet says a "create" or "develop" id is met by the child's own algorithm or program;
the unit 3 end-of-unit scores "each pair's saved program". The boundary allows a classmate's algorithm with credit,
but the implementing is what is assessed.
Fix: keep the pair build, and score each child on a short individual implement step on day 20: each child adds the
choice (if-else) for one fork of the pair's game, or builds one given four-card algorithm alone; the pair program
is carried as supporting evidence.

**M4. Grade 4 year-end check day 24 is overloaded.** LAYER frame. REPEAT new.
What is wrong: one 40-minute sitting carries trace, compare, test and comment items, the team rubric and three
sampled items.
Fix: move the team rubric to the unit's last teaching session as observed evidence (scored there is fine, as it does
not first teach the row), and keep day 24 to the written items and the samples, about 25 minutes.

**M5. Grade 5 unit 3 session 3 carries five debugging strategies in one 40-minute session.** LAYER frame. REPEAT new.
Fix: teach three in session 3 (trace by hand, test one part, take pieces out) and the other two (read the tool's
message, add a temporary output) in session 4, where each pair already picks a strategy.

**M6. Grade 5's mid-year item for E5-PRO-PD-04 is thin.** LAYER frame. REPEAT new.
What is wrong: "add a given credited part to a given working program" checks placement and credit, but the boundary
asks for purposeful changes that make a unique variation.
Fix: let the item give two or three code segments and ask the child to choose one, place it, change one value so the
result is their own variation, write the credit comment, and say in one line what the new version does differently.

### Minor

**m1. Column numbering.** Grade 1 calls the Practices column the "seventh column"; it is the sixth. K and grade 2
call it the "fifth column (the C3 column)". LAYER frame. REPEAT new. Fix: name the column by its heading
("the Practices column") in every frame, so a column count cannot drift.

**m2. "catalogue id".** K to 5 (and STANDARD.md) use the UK spelling; grade 6 uses "catalog id". LAYER frame and
standard. REPEAT new. Fix: "catalog id" everywhere, STANDARD.md included.

**m3. Grade 4's "picked up" table omits g3-benefits-risks to g4-history-limits.** The row's assumes names it.
LAYER frame. REPEAT new. Fix: add the row to the table with its grade 3 unit.

**m4. g5-network-parts lacks "switch".** Grade 5 unit 1 teaches a switch among the network parts. LAYER progression.
REPEAT new. Fix: add it to the row's notes, or drop it from the session.

**m5. Grade 5's device-share sentence contradicts its count.** About 12 of 22 teaching sessions are on a device, yet
the frame says "well over half the time away". LAYER frame. REPEAT new. Fix: "a little under half the time away from
a device, about half of the teaching sessions on one".

**m6. Grade 4 row leftovers.** "labelled" in g4-ml-learning, "practise" in g4-debug-increment, and "a pet picture"
in g4-table-tool. LAYER progression. REPEAT new. Fix: "labeled", "practice", and a class-object picture.

**m7. Duplicate sentence in g5-variability.** LAYER progression. REPEAT new. Fix: delete the second copy.

**m8. Grade 3 "a misspelled name makes a second box".** That is how a typed language behaves; in a block editor a
variable is picked from a menu. LAYER frame. REPEAT new. Fix: "a variable keeps one name; making a second variable
with a near-same name makes a second box", or drop the line.

### Judgment calls

**J1. E2-PRO-PD-04 full on paper, E3-PRO-PD-04 part met.** Having read both boundaries, the two frames are
consistent, not in conflict: grade 2's boundary counts coding a robot from an algorithm of arrows and lets the
teacher give the algorithm, while grade 3's places the code in a block-based environment. I would keep both as
written and record the reason in STANDARD.md "Devices and rooms" so it is not reopened. Grade 3's "For the lead 4"
can close on that.

**J2. Grade 3's device share.** If M1 is settled by an APPROACH line, grade 3's quarter is acceptable; if by the
share, grade 3 is the one grade that must move.

**J3. Grade 5 debugging strategies.** If the lead prefers one session that names all five, keep it, but then the
session's make (trying them) needs the next session (M5).

**J4. E4-DAT-DC-09 and E5-DAT-DC-09 part met on paper.** Correct by the boundaries (paper tables are allowed before
a computational tool, not instead of one). No change.

## Base text

All five map the archived Teach Computing edition from lesson titles only, Year N+1 to grade N, and say so. The
offers across grades are consistent: grade 2 offered Branching databases lessons 3 to 6 and Connecting computers
4 to 6 to grade 3, and grade 3 took Branching databases 3 and 4 and Connecting computers 4 to 6, stating why lessons
5 and 6 stay out; grade 4 offered Flat-file databases lesson 4 to grade 6; grade 5 offered addresses and packets to
grade 6. No lesson is claimed twice. The store folder is still pending, so every mapping stays provisional until
the edition is confirmed (For Cory).

## Seams

Grade to grade, each frame's "picked up" table matches the earlier grade's units and days, apart from m3. The grade 5
to grade 6 handoff matches all 16 rows and their days; blocks to text is bridged in grade 6 unit 1 sessions 1 to 3.

## Course-level check stagger clashes (not counted as findings)

Left for the lead's calendar pass. After-core subjects sharing a check week:

| Grade | Week | Also checking |
|---|---|---|
| 1 | 27 | health |
| 2 | 11 | health |
| 2 | 26 | visual arts, SEL |
| 3 | 26 | media arts, PE, SEL, visual arts |
| 4 | 24 | music |
| 5 | 18 | dance, media arts, theater, visual arts, PE, ELD |
| 5 | 25 | media arts |

Grade 3's unit 3 end-of-unit (day 20) falls in core check week 20; it is a unit assessment, not a course-level check,
so it is noted only.

## Settled by the expert

| Question | Settled as |
|---|---|
| E2-PRO-PD-04 on paper | Met in full: the boundary counts a robot coded from arrows and allows a given algorithm |
| E3-PRO-PD-04 on paper | Part met without a device: the boundary names a block-based environment |
| E4-DAT-DC-09, E5-DAT-DC-09 on paper | Part met: paper comes before the tool, not in place of it |
| E3-PRO-PD-05 | A pair need not take every suggestion; one taken and its change recorded meets it |
| Grade 3 base lessons left out | Right: Year 4 turtle text commands stay out (no text languages in grade 3) |
| Grade 5 to 6 handoff | Matches, 16 of 16 rows |

## For Cory

- **The training tool (scope).** Grades 4 to 6 lean on a tool that trains a small sorter; until it exists,
  E5-ALG-ML-02 is part met for every child, not only on the paper path. Build it, or accept part met for now.
- **The K to 2 picture-block editor mode (scope).** Grades K to 2 need icon blocks with a counted repeat; it is a
  mode of our own editor, so it is a tool-build choice.
- **The archived edition (scope).** Confirm which Teach Computing edition the store will hold, so the title-only
  mappings can be checked against the lessons.
