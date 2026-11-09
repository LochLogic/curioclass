# Note Card Shuffle

## One idea
The student picks a question (How do octopuses hide? How does a bicycle work? What do bats eat? Who invented the ice cream cone?), reads three short kid pages, writes facts on note cards in their own words (a card that copies five or more words in a row wrinkles and asks again), and sorts the cards into the project's category pockets, and an empty or stuffed pocket shows what to look up next, so they learn that research is a loop of reading, noting and sorting, ending with a report outline.

## Not like
- research-rover (4, concept): a sources list and combining two texts. Here grade 3 notes and categories.
- big-question-chart (K-2, spec): a class question chart. Here one student's notes from three pages.
- fact-fusion (5, concept): a report from three sources. Here the outline is the end.
- main-idea-pinboard (3-5, spec): proving a main idea with pinned sentences. Here notes in your own words.
- headline-writer (3, spec): one news story's main idea. Here gathering across pages.

## Who and how
- Grade 3, ELA, module "Notes and Categories" (Writing). Standards: W.3.7, W.3.8.
- Driver: one student (tool.json `driver: "student"`). Kid pages are read on tap; typed cards are read back by the browser's speech voice.
- Four questions, each with three kid pages and four category pockets. tool.json `modes: []`, `minutes: "25-40"`, `grades_label: "Grade 3"`.
- Saving: the card box is kept in this browser (research engine Store); the footer says "Your notes stay on this device." `Clear my box` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.3.8 (recall) | Add a "something I know already" card before reading | a card with a house icon | 2 |
| W.3.8 (gather) | Read three kid pages (print-style and web-style) and highlight a fact | the highlighted sentence | 3 |
| W.3.8 (brief notes) | Write the fact on a card in a few words; copied runs of 5 words wrinkle the card | the card, flat or wrinkled | 3 |
| W.3.8 (sort) | Sort cards into category pockets; each card shows the page it came from | pockets with counts | 4 |
| W.3.7 | Fill every pocket, use all three pages, then turn the box into a report outline | the outline with headings and bullets | 5, 6 |

## Screens and modes
Header (kit): title "Note Card Shuffle"; `Questions`, `My box`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A school library desk with a card box, a pencil cup and Ms. Quill, an owl librarian. Four question cards. First hint: "Tap a question you want to find out about." The first tap reads the question; the welcome is queued after it (`welcomeAfter: true`).

**Know already.** One card: "What do you already know?" Type a few words or skip. It goes in the box with a house icon (from me).

**Read.** Three page tabs (a book page, a museum web page, a kid magazine page; all written for Curio Class). Tap a sentence to hear it; long-press or `Highlight` to mark a fact. Highlighted facts get a card slot.

**Card.** Type the fact in a few words (up to 15 words). The research engine's `R.closeness` checks the card against the highlighted sentence: a run of 5 or more identical words wrinkles the card with "Try it in your own words. Cover the page and say it to yourself first." A `Cover page` button hides the page while typing. Each card shows the page's small icon.

**Sort.** The box opens into four pockets (labeled with words and icons). Drag cards in. The pocket bar shows counts; an empty pocket says "Nothing here yet" with a `Look it up` button that opens the page holding a fact for that pocket (data); a pocket with 5 or more cards says "Crowded! Any repeats?" and lets the student merge two cards.

**Outline.** When every pocket has at least one card and cards came from all three pages, `Make outline` turns pockets into headings and cards into bullets, with the question as the title and the pages listed as sources (title and kind). The student can reorder bullets.

At 1366x768 the page and the card fit side by side; at 680x425 the card slides up over the page.

## Content
Pages are written for Curio Class from sources; each page 8 to 12 sentences; every fact sourced.
- **How do octopuses hide?** Pockets: Color change, Shape and texture, Ink, Hiding places. Facts: octopuses change color with skin cells called chromatophores; they can change skin texture to look like rock or coral; they squirt ink to escape; they squeeze into small cracks because they have no bones; a few kinds copy other animals (the mimic octopus).
- **How does a bicycle work?** Pockets: Parts, Pedaling and chain, Steering and balance, Stopping. Facts: pedals turn a crank and gear; the chain carries the turning to the back wheel; handlebars turn the front wheel; brakes press pads against the wheel or a disc; gears make pedaling easier or faster.
- **What do bats eat?** Pockets: Insects, Fruit, Nectar, How they find food. Facts: most bats eat insects; some eat fruit and spread seeds; some drink nectar and pollinate flowers; many insect-eating bats use echolocation; a few kinds (vampire bats, in Central and South America) drink blood from animals.
- **Who invented the ice cream cone?** Pockets: Early cones, The 1904 World's Fair, Who says they did it, How cones are made now. Facts: edible cones appear in recipe books before 1904; cones became popular at the 1904 St. Louis World's Fair; several people claimed to have invented the cone there, and historians don't agree who was first. The page says so plainly: this is a question with more than one answer.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be edited, merged or thrown out (to a recycle bin that can be emptied).
- The closeness check compares lowercased words without punctuation; a fact with a name or number (1904, St. Louis) is allowed to repeat those words; only 5-word runs of other words wrinkle.
- The outline prints as a one-page plan for a poster or report.

## Look
- Accent `--brand` #0e6e5c notecard green (header, pockets, tabs); gold #f4c542 (highlights, the lamp); paper #f2f9f7; ink #0b241f; muted #4a5e59. Scene: a quiet school library desk.
- Contrast (WCAG 2.1, computed): white on brand 6.17:1; brand on paper 5.78:1; ink on paper 15.29:1; muted on paper 6.48:1; ink on gold 10.04:1.
- Never color alone: pockets have words and icons; wrinkled cards also carry the note.
- Different from this batch (film-set red, cork brown, curtain plum, blueprint blue).

## Art
Local FLUX (`scripts/localart.py`).
- desk (1); Ms. Quill (4 poses: read, point, nod, cheer), "A friendly owl librarian with half-moon glasses <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- page pictures (12): "<an octopus blending into coral / a bicycle chain and gears close up / a fruit bat eating a fig / an old-time fair with an ice cream stand>, realistic illustration"; 4:3; cutout no. The 1904 fair is shown as a scene, with no real people's faces.
About 17 images. Drawn in code: cards, pockets, wrinkles, outline.

## Voice
Bank voice `curious-librarian` as Ms. Quill and the page reader (unique in this batch). `Curio.voice` with `scope: () => state.question + ':' + state.step`, `welcomeAfter: true`.
- event `question`: "{How do octopuses hide?}"
- how `welcome`: "Researchers read, take notes and sort. Start with what you already know, then read the pages and make a card for each fact."
- event, whole, `sentence`: the tapped sentence.
- how `cardHow`: "Write the fact in a few words, in your own words."
- event `wrinkle`: "Try it in your own words. Cover the page and say it to yourself first."
- how `sortHow`: "Drag each card into the pocket where it belongs."
- event `empty` / `crowded`: "Nothing here yet. Tap Look it up." / "Crowded! Any repeats?"
- event `outline`: "Look at that: your notes are an outline."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
research (`kit/research.js`), described in full in tools/question-sharpener/spec.md, exposed as `R`. This tool uses: Source (title, kind and segments only), Shelf and Reader (page tabs and sentence picking), Note (`R.note` kind paraphrase, with `R.closeness` and a run threshold of 5), Board (four pockets with `empty` and `crowded` readouts; crowded at 5), Cite (`'simple'`), Store (`ncs-box`). Not Trace, Conflicts, Weight, Matrix or Question.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Own words | Copy with one word changed every few words | Runs under 5 pass; that is close paraphrase, and the cover-page habit is the lesson. The check catches straight copying, which is the grade 3 target. |
| Outline unlock | Make cards of nonsense | Not caught; the outline shows the cards plainly. Cards must come from highlighted facts, so each has a page. |
| Pockets | Put all cards in one pocket | The outline needs every pocket filled. |
| Three pages | Use one page | The outline needs cards from all three pages. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a question: `question`, `welcome` (queued, first time).
2. Pages: `sentence` (whole); first highlight: `cardHow`; copy: `wrinkle`.
3. Sort: `sortHow`; readouts: `empty`, `crowded`.
4. Outline: `outline`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.3.7, W.3.8 wording | thecorestandards.org, Writing Grade 3 | CCSS ELA 2010 PDF | yes |
| Octopuses change color with chromatophores, change skin texture, squirt ink, fit through small gaps (no bones); the mimic octopus copies other animals | Smithsonian Ocean, octopus | Monterey Bay Aquarium, giant Pacific octopus and mimic octopus pages | yes |
| Bicycle pedals turn a crank and chainring; the chain drives the rear wheel; brakes press pads on a rim or disc | Exploratorium, Science of Cycling | Britannica, bicycle (mechanics) | yes |
| Most bats eat insects; some eat fruit and nectar and spread seeds and pollen; many use echolocation; vampire bats live in Central and South America | National Park Service, bats | Bat Conservation International, bat facts | yes |
| Cones were popularized at the 1904 St. Louis World's Fair, with several rival claims to inventing them; earlier edible cones appear in 19th-century recipes | Library of Congress, Everyday Mysteries, ice cream cone | Missouri History Museum, 1904 World's Fair ice cream cone | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad b11, 2026-11-09): every question has at least one fact per pocket across its three pages; a straight-copied sample card trips the 5-word run; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the page and card fit side by side; at 680x425 the card slides over.
2. The know-already card goes in with its icon. (W.3.8)
3. Highlighting makes card slots; 5-word copied runs wrinkle cards. (W.3.8)
4. Pockets show counts, empty and crowded readouts, and Look it up opens the right page. (W.3.8)
5. The outline needs every pocket and all three pages. (W.3.7)
6. The outline lists the pages as sources and prints.
7. The box survives a reload where storage works; `Clear my box` removes it.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: wrinkles show as a dashed border; no network requests.

## Open questions
- None for Cory.
