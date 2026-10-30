# Punctuation Power-Ups

## One idea
Every mark is a power-up with one test it must pass (a semicolon needs a full sentence on both sides, a colon needs a full sentence before it, a dash pair needs words you could lift out), so a wrong mark doesn't just cost time: the race stalls and shows the exact test that failed on the exact words, and the last heat changes the right answer by switching the style guide.

## Not like
- comma-chameleon (ela 5, puzzle, not specced): one comma changes a picture's meaning. Here the marks are semicolons, colons and dashes between clauses, each checked by a named test, in a race.
- pause-and-break (ela 6-8, puzzle, not specced): a reading voice pauses where the punctuation says. Here nothing is read aloud; the point is the grammar test behind each mark and speed with accuracy.
- usage-panel (ela 11, roleplay, spec): debates contested usage with no right answers and a year slider of style guides. Here every gate has an answer under the chosen guide, and the guides are today's editions, side by side.
- parallel-parking (ela 9, puzzle, this group): reshapes words; no marks, no clock.
- editors-in-the-margin (ela 9-12, studio, this group): spelling and hyphens inside a whole essay, with reasons. Here spelling is two quick pit stops per heat.

## Who and how
- Grade 10 ELA. Module: Semicolons, Colons and Style (Language).
- Driver: students on laptops, alone; pairs can race the same ghost. 15 to 30 minutes (a heat takes about 1 to 4 minutes; students rerun to beat their ghost).
- Standards: L.9-10.2 (capitalization, punctuation and spelling): 2a semicolons, with and without a conjunctive adverb, in Heat 1; 2b colons to introduce a list or quotation in Heat 2; 2c spelling in the pit stops. L.9-10.3 (apply knowledge of language; write and edit to conform to a style manual): Heat 4, Style sheet, and the guide notes on every gate.
- tool.json: driver "students", minutes "15-30", modes ["Race", "Practice lap", "Rule book"], grades_label "Grade 10". Kit starter plus `kit:theme-912`.

## Screens and modes
Header: title "Punctuation Power-Ups", small line "Every mark has a test."; mode buttons **Race** (opens first), **Practice lap**, **Rule book**; Motion, Sound, Read. Panel: `#hint`, heat picker **1 Semicolons**, **2 Colons**, **3 Dashes**, **4 Style sheet**, the style guide picker (Heat 4 and Rule book only) **Chicago 18**, **APA 7**, **MLA 9**, **AP**, best time per heat, **Clear best times** (asks Yes / No).

### Race (opens first)
Focus: the sentence card with its glowing gap, centered over the track and the largest text on the stage; the power-up tray sits right under it. The track is a thinner band below.
- Stage, lower band: a painted night raceway backdrop (Art) with a lane of gates drawn in code over it, 12 gates in Heats 1 to 3 (10 sentence gates and 2 pit stops) and 8 gates in Heat 4 (no pit stops). The runner is a painted hover craft cutout (Art); the ghost of the best run is the same cutout at 40 percent in the next lane. A clock reads tenths of a second (`mm:ss.s`). A streak meter shows tiers 0 to 3 with chevrons.
- **Start** begins the clock. The craft glides toward gate 1, and gate 1's sentence card drops in above the track at once with one or two glowing gaps (a caret ^ under each). The card above is always the next closed gate's sentence.
- Power-up tray under the card, five buttons with glyph and name: **;** Semicolon, **:** Colon, **--** Dash (drawn as one long bar, see Look), **,** Comma, **∅** No mark. Keys 1 to 5. For two-gap sentences the student fills the first gap, then the second.
- The tray is live the whole time, gliding or not. Right: the marks snap into the gaps at once, the gate opens, a short "Pass: two full sentences" line flashes under the card, the next card drops in, and the streak rises a tier. The craft flies through open gates without stopping and stops at the first closed one. Higher tiers make the glide between gates shorter (2.0, 1.4, 0.9, 0.6 seconds).
- Wrong: the craft swaps to its stalled cutout and stops where it is for 1.5 seconds, the streak drops to 0, 3 seconds are added, and the failed test appears on the words themselves: the clause before the gap is boxed and labeled, for example "'The supplies are' can't stand alone, so a colon can't follow it." The tray stays live during the stall; the wrong mark greys out, and a right mark tapped during the stall passes at once (the stall still costs its time).
- Accepted alternatives: some gates take two marks (Content). Either passes; the flash says "Pass. A dash works too; the colon is more formal."
- Pit stops: the craft pulls into a painted pit bay (Art) and the card shows a word with one tile missing its spelling ("acco__odate"); three spellings on buttons. Right passes; wrong stalls like a wrong mark and shows the correct spelling with its tricky part bold.
- After the last gate: the finish card with time, the ghost's time, the difference, marks right first try ("9 of 12"), and a list of gates missed with their test. **Run again**, **Practice this heat**. A new best becomes the ghost. No confetti; the clock just turns the brand color.

### Practice lap
Focus: the sentence card, centered, with the test result under it. No clock, no ghost, no streak, no track. Each gate shows a **Test it** button: tap a mark and the tool runs its test on the words before choosing ("Semicolon test: 'Because the road was icy' is not a full sentence. Fails."). The student can test every mark before committing. **Next gate** and **Back**.

### Rule book
Focus: the open mark card. One card per mark (semicolon, colon, dash, comma between clauses), each with its test in one line, two examples from the heats and a "When guides differ" table for the chosen guide (Content). A card for spelling lists the six pit-stop words with their tricky parts.

### Heat 4, Style sheet
- Before the heat starts, the guide picker must be set (it opens as a card: "Pick the guide your class uses."). Gates here offer the choices in Content (for example **,** or **∅**; **c** or **C**; **closed** or **spaced** dash). The answer depends on the guide; the pass line names it: "Pass under AP: no comma before 'and' in a simple series."
- **Same sentence, other guide** on the finish card replays the heat under another guide so students see which gates flip.

## Content
All sentences are original, written for Curio Class. In this spec "--" stands for the dash the tool draws. Each gate: sentence with ^ at the gap; accepted marks; the test line shown on a wrong mark.

### Tests (shown on a wrong mark)
- Semicolon: "A semicolon needs a full sentence on both sides (or separates list items that already have commas)."
- Colon: "The words before a colon must be a full sentence."
- Comma splice: "Two full sentences can't be joined by a comma alone. Use a semicolon, or add 'and', 'but' or 'so'."
- Dash pair: "Words between two dashes must lift out and leave a full sentence."
- No mark: "The sentence needs a break here."
- Introductory clause: "'Because ...' can't stand alone, so it takes a comma, not a semicolon."
- Colon purpose: "A colon promises that what follows explains, lists or quotes what came before. These words just come next."
- Dash between two sentences: "A dash can join two sentences for a sudden turn, but these two balanced sentences want a semicolon."
- Missing comma before a joining word: "Two full sentences joined by 'and', 'but' or 'so' take a comma before the joining word."
- Every wrong mark shows the test that fits it; the gate data names which test each wrong mark gets.

### Heat 1: Semicolons
1. "The power went out at noon ^ the generator kicked on a minute later." Accept ; .
2. "The trail was steep ^ however, the view from the top was worth it." Accept ; .
3. "We packed water and a paper map for the long hike ^ and we left the trailhead before sunrise." Accept , . (Semicolon fails: "With 'and' joining two full sentences, a comma is enough.") The first clause has no commas inside on purpose: Chicago allows a semicolon before 'and' when the clauses already hold commas, and this gate should have one answer.
4. "The tour stops in Boise, Idaho ^ Reno, Nevada ^ and Fresno, California." Accept ; at both gaps.
5. "Mia studied for three weeks ^ therefore, she felt ready." Accept ; .
6. "The library opens at nine ^ the cafe opens at seven." Accept ; .
7. "Because the road was icy ^ the bus took the long way." Accept , .
8. "I wanted to go to the game ^ but I had a shift at work." Accept , .
9. "The experiment failed twice ^ nevertheless, the class learned something each time." Accept ; .
10. "The team lost the first game ^ they won the next four." Accept ; .
Pit stops: "sep_rate" (separate / seperate / seperete; tricky part "par"), "nece_ary" (necessary / neccessary / necesary; "one c, two s").

### Heat 2: Colons
1. "You need three things for the lab ^ goggles, gloves and a notebook." Accept : .
2. "The supplies are ^ goggles, gloves and a notebook." Accept ∅ .
3. "The sign gave one instruction ^ keep the gate closed." Accept : . (Capitals after colons wait for Heat 4.)
4. "Lincoln ended with a hope ^ \"that government of the people, by the people, for the people, shall not perish from the earth.\"" Accept : .
5. "The coach said ^ \"Run it again.\"" Accept , . (Colon fails: "'The coach said' isn't a full sentence, so a colon can't follow it. A comma introduces the quotation.")
6. "Her goal was simple ^ finish the race without walking." Accept : and -- .
7. "We visited ^ the museum, the park and the old mill." Accept ∅ .
8. "The recipe calls for ^ flour, eggs and milk." Accept ∅ .
9. "There was only one problem with the plan ^ nobody had a key." Accept : and -- .
10. "The report listed three causes of the flood ^ heavy rain, a blocked drain and an old levee." Accept : .
Pit stops: "defin_tely" (definitely / definately / definitly; "finite in the middle"), "occu_ence" (occurrence / occurence / ocurrence; "two c, two r").

### Heat 3: Dashes
1. "The answer ^ if there is one ^ is in chapter four." Accept -- at both, or , at both; pass line for commas: "Commas work; dashes make the break louder."
2. "Three cities ^ Lima, Quito and Bogota ^ sit high in the Andes." Accept -- at both. (Commas fail: "The inside list already has commas, so commas around it blur where it starts and ends.")
3. "She opened the box and found ^ nothing." Accept -- and ∅ ; the pass line for ∅ says "Correct and plain. The dash adds a beat of surprise." (Colon fails: "'She opened the box and found' isn't a full sentence.")
4. "My brother ^ who never reads ^ finished the book in a day." Accept , at both or -- at both.
5. "Honesty, patience and humor ^ these are what make a good coach." Accept -- .
6. "We could take the bus ^ or we could walk." Accept , .
7. "The test is on Friday ^ study the vocabulary first." Accept ; .
8. "The old bridge ^ built in 1890 ^ still carries traffic every day." Accept , at both or -- at both.
9. "The plan had one flaw ^ it needed a key." Accept : and -- .
10. "The crowd went silent ^ then everyone cheered." Accept -- and ; .
Pit stops: "acco_odate" (accommodate / accomodate / acommodate; "two c, two m"), "embar_ass" (embarrass / embarass / embaras; "two r, two s").

### Heat 4: Style sheet (answers per guide: Chicago 18 / APA 7 / MLA 9 / AP)
1. "We brought tents, stoves ^ and lanterns." Choices , / ∅. Chicago , ; APA , ; MLA , ; AP ∅.
2. "The answer was obvious: ^e should take the bus." Choices w / W. Chicago w ; APA W ; AP W ; MLA see note.
3. "The room went quiet ^ then everyone laughed." Choices closed dash / spaced dash. Chicago closed; APA closed; MLA closed; AP spaced.
4. "Bring a pencil, an eraser ^ and a calculator." Same as 1.
5. "She had two choices: ^he bus or the train." Choices t / T. All guides t (what follows is not a full sentence).
6. "One fact stood out: ^he river had risen four feet overnight." Choices t / T. Chicago t ; APA T ; AP T ; MLA see note.
7. "Our team ^ the one in red ^ scored first." Choices closed / spaced at both. As 3.
8. "The menu offered soup, salad ^ or a sandwich." Same as 1.
- MLA note: gates 2 and 6 under MLA 9 use the colon rule in the MLA Handbook, 9th ed.; the builder fills it from the handbook. If the rule can't be confirmed from the handbook or the MLA Style Center, those two gates are skipped under MLA with the line "Check your MLA Handbook for this one", and the flip counts under MLA drop those gates. Neither sentence after a colon is a rule or a formal statement, so no guide's exception for those applies.
- Rule book "When guides differ" table: serial comma (Chicago, APA, MLA use it; AP leaves it out of a simple series); capital after a colon before one full sentence (Chicago lowercase; APA and AP capital; MLA from the handbook); dash spacing (Chicago, APA and MLA closed; AP a space on each side).
- Curio Class's own pages leave out the serial comma (the tool's other heats follow that house style); the Rule book says so in one line: "This tool's own sentences follow a house style without the serial comma."

## Interactions in detail
- Each gate is data: `{text, gaps:[{accept:[...], tests:{mark: line}}], passLine:{mark: line}}`. A gate with two gaps passes only when both are right; the first right gap stays placed after a wrong second.
- Clock: starts on Start, stops when the last gate opens; it is wall time plus 3 penalty seconds per wrong mark (the 1.5 s stall is wall time). Glides only cost time when the student answers faster than the craft flies, so the streak matters most to fast, accurate racers. Times save per heat (and per guide for Heat 4) in localStorage `punctuation-power-ups:v1` (try/catch) with the ghost's per-gate splits. Clear best times asks first.
- Ghost: replays the stored splits; if none, the lane is empty with "No ghost yet."
- Keyboard: 1 to 5 choose marks, Enter starts and continues, Esc pauses (the clock stops and the card blurs so the sentence can't be read while paused).
- Motion off: the craft jumps gate to gate; times are the same (glide times still count) so ghosts stay fair.
- Sizes: at 680x425 the card, the tray and the lane fit without scrolling (the lane shrinks to a thin progress strip under 500 px tall, the backdrop hidden, the craft a small chip on the strip). At 375 wide the tray becomes a row of five 56 px buttons under the card and the lane a strip. No horizontal scroll.
- Sound: a short rising tone on a pass, a low thud on a stall (`Curio.tone`), off with Sound.

## Look
- Accent `--brand #ff4fd8` (power-up magenta: header rule, streak chevrons, Start, the finish time) on the kit `theme-912` base. The painted raceway sits under a `#10161f` wash at 55 percent so lane lines `#2b3646` and gate outlines in `--line` read on it; gates fill brand when open. Mark glyphs in the tray are large (28 px) in `--ink`; the dash is drawn as a 1.6 em bar so it can never be confused with a hyphen.
- Failed-test boxes use `--warn #ffb8a8` outlines with the test in words; passes use `--ok #6fdca6` with "Pass" in words.
- Contrast (WCAG 2.1): brand on panel #141b25 6.07:1, on sec-bg 5.75:1; brand-ink #1c1203 on brand 6.47:1; theme ink on panel 14.7:1; warn and ok as in theme-912. The clock and streak sit on a solid `--panel` chip, never directly on the painting.
- Different from ELA 9-12 neighbors (shakespeare-remix lavender, portrait-in-four-media coral, tone-dial orchid #f29ff0 at dE 38, source-mixer cyan, usage-panel ink red on dark) and this group. The nearest accent in 9-12 ELA is idea-threads magenta #ff6fd0 (dE 18), not a neighbor and a light-text explorer; this one is pinker and sits on a race track.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere, house style "sleek futuristic racing game art, night, glowing magenta and teal trim, clean painted look". 4 images.
- ppu-raceway: a long empty hover-racing track at night seen from the side, a smooth dark road band across the lower half, glowing trim lights along its edges, a distant city skyline under a dark sky; 4:1; cutout no; people no; the backdrop of the Race track band, behind the code lane and gates.
- ppu-craft: a small sleek one-seat hover racing craft seen from the side, rounded nose pointing right, a closed tinted canopy, glowing magenta stripes and a soft blue glow underneath, plain white background; 16:9; cutout yes; people no; the runner (full color) and the ghost (same image at 40 percent opacity).
- ppu-craft-stall: the same hover racing craft seen from the side, nose dipped toward the ground, small sparks and a puff of grey smoke at its rear, its underglow flickering dim, plain white background; 16:9; cutout yes; people no; swapped in for 1.5 s on every stall.
- ppu-pit-bay: an empty brightly lit pit garage bay at a night race track, a tool cart, a tire stack and a blank wall panel; 16:9; cutout no; people no; shown behind the pit-stop card while the craft is in the pit.
Drawn in code: the lane, gates, clock, streak chevrons, sentence cards, tray glyphs and the drawn dash bar (controls and labels that change every moment).

## Voice
Bank voice `hero-coach`, style "Say with bright, encouraging energy, like a friendly coach at a time trial, kept short." The only 9-12 ELA tool with this voice; none of its neighbors or this group uses it. The kit voice queue (`Curio.voice`), `scope: () => state.mode + ':' + state.heat`. Sentences are never voiced (that would give away the pauses).
- w-race (how; on entering Race before Start; stale once Start is pressed): "Press Start. Then tap the mark in the tray that passes each gate's test."
- stall (how; the first wrong mark; stale when that gate passes): "Stalled. Read the box: it shows the test that failed. Tap another mark in the tray."
- pit (how; the first pit stop; stale when that pit stop passes): "Pit stop. Tap the right spelling."
- finish (event; every finish; stale on Run again or a mode change): "Finished. {n} of 12 right the first time." ({n} of 8 in Heat 4.)
- best (event; a new best time; stale on Run again or a mode change): "New best. That's your ghost now."
- w-practice (how; on entering Practice lap; stale once Test it is used): "No clock here. Tap a mark, then tap Test it to check it before you choose."
- w-rules (how; on entering Rule book; stale on a guide change): "Each card shows one mark's test. Pick a guide in the panel to see where guides differ."
- w-style (how; Heat 4 first opened, while the guide card shows; stale once a guide is picked): "Pick the guide your class uses. The right answer depends on it."
- flip (event; each Same sentence, other guide; stale on a mode change): "{n} gates flip under {guide}."

## Family engine
None.

## Sources
- Standards: CCSS ELA L.9-10.2 and L.9-10.3, https://www.thecorestandards.org/ELA-Literacy/L/9-10/.
- Semicolon, colon, dash and comma tests, and Chicago's serial comma, colon capitalization and closed em dash: The Chicago Manual of Style, 18th ed. (2024), chapter 6, "Punctuation"; cite section numbers at build.
- APA serial comma, capital after a colon before a complete sentence, closed em dash: Publication Manual of the American Psychological Association, 7th ed. (2020), chapter 6; confirm sections at build.
- MLA serial comma and dash form: MLA Handbook, 9th ed. (2021); colon capitalization only if confirmed (see Content).
- AP: no serial comma in a simple series, space on each side of a dash, capital after a colon when a complete sentence follows: The Associated Press Stylebook, current edition (name the edition and year on screen at build).
- Spellings: Merriam-Webster.com Dictionary entries for separate, necessary, definitely, occurrence, accommodate, embarrass.
- Lincoln quotation: Gettysburg Address, Bliss copy, https://www.loc.gov/exhibits/gettysburg-address/.
- Number checks (Python, 2026-10-29): Heat 4 flips from the answer table: Chicago to AP 7 of 8 (every gate but 5), Chicago to APA 2 of 8 (gates 2 and 6), APA to AP 5 of 8 (1, 3, 4, 7, 8), Chicago to MLA 0 of the gates MLA answers. Heat length: a race model with glides overlapping thinking time, 500 runs per case, gave 12-gate medians of 25 s (2 s per gate, no misses), 55 s (4 s, 10 percent wrong), 123 s (8 s, 25 percent wrong) and 238 s (15 s, 40 percent wrong); the old "2 to 5 minutes" was too long for most students and now reads "about 1 to 4 minutes". The fastest possible 12-gate run is 9.7 s of glides.

## Done when
1. Heats 1 to 3 run 12 gates and Heat 4 runs 8; every gate passes with its accepted marks and fails with each other mark, showing the listed test line.
2. Two-gap gates need both gaps right; a two-mark gate passes with either and shows the alternative line.
3. Clock math: with a fixed script of answers, the finish time equals the last pass's wall time minus Start plus 3 seconds per wrong mark (recompute from the log).
4. A new best is saved and replayed as the ghost; Clear best times asks first.
5. Heat 4 answers change with the guide; Same sentence, other guide reports the right number of flipped gates (Chicago to AP: 7 of 8, every gate but 5; Chicago to APA: 2 of 8, gates 2 and 6).
6. Practice lap's Test it runs the test without committing.
7. The dash is drawn as a long bar, never as a hyphen; no em dash character appears anywhere on screen (sentences, instructions, hints, Rule book).
8. Heat 2 gate 5 fails a colon with the colon test; Heat 3 gate 3 passes with the dash or no mark; Heat 1 gate 10 with a dash shows the dash-between-sentences line.
9. Focus: at 1366x768 and 680x425 the sentence card is the largest text on the stage, centered, with the tray directly under it; the track never pushes the card or tray below the fold.
10. A tap while the craft glides or stalls: a right mark tapped mid-glide opens the gate and shows the next card at once; a right mark tapped during a stall passes at once.
11. At 375 and 680x425 the card and tray are visible without scrolling; no horizontal scroll at any listed size.
12. Voice: the stall line is spoken once; later stalls only update the hint; the finish line is spoken every finish; all 4 images load and none shows a person.

## Open questions
None. Settled:
- The dash stays a drawn bar, never the em dash character (Cory's standing no-em-dash rule; the tool still teaches the mark).
- The MLA colon rule is a build-time fact check: confirmed from the handbook, or the two gates are skipped under MLA with the note (facts must be checkable).
- The house-style note stays: the wave rule says that where guides differ, the tool says so, and the tool's own sentences are one more example of a style choice.
