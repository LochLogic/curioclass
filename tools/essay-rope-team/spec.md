# Essay Rope Team

## One idea
Each paragraph of an essay is a climber on a rope team going up a mountain and each transition is the rope between them; the student lines up the climbers so each one leads to the next and ties ropes that fit the link (for example, as a result, in contrast, especially), and when the climb runs a wrong order or a rope that doesn't fit makes a climber slip and says why, so they learn that an essay holds together by its order and its links; at the summit the essay reads aloud top to bottom, and then the student writes their own and sends it up.

## Not like
- blueprint-builder (4, spec): reading and building text structures from facts. Here ordering and linking whole essays, grade 5.
- hamburger-paragraph (2, concept): one paragraph. Here a five-paragraph essay.
- sentence-train (K, concept): a train of words. Here paragraphs and transitions.
- quote-picker (4, spec): choosing and introducing quotes. Here order and links across paragraphs.
- main-idea-pinboard (3-5, spec): main idea and proof. Here essay structure.

## Who and how
- Grade 5, ELA, module "Organized Essays" (Writing). Standards: W.5.1, W.5.2.
- Driver: one student (tool.json `driver: "student"`). Every paragraph is read on tap; the student's own essay is read back by the browser's speech voice.
- Two climbs: the Opinion Climb ("Should our school start a school garden?") and the Explain Climb ("How Glaciers Shape the Land"), then the student's own climb. tool.json `modes: []`, `minutes: "30-45"`, `grades_label: "Grade 5"`.
- Saving: the student's own essay is kept in this browser; footer: "Your essay stays on this device." `Clear my essay` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.5.1a | Opinion climb: the intro climber with the opinion leads; reasons are grouped in a logical order | the rope team order | 2 |
| W.5.1b | Each reason climber carries facts and details (check the pack: two facts each) | the climber's pack with facts | 2 |
| W.5.1c | Tie ropes with linking words, phrases and clauses that fit (consequently, specifically, for this reason) | the ropes with their words | 3 |
| W.5.1d | The conclusion climber ties back to the opinion | the summit flag | 2 |
| W.5.2a, b | Explain climb: a focus intro; sections grouped with headings; facts, a definition and a quote in the right sections | climbers with heading flags and packs | 4 |
| W.5.2c, d | Ropes across sections (in contrast, especially) and precise subject words picked over plain ones | ropes and the word swap | 4 |
| W.5.2e | A conclusion related to the information | the summit flag | 4 |
| W.5.1, W.5.2 | Own climb: write your own short essay in the same frames and send it up | the student's team | 6 |

## Screens and modes
Header (kit): title "Essay Rope Team"; `Climbs`, `My climb`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A snowy mountain with a base camp and five paragraph climbers milling around, and Captain Juno, a mountain goat guide with a coil of rope. First hint: "Tap a climb to meet your team." The first tap reads the climb's title; the welcome is queued after it (`welcomeAfter: true`).

**Line up.** Five climbers, each a paragraph (tap to hear; a card shows the first sentence). The student drags them onto the rope in order from base to summit. Each climber's data holds its role (intro, reason, section, conclusion) and the order rules (the intro first, the conclusion last, a reason that depends on another after it; for the Explain climb, a definition section before the sections that use the word).

**Tie ropes.** Between each pair, a rope slot. A rope rack holds 10 linking words, phrases and clauses, each tagged by the kind of link (adds, gives an example, shows a result, contrasts, narrows down, ties back). The data says which kinds fit each joint. The student ties one rope per joint.

**Packs (Opinion).** Each reason climber has a pack with three fact cards; one doesn't belong (it backs a different reason). The student swaps it to the right climber.

**Precise words (Explain).** Three plain words in the sections glow (the ice "moves", "big rocks", "leftover piles"); the student picks the precise word (flows, boulders, moraines).

**Climb.** `Climb!` runs the team up. At the first wrong order, the climber slips back to base camp with a reason ("The conclusion can't go before the reasons. What does it tie back to?"); at a rope that doesn't fit, the rope frays ("Consequently shows a result. This paragraph gives an example."). At the summit, the whole essay reads aloud top to bottom.

**My climb.** Frames for the student's own short essay (5 boxes with role labels); the student writes each paragraph, ties ropes from the rack (or types their own link), and sends it up. Their own essay isn't graded; the climb checks only that each box is filled, each rope is tied and the conclusion box mentions a word from the intro.

At 1366x768 the mountain and paragraph reader fit side by side; at 680x425 the reader slides over the mountain.

## Content
- Opinion Climb: "Should Our School Start a School Garden?" (written for Curio Class; intro with opinion; reasons: fresh food and healthy eating, hands-on science, a calm place outside; facts sourced from USDA Farm to School and garden education research summaries; a conclusion).
- Explain Climb: "How Glaciers Shape the Land" (intro with focus; sections: What a glacier is, with a definition; How glaciers move; What glaciers carve, U-shaped valleys and lakes; What glaciers leave behind, boulders and moraines; a conclusion). One quote from a National Park Service ranger page, attributed.
- Rope rack: in addition, for example, specifically, as a result, consequently, in contrast, however, especially, for this reason, because of this; plus clauses: "this is important because", "even though".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Climbers and ropes can be swapped any time; Climb! can be pressed any time.
- With Motion off, slips are shown as a jump back with a mark, not a fall.

## Look
- Accent `--brand` #136f80 glacier teal (header, ropes, flags); gold #f4c542 (tied ropes, the summit sun); paper #f1f8f9; ink #0a2329; muted #4a5d62. Scene: a bright snowy mountain under blue sky.
- Contrast (WCAG 2.1, computed): white on brand 5.81:1; brand on paper 5.41:1; ink on paper 15.20:1; muted on paper 6.44:1; ink on gold 10.05:1.
- Never color alone: climbers carry role tags in words; frayed ropes show a mark and a word.
- Different from this batch (rover indigo, root plum, card red, chameleon green).

## Art
Local FLUX (`scripts/localart.py`), animals only.
- mountain (1); base camp (1); Captain Juno (4 poses: rope, point, think, cheer), "A friendly mountain goat climbing guide with a coil of rope and a helmet <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- climbers (5 animal climbers in helmets with packs: a marmot, a pika, a fox, a hare, a bear cub), "<animal> in a climbing helmet with a small pack, soft gouache, plain white background"; 1:1; cutout yes.
- section pictures (4): "<a valley glacier / a U-shaped valley / a moraine with boulders / a school garden>, realistic illustration, no text"; 4:3.
About 15 images. Drawn in code: rope, slots, packs, flags.

## Voice
Bank voice `firm-captain` as Captain Juno (unique in this batch); paragraphs are read by `science-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.climb + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "A strong essay climbs together. Line up your paragraphs so each one leads to the next, then tie ropes that fit."
- event, whole, `para`: the tapped paragraph.
- how `ropeHow`: "Pick a rope for this joint. Does the next paragraph add, give an example, show a result or contrast?"
- event `slip`: the joint's slip reason.
- event `fray`: "{Consequently} shows a result. This paragraph {gives an example}."
- event `summit`: "Summit! Listen to your essay from the bottom up." then the essay (whole).
- how `ownHow`: "Your turn. Write each paragraph, tie your ropes, and send your team up."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: rope team order, rope rack with link kinds, packs, word swap, climb run.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Try orders until it climbs | 5 climbers with the intro and conclusion fixed leave 3! = 6 middle orders, and each slip says why (checked); the order rules accept 1 (Explain) or 3 (Opinion). |
| Ropes | Use "in addition" everywhere | Joints that need a result or contrast fray; at least two joints per climb need a different kind (checked). |
| Packs | Leave the stray fact | The climb stops: "This fact backs a different reason." |
| Own climb | Leave boxes empty | Each box must have text; the essay itself is not scored. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a climb: title, `welcome` (queued, first time).
2. Paragraphs: `para` (whole). First joint: `ropeHow`.
3. Climb!: `slip` or `fray` at the first fault, or `summit` and the essay.
4. My climb: `ownHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.5.1 and W.5.2 wording | thecorestandards.org, Writing Grade 5 | CCSS ELA 2010 PDF | yes |
| A glacier is a body of dense ice that forms from compacted snow over many years and flows under its own weight | National Snow and Ice Data Center, glacier basics | USGS, glaciers and ice sheets | yes |
| Glaciers carve U-shaped valleys and lake basins and leave boulders and moraines | National Park Service, glacial landforms | USGS, glacier landforms | yes |
| School gardens support science learning and healthy eating | USDA Food and Nutrition Service, Farm to School and school gardens | CDC, school gardens and healthy eating (school health resources) | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b14, 2026-11-09): 3 middle climbers give 6 orders, with 1 accepted for the Explain climb and 3 for the Opinion climb under the order rules (reasons may come in any order that keeps fresh food before the calm place it leads to); each climb has at least two joints needing a non-adding rope; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the mountain and reader fit; at 680x425 the reader slides over.
2. The Opinion climb checks order, packs and the conclusion. (W.5.1a, b, d)
3. Ropes fit by link kind; misfits fray with a reason. (W.5.1c, W.5.2c)
4. The Explain climb checks sections, the definition, the quote, precise words and the conclusion. (W.5.2)
5. At the summit the essay reads top to bottom.
6. My climb checks boxes, ropes and a tie-back word, and the essay survives a reload where storage works.
7. Print shows the finished essays.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: slips are shown as jumps with a mark; no network requests.

## Open questions
- None for Cory.
