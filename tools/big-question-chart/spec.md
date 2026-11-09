# Big Question Chart

## One idea
The class answers one big question the way real researchers do: a giant chart on the wall has a column for each part of the answer (for "How do frogs grow?": egg, tadpole, growing legs, frog), the class reads short picture pages and turns any sentence into a fact card, adds what it has seen itself as "We saw it" cards, votes on which column each card helps, sends true but off-question facts to the "Cool, but not our question" basket, and when every column has support the chart turns into a short class report, read back with where each fact came from.

## Not like
- because-bridge (k-2, spec): picking the reasons for an author's point. Here building an answer to the class's own question from several pages and the class's own experience, sorted by part of the answer.
- question-cube (k-2, spec): answering question words about a read-aloud. Here gathering facts to answer one question and writing them up.
- alike-and-different-books (k-2, spec): comparing two books in hoops. Here one question, a chart and a report.
- text-feature-makeover (1, concept): headings and glossaries that help find answers. Here the facts and the report.
- note-card-shuffle (3, concept, same family): own-words note cards sorted into categories by one student. Here a whole-class chart with picture pages, votes and "We saw it" cards.

## Who and how
- Grades K to 2, ELA, module "Class Research Projects" (Writing). Standards: W.K.7, W.K.8, W.1.7, W.1.8, W.2.7, W.2.8.
- Driver: teacher on a projector (tool.json `driver: "teacher"`). The class votes with fingers (one finger for column 1 and so on), the teacher or a helper taps the winning column. Every page, card and column is spoken and every card has a picture, so a pre-reader can take part (BASELINE rule 4).
- Three questions, tagged K, 1 and 2; any class can open any. Steps per question: Read and collect, Sort on the chart, Write our report. tool.json `modes: []`, `minutes: "15-25"` per question, `grades_label: "Grades K-2"`. Nothing is saved; `Print chart` prints the finished chart and report.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.K.7 | Pets question: the whole class collects facts and builds one shared report | the chart; the report page | 6 |
| W.K.8 | Pets question: add "We saw it" cards from home life and fact cards from the provided pages, each to the part it answers | page sentences that become cards; picture cards with an eye icon | 2 |
| W.1.7 | Seed question: the chart columns are the steps of a how-to; the report is the how-to in order (First, Next, Then, After that, Last) | five step columns; the report with order words | 3, 6 |
| W.1.8 | Seed question: facts from the pages and what the class has seen when planting | as in W.K.8 | 3 |
| W.2.7 | Frog question: read the pages on one topic, record the class tank's observations in a log, and write a report | four stage columns; the tank log; the report | 4, 6 |
| W.2.8 | Frog question: sort page facts and logged observations under the part of the question each answers | the chart with page and eye icons | 4 |

## Screens and modes
Header (kit): title "Big Question Chart"; `Questions` (chart icon); `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A classroom wall with three rolled-up charts, each with a big question and a picture: "What do pets need?" (K), "How do you plant a seed?" (1), "How do frogs grow?" (2). Mo the tortoise, the class's research helper, stands by with a pointer. First hint: "Pick a big question. Tap a chart to unroll it." The first tap unrolls that chart with its line; the welcome is queued after it (`welcomeAfter: true`).

**Read and collect.** Focus: a picture page (760 x 470) on the left with its sentences under the picture (read aloud in order, each lighting as read), page arrows, and the card tray on the right. Tap any sentence: it is read and `Make a fact card` turns it into a card in the tray with the page's book icon. A sentence already made into a card shows a check. `We saw it`: a row of picture cards of things children may have seen ("filling a water bowl"); the teacher asks "Who has seen this?" and taps the ones the class has seen to add them to the tray with an eye icon. Grade 2 adds `Tank log`: the class's tank observations, one per day, added in order as "We saw it" cards.

**Sort on the chart.** Focus: the chart (1200 x 520): the question across the top, one column per part with a picture header, and the basket "Cool, but not our question" at the side. One tray card at a time is shown big (300 x 220) and read. `Vote`: the columns get big numbers and the class holds up fingers; the teacher taps the column. Right: the card pins there with a thumbtack. Wrong: it slides back and Mo asks a question that points at the part ("Does that tell us about water?"). An off-question card dropped in a column: "That's true! Does it help answer our question?" A column with nothing pinned shows "Nothing here yet. Which page can help?"

**Write our report.** Focus: a report page (1000 x 560). For each column, in order, its pinned cards are offered as sentences; the class votes on the one to use (or the teacher types one with `Type it`). The report fills with a title (the question), an opening ("We wanted to know how frogs grow."), one sentence per column (grade 1 with order words added: First, Next, Then, After that, Last), and "We learned this from:" with the book and "What we saw". `Read our report` reads it all. `Print chart` prints the chart and the report.

At 1366x768 the page and tray, or the chart and the big card, fit above the fold. At 680x425 the page and tray become tabs and the chart columns narrow to icons with their words.

## Content
Every page and card is written for Curio Class. (P = page sentence, S = "We saw it" card; the part each answers in brackets; Off = not our question.)

**K: "What do pets need?"** Book: "Caring for Pets". Columns: Food, Water, A safe home, Play.
- P1: "Dogs and cats need food every day." [Food] "Some dogs have spots." [Off]
- P2: "Pets need fresh, clean water." [Water] "Fish need a clean tank to live in." [A safe home]
- P3: "A dog needs a warm, safe place to sleep." [A safe home] "Rabbits eat hay and fresh vegetables." [Food]
- P4: "Dogs need walks to stay healthy." [Play] "Cats like to chase toys." [Play] "A goldfish can be orange." [Off]
- S (pick the ones seen): pouring dog food [Food]; filling a water bowl [Water]; a cat bed by a window [A safe home]; throwing a ball for a dog [Play]; a dog with a red collar [Off].
- Report frame per column: "Pets need {food}." then the chosen sentence.

**Grade 1: "How do you plant a seed?"** Book: "Let's Plant a Seed". Columns in order: 1 Dig, 2 Drop it in, 3 Cover it, 4 Water it, 5 Give it sun.
- P1: "Use your finger to poke a small hole in the soil." [Dig] "Seeds come in many shapes and sizes." [Off]
- P2: "Drop one or two seeds into the hole." [Drop it in] "Cover the seeds with soil and pat it gently." [Cover it]
- P3: "Water the soil so it is damp, not soggy." [Water it] "Sunflowers can grow taller than a grown-up." [Off]
- P4: "Put the pot where it gets sun." [Give it sun] "Check the soil every day, and water it when it feels dry." [Water it]
- S: a cup of soil with a finger hole [Dig]; a bean seed in a hand [Drop it in]; a watering can [Water it]; a pot on a sunny window sill [Give it sun]; a packet of seeds with a flower on it [Off].
- Report: "Here is how to plant a seed." then one step per column with First, Next, Then, After that, Last.

**Grade 2: "How do frogs grow?"** Book: "From Egg to Frog". Columns: Egg, Tadpole, Growing legs, Frog.
- P1: "A frog starts as an egg in a pond." [Egg] "Frog eggs are soft, like little balls of jelly." [Egg]
- P2: "A tadpole hatches from the egg. It has a tail and breathes with gills, like a fish." [Tadpole] "Frogs can be green, brown or even bright blue." [Off]
- P3: "Back legs grow first, then front legs." [Growing legs] "The tail gets shorter and shorter." [Growing legs]
- P4: "The young frog climbs out of the water and breathes air with lungs." [Frog] "Grown frogs catch insects with their sticky tongues." [Frog] "Toads have bumpy, dry skin." [Off]
- Tank log (S, added in order): "Day 1: The eggs look like jelly with dark dots." [Egg] "Day 10: Tiny tadpoles are wiggling." [Tadpole] "Week 6: Back legs!" [Growing legs] "Week 9: Front legs, and a shorter tail." [Growing legs] "Week 12: A tiny frog sits on the rock." [Frog]
- Report: "We wanted to know how frogs grow." then one sentence per column, then "We learned this from: From Egg to Frog, and our tank log."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Read and collect: any page sentence can become a card, including off-question ones; the tray holds every card made. `Sort` is on once the tray has one card; the pages stay open from the chart (`Pages` button) to make more.
- Sort: cards come up in the order made; `Skip` puts one at the back. A card that slid back keeps its place for the next vote. Each column shows its count; a column with a first-vote pin gets a star.
- Report: a column with no cards is skipped in the report with a gap the class can see ("Our chart has nothing about Play yet."), and `Pages` is offered; the report can still be read.
- `Type it` takes up to 120 characters; typed sentences are read aloud and marked with a pencil icon.
- `Questions` returns to the wall; each chart keeps its cards until `Start over`.

## Look
- Accent `--brand` #3f6b21 moss green (header, chart frame, thumbtacks); gold #f2c94c (stars); chart paper #fbfaf3; ink #1d2614; muted #5b6250. Scene: a cheerful classroom wall with chart paper and markers.
- Contrast (WCAG 2.1, computed): white on brand 6.29:1; brand on paper 6.02:1; ink on paper 14.98:1; muted on paper 6.07:1; ink on gold 9.88:1.
- Never color alone: book and eye icons mark where a card came from; the basket has a picture and words; a pinned card has a thumbtack.
- Different from this batch (indigo, engine black, curtain wine, wind cyan) and the K-2 ELA neighbors.

## Art
Local FLUX (`scripts/localart.py`); no people (hands only where a card needs one, with no face).
- wall (1): "A cheerful classroom wall with three rolled charts and a cup of markers, soft gouache, no text"; 16:9; cutout no.
- mo (stand, point, think, cheer: 4): "A friendly old tortoise with round glasses holding a pointer, <standing / pointing / thinking / cheering>, soft gouache, plain white background"; 1:1; cutout yes.
- page pictures (12, one per page): "<the page's scene: a dog eating, a fish tank, a dog asleep in a basket, a cat chasing a toy, a finger poking soil, seeds dropping into a hole, a watering can over a pot, a pot in a sunny window, frog eggs in a pond, tadpoles, a tadpole with back legs, a young frog on a lily pad catching a fly>, soft gouache, simple background"; 4:3; cutout no.
- card pictures (S cards 15, page-card thumbnails reuse page pictures): "<subject>, soft gouache, plain white background"; 1:1; cutout yes.
- column headers (13): "<food bowl / water bowl / pet bed / ball / hole in soil / seed / soil mound / watering can / sun / frog eggs / tadpole / tadpole with legs / frog>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
About 45 images. Drawn in code: the chart, thumbtacks, basket, book and eye icons, the report page, every control.

## Voice
Bank voice `calm-professor` as the narrator, Mo the tortoise. Not used by the K-2 ELA neighbors or the rest of this batch. `Curio.voice` with `scope: () => state.question + ':' + state.step`, `welcomeAfter: true`.
- event `chart`: the big question.
- how `welcome`: "Hello, researchers. I'm Mo. We'll answer a big question the way scientists do: read, look, and sort what we find."
- how `collectHow`: "Tap a sentence that helps answer our question, then make it a fact card."
- event, whole, `sentence`: each page sentence.
- event `cardMade`: "Fact card!" event `sawAsk`: "Who has seen this? {Filling a water bowl}?"
- how `sortHow`: "Which part of our question does this card help? Hold up your fingers to vote."
- event, whole, `cardRead`: the card's words.
- event `pinYes`: "Yes. That helps us answer {water}." event `pinNo`: "Hmm. Does that tell us about {water}?" event `offNo`: "That's true! Does it help answer our question?" event `offYes`: "Cool, but not our question. Into the basket."
- event `empty`: "Nothing under {Play} yet. Which page can help?"
- how `reportHow`: "Our chart is ready. Let's write our report, one part at a time."
- event, whole, `report`: the report, sentence by sentence.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
research (`kit/research.js`), described in full in tools/question-sharpener/spec.md, exposed as the family's `R`. This tool uses:
- **Source**: each book is one source with `title`, `kind: "picture book"` and segments (one per sentence, with its page); the "We saw it" cards and the tank log are one source of `kind: "what we saw"`.
- **Shelf and Reader**: one book per question, read page by page; picking a segment makes a note.
- **Note**: `kind: "idea"`, `from` the segment; no closeness check (the cards are the page's own words, said so in the report's "We learned this from").
- **Board**: the chart, with the columns as categories and the basket as Unsorted; the `empty` readout is used.
- **Cite**: `R.cite(source, 'simple')` for the "We learned this from" line.
Not Trace, Conflicts, Weight, Matrix, Question or Store.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort a card | Vote at random; put everything in one column | 1 in 5 (K, grade 2) or 1 in 6 (grade 1) per card; wrong pins slide back with a question about the part; stars only for first-vote pins. |
| Off-question cards | Pin every true fact | Off cards are true and about the same animals or plants (spots on dogs, frog colors, sunflower height), so "it's true" does not decide; they only fit the basket. |
| Grade 1 steps | Pin by picture look | Water it has two cards from different pages; Dig and Drop it in pictures both show soil and a hand; the order words in the report follow the columns, so a wrong pin reads out as a wrong how-to. |
| Report | Skip the chart and type anything | A typed sentence is marked with a pencil, and a column with no pins shows its gap in the report; the report can be printed with gaps but not hidden. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a chart: `chart`, `welcome` (queued, first time), `collectHow`, then the page's `sentence`s (whole, each waits).
2. Sentence taps read at once; `cardMade` on Make a fact card; `sawAsk` per "We saw it" card when shown.
3. Sort: `sortHow` (first), per card `cardRead` (whole), then after the vote `pinYes`, `pinNo`, `offNo` or `offYes`; `empty` when the chart is opened with an empty column.
4. Report: `reportHow`, then `report` (whole).
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.K.7, W.K.8, W.1.7, W.1.8, W.2.7, W.2.8 wording (shared research and writing projects; how-to books and a sequence of instructions; read books on a single topic to produce a report and record science observations; recall information from experiences or gather information from provided sources to answer a question) | thecorestandards.org, Writing K-2 | CCSS ELA 2010 PDF | yes |
| Pets need daily food, fresh water, safe shelter and exercise or play; rabbits eat hay and fresh vegetables | ASPCA, "General dog care", "General cat care" and "Rabbit care" | American Veterinary Medical Association, pet care pages | yes |
| Planting a seed: a small hole, one or two seeds, cover with soil, keep damp not soggy, give light; sunflowers can grow taller than an adult | University of Illinois Extension, "Starting seeds" / "Sunflowers" | Royal Horticultural Society, "Sowing seeds" and "Sunflowers" | yes |
| Frog life cycle: eggs in water in jelly, tadpoles with tails and gills, back legs then front legs, tail shrinks, young frog breathes with lungs; adults catch insects with sticky tongues; eggs hatch in about one to three weeks and tadpoles become frogs over weeks to months | National Wildlife Federation, "Frogs" | Smithsonian's National Zoo, "Frogs" and USGS Amphibian Research, frog life cycle | yes |
| Frogs can be green, brown or bright blue (poison dart frogs); toads have bumpy, dry skin | Smithsonian's National Zoo, "Blue poison dart frog" | San Diego Zoo Wildlife Alliance, "Frogs and toads" | yes |
Backed twice: 5. Cut: 0. The tank log's days are a model class tank ("about", per the frog row), said so on its card: "Our tank's frogs grew on their own schedule."

Checks run (Python, scratchpad b4, 2026-11-08): every card has exactly one right place; counts per column (K: Food 3, Water 2, A safe home 3, Play 3, Off 3; grade 1: Dig 2, Drop it in 2, Cover it 1, Water it 3, Give it sun 2, Off 3; grade 2: Egg 3, Tadpole 2, Growing legs 4, Frog 3, Off 2); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the page and tray (or chart and big card) show with no scroll; at 680x425 as tabs.
2. Pets: every card pins only in its column or the basket; "We saw it" cards carry the eye icon. (W.K.8)
3. Seed: the five step columns in order; every card pins only in its step; the report uses First, Next, Then, After that, Last. (W.1.7, W.1.8)
4. Frogs: the tank log adds five cards in order; every card pins only in its stage; off cards only in the basket. (W.2.7, W.2.8)
5. Empty columns show the empty readout on the chart and a visible gap in the report.
6. Report: one sentence per column, the opening and "We learned this from" with the book and what we saw; Read our report reads it whole; Print chart prints chart and report on two pages. (W.K.7, W.1.7, W.2.7)
7. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
8. Pre-reader: every page, card and column is spoken; every card has a picture.
9. Motion off: cards move without sliding; no network requests; nothing saved.

## Open questions
- None for Cory.
