# Setting Swap

## One idea
The student moves Jack London's "To Build a Fire" to a new time, place or season with setting dials, predicts which of the story's eight events and the man's choices will break, then presses Run and watches the chain of causes crack where the new setting no longer holds it up (a July afternoon makes the fire pointless; a phone changes "alone"), explains each crack and rewrites the event to fit, so they learn how setting, plot and character hold each other up.

## Not like
- plot-rollercoaster (6, spec): tension across episodes and a character's change. Here how the setting causes events and choices.
- tone-dial (10, concept): rewriting a scene's tone. Here changing the setting and tracing what breaks.
- blizzard-scenes (spec): writing a scene in a storm. Here analyzing a published story's setting.
- perspective-camera (6, spec): narrator point of view. Here setting's effect on plot and character.
- theme-evidence-ladder (6-8, spec): passages proving a theme. Here a cause chain.

## Who and how
- Grade 7, ELA, module "Setting, Plot and Character" (Reading Literature). Standard: RL.7.3.
- Driver: one student; class mode looks for a swap that breaks nothing (tool.json `driver: "student"`). Every card is read on tap.
- Stories: "To Build a Fire" by Jack London (1908 version, in Lost Face, 1910), public domain; second level "The Gift of the Magi" by O. Henry (1905), public domain. tool.json `modes: ["To Build a Fire", "The Gift of the Magi", "Break nothing"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.
- Content note on the first screen: "The man in this story dies of the cold. The story tells this plainly." Nothing is saved; `Print` prints the chain, the cracks and the rewrites.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.7.3 (how setting shapes plot) | Turn a dial and predict which event cards will break, then Run | the predictions and the cracked chain | 2 |
| RL.7.3 (how setting shapes characters) | For each crack, explain the setting link it depended on and how the man's choice changes | the explanation on each crack | 3 |
| RL.7.3 (how elements interact) | Rewrite a cracked event to fit the new setting | the repaired card | 4 |
| RL.7.3 | Find the one setting detail that breaks the most cards and write how the setting shapes the man and his fate | the count and the paragraph | 5 |

## Screens and modes
Header (kit): title "Setting Swap"; `Chain`, `Dials`, `Run`, `Write`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A frosty map table with eight event cards linked in a chain by small cords to setting tags (seventy-five below, alone, the Yukon trail, 1898, no dog obeys him) and character tags (ignores the old-timer's advice, lacks imagination); four brass dials on the table edge. An old-timer from Sulphur Creek sits by a stove. First hint: "Tap the first card to hear the story begin." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Chain.** Eight events: he sets out alone on the trail; he notices the cold and dismisses it; he eats lunch and builds a first fire; he breaks through ice into water; he builds a fire under a snowy tree; snow falls and puts it out; he tries to kill the dog for warmth; he runs, then sits down and dies, and the dog goes on to camp. Each card's cords lead to keyed setting and character tags, and a `Read the passage` link opens the story text.

**Dials.** Place (Yukon, a big city, a desert), Time (1898, today), Season (deep winter, July), Who comes along (no one, a partner). The student turns one or more dials and taps each card they predict will break.

**Run.** The chain replays. A card cracks if any of its keyed tags no longer holds (July cracks the cards tied to seventy-five below; "a partner" cracks "alone" and the death; "today" cracks no phone or help). Predictions are scored: hits, misses and surprises.

**Explain and repair.** For each crack, the student picks the tag it depended on and writes one line on how the man's choice changes too. Then they rewrite the event to fit (for example, in July the trail crossing a creek is a nuisance, not a death sentence). Rewrites are the student's own; the tool checks only that the rewrite no longer uses a cracked tag word.

**Write.** The tool counts which single tag breaks the most cards (keyed: the cold). The student writes a short paragraph on how the setting shapes the man and his fate.

**The Gift of the Magi.** Eight cards tied to tags like poverty, Christmas Eve, a flat at $8 a week, 1905 New York; swaps show how setting shapes Della and Jim's choices.

**Break nothing.** A class challenge: find a swap that cracks no cards, then discuss whether it's still the same story.

At 1366x768 the chain and dials fit; at 680x425 the dials are a drawer.

## Content
- "To Build a Fire", Project Gutenberg #2429 (Lost Face), split into eight passages with keyed tags.
- "The Gift of the Magi", Project Gutenberg #7256, split into eight passages with keyed tags.
- Card summaries and the dial key written for Curio Class.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Dials can be reset; the chain rebuilds.
- With Motion off cards crack without shaking; a "cracked" label shows.

## Look
- Accent `--brand` #1f5a85 frost blue (header, cords, dials); gold #f4c542 (predictions, the strongest tag); paper #f1f6fa; ink #0a1d2c; muted #4c5966. Scene: a cabin map table with frost on the window.
- Contrast (WCAG 2.1, computed): white on brand 7.34:1; brand on paper 6.75:1; ink on paper 15.76:1; muted on paper 6.59:1; ink on gold 10.54:1.
- Never color alone: cracked cards say "cracked"; predictions say "predicted".
- Different from this batch (magazine plum, ember brown, leaf green, newsprint slate).

## Art
- Local FLUX (`scripts/localart.py`): cabin map table (1); setting versions of the trail (6: Yukon winter, Yukon July, a city street in winter, a desert trail, today with a snowmobile, a partner's sled tracks), no faces shown; the old-timer (3 poses), "An old gold prospector with a gray beard by a stove, <pose>, soft gouache, plain white background"; 1:1; cutout yes; a husky dog in snow (1); a 1905 New York flat at Christmas (1).
- The man is never shown in close-up, and his death is not pictured.
About 12 images. Drawn in code: cards, cords, tags, dials.

## Voice
Bank voice `gravel-ranger` as the old-timer (unique in this batch); the stories are read by `smooth-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.story + ':' + state.view + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: "Change where and when this story happens. Guess what breaks before you run it."
- event, whole, `card`: the tapped card or passage.
- event `predict`: "You think {four} cards will break. Run it."
- event `crack`: "{The fire} cracked. It needed {seventy-five below}."
- event `score`: "{Three} hits, {one} surprise."
- how `repairHow`: "Rewrite this event so it fits the new setting."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: cards with keyed setting and character tags, dials, crack rules, prediction scoring, repair checks.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Predict every card | Misses are counted as well as hits; the score shows both. |
| Explanations | Pick any tag | The tag must be one of the card's keyed cords. |
| Repair | Delete the event | A repair must keep the card and change it; empty rewrites aren't accepted. |
| Paragraph | Skip it | The print shows it blank. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the first card: card, `welcome` (queued, first time).
2. Dials: `predict` when Run is tapped (waits), then `crack` per card in chain order, then `score`.
3. Repair: `repairHow` (first time).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.7.3 wording | thecorestandards.org, Reading Literature Grade 7 | CCSS ELA 2010 PDF | yes |
| "To Build a Fire" (1908) is in London's Lost Face (1910), public domain; the story's details (seventy-five below, the old-timer on Sulphur Creek) | Project Gutenberg eBook #2429 (checked 2026-11-09) | Library of Congress catalog record for Lost Face (1910) | yes |
| "The Gift of the Magi" by O. Henry (1905), public domain | Project Gutenberg eBook #7256 (checked in batch 16) | Library of Congress catalog record for The Four Million (1906) | yes |
| Setting can shape plot and characters (setting as a cause in fiction) | ReadWriteThink, setting | Purdue OWL, literary terms (setting) | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: the man's death is told plainly with a content note and is not pictured; the dog-killing attempt is told, not shown.

Checks run (Python, scratchpad b21, 2026-11-09): the Gutenberg file is Lost Face and contains "TO BUILD A FIRE", "seventy-five below" and "Sulphur Creek"; in the sample key the cold tag cracks more cards than any other single tag; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 chain and dials fit; at 680x425 the dials are a drawer.
2. Dials, predictions and Run work; cracks follow keyed tags. (RL.7.3)
3. Each crack takes a tag and a line on the man's choice. (RL.7.3)
4. Repairs keep the card and drop the cracked tag word. (RL.7.3)
5. The most-breaking tag is counted and the paragraph is taken. (RL.7.3)
6. The Gift of the Magi and Break nothing work.
7. The content note shows on the first screen.
8. Print shows the chain, cracks and rewrites.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: cards crack without shaking; no network requests.

## Open questions
- None for Cory.
