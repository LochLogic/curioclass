# Science K to 3 continuity read, 2026-11-22

Courses: science-kindergarten, science-grade-1, science-grade-2, science-grade-3. Report only; no day file was edited.
Helper and claim list: `_scratch/scifix/tmp/science-k-3-continuity/` (claims.py, claims.csv, q.py, tan.py, recheck.txt).
The brief named two helper folders (`tmp/continuity-science/` in WORK step 2, `tmp/science-k-3-continuity/` in the
helper rule); everything went in the second.

## Totals

| Measure | Count |
|---|---|
| Lines matched by the claim helper (grades 1 to 3) | 104 |
| Cross-grade claims (after dropping 6 lines that cite nothing) | 98 |
| Held | 88 |
| Drifted | 9 |
| Could not judge | 1 |
| Taught as new | 3 |
| Recheck problems | 7 (5 planned only, 2 unmatched; none is a day-text fault, see below) |

Dropped as not claims: grade-1 u05-1 d040:39, grade-1 u08-1 d068:39, grade-2 u07-2 d076:47 and d076:74, grade-3
u02-2 d025:37 (a heading; judged with d025:39), grade-3 u03-2 d046:81.

## Recheck (ledger.py recheck science)

```
science-grade-2 u06-1 (planned): Pip says one line, the class checks it against evidence | cites science-grade-2 u05-2 day 51 -> planned
science-grade-2 u07-1 (planned): Pip says one line, the class checks it against evidence (rev | cites science-grade-2 u05-2 day 51 -> planned
science-grade-3 u04-3 (planned): does well, does poorly (review of the design sense) | cites science-grade-3 u02-2 days 17,18,19 -> planned
science-grade-2 u01-1 day 2: key (a box that tells what each mark means) | cites science-grade-1 (map key) -> unmatched
science-grade-2 u01-2 day 6: map key (what each dot means; here the filled dot is liquid  | cites science-grade-1 (map key) -> unmatched
science-grade-2 u04-1 day 42: solid water, liquid water (review: ice keeps its shape, liqu | cites science-grade-2 u03-3 day 36 -> planned
science-grade-2 u07-1 day 68: Pip says one line, the class checks it against evidence (eve | cites science-grade-2 u05-2 day 51 -> planned
science recheck: 2675 citations; target written 2668, planned only 5, unmatched 2; target day gone 0; flagged 7
```

What each is (all are ledger-note citations, not day text):
- Grade 2 "Pip says one line" (3 rows): day 51 is written, in u05-1 (`courses/science-grade-2/u05-1/d051.md`), not u05-2. Fix the note's where to u05-1.
- Grade 2 u04-1 day 42: day 36 is written in u03-2 (`courses/science-grade-2/u03-2/d036.md`, solid water taught), not u03-3. Fix the where to u03-2.
- Grade 3 u04-3 planned "does well, does poorly": u02-1 days 17 to 19 never say it; the design sense is taught in u02-2 days 25 to 28 (d025:39 "it does well"). Fix the citation to u02-2 days 25 to 28.
- Grade 2 map key (2 rows): the notes cite social-studies-grade-1, which did teach map (u02-2 day 14, u05-1 day 44) and key (u05-1 day 45); recheck reads the bare "grade-1" inside the course name as science. Not a content fault; a tool point for cross-subject citations.

## Drifted claims

### science-grade-2

- u01-1/d003.md:47 - "the grade 1 gallery again" - grade 1 never had a gallery; its share was the partner sketch explain (science-grade-1 u02-2 day 17, "this shape ___, so ___"). Fix: say "like the grade 1 partner share" and keep the gallery as new today. Stage: day writer (ledger note already says partner share).
- u01-1/d003.md:65 - "The gallery (review from grade 1)" - same as above. Fix: "The gallery (new today, built on the grade 1 partner share)". Stage: day writer.
- u01-2/d006.md:31 - "Review the two chick pages from grade 1" - grade 1 had one chick page, as an assessment item (science-grade-1 u08-1 day 67, c2-A67b, beside a lamb page); the taught young-animal pages were robin and fawn (u07-1 days 56 to 58). Fix: "Review the robin pages from grade 1 (days 56 to 58)" or present the two chick pages as new, invented for practice. Stage: day writer.
- u02-1/d011.md:39 - "Remember the kindergarten forecast: a forecast warns of strong wind." - kindergarten's forecast was a storm and thunder page that led to a plan for indoor recess (science-kindergarten u02-2 days 15 to 17); strong wind was never named. Fix: "Remember the kindergarten forecast: a page said a storm might come, so we planned indoor recess." Stage: day writer.

### science-grade-3

- u01-1/d001.md:41 - "A push or a pull is a force (review from kindergarten)." - kindergarten taught push and pull (days 1 and 3), never the word force; the ledger has force first taught here. Fix: "Push and pull are review from kindergarten; force is the new word for either one." Stage: day writer.
- u02-2/d025.md:39 (with heading d025:37) - "Show the two paper carriers, review from grade 2" - the carriers are new, invented today (ledger: taught day 25); grade 2 taught barriers, does well and does poorly, and limit (science-grade-2 u02-2 days 16 to 19). Fix: "Show two new paper carriers, invented for practice; does well and limit are review from grade 2." Stage: day writer.
- u03-1/d037.md:39 - "Review from grade 2: flowers help make seeds, fruits keep seeds safe, and pollen is not a seed." - grade 2 taught pollen is not a seed and flowers making pollen (science-grade-2 u06-1 days 60 to 63); no grade 2 day mentions fruit. Fix: keep flowers and pollen as review, teach "fruits keep seeds safe" briefly as new. Stage: day writer.
- u05-1/d082.md:32 - "six children ... each say one grade 2 fossil note and its source" - no grade 2 day mentions fossils; grade 2 taught slow change from two sources, a picture and the words that say when (science-grade-2 u02-1 days 12 to 14). Fix: cut "grade 2 fossil note"; have them say one grade 2 slow-change note and its source, or read today's fossil caption together. Stage: day writer.
- u06-3/d109.md:35 - "Review: grade 2 barriers, goals and limits, merit." - grade 2 taught barriers and limits (u02-2 days 16 to 19) and does well or poorly; goal and merit are grade 3's own (science-grade-3 u05-2 day 87). Fix: "Review: grade 2 barriers and limits, and merit from day 87." Stage: day writer.

### Could not judge

- science-grade-2 u03-1/d027.md:35 - retrieval card "which has a bowl for soup", called a review of grade 1 and unit 2. No earlier written day in science K to 2 names a bowl for soup; it may stand for grade 1 shape and job (u02-1 day 15). The lead or the grade 2 fix job should say which, or mark the card new.

### Held, worth a word (not faults)

- science-grade-2 u01-1 d001:33, d002:85, d004:84 "grade 1 map words", "Map, as in grade 1": held through social-studies-grade-1 (map day 14, key day 45). Optional wording: "grade 1 social studies".
- science-grade-2 u01-1 d002:21 "splash goggles from the start, as in kindergarten": kindergarten wore impact eye protection from day 1; the habit holds, the type is new.
- science-grade-3 u04-1 d060:27 "a chick calls and the parent brings food": grade 1 taught it with a young robin (u07-1 day 57); holds.

## Taught as new

- science-grade-2 u02-2/d017.md:53 - about the same - science-kindergarten u01-1 day 2 (nearer, farther, about the same) and u05-1 days 46 to 48. Fix: add "About the same is from kindergarten; today it means numbers 1 centimeter apart." Keep the minutes.
- science-grade-3 u04-3/d069.md:35 - missing link - science-kindergarten u04-2 day 36 (system: a missing link means it cannot live there). Fix: add "a missing link, as on the kindergarten system chart (review)". Keep the minutes.
- science-grade-3 u06-2/d104.md:35 - source ("A source is a card or page that tells you something.") - science-grade-2 u01-2 day 6 (source: a page or picture that gives information). Fix: add "(review from grade 2)" to that sentence. Keep the minutes.

Checked and not faults: grade-3 d028 tradeoff (day says "from grade 2"), grade-3 d098 season (day says review), grade-3 d045 litter (animal litter, not kindergarten's waste litter), grade-3 d025 need (design need, a different sense; d069 reviews the living-thing need), grade-2 d006 source (day itself sets the new sense apart), grade-3 d086 uncertain (used in a word list, not taught), and the return and repair and question board routine rows (used again, not taught again).

## Lead run notes

No file listing capstone items for this subject was named in the brief, so there was nothing to cross-check.

## Fixes applied (2026-11-22, science-grade-2)

- u01-1/d003.md:47 gallery: applied. Now "new today and built on the grade 1 partner share"; ledger day 3 note set to new, builds on science-grade-1 u02-2 day 17.
- u01-1/d003.md:65 gallery (at home skip): applied. Now "new today, built on the grade 1 partner share".
- u01-2/d006.md:31 chick pages: applied. Now "two new chick pages, invented for practice, like the grade 1 robin chick pages"; miss line trimmed to hold the cap. Ledger day 6 chick row note set to new pictures, recalls science-grade-1 u07-1 days 56 to 59.
- u02-1/d011.md:39 kindergarten forecast: applied. Now "a page said a storm might come, so we planned indoor recess. Today the forecast warns of strong wind." Ledger notes already right.
- Taught as new, u02-2/d017.md:53 about the same: applied. Added "About the same is from kindergarten; here it means numbers 1 centimeter apart." Trimmed the chart timing aside and one width phrase so the page holds its cap; minutes unchanged. Ledger day 17 note set to extends science-kindergarten u01-1 day 2.
- Could not judge, u03-1/d027.md:35 soup bowl card: holds. The card is a spoon and fork, keyed "its shape fits the job", which is grade 1 shape and job (science-grade-1 u02-1 day 15, "Which shape could do the job?"); the pictures are new. Reworded to "which shape holds soup (grade 1 shape and job)"; ledger day 27 note records it.
- Recheck, Pip says one line: partly. Day 68 and the u06-1 planned row now cite u05-1 day 51. The u07-1 planned row ("... (review)") could not be set: `ledger.py note` matches by day only, and 7 planned grade 2 rows share that entry with a blank day. Tool point for the lead.
- Recheck, u04-1 day 42: applied. Note now cites u03-2 day 36.
- Recheck, map key (2 rows): left; the report calls it a tool point (social-studies-grade-1 read as science).
- Gates: plan.py check science-grade-2 17 FAIL before and after (all "section is not in data/units.csv" and the s02-E11/E12 shared numbers, unchanged); lesson.py check filtered 0 FAIL before and after.

## Fixes applied (2026-11-22, science-grade-3)

- u01-1/d001:41 force: applied. "Push and pull are review from kindergarten; force is the new word for either one."
- u02-2/d025:37 and :39 carriers: applied. Heading now "Retrieve grade 2 design words"; line opens "Two new practice carriers; does well and limit are grade 2 review." Rest of the line trimmed to hold the 675-word cap; items and expected answers unchanged.
- u03-1/d037:39 fruit: partly. The ledger shows grade 1 taught "fruits keep seeds safe" (science-grade-1 u02-1 days 10 and 11), so it stays review, now credited to grade 1: "Review: pollen is not a seed (grade 2); flowers help make seeds and fruits keep them safe (grade 1)."
- u05-1/d082:32 fossil note: applied. Children now say one grade 2 slow-change note and its source (a picture or the words that say when); a miss reads today's fossil caption.
- u06-3/d109:35 goals and merit: applied. "Review: grade 2 barriers and limits; this year's goals and merit." (goal is grade 3 u02-2 days 25 to 28, merit day 87). Misses line trimmed for the cap.
- Taught as new, u04-3/d069:35 missing link: applied. "a missing link (review from kindergarten), so it cannot stay." Minutes unchanged.
- Taught as new, u06-2/d104:35 source: applied. "(review from grade 2)" added. Minutes unchanged.
- Recheck, u04-3 planned "does well, does poorly": ledger note for the lead (below); not written, per the lead's change to the brief.
- Ledger entries for the lead (ledger.py note not run, per the lead's change to the brief):
  - science-grade-3 day 37 "flower, fruit, seed; pollen is not a seed" -> "review of science-grade-2 u06-1 days 60 to 63 (pollen is not a seed) and science-grade-1 u02-1 days 10 and 11 (flowers help make seeds, fruits keep seeds safe)"
  - science-grade-3 day 69 "missing link (a need that no condition of the place meets, marked with a cross; the kind cannot stay)" -> "review of science-kindergarten u04-2 day 36; grade 3 sense: a need no condition meets, marked with a cross"
  - science-grade-3 day 104 "source (a card or page that tells you something: an atlas card, a station card)" -> "review of science-grade-2 u01-2 day 6"
  - science-grade-3 day 25 case "two paper carriers for two blocks, one holding three and one holding one (invented for practice)" -> "invented for practice, new day 25; does well and limit reviewed from science-grade-2 u02-2 days 16 to 19"
  - science-grade-3 u04-3 (planned, no day) "does well, does poorly (review of the design sense)" -> "review of science-grade-3 u02-2 days 25 to 28"
- Gates: plan.py check science-grade-3 21 FAIL before and after, output identical (all "section is not in data/units.csv"); lesson.py check filtered 0 FAIL before and 0 after (four pages briefly went over the cap and were trimmed back).
