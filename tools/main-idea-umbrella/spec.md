# Main Idea Umbrella

## One idea
Every detail in a text is a raindrop, and a main topic is an umbrella that has to be just the right size: too small ("bees eat nectar") and drops splash through, too big ("animals") and it catches rain from other stories too and wobbles in the wind; the class sizes one umbrella for each paragraph and one big umbrella for the whole text, then hangs the steps of a process or the events of history on a rain chain, where a link in the wrong place stops the water from running down.

## Not like
- headline-writer (3, concept): main idea of a news story with supporting details. Here the main topic and each paragraph's focus of a grade 2 text, sized by coverage.
- text-feature-makeover (1-2, spec): features that help you find facts. Here what the text is about.
- author-s-mailbox (2, spec): why the author wrote it. Here what it is about and how its parts connect.
- because-bridge (k-2, spec): joining a point to its reason. Here a chain of steps or events.
- first-next-last (1, spec): writing steps for a robot. Here reading steps and events in someone else's text.

## Who and how
- Grade 2, ELA, module "Main Idea and Connections" (Reading Informational Text). Standards: RI.2.2, RI.2.3.
- Driver: a pair at one device or the teacher on a projector (tool.json `driver: "either"`). Every sentence and tile is read on tap (BASELINE rule 4).
- Three texts: `Busy Honeybees` (science), `From Seed to Tree` (science), `The Wright Brothers Learn to Fly` (history). Each: `Umbrellas`, then `Rain Chain`. tool.json `modes: []`, `minutes: "15-20"`, `grades_label: "Grade 2"`. Nothing is saved.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.2.2 | For each paragraph, pick the umbrella label that covers every detail drop and no drops from elsewhere | drops caught or splashing; a wobbling too-big umbrella | 2, 3 |
| RI.2.2 | Build the big umbrella for the whole text over the paragraph umbrellas | the small umbrellas tucked under the big one | 4 |
| RI.2.3 | Hang steps (science) or events (history) on the rain chain in order, and pick the link word that connects each pair | water running down the chain cup by cup | 5, 6 |

## Screens and modes
Header (kit): title "Main Idea Umbrella"; `Texts`; `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word.

**On load and first tap.** A rainy storybook street with Drizzle the duck in a yellow raincoat under a bare umbrella frame. First hint: "Tap a text to start." The first tap opens the text with its line; the welcome is queued after it (`welcomeAfter: true`).

**Umbrellas.** Focus: the text on the left (three paragraphs, each with a small picture, 560 x 520), and the street on the right (640 x 520) with a cloud over it. Tap a paragraph: it lights and its details fall as raindrops, each drop carrying a few words of one detail ("drink nectar"). Below, the label rack: four umbrella labels for that paragraph (too small, right, too big, off topic), each on a canopy of its size. Drag a label onto the frame (or tap it). The umbrella opens over the drops:
- Right: every drop lands on the canopy and rolls off into a puddle; a sun peeks out.
- Too small: the canopy is narrow; the drops it misses splash, and Drizzle reads one missed detail ("This one isn't about drinking nectar").
- Too big: the canopy is huge and drops from another text (a frog, a fish) blow in from the side and land on it; it wobbles, and Drizzle says "This umbrella catches rain from other stories too."
- Off topic: the drops fall right through.
**Big umbrella.** After the three paragraph umbrellas, they shrink and stand side by side; four big labels; the right one opens above all three, and each small umbrella tucks under it.

**Rain Chain.** A rain chain hangs from the roof gutter with cups (four or five). The class drags step or event cards onto the cups in order, then picks a link word between each pair: `then` (it just happens next) or `so` (the first one makes the second happen). `Pour`: water runs from the gutter down cup by cup; at the first out-of-order card the water stops and spills, and Drizzle reads the two cards ("Can a bee fan nectar into honey before it brings the nectar home?"). A wrong link word ("then" where the first makes the second happen) makes the water drip slowly and Drizzle reads the pair with the word.

At the end, a summary card: the text's main topic and one line per paragraph's focus, read aloud.

At 1366x768 the text and street fit above the fold. At 680x425 the street sits above the text, and the text scrolls inside its card.

## Content
All texts written for Curio Class.

**Busy Honeybees.** P1 (focus: what bees eat): Honeybees drink sweet nectar from flowers. They also eat pollen, a yellow dust in flowers. Young bees are fed a food called royal jelly or bee bread. Drops: drink nectar | eat pollen | young bees fed. Labels: "bees drink nectar" (too small) | "what bees eat" (right) | "animals and food" (too big) | "how bees fly" (off topic).
P2 (how bees make honey): A bee sips nectar and carries it home in its honey stomach. Inside the hive, bees pass the nectar to other bees. They put it in wax cells and fan it with their wings until it gets thick. Then they cap the cell with wax. Labels: "wax cells" | "how bees make honey" | "things bees make and do" | "what flowers look like".
P3 (how bees help plants): When a bee visits a flower, pollen sticks to its fuzzy body. At the next flower, some pollen rubs off. This helps the flower make seeds and fruit, like apples. Labels: "fuzzy bees" | "how bees help plants" | "how animals help the world" | "bee stings".
Big umbrella: "honeybees and how they live and help" (right) | "nectar" | "insects" | "a picnic".
Rain chain (how bees make honey, 5 cups): sip nectar from a flower | carry it home | pass it to other bees | fan it in wax cells | cap the cells. Links: then, then, then, so (the honey is thick, so they cap it).

**From Seed to Tree.** P1 (what a seed needs), P2 (how it sprouts), P3 (how a tree grows). Rain chain (5): a seed falls to the ground | rain soaks it | a root grows down | a shoot pushes up | leaves use sunlight to make food and the tree grows taller. Links: then, so, then, so (the leaves make food, so the tree grows).

**The Wright Brothers Learn to Fly.** P1 (who they were: brothers who ran a bicycle shop in Dayton, Ohio), P2 (how they tested: kites and gliders at Kitty Hawk, North Carolina), P3 (the first flight: December 17, 1903, 12 seconds). Rain chain (5): they watched birds and read about flying | they built a kite to test wing-warping (1899) | they flew gliders at Kitty Hawk (1900 to 1902) | they built a light engine and propellers | Orville flew for 12 seconds (1903). Links: so, then, then, so (the engine made it possible, so Orville flew).
Each text's labels follow the same four-size pattern. Canopy widths: too small < right < too big; off topic is drawn second widest in sets 1 and 3 of each text (so the right label is second narrowest) and narrowest in sets 2 and 4 (so the right label is second widest); drop texts from other texts (frog, fish) blow onto too-big umbrellas.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each label shows its canopy width before it is dropped, but width alone does not give the answer: the right label is the second widest in 2 of 4 positions and the off-topic one varies in width.
- A wrong umbrella closes after 2 s and returns to the rack; the paragraph's star counts first tries.
- Rain chain: cards can be swapped between cups; `Pour` checks all cups and stops at the first problem; link words are checked after the order is right.
- `Start over` per text, one confirm.

## Look
- Accent `--brand` #3a5a78 rain blue-gray (header, frames, rain chain); gold #f4c542 (umbrella canopies when right, stars, Drizzle's raincoat); paper #f4f7fa; ink #14202b; muted #4f5d6a. Scene: a rainy storybook street with shop awnings.
- Contrast (WCAG 2.1, computed): white on brand 7.21:1; brand on paper 6.70:1; ink on paper 15.36:1; muted on paper 6.29:1; ink on gold 10.16:1.
- Never color alone: right and wrong umbrellas differ by what the drops do (rolling off, splashing, falling through, wobbling) and a word line; drops carry words.
- Different from this batch (wine fable table, velvet theater, playground orange, lab purple).

## Art
Local FLUX (`scripts/localart.py`); the Wright brothers are real people, so their two pictures go to Gemini, drawn from period photographs' poses, not copied.
- street (1): "A rainy storybook street with shop awnings and puddles, soft gouache, no text"; 16:9; cutout no.
- Drizzle (4, wait, cheer, puzzled, point): "A small duck in a yellow raincoat <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- paragraph pictures (9): "<a honeybee on a flower / bees on honeycomb / a bee covered in pollen / ...>, soft gouache"; 4:3; cutout no.
- Wright pictures (2, Gemini): "two brothers in early 1900s clothes testing a glider on sand dunes"; "a 1903 biplane lifting off a sandy rail"; 4:3; cutout no.
- stray drops (4): "a frog / a fish / a cat / a car, tiny simple icon"; 1:1; cutout yes.
About 20 images. Drawn in code: umbrellas, drops, rain chain, cups, water, controls.

## Voice
Bank voice `bright-teacher` as Drizzle (unique in this batch). `Curio.voice` with `scope: () => state.text + ':' + state.step`, `welcomeAfter: true`.
- event `open`: "{Busy Honeybees}! Here comes the rain."
- how `welcome`: "Hi, I'm Drizzle! Every detail is a raindrop. Pick an umbrella that covers every drop, but no bigger."
- event, whole, `para`: the paragraph.
- event `covered`: "Every drop is covered! This part is about {what bees eat}."
- event `tooSmall`: "{This one isn't about drinking nectar.} Try a bigger umbrella."
- event `tooBig`: "This umbrella catches rain from other stories too. Try a smaller one."
- event `offTopic`: "The drops fall right through! This part isn't about that."
- event `bigOne`: "Now one big umbrella for the whole text."
- how `chainHow`: "Hang each step on a cup in order, then pick a word to link them. Tap Pour."
- event `spill`: "{Can a bee fan nectar into honey before it brings it home?}"
- event `slowLink`: "{Did sipping nectar make the bee carry it home, or did it just come next?}"
- event `flows`: "The water runs all the way down!"
- event, whole, `summary`: the main topic and each paragraph's focus.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Umbrella | Pick the biggest canopy | Too big always wobbles; the right label is not the widest in any set. |
| Umbrella | Pick the second widest | Canopy widths are drawn by data, and the right label is second widest in 2 of 4 sets per text (computed), smallest-but-one elsewhere. |
| Umbrella | Try all four | The star counts first tries. |
| Rain chain | Random order | 5 cards: 120 orders, one right (computed). |
| Link words | Always "then" | Each text has at least one "so" pair (computed). Always "so" fails every "then" pair. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a text: `open`, `welcome` (queued, first time).
2. Tap a paragraph: `para` (whole); drop a label: `covered`, `tooSmall`, `tooBig` or `offTopic`.
3. `bigOne`; then `covered` for the big umbrella.
4. Rain chain: `chainHow` (first time); Pour: `spill`, `slowLink` or `flows`; then `summary` (whole).
No line contains a bare letter or letter sound.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.2.2 and RI.2.3 wording | thecorestandards.org, RI Grade 2 | CCSS ELA 2010 PDF | yes |
| Honeybees eat nectar and pollen; larvae get royal jelly and bee bread | Penn State Extension, honey bee biology | USDA ARS, honey bee pages | yes |
| Bees make honey by passing nectar, storing it in wax cells, fanning it to thicken, and capping cells | National Honey Board, "How honey is made" | Penn State Extension, honey bee biology | yes |
| Pollen sticks to bees and transfers between flowers, helping plants make seeds and fruit | USDA Forest Service, "Bee pollination" | NPS, pollinators | yes |
| Seeds sprout a root first, then a shoot; leaves use sunlight to make food | University of Illinois Extension, seed germination | RHS (rhs.org.uk), seed germination advice | yes |
| The Wrights ran a bicycle shop in Dayton, tested a kite in 1899, flew gliders at Kitty Hawk 1900 to 1902, and Orville flew 12 seconds on December 17, 1903 | Smithsonian National Air and Space Museum, "The Wright Brothers" | NPS, Wright Brothers National Memorial | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad b7, 2026-11-08): 5-card chain orders 120; right-label width rank per set (never widest, second widest in 2 of 4 per text); each chain has at least one "so" link and one "then" link (bees 1 and 3, seed 2 and 2, Wright 2 and 2); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the text and street fit with no scroll; at 680x425 the street sits above the text.
2. Each paragraph's right label covers all its drops; the too-small one shows splashes. (RI.2.2)
3. Too-big labels wobble with stray drops; off-topic labels let drops fall through. (RI.2.2)
4. The big umbrella takes only its right label and tucks the three small ones under it. (RI.2.2)
5. Rain chain: water runs only when every card is in order; it stops at the first wrong cup. (RI.2.3)
6. Link words: each pair takes only its accepted words. (RI.2.3)
7. Summary reads the main topic and three focus lines.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Pre-reader: every sentence, drop and label is read on tap.
10. Motion off: drops appear in place, the umbrella does not wobble (a shake icon instead), water fills cups without flowing; no network requests; nothing saved.

## Open questions
- None for Cory.
