# Run-end fixes, social-studies-kindergarten, 2026-11-21

Source: S:/CurioClass/_scratch/gemini/out2/cold-keys-ss-k-3.md (cold answer check, kindergarten section). Every finding was checked against items.csv, wrongs.csv, handbacks.csv and the day and card files. New item ids carry a letter suffix; each has a key, steps, samples, wrongs and a print line.

## Findings

- cold-keys, 8 child card or sheet files with "Key (teacher)": applied. Eight key pieces made (key-exits-1-2, key-exits-3-5, key-exits-6-10, key-sheet-dated-picture-log, key-sheet-hook-washing, key-sheet-room9-strip, key-sheet-drawings-and-stand-in, key-sheet-then-now-chart); the key sections removed from the child pieces; each key named in Before class of the days that use it (d001-d008, d010, d034 to d038; not d053, which only reviews the washing chart). A day 1 line was added to the first key.
- s01-X1: applied. Circle (paper) kept in s01-X1; the reason moved to new s01-X1b (spoken). Error A and the day 2 hand-back now point at s01-X1b.
- s01-X5: applied. s01-X5 is the circle (key names the take-turns picture); s01-X5b why not fair (B, E); s01-X5c what to do instead (J).
- s01-X8: partly. s01-X8 circle; s01-X8b the reason (the partner's "Why do you think that?" stays a prompt inside it, error L); s01-X8c the partner's own question (error F). The partner follow-up was not split from the reason because it only prompts a second because.
- s01-E3: applied. s01-E3 why each rule is needed; new s01-E3b what could happen without it.
- s02-X12: applied. s02-X12 token on the picture (key names which); s02-X12b the partner action (H, A).
- s02-X16 (four asks): applied. s02-X16 in charge; s02-X16b who kept the promise; s02-X16c agreeing picture; s02-X16d following picture. Stems carry no page digits so the c and d stems differ.
- s02-X16 (stem and key mismatch): applied. The "two-scene story" wording is gone and Jun is named; pictures-class-book.md already matches (Jun on pages 1 and 2, agreeing on page 4, following on page 5).
- s02-E1b: applied. s02-E1b what finishes the job; new s02-E1c what a polite helper says (error H).
- s02-E4: partly. Each trait is already its own response row with its own token, so it was not split into five items. The stem now says one row at a time, "Show what each did" is gone, and the key lists the pictured action per character (Mo, Rae or Bo, Jo, Lena) and uses "puts an unfair thing right" instead of "Just".
- s03-X21: applied. s03-X21 circle the slide; new s03-X21b where the gate is (K, A).
- s03-X25: applied. s03-X25 circle the block; s03-X25b how you know (C, D, G); s03-X25c finger on the wrong row (L); s03-X25d say what is wrong. Card 1 and card 2 now have their own items.
- s03-X28: applied. s03-X28 town dot (F); s03-X28b school on the street map; s03-X28c street name (E).
- s03-E2 (five asks): applied. s03-E2 land and water on both; E2b a likeness; E2c a difference; E2d middle of each map (with help); E2e why each map has a different middle.
- s03-E2 (key "maker chose each middle" did not answer "what does each help us see together"): applied. The unanswerable ask is replaced by s03-E2e "Why does each map have a different middle?", which the key answers (error B).
- s03-E4: applied. s03-E4 show the real feature (D); new s03-E4c how the drawing matches the model and place (C). Hand-backs name s03-E4c.
- s04-X40d: applied. s04-X40d point to a clue; new s04-X40e what the photograph helps us learn (F).
- s04-E2 (three marks): applied. s04-E2 today; new s04-E2c last week (B); new s04-E2d next month (H). Hand-back row names all four items of the day.
- s04-E2 (giveaway labels): applied. The teacher now reads only the event names, never "yesterday", "today", "last week", "next month"; the child finds each by the strip.
- s04-E3c: applied. Stem now asks about other people or other times; the key accepts any accurate limit and still wants another source or the one place and time.
- s05-X42a: applied. The harvest card is replaced by children in costumes at a front door at night; "(a veteran)" is gone from the stem and the card file.
- s05-X43a: applied. Distractors are now one grown-up putting up a rule sign alone and children following a posted rule; wrongs and the card file match.
- s05-X46c: applied. The ask is now "What is one question about this bird that our book page could answer? Point to the page."
- s05-E5: applied. s05-E5 point to the bird; new s05-E5b why the bird stands for the United States (D).
- s06-E20: applied. s06-E20 which card; new s06-E20b what it shows. Assessment pages and key line updated.
- s06-X61c: applied. Pair is now a rain jacket and a sparkly rain sticker; the stem asks which one a person needs (error C).
- s06-X61k: applied. s06-X61k asks politely; new s06-X61m accepts the no (K). Cards file updated.
- sc1-E2 (two asks): applied. sc1-E2 token on the unsafe spot; new sc1-E2b why the pool has the rule.
- sc1-E2 (walking feet vs puddle): applied. The ask is now "the unsafe spot the rule is about", which only the puddle fits.
- sc1-E6: applied. sc1-E6 map or globe; new sc1-E6b why (G, B).
- sc1-X33b: applied. sc1-X33b next to the door (F moved to new sc1-X33g far from the door).
- sc2-E14: applied. sc2-E14 point to the pick (limit heard); new sc2-E14b why (B).

## Totals

32 findings: 30 applied, 2 partly (s01-X8, s02-E4), 0 rejected. Items 240 to 272, wrong answers 394 to 417.

## Gates (course only)

- plan.py check: 19 failures before, 19 after (all "not in data/units.csv", known template points).
- lesson.py check: 2 FAILs before (d031, d032 ledger review wording), 2 after (same two, not mine).

## Judgement calls for the lead

- Item path. Mark items on end-of-unit response rows, and exit marks done by pointing, token or finger, stay path "spoken" (the course's existing convention). Paper (blank path) exit items go on a printed slip, and a day with several of them overflows it. Blank path was kept for the pure paper circles s01-X1, s01-X5, s01-X8, s03-X21 and s03-X25 (already passing the slip gate).
- Teacher page word caps forced small trims in d002, d003, d007, d008, d016, d025, d028, d034, d037, d060 (wording only).
- Not in my findings: u02-3/pictures-class-book.md and u06-3/pages-day60-assessment.md also hold a "Key (teacher)" block in a printable piece; left for the lead to decide.
- docs/courses/social-studies-kindergarten/day-skeletons were not regenerated (plan.py tables changed 0 files).

## Follow-up (coordinator request)

Two more keys moved out of printable pieces: key-class-book.md (u02-3, named in d016 Before class) and key-day60-assessment.md (u06-3, named in d060 Before class). The course lists no key pieces in leans_on, so none added. d060 trimmed three words to stay in its cap. Gates unchanged: plan 19 failures, lesson 2 FAILs (d031, d032).
