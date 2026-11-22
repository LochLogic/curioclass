# Full read, science-grade-1, set e (days 19 to 25), 2026-11-22

Read-only grade-close full read (stage 6 of docs/COURSE-RUN.md), part e of eight. Each day was read cold with the day before it, its section plan block, DEFAULTS.md, its days.csv, items.csv and wrongs.csv rows, the unit's errors.csv and handbacks.csv rows, and every piece in `leans_on`. Every exit and end key was reworked by hand. Facts checked against a source: the tortoise shell (sources.csv 4G, NPS). Facts judged only, with no source row: beetle wing covers protect the wings, pine cone scales cover seeds, fish scales cover the body, insect feelers touch, pig and willow features, gray squirrel and white mouse features. All blade orders were checked against the stated millimeters (MY1 40, MY2 55, MP 70, MA 80; EY1 35, EY2 65, EP 85; WY1 45, WY2 80, WP 110, WA 130): every stated order is right.

Gates: `plan.py check` (filtered) prints 13 FAIL lines for science-grade-1 plus shape-note FAIL lines. All of them are the known "section not in data/units.csv" and "shape-note" lines, so none belongs to this set. The lesson gate was not run (the lead runs it).

## Days read

- courses/science-grade-1/u02-2/d019.md, Application: teachable and well staged, but the exit no longer asks children to copy a plant or animal part, so it does not measure 1-LS1-1.
- courses/science-grade-1/u02-2/d020.md, Check (observe): runs in its minutes and is clean, with small mismatches (the prompt count, a caption that hints at a job, one marker table or six).
- courses/science-grade-1/u02-2/d021.md, Check (observe): the 36-second group turn cannot hold the account both end items ask for, and one distractor on the unscored exit is also a right answer.
- courses/science-grade-1/u03-1/d022.md, Understanding: a strong hook and model, but the length exit is the group practice in new numbers, and the per-child exit print carries the keys.
- courses/science-grade-1/u03-1/d023.md, Application: sound and teachable. The data rows are stale, and "fur" is said to come from a chart that does not have it.
- courses/science-grade-1/u03-1/d024.md, Fluency: clean routine day with a correct repair. Only the data rows are stale.
- courses/science-grade-1/u03-1/d025.md, Application: good consolidation day. One review claim does not hold, the expected sentence has a grammar slip, and the exit skips the "ordered differences" half of the goal.

## Findings, most serious first

| day | severity | kind | what is wrong | the exact fix | stage | gate? |
|---|---|---|---|---|---|---|
| d021 | FIRM | timing | Group turns give about 36 seconds a child (18 min for 30) for both s02-E21a and s02-E21b. Together they ask for about ten pointing acts: roots and water, the stem and light, the shoot bend, the tortoise, the shell joined to the cover, the marker, the gap, the open side, the arch and the viewing side. The teacher must also write each spoken reason. That cannot fit in 36 seconds. | Read the marking components (roots, stem, shoot arrow, tortoise arrow, and the marker, gap and open side already circled on the day 20 cover page) from the paper, as the record rule for components 1 to 5 already allows. Cut the oral turn to two asks: "Which part did you copy, and why?" and "Show how your shape keeps the vase safe and lets a visitor see." Change the s02-E21a and s02-E21b steps and the s02.md field 5 schedule to match. | unit plan | no |
| d021 | FIRM | key | The s02-X21 cards are: strips that close around the berry; a bird picture stuck on; "a longer strip". The problem is two strips that cannot meet, so a longer strip is also a fix that lets them meet and grip. The distractor is a second right answer. | Replace "a longer strip" with a distractor that cannot help the strips meet, for example "the strips colored red". Change items.csv s02-X21 stem and cards-exits-16-19-21.md to match. | section plan | no |
| d019 | FIRM | exit-goal | s02-X19a is tagged 1-LS1-1, copy-part, and the shows map says it shows "choose another nature-inspired problem". The kit (a slot card, a scrap, three strips) names no plant or animal part, so a child can pass with no copying at all. The plan's E19a (cards to touch) was also changed to a build without the plan being updated. | Give the exit a copied part: show one invented-for-practice part card the class has not seen (for example a camel's long eyelashes, which keep sand out and still let it see), then ask "Lay the strips across the window the way the eyelashes keep sand out." Change s02-X19b to "Say which part you copied and how its shape does the job." Add a source row for the eyelash fact, and update u02-2.md E19a and E19b to the kit form. | data | no |
| d022 | FIRM | rule4 | s03-X22b (lay three blades, bases together, shortest to longest: two young, then the parent) is the group practice (lay MY1, MY2 and MP and say longest and shortest) in new numbers. DEFAULTS says an exit is "not the worked example in new numbers". A child can also answer from "young are small" without comparing tips. | Use exit blades whose order breaks the young-then-parent pattern, for example EA (another adult) 50 mm, EY2 65 mm and EP 85 mm, with the key EA, EY2, EP. Keep gaps of at least 15 mm. Update cards-exits-22-27.md, items.csv and wrongs.csv. | section plan | no |
| d022 (also d023 to d025) | FIRM | key-on-child-page | The print lines give "Per child: exit card (cards-exits-22-27)". That piece prints every **Key:** line, the teacher-only blade sizes and the wrong answers. The per-group M22 packet (cards-m22.md) also prints "Order: MY1, MY2, MP" and "Key: needles". | Print the child's exit card and packet from picture-only masters. Mark cards-exits-22-27.md and cards-m22.md as teacher pieces, and name a picture-only master in each print line (the "exit masters" the plan lists as still to make). | kit | yes |
| d019 | SOFT | rule4 | Problem card 2 (keep paper rain off a bed, leave a way for a hand in) has the same shape as the exit (keep a scrap out, let air through). | Once the exit is rebuilt around a copied part, make the practice keep-out card a "cover" task with no let-through condition, or make the exit a detect or hold task. | section plan | no |
| d019 | SOFT | other | Before class never says to make 30 slot cards with 5 cm windows and cut the scraps and strips. The print line does not list the kit. | Add to Before class: "Cut a 5 cm window in 30 cards; bag each with a 2 cm scrap and three 1 cm strips." Add the kit to print or materials. | day | no |
| d019 | SOFT | key | The error D look-for is "a drawn thorn picture", but no thorn appears anywhere in the day or the kit, so children have nothing to prompt it. wrongs.csv rows s02-X19a and s02-X19b keep it. | Make the D look-for the stuck-on copied-part picture from the new exit card (for example "draws eyelashes on the card"). Update wrongs.csv. | data | no |
| d019 | SOFT | timing | "Say it", 3 min: pair talk (about 40 s) plus six heard at 30 s (180 s) comes to about 220 s. | Hear four, or cut to 20 seconds each. | day | no |
| d019 | SOFT | source | Part cards 5 to 8 (pine cone scales, insect feelers, beetle wing cover, fish scales) state facts about real organisms with no sources.csv row. I judged them right. | Add a solid source row (a museum or university page), checked 2026-11-22. | data | no |
| d019 | SOFT | other | The at-home exit needs a card with a window, but Swap gives no stand-in. | Swap: "Cut a window about two fingers wide in a cereal-box card." | day | no |
| d019 | SOFT | key-on-child-page | The per-group problem and part cards piece prints which four cards fit the problems. | Move that line to a teacher note that is not printed. | kit | no |
| d020 | SOFT | words | "Read eight prompts aloud" is followed by only seven prompts. | Change to "seven prompts". | day | yes |
| d020 | SOFT | exit-goal | The evidence-page captions "roots in water" and "leaves raised on a stem" all but name the jobs that s02-E20a asks children to mark. The plan says captions give observations, not jobs. | Recaption them as "roots in a jar" and "a stem with leaves". | kit | no |
| d020 | SOFT | other | Set-up gives "six tables of five, each with a marker", but Sketch, make, check runs one marker table of 30 slides that the teacher records. | Choose one: a single marker table at the teacher, one marker in materials. | day | no |
| d021 | SOFT | timing | Exit, 3 min: show the cards, all touch, then six said at 30 s each comes to more than 180 s. | Six at 20 seconds each. | day | no |
| d022 | SOFT | exit-goal | The s03-X22a key accepts "the stem, or the roots". Every plant, the pine included, has them, so the answer shows nothing about resemblance to a parent. | Key: the oval, smooth-edged blade. Stem or roots alone counts as shown with help, with the prompt "what about the leaf?". | data | no |
| d022 | SOFT | ladder | The retrieval and the model use "I saw ___, so ___". Kindergarten taught the claim and evidence frame as "I think ___, because I saw ___" (science-kindergarten u04-2 day 38). Those are new words for an old idea. | Use "I think ___, because I saw ___ (review)" in the retrieval and the model. | day | no |
| d022 | SOFT | timing | Exit, 5 min: six said at 30 s for X22a (3 min), then 30 children lay blades and the teacher checks each layout. That is over the 5 minutes. | Hear six for X22a at 20 seconds; check six layouts during the exit and the rest after class, and say so. | day | no |
| d022 | SOFT | handoff | Tomorrow opens with "Day 21 closed unit 2". It sends a support (the tape line beside the chart for children shown with help) that d023 never picks up. | Drop the day 21 line. Either add the tape-line support to d023's Open or drop it here. | day | no |
| d023 | SOFT | content | Open says "Class says ears and fur from the part-and-job chart". The chart's animal rows are ears and eyes, legs, nostrils and mouth, and scales. Fur is not on it. | "Class says ears from the part-and-job chart; name fur from the picture." | day | no |
| d023 | SOFT | key | items.csv s03-X23a steps say "the parent and the puppy", but the exit case is a squirrel. days.csv day 23 exit still says "a black dog and its puppy". | Steps: "the parent and the young squirrel". Change the days.csv exit to the squirrel case. | data | yes |
| d023 | SOFT | timing | Share, 4 min: six pairs at 40 s fills all 240 s and leaves no time for the partner challenge the plan asks for. | Five pairs, or 30 seconds each. | day | no |
| d023 | SOFT | rule4 | The squirrel parent's "white chest patch" repeats the taught dog parent's white chest. All four exits (squirrel, mouse, goose, and the pig variant) hinge on "one patch in a different place", so a child can learn to find the patch rather than compare. | Give the squirrel exit a different kind of difference, for example tail length, and keep the patch for the mouse. | section plan | no |
| d024 | SOFT | key | items.csv s03-X24a steps say "the cat and the kitten", but the case is a mouse. days.csv day 24 exit says "a white cat and its kitten". | Steps: "the mouse and the young mouse". Change the days.csv exit to the mouse case. | data | yes |
| d025 | SOFT | ladder | Open says "the flat part of a leaf is its blade (review)", but d022 uses "blade" throughout without ever defining it, so the review claim does not hold. | Define "blade" in d022's model and Words. | day | no |
| d025 | SOFT | words | The expected account says "alike their parents". | "Young plants and animals are like their parents in some features and different in others." | day | no |
| d025 | SOFT | exit-goal | The goal names "ordered or listed differences", and the shows map assigns that to s03-X25b. The exit cards give willow blade lengths, but no exit ask uses order. | Either add to the X25b key "the willow blades go from short to long, and all are willows", or change the shows map to "listed differences" only. | data | no |
| d020, d021 | TEMPLATE | other | DEFAULTS says "three asks in one stem are three items". s02-E20a (seven asks), s02-E21a and s02-E21b each bundle many asks under one item id. The day speaks them as separate prompts, and the record reads each as a component on one scale. For a grade 1 observation sitting, one item with component look-fors is the right design. | Leave the items whole. Let the DEFAULTS rule exempt observation end items whose steps are scored as components. | kit | yes |

## Ladder

The grade gap did little harm here. Unit 2.2 leans on grade 1's own unit 2.1 (the part-and-job chart and the day 15 copy-the-shape idea) and names it as review correctly. It uses the kindergarten design cycle and "sometimes, every time" in kindergarten's own words. Unit 3.1 is new content with no lower-grade term ("parent", "alike", "feature", "shorter, longer" are all first taught on day 22), and that is right. The one slip is day 22's retrieval: kindergarten's claim-and-evidence frame ("I think ___, because I saw ___") comes back in new words ("I saw ___, so ___"). Kindergarten's nest case is used only for retrieval, never as an exit, which is good. Kindergarten's "about the same" is used correctly on cards-m22, but no day says it is review. No exit reuses a lower grade's case.

## Counts

| day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| d019 | 1 | 7 | 0 |
| d020 | 0 | 3 | 1 |
| d021 | 2 | 1 | 0 |
| d022 | 2 | 4 | 0 |
| d023 | 0 | 4 | 0 |
| d024 | 0 | 1 | 0 |
| d025 | 0 | 3 | 0 |
| **all** | **5** | **23** | **1** |

The key-on-child-page FIRM is counted once, at d022, though the same print line is in d023 to d025. The TEMPLATE point is counted once, at d020.
