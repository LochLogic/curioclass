# Finish fix: science grade 1 (2026-11-22)

One fix pass over the twelve fresh-reader reports. Each report now ends with "Fixes applied (2026-11-22)", one line per finding.

## Counts per report

| Report | Applied | Rejected | Left |
|---|---|---|---|
| answer-key checks | 8 | 0 | 0 (confetti note: no change, as advised) |
| answer-key u01 | 4 | 0 | 0 |
| answer-key u02 | 4 | 0 | 0 (one no change, as advised; photographs wait for the media stage) |
| answer-key u03 | 4 | 0 | 0 |
| answer-key u04 | 7 | 0 | 0 |
| answer-key u05 | 6 | 0 | 0 |
| answer-key u06 | 3 | 0 | 0 |
| answer-key u07 | 6 | 0 | 0 |
| answer-key u08 | 3 | 0 | 0 (one no change, as advised) |
| safety | 14 | 0 | 2 (class size, for Cory; acknowledgment form, the school's own) |
| sensitivity | 5 | 0 | 1 (which family-engagement body to cite; nothing taught rests on it) |
| cold read | 6 | 0 | 8 (listed below) |

Items: 240 to 244 (new s07-E60d, s07-E60e, s05-E46c, s05-E46d, each with key, wrongs rows and a handbacks row). Wrongs rows: 369 to 376. US spelling: 40 replacements across six course files and section plans s02, s03, s05, s07.

## Safety page

courses/science-grade-1/safety.md, 891 words in the body, modeled on the grade 2 page: the stop rule, eye protection (impact-rated, Z87, everyone in the room), hand washing, allergies (dust, plants, latex, foods, egg cartons), plants, soil and mold, outdoor looks and adult ratios, heat and lamps (no button cells), electricity, small parts and string (cup-at-the-ear rule), glass and sharp edges, clean-up; each rule names its days. DEFAULTS.md has a "Safety page." line. Sources rows 14A to 14E (eye protection, hand washing, latex, eclipse and sun viewing, button batteries), each opened and marked checked: 2026-11-22.

## Gate counts

- plan.py check, filtered: before 240 items, 369 wrongs, 13 FAIL; after 244 items, 376 wrongs, 13 FAIL. All 13 are the known "section N.N is not in data/units.csv" lines.
- lesson.py check, filtered: before 0 FAIL; after 0 FAIL (d060 and u07-1/family.md re-checked after the last trim).

## For Cory

1. Plant parent-young records (scope; units 2, 3 and 7). Options: (a) real, verified class records (a grown plant and its young, dated) across units 2, 3 and 7, with the scope and unit plans changed to grow or collect them; (b) keep the labeled invented masters, now all printed "invented for practice", cut day 12's pressing claim to what the masters show, and align the scope wording. My pick: (b) now, (a) when the media stage makes real records.
2. Class size: the course plans for 30 children; NSTA advises no more than 24 per teacher in hands-on science. Options: (a) state a 24-child assumption for the hands-on days; (b) require a helper adult on the hands-on days (18 to 21, 28, 29, 31, 33, 49, 51, 52, 54), as the safety page now asks; (c) keep 30 and the group plans as they are. My pick: (b), already on the safety page, with (a) noted for schools without a helper.

## For the lead: sweep

- Unit plan exit tables in s02, s04 and u04-2 that do not match the day items (unit plan stage).
- Days 10 and 13 tell before the evidence; moving the read-alouds reorders parts across days 10, 11 and 13 (section plan 2.1).
- s02-E11a, E11b, E12a need re-posing as evidence with new held-back pictures (section plan 2.1).
- Unit 7 media: fawn photograph rights and a credited duck photograph (unit plan, data).
- Running s04 item 2 live for every group (unit plan s04).
- s07.md says item 1 earns eight points; the points now split over E60a, E60d and E60e (unit plan s07). Likewise s05.md for E46b, E46c, E46d.
- revise-model scoring on day 47 vs day 46 (unit plan s05).
- UK spellings left in scope-and-sequence.md, frame.md and the unit and section skeletons (scope, unit plan).
- units.csv rows for this grade's sections (data, repository-wide).
- d060 NOTE: the section plan's day 60 block names 40, which the day never uses (section plan 7.1).
- Ledger: no ledger entries changed by this pass. Suggested notes for the lead: none required; if the ledger lists 1-PS4-3 error D for grade 1, it now reads "the mirror is sorted out of the no-light group, as if light went through it".

## Left

- APPROACH-SCIENCE.md, a course family note and a supplies list: rubric known gaps, not this pass.
- Growing a real class shoot for days 11 and 12: section plan change; strips-shoots.md already prefers the class's own photographs.
- Real photographs and recordings for day 20, day 33, the unit 4 exits and day 46: media stage; each card now states what the finished record must show, with a paper fallback.
- Helper adult lines on the day pages: those pages are at their prose caps; the safety page carries the rule and its days.

## Browser check

None from this pass's sources. The sensitivity report's study pages refused automated reads (fosterclub.com real stories, naeyc.org family engagement, headstart.gov family engagement), and the CPSC button battery page returned 403; no fact in the course rests on any of them.
