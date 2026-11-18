# Fix report: english-language-arts-grade-11 unit 6 (s06), 2026-11-17

Findings merged: 32 (33 raised; assessment 11 and sources 1 are the same fault, Occom not cleared). Fixed 16, rejected 13, lead 3.
Held up per lens: assessment 12 of 12, sources 3 of 11 (1 shared with assessment 11, 6 and 8), sequence 2 of 10.
Gate: python -X utf8 scripts/unitplan.py check english-language-arts-grade-11 reports PASS for s06.md. The plan sits at the 1,250 word cap, so every counted-field fix was written to fit and the rest are rejected for the cap.

Fixed: assessment 1 to 8 (passage bounds and "final" labels at days 96, 98, 101 to 106; wrong-answer letters at 104, 106, 110, 112; days 109 and 110 exits split, the plowboy analogy and Winthrop's Moses exhortation moved to the comparisons; day 110 instruction moved to the question; day 114 does-not sample), assessment 9 and 10 (marking time by pass, component-to-letter line in field 7), assessment 11 with sources 1 (Occom fallback in field 5 and field 8), assessment 12 (separate breadth-meets line), sources 6 (Brown date marked from memory), sources 8 (label no longer claims a persecution history), sequence 6 (unit 9 hand-off now 151 and 152), sequence 7 (SL parts a to d on 104, 108 uncoded).

REJECTED: sources 4 | Field 10 should name one Scarlet Letter copy and mark the day 96 and 107 frame exits provisional until the frame text is restored | adds about 20 counted words and the plan is at the 1,250 cap (days.csv already says the frame copy must be restored) | over the word cap (UNIT-PLAN "Length")
REJECTED: sources 5 | Winthrop's edition label and the quoted phrase "Now the onely way" may not match the modernized Hanover page | needs the page opened and about 15 counted words; over the word cap | over the word cap (UNIT-PLAN "Length")
REJECTED: sources 7 | Terms of reuse of the modern transcriptions (Winthrop 1996, Longfellow 1998, undated archives) are not named | adds a line to a plan at the cap; the lead should rule on reset packets | over the word cap (UNIT-PLAN "Length")
REJECTED: sources 10 | First-publication years and Wheatley's source volume are not given for the poems | about 15 counted words, over the cap | over the word cap (UNIT-PLAN "Length")
REJECTED: sources 11 | The "five whole works, four excerpts" count does not state its counting rule | about 10 counted words, over the cap | over the word cap (UNIT-PLAN "Length")
REJECTED: sequence 1 | Days 100 to 103 and 105 carry 44 to 56 minutes of first reading with no split | a per-day reading split is a section or day plan matter and the plan is at the cap | UNIT-PLAN field 9 of the section plan (reading load); over the word cap
REJECTED: sequence 2 | Day 96 has no time budget and begins several standards | same reason; day budgets belong to the day plan | UNIT-PLAN section plan field 6; over the word cap
REJECTED: sequence 3 | Day 111 has no time budget and teaches many W parts in one day | same reason | UNIT-PLAN section plan field 6; over the word cap
REJECTED: sequence 4 | Editing and publishing (W.11-12.5, W.11-12.6) have no class day and day 114's 45 minutes do nothing the check needs | field 5 already states day 114 is filing plus unscored rereading by design, and days.csv fixes the day shape | days.csv; over the word cap
REJECTED: sequence 5 | Unit 5 promised religious judgment returns on days 96 and 104 and this plan does not say how | the promise belongs to unit 5's plan; adding a claim here invents teaching not in days.csv and costs counted words | none (lead should reconcile unit 5 or give the line)
REJECTED: sequence 8 | Field 8 names no device for the shared digital draft and calls W.11-12.6 both planned and unfinished | needs about 15 counted words and a lead ruling on the device supply | over the word cap (UNIT-PLAN "Length")
REJECTED: sequence 9 | Days 106 to 108 give no home-reading amounts or retrieval placement | day-plan detail, plan at the cap | UNIT-PLAN section plan field 6; over the word cap
REJECTED: sequence 10 | The tracker fade after day 103 has no test | day-plan detail, plan at the cap | UNIT-PLAN section plan field 6; over the word cap

LEAD:
- sources 2: confirm against the Occom transcription that the service and pay account, "I leave it with the World" and the plowboy analogy lie inside the stated excerpt bounds; extend field 10 bounds if so.
- sources 3: add rows for the seven texts with no record (Wheatley, Occom, Emerson's two excerpts, Brown, Winthrop, Each and All, The Arrow and the Song) to data/plans/ela-texts.csv.
- sources 9: open each field 10 URL and confirm the quoted passage is on the page (Wikisource page numbers 51 and 53, Occom, both poems, Winthrop spelling, Quaker page fit); add checked wording only after that.
