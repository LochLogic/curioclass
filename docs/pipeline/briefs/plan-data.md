# Job: apply the plan read, then put unit {unit} of {course} into data, plus its shared pieces

1. Apply the newest docs/reviews/plan-s{uu}-*.md: every finding and every row of "Settled by the expert", to the
   plan files docs/courses/{course}/s{uu}.md and u{uu}-*.md. Do not act on its "For Cory" list; repeat it in your
   report. Log each finding with `python -X utf8 scripts/plan.py defect {course} s{uu} <layer> expert <kind>
   "<summary>" docs/reviews/<report>.md#<n>`, marked fixed, open or rejected.
2. The plan as data, following data/plans/README.md and the way unit 2 was done (commit a40b62a1): parts.csv,
   days.csv rows for days {first} to {last}, items.csv (readiness, exits, end-of-unit assessment, written
   tasks), wrongs.csv, errors.csv, words.csv, and every column the README requires. In ELA each items.csv row also
   fills `text_id`, `text_ref` and `needs_text`, and the unit's word list goes in wordlist.csv (UNIT-PLAN.md,
   "English language arts data"). `opens_min` counts only the parts after the warm-up (lesson.py reads it so), even when the warm-up holds the
   repair (L78). Then
   `python -X utf8 scripts/plan.py tables {course}`.
3. Shared pieces in courses/{course}/u{uu}-1 (and the other section folders): readiness.md, the section
   opener(s), record.md, family.md (English only), and any recording page or sheet the plan names. Match the
   newest units' pieces (courses/{course}/u02-1 and u03-1) for shape and tone; read docs/courses/LESSON-DAY.md
   first. Where an earlier day's file names one of your pieces with "when it exists:", remove those words.
   Source sheets: every quoted passage is copied from a checked free source (a primary-text archive, a park service
   or other government page) and its link goes in the course's sources.csv; a passage you cannot check is cut, not
   left as a placeholder (`[to check ...]` fails lesson.py). A paraphrase of a book we cannot read is cut (settled
   2026-11-15: free sources, no book purchases). A text found only in paid editions may be named and described,
   never quoted, from a free secondary source that says what it holds, credited to that source (UNIT-PLAN field 10).
   Keys (the faults two reads still found after the answer-key read, L78): a key quotes the text exactly and takes
   each referent from the sentence itself; "stated" and "implied" are used as the text supports; a key never leans on
   events after the passage the item gives; science wrong answers and keys are right about what moves (particles,
   not the solid itself); an exit or check is not the worked example's structure in new numbers; a shared piece is
   the sheet itself (boxes and lines to write in), never a description of it or a note to the teacher.
4. Sources, once for the course (later.csv L75): for every sources.csv row a day of this unit will use, open the
   link, read its licence or terms, fill `rights` and set `status` to `checked: <date>` (or `written: <path>` for a
   piece we make). A row you cannot check is cut, with its passage. The day skeleton STOPs on any source left
   unchecked, as a backstop only: day writers never set a status themselves.

5. Checks before the days lean on the data (science ladder report, 2026-11-19: wrong keys were one firm fault in
   seven, and plan numbers the data overruled went unmarked):
   - **Rule 4 on the pieces.** No shared piece (picture page, card, story, sheet) shows the case, picture or numbers
     of an exit or end item of these days, and no exit or end item reuses a case a lower grade's ledger lists
     (`python -X utf8 scripts/ledger.py show <subject> --before {course} --term "<word>"`, filtered).
   - **Plan against data.** Where a source or a key overruled a number or fact in a section plan, correct the plan's
     `## Day N` block to the data and list each change; never leave the two disagreeing.
   - **Sources.** Every animal, plant, place, weather or other fact a piece or item states rests on a checked source
     row; list any fact you reworded or cut because no source supports it.
   - **Answer-key read.** Before the unit's days are queued, a fresh agent runs docs/pipeline/briefs/sensitivity-read.md
     with kind `answer-key` on this unit's items.csv rows, solving every exit and end item cold; every mismatch is
     fixed in the data before any day is written.

Gates: `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/lesson.py check` (failures only because
the days are not written yet are expected; list them). When this job ends, the unit's days are queued.

Do not commit or push; `turn.py end` does it. Last message (under 200 words): rows added by file, pieces written,
plan points you decided, expected failures, anything for Cory.
