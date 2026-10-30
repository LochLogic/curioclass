# Pacing Strip

## One idea
Pacing is how many words you spend on how much story time: tag each sentence of your scene by kind (action, dialogue, description, reflection) and by how much time passes in it, and the strip lays the scene out as blocks as wide as their word counts over a speed lane (clock stopped, real time, skipping ahead), so you can see at a glance that the drive to the game got 40 words and the moment the bus broke down got 11, then stretch and squeeze until the turning point gets the room it needs.

## Not like
- tension-meter (ela 9, data, not specced): graphs a reader's suspense through a given story with parallel plots and flashbacks. Here the student writes the scene, the measure is words against story time, and the fix is a revision.
- flashback-editor (ela 8, builder, not specced): reorders scenes. Here the order stays; the space each moment gets changes.
- personal-essay-studio (ela 11, studio, this group): zooms a true moment into close-up detail and measures specific against general. Here the scene is made up, every sentence is tagged by kind and time, and the target is the turning point's share.
- director-s-chair (arts 9-12, story, spec): stages a play scene in five theaters. Here the scene is prose and the student is the writer.
- editors-in-the-margin (ela 9-12, studio, this group): sentence rhythm as one of three gauges on a given essay. Here time and space in a narrative are the whole point.

## Who and how
- Grades 9 to 12 ELA. Module: Narrative Scenes and Pacing (Writing).
- Topic line: "pacing a narrative scene".
- Driver: students on laptops, alone or in pairs; a teacher can project a sample scene's strip to start. 30 to 45 minutes.
- Standards: W.9-10.3 and W.11-12.3 (narratives using techniques such as dialogue, pacing, description and reflection; sequencing events so they build): tagging by kind and time, the strip, the turning-point share, the opening and ending readings (3a orients the reader; 3e a conclusion that reflects on or resolves what happened), the Stretch moves that add sensory detail and dialogue (3b, 3d), and revision (Stretch and Squeeze). At the 11-12 setting the strip adds two plot-line lanes for W.11-12.3's "multiple plot lines".
- Grade setting in the panel: **9-10** or **11-12**.
- tool.json: driver "students", minutes "30-45", modes ["Write", "Tag", "Strip", "Compare"], grades_label "Grades 9-12". Kit starter plus `kit:theme-912`.

## Screens and modes
Header: title "Pacing Strip", small line "Words against story time."; scene picker **My scene** / **Sample: The Bus** / **Sample: The Key**; mode buttons **Write** (opens first for My scene; samples open in Strip), **Tag**, **Strip**, **Compare**; Motion, Sound, Read. Panel: `#hint`, grade setting, the readouts (below), **Save version**, **Clear my scene** (asks Yes / No).

### Write
Focus: the writing area, center and widest; the prompt shelf is a row of small painted cards above it.
- A prompt shelf (8 neutral scene prompts, Content), each card with its painted picture (Art) and **Use this prompt**, and a plain writing area. A note: "Aim for 10 to 25 sentences. One scene, one turning point."
- Live count: words and sentences. Nothing else is shown while writing.

### Tag
Focus: the sentence rows and their chips.
- The scene as a list of sentence rows, numbered. Each row has two chip sets:
  - Kind: **Action** (▶), **Dialogue** (❝), **Description** (◐), **Reflection** (✎). One per sentence; a sentence that mixes two takes the one that does most of the work (the tip says so).
  - Story time: **Clock stopped** (description or thought while nothing happens), **An instant**, **Seconds**, **A minute**, **Minutes**, **An hour**, **Hours**, **A day or more**.
- Suggestions: a sentence with quotation marks gets a faint ❝ suggestion; nothing else is suggested. The student confirms every tag.
- **Mark turning point**: tap the flag on the row where the moment begins (the moment after which things can't go back), and optionally the end flag on a later row if the moment runs over several sentences. The span from start to end flag is the turning point. Required before the strip shows its readouts.
- Under the first two rows, two small chips **Who** and **Where** for the student to tick if those sentences name a character and a place (the Opening reading uses them).
- At 11-12, a third chip set **Plot line A / B** appears, with a box to name each line (for example "the game", "Dani").

### Strip
Focus: the strip and its speed lane, full width across the middle of the stage; readouts in the panel.
- Stage: the strip, one horizontal band of blocks in sentence order, each block's width proportional to its words (with a 6 px minimum), filled by kind with a pattern and glyph: Action solid with ▶, Dialogue dotted with ❝, Description hatched with ◐, Reflection wavy with ✎. The turning point's blocks have a flag above them and are bracketed.
- Under it, the speed lane, aligned block for block: Clock stopped draws a flat bar labeled "pause"; An instant to A minute draw a level bar labeled "scene" (words take about as long as the moment); Minutes and longer draw chevrons labeled "summary", more chevrons for more time skipped.
- At 11-12, the strip splits into two lanes (A on top, B under), each sentence in its line's lane, so crosscutting shows as blocks alternating lanes.
- Readouts (panel), all in words and numbers:
  - "Turning point: 13 of 116 words (11 percent)."
  - Share of words by kind (four numbers with glyphs).
  - Story time covered by the scene: the sum of the time chips' values, rounded to a friendly unit ("about 11 hours"), with the note "Rough total: sentences that overlap in time count twice."
  - Readings (soft lines, shown only when they apply; never called errors): **Rush**: "The turning point has under 15 percent of the words." **Long run**: "Sentences 1 to 5 are all description before anything happens." **Jump**: "The clock skips from seconds to hours right after the turning point." **No pause at the turn**: "Nothing slows down at the turning point: it is all action." **Ending**: always shown once readouts are on, from the last sentence's kind: "Your scene ends by looking back." when it is Reflection; otherwise "Your scene ends on Action. Does the reader learn what it meant or how it settled?" (with that sentence's kind in place of Action). **Opening**: always shown, naming the first sentence's kind and whether a character and a place are named in the first two sentences (the student ticks **Who** and **Where** chips on the Tag screen; the tool never guesses).
- Tap any block to jump to its sentence in a side editor and change it in place; the strip re-measures as the student types (after a 400 ms pause).
- Revision helpers (buttons, they suggest moves and never write words):
  - **Stretch the turn**: highlights the turning point and offers four moves as cards: "Add what you see or hear in that second", "Add one line someone says", "Add the thought that flashes by", "Split the action into two or three smaller actions". Each card has **Insert a blank sentence here** so the student writes it.
  - **Squeeze a run**: select two or more neighboring blocks; the tool shows them in a box with the prompt "Say all of this in one sentence" and a write box; **Replace with my sentence** swaps them (the old text goes into the last saved version, never lost).
- **One reading** (samples only): draws the tool's tags as thin outlines over the student's, with "One reader's tags. Yours can differ."

### Compare
Focus: the two strips, stacked.
- Two saved versions as two strips stacked, with the readouts side by side and the change in the turning point's share ("9 percent to 31 percent").

## Content
All scenes and prompts are original, written for Curio Class.

### Prompts (Write)
1. "The bus breaks down on the way to a game."
2. "Someone finds a key inside a library book."
3. "Two friends have ten minutes to finish a cake before the guests arrive."
4. "The power goes out during the last minute of a concert rehearsal."
5. "A stray dog follows you to the bus stop."
6. "A sudden storm on the last afternoon of a camping trip."
7. "The wrong name is called at an awards assembly."
8. "You open your locker and something is in it that isn't yours."

### Sample: The Bus (a rushed turning point). One reading's tags: kind, time; turning point sentence 6.
1. "Coach Ruiz counted heads twice before the bus pulled out of the school lot." Action, a minute.
2. "We drove for an hour through flat fields and three small towns." Action, an hour.
3. "Dani talked the whole way about the other team's goalie." Action, an hour.
4. "Somewhere past the grain elevator, the sky turned the color of a bruise." Description, minutes.
5. "Rain hit the windows in long gray streaks, and the wipers could not keep up." Description, minutes.
6. "Then the bus shuddered, coughed and rolled to a stop on the shoulder." Action, seconds. Turning point.
7. "We waited two hours for another bus and got to the field after halftime." Action, hours.
8. "We lost 3 to 1." Action, an hour.
9. "On the ride home, Dani said, \"At least we have a story.\"" Dialogue, seconds.
10. "I thought about that for a long time." Reflection, hours.
- Plot lines at 11-12: A "the trip" (1, 2, 4 to 8), B "Dani" (3, 9, 10).

### Sample: The Key (a long run of description, then a rushed turn). Turning point sentence 8.
1. "The library on Fourth Street has tall windows that face the river." Description, clock stopped.
2. "The carpet is green and worn pale in front of the returns desk." Description, clock stopped.
3. "There are twelve tables, and each one has a brass lamp with a pull chain." Description, clock stopped.
4. "The shelves in the back smell like dust and old glue." Description, clock stopped.
5. "Mrs. Aldana, the librarian, has worked there for thirty years." Description, clock stopped.
6. "I go there every Thursday after practice." Action, a day or more.
7. "That Thursday I pulled a book about lighthouses off the bottom shelf." Action, seconds.
8. "A small brass key fell out of it and landed on my shoe." Action, an instant. Turning point.
9. "I gave it to Mrs. Aldana and went home." Action, minutes.
10. "\"Where did you find this?\" she asked the next week, holding it up like it might bite." Dialogue, seconds.
11. "It opened a case of old maps that no one had seen in years." Action, a day or more.
- Plot lines at 11-12: A "the key" (6 to 11), B "the library" (1 to 5).

### Time values used by the measures (seconds; shown on screen only as words)
Clock stopped 0; An instant 1; Seconds 10; A minute 60; Minutes 600; An hour 3600; Hours 14400; A day or more 86400. Covered time is the sum of these values, shown in seconds under 2 minutes, minutes under 2 hours, hours under 2 days, days after that, rounded to a whole number ("about 11 hours"). With One reading's tags: The Bus about 11 hours (40,880 s), The Key about 2 days (173,421 s). (The old rule added lower and upper bounds and gave The Bus "about 7 to 54 hours", too wide to read.)

### Craft notes (a **Pacing words** card in the panel)
- "Scene: the words take about as long to read as the moment takes to happen."
- "Summary: a few words cover a lot of time."
- "Pause: description or thought while the clock stops."
- "Writers often slow down at the turning point, so the reader lives in it."
- "An ending can reflect on what happened, resolve it, or leave a last image; a scene that stops on the turning point leaves the reader there."
- "An opening orients the reader: who, where, and what is at stake."
- "These ideas are common in writing craft books; this tool's thresholds are rules of thumb, not laws."

## Interactions in detail
- Sentence split: . ! ? followed by a space or a closing quote; quoted dialogue stays with its tag clause ("she asked"); abbreviations Mr. Mrs. Ms. Dr. St. don't split. A sentence edited into two in the side editor becomes two rows; the new row starts untagged (grey block with "?").
- The strip draws untagged blocks grey with "?"; readouts wait until every sentence has a kind and a time and the turning point is marked ("Tag 3 more sentences to see the readings").
- Turning-point share = words in the turning-point span divided by all words, rounded to a whole percent. Rush when under 15 percent. Sentences the student inserts inside the span (Stretch the turn inserts there) join it. Long run when 4 or more consecutive sentences before the span share one kind. Jump when the time chip of the sentence right after the span is 1000 times or more the span's last chip (a Clock stopped chip is skipped when comparing). No pause at the turn when every sentence in the span is Action.
- Checks on the samples (with One reading's tags, words split on spaces): The Bus has 116 words; its turning point (sentence 6) has 13, 11 percent: Rush, Jump (seconds to hours) and No pause at the turn. The Key has 133 words; its turning point (sentence 8) has 13, 10 percent: Rush, Long run (sentences 1 to 5) and No pause at the turn; no Jump (an instant to minutes is 600 times).
- Save version keeps text and tags (up to 8 versions). Squeeze saves a version first automatically.
- Storage: localStorage `pacing-strip:v1` (try/catch): My scene, tags, versions, grade setting. Sample edits are kept separately per sample with **Reset sample**. Clear my scene asks first.
- Sizes: the strip is redrawn at real pixel size each layout; when blocks would go under 6 px it wraps into two rows with a "continued" mark. At 760 wide and below, the side editor becomes a bottom sheet. At 680x425 the strip, speed lane and readouts fit without scrolling. At 375 the strip runs vertically (blocks as rows whose height is the word count) so text stays readable. No horizontal page scroll.
- Motion off: blocks resize instantly instead of easing. With Motion on, blocks ease over 250 ms; a tap on a block during an ease opens its sentence at once, and a chip changed during an ease restarts it from where the blocks are.

## Look
- Accent `--brand #3fe0c5` (film-leader mint: header rule, the turning-point flag, active mode, Stretch the turn) on the kit `theme-912` base. Kind fills (each with glyph and pattern): Action `#5aa9ff` solid, Dialogue `#ffd166` dots, Description `#c9a0ff` hatch, Reflection `#ff8a8a` waves; speed lane `#a6b3c4` with labels.
- Contrast (WCAG 2.1): brand on panel #141b25 10.45:1, on sec-bg 9.90:1; brand-ink #1c1203 on brand 11.15:1; glyphs drawn in `#0d1219` on each fill, computed 2026-10-29: Action 7.65:1, Dialogue 13.03:1, Description 8.91:1, Reflection 8.28:1; speed lane labels on #a6b3c4 8.83:1.
- Different from ELA 9-12 neighbors: argument-map cyan #19ffff on navy (dE 18.5, and this is greener and softer), source-mixer cyan #45d4e8, theme-ledger and others on light. Different from this group's accents.

## Art
Eight painted prompt pictures, all local FLUX (`scripts/localart.py`), people: false. The strip, lanes and readouts are charts and stay in code.
- Prompt kit (8 images, one per Write prompt; the first two are also the two samples' pictures). Shared prompt: "painted, story-book realism, quiet light, wide view, signs and labels blank". Pieces: `p1-bus` a yellow school bus stopped on the shoulder of a rainy two-lane highway between flat fields, hazard lights on, grey sky; `p2-key` a small brass key lying on worn green library carpet beside a fallen book with a blank cover; `p3-cake` a half-frosted layer cake on a kitchen counter with bowls, spatulas and a wall clock; `p4-stage` a school auditorium stage gone dark, music stands and chairs lit only by an exit-sign glow; `p5-dog` a scruffy brown stray dog sitting on a sidewalk curb in morning light; `p6-storm` a small orange tent at a lakeside campsite under a black storm front; `p7-trophy` a single gold trophy on a table draped in blue cloth on an empty school stage; `p8-locker` a row of school lockers with one door open and a small wrapped package inside. 4:3; cutout no; people: false. Prompt shelf cards (about 140 px wide; 100 px at 375 wide); the scene picker shows p1 for Sample: The Bus and p2 for Sample: The Key.
Drawn in code: the strip, kind patterns and glyphs, the speed lane, flags, plot-line lanes and readouts.

## Voice
Bank voice `playful-friend`, style "Say playfully and cheerfully, like a fun music teacher talking about tempo." The only 9-12 ELA tool with this voice, and not used by another spec in this batch. The kit voice queue (`Curio.voice`), `scope: () => state.mode + ':' + state.scene`. Scenes are on screen, never voiced.
- w-write (how, Write welcome; stale once the writing area has text): "Tap Use this prompt on a card, or start typing your own. Write one scene with one turning point."
- w-tag (how, Tag welcome; stale once every row is tagged): "Tap a kind and a story time on each sentence. Then tap the flag on your turning point."
- w-strip (how, Strip welcome; stale on mode change): "Each block is as wide as its words. Look at how much room your turning point gets, and tap a block to edit it."
- rush (event, each time Rush appears; stale when it clears): "Your turning point is rushed. Try Stretch the turn."
- run (event, each time Long run appears; stale when it clears): "A long run of one kind. Try Squeeze a run."
- stretch (how, first Stretch the turn; stale when its cards close): "Pick a move, then tap Insert a blank sentence here and write it yourself."
- squeeze (how, first Squeeze a run; stale when the box closes): "Say all of the selected sentences in one sentence. Then tap Replace with my sentence."
- w-compare (how, Compare welcome; stale on mode change): "Two versions, one above the other. Did the turning point get more room?"
- reading (how, first One reading; stale when it is turned off): "The thin outlines are one reader's tags. Yours can differ."

## Family engine
None.

## Sources
- Standards: CCSS ELA W.9-10.3, https://www.thecorestandards.org/ELA-Literacy/W/9-10/; W.11-12.3, https://www.thecorestandards.org/ELA-Literacy/W/11-12/.
- Scene, summary and pause as kinds of narrative speed: Gérard Genette, Narrative Discourse (1972; English translation 1980), named only, not quoted; the Pacing words card is original wording and says the thresholds are rules of thumb.
- Scenes and prompts: original, written for Curio Class.
- Checks run in Python (2026-10-29) with One reading's tags and words split on spaces: The Bus 116 words (14, 12, 10, 13, 15, 13, 14, 5, 12, 8), turning point 13 = 11 percent (Rush), next chip Hours after Seconds = 1,440 times (Jump), turning point all Action (No pause), longest same-kind run before the turn 3 (no Long run), ends on Reflection. The Key 133 words, turning point 13 = 10 percent (Rush), An instant to Minutes = 600 times (no Jump), sentences 1 to 5 Description (Long run), No pause, ends on Action. Covered time: The Bus 40,880 s (about 11 hours), The Key 173,421 s (about 2 days); the old bounds rule gave The Bus about 7 to 54 hours and was replaced.

## Done when
- Focus: at 1366x768 and 680x425 in Strip, the strip and speed lane run full width across the middle and are the largest thing on screen, with the readouts visible without scrolling.
- Typing a scene splits it into rows per the rules; quoted dialogue gets a ❝ suggestion and nothing else is suggested.
- The strip's block widths are proportional to word counts (check three blocks against their counts) and every block shows its glyph and pattern.
- The speed lane shows pause, scene and summary from the time chips.
- With One reading's tags, The Bus shows Rush (13 of 116 words, 11 percent), Jump and No pause at the turn and "about 11 hours"; The Key shows Rush (13 of 133, 10 percent), Long run (sentences 1 to 5) and No pause, no Jump, and "about 2 days"; recompute in Python from the text.
- A tap on a block while the strip is easing opens its sentence at once; no voice line names a control that is hidden or disabled.
- Stretch the turn inserts blank sentences only; Squeeze replaces the selected run with the student's sentence and saves a version first.
- At 11-12 the strip shows two lanes and the samples' plot lines fall in the listed lanes.
- Compare shows two strips with the turning-point share change.
- The Bus shows the Ending line "Your scene ends by looking back." (sentence 10 is Reflection); The Key shows "Your scene ends on Action..." (sentence 11 is Action).
- Each prompt card shows its painted picture; no people appear.
- Work survives a reload; Clear my scene asks first; Reset sample restores a sample; at 375 the strip runs vertically with readable text.

## Open questions
None. Settled: the Rush and Long run thresholds stay fixed and labeled as rules of thumb on screen; a teacher setting would be an extra, not the main path (BASELINE rule 4).
