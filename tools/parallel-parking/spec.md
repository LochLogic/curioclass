# Parallel Parking

## One idea
A list in a sentence is a row of parking spaces, and the first car sets the shape of every space: each item can be reshaped (to swim, swimming, a swim, she swims) until it slides in flush, a mismatched car scrapes the one beside it with the exact mismatch named, and a row can be perfectly parallel and still bump the curb when the shape doesn't fit the words that come before it.

## Not like
- sentence-diagram-builder (ela 7, puzzle, not specced): snaps clauses into a sentence tree. Here there is no diagram; the test is whether list items match each other and the frame.
- grammar-garage (ela 4, puzzle, not specced): repairs broken sentences of many kinds. Here the only fault is a mismatch between parallel parts, and the lot also builds varied sentences in the Garage.
- rhetoric-spotter (ela 9, sort, spec): finds tricolon and anaphora in speeches to name persuasion. Here students build the parallel form themselves, and the one famous line (Lincoln) is a repair job, not a device to label.
- punctuation-power-ups (ela 10, race, this group): marks between clauses against a clock. Here the words change shape, there is no clock, and punctuation is placed for you.
- editors-in-the-margin (ela 9-12, studio, this group): revises a whole essay. Here one sentence at a time, with a small set of shapes per item.

## Who and how
- Grade 9 ELA. Module: Parallel Structure and Phrases (Language).
- Topic line: "parallel structure".
- Driver: students on laptops, alone or in pairs. 20 to 35 minutes (Lots 1 to 6 take about 20; the Garage 10 to 15).
- Standards: L.9-10.1 (command of standard English grammar and usage): 1a "use parallel structure" in Lots 1 to 6; 1b "use various types of phrases (noun, verb, adjectival, adverbial, participial, prepositional, absolute) and clauses (independent, dependent; noun, relative, adverbial) to convey specific meanings and add variety and interest" in the Garage, where every piece carries both its form and its job, work orders ask by both, and the clause count names independent and dependent clauses.
- tool.json: driver "students", minutes "20-35", modes ["Lots", "Garage"], grades_label "Grade 9". Kit starter plus `kit:theme-912`.

## Screens and modes
Header: title "Parallel Parking", small line "Make every item the same shape."; mode buttons **Lots** (opens first), **Garage**; Motion, Sound, Read. Panel on the right (stacked under the stage below 1000 px wide): `#hint`, the shape key, **Reset this sentence**, **Clear my progress** (asks Yes / No).

### Lots (opens first)
- Lot picker across the top of the stage: **1 Words and verbs**, **2 Phrases**, **3 Clauses**, **4 Pairs**, **5 Comparisons**, **6 Your lead**. Each lot holds 3 sentences, shown as "Sentence 2 of 3". All lots are open from the start (explore first); a lot's tab shows a small ✓ when all its rows are parked clean.
- Focus: the parking row of cars with any scrape tags, the biggest thing on the stage and centered in it, with the frame on the curb just above. The lot picker and Read it are smaller and sit at the edges.
- Stage: a top-down parking lot: painted asphalt (art: lot-asphalt) and a painted curb strip (art: lot-curb) along the top. The sentence's fixed words run along the curb as text drawn in code (the "frame"). Below it, one parking row: a space for each list item, with stall lines and the connecting words ("and", "or", "but also", "than") drawn in code on the asphalt between spaces.
- Each item is a painted car seen from above (art: car-mustard, car-teal, car-red, car-white; the lead is always car-mustard) with its words in code on a roof plate and a shape badge on the hood (glyph plus word): ◆ "-ing", ▲ "to + verb", ● "verb", ■ "noun phrase", ⬟ "clause", ✚ "prepositional phrase", ★ "adjective". The space it sits in is outlined in the lead car's shape (the same glyph painted on the asphalt).
- The lead car (first item) is locked in Lots 1 to 5, marked with a small padlock and the word "lead".
- **Reshape** (a wrench button on each unlocked car, or tap the car then press R or Enter): the car cycles through its forms (3 per item, listed in Content); the roof words and badge change; the car rolls back and parks again.
- When an item's shape differs from its neighbor's, the two cars touch and show a scrape (a jagged mark drawn between them) with a tag: "-ing next to to + verb". When a row's shared shape doesn't fit the frame, the whole row bumps the curb with the tag "Parallel, but 'should' needs a verb here".
- When every car matches and fits the frame, the row slides into line, the sentence prints in full under the lot ("Parked clean"), and **Next sentence** lights. No points, no timer.
- **Read it** (button under the row) shows the current sentence as plain text with mismatched items underlined, so a student can hear the problem in their head.

### Garage
- Focus: the base sentence on the chassis with its glowing hitch points, large and centered; the work order card sits right above it and the rack at the side.
- Stage: a painted garage bay (art: garage-bay) behind one base sentence on a car chassis in the middle (the chassis and pieces are drawn in code, because they stretch with their words), and a rack of trailer pieces along the side (10 or 11 per base), each a labeled block with two tags: its **form** (glyph and name: prepositional phrase, participial phrase, absolute phrase, appositive (a noun phrase), adjective phrase, adverb phrase, verb phrase, adverb clause, relative clause, noun clause, independent clause) and its **job** in this sentence (acts as a noun, acts as an adjective, acts as an adverb, main verb, stands alone), and its words.
- The base sentence's own parts are labeled too: its subject is a **noun phrase** and its main verb a **verb phrase** (small tags under the chassis), so every phrase type the standard names is on screen and in play.
- A **Work order** card above the bay (3 per base sentence, Content) asks for a meaning, then names the type: "Show what the bus looked like without a new main verb: add an absolute phrase."
- The student taps a piece, then taps one of the glowing hitch points (front, after the subject, end, or replace the subject), or drags it there. Each piece offers only the hitch points where it is grammatical (Content). Commas are placed automatically.
- The finished sentence prints under the chassis with each piece in its own type's underline style (dotted, dashed, double, wavy, solid, thick, boxed) and the type name in small type below it.
- **Check work order** compares the hitched pieces with the order: "Done: the absolute phrase paints the whole scene." or "This order wants an adverb clause: a piece that says when or why." Extra pieces are fine.
- **What it adds** card for the last piece tapped: one plain sentence about what that form does and one about its job here (Content).
- **Clause count** under the printed sentence: "1 independent clause, 2 dependent clauses: a complex sentence." It names simple, compound, complex or compound-complex as pieces are added.
- **Variety meter** in the panel: how many different forms the student has used across all three bases, of 11. It never says "low"; it reads "5 forms used".
- **Strip it** takes every piece off the current base.

## Content
All sentences are original, written for Curio Class, except the Lincoln line (Sources). Each item lists its 3 forms with shapes; the accepted form is in bold. "Frame shapes" are the shapes the frame accepts.

### Lot 1: Words and verbs
1. "The coach said the drill builds [speed], [ ] and [ ]." Lead **speed** (■, locked). Items: **agility** ■ / being agile ◆ / you get agile ⬟; it makes you strong ⬟ / **strength** ■ / to be strong ▲. Clean: "...builds speed, agility and strength."
2. "Before the trip, Ana had to [pack her bag], [ ] and [ ]." Lead **pack her bag** (●). Items: a phone charger ■ / **charge her phone** ● / charging her phone ◆; she found her ticket ⬟ / **find her ticket** ● / finding her ticket ◆.
3. "Lena enjoys [sketching birds], [ ] and [ ]." Lead **sketching birds** (◆). Items: to visit the shore ▲ / **visiting the shore** ◆ / the shore ■; she rides her bike ⬟ / **riding her bike** ◆ / a bike ride ■.

### Lot 2: Phrases
4. "You can get to the library [by bus], [ ] or [ ]." Lead **by bus** (✚). Items: **on foot** ✚ / walking ◆ / if you walk ⬟; **by bike** ✚ / biking ◆ / you could ride ⬟.
5. "The new bus schedule is [cheaper], [faster] and [ ]." Lead **cheaper**, second **faster** (both ★, locked). Item: it is more reliable ⬟ / **more reliable** ★ / reliability ■.
6. "The guide asked us [to stay with the group], [to keep our voices low] and [ ]." Leads ▲ locked. Item: not touching the paintings ◆ / **to leave the paintings alone** ▲ / the paintings are not for touching ⬟.

### Lot 3: Clauses
7. "The survey showed [that students sleep too little], [ ] and [ ]." Lead ⬟. Items: too much homework ■ / **that they have too much homework** ⬟ / having homework ◆; the early buses ■ / arriving early ◆ / **that the buses come too early** ⬟.
8. "The ranger explained [where the trail begins], [ ] and [ ]." Lead ⬟. Items: the length of it ■ / **how long it runs** ⬟ / running long ◆; **what we should carry** ⬟ / water and snacks ■ / carrying gear ◆.
9. "We chose the park because [it is close], [ ] and [ ]." Lead ⬟. Items: **it is free** ⬟ / free of charge ★ / costing nothing ◆; shade ■ / shady ★ / **it has shade** ⬟.

### Lot 4: Pairs (correlatives: the words after each half must match)
10. "The class can either [present on Friday] or [ ]." Lead ●. Item: **post a video** ● / posting a video ◆ / a video posted online ■. The asphalt between spaces reads "either ... or".
11. "The storm not only [closed the roads] but also [ ]." Lead ●. Item: the power went out ⬟ / **knocked out the power** ● / power outages ■.
12. "Good notes are both [short] and [ ]." Lead ★. Item: **easy to scan** ★ / they are easy to scan ⬟ / scanning easily ◆.

### Lot 5: Comparisons (compare like with like)
13. "[Biking] to school is faster than [ ]." Lead ◆. Item: to walk ▲ / **walking** ◆ / the walk ■.
14. "[To write a draft] is easier than [ ]." Lead ▲. Item: revising it ◆ / **to revise it** ▲ / revision ■.
15. "The new phone's battery lasts longer than [ ]." No lead car; the lead is the painted phrase "The new phone's battery" (■). Item: the old phone ■ (bumps: "Compares a battery with a whole phone") / **the old phone's battery** ■ / **the old phone's** ■. Both bold forms park clean; the tool notes "'the old phone's' leaves out 'battery' because it is understood."

### Lot 6: Your lead (no locked car; any shape the frame accepts parks clean)
16. "Our club's goals for spring are [ ], [ ] and [ ]." Frame shapes: ◆ ▲ ■. Items: raising money ◆ / to raise money ▲ / more money ■; planting trees ◆ / to plant trees ▲ / new trees ■; cleaning the creek ◆ / to clean the creek ▲ / a clean creek ■. Start forms: raising money, to plant trees, a clean creek. Three clean rows exist; after one is found, **Find another clean row** asks for a second. The tool says: "Parallel isn't one right answer. It's a match."
17. "The report says the town should [ ], [ ] and [ ]." Frame shapes: ● only. Items: fix the sidewalks ● / fixing the sidewalks ◆ / sidewalk repair ■; add bike lanes ● / adding bike lanes ◆ / more bike lanes ■; light the crosswalks ● / lighting the crosswalks ◆ / brighter crosswalks ■. Start forms: fix the sidewalks, adding bike lanes, brighter crosswalks. An all-◆ or all-■ row bumps the curb: "Parallel, but 'should' needs a verb here."
18. Lincoln, 1863: "...that government [ ], [ ], [ ], shall not perish from the earth." Frame shapes: ✚. Items: **of the people** ✚ / which the people run ⬟ / popular ★; **by the people** ✚ / that people elect ⬟ / people-made ★; **for the people** ✚ / serving the people ◆ / for everyone's good ✚. The last item's ✚ form "for everyone's good" parks but the panel adds: "Clean. Lincoln repeated 'the people' three times; listen to the difference." When the three bold forms are parked, a context card: "From the Gettysburg Address, November 19, 1863, at the dedication of a cemetery for soldiers killed in the Battle of Gettysburg. Wording from the Bliss copy."

### Garage
Each piece: form, job, words, hitch points. Commas are added at front, around after-subject pieces, and before ", and" or ", but" with an independent clause.
- Base G1 "The bus pulled away from the curb." Labeled parts: noun phrase "The bus" (subject), verb phrase "pulled away" (main verb). Pieces: prepositional "in a cloud of gray exhaust" (adverb job; end); prepositional "with the cracked windshield" (adjective job; after subject); participial "Rattling over the potholes" (adjective job, describes the bus; front); absolute "its windows fogged with breath" (modifies the whole clause; front, end); appositive "the last one of the night" (noun phrase renaming the bus; after subject); adjective phrase "Late and nearly empty" (adjective job; front); adverb phrase "far too slowly" (adverb job; end); verb phrase "had already pulled away" (main verb; replaces "pulled away"); adverb clause "before Maya reached the stop" (adverb job; end, front); relative clause "which was twenty minutes late" (adjective job; after subject); independent clause "and Maya watched it go" (stands alone; end, with ", and").
  Work orders: (a) "Tell when, from Maya's side: add an adverb clause." (b) "Show what the bus looked like without a new main verb: add an absolute phrase." (c) "Tell which bus with a prepositional phrase doing an adjective's job."
- Base G2 "The volunteers cleared the trail." Labeled parts: noun phrase "The volunteers", verb phrase "cleared". Pieces: prepositional "after the storm" (adverb job; end, front); prepositional "from three schools" (adjective job; after subject); participial "Working in pairs" (adjective job; front); absolute "their gloves soaked through" (end, front); appositive "students from the high school" (noun phrase; after subject); adjective phrase "Tired but proud" (adjective job; front); adverb phrase "more quickly than anyone expected" (adverb job; end); verb phrase "had cleared" (main verb; replaces "cleared"); adverb clause "so that the race could go on" (adverb job; end); relative clause "who had signed up that morning" (adjective job; after subject); independent clause "but the bridge stayed closed" (stands alone; end, with ", but").
  Work orders: (a) "Say why they did it: add an adverb clause." (b) "Show how they felt with an adjective phrase." (c) "Join a second complete thought: add an independent clause and make the sentence compound."
- Base G3 "The plan worked." Labeled parts: noun phrase "The plan", verb phrase "worked". Pieces: noun clause "What the class planned" (noun job, the subject; replaces the subject); prepositional "on the first try" (adverb job; end); participial "Surprising everyone" (adjective job; front); absolute "the budget still intact" (end); adverb phrase "remarkably well" (adverb job; end); verb phrase "had finally worked" (main verb; replaces "worked"); adverb clause "because each team knew its job" (adverb job; end); independent clause "and the class celebrated" (stands alone; end, with ", and"); appositive "a two-week fundraiser" (after subject; not offered once the noun clause has replaced the subject); relative clause "which the class designed" (adjective job; after subject; same rule).
  Work orders: (a) "Make the subject a whole clause: add a noun clause." (b) "Change the verb phrase so it shows the plan took a while." (c) "Make it compound-complex: add an adverb clause and an independent clause."
- What it adds (one line each, plus a job line "Here it acts as ..."): Noun phrase: "A noun and the words that belong to it; it can be a subject or an object." Verb phrase: "A main verb with its helping verbs (had, will, was); it carries the action and its time." Adjective phrase: "Adjectives working as a group to describe a noun." Adverb phrase: "Adverbs working as a group to tell how, how much or when." Prepositional phrase: "A preposition and its object; it can do an adjective's job (which one) or an adverb's job (where, when, how)." Participial phrase: "Built on an -ing or -ed verb form; it describes the subject in action." Absolute phrase: "A noun plus a participle, loosely attached; it adds a detail about the whole scene." Appositive: "A noun phrase that renames the noun right before it." Adverb clause: "A dependent clause that starts with a word like because, before or so that; it tells why, when or how." Relative clause: "A dependent clause that starts with who, which or that; it tells which one or adds a fact." Noun clause: "A whole dependent clause doing a noun's job, here the subject." Independent clause: "A clause that could stand alone as a sentence; joined here with a comma and and, but or so."
- Shape key (panel): the 7 Lots shapes with glyph and word; the 11 Garage forms with glyph and underline style, and the 5 jobs.
- Work order check: an order that names a job ("a prepositional phrase doing an adjective's job") passes only with a piece whose form and job both match; an order for a sentence type passes when the clause count says that type.

## Interactions in detail
- Shapes are data: each form has one shape tag. A row is clean when every item has the same tag and that tag is in the frame shapes (Lots 1 to 5: the lead's tag). Scrapes are computed between neighbors left to right; one odd car in the middle shows two scrapes.
- Each unlocked car starts on the first listed form that is not bold (in sentences 16 and 17, where nothing is bold, on the start forms listed in Content), so no row starts clean; Reshape then cycles forms in the listed order and wraps. Keys: Tab moves between cars (panel controls come first in tab order), R or Enter reshapes, Space shows Read it.
- Sentence 15 accepts either bold form; sentence 16 accepts any of three rows and counts each one found ("2 of 3 clean rows found").
- Reset this sentence returns every unlocked car to its starting form.
- Frame misfits are data too: a form can carry a `misfit` line that bumps the curb even when its shape matches (sentence 15: "the old phone" is a noun phrase like the lead but compares a battery with a whole phone).
- Garage: a piece can be hitched once per base; a hitch point holds one piece; hitching to a full point swaps the old piece back to the rack. Replace-the-subject removes the after-subject points. A verb-phrase piece replaces the main verb; **Strip it** puts the original back.
- Progress (which rows are clean, Garage pieces per base) saves to localStorage `parallel-parking:v1` (try/catch). Clear my progress asks first. Nothing else is stored; nothing leaves the page.
- Sizes: the lot is drawn at real pixel size per layout. At 760 wide and below, cars stack in a vertical row (spaces become stalls down the page) so roof words stay at 14 px or more. At 680x425 the frame, row and Reshape buttons fit without scrolling (compact panel beside the stage). At 375 the Garage rack becomes a scrolling strip under the chassis.
- Motion off: cars jump to their stalls instead of rolling; the scrape mark and tag still show.
- A tap while a car rolls (400 ms) or the row slides into line acts at once: the motion jumps to its end, the new reshape or sentence starts, and any line about the old state is dropped.

## Look
- Accent `--brand #f7e463` (lane-line yellow: header rule, active lot tab, Next sentence, lead badge) on the kit `theme-912` base. Scene: the painted asphalt is kept dark (average near `#262c36`, the value the contrast below uses), stall lines `#e8edf3`, the painted curb a cool grey near `#8a93a3`, connector words `#c9d3df`. Roof words sit on a code-drawn roof plate `#3a4558` with text in `--ink`, so they read the same on every painted car; scrape marks `#ffb8a8` (the theme's warn) always with the tag in words. Art style: clean flat gouache, seen from straight above, soft shadows, night-lot colors.
- Shapes carry the meaning by glyph and word on every car and stall; color is never the only signal.
- Contrast (WCAG 2.1): brand on panel #141b25 13.38:1, on sec-bg #18202b 12.68:1, on asphalt 10.85:1; brand-ink #1c1203 on brand 14.27:1; roof text #e8edf3 on car #3a4558 8.21:1; warn #ffb8a8 on asphalt 8.47:1.
- Different from 9-12 ELA neighbors: shakespeare-remix lavender #9d8cff and page-to-screen blue (the earlier periwinkle sat 17 dE from shakespeare-remix, so it moved), portrait-in-four-media coral, rhetorical-situation-simulator sand #ffd18c (dE 29), and the theme-912 default amber. Different from this group's accents.

## Art
Local FLUX (`scripts/localart.py`), one clean flat gouache style seen from straight above, asked in one session. No people. Text (roof words, the frame, connector words) stays in code.
- lot-asphalt: "Dark grey asphalt seen from straight above, fine gravel speckle, a few faint oil stains, even night lighting, flat gouache texture"; 16:9; cutout no; people no; full-frame texture under the Lots stage, tiled or cropped per size, with stall lines drawn over it in code.
- lot-curb: "A long grey concrete curb seen from straight above, with a strip of sidewalk behind it, even lighting, flat gouache"; 5:1; cutout no; people no; runs across the top of the Lots stage under the frame text.
- Cars (kit of 4 cutouts, one shared prompt): "A small hatchback car seen from straight above, pointing right, a plain flat blank roof panel, clean flat gouache, soft shadow, plain white background", one each in mustard yellow, teal, brick red and white; 16:9; cutout yes; people no; one car per space, scaled so its length is 90% of the stall; car-mustard is always the lead; the others take turns in row order. At 760 wide and below the builder rotates them 90 degrees for the stacked stalls.
- garage-bay: "Inside an empty clean auto repair garage bay, a pegboard wall of hanging wrenches and tools, a red rolling tool chest, concrete floor, warm work lights, clean flat gouache"; 16:9; cutout no; people no; Garage backdrop, dimmed to 70% behind the chassis.
7 images, none with people. Drawn in code: stall lines, connector words, shape badges, roof plates, the padlock, wrench buttons, scrape marks, the chassis, hitch points, trailer pieces and every label (they stretch with their words or carry text).

## Voice
Bank voice `clear-teacher`, style "Say clearly and kindly, like a patient driving instructor." Not used by another tool in this batch or by any neighbor (argument-map, grade 12, is the only other 9-12 ELA user). It moved off upbeat-guide, which neighbor world-lit-atlas uses. The kit voice queue (`Curio.voice`), `scope: () => state.mode + ':' + state.sentence`. Sentences are on screen, never voiced, so the student hears the instructions, not the answers. Event line ids: clean, lincoln, order-done, order-miss.
- w-lots (how, welcome on entering Lots in Lots 1 to 5; stale when a wrench is tapped or the lot changes): "The first car sets the shape. Tap the wrench on each other car until it matches."
- scrape (how, the first time a scrape shows; stale when that scrape clears): "A scrape means two shapes don't match. Read the tag, then tap the wrench on that car."
- curb (how, the first curb bump; stale when the row changes): "The row matches, but it doesn't fit the words before it. Tap a wrench and try a shape the curb accepts."
- clean (event, every clean row; stale when the sentence changes): "Parked clean."
- lot6 (how, first entry to Lot 6; stale when a wrench is tapped): "No lead car here. Pick any shape with the wrenches, then make every car match it."
- another (how, after the first clean row in sentence 16; stale when the sentence changes): "There's more than one clean row. Tap Find another clean row."
- lincoln (event, sentence 18 clean; stale when the sentence changes): "That's Lincoln's line, from 1863."
- w-garage (how, welcome on entering Garage; stale when a piece is tapped): "Read the work order. Tap a piece, then tap a glowing spot on the sentence."
- jobs (how, the first piece tapped; stale when it is hitched or another piece is tapped): "Each piece has a form and a job. Check both tags, then tap a glowing spot."
- order-done (event, Check work order passes; stale on any hitch): "Work order done."
- order-miss (event, Check work order fails; stale on any hitch): "Not yet. Read what this order asks for, then tap another piece."
- Read speaks the hint, which always names the next action and control.

## Family engine
None.

## Sources
- Standard: CCSS ELA Language L.9-10.1a and 1b, https://www.thecorestandards.org/ELA-Literacy/L/9-10/ (wording quoted in Who and how).
- Phrase and clause types and parallel structure: The Chicago Manual of Style, 18th ed. (2024), chapter 5, "Grammar and Usage" (parallel structure with correlative conjunctions; noun, verb, adjective, adverb, prepositional, participial and absolute phrases; independent and dependent clauses and sentence types, as used in What it adds); confirm section numbers at build and cite them in the source comment.
- Gettysburg Address, Bliss copy: Abraham Lincoln, November 19, 1863, text at the Library of Congress exhibition "The Gettysburg Address", https://www.loc.gov/exhibits/gettysburg-address/ ("that government of the people, by the people, for the people, shall not perish from the earth"). Date and occasion from the same page.
- All other sentences are original, written for Curio Class.
- Checks run (Python, 2026-10-29): every Lots sentence simulated over all form combinations. Sentences 1 to 15 have exactly one clean row each except 15 (two: either bold form) and every clean row uses only bold forms; no starting row is clean. The old start rule (first form that is not bold) left sentences 16 and 17, which have no bold forms, starting clean, so both now list start forms. Sentence 16 has 3 clean rows; 17 has 1 clean row and 2 rows that are parallel but bump the curb (all ◆, all ■); 18 has 2 clean rows (the bold three, and the one ending "for everyone's good", which carries its note). Garage clause counts: G1 plus "and Maya watched it go" is compound; G2 plus "but the bridge stayed closed" is compound; G3 plus "because each team knew its job" and "and the class celebrated" is 2 independent and 1 dependent clause, compound-complex. Contrast ratios in Look recomputed with the WCAG 2.1 formula; all match to 0.01.

## Done when
- Every Lots sentence starts unclean and reaches "Parked clean" only with the bold forms (sentence 15: either bold form; 16: each of 3 rows).
- A single mismatched middle car shows two scrapes, each tagged with both shapes in words.
- Sentence 17 with an all -ing row shows the curb bump tag, not a scrape.
- Sentence 18 parks clean with "of / by / for the people" and shows the dated context card.
- Garage: each piece offers only its listed hitch points; G3's noun clause removes the after-subject points; commas appear correctly in the printed sentence; the clause count is right (G3 with "because each team knew its job" and "and the class celebrated" reads compound-complex).
- All 11 forms and 5 jobs appear on at least one piece or labeled part; G1 order (c) fails with "in a cloud of gray exhaust" (prepositional, but an adverb's job) and passes with "with the cracked windshield".
- Each work order passes with its named type and fails with a different one, with the line in Content.
- Progress survives a reload; Clear my progress asks first and empties it.
- Voice: the reshape instruction is spoken once; five reshapes in a row speak nothing new; each clean row says "Parked clean."
- Focus: at 1366x768 and 680x425 the parking row (or the Garage chassis) is the largest thing on the stage, centered, with every car's roof words readable.
- Tap while it plays: a wrench, Next sentence or lot tab tapped while a car rolls or the row slides acts at once; nothing waits for the animation and no stale line plays.
- Sentences 16 and 17 open unclean on their listed start forms.
- At 375 and 760 wide the cars stack with roof text at 14 px or more and no horizontal scroll; at 1366x768 the frame, row and Reshape controls are visible without scrolling.

## Open questions
None. Settled with BASELINE rule 2: the Garage now teaches every phrase and clause type L.9-10.1b names, by form and by job.
