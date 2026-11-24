# Structure pass, core electives, 2026-11-24

later.csv L109. Applies the shared-file items of the six core elective fix reports
(docs/reviews/sequence-<course>-fixes-2026-11-24.md, "For the structure pass" and "Not applied") and their Gemini fix
reports (docs/reviews/gemini-fixes-sequence-<course>-2026-11-24.md) for psychology, earth-and-space-science,
environmental-science, calculus, precalculus and statistics. Each old text was checked in the file before the edit;
every one was still there as the report gave it. CSV line endings and quoting kept.

## Applied

- **data/plans/calendar.csv** (psychology): unit 15 label "when thoughts and behaviour" to "when thoughts and
  behavior". The frame already had the US spelling, so `frame.py sync` writes the same label (now
  "...thoughts and behavior ", the generator's 80-character cut).
- **`python -X utf8 scripts/frame.py sync`** (statistics): rewrote data/plans/frames.csv (no change),
  data/plans/calendar.csv and the generated table in docs/courses/CALENDAR.md. Statistics now shows its written days:
  held unit 10 days 47 to 48 (week 10) and 70 to 71 (weeks 14 to 15) in their weeks, unit 5 split around them, Check 2
  on days 90 to 92 (weeks 18 to 19), Check 3 on days 149 to 151 (weeks 30 to 31). CALENDAR.md row: Check 2 "weeks 18 to
  19", Check 3 "week 30". The same sync also picked up Calculus's frame change "travelled" to "traveled" in its unit 8
  label. No other course's rows changed. `frame.py calendar` re-run: output identical to before.
- **data/progressions/science.csv** (environmental science), notes column, the three edits in the exact form given:
  env-soil-conservation (chem-resource-cost-benefit readiness, last used in Chemistry; bio-evaluate-impact-solutions
  retrieval, last used in Physics, grade 11), env-water-quality (s7-human-impact-design last used in Chemistry, grade
  10), env-conservation-strategies (bio-biodiversity-simulation readiness; bio-define-human-impact-problem retrieval,
  last used in Physics, grade 11). These match the frame and the scope gate's count; as the fix report says, the
  Physics "use" rests on one hop (Chemistry day 88 retrieves both bio- rows; Physics day 19 retrieves Chemistry's row).
- **data/progressions/math.csv**:
  - pc-polynomial-complex-zeros `assumes` adds alg1-completing-square (precalculus, expert finding 5, optional; taken
    because Precalculus day 20 now retrieves it). The progression gate then failed ("alg1-completing-square does not
    hand on to it"), so alg1-completing-square `hands_on` adds pc-polynomial-complex-zeros, as the 2026-11-15 math
    structure pass did for the same failure.
  - calc-continuity notes: "assumes pc-function-analysis from Precalculus" becomes "assumes pc-function-analysis and
    pc-informal-limits from Precalculus" (precalculus frame For the lead 5, the form the frame gives; pc-informal-limits
    is CUR-PC.16, Precalculus unit 10).
  - calc-riemann-sums notes (calculus): adds "By course order: picks up pc-sequences-series-binomial (sigma notation,
    Precalculus unit 10), retrieved on its second day." before its Re-entry sentence. Checked: Calculus day 67 (unit 5's
    second day) retrieves it. Wording mine around the report's phrase, in the "By course order" form the
    calc-series-convergence seam uses.
- **data/standards/curio-math-electives.txt** (statistics), US spelling: CUR-ST.11 "centre" to "center"; CUR-ST.17
  "Recognise ... analyse" to "Recognize ... analyze"; CUR-ST.18 "randomised" to "randomized".
- **data/plans/later.csv**: new row L110 for the Calculus route item below (the Calculus report asked for a row if it
  waits).

## Not applied

- **scripts/sequence.py rule2_notes: let a course name its route** (calculus): a gate code change with a design
  choice (a frame field or a frames.csv column, and how Precalculus and Statistics take it), not a listed edit.
  Parked as later.csv L110. Calculus still prints its seven expected rule 2 notes.
- **Load the high school Progressions documents into the source store** (precalculus): needs downloads from outside
  the repository and a license check before they go in S:\CurioClass-sources and docs/sources/BASE-TEXTS.md. Listed for
  the lead (download and license go). N-CN and N-VM stay marked "no document".
- **docs/sources/BASE-TEXTS.md, statistics microdata files** (statistics frame For the lead 3): the report makes it
  conditional on "when the microdata extra is recorded"; BASE-TEXTS.md has no microdata entry yet, so nothing to edit.
- Earth and space science: the report lists none. Psychology and the Gemini reports: nothing else for this pass
  (statistics Gemini G4 is the `frame.py sync` above).

## For Cory

None.

## Gates (before, after)

- `progression.py check math`: 382 rows, 0 failures; after 0 failures.
- `progression.py check science`: 237 rows, 0 failures; after 0 failures.
- `frame.py check` (all 58 frames): exit 0, 0 failures, 71 notes; after the same. One note grew: algebra-i "Seams does
  not name ..." now also lists pc-polynomial-complex-zeros (the new handoff); a note, the same kind as the 16 ids
  already in it.
- `frame.py calendar`: identical output before and after.
- `sequence.py check` (all 40 courses): 0 failures, 90 notes; after identical. The six: 0 failures each.
- `plan.py check`: exit 1 before and after with 1,669 FAIL lines both times (existing failures, e.g. algebra-ii
  sections not yet in units.csv); the only difference is the algebra-i note above.
