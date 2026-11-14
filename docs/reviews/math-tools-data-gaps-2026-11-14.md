# Math cluster weights and days.csv tools, supplies, safety columns (2026-11-14)

Files changed: data/standards/ccss-math-focus.csv, docs/pipeline/briefs/sequence-write.md (days.csv section only),
scripts/sequence.py. Nothing else was touched.

## 1. High school cluster weights

Gap found: 35 clusters of data/standards/ccss-math-clusters.txt had no row (147 clusters now all have one; every
cluster cited by data/progressions/math.csv and the Algebra I, Algebra II and Geometry frames also has one; the grade 4
frame was not opened under the blind rule, but all its clusters are in clusters.txt, which is covered).

Filled: 35 rows. 7 major, 7 supporting, 14 additional, 7 plus.

Sources (named in each row's source cell):
- PARCC Model Content Frameworks for Mathematics, Grades 3-11, Version 4.0, December 2014, course overview charts:
  Algebra I (page 43), Geometry (page 47), Algebra II (pages 50 and 51). The marks are drawn shapes on the charts (green
  square major, blue square supporting, yellow ring additional), read by eye from the rendered pages; the PDF text does
  not carry them. 28 rows. Source cell is the PDF URL with `#page=N` naming the chart used.
- Student Achievement Partners, High School Publishers' Criteria, Spring 2013 (pages 5 and 6), for 7 rows marked
  `plus`: N-CN.B, N-VM.A, N-VM.B, N-VM.C, G-SRT.D, S-MD.A, S-MD.B. Every standard in these clusters carries (+) in
  data/standards/ccss-math-standards.txt (checked mechanically). PARCC does not chart (+) standards and the criteria
  give them no weight, only the boundary, so `plus` means "outside the weighted set" and nothing more. New focus value:
  see the unit_skeleton.py change below.

Disagreements and the choices made (also in the file header):
1. Rule: the mark from the first traditional-pathway course (Algebra I, Geometry, Algebra II) that lists the cluster,
   because that is where it is introduced and those are the Curio Class courses. Three clusters differ by course:
   F-BF.A (Algebra I supporting; Algebra II and Mathematics I major) filed supporting; S-ID.B (Algebra I supporting;
   Mathematics I additional) filed supporting; S-ID.A (Algebra I additional; Mathematics I supporting) filed additional.
   A course that teaches F-BF.A in Algebra II should treat it as major there.
2. PARCC (relative weight on an end-of-course test) and the SAP criteria (what is widely applicable for college) answer
   different questions, so they are not merged. The 19 existing `wap` rows are unchanged (none found wrong), even where
   PARCC marks the same cluster differently (A-REI.C and N-RN.B additional, F-IF.C supporting).
3. Licence: the PARCC PDF carries no licence line; the file stores only cluster ids and one word, as the header says.
   The organisation's own site no longer serves the PDF; the copy read is at iarss.org (URL in the header).
Existing K-8 and wap rows: unchanged.

## 2. days.csv columns for tools, supplies, safety

Format: optional columns after `note`: `day,stretch,unit,kind,goal,skills,codes,assess,school_day,note,tools,supplies,safety`.
Math and science only; social studies and ELA files have none and are never checked for them.
- Every cell is a `; `-separated list, empty when none; no empty item, no trailing semicolon.
- tools: digital or drawn tools by their name in the tools file. supplies: physical things students handle.
  safety (science fills, math leaves empty): hazard and control per supply day, or the lower-case word `none` alone.
- Names match the skeleton's TOOLCOLS, UNIT-PLAN.md field 8 (tools and supplies; science adds materials and safety).

Gate rules in scripts/sequence.py (`tool_cols`, called from `check`):
- Fail: an empty item or stray semicolon in any of the three cells (math and science).
- Fail (science): `supplies` column without `safety` or the reverse; a day with supplies and empty safety; `NONE` in
  other case; `none` inside a list.
- Note, not fail: a science file with none of the columns; a science day whose goal or note reads hands-on (lab,
  investigate, build, heat, and similar) but names no supplies and no safety; columns empty on every day.
- days.csv has no hands-on marker, so "hands-on day" is read as "day with supplies"; that is the strongest mechanical test.
- Subject comes from data/plans/frames.csv (name prefix fallback). Social studies, ELA and any other subject return
  nothing from the check.

## 3. Gate proof, 15 social studies courses

`python -X utf8 scripts/sequence.py check <course>` for each course from `unit_skeleton.py --list social-studies`,
before and after the change: identical output (diff empty). Every course prints `0 failure(s)` and exits 0:
civics-government-and-civic-life, economics, social-studies-grade-1 to 5, social-studies-kindergarten,
us-government-and-politics, us-history-i, us-history-ii, world-geography-and-ancient-civilizations-i and -ii,
world-history-i and -ii. A final `plan.py check` run showed no new failures in the frame lines it printed.

## 4. Change needed in scripts/unit_skeleton.py (not made; another agent owns it)

The skeleton already reads columns named tools, tool, supplies, materials and safety (TOOLCOLS, `column_lines`), so the
new columns are picked up with no change to the reader. Two exact edits:
1. Weight line: `header_weight` loops over `('major', 'supporting', 'additional', 'wap')` and `WEIGHTWORD` has four keys.
   Add `'plus': 'advanced (+) standards, outside the weighted set'` to `WEIGHTWORD` and `'plus'` to the tuple, or the
   seven plus clusters silently drop out of the weight line (they are not reported as missing either, since the value
   is non-empty).
2. Science field 8: `field8_lines` puts `column_lines(rows)` (which includes the safety column) under "Materials and
   tools". Split it: pass `column_lines(rows)` filtered to `col != 'safety'` to the materials bullet, and the safety
   column lines (`  - Day N, safety column: ...`, skipping `none`) to the safety bullet ahead of `safe`.
