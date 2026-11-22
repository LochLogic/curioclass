# Finish fix: science-kindergarten, 2026-11-22

Stage 7, one fix pass over the ten fresh-reader reports. Each report now ends with "Fixes applied (2026-11-22)", one line per finding.

## Counts per report

| Report | Applied | Rejected | Left |
|---|---|---|---|
| Answer key, checks | 6 | 0 | 0 (tag question to the lead) |
| Answer key, unit 1 | 9 (one in part) | 0 | 0 |
| Answer key, unit 2 | 8 | 0 | 1 (F3a distractor kept) |
| Answer key, unit 3 | 5 | 0 | 1 (P2b "stays low") |
| Answer key, unit 4 | 8 | 0 | 1 (s04.md rabbit or turtle, lead) |
| Answer key, unit 5 | 6 | 0 | 0 |
| Answer key, unit 6 | 4 | 1 (T1b second ask) | 0 (2 need no change) |
| Safety | 13 (3 H, 7 M, 3 L) | 0 | 0 |
| Sensitivity | 8 (4 M, 4 L) | 0 | 4 could-not-settle (2 to Cory) |
| Cold read | 11 (3 in part) | 0 | 9 |

New item: s01-E2b (split from E1/E2), s05-D2d (split from D2c). Items 357, wrongs 300.

## Safety page

courses/science-kindergarten/safety.md, about 870 words, a teacher page. It covers the stop rule, eye protection (Z87.1, fit-over goggles, cleaning, the recorder path), hand washing, allergies (plants, foods, latex), plants, soil, sand and mold (Safety Data Sheet), the outdoor check and adults, sun-warmed surfaces and the lamp, electricity, magnets and small parts (the fist and tube test), glass and sharp things, and clean-up. Each rule names its days. The day files' "Outdoor check done (safety page)" and "too warm for your hand at a count of three is not cleared" point to it. DEFAULTS.md names it. sources.csv row SAF1: NSTA "Safety in Elementary Science", opened and read 2026-11-22.

## Gates

- plan.py check: before 13 FAIL, after 13 FAIL, all "section N.N is not in data/units.csv" (known). Sequence 0.
- lesson.py check: before 0 FAIL, after 0 FAIL.
- Note for the lead: the full runs of both scripts now crash on data/plans/science-grade-1/days.csv row 26 (a row with more fields than the header: "keywords must be strings" at plan.py line 1020). That is another course and was not touched. The after counts come from `plan.py check science-kindergarten` with the same awk filter, and from lesson.py's own check run over this course's day files only (helper lesson_k.py in my scratch folder). Please re-run the full gates once grade 1 is fixed.
- Also fixed: materials.csv "shallow plastic water trays" row had a stray seventh field (an unquoted comma in its note); it is joined back into the note.

## For Cory

1. **Local severe-weather hazard (K-ESS3-2, unit 2 days 15 to 19).** The days use labeled Denver and Seattle records, so "where students live" is not localized. Options: (a) keep Colorado as the worked example and add a one-line teacher swap "use your state's weather service page for your region's most common hazard"; (b) write region variants (thunder, snow, heat, wind) with checked state sources; (c) keep as is. My pick: (a), as it needs no new data and keeps the day count.
2. **Element-level coverage table (scope, S11).** Options: (a) add a table counting each practice and crosscutting concept per unit to scope-and-sequence.md; (b) leave expectation-level coverage. My pick: (a), at the scope stage for all science grades together.
3. **Unit 5 W2 caption transcription and the 80 percent idea rule.** Options: (a) replace the transcribing points with one spoken reason per material; (b) keep W2 and lower its weight. My pick: (a).
4. **One scoring scale for unit 2.** s02 scores by points; the sections use shown / shown with help / not yet seen. Options: (a) the three-step scale everywhere, written in s02; (b) points everywhere. My pick: (a), it is what the days use.
5. **Unit 4 assessment time (day 41, about 4 seconds an answer).** Options: (a) cut the spoken parts to one brief reason per code, as the unit plan says; (b) spread the groups over days 41 and 42 (changes day 42). My pick: (a).
6. **Days 48 and 51 fold versus full.** Notes say fold into 46 and 50 but the rows remain. Options: (a) keep them as full days and fix the notes; (b) fold them (changes the day count). My pick: (a).
7. **Sensitivity, could not settle.** (a) Family notes: NAEYC and Head Start pages refused automated reads (403), PTA 404; the notes follow the course's own rules. Options: keep as is, or have the lead open those pages in a browser and check the notes. My pick: browser check at grade close. (b) Disaster voices: s02.md says two voluntary public accounts are "still to select". Options: select two calm public accounts with sources, or drop the line and keep children's own non-disclosure talk only. My pick: drop the line for kindergarten.

## For the lead: sweep

- c1-T1 keeps its K-2-ETS1-1 tag as a transfer item or is retagged (checks, item stage).
- c1-F3 and c1-F3b each have two asks in one stem (checks, item stage); found late in this pass and not split, so each needs its own item, key, wrongs, handback and print line.
- s04.md generated table says rabbit where the item now says turtle (unit plan stage).
- Unit 2 exits are mostly touch-a-card recognition (data stage, from the item writing); replacing some with a spoken reason means new exit items across days 10 to 17.
- u04 s04.md:52 limit "no controlled deprivation experiment" versus the dark-shelf plant (unit plan stage).
- data/units.csv: 13 sections not registered (repository data).
- Ledger: no ledger entry needs a change from this pass.

## Left

- Day 12 morning mark for every child: needs a morning slot outside the lesson; every child already marks the afternoon bench.
- Answer key unit 2, F3a wrong card: a fair distractor by the reader's own account; kept.
- Answer key unit 3, P2b "stays low": consistent with the card; kept.
- Sensitivity L5 per-day eye protection line in unit 1: carried by the safety page and materials row instead, as days 1 to 9 sit at the word cap.
- Day 37 plan limit alignment and the day 33 limit line: unit plan stage.

## Browser check

- The NAEYC and Head Start family-engagement pages named in the sensitivity report (its urls, 403): guidance only, no fact rests on them, no sources.csv row.
