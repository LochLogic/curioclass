# Section refine: english-language-arts-grade-4 unit 2, sections 2.1 to 2.7 (days 39 to 77), 2026-11-27

I ran this pass after the cold answer-key read of the same unit (answer-key-english-language-arts-grade-4-u02-2026-11-27.md). I reconciled both sets of fixes in the plans, the ledger, the shared pieces and the unit's data rows.

**Rules read:**
- docs/pipeline/briefs/section-write.md
- UNIT-PLAN.md ("The rules", "The section plan: fields, in order", "Length")
- DEFAULTS.md
- docs/APPROACH-ELA.md
- s02.md

**Skeletons:** rebuilt first with `python -X utf8 scripts/section_skeleton.py english-language-arts-grade-4 u2`.

**Prep notes:** build/sections/prep/english-language-arts-grade-4/u02-<n>.md do not exist (that folder holds only math-grade-1). I worked without them.

## What I checked, and what held

- **Minutes.** All 39 days add to 90 under DEFAULTS.md parts.
- **Turns.** Every spoken check hears six named children at 45 seconds (4.5 minutes). Everyone else hands back paper with a written next step in the next named repair slot. Day 50's other 24 oral turns are moved to day 51 Independent reading. Device waves fit: 15 devices for 30 children in two turns.
- **Length.** Words outside fields 3, 4 and 6 run from 606 (u02-2) to 1,025 (u02-5), all under the 1,600 cap.
- **Owed items.** Every item the rebuilt skeletons owe is named in its plan. S54's five components are described together in u02-3 field 3. Every exit column in days.csv matches its exit items, including the new X60-word, X73-detail and X74-end.
- **Codes.** Field 1 names every day code except the SL.4.1 gap below.
- **Rule 4.** These pass:
  - Word-work teaching words (photosensitive, autograph, telescope, telephone, transport, interrupt, disruption, eject, inject, audible, visible) appear in no unit 2 exit or check.
  - Telegraph, telephoto and photographic are checked cold.
  - Photograph is review on purpose.
- **Letters.** Every wrong carries one letter from the s02 register, and the letter gate passes.
- **Terms and notation.** Each is taught before it is tested: wary and recoiled on 41, can/may/must on 42, tele on 47, port on 51, rupt on 56, ject on 61, adjective order on 73.
- **Plain words.** No em dash and no writer TODO marker in the seven plans or the unit's pieces.

## Faults

| File | Fault | Fix or rejected, with why | Stage |
|---|---|---|---|
| u02-1 | Field 1 did not name SL.4.1a/b/c/d, though day 40 codes them for formal discussion. | Added: SL.4.1a/b/c/d, "Come," "Follow," "Pose and respond" and "Review," guides formal discussion on 40. | write |
| u02-1 | Day 43 modeled a faulty sense with plate, but S54 on day 54 checks plate's sense (rule 4). | Model word now band, a music group versus an armor strip. Band is checked nowhere in the course; the kindergarten band card is a different case. | write |
| u02-1 | D44m dictated protection, a grade 3 case (u04-3 day 130). | distraction and attraction, with the reason in the line. Matches items.csv and word-probe-key.md. | write |
| u02-1 | Field 3 D44 table (9 rows) and the X42 key had drifted from items.csv. h-digital's wrong was E in the plan and I in data. | Rows set to the item stems, keys and letters. | write |
| u02-2 | X47 ask and key: singular "distinction", and the key had no locations. | Synced to the fixed item. | write |
| u02-2 | X50 was coded RI.4.9 but read one paragraph. | Reserved passage now pairs the familiar book overview, paragraph 5. Ask, key, Shape, day 50 exit line and both day 50 shape lines updated. The exit line now names X50-oral for the pairs and X50 for the paper. | write |
| u02-2 | D48 overrides (7 asks) did not match the stems. | Set to the stems, with keys from data. | write |
| u02-3 | X55 key, D56a/f overrides (7 asks) and the cold-solving "Main point means main idea" no longer matched data after the A56f-sense fix. | Synced. a-question renamed a-questions to match the item id; K added for an off-aspect answer, as in wrongs.csv. | write |
| u02-4 | X60 asked two things. | Split into s02-X60 (L.4.1c) and s02-X60-word (L.4.6), each with an Ask, Key and Shape. Day 60 exit, shape and evidence lines name both. Cold-solving "Can shows ability" now reads "ability or what is possible" (A62j-can fix). | write |
| u02-5 | X65 "Name the part you used" read as a body part. | "Name the source section you used." | write |
| u02-6 | X73 asked two things. | Split into s02-X73 (L.4.1d) and s02-X73-detail (W.4.3d). Day 73 exit, shape and evidence lines updated. | write |
| u02-7 | X74 asked two things. | Split into s02-X74 (W.4.3c) and s02-X74-end (W.4.3e). Day 74 exit, shape and evidence lines updated. | write |
| u02-7 | D74c/e asks did not match the stems. | Set to the stems. | write |
| u02-7 | Day 74's D75h line ("large and rough before shell") printed the key order. | "put rough and large in order before shell", as in the fixed item. | write |
| u02-7 | Field 1 seemed to lack W.4.9b. | Rejected: it is named ("W.4.5/6/7/8/9b ... Apply"). My code script misparsed the slash list. | none |
| u02-1 | X43 "Use the talk and chart" seemed vague. | Rejected: the comparison is read aloud twice just before the exit, so "the talk" is clear. | none |
| u02-4 | C61-spelling's word, appearance, is printed correctly in X61 earlier on day 61. | Rejected for the plan: the evidence is the recorded lookup, and a new word needs a data row first. Listed under plan points. | prep |
| u02-3 | S54 components and A56a-body/setting/protection are not quoted one by one. | Rejected: S54 is described as one record by design, and the A56a line quotes the shared stem with the aspect in brackets. | none |

## Ledger rows

These were checked with `ledger.py show ela --course english-language-arts-grade-4 --term`, then fixed or added through ledger.py:

**Fixed (with `ledger.py note`):**
- u02-1 case D44: the note now reads distraction/attraction, and says why protection left.

**Added (one `add` call each, day blank):**
- u02-1 case: Day 43 faulty-sense model, band.
- u02-2 case: the s02-X50 pairing with g4-u2-01 Overview, paragraph 5.
- u02-4 case: s02-X60-word.
- u02-6 case: s02-X73-detail.
- u02-7 case: s02-X74-end.

None cites a lower-grade row, so no "planned only" note was needed.

## Gates

- `python -X utf8 scripts/unitplan.py check english-language-arts-grade-4`: PASS for s02.md and u02-1 to u02-7. s01.md shows FAIL (4); that is unit 1, not touched here.
- `python -X utf8 scripts/ledger.py check ela`: 10802 rows, 0 problems.
- `python -X utf8 scripts/gate.py --course english-language-arts-grade-4`: 0 failing findings, 1 new note line. No new FAIL.
- No em dash and no writer TODO marker in the u02 plans or pieces.

## Plan points

- **s02.md** (I may not edit it) still prints the old forms:
  - "Write protection and photograph" (day 44 L.4.2d row)
  - "Arrange large and rough before shell" (day 75 L.4.1d row)
  - "choose which point meaning fits a report's main point" (D56 row)
  
  The plans and data now differ from it on purpose.
- **s02.md** day 61's exit, "Edits a fresh short passage for quotation marks and one misspelling", has no data row for its spelling part. C61-spelling lives only in u02-4 field 3. A data job should register it, using a word not printed on the X61 slip.
- **Prep notes** for this unit are missing.
- **section_skeleton.py** printed "written" for all seven skeletons, then exited with code 1 and printed no reason.
- **g4-u2-04** names an outside author and book title in its opening paragraph. This is for the text owner.
- **Core text sentences** over the grade cap stay with the text owner, as the plans already note.

## My own errors

- My field 1 code script misread "W.4.5/6/7/8/9b" and reported W.4.9b missing in u02-7. I caught it by reading the line, and I made no edit.
- I first listed the X42 key line as out of sync. It matched in meaning; I aligned its wording to the item anyway, keeping the escape-limit note.

## Changed for the next unit

- Split any exit that asks two things before writing its key. Each part gets its own item, key, wrongs row, handbacks row and print line.
- Check every dictation and probe word against the lower-grade ledger, not only the newest word in the pair.
- Keys use only what the child's page shows. Species names and facts from teacher notes do not belong in a key.
- Write field 3 asks and override tables as the item stems, word for word, and rerun the stem sync after any data change.
- Keep key words out of stems: no stem should print the answer or list words in the key's order.
- An RI.4.9 exit needs two texts, even when one of them is familiar.
- When one day has a punctuation or editing exit and then a spelling check, keep the check word off that exit's slip.
