# Context Clue Hunt

## One idea
Every case is a sentence where a real word has been swapped for a silly one ("The blorp barked at the mail carrier."), and Detective Sly the fox lines up four suspects; the class opens clues one at a time (the nearby words, the picture, the word's ending, the group it belongs to) and each clue clears suspects off the board, so the class names the meaning with as few clues as it can, then defends the claim by pointing to the clue that cracked it.

## Not like
- vocabulary-jar (k-2, spec): real new words from read-alouds, worked out from a picture clue and a word clue, then reused. Here made-up words in single sentences, four kinds of clue, suspects cleared one by one, and a claim defended.
- word-meaning-yard (k, spec): sorting familiar words by meaning, endings, categories and opposites. Here working out an unknown word from what is around it.
- word-zoo (1, concept): sorting words by part of speech. Here meaning from context.
- meet-the-book-makers (k, spec, same format): a mystery about who made a book's parts. Here a mystery about what a word means.
- blend-bakery (1, spec): reading words by sound. Here a word that cannot be read for meaning, only worked out.

## Who and how
- Grade 1, ELA, module "Word Meanings" (Language). Standards: L.1.4 (a, b, c), L.1.5 (a, b, c, d).
- Driver: teacher on a projector or a child alone (tool.json `driver: "either"`). Every sentence, clue and suspect is spoken and every suspect has a picture.
- Ten cases in a case file, any order, then `Look Closer` (shades of meaning). tool.json `modes: ["Cases", "Look Closer"]`, `minutes: "10-20"`, `grades_label: "Grade 1"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.1.4a | Open the Nearby words clue: the words around the silly word light up and are read; suspects that don't fit them are cleared | the sentence with clue words underlined | 2 |
| L.1.4b | Cases 6 and 7: open the Word parts clue on a silly word with re- or un- and decide what the part adds | the silly word split into its part and the rest | 3 |
| L.1.4c | Cases 3 and 8: the Ending clue shows -s, -ed or -ing on a silly word; find the root, then pick the form | the ending glows; the root card | 3 |
| L.1.5a | The Group clue: sort the suspects into the group the sentence needs (clothing, animals, food, colors) | a group bin and suspect cards | 4 |
| L.1.5b | Case 9 and the Claim step: say what the word is with a group and a feature ("A glorp is a bird that swims and quacks.") | a frame with two blanks | 5 |
| L.1.5c | Detective's notebook after each case: pick a real-life connection from three pictures, then name one aloud | three pictures; `We said one!` | 6 |
| L.1.5d | Look Closer: peek, glance, stare and peer; large and gigantic: pick the word for each cartoon, then act it out | short loops; word cards | 7 |

## Screens and modes
Header (kit): title "Context Clue Hunt"; mode tabs `Cases` and `Look Closer`; `Case file`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A cozy detective office: Detective Sly the fox at a desk, a case file with ten folders. First hint: "Pick a case. Tap Case 1 to start." The first tap opens the case with its line; the welcome is queued after it (`welcomeAfter: true`).

**A case.** Focus: the case sentence on a big card (1100 x 140, 40 px type, the silly word in a squiggly box), the suspect board below it (four suspect cards, 220 x 200, each a picture and a word, spoken on tap), and four clue envelopes on the right (Nearby words, Picture, Ending or Word parts, Group). Tap an envelope: the clue opens (words light up in the sentence, a picture slides in, the ending glows, or a group bin appears), Sly reads it, and suspects it rules out are stamped "Cleared" and grayed (still tappable to hear why). `Make my claim` is always on: tap a suspect to claim it. Right: the real word replaces the silly one and the sentence is read. Then `Which clue cracked it?`: tap the envelope that did the most. Right claim with one or two clues: a gold badge; three or four: a silver badge.

**Claim frame (case 9 and every case's end).** "A {glorp} is a {bird} that {swims and quacks}." with the blanks filled from the cracked clues.

**Detective's notebook.** After each case, a page: "Where at home might you find {a cozy spot}?" with three pictures, then "Name one at your home!" and `We said one!`.

**Look Closer.** Focus: a cartoon loop (600 x 340) and word cards. "Which word fits? Peek, glance or stare?" Pick; the word's meaning is said; `Act it out` gives 5 s for the class to do it.

At 1366x768 the sentence, board and envelopes fit above the fold. At 680x425 the sentence is 26 px, suspects 140 x 130, envelopes a row under the board.

## Content
Silly words are made up and never real words. (sentence | suspects, answer first | clues and what each clears)
1. "The blorp barked at the mail carrier." | dog, cat, duck, bus | Nearby "barked" clears cat, duck, bus; Picture: a wagging tail behind a fence; Group: animals clears bus; Ending: none (the envelope says "No ending on this one").
2. "I wore my snerg on my head because the sun was hot." | hat, sock, cup, mitten | Nearby "on my head" clears sock, mitten, cup; "sun was hot" clears mitten; Group: clothing clears cup; Picture: a wide brim's shadow.
3. "She is zimming the ball across the yard." | kicking, eating, sleeping, reading | Ending "-ing" (an action happening now; all four have it, so it clears none and Sly says so); Nearby "ball", "across the yard" clear eating, sleeping, reading; Picture: a foot and a ball. Then root: "What is the root of kicking?" kick | kid | king.
4. "The puppy was so flimpy after his bath that he shook water everywhere." | wet, dry, hungry, tall | Nearby "after his bath", "shook water" clear dry, hungry, tall; Group: words that tell how something feels to touch clears hungry, tall; Picture: drips.
5. "We put on our crumbits and went out into the snow." | boots, boot, sandals, hats | Ending "-s" (more than one) clears boot; Nearby "out into the snow" clears sandals; "put on our ... and went out" with Group: things for your feet clears hats.
6. "Gran rezorbed the letter because she liked it so much." | read it again, read it once, threw it away, lost it | Word parts "re-" (again) clears read it once, threw it away, lost it; Nearby "liked it so much" agrees.
7. "The box was unblicked, so all the toys spilled out." | open, shut, full, heavy | Word parts "un-" (not: the box was not something) clears none on its own and Sly says so; Nearby "toys spilled out" clears shut, full, heavy; Picture: a box with its lid flipped back.
8. "Yesterday, Max plimbed the ball, and it went over the fence." | threw, throws, throwing, caught | Ending "-ed" (it already happened) and Nearby "Yesterday" clear throws, throwing; "went over the fence" clears caught. Root: throw.
9. "A glorp is a bird that swims and quacks." | duck, owl, fish, frog | Group "bird" clears fish, frog; feature "swims and quacks" clears owl; Claim frame: A glorp is a bird that swims and quacks.
10. "My favorite color is the color of the sky on a sunny day: zarn." | blue, red, green, black | Group: colors (all four are, so Sly says it clears none); Nearby "sky on a sunny day" clears red, green, black; Picture: a sunny sky.
Detective's notebook prompts (real-life connections, right first): cozy: a blanket fort | a puddle | a mailbox. Loud: a blender | a pillow | a book. Bumpy: a bike path with rocks | a mirror | a plate. Shiny: a spoon | a towel | a leaf. Soft: a teddy bear | a fork | a brick. Busy: a kitchen at dinner | an empty room | a closet. Sticky: honey | a sock | a ball. Cold: the freezer | the oven | a blanket. Tall: a bookshelf | a cup | a shoe. Quiet: a library corner | a drum | a whistle. One per case, in order.
Look Closer (cartoon | word, two others): a mouse looking out of a hole for a second, hiding | peek | stare, glance. A cat looking at a goldfish for a long, long time | stare | peek, glance. A rabbit looking quickly at a clock, then away | glance | stare, peer. An owl looking hard at a tiny bug far off, squinting | peer | glance, peek. A big dog next to a small dog | large | gigantic, tiny. A whale next to a boat | gigantic | large, little. Meanings: peek "a quick, secret look"; glance "a quick look"; stare "a long look"; peer "a hard look, to see something hard to see"; large "big"; gigantic "very, very big".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Clues open in any order; each opened clue stays open; a clue that clears nothing says so (cases 3 and 10 teach that a clue can fit every suspect).
- A cleared suspect can still be tapped to hear why it was cleared; it can't be claimed. A claim of a suspect not yet cleared but wrong: "Hmm, look at the clue words again." and that suspect is cleared with its reason.
- Which clue cracked it?: any opened clue that cleared at least one suspect is accepted; the one that cleared the most gets "That's the one!", any other "That helped too!"; a clue that cleared nothing is refused. Envelope positions are shuffled per case.
- Badges count clues opened before the right claim; there is no penalty or timer.
- Case file shows each case's badge until `Start over`.

## Look
- Accent `--brand` #5c2a5e detective plum (header, envelopes, the squiggly box); gold #f2c94c (badges, the magnifier glint); paper #faf6fa; ink #1f1420; muted #62546a. Scene: a cozy office with a lamp and a corkboard.
- Contrast (WCAG 2.1, computed): white on brand 10.78:1; brand on paper 10.08:1; ink on paper 16.65:1; muted on paper 6.55:1; ink on gold 11.22:1.
- Never color alone: cleared suspects are grayed, stamped "Cleared" and crossed; clue words are underlined as well as tinted.
- Different from this batch (rose, airmail blue, storybook green, savanna) and the grade 1 and K-2 ELA neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people.
- office (1): "A cozy detective office with a desk lamp, a corkboard and a case file, soft gouache, no text"; 16:9; cutout no.
- sly (stand, think, point, cheer: 4): "A friendly fox detective in a tweed cap holding a magnifying glass, <standing / thinking / pointing / cheering>, soft gouache, plain white background"; 1:1; cutout yes.
- suspects (about 34 unique, from Content): "<subject>, simple soft gouache icon, plain white background"; 1:1; cutout yes. Actions (kicking, reading) shown with animals.
- picture clues (8): "<a wagging tail behind a fence / a wide brim's shadow / a foot and a ball / drips / a sunny blue sky / ...>, soft gouache, close-up"; 4:3; cutout no.
- notebook pictures (30): "<subject>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
- look closer loops (6 x 2 frames = 12): "<the cartoon>, frame <1 / 2>, soft gouache"; 16:9; cutout no.
About 89 images. Drawn in code: the case card, envelopes, stamps, the claim frame, badges, every control.

## Voice
Bank voice `smooth-narrator` as Detective Sly. Not used by the rest of this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.case`, `welcomeAfter: true`.
- event `case`: "Case {1}."
- how `welcome`: "Detective Sly here. A real word has gone missing, and a silly word took its place. Let's crack the case with clues."
- event, whole, `sentence`: the case sentence (the silly word said as written).
- event `suspect`: the suspect's word. event `whyCleared`: "{Cat} was cleared. Cats don't bark."
- event, whole, `clue`: the clue's reading ("Look at the nearby words: barked." / "The ending is ing. That means it's happening now." / "Re means again." / "Un means not." / "It's in the group: clothing." / "This clue fits every suspect. It doesn't clear anyone.").
- event `claimYes`: "Case cracked! The word is {dog}." then the sentence with the real word (whole). event `claimNo`: "Hmm, look at the clue words again."
- event, whole, `crackAsk`: "Which clue cracked it?" event `crackYes` / `crackAlso` / `crackNo`: "That's the one!" / "That helped too!" / "That clue didn't clear anyone."
- event, whole, `frame`: the claim frame.
- event, whole, `notebook`: "Where at home might you find something {cozy}?" event `notebookYes`: "Yes! Now name one at your home!"
- event, whole, `look`: "Which word fits? {Peek}, {glance}, or {stare}?" event `lookYes`: the word and its meaning, then "Act it out!" event `lookNo`: "Watch again. Is it quick or long?"
- event `badge`: "A {gold} badge!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Claim | Claim at random with no clues | 1 in 4, and a wrong claim gives only a silver badge path; the reveal sentence and the defend step follow every claim. |
| Claim | Open every clue, then pick the last suspect standing | Allowed and still learning: every cleared suspect came with a reason read aloud; the badge shows it took four clues. |
| Suspects | Pick the most familiar word | Suspects are all common words from the same group or form (boots, boot, sandals, hats; kicking, eating, sleeping, reading), so familiarity does not pick. |
| Which clue cracked it? | Tap the first envelope | Envelope positions are shuffled per case, and a clue that cleared nothing (as in cases 3, 7 and 10) is refused, so the class has to remember what each clue did. |
| Look Closer | Guess | 1 in 3; each word is right once and wrong at least once (computed). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a case: `case`, `welcome` (queued, first time), `sentence` (whole).
2. Envelope taps: `clue` (whole); suspect taps: `suspect` or `whyCleared`.
3. A claim: `claimYes` and the sentence (whole), then `crackAsk` (whole) and its answer line, then `frame` (whole), `badge`; or `claimNo`.
4. Notebook: `notebook` (whole), `notebookYes`.
5. Look Closer: `look` (whole), `lookYes` or `lookNo`.
No line contains a bare letter or letter sound (endings and parts are said inside their words or as "re" and "un", which are said as syllables).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.1.4 a to c and L.1.5 a to d wording (sentence-level context; frequently occurring affixes; root words and inflectional forms such as look, looks, looked, looking; sort words into categories; define by category and key attributes, such as a duck is a bird that swims; real-life connections such as places at home that are cozy; shades of meaning among verbs such as look, peek, glance, stare, peer and adjectives such as large, gigantic) | thecorestandards.org, Language Grade 1 | CCSS ELA 2010 PDF, Language Standards K-5 | yes |
| Meanings used in Look Closer: peek, glance, stare, peer, large, gigantic | Merriam-Webster entries | Cambridge Dictionary entries | yes |
| Prefixes re- (again) and un- (not, opposite of) | Merriam-Webster, prefix entries | Reading Rockets, "Root words, roots and affixes" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b5, 2026-11-08): each case's clues leave exactly one suspect when all are open; silly words picked as non-words (blorp, snerg, zimming, flimpy, crumbits, rezorbed, unblicked, plimbed, glorp, zarn; confirm at build that none is in Merriam-Webster); Look Closer each word right once; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the sentence, board and envelopes show with no scroll; at 680x425 the same, smaller.
2. Every case: with all clues open exactly one suspect stands, and it is the answer; Nearby clues underline and read their words. (L.1.4a)
3. Cases 3, 6, 7 and 8: the Ending or Word parts clue shows the part and says what it means; root picks take only the root. (L.1.4b, L.1.4c)
4. Group clues clear only the suspects outside the group; cases 3 and 10 say the clue clears none. (L.1.5a)
5. Case 9 and claim frames: the frame reads the group and the feature. (L.1.5b)
6. Notebook: each takes only its home picture and offers We said one. (L.1.5c)
7. Look Closer: each loop takes only its word, says its meaning and gives 5 s to act. (L.1.5d)
8. Which clue cracked it?: the clue that cleared the most gets "That's the one", others that cleared something get "That helped too", clues that cleared none are refused.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Pre-reader: every sentence, suspect and clue is spoken. Motion off: loops show two still frames; no network requests; nothing saved.

## Open questions
- None for Cory.
