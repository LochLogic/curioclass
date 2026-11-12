# The lesson day: what one teaching day ships as

Draft 1, 2026-11-12. Written against day 90 of grade 4 math (pilot unit 11.1), which is the worked case at the
end. BASELINE rule 27 points here. **Not yet approved: Cory says yes once, because this sets the shape of about
15,000 lesson days.** The curriculum expert reads it first.

A unit plan says what each day is for. This page says what a teacher and a student hold in their hands on that
day, how big each piece may be, and which pieces are written and which are generated. It holds for every subject;
where a subject needs something else (ELA texts, science materials) the first pilot in that subject adds it here.

## What one day ships as

| Piece | Who reads it | Made how | Size |
|---|---|---|---|
| **Teacher page** | The teacher, the night before | Written, plus a header and tables generated from data | 900 words of prose at most on a teaching day, 500 on a check day. Generated tables do not count |
| **Student page** | Each student | Written frame; every question pulled from data | One sheet, both sides of US Letter at most. 250 words a student reads, not counting the questions. 14 point type in grades 3 to 5, 12 point from grade 6 |
| **Exit slip** | Each student, then the teacher | Generated from data | A quarter page, four to a sheet |
| **Key** | The teacher | Generated from data: every answer, its equation or working, and what each wrong answer means | Usually one side |
| **Display page** | The class, on the projector | Generated: the worked examples, the wrong answers to fix and the planned questions, one to a screen, large type | No words of its own |
| **Slides** | Nobody | **None.** The display page and the tool's own screen do this job; a slide deck would be a second copy of the teacher page to write and keep right | 0 |
| **Materials** | The teacher | A line in the header: per student, per class, what to print and how many, and the stand-in for a room without it | Part of the header |

**Once per unit** (not per day): the unit opener (the teacher page for the unit: the math explained at an adult's
level, why this model, the error register in plain words, the supply list; 1,200 words at most), the family note in
English and Spanish (150 words at most each), the record sheet, the readiness check and end check with their keys,
and any generator sheet the plan defines. These are generated from data wherever they can be.

**The arithmetic, so the size is seen.** A teaching day is about 1,150 written words (900 teacher, 250 student).
At about 150 days a course and 105 courses that is about 18 million words, before checks and unit openers. The
caps are there to hold that down; the pilot's real counts go in docs/pilots/COST.md.

## Where it lives

One source file a day: `courses/<course>/u<stretch>-<unit>/d<day>.md` (day 90 of grade 4 math is
`courses/math-4/u11-1/d090.md`). The teacher page and the student page are both in it, so they cannot drift apart.
The questions are not: every question a student answers on the day (worked examples, the tool's notes, practice,
wrong answers to fix, the exit) is a row in `data/plans/<course>/items.csv`, and its key is computed there. A day
file names a question by its id, `[[s11-P90-1]]`, and never types a key. `python -X utf8 scripts/lesson.py build`
makes the print pages in `build/lessons/`.

The file starts with a header block: `day`, `course`, `unit`, `version` ("draft, not yet taught" until a taught
run), `materials`, `print`, and `credit` (see rule 4).

## The teacher page, in this order

Fixed headings, so a script can find each part and a teacher always finds it in the same place.

1. **The header** (generated): day, unit, kind of day, goal in student words, the parts of the standard, the tool
   and its mark, materials, what to print, version, credit.
2. **Before class.** Set-up only: what to print, what to open, what to lay out. 80 words at most.
3. **The day.** One part per block of time, headed with its minutes: `### 10 min. Teaching first`. The minutes
   add up to the length of the day (60 in grade 4 math, DEFAULTS.md) and agree with `days.csv`. Each part says
   what the teacher does, what students do, what to watch for, and what to do if many get it wrong (from the
   error register). Wording is written out only where the words matter: the steps of a worked example as the
   teacher says them, and the planned questions, each marked **Ask.** with the answers to expect and the order to
   show them in. Everything else is told, not scripted.
4. **Other rooms.** The paper path when there are no devices, one projector, one child at home: only what
   differs from the course's DEFAULTS.md. Every day has a paper path.
5. **Shorter or longer.** What to cut when time runs short without making the work easier, and the extension,
   on the same standard.
6. **Words and supports.** The key words with their Word Wall cards, the sentence frames, and any access note:
   only what differs from the unit opener.
7. **Tomorrow.** What the exit tells the teacher, and what changes the next day because of it.
8. **Credit.** See rule 4.

## The student page

- A name and date line, then the goal in student words.
- Frames to fill during the worked examples, so copying the model is part of the page.
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
   fails the build.
2. **The minutes add up** to the day and agree with the plan's row.
3. **Every number is new.** The worked examples, the tool's notes and the practice questions are "taught"; no exit
   question or check item may use the same numbers, and a generator refuses them.
4. **Credit on the lesson.** A day adapted from an open course prints, in its teacher page header and at the foot
   of every student page that carries adapted material: the source, its author, its licence with a link, and what
   we changed. Only material under CC BY, CC0 or in the public domain may be adapted, because Curio Class content
   is CC BY 4.0; a source with a NonCommercial or ShareAlike term may be read to learn, never adapted. A source
   read only to learn is named under Credit as "informed by". A day that is all ours says so.
5. **It stands alone.** A teacher who has read the unit opener can teach the day from its teacher page. Nothing
   says "see the plan".
6. **The tool is named by its own words** (its modes and screens), with the minutes it gets and the point to stop
   at, and the paper path does the same job.
7. **No countdown, no rank, nothing leaves the room.** No timer is shown to a student; results live on the record
   sheet and in score codes.

## What the script checks

`python -X utf8 scripts/lesson.py check` fails a day on: a missing header field or heading; minutes that do not
add up to the day or disagree with `days.csv`; a prose cap passed; an `[[id]]` with no row, or a row for the day
that no page uses; a keyed row with no computed key (from `plan.py check`, which it runs); a reused set of
numbers; an adapted credit with no licence or link; a student page that prints to more than two sides (checked on
the built PDF when Chrome is present). It cannot judge whether the day teaches; the expert and people do that.

## Not decided here

- Spanish student pages (ROADMAP, finished course item 14: Cory's in or not-now).
- An accessibility conformance level for print (item 10: Cory's).
- How a day uses the older shelves: for now a day names a worksheet, Word Wall card or chart only when it serves as
  it is, by link.

## The worked case: day 90

Day 90 is written to this page: [courses/math-4/u11-1/d090.md](../../courses/math-4/u11-1/d090.md), its rows in
`data/plans/math-4/items.csv` (ids starting `s11-` with `90` in them), and its built pages in
`build/lessons/math-4/u11-1/` (teacher, student, large print, key, exit slips, display). Counts: teacher page 880
words of prose, student page 98 words a student reads, 60 minutes, student page two sides.

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
