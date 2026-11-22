# Answer-key read: science-grade-1, unit 6 (2026-11-22)

Kind: answer-key. Target: science-grade-1-u06, the check, mid and end items of unit 6. Course finish (COURSE-RUN stage 7). Read-only: this report is the only file written.

## What I studied

- No outside study for this kind: the study step is to solve. Both items were solved cold from the stem and steps before the answer, samples and wrongs.csv rows were opened.
- data/plans/science-grade-1/items.csv, unit 6 filtered: 18 rows, 16 exit, 2 end (s06-E54a, s06-E54b). No check or mid items in this unit.
- data/plans/science-grade-1/wrongs.csv rows for s06-E54a (2) and s06-E54b (6).
- courses/science-grade-1/u06-2/d054.md (the check day), d053.md (where the E54a product is made), sheet-revised-sketch.md, sheet-trial-record.md, cards-display-helper.md, cue-cards.md, key-cards-exits-52-55.md; message and marking cards in u06-1 (cards-messages.md, cards-trials.md) for the pictures receivers mark.
- docs/courses/science-grade-1/s06.md: standard 1-PS4-4, error register A to F, goal map and day list (day 53 design and build, day 54 check).

## Verdict

Pass with fixes. Both keys match my cold answers and both items test 1-PS4-4 as the day 54 goal states, but the day 54 materials give receivers no "ready" picture to mark, so the keyed message cannot be marked as written; two smaller wording fixes keep fair answers from being scored wrong.

## Items solved

| Item | My cold answer | Key | Result |
|---|---|---|---|
| s06-E54a | Dated sketch names the helper's problem (picture is ready, helper far across the room); a feature tied to a named earlier trial; one part really made on the device; a line on how that part helps the message reach the helper. A drawing alone does not count. | Same, a drawing without a built part is error B. | Match. |
| s06-E54b | Send three quick, same signal, at 3 strips then 6 strips, only the distance changing (string re-set gently straight); record the friend's actual mark at each; draw sender, device, receiver with an arrow; ring what the two marks show and claim nothing beyond those two marks. | Same, with errors A, C, D, E, F named. | Match. |

Mismatches: 0 key errors, 3 item or print problems (below), 0 my errors.

## Findings

1. **The receiver has no "ready" picture to mark (worst; item cannot run as keyed).** d054.md materials: "picture cards for marking (line up, wait), the sealed message card (three quick)". The message on day 54 is "picture is ready", three quick, and the E54a/E54b sample reads "The friend marked ready at both places." With only line up and wait, a receiver who understood the message has no right card, so step 3 and 4 ("records the receiver's actual mark") cannot be credited and every child would read as error A or a failed send. The marking pictures in u06-1/cards-messages.md also hold only line up and wait; cards-display-helper.md picture 3 ("three quick dashes... Big words: ready") is the sender's pattern card, not a receiver's marking picture.
   Fix: d054.md materials, change to "picture cards for marking (line up, wait, ready)", and add one marking picture to cards-display-helper.md: "**Picture 4.** The ready marking card: one framed picture on a display table with a small star beside it. Big word: ready. One per receiver, beside the line up and wait cards." The same three cards serve the At home version ("you mark a picture first").

2. **E54a step reads a partner as required.** Step 3: "the made device shows one added or changed part built from the provided materials, and a partner's making part is named". Day 53 says each child sketches and makes "alone or with a partner" (days.csv day 53 note), so a child who built alone would be scored incomplete on a fair answer.
   Fix: items.csv s06-E54a steps, step 3 to "the made device shows one added or changed part built from the provided materials, and a partner's making part, if there was a partner, is named".

3. **Trial record ring has no fair choice for a far-only success.** sheet-trial-record.md offers "near and farther | near only | not yet". A child whose near send was misread but whose farther send was marked right (it happens with a light aimed at the far card) has no matching ring, and E54b's judge step ("limited to the marks tried") would mark an honest "not yet" or a drawn note as wrong or unclear.
   Fix: items.csv s06-E54b answer, add after "limited to those two marks": "A child whose near mark missed and farther mark matched rings not yet and says the near send missed; that is a fair judgment and is credited." (Leaves the sheet as printed; a fourth ring "farther only" is the alternative if the lead prefers a print change.)

## Checked and fine

- Stems and pieces show what the keys need: E54a uses the revised sketch sheet's boxes (problem, the trial that told me, the part I added, I added ___ because ___, my partner made); E54b uses the trial record's near and farther rows, friend marked column, "how my device carries the message" box and ring.
- Distances agree everywhere: near 3 strips, farther 6 strips (d053 agreement, d054 set-up, stem, home version).
- Error letters in the key and wrongs.csv match the s06 register (A noticing, B sketch for build, C near settles far, D two changes, E gap counted, F one success dependable). Error E can still arise because the child writes the strip count in the record's strips column.
- Both items name 1-PS4-4 and test the day 54 goal (own device, near and farther trial, spoken or drawn account) and the day 53 goal (design from prior trials) that E54a scores. No device workings are asked, within the standard's limit.

## Gate

plan.py check, filtered for science-grade-1: 240 items and 369 wrong answers checked, 13 failures, all "section N.N (science-grade-1-uNN-N) is not in data/units.csv" for sections 1.1 to 8.1 (6.1 and 6.2 among them). None concerns an item or key; this read did not cause or fix them.

## Could not settle

Nothing.

## Fixes applied (2026-11-22)

1. Ready marking card: applied. d054 materials list line up, wait, ready; cards-display-helper.md adds Picture 4, the ready marking card.
2. Partner step: applied. "a partner's making part, if there was a partner, is named".
3. Far-only success: applied. The E54b answer credits ringing not yet and saying the near send missed.
