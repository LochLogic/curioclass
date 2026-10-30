# Personal Essay Studio

## One idea
Every vague sentence in a personal essay is a wide shot ("Cooking taught me patience"), and the Zoom lens turns it into one moment by asking five close-up questions (where exactly, what you saw or heard, the exact words someone said, what your hands were doing, what you thought right then), while a meter shows the draft's balance of close-ups and wide shots, and a then-and-now page turns the moment into the reflection that ends the essay.

## Not like
- pacing-strip (ela 9-12, lab, this group): tags each sentence of a made-up scene by kind and graphs pacing around a turning point. Here the writing is true and personal, the measure is specific versus general, and the goal is a whole essay with reflection.
- editors-in-the-margin (ela 9-12, studio, this group): revises a given essay by answering editors' comments. Here the student writes their own essay from a blank page; the tool asks questions and never proposes wording.
- speech-coach (ela 12, lab, this group): rehearses a spoken talk. Here nothing is spoken.
- memoir-and-biography (ela 6-8, explorer, not specced): reads a memoir against a biography. Here the student writes the memoir piece.
- shakespeare-remix (ela 9, studio, spec): logs changes to a source text. Here the only source is the student's memory.

## Who and how
- Grade 11 ELA. Module: College Personal Essay (Writing).
- Driver: students on laptops, alone. Two or three sittings of 30 to 45 minutes (Spark and a first Draft, then Zoom and Then and Now, then Revise); work stays on the device between sittings.
- Standards: W.11-12.3 (narratives with well-chosen details and well-structured event sequences): 3a situation and point of view (Spark, Opening swap), 3b dialogue, description, reflection (Zoom lens), 3c sequence toward a tone and outcome (Sequence board in Revise), 3d precise words and sensory language (Close-up meter), 3e a conclusion that reflects on what was experienced (Then and Now). W.11-12.5 (develop and strengthen writing by planning, revising, editing, rewriting or trying a new approach, focusing on what matters most for purpose and audience): Revise (versions, Compare, Opening swap).
- Privacy: everything the student writes stays in this browser (localStorage, with Clear everything). No names, no account, no upload. The tool never suggests trauma, health, family conflict or other private matters; its prompts are neutral, and a line on every screen says "You choose what to share."
- tool.json: driver "students", minutes "30-45", modes ["Spark", "Draft", "Then and Now", "Revise"], grades_label "Grade 11". Kit starter.

## Screens and modes
Header: title "Personal Essay Studio", small line "Zoom in on one moment."; mode buttons **Spark** (opens first), **Draft**, **Then and Now**, **Revise**; Motion, Sound, Read. Panel: `#hint`, the word count with the chosen limit, the Close-up meter, **See an example**, **Clear everything** (asks twice: "Clear your whole essay from this device?" then "This can't be undone. Clear?").
A one-line note sits under the header on every mode: "You choose what to share. Pick a moment you'd be comfortable with a teacher reading. Your writing stays on this device."

### Spark (opens first)
Focus: the wall of prompt cards, center; the spark list sits in the panel column on the right.
- A wall of 10 prompt cards (Content), each a neutral starting point. Tapping a card flips it to three smaller "narrow it" questions. The student writes up to five quick sparks (one line each) in a list on the right: **Add spark**.
- Each spark gets **Small enough?**: two checks the student ticks, "It happened in one place" and "It took less than a day". A spark with both ticked gets a ◎ mark and the line "Good size for one essay."
- **Use this spark** moves it to the top of the Draft page as the working title.

### Draft
Focus: the writing area, the largest thing on the stage, centered; the lens drawer opens beside it and never covers the outlined sentence.
- A plain, large writing area (18 px, line length about 70 characters) with the working title above it. Autosaves every few seconds.
- The **Zoom lens** button (also the Z key with a sentence selected): the student taps any sentence; the tool outlines it and opens the lens drawer beside it with five boxes:
  1. "Where exactly were you? Name the place."
  2. "What could you see, hear, smell or feel?"
  3. "Did anyone say something? Write their exact words."
  4. "What were your hands or feet doing?"
  5. "What were you thinking right then, not now?"
  The student answers any of them (short notes). **Drop notes under this sentence** places the notes as a grey indented note block in the draft for the student to turn into sentences; the tool never writes sentences itself. The original sentence gets a small ⌖ mark until the student deletes or rewrites it.
- **Wide-shot finder** (toggle): underlines general phrases (Content lists) with a dotted line and a hover note "Wide shot: what moment shows this?"; abstract words get a different dotted style with "Big word: show it, then decide if you still need it." Nothing is blocked or deleted.
- **Close-up meter** (panel): two bars per 100 words, "Close-ups" (numbers, named places and people, quoted speech, sense words) and "Wide shots" (stock phrases and big abstract words), with the counts behind each bar listed under it. It reads, never judges: "12 close-ups, 4 wide shots per 100 words."

### Then and Now
Focus: the three boxes (Then, The turn, Now) in one row across the stage; the draft shows as a narrow strip only while Pick a detail is on.
- Two columns: **Then** ("What did you believe or expect before this moment?") and **Now** ("What do you notice or believe now?"), each a short box; between them **The turn** ("What in the moment changed it? Point to a detail from your draft."), where the student can tap **Pick a detail** and then a highlighted close-up in the draft.
- **Draft an ending** builds a three-line ending frame from the three boxes, with the student's words in place and blanks marked, to paste into the draft (**Add to the end of my draft**). The student edits it there.
- A note: "An ending that reflects doesn't sum up a lesson. It shows how your thinking moved."

### Revise
Focus: the open Revise tool (Compare, Opening swap or Sequence board), one at a time in the stage; the others are buttons in the panel.
- **Save version** stores a named snapshot (up to 10; the oldest unnamed one drops first, with a note).
- **Compare**: pick two versions; the tool shows them side by side with added words underlined and cut words struck, plus a row of numbers: words, close-ups, wide shots, quoted lines, and the opening sentence of each.
- **Opening swap**: three boxes for alternate first sentences, labeled "Start inside the moment", "Start with someone's words", "Start with a thought from now". **Try it** shows the draft's first paragraph with that opening in place (preview only); **Use this opening** replaces the first sentence and saves a version first.
- **Word limit**: 250, 500, 650 or none (student's choice); the count turns the brand color past the limit with the words "over by 37". A note: "Many college applications set a limit between 250 and 650 words. Check the one you're writing for."
- **Read-aloud check**: a checklist the student ticks after reading the essay aloud to themselves or a partner: "I stumbled on a sentence", "A part dragged", "The ending surprised me (good)", "Someone else could picture the moment". Ticks are private notes, nothing else.
- **Sequence board** (3c): the draft's paragraphs as cards in a column. The student gives each card a job from chips (**Set the scene**, **The moment**, **The turn**, **Looking back**, **Background**) and picks the outcome the essay builds toward (**Growth**, **Surprise**, **Resolution**, **An open question**). The board shows the order as a strip of job glyphs and asks one question per pattern it sees, never a verdict: Background before The moment ("Your reader waits 2 paragraphs for the moment. Is that the wait you want?"), no Looking back card ("Where does the reader learn what changed?"), The turn after Looking back ("The ending comes before the change. Try moving The turn up."). Cards move with drag or **Move up / Move down**; **Try this order** previews the essay; **Use this order** saves a version first, then reorders.
- **Two ways to order it** (in See an example): the Zoomed sample split into four blocks (Content) and shown in two orders, with the job strip for each, so the student sees one story told two ways: as written (The moment, Background, The turn, Looking back) and in time order (Background first: "I had come to the kitchen because a friend needed a ride..." moved to the top).
- **Copy essay** copies the plain text.

### See an example
- A drawer with an original sample essay in two versions (Content): "Wide shot" and "Zoomed", with the Close-up meter shown for each and the five lens answers that turned one into the other. Each version sits under its own painting (Art): a wide shot of the community center kitchen from its doorway over the Wide shot version, and a close-up of a torn tortilla on a hot iron pan over the Zoomed version, so the camera words in the tool have a picture.

## Content
### Spark prompts (10 cards, each with three narrow-it questions)
1. "An object you keep for no good reason." Narrow: Where does it sit right now? When did you last touch it? What would you lose if it disappeared?
2. "A place where you lose track of time." Narrow: What time of day is it there? What do you hear? What is the first thing you do when you arrive?
3. "A skill you learned slowly." Narrow: What was your first bad attempt? Who saw it? What did the first good one feel like?
4. "A job, chore or role you take seriously." Narrow: What's the hardest five minutes of it? What do other people not notice about it? When did you start caring?
5. "A time you changed your mind about something small." Narrow: What did you believe before? What made it wobble? What do you do differently now?
6. "Something you make, build or fix." Narrow: What tool do you reach for first? What goes wrong most often? What did the last one look like?
7. "A food you can cook or a recipe you know by heart." Narrow: Where did you learn it? What step do you always rush? What does it smell like at the halfway point?
8. "A question you keep asking." Narrow: When did you first ask it? Where were you? What answer have you heard that didn't satisfy you?
9. "A routine you would defend." Narrow: What time does it start? What is the one step you'd never skip? Who has tried to change it?
10. "A moment you were a beginner in front of other people." Narrow: Where was it? What did you get wrong first? What did someone say?

### Wide-shot finder lists
- Stock phrases (dotted underline): "ever since I was young", "ever since I was little", "I have always", "life-changing", "made me who I am", "taught me a lot", "hard work pays off", "a big success", "in today's society", "comfort zone", "at the end of the day", "eye-opening", "everything happens for a reason", "the dictionary defines", "never give up", "I realized that", "it was a great experience", "words can't describe".
- Big abstract words (dashed underline): responsibility, perseverance, passion, dedication, determination, resilience, growth, journey, leadership, teamwork, success, potential, inspire, inspired, inspiring, amazing, incredible.
- A big word inside a matched stock phrase counts once, as part of the phrase ("a big success" is one wide shot, not two).
- Close-up signals counted by the meter: numerals and number words (one to twenty, thirty to ninety by tens, hundred, first to tenth); capitalized words not at a sentence start (excluding "I" and month and day names, which count as close-ups anyway); text inside quotation marks (each quoted span counts once); sense words: smell, smelled, smoke, sound, loud, quiet, hiss, buzz, creak, crunch, clatter, hum, bright, dim, glow, shadow, cold, warm, hot, damp, dry, dusty, sticky, rough, smooth, sharp, soft, heavy, bitter, sweet, salty, sour, burnt, tore, cracked, dripped, scraped, flickered.

### Sample essay (original, written for Curio Class)
- Wide shot (94 words): "I have always loved cooking. When I started helping at the community center, it was a life-changing experience. Cooking taught me responsibility and patience. Whenever I cook, I feel happy and relaxed. One time I made dinner for a lot of people and it was a big success. Since then I have learned that hard work pays off. I realized that cooking is about more than food. Cooking is my passion, and it has made me who I am. I will bring this passion and dedication to everything I do in college and beyond."
- Zoomed (155 words): "The first tortilla I flipped landed on the burner. Mr. Ortega, who ran the Saturday kitchen at the community center, didn't look up from his dough. \"Again,\" he said, and slid me another ball the size of a walnut. I pressed it flat, peeled it off the plastic and laid it on the hot iron pan. Thirty seconds. Bubbles. Flip. This one tore in half. By the eighth, my palms were dusted white and I had stopped counting the ruined ones. I had come to the kitchen because a friend needed a ride, not because I cared about food. I thought cooking meant following a recipe. Standing at that stove, I learned it meant paying attention: to the hiss of the pan, to the edge of the dough going from wet to dull. Now when I start something new, I expect the first one to land on the burner, and I reach for the second."
- Lens answers shown between them: 1 "The Saturday kitchen at the community center." 2 "Hiss of the pan, flour on my palms, the dough edge going dull." 3 "\"Again.\"" 4 "Pressing dough, peeling plastic, flipping." 5 "I thought cooking meant following a recipe."
- Blocks for Two ways to order it (the Zoomed text, split without changing a word): 1 The moment, from "The first tortilla" to "the ruined ones."; 2 Background, "I had come to the kitchen... following a recipe."; 3 The turn, "Standing at that stove... wet to dull."; 4 Looking back, "Now when I start... reach for the second."
- Meter values for each version are computed by the tool from the text, not stored, so the example always agrees with the meter.

### Ending frame (Draft an ending)
"Before, I [Then]. That changed [The turn]. Now I [Now]." with each bracket replaced by the student's words, or left as a marked blank.

## Interactions in detail
- Prompt cards flip in 250 ms (instant with Motion off); tapping another card mid-flip finishes the first at once and flips the new one. Autosave never blocks typing.
- Sentences are split on . ! ? followed by a space or a closing quote; text in quotation marks stays with its sentence; "Mr." "Mrs." "Ms." "Dr." "St." do not end sentences.
- The meter counts per 100 words (rounded to whole numbers) and needs 50 words before it shows bars ("Write 50 words to see the meter").
- Lens notes are stored with the sentence's text; if the student rewrites the sentence, the notes stay in the draft as plain notes.
- Versions store the full text and a timestamp; Compare uses a word-level diff (longest common subsequence on words).
- Storage: localStorage `personal-essay-studio:v1` (try/catch): sparks, draft, lens notes, Then and Now, versions, limit, checklist. If storage fails, a banner says "This browser isn't saving. Copy your essay before you close the tab." Clear everything asks twice.
- No network; the copy button uses the clipboard only on tap.
- Sizes: the writing area stays at least 60 characters wide at 1000 px and up; at 760 and below, the lens drawer and panel become bottom sheets that cover half the screen, and the draft scrolls above them. At 680x425 the draft and the mode buttons are visible without scrolling. At 375 the Spark wall is one column.

## Look
- Accent `--brand #9c2a55` (deep rose ink: header rule, active mode, Zoom lens button, ◎ marks). Own light `:root`, a writing desk at dusk: `--paper #faf6ef`, `--panel #fffdf9`, `--ink #2a2125`, `--muted #635860`, `--line #e3d9cc`, `--btn #9c2a55`, `--head-ink #ffffff`, `--focus #1b6a8a`. Writing text in a serif stack (Georgia, 'Iowan Old Style', serif) at 18 px; UI in the kit sans.
- Meter bars: Close-ups solid brand, Wide shots hatched `#635860`; each bar has its word and number.
- Contrast (WCAG 2.1): brand on paper 6.82:1, on panel about 7.2:1; white on brand 7.30:1; ink on paper about 15:1; muted on paper about 6.4:1; focus on paper about 5.9:1 (confirm the last three at build).
- Different from neighbors: thesis-workshop slate #5b63a6, editors-in-the-margin red pencil #b3261e (this group, light, more orange), question-sharpener violet, usage-panel ink red on dark, theme-ledger wine #592439 (not a neighbor, darker and browner), and this group's accents.

## Art
Local FLUX (`scripts/localart.py`), no people, house style "warm natural-light photograph look, shallow depth of field". 2 images, both in See an example. The prompt cards stay plain text on purpose: a picture on a prompt would steer students toward one kind of moment, and the prompts must stay neutral. Everything else (writing area, lens drawer, meter, cards, strips) is a writing interface drawn in code.
- pes-kitchen-wide: a community center kitchen seen from its open doorway, long steel counters, a big stove with an iron pan, a bowl of dough and a stack of plates, Saturday morning light through high windows; 16:9; cutout no; people no; above the Wide shot version.
- pes-tortilla-close: a close-up of a torn flour tortilla on a hot black iron pan, small bubbles and brown spots on it, a dusting of white flour on the wooden board beside it; 16:9; cutout no; people no; above the Zoomed version.

## Voice
Bank voice `calm-professor`, style "Say evenly and warmly, like a calm college writing professor reading over your shoulder." Not used by this group or any neighbor (research-notebook, grade 9, is the only other 9-12 ELA user, and neighbors.py does not list it for this tool). It moved off wise-mentor, which neighbor thesis-workshop used then. The kit voice queue (`Curio.voice`), `scope: () => state.mode`. The student's writing is never read aloud.
- w-spark (how; on entering Spark; stale once a card is tapped or a spark added): "Tap a card that sparks something. Then type a small moment in the box and tap Add spark."
- small (how; the first spark added; stale once both checks on it are ticked): "Tick both checks if it happened in one place, in less than a day. Small moments make strong essays."
- w-draft (how; on entering Draft; stale once the lens is opened): "Write freely first. Then tap a sentence that feels general and press Zoom lens."
- lens (how; the first lens opened; stale once notes are dropped or the drawer closes): "Answer any of the five questions in short notes. Then tap Drop notes under this sentence."
- finder (how; the first time the Wide-shot finder is turned on; stale when it is turned off): "Dotted lines mark wide shots. Ask what moment shows each one."
- w-then (how; on entering Then and Now; stale once any box has text): "Write what you thought then and what you think now. Then tap Pick a detail and tap the detail that changed it."
- w-revise (how; on entering Revise; stale once a version is saved): "Tap Save version before big changes. Then try a new opening with Opening swap."
- order (how; the first Sequence board; stale once a card gets a job): "Tap a job chip for each paragraph. Then drag the cards to try a new order."
- saved (event; each Save version; stale after 5 seconds): "Version saved."
- over (event; each time the count passes the limit after being under it; stale when under again): "You're over your word limit. Look for a wide shot to cut."

## Family engine
None.

## Sources
- Standards: CCSS ELA W.11-12.3 and W.11-12.5, https://www.thecorestandards.org/ELA-Literacy/W/11-12/.
- "Many college applications set a limit between 250 and 650 words": the Common App first-year essay instructions (2025-2026 prompts page, commonapp.org) give 250 to 650 words; confirm on the current page at build and keep the line generic (no application named on screen). If it can't be confirmed, drop the sentence and keep the limit picker.
- Sample essay, prompts, lens questions and lists: original, written for Curio Class.
- Number checks (Python, 2026-10-29), the meter rules run on the two samples: Wide shot, 94 words, 1 close-up ("One") and 10 wide shots (6 stock phrases: "I have always", "life-changing", "a big success", "hard work pays off", "I realized that", "made me who I am"; 4 big words outside them: responsibility, passion twice, dedication), so 1 close-up and 11 wide shots per 100 words. Zoomed, 155 words, 13 close-ups (number words first, Thirty, one, eighth, first, one, second; the name Ortega; the day Saturday; one quoted span; sense words hot, tore, hiss) and 0 wide shots, so 8 and 0 per 100 words. The finder finds nothing in the Zoomed sample. Without the new once-only rule, "success" counted twice and the Wide shot read 12 per 100.

## Done when
1. A spark with both checks ticked shows ◎ and moves to Draft as the working title.
2. Zoom lens opens beside a tapped sentence; Drop notes adds a note block and never adds sentences.
3. The Wide-shot finder underlines every phrase and word in the lists (case-insensitive) and finds nothing in the Zoomed sample (check by running both samples).
4. The Close-up meter on the two samples: Wide shot 1 close-up and 11 wide shots per 100 words; Zoomed 8 close-ups and 0 wide shots per 100 words (recompute with the listed rules).
5. Draft an ending fills the frame from the three boxes and marks empty ones as blanks.
6. Save version, Compare (word diff with underline and strike) and Opening swap with Use this opening (which saves a version first) all work.
7. Sequence board: tagging Background before The moment shows the wait question with the right paragraph count; Use this order saves a version first and reorders the draft paragraphs exactly.
8. Focus: at 1366x768 and 680x425 the writing area is the largest thing in Draft and the open lens drawer does not cover the outlined sentence.
9. A tap while anything plays: tapping a second prompt card mid-flip flips it at once; typing during an autosave loses no keystroke.
10. Everything survives a reload; Clear everything asks twice; with storage blocked the banner appears.
11. Every screen shows the "You choose what to share" line; no prompt mentions health, loss, conflict or family trouble; both example images load and show no person.
12. At 375 and 760 wide the lens and panel open as bottom sheets with no horizontal scroll; at 1366x768 the draft and mode buttons are visible without scrolling.

## Open questions
None. Settled:
- Prompt 7's narrow question is now "Where did you learn it?" (wave rule: neutral prompts that don't steer toward family).
- The ten prompt cards stay fixed; a student can already write any spark of their own, and a teacher-added card would be an extra, not the main path (BASELINE rule 4).
