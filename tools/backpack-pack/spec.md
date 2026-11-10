# Backpack Pack

## One idea
A backpack with only six pockets and twelve things to choose from means every new thing pushes another out, and the camping trip that plays next shows the child which ones they needed (the night gets cold, the rain comes, it gets dark) and which were only wants, so a kindergartner feels scarcity force a choice and learns needs come first.

## Not like
- piggy-bank-planner (2, concept): saving money over weeks toward one goal. Here a fixed space, one trip, no money.
- market-day (1, concept): spending tokens on goods and services. Here no prices; space is what runs out.
- then-and-now-flip (K, concept, this batch): sorting pictures by time. Here packing by use, and the sort comes after the trip shows why.
- playground-rules (K, concept, this batch): hanging signs and watching a replay change. Here what you pack changes how a trip goes.
- me-on-the-map (K, built): zooming out through places. Here one backpack and one trip.

## Who and how
- Kindergarten, Social Studies (Economics), module "Needs and Wants". Standard: D2.Eco.1.K-2 (explain how scarcity necessitates decision making).
- Driver: teacher on the projector with the class answering out loud, or one child alone; every picture, question and choice is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Two trips: Camping (first) and Beach Day (opens after the first trip). tool.json `modes: ["Pack", "Trip", "Need or want"]`, `minutes: "10-15"`, `grades_label: "Grade K"`.
- Nothing is saved; `Print` prints a "My backpack" page with the six things the child packed and their need and want stickers.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Eco.1.K-2 (scarcity forces a decision) | With all six pockets full, choose one thing to take out before a new one goes in | the "Take one out" moment with the six pockets lit | 3 |
| D2.Eco.1.K-2 (explain the choice) | After the trip, drag each packed thing to Need or Want and tap the trip moment that shows why | the Need and Want baskets with the moment picture | 5 |
| D2.Eco.1.K-2 (decide again) | Repack once and run the trip again | the second trip with no sad moments | 6 |

D2.Eco.6.K-2 (from the idea card) moved to community-helpers-village and is not claimed here.

## Screens and modes
Header (kit): title "Backpack Pack"; `Pack`, `Trip`, `Need or want`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A campsite at the edge of a forest in late afternoon. An open backpack in the middle with six empty, glowing pockets; a pile of twelve things on a blanket to its left; Ranger Hal beside a tent on the right. The welcome is queued (`welcomeAfter: true`): "We're going camping tonight! Your backpack has six pockets. Tap a thing to hear it. Then drag it into a pocket." First hint (screen and Read): "Tap a thing to hear it. Then drag it into a pocket." The first tap on a thing says its name and cuts the welcome.

**Pack (focus: the backpack and the pile).** At 1366x768 the backpack is center and largest, the pile left, Ranger Hal right, and `Go camping` under the backpack (shown only when all six pockets are full). At 680x425 Ranger Hal folds away and the pile becomes two rows under the backpack.
- Tap a thing: its name plays. Drag it (or tap it, then tap a pocket) to pack it. A packed thing can be dragged back to the pile.
- When all six are full and the child drags a seventh thing in, it stops above the backpack and every pocket wiggles: "Your backpack is full. Tap one thing to take out." The child taps one; it goes back to the pile and the new thing goes in. This happens every time; the line is spoken the first two times, then hint only.

**Trip (focus: the campsite scene).** Plays as five short beats, each about 4 seconds, and each beat checks one need. The backpack shows small in the corner and opens at each beat.
- Hike: "It's a long, hot walk. We're thirsty!" Water bottle packed: the kids drink and smile. Missing: they droop, Ranger Hal says "Oh no. What would help us when we're thirsty?"
- Snack time: food packed (the sandwich or the apples): they eat. Missing: tummies rumble.
- Rain: rain jacket packed: they stay dry under hoods. Missing: they shiver, wet.
- Dark: flashlight packed: a circle of light. Missing: a dark screen with only eyes showing (kind, not scary).
- Cold night: warm sweater packed: cozy by the tent. Missing: teeth chatter.
Each want that was packed gets one happy moment after all five beats if every need was packed ("And we had time to play with the ball!"). If a need was missing, the want shows sitting unused in the corner.
Every beat's picture is its own painted state, different at a glance (smiling, drooping, wet, dark, shivering). A tap during the trip acts at once: tapping a beat's picture repeats its line; tapping `Pack` stops the trip and goes back.
After the trip: "Let's see what we needed." and the tool moves to Need or want.

**Need or want (focus: two big baskets).** The six packed things sit in a row on top; a Need basket (a water drop and a sweater icon) and a Want basket (a heart and a ball icon) below. The child drags each thing to a basket. When a thing goes to Need, the beat picture where it helped shows beside it ("The jacket kept us dry in the rain."). When a need goes to Want, Ranger Hal says "Hmm. Remember the rain? Try again." and it slides back. When a want goes to Need, "Did we need it on the trip? Try again." Then `Pack again` and `Go camping again` let the child repack and rerun.

**Beach Day.** After the first camping trip a beach umbrella appears on the Pack screen. Its twelve things and five beats: sun (sun hat), hot sand (sandals), thirsty (water), lunch (food), wet after swimming (towel). Wants: pail and shovel, kite, beach ball, sunglasses with stars, toy boat, comic book, music player.

**Class vote.** Teacher notes suggest: before each beat, pause and ask the class "Did we pack it?" and let them call out.

## Content
- Camping, 12 things (5 needs, 7 wants): water bottle, sandwich and apples, rain jacket, flashlight, warm sweater (needs); toy truck, ball, stuffed bunny, paper crown, bubbles, coloring book, game tablet (wants).
- Beach Day, 12 things: water bottle, lunch box, sun hat, sandals, towel (needs); pail and shovel, kite, beach ball, star sunglasses, toy boat, comic book, music player (wants).
- With six pockets and five needs, a child who packs every need still has one pocket for a want, so wants are never "bad".
- Teacher note: needs and wants depend on the trip; a sun hat is a need at the beach and not on a cold night. The bunny can be a comfort for some kids; the class may talk about it, and the tool counts it as a want for this trip only.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Go camping` stays hidden until all six pockets are full; the hint before then says "Drag a thing into a pocket." and never names `Go camping`.
- A seventh thing always needs a "take one out" choice; there is no way to have more than six.
- With Motion off the trip shows each beat as a still picture with its line, and things snap into pockets without flying.

## Look
- Accent `--brand` #2f5d34 forest green (header, backpack trim, the Need basket rim); gold #f4c542 (glowing empty pockets, the selected thing); paper #f3f7ef; ink #10200f; muted #4d5a4b. Scene: a campsite at dusk with a tent and pine trees.
- Contrast (WCAG 2.1, computed): white on brand 7.67:1; brand on paper 7.08:1; ink on paper 15.67:1; muted on paper 6.72:1; ink on gold 10.45:1.
- Never color alone: baskets have icons and the words Need and Want; missing needs show a picture, not only a color.
- Different from this batch (playground blue, brick red, sepia, festival purple).

## Art
- Local FLUX (`scripts/localart.py`): campsite at afternoon (1, 16:9); beach (1, 16:9); 24 things in one sticker style, each a cutout on white (24, 1:1).
- People art goes to Gemini (`people: true`): Ranger Hal (a Black man in his fifties in a park ranger uniform and hat), 4 poses (waving, pointing, thinking, thumbs up); two campers, a girl and a boy about five (one South Asian girl, one Mexican American boy), each in 6 states that read at a glance (smiling, drinking, drooping thirsty, wet and shivering, cozy, holding a light), plus beach states (sunburned-squint under no hat, happy in hats, hot feet hopping, wrapped in towels); "illustrated kindergarten camper <state>, soft gouache, plain white background, big clear face"; 3:4; cutout yes. Campers and Ranger are separate cutouts over the scene so they show whole at every beat.
- The dark beat is the campsite painted at night (1, 16:9) with the light circle drawn in code.
About 46 images. Drawn in code: pockets, baskets, the light circle.

## Voice
Bank voice `gravel-ranger` as Ranger Hal and the narrator (unique in this batch), style: warm, slow, outdoorsy. `Curio.voice` with `scope: () => state.mode + ':' + state.trip + ':' + state.beat`, `welcomeAfter: true`.
- how `welcome` (Pack, first time): "We're going camping tonight! Your backpack has six pockets. Tap a thing to hear it. Then drag it into a pocket."
- event `name`: the thing's name, every tap ("Rain jacket.").
- how `full` (first two times only): "Your backpack is full. Tap one thing to take out."
- how `ready` (once, when the sixth pocket fills): "Your backpack is full. Tap Go camping when you're ready."
- event, whole, each beat line (5 per trip, both versions: packed and missing), for example "It's raining! Good thing we packed the rain jacket." and "It's raining! We're getting wet. What would keep us dry?"
- event `play`: "And we had time to play with the [want]!"
- event `sort-start` (whole): "Let's see what we needed. Drag each thing to Need or Want."
- event `why`: the reason line for a need ("The jacket kept us dry in the rain.").
- event `try-need`: "Hmm. Remember the [beat]? Try again."
- event `try-want`: "Did we need it on the trip? Try again."
- event `done` (whole): "You packed what you needed! Tap Pack again to try a different backpack, or tap the beach umbrella for Beach Day."
- how `beach` (first time): "Now we're going to the beach. Six pockets again. Tap a thing to hear it."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: six pockets with take-one-out, the five-beat trip from packed state, the two baskets, the second trip.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Trip | Pack six things at random | The trip shows every missing need with a sad picture; the done line needs all five needs. |
| Trip | Pack the six biggest or brightest things | Sizes and colors are mixed across needs and wants (the crown and truck are bright; the flashlight is small). |
| Pack | Pack nothing and press Go | `Go camping` shows only with six packed. |
| Sort | Drag everything to Need | Each want bounces back with "Did we need it on the trip?" |
| Sort | Copy positions from the pile | Things are shuffled on every load; positions carry no meaning. |
| Sort | Guess until it sticks | Allowed, but the "why" moment plays only for needs, and the reason line repeats the trip picture, so even guessing ends in the reason. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; the first tap may cut it). Each tap on a thing: `name`.
2. Sixth pocket: `ready`. Seventh thing: `full` (first two times), then the child taps one to take out.
3. Go camping: five beats, each line whole and waited for before the next beat; then `play` if every need was packed.
4. `sort-start` (whole), then the child drags: `why` or `try-need` or `try-want` per drag, each before the next drag is accepted.
5. All sorted: `done` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| D2.Eco.1.K-2: explain how scarcity necessitates decision making | C3 Framework for Social Studies State Standards (NCSS, 2013), Economics | NCSS, C3 Framework Dimension 2 summary | yes |
| Needs are things we must have to live (water, food, shelter, clothing); wants are things we would like to have | Federal Reserve Bank of St. Louis, Econ Lowdown, "Needs and Wants" (K-2 lesson) | Council for Economic Education, Voluntary National Content Standards in Economics, Standard 1 (scarcity) | yes |
| Packing lists for a camp hike include water, food, rain gear, a light and warm layers | The Mountaineers, Ten Essentials (Wikipedia, Ten Essentials, checked 2026-11-09) | National Park Service, "10 Essentials" | yes |
| At the beach, sun hats, water and shade protect against sun and heat | CDC, Sun Safety | American Academy of Dermatology, sun protection for children | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r1, 2026-11-09): for every 6-item pack from 12 things (924 packs per trip), exactly 7 include all five needs and each of those has one want; the done line fires only for those 7; a random pack reaches done with chance 7/924; the sort accepts each thing only in its keyed basket; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the backpack is center with pile and Ranger; at 680x425 the pile is below and Ranger folds.
2. Every thing, question and choice is spoken on tap.
3. A seventh thing always asks the child to take one out. (D2.Eco.1.K-2)
4. The trip plays five beats, each picture different for packed and missing.
5. Need or want sorts with the trip moment as the reason. (D2.Eco.1.K-2)
6. Pack again and Go camping again rerun the trip; Beach Day opens after the first trip. (D2.Eco.1.K-2)
7. Go camping never shows or is named before six are packed.
8. Tap while it plays: any tap during a beat acts at once; no older line plays after a newer one.
9. Motion off: still beats; no network requests.

## Open questions
- None for Cory.
