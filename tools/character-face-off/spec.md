# Character Face-Off

## One idea
The student builds trading cards for two characters lost in two adventure stories (Tom Sawyer lost in a cave with Becky Thatcher, and David Balfour stranded alone on a tiny island in "Kidnapped"), filling each stat slot (wants, fears, how they solve problems, setting, turning point) only with a pinned detail from the text, then plays the cards head to head on challenge cards and says which choice was braver, smarter or kinder and why, so they learn to compare characters, settings and themes on evidence; a theme round shows what each story says about being lost.

## Not like
- character-web (9, concept): one character's pulls. Here two characters compared on evidence, grade 5.
- theme-tracker (4, spec): one story's theme with lamps. Here two stories on one theme.
- stay-in-character (3, spec): predicting a character's choices. Here comparing two characters' real choices.
- side-by-side-reader (spec): two texts compared in general. Here a card game with stat slots and challenges.
- eyewitness-vs-reporter (4, spec): two accounts of one event. Here two stories on one theme.

## Who and how
- Grade 5, ELA, module "Comparing Characters and Themes" (Reading Literature). Standards: RL.5.3, RL.5.9, RL.5.2.
- Driver: one student, or two players building one card each (tool.json `driver: "student"`). Every sentence is read on tap.
- The two texts, adapted for grade 5 (about 1,200 words each): Mark Twain, "The Adventures of Tom Sawyer" (1876), chapters 31 and 32 (Project Gutenberg eBook #74); Robert Louis Stevenson, "Kidnapped" (1886), chapter 14, "The Islet" (Project Gutenberg eBook #421). tool.json `modes: ["Solo", "Two players"]`, `minutes: "30-40"`, `grades_label: "Grade 5"`.
- Nothing is saved; `Print` prints both cards and the theme round.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.5.3 | Fill each card's slots (wants, fears, how they solve problems, setting, turning point), each with a pinned detail from the text | two trading cards with pinned details | 2 |
| RL.5.3 | Challenge rounds: play the detail that shows how each character met the challenge and say which choice was braver, smarter or kinder, with a because | the face-off table with both details and the student's call | 3 |
| RL.5.2 | Write a three-sentence summary on each card's back | the card back | 4 |
| RL.5.2, RL.5.9 | Theme round: write what each story says about being lost, then mark where the two themes match and where they part | two theme lines and a match and part grid | 5 |

## Screens and modes
Header (kit): title "Character Face-Off"; `Stories`, `Cards`, `Face-off`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A game table under a lamp, two blank trading cards and a deck of challenge cards, and Coach Rio, a raccoon in a referee's shirt with a whistle. First hint: "Tap a story to start reading." The first tap reads its title and first line; the welcome is queued after it (`welcomeAfter: true`).

**Read.** Each adapted text in numbered sentences, tap to hear. A glossary strip explains a few old or Scots words (bannock, ebb, "I was a lost man").

**Build a card.** Five slots: Wants, Fears, Solves problems by, Setting (where and when), Turning point. Tap a slot, then a sentence (or a word range) in the story to pin it; then write the stat in a few words ("wants to get Becky home"). A slot pinned to a sentence the key rates 0 for that slot asks "How does this line show what he fears?" (the student may keep it).

**Face-off.** Four challenge cards: Lost in the dark (or alone), Running out of food, A friend in trouble (Tom with Becky; David has no friend there: the student plays the detail that shows him thinking of others or of no one, and the card notes the difference), The way out. For each, the student plays one pinned detail per character, then picks a call (braver, smarter, kinder, or "different, not better") and writes a because. Coach Rio reads both details and the call.

**Card back.** A three-sentence summary of each story (beginning, middle, end), with a check that it names the character, the problem and how it ends.

**Theme round.** Both characters faced being lost. The student writes one theme line per story (frames: "In Tom Sawyer, being lost shows that ___."). Then a grid: rows (Keeping hope, Helping someone else, Looking closely at where you are, Asking for help) and two columns; the student marks each row for each story as shown, not shown or opposite, with a pinned detail. The grid shows where they match and where they part (Tom keeps hope and keeps trying; David loses hope and misses that the tide could let him walk off).

**Two players.** Each builds one card; the face-off alternates turns.

At 1366x768 the story and card fit side by side; at 680x425 the card is a tab.

## Content
- Tom Sawyer, adapted (chapters 31 and 32): Tom and Becky wander from the picnic party into the cave, get lost, their candle burns low, Tom keeps Becky's hope up, they share their last cake, Tom explores side passages with a kite line tied to a rock, sees daylight, and they get out on the river bank five miles below the cave. The adaptation leaves out the scene with the villain in the cave (it uses an offensive name and the meeting is not needed for this comparison) and says so in the data file's change list.
- Kidnapped, adapted (chapter 14): David is washed ashore on Earraid, a small tidal island; he is cold, wet and alone; he eats raw shellfish and gets sick; he loses hope, watches for boats; fishermen shout to him in Gaelic he can't understand; he finally learns that at low tide he can walk across to the mainland, and he walks off.
- Key: each sentence rated 0 to 3 for each slot of each card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Pins can be changed; each slot holds one pin and a short stat.
- Calls are opinions; any call is accepted with a pinned detail and a because.

## Look
- Accent `--brand` #b03a2e card red (header, card borders, challenge backs); gold #f4c542 (pins, the lamp); paper #fdf5f4; ink #2b0f0b; muted #68524e. Scene: a cozy game table.
- Contrast (WCAG 2.1, computed): white on brand 6.02:1; brand on paper 5.60:1; ink on paper 16.62:1; muted on paper 6.73:1; ink on gold 10.98:1.
- Never color alone: slots are labeled; grid marks are icons with words.
- Different from this batch (rover indigo, root plum, chameleon green, glacier teal).

## Art
- People art goes to Gemini: Tom and Becky in the cave by candlelight (2 scenes), David on the rocky islet (2 scenes), and a card portrait of each of Tom and David; "illustrated adventure book scene <description>, 19th-century clothing, ink and watercolor, no text"; 3:4 for portraits, 4:3 for scenes. Public-domain illustrations from the original books are not used here; the generated portraits fit the card frame.
- Local FLUX (`scripts/localart.py`): game table (1); Coach Rio (4 poses: whistle, point, think, cheer), "A friendly raccoon referee in a striped shirt with a whistle <pose>, soft gouache, plain white background"; 1:1; cutout yes.
About 11 images. Drawn in code: cards, challenge cards, grid.

## Voice
Bank voice `hero-coach` as Coach Rio (unique in this batch); both stories are read by `smooth-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.card + ':' + state.slot`, `welcomeAfter: true`.
- how `welcome`: "Two characters, two stories, one big problem: being lost. Build a card for each, and every stat needs proof from the story."
- event, whole, `sentence`: the tapped sentence.
- how `pinHow`: "Tap a slot, then tap the sentence that proves it."
- event `zero`: "How does this line show {what he fears}?"
- event `challenge`: "Challenge: {Running out of food}. Play a detail for each."
- event `call`: "{Tom}: {they share the last cake}. {David}: {he eats raw shellfish}. Your call: {kinder}, because {...}."
- how `themeHow`: "What does each story say about being lost? Write one line for each, then fill the grid."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: card slots and pins, challenge table, summary check, theme grid. (The evidence engine is not used; the slot key is simpler than its source pack.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Slots | Pin any sentence | A 0-rated pin gets a question; the card shows the pinned line, so a mismatch is visible. |
| Face-off call | Pick a call with no because | The because is required; the call is read with both details. |
| Summary | Copy three sentences | The check needs the character, the problem and the ending; copied lines usually miss one. |
| Theme grid | Mark everything shown | Each mark needs a pinned detail; "opposite" rows are in the key for at least two rows (checked). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a story: title, first line, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). Cards: `pinHow` (first time); `zero` as it fires.
3. Face-off: `challenge`, then `call`.
4. Theme round: `themeHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.5.3, RL.5.9, RL.5.2 wording | thecorestandards.org, Reading Literature Grade 5 | CCSS ELA 2010 PDF | yes |
| Tom Sawyer chapters 31 and 32: lost in the cave with Becky, the kite line, the way out | Project Gutenberg eBook #74, chapters XXXI and XXXII (checked 2026-11-09) | Library of Congress, catalog record for the 1876 first edition | yes |
| Kidnapped chapter 14, "The Islet": David alone on a tidal islet, finally walking off at low tide | Project Gutenberg eBook #421, chapter XIV (checked 2026-11-09) | National Library of Scotland, Robert Louis Stevenson and Kidnapped | yes |
Backed twice: 3. Cut: 1 (a real-world note that Earraid can be reached on foot at low tide; only one source was found, so the tool keeps to what the novel says).

Sensitivity note: the Tom Sawyer adaptation leaves out the villain's scene and name; people art goes to the fresh-agent review.

Checks run (Python, scratchpad b14, 2026-11-09): both Gutenberg texts fetched, and chapter XIV of Kidnapped is titled "The Islet"; the theme key has at least two "opposite" rows; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the story and card fit; at 680x425 the card is a tab.
2. Card slots take pins and stats; 0-rated pins get a question. (RL.5.3)
3. Four face-off challenges take two details, a call and a because. (RL.5.3)
4. Card backs take a checked summary. (RL.5.2)
5. The theme round takes two theme lines and the grid with pins. (RL.5.2, RL.5.9)
6. Two players can each build one card.
7. Print shows both cards and the theme round.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: cards don't flip; no network requests.

## Open questions
- None for Cory.
