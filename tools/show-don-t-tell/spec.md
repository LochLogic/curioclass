# Show, Don't Tell

## One idea
Each card holds a telling sentence (Jaylen was nervous; The house was creepy); the student first collects what characters think, say and do in short scenes, then rewrites a face-down card as a short scene built from detail cards and their own sentences, and Ms. Okafor, a reader who can't see the card, guesses the hidden feeling from the details, saying "I'm not sure" when the signals mix, so they learn that readers know characters from details, not labels.

## Not like
- slow-mo-writer (5, concept): slowing one moment down. Here showing a feeling or a place through details.
- character-choice-story (3, concept): traits from choices. Here think, say and do details in a written scene.
- dialogue-director (3, spec): a comic into prose. Here writing a scene that hides its label.
- stay-in-character (3, spec): what a character would do. Here how details reveal a feeling.
- mood-in-the-pictures (spec): mood from pictures. Here mood from words.

## Who and how
- Grade 4, ELA, module "Showing Character Through Details" (Writing and Reading Literature). Standards: RL.4.3, W.4.3.
- Driver: one student (tool.json `driver: "student"`). Scenes and detail cards are read on tap; typed sentences are read back by the browser's speech voice.
- Eight read scenes, 12 telling cards (8 feelings, 4 settings). tool.json `modes: ["Solo", "Class guess"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.
- Saving: written scenes are kept in this browser; footer: "Your scenes stay on this device." `Clear my scenes` removes them.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.4.3 | Read a scene and tap details, sorting them into Thinks, Says, Does (or Sees and Hears for settings) | three sorting trays with the details | 2 |
| RL.4.3 | Name the feeling or mood the details show and pick the two strongest clues | a feeling card with two clue pins | 3 |
| W.4.3a | Draw a telling card and write an opening that sets up the situation | the opening line | 4 |
| W.4.3b, d | Build the scene from detail cards (actions, dialogue, senses) and the student's own sentences | the scene page with card and own-sentence marks | 4, 5 |
| W.4.3c | Add time words from the strip (later, meanwhile, at last) | time words in the scene | 5 |
| W.4.3e | Write an ending line | the closing line | 5 |
| RL.4.3, W.4.3 | Ms. Okafor guesses the feeling from the details; mixed signals get "I'm not sure" | her guess with the clues she used | 6 |

## Screens and modes
Header (kit): title "Show, Don't Tell"; `Read scenes`, `Write scenes`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A cozy library reading corner with a card deck on a table and Ms. Okafor, a school librarian with a cardigan and a mug, in an armchair. First hint: "Tap Read scenes to collect clues first." The first tap opens the first scene; the welcome is queued after it (`welcomeAfter: true`).

**Read scenes.** A short scene (80 to 120 words). The student taps details; each tapped detail flies into a tray: Thinks, Says, Does (setting scenes: Sees, Hears, Feels on skin). The scene's data holds 4 to 6 key details. Then three feeling cards (one right, two near): the student picks one and pins its two strongest clues.

**Write scenes.** Draw a face-down telling card (the student sees it; Ms. Okafor doesn't). A hand of 8 detail cards (4 fit the hidden feeling, 2 fit a different feeling, 2 neutral), each an action, a line of dialogue or a sense detail. The scene page has an opening line box, a body, a time-word strip and an ending line box. The student drags in cards and types their own sentences (own sentences are marked with a pencil icon). Telling words (a list per card: nervous, scared, worried, creepy, spooky...) get a "You told!" stamp and a suggestion to show it instead.

**Reader test.** `Hand it to Ms. Okafor` reads the scene aloud. She guesses from the detail cards played (each card carries feeling weights in data) and from the student's own sentences (matched against cue-word groups per feeling, generous forms): a clear lead gives a guess with the clues she used ("You're nervous! The tapping pencil, and 'Is it my turn yet?'"); two or more cards for each of two different feelings give "I'm not sure. Smiling and shaking? Which one do you mean?" and the mixed clues glow.

**Class guess.** The scene is shown on the board without its card; the class votes on four feelings, and the writer reveals the card.

At 1366x768 the scene and trays fit side by side; at 680x425 the trays are a drawer.

## Content
Written for Curio Class:
- Read scenes (8): Jaylen waits to give a speech (nervous); Ana gets a letter from her best friend who moved (happy and missing her); Marcus loses the spelling bee (disappointed); Priya hears a noise in the attic (scared); a kitchen on a holiday morning (cozy); an empty school at night (eerie); a busy market (lively); a beach after a storm (calm).
- Telling cards (12): nervous, proud, jealous, embarrassed, excited, lonely, relieved, frustrated; the house was creepy; the classroom was chaotic; the forest was peaceful; the cafeteria was gross.
- Detail cards: 8 per telling card (96 total), written to the card's feeling, with weights for near feelings.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The "You told!" stamp is a suggestion; the student may keep the word, and Ms. Okafor still guesses (and says "You told me!").
- Own sentences matter: they can tip the guess, so a student can show a feeling with no cards.
- Scenes print with their card hidden under a fold line.

## Look
- Accent `--brand` #8a2b3a card crimson (header, card backs, trays); gold #f4c542 (tapped details, the reader's lamp); paper #fbf3f4; ink #2a0d12; muted #66505a. Scene: a warm library corner.
- Contrast (WCAG 2.1, computed): white on brand 8.44:1; brand on paper 7.73:1; ink on paper 16.51:1; muted on paper 6.72:1; ink on gold 11.09:1.
- Never color alone: trays have words and icons; stamps carry words.
- Different from this batch (garage blue, lamp amber, editor green, vase terracotta).

## Art
- People art goes to Gemini: Ms. Okafor (a Nigerian American school librarian in her forties, cardigan, reading glasses, warm smile), 5 poses (reading, thinking, guessing, unsure, delighted); scene characters Jaylen, Ana, Marcus and Priya, 2 each (a face and a gesture that match the scene); "illustrated children's book character <description> <pose>, soft colored pencil, plain white background"; 1:1; cutout yes. Faces and gestures carry the feeling, so each scene picture is checked to match its key details.
- Local FLUX (`scripts/localart.py`): library corner (1); setting scenes (4: holiday kitchen, empty school at night, market, beach after a storm; no people); 16:9.
About 18 images. Drawn in code: cards, trays, stamps, scene page.

## Voice
Bank voice `gentle-storyteller` as Ms. Okafor and the scene reader (unique in this batch). `Curio.voice` with `scope: () => state.mode + ':' + state.card + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "Writers don't just say how someone feels. They show it. Tap the details that show you what's going on inside."
- event, whole, `scene`: the scene.
- event `detail`: the tapped detail.
- how `writeHow`: "Keep your card secret. Write a scene that shows it, and I'll guess."
- event `told`: "You told! Can you show it instead?"
- event `guess`: "{You're nervous!} {The tapping pencil}, and {'Is it my turn yet?'}"
- event `unsure`: "I'm not sure. {Smiling} and {shaking}? Which one do you mean?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: detail trays, card hand, telling-word list, the reader's guess.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reader guess | Write the feeling word | The stamp catches it; Ms. Okafor says "You told me!" and the guess doesn't count as shown. |
| Reader guess | Play all 8 cards | The 2 off-feeling cards are mixed signals, so she says "I'm not sure" (every hand has 2 cards of one other feeling, checked). |
| Read trays | Tap every word | Only key details fly to trays; other taps just read the sentence. |
| Feeling pick | Guess | 3 choices; the two clue pins must be key details. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Read scenes: `scene` (whole), `welcome` (queued, first time); taps: `detail`.
2. Write scenes: `writeHow` (first time); stamps: `told`.
3. Reader test: the scene, then `guess` or `unsure`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.4.3 and W.4.3 wording | thecorestandards.org, Reading Literature and Writing Grade 4 | CCSS ELA 2010 PDF | yes |
| Writers reveal character through what a character says, does and thinks and how others react (indirect characterization) | ReadWriteThink, character trait and characterization lessons | Purdue OWL, characterization in fiction (elements of fiction) | yes |
Backed twice: 2. Cut: 0.

Design choices (not claims): the feeling weights and the mixed-signal rule (two or more cards played for each of two different feelings gives "I'm not sure").

Sensitivity note: people art goes to the fresh-agent review; Marcus's disappointment and Priya's fear are everyday-sized.

Checks run (Python, scratchpad b13, 2026-11-09): in a sample hand the 4 fitting cards give one clear feeling, and playing all 8 trips the mixed-signal rule; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the scene and trays fit; at 680x425 the trays are a drawer.
2. Read scenes sort key details into trays. (RL.4.3)
3. The feeling pick needs two clue pins. (RL.4.3)
4. Write scenes build from cards and own sentences with an opening. (W.4.3a, b, d)
5. Time words and an ending line are prompted. (W.4.3c, e)
6. Ms. Okafor guesses or says "I'm not sure" with the clues she used.
7. "You told!" stamps telling words.
8. Scenes survive a reload where storage works and print with the card folded under.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: details appear in trays without flying; no network requests.

## Open questions
- None for Cory.
