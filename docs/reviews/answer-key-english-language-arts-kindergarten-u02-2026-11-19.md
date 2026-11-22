# Answer-key read: english-language-arts-kindergarten, unit 2, days 35 to 76 (2026-11-19)

Reader: a fresh agent that did not write the data. Study step: solve first. Every item's stem and its card or text was solved cold (answers written to a scratch file) before the answer, samples or look-for columns were opened.

## What I studied

- data/plans/english-language-arts-kindergarten/items.csv, stems only: what each item asks, nothing else.
- courses/english-language-arts-kindergarten/u02-*/cards-exits-*.md, the picture and card text for the item (key sections skipped until after solving).
- courses/english-language-arts-kindergarten/texts/gk-u2-01, gk-u2-02, gk-u2-03 and gk-u2-weather-words (verse 8 and the verse hooks): what the shared texts already show.
- Shared pieces of u02-1 to u02-10 (scene cards, story-map, priya map cards, feeling chart, strips, posters, openers): the cases and pictures rule 4 compares against.
- scripts/ledger.py for ela before this course: the ela ledger is empty, so there is no lower-grade case to collide with.

## Verdict

Pass with fixes. The keys were right (no wrong key found; my cold answers matched on every item), but about 20 items or their shared pieces had faults: answers readable from the card, pictures that could not tell right from wrong, cases that the shared texts or teacher notes already show, and two-picture guesses.

## Items read

114 items (days 35 to 76: 62 exits, 52 readiness and end items) and their 168 wrong-answer rows.

## Faults and fixes

| Item | Kind | What was wrong | Fix |
|---|---|---|---|
| s02-X41a, X41b | ambiguous (answer given away) | Card said "This page tells about ice." so "What is the page about?" was read off the card. | Sentence removed from the card (items.csv and cards-exits-39-42). The ring of three pictures stays. |
| s02-X35a | needs-info | "Point to the wind card" but the ring held a pinwheel, a puddle and a snowman: no wind picture to point to. | Ring now shows wind lines alone, a puddle and a snowman; answer says "wind picture". |
| s02-X35a, X35b | rule4 | Wind lifting a kite is the unit's own case (gk-u2-01 playground picture, verse 4 kite and "wind pushes things"). | Kite replaced by a feather in card, key, samples and wrongs. |
| s02-X52a | rule4 | "Wind moves the flag" is gk-u2-01 (flag stands out in the wind) and the verse "tugs a flag". | Card now "Wind bends the reeds by the shed."; key and samples updated. |
| s02-X53b | ambiguous | Pictures "a gift wrapped" and "a gift wrapped again" cannot be told apart; the listed wrong ("unwrapped") did not match its note (base word heard would be the first picture). | Pictures: first wrapping; unwrapped with paper beside it; wrapped a second time (two panels). Wrong rows: first wrapping (re- ignored) and unwrapped (opposite). |
| s02-X58b | ambiguous | "A coat hung up again" is the same picture as "a coat hung up"; a child who ignores re- could not be caught. | Pictures: hung the first time; fell and hung a second time (two panels); taken down. Wrongs updated. |
| s02-X55a | ambiguous (guess) | Two pictures, 50 percent by guessing. | Third picture added (a boat on a lake) and a wrong row for it. |
| s02-X60a, X60b | ambiguous (guess) | Two pictures each, 50 percent by guessing. | Third picture added to each (a barn; the dog alone); wrongs widened. |
| s02-X65 | ambiguous | Plan card "the tree" could go in the where box (they step under a tree). | Card replaced by a bicycle (object, not on the card); key and wrongs updated. |
| s02-X68a | ambiguous | "Story boxes" could mean the setting box; the pier alone is a place and had no wrong row. | Asked as "Which three pictures show things that happen in the story?"; wrong row added for the pier alone. |
| s02-H1d, H1e, H1f | rule4 | Used the verse 8 hooks themselves (coat/throat, hop/top, sweater, h + op, top), so a child could answer from memory of the verse. | New cases that no text shows: pan/fan and a rhyme for pan; clap rabbit; n + ut then mud in two parts. needs_text now no (text_id cleared). Keys, samples and wrongs updated. |
| s02-H1g | ambiguous | "The line of the verse that holds them": on and to are in two different lines. | Stem says the lines, and names which line holds each word. |
| s02-P1b1, P1b2 | rule4 | sun is a taught three-sound word in verses 1, 7 and 9. | Word changed to pig (p, short i, g); keys, samples updated. |
| s02-S1a | key | Key accepted Baba as a possible carrier; the text only has Yusuf carrying the parcel home. | Key says Yusuf; naming Baba as walking with him is fine; look-for tightened. |
| s02-X48 (opener 2.4) | rule4 | u02-4/opener teaches "Fog sat on the harbour." with the exact "boats alone" miss: the day 48 card and key. | Opener example changed to "Snow lay on the steps." Item unchanged. |
| s02-X66a (opener 2.8) | rule4 | u02-8/opener teaches "the green scarf, not just a girl": Zia's detail. | Opener example now "the red boots". Item unchanged. |
| s02-X69b, X72b (poster, opener 2.8) | rule4 | Writing-process poster key printed "Who does Ona wave to?" (the exit's key) and "What is for lunch?" (the exits' wrong); opener repeated lunch. | Poster key now uses a different draft (Pip climbed) and "What is for dinner?"; opener says dinner. Items unchanged. |
| s02-X58b (word-part-cards) | rule4 | Key line named the exit's miss ("rehangs is a different coat"). | Line reworded without the exit case. |

Not changed, with reasons:

- s02-X55a, X69a, X70a, X71a, X72a (W.K.2 or W.K.3 tested by picking a picture). They are receptive stand-ins for composing; the codes are the plan's only fit for those days and plan.py ties the code to the day. Kept, but the dictated or drawn follow-up (X70b, X73b, X72b) carries the writing evidence.
- X54 and X59 each have two cards that look the same (the umbrella and the umbrella alone; the rug and the rug alone). Not wrong (neither is right in any box), only redundant. Left.
- H1h letters (v s g i d f l k y q u x): not checked against the cycle table in this job.

## Field 3 lines in the section plans that no longer match items.csv

items.csv is the truth. docs/courses/english-language-arts-kindergarten/:

- u02-6.md: E54 kitchen (data: market). E55 pond (lake), "wind pond" (wind lake); now three pictures. E56 "Now i hop" (Soon i run / Soon I run). E57 bowl x3 (jar). E58 hail card "It bounces on the path" (falls when it gets too heavy), "Jo rehangs" (Pia rehangs), pictures now first hanging, hung a second time, taken down.
- u02-7.md: E59 sunrise, bright cloth, goat (dusk, blue rug, hen; cards cloth to rug). E60 kitchen, berries, bowl, cat (shed, cups, crate, dog; now three pictures each).
- u02-8.md: E65 the tree as who (now a bicycle as who, after this read). E66 Noor, green hat, paper bird, kite (Zia, green scarf, paper boat, bus). E67 a kitchen (a bus shelter). E68 boy, kite, hill, he carries it home (girl, paper plane, pier, she picks it up; asks "things that happen"; pier alone added). E69 Jo (Ona).
- u02-9.md: E70 Avi, Dad, garden gate, pond (Rafa, Mum, barn door, beach). E71 Avi, hat, bag; item b "a hat, a bag" (Rafa, lunch; "a map, a pen"). E72 Avi, gate alone (Rafa, door alone). E73 draft "Rain started. I waited." (Snow fell. I stayed.), picture of a child waiting inside (a child in the hall).
- E35 to E53 were not read for this note.

## Gate

`plan.py check` for english-language-arts-kindergarten: same FAIL lines as before my edits except one number: "items.csv: N percent of questions need the text; at least 80 percent must" moved from 18 to 16, because H1d, H1e and H1f no longer need the verse text. That FAIL was already failing. To keep it at 18, those three items can go back to verse words, which re-opens the rule 4 fault above; the lead decides.

## My own errors

None that changed an item. Two early doubts were mine and were cleared: I first read X47 as giving away its answer in the stem ("who held the door?"), but the key accepts any detail from the card and the second partner question carries the skill; and I first read S1b as having two right places, but the key accepts the street, the bakery or both, which matches sections 2 and 3.

## Could not settle

- Whether the plan's field 3 lines should be regenerated from items.csv now (lead's call; I did not touch docs/courses).
- Two-panel pictures for X53b and X58b need drawing when the cards are made.
