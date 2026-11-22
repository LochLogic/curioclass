# Answer-key read: english-language-arts-kindergarten, unit 3, days 80 to 118

Kind: answer-key (docs/pipeline/briefs/sensitivity-read.md, sections 1 to 3). Reader: a fresh agent that did not write the data.

## What I studied

Nothing outside; for an answer-key read the study step is to solve. I solved every item cold from its stem and the card or text it names (items.csv columns item_id, day, check, code, stem only; the answer, steps and samples columns stayed unprinted until my answers were written to a scratch file). Then I opened the key, the wrongs, the unit pieces (courses/english-language-arts-kindergarten/u03-*/, texts gk-u3-01-b, 05-a, 06, 07, tw, sc), days.csv goals and the section plans u03-1 and u03-9 for the exit lines.

## Verdict

Pass with fixes. Of 140 items, 129 solved to the key on the first pass; 11 items had faults (plus 1 rule-4 fault in a shared piece), all fixed in items.csv, wrongs.csv and the pieces that print them. All changed items were solved cold again after the fix and agree with the new key.

Items read: 140 (62 exit items and 78 end items: check, readiness and end-of-unit, on days 80 to 118).

## Faults and fixes

| Item | Kind | What was wrong | Fix |
|---|---|---|---|
| s03-X103a | ambiguous | Stem asked for "the note for this tree, what it needs and who uses it". The no-arrow drawing also shows the need and the user, so two drawings fit; only the key's step (arrow) decided it. | Stem now "Which drawing joins what this tree needs and who uses it?" (same ask as X117a). Piece cards-exits-102-106.md updated. |
| s03-X108b | needs-info | "Where does it go on the collage?" cannot be answered from the card or the stem; the collage layout is not given, so the key (beside the berries, with an arrow) depended on a picture the child has not seen. | Stem "Which line on the card did that strip come from?"; key "Waxwings eat the berries." Wrong row now "points to the sentence about green, sharp leaves" (E). Piece cards-exits-108.md updated. |
| s03-X111a | needs-info | Picture named "seed balls"; the card says only "seeds". Not a given fact. | Picture now "a goldfinch eating seeds on a sweetgum branch" in stem, key and piece. |
| s03-X115b | ambiguous | "Which words say how they go together?" on a card with no joining word (the card says only "Koalas eat the leaves."); "so it gives them food" comes from spoken explanation (a), not the card. Two defensible answers. | Stem names explanation (a): "Which words in explanation (a) say how the tree and the koalas go together?" Piece updated. |
| s03-X117b | ambiguous | "How do they go together?": "they" has no referent (water, tree, agouti). | Stem "What does the tree need, and who uses the tree?"; key and sample rewritten to match. Piece updated (stem and key). |
| s03-T1a | key | Sample answer "no, the buds come later". Text 07 page 5 says the buds are already on the twigs, waiting; they open later. | Key now "no, the buds are waiting". |
| s03-T2b | key | Answer and sample said "a nest rests in a fork"; text 06 says nothing of a fork (that is text 05a), and its topic is animals that depend on trees. | Key and sample from text 06: animals depend on trees; the squirrel eats nuts and seeds; the branches hold the bird's nest up. |
| s03-T2d | ambiguous | "It is held by the branches": "it" could be the nest or the egg; "What does it mean?" had no clear target; the key's clarifying question was not what the stem asked. | Stem names the nest ("The nest is held by the branches"), invites a question about an unclear word, asks "What does held mean?" then "What is held, and what holds it?". Key, steps, samples and the Y wrong row updated. |
| s03-R116c | key | Sample "The squirrel needs the oak because it eats the acorns" names no tree need, which the key requires. | Sample "The oak needs water, and the squirrel depends on the oak because it eats the acorns." |
| s03-P4a | rule4 | "Which word rhymes with cat: hat or sun?" is the taught rhyme set of picture-sort-cards (cat, hat, mat, bat; sun, run, bun) and the section plan's error AD example. | Fresh case: pig, wig or fox; another rhyme such as big. Wrong row updated. |
| s03-P4c | rule4 | Split "sun": the picture sort teaches sun, run, bun by keeping the end and changing the start. | Fresh word fan: /f/ /an/. Wrong row updated. |
| u03-3 opener (shared piece) | rule4 | Opener teaches "A palm and its shade" as the topic-with-detail example; the ledger lists palm shade as an exit-card-only case (E89). | Opener now says "A named tree and one fact about it". |

## Checks that passed

- Every other exit item (X80 to X118) solved to the key; each picture set has exactly one fit, the wrong choices are named by the wrongs rows, and no stem or caption gives the answer away. X84 (first and later) matches day 84's goal of what changes over time; X100a and X114a, each with one match and two foils, are fair.
- Each end item matches the standard in its code (RF.K.1a to 1c, 2a to 2e, 3a, 3c, 3d, 4; L.K.1a, 2c, 2d; SL.K.1 to 6; W.K.2, 7, 8; RI.K.1 to 3, 7, 10; RL.K.1, 10).
- F1 (pen/pin, bed, sun, the Ben passage): the answer is in the card ("The pot has mud"), and the words are kept out of the unit's decodable texts (gk-u3-sc). The spoken-only picture sort also holds pen and sun; this is a sound sort, not print, so I left it and note it below.
- Ledger check (`ledger.py show ela --before english-language-arts-kindergarten`, filtered): no X item case appears in a lower grade (the course is the lowest). Within the unit, none of the pine, fish, cactus, whale, Omar, frog, camel, bee, owl, rabbit, birch, caterpillar, cedar, sloth, chickadee, moose, giraffe, mulberry, magnolia, willow, baobab, holly, sweetgum, beech, aspen, ash, eucalyptus, persimmon, Brazil nut or mangrove cases is in a shared piece or text. C1 (sapling and stake) is shown only in check-cards.md and used on its check days.

## Section plan exit lines that no longer match items.csv

The section plans (docs/courses/english-language-arts-kindergarten/u03-N.md) were not in my edit scope. These E lines now differ from items.csv and the card pieces and need the same edits (the lead should apply them):

- u03-6 E103: Mark question now "Which drawing joins what this tree needs and who uses it?"
- u03-7 E108: Spoken question now "Which line on the card did that strip come from?"; key `"Waxwings eat the berries."`; wrong "points to the sentence about green, sharp leaves (E)".
- u03-8 E111: picture is "a goldfinch eating seeds on a sweetgum branch" (was seed balls).
- u03-9 E115: Heard question now "Which words in explanation (a) say how the tree and the koalas go together?"
- u03-9 E117: Heard question now "What does the tree need, and who uses the tree?"; Meets now "The tree needs water, which it takes in through its roots; the agouti uses the tree, opening its pods for the seeds."
- u03-1 error AD example ("Picks hat as cat's rhyme") and the P4 item entries in u03 section plans that name cat/hat or "split sun" still use the old words.
- docs/courses/english-language-arts-kindergarten/s03.md section U3 (Exit questions table): every row's fresh text and exit question is an older design (pear tree, beaver bark, maple squirrel, woodpecker, and so on) and no longer matches items.csv for any day from 80 to 118. Day 117 there says no individual prompt, while items.csv has X117a and X117b.

## My own errors

- None that changed the outcome. I first read the C1 card ("How does the stake help the sapling?") as needing a fact not given; the picture set and the word "ties" support the inference at this level, so I left it (see below).

## Could not settle

- C1a and C1c: the card never says the stake holds the sapling up; the key takes it as a plain inference ("the stake keeps the wind from bending it"). A child who says "it holds it up" without naming wind would meet only one of the two steps. If Cory wants a stricter card, add "The stake holds it up." to the card, the three stems and check-cards.md.
- Rule-4 near misses left alone: F110a and F110b use pen and sun, and P4e uses sat and mat, which also appear as spoken picture-sort or tile-chain words in the unit. Those are different skills (print and spelling, not sound sort), so I did not change them.
- The reader "Mud in a Tub" (days 95 to 101) shares the word mud with the F1 passage; the readers are not in this course folder and I did not open them.
