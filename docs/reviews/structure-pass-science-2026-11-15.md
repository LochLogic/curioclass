# Structure pass, science group, 2026-11-15

Shared-file items from the 37 scope fix reports (docs/reviews/sequence-<course>-fixes-2026-11-15.md) whose target is
a file the science group owns. Items for files other groups own (scripts/frame.py, math.csv, ela.csv, ela-texts.csv,
RUBRIC-ELA, RUBRIC-MATH-K8, APPROACH-SOURCES, APPROACH-MATH, lenses/science.md, library files, modules, coverage,
later.csv, us-history-i days) were left to their owners.

## Applied

- **data/progressions/science.csv** (108 cell edits, CRLF and quoting kept). Handoff and model-return notes rewritten to
  the counted last-use rule, as each report gave them: physics 1 to 4; grade 2 items 6 and 7; grade 3 items 1 to 7;
  grade 4 items 1 to 8 (including the s4-wave-model cross_subject lean); grade 5 items 1 to 4 (water shares,
  force and sky handoffs); grade 6 table (7 rows); grade 7 table and items 1 to 5; grade 8 table (3 rows); biology
  items 1 to 3; chemistry items 1 to 7. phys-wave-technologies assumes gains s6-light-paths, with a readiness note.
- **data/standards/ngss-pe-dimensions.csv**: K-ESS3-3 statement "air and living things" to "air and/or living
  things" (the official expectation reads "land, water, air, and/or other living things"; the kindergarten read and
  the beaver-builders spec quote it the same way).
- **docs/RUBRIC-SCIENCE.md**: Gateway 2 full-scope cell (dimension file exists; coverage traced by element), S5
  failure cell (safety agent, FOUNDATION 7.3), "What this adds" item 2, Questions for Cory safety bullet.
- **data/plans/frames.csv**: per_week 2 to 3 for science-kindergarten, science-grade-1, science-grade-2 (lead call;
  weeks kept at 29, 29, 28 as all three reports asked, and frame.py's WEEKS table holds those weeks).
- **data/courses.csv**: science-ms notes, grade 6 report.
- **docs/courses/CALENDAR.md**: grade 2 science target cell 17, 28 to 20, 28 (hand-written table). The generated row
  (line 79) is left to `frame.py sync`.
- **docs/pipeline/briefs/frame-write.md**: one line after the Units header: ELA heads C3 as Texts (ELA 8 item 4);
  science heads it Practices and crosscutting concepts (grade 3 item 12, grade 5 item 7).
- **docs/courses/science-grade-8/frame.md**: physics items 5 and 6 (light-ray return in Physics unit 6; Models
  carried row).
- **docs/courses/math-grade-1/frame.md**: grade 1 science timing (daylight sort day 62, school day 133, week 27;
  light sort day 45, week 19; daylight recording from week 4; length ordering day 22, week 9; first measuring day 50,
  week 21; math unit 1 school days 1 to 16, weeks 1 to 4; math unit 6 school days 111 to 128). Applied to the text
  as the math fixer left it (line numbers had moved; the wording had changed to "weeks 27 to 28").
- **docs/courses/english-language-arts-grade-1/frame.md**: science unit 2 "about weeks 5 to 10" to "weeks 4 to 9".
- **docs/courses/civics-government-and-civic-life/frame.md**: ELA 8 item 3, sequential writing windows sentence.
- **docs/reviews/DIGEST.md**: "## Scope fix pass, 2026-11-15: science" appended (21 lines, deduplicated).

## Skipped

- data/plans/calendar.csv (grade 1, grade 2, ELA 2): every requested change is a regeneration; `frame.py sync`
  produces it. No hand edit made. Grade 1 expects a new unit 8 fall-run row (day 9); check that sync emits it.
- Grade 2 item 2 (frame.py PINS {58: 98}): not this group's file; already present in scripts/frame.py.
- Grade 4 items 12 and 13 (math-grade-4 and ELA 4 frames) and grade 5 item 6 (math-grade-5 frame): already done;
  the frames carry the new school days and the unnumbered-strip wording.
- Grade 1 conflict: grade 1 and grade 2 both rewrote s2-fast-slow-events. Grade 2's wording used (the row is grade 2's,
  and it states grade 1's point plus the day 10 readiness).

## Conflicts reconciled

- RUBRIC-SCIENCE: eight reports gave different wordings for the same three cells. One merged wording each: element
  tracing including band practice and crosscutting elements (grade 8), safety data sheets of named chemicals
  (biology), separate human pilot requirements (physics, grade 6, chemistry), no new staffing question.
- s4-wave-model cross_subject: the report's semicolon inside the parenthesis broke the subject:code list gate;
  written with a comma ("teaches them, while science first compares...").
- data/courses.csv: "one OpenSciEd year each" written as "one year of the adapted middle school base each" (no source
  name outside credit lines, RUBRIC-SCIENCE S8).
- s6-light-paths hands_on gains phys-wave-technologies so both ends of the new physics handoff are written (gate).

## For the lead

- **Before `frame.py sync`:** science-kindergarten's Days bullet says "three meetings a week", which frame.py's
  per_week regex does not read ("meetings" is not in its word list), so it falls to "daily" and sync would write
  per_week 5, undoing the lead call. Either the kindergarten frame says "three lessons a week" or the regex accepts
  "meetings". Grades 1 and 2 parse as 3 already.
- The math-grade-1 frame's ss1-voting row still says math unit 1 is "Weeks 2 to 4"; the science rows now say weeks
  1 to 4 (school days 1 to 16). Not asked; left for the math owner.

## For Cory

None.

## Gates

- `progression.py check science`: 0 failures (198 rows). `stale.py check` on science.csv: 0.
- `frame.py check` and `sequence.py check`: 0 failures for science-kindergarten, science-grade-1, science-grade-2,
  science-grade-8, math-grade-1, english-language-arts-grade-1, civics-government-and-civic-life. Kindergarten notes
  frames.csv is behind the frame (the per_week parse above).
