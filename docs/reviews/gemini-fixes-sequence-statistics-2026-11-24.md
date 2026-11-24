# Gemini fixes: scope and sequence of statistics, 2026-11-24

The fix pass on the outside second read S:\CurioClass-gemini\reports\sequence-statistics-gemini-read.md, after the expert read (docs/reviews/sequence-statistics-2026-11-24.md) and its fix pass (docs/reviews/sequence-statistics-fixes-2026-11-24.md). Every finding was checked against the files. Files changed: data/plans/statistics/days.csv (day 149 note), data/plans/statistics/source-map.csv (three rows added), docs/courses/statistics/scope-and-sequence.md (Check 3 row, Language goals paragraph). No unit, unit order, owned row, day count or code list changed.

Totals: 5 items. Holds 1, partly 2, wrong 1, already fixed 1.

## Findings

- **G1, earlier-grade retrieval ids in `skills` on 13 days** (days 5, 6, 12, 18, 19, 25, 31, 36, 49, 79, 130, 138, 142): wrong. The ids are there and every note says retrieval, but they are retrievals, not readiness rows. sequence-write.md rule 2 and the Desk decision of 2026-11-15 keep *readiness* rows out of `skills` (days 1 and 46 hold readiness, and their `skills` carry no earlier-grade id). Math lead call 4 (docs/reviews/sequence-lead-calls-2026-11-15.md) puts a retrieval's row id in `skills`, and the unit skeleton counts a retrieval day by exactly that (scripts/unit_skeleton.py earlier_rows: id in `skills` plus "retriev" in the note). Removing them would drop the retrieval count. The expert fix pass already recorded math lead call 4 as held. No change.
- **G2, source-map.csv has no row for the nine course-level days** (44 to 46, 90 to 92, 149 to 151): partly. True, and rule 8 has `ours` "for a day with no base lesson". Gemini's fix (unit blank or `C`) fails the gate (a non-cut row needs a unit 1 to 10). Added three `ours` rows, one per check window, filed under the unit before it (3, 6, 9) with a why that names stretch C and says the unit is the filing place only, as Algebra II's map does. Every day 1 to 160 is now in the map.
- **G3, day 149's fluency station budget (about 15 minutes for seven items)**: partly. The expert's settled form stays (one short conditions-and-calculation item per fluency from a given summary, five audit codes CUR-ST.6, 9, 11, 14, 15, Settled table of the fix pass); trimming the audit set to four would undo that, so it is not taken. The minute figure was an estimate and is tight for an untimed station: the station is now about 20 minutes and the five audit items the other about 20 (50 minutes less the opening and papers leaves about 40). days.csv day 149 note and the scope's Check 3 row.
- **G4, calendar.csv stale** (Gemini's judgment of For the lead 3): already fixed in the sense that it is listed. `frame.py sync` writes a shared file this pass may not edit; it stays with the structure pass (expert finding 11, scope For the lead 3). No change.
- **G5, no language goals line** (Gemini's "could not judge": RUBRIC-MATH-HS gap 9 not placed, unlike Precalculus): holds. Gap 9 asks for a line in each scope and sequence on how language goals grow, and the frame applies the multilingual criteria in full. Added a "Language goals" paragraph before unit 1: frames and a word bank in units 1 to 3, frames for new forms only in 4 to 6, written frames dropped in 7 to 9, unaided in unit 10's report and talk; teacher notes, home language and check accommodations owed by the unit plans. Per-section goals stay with the unit plans.

## Fact checks

Gemini flagged no fact as wrong. Two of its confirmations were checked again:

- One-cent coin masses 3.11 g (95 percent copper) and 2.5 g (copper-plated zinc), both struck in 1982, so excluding 1982 is right: [Wikipedia, Penny (United States coin)](https://www.wikipedia.org/wiki/US_cent), [PCGS CoinFacts 1982](https://www.pcgs.com/coinfacts/coin/3045).
- Azzalini and Bowman (1990), Applied Statistics 39(3), 357 to 365: 299 consecutive eruptions, a second-order Markov structure, so the series is not independent (days 142 to 143 treat it as a conditions case): [EconPapers record](https://econpapers.repec.org/RePEc:bla:jorssc:v:39:y:1990:i:3:p:357-365), [MASS geyser documentation](https://www.rdocumentation.org/packages/MASS/versions/7.3-51/topics/geyser).

Browser check urls: none.

## Settled kept

- Math lead call 4 (retrieval ids in `skills`) over G1.
- Expert fix 6 and the fix pass's Settled row (day 149 form and its five audit codes) over G3's trim option.

## For Cory

Nothing. No change touches scope, audience, money or people, and no unit or day count moved.

## Gates

- `python -X utf8 scripts/sequence.py check statistics`: 0 failures, 0 notes.
- `python -X utf8 scripts/frame.py check statistics`: 0 failures (10 units, 160 days).
- `python -X utf8 scripts/frame.py calendar`: runs clean, exit 0.
