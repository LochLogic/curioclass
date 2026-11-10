# Who's My Baby?

## One idea
A table of face-down cards waits with a friendly guide, Hazel the owl (made up); the student flips a baby card (a spotted kitten, a duckling, a sunflower seedling, a fawn), three possible parents show, and the student picks one and taps the clue that matched (stripes, ear shape, leaf shape, beak); tricky rounds show three parents of the same kind (three cats, three dogs, three sunflowers), so the student has to look at details, and the game points out what is like the parent and what is a little different (the kitten has its mother's ears but its own spots); when a pair is matched, a short read-aloud care card with a moving picture shows what that parent does (an emperor penguin dad keeps the egg on his feet, a kangaroo carries her joey in a pouch, a crocodile carries hatchlings in her mouth to the water, a deer hides her fawn in tall grass), and the student sorts each into feeding, keeping warm, protecting or teaching; at the end a family album shows babies next to parents with "same" and "different" labels, and a care chart shows the patterns, so a first grader learns that young plants and animals are like, but not exactly like, their parents, and that parents' behaviors help their young survive.

## Not like
- puppy-traits (3, concept): inheritance and environment. Here first matches of parent and young.
- life-cycle-wheel (3, concept): stages over a life. Here a parent and its baby.
- terrarium-pal (K, spec): what living things need. Here how parents help.
- nature-inventor (1, spec): copying animal parts. Here noticing them.

## Who and how
- Grade 1, Science, module "Parents and Offspring". Standards: 1-LS1-2 (read texts and use media to determine patterns in behavior of parents and offspring that help offspring survive), 1-LS3-1 (make observations to construct an evidence-based account that young plants and animals are like, but not exactly like, their parents).
- Format: cards. Driver: one child, or two children taking turns (tool.json `driver: "either"`). Every card is spoken. Controls 56 px or more.
- 12 baby cards (8 animals, 4 plants), 4 tricky rounds, 8 care cards, the care sort, the album and chart. Extra: Two players (take turns; matched pairs count for each). tool.json `modes: ["Match", "Two players"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1-LS3-1 | Match each baby to its parent and tap the clue that matched | three parents; the clue spots | 2 |
| 1-LS3-1 (not exactly alike) | In tricky rounds, find the right parent among three of the same kind and see what differs | "same" and "different" labels | 3 |
| 1-LS1-2 | Hear each care card and sort the behavior | the care card; the four sort bins; the care chart | 4 |

## Screens and modes
Header (kit): title "Who's My Baby?"; `Match`, `Two players`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A wooden table with face-down cards and Hazel the owl on a branch. The welcome is queued (`welcomeAfter: true`): "Every baby here has a parent hiding in the cards. Look closely! Tap a card to flip it." First hint: "Tap a card."

**Matching (focus: the baby and three parents).** At 1366x768 the baby card sits left with three parents right; at 680x425 the parents sit below. The student taps a parent, then taps a clue spot on the baby (ears, stripes, beak, leaf). A right match glows with the clue named; a wrong one gets a kind spoken hint ("Look at the ears").

**Tricky rounds (1-LS3-1).** Four rounds with three parents of the same kind: three cats (a spotted kitten's mother has the same ears and face shape), three dogs, three sunflowers (the seedling's first true leaves match one parent's leaf edge), three ducks. After the match, the game labels "same" (ear shape, color) and "different" (spots, size).

**Care cards (1-LS1-2).** Eight cards, each read aloud with a short moving picture:
1. An emperor penguin dad keeps the egg warm on his feet through the winter.
2. A kangaroo carries her joey in her pouch for months.
3. A Nile crocodile carries her hatchlings in her mouth to the water.
4. A white-tailed deer hides her fawn in tall grass and comes back to feed it.
5. A robin brings worms to its chicks.
6. A cat carries her kitten by the scruff to a safe spot.
7. An elephant herd circles its calf when danger comes.
8. An orca mother teaches her calf where to find fish.
- The student sorts each into Feeding, Keeping warm, Protecting or Teaching; some fit two.
- Plant cards note that plants don't care for young, but seeds carry food inside for the seedling.

**The album and chart (the aha).** Each baby beside its parent with "same" and "different" labels; a care chart with pictures in four rows. Narrator: "Babies look like their parents, but not exactly. And parents do lots of things to help their babies stay alive."

**The end.** The album and the chart. `Print` prints them as picture pages.

**Two players (extra).** Two children take turns flipping and matching.

## Content
- 12 babies with parents and two look-alike parents each, 4 tricky rounds, 8 care cards with moving pictures, the sort, the album and chart.
- Care is shown gently: no predators catching young on screen.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards flip on tap; any match can be retried.
- Keyboard: Tab to cards, parents, clue spots and bins; Enter flips and picks.
- With Motion off cards change face without flipping and care pictures are still.

## Look
- Accent `--brand` #9b2f5a berry (header, card backs, the album); gold #f4c542 (the card in play, the clue spot); paper #fcf1f5; ink #2c0a19; muted #615159.
- Contrast (WCAG 2.1, computed): white on brand 7.12:1; brand on paper 6.46:1; ink on paper 16.35:1; muted on paper 6.73:1; ink on gold 11.09:1.
- Never color alone: labels "same" and "different" carry words and checkmark or star icons; bins carry pictures.
- Different from this batch (gadget green, dusk blue, canyon rust, lagoon).

## Art
- Local FLUX (`scripts/localart.py`): real-looking babies and parents true to each species, including look-alikes for tricky rounds (about 36, 1:1); eight care scenes (8, 4:3).
- Illustrated Hazel the owl (Gemini, 1; cutout yes).
- Drawn in code: card frames, clue spots, bins, the chart.
About 45 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as Hazel and the care cards; `playful-friend` as the game host and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `flip`: "Tap a card."
- how `match`: "Tap the parent, then tap the clue."
- event, whole, each match's same and different.
- event, whole, each care card.
- how `sort`: "Drag the card to what the parent does."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the deck, clue spots, labels, care cards, the sort, the album.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Matching | Tap parents at random | A match needs the clue tap too; the clue must be a real shared feature. |
| Tricky rounds | Guess | Only one parent shares the clue; the hint names where to look. |
| Care sort | Put everything in Protecting | Each card checks against its behavior; cards that fit two accept either. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `flip`; `match`.
2. Same and different (whole); care card (whole), waits.
3. `sort`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 1-LS1-2, 1-LS3-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Emperor penguin males keep the egg on their feet through winter | Australian Antarctic Program, "Emperor penguins" | San Diego Zoo Wildlife Alliance, "Emperor Penguin" | yes |
| Kangaroo joeys live in the pouch for months | Australian Museum, "Kangaroos" | San Diego Zoo Wildlife Alliance, "Kangaroo" | yes |
| Nile crocodile mothers carry hatchlings in their mouths | Smithsonian's National Zoo, "Nile crocodile" | San Diego Zoo Wildlife Alliance, "Crocodile" | yes |
| White-tailed deer hide fawns and return to nurse | National Park Service, "White-tailed deer" | U.S. Fish and Wildlife Service, "Leave young wildlife alone" | yes |
| Elephant herds protect calves; orca mothers teach calves | Smithsonian's National Zoo, "Asian elephant" | NOAA Fisheries, "Killer Whale" | yes |
| Seeds carry stored food for the seedling | U.S. Department of Agriculture Forest Service, "Seeds" | Missouri Botanical Garden, "Seeds and germination" | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r26, 2026-11-09): 12 babies with 3 parents each is 36 parent pictures; 8 animals and 4 plants; 8 care cards across 4 bins; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 baby and parents side by side; at 680x425 parents below.
2. Twelve matches each need a parent and a clue. (1-LS3-1)
3. Four tricky rounds label what is the same and what differs. (1-LS3-1)
4. Eight care cards are heard and sorted into the care chart. (1-LS1-2)
5. Every card is spoken; animals are true to their species.
6. No predators catching young on screen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still cards; no network requests.

## Open questions
None.
