# Calibration before trust: testing the expert reader (pre-work P5d)

Written 2026-11-13 for docs/PRODUCTION-PATH.md P5d. There are no people reading yet, so the expert agent and Codex
are the reviewers of every progression, frame, scope and sequence and unit. Before their reads are trusted, both
read a small test set whose faults we already know, and we count what each catches and what each flags wrongly.
The line for "good enough" is set here, before the run, and shown to Cory before it is used.

## The test set

Kept outside the repository, so a reader cannot find the answer key: `S:\CurioClass-sources\_calibration\`
(`set\` holds what the readers see, `key\` holds the planted faults). A reader is given only `set\` and the
normal brief for the layer.

| Piece | What it is | Planted faults |
|---|---|---|
| A progression slice | About 25 rows in the data/progressions format: grades 3 to 5 fractions (math), and grades 4 to 5 early American history (social studies), built correct first from the standards | 6 |
| A course frame | One frame with its units and reasons (grade 5 social studies) | 3 |
| A unit plan | A copy of grade 4 math unit 4 (s04.md, already read and held, so its true state is known) | 5 |
| A science unit outline | One middle school unit storyline, built correct from the base text's order | 4 |
| Settled past findings | 10 findings from data/plans/defects.csv: 6 fixed (real) and 4 rejected (false), shown as claims to judge | 10 claims |

The planted faults cover every kind P5d names, at least twice each across the set:

1. A skill owned by two grades.
2. A handoff that skips a grade (`hands_on` not picked up, or assumed two grades early).
3. A model used before it is taught (number line, timeline, map scale, a science model).
4. A standard taught only in part.
5. A values-rule miss (a group described only in the past tense, a sensitive topic with no teacher note, a
   one-sided source set).
6. An exit ticket that misses the day's goal.

Each planted fault is major (a writer would build wrong days from it). Three or four minor ones (wording, a
count slightly off) are planted too, to see whether a reader ranks them below the majors; they are not counted
toward the catch rate.

## The line, set before the run

Recommended, for Cory's yes:

- **Catch rate:** each reader catches at least 8 in 10 of the planted major faults (that is, at least 15 of the 18 in the table).
- **False alarms:** at most 3 findings marked major across the whole set that are not real faults, and the 4
  rejected past findings are judged false by the reader at least 3 times in 4.
- **Coverage:** no fault kind is missed by both readers in all its plantings.
- **Ranking:** the reader's most serious findings are planted majors, not minors, in at least 3 of the 4 pieces.

A reader under the line is not used alone for that layer: its brief or EXPERT.md is changed, and the set is read
again. The run is repeated after any change to EXPERT.md, a lens or a brief, with a fresh set of plantings so a
reader cannot learn the set.

## How it is run

1. The lead builds `set\` and `key\` (the set is built correct first, then the faults are planted one at a time
   and logged in `key\faults.csv`: piece, row or line, kind, major or minor, what is wrong, the fix).
2. A fresh expert agent reads each piece with its normal brief (progression-read, frame-read, plan-read), cold.
3. Codex reads the same pieces with the same briefs (pasted by Cory, a new chat for each piece).
4. The lead scores both against `key\faults.csv` and writes docs/reviews/calibration-<date>.md: caught, missed and
   false per reader and per kind, against the line.
5. Cory sees the result on the Desk before step 1's reads are trusted.

## Known limits

- The set is small; a reader can pass it and still miss a kind of fault the set does not hold. New fault kinds
  found in real reads are added to the next set.
- Planted faults are cleaner than real ones. Real past findings (part 5) are there to keep the test honest.
