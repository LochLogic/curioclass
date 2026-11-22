# Ladder sample, science-kindergarten, set b (re-sample, 2026-11-22)

Read-only grade-close sample of the Curio Class course science-kindergarten, set b. Each day was read cold with the day before it, its section plan block, DEFAULTS.md, its days.csv, items.csv and wrongs.csv rows, the unit's errors.csv rows and every shared piece in `leans_on`. Exit and end keys were reworked by hand.

Checked against a source: nothing needed one. None of the five days states a fact about a real place, person, event, species or number (the Denver records sit in other days). Judged only: every science claim (surface warmth is not air warmth, farther stop is not faster start, animals eat and a plant is not fed a meal, litter moves, roots and dens change a place) was judged against the unit plan's stated limits, not against a page.

Gates, run filtered as told: lesson.py reports 0 failures for all five day files. plan.py's whole filtered output has 43 FAIL lines: 13 "section is not in data/units.csv" (course-wide, none about these days), 1 one-ask on s02-X14a (not my day), and 29 "shape-note" lines. Four of those name my days (u02-1 day 12, u04-1 day 35, u04-3 day 43, u06-1 day 57) and are real, not template: the section plan block has no "Shared shape" note. Day 22 has its note. One lesson.py NOTE on d043 is a template point (below).

## Days read

| Day | File | Kind | Verdict |
|---|---|---|---|
| 12 | courses/science-kindergarten/u02-1/d012.md | Fluency | Runs and the key is right; the afternoon marks it reads depend on an unscheduled afternoon look in day 11's "Other rooms", and the exit re-asks day 11's exit rather than testing the day's claim. |
| 22 | courses/science-kindergarten/u03-1/d022.md | Application | Content and keys are right; the 11-minute build-and-test cannot finish the third group, and the exit's first stem hands over its own answer. |
| 35 | courses/science-kindergarten/u04-1/d035.md | Fluency | Teachable and correct; one false line about the invented set, a card key that disagrees with its card sheet, and an exit that is practice-shaped. |
| 43 | courses/science-kindergarten/u04-3/d043.md | Respond, assessment | The assessment sittings are sound and keys are right; the caption-reading part contradicts itself and the group turns have no slack. |
| 57 | courses/science-kindergarten/u06-1/d057.md | Application | Weakest of the set: the exit reuses day 56's case and the day's own repair picture, the key phrase "If we ___, then ___" is called review but was never taught, and the exit does not fit its 3 minutes. |

## Findings, most serious first

| Day | Severity | Kind | What is wrong | The exact fix | Stage | Script gate catch? |
|---|---|---|---|---|---|---|
| 57 | FIRM | rule4 | Exit X57a/X57b show a bench with loose wrappers, a used sheet, an empty bottle and wind lines toward shrubs. That is day 56's chain 3 (wrapper carried by wind), day 57's own repair picture (wrapper pushed under shrubs, error C), and day 57's own samples (bottle, sheet). The "Draw it" part (8 min, no item) asks the same thing as X57a: draw the action and its effect. | New exit case with none of these: for example a school hallway with muddy boot prints and a coat hook, "draw what our trial would do here", or a classroom paper bin and a tray of single-use cups. Keep the "If we, then" frame. Move the shrub error out of the exit key. Add a "Shared shape" note and make "Draw it" a different shape (point to and say, not draw). | day (exit), section plan (no practice items) | yes for the missing shape note; no for the reused case |
| 57 | FIRM | ladder | Warm-up "Say it back" and the plan call "If we ___, then ___" a review of the arrow, and materials cite "day 56's drawing and sentence". Day 56 has no such sentence or frame (its frame is "The ___ can hurt the ___"); the ledger lists the frame as first used on day 57. The Application day teaches it as new and X57b asks for it. | Teach the frame on day 56 in the "Start the trial" part (one line, with the arrow), or on day 57 as a named new model in 3 minutes. Delete "review" and "day 56's sentence" until it is true. | section plan / unit plan | no |
| 22 | FIRM | timing | "Build and test", 11 min, two halves of 5 minutes. Three groups test at once; the teacher checks each build serially at about 1 minute (rule in the day), and each child rolls once at about 40 seconds, 5 x 40 = 200 seconds. Group 1 is checked at 0 to 60 s and finishes at 260 s; group 2 starts at 120 s and finishes at 320 s; group 3 starts at 180 s and finishes at 380 s, past the 300-second half. The build itself and the square moves are not counted. The teacher also hears the six in the same minutes. | Three rolls each ("Shorter" already allows it), or two builds checked before the part starts (in "Before class"), and 12 minutes for the part by taking 1 from the 4-minute two-pushes rug, or four groups testing at a time with a second adult. | section plan | no |
| 57 | FIRM | timing | Exit, 3 min: X57a all draw a changed bench scene (a before and after in a box, about 90 s for a five-year-old), then X57b hear six at 20 seconds each is 120 s, plus two spoken asks. At least 3.5 to 4 minutes. | One drawing, not two ("draw the action" only); hear three, not six, or give the exit 5 minutes by taking 2 from the 8-minute "Draw it". | section plan | no |
| 43 | FIRM | other | "Read the captions" (3 min) gathers four groups by "the strip on their mat" and reads needs, links, claims and impacts, then the same part says the claims and impacts strips "are written on the mats after class and read at the next meeting". Strips G to J do not exist on any mat today. The caption-strips piece and the plan repeat the contradiction. | Day 43 reads only A to F in two groups (needs, links), 40 s each, and says the other strips come at the next meeting; day 44's hand-off names the G to J reading. | section plan | no |
| 12 | SOFT | handoff | Practice (4 min) reads "day 11's afternoon dots beside its morning dots on three sheets", but day 11 puts the afternoon look only in "Other rooms" (afternoon recess, no minutes in its 30). A class that does not do it has no sheets and day 12 names no fallback for this part. | In d012 practice add: "No afternoon sheets: read three chart rows with the same pointing." Move the afternoon look from "Other rooms" to day 11's "Tomorrow" as a named set-up. | day (d011 and d012), section plan | no |
| 12 | SOFT | timing | No minutes to take 30 children out and in. "Teacher check" (3 min) starts "Go out in sight"; the walk back, before 4 minutes of compare "on the rug", has none (day 11 gives 3 minutes to line up). | Warm-up 5 to 4, practice 4 to 3, teacher check 3 to 5 (line up and go out); fold the walk in into "Compare". | section plan | no |
| 12 | SOFT | exit-goal | X12 reads rays and plain dots on a pretend table and picks the warmer time: the same ask and shape as day 11's X11b (two squares, which was warmer). It does not test the day's claim ("this bench, this afternoon", the bench is not the air). The "Shared shape" note is missing (gate FAIL). | Replace with one ask that tests the claim: Pip says "every bench is warmer in the afternoon", show one pretend table with a plain afternoon dot, "does this table say so? yes or no". Add the shape note. | section plan (exit), data | yes (shape note only) |
| 12, 43, 57 | SOFT | key-on-child-page | Exit card masters (cards-exits-10-12, cards-exits-40-43, cards-exits-55-58) print "Spoken" and "Key" lines in the same file the day sends to print for the class; the cards themselves are shown to children. No student page prints a key. | Split each exit master into a card sheet (pictures only, printed) and a teacher key block that is not on the print line. | kit (pieces) | yes (a "**Key:**" line inside a file on a day's print line) |
| 12 | SOFT | ladder | The ledger records "claim for this bench, this afternoon" as a review of unit 1.2 day 7, but d012 never says "review" or "claim" and never calls back to the box and block claim. | In the Compare part say "like the box and the block on our floor" before writing "this bench, this afternoon". | day | no |
| 22 | SOFT | exit-goal | X22a's stem says "Nobody watched how it left the line", then asks if it started faster, with "we cannot tell" as a card. The stem gives the reason for the key. | Drop the sentence "Nobody watched how it left the line" from the stem and show a picture with no start in it (the picture already has none); the child must see there is no start. | data (stem), kit (card) | no |
| 22 | SOFT | rule4 | Shape: P22-1 (draw a ball, move the square to reached or not reached) and X22c (draw a tick or a cross for reached or not) are the same two-way mark; X22b builds a ramp with cards, as the day's real build does. The plan's own "Shared shape" note lists this and calls it fine. | Make X22c ask for a different mark: "Point to the place the ball should be to say it worked." Keep X22b (new target, cards not wood). | section plan, data | no |
| 22 | SOFT | other | The exit needs 30 mats, each with a ramp card, two book cards and a ball card (22b). Materials and print list "exit cards" only per class. | Print line: "Per child: ramp mat and cards (cards-exits-20-24)". | kit, day | no |
| 22 | SOFT | other | The warm-up holds two repairs (retell keep, change, watch, then order book cards) against the plan's "one repair only", and the 4-minute rug holds four things (three cards, Pip's picture, an ask, 30 guess cards). Kind is Application, but the two-pushes rug teaches the day's new idea (error C). | Drop the keep, change, watch retell from the warm-up; mark the two-pushes part as the day's one new model in the ledger and the plan. | section plan | yes (warm-up repair count) |
| 35 | SOFT | words | "This is another observer's record, labeled by date" is said right after "this is the park pond, and it is invented for practice". The cards are our own drawings ("Curio Class drawing" on the back). One line says the cards are invented and the next that they are someone's record. | Delete the sentence unless the teacher has dated local pictures; then say "these are from a real place, with dates". | day | no |
| 35 | SOFT | key | P35-2 key puts a sun only on the sunny bank, while the card sheet puts P3 and P4 on the light row; P35-3 key puts the bite on the duck, but P2 is a duck dabbing at the water's surface (can be drinking). | Card sheet and key to agree (P3 sun, P4 "less light", say which); change P2 to a duck with a plant in its bill. | data (key), kit (card) | no |
| 35 | SOFT | rule4 | X35a (touch the picture that shows water) has the shape of P35-1 (draw a drop on pictures that show water) and X35b re-asks day 34's X34b (do they eat the same, yes or no, with a new animal pair). The exit asks nothing about light; the plan's goal names all three needs. Shape note missing (gate FAIL). | Replace X35a with a light ask on a new place ("which plant has what it needs, the one in the box or the one by the window"); add the shape note. | section plan (exit), data | yes (shape note only) |
| 43 | SOFT | timing | Each group turn: 3 minutes for 7 asks and 5 children, with the stems at about 62 seconds (the rate day 42 measured), 70 seconds of children's answers, about 20 of touches and a 30-second swap (day 42 counted it, day 43 does not): 182 seconds against 180, with no marking or "invented" line. | Four asks to the group and three to each child, or 3 minutes 20 seconds a group by taking 2 from the set-up and 1 from "Read the captions". | section plan | no |
| 43 | SOFT | timing | Twenty-five children have one 3-minute task (match three animals to food) for 18 minutes. No second task is named, as day 42 did ("a finished child draws a plant at its place"). | Name a second and third task: draw the plant and its line, then sort the water cards. | day | no |
| 43 | SOFT | handoff | "Day 41's items and day 42's assessment left captions D and E on the mats": the strips are per child, A to D on the needs mat and E and F on the model mat (day 42 says "errors E and F"). | "Left each child's own needs captions (A to D) and model captions (E and F)." | day | no |
| 43 | SOFT | words | "Shelter" is taught on unit 2.2 day 17 as the school building in thunder (a tree is not shelter); C2b's key and the day's words list reuse it for an animal's den. | Say "a safe place" (the key already allows it) and drop "shelter" from the words list. | day, data | no |
| 43 | SOFT | exit-goal | X43b stem "Same pictures. Say: I think, because I saw." names no thing to say about. X43a (touch what the tree changed) is the same shape as C1a (touch what the roots changed). | "Say what the tree changed: I think ___, because I saw ___." | data (stem) | no |
| 57 | SOFT | key | X57a's key is "the class's chosen action drawn on the bench scene", which a teacher cannot judge before day 56's vote; reuse, recycle and pick-up give three different right pictures and "fewer loose wrappers" fits only one. | Key per action: pick-up gives fewer wrappers, reuse a sheet turned over, recycle the bottle at the bin. | data | no |
| 43 | TEMPLATE | other | lesson.py NOTE: "the section plan's day 43 block names 30, which the day and its items never use". The 30 in the plan is the number of children ("Each of 30 children"), not a part length. | The gate should read "30" as minutes only inside a part line. | kit (gate) | yes (it is the gate) |

## Ladder

Kindergarten is the lowest grade, so the ledger's "before science-kindergarten" lookups return only this course's earlier units; the grade gap itself caused nothing here. The course used its own earlier units well in four of five days:

- Day 12 keeps "this bench, this afternoon" from unit 1.2 day 7 and keeps the unit's own limits (a bench is not the air).
- Day 22 reviews keep, change, watch (unit 1.1) in the same words and does not reteach them.
- Day 35 reuses the three rows of unit 4.1 day 34 and teaches nothing new, as its kind says.
- Day 43 reuses "I think, because I saw" (unit 4.2 days 38 and 39) and "less harm" (unit 4.3 day 40) as named reviews.

Two ladder faults: day 57 assumes a sentence frame ("If we ___, then ___") that no earlier day taught and calls it review; day 43 reuses "shelter" for a different idea than unit 2.2 day 17. No exit reuses a lower unit's case. "In unit N you learned" claims were checked against the named day for days 22, 35 and 43 and held. The "less harm" review on day 43 holds; the "If we, then" review on day 57 does not.

## Counts

| Day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| 12 | 0 | 5 | 0 |
| 22 | 1 | 4 | 0 |
| 35 | 0 | 3 | 0 |
| 43 | 1 | 5 | 1 |
| 57 | 3 | 1 | 0 |
| All | 5 | 18 | 1 |

The "key-on-child-page" row is counted once, under day 12, though it applies to the exit masters for days 43 and 57 too.


## Fixes applied (2026-11-22)

Cleanup job at grade close. One line per finding.

- d057 FIRM rule 4, exit reuses day 56 and the repair picture: applied. The exit is a new classroom corner (paper bin, single-use cups, gap behind the cupboard). X57a is a touch; X57b is "Tell why that helps" (hear three, 30 seconds each). Items, wrongs, cards, key, u06-1.md updated.
- d057 FIRM "If we ___, then ___" called a review: applied. Taught as "A new frame" (2 minutes); the review claim removed in d057 and u06-1.md. Stage: section plan. Ledger entry for the lead.
- d057 FIRM exit timing (3 minutes): applied (a touch plus hearing three at 30 seconds).
- d057 SOFT X57a key depends on the vote: applied (key now names the three possible pictures).
- d022 FIRM build and test cannot finish: applied. Builds are checked before class plus a 10 second glance per group; d022 and u03-1.md updated.
- d022 SOFT X22a hands over the answer: applied.
- d022 SOFT shape of P22-1 and X22c: applied (X22c now points to where the ball should be to say the ramp worked, the cup).
- d022 SOFT 30 ramp mats not in print: applied (print line: per child ramp mat and cards).
- d022 SOFT warm-up holds two repairs, rug four things: partly (warm-up retell dropped; the rug still holds four things).
- d012 SOFT afternoon look only in day 11 "Other rooms": left.
- d012 SOFT no minutes for going out and in: applied (warm-up 4, practice 4, line up, go out and teacher check 4).
- d012 SOFT X12 same shape as X11b: applied (yes/no on Pip's claim about every table).
- d012 SOFT key lines on the exit-card piece: applied (part C).
- d012 SOFT claim never called back: partly ("as the box and the block were laid on our floor" added; the word "review" is not used).
- d035 SOFT "another observer's record" about our own cards: applied (sentence removed; P2 now a plant in the duck's bill).
- d035 SOFT P35-2 and P35-3 keys disagree with the card sheet: partly (key and card agree on the duck; the light row reading was left).
- d035 SOFT X35a and X35b shapes: applied (light ask; "Tell me what the hiker eats").
- d043 FIRM "Read the captions" contradicts itself: applied. Only strips A to F in two groups, 40 seconds each; G to J written after class and read on day 44. d043, caption-strips.md, u04-3.md updated.
- d043 SOFT group turns timing: left (182 seconds against 180).
- d043 SOFT no second task for waiting children: applied.
- d043 SOFT captions D and E wording: applied.
- d043 SOFT "shelter" reused: applied ("safe place").
- d043 SOFT X43b names no thing: applied; X43a shape kept and the note written.
- d043 TEMPLATE lesson.py NOTE about the number 30: left (template point).


## Key lines in pieces (part C)

Moved: 36 teacher key pieces (key-<name>.md, "Teacher only. Never print this page") were made in the same unit folders, and the key text was removed from the child-facing card, sheet and page pieces they answered: cards-exits-1-4, cards-same-or-different (u01-1); cards-day9-fresh, cards-exits-5-7 (u01-2); cards-exits-10-12, cards-exits-13-14 (u02-1); cards-actions, cards-assessment-forecast, cards-assessment-weather, cards-exit-19, cards-exits-15-17, cards-repair, pages-july-first, squares-regional-july (u02-2); cards-exits-20-24 (u03-1); cards-exit-28, cards-exits-25-26 (u03-2); cards-exits-32-35, cards-park-pond, cards-water-light (u04-1); cards-dam-nest, cards-evidence-38, cards-exits-36-39, cards-places, map-pips-town (u04-2); cards-assessment-argument, cards-assessment-model, cards-assessment-needs, cards-exits-40-43, plans-pips-town (u04-3); cards-exits-44-48 (u05-1); cards-assessment-cover, cards-assessment-warmth, cards-exits-49-54 (u05-2); cards-exits-55-58 (u06-1); cards-exits-59-61 (u06-2). About 55 day files now name their key piece in Before class ("Key: key-..."), and the lesson-day check passes with them.

Left, with the reason: u06-2 scene-shortcut (false hit: no key, only the words "never a finished answer"); u05-1 cards-shade-covers (its "(key)" labels described the drawings of the nine sort cards, teacher-side drawing specs, so they were relabeled, not moved); the repair card sets (u01-2 cards-repair, cards-repair-34-35, cards-repair-36-40) and the caption strips and sticker cards, which are teacher-only strips read aloud or wrong-beside-right pairs by design.

## Gate counts

| Gate (filtered to this course) | Before | After |
|---|---|---|
| plan.py check, FAIL lines | 43 | 13 (all "section ... is not in data/units.csv", the known template point) |
| lesson.py check, FAIL lines | 0 | 0 |

The lesson check also printed no FAIL lines after the fix. Along the way, adding key names to Before class pushed 29 teacher pages over the 450 word cap; I trimmed words (not content) until all passed. Whole filtered output after: 13 FAIL lines, all the known template points.
