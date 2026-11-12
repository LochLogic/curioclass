# The lesson day: what one teaching day ships as

Draft 2, 2026-11-12. Written against day 90 of grade 4 math (pilot unit 11.1), which is the worked case at the
end. BASELINE rule 27 points here. **Approved by Cory, 2026-11-12: this sets the shape of about 15,000 lesson
days.** The curriculum expert read draft 1 cold (docs/reviews/lesson-day-2026-11-12.md); draft 2
makes its seven "before the yes" changes. **Proved on grade 4 math only** until the ELA and science pilots run.

A unit plan says what each day is for. This page says what a teacher and a student hold in their hands on that
day, how big each piece may be, and which pieces are written and which are generated. The shared shape holds for
every subject; "What changes by subject" below lists what is known to differ, and the first pilot in each subject
adds the rest.

## What one day ships as

| Piece | Who reads it | Made how | Size |
|---|---|---|---|
| **Teacher page** | The teacher, the night before | Written, plus a header and tables generated from data | 900 words of prose at most on a teaching day, 500 on a check day. Generated tables do not count |
| **Student page** | Each student | Written frame; every question pulled from data | One sheet, both sides of US Letter at most. Words a student reads counts everything printed for the student, questions included; the cap is set per course in DEFAULTS.md (grade 4 math: 350, ours, untested), and the gate reports frame and questions apart. No sentence over 15 words in grades 3 to 5. 18 point type in kindergarten to grade 2, with a line telling the teacher what to read aloud; 14 point in grades 3 to 5; 12 point from grade 6 |
| **Exit slip** | Each student, then the teacher | Generated from data: the paper path's exit rows | A quarter page, four to a sheet |
| **Key** | The teacher | Generated from data: every answer on both exit paths, its equation or working, and what each wrong answer means | Usually one side |
| **Display page** | The class, on the projector | Generated from data, in the order the teacher page runs, part by part. For each worked example, the question with its labelled figure, then the steps one screen at a time; for each wrong answer to fix, their working beside the right working; one screen per **Ask.**; a challenge screen; the answers to a plain sum; a "check your answers" screen only where a part names a partner or self check (a `Check: ...` line in the part gives its sentence); on a check day, the answers screen and one screen per group in the respond part; the sentence frames last | No words of its own |
| **Slides** | Nobody | **None.** The display page and the tool's own screen do this job; a slide deck would be a second copy of the teacher page to write and keep right | 0 |
| **Materials** | The teacher | A line in the header: per student, per class, what to print and how many, and the stand-in for a room without it ("no document camera: draw it on the board") | Part of the header |

**Every built piece prints a foot line:** "Curio Class, grade 4 math, day 90, version <v>, CC BY 4.0,
curioclass.org", and the credit of any adapted item it prints (rule 4), so last year's photocopy can be matched to
today's key and a reuser can see whom to credit.

**Once per unit** (not per day): the unit opener (the teacher page for the unit: the math explained at an adult's
level, why this model, the error register in plain words, the supply list; 1,200 words at most), the family note in
English and Spanish (150 words at most each), the record sheet, the readiness check and end check with their keys,
and any generator sheet the plan defines. A sheet with no preset questions (a strip sheet, a blank grid) is a
`piece: blank`: it prints for students, its words are counted without markup, and it must fit two sides. These
are generated from data wherever they can be.

**The arithmetic, so the size is seen.** A teaching day is at most about 1,250 words a person reads (900
teacher, 350 student, questions included), of which only the teacher prose and the student frame are written
free: day 90 has about 1,000 such words. At about 150 days a course and 105 courses that is about 16 to 20
million words, before checks and unit openers. The cost is in the reading as much as the writing (see "How days
are read"). The caps hold it down; the pilot's real counts go in docs/pilots/COST.md.

## Where it lives

One source file a day: `courses/<course>/u<stretch>-<unit>/d<day>.md` (day 90 of grade 4 math is
`courses/math-4/u11-1/d090.md`). The teacher page and the student page are both in it, so they cannot drift apart.
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
`steps` (the worked steps as the teacher says them, split by `|`; for a wrong answer to fix, their working then
the right working; a teacher-judged row lists its look-fors here), `samples` (a teacher-judged row's two sample
answers, one meeting the look-fors and one not, shown on the key), `path` (an exit's `tool` or `paper`; `board`
for a practice row written on the board when there is no printer) and `source` (rule 4).

The file starts with a header block: `day`, `course`, `unit`, `version` ("draft, not yet taught" until a taught
run), `materials`, `print`, `credit` (see rule 4) and `leans_on`: every outside piece the day needs, by path (the
tool, the unit opener, a sheet from another stretch, the record sheet), or "nothing". The check fails a day whose
piece is missing unless its version says "not ready", and the build then prints "Not ready to teach: <piece>
missing" at the top of the teacher page. A piece that does not exist yet and is not needed to teach the day is
written `when it exists: <path>`; the check skips it, the header prints it as "Uses when it exists", and the
prose must say what the day does until it exists.

## The teacher page, in this order

Fixed headings, so a script can find each part and a teacher always finds it in the same place.

1. **The header** (generated): day, unit, kind of day, goal in student words, the parts of the standard, the tool
   and its mark, materials, what to print, version, credit.
2. **Before class.** Set-up only: what to print, what to open, what to lay out. 80 words at most.
3. **The day.** One part per block of time, headed with its minutes: `### 10 min. Teaching first`. The minutes
   add up to the length of the day (60 in grade 4 math, DEFAULTS.md) and agree with `days.csv`. Each part says
   how students work (alone, pairs, groups, whole class), what the teacher does, what students do, what to watch
   for, and what to do if many get it wrong (from the error register). Wording is written out only where the
   words matter: the steps of a worked example (from the row, `[[steps:id]]`), and the planned questions, each
   marked **Ask.** with the answers to expect and the order to show them in. Everything else is told, not
   scripted.
4. **Other rooms.** The paper path when there are no devices, one projector, one child at home: only what
   differs from the course's DEFAULTS.md. Every day has a paper path. When the day's tool is planned but not
   built, the paper path is written as fully as the tool path: what students do, how they check, what to watch
   for.
5. **Shorter or longer.** What to cut when time runs short without making the work easier, and the extension,
   on the same standard.
6. **Words and supports.** The key words with their Word Wall cards, the sentence frames, and any access note:
   only what differs from the unit opener.
7. **Tomorrow.** What the exit tells the teacher, and what changes the next day because of it, naming the sign
   of each error on both exit paths. The hand-off is two-sided: the next day's file carries an "If many ...
   day N's exit" line (or an "If day N's slips showed ..." branch) that acts on it, and the gate checks it,
   finding the next day by number in any unit folder of the course. On a check day, a display line
   `Check: ...` shows each row with its answer; `Check (sort): ...` shows only the kind (the answer's first part).
8. **Credit.** See rule 4.

## The student page

- A name and date line, then the goal in student words.
- Frames to fill during the worked examples, so copying the model is part of the page. A frame on the
  teacher page under Words and supports is printed on the student page too.
- Room to write: every question that asks for a sketch has a box (`{sketch}`, or `{small}` for a short fix);
  every "show your working" has `{work}`.
- Then the day's questions in the order they are used, each pulled from data, with room to write.
- No answers printed. No timer, score or rank. Black and white, readable with no colour.
- A large-print version (18 point) is generated from the same file.
- Instructions a student reads are short sentences in plain words; numbers are written as numerals.

## Check days

A check day ships a shorter teacher page (the run of the day, the accommodations, how marking and the respond
half go), the check itself as the student page (generated from data), its key and the record sheet. No exit slip:
the check is the evidence.

## Rules every day keeps

1. **Facts in data.** Every question is a row with a computed key (rule 27). A key the script cannot reproduce
   fails the build. This includes the items a tool asks on its own: a tool's exit items are rows with `check` =
   `exit` and `path` = `tool` (the slip's rows have `path` = `paper`). Both paths ask the same parts with
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
   `credit` header. Sources read only to learn are named under Credit as "informed by". A day that is all ours
   says so. Texts, images and other material used but not adapted have their own rights record (texts.csv for
   ELA), and the first pilot in that subject sets its rule here.
5. **It stands alone.** A teacher who has read the unit opener can teach the day from its teacher page. Nothing
   says "see the plan".
6. **The tool is named by its own words** (its modes and screens), with the minutes it gets and the point to stop
   at, and the paper path does the same job.
7. **No countdown, no rank, nothing leaves the room.** No timer is shown to a student; results live on the record
   sheet and in score codes.
8. **An item id is never reused for different numbers.** A changed item gets a new id, and the day's version goes
   up.

## What the script checks

`python -X utf8 scripts/lesson.py check` fails a day on: a missing header field or heading, or a heading with
nothing under it; minutes that do not add up to the day or disagree with `days.csv` (the parts after the warm-up
must sum to the plan's lesson minutes, and a check day's parts follow its `check_min`); a Tomorrow that the next
day's file does not pick up; two numbered questions on one source line; a sketch asked for with no box (a `[[fig:]]`, a {sketch} box or the strip sheet; the goal line and bold labels
are not read as asking); a table too wide
for its page (under half an inch a column); a "when it exists" piece the prose does not explain; a figure number
missing from its stem; a teacher-judged row with no look-fors or samples (from `plan.py check`, which also
checks duplicate stems, challenges with the same numbers and the course's word rules in `words.csv`); a prose cap passed, or the
student reading cap (frame and questions together); a question sentence over 15 words in grades 3 to 5; an
`[[id]]` with no row, or a row for the day that no page uses; a keyed row with no computed key (from `plan.py
check`, which it runs); a reused set of numbers; a `leans_on` piece missing on a day not marked "not ready"; an
adapted credit or `source` with no licence or link, or with NonCommercial, ShareAlike or NoDerivatives terms; a
student page that prints to more than two sides (counted on the printed page whenever Chrome is present, and the
output says so when it was skipped). It cannot judge whether the day teaches; the expert and people do that.

**How days are read.** Every day by the gates; a sample of days per unit by the expert; the whole of the first
unit in each course by a teacher, in a taught run.

**Known gaps in the gates** (expert finding 8, for the taught run): a compute cell that only restates its answer;
error letters named in prose not checked against the register; sub-minutes inside a part not checked against the
part; the order of parts against the plan's row (only their minutes are checked); a rendered page's empty space
(the two-side count is checked, not wasted height); numbers in the unit opener's prose against the reserve.
The same fact turned round (two sides with their area or perimeter, in any order) is now caught by the reserve,
on every row and in the generator.

## What changes by subject

The shared shape (one file a day, fixed headings, minutes tied to the plan, a paper path, questions as rows, no
slides) holds everywhere. Known now to differ:

- **Judged items.** Facts in data holds everywhere, but an item judged by a person carries look-fors and two
  sample answers instead of a computed key, and a note telling a language gap from a content gap.
- **New on a check.** Rule 3 is, in general, "nothing on a check is a taught item": new numbers in math, a cold
  text in ELA, a new situation in science.
- **Caps run per minute.** 15 words of teacher prose a minute of the day (900 at 60 minutes, 1,350 for a
  90-minute literacy block). "Before class" and the student reading cap are set in each course's DEFAULTS.md.
- **Science** adds a required "Safety and set-up" heading (materials per group, set-up the day before, clean-up
  minutes) and a data sheet.
- **ELA** prints the text as its own piece, outside the two-side limit, with its rights line; a writing day
  prints a lined page outside it too.
- **Runs of days.** A day may belong to a run (`continues: d091`), so an investigation or the writing process is
  not forced into one sheet.

## Not decided here

- Spanish student pages (ROADMAP, finished course item 14: Cory's in or not-now).
- An accessibility conformance level for print (item 10: Cory's).
- (Decided 2026-11-12, card `q-shelves-in-courses`.) How a day uses the older shelves: a day names each shelf
  item it uses (Word Wall card, chart, worksheet row, generator preset, game) by id, and the gate fails on an id
  that does not exist. Not built into `lesson.py` yet; it comes with unit 11.1's shelf pieces. A course day's Sub
  Day packet is generated from the day itself. The Reading Room is not where course texts come from below the
  higher grades: K-8 anchors on newer texts, mostly our own (card `q-course-texts`).

## The worked case: day 90

Day 90 is written to this page: [courses/math-4/u11-1/d090.md](../../courses/math-4/u11-1/d090.md), its rows in
`data/plans/math-4/items.csv` (ids starting `s11-` with `90` in them), and its built pages in
`build/lessons/math-4/u11-1/` (teacher, student, large print, key, exit slips, display). Counts (draft 2):
teacher page 898 words of prose, student page 247 words a student reads (98 frame, 149 questions), 60 minutes,
student page two sides. Version "draft 2, not ready, not yet taught": the tool, the unit opener, the facts check
sheet and the record sheet do not exist yet.

### What day 90 showed

1. **The plan's day left 15 minutes unplanned.** Its row gave 10 minutes of teaching and 25 of tool, 35 of the
   50-minute lesson. Writing every minute down found it. The day now adds 15 minutes on paper (fix the two
   wrong answers the error register puts on day 90, then two missing sides alone, checked by a partner) and 5
   minutes pulling the two halves together. The plan's row in `days.csv` was changed to match.
2. **900 words is tight but holds.** The first draft was 1,074; it was cut to 880 without losing a part. The two
   worked examples, written out as the teacher says them, take about 200.
3. **The page gate earns its place.** The first build of the student page ran to three sides.
4. **The tool's numbers are now checked too.** Its five family notes are rows (`s11-T90-1` to `5`), so the
   no-reuse gate covers them; before, they lived only in the tool's spec.
5. **The day leans on three things that do not exist yet:** the tool (spec only, so the paper path is the only
   one that can be taught today), the unit opener (it holds the reteach the day points to), and the facts check
   part 2 sheet (stretch 1's, "still to make").
6. **Large print runs longer than two sides.** The two-side rule is for the standard page only.
7. **The cold read found what the gates could not** (draft 2): the display carried no pictures, the tool's exit
   was outside the data (and one of its items tested nothing on the day's goal), a day could look ready while
   leaning on missing pieces, the student reading count left out the questions (98 words became 247), and the
   exit's answer was 9, the same as the worked example's. Each is now a rule or a gate.
8. **Room to write costs space.** Writing boxes for the fixes and "On your own" pushed the page to four sides;
   the expert's fix (the Plot notes table shows the family and the numbers given, which is all a student needs to
   solve it; the full note stays in the tool and the key) brought it back to two.
