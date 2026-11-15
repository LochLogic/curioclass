# Probe report: social studies (2026-11-15)

The first probe under docs/pipeline/PROBE-GUARD.md. One section of US History I (unit 5, section 5.2, days 78 to
82) was written from the new social studies unit plans and read the full way: Codex writer, cheap read, expert read,
sensitivity read, fix pass, fresh re-read.

## Result: Off. Correct the social studies units and the template line, then probe one more section.

| Measure | Reading | Band |
|---|---|---|
| 1. Plan share | 83 of 138 findings (60%) have origin unit, scope, frame or template | **Off** (line: over 35%) |
| 2. Unit plans changed | 121 of 138 social studies unit plans (88%) need the same fix | **Off** (line: over 25%) |
| 3. Template or one unit | Rule lines and gate checks only; no change to the template's shape | **On** |

No finding had origin frame, so nothing moves between grades.

## Measure 1: plan share

Source: data/plans/defects.csv, course us-history-i, dated 2026-11-15, rejected rows left out (2), and the re-read's
"reopened" row not counted twice. MEASURED.

| Origin | Findings |
|---|---|
| unit | 56 |
| template | 26 |
| scope | 1 |
| frame | 0 |
| section | 34 |
| day | 21 |
| **All** | **138** |

Plan share = (56 + 26 + 1) / 138 = 60%. Expert findings alone gave 40 of 63 (63%) before the re-read, so the reading
does not hang on the cheap read. By day: 78 10 of 19, 79 15 of 25, 80 13 of 21, 81 8 of 13, 82 17 of 24 (before the
re-read's 13). Against the old math baseline of about 25%, these plans were clearly worse to write from.

What drove it (from the expert, cheap and sensitivity reads):
- **Placeholder source sheets.** The stage-1 planner left excerpts marked to cut or check, so the writer had nothing
  verified to quote. Several facts changed once checked (Butler's letter date and wording, Grant's distance in time,
  the photograph's dates, Douglass's date, Port Hudson). Unit origin.
- **Items, keys and look-fors that let a wrong answer pass** or that score first-encounter work. Unit origin.
- **The error register** (letters that carry two misconceptions, wrong answers filed under a letter that does not
  describe them). Unit origin.
- **Math-shaped template rules** that did not fit a social studies day (repairs taking the next worked example, the
  typed name line, bare letters shared by errors and sources, hand-backs ignoring handbacks.csv). Template origin; all
  fixed as small rule lines and gate checks.

## Measure 2: unit plans changed

Full read in docs/reviews/probe-measure2-2026-11-15.md. 121 of 138 units (88%), Off. The driver is **K1**, error
letters holding two or more misconceptions, written by Codex in 119 units. Without K1 the count is 33 (24%, Watch),
mostly **K2**, end-of-unit parts scored from a day's first-encounter work with no feedback, which follows the
2026-11-14 settled rule that product-day parts "come off the sitting" (world history I and II above all). Smaller
kinds: K4 (exits answered from today's taught sources, about 6 units), K10 (a sensitivity read that leaves out a group
the days need, 4 units), K3 and K7 (1 each).

## Measure 3: template changes

All small, made by the fix pass and logged in DESK-ANSWERS (2026-11-15 entry): LESSON-DAY.md rule lines (credit
`ours`, letters in words, placeholders fail, a repair never takes the next worked example, hand-backs follow
handbacks.csv, a revision-note box on writing days, no typed name line), UNIT-PLAN.md rule 6 (the social studies
repair), DAY-WRITER.md, CHEAP-READ.md check 7, and gates in scripts/lesson.py, plan.py and day_skeleton.py. None adds or
removes a section or changes a required table. On.

## The re-read

docs/reviews/reread-u05-2-2026-11-15.md. Of 105 fixes, 103 hold and 2 hold in part (day 82 minutes not carried into
the section plan and skeleton; Source C still called a newspaper report in the family note and opener). 13 new
findings: unit 6, section 2, day 5. The most serious: day 79's exit tests the 1862 Homestead and Pacific Railway Acts
that the day no longer teaches; error K's repair asks students to name Native nations no student source names; day
78's read-aloud gives away the obstacle look-for. Four rest on the reader's memory and need the named texts checked.

## What happens next

1. **Correct the social studies units** (all 15 courses), in this order:
   - Template line first: one misconception per register letter (UNIT-PLAN field 6 and the Codex unit brief), so
     the fix is made once and then applied.
   - K1: split compound letters in the 119 units (scripted find, Codex rewrite per course, cheap read).
   - K2: score an end part only from work that has had feedback or a revision chance; the 2026-11-14 rule is
     replaced by this (a decision entry when made). About 26 units.
   - K4, K10, K3, K7: the units named in the measure 2 report.
   - Source sheets: the unit-planning brief requires verified excerpts or none; no placeholder reaches a section.
2. **Close the probe section's open findings** (33 open on days 78 to 82, ledger status open), with the source
   checks the re-read names.
3. **Probe one more social studies section** from the corrected units, in a different course (not US History I),
   read the same full way, and report it beside this one.
4. Science, ELA and math units wait on step 1's template line, so they are written with it from the start.

## Questions for Cory

- **Books.** The Quarles, Fields-Black and Green paraphrases cannot be checked for free: buy three books, or use the
  National Park Service pages and the primary texts instead.
- **Native nations read.** Day 79 and error K need a Native nations sensitivity read; the plan is to run it the same
  way as the u05-2 read.
- **Map.** Day 79's map task returns once our own map is drawn (art step).
