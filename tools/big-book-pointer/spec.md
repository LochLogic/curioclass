# Big Book Pointer

## One idea
Dot the mouse holds the reading pointer and reads aloud only the word she lands on, and she only goes where the class tells her, so a wrong move is heard at once: go left and the page reads backwards, skip the return sweep and she bonks off the edge, squish the spaces out and she can't read at all; the class hears why print goes left to right, top to bottom, word by word.

## Not like
- letter-lanterns (k, draft): matches letters to their sounds and lights a village. Here letters are found and named by letter name, inside real pages, and the main work is direction, words and spaces.
- sentence-train (k, concept): builds sentences from word cars with a capital and an end mark. Here nothing is built; the class steers a reader through a finished book.
- rhyme-time-rumble (k, concept): listen-only sound play with no print. Here everything is print on a page.
- story-stage, my-story-strip (k, concept): retell or make stories. Here the story is only the road the pointer travels.
- echo-reader (1, concept): the class reads and records. Here the class never reads aloud for a recording; it points and Dot reads.
- meet-the-book-makers (k, this batch): the parts of a book (covers, title page) and who made it. Here the inside of one page: where to start, which way, what a word is.
- socratic-seminar-board (10, spec, same format): a talk map for seminars. Here the showdown is two class teams taking turns steering one pointer.

## Who and how
- Kindergarten, ELA, module "Print Concepts and the Alphabet" (Foundational Skills). Standard: RF.K.1 (a follow words left to right, top to bottom, page by page; b spoken words are written as specific sequences of letters; c words are separated by spaces; d recognize and name all upper- and lowercase letters).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class calls out the move and a helper taps. Optional `Teams` (Sun and Moon) take turns; no points. Every question, choice and next step is spoken and every choice is a picture or a place on the page, so a child alone can play (BASELINE rule 4).
- Modes: `Which Way?` (RF.K.1a), `Words and Spaces` (RF.K.1b, c), `Letters` (RF.K.1d). tool.json `modes: ["Which Way?", "Words and Spaces", "Letters"]`, `minutes: "10-15"`, `grades_label: "Kindergarten"`.
- Not a personal prompt. Nothing is stored except the alphabet strip's found letters for this page load (not saved).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RF.K.1a | Which Way?: tap where the page starts, then steer Dot with Right, Back to the start of the next line (return sweep), and Turn the page; Read it back | Dot hops onto each word and reads only it; the "heard" ribbon under the book shows the words in the order they were read, so a wrong way shows (and sounds) scrambled; Dot bonks at a line's right edge | 2, 3 |
| RF.K.1b | Words and Spaces, Find the word: Dot says a word; the line holds that word and a word with the same letters in another order (top, pot); the class taps one and Dot reads it, then names its letters in order | the tapped word lights with its letters numbered by little dots in order; "Same letters, different order, different word" card | 4 |
| RF.K.1c | Words and Spaces, Squished lines: a line with every space gone; the class taps between letters to put spaces back; Dot reads each chunk that is a real word and shrugs at any chunk that is not | spaces open as gaps; real words get a word box under them; a non-word chunk shakes; count of word boxes | 5 |
| RF.K.1d | Letters: Letter hunt (Dot names a letter and its case, the class finds it on the page) and Name it (Dot points at a letter, the class says its name, Say it confirms) | the letter glows, Dot stands on it; the alphabet strip fills each capital and small letter as it is found or named | 6 |

## Screens and modes
Header (kit): title "Big Book Pointer"; mode buttons (`.seg`, icon plus word, 60 px tall): `Which Way?` (arrow icon), `Words and Spaces` (two word boxes icon), `Letters` (Aa icon); `Teams` toggle (sun and moon icon); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), with an icon and a word.

Stage, drawn at real pixel size and re-laid per size:
- The big book: an open picture book filling the stage (1046 x 520 at 1366x768). The painting fills the top half of the right page; the page's text is drawn in code on the left page in a large primer type (44 px at 1366x768, line height 1.6, word spaces 0.6 em), dark ink on cream. Text lines never re-wrap: each page's line breaks are fixed (Content), and the type shrinks to fit the page.
- Dot: a small painted mouse holding a pointer stick, 70 px tall, standing on the top edge of the word she is on, the stick's tip under the word's first letter. She hops along a low arc (300 ms) between words.
- Under the book: the "heard" ribbon (Which Way?), the word boxes row (Words and Spaces) or the alphabet strip (Letters), 120 px tall.
- Panel (right, 320 px): the hint (20 px), the mode's buttons, the Teams badge when on (whose turn: a big sun or moon, 80 px), footer.
- Focus: the page's text and Dot. At 1366x768: header 56, book 520, ribbon 120: all above the fold. At 680x425: header 44, book 460 x 230 with 20 px type, ribbon 60, panel 220; the arrow buttons stay 44 px.

**On load and first tap.** Which Way? opens on page 1 with Dot sitting on the book's top edge, off the text. Nothing speaks before the first tap (kit). First hint: "Where does the page start? Tap the first word." The first tap on a word places Dot there and plays its result (its own line); the welcome is queued after it (`welcomeAfter: true`). Any word can be tapped; the start word is not marked.

### Which Way? (RF.K.1a)
- Step 1, Start: the class taps the word where reading starts. Right (the top-left word): Dot hops there, reads it, the word goes on the ribbon. Wrong: Dot hops there and reads it, the word goes on the ribbon in red-outlined form, and `startWrong` plays; the class taps again. The start step is done when Dot is on the first word.
- Step 2, Steer: four arrow buttons in the panel, 96 px, picture plus word: `Right` (arrow right), `Next line` (curved arrow down and back to the left: the return sweep), `Turn page` (page corner), `Left` (arrow left). Each tap moves Dot by that rule and she reads the word she lands on, which joins the ribbon:
  - Right: the next word on the same line. At a line's last word, Right makes her bonk the page edge (wobble, bump sound), nothing is read, and `edge` plays.
  - Next line: the first word of the next line. Not at a line's end: she goes anyway (skipping words), and the skipped words show as empty dashed gaps on the ribbon. At the page's last line: she bonks the page bottom, `bottom` plays.
  - Turn page: the page turns and she lands on the new page's first word. Not at the page's end: it turns anyway and the unread words show as dashed gaps.
  - Left: the previous word (reading backwards).
- `Read it back` (ear icon): Dot reads the ribbon in the order it was built, one word per 450 ms. A ribbon in the right order sounds like the page; a scrambled one sounds scrambled, which `backWrong` names. `Start page again` (circle arrow) clears the ribbon and puts Dot back on the top edge.
- When a page is read in order to its end and Turn page is tapped, `pageDone` plays, then the next page opens with Step 1. After page 5, `bookDone`, and the book closes on its cover; `Read again` opens page 1.
- What the picture shows: Dot on the word read; the ribbon's word chips (ink on cream, the wrong-way ones with a red dashed outline and a small turned-arrow icon, never color alone); skipped words as dashed gaps.

### Words and Spaces (RF.K.1b, 1c)
Two activities as `.seg` sub-buttons in the panel: `Find the word` and `Squished lines`.
- Find the word: the book shows a "Look Closely" page (Content), one line at a time, large (56 px type). Dot says the target word (`findAsk`). The class taps a word. Dot hops to it and reads it. Right: the word gets a box, then its letters light one at a time while Dot names them in order (letter-name clips), and `findYes`. The same-letter word (the trap): `findSame`: "That word is {word}. Same letters, different order, different word." and both words light their letters, numbered by dots under each letter, so the order difference shows. Any other word: Dot reads it, `findNo`. Then `Next line` (gold).
- Squished lines: a story line with every space removed shows large (56 px). Between each pair of letters there is a thin tap target (the full letter height, at least 44 px wide by overlapping both letters' halves); tapping it opens or closes a space. `Read it` (Dot with an open book icon): Dot hops chunk by chunk; a chunk that is a word on the page's word list (its own words, Content) gets a word box under it and Dot reads it; a chunk that is not a word shakes and Dot shrugs with a "hmm" sound (no voice reads a non-word). When every chunk is a word and the line matches, Dot reads the whole line and `squishYes` counts the word boxes ("Four spaces, five words!"). `Next line` (gold) after that.

### Letters (RF.K.1d)
Two sub-buttons: `Letter hunt` and `Name it`.
- Letter hunt: Dot asks for one letter form ("Find a capital B." / "Find a small b."). The book opens the page in Content that holds that form. Every letter on the page is a tap target (letters at 44 px type, targets padded to 44 px). Right: Dot hops onto it, it glows, `huntYes`, and the strip lights that form. Wrong: Dot hops onto it and names it ("That's a small d."), `huntNo` repeats the ask. The prompts run through all 52 forms in the fixed order in Content; `Skip` moves on (the form stays dark on the strip).
- Name it: Dot hops to a letter on the current page (`nameAsk`: "What is this letter? Say it out loud."); the class says it; `Say it` (speech bubble) makes Dot say the name and case; the strip lights it. `Next letter` picks another form not yet lit if any is on the page.
- Alphabet strip: 26 tiles under the book, each with a capital and a small letter; a found form turns from outline to filled with a small star; a full tile (both forms) gets a ring.
- Page arrows (`<` `>` under the book, 60 px) are live in Letters, so the class can browse.

## Content
**The big book, "Zebra Is Last"** (our own story; fixed line breaks):
- Cover: "Zebra Is Last" (title), "a parade story".
- 1: "The animals line up / for the big parade. / They go from A to Z."
- 2: "Ant is first in line. / Bat and Cat are next. / Zebra is last."
- 3: "Zebra looks up the long line. / I am always last, she says. / Her tail droops very low."
- 4: "The band starts a quick, jazzy tune. / Then Owl yells, Turn around! / The whole line turns."
- 5: "Now Zebra is first! / She jumps and kicks. / Fox and Yak dance at the back."
- 6, the parade page (Letters only): 26 banners in two rows of 13, each held by its animal: Ant, Bat, Cat, Dog, Elk, Fox, Goat, Hen, Ibis, Jay, Koala, Lion, Mole, Newt, Owl, Pig, Quail, Rat, Seal, Tiger, Urchin, Vole, Wolf, Xerus, Yak, Zebra.
Words per line (pages 1 to 5): 4 4 6; 5 5 3; 6 6 5; 7 5 4; 4 4 7.

**Look Closely lines** (Find the word; target, the line; the same-letter word):
1. top: "The top is on the pot." (pot) 2. pot: "The top is on the pot." (top) 3. no: "Owl says no, Yak says on." (on) 4. was: "I saw it was Zebra." (saw) 5. tab: "The bat has a tab." (bat) 6. ten: "Ten ducks in a net." (net)

**Squished lines** (from the story; the answer has the spaces shown): "Ant is first in line." / "Zebra is last." / "Her tail droops very low." / "The whole line turns." / "Now Zebra is first!" / "She jumps and kicks." The end mark stays attached to the last word.

**Letter hunt order** (each form with the page that shows it): the capitals A to Z on page 6 (each banner's first letter), then the small letters a to z on the first story page that has them (computed): a p1 ("animals"), b p1 ("big"), c p4 ("quick"), d p1 ("parade"), e p1 ("The"), f p1 ("for"), g p1 ("big"), h p1 ("The"), i p1 ("animals"), j p4 ("jazzy"), k p3 ("looks"), l p1 ("animals"), m p1 ("animals"), n p1 ("animals"), o p1 ("for"), p p1 ("up"), q p4 ("quick"), r p1 ("for"), s p1 ("animals"), t p1 ("the"), u p1 ("up"), v p3 ("very"), w p3 ("always"), x p2 ("next"), y p1 ("They"), z p4 ("jazzy"). The order alternates two capitals, then their two small letters (A B a b C D c d ...), so a capital and its small letter are found close together.

**Letter names** (clips): each letter name as a word ("ay", "bee", "see", "dee", "ee", "eff", "jee", "aitch", "eye", "jay", "kay", "ell", "em", "en", "oh", "pee", "cue", "ar", "ess", "tee", "you", "vee", "double you", "ex", "why", "zee"), each recorded with "capital" and "small" forms ("capital bee", "small bee").

## Interactions in detail
- Every tap acts at once: a new arrow tap while Dot hops or reads cuts the old word and moves on. Mode and sub-buttons stop everything.
- Which Way?: the ribbon holds up to 40 chips, then scrolls left inside its own strip. Read it back during a hop waits for the hop (300 ms) and then reads; any tap stops Read it back. Teams on: the badge flips after each arrow tap, start tap, gap tap or letter tap.
- Squished lines: taps between letters toggle a space; a space after the end mark is not possible; Read it with no spaces reads nothing and shakes the whole line (`squishNone`). A line can be re-spaced after Read it.
- Letter hunt: a letter tap is judged against the asked form only (capital B vs small b); a capital tapped when the small one is asked gets `huntCase`. The strip lights from Name it too.
- Keyboard: arrows Right, Down (next line), Page Down (turn page), Left; Space is Read it back; in Letters, Tab moves through letters.
- Motion off: Dot appears on each word with no hop or bonk wobble; timing (300 ms per hop) is kept, so the words are read on the same beat.
- Nothing is saved.

## Look
- Accent `--brand` #a8431e brick red (header, mode buttons, arrows); gold #f2c14e for Next line, Read it, Read it back; paper #fbf7ee; ink #2a1d16; muted #655a50. The book is cream paper on a warm wooden reading-rug table; the parade page is bright.
- Contrast (WCAG 2.1, computed): white on brand 6.02:1; brand on paper 5.63:1; ink on paper 15.28:1; muted on paper 6.27:1; ink on gold 9.73:1.
- Never color alone: wrong-way chips carry a dashed outline and an icon; found letters a fill and a star.
- Different from the K ELA neighbors: letter-lanterns #1B1A3A night indigo; this batch's other four (plum, pine, blue, amber).

## Art
Local FLUX (`scripts/localart.py`), one warm gouache picture-book style; no people.
- book-spread: "An open giant picture book lying flat, cream pages, a soft shadow at the spine, the left page and the lower right page plain cream paper, warm gouache illustration"; 16:9; cutout no; people no; the book every page sits in (the text and paintings are placed on it).
- pages 1 to 5 paintings: (1) animals forming a line under bunting at a parade ground; (2) an ant at the front, a bat and a cat behind, a zebra far at the back; (3) a zebra at the end of a long line looking ahead, tail drooping; (4) a small animal band with drums and horns, an owl calling out; (5) the zebra leaping at the front of the line, a fox and a yak dancing at the back; each 4:3; cutout no; people no; the upper right page.
- parade: "Twenty-six animals marching in two rows in a parade, each holding a blank cream banner on two poles, bright gouache"; 16:9; cutout no; people no; page 6 (banner names in code).
- dot-stand, dot-hop, dot-shrug, dot-bonk: "A small grey mouse in a red scarf holding a long thin wooden pointer stick, <standing / mid-hop / shrugging / dizzy after a bump>, gouache, plain white background"; 3:4; cutout yes; people no; Dot's poses.
- look-closely-1 to 6: small spot paintings for each Look Closely line (a top beside a pot; an owl and a yak; a zebra seen through a window; a bat with a tag; ten ducks by a net); 4:3; cutout no; people no.
16 images, none with people. Drawn in code: all page text, the ribbon, word boxes, letter targets and numbering dots, the alphabet strip, the Teams badge, all controls.

## Voice
Bank voice `bright-teacher` (style "Say brightly and cheerfully, like an upbeat first grade teacher"): Dot's voice. Not used by any K-2 ELA tool specced so far (letter-lanterns playful-friend; nonsense-words, hamburger-paragraph curious-librarian; sight-words, contraction-crusher warm-teacher) or by the other four in this batch. Every story word, Look Closely word and letter name is its own clip (Dot reads only one word at a time). `Curio.voice` with `scope: () => state.mode + ':' + state.sub + ':' + state.page`, `welcomeAfter: true`.
- how `welcome` (Which Way?; stale once Dot is on the first word): "I'm Dot, and I read only the word I land on. You tell me where to go!"
- event `word` (each hop): the word.
- event `startWrong`: "Hmm. Is that where the page starts? Start at the top, on the left. Tap the first word."
- how `steerHow` (after the start word, first page only): "Which way now? Tap Right, Next line, or Turn page."
- event `edge` (once per line): "Bonk! That's the end of the line. Tap Next line."
- event `bottom`: "Bonk! No more lines. Tap Turn page."
- event `backWrong` (Read it back on a scrambled ribbon): "That sounded mixed up! Tap Start page again and try again."
- event, whole, `pageDone`: "We read the whole page, left to right and top to bottom!"
- event, whole, `bookDone`: "The end! We read every page."
- how `findHow` (Find the word, first time): "Listen to my word. Then tap it on the page."
- event, whole, `findAsk`: "Find the word {word}." event `findYes`: "Yes! {word}: {letter names in order}." event, whole, `findSame`: "That word is {word}. Same letters, different order, different word." event `findNo`: "That word is {word}. Find {target}."
- how `squishHow` (first time): "Oh no, the spaces fell out! Tap between letters to put a space back. Then tap Read it."
- event `squishNone`: "I can't read it with no spaces. Tap between two letters."
- event, whole, `squishYes`: "{n} spaces, {n+1} words! {the line}."
- how `huntHow` (first time): "I'll name a letter. Find it on the page and tap it."
- event, whole, `huntAsk`: "Find a {capital / small} {name}." event `huntYes`: "Yes! A {capital / small} {name}." event `huntNo`: "That's a {case} {name}. Find a {case} {name}." event `huntCase`: "That's the capital {name}. Find the small {name}." (or the reverse)
- how `nameAsk` (first time, then hint only): "What is this letter? Say it out loud. Then tap Say it."
- event `nameSay`: "{capital / small} {name}."
- event, whole, `stripFull` (all 52 lit, once): "We found every capital and every small letter!"
Read speaks the hint, which names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Start word (RF.K.1a) | Tap the biggest or first-painted thing; tap anywhere | Only words are targets; the painting is not. Any wrong start is read aloud and the ribbon shows it out of order. Guess on page 1: 1 of 14 words. |
| Steering (RF.K.1a) | Always Right; always Next line; mashing; guessing an arrow | Computed over pages 1 to 5: always Right is right on 60 of 75 moves but bonks at every one of the 10 line ends and 5 page ends, so no page can be finished with it; always Next line skips words (dashed gaps) on every line with more than one word; a random arrow is right 25 percent and every wrong move is heard and shown on the ribbon. Nothing is scored; the page is done only when the ribbon matches the page in order. |
| Find the word (RF.K.1b) | Guessing; the first word; the same-letter word (the common wrong answer); first letter only | Guess 1 in 5 or 6 words; the target is never the line's first word except "Ten" (line 6), where the first-letter rule also finds it and that is reading its letters; the same-letter word plays `findSame` and shows both letter orders; first-letter matching is the start of reading letter order and still has a second candidate ("the") in lines 1 and 5. |
| Squished lines (RF.K.1c) | Spaces at random; a space after every letter; no spaces | Random placement right 1 in 45 to 1 in 3,876 per line (computed); a space after every letter makes one-letter chunks, which shake (only "I" or "a" can be words, and the lines have neither as a chunk); no spaces plays `squishNone`. Dot reads only real word chunks, never a non-word. |
| Letter hunt (RF.K.1d) | Tap every letter; tap the biggest letter; look-alikes (b and d, p and q) | A wrong tap is named aloud (that is still letter naming) and the ask repeats; the strip lights only the asked form. Look-alikes are named by their own name and case. Mashing lights at most the asked form, after hearing every wrong name. Not scored. |
| Name it | Wait for Say it | Not scored: the class says the name first; Say it is the check. |

## Heard in order
Waits means the next line waits for it to finish; taps always act at once and never wait for a line.
1. Load, first tap on a word: `word` (that word), then `startWrong` if not the first word, then `welcome` (welcomeAfter). Right start: `word`, `welcome`, `steerHow` (first page only). Next action spoken in `steerHow`.
2. Each arrow: `word` (a new tap cuts it). At a line end: `edge`. Page end: `bottom`. Turn page after a full page: `pageDone` (whole) before the new page's first word. After page 5: `bookDone` (whole).
3. Read it back: the ribbon's words, one clip each, in ribbon order; then `backWrong` if scrambled.
4. Find the word: `findHow` (first), `findAsk` (whole); a tap: `word`, then `findYes` (with letter names in order, each a clip) or `findSame` (whole) or `findNo`. Feedback plays before Next line's `findAsk`, which waits for it.
5. Squished lines: `squishHow` (first); Read it: the word clips chunk by chunk (a non-word chunk only a "hmm" sound); then `squishYes` (whole) or nothing.
6. Letter hunt: `huntAsk` (whole); a tap: `huntYes`, `huntNo` or `huntCase`; the next `huntAsk` waits for the feedback. Name it: `nameAsk`, then `nameSay` on Say it.
Letters are always spoken as their recorded names ("bee"), never as sounds.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RF.K.1 and its parts a to d (left to right, top to bottom, page by page; words as letter sequences; spaces between words; name all upper- and lowercase letters) | Common Core State Standards, ELA, RF/K page, thecorestandards.org | CCSS ELA 2010 PDF, Reading Standards: Foundational Skills K to 5 (the official document) | yes |
| Pointing to each word as it is read (finger-point reading) helps young children match spoken words to printed words and learn left-to-right order and the return sweep | Clay, An Observation Survey of Early Literacy Achievement (concepts about print) | Morris (1993), "The relationship between children's concept of word in text and phoneme awareness", Research in the Teaching of English 27(2) | yes |
| A xerus is a real animal (African ground squirrel); an urchin (sea urchin), vole, newt, ibis, quail and elk are real animals | Encyclopaedia Britannica, "ground squirrel" (genus Xerus) | Smithsonian National Zoo animal pages (vole, newt, ibis, quail, elk); NOAA, "sea urchins" | yes |
Backed twice: 3. Cut: 0. "Zebra Is Last" and the Look Closely lines are our own writing; teacher notes say the parade's A to Z order is a story game.

Checks run (Python, scratchpad b1/pointer.py, 2026-11-08):
- Every capital A to Z and every small a to z appears in the book (capitals on the parade page; all 26 small letters in the story pages 1 to 5; the first draft lacked a small v, so page 3 gained "very").
- Steering strategies over pages 1 to 5 (75 moves): always Right 60 of 75 and fails every line and page end; random arrow 25 percent.
- Squished lines: chance of a random right spacing 1/1365, 1/45, 1/3876, 1/560, 1/364, 1/455.
- Look Closely: each line holds the target and exactly one same-letter word.
- Contrast ratios as in Look.

## Done when
1. Focus and fold: at 1366x768 the whole page text, Dot, the ribbon or strip, and every arrow button show with no scroll; at 680x425 the page text is 20 px or more and the four arrows show.
2. Which Way?: Dot reads only the word she lands on; Right bonks at every line end; Next line goes to the next line's first word and dashes any skipped words; Turn page opens the next page; the ribbon shows the reading order. (RF.K.1a)
3. Read it back reads the ribbon in its order; a page finished in order plays `pageDone`; a scrambled ribbon plays `backWrong`. (RF.K.1a)
4. Find the word: each of the 6 lines speaks its target; the same-letter word plays `findSame` with both letter orders lit and numbered; the right word's letter names are spoken in order. (RF.K.1b)
5. Squished lines: taps open and close spaces; Read it reads only real word chunks and shakes non-words; each of the 6 lines ends with the space and word count spoken. (RF.K.1c)
6. Letters: Letter hunt asks all 52 forms in the Content order; capital vs small is judged; the strip lights each form found or named; `stripFull` plays once. (RF.K.1d)
7. Tap while it plays: an arrow, word or letter tap during a hop or a line acts at once; no older word plays after a newer one.
8. Pre-reader: every ask, result and next action is spoken; every choice is an arrow picture or a place on the page.
9. Voice: five arrow taps in a row speak five words and no how-to line twice; `edge` plays once per line.
10. Motion off: no hop or wobble, same 300 ms beat; no network requests; nothing saved.

## Open questions
- None for Cory.
