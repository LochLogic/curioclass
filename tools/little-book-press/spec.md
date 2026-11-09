# Little Book Press

## One idea
A small print shop on screen where a child's picture book becomes a real one: draw, stamp and record or type each page, then the press publishes it two ways, as a screen book that turns its pages and plays the child's own voice, and as a single sheet of paper that prints, folds and cuts into a real eight-page mini book to hold, with the press showing every fold.

## Not like
- my-story-strip (k, concept): three panels, told aloud and labeled. Here a whole book: cover, title, author, six pages, back cover, publishing and print.
- owl-wants-more (k-2, concept): an owl asks for details that grow the picture. Here no one asks; the child chooses tools, and the point is producing and publishing.
- show-and-tell-spotlight (k-2, concept): telling an object in full sentences. Here the telling is recorded onto a page of a book.
- poem-drum (k-2, concept): records a reading in time with a drum. Here the recording is a page's words in a book.
- shakespeare-remix, personal-essay-studio, editors-in-the-margin (9-12, same format): revision studios for older writers. Here a K-2 picture-book press with stamps, a microphone and a fold-up print.

## Who and how
- Grades K-2, ELA, module "Publishing with Digital Tools" (Writing). Standards: W.K.6, W.1.6, W.2.6.
- Driver: either. On a projector the teacher models (one class book, students take turns at the board); on devices a child or a pair works, with a grown-up helping to type. tool.json `driver: "teacher"` (K-2 rule) with teacher notes on device use. Every tool button is a picture and is spoken on first use, so a child alone can make and publish a book (BASELINE rule 4).
- Modes: `Make` and `Publish` (header), with `My shelf` (up to 6 books). A book is `Just me` or `Two authors` (chosen when a book is started). tool.json `modes: ["Make", "Publish"]`, `minutes: "20-40"` (over several sessions), `grades_label: "Grades K-2"`.
- Privacy: books, drawings and recordings are saved only on this device (IndexedDB, try/catch), and the shelf says "Your books and recordings are saved only on this device." (BASELINE rule 7). Authors are named by an animal badge; typing a first name is optional and stays on the device.
- Not a personal prompt (the child picks any topic). Teacher notes: the About the author box invites a self-portrait, never personal details.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.K.6 (explore a variety of digital tools, with adult guidance, including with peers) | use the pen, stamps, backgrounds, Type, Record, Read my words and page order on their own pages; the back cover collects a stamp for each tool used | each tool button glows "new" until first used; the "Made with" row on the back cover fills with tool icons | 2, 3 |
| W.1.6, W.2.6 (use digital tools to produce and publish, including with peers) | make a cover (title, author badge, picture), at least one page with words, order the pages, and publish it as a screen book and as a print; in Two authors, pass the book page by page and leave a note on the partner's page | the Publish checklist (pictures, not a lock); the screen book playing; the print sheet with its fold guide; the author badge on every page; partner notes | 4, 5, 6 |

## Screens and modes
Header (kit): title "Little Book Press"; mode buttons (`.seg`, icon plus word, 60 px): `Make` (pencil and page), `Publish` (press icon); `My shelf` (books icon); then `Read`, `Motion`, `Sound`. Every control is 60 px or more at 1366x768 (44 px at 680x425), with an icon and a word.

**On load and first tap.** The shelf opens: a painted wooden shelf with a gold `New book` (book with a plus) and any saved books as spines. First hint: "Tap New book to start." First tap on New book opens a two-picture choice: `Just me` (one child) and `Two authors` (two children side by side), each 160 px; the choice plays its own line and the welcome is queued after it (`welcomeAfter: true`). Then each author taps an animal badge (8 badges: fox, owl, bear, rabbit, turtle, whale, lion, frog), and `Start` opens the cover in Make.

**Make.** Layout at 1366x768: tool column (left, 200 px), the page (center, a portrait page 420 x 650, aspect 0.647 to match a printed mini-book page), the page strip (right of the page, 110 px: eight thumbnails, Cover, 1 to 6, Back, each 90 px tall, the current one ringed), panel (320 px: hint, the tool's options, footer). The page is the focus and the biggest thing on screen. At 680x425: tool column becomes a row of 44 px icons above the page, the page is 230 x 355, the strip folds into `<` `>` page arrows, the panel shows only the open tool's options.
- Tools (each a 60 px button, picture plus word):
  - `Pen` (pencil): 3 sizes (dots), 8 colors (swatches with names on hover and spoken on first tap), `Eraser` (eraser icon).
  - `Stamps` (stamp icon): four trays, `Animals`, `Nature`, `Things`, `Kids` (Content), each stamp 80 px; tap a stamp, then tap the page to place it; drag to move; corner handles to size (40 to 400 px) and a `Flip` button; tap a placed stamp then `Remove` (trash).
  - `Scene` (picture frame): 8 painted backgrounds (Content) plus `Plain`.
  - `Type` (keyboard icon): a text box on the page, 3 sizes; the words sit in the lower third unless dragged.
  - `Record` (microphone): press `Record` (red dot, 120 px), speak up to 30 s, press `Stop`; `Play` plays it; `Again` replaces it. A page with a recording shows a small speaker badge.
  - `Read my words` (speaker): reads the page's typed words aloud with the browser voice (typed text has no recorded clip; the hint says "This is the computer's voice").
  - `Undo` (curved arrow, 20 steps) and `Clear page` (with a confirm card: `Clear it` / `Keep it`).
- Cover: a title box (Type, big), the author badge(s) placed automatically ("by" plus the badges and any typed names), and the page to draw on. Back cover: an About the author box (draw yourself or a favorite thing) and the "Made with" row (tool icons, filled automatically).
- Page order: in the page strip, drag a thumbnail (pages 1 to 6 only; covers stay put), or select it and tap `Earlier` / `Later` (arrow buttons under the strip).
- Two authors: each page belongs to the author whose turn it is when it is first drawn on; its corner shows that author's badge. `Pass` (two hands passing a book, gold) shows a full-stage curtain "{badge}'s turn. Tap I'm ready." with the next author's badge; behind it the book waits. Either author can open any page; on the partner's page the `Note` tool appears (sticky note icon) with three picture notes to stick on it: `I like it` (heart), `Tell more` (speech bubbles), `Is this right?` (question mark), each placed in the margin and spoken when tapped. Notes never print.

**Publish.** A checklist card first (pictures plus words, each spoken when tapped): a title on the cover; an author on the cover; a picture on the cover; words on at least one page (typed or recorded); every page has something. Missing items show an empty box and a `Go fix` arrow that opens that page in Make. Publishing is never locked; the checklist is a reminder. Then two big buttons:
- `Screen book` (tablet icon): the book fills the stage; `<` `>` turn pages with a page-turn (Motion off: a cut); each page plays its recording (or, with `Read my words` on, its typed words by browser voice). `Read to me` plays the whole book page by page. The cover reads the title and "by" plus the badges' animal names (or typed names).
- `Print` (printer icon): a print preview of one landscape letter sheet (US Letter, with an A4 option) in 4 columns by 2 rows; the top row is printed upside down. Panel order (left to right): top row, upside down: page 4, page 3, page 2, page 1; bottom row: page 5, page 6, back cover, front cover. Dashed fold lines and one solid cut line (the middle of the horizontal fold, across the two middle columns). A recording-only page prints with three writing lines under its picture ("write your words here"). `Fold guide` plays a 6-step animation (code-drawn): fold in half long ways and open; fold in half short ways; fold in quarters; open; cut the middle line; fold long ways and push the ends together, then flatten into a book. `Print` calls the browser's print (print CSS sizes the sheet). `Print big pages` (option) prints one page per sheet, portrait, for a class library.

**My shelf.** Saved books as painted spines with their cover picture; tap to open in Make; `Delete` with a confirm card; at 6 books, `New book` asks to delete one first.

## Content
- Pen colors (name, hex): black #222222, red #d63a2f, orange #f08a24, yellow #f6d32d, green #3a9a4a, blue #2f6fd6, purple #7d4cc2, brown #8a5a3b. Sizes 4, 10, 22 px at the 420 px page width (scaled with the page).
- Stamps (32): Animals: cat, dog, rabbit, bird, fish, frog, turtle, horse. Nature: tree, flower, sun, cloud, rain cloud, moon, star, mountain. Things: house, car, boat, ball, kite, cake, book, rocket. Kids (people, Gemini, `people: true`): six children of varied skin tones, hair and clothing, one using a wheelchair, standing or waving, full body.
- Scenes (8): park, beach, forest, city street, farm, outer space, under the sea, a bedroom.
- Checklist lines: "A title on the cover", "An author on the cover", "A picture on the cover", "Words on a page", "Something on every page".
- Badges: fox, owl, bear, rabbit, turtle, whale, lion, frog (two authors must pick different badges).
- Limits: 6 books, 8 pages each, 30 s of recording a page, 40 stamps a page.

## Interactions in detail
- Every tap acts at once. Drawing is pointer-based, whole-pixel, smoothed; a two-finger touch is ignored while drawing. Undo covers strokes, stamps, moves, text and scene changes on the current page.
- Saving: after every change (debounced 1 s) the page is saved (drawing as a PNG blob, stamps and text as data, the recording as an audio blob). On reopening a book everything returns. Storage full or blocked: a card says "This device can't save right now. Your book stays open until you close the page." and nothing is lost on screen.
- Microphone: the first Record asks the browser for permission; if refused, Record shows "Microphone off" and the hint suggests Type; nothing else changes. Recording never leaves the device.
- Two authors: Pass is available any time; the curtain blocks the page until I'm ready (so a partner doesn't draw by accident during a hand-off). A note can be removed by either author (tap it, then `Remove`).
- Publish with missing items: the screen book and print still work; empty pages print blank with writing lines.
- Print: the fold layout is fixed; covers are always panels 7 and 8 of the bottom row; text and stamps are drawn into each panel at print resolution (150 dpi) with a 0.25 inch safe margin inside each panel.
- Extremes: 40 stamps on a page (the 41st plays `stampFull`); a 30 s recording (stops itself); typing a very long text (it shrinks to fit, smallest 14 px at the 420 px page, then stops taking characters with `textFull`); deleting the open book returns to the shelf.
- Keyboard: Tab through tools and options; arrow keys move a selected stamp 5 px; Delete removes it; Ctrl+Z undo.

## Look
- Accent `--brand` #2a4d9b press blue (header, tool buttons, current-page ring); gold #f2c14e for New book, Pass, Publish actions; paper #f8f7f3; ink #1a1f2e; muted #545b6b. Scene: a cozy print shop: a wooden worktable, a small red press in the corner of the shelf, ink jars.
- Contrast (WCAG 2.1, computed): white on brand 7.97:1; brand on paper 7.44:1; ink on paper 15.31:1; muted on paper 6.35:1; ink on gold 9.78:1.
- Never color alone: the current tool has a ring and a check; pen colors carry names when tapped.
- Different from the K-2 ELA tools specced so far and this batch (plum, brick, pine, amber; letter-lanterns indigo).

## Art
Local FLUX (`scripts/localart.py`) in one bright, simple gouache sticker style for stamps and a warmer painted style for the shop; the Kids stamps by Gemini (`scripts/art.py`, `people: true`, Cory reviews, and a fresh agent checks the set for stereotypes and representation).
- shop: "A cozy little print shop with a wooden worktable, ink jars and paper stacks, a small red printing press on a shelf, warm light, gouache, the table top clear"; 16:9; cutout no; people no; behind Make and Publish.
- shelf: "An empty wooden bookshelf with three long shelves, warm light, gouache"; 16:9; cutout no; people no; My shelf (spines drawn in code over it).
- 24 stamps (Animals, Nature, Things): "a <object>, bright simple gouache sticker, front or side view, plain white background"; 1:1; cutout yes; people no.
- 6 Kids stamps: "a child <description>, standing and waving, full body, bright simple gouache sticker, plain white background"; 3:4; cutout yes; people yes.
- 8 scenes: "<scene>, bright simple gouache, wide and open with plenty of empty space in the middle, full frame"; 0.647 portrait (crop from 3:4); cutout no; people no.
- 8 badges: "a round badge with a friendly <animal> face, gouache, plain white background"; 1:1; cutout yes; people no.
- curtain: "A deep blue velvet stage curtain, closed, gouache, full frame"; 16:9; cutout no; people no; the Pass curtain.
48 images; 6 with people. Drawn in code: the page, tools and icons, checklist, page strip, print sheet, fold lines, the fold guide animation, notes, all controls.

## Voice
Bank voice `big-sister` (style "Say in a friendly, youthful way, like a helpful older student"): the press helper, an older student who runs the little press. Not used by any K-2 ELA tool specced so far or by the other four in this batch. `Curio.voice` with `scope: () => state.mode + ':' + state.tool`, `welcomeAfter: true`. Tools speak their name on their first tap only (how lines); the hint keeps their how-to after that.
- how `welcome` (after the first choice): "Welcome to the Little Book Press! You make the book, and the press helps you publish it."
- event `justMe` / `twoAuthors`: "A book by you!" / "A book by two authors! Take turns."
- how `badgeHow`: "Tap an animal badge. That's how your book will say who made it."
- how `coverHow` (cover opens): "This is your cover. Tap Type to give your book a title. Then draw or stamp a picture."
- how, per tool on first tap (each once): `pen` "Draw with your finger or the mouse. Pick a color and a size." `eraser` "The eraser rubs out lines." `stamps` "Tap a stamp, then tap your page to put it there." `scene` "Pick a place for your page." `type` "Type your words. A grown-up can help you spell." `record` "Tap Record and say your words. Tap Stop when you're done." `readWords` "The computer will read your typed words." `order` "Drag a page to move it, or tap Earlier or Later."
- event `recorded`: "Got it! Tap Play to hear your words."
- event `micOff`: "The microphone is off. You can tap Type instead."
- how `passHow` (Two authors, first page drawn on): "When you finish a page, tap Pass to give the book to your partner."
- event `yourTurn` (curtain): "{badge animal}, it's your turn. Tap I'm ready."
- how `noteHow` (first partner page opened): "This is your partner's page. Tap Note to tell them what you think."
- event `noteSaid` (a note tapped): "I like it!" / "Tell me more!" / "Is this right?"
- how `publishHow` (Publish opens): "Let's check your book. Then tap Screen book or Print."
- event `checkItem` (a checklist item tapped): its line, plus "Done!" or "Not yet. Tap Go fix."
- event, whole, `coverRead` (screen book cover): "{title}, by {authors}."
- how `printHow` (Print opens): "Print one sheet, then follow the fold guide to make a real little book."
- event, whole, `foldStep` 1 to 6: "Fold it in half the long way, then open it." / "Fold it in half the short way." / "Fold it in half again." / "Open it back up to the long fold." / "Cut along the middle line, between the two middle boxes. A grown-up can help." / "Fold it the long way and push the ends together. Flatten it into a book!"
- event `stampFull` / `textFull` / `saveOff`: "This page is full of stamps!" / "That's all the words that fit on this page." / "This device can't save right now."
Read speaks the hint, which always names the current action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Publish checklist (W.1.6, W.2.6) | Type gibberish as a title; one scribble per page; skip it | Not a score and never a lock (a studio: nothing to win). The checklist names what a published book has; a teacher sees the book itself. Gibberish still publishes, which is honest: the standard is using the tools to produce and publish, and the book shows what was made. |
| "Made with" row (W.K.6) | Tap every tool once without using it | Only an actual use stamps the row: a stroke, a placed stamp, a scene picked, typed words, a finished recording, Read my words played, a page moved. Tapping a tool button alone does not. |
| Two authors (W.K.6, W.1.6, W.2.6 with peers) | One child does every page; never passing | Not scored. Each page shows its author's badge, so the teacher sees who made what; the curtain makes a pass a real hand-off. |

## Heard in order
Waits means the next line waits for it to finish; taps always act at once and never wait for a line.
1. Load, first tap New book; choice tap: `justMe` or `twoAuthors`, then `welcome` (welcomeAfter), then `badgeHow`. Start: `coverHow`.
2. Each tool's first tap: its how line (once); later taps only change the hint. Record then Stop: `recorded`. A refused microphone: `micOff`.
3. Two authors: first page drawn: `passHow` (once); Pass: `yourTurn` with the curtain; first time a partner's page is opened: `noteHow`; a note tapped: `noteSaid`.
4. Publish: `publishHow`; checklist item taps: `checkItem`. Screen book: `coverRead` (whole), then each page's recording or typed words (whole), in order with Read to me; a page turn cuts the current page and plays the new one.
5. Print: `printHow`; Fold guide: `foldStep` 1 to 6 in order, each whole, each waiting for its animation step; `Next step` and `Back` act at once.
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.K.6 "With guidance and support from adults, explore a variety of digital tools to produce and publish writing, including in collaboration with peers"; W.1.6 and W.2.6 "use a variety of digital tools to produce and publish writing, including in collaboration with peers" (with guidance and support from adults) | Common Core State Standards, ELA, W/K, W/1, W/2 pages, thecorestandards.org | CCSS ELA 2010 PDF, Writing Standards K to 5 (the official document) | yes |
Backed twice: 1. Cut: 0. The tool teaches no other real-world claim.
The one-sheet mini-book layout (top row upside down: 4, 3, 2, 1; bottom row: 5, 6, back, front; cut across the middle two columns) is a craft layout the tool uses, not a fact it teaches. Two fact-check pages tried for it could not be reached (2026-11-08), so the layout was worked out by tracing the folds: after the long fold the top row sits behind the bottom row right side up; pushing the ends in makes a booklet whose outside is the bottom-right panel (front) and whose pages run along the top row from right to left, then along the bottom row from left to right, ending at the back cover beside the front. **Self-check must print one sheet, fold it by the fold guide, and confirm the page order before Refine.**

Checks run (Python, scratchpad b1/checks.py, 2026-11-08): contrast ratios as in Look. Page aspect: a letter sheet 11 x 8.5 in, in 4 by 2 panels, gives 2.75 x 4.25 in panels, aspect 0.647, used for the on-screen page so screen and print match.

## Done when
1. Focus and fold: at 1366x768 the page is the largest thing on screen, with every tool button and the page strip visible with no scroll; at 680x425 the page, the tool icon row and page arrows show with no scroll.
2. Every tool works on every page (pen, eraser, stamps with move, size, flip and remove, scenes, type, record, read my words, undo, clear) and its first tap speaks its how line once. (W.K.6)
3. The back cover's "Made with" row fills only from real uses of each tool. (W.K.6)
4. Publish shows the checklist with Go fix links; Screen book turns pages and plays each recording; the cover reads the title and authors. (W.1.6, W.2.6)
5. Print shows the 4 by 2 sheet with the top row upside down in the stated order, fold and cut lines, writing lines on recording-only pages; the fold guide plays its 6 steps; a printed, folded test sheet reads in page order. (W.1.6, W.2.6)
6. Two authors: Pass shows the curtain and the next badge; each page carries its author's badge; notes stick on a partner's page, are spoken when tapped, and never print. (W.K.6, W.1.6, W.2.6 with peers)
7. Saving: a reload brings back every book, page, stamp, text and recording; the shelf shows the on-device line; storage blocked shows the save card and loses nothing on screen.
8. Tap while it plays: a page turn, tool tap or Pass during a line or a recording acts at once; no older line plays after a newer one.
9. Pre-reader: every tool and choice is a picture and is spoken on first use; a child alone can make and publish a book.
10. Motion off: no page-turn or curtain animation, same pacing; no network requests.

## Open questions
- None for Cory.
