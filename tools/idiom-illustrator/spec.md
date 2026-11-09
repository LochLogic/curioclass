# Idiom Illustrator

## One idea
The student meets an idiom inside a short story ("Grandpa said Mia was in hot water"), guesses what it means from the scene, then builds the silly literal picture from stickers (Mia sitting in a steaming pot) and flips the card to see the real meaning beside it, so the gap between what words say and what people mean becomes something they made and can laugh at; a word-shades shelf after some cards orders words from guessing to knowing.

## Not like
- simile-slam (5, concept): an arcade of fresh comparisons. Here reading known idioms in context and picturing them literally.
- myth-museum (concept): allusions. Here everyday idioms.
- context-clue-hunt (1, spec): made-up words. Here real phrases whose meaning is not the sum of their words.
- moral-of-the-story (2, spec): lessons of whole stories. Here single phrases.
- headline-writer (3, spec): the main idea of a story. Here meaning of a phrase.

## Who and how
- Grade 3, ELA, module "Literal and Figurative Language" (Language). Standards: L.3.4a and L.3.4d (context and glossary; prefixes and roots move to syllable-surgeon), L.3.5a, L.3.5b, L.3.5c, RL.3.4. Grade 4 deck: L.4.5a, L.4.5b (taken in from glossary-makers; the grades 3-4 span is a question for Cory).
- Driver: one student (tool.json `driver: "student"`). Everything is read on tap.
- Two decks: Grade 3 Idioms (12 cards) and Grade 4 Sayings (12 cards: similes, metaphors, adages, proverbs). tool.json `modes: []`, `minutes: "15-25"`, `grades_label: "Grades 3-4"` (pending).
- Nothing is saved; the gallery lasts until the page closes. `Print` prints the gallery as cards.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.3.4a, RL.3.4 | Read the idiom in its story panel and pick its meaning from three choices using the scene | the story panel and choice pictures | 2 |
| L.3.4d | Flip the card and check the meaning in the studio glossary | the glossary entry beside the card | 3 |
| L.3.5a | Build the literal picture from stickers, then flip to the real meaning | literal and real side by side | 3 |
| L.3.5b | "Where would you hear this?" pick the real moment that fits | three moment pictures | 4 |
| L.3.5c | Word-shades shelf: order related words (wondered, suspected, believed, knew) | the shelf from least to most sure | 5 |
| RL.3.4 | Final story: mark each colored phrase literal or not | the marked story | 6 |
| L.4.5a | Grade 4: explain a simile or metaphor by picking what is being compared and how | the two things joined by a "like" bridge | 7 |
| L.4.5b | Grade 4: picture an adage or proverb literally, then match it to a life moment | the card and its moment | 7 |

## Screens and modes
Header (kit): title "Idiom Illustrator"; `Decks`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** An art studio with an easel and Pip the parrot holding a paintbrush. A deck box for each deck. First hint: "Tap a deck to open your first card." The first tap opens the first card's story; the welcome is queued after it (`welcomeAfter: true`).

**Story panel.** Focus: a comic-style panel (720 x 300) with 2 to 3 sentences; the idiom is underlined. Three meaning choices with small pictures; a wrong choice shows what in the scene argues against it ("Mia isn't wet in the picture. Look at Grandpa's face.").

**Sticker studio.** A blank card (520 x 390) and a sticker tray of 12 (each card's tray holds the 3 to 4 needed stickers and decoys). Drag stickers to build the literal scene; the card checks for its needed stickers (any placement). Then `Flip`: the back shows the real meaning and the glossary entry (word, part of speech words kept simple, meaning, example).

**Where would you hear this?** Three moment pictures; one fits (a kid who broke a vase hears "you're in hot water").

**Word-shades shelf** (after cards 4, 8 and 12 of grade 3). Four word blocks to put on a shelf from least to most sure, each read on tap and used in a sentence. The words come from the standard's own example (knew, believed, suspected, heard, wondered), used in reverse of the order it lists them, so from least to most sure: wondered, heard, suspected, believed, knew. Each shelf uses four of the five: wondered, suspected, believed, knew; heard, suspected, believed, knew; wondered, heard, believed, knew.

**Final story.** A one-page story with eight colored phrases (five idioms, three literal uses like "a cold glass of water"). Tap each to mark Literal or Not literal.

**Gallery.** Each finished card shows the student's literal picture with the meaning under it.

**Grade 4 deck.** Similes and metaphors: the card shows the two things compared and asks what they share (busy as a bee: always working). Adages and proverbs: same studio and moment steps.

At 1366x768 the panel and studio fit; at 680x425 the tray becomes a drawer.

## Content
Grade 3 idioms (12), each with a story panel, three choices, stickers and a moment: in hot water (in trouble), raining cats and dogs (raining hard), a piece of cake (very easy), break the ice (start talking with someone new), hit the books (study hard), cold feet (nervous about doing something), spill the beans (tell a secret), on cloud nine (very happy), under the weather (a little sick), bite off more than you can chew (take on too much), let the cat out of the bag (tell a secret by accident), lend a hand (help).
Grade 4 sayings (12): similes busy as a bee, quiet as a mouse, slow as a snail; metaphors the classroom was a zoo, her heart was a drum, time is a thief; adages and proverbs look before you leap, don't count your chickens before they hatch, practice makes perfect, the early bird catches the worm, two heads are better than one, actions speak louder than words.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Wrong meaning choices give a scene clue and let the student pick again.
- Stickers can be scaled and rotated with two handles (44 px); the studio checks only that needed stickers are on the card.
- Shelf blocks swap on drop; `Check` lights the shelf when the order matches.
- Gallery cards print 4 per page.

## Look
- Accent `--brand` #a12f6b sticker magenta (header, card borders, flip button); gold #f4c542 (the flip shine, stickers' outline when picked); paper #fdf5f9; ink #2a1220; muted #6b5060. Scene: a sunny art studio with paint jars.
- Contrast (WCAG 2.1, computed): white on brand 6.70:1; brand on paper 6.26:1; ink on paper 16.26:1; muted on paper 6.67:1; ink on gold 10.71:1.
- Never color alone: literal and not-literal marks use words and icons (a picture frame, a speech bubble).
- Different from this batch (office green, ink navy, car-wash blue, newsprint red).

## Art
Local FLUX (`scripts/localart.py`). Story characters are animals (Mia is a young fox, Grandpa an old fox), so no people art.
- studio (1): "A sunny cartoon art studio with an easel and paint jars, soft gouache, no text"; 16:9; cutout no.
- Pip (4, wave, paint, laugh, point): "A cheerful parrot artist with a beret and paintbrush <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- story panels (24): "<a young fox looking worried while an old fox frowns beside a broken vase / ...>, soft gouache comic panel"; 12:5; cutout no.
- stickers (about 90): "<a steaming pot / a falling cartoon cat / a cake slice / ...>, flat sticker style, plain white background"; 1:1; cutout yes.
- moments (72): small scene pictures; 4:3; cutout no.
About 190 images, the largest art set in this batch. Drawn in code: cards, shelf, tray, marks.

## Voice
Bank voice `playful-friend` as Pip (unique in this batch). `Curio.voice` with `scope: () => state.deck + ':' + state.card + ':' + state.step`, `welcomeAfter: true`.
- event, whole, `story`: the story panel.
- how `welcome`: "Welcome to the studio! Some sayings don't mean what their words say. Let's paint what they say, then flip to what they mean."
- how `guessHow`: "What do you think it means here? Tap a picture."
- event `clue`: the scene clue.
- how `studioHow`: "Now paint it the silly way. Drag stickers onto the card, then tap Flip."
- event `flip`: "{In hot water} really means {in trouble}!"
- how `momentHow`: "Where would you hear this? Tap the moment."
- how `shelfHow`: "Put the words in order, from least sure to most sure."
- event `shelfDone`: "From wondering to knowing!"
- how `finalHow`: "Tap each colored phrase. Is it literal, or not?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Meaning pick | Guess | One in three; wrong picks give a clue and the flip shows the meaning anyway. Not scored. |
| Studio | Drag all stickers | Decoys don't fail it; it's a creative step. The learning is the contrast at the flip. |
| Shelf | Random order | 1 in 24 for four words (computed); `Check` shows which blocks are in place. |
| Final story | Mark all Not literal | Three phrases are literal; marking all one way leaves three wrong, each with a reason. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Open a deck: `story` (whole), `welcome` (queued, first time), `guessHow`.
2. Wrong pick: `clue`. Studio: `studioHow`; Flip: `flip`.
3. Moment: `momentHow`. Shelf: `shelfHow`, `shelfDone`.
4. Final story: `finalHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.3.4, L.3.5a-c (including the example words knew, believed, suspected, heard, wondered), RL.3.4, L.4.5a-b wording | thecorestandards.org, Language and Reading Literature Grades 3 and 4 | CCSS ELA 2010 PDF | yes |
| The 12 grade 3 idiom meanings | Cambridge Dictionary, idiom entries | Merriam-Webster, idiom entries | yes |
| The 6 adage and proverb meanings | Cambridge Dictionary | Merriam-Webster | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b8, 2026-11-08): 12 plus 12 cards; shelf random order 1/24; final story 5 idioms and 3 literal; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the panel and studio fit; at 680x425 the tray is a drawer.
2. The story panel offers three meanings, and wrong picks give scene clues. (L.3.4a, RL.3.4)
3. The studio checks for needed stickers, and Flip shows the meaning and glossary entry. (L.3.4d, L.3.5a)
4. "Where would you hear this?" offers three moments with one fit. (L.3.5b)
5. The shelf orders four words and checks against data. (L.3.5c)
6. The final story's eight phrases can be marked, with reasons. (RL.3.4)
7. The grade 4 deck works for similes, metaphors, adages and proverbs. (L.4.5a, b)
8. The gallery prints 4 cards per page.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the flip is instant; no network requests.

## Open questions
- None for Cory. (The grade 4 deck question is in sara-questions.md.)
