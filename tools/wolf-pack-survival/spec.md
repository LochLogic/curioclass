# Wolf Pack Survival

## One idea
In a winter valley with elk, a choice card shows a lone wolf and a pack of six: the student picks alone or a group size, runs a sped-up winter, and reads a simple tally (meals found, pups raised, wolves alive in spring); then sardines face a dolphin and diving seabirds, alone or in a school that swirls into a bait ball; then honeybees, a lone bee or a hive that divides the work (foragers, guards, nurses) and huddles to keep warm in winter; cost cards keep it honest (a big pack shares each meal among more mouths; a big school is easier to spot from far away; a hive needs a lot of stored honey); the model's numbers follow real field findings, such as Yellowstone studies showing that hunting success rises with pack size up to about four wolves and then levels off, while bigger packs are better at keeping their kills and defending territory; at the end an argument builder asks the student to pick a claim, drag in two pieces of evidence from their own tallies and add one reason, and the tool checks that the evidence supports the claim, so a third grader learns to argue with evidence that some animals form groups that help members survive.

## Not like
- food-web-wobble (5, concept): whole food webs. Here living alone or together.
- beaver-builders (K, spec): animals changing a place. Here animals helping each other.
- fossil-clues (3, spec): survival in a changed habitat. Here survival in a group.
- life-cycle-wheel (3, spec): stages of a life. Here getting through a season.

## Who and how
- Grade 3, Science, module "Living in Groups". Standards: 3-LS2-1 (construct an argument that some animals form groups that help members survive).
- Format: simulator. Driver: one student alone, or the class choosing together (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- Three animals with group-size choices, seasons with tallies, six cost cards, the argument builder. Extra: Class choices (the class votes each group size, then compares tallies). tool.json `modes: ["Seasons", "Class choices"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-LS2-1 (groups help) | Run each animal alone and in a group | the tallies side by side | 2 |
| 3-LS2-1 (costs) | Read cost cards and try a group that's too big | the tally leveling off or falling | 3 |
| 3-LS2-1 (argument) | Pick a claim, drag two tallies as evidence, add a reason | the checked argument | 4 |

## Screens and modes
Header (kit): title "Wolf Pack Survival"; `Seasons`, `Class choices`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A snowy valley with an elk herd in the distance. A choice card: a lone wolf, or a pack with a slider from 2 to 12. The welcome is queued (`welcomeAfter: true`): "Winter is hard. Will this wolf do better alone or with a pack? Pick one, then run a winter and see." First hint: "Tap Alone or move the pack slider."

**Wolves (focus: the valley and the tally).** At 1366x768 the scene fills the left with the tally right; at 680x425 the tally is a sheet. A sped-up winter plays: hunts happen off-screen or as a chase that ends in a cut, never shown in detail. The tally: meals found, pups raised, wolves alive in spring. Alone, meals are few and an elk can't be brought down; a pack of four or so does best per wolf at the hunt; bigger packs keep their kills from other packs and scavengers but share each meal among more mouths.

**Sardines.** A dolphin and diving seabirds. Alone: a single sardine is easy to catch. In a school: the swirl confuses predators and each fish's chance of being caught falls; a cost card: a huge bait ball can be spotted from far away and draws more hunters.

**Honeybees.** A lone bee or a hive of thousands. The hive divides work: foragers bring nectar, guards defend the door, nurses feed the young. In winter the bees huddle in a cluster and shiver their wing muscles to keep the middle warm. A lone bee can't survive the winter. A cost card: the hive needs a lot of stored honey.

**The argument (the aha).** "I claim that ___ (claim card). My evidence: ___ and ___ (dragged from my tallies). My reason: ___." The tool checks that each piece of evidence supports the claim and points to a better tally if not. Narrator: "Living in a group isn't free, but for wolves, sardines and bees, it helps more than it costs."

**The end.** The three tallies, the cost cards and the argument. `Print` prints them.

**Class choices (extra).** The class votes each group size and compares tallies.

## Content
- Three animals with stated models based on field findings, group-size choices, six cost cards, claim cards and the argument checker.
- Hunts are shown plainly, without blood or gore; no pup dies on screen (the tally counts pups raised).

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each season waits for a choice; seasons can be rerun with a different size.
- Keyboard: Tab to choices, the slider, `Run`, tallies and the argument builder; arrow keys move the slider; Enter runs.
- With Motion off seasons show as before and after pictures.

## Look
- Accent `--brand` #2b5a6b winter teal (header, the tally, the slider); gold #f4c542 (the chosen size, the dragged evidence); paper #eff5f7; ink #0a1d24; muted #4f5b5f.
- Contrast (WCAG 2.1, computed): white on brand 7.56:1; brand on paper 6.87:1; ink on paper 15.71:1; muted on paper 6.37:1; ink on gold 10.63:1.
- Never color alone: tallies carry numbers and icons; claim cards carry words.
- Different from this batch (clay pot, team blue, sandstone, wheel violet).

## Art
- Local FLUX (`scripts/localart.py`): wolves in snow, alone and in a pack (2, 16:9); a sardine bait ball with a dolphin and birds (1, 16:9); a lone sardine (1, 4:3); inside a hive with workers (1, 16:9); a winter cluster (1, 4:3).
- Drawn in code: tallies, the slider, cost cards, the argument builder.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the nature film narrator; `easy-coach` as the guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.animal + ':' + state.season + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `choose`: "Pick alone or a group size."
- how `run`: "Tap Run to play the season."
- event, whole, each season's tally.
- event, whole, each cost card.
- how `argue`: "Pick a claim and drag in two tallies."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the three season models, tallies, cost cards, the argument checker. Model numbers sit in a marked block `/* WOLF-PACK DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Seasons | Run only the biggest group | The tally levels off; the cost card asks why bigger isn't always better. |
| Evidence | Drag any tally | The checker needs evidence that supports the claim. |
| Reason | Skip it | The argument needs a reason before it saves. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `choose`; `run`.
2. Tally (whole), waits; cost cards (whole).
3. The next animal.
4. `argue`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 3-LS2-1 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Wolf hunting success rises with pack size to about four and then levels off | MacNulty and colleagues, Behavioral Ecology (2012) | National Park Service, Yellowstone Wolf Project reports | yes |
| Bigger packs win territory contests and keep kills | Cassidy and colleagues, Behavioral Ecology (2015) | National Park Service, Yellowstone Wolf Project | yes |
| Schools and bait balls lower each fish's risk; confusion of predators | NOAA Fisheries, "Pacific Sardine" | Pitcher and Parrish, "Functions of shoaling behaviour" (in "Behaviour of Teleost Fishes", 1993) | yes |
| Honeybee division of labor and winter clusters | U.S. Department of Agriculture Agricultural Research Service, "Honey bees" | Seeley, "Honeybee Democracy" (Princeton, 2010) | yes |
| Wolves were returned to Yellowstone in 1995 and 1996 (31 wolves) | National Park Service, "Wolf Reintroduction" | U.S. Fish and Wildlife Service, gray wolf history | yes |
Backed twice: 6. Cut: 0.

Checks run (Python, scratchpad r27, 2026-11-09): 14 wolves in 1995 and 17 in 1996 is 31; in the model, meals per wolf peak at a pack of 4 and fall by a pack of 12; three animals with two cost cards each is six; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and tally; at 680x425 sheet.
2. Each of three animals runs alone and in a group with tallies. (3-LS2-1)
3. Cost cards show that groups also cost something. (3-LS2-1)
4. The argument uses two supporting tallies and a reason. (3-LS2-1)
5. Model numbers follow the cited field findings and are stated.
6. Hunts are shown without gore; no pup dies on screen.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: before and after pictures; no network requests.

## Open questions
None.
