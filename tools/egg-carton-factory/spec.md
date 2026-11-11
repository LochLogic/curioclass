# Egg Carton Factory

## One idea
Every egg order must go in one rectangular carton with no empty cups: drag the carton's edge to change the rows and
the eggs re-pack at once, so each carton that fits is a factor pair, past the square carton every fit is one you
already have turned, and a prime order only ever fits one long row.

## Not like
- equal-groups-zoo (gr 3, sandbox, concept): builds equal groups and arrays to find a product or quotient (meaning of multiplication). Here the total is fixed and the question is which rectangles exist at all; no division word problems.
- tile-the-floor (gr 3, puzzle, concept): covers a given room with tiles for area. Here the count is fixed and the shape is free; no area, no units.
- garden-grid (gr 2, builder, concept): splits a given bed into rows and columns and counts. Here you search for every rectangle a number makes and decide prime or composite.
- factor-forge (gr 6, arcade, built): breaks numbers into prime factors on an anvil, GCF and LCM, a timed rush. Here no factor trees, no primes multiplied together, no timer: only factor pairs, multiples and prime or composite, with a warm daylight shed look (factor-forge is dark forge orange).
- growth-spurt (gr 4, simulator, concept): packs seedlings into trays and asks what a remainder means. Here a leftover only ever means "not a multiple"; no remainder interpretation.
- area-model-builder (gr 4, sandbox, concept): slices rectangles at place-value breaks to multiply. Here rectangles are never split; the eggs re-deal into rows.
- pattern-painter (gr 3, mystery, concept): colors a 10 by 10 multiplication-table mural by rules. Here the 1 to 100 board colors only numbers the student has fully packed, by prime or composite.
- box-packer (gr 5, puzzle, concept): unit cubes in 3D for volume. Here flat cartons and a fixed count.

## Who and how
Grade 4 math, module math-4-factors-and-multiples. Driver: students (solo by default) or teacher on a projector.
15 to 35 minutes. Standard: 4.OA.B (4.OA.4: factor pairs for 1 to 100, a number is a multiple of each of its
factors, whether a number is a multiple of a one-digit number, prime or composite). No personal prompts. Gus, the
farm, and the orders are made up; the Rush card footer says "Gus's farm and orders are made up for practice."
Role: lesson. Change note (spec fix, 2026-11-10; the tool is built, so the code follows this spec later): Rush shift 5,
"From the shelf", was added: three cards where the student uses a known factor pair or factor list to say which
carton sizes an order fills, with no bench and no line to run, and finishes the factor and multiple sentences.
Before this, "a number is a multiple of each of its factors" was only printed on the seal card. Nothing else changed.
Rush goes from 12 cards to 15.
- Change note (hooks, 2026-11-11): Added the three hooks (spec only; the tool is built, so the code follows later): six items on your own with the end screen by part, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. The words factor, factor pair, multiple, prime and composite each show on a stamped carton the first time they are used.

## Standards map
| Code part | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.OA.4 factor pairs | Pack Station: change the rows until every carton for the order is on the shelf; Rush shifts 1 and 4 (Every shape, no live preview) | eggs re-deal into the rows; a fit stamps "4 by 9" onto the shelf; a turned fit flies to its twin; the turn line after the square or last pair | Rush 1a (12) ships only with 1 by 12, 2 by 6, 3 by 4 on the shelf; shipping with two of them plays shipMissing |
| 4.OA.4 multiple of each factor | Rush shift 5 (From the shelf): from a packed carton or a factor list, pick the sizes the order fills, type how many cartons, and finish "7 is a ___ of 56. 56 is a ___ of 7."; also seal an order in Pack Station, then tap a factor chip to run that order on the Fill Line | the seal card "36 is a multiple of each factor: 1, 2, 3, 4, 6, 9, 12, 18, 36"; the chip opens Fill Line, where every carton fills | after sealing 36, tapping chip 4 runs 36 in cartons of 4: 9 full cartons, counter "4, 8, ... 36", fillYes |
| 4.OA.4 multiple of a one-digit number | Fill Line: pick a carton size 2 to 9 (also 10 and 12) and run the order; Rush shift 3 (pick the sizes that fill, type how many cartons) | cartons fill one after another with a skip-count; the last carton full or showing empty cups | Rush 3a (72; sizes 6, 5, 8) passes only with 6 and 8 picked and counts 12 and 9 |
| 4.OA.4 prime or composite | Pack Station seal reads prime, composite or neither; Rush shift 2 (sort three orders, a composite needs a proof carton); Rush 4c (pick every prime in a decade) | the board cell turns gold (one long row only), blue (more shapes) or gray (1); the Composite bin refuses an order without a fitting carton of 2 or more rows | Rush 2a (13, 21, 27) passes only with 13 in Prime and 21, 27 in Composite; 27 in Prime plays missOdd |

## Screens and modes
Header: title, mode buttons **Pack Station**, **Fill Line**, **Order Board**, **Rush Orders**, then kit Motion,
Sound, Read. Gus's portrait sits at the top of the panel in every mode (hidden at 680x425).

On load: Pack Station, order 36. The eggs are already in a 5-row carton: 7 full columns, 1 egg in column 8, its 4
empty cups ringed in dashed red; readout "5 rows: 7 full columns, then 1 egg in the next. 4 cups empty." Nothing
plays before the first tap. Hint: "Drag the carton's bottom edge to change the rows. No empty cups allowed." The
first tap on the edge handle starts the drag (the main path); a first tap on Rows - or + changes the rows at once.
The welcome (wPack) queues after a first tap with no line of its own and may be cut (rule 16); its premise (one
carton, no empty cups) is in the hint and Read.

**Pack Station** (explore). Focus: the carton, centered in the stage, drawn in code over pulp texture, cups up to
56 px (cup = the smaller of stage width / columns, carton area height / rows, 56). The order sign (painted, number in
code) hangs top left; the hen sits at the top right corner of the carton area; the shelf runs along the bottom of
the stage (6 slots wide, fits the most shapes any order up to 100 has). Controls: the drag handle on the carton's
bottom edge (36 px of drag per row, whole rows, 1 to 12; arrow keys up and down when focused), panel **Rows -**,
**Rows +**, the order box with **Order -**, **Order +** (1 to 100) and a typed box, **Next order** (cycles the starter
list in Content). The eggs re-deal at every row change: they fill column by column, top to bottom, so only the last
column can be short. Readout under the carton (Content wording). A fit: chime, the hen's cluck pose for 0.6 s, the
carton's "rows by columns" label stamps, and a copy slides to its shelf slot (smaller side first). A fit whose rows
are more than its columns is a turn: the copy flies to its twin, which glows with "same as 4 by 9, turned". Once the
rows reach the square or pass the last pair, a dashed turn line appears on the shelf after the last slot. When every
pair is on the shelf the order seals: the panel shows the seal card (factor list, shape count, verdict) and factor
chips; the board cell colors. **Reset order** clears this order's shelf.

**Fill Line** (explore). Focus: the pallet of carton slots filling, center of the stage (10 slots a row, up to 5
rows, about 80 px each), under a belt along the top with the egg stream. Panel: the order box (same controls, shared
with Pack Station), carton size buttons **2, 3, 4, 5, 6, 7, 8, 9, 10, 12**, each drawn as its little carton (layouts in
Content), **Run the line**. Run: cartons fill one at a time, 0.25 s each, the whole run capped at 4 s (100 in cartons
of 2 is 50 cartons in 4 s); the big counter skip-counts the full cartons ("6, 12, 18 ... 72"). The end card shows the
result (Content). A tap on any size, order control or Run during a run restarts at once with the new setting. Motion
off shows the end state at once.

**Order Board** (explore). Focus: a 10 by 10 board of 1 to 100, filling the stage (cells 60 px at 1366x768).
Blank cells are pulp; a sealed order (from Pack Station or a Rush card) colors: gold with a one-row icon (prime),
blue with dots for its shape count (composite), gray with one egg (1). Square numbers carry a small square-carton
mark once sealed. Panel: counter "Packed 23 of 100: 9 prime, 13 composite, and 1", a legend, and the line "Saved on
this device only." Tap a blank or colored cell: Pack Station opens with that order. There is no button that fills the
board for you.

**Rush Orders** (the puzzle levels). Five shifts of three cards (Content), a shift pager and dots per card. Each card
gives two Ships: a first miss plays its reason and resets the card (nothing marked); a second miss plays shown, Gus
does it, and the card counts "Gus helped". Leaving Rush (or switching card) re-rolls an unshipped card to another
variant, preferring the variant with the fewest numbers already sealed on the board. The board and the seal card are
never on screen in Rush. Counter in the panel: "Orders shipped 5 of 15 (4 on your own)".
- From the shelf cards (shift 5): the stage shows one stamped carton label or one factor list and nothing else: no
  bench, no belt. The card lists three sizes with a Fills toggle and a count box each, as on Multiples cards, then
  two sentences with a word slot each and two word chips, **factor** and **multiple**, which can each be used more
  than once. Card 5c shows two sizes that both filled and three orders to choose from.
- Every shape cards: the stage is the Pack Station bench without live re-dealing: set rows, tap **Pack**; the eggs
  roll in; a fit joins the shelf as usual. **Ship it** when you think the shelf is complete. No empty slots show.
- Sort cards: three order tags in a tray above the bench, three painted crates below labeled in code **Prime: one
  long row**, **Composite: more shapes**, **Neither**. Tap a tag to load it on the bench (rows and Pack as above), then
  tap a crate. Composite accepts a tag only when this card's bench has packed that order in a fitting carton of 2 or
  more rows (else proofHow plays and the tag stays). **Ship it** once all three are placed.
- Multiples cards: the order and three carton sizes; each size has a **Fills** toggle and a count box ("how many
  cartons") that opens when toggled. No bench, no belt. **Ship it** when ready.
- Decade card: a strip of the nine numbers between two tens; tap a number to load it on the bench; each has a
  **Prime** toggle. **Ship it**.
A shipped card: the farm truck drives off with it (1.5 s; Motion off: it is gone at once), the next card opens. A
shift done plays shiftDone.

What the picture shows for every outcome: fit: all cups full, label stamped, hen clucks; short column: dashed red
rings on the empty cups and their count; rows more than the order (for 5 eggs in 7 rows): one column, the empty cups
below; turn: the twin glows; seal prime: the one carton on the shelf is the long row, the board cell gold; seal 1:
one egg in one cup, gray cell; Fill Line multiple: every carton full, green check on the last; not a multiple: the
last carton with empty cups ringed red.

1366x768: header 52 px; stage left about 900 px, panel right about 440 px; the carton, shelf, Rows buttons, order
box and every Rush control (crates, toggles, Ship it) sit above the fold. A long row (1 by 100) uses the full stage
width with 8 px cups drawn as code ovals (sprites below 16 px are code ovals). 680x425: stage and panel stay side by
side, panel 250 px; the shelf becomes a list of labels ("1 by 36"); Gus's portrait and the hen hide; Fill Line slots
shrink to 40 px; the board cells to 36 px with 12 px numbers.
**On your own.** Six items with no carton, no board colors, no live preview, no hints, one answer each. Nothing is marked until all are in.

**Results strip (on the end screen).** For the teacher: for each part of 4.OA.4 (factor pairs, multiples, prime or composite), how many of its items on your own were right, in numbers and words, with each item missed and the answer the child gave. It prints with the rest.

## Content
Starter orders (Next order cycles): 36, 12, 13, 24, 1, 30, 49, 72. Order 30 adds the tag "Real egg flats hold 30
eggs, 5 by 6."

Pack readouts: fit "4 rows of 9 = 36. Fits!"; short "5 rows: 7 full columns, then 1 egg in the next. 4 cups empty.";
more rows than eggs "7 rows: 5 eggs in 1 column. 2 cups empty."
Seal card: "36: 5 carton shapes. Factors: 1, 2, 3, 4, 6, 9, 12, 18, 36. 36 is a multiple of each one. Composite: more
than one shape." Square orders add "6 by 6 uses one number twice, so 9 factors make 5 shapes." Prime: "13: one long
row only. Factors: 1 and 13. Prime." Order 1: "1: one egg, one cup. Its only factor is 1, so 1 is neither prime nor
composite." Factor chips 2 to 10 and 12 open Fill Line; others are plain labels.

Fill Line carton layouts (rows by columns): 2 (1 by 2), 3 (1 by 3), 4 (2 by 2), 5 (1 by 5), 6 (2 by 3), 7 (1 by 7),
8 (2 by 4), 9 (3 by 3), 10 (2 by 5), 12 (2 by 6). End cards: "72 eggs: 12 full cartons of 6. 72 = 12 x 6, so 72 is a
multiple of 6, and 6 is a factor of 72." and "70 eggs: 17 full cartons of 4, then 2 eggs in the last one. 70 is not a
multiple of 4."

Rush shifts (three variants per card; answers):
- 1a Every shape: 12 (1x12, 2x6, 3x4); 20 (1x20, 2x10, 4x5); 18 (1x18, 2x9, 3x6).
- 1b Every shape, squares: 16 (1x16, 2x8, 4x4); 25 (1x25, 5x5); 9 (1x9, 3x3).
- 1c Every shape: 30 (1x30, 2x15, 3x10, 5x6); 28 (1x28, 2x14, 4x7); 40 (1x40, 2x20, 4x10, 5x8).
- 2a Sort: 13, 21, 27 (P, C 3x7, C 3x9); 17, 39, 25 (P, C 3x13, C 5x5); 11, 37, 49 (P, P, C 7x7).
- 2b Sort: 2, 9, 31 (P, C 3x3, P); 1, 19, 57 (Neither, P, C 3x19); 2, 23, 51 (P, P, C 3x17).
- 2c Sort: 91, 97, 87 (C 7x13, P, C 3x29); 77, 79, 93 (C 7x11, P, C 3x31); 89, 69, 81 (P, C 3x23, C 9x9).
- 3a Multiples: 72 in 6, 5, 8 (6: 12, 8: 9; 5 no); 48 in 6, 9, 8 (6: 8, 8: 6; 9 no); 84 in 4, 6, 9 (4: 21, 6: 14; 9 no).
- 3b Multiples: 70 in 4, 7, 5 (7: 10, 5: 14; 4 no); 90 in 4, 6, 9 (6: 15, 9: 10; 4 no); 54 in 4, 6, 9 (6: 9, 9: 6; 4 no).
- 3c Multiples: 91 in 7, 3, 9 (7: 13; 3, 9 no); 78 in 3, 6, 9 (3: 26, 6: 13; 9 no); 96 in 7, 8, 9 (8: 12; 7, 9 no).
- 4a Every shape: 60 (1x60, 2x30, 3x20, 4x15, 5x12, 6x10); 72 (1x72, 2x36, 3x24, 4x18, 6x12, 8x9); 84 (1x84, 2x42, 3x28, 4x21, 6x14, 7x12).
- 4b Every shape: 96 (1x96, 2x48, 3x32, 4x24, 6x16, 8x12); 100 (1x100, 2x50, 4x25, 5x20, 10x10); 90 (1x90, 2x45, 3x30, 5x18, 6x15, 9x10).
- 4c Decade: 41 to 49 (41, 43, 47); 61 to 69 (61, 67); 81 to 89 (83, 89). Odd composites in them: 45, 49; 63, 65, 69; 81, 85, 87.
- 5a From a carton: "Gus packed 56 eggs as 7 by 8." Sizes 7, 8, 6 (7: 8 cartons, 8: 7; 6 no); 63 as 7 by 9, sizes 7, 9, 8 (7: 9, 9: 7; 8 no); 42 as 6 by 7, sizes 6, 7, 8 (6: 7, 7: 6; 8 no). Sentences: "7 is a factor of 56. 56 is a multiple of 7."
- 5b From a factor list: "45 has factors 1, 3, 5, 9, 15, 45." Sizes 9, 5, 6 (9: 5, 5: 9; 6 no); 32 with 1, 2, 4, 8, 16, 32, sizes 4, 8, 6 (4: 8, 8: 4; 6 no); 50 with 1, 2, 5, 10, 25, 50, sizes 5, 2, 4 (5: 10, 2: 25; 4 no). Sentences: "45 is a multiple of each of its factors. 9 is a factor of 45."
- 5c Which order: "Cartons of 6 all filled. Cartons of 9 all filled. Which order was it?" 54, 48 or 63 (54); sizes 4 and 7: 28, 42 or 49 (28); sizes 8 and 3: 24, 32 or 27 (24). Then type both carton counts (54: 9 and 6; 28: 7 and 4; 24: 3 and 8) and finish "54 is a multiple of 6 and of 9."
Card prompts for shift 5: "No bench this time. Use the carton Gus packed. Which sizes will fill?"
Card prompts: "Find every carton for 12 eggs. Then tap Ship it."; "Sort these orders. A composite needs a carton
that proves it."; "Which cartons will 72 eggs fill with no gaps? Type how many cartons."; "Mark every order from 41 to
49 that only fits one long row."
- On your own, with what each common wrong answer means:
  - Factor pairs: "Type every factor pair of 48." (1 x 48, 2 x 24, 3 x 16, 4 x 12, 6 x 8.) "Which of 4, 6 and 8 are factors of 54?" (6 only.) Leaving out 3 x 16 means the child only tries facts from the times tables; picking 4 means 54 was judged by its last digit.
  - Multiples: "Is 84 a multiple of 7?" (Yes, 12 sevens.) "Is 58 a multiple of 4?" (No.) A no for 84 means the child stops at 7 x 10.
  - Prime or composite: 37 (prime); 51 (composite, 3 x 17). Calling 51 prime means "odd and not in the tables" is being used as the test.

## Interactions in detail
- Rows 1 to 12 in every order (12 lets 36 show the turns 9 by 4 and 12 by 3). Any order up to 100 has its smaller
  side at 10 or less, so every pair is reachable.
- Re-deal: Motion on, eggs slide to their new cups in 250 ms; a new row change during it jumps to the new state at once.
- A fit already on the shelf (same rows and columns) only glows; it is not added twice.
- Seal happens the moment the last missing pair is packed, in any order of tries. Sealing a sealed order again does nothing new.
- Order box: typed values outside 1 to 100 snap to the nearest end with "Orders run 1 to 100." Changing the order keeps the rows and re-deals.
- Fill Line with order below the size (5 in cartons of 6): one carton, 1 cup empty, "not a multiple".
- Rush Every shape: Pack with rows that do not fit shows the short column for 1 s, then the eggs roll back (no penalty, no count). Ship it is disabled until at least one carton is on the shelf.
- Rush Sort: a tag in a crate can be tapped back to the tray. Ship it is disabled until all three are placed. Neither accepts any tag (checked on Ship).
- Rush Multiples: a count box takes whole numbers 1 to 99; Ship it is disabled while a toggled size has an empty box.
- Rush Decade: Ship it is enabled at once (a strip with no primes is never asked, but the student may ship any set).
- Reasons on a miss (first matching): Sort: an odd composite in Prime missOdd; 2 not in Prime missTwo; 1 not in Neither, or another number in Neither, missOne; otherwise missOther. Multiples: a wrong Fills set missFill; right set with a wrong count missCount. Decade: an odd composite marked missOdd; a prime left out missLeft. Every shape: shipMissing.
- Saved on this device (localStorage, try/catch): sealed orders, Rush progress. "Saved on this device only." shows on the board and the Rush counter. **Start over** on the board clears everything after a confirm.
- Access: every action works by tap and by keyboard. Rows, order and size controls are buttons that work by tap and by key; chips can be dragged, or picked with a tap and placed with a tap. Board cells carry the words prime, composite or neither with their color. Motion can be paused.
- On your own: one answer each, no feedback until the sixth is in.

## Look
Paper `#fbf7ef`, ink `#2a2118` (14.79:1), muted `#62574a` (6.59:1). Accent `--brand #44691a` meadow green (5.99:1 on
paper, white on it 6.4:1): mode buttons, Pack, Ship it, the turn line. Prime gold `#e9b43a` fill with ink text
(8.32:1) and a `#7a5a00` outline (5.97:1 on paper), since gold on paper alone is 1.78:1; composite blue `#2f5f9e` with
white text (6.46:1); one gray `#d9d2c7` with ink (10.53:1). Empty-cup ring `#b23a2a` dashed (5.56:1 on paper, 3.65:1 on
pulp), always with the count in the readout, so color is never the only signal; board cells also carry their icon.
Pulp `#cfcac2` cartons, ink on pulp 9.69:1. Different from factor-forge (dark forge, orange and gold), skate-park-angles
violet, roller-coaster-rounding teal and estimation-station freight red.

## Art
- shed-bg: a warm farm packing shed interior in morning light, plank walls, a window, a steel conveyor belt along the bottom, an empty wooden workbench in the middle; 16:9; no cutout; no people; Pack Station and Fill Line backdrop.
- pulp-texture: gray molded paper pulp, full frame, soft even light; 1:1; no cutout; clipped to code-drawn cartons, cups, crates' labels and blank board cells.
- egg-brown, egg-white: one egg upright seen from slightly above, soft shadow; 1:1; cutouts; sprites in cups 16 px and up (alternating by a fixed pattern).
- order-sign: a hanging chalkboard sign on two chains, wooden frame, blank dark face; 4:3; cutout; top left in Pack Station and Rush (number in code).
- hen-calm, hen-cluck: a red-brown hen standing calm, and the same hen mid-cluck with wings out; 1:1; cutouts; top right of the carton area.
- gus-portrait, gus-thumbs, gus-point, gus-shrug: Gus, a farmer about 55, warm brown skin, gray stubble, a canvas cap, a denim work apron over a plaid shirt; head and shoulders smiling, thumbs up, pointing to the side, a friendly shrug; 3:4; cutouts; people: true. Panel avatar (portrait); thumbs on a ship, point on shown, shrug on a miss.
- crate: an empty wooden farm crate seen from the front, plain blank slat face; 4:3; cutout; the three Sort bins (labels in code).
- pallet: a wooden shipping pallet seen from above at an angle; 16:9; no cutout; under the Fill Line slots.
- truck: a small farm delivery truck from the side with a blank cargo panel; 16:9; cutout; Rush ship animation.
- board-wood: a smooth painted wooden board surface, full frame; 1:1; behind the Order Board grid.
Drawn in code: cartons and cups, the shelf, turn line, readouts, Fill Line cartons, the board grid and cells, toggles.
14 images. Each cutout shows whole in every mode where it appears (the hen and Gus hide at 680x425 rather than crop).

## Voice
Bank voice `friendly-dad` (Achird): he is Gus. Style line: "Say in a relaxed, friendly way, like a kind farm shed
boss showing a kid the ropes." Not used by any close neighbor (skate-park-angles big-sister, roller-coaster-rounding
upbeat-guide, estimation-station gravel-ranger; the others are unbuilt; factor-forge has no recorded voice).
`Curio.voice`, scope = mode + Rush card id. No line carries a number, so all are recordable; readouts and cards are
read on screen and Read speaks the hint plus the card (browser voice for numbers). Welcomes and hows are `how`.
- wPack (how, Pack welcome; stale once a carton has sealed): "I'm Gus. Every order goes in one carton with no empty cups. Drag the carton's edge to change the rows."
- fitHow (how, first fit): "That one fits, so it goes on the shelf. Try other rows to find every shape."
- turnHow (how, first turn): "That's a carton you already have, just turned. Once the rows pass the columns, every fit is a turn."
- sealComp (event, every composite seal): "That's every carton. More than one shape, so it's composite."
- sealPrime (event, every prime seal): "Only one long row fits. That order is prime."
- sealOne (event, sealing 1): "One egg, one cup. One has just one factor, so it's neither prime nor composite."
- wFill (how, Fill Line welcome): "Pick a carton size, then tap Run the line. If the last carton fills up, it's a multiple."
- fillYes (event, every full run, whole): "Every carton is full. It's a multiple of that size."
- fillNo (event, every short run, whole): "The last carton has empty cups. Not a multiple."
- wBoard (how, Order Board welcome): "Every order you finish colors its number. Tap a number to pack it."
- wRush (how, Rush welcome): "Rush orders get harder each shift. Read the card, then work it out."
- everyHow (how, first Every shape card; needs Pack): "Set the rows and tap Pack. When the shelf has every shape, tap Ship it."
- sortHow (how, first Sort card): "Tap an order to load it. Then tap its crate. Composite needs a carton that proves it."
- proofHow (event, a tag tapped onto Composite without proof; once per tag): "Pack it in a carton with more than one row first."
- multHow (how, first Multiples card): "Turn on each size that fills with no gaps, type how many cartons, then tap Ship it."
- decadeHow (how, first Decade card): "Mark every order that only fits one long row, then tap Ship it."
- shipRight (event, whole): "Shipped. Right on time."
- shipMissing (event, whole): "Not every shape yet. Try the rows you skipped."
- missOdd (event, whole): "Odd doesn't mean prime. One of those has another carton. Try more rows."
- missTwo (event, whole): "Two only fits one long row. It's the one even prime."
- missOne (event, whole): "Only one goes in Neither. It has just one factor."
- missFill (event, whole): "One size is off. Think about the last carton for each."
- missCount (event, whole): "The sizes are right. Check how many cartons."
- missLeft (event, whole): "You missed one that only fits a long row."
- missOther (event, whole): "Not quite. Check each order again."
- shown (event, whole): "Here's how I'd pack it. Watch."
- shiftDone (event, whole): "Shift done. The truck's loaded."
How lines play once, then live in the hint. Each miss reason plays once per miss. No line names a disabled control:
everyHow needs Pack, and its hint keeps "tap Ship it" for when Ship it enables; multHow and decadeHow need Ship it
enabled or name it only as the last step once boxes are filled (hint text updates when it enables).
- how `own`: "Six more on your own. No hints this time."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Every shape (1a to 1c, 4a, 4b) | try every row from 1 to 12, then ship; mash Ship it; ship after one carton; read the shelf slot count; use Pack Station's live preview, then return | trying rows in order is the standard's own method (a systematic factor search), so it is the skill, not a bypass, and the seal-free shelf still has to be judged complete; Ship it with a missing pair is a miss, two misses mark "Gus helped"; no empty slots show; leaving Rush re-rolls the card to another variant |
| Sort (2a to 2c) | everything in Prime; everything in Composite; odd means prime; guess bins (1 in 27); the count of primes per card; elimination after a miss | Composite accepts only an order with a packed fitting carton of 2 or more rows, so placing a composite needs a found factor; all-in-Prime fails on every card (each has a composite); odd composites (21, 27, 39, 25, 33, 49, 9, 57, 51, 91, 87, 77, 93, 69, 81) fail with missOdd; cards hold 1 or 2 primes and one holds 1, so no fixed count; a miss resets all three with nothing marked, and a fix still needs a proof carton |
| Multiples (3a to 3c) | guess the Fills set (1 in 8 per try); even means fills cartons of 4 (70, 90, 54); type the order or the size as the count; run the line in Fill Line and copy | counts must be exact (12, 9, 10, 14 ...), never the order or a shown size (checked); every card has a "no" size; 70, 90, 54 in 4s each leave 2 and fail with missFill; leaving Rush re-rolls; no belt or bench on the card |
| Decade (4c) | mark all odd numbers; mark none; guess (1 in 512); the board | odd composites 45, 49; 63, 65, 69; 81, 85, 87 fail with missOdd; none fails with missLeft; the board is never on screen in Rush, and the variant prefers numbers not yet sealed |
| From the shelf (5a to 5c) | guess the Fills set (1 in 8); type a number on the card as the count; try both chips in each slot (1 in 4); in 5c pick the biggest or the first order | counts must be exact and Ship it checks toggles, counts and both word slots together, so a blind try is about 1 in 32 and two misses mark "Gus helped"; every card has a "no" size; in 5a the right count is the other number of the pair, which is the point (56 = 7 x 8, so 8 cartons of 7), and the word slots and the "no" size still need the idea; in 5c each wrong order is a multiple of exactly one of the two sizes (48 and 63; 42 and 49; 32 and 27), and the right order is the biggest once, the smallest twice and never in a fixed position |
| Seal and board colors | none (no check) | they appear only after the student has packed every pair; there is no fill-for-me button |
| Rush counter "on your own" | let Gus show every card; replay a shipped card | shown cards count shipped, not on your own; each card counts once |
| Pack Station, Fill Line | none (explore, no checks) | their answers can't be carried into Rush, which re-rolls on return |
| On your own | Retry until right; lean on the hints | One answer each, no hints or models, and nothing is marked until all are in. |

## Heard in order
Grade 4: not every action speaks, but a result lands before the next card.
1. Load, first tap on the carton edge: the drag starts; wPack queues after the tap (may be cut, rule 16). Next action in the hint: "Drag the carton's bottom edge to change the rows."
2. First fit: chime, then fitHow (waits for wPack if it is playing). First turn: turnHow. Seal: sealComp, sealPrime or sealOne after the stamp lands.
3. Fill Line: wFill on entry; a run plays no speech until its end, then fillYes or fillNo (whole); a restart drops it unspoken.
4. Rush, first card of each kind: wRush, then everyHow / sortHow / multHow / decadeHow. Ship: shipRight (whole) plays before the truck leaves and the next card opens; a miss reason (whole) plays before the card resets; a second miss: shown (whole), then Gus's fill animation.
5. Shift end: shipRight, then shiftDone (whole) before the next shift's first card.
No line contains a number or a bare letter; numbers are on screen and spoken by Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| Find all factor pairs for 1 to 100; a number is a multiple of each of its factors; multiple of a one-digit number; prime or composite (4.OA.4) | CCSS Math 4.OA.B.4 (corestandards.org) | Illustrative Mathematics grade 4 unit "Factors and Multiples" | yes |
| A prime has exactly two factors, 1 and itself; a composite has more than two | Wikipedia, "Prime number" | Math is Fun, "Prime and Composite Numbers" | yes |
| 1 is neither prime nor composite | Wikipedia, "Prime number" (primality of one) | Math is Fun, "Prime and Composite Numbers" | yes |
| 2 is the only even prime | Wikipedia, "Prime number" | Math is Fun, "Prime Numbers" | yes |
| A search for factor pairs can stop once the smaller factor passes the square root (pairs repeat turned) | Wikipedia, "Trial division" | Math is Fun, "Factors and Multiples" (finding factor pairs) | yes |
| Egg flats hold 30 eggs in 5 rows of 6 | Miller Manufacturing, "Egg Flats 30 count 5 x 6" product page | Little Giant 12-Pack Egg Flats (Blain's Farm and Fleet listing): 5 x 6 flat holds 30 eggs | yes |
Cut: "a standard carton is 2 rows of 6" (Wikipedia gives 10 or 12 eggs but no layout; no second layout source found),
so Fill Line's carton layouts are labeled the shed's own cartons, with no real-world claim.

Number checks (Python, run 2026-11-06): factor pairs of every order used (1 to 100 starters and all 27 Rush variants
listed in Content); most shapes up to 100 is 6 (60, 72, 84, 90, 96), so a 6-slot shelf always fits; largest smaller
side up to 100 is 10, so rows 1 to 12 reach every pair; every Sort label (prime, composite with a proof pair,
neither) and every card has a composite; primes in each decade (41 43 47; 61 67; 83 89; 97) and the odd composites
beside them; every Multiples size with quotient and remainder (70, 90, 54 in 4s each leave 2; 91 = 7 x 13), and no
correct count equals the order or a shown size; readout example 36 in 5 rows (8 columns, 4 empty); cup sizes at
1366x768 (1 by 100: 8.2 px; 6 by 6: 56 px; 10 by 10: 43 px); Fill Line run times (72 in 6s 3.0 s; 100 in 2s capped
4 s); guess odds (Sort 1/27 by bins and blocked by proof; Multiples 1/8 sets plus exact counts; Decade 1/512);
contrast ratios in Look.

Number checks for the spec fix (Python, run 2026-11-10): 56 = 7 x 8, 63 = 7 x 9, 42 = 6 x 7 and 6, 8, 8 do not divide
them; 45, 32 and 50 with their listed factors and counts, and 6, 6, 4 do not divide them; in 5c 54, 28 and 24 are the
only orders divisible by both sizes, and each wrong order is divisible by exactly one.
Checks run for the items on your own (Python, 2026-11-11): 48 = 1 x 48 = 2 x 24 = 3 x 16 = 4 x 12 = 6 x 8; 54 / 6 = 9, 54 / 4 and 54 / 8 leave remainders; 84 = 7 x 12; 58 = 4 x 14 + 2; 37 has no factor from 2 to 6; 51 = 3 x 17.

## Done when
1. Focus: in every mode the carton, pallet, board or Rush bench is the biggest central thing, and at 1366x768 every control the mode needs (Rows, order box, sizes, Run, crates, toggles, Ship it) is above the fold; at 680x425 stage and panel stay side by side.
2. On load the 5-row carton shows 4 ringed empty cups; dragging to 4 rows stamps "4 by 9", chimes and adds it to the shelf; 9 rows makes 4 by 9 glow "turned" without a new slot.
3. Packing 1, 2, 3, 4 and 6 rows for 36 seals it with the factor list and "composite"; 13 seals after 1 row with "prime"; 1 seals as neither; each colors its board cell.
4. A tap while anything plays acts at once: a row change mid re-deal jumps, a size tap mid-run restarts the line, a mode switch stops the truck.
5. Fill Line: 72 in cartons of 6 shows 12 full cartons and plays fillYes; 70 in 4s shows the last carton with 2 empty cups and plays fillNo.
6. Rush 1a (12) ships only with three shapes; a two-shape ship plays shipMissing; a second miss shows Gus and counts "Gus helped".
7. Rush 2a: 21 cannot enter Composite until a 3-row (or 7-row) carton is packed; 27 in Prime plays missOdd.
8. Rush 3a passes only with 6 (12) and 8 (9); 5 toggled plays missFill; 6 with count 72 plays missCount.
9. Rush 4c (41 to 49) passes only with 41, 43, 47; marking 49 plays missOdd.
10. The board and seal card never show in Rush; leaving Rush with a card open re-rolls it.
11. Voice: each how line speaks once in five repeats; ship and miss lines speak every time and finish before the next card; no line names a disabled control.
12. Rush 5a (56 as 7 by 8) ships only with 7 (8 cartons) and 8 (7 cartons) on, 6 off, and the sentences reading "7 is a factor of 56. 56 is a multiple of 7."; no bench or belt shows on shift 5 cards; the counter reads "of 15".
13. Six items on your own run with no model or hint, one answer each; the end screen shows the result by code and the items missed. (4.OA.4)
14. Every spoken instruction is also on screen, and each key word shows with a picture or example at first use.
15. Every action works by keyboard as well as tap, drags have a tap way, nothing is shown by color alone, and motion can be paused.

## Open questions
none
