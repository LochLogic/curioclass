# Answer-key read: math-grade-2 unit 3 (days 39 to 57), 2026-11-27

Kind `answer-key`, a fresh agent read. Target: the packet build/sections/packets/math-grade-2-u03.md (items.csv rows,
wrongs.csv rows, handbacks rows, the error register, field 3 lines, shared pieces).

## What I studied

Nothing outside, as the brief says for this kind: the study step was to solve. I solved every item cold from its stem
and the child's page (exit-39 to exit-54, the station, story, track, join, cable and comparison pages, the recheck
pages) before opening any key piece (key-exits for u03-1 to u03-4, key-closing) and before reading the plans or prep
notes.

## Items read

53 items in the packet: X39 to X54 (16 exits), T, E and E2 in cm, ft, m and in (12), P, C, D, L, SD, S1 to S13,
D-length, L-story, D-story, F-D, F-L, F-S4 and F-S9. Two splits added two items, so unit 3 now holds 55 scored items.
Apart from the faults below, my answers matched every key, and each wrong's `compute` gives its `value` with one fitting
letter.

Rule 4: `ledger.py show math --before math-grade-2 --term ...`, filtered by each item's object and length words, plus a scan of every piece in
courses/math-grade-2/u01-* to u03-* for two or more of an item's numbers on one line. One echo was found (X40,
below). Grade 1 lanterns and pockets use other numbers. Unit 1's s01-S7 (7 round and 3 square tiles) and s01-S8
(shape box of 19) do not appear. No unit 2 reserved family appears as a pair.

Facts: three rows carry outside facts, and each traces to a sources.csv row marked checked 2026-11-27: 43A (1 m = 100
cm), 47A (12 in = 1 ft, so 7 ft = 84 in and 24 in = 2 ft) and 56A (a yard is 36 in). Field 3 lines agree with
items.csv. No child-held page prints a key.

## Faults

| Item | Kind | What was wrong | Fix | Stage |
|---|---|---|---|---|
| s03-X39 | ambiguous | The page gave "22 narrow tiles" and "two narrow match one wide" but not that Mika has only wide tiles, so 22 narrow tiles also fills the gate. The ledger held the limit and the page did not. | items.csv steps, exit-39.md and u03-1/key-exits.md now say "Mika has only wide tiles." The u03-1.md field 3 line too. Key 11 wide tiles unchanged. | unit plan |
| s03-X40 | rule4 | A 16 cm window, 27 cm tab and 11 cm out echoed grade 1's reserved two strips of 11 and 16 units. | Window now 20 cm, so 7 cm sticks out. Answer, compute, value and samples in items.csv; A "0 cm after spreading 20 units"; C "8 cm" from 28 − 20; exit-40.md caption, teacher note and window width (63% of the 85% tab); key-exits; field 3; ledger note. A 15 cm window was a retired version, so it was not used. | section plan |
| s03-X45 | two-asks | One item scored an extension estimate and the joined length. | Split: new s03-X45-estimate ("About how long is the extension in centimeters?", about 30 cm; A about 20, C about 40), wrongs and handbacks rows (day 46 Repair, 0 minutes, alongside G or M). s03-X45 keeps the joined length: "87 cm. The extension measures 28 cm. 59 + 28 = 87." exit-45.md prints two cues; key-exits and field 3 follow. | unit plan |
| s03-X51 | two-asks | The same double ask for the insert estimate and the gap. | Split: new s03-X51-estimate (about 35 cm; A about 25, C about 40), wrongs and handbacks rows (day 52 Measure, alongside H or C). s03-X51 answer "51 cm. The insert measures 34 cm. 85 − 34 = 51." exit-51.md, key-exits, field 3 and field 4 follow. | unit plan |
| s03-X45-estimate, s03-X51-estimate | ambiguous | Found in the recheck. The drawn extension was 24% wide against a 65% rail of 59 cm, which reads as about 22 cm and pulls toward A. The insert was 34% against a 90% opening of 85 cm. | Widths now 31% and 36%, to scale. | data |
| s03-X54 | key | The key gave the value before the equation. | "76 − 71 = □ or 71 + □ = 76, with □ = 5 cm." items.csv, key-exits, field 3. | section plan |
| s03-S8 | key | Value list before the equation. | "□ + □ = 94 with one pair, such as 47 + 47 = 94", then the accepted pairs. items.csv, key-closing, field 3. | section plan |
| s03-X44, X49, X50, D, SD, L, D-length, L-story, D-story | key | items.csv put the equation first, but the key pieces put the value first. SD's field 3 key gave only 81 − 69 = 12. | Key pieces and the SD field 3 line now give the equation first. items.csv unchanged. | data |
| s03-E-cm to E-in, s03-E2-cm to E2-in | needs-info | The keys rest on spans of a checked reference (10 cm, foot, meter, 6-inch), but the stations and rechecks did not set one out. | station-*.md and recheck-*.md teacher notes leave that checked strip uncovered beside the tools. u03-4.md days 55 and 57 say the same. | section plan |

Considered and kept: the X44 gap ticks are tight at print (32 lines in 37 px), so the C wrong answer (32 cm) is
unlikely to be seen. The key holds, so I left it as a plan point. C's forecast boxes are unscored by unit plan design.
X45 and X51 keys give the value first because the stems ask for a length, not an equation.

Changed items answered cold again against the final files: X39 (11 wide tiles), X40 (27 − 20 = 7 cm), X45-estimate
(about 30 cm from three 10 cm spans), X45 (59 + 28 = 87), X51-estimate (about 35 cm from seven 5 cm spans), X51 (85 −
34 = 51), X54 (76 − 71 = 5), S8 (any pair from 42 and 52 to 47 and 47), D (29 − 12 = 17), SD (81 − 69 = 12), L (37 + 26
= 63). Every key holds. The gate shows no new FAIL (435 lines, the baseline).

## My own errors

- I added the estimate cue above the exit-45 and exit-51 pictures without checking their scale. The cold recheck caught
  it, and both widths are now fixed.
- One search tool call with a Windows glob returned no matches for "Equation" on the exit pages, though the pages print
  it. I confirmed with a second search before writing the ledger row. No wrong edit came from it.
- No git command was run.

## Changed for the next unit

- An exit with an estimate box is two items: the estimate first, then the measure. Each has its own wrongs and handbacks
  rows, and the goal map lists both.
- Keys and every key piece give the equation first, then the value.
- A page states every limit its key relies on (X39 "Mika has only wide tiles").
- A picture drawn beside an estimate is to scale, so it does not pull toward a listed wrong answer.
- Every estimate station and recheck sets out the checked reference whose spans the key counts.
- Name earlier units' reserved cases by item id, never by nickname.
- A word printed on a child page ("Equation") needs a review row in the ledger and a field 8 mention where it first
  prints.
- Used up: grade 1's reserved 11 and 16 strips, and unit 3's reserved cases (X39 to X54 with X45-estimate and
  X51-estimate, T, E and E2 in all four units, P, C, D, L, SD, S1 to S13, and the F, D and L story rows), including
  X40's 27 cm tab and 20 cm window and its retired 16 and 15 cm windows. Later units keep off them.
