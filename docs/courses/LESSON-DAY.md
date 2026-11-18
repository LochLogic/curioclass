# The lesson day: what one teaching day ships as

This page sets the shape of every lesson day, about 15,000 of them (approved by Cory, settled 2026-11-12, see
DESK-ANSWERS). BASELINE rule 27 points here. The worked case is day 90 of grade 4 math, at the end. The expert's
cold read of the first draft is docs/reviews/lesson-day-2026-11-12.md. Every day carries an At home block for a
parent teaching one child (settled 2026-11-12, see DESK-ANSWERS, "homeschool parents and the site's shape"). The
shape is **proved on grade 4 math only** until the probe and guard run in other subjects
(docs/pipeline/PROBE-GUARD.md).

A section plan says what each day is for. This page says what a teacher and a student hold in their hands on that
day, how big each piece may be, and which pieces are written and which are generated. The shared shape holds for
every subject; "What changes by subject" below lists what is known to differ, and the probe in each subject adds
the rest.

## What one day ships as

| Piece | Who reads it | Made how | Size |
|---|---|---|---|
| **Teacher page** | The teacher, the night before | Written, plus a header and tables generated from data | 15 words of prose a minute of the day at most (900 at 60 minutes) on a teaching day, 500 on an assessment day (see "What changes by subject"). Generated tables do not count |
| **At home view** | A parent teaching one child | Written: the teacher page's At home block. Built as `dNNN-home.html`, each question it names pulled from data with its answer | 170 words at most, counted apart from the teacher prose cap |
| **Student page** | Each student | Written frame; every question pulled from data | One sheet, both sides of US Letter at most. Words a student reads counts everything printed for the student, questions included; the cap is set per course in DEFAULTS.md (grade 4 math: 350, ours, untested), and the gate reports frame and questions apart. No sentence over 15 words in grades 3 to 5. 18 point type in kindergarten to grade 2, with a line telling the teacher what to read aloud; 14 point in grades 3 to 5; 12 point from grade 6 |
| **Exit ticket** | Each student, then the teacher | Generated from data: the paper path's exit rows | A quarter page, four to a sheet |
| **Answer key** | The teacher | Generated from data: every answer on both exit paths, its equation or working, and what each wrong answer means | Usually one side |
| **Display page** | The class, on the projector | Generated from data, in the order the teacher page runs, part by part. For each worked example, the question with its labelled figure, then the steps one screen at a time; for each wrong answer to fix, their working beside the right working; one screen per **Ask.**; a challenge screen; the answers to a plain sum; a "check your answers" screen only where a part names a partner or self check (a `Check: ...` line in the part gives its sentence); on an assessment day, the answers screen and one screen per group in the respond part; the sentence frames last | No words of its own |
| **Slides** | Nobody | **None.** The display page and the tool's own screen do this job; a slide deck would be a second copy of the teacher page to write and keep right | 0 |
| **Materials** | The teacher | A line in the header: per student, per class, what to print and how many, and the stand-in for a room without it ("no document camera: draw it on the board") | Part of the header |

**Every built piece prints a foot line:** "Curio Class, grade 4 math, day 90, version <v>, CC BY 4.0,
curioclass.org", and the credit of any adapted item it prints (rule 4), so last year's photocopy can be matched to
today's key and a reuser can see whom to credit.

**Once per section** (not per day): the section opener (the teacher page for the section: the math explained at an adult's
level, why this model, the error register in plain words, the supply list; 1,200 words at most) and any generator sheet the plan defines. **Once per
unit** (filed in the folder of the unit's first section, as docs/courses/UNIT-PLAN.md puts them in the unit
plan): the family note in English and Spanish (150 words at most each), the record sheet, the readiness check
and end-of-unit assessment with their answer keys. A sheet with no preset questions (a strip sheet, a blank grid) is a
`piece: blank`: it prints for students, its words are counted without markup, and it must fit two sides. These
are generated from data wherever they can be.

**The arithmetic, so the size is seen.** A teaching day is at most about 1,420 words a person reads (900
teacher, 170 at home, 350 student, questions included), of which only the teacher prose, the At home block and the
student frame are written free: day 90 has about 1,100 such words. At about 150 days a course and the 105 active courses that is about 16 to 20
million words, before checks and section openers. The cost is in the reading as much as the writing (see "How days
are read"). The caps hold it down; real counts (first from grade 4 math, docs/pilots/COST.md) are measured again at the probe.

## Where it lives

One source file a day: `courses/<course>/u<unit>-<section>/d<day>.md` (day 90 of grade 4 math is
`courses/math-4/u11-1/d090.md`). The teacher page and the student page are both in it, so they cannot drift apart:
a header block, then `## Teacher page` with its fixed `###` headings, then `## Student page` with `### Side 1` and,
where needed, `### Side 2`.
The questions are not: every question a student answers on the day (worked examples, the tool's notes, practice,
wrong answers to fix, the exit) is a row in `data/plans/<course>/items.csv`, and its key is computed there. A day
file names a question by its id, `[[s11-P90-1]]`, and never types a key. `[[steps:id]]` prints a worked
example's steps from the row's `steps` cell, the same cell the display reveals, so the teacher page and the
display cannot drift; `[[note:id]]` prints a short form (who, and the numbers given) from the row's `figure` cell
for a table; `[[fig:id]]` draws the row's figure in place (on the student page, the key and the display). `python -X utf8 scripts/lesson.py build` makes the print pages in `build/lessons/`.

A row may carry, beside its key: `figure` (a labelled shape, `rect w=7 l=? A=63 u=ft`; a mixed number joins
with `_`, as `l=6_3/4`; flags `grid` draw the unit squares and `marks` tick and number each unit side; `around=`
names what goes round; small whole sides are drawn to scale; every number in the figure must be in the stem),
or a strip (tape) picture, `strip Ada:6 Eli:6*2=?`: one bar per `Name:pieces`, `_` for a space in the name;
pieces join with `+`, the first is the unit, `6*2` is two copies of it, a piece of another value (`6+2`) is
drawn dashed as the extra "more than" piece, a letter count (`6*n`) draws one long piece marked "n times";
`=total` brackets the bar (`=?` or a letter for the unknown), and `/a,b` brackets each segment. A wrong answer
to fix may hold two figures, their picture then the right one, split by ` | ` (`| strip ...` gives the right
one only). The first figure's numbers must be in the stem; the second's in the stem or steps.
A sum or difference in place-value columns is `cols 3746+2538` (or `cols 9372-4156`): place names over the
columns, a row for the small 1s or the rename (the old digit crossed out, the new one above), the two numbers,
a line and the answer. A wrong answer's working takes `carry=3` (the places, ones 0, that get a small 1),
`rename=-,-,-,14` (the new top digits left to right, `-` for one left as it was, `none` for no rename) and
`ans=4136` (or `ans=5/12/7/14` for a column written whole). On the display a worked example fills in step by
step as `by=` says, one entry a step: `0` the numbers only, `r2` the rename of the first two places, `d3` three
answer places, `-` no figure, `*` everything.
Fractions have two kinds. A number line is `line to=2 d=4 pt=7/4 / d=8`: `to=` the range from 0 (1 by
default), then one line per group split by a lone `/`, all stacked to one scale so a point sits straight above the
same amount below. Per line: `d=` the parts in a whole (the ticks), `sub=` cuts each part again with short ticks,
`lab=` the labels under the ticks (`whole` 0, 1, 2 by default; `all` adds every fraction; `none`; or a list,
`0,1/4,1`), `pt=` points named above the line, `blank=` points with an empty box above for the student to write
the name, `seg=` a shaded strip lying on the line from 0, `name=` a word at the left (the flag `names` writes each
line's parts word: fourths). A fraction strip is `fstrip 1/2 2/4 4/8`: each `k/n` a whole in n equal parts with k
shaded (past n a second whole follows), all at one length so they compare; `Lu:2/6` names the strip at its left,
`2/6=?` leaves a box there, `unit` writes 1/n in each part, `lab=none` writes nothing. Points, labels listed and
shaded strips count as the figure's numbers for the stem gate; ticks, blanks and generated labels do not. On the
display a line or strip figure grows one line or strip a step, and an exit ticket prints its figure on the ticket.
Three words set what each page shows. `then` starts the lines or strips that are the answer: the
student page and the display's question screen stop before it, the key and the last step show all
(`line d=5 pt=2/5 / then d=5 sub=2 pt=4/10`, `fstrip 8/12 then 4/6 2/3`). `ask=N` prints only the first N lines
or strips on the student page and the question screen (`fstrip 6/8 1/2 ask=1`). `by=` sets the display, one entry
a screen, the question screen first and then one per step: a number of lines or strips, `-` none, `*` all, the last
entry carried on (`by=1,1,2,*`). With no `by=`, a figure with `then` or `ask=`, or a worked example whose later
lines carry points, opens with the lines it asks about (one line in the second case) and adds one a step from the
first step that says cut, draw, fold, sketch or circle, all by the last step; the question screen never shows the
answer's line. A strip of more than 24 parts prints as thin lines with a heavy line every 10 parts, so tenths of a
hundred count by eye. On the student page a line figure's words and whole numbers print at 14 point (its
fractions stay at the figure's size, so the page keeps to two sides).
A tile figure is `tiles #/# ##/##`: rows split by `/`, `.` a gap, `sticks` for outlines.
`steps` (the worked steps as the teacher says them, split by `|`; for a wrong answer to fix, their working then
the right working; a teacher-judged row lists its look-fors here), `samples` (a teacher-judged row's two sample
answers, one meeting the look-fors and one not, shown on the key), `path` (an exit's `tool` or `paper`; `board`
for a practice row written on the board when there is no printer; `spoken` for an exit or check item asked aloud with
picture cards and never printed for the child, kindergarten, 2026-11-18) and `source` (rule 4). In wrongs.csv, error `x`
is any other wrong answer, with no group.

The file starts with a header block: `day`, `course`, `unit`, `version` ("draft, not yet taught" until a taught
run), `materials`, `print`, `credit` (see rule 4) and `leans_on`: every outside piece the day needs, by path (the
tool, the section opener, a sheet from another unit, the record sheet), or "nothing". The check fails a day whose
piece is missing unless its version says "not ready", and the build then prints "Not ready to teach: <piece>
missing" at the top of the teacher page. A piece that does not exist yet and is not needed to teach the day is
written `when it exists: <path>`; the check skips it, the header prints it as "Uses when it exists", and the
prose must say what the day does until it exists. The record sheet's own header (not a day file's) may carry
`exitlooks: 7;8`, which gives a judged exit one tick a look-for. A unit whose end items are judged by component
(social studies) adds `endlooks: 012`: each teacher-judged end item then takes one column a look-for, headed by
its id (A1, A2, ...), and the sheet prints the 2, 1, 0 rule.

## The teacher page, in this order

Fixed headings, so a script can find each part and a teacher always finds it in the same place.

1. **The header** (generated): day, section, kind of day, goal in student words, the parts of the standard, the tool
   and its mark, materials, what to print, version, credit.
2. **Before class.** Set-up only: what to print, what to open, what to lay out. 80 words at most.
3. **The day.** One part per block of time, headed with its minutes: `#### 10 min. Teaching first`. The minutes
   add up to the length of the day (60 in grade 4 math, DEFAULTS.md) and agree with `days.csv`. Each part says
   how students work (alone, pairs, groups, whole class), what the teacher does, what students do, what to watch
   for, and what to do if many get it wrong (from the error register). Wording is written out only where the
   words matter: the steps of a worked example (from the row, `[[steps:id]]`), and the planned questions, each
   marked **Ask.** with the answers to expect and the order to show them in. Everything else is told, not
   scripted. An action counted out ("say four pairs aloud", "read six comparisons") lists the pairs or
   comparisons it counts, so the teacher does not invent them in front of the class and the reserve sees them.
   An Ask that belongs inside a worked example says "after step N": its screen waits for that
   step on the display.
4. **Other rooms.** The paper path when there are no devices, no printer, one projector: only what differs from
   the course's DEFAULTS.md. Every day has a paper path. When the day's tool is planned but not built, the paper
   path is written as fully as the tool path: what students do, how they check, what to watch for. One child at
   home is not here: it has its own block, next.
5. **At home.** The same day for one parent and one child (see "The At home block" below). Required on every day.
6. **Shorter or longer.** What to cut when time runs short without making the work easier, and the extension,
   on the same standard.
7. **Words and supports.** The key words, with their Word Wall card ids where the topic has cards (never a line
   saying none are supplied), the sentence frames, and any access note: only what differs from the section opener.
8. **Tomorrow.** What the exit tells the teacher, and what changes the next day because of it, naming the sign
   of each error on both exit paths. A fix-it named by its pupil (Kai, Mia) is handed on by its sum or difference, not
   by the name, since the names come back on later days with other errors. The hand-off is two-sided: the next day's file carries an "If many ...
   day N's exit" line (or an "If day N's tickets showed ..." branch) that acts on it, and the gate checks it,
   finding the next day by number in any section folder of the course. On an assessment day, a display line
   `Check: ...` shows each row with its answer; `Check (sort): ...` shows only the kind (the answer's first part).
9. **Credit.** See rule 4. A day that adapts nothing has the header `credit: ours`, exactly.

**Teacher prose names errors and sources in words.** Write "error C" and "Source C", never a bare "(C)":
error letters and source letters share the alphabet (the gate fails a bare letter in a course with sources).
**No writer's placeholder reaches a page.** "[to cut]", "[to check]", "[to add]", "[to make]" and "[image:" fail
on a day and on every piece; cut what cannot be finished. **A repair never cuts the next day's worked example.**
The warm-up carries it, and a small group during the pairs or alone part takes what does not fit. **Hand-backs
follow handbacks.csv:** a row routes an item past the next day (a writing day between); its letters are that
later day's to pick up. **A writing day's student page gives the revision note its own box.**

## The student page

- The goal in student words. The build prints the name and date line; never type one (the gate fails it).
- Frames to fill during the worked examples, so copying the model is part of the page. A frame on the
  teacher page under Words and supports is printed on the student page too.
- Room to write: every question that asks for a sketch has a box (`{sketch}`, or `{small}` for a short fix);
  every "show your working" has `{work}`.
- Then the day's questions in the order they are used, each pulled from data, with room to write.
- Warm-up questions are rows too, so the key and the reuse gate see them. A printed sentence frame sits under
  the question it belongs to, and list numbers carry on across a side (no two items 1 on one side).
- Tables print at the page's own type size (14 point); a day that will not fit two sides trims, not the type.
- Strip pictures that are compared side by side share one scale (`scale=N` on each strip figure).
- An exit ticket that asks for a strip picture prints a box for it; a teacher-judged ticket item gets a tall box.
- No answers printed. No score or rank; no timer without a grounded purpose (BASELINE rule 30). Black and white, readable with no colour.
- A large-print version (18 point) is generated from the same file. It may run longer than two sides; the
  two-side rule is for the standard page only.
- Instructions a student reads are short sentences in plain words; numbers are written as numerals.
- A stem with parts prints each of (a), (b), (c) on its own line, on the page and on the ticket.
- An exit ticket gives each sentence of its stem the room it asks for: a blank to fill is the room for its
  sentence, a "why" or "how do you know" gets two lines, a question or a "write" gets one, and a stem that says
  show, rename or explain gives every part a line.
- A stem holds only what the student reads: no "No drawing." or "No line given." (that goes on the teacher page),
  no quote marks round the student text, no description of the figure printed beside it.

## The At home block

Every day carries one, under `### At home` on the teacher page, built from the same day: same goal, same items,
fewer of them. It is written to a parent with no teacher training, who reads it the night before and teaches one
child at the table. The build turns it into the At home view of the day page (`dNNN-home.html`): the goal and the
minutes, the block, then every question it names with its answer, pulled from data. It is not printed on the
teacher page. Because the student page already holds the questions, the block only says which ones, what to say and
what to swap; on grade 4 math days 89 to 93 it took 110 to 137 words.

- **Minutes.** 30 to 40 on a teaching day. On an assessment day, the assessment alone, then the respond part one
  to one, about 45 in all (40 to 50). A course whose day is under 45 minutes (kindergarten, 20 to 30) keeps home to the
  class day: 5 minutes under its shortest to its longest on a teaching day, its shortest to 10 over its longest on an
  assessment day (kindergarten probe, 2026-11-18).
- **Parts**, written `- **N min. Name.** ...`, in the order of the day: the minutes and the name inside one pair of
  `**`, on one line. The closing period may be left off, and a name may end in "?" or "!". The check names any part
  line it cannot read. Their minutes add up to the total; there is no other place the total is written.
- **Items by name.** Each question is named by its id, `[[s11-P90-1]]`, and must be on that day's student page
  (or the day's paper exit ticket). The view prints it by where it sits ("On your own 1 (side 2)"), so the parent
  finds it on the page in the child's hands. A bold label ending in ".", "?", "!" or ":" names the group below it,
  across the side break, until the next label; a label with its own question ("**Example 2.** [[id]]") names only
  that question. A question in a table row with no number is found by its table and row ("Bo's stamps, row 2"), so
  a table needs no numbers for the At home block to name its rows. Fewer items than the class, never other ones.
- **Say.** Wherever the class version has pairs or whole-class talk, at least one `**Say.**` line (indented under
  its part) gives the parent's words in quotes and the answer to expect (`Expect: ...`). The parent is the partner.
- **Swap.** One `**Swap.**` line, above the parts, for each thing a home lacks that the day's materials name: no
  projector (point at the page), no grid paper, no tiles, no class set, no device.
- **Skip.** One `**Skip.**` line: what the class does that home leaves out (the facts check, the tool, a third
  rectangle, the groups).
- **The exit ticket last** on a teaching day, naming the paper ticket's rows. The child answers alone.
- **Cap.** 170 words, counted apart from the 900-word teacher prose cap.
- **Plain words.** No teacher terms without a gloss, no timer without a grounded purpose, no grades or scores.
- **The view** gives a worked example's steps and a judged row's look-fors, names a question inside an example
  "Example 2, question 3", and on an assessment day names every assessment item.

## Assessment days

An assessment day ships a shorter teacher page (the run of the day, the accommodations, how marking and the respond
half go), the check itself as the student page (generated from data), its key and the record sheet. No exit ticket:
the check is the evidence.

## Rules every day keeps

1. **Facts in data.** Every question is a row with a computed key (rule 27). A key the script cannot reproduce
   fails the build. This includes the items a tool asks on its own: a tool's exit items are rows with `check` =
   `exit` and `path` = `tool` (the ticket's rows have `path` = `paper`). Both paths ask the same parts with
   different numbers, so the record sheet's column means the same thing in every room.
2. **The minutes add up** to the day and agree with the plan's row.
3. **Every number is new.** The worked examples, the tool's notes and the practice questions are "taught"; no exit
   question or check item may use the same numbers, and a generator refuses them.
4. **Credit on the lesson.** Only CC BY (any version), CC0 or public domain material may be adapted, because
   Curio Class content is CC BY 4.0. Anything with NonCommercial, ShareAlike or NoDerivatives terms may be read to
   learn, never adapted, and "informed by" means no wording, task sequence or problem context taken over. An
   adapted item carries its credit in its row's `source` cell (title, author, licence with link, what we changed,
   in the form the licensor asks for), and every built piece that prints the item prints the credit at its foot.
   A name or logo the licence excludes appears only in the credit line. A day adapted as a whole says so in its
   `credit` header.
   **A day adapted from a base text (docs/sources/BASE-TEXTS.md) carries one short credit and no more** (settled
   2026-11-13, see DESK-ANSWERS). The `credit` header, printed once in the foot, reads:
   `Adapted from Illustrative Mathematics K-12 Math, grade 4, unit 3, lessons 7 and 8, CC BY 4.0,
   https://creativecommons.org/licenses/by/4.0/. Changed by Curio Class.` The teacher page's Credit section says
   the same in one line. Rows taken from that lesson do not repeat it in `source`. The source's name appears
   nowhere else (`lesson.py check` fails on it). Sources read only to learn are named under Credit as "informed by". A day that is all ours
   says so. Texts, images and other material used but not adapted have their own rights record (data/plans/ela-texts.csv
   for ELA), and the probe in that subject sets its rule here.
5. **It stands alone.** A teacher who has read the section opener can teach the day from its teacher page. Nothing
   says "see the plan".
6. **The tool is named by its own words** (its modes and screens), with the minutes it gets and the point to stop
   at, and the paper path does the same job.
7. **No purposeless timer, no rank, nothing leaves the room.** A timer is shown to a student only with a grounded
   purpose (a pace cue, a movement game, classroom management; BASELINE rule 30); results live on the record
   sheet and in score codes.
8. **An item id is never reused for different numbers.** A changed item gets a new id, and the day's version goes
   up.

## Shelves and sub days

A day names each shelf item it uses (Word Wall card, chart, worksheet row, generator preset, game) by id, and the
gate fails on an id that does not exist (settled 2026-11-12, see DESK-ANSWERS, card `q-shelves-in-courses`). Not
built into `lesson.py` yet; it comes with the section 11.1 shelf pieces (later.csv L13). A course has one sub-ready day per unit, written with the unit (docs/SITE-DESIGN.md);
the per-tool Sub Day packets stay on the shelf. The Reading Room is not where course texts come from below the
higher grades: K-8 anchors on newer texts, mostly our own (settled 2026-11-12, see DESK-ANSWERS, card
`q-course-texts`).

## What the script checks

`python -X utf8 scripts/lesson.py check` runs `plan.py check` and fails a day on what follows. Items marked "note"
are reported and do not fail. It cannot judge whether the day teaches; the expert and people do that.

**The header and the teacher page.** A missing header field or heading, or a heading with nothing under it; a
`leans_on` piece missing on a day not marked "not ready"; a "when it exists" piece the prose does not explain, or
one that exists; minutes that do not add up to the day or disagree with `days.csv` (the parts after the warm-up
must sum to the plan's lesson minutes, and an assessment day's parts follow its `check_min`); a prose cap passed; a
bold `**Ask**` not written `**Ask.**` (the build reads both, and holds a fix's right working until an Ask later in
the same part); `Check:` written mid-line; "after each set" with fewer `Check:` lines than sets; a partner check with
no `Check:` line or peer key; a part that says the display shows the answers ("answers on the display", "the
answers on the screen") with no check named; a warm-up with no row; grid paper used in a part and on neither the
materials nor the print line, or the column sheet used and not printed; a section whose opener sends the family note
home on a day that does not print it; an adapted credit or `source` with no licence or link, or with
NonCommercial, ShareAlike or NoDerivatives terms. Notes: "under the camera" on a day with no document camera; a
strip, card or sheet handled and not listed; a "from day N" material day N never names; an opener sheet listed for
the day that the day never names; the student page running in another order than the day (unless the part says to
turn back).

**Tomorrow and the next day.** A Tomorrow that the next day's file does not pick up; an error letter or "near you"
in Tomorrow that the next day does not name; a teacher-judged practice row the next day does not hand back (unless
its pages stay with students); an assessment day with teacher-judged items when the next day's file never names
"day N's assessment" or "day N's items"; an "If many X" branch on a ticket whose exit has no wrong answer for X.
Note: a fraction Tomorrow says day N+1 uses that it does not.

**The At home block.** A day with no At home section ("At home block missing"); parts that do not add to 30 to 40
minutes (40 to 50 on an assessment day); an `[[id]]` in it that is not on the student page or the paper exit ticket;
no **Say.** line on a day whose The day has pairs or class talk, or a Say. line with no "Expect"; no **Swap.** line
when the materials name a projector, grid paper, tiles, a device or a string loop; no **Skip.** line; on a teaching
day a last part that is not the exit ticket or does not name its rows; on an assessment day a first part that is not
the assessment; a timer, grade or score; the 170-word cap; and "One child at home" left in Other rooms. `HOME_TODO`
in `lesson.py` lists any sections whose days report the missing block as a note instead of a failure while they are
backfilled.

**The student page and the ticket.** The student reading cap passed (frame and questions together); a question
sentence over 15 words in grades 3 to 5; two numbered questions on one source line; repeated list numbers on a
side; a sketch asked for with no box (a `[[fig:]]`, a {sketch} box or the strip sheet; the goal line and bold labels
are not read as asking); a table too wide for its page (under half an inch a column); a student table of only ■
cells (draw an `fstrip`); a student line that runs a blank or a number into a fraction ("___/15   4/5"), which
prints as a mixed number; a Words and supports frame missing from the side it names; a paper exit with no room to
write; compared strips with different scales; a student page that prints to more than two sides (counted on the
printed page whenever Chrome is present, and the output says so when it was skipped).

**Rows and numbers.** An `[[id]]` with no row, or a row for the day that no page uses; a keyed row with no computed
key; a reused set of numbers; a figure number missing from its stem; a teacher-judged row with no look-fors or
samples. `plan.py check` adds: duplicate stems; challenges with the same numbers, or whose one fraction matches; the
course's word rules in `words.csv`; a stem that starts "No drawing", "No line given", "No strips" or "No grid";
student text in quote marks beside other words; a wrong answer for H that is not a left-to-right running value; a
sentence-shaped wrong answer on an exit that asks for no sentence; an exit or check item whose given number is a
taught step's result for the same fact (the fact turned into its answer); a check or exit part that prints both
fractions of an equality a taught row names (stem, answer or `F()` terms, either order, by the exit's day); an end
item whose stem list shares three or more numbers (10 or more) with one taught list; a difference with one
ungrouping whose two errors (smaller from larger, the small 1 only) give one answer, or, past the day both are
taught, a row keying only one of them; a day that names a tool with no tool rows. Notes from `plan.py check`: an exit
whose carries fall where the day's worked example's do; a fix on a worked example's numbers; a row coded to a
standard the scope and sequence teaches later; an exit or end row that asks why or to explain but is keyed, not
judged; a comparing section's register letter no comparing end item has a wrong row for; one shown value under two
letters on a check item. A fraction rule's multiplications are not area facts, and the "same answer" note skips
answers that are only True or False.

**What the build does with them.** The display: a fix shows the stem, the picture and their working, then, after the
class answers the Ask (or at the fix's `[[steps:id]]`), their working beside the right working, one step a line; a
warm-up's questions get a screen before "Check your answers"; that screen says an equal name is right, and that a
sign is right when it reads true as a sentence, when the answers hold fractions or signs; a check screen says "Your
feature may be different" when rows ask for a feature; a group screen is headed "Find your group." and shows only
what students match and the first task. The key lists the assessment rows first, then rows in the order the student
page meets them (the warm-up first), names an error without its example, prints a strip or fraction figure in a
full-width row under its item, and on a fraction day says any right grouping or cut is right and a name need not be
the smallest. The key's opening line is the equal-forms note only on a day with an equation, the estimate rule on a
day of estimates, and the feature and reason rule on a 4.OA.C.5 day. A line or strip figure on a check piece prints
under its item, with an answer line in place of the work box.

**How days are read.** Every day by the gates; a sample of days per section by the expert; the whole of the first
section in each course by a teacher, in a taught run.

**Known gaps in the gates** (expert finding 8, for the taught run): a compute cell that only restates its answer;
error letters named in prose not checked against the register; sub-minutes inside a part not checked against the
part; the order of parts against the plan's row (only their minutes are checked); a rendered page's empty space
(the two-side count is checked, not wasted height); numbers in the section opener's prose against the reserve.
The same fact turned round (two sides with their area or perimeter, in any order) is caught by the reserve,
on every row and in the generator.

## What changes by subject

The shared shape (one file a day, fixed headings, minutes tied to the plan, a paper path, questions as rows, no
slides) holds everywhere. Known now to differ:

- **Judged items.** Facts in data holds everywhere, but an item judged by a person carries look-fors and two
  sample answers instead of a computed key, and a note telling a language gap from a content gap.
- **New on a check.** Rule 3 is, in general, "nothing on a check is a taught item": new numbers in math, a cold
  text in ELA, a new situation in science, an unseen source in social studies.
- **Caps run per minute.** 15 words of teacher prose a minute of the day (900 at 60 minutes, 750 at 50, 1,350 for
  a 90-minute literacy block); `lesson.py check` reads the day's length from the course's frame. An assessment day
  keeps 500 unless it carries a revision part or scores a product made on earlier days (a handbacks.csv row with
  `where` = `assessment` into it); then it takes the teaching cap. "Before class" and the student reading cap are set
  in each course's DEFAULTS.md.
- **Science** adds a required "Safety and set-up" heading (materials per group, set-up the day before, clean-up
  minutes) and a data sheet.
- **ELA** prints the text as its own piece, outside the two-side limit, with its rights line; a writing day
  prints a lined page outside it too.
- **Social studies** (settled by the us-history-i probe, 2026-11-15) prints each day's primary sources as its own
  piece (`sources-78.md`, `piece: blank`), outside the two-side limit like an ELA text, with a rights line under
  each source. Its rights record is `data/plans/<course>/sources.csv` (data/plans/README.md): rule 4's "own rights
  record" for this subject. There is no base text, so every day is ours and says so in its `credit` header; a
  modern interpretation under copyright is paraphrased in our words and attributed, never quoted. Exits and essay
  tasks are judged by the teacher (look-fors and samples), and an organizer a student completes is a practice row.
  Day-level parts are read from the section plan's `- **N min. Name.**` lines.
  Settled by the world-history-i probe (2026-11-15): **new by situation.** A judged exit is not its worked example
  with the nouns swapped; it gives a fresh stimulus (a short invented note, an unseen source) and asks the day's
  move on it. **A respond day's practice or exit** works a parallel case or a second source, never a redo of the
  returned item whose key was read. **Scale.** A look-for never asks for a scale on a sketch the day labels not to
  scale; it asks for the label or the journey times a source gives. **A product scored from collected work** prints
  under its stem "Scored from the work you handed in. Write nothing here." **Rotated forms** (three word sets, three
  sources) each get their own key line or row. **Words and supports** glosses only words the day's talk or items
  use; a word coded to the day is used in an Ask or a look-for, not left on the list. **A reserved source** (sources.csv
  `use` = `reserved`) is named in no day before its own; its note lists the words to watch (`watch: Taghaza`), and
  `lesson.py check` fails a day that names one.
- **Runs of days.** A day may belong to a run (`continues: d091`), so an investigation or the writing process is
  not forced into one sheet.

## Not decided here

- Spanish student pages (ROADMAP, finished course item 14: Cory's in or not-now).
- An accessibility conformance level for print (item 10: Cory's).

## The worked case: day 90

Day 90 is written to this page: [courses/math-4/u11-1/d090.md](../../courses/math-4/u11-1/d090.md), its rows in
`data/plans/math-4/items.csv` (ids starting `s11-` with `90` in them; the tool's five family notes are rows
`s11-T90-1` to `5`), and its built pages in `build/lessons/math-4/u11-1/` (teacher, student, large print, key, exit
tickets, display, and `d090-home.html`). Counts: teacher prose 879 words, At home 128 words and 40 minutes, student
page 247 words a student reads (98 frame, 149 questions), 60 minutes, student page two sides. The two worked
examples, written out as the teacher says them, take about 200 of the teacher's words. Version "draft 2, not ready,
not yet taught": the tool (spec only, so the paper path is the only one that can be taught today), the section opener
(it holds the reteach the day points to), the facts check part 2 sheet (unit 1's, still to make) and the record sheet
do not exist yet.
