# Alike and Different Books

## One idea
The two books are the judges: the class drops picture cards into two overlapping hoops (this book, both books, that book) or the "not in either book" basket, then taps Ask the books, and each book flips through its own pages to the page that shows the card (or searches and comes up empty), so every alike and every different is proved by a real page, not by the teacher.

## Not like
- windblown-pages (k-2, concept): puts pictures and captions back on a story and a fact book and names who made them. Here nothing is put back; two whole books are compared card by card, and the books themselves check the sort.
- question-cube (k-2, concept): one read-aloud, one question at a time, tap the proof. Here two books at once, and the question is always "which book, or both?"
- big-question-chart (k-2, concept): pins facts from many pages under parts of one answer. Here facts and story parts are pinned by book, in a Venn of two books.
- read-along-shelf (k-2, concept): reading along with fading help. Here the narrator reads both books first, and the work is comparing them.
- poem-drum (k-2, concept): decides poem or story. Here the kind-of-book question is story or fact book (RL.1.5), shown by what each book has, not by a beat.
- who-said-that, word-zoo (1, concept) and word-meaning-yard (k, concept), the other early sorts: sort lines, word classes or meanings into bins. Here the bins overlap, the sort is checked against two texts, and a basket catches what neither book says.
- rhetoric-spotter (9, spec, same format): sorts speech lines and taps the words. Different band, different look; the shared move (prove the sort with the text) is done here by the books flipping, not by tapping words.

## Who and how
- Grades K-2, ELA, module "Comparing Two Books" (Reading Literature and Informational Text).
- Driver: teacher on a projector (tool.json `driver: "teacher"`); the class says where each card goes and a helper drags it. Every question, card and next step is spoken and every card is a picture, so a child alone can play (BASELINE rule 4).
- Standards: RL.K.9, RL.1.9, RL.2.9, RL.1.5, RI.K.9, RI.1.9, RI.2.9.
- Three modes (each a book pair), each with a grade tag on its button: `Runaway Tales` (K-2: characters' adventures, two versions of one tale), `Story and Facts` (1: storybook vs fact book), `Pumpkin Books` (K-2: two fact books on one topic, with a grade 2 `Big points` step). Any mode works for any grade.
- Minutes: 15 to 20 per pair. tool.json `modes: ["Runaway Tales", "Story and Facts", "Pumpkin Books"]`, `minutes: "15-20"`, `grades_label: "Grades K-2"`.
- Not a personal prompt. Nothing is stored.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.K.9 (with support), RL.1.9 | Runaway Tales: hear both tales, sort what happens to the Gingerbread Boy and the Pancake (who made them, what chases them, who eats them), Ask the books, then finish the Say it sentences out loud | the two books flip to the page with each event; cards glide to their true region; Say it frames | 2, 5 |
| RL.2.9 | Runaway Tales: the same sort read as "two versions of one tale from two lands" (United States, 1875 and Norway); Say it adds "In the tale from Norway..." frames | the book covers name where each version comes from; a small map pin on each cover | 2, 5 |
| RL.1.5 | Story and Facts: sort what each book has (a penguin who talks and has a name; labels and a real place), then the Kind of book step: tap which book is the story and which tells facts, and pick the clue card that shows it | the story's speech bubbles and the fact book's labeled diagram flip into view; the Kind of book tags | 3 |
| RI.K.9, RI.1.9 | Pumpkin Books: sort pictures from a book that describes how a pumpkin grows and a book of steps for growing one (illustrations, descriptions, procedures) | the describing book's growing pictures and the steps book's numbered steps flip into view | 2, 4 |
| RI.2.9 | Pumpkin Books, Big points: pick each book's most important point from three sentences (one big point, two details), then pick what both big points share | the two big points move to the hoop tops; the shared statement settles in the middle | 4 |

## Screens and modes
Header (kit): title "Alike and Different Books"; mode buttons (`.seg`, icon plus word plus grade tag, 60 px tall): `Runaway Tales` (running cookie icon, "K-2"), `Story and Facts` (speech bubble plus magnifier icon, "1"), `Pumpkin Books` (pumpkin icon, "K-2"); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), with an icon and a word.

Shared stage, drawn at real pixel size and re-laid per size:
- Top row: Book A (left) and Book B (right), each an open picture book (cover, then pages 1 to 4) at 470 x 250 at 1366x768, with page arrows under it (`<` and `>`, 60 px, arrow icon plus "Page"). The current page's words show in code under its painting (20 px, ink on paper). Each cover carries a map pin or a book-type tag (see Content).
- Middle: two overlapping hoops, 1000 x 300 at 1366x768: left hoop tinted with Book A's color and labeled with Book A's small cover, right hoop with Book B's, the overlap labeled "Both" (two small covers). Under the hoops, a basket 220 x 70 labeled "Not in these books" (basket icon).
- Panel (right, 320 px): the hint (20 px) at top, the card tray (two columns of 120 x 96 cards: picture on top, one to three words under it), then the step buttons, then the footer.
- Focus: the two books while they are read and while they flip; the hoops while the class sorts. At 1366x768: header 56, books 250 plus words 50, hoops 300, basket 70: all above the fold. At 680x425: books 220 x 118 with 12 px words, hoops 460 x 150, basket 120 x 40, tray cards 88 x 70 in one scrolling column inside the panel (the panel scroll is allowed for the tray only; the step buttons sit above the tray).

**On load and first tap.** `Runaway Tales` opens on its Read step with both books closed on their covers. Nothing speaks before the first tap (kit). First hint: "Two books about food that runs away. Tap Read the books to hear them." The first tap on `Read the books` starts reading Book A's cover (its own line), and the welcome is queued after it (`welcomeAfter: true`). Tapping a book's page arrow instead turns that book and speaks that page.

**Steps (every mode), as gold step buttons in the panel, one at a time:**
1. `Read the books` (open book icon): the narrator reads Book A cover to page 4, then Book B, turning each page as it reads (`bookPage` lines, whole). A tap on any page arrow during reading stops the reading and goes to that page (it speaks that page). `Read the books` becomes `Read again`; `Sort the cards` (gold) appears once both books have been heard to page 4 or `Skip reading` (small, under it) is tapped.
2. `Sort the cards` (cards icon): the tray fills with the mode's 10 cards in a shuffled order. Tapping a card speaks its name and picks it up (thick border); then tapping a hoop region or the basket drops it there (drag works too). A dropped card can be moved again. Tapping a placed card speaks its name. `Ask the books` (two books icon, gold) is disabled until the tray is empty (the hint says "Place every card first", and no line names Ask the books while it is disabled).
3. `Ask the books`: one card at a time, left to right, top to bottom, 1.6 s each (Motion off: the same pace, no flipping animation): each book flips to the page that shows the card (the page and the card glow) or riffles its pages and shows "Not in this book" with a small closed-book icon; then the card glides to its true region. A card already right gets a check badge; a card that moved gets a "moved" badge (swap icon). After the last card the step changes to `Say it`. A tap on a card during Ask the books jumps the check to that card (and its line); a tap on `Stop` (square icon, shown only during Ask the books) finishes all cards at once, silently, and goes to Say it.
4. `Say it` (speech bubble icon): three sentence frames over the hoops, one at a time, with a blank: "Both books have ___." "Only {Book A} has ___." "Only {Book B} has ___." Tapping any card in the matching region fills the blank and the narrator reads the whole sentence. `Next sentence` (gold) moves on; after the third, `Next sentence` becomes `New cards` in Pumpkin Books (Big points, below) or `Start over` in the other modes (back to step 2 with the cards shuffled).

**Runaway Tales.** Book A "The Gingerbread Boy" (cover tag: map pin "United States, 1875") and Book B "The Pancake" (map pin "Norway"). Say it frames read "Both tales have ___." "Only the tale from the United States has ___." "Only the tale from Norway has ___."

**Story and Facts.** Book A "Pip Wants to Fly" (story) and Book B "Penguins" (fact book). The covers carry no tags until the `Kind of book` step, which comes after Say it: two big tag buttons appear under each book, `Story` (open book with a star) and `Facts` (open book with a magnifier). The class taps one tag per book; then `Why?` shows three clue cards for the book just tagged, one right clue and two that are true of both books (Content), and the class picks the clue that tells. A wrong tag or clue gets the hint line and stays open; the right one gets a check and its line.

**Pumpkin Books.** Book A "Pumpkins" (describes how one grows; painted growth pictures) and Book B "Grow a Pumpkin" (four numbered steps and a diagram). After Say it, `Big points` (grade 2 tag "2"): over each book in turn, three sentence cards (Content), shuffled, each spoken when tapped; the class picks the book's most important point. A pick shows a check (right) or the hint "That is one small part. Which one tells about the whole book?" and stays open. Both big points then sit at the top of their hoops, and `What do both books do?` shows three statement cards; the right one settles in the overlap with its line.

What the picture shows for every outcome: a card on the right place shows a check badge and no move; a card on a wrong place glides to its true place with a "moved" badge; a "not in either book" card shows both books riffling and both "Not in this book" tags before it drops into the basket. The two books show the proving page side by side at the moment each card is checked.

## Content
Card pictures are painted cutouts in one neutral sticker style (thick white edge), never in either book's style, so the art never tells which book a card is from. Card words are spoken on tap.

**Runaway Tales.** Our own retellings of two traditional tales (Sources).
Book A, "The Gingerbread Boy" (watercolor, warm farm colors):
- Cover: "The Gingerbread Boy. An old tale printed in the United States in 1875."
- 1: "A little old woman and a little old man lived alone. One day the old woman baked a little boy out of gingerbread."
- 2: "When she opened the oven, out jumped the Gingerbread Boy! He ran out the door. The old woman and the old man ran after him."
- 3: "He ran past a barn full of threshers and a field full of mowers. He ran past a cow and a pig. 'I can run away from you, I can!' he called."
- 4: "Then he met a fox. Foxes can run very fast. The fox caught the Gingerbread Boy and ate him all up."
Book B, "The Pancake" (bold cut-paper, blues and yellows):
- Cover: "The Pancake. An old tale from Norway."
- 1: "A mother had seven hungry children. She fried a big, fat pancake for them."
- 2: "The pancake jumped out of the pan and rolled out the door! The mother and the seven children ran after it."
- 3: "It rolled past a man, a hen, a rooster, a duck, a goose and a gander. 'I can roll away from you!' it called."
- 4: "Then it came to a brook. A pig said, 'Sit on my snout, and I will carry you over.' The pancake sat on the pig's snout. Gulp! The pig ate it."
Cards (true place; proving pages):
| Card (spoken) | Place | Pages |
|---|---|---|
| a fox | A only | A4 |
| an oven | A only | A2 |
| a cow | A only | A3 |
| seven children | B only | B1, B2 |
| a frying pan | B only | B1, B2 |
| a brook | B only | B4 |
| a pig | both | A3, B4 |
| runs away from home | both | A2, B2 |
| gets eaten at the end | both | A4, B4 |
| a bear | neither | none |
"A pig" is in both tales on purpose: the Say it line after the check is "A pig is in both tales. Only in the tale from Norway does the pig eat it."

**Story and Facts.**
Book A, "Pip Wants to Fly" (bright cartoon gouache): Cover "Pip Wants to Fly." 1: "Pip was a little penguin. Pip wanted to fly like the gulls." 2: "Pip flapped and flapped. 'Look at me!' said Pip. But Pip did not go up." 3: "Then Pip slid into the sea. Zoom! Pip zipped through the water." 4: "'I can't fly in the sky,' said Pip, 'but I can fly in the sea!'"
Book B, "Penguins" (realistic painting, cool blues): Cover "Penguins." 1: "Penguins are birds. They have wings, but they cannot fly in the air." 2: "Penguins use their wings like flippers to swim fast under water." 3: "Emperor penguins live in Antarctica. A father keeps the egg warm on his feet." 4: "Parts of a penguin" (a labeled diagram drawn in code over the painting: beak, flipper, feet, feathers).
Cards: a penguin (both: A1, B1); swimming in the sea (both: A3, B2); wings that can't fly in the air (both: A2, B1); a penguin who talks (A only: A2, A4); a name, Pip (A only: A1); gulls in the sky (A only: A1); labels (B only: B4); an egg on a father's feet (B only: B3); a map of Antarctica (B only: B3); a polar bear (neither).
Kind of book clues: for the story, right clue "A penguin talks and has a name"; for the fact book, right "Labels and real facts"; the two wrong clues for both are "It has penguins" and "It has pictures" (true of both books, so they do not tell).

**Pumpkin Books.**
Book A, "Pumpkins" (soft colored pencil): Cover "Pumpkins." 1: "A pumpkin starts as a flat, white seed." 2: "The seed grows into a long green vine with big leaves." 3: "Yellow flowers open on the vine. Bees visit the flowers." 4: "A little green pumpkin grows. Then it turns orange."
Book B, "Grow a Pumpkin" (clean flat diagram style, numbered): Cover "Grow a Pumpkin." 1: "Step 1. Find a sunny spot with lots of room." 2: "Step 2. Plant seeds about one inch deep in warm soil." 3: "Step 3. Water the soil when it feels dry. A vine will grow." 4: "Step 4. Wait three or four months. Pick the pumpkin when it is orange and the stem is hard."
Cards: a seed (both: A1, B2); a green vine (both: A2, B3); an orange pumpkin (both: A4, B4); yellow flowers (A only: A3); a bee (A only: A3); a little green pumpkin (A only: A4); a watering can (B only: B3); a sunny spot (B only: B1); a calendar, three or four months (B only: B4); an apple (neither).
Big points (right one first here; shown shuffled):
- Pumpkins: "A pumpkin grows from a seed to a vine to a pumpkin." / "A little pumpkin starts out green, and then it turns bright orange." / "Bees visit the yellow flowers on the vine."
- Grow a Pumpkin: "Give a pumpkin sun, room, water and time." / "Plant each seed about one inch deep in warm soil." / "Pick the pumpkin when it is orange and the stem is hard."
What do both books do? Right: "Both tell how a pumpkin grows." Others: "Both give steps to follow." (only Book B) / "Both tell about bees." (only Book A).

## Interactions in detail
- Every tap acts at once. A page arrow tap during reading or during Ask the books stops that and turns the page. Mode buttons stop everything (V.hush) and open the new mode on its Read step, books on their covers.
- Cards: tap to pick up and tap a place, or drag (pointer, whole-pixel). Dropping outside any place returns the card to the tray. A picked card is put down by tapping it again. Keyboard: Tab to a card, Enter to pick it up, 1 (Book A), 2 (Both), 3 (Book B), 4 (basket) to drop.
- Ask the books checks every card, in reading order of where they sit. The check never waits for a line to start the next card's flip, but each card's line is queued and plays in order (whole), so the class hears every result; Stop drops the remaining lines and finishes silently.
- Say it frames take only cards in the matching region; a tap on a card elsewhere wiggles it and leaves the blank. Every card can be used in turn; the frame keeps the last one tapped.
- Start over (or a mode switch and back) reshuffles the tray and clears every badge. Nothing is saved.
- Motion off: no page flips, glides or wiggles; pages and cards appear at their end states on the same timing.
- Extremes: every card in one place (still allowed; the check moves 7 of 10); a card dragged twice; Ask the books while Read is speaking (Read stops first); a resize during Ask the books keeps the current card and its place.

## Look
- Accent `--brand` #7a3e8e plum (header, mode buttons, picked-card border); gold #f0b43c for the step buttons; paper #faf6ef; ink #231a26; muted #5e5463. Book A's hoop tint is a warm apricot, Book B's a cool sky, the overlap their blend; each hoop also carries its book's small cover, so color is never the only sign. The basket is woven brown.
- Contrast (WCAG 2.1, computed): white on brand 7.22:1; brand on paper 6.71:1; ink on paper 15.63:1; muted on paper 6.67:1; ink on gold 9.06:1.
- Check badge: green with a check icon; moved badge: a swap icon; "Not in this book": a closed-book icon plus words.
- Different from the K-2 ELA tools already specced: letter-lanterns #1B1A3A night indigo; the others in this batch (big-book-pointer brick #a8431e, class-phone-call pine #2d6a4f, little-book-press blue #2a4d9b, meet-the-book-makers amber #8a4f00).

## Art
Each book has its own illustration style, so illustration differences are there to compare (RI.K.9). Local FLUX (`scripts/localart.py`) except the people pages (Gemini, `scripts/art.py`, `people: true`, Cory reviews). Text stays in code on blank page areas.
- ginger-1 to ginger-4, ginger-cover: watercolor, warm farm colors, one per page as in Content (an old woman and old man in a farm kitchen; the Gingerbread Boy leaping from the oven; threshers in a barn and mowers in a field, a cow and a pig; a fox by a stream with the Gingerbread Boy); 4:3; cutout no; people yes on 1 to 3 (Gemini), no on 4 and the cover (a gingerbread boy on a plate).
- pancake-1 to pancake-4, pancake-cover: bold cut paper, blues and yellows (a mother and seven children at a stove; the pancake rolling out a door with the family chasing; a man, hen, rooster, duck, goose and gander along a road; a pig with the pancake on its snout at a brook); 4:3; cutout no; people yes on 1 to 3 (Gemini), no on 4 and the cover.
- pip-1 to pip-4, pip-cover: bright cartoon gouache (a small penguin watching gulls; flapping on the ice; sliding into the sea; zooming underwater); 4:3; cutout no; people no.
- penguin-1 to penguin-4, penguin-cover: realistic painting, cool blues (emperor penguins on ice; one swimming underwater; a father with an egg on his feet in Antarctica, with a small inset globe; one standing side-on, plain background for the code labels); 4:3; cutout no; people no.
- pumpkin-1 to pumpkin-4, pumpkin-cover: soft colored pencil (a flat white seed in soil; a vine with big leaves; yellow flowers with bees; a small green pumpkin and a ripe orange one); 4:3; cutout no; people no.
- grow-1 to grow-4, grow-cover: clean flat diagram style (a sunny open garden bed; seeds in soil with a depth line; a watering can over soil and a young vine; a calendar page beside an orange pumpkin with a hard stem), number areas left blank for code; 4:3; cutout no; people no.
- Cards: 30 sticker cutouts in one neutral sticker style with a thick white edge (each card's object from Content: fox, oven, cow, seven children (people yes, Gemini), frying pan, brook, pig, running cookie and pancake together, an empty plate with crumbs, bear, penguin, swimming penguin, penguin flapping, speech bubble with a penguin, name tag on a penguin, gulls, labeled-diagram icon, egg on feet, Antarctica map, polar bear, seed, vine, orange pumpkin, yellow flowers, bee, green pumpkin, watering can, sun over soil, calendar, apple); 1:1; cutout yes; people yes only on seven children.
60 images; 7 with people (ginger 1 to 3, pancake 1 to 3, the seven children card). Drawn in code: hoops, basket, badges, page words, labels on the penguin diagram, step numbers, map pins, all controls.

## Voice
Bank voice `gentle-storyteller` (style "Say gently and expressively, like a grandmother reading a picture book aloud"): these are read-aloud books first. Not used by any K-2 ELA tool specced so far (letter-lanterns playful-friend, nonsense-words and hamburger-paragraph curious-librarian, sight-words and contraction-crusher warm-teacher) or by the other four in this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.step`, `welcomeAfter: true`. Repeats: how lines once per load then hint only; event lines every time.
- how `welcome` (per mode, after the first tap's own line; stale once Sort the cards is tapped): "Two books, side by side. We'll find what is alike and what is different."
- event, whole, `bookPage` (Read the books, or a page arrow): the page's words as in Content (cover lines included).
- how `readDone` (both books heard): "Now tap Sort the cards."
- how `sortHow` (Sort step opens; stale once the first card is placed): "Tap a card to hear it. Then tap where it goes: this book, both books, that book, or the basket if neither book has it."
- event `cardName` (card tap): the card's spoken name.
- how `askReady` (tray empty, first time): "Every card has a place. Tap Ask the books."
- event, whole, `cardYes` (a card already right): "{card}: yes. {where line}." event, whole, `cardMoved` (a card that moves): "{card}: the books say {where line}." Where lines: "Both books have it." / "Only {Book} has it." / "Neither book has it."
- event, whole, `pigBoth` (Runaway Tales, after the pig card): "A pig is in both tales. Only in the tale from Norway does the pig eat it."
- how `sayHow` (Say it opens): "Finish the sentence out loud. Then tap a card in the right place to check."
- event, whole, `sentence` (frame filled): the whole sentence with the card's words.
- how `kindHow` (Kind of book): "Which book is a story, and which tells facts? Tap Story or Facts under each book."
- event `kindYes` / `kindNo`: "Yes, {Book} is a {story / fact book}. Tap Why to find the clue." / "Look again at the pages. Does it tell a story or real facts?"
- event, whole, `clueYes` / `clueNo`: "Yes! {clue}. That tells it is a {story / fact book}." / "Both books have that, so it doesn't tell. Try another clue."
- how `bigHow` (Big points): "Which sentence tells about the whole book? Tap it."
- event, whole, `bigYes` / `bigNo`: "Yes. That is the big point of {Book}." / "That is one small part. Which one tells about the whole book?"
- event, whole, `bothYes` / `bothNo`: "Yes. Both books tell how a pumpkin grows. One tells what happens. One tells what to do." / "Only one book does that. Look at both big points."
- event `wiggle` (Say it, a card from the wrong region, once per frame): "That card is in a different place. Look in {region}."
Read speaks the hint, which always names the current step's action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Card sort, checked by Ask the books (RL.K.9, RL.1.9, RL.2.9, RI.K.9, RI.1.9) | Guessing; everything in Both; everything in one book's hoop; the basket for anything strange; the card's art style; tray order; Ask the books with cards still in the tray; mashing | Per mode 3 A, 3 B, 3 both, 1 neither (computed): guessing 25 percent; all in Both 3 of 10; all in one hoop 3 of 10; the basket only ever right once. Card art is one neutral sticker style in every mode, never a book's style. The tray is shuffled each time. Ask the books is disabled until every card is placed. Nothing is scored: wrong cards move with the proving pages showing, which is the lesson. "A pig" (both, but different roles) catches "the animal that eats it is only in one book". |
| Kind of book tag and clue (RL.1.5) | Tag both the same; guess; pick the first clue; pick "It has penguins" | Tags: one book is the story and one the facts, so tagging both alike is always half wrong; guess 50 percent per book, 25 percent both right. Clues are shuffled; the two wrong clues are true of both books and the line says so ("Both books have that, so it doesn't tell"), which is the RL.1.5 point. |
| Big points (RI.2.9) | Longest sentence; shortest; the one with the title word; first in the list; guess | Computed: longest wins 0 of 2 (the longest is a detail in both books: 67 and 56 characters vs big points 51 and 41); shortest wins 1 of 2; title word "pumpkin" is in 2 of 3 cards in each book; order is shuffled; guess 33 percent each. |
| What both books do (RI.2.9) | Guess; the statement naming the book with more cards | Guess 33 percent. Each wrong statement is true of exactly one book, so a student who read only one book picks wrong half the time; the line names why. |
| Say it frames | Tapping any card | A frame takes only cards from the matching region; the sentence is said by the class first, then checked by the tap. Not scored. |

## Heard in order
Waits means the next line waits for it to finish; taps always act at once and never wait for a line.
1. Load, first tap `Read the books`: `bookPage` (Book A cover) then the welcome (welcomeAfter), then `bookPage` for each page in order, each whole, each waiting for the one before; after Book B page 4, `readDone`. Next action spoken in `readDone` (Sort the cards).
2. A page arrow tap: drops queued pages, speaks that page (whole).
3. Sort: `sortHow` (first time), then `cardName` per card tap (a new tap cuts the old name). Tray empty: `askReady` (first time; hint after).
4. Ask the books: per card in order, `cardYes` or `cardMoved` (whole), each waiting for the one before; Runaway Tales adds `pigBoth` right after the pig's line. Then `sayHow`.
5. Say it: the class speaks, then a card tap plays `sentence` (whole); `Next sentence` drops nothing that is playing and queues the next frame's hint.
6. Kind of book: `kindHow`, then `kindYes`/`kindNo`, then `clueYes`/`clueNo` (whole). Big points: `bigHow`, `bigYes`/`bigNo` per pick, then `bothYes`/`bothNo`. Feedback always plays before the next prompt, which waits for it.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| "The Gingerbread Boy" was printed in St. Nicholas Magazine, May 1875: old woman bakes him, he runs from her and the old man, threshers, mowers, a cow, a pig; a fox eats him; refrain "I can run away from you, I can!" | D. L. Ashliman, "The Runaway Pancake" (folktales of type 2025), University of Pittsburgh, citing St. Nicholas vol. 2 no. 7 (May 1875) pp. 448 to 449 | Wikipedia, "The Gingerbread Man" ("first appeared in print in the May 1875 issue of St. Nicholas Magazine"; "Run, run as fast as you can" is from later retellings) | yes |
| "The Pancake" is a Norwegian tale (Asbjørnsen): a mother of seven hungry children fries it; it rolls past a man, hen, rooster, duck, goose and gander; a pig offers to carry it over a brook on its snout and eats it | Ashliman, type 2025 page, "The Pancake" (Norway), Asbjørnsen, tr. H. L. Brækstad | Asbjørnsen and Moe, Norwegian folktale collection (Norske Folkeeventyr), "Pannekaken" | yes |
| Both are versions of one tale type told in many lands | Ashliman type 2025 page (versions from Norway, Germany, England, Ireland, Scotland, the United States, Russia) | Uther, The Types of International Folktales (ATU 2025, "The Fleeing Pancake") | yes |
| Penguins are birds that cannot fly in the air; their wings work as flippers for swimming | National Geographic, "Penguins" | Australian Antarctic Division, "Penguins" | yes |
| Emperor penguins live in Antarctica; the father keeps the egg warm on his feet | British Antarctic Survey, "Emperor penguin" | National Geographic, "Emperor penguin" | yes |
| A pumpkin grows from a flat seed into a vine with large leaves and yellow flowers; bees pollinate the flowers; fruit starts green and turns orange | University of Illinois Extension, "Pumpkins and More" | University of Minnesota Extension, "Growing pumpkins and winter squash" | yes |
| Plant pumpkin seeds about one inch deep in warm soil in a sunny spot with room to spread; water when dry; harvest when fully colored with a hard rind and stem, about 90 to 120 days | University of Minnesota Extension, "Growing pumpkins and winter squash" | University of Illinois Extension, "Pumpkins and More" | yes |
| Standards wording (RL.K.9, RL.1.9, RL.2.9, RL.1.5, RI.K.9, RI.1.9, RI.2.9) | Common Core State Standards for ELA, thecorestandards.org strand pages | CCSS ELA 2010 PDF (same publisher, the official document) | yes |
Backed twice: 8. Cut: 1 ("the Gingerbread Man refrain 'Run, run as fast as you can' is the original": later retellings only, so the 1875 refrain is used). The retellings, Pip's story and the book texts are our own writing. "Three or four months" is Book B's plain wording of 90 to 120 days.
Flag for the sensitivity review: the tale from Norway is retold from a Norwegian collection; check the retelling and art (seven children, the family) are respectful and not stereotyped.

Checks run (Python, scratchpad b1/checks.py, 2026-11-08): contrast ratios as in Look. Card counts per mode 3/3/3/1, so any single place scores at most 30 percent. Big point lengths in characters: Pumpkins 51 (big), 67, 42; Grow a Pumpkin 41 (big), 49, 56; longest-card strategy 0 of 2, shortest 1 of 2.

## Done when
1. Focus and fold: at 1366x768 both books, their page words, the hoops, the basket and the panel's step button show with no scroll; at 680x425 the books, hoops, basket and the next step button show with no scroll and text is 10 px or more.
2. Every card in all three modes is checked by Ask the books against the table: each book flips to its listed page or shows "Not in this book", and the card ends in its true place with a check or moved badge. (RL.K.9, RL.1.9, RI.K.9, RI.1.9)
3. Story and Facts: Kind of book takes one tag per book and one clue; the two wrong clues explain that both books have them. (RL.1.5)
4. Pumpkin Books: Big points takes one right sentence per book; the shared statement settles in the overlap with the "what happens / what to do" line. (RI.2.9)
5. Runaway Tales: covers show "United States, 1875" and "Norway"; Say it frames name the lands; the pig line plays after the pig card. (RL.2.9)
6. Ask the books is disabled until the tray is empty, and no line names it before then.
7. Tap while it plays: a page arrow, card or mode tap during reading or Ask the books acts at once; Stop finishes every card silently; no older line plays after a newer one.
8. Pre-reader: every card, frame, choice and next action is spoken; every card is a picture; a child alone with Sound on can play each mode without reading.
9. Voice: five card taps in a row speak five names; `sortHow`, `askReady`, `sayHow` play once each.
10. Motion off: no flips or glides, same pacing; no network requests; nothing saved.

## Open questions
- None for Cory. Sensitivity review: the two retold tales and their people art (see Sources).
