# Cleanup, science-grade-1, lane 4 (u07-1, u08-1; days 9, 56 to 68), 2026-11-22

## Findings

FIRM
- i:21, d059, applied: X59a and X59b are now touches on three word strips read aloud (chick, adult penguin); items, wrongs, cards-exits, section plan synced.
- i:22, d057, applied: X57c is a new pea case (three loose pictures, no arrows); bean page stays teaching only.
- i:25, d060, applied: turns hold E60a only; E60c moved to a whole-class thumbs part (3 min "Every animal"); minutes rebalanced, total 34 kept; days.csv check_min synced.
- j:20, d067, applied: lane turn holds M67a only; M67b, M67c, M67d asked to the whole class in Record completion.
- j:21, d067, applied: A67 and S67 items read aloud stem by stem to the whole class, one ask each; S67a thumbs.
- j:22, d067, applied: third place is Seattle (Jan. 10 and Apr. 10, USNO one-day service), strips-key rows, card SVG strips, sources.csv 13P.
- j:23, d066, applied: each child tries three pieces and marks all three cards (T66a, marked after class), then the mirror (T66b).
- j:24, d066, applied: Plans draw only lamp, one piece and screen with stays-still and changes marks; P66a plus new P66b.
- j:25, d066, applied: home key matches the home set.
- j:26, d063, partly: 48 cm strips rejected (page width); cut-out strips slid with sunrise pictures together instead, X63b split into X63b and new X63c.
- j:27, d068, applied: fresh exits X68a to X68e are new cases and shapes (draw the patch, drum record, April 10 shadow drawing, elephant seal pup and mother, source 13Q).

SOFT
- a:42 d058 applied (robin photograph named in Materials, Before class, Safety). a:45 d058 applied (exit 6 min, strips read aloud; Share and Revise trimmed, total kept).
- i:31 applied (u07-1 and u08-1 exit text). i:34 d056 applied (X56b distractor is an adult resting). i:35 d056 applied (unit 2 respond retrieval line). i:36 d057 applied ("parent plant, as in unit 3"). i:38 d057 applied (six heard). i:40 d059 applied (side label). i:41 d060 applied (sheets down, waiting groups unscored). i:42 d060 partly (diagram out of order, no arrows, no words; still a sunflower).
- j:28 d067 applied (new Seattle claim). j:31 applied (days.csv day 67 holds, spelling). j:32 d067 applied (home swap is drawn). j:33 applied (cards rule allows word strips read aloud). j:35 d066 applied (one ask per stem, P66 split, V66b yes or no). j:36 d066 applied (closet look at night, lamps off). j:37 applied (day 66 supplies). j:38 applied (mirror tilted in the beam). j:39 applied (X68d replaced). j:40 d068 applied (hand-off record after class). j:41 d068 applied (cue cards named). j:43 d063 applied (Open is a thumbs judgment). j:44 d063 applied (split). j:46 applied (US spelling across lane files and CSVs). j:52 d061 applied (X61c one ask). j:55 applied (E64a B note).
- Rejected: i:30 ("drawn" is not a path the scripts know; spoken is right).
- Left: a:43 (ladder term, lead), a:44 (X58b matching), a:46 and i:44 (source re-dates 12C, 12G, 12D, 12F, 12H), a:47 (shape-note job), a:48 (home exits for per-class cards), b:46 to b:50 (Denver fresh dates, home swaps), i:37 and j:53 (alligator overuse; needs new sourced animals), i:39 (X59c shape), j:29 (A67b chick), j:30 (lamb, calf, pumpkin sources), j:34 (V66b, T66b cases), j:42 (unit letters), j:45, j:47 (d009), j:48, j:49, j:50 (d062), j:51 (d061 practice shape), j:54 (d064 timing).

## Key lines (part C)

Scanned piece files in u07-1 and u08-1 (not day files, not key-*). Hits only in cards-exits-56-61.md (15 "Key:" lines): teacher-only (exit card descriptions held out of sight by the teacher), left. strips-key.md has no hits and is teacher-only. Nothing moved.

## Gates

- plan.py filtered: before 67 FAIL (13 "not in units.csv", 54 shape-note); after 71. The 4 extra are other lanes' rows (s02-X16b x3, s05-X43a, s05-X38/X41, materials rows for days 3, 27, 36, 41; counts shift as lanes work). None in lane 4. I fixed one I caused: s07-X59a stem was unquoted with a comma (shifted columns).
- lesson.py filtered (run once, at end): 66 FAIL, 9 in lane 4 days (word caps on d056, d057, d060, d063, d065, d066, d068; d060 check_min; d068 copied-exit). All 9 fixed after the run and confirmed with check_day on each lane day (0 FAIL); also fixed a d056 kindergarten-review ledger line and the d067 "day 67's assessment" hand-back line. Lane before snapshot (lesson-before.txt) had 0 FAIL in lane days.

## For the lead: sweep

- Unit and section plan stage: exits planned with no slack (d058, d063 exit timing); stale section plan exit bullets after item changes.
- Section plan stage: practice and exit sharing a case or shape (alligator across 56 to 61; sunflower and bean template).
- Day stage: At home exits that name per-class cards.
- items.csv: s02-X16b row has unquoted commas (shifted columns), and a blank line sits after s04-P32-3; not lane 4.
- materials.csv: no rows for the day 66 pieces (clear folder piece, coffee filter, egg-carton piece). A67a still asks two things in one stem.
- DEFAULTS.md: no change needed.

## Ledger entries for the lead

- science-grade-1 day 58: words-versus-picture ("what the words tell, what a picture shows") first taught here; add the term (a:43).

## Browser check

None.
