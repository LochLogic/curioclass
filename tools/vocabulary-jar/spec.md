# Vocabulary Jar

## One idea
During a read-aloud the class taps any word it wonders about, works it out with two clues (a part of the picture that glows, then the nearby words that light up), and drops it into a glass jar as a glowing marble; later, new pictures appear, and every time the class picks a jar word to describe one and says it in a sentence, that word's marble sparkles brighter, so the jar shows which words the class has really started to use.

## Not like
- context-clue-hunt (1, concept): a silly word replaces a real one and the class collects clues. Here real words in a real read-aloud, chosen by the class's own wondering, and then used again.
- word-meaning-yard (k, concept): sorting meanings, endings and opposites. Here new words from books.
- meet-the-book-makers (k, spec): words versus pictures. Here pictures help unlock a word.
- class-phone-call (k-2, spec): a meaning card for one new word per call. Here the words come from reading and are reused to describe.
- question-cube, turn-and-talk-wheel (same format): questions about a text; conversation moves.

## Who and how
- Grades K-2, ELA, module "New Words from Read-Alouds" (Language). Standards: RL.K.4, RI.K.4, RI.1.4, RI.2.4, L.K.6, L.2.6.
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class raises hands to wonder and votes on meanings; a helper taps. Every word, clue and choice is spoken and every choice is a picture, so a child alone can play (BASELINE rule 4).
- Two books: `The Giant Turnip` (story, K-1: RL.K.4) and `Busy Beavers` (fact book, grades 1-2: RI.K.4, RI.1.4, RI.2.4). Steps per book: Read, Wonder, Describe. tool.json `modes: []`, `minutes: "15-25"` per book, `grades_label: "Grades K-2"`.
- Privacy: the jar is saved only on this device (localStorage, try/catch), and the jar says "Your jar is saved only on this device." (BASELINE rule 7). Not a personal prompt.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.K.4, RI.K.4 | During Wonder, tap a word you don't know (asking about it), then answer what it means using the picture clue and the nearby-words clue | the tapped word circled; the glowing part of the picture; the nearby words lit; three meaning pictures | 2, 3 |
| RI.1.4, RI.2.4 | Beavers book: work out topic words (gnaw, dam, lodge, sturdy, swiftly, steer) from the clues; grade 2 also says which clue helped most | the clue cards; the "Which clue helped?" picker | 3, 4 |
| L.K.6 | Describe: pick the jar word that fits a new picture and say it in a sentence | the picture, three jar words; the marble sparkles; the sentence frame | 5 |
| L.2.6 | Describe with the adjectives and adverbs (enormous, sturdy, swiftly) in a frame that uses them to describe | frames like "The cheetah runs ___." | 5 |

## Screens and modes
Header (kit): title "Vocabulary Jar"; `Books` (shelf icon), `Jar` (jar icon); `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** The shelf with two covers and the jar beside them (empty, or holding saved marbles). First hint: "Pick a book to read. Tap The Giant Turnip or Busy Beavers." The first tap opens the book with its own line (`open`); the welcome is queued after it (`welcomeAfter: true`), then Read starts.

**Read.** Focus: the open page (picture left 520 x 520, words right 30 px). The narrator reads each page; the current sentence is underlined. `Next page`, `Back`, `Read this page`. At the end: "Now let's go wonder hunting!" and `Wonder` (magnifier with a question mark) glows.

**Wonder.** The book again from page 1, no narration until asked. Every word is a tap target. The hint asks "Did you hear a word you wonder about? Tap it." and `Read this page` reads it.
- A jar word tapped: it is circled and read, and the Work it out card opens beside the page (380 x 520): Clue 1, `Picture clue` (eye icon): the part of the picture that shows it glows, and the narrator says "Look here." Clue 2, `Word clue` (book icon): the nearby words that point to the meaning light up and are read. Then "What do you think {sprout} means?" and three meaning pictures (each with a short kid definition, spoken on tap). Right: the word becomes a marble (gold glass with the word in code) and drops into the jar (Motion off: it appears there), the definition is read (whole). Wrong: `meaningNo` with the reason, the card dims.
- Grade 2 (Beavers): after a right meaning, "Which clue helped most?" with `Picture clue`, `Word clue`, `Both`. No wrong answer; the pick is shown on the marble's tag.
- A non-jar word tapped: it is read, and "Good wondering! That one's not in today's jar. You can ask your teacher about it." After two non-jar taps on one page, the page's jar word gives a soft sparkle once.
- Each page has one jar word (six pages in each book carry one). `Jar` shows the jar: tap a marble to hear its word and definition.
- At 1366x768: page 1000 x 560 and the Work it out card fit with the panel (the page shrinks to 640 wide while the card is open). At 680x425: the card covers the words column; the picture stays.

**Describe.** Opens when a book's six marbles are in the jar (or from `Jar` any time with at least three marbles). Focus: a new picture (560 x 420, center) and three marble buttons (each a jar word, spoken on tap). The class says which word fits, the helper taps. Right: the frame sentence is read with the word ("The pumpkin is enormous!"), the class says it too, `We said it!` (speech bubble) sparkles that marble once more. Wrong: "Hmm, is a {pumpkin} {scurrying}?" and the marble dims. Six pictures per book.
- The jar view shows each marble's sparkle level: 1 (in the jar), 2 (used once), 3 (used twice or more, glowing).

## Content
**The Giant Turnip** (a traditional folk tale, retold with animals; our words). Jar word per page, picture clue, word clue, meaning (right first) and two wrong meanings.
1. "Grandpa Rabbit planted a turnip seed. 'Grow, little turnip, grow sweet and strong!'" (no jar word)
2. "Soon a tiny green sprout poked out of the dirt." sprout | glow: the little green shoot | words: "tiny green ... poked out of the dirt" | a tiny new plant / a pile of dirt / a watering can
3. "The turnip grew and grew. It grew enormous! It was bigger than Grandpa." enormous | glow: the giant turnip beside Grandpa | words: "grew and grew ... bigger than Grandpa" | very, very big / very tiny / very old
4. "Grandpa gave the leaves a tug. He pulled and pulled." tug | glow: Grandpa's paws gripping the leaves | words: "He pulled and pulled" | a hard, quick pull / a gentle pat / a jump
5. "Grandma, Little Rabbit, the dog and the cat all pulled too. But the turnip would not budge. It stayed right where it was." budge | glow: the turnip, still in the ground | words: "It stayed right where it was" | move just a little / grow bigger / fall asleep
6. "Then a little mouse came scurrying across the yard, quick, quick, quick, on tiny feet." scurry | glow: the mouse mid-run with motion lines | words: "quick, quick, quick, on tiny feet" | run with quick little steps / sleep curled up / climb slowly
7. "They all pulled together, and POP! Out came the turnip. Everyone cheered, 'Hooray!'" cheer | glow: the animals with arms up | words: "'Hooray!'" | shout happily / cry softly / whisper
Describe pictures (frame | right word | two other jar words): a giant pumpkin at a fair ("The pumpkin is ___." enormous | scurry, sprout); a puppy pulling a rope toy ("The puppy gives the rope a ___." tug | cheer, budge); a bean plant just poking up ("A little bean ___ is growing." sprout | enormous, tug); a squirrel dashing across a path ("The squirrel ___ across the path." scurries | budge, cheer); animal fans with paws up at a race ("The fans ___ for the runners." cheer | sprout, scurry); a wagon stuck deep in mud ("The wagon won't ___." budge | tug, enormous).

**Busy Beavers** (fact book, our own):
1. "Beavers are busy builders that live near streams and ponds." (no jar word)
2. "A beaver can gnaw through a tree trunk. It bites and chews with its strong front teeth until the tree falls." gnaw | glow: the beaver's teeth on the trunk, chips flying | words: "bites and chews with its strong front teeth" | bite and chew again and again / lick / sniff
3. "Beavers pile up sticks and mud to make a dam. The dam holds back the stream, and a pond fills up behind it." dam | glow: the wall of sticks across the stream | words: "holds back the stream ... a pond fills up behind it" | a wall that holds back water / a kind of boat / a tall tree
4. "In the pond, beavers build a home called a lodge. Its doors are under the water." lodge | glow: the dome of sticks in the pond | words: "a home called" | a beaver's home / a beaver's food / a beaver baby
5. "A lodge is sturdy. In winter its mud walls freeze hard, and it stays strong." sturdy | glow: the snowy lodge | words: "freeze hard, and it stays strong" | strong and hard to break / soft and squishy / wet
6. "Beavers swim swiftly. They zoom through the water with their webbed back feet." swiftly | glow: the beaver with speed ripples | words: "zoom through the water" | very fast / very slowly / very loudly
7. "A beaver uses its wide, flat tail to steer, so it can turn left or right as it swims." steer | glow: the tail turning in the water | words: "so it can turn left or right" | make it go the way you want / make it stop / make it bigger
Describe pictures: a puppy chewing a bone ("The puppy likes to ___ on a bone." gnaw | steer, lodge); a strong brick house ("The brick house is ___." sturdy | swiftly, dam); a cheetah running ("The cheetah runs ___." swiftly | sturdy, gnaw); a duck steering a toy boat with a wheel ("The duck can ___ the boat." steer | dam, swiftly); a concrete river dam ("People built a ___ across the river." dam | lodge, steer); a beaver lodge in snow ("The beavers stay warm in their ___." lodge | gnaw, sturdy).

## Interactions in detail
- Every tap acts at once; a word tap stops the narrator and reads that word.
- Work it out: the two clue buttons can be pressed in either order or skipped; the meaning question appears after the first clue (or after 4 s with no clue for a teacher who skips). A right meaning makes the marble; a jar word already in the jar is read with its definition and "It's already in our jar!"
- Describe: a wrong pick dims that marble for this picture only. `We said it!` adds one sparkle per picture (a second tap does nothing).
- Jar: up to 12 marbles (both books). `Empty the jar` (with a confirm card) clears the save. Storage blocked: the jar works for this page load and says it can't be saved.
- Motion off: no marble drop or sparkle shimmer; the marble appears, and sparkle levels show as one, two or three small stars on the marble.

## Look
- Accent `--brand` #0f6b46 deep emerald (header, the jar's rim, Wonder); gold #f3c44b (marbles, sparkles); paper #f6fbf6; ink #14261c; muted #4d5f53. Scene: a sunny reading nook with the big glass jar on a windowsill.
- Contrast (WCAG 2.1, computed): white on brand 6.54:1; brand on paper 6.24:1; ink on paper 15.14:1; muted on paper 6.51:1; ink on gold 9.68:1.
- Never color alone: a circled word, a glowing outline on the picture part, lit nearby words underlined; sparkle levels show stars as well as glow.
- Different from the K-2 ELA neighbors and this batch (cobalt, barn red, slate, brown).

## Art
Local FLUX (`scripts/localart.py`); no people (the turnip family are rabbits).
- nook: "A sunny reading nook with a windowsill and a big empty glass jar on it, soft gouache"; 16:9; cutout no; the shelf and jar view.
- jar-front: "A big clear glass jar with a cork lid, soft gouache, plain white background"; 3:4; cutout yes (marbles are drawn inside in code, behind a glass highlight layer).
- covers (2): "A picture book cover of rabbits pulling a giant turnip, folk art gouache, a blank band at the top" and "A beaver carrying a stick past its lodge in a pond, bright watercolor, a blank band at the top"; 3:4; cutout no.
- turnip pages (7) and beaver pages (7): one painting per page as described in Content (each with the clue part clear and unobstructed; the builder sets each glow region); 1:1; cutout no.
- meaning pictures (36): one per meaning in Content (right and wrong), "<a tiny new plant / a pile of dirt / ...>, soft gouache, plain white background"; 1:1; cutout yes.
- describe pictures (12): as listed in Content; 4:3; cutout no.
About 71 images, no people. Drawn in code: marbles and their words, circles, glows, lit words, sparkle stars, every control.

## Voice
Bank voice `friendly-dad` (style "Say in a relaxed, friendly way, like a kind dad helping with homework"): the reader and word helper. Not used by K-2 ELA neighbors or batches 1 and 2, nor the rest of this batch. `Curio.voice` with `scope: () => state.book + ':' + state.step + ':' + state.page`, `welcomeAfter: true`.
- event `open`: the title ("The Giant Turnip, a folk tale." / "Busy Beavers.")
- how `welcome`: "Welcome to the Vocabulary Jar! We'll read, wonder about words, and catch them in our jar."
- event, whole, `page`: the page's text.
- how `wonderHow`: "Did you hear a word you wonder about? Tap it, and we'll figure it out together."
- event `word`: the tapped word. event `notJar`: "Good wondering! That one's not in today's jar. You can ask your teacher about it."
- event `pictureClue` / `wordClue`: "Look here." / "Listen to the words nearby: {words}."
- event, whole, `meaningAsk`: "What do you think {word} means? Tap a picture."
- event, whole, `meaningYes`: "{Word} means {definition}. Into the jar it goes!" event `meaningNo`: "Hmm. Look at the clue again. Does {word} mean {wrong}?"
- event `whichClue`: "Which clue helped most?" event `already`: "It's already in our jar!"
- how `describeHow`: "Let's use our jar words! Which word fits this picture?"
- event, whole, `frame`: the frame sentence with the word. event `sayIt`: "Now you say it!" event `describeNo`: "Hmm, is a {pumpkin} {scurrying}? Try another word."
- event `sparkle`: "Sparkle! That word is getting stronger."
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Find the jar words | Tap every word | Allowed and harmless: non-jar taps are read and praised; the sparkle hint comes only after two non-jar taps on a page, so finding words still starts with wondering. |
| Meaning | Guess; the picture that looks like the page; the biggest | 1 in 3, one size, shuffled; meaning pictures are their own paintings, not page crops; wrong meanings are things on or near the page (dirt, a watering can, the stream), so "it was on the page" does not pick. |
| Which clue helped | Any pick | Not checked by design: it is the child's reflection. |
| Describe | Guess; pick the newest marble; pick the word heard most | 1 in 3 per picture; each set includes two other jar words from the same book; every word is right exactly once per book (computed), so no word wins more than once. |
| Sparkles | Tap We said it! repeatedly | One sparkle per picture; sparkles count uses in Describe only. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Open a book: `open`, then `welcome` (queued, first book), then `page` for page 1 (whole), and each page as it turns.
2. Wonder: `wonderHow` (first), `word` on taps, then `notJar` or the card: `pictureClue`/`wordClue` on their taps, `meaningAsk` (whole), `meaningYes` (whole) or `meaningNo`; Beavers adds `whichClue`.
3. Describe: `describeHow` (first), per picture: marble taps read the word; a pick plays `frame` (whole) then `sayIt`, or `describeNo`; `We said it!` plays `sparkle`. The next picture waits for `sayIt`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.K.4, RI.K.4, RI.1.4, RI.2.4, L.K.6, L.2.6 wording (ask and answer questions about unknown words; determine or clarify the meaning of words and phrases; use words acquired through conversations, reading and being read to, including adjectives and adverbs to describe) | thecorestandards.org, RL, RI and L pages K to 2 | CCSS ELA 2010 PDF | yes |
| The Giant Turnip is a traditional Russian folk tale (a family and animals pull a huge turnip, the smallest helper makes the difference) | Encyclopaedia Britannica or the Afanasyev collection entry, "The Turnip" | Project Gutenberg, Russian fairy tale collections (Afanasyev, translated) | yes |
| Beavers cut down trees by gnawing with their strong front teeth | National Wildlife Federation, "American beaver" | U.S. Fish and Wildlife Service, "Beaver" | yes |
| Beavers build dams of sticks and mud that hold back streams and form ponds | NWF, "American beaver" | National Park Service, "Beavers" | yes |
| Beavers live in lodges in the pond, with underwater entrances | NPS, "Beavers" | Smithsonian's National Zoo, "North American beaver" | yes |
| Lodge walls plastered with mud freeze hard in winter | Smithsonian's National Zoo, "North American beaver" | Minnesota DNR, "Beaver" | yes |
| Beavers swim with webbed hind feet and use their flat tails to steer | NWF, "American beaver" | Smithsonian's National Zoo | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad b3, 2026-11-08): each jar word is the right Describe answer exactly once per book and appears as a wrong option at most twice; every page from 2 to 7 has exactly one jar word; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the page and the Work it out card show together with no scroll; at 680x425 the picture and the card show.
2. Wonder: every word is tappable and read; jar words open the card, others play notJar; the sparkle hint comes after two non-jar taps on a page. (RL.K.4, RI.K.4)
3. Each of the 12 jar words takes only its right meaning, with its picture and word clues working. (RL.K.4, RI.K.4, RI.1.4, RI.2.4)
4. Beavers asks which clue helped after each right meaning. (RI.2.4)
5. Describe: each of the 12 pictures takes only its word and plays its frame; the marble's sparkle level rises. (L.K.6, L.2.6)
6. The jar keeps marbles and sparkles after reload; Empty the jar clears it; the privacy line shows.
7. Tap while it plays: a word or marble tap during reading acts at once; no older line plays after a newer one.
8. Pre-reader: every word, clue, meaning and frame is spoken; meanings are pictures.
9. Motion off: no drops or shimmer, same pacing; no network requests.

## Open questions
- None for Cory.
