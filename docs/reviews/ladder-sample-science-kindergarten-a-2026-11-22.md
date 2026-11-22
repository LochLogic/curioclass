# Grade-close sample, science-kindergarten, set a (re-sample, 2026-11-22)

Read-only fresh-reader sample. Days: d007, d014, d030, d036, d054, each with the day before and its plan block, data rows and shared pieces. Gates run filtered: plan.py shows 13 FAIL lines, all "section X is not in data/units.csv" (a registration gap for the course's 13 sections, not a content finding); lesson.py shows no FAIL line on any science-kindergarten day.

## Days read

- courses/science-kindergarten/u01-2/d007.md (Fluency): the loaded-box pulls run in the minutes and hand off cleanly on error E, but the rug question has no clear referent and the exit is a binary read-and-compare.
- courses/science-kindergarten/u02-1/d014.md (Application): the Denver July rows are right (checked), but three exit asks plus a crowded 12-minute count part strain the minutes and the exit leaves the pattern-sheet revision unmeasured.
- courses/science-kindergarten/u03-2/d030.md (Check, form B): the minute sums are right, but the 8-second answers and the five-at-once marking do not hold, and F3b repeats a unit 2 case.
- courses/science-kindergarten/u04-2/d036.md (Understanding): the model contradicts itself (meadow with no water but grass and deer linked to water) and the table cards print a key.
- courses/science-kindergarten/u05-2/d054.md (Respond): the touch and the 18 observed minutes fit, but the 5-minute repair names more groups than the data allows and cannot run as written.

## What I checked against a source, and what I could only judge

- Checked against the source: d014's Denver July counts. I re-ran the IEM query in sources.csv row 20A (station DEN, July 2024, local time). Rain-report days 2, 13, 15, 16, 20, 21, 27, 28 = 8 (matches X14a). Days with sustained wind of 20 knots or more: 1, 3, 6, 7, 15, 16, 17, 19, 20, 25, 26, 27, 28 = 13 (matches the windy row). The sunny (14) and cloudy (13) rows rest on the row's own "counts confirmed 2026-11-22" note; I did not recompute them, but 14 + 13 + the four scattered days (2, 6, 11, 20) = 31, so the lists are consistent.
- Checked by hand: every number in d030's form B (windy 2, 4, 5, 8, 9 = 5; cloudy 1, 2, 5, 6, 8; overlap 2, 5, 8; rainy rows 8 and 5, 3 left over; day pairs cooler, warmer, cooler), d014's fourteen, eight and the three exit keys, and all part minutes of the five days (all sum to 30; d030 blocks 3:40 + 2:10 + 2:10 = 8:00; d054 six groups x 3:00 = 18 and 6 x 125 s = 12.5 min).
- Judged only: that a gentle pull may not start the loaded box (d007), the fish-eats-pond-plants link and deer/grass needs (d036, general science, no source row), and the sun and covered-patch warming claims (d054, grounded in source row B7 for the hot-surface rule only).
- Browser check: none. No fact needed a blocked page.

## Findings, most serious first

| day | severity | kind | what is wrong | the exact fix | stage | script gate? |
|---|---|---|---|---|---|---|
| d036 | FIRM | content | The meadow picture (cards-places) shows "no water in view", yet the day has the tables link the grass to water and the deer to grass, water and air, P36-2's key says the meadow has no water, and What if says "no water link, no fish here". A child sees grass living in the meadow with no water link, which teaches unit 4.1's error A (plants do not need water) and breaks the day's own rule. It never says which place the deer is in (forest has a stream but no grass; meadow has grass but no water). | In cards-places add a rain cloud with drops to the meadow (and grass to the forest edge, or place the deer in the meadow with the rain). Change P36-2's key to grass to the sun, the rain or the land. Say in the day which place each of the deer and grass sits in. The fish-in-the-meadow case stays (no pond water). | section plan, kit | no |
| d036 | FIRM | key-on-child-page | cards-places.md is printed "per table" and handled by children, and it ends with a `## Key` section ("The fish: lines to water and to pond plants ... the grass in the dark forest has no light line") plus a "What happens" section that gives away the hook. | Move Key and What happens to a teacher-only key piece (as key-order.md does), unprinted, and leave the pictures, cards and marks in cards-places. | kit | yes |
| d054 | FIRM | timing | Return and repair (5 min) lists six error sets (A and B, C, G, H, D, E and F) while saying "at most four" groups, and the handbacks table has no row for error G at all (only A, B, C, H from day 52 and D, E, F from day 53). Every child also revises the day 54 mat from the sticker in the same five minutes. One teacher cannot run swap-a-sample, trace the shadow, move-and-tape and a paired-record repair at 75 seconds each while thirty children revise mats. | Rewrite the part: the two largest error groups (from the record) work with the teacher, 2 min each; everyone else revises the mat from the sticker alone; drop G or add its handbacks row and a day 52 source; write "at most two" in day, plan and handbacks. | day, section plan, data | partly (a count of sets against "at most four" and a missing handback) |
| d030 | FIRM | timing | c1-K5b is 40 s for five children, 8 s each, but it asks three explanations (van, sled box, ball) plus "point to a mark". No five-year-old can do that in 8 s, and the teacher is also watching four other lanes. | Cut K5b to one ask ("What made the van go? Point to a mark") at 8 s, or give it 20 s each and take the time from a change-over. Move the other two explanations to the day 31 fresh questions. | data (item), day | no |
| d030 | SOFT | other | Five children are marked at once on 14 items with three or four look-fors each in 8 minutes by one teacher; most steps ("keeps every mark made", "does not touch a different van") cannot be seen at lane distance. | Mark each child only on the outcome look-for per item (the first listed step) and mark the rest as "seen" when the child's mat shows it; or add a second adult for the three lane items. | section plan (course check design) | no |
| d030 | SOFT | other | Rule 7 (one ask per stem): K1b asks two things, K2b four (push, push, dot, mark faster), K3b, K4b and K5b two to four, W3b three (match, which month, point), F3b two (before and thunder). | Split into one-ask stems and cut the step count, or give each its own seconds. | data | partly (count of verbs) |
| d030 | SOFT | content | F3b, F1b and F4b use "a school garden walk after lunch", but the F3b key says "plan the picnic indoors first" and Page B uses "the same cards" (which says picnic). The town rows (Hill 9, Lake 1) are not tied to the class's own town, so "the town with more thunder days" is open. | Page B card to read "plan to be indoors first"; key to match; add a line saying which town is the school's. | kit, data | no |
| d030 | SOFT | rule4 | F3b ("go into the school building, a tree is not shelter") is the same case as s02-F3b on day 19. | Use a new setting (a bus stop, a sand lot) with a shelter card the class did not meet. | data | no (needs a text match across days) |
| d030 | SOFT | other | The "form B so a child told cannot repeat an answer" claim is false: K1, K3, K5 and F3 have the same answers as form A. | Delete the claim, or change the structure (compare "which way" first, pull before push) so the order and the cards differ. | day | no |
| d030 | SOFT | other | P30-2 (sort weather pictures into windy and calm) has no cards in the materials or print list, and 25 children have two small tasks for 26 minutes (sort or draw side 2). | Add a sorting-card set to print and name a third task (the unit 1 order cards) for waiting children. | day, kit | partly |
| d030 | SOFT | timing | "Collect the mats and finish the record sheet for days 29 and 30" has no minutes (the last block is the 8 min for group 6); a child away yesterday joins group 4 (six children, five lanes). | Take 1 minute from the day for collect and finish, or tell the teacher to finish the sheet after school; seat the absent child at group 6. | day | no |
| d030 | SOFT | other | At home "Skip: the rug" (no rug in the day); "firm paper ball" has no size, and the motion is rolled by hand. | Delete "the rug"; say "a ball too big to put in a mouth". | day | no |
| d036 | SOFT | exit-goal | The goal is deer, grass and fish links to forest, meadow and pond; the exit (sunflower, sunny bed with tap versus dark bed) re-asks unit 4.1's water and light needs on a plant and uses none of the day's deer, fish, air or land links. | Make 36a a link question on the day's idea in a new pair: "Touch the place where a duck gets what it needs: a pond edge or a dry parking lot." | section plan, data | no |
| d036 | SOFT | rule4 | X36b ("draw one line from the sunflower to one thing in its bed that helps it live") has the same shape as P36-1 and P36-2 ("draw a line from the fish/grass to something it needs"). | Make 36b a spoken tell ("Tell me what one line from the duck would go to"), or touch one of three marks. | data | no (shape match) |
| d036 | SOFT | words | The exit key accepts "soil", the day teaches "land" (brown mark), and the day never names resource or system although the ledger plans both for day 36. | Use "land" in the exit key and either teach "resource" in the Build part or move the ledger lines to day 37. | data, ledger | partly |
| d036 | SOFT | other | X36b needs a per-child yard sheet ("on the sheet"), but only one exit card set is printed for the class, and the at-home exit says "ask once each" with no picture to touch or draw. | Print the yard picture on the back of the student page and add a one-line home swap ("draw two beds, one with a tap and one dark"). | day, kit | yes (print list against stem) |
| d036 | SOFT | ladder | Air is introduced as a need ("the swirl for air") with "do not say how it is used" and no first-time label; the day is "Understanding", new content. | Add one line: "Air is all around the deer; the swirl mark is our picture of it," or drop air from the day and keep three marks. | day | no |
| d036 | SOFT | timing | The 10-minute Build holds the teacher model, two table drawings, two student-page drawings per child, and 6 x 40 s of hearing. | Cut the hearing to 20 s each or the student page to one picture. | day | partly |
| d054 | SOFT | rule4 | X54a (move the cover over the patch) is the same case and shape as day 53's D1a (a cover over versus beside the patch) and the day's own repair for error D (move a piece and tape it). | Use a new object (a doll's umbrella over a doll's seat) and keep the three cards, or ask for the reason first. | data | no |
| d054 | SOFT | exit-goal | X54b ("Same card. How does the card help you choose?") is unclear to a five-year-old ("card"), and its key restates the caption read aloud in X54a (the open patch was warmer); the only new part is "so the sun must be kept off". "Move or stretch" has a word children do not use. | "Why does moving the cover help?" key: it keeps the sun off the patch. Card text: "move the cover over the patch". | data, kit | no |
| d054 | SOFT | other | At home the exit asks cards the home does not have; a home "Longer" option adds a second material (extra safety load). | Add "Draw a roof beside a patch and a roof over a patch" as the home swap; delete the longer option or add sand-only wording. | day | yes |
| d054 | SOFT | timing | 25 children draw the same slide-and-shade picture (P54-1, the third day running after days 52 and 53) for 18 minutes while one group is observed; before class the teacher touches about 60 samples. | Give the waiting groups a second quiet task (the cover mat, a stage-by-stage "my build" drawing) and drop the pre-touch to 30 by touching only the covered side first. | day | no |
| d054 | SOFT | other | The day 54 feedback and repair rely on strips A to H "held back", but only G's hint ("two bowls of sand with the same clock") duplicates C's picture ("two pots of the same sand"). | Redraw G with two clocks showing different hours. | kit | no |
| d007 | SOFT | words | The rug asks "Is it true for this box and this floor?" with Expect "yes", but "it" is the day 3 claim (not named in the day) and the same day's exit key is "no" (the loaded gentle pull did not move). A teacher with no prep cannot tell what "yes" means. | Write the claim in the day ("a harder pull moves the box farther") and Expect: "yes for the harder pull; the gentle pull may not start it, and we keep that". | day | no |
| d007 | SOFT | rule4 | The plan notes the exit "reads two finished strips and says whether they match, which no practice part asks", but the Rug lays strips side by side to compare them, which is the same ask. | Change the exit to "which cart needs a harder pull to start" or have children say what to do next. | section plan, data | no |
| d007 | SOFT | exit-goal | X7 is a two-way yes or no with a hint in the stem (empty moved both times), so "no" can be guessed; the key also needs the gentle-pull mention, a second ask. | Ask "What happened to the loaded cart on the gentle pull?" key: it did not move. | data | no |
| d007 | SOFT | handoff | The plan says "Hand-back out: error A to day 9"; the day, the data and the Tomorrow line say E. | Fix the plan to E (A belongs to day 3). | section plan | partly |
| d007 | SOFT | timing | Pulls (12 min) = 6 + 6 with 5 x 2 x 35 s = 5.8 min a half and no swap time, while the warm-up repair adds "two minutes at one lane". | Make it 5 + 5 with a 2-minute swap, or cut the repair to the warm-up only. | day | no |
| d014 | SOFT | exit-goal | The goal includes "revise the pattern chart" and the day's written task is the dictated "more ___ than ___" line; no exit item measures either (X14b and X14c test overlap and matching). | Add or replace X14c with "Say what this month shows: more sunny or more rainy days", key: sunny (14 against 8). | section plan, data | no |
| d014 | SOFT | rule4 | X14a (touch each rainy day once in a Denver row and say how many) is the day 13 exit s02-X13 (rainy days in a Denver row) with 8 in place of 4. | Count windy days (13) or a month with a 10 total; or a new weather. | data | no |
| d014 | SOFT | ladder | The exit uses "the card with one dot or two dots" for one day or two, a notation no day teaches. | Teach the dots in the Rug or use "touch the date square that is in both rows". | day, data | no |
| d014 | SOFT | timing | The 12-minute count part (sort about 20 squares, count four rows, dictate a line the teacher writes for six groups, each child draws a row, hear six) and the 5-minute Rug (fill the graph, recount, match, ask, revise) are crammed; the exit has three asks, "everyone touches" one class card, and six x 15 s in 3 minutes. | Drop the graph fill to the next day, have groups write their own line with a frame, and make X14b and X14c a two-ask exit. | day | no |
| d007, d014, d036, d054 | SOFT | key-on-child-page | The exit-card pieces (cards-exits-5-7, -13-14, -36-39, -49-54) are printed "per class" and shown to children, and contain **Key:** lines and spoken answers; the file says the teacher's readings "are in brackets and never printed", but the keys are not bracketed. | Split each exit-card file into pictures and a teacher key piece (unprinted), as u01-1 does with key-order.md. | kit | yes |

## Ladder

Kindergarten is the bottom of the science ladder, so there is no lower grade to reuse or to be reused wrongly: `ledger.py show science --before science-kindergarten` returned only this course's own planned lines. The grade gap showed up in three places. First, d036 introduces air and land as resources with no earlier unit teaching them; the plan says "place, resource, system" are taught on days 36 to 37, but the written day names none of them except "link" and "place". Second, d014 and d013 call the unit 1 strips "stopping strips" while unit 1's own days say "before and after strip" and "dot strip", a third name for one idea. Third, d030 re-asks taught cases (the school building versus the tree) by design, which is right for a check but means rule 4 as written cannot hold there. The course otherwise used its own earlier units well: d035 to d036 repeat the same words (water, light, eats) and d053 to d054 keep the design-cycle and covered-and-open frames; every review claim I followed ("as the strips were in unit 1", "day 12 claim") held in the day it names.

## Counts

| day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| d007 | 0 | 5 | 0 |
| d014 | 0 | 4 | 0 |
| d030 | 1 | 8 | 0 |
| d036 | 2 | 6 | 0 |
| d054 | 1 | 5 | 0 |
| shared exit-card key (d007, d014, d036, d054) | 0 | 1 | 0 |
| all | 4 | 29 | 0 |


## Fixes applied (2026-11-22)

Cleanup job at grade close. One line per finding; "stage" is where the fault was made. Files touched are under courses/, data/plans/ and docs/courses/science-kindergarten/ only.

### Findings, set a

- d036 FIRM meadow shows no water: applied. Stage: section plan and card kit. cards-places now draws a grass strip beside the stream in the forest and a rain cloud with drops over the meadow; d036 says the deer stands at the forest edge, the grass is in the meadow, adds the air line; P36-2 answer is sun, rain or land; the 20 second hearings.
- d036 FIRM key on a child page: applied. The "What happens" and Key text left cards-places for key-places.md; the day names it in Before class.
- d054 FIRM six error sets in 5 minutes, no row for G: applied. Stage: day, section plan, data. At most two groups at 2 minutes each, everyone else revises the mat from the sticker, G read in feedback only; d054, u05-2.md, caption-strips and the handbacks W3c row note updated.
- d030 FIRM K5b too many asks for 8 seconds: applied (also c1-K5 on d029). One ask (what made the van or car start; point to a mark); wrongs row now "Rubs out a mark that looks wrong".
- d030 SOFT five-child marking load: left (a teacher judgment about the lanes, no short clear fix).
- d030 SOFT rule 7 splits for K1b to K4b and W3b: left. Only K5b was a FIRM cut; the rest wait for a rule 7 sweep of the form.
- d030 SOFT F3b and Page B "same cards" says picnic: applied. The F3b answer and Page B now say "plan to be indoors first".
- d030 SOFT F3b reuses the day 19 case: left (a deliberate repeat for a check).
- d030 SOFT form B claim false: applied (claim removed; group-absent seat is group 6).
- d030 SOFT P30-2 has no card set: left (needs a new print piece).
- d030 SOFT collect mats and record sheet unminuted: applied (collect at the last child, finish the sheet after school).
- d030 SOFT at-home "rug" and firm ball: applied.
- d036 SOFT exit does not use the day's links: applied. X36a and X36b are now a duck at a pond edge or a dry parking lot; wrongs, cards, key, u04-2.md updated.
- d036 SOFT X36b same shape as practice: applied (spoken tell).
- d036 SOFT soil versus land, resource and system never named: partly. The exit key says land; "resource" and "system" are not taught (ledger entry for the lead below).
- d036 SOFT yard sheet per child with one card set: applied (the new exit needs no sheet).
- d036 SOFT air has no first-time label: applied (one air line).
- d036 SOFT Build part crammed: applied (hearing 20 seconds each).
- d054 SOFT X54a same case as day 53: applied (doll's umbrella over a doll; X54b a doll's blanket, "Why does moving the umbrella help?"). Items, wrongs, cards, key, u05-2.md updated.
- d054 SOFT X54b unclear card: applied (same change).
- d054 SOFT at-home cards and longer option: applied (swap: a roof beside and a roof over a patch).
- d054 SOFT waiting groups draw the same picture: applied (second task: cover mat; pre-touch about 30 samples).
- d054 SOFT strip G hint: left (needs a redraw of the strip picture).
- d007 SOFT rug claim not named: applied. Exit X7 changed to "Tell me what happened to the loaded cart on the gentle pull" (it did not move).
- d007 SOFT exit shape: applied (new exit).
- d007 SOFT X7 yes/no with hint: applied.
- d007 SOFT plan says error A to day 9: applied (plan now says E).
- d007 SOFT pull timing: left.
- d014 SOFT exit does not test revise: applied (X14c "say what this month shows").
- d014 SOFT X14a same as day 13 exit: applied (windy days, thirteen; "Touch each windy day once. Say the last number.", which also clears the one-ask FAIL).
- d014 SOFT dots notation untaught: applied (X14b "Say one or two").
- d014 SOFT crammed count part: left.
- Shared exit-card key lines (d007, d014, d036, d054): applied, see part C.

### Findings, set b (also listed in report b)

See the "Fixes applied" section of report b for d012, d022, d035, d043 and d057 line by line.

### Part D: shape-note days

The filtered plan check printed 30 shape-note FAILs. For each day below the practice and the exit were read. Where they truly shared a shape the exit was changed (new case, different act); then the plan day block's "Shared shape (note, not timed)" was written to say what the day does.

#### Day 1
No change. Practice rolls, draws three boxes and sorts notices; the exit is a new cushion case on cards. Note written.
#### Day 7
Exit changed (see above). Note written.
#### Day 9
No change. Practice is an observed turn and the record; the exit is two invented picture pairs. Note written.
#### Day 10
No change. Practice reads dated rows and draws a sky; the exit chooses which question two invented pictures answer. Note written.
#### Day 12
Exit X12 changed to a yes/no on Pip's claim about every table (a new case and a claim test instead of reading rays). Minutes: warm-up 4, practice 4, line up and teacher check 4 (opening matches days.csv). Note written.
#### Day 13
No change to the exit. Honest note: the practice and the exit both count by touching each once and saying the last number; the exit counts five invented squares alone, with no placing and no partner, and the count is the thing measured.
#### Day 14
Exit changed (X14a windy days, X14b "Say one or two", X14c what this month shows). Note written.
#### Day 19
X19b changed from the plan-first card touch (the same as practice F3a) to a spoken reason for the plan-first rule. Wrong row F updated; cards, key and u02-2.md updated. Note written.
#### Day 22
X22a hint sentence dropped; X22c now "Point to where the ball should be to say the ramp worked" (the cup); builds checked before class plus a 10 second glance; retell dropped from the warm-up. Note updated.
#### Day 25
X25b changed to "Tell me one thing you could look at to find out why it tips." Items, wrongs, cards, key and u03-2.md updated. Note written.
#### Day 28
X28a changed to "Touch the place where the boat should end to say the guide worked" (the dock; the guide or the turn is error E). Items, wrongs, card, key, u03-2.md updated. Note written.
#### Day 32
No change. Practice circles repeating pictures and draws a need; the exit is a new roof garden, one pointing ask and one spoken wonder. Note written.
#### Day 33
X33a changed to "A sunflower and a goat. Tell me one thing both of them need." (water; leaving the plant out is error A). Cards, key, items, wrongs, u04-1.md updated. Note written.
#### Day 34
X34a changed to "A goat eating grass and a sunflower being watered. Touch the one that eats." (the goat; the sunflower is error C). Two cards only. Note written.
#### Day 35
X35a is a light ask (two bushes, one in the sun and one under a roof of branches); X35b is "Tell me what the hiker eats". Note written.
#### Day 36
Exit replaced by the duck case (see above). Note written.
#### Day 37
X37b changed from a drawn line to a spoken "Tell me one more thing from the land that the keeper uses." Note written.
#### Day 40
X40a is now spoken ("Tell me what is left standing if the rack goes on spot 1"). Note written.
#### Day 43
Exit X43b now "Say what the tree changed: I think ___, because I saw ___." Note written.
#### Day 44
X44b changed to "If the wall shade came back over the soil, what would the soil feel like?" (cooler; "the same because it is later" is error H). Items, wrongs, cards, key, u05-1.md updated. Note written.
#### Day 47
X47a changed to a spoken "what to do with the awning to keep the sun off the bench" (move it over); X47b now points to the part of that awning. Items, wrongs, cards, key, u05-1.md updated. Note written.
#### Day 48
No change. The practice touches real pairs; the exit predicts from the class pattern on invented pictures. Note written.
#### Day 50
No change. The practice touches real samples and moves a piece; the exit is a card fix and a claim from the card. Note written.
#### Day 51
No change. The practice touches two real patches and marks; the exit is a yes/no on a caption card and a why. Note written.
#### Day 54
Exit changed (doll's umbrella and doll's blanket). Note written.
#### Day 55
X55a changed from a tally to "Touch the kind there is more of" (four paper scraps against two bottles). Card, key, items, wrongs, u06-1.md updated. Note written.
#### Day 56
X56b changed to a spoken "Tell me one thing the school could do so the pond is hurt less." Note written.
#### Day 57
Exit moved to a classroom corner (a touch, then "Tell why that helps"); the warm-up now teaches "If we ___, then ___" as a new frame. Note written.
#### Day 58
X58a changed to a spoken "Tell me what changed between the two drawings." Note written.
#### Day 59
X59a changed to "Touch the corner that had fewer wrappers after the action." (the first corner). Note written.
#### Day 61
X61a changed to a card touch (a grown-up closing the lid; paper tucked under the shrubs is error C; a longer path). Note written.

### For the lead: sweep

- "Review" claims for a frame never taught (stage: section plan): d057 called "If we ___, then ___" a review though day 56 never taught it. Look for the same in other unused day blocks.
- Key text inside a printed card or page piece (stage: piece/kit): found in 36 pieces here; check unused pieces in every course.
- Exit that repeats the day's practice act (stage: section plan): 23 of the 31 shape-note days needed a new exit act.
- Exit that reuses an earlier day's case (stage: section plan, data): d014/d013 and d054/d053.
- Parts that name more error sets than the minutes allow (stage: section plan, data): d054.
- Rule 7 multi-ask stems on the observation form (stage: data): d030 K1b to K4b, W3b.

### Ledger entries for the lead

- "If we ___, then ___" is first used on day 57 (not day 56).
- "resource" and "system" are planned for days 36 and 37 but not taught.
- "air" is now introduced on day 36 (one line, the swirl mark).

## Key lines in pieces (part C)

Moved: 36 teacher key pieces (key-<name>.md, "Teacher only. Never print this page") were made in the same unit folders, and the key text was removed from the child-facing card, sheet and page pieces they answered: cards-exits-1-4, cards-same-or-different (u01-1); cards-day9-fresh, cards-exits-5-7 (u01-2); cards-exits-10-12, cards-exits-13-14 (u02-1); cards-actions, cards-assessment-forecast, cards-assessment-weather, cards-exit-19, cards-exits-15-17, cards-repair, pages-july-first, squares-regional-july (u02-2); cards-exits-20-24 (u03-1); cards-exit-28, cards-exits-25-26 (u03-2); cards-exits-32-35, cards-park-pond, cards-water-light (u04-1); cards-dam-nest, cards-evidence-38, cards-exits-36-39, cards-places, map-pips-town (u04-2); cards-assessment-argument, cards-assessment-model, cards-assessment-needs, cards-exits-40-43, plans-pips-town (u04-3); cards-exits-44-48 (u05-1); cards-assessment-cover, cards-assessment-warmth, cards-exits-49-54 (u05-2); cards-exits-55-58 (u06-1); cards-exits-59-61 (u06-2). About 55 day files now name their key piece in Before class ("Key: key-..."), and the lesson-day check passes with them.

Left, with the reason: u06-2 scene-shortcut (false hit: no key, only the words "never a finished answer"); u05-1 cards-shade-covers (its "(key)" labels described the drawings of the nine sort cards, teacher-side drawing specs, so they were relabeled, not moved); the repair card sets (u01-2 cards-repair, cards-repair-34-35, cards-repair-36-40) and the caption strips and sticker cards, which are teacher-only strips read aloud or wrong-beside-right pairs by design.

## Gate counts

| Gate (filtered to this course) | Before | After |
|---|---|---|
| plan.py check, FAIL lines | 43 | 13 (all "section ... is not in data/units.csv", the known template point) |
| lesson.py check, FAIL lines | 0 | 0 |

The lesson check also printed no FAIL lines after the fix. Along the way, adding key names to Before class pushed 29 teacher pages over the 450 word cap; I trimmed words (not content) until all passed. Whole filtered output after: 13 FAIL lines, all the known template points.
