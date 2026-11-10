# Beaver Builders

## One idea
A fast stream runs through a valley with aspen trees and few animals, and a beaver family needs deep water to be safe; the student taps trees for the beavers to chew and drags sticks and mud onto a dam, and over sped-up seasons the stream rises into a pond with a lodge whose door is under the water; new animals move in (frogs, ducks, fish, a moose eating willows at the edge), each with a picture card of what it needs, and the student drags each plant and animal to the part of the valley that meets its needs; then a family moves in and builds a house and a road, and the student helps them choose (a pipe under the road so water still flows, leave trees by the water, walk or bike, reuse and recycle) and sees the pond stay healthy; at the end a before-and-after picture of the valley lets the student say how the beavers changed it and how the family helps, so a kindergartner learns that animals and people change their surroundings to meet their needs, that living things live where their needs are met, and ways people can take less from a place.

## Not like
- terrarium-pal (K, spec): what living things need in a jar. Here animals changing a whole valley.
- shade-builder (K, spec): people building against sunlight. Here an animal's building.
- weather-wardrobe (K, spec): weather patterns. Here a place that changes.
- wolf-pack-survival (3, concept): animals in groups. Here a family reshaping its home.

## Who and how
- Kindergarten, Science, module "Living Things Change Their Environment". Standards: K-ESS2-2 (construct an argument supported by evidence for how plants and animals, including humans, can change the environment to meet their needs), K-ESS3-1 (use a model to represent the relationship between the needs of different plants and animals, including humans, and the places they live), K-ESS3-3 (communicate solutions that will reduce the impact of humans on the land, water, air, and/or other living things in the local environment).
- Format: simulator. Driver: one child with a grown-up nearby, or the class on the projector (tool.json `driver: "either"`). Every card is spoken; no reading needed. Controls 64 px or more.
- Build the dam over four seasons, six animals arriving, a matching step, a people step with four choices, the before-and-after. Extra: Class valley (the class votes each family choice on the projector). tool.json `modes: ["Build", "Class valley"]`, `minutes: "15-20"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K-ESS2-2 | Help build the dam and say how the beavers changed the stream; see the family clear land | the stream becoming a pond; the before-and-after | 2 |
| K-ESS3-1 | Drag each plant and animal to the place that meets its needs | the valley map with deep water, the edge and the trees | 3 |
| K-ESS3-3 | Pick choices with the family and see the pond stay healthy | the family's choices; the pond and its animals | 4 |

## Screens and modes
Header (kit): title "Beaver Builders"; `Build`, `Class valley`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A fast, shallow stream in a valley with aspen trees. Two beavers and two kits sit on the bank. The welcome is queued (`welcomeAfter: true`): "The beavers need deep water to be safe. Help them build! Tap a tree." First hint: "Tap a tree by the stream."

**Build the dam (focus: the stream).** At 1366x768 the valley fills the screen with a small tray of sticks and mud; at 680x425 the tray sits below. Tap a tree: a beaver chews it and drags it to the water. Drag sticks and mud to the dam spot. After each season (spring, summer, fall, winter) the water rises. A lodge appears with its door under the water, and the narrator says why: "The door is under the water, so the beavers can swim in where other animals can't follow."

**New neighbors (K-ESS3-1).** Six arrive, each with a picture card of its needs: a fish (deep water), a duck (deep water to swim and dive), a frog (the shallow, weedy edge), a moose (willows to eat at the edge), the willow itself (wet ground at the edge), a squirrel (trees). The student drags each to its place; the right place makes it smile and stay.

**The family (K-ESS2-2, K-ESS3-3).** A family moves in and builds a house and a road; the road could block the stream. Four choices, each spoken with a picture: a pipe under the road so water flows; leave trees by the water; walk or bike to school; reuse and recycle. Each choice shows the pond and animals staying well; a choice skipped shows a small problem (the water backs up, a bank washes away) that the next choice can fix. Nothing is hurt on screen.

**Before and after (the aha).** The first valley and the last side by side. The student taps three changes the beavers made and one thing the family did to help, and says (or the grown-up types): "The beavers changed the stream to ___ so they could ___. The family helped by ___." Narrator: "Beavers build to stay safe. People build too. We can build and still share."

**The end.** The before-and-after and the student's words. `Print` prints a coloring page of the valley with the four choices.

**Class valley (extra).** The class votes each family choice on the projector.

## Content
- Four seasons of building, six neighbors with need cards, four family choices with picture outcomes, the before-and-after with tap spots.
- Nothing dies or is hurt; problems are small and fixable.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Drags snap to the nearest right spot; a wrong drop slides back with a spoken hint.
- Keyboard: Tab to trees, the tray, animals and choices; Enter picks up and places.
- With Motion off the water level steps up without flowing and animals appear in place.

## Look
- Accent `--brand` #2e6b3a pond green (header, the tray, cards); gold #f4c542 (the item in hand, the right spot); paper #f1f8f2; ink #0b2311; muted #4f5d52.
- Contrast (WCAG 2.1, computed): white on brand 6.40:1; brand on paper 5.93:1; ink on paper 15.40:1; muted on paper 6.44:1; ink on gold 10.23:1.
- Never color alone: places carry picture icons; need cards carry pictures and spoken words.
- Different from this batch (sun orange, sky blue, snail plum, night indigo).

## Art
- Local FLUX (`scripts/localart.py`): the valley in five states (stream, early dam, rising water, pond with lodge, pond with the family's house) (5, 16:9).
- Illustrated animals: two beavers, two kits, fish, frog, duck, moose, squirrel (Gemini, 9 characters; cutout yes); the family, labeled "illustration" (Gemini, `people: true`, 1 group).
- Drawn in code: the tray, need cards, the dam pieces.
About 15 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator of the valley; `friendly-dad` as the beaver dad and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.season + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `chew`: "Tap a tree for the beavers."
- how `stack`: "Drag sticks and mud to the dam."
- event, whole, each season's change.
- how `match`: "Drag the animal to the place it needs."
- how `choose`: "Pick a way the family can help."
- how `after`: "Tap something the beavers changed."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the valley states, drag and snap, need cards, family choices, the before-and-after.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Matching | Drag at random | Each animal only stays where its needs are met; the hint names the need. |
| Family | Skip every choice | Small problems show and the before-and-after asks what helped. |
| Before and after | Tap anywhere | Only real changes count as taps. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `chew`; `stack`.
2. Season changes (whole), waits.
3. `match`; `choose`.
4. `after`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for K-ESS2-2, K-ESS3-1, K-ESS3-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Beavers dam streams to make deep water; lodge doors under water | National Park Service, "Beaver" | U.S. Fish and Wildlife Service, "Beaver" | yes |
| Beaver ponds bring frogs, ducks, fish and moose | Naiman, Johnston and Kelley, BioScience (1988) | U.S. Forest Service, "The Beaver Restoration Guidebook" (2018) | yes |
| Beavers eat bark of aspen and willow | National Park Service, "Beaver" | Smithsonian's National Zoo, "North American Beaver" | yes |
| Pipes (culverts) under roads keep streams flowing; streamside trees protect banks | U.S. Forest Service, aquatic organism passage | U.S. Environmental Protection Agency, "Riparian buffers" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r25, 2026-11-09): four seasons and five valley pictures; six neighbors with one place each among three places; four family choices; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the valley with tray; at 680x425 tray below.
2. The dam turns the stream into a pond over four seasons, and the student says how. (K-ESS2-2)
3. Six neighbors are matched to the places that meet their needs. (K-ESS3-1)
4. Four family choices show the pond staying healthy. (K-ESS3-3)
5. Every card is spoken; controls are 64 px or more.
6. Nothing is hurt on screen; problems are small and fixable.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: water steps up; no network requests.

## Open questions
None.
