# Grade-close sample, set a: science-grade-2 (re-sample after the 2026-11-19 read and the 2026-11-22 exit fixes)

Reader: fresh, read-only. Days read cold, one at a time, each with the day before, its section plan block, DEFAULTS.md, its days.csv, items.csv, wrongs.csv, handbacks.csv rows, the unit's errors.csv rows and the pieces its `leans_on` names. Ledger terms looked up with filtered `ledger.py show`.

Gates run (filtered only): `lesson.py check` prints 0 FAIL lines for science-grade-2 (all five days pass: teacher 542, 465, 524, 549, 524 words; student 64, 140, 41, 49, 22 words). `plan.py check` for science-grade-2 prints 16 FAIL lines, all "section N.n is not in data/units.csv" (one for each of the 16 sections), plus error-source notes. They are a data-registration gap, not a fault in any of these days.

## Days read

| Day | File | Kind | Verdict |
|---|---|---|---|
| 5 | courses/science-grade-2/u01-2/d005.md | Understanding | Runs in its 39 minutes and the hand-off both ways is clean, but the exit E5 does not measure the day's pattern and reuses the Stone Bay stream picture. |
| 23 | courses/science-grade-2/u02-3/d023.md | Application, assessment (observe) | Content and keys are right and the minutes fit, but the stems name which records are fast and which are slow, so the child never has to tell them apart. |
| 38 | courses/science-grade-2/u03-3/d038.md | Respond | Sound, workable repair-and-retry day with correct keys; weak points are shared shapes between repair and retry, group time for four letters, and one loose science picture. |
| 49 | courses/science-grade-2/u05-1/d049.md | Application | Fits 38 minutes, safe apart from the handwashing gap; the exit mostly copies from the picture and is built on the day's own cup trio. |
| 65 | courses/science-grade-2/u06-1/d065.md | Respond | Keys and science are right, timing adds to 35; "all touch" on class-only cards cannot be recorded for 24 of 30 children, and the food-not-help idea is tested but barely taught. |

## Findings, most serious first

Severity: FIRM / SOFT / TEMPLATE. "Gate?" = would a script gate have caught it.

| Day | Severity | Kind | What is wrong | Exact fix | Stage that made it | Gate? |
|---|---|---|---|---|---|---|
| 5 | FIRM | exit-goal | s01-X5 asks the child to pick the page that does not fit "water always lies between hills". That claim is not in the day; the day's pattern is "water runs down and collects low, the shapes differ". The answer is found by matching the words "between hills", so the exit never tests the revised model. | Replace Pip's claim in X5 with one the day's pattern decides, for example Pip says "water always collects in a hole in the ground". Show two new invented pages, one low flat place where water stands and one hilltop with no water, and ask which page does not fit. Update items.csv, wrongs.csv, cards-exits-5-7.md and the day. | data (items.csv X5) then kit | no |
| 5 | FIRM | rule4 | X5's second page, "a stream running between two hills", is the Stone Bay picture taught in the day (page 1 of place-cards-day5). The exit also shares its shape with practice P5-2 (Pip says a claim, test it against pages). | Draw the exit pages from new places (a pond with no outlet, a spring on a slope) and make the question a different shape, for example "draw where the water in this new place would collect". | data and kit | no |
| 23 | FIRM | exit-goal | E1 says "Use A and B to explain a fast land change" and E2 says "Use C and D to explain a slow land change". The stems also give the conclusions ("hot melted rock added a mound", "farther inland", "little by little"). The child only repeats the stem, and the plan's skill (mark which is fast and which is slow) is never asked. It also contradicts the directions line "Name no record as the right one" and the at-home "give no hint about which record". | Reword E1 to "Look at records A to D. Which two records show a fast change, and how do you know?" and E2 to "Which two show a slow change?". Strip the conclusion words from the item stems (keep them only in the packet captions, and make one caption ambiguous). Then E3 can ask for labelling the two routes. | data (items.csv E1, E2) | no |
| 23 | SOFT | key-on-child-page | packet-day23.md ends with a "## Key (teacher)" section and sits in the "Per child" print line. The gate's key-line pattern is `key:` and does not see "Key (teacher):", so it passes. | Move the key into key-packet-day23.md (the key- prefix is already skipped, as days 8 and 37 do) and print only the packet. | kit | no (pattern gap) |
| 23 | SOFT | words | The student page prints three long stems (128 words of questions, 140 words of student page against a 150 cap) for a grade where "children read little or not at all". The stems carry a before/after story each. | Print only the three asks as short labels ("Fast: A and B", "Slow: C and D", "My model") and keep the story in the teacher read-aloud. | day (student page) | partly (word cap, only just under) |
| 23 | TEMPLATE | other | DEFAULTS and the items gate want `path: spoken`, but this is a 20-minute silent, independent packet for about 30 children with no group talk. Only six can be scribed (3 minutes), so 24 answers must be written or drawn on paper. | Allow `path: paper` or `drawn` for an observe day with a written packet in K to 2 (a spoken answer is still accepted for any child); mark the answer collected on the record sheet from the papers. | template (items.csv path rule) | yes, that is the gate |
| 23 | SOFT | timing | The part says "Mark six look-fors on one scale" during the 20 minutes. That is 180 marks while 30 children work and six are being scribed. Marking must happen after class from the papers (about 20 to 30 minutes), which the day does not say. | Add a "Marking" line (after class, from the papers; the six scribed children marked live). | day | no |
| 38 | SOFT | rule4 | The retries and the repair set share a shape item for item: a (dent or no dent) with repair group A, b (same color, bends differently) with group B, d (fixed lamp or moved lamp) with group D, e, g, h (compare two readings, pick the one that bends more or stays more level) with groups F and G. A child can answer by copying the repair's move. | Keep one repair shape and make the retry a different shape (for example a, ask "which test shows hardness: pressing or looking?"; g, ask a child to draw the wet mark of a strip that took in more). Retries are unscored, so this is a softening, not a stop. | day, kit (repair-set, retry-cards) | no |
| 38 | SOFT | timing | "Repair by letter groups" gives group E with F, G and H 3 minutes of teacher time for four letters (and group A with B covers three hand-back sources in 3 minutes). Children with F, G or H wait for the letter "most children made". | Name which letter is repaired first and give the other letters a picture-directions card they do alone; or move group E, F, G, H to a 4 minute turn and group C to 2. | section plan and day | yes (plan.py repair-slot check), but it counted 3 minutes and passed |
| 38 | SOFT | exit-goal | The retries are touch answers on class-copy cards, "a child marks or says only the card on their feedback form". With about 30 children and 8 cards, the teacher cannot see or record 30 touches in 45-second pauses, and the second half of the goal (explain the revised hat choice) has no item: only three children answer aloud, while the student page asks every child to write "The hat keeps the doll dry because". | Print the eight retry cards as a per-child half page with a circle-it box so each child marks their own; mark the written student-page lines against the two look-fors (names a test, names what was not tested). | day, kit | no |
| 38 | SOFT | content | Card c (X38c) shows water "flowing, thickening, nearly set, holding its shape" as it cools. Plain water does not thicken as it cools: it stays liquid and then freezes. The picture would teach slush or gel. | Draw the four pictures as liquid water, water with ice crystals forming, mostly ice, solid ice block, and name them ("cooler, still cooler"). | kit (retry-cards-day38.md) and data (X38c stem) | no |
| 38 | SOFT | words | UK spellings: "colour" (card b title, repair group B title and key), "favourite" (repair set E, errors.csv E, "Colour tells only the colour"). | colour to color, favourite to favorite in the retry cards, repair set and errors.csv. | kit and data | partly (spelling) |
| 38 | SOFT | other | wrongs.csv tags "Strip Q, because it is rough" with error B (same color shares every property); the note says "nearest letter". The child's slip is not B. | Tag it with no letter (x) with the note "sorted by one feature, ask which strip bent", as the plan allows. | data (wrongs.csv) | no |
| 38 | SOFT | other | Before class asks the teacher to write 30 feedback forms from days 35 to 37 (plan: "60 minutes of marking, ours, untested"). A teacher with no prep time cannot do this. | Print a fill-in form with the letter and the one next step as tick boxes, or let the record sheet's error letters print the step. | section plan | no |
| 49 | SOFT | safety | The safety field says "Wash hands after soil and plants" and the clean-up part wipes goggles, tables and hands with one damp cloth a table and defers washing to "the next washing time". Wiping soiled hands with a shared cloth is not handwashing; DEFAULTS asks clean-up to have supplies and minutes. | Either schedule the wash (two sinks, five children at a time during the exit and clean-up: name it as 5 minutes and say so) or say "hands are washed straight after, at the room's sink, table by table" and give each table its own cloth. | section plan and day | no |
| 49 | SOFT | rule4 | The exit's cups A, B, C are the day's own trio (sun and water, dark, dry) with B dark and dry at once. That is the very contrast the return-and-repair part teaches (dark cup beside dry cup). X49b asks a child to draw leaves and stem already drawn in the stem ("two green upright leaves"), so it is copying. | Make the exit a new factor pair (for example heat or soil) or ask the child to write the starting record line for a plant described only by a picture (height read at the ruler, leaves counted) so the picture is not pre-written. | data (items.csv X49a, X49b) | no |
| 49 | SOFT | exit-goal | "All draw on the ticket" and "all show 1, 2 or 3 fingers": the print line has exit cards per class and no child ticket for X49b. The teacher can mark only the three or six who say why. | Print a per-child exit ticket (X49b box) and have each child draw or circle; add it to the print line. | day (print line) and kit | no |
| 49 | SOFT | words | Day 48 names the cups "healthy, no-light and no-water plant", day 49 says "healthy, dark, dry" (the ledger lists "dark plant, dry plant" as first taught day 49 on an Application day). Two words for one idea. | Keep one set of names across days 48 to 51 (the same words on the planning chart, the cup cards and the student page). | section plan | no |
| 49 | SOFT | content | "The day before, the adult grows the radish plants, matches their size, dampens the soil": radish seedlings need about a week from sowing. The unit plan says pre-grown. | Say "Seven days before, sow radish seeds; the day before, choose three matched seedlings and dampen the soil." | day | no |
| 49 | SOFT | source | No sources.csv row backs "plants need light and water" or the seedling test; the safety sheet spells "mould". | Add a teacher-reference row (a university extension or government plant page, `checked: 2026-11-22`); mold in US spelling. | data (sources.csv) and kit | no |
| 65 | SOFT | exit-goal | The exit asks "all touch" on class-only cards (print: "Per class: exit cards"), 0.5 minute each, and only six say why. The teacher cannot see or mark 30 touches, so 24 children have no record. The bat card is also a per-class card that each child "draws from". | Add a per-child exit half page (three part cards to circle, food or help to circle) and a bat card for each table; keep the six rotating for talk. | day (print line) and kit | no |
| 65 | SOFT | rule4 | X65b ("why did the moth go to the flower?", food or to help the plant) is the day's consensus question and the answer of repair group C and the bat key. X65a rebuilds the day 62 model (felt body, yellow dots, receiving patch) and has the same shape as repair group B (fix the part so the model delivers). | Use a new case for X65b (a hummingbird at a feeder-shaped flower, or a beetle) and change X65a to "draw the part that is missing" instead of "touch the part to move". | data (items.csv X65a, X65b) and kit | no |
| 65 | SOFT | ladder | The idea "an animal visits a flower for food, not to help the plant" is said once (one clause in d060, the Tell) and then tested on day 65. The ledger lists nectar as "first taught day 65 (bat card and exit)", on a Respond day where nothing is taught as new. Error C is anticipated for day 62 but no day 60 to 62 item tests it. | Add a 2-minute "why does the bee visit" look to day 62 (or 61) with the term nectar, and add the same words to the ledger row on that day. | section plan | no |
| 65 | SOFT | words | "Receiver" is a grade 1 word (the end of a message) and here means the receiving patch on a flower; the day and cards say "receiving patch" and "receiver" interchangeably. | Name the part "receiving patch" everywhere and drop "receiver" from the cards, or say once that it is a new use of the word. | section plan and kit | no |
| 65 | SOFT | source | Pollen carried by bees and hooked burrs have no sources.csv row (rows exist for the bat, U9, and the jay, U10). The "not every plant needs an animal" line has none. | Add one museum or government page for bee and pollen and one for burdock or hooked seeds, `checked: 2026-11-22`; a refused page is kept as "browser check". | data (sources.csv) | no |
| 65 | SOFT | handoff | At home the exit "[[X65a]] and [[X65b]], your child answers alone" needs the moth and the three part cards, which exist only on the class set. | Add a drawn swap: "draw a moth, a flower and a patch", or leave the item out of At home. | day | no |
| 65 | SOFT | timing | The consensus (4 minutes) dictates and writes six claims and answers the burr and bee question, citing days. | Cut to four claims (the other two come from the repair sets) or give it 5 minutes taken from clean-up. | day | no |
| 5 | SOFT | ladder | "Not every river reaches the ocean" is taught in u01-1 day 3 (ledger, with the "ocean at the page edge" wording). Day 5 says "Say it plainly: not every river reaches the ocean" as if new, and the ledger lists the day 5 term line as review of days 1 to 3 without it. | Say "In day 3 we saw a river ends where the land is lowest. Today Dry Ridge shows it ends in a lake" and add that review to the ledger. | day | no |
| 5 | SOFT | words | Dry Ridge's page reads "a gully runs down to a lake", while P5-2, the day and the key say "stream" and Pip's claim is about "rivers": the page has no river. | Change the Dry Ridge page to "a stream runs down to a lake" and Pip's claim to "every stream goes to the ocean", or reword P5-2 to "river". | kit (place-cards-day5.md) and data | no |
| 5 | SOFT | ladder | The exit uses "pond" and "cliff"; "pond" is first taught on day 6 (ledger) and "cliff" is never taught. | Use the day's own words (a lake or a bay) or add "cliff" to the Words line. | data | no |
| 5 | SOFT | words | "grey braids" in the Dry Ridge picture note is UK spelling. | gray. | kit | partly |
| 5 | SOFT | source | The real-world fact "not every river reaches the ocean" (Dry Ridge) has no row in sources.csv beyond U1 (downhill, collects low). | Add a USGS or encyclopedia page that says some streams end in an inland lake (closed basin), `checked: 2026-11-22`. | data (sources.csv) | no |

Hand-off, read both ways (all five days): day 4 to 5, day 22 to 23, day 37 to 38, day 48 to 49, day 64 to 65 each name the same error letters and the same opening repair slot as the next day's handbacks.csv rows. No break found.

Timing sums checked (children about 30): d005 39 minutes (the six at 30 s = 3 inside the 12; pairs 20 s each = 4); d023 35 minutes (six scribed at 30 s = 3 inside 20); d038 35 minutes (4 x 3 + 3 = 15; 8 cards at about 60 s = 8 of 10); d049 38 minutes (set up 1 + 5 + 1 + 4 + 2 = 13; six at 20 s = 2); d065 35 minutes (4 x 2.5 + 2 = 12; six at 30 s = 3; six at 15 s = 1.5). All parts fit as written; the doubtful points are in the table.

Keys reworked by hand: every exit and end item key on all five days. All hold. Checked against a source: Mount St. Helens eruption case (USGS rows, day 12) and the bat nectar and jay acorn facts (U9, U10, nps.gov and the Forest Service). Judged only: landforms, plant needs, bee and burr facts, the water-freezing picture, and the stiffness, hardness and bend readings (no source row).

Browser check: none. I opened no page, so no source was added or changed; the source rows above are for a later pass.

## Ladder

What the grade gap caused:

- **Day 5 and the grade 1 and kindergarten words.** The day uses grade 2's own u01-1 words (hill, hollow, river, lake, ocean, key box) as review and names the grade 1 map and key. It treats "not every river reaches the ocean" as new when day 3 already taught it, and tests "pond" and "cliff" that day 6 teaches.
- **Day 23 and u02-1.** It rests on day 12's Mount St. Helens case (eruption, fast change) and day 13's "words that say when". The review claim is true in the written day 12 and 13. The exit does not use the lower unit's case, but it names which records are fast and slow, which day 12 had children decide.
- **Day 38.** The retries use the unit's own taught set (dent, bend, lamp, water climb, ledge drop). The review claim "days 30 and 31" holds in the written days 30 and 31 (water passes, water does not). Nothing from a lower grade is assumed that was not taught.
- **Day 49.** Uses the kindergarten and grade 1 "fair test" and "needs of plants" ideas as review (ledger rows exist for both). It does not name them as review in the day, and the grade 2 words for the cups shift between days 48 and 49.
- **Day 65.** "Receiver" re-uses a grade 1 word for a different idea (message end, here a flower patch). The food-not-help idea was meant to be taught on days 60 to 62 and is present only as one clause.

Did this grade use the lower grades well? Mostly yes: the grade 2 units carry their own earlier days forward and name them in the leans_on lines, and grade 1 seedling cases come back as reminders, never as exits. The weak spots are two terms (pond, nectar) tested before or without being taught, and two review claims that are not named as review (days 5 and 49).

## Counts

| Day | FIRM | SOFT | TEMPLATE |
|---|---|---|---|
| 5 | 2 | 5 | 0 |
| 23 | 1 | 3 | 1 |
| 38 | 0 | 7 | 0 |
| 49 | 0 | 6 | 0 |
| 65 | 0 | 7 | 0 |
| All | 3 | 28 | 1 |

(The 16 plan.py "not in data/units.csv" lines are a registration gap in data, not counted per day.)

## Fixes applied (2026-11-22)

Cleanup job for science-grade-2 at grade close. Lines are day, outcome, what changed.

FIRM findings
- Day 5, exit-goal: applied. The exit job's rejection did not hold here: Pip's "between hills" claim was never in the day, and the answer was found by matching words. s01-X5 is now a new case (Maple Hill: rain on a hill that slopes to a meadow with one hollow); the child draws where the rain water runs and where it stops. New key, steps, samples, three wrongs rows (arrow up, E; water alone, D; water spread on the meadow, no letter), handbacks row (Talk), cards-exits-5-7 card, days.csv exit line, d005 Tomorrow, d006 talk line, and the s01.md and u01-2.md plan rows synced.
- Day 5, rule4: applied. The same fix: no Stone Bay picture and a new shape (draw, not "which page does not fit").
- Day 23, exit-goal: applied. s02-E1 and s02-E2 no longer give the conclusion or count ("Which of them show a fast change, and what tells you?"; same for slow); the packet task lines, Directions (step 1 now reads all four records) and the at-home lines match. Record captions are unchanged: they carry the taught cue words, so an ambiguous caption was not added (left).

SOFT findings
- Day 23, key-on-child-page: applied. Key moved to key-packet-day23, named in the print line, leans_on and Before class.
- Day 23, words: partly. The two stems and the packet tasks are shorter; the student page still prints the stems.
- Day 23, timing: applied. A Marking line says the six scribed children are marked live, the rest after class from the papers.
- Day 23, TEMPLATE (path: spoken for a silent packet): left for the lead.
- Day 38, rule4: left (retries are unscored; a new retry shape needs new cards). Timing (group E to H): left. Exit-goal (per-child retry cards): left. Feedback forms before class: left (section plan).
- Day 38, content (card c): applied. The four pictures are now liquid water, ice crystals forming, mostly ice, a solid ice block.
- Day 38, UK spellings: applied in the retry cards, repair set, unit 3 opener and errors.csv (color, favorite).
- Day 38, wrongs tag: applied. "Strip Q, because it is rough" is now no letter, note "sorted by one feature; ask which strip bent".
- Day 49, safety: applied. The clean-up wipes tables and spills only; hands are washed at the room's sink straight after, each table with its own cloth.
- Day 49, content (radish timing): applied. "Seven days before, sow radish seeds; the day before, choose three matched radish plants."
- Day 49, "mould": applied (mold in the safety sheet). Source row: left (no page opened). Rule4, exit-goal (per-child ticket), words (cup names across days 48 to 51): left.
- Day 65: all seven SOFT findings left (per-child exit half page, new case for X65b, a day 62 nectar look and ledger row, "receiver" wording, bee and burr sources, at-home swap, consensus minutes). They need new cards or earlier-day edits.
- Day 5, ladder (not every river reaches the ocean): applied. d005 now says day 3 showed a river ends where the land is lowest. Ledger row for the lead.
- Day 5, words (gully, stream): applied. Dry Ridge now has a stream (page and picture note); P5-3 sample says stream.
- Day 5, pond and cliff: applied by the new exit (neither word appears). "grey braids" to gray: applied. Source (closed basin): left, no page opened.

Key lines in pieces (all child-printed pieces under courses/science-grade-2/ checked against each day's print line)
- Moved to a key piece and named in Before class, print line and leans_on of each day that prints the piece (38 pieces): cards-exits-1-4, frozen-water-places, water-places, cards-exits-5-7, packet-day9, cards-exits-11-15, fast-cards-day12, marsh-hill-day13, slow-cards-day14, path-cards-day15, bare-strips-day16, slope-card-day16, cards-exits-16-20, cards-exits-21-22, packet-day23 (new key-packet-day23), packet-day24, packet-day25, repair-set-day26, retry-packet-day26, grip-pictures-day34, evidence-cards-day35, hook-pictures-day39, stiff-floppy-strips, leaf-photographs-day43, paper-photographs-day43, evidence-cards-day44, argument-records-day46, repair-set-day47, plan-cards-day48, corn-cards-day51, oat-cards-day53, retrieval-card-day63, retrieval-cards-day66, pond-and-forest-cards-day68, desert-and-shore-cards-day69, wet-and-dry-pair-days-71-73, scenes-day72, hedge-and-dune-cards-day73 (each as key-<name>.md in its unit folder).
- Left (56 pieces, all listed only under "Per class" in every day that prints them: retrieval, repair, retry and exit-picture cards the teacher holds, shows or reads aloud): the Key (teacher) lines stay. If the lead wants class-shown exit pictures also split, the same script pattern applies.
- Already separate: key-packet-day8, key-retry-packet-day10, key-packet-day37, key-plan-sheet-day54, key-puppet-record-day55.

Gate counts (filtered, FAIL lines in the whole output)
- plan.py check, science-grade-2: before 72 FAIL lines (270 items, 334 wrong answers, 16 failures); after 72 FAIL lines (270 items, 336 wrong answers, 16 failures). All are the known "section ... is not in data/units.csv" lines and shape-note template points; no new failure.
- lesson.py check, courses/science-grade-2/: before 0 FAIL; after 0 FAIL (two intermediate runs showed word-cap and handback-wording fails from my key sentences and edits; fixed by compact key lines and trims).
