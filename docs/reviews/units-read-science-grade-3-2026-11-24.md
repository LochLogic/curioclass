# Units read together: science-grade-3, 2026-11-24

COURSE-RUN stage 4 "Reads" for science-grade-3. The expert read all six unit plans together and fixed them. Each unit had
already had its own read and fixes, and the course was signed off at stage 7 (2026-11-23) with every day written, so this read
looked for what a single-unit read misses: drift between the plans and the data and days that came after them.

## What was read

AGENTS.md; docs/COURSE-RUN.md stage 4; docs/agents/EXPERT.md; docs/agents/lenses/science.md; docs/courses/UNIT-PLAN.md;
docs/GLOSSARY.md (locked words). The course: scope-and-sequence.md (frame.md where the plans cite it); days.csv; s01 to s06 in
order; items.csv exit rows, handbacks.csv and source-map.csv; the course's 15 grade 3 rows in data/progressions/science.csv;
science-grade-2 s07 (continuity in); science-grade-4 s01 (continuity out). Written days were opened only to settle a plan
claim (d013, d017, d029, d059, d061, d062 and the return slots on d036, d081, d098, d120). There are no sections for
science-grade-3 in docs/reviews/lead-list-lens-pass-2026-11-17.md.

## Verdict

The six units make a sound arc. The fair test and force arrows from unit 1 carry into unit 2, the design cycle runs through
units 2, 5 and 6, claim-evidence-reasoning starts in unit 3 and grows through units 4 to 6, and the weather log runs all year
into unit 6. The seams with grade 2 (readiness on day 1 for kindergarten and grade 1 rows) and with grade 4 (retrieval of the
day 34 record) hold. The faults were drift: the plans had fallen behind changes made later in days.csv, source-map.csv and
the written days. All drift is now fixed, and all three gates pass.

## Findings

| # | Severity | Finding | Verdict |
|---|---|---|---|
| 1 | Serious (a gate failure) | s02 day list showed day 29 as Fluency, but days.csv now has Application. The header count (fluency 2, application 6) was wrong too. | **Fixed.** Day list regenerated from days.csv. Header now reads fluency 1, application 7. |
| 2 | Serious (a gate failure) | s04 field 10 did not name source-map rows G56, G57, G59, G60 and G61. s05 did not name G58. These are teacher references added at the 2026-11-19 and 2026-11-22 day reads. | **Fixed.** Each row is named with its link and day (the G60 link stays in sources.csv). |
| 3 | Moderate | The prose describing section exit tickets in s01 (day 13) and s02 (days 28, 30 and 33) no longer matched the written days or items.csv. s01's stale day 13 key even said that no prediction can be made, while the written ticket asks for one. A rebuild from the plan would have produced the wrong tickets. | **Fixed.** The prose now follows items s01-X13d/e and s02-X28 to s02-X33c and names them. |
| 4 | Moderate | In s04, a 474-word "Teaching-day timing" table sat after the generated day list. The next day-list refresh would have deleted it. | **Fixed.** Moved to the end of field 5, before the Goal map. The day list now matches the generator exactly. |
| 5 | Minor | The s01 day list (day 6 note) and s05 day list (day 83 codes: days.csv dropped 3-LS4-4) had drifted from days.csv. No gate caught it. | **Fixed.** Regenerated. |
| 6 | Minor | s03 field 7 said unit 3's scored papers come back in "day 59's Return and repair". Day 59 has no such slot: the papers are handed out at the hook, without comment. | **Fixed.** Field 7 now says how day 59 actually hands them back. |
| 7 | Minor | s05: the single readiness item (sk-reduce-impact) serves section 5.2, but it is given on day 81 and repaired on day 83 in section 5.1. Read alone, rule 6 would want at least half the items for the first section. | **No change.** The scope and sequence sets the before-the-unit timing on purpose, and day 87 retrieves unit 2 criteria before the merit work. |
| 8 | Minor | Day 29's exit (s02-X29) samples only the static and magnetic comparison. The day's goal also joins that evidence to the latch problem. | **No change.** The lid record collected that day carries the latch half and gets the checklist. It is not a day fault. |
| 9 | Note | Exits on day 93 ("one cold week") and day 113 ("one hot July") have the same shape. | **No change.** This is spaced return across two ideas (deep time, then climate range), not a repeat. |

Cross-unit checks that came out clean: the header day counts match days.csv in five of six units (s02 is fixed); every
"comes back" pointer names a day that teaches that thing; every retrieval row was used the year before or earlier the same
year, and the readiness rows (days 1, 36 and 81) are two or more grades back; every scored paper has a return day in
handbacks.csv (17, 36, 59, 81, 98 and 120); every Goal map exit differs from its practice; no unit's load is out of line with
days.csv.

## Day faults

None. Every fix brings the plan into line with the written days, so none asks a day to change.

## For the structure pass

- docs/courses/science-grade-3/scope-and-sequence.md, standards table, row 3-LS4-4: change the teaching evidence "83, 87 to 94"
  to "87 to 94" (days.csv day 83 now carries 3-LS4-1 only).
- Same file, "Materials, access and safety decisions", last paragraph: "no source-map.csv is required or written" is stale.
  Replace it with: "source-map.csv holds the section rows and the teacher references G56 to G61 (paraphrase only)."
- docs/courses/science-grade-3/u02-3.md header: change "fluency 1 (29), application 1 (30)" to "application 2 (29, 30)" to
  match days.csv.

## For Cory

None.

## Lead-list items worked

None: the 2026-11-17 lead list has no science-grade-3 sections (0 LEAD items, 0 CAP rejections).

## Outcomes

Fixed 6, no change 3, day faults 0, for the structure pass 3, for Cory 0.

## Gates

- `python -X utf8 scripts/unitplan.py check science-grade-3`: all 27 plans PASS. Before the fixes, s02, s04 and s05 failed
  (findings 1 and 2).
- `python -X utf8 scripts/sequence.py check science-grade-3`: 0 failures. Two notes stay as they are: days 63 and 102 are
  Fluency days that revise writing; days.csv kinds are not this job's to change.
- `python -X utf8 scripts/goalmap.py audit science-grade-3`: runs; every teaching day has a Goal map row (0 missing). It
  prints a listing and has no pass or fail result.
