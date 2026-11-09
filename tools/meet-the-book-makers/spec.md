# Meet the Book Makers

## One idea
A brand new bee book came back from the print shop in pieces, with the makers' names smudged off the cover: the class are book detectives who send every piece to the maker who made it (Olive the owl writes the words, Bruno the bear paints the pictures), put each page back by matching words to the picture that shows them, tour the finished book's covers and title page, and close the case by naming what the whole book is about, two details, and how two ideas in it connect.

## Not like
- windblown-pages (k-2, concept): a gust blows pictures and captions off two books, put back and credited. Here one book, rebuilt from scratch as a case with its makers as characters, plus the parts of a book and the main topic. windblown-pages should not repeat the maker sort; its own spec can center what a picture shows that the words do not.
- big-book-pointer (k, this batch): inside a page (direction, words, letters). Here the whole book as an object and who made it.
- text-feature-makeover (1, concept): headings, glossary, contents make a page easier to use. Here kindergarten book parts: front cover, back cover, title page.
- story-stage, context-clue-hunt (concept): a puppet retell; a word mystery. Here an informational book and its main topic.
- satire-decoder (11, spec, same format): a two-case satire mystery. Different band and look; the shared move (clues lead to a claim) is a case file for five-year-olds.

## Who and how
- Kindergarten, ELA, module "All About Books" (Reading Informational Text). Standards: RI.K.2, RI.K.3, RI.K.5, RI.K.6, RI.K.7 (with prompting and support where the standard says so).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class calls out answers and a helper taps. Every question, piece and next step is spoken and every choice is a picture, so a child alone can play (BASELINE rule 4).
- Four case steps, in order, each reachable from the case file: `The Mix-up` (RI.K.6, RI.K.7), `Book Tour` (RI.K.5), `Big Idea` (RI.K.2), `Tie It Together` (RI.K.3). Then `Case closed`. tool.json `modes: []` (one case; steps in the case file), `minutes: "20-30"` (or one step a day), `grades_label: "Kindergarten"`.
- Not a personal prompt. Nothing is stored except the case file's stamps for this page load.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.K.6 | The Mix-up: send each piece to Olive (words) or Bruno (pictures); then say what each maker does; on the cover, put the names back: "words by" and "pictures by" | Olive's desk with a notebook and pencil; Bruno's easel with paints; each maker says their job; the cover's two name lines | 2 |
| RI.K.7 | The Mix-up, second half: match each picture to its words to rebuild five pages; then Point to it: Olive reads a word from the page and the class taps that thing in the picture | a page rebuilt; the named part of the painting glows (the six legs, the hive, the pollen) | 3 |
| RI.K.5 | Book Tour: tap the front cover, flip the book and tap the back cover, open it and find the title page among the endpaper, title page and page 1 | a closed book you can turn over; the open book's first spreads | 4 |
| RI.K.2 | Big Idea: pick what the whole book is mostly about (bees, flowers or honey), then pin two details that this book tells (from five, two of them not in this book), and tap the page that shows each | the case board with the topic card in the center and two detail pins; the proving page | 5 |
| RI.K.3 | Tie It Together: link each cause card to the card it leads to with red string, and hear the link read with "so" | the string between two cards; the link line on a strip under the board | 6 |
| RI.K.6 (transfer) | Your book: hold up a real classroom book; find the names on its cover; say who wrote the words and who made the pictures | a card with a pointing hand on a book cover (not checked) | 7 |

## Screens and modes
Header (kit): title "Meet the Book Makers"; `Case file` (folder icon, opens the step list); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), with an icon and a word.

Stage, drawn at real pixel size and re-laid per size: a print shop floor (painted) where the case happens. Panel (right, 320 px): the hint (20 px), the step's buttons, the case file's four stamps (each a picture: a pencil and brush, a book, a light bulb, a red string), footer. Focus per step below. At 1366x768 the stage is 1046 x 712 and everything each step needs is above the fold; at 680x425 the stage is 460 x 380 with 10 px or larger text, pieces 64 px.

**On load and first tap.** The stage shows the print shop floor, pieces scattered, Olive and Bruno standing at the back looking worried, and a cover with smudged names. First hint: "The bee book fell apart! Tap Start the case." The first tap on `Start the case` (magnifier icon, gold, 120 px) plays its own line and the welcome is queued after it (`welcomeAfter: true`). The case premise ("the book fell apart, and we must find who made each piece") is in every step's first hint and in Read.

### The Mix-up (RI.K.6, RI.K.7)
- Part 1, Who made it? Focus: the twelve pieces in the middle of the floor and the two makers' workplaces at the left (Olive's desk) and right (Bruno's easel), each 300 px wide with the maker standing by it. Pieces: the five word strips of pages 1 to 5, the five page paintings, the cover title "Busy Bees" (words) and the cover painting (a picture). Tap a piece to hear it (a word strip is read; a picture is named "a picture of ...") and pick it up; tap Olive or Bruno (or drag) to send it. Right: it lands on that workplace, the maker nods. Wrong: the maker shakes their head and says why ("I paint the pictures. Olive writes the words."), the piece goes back. When all twelve are home: Olive and Bruno each say their job (`jobs`), then the cover's smudged lines refill as the class taps `Words by` then `Pictures by` and picks the maker's face for each (two 120 px face buttons).
- Part 2, Put the pages back: Olive's five word strips line up along the bottom; Bruno's five paintings sit on the easel. The class taps a word strip (Olive reads it), then the painting that shows it. Right: they join into a page in the book frame (top center, 500 x 330) and the page number appears. Wrong: Olive reads the strip again and Bruno says "My picture shows {its subject}. Look for {strip subject}." The strip stays picked.
- Point to it (after each page is rebuilt): Olive says one thing from the words ("Point to the hive."); the class taps the painting; the right hotspot glows (Content). A wrong tap names what was tapped ("That's a flower."). `Next page` (gold) moves on.

### Book Tour (RI.K.5)
- Focus: the finished book, closed, front cover up, large in the center (400 x 520), with `Turn over` (curved arrow) and `Open` (open book icon) under it.
- Tasks in order: "Tap the front cover." (targets: the front cover, the spine edge, and, after Turn over, the back cover); "Turn the book over. Tap the back cover."; "Open the book. Find the title page." The open book shows the inside front endpaper (honeycomb pattern, no words), then the title page, then page 1 as tappable spreads (`<` `>` page arrows). Right: the part gets a gold label (Front cover, Back cover, Title page) and `tourYes`. Wrong: that part's name is said ("That's the spine.", "That's page 1. The title page comes before it."), and the task repeats. After all three, the labels stay and `Tour again` resets them.

### Big Idea (RI.K.2)
- Focus: the case board (cork, 760 x 520) with a center spot and two pin spots.
- `Read the book` (open book icon) reads pages 1 to 5 aloud with the book on the board (optional; on by default the first time).
- Topic: three picture cards, Bees, Flowers, Honey (shuffled). The class says it; the helper taps. Right: the Bees card goes to the center (`topicYes`). Flowers or Honey: `topicNo` ("Some pages tell about {it}. Is the whole book about {it}?") and the card dims.
- Details: five detail cards (pictures plus a few words, each read when tapped). Pin two that this book tells. A card from this book pins with `detailYes` and then `Show me`: the class taps one of the five page thumbnails that shows it; right: that page opens beside the board. A card not in this book: `detailNo` ("That may be true, but this book doesn't tell it. Look at the pages.") and the card dims.
- Retell: when the topic and two details are pinned, `Say it` plays the sentence frame and the class says it with the pinned cards: "This book is about bees. It tells that ___ and ___."

### Tie It Together (RI.K.3)
- Focus: three cause cards on the left of the board and three result cards on the right (shuffled), 160 x 120 each.
- Tap a left card, then a right card: a red string is drawn between them and Olive reads the link with "so" (Content). Right: the string stays and its link line appears on a strip under the board. Wrong: the string snaps (a short twang) and `tieNo` plays; the left card stays picked.

**Case closed.** After the four stamps: a library card fills in (title, words by, pictures by, about, two details, one link) and is read whole. `Your book` card then: "Find a book in your classroom. Who wrote the words? Who made the pictures? Look on the cover!" with a pointing hand on a painted book cover. `New case` resets every step.

## Content
**The book, "Busy Bees"** (words by Olive Owl, pictures by Bruno Bear, Hollow Tree Books; our own text):
- Cover: "Busy Bees", "words by Olive Owl", "pictures by Bruno Bear" (smudged at the start).
- Title page: "Busy Bees", "words by Olive Owl", "pictures by Bruno Bear", "Hollow Tree Books".
- 1: "Bees are insects. A bee has six legs and four wings." Point to it: the legs (hotspot on the legs), alt "the wings".
- 2: "Honey bees live together in a hive." Point to it: the hive.
- 3: "Bees fly from flower to flower. They drink a sweet juice called nectar." Point to it: the flower.
- 4: "Bees make honey from nectar. They keep the honey in the hive." Point to it: the honey.
- 5: "Pollen sticks to a bee's fuzzy body. The bee carries it to the next flower. Then the flower can make seeds." Point to it: the pollen (yellow dust on the bee).
- Back cover: "Buzz along with the busy bees!" and a code-drawn bar code shape.
Pieces for the Mix-up: word strips 1 to 5, paintings 1 to 5 (subjects: a bee up close with legs and wings; a hive in a tree with bees; a bee on a flower; honeycomb dripping honey; a bee dusted with pollen flying to a flower), the cover title words, the cover painting (a smiling bee over flowers).
Topic cards: Bees (right), Flowers, Honey.
Detail cards (in this book unless marked): "A bee has six legs" (p1); "Bees make honey from nectar" (p4); "Bees carry pollen to flowers" (p5); "Bees can sting" (not in this book); "Bears eat honey" (not in this book).
Links (cause, result, spoken line):
- "Bees drink nectar", "Bees make honey": "Bees drink nectar, so they can make honey."
- "Pollen sticks to bees", "Flowers make seeds": "Pollen sticks to bees and goes to the next flower, so the flower can make seeds."
- "Bees have four wings", "Bees fly from flower to flower": "Bees have wings, so they can fly from flower to flower."
Maker jobs: Olive: "I'm Olive. I'm the author. I write the words." Bruno: "I'm Bruno. I'm the illustrator. I make the pictures."

## Interactions in detail
- Every tap acts at once; a new tap cuts a reading line. `Case file` lets the teacher jump to any step; the steps keep their state until `New case`.
- The Mix-up: pieces can be sent in any order; a piece already home can be tapped to hear it again but not moved. Part 2 needs Part 1 done (the hint says so; the case file shows its lock as a padlock icon plus "first, the Mix-up").
- Pages are rebuilt in any order; each sits at its number in the book frame. Point to it hotspots are generous (a 60 px minimum circle around each target).
- Book Tour: Turn over and Open are always live; tapping the right part while the book is the wrong way round still counts if it is visible.
- Big Idea: dimmed cards stay tappable to hear them again; a pinned detail can be unpinned by tapping it.
- Tie It Together: a right string stays; tapping a tied card again does nothing but read the link.
- Motion off: no flips, flights or string animation; pieces and pages appear at their end states on the same timing.
- Nothing is saved.

## Look
- Accent `--brand` #8a4f00 deep honey amber (header, Start the case, labels); gold #f5c542 for step buttons and the tour labels; paper #fdf8ec; ink #2b2112; muted #625844. Scene: a sunny print shop floor with paper stacks; the case board is cork with red string.
- Contrast (WCAG 2.1, computed): white on brand 6.56:1; brand on paper 6.19:1; ink on paper 14.91:1; muted on paper 6.61:1; ink on gold 9.74:1.
- Never color alone: right gets a check icon; dimmed cards get a faded look and a small x icon; labels are words on gold.
- Different from the K ELA neighbors (letter-lanterns night indigo) and this batch (plum, brick, pine, blue).

## Art
Local FLUX (`scripts/localart.py`); no people (the makers are animals). Bruno's paintings are in a soft watercolor style different from the shop's flat gouache, so "the pictures" look like one artist's work.
- shop-floor: "A sunny print shop floor with paper stacks and a wooden table at the back, flat gouache, the middle of the floor clear"; 16:9; cutout no; people no; the Mix-up backdrop.
- olive-stand, olive-nod, olive-shake, olive-read: "A friendly brown owl with round glasses holding a notebook and a pencil, <standing / nodding / shaking head / reading aloud>, flat gouache, plain white background"; 3:4; cutout yes; people no.
- bruno-stand, bruno-nod, bruno-shake, bruno-paint: "A friendly brown bear in a paint-spotted apron holding a paintbrush, <...the same poses, painting>, flat gouache, plain white background"; 3:4; cutout yes; people no.
- desk: "A small wooden writing desk with a notebook and a jar of pencils, flat gouache, plain white background"; 4:3; cutout yes; people no. easel: "A wooden easel with a blank canvas and a paint palette, flat gouache, plain white background"; 3:4; cutout yes; people no.
- bee-1 to bee-5 and bee-cover (Bruno's paintings, Content subjects): "<subject>, soft watercolor picture book illustration"; 4:3 (cover 3:4); cutout no; people no; each with hotspot coordinates set by the builder on the target part.
- book-closed-front, book-closed-back, book-spine: "A closed hardcover picture book <front cover blank / back cover blank / seen from the spine>, flat gouache, plain white background"; 3:4 (spine 1:4); cutout yes; people no; the cover painting and words are composited in code.
- endpaper: "A honeycomb pattern endpaper, warm yellow, flat gouache, full frame"; 3:4; cutout no; people no.
- case-board: "A cork board with pushpins in the corners, flat gouache, the cork empty"; 16:10; cutout no; people no.
- your-book: "A child's hand pointing at the cover of a picture book on a classroom table, flat gouache"; 4:3; cutout no; people yes (a hand only; Gemini, `people: true`).
23 images; 1 with people (a hand). Drawn in code: word strips, cards, labels, the string, the library card, the smudge, the bar code, all controls.

## Voice
Bank voice `upbeat-guide` (style "Say brightly and clearly, like an upbeat tour guide"): the case guide who leads the class through the print shop; Olive and Bruno speak through the same voice (their lines are short and named on screen with their faces). Not used by any K ELA tool specced so far or by the other four in this batch. `Curio.voice` with `scope: () => state.step + ':' + state.part`, `welcomeAfter: true`.
- event `start` (Start the case): "Oh no! The new bee book fell apart at the print shop."
- how `welcome`: "Let's be book detectives. We'll find who made each piece and put the book back together."
- how `sortHow`: "Tap a piece to hear it. Then tap Olive if it's words, or Bruno if it's a picture."
- event `pieceRead`: the strip's words, or "A picture of {subject}."
- event `sortYes` (each right): "Thanks!" from that maker (2 variants). event `sortNo`: Olive "I write the words. Bruno makes the pictures." or Bruno "I paint the pictures. Olive writes the words."
- event, whole, `jobs`: Olive's then Bruno's job lines (Content).
- how `namesHow`: "Put the names back on the cover. Who wrote the words? Tap a face."
- event `namesYes` / `namesNo`: "Words by Olive Owl. Pictures by Bruno Bear!" / "Look again. Who writes the words?"
- how `matchHow`: "Tap Olive's words to hear them. Then tap the picture that shows them."
- event `matchYes` / `matchNo`: "Page {n}!" / "My picture shows {its subject}. Look for {strip subject}."
- event, whole, `pointAsk` / `pointYes` / `pointNo`: "Point to the {thing}." / "Yes, the {thing}!" / "That's {the thing tapped}."
- how `tourHow` (Book Tour): "Every book has a front cover, a back cover and a title page. Tap the front cover."
- event, whole, `tourAsk`: the task line. event `tourYes`: "Yes, the {part}!" event `tourNo`: "That's the {part tapped}." (plus, for page 1: "The title page comes before it.")
- event, whole, `bookPage` (Read the book): each page's words.
- how `topicHow`: "What is this whole book mostly about? Tap a card."
- event `topicYes`: "Yes! The whole book is about bees." event `topicNo`: "Some pages tell about {it}. Is the whole book about {it}?"
- how `detailHow`: "Now pin two details this book tells about bees."
- event `detailYes`: "Yes, this book tells that. Tap Show me, then tap the page." event `detailNo`: "That may be true, but this book doesn't tell it. Look at the pages." event `showYes`: "There it is, on page {n}!"
- event, whole, `sayIt`: "This book is about bees. It tells that {detail 1} and {detail 2}. Now you say it!"
- how `tieHow`: "Tap a card on the left, then the card it leads to on the right."
- event, whole, `tieYes`: the link line. event `tieNo`: "Snap! Those don't go together. Try another."
- event, whole, `closed`: "Case closed! Busy Bees, words by Olive Owl, pictures by Bruno Bear. It is about bees."
- how `yourBook`: "Find a book in your classroom. Who wrote the words? Who made the pictures? Look on the cover!"
Read speaks the hint, which always names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Who made it (RI.K.6) | Guess; send everything to one maker | Guess 50 percent a piece; all twelve by chance 1 in 4,096; 6 words and 6 pictures, so one maker gets half; each wrong send is answered with the maker's job, which is the lesson. |
| Cover names | Guess | Two faces, two lines; a wrong pick repeats the job question. Low stakes by design: the jobs were just heard. |
| Put the pages back (RI.K.7) | Guess; elimination (the last pair is forced); matching by color | First guess 1 in 5, all five by chance 1 in 120; the last page is forced, so it is the Point to it step after it (a tap on the thing the words name) that checks that page; strips are word strips with no picture, and paintings share one palette. |
| Point to it (RI.K.7) | Tap the biggest thing; tap the middle | Targets differ in size and place per page (legs, hive, flower, honey, pollen); the target is the biggest thing only on page 2 (the hive); on pages 1 and 5 it is a small part of the bee (the legs, the pollen), and on 3 and 4 it is beside the bee. Wrong taps are named aloud. |
| Book Tour (RI.K.5) | Tap whatever faces up; tap the first page after opening | Front cover: the spine is also tappable; back cover: needs Turn over; title page: the first thing after opening is the endpaper, and page 1 is next to the title page, so "first page" and "the page with words" both fail; each wrong part is named. |
| Topic (RI.K.2) | Guess; the biggest card; the title word | Guess 1 in 3; cards are one size and shuffled; "Busy Bees" on the cover names the topic, and using the title is a real way to find a topic, so that is not a beat. Flowers and Honey are each in two pages (the common wrong answer), and the line asks the whole-book question. |
| Details (RI.K.2) | Guess; anything true about bees | Two right by chance 3 in 10 (computed: 3 of 5 cards are in the book); "Bees can sting" is true but not in this book, so "true facts" fail; each pinned detail also needs Show me on the right page. |
| Tie It Together (RI.K.3) | Guess; elimination; same-word matching | First link 1 in 3, all three 1 in 6; no cause card shares a content word with its result except "Bees", which starts two of the three result cards, so word matching cannot settle any link; "nectar" and "pollen" appear on no result card. |

## Heard in order
Waits means the next line waits for it to finish; taps always act at once and never wait for a line.
1. Load, tap Start the case: `start`, then `welcome` (welcomeAfter), then `sortHow`. Next action spoken in `sortHow`.
2. The Mix-up: a piece tap: `pieceRead`; a send: `sortYes` or `sortNo`. All home: `jobs` (whole), then `namesHow`; then `namesYes`/`namesNo`. Part 2: `matchHow` (first), then per strip tap the strip's words, per picture tap `matchYes`/`matchNo`; after each page: `pointAsk` (whole), the tap, `pointYes`/`pointNo`. Feedback plays before the next `pointAsk`, which waits for it.
3. Book Tour: `tourHow` (first), then each `tourAsk` (whole), `tourYes`/`tourNo`; the next ask waits for the feedback.
4. Big Idea: `bookPage` 1 to 5 in order (whole each) when Read the book is on; `topicHow`, `topicYes`/`topicNo`; `detailHow`, `detailYes`/`detailNo`, `showYes`; then `sayIt` (whole).
5. Tie It Together: `tieHow`, then `tieYes` (whole) or `tieNo` per pair. Then `closed` (whole), then `yourBook`.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.K.2, RI.K.3, RI.K.5, RI.K.6, RI.K.7 wording (main topic and key details; connection between two pieces of information; front cover, back cover, title page; author and illustrator and their roles; illustrations and the text) | Common Core State Standards, ELA, RI/K page, thecorestandards.org | CCSS ELA 2010 PDF, Reading Standards for Informational Text K to 5 (the official document) | yes |
| Bees are insects with six legs and four wings (two pairs) | USDA Forest Service, "Bee basics: an introduction to our native bees" | Penn State Extension, "Honey bee biology" | yes |
| Honey bees live together in a colony in a hive | Penn State Extension, "Honey bee biology" | USDA Agricultural Research Service, "Honey bee" pages | yes |
| Bees drink nectar from flowers and make honey from nectar, stored in the hive | USDA ARS, honey bee pages | National Honey Board, "How honey is made" | yes |
| Pollen sticks to a bee's hairy body and is carried to other flowers, which lets flowers make seeds (pollination) | USDA Forest Service, "Bee basics" / pollinator pages | U.S. Fish and Wildlife Service, "Pollinators" | yes |
| Bees can sting (a decoy detail: true, but not in this book) | Penn State Extension, "Honey bee biology" | USDA ARS, honey bee pages | yes |
Backed twice: 6. Cut: 0. Olive, Bruno, the book and Hollow Tree Books are our own; teacher notes say real books are made by real people and suggest the Your book card for that.

Checks run (Python, 2026-11-08): two details right by chance 0.3 (3 in 10); all three links by chance 1 in 6; all five page matches 1 in 120; all twelve maker sends 1 in 4,096. Contrast ratios (scratchpad b1/checks.py) as in Look.

## Done when
1. Focus and fold: at 1366x768 each step's focus (the floor and both workplaces; the book frame and paintings; the closed book; the case board) and its controls show with no scroll; at 680x425 the focus and next control show with 10 px or larger text.
2. The Mix-up: all twelve pieces go only to the right maker; wrong sends say the job; the jobs play once all are home; the cover names come back. (RI.K.6)
3. Every page is rebuilt only by its right picture; Point to it glows the named part on all five pages and names any wrong tap. (RI.K.7)
4. Book Tour: front cover, back cover (after Turn over) and title page (after the endpaper) each take only the right part; wrong parts are named. (RI.K.5)
5. Big Idea: only Bees takes the center; only the three in-book details pin, each proved by Show me on its page; Say it plays with the pinned details. (RI.K.2)
6. Tie It Together: only the three right pairs hold a string; each reads its "so" line. (RI.K.3)
7. Case closed reads the library card; the Your book card plays. (RI.K.6)
8. Tap while it plays: a piece, card or step tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every piece, card, question and next action is spoken; every choice is a picture; a child alone can close the case.
10. Voice: how lines play once each; feedback lines every time; no line names a locked step.
11. Motion off: no flips or string animation, same pacing; no network requests; nothing saved.

## Open questions
- None for Cory.
