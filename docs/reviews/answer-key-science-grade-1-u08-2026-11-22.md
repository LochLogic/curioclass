# Answer-key read: science-grade-1, unit 8 (2026-11-22)

Kind: answer-key. Target: science-grade-1-u08, the check, mid and end items (course finish, COURSE-RUN stage 7). Read-only; nothing but this report was edited.

## What I studied

The answer-key brief studies nothing outside: the study step is to solve. I solved every in-scope item cold from its stem and the printed strips before opening the key or wrongs.csv.

- data/plans/science-grade-1/items.csv, unit 8, filtered: one item is in scope, s08-E64a (check `end`). Unit 8 has no `check` or `mid` items; the other ten rows (s08-X9a to s08-X65b) are exits and are out of scope.
- courses/science-grade-1/u08-1/d064.md, strips-boston.md (the printed check strips and report card), sheet-response.md, record.md, strips-key.md (adult key with the source times).
- data/plans/science-grade-1/wrongs.csv rows for s08-E64a; sources.csv rows 13C, 13E, 13I, 13L, 13O.
- docs/courses/science-grade-1/s08.md: the standard line for 1-ESS1-2, the day 64 check row (field 5) and U3.

## Cold solve

s08-E64a. Three real Boston strips, Oct. 20 (fall), Jan. 20 (winter), Apr. 20 (spring), plus an invented Oct. 20 "light at 5:30" report. Measured light parts on the printed SVGs: fall 6.05 to 16.90 = 10.85 cm, winter 7.13 to 16.72 = 9.58 cm, spring 4.92 to 18.53 = 13.62 cm, all on a 24 cm bar. My answer: winter's light part is shorter than fall's and shorter than spring's; the evidence is the three full-day strips; the evening report shows one moment and cannot tell how long the day was light. On the response sheet, "winter" is circled in both rows.

Key: same. No mismatch.

Scaling check: the drawn positions match strips-key.md to the hundredth (06:03, 16:54; 07:08, 16:43; 04:55, 18:32 standard time, 1 cm to the hour), and the times match what Boston standard time gives for those dates. The response sheet strips are identical to the group strips. Winter is 1.3 cm shorter than fall and 4.0 cm shorter than spring: the fall gap is the smaller one but is plainly visible at 24 cm.

wrongs.csv: A (all the same), B (winter has more), C (evening report as whole-day evidence), D (dark part as daylight) and x (names seasons, points to nothing) agree with the key, d064.md and the s08.md field 5 row, including the s08.md rule that "winter has more" with the dark part as the reason is D.

Standard: the item asks for observations at different times of year related to daylight, winter compared with fall and spring, relative length only, no hours. That is 1-ESS1-2 within its boundary, and the day 64 goal in s08.md. Pass.

## Verdict

Pass with fixes. The one in-scope item is keyed right, its strips are drawn true to the source times, and it tests the unit's goal; three small points below would make the marking fairer and the home path sounder.

## Findings

1. Fair alternative not named (item slightly ambiguous in marking). Look-fors in d064.md read "compares winter with fall; compares winter with spring". A child who says "Winter is the shortest" while pointing across all three strips has made both comparisons, but a strict marker may credit neither. Fix: in items.csv s08-E64a `steps`, after the two compare steps add "(saying winter's light part is the shortest of the three, while pointing to the strips, credits both)"; in d064.md, after "compares winter with spring" add "(winter is the shortest of the three counts for both)".

2. At-home swap gives away the pattern. d064.md At home, Swap: "draw three bars of one length, winter's white part clearly shortest." The family draws the answer before the child is asked for it, so the check no longer uses a record. Fix: "No printed strips: draw three bars of one length, 24 cm each, and make the white parts 10.9 cm for Oct. 20, 9.6 cm for Jan. 20 and 13.6 cm for Apr. 20, starting 6 cm, 7.1 cm and 4.9 cm from the left." (These are the key's Boston values; families never see the times.)

3. Report time against the standard-time strip (adult only, minor). The report says "light at 5:30" on Oct. 20. strips-key.md says reports are wall-clock time, and Oct. 20, 2025 is still daylight time, so 5:30 is before the 5:54 wall-clock sunset: consistent. An adult who lays 5:30 on the standard-time strip finds it at 17.5 cm, in the dark part past the 16.9 cm sunset, and may think the report is wrong. Fix: in strips-key.md, under the records table, add "The day 64 report's 5:30 is wall-clock daylight time; on the standard-time strip it sits at 4:30, inside the light part."

4. Pointing to strips and the report together (noted, no change needed). The record credits the evidence look-for only when the child points to the strips "and not to the evening-only report". A child who points to all four records is not error C (C is the report alone) and simply leaves that look-for unshown. This matches the unit's aim of telling full-day records from one moment, so it is a fair design choice, not a key error.

## Gate

Filtered `plan.py check` for science-grade-1: 13 FAIL lines, all "section N.N (science-grade-1-uNN-N) is not in data/units.csv", one per section, course-wide, none from this item. Sequence: 0 failures.

## Could not settle

Nothing.

## Fixes applied (2026-11-22)

1. Winter shortest of three: applied in the E64a step and the d064 look-fors.
2. At-home swap: applied. Bars of 24 cm with the key's Boston lengths and starts.
3. Wall-clock note: applied under the strips-key.md table.
4. Pointing to all four: no change, as the report advised.
