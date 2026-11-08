# Bus Stop

## One idea
You drive Ms. Rosa's little school bus down a road you pick: kids hop on and off at each stop, Ms. Rosa can't see the back seats, so you show her who is aboard by filling the seat chart with counters and then pick the number sentence that tells the stop's story, and the bus only drives on when the sentence matches.

## Not like
- story-replay (grade 1): cartoons stop at a question, you act them out, and the cartoon replays your sentence, all story types within 20. Here the riders carry over from stop to stop (each stop starts where the last one ended), the road you pick changes every later number, and everything stays within 10.
- ten-frame-spillover (grade K): ladybugs fill a ten frame and spill into a second for teen numbers. Here the 2 by 5 seat chart is a bus that holds exactly ten: it never spills, and filling it is the make-ten question.
- sheep-count (grade K): counting how many, no operations. Here every stop is an add or take-away story.
- make-ten-machine (grade 1): strategies for harder facts. Here making ten is filling empty seats with counters, no strategy names.
- hundred-hop (grade K): counting along a path. Here no counting sequence past 10.

## Who and how
- Grade K, math, module "Putting Together and Taking Apart". Standards: K.OA.A.1, K.OA.A.2, K.OA.A.3, K.OA.A.4, K.OA.A.5.
- Driver: teacher on a projector or smartboard (tool.json `driver: "teacher"`); the class tells each stop's story and says answers out loud, a child taps. Every question and choice is spoken and every choice is a picture, so a child alone at home can play it (BASELINE rule 4).
- Minutes: one Drive trip 8 to 12, a Split round 5, an Express ride 3, a Fill up ride 4. A class period: one trip plus one Express ride.
- No personal prompts. Nothing is stored (only the kit's Motion setting).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.OA.A.1 represent with objects, expressions, equations | Taps the counter cup (or drags) once per kid who got on, or taps a counter once per kid who got off, then picks the number sentence that matches | Solid counters for riders already aboard, ringed counters for new riders, dashed empty rings for riders who left; the three sentence cards with dot pictures under each number | Check 3 and 4 |
| K.OA.A.2 solve add and take-away stories within 10 | Watches the story stop (kids board or leave), shows it with counters, answers "How many riders now?" by picking the right card | Riders walking on or off the painted bus; the chart's new count; the card's total | Check 2, 3 and 4 |
| K.OA.A.3 decompose a number every way, record each | At the Split stop (and in Split mode) taps counters across two play areas, then taps Keep it to record each new way | Live equation "7 = 4 + 3" with dots; the way list filling its empty slots; turn-around ways linked | Check 5 |
| K.OA.A.4 make 10 from any number 1 to 9 | At the Ten stop (starts 4 to 8) and in Fill up (starts 1 to 9, every start within two rides) fills every empty seat with counters, taps Done, then picks "n + e = 10" from three cards that all end in 10, so the child must match the new counters to the second number | The 2 by 5 chart going full, the extra kids waving at the curb, the cards | Check 6 and 13 |
| K.OA.A.5 fluently add and subtract within 5 | In Express, hears a quick story, says the answer out loud and taps a number tile (or the teacher taps Show me after the class calls it) | A five-seat strip holding the starting riders only (leavers stand at the door, no ring marks who left until the reveal), the riders moving, the sentence, a ticket per fact | Check 7 |

## Screens and modes
Header (kit): title "Bus Stop", mode buttons (`.seg`, icon plus word, 60 px tall): `Drive` (bus icon, default), `Split` (two groups of dots), `Express` (lightning bolt), `Fill up` (full bus icon); then `Read`, `Motion`, `Sound`. Every control is 60 px or more (44 px at the 680x425 preview) and carries an icon and a word.

Panel (right, 330 px at 1366x768): Ms. Rosa's portrait (painted cutout, 120 px, three faces, see Art) beside the hint (22 px type, the kit `#hint`), then the mode's panel buttons, then the trip map (Drive only).

**On load and first tap.** Drive opens at school: the school scene fills the top of the stage with the bus parked and Ms. Rosa in the driver's window; three big painted road signs stand across the lower stage: `Park` (tree icon), `Library` (book icon), `Farm` (barn icon). Nothing speaks before the first tap (kit). The first hint: "Ms. Rosa can't see the back seats. You show her! Tap a road sign: the park, the library or the farm." The first tap on a sign picks that road: its own line plays ("The park road! Off we go."), the bus drives out and the route's start counters appear on the chart. A first tap anywhere else queues the welcome. The welcome may be cut by that tap (BASELINE 16); the premise (Ms. Rosa can't see the back, you show her with counters) lives in the hint, in Read and in the first stop's how line.

**Drive.** Focus: the bus at the stop and, under it, the seat chart where the child acts. Layout at 1366x768 (stage about 1036 x 704, all above the fold):
- Top band (about 45 percent, 310 px): the painted stop scene, the bus cutout (about 520 px wide) at the curb, riders as kid cutouts on the curb or at the door, the stop's name in code on a blank painted sign post. The ticket strip runs across the top edge of the scene (40 px): one ticket per finished stop with its sentence.
- Bottom band: the counter cup (120 px, a code-drawn yellow cup of counters, left), the seat chart (code-drawn top view of the bus floor, 2 rows of 5 seats, each seat 84 px; the driver's seat drawn at the front for orientation), and to its right `Done` (gold, check icon) and `See again` (eye icon, replays the boarding or leaving). When the counters are right, the sentence cards slide up in a row under the chart (three cards about 270 x 110, sentence type 40 px, dots under each number, a speaker icon on each card that reads it).
- Panel: portrait and hint, `Tell first` (speech-bubble toggle, off by default), `Go` (shown only while Tell first is holding riders at the curb), `New road` (map icon), and the trip map: school, the stops as circles, the fork as a split in the line with the chosen road drawn and the other faint, the current stop ringed.
- At 680x425: header 44 px, panel 210 px wide; the portrait shrinks to 48 px beside the hint, the trip map and `New road` fold away (`New road` stays on the end screen), the ticket strip shows only the last ticket, seats 44 px, cards shrink to sentence type 20 px and stay in one row. Scene text stays 10 px or more.

Each stop runs in steps: watch (riders board or leave while the story line plays), show (counters, then `Done`), tell (pick a card). The step's control is always lit and named by the hint.

What the picture shows at each outcome: right card, the ticket flies to the strip, the door closes, the bus drives off right and the next scene slides in; wrong card, the card wobbles and greys, and the chart acts out what the card says (see Interactions), then returns; end of trip, the empty bus at school, the trip map with the whole path, every ticket in a big row, and the buttons `Other road` (fork icon), `New road`, `Express ride` (lightning).

Fork: after stop 2 the stage shows two painted road signs with icons (Content) and the bus waiting between them. Tap one to take it.

**Split.** Focus: the two play areas and the counters on them. Layout at 1366x768: across the stage top, `Fewer` (minus and one rider icon), the big numeral of riders (spoken when it changes), `More` (plus and one rider icon), and three place buttons with icons (`Park`, `Library`, `Farm`) that swap the two painted play-area tiles. Left two thirds: the two painted area tiles side by side (each about 330 x 260), counters (70 px) sitting on them in rows of 5; under them the live equation "7 = 4 + 3" (48 px, dots under the 4 and the 3) and `Keep it` (gold, pin icon). Right third: the way list, one empty outlined slot per possible way (n + 1 slots; one column up to 6 slots, two columns for 7 to 11), each 44 px tall, so the whole list always shows. At 680x425 the list stays on the stage in two columns with 28 px rows; the place buttons fold into one `Place` button that cycles.

**Express.** Focus: the five-seat strip and the riders. Layout at 1366x768: the school-street scene on top with the bus and the waiting or leaving kids; under it a five-seat strip (one row of 5 seats, 110 px each); under that six number tiles `0` to `5` (120 x 110, the numeral in 56 px over its dot pattern) and `Show me` (eye icon). The ride's five tickets sit across the scene top. Panel: portrait, hint, `Again` (circular arrow, shown when a ride ends). At 680x425 tiles are 64 x 60 and the tickets show the last one only.

**Fill up** (added in Refine round 1, 2026-11-06, so K.OA.A.4 covers every start from 1 to 9). Focus: the seat chart and the cup, laid out as a Drive Ten stop (same scene band, chart, cup, `Done`, `See again`, cards). A ride is 5 buses at the Ice Cream Corner scene. Starts are drawn without repeats from 1 to 9 for the page load: ride 1 takes 5 of the nine, ride 2 the other 4 plus one, so two rides use every start. Each bus plays exactly as the Ten stop (Interactions), with e = 10 - n empty seats and e + 1 kids waiting (at most 10). Its three cards: `n + e = 10` | `n + (e-1) = 10` | `n + (e+1) = 10` (for n = 9 the second is `9 + 0 = 10`). A right card adds the ticket and the next bus pulls up; after 5 buses, `Again` (circular arrow) starts a new ride. Panel: portrait, hint, `Again` when a ride ends. At 680x425 as the Drive Ten stop.

## Content
Seat chart order: counters fill seats left to right, top row then bottom row. Counter looks (never color alone): already aboard = solid yellow disc with an ink outline; got on at this stop = blue disc with a thick white ring and a plus mark; got off = the seat keeps a dashed empty ring with a small arrow out.

**Routes** (start riders, then stops in order; "on k" or "off k"; the three cards, right one first; the builder shuffles card order per stop, fixed per page load):

Park road (start 3 riders):
1. Maple Street, on 2: `3 + 2 = 5` | `3 - 2 = 1` | `3 + 2 = 6`
2. Duck Pond, off 1: `5 - 1 = 4` | `5 + 1 = 6` | `5 - 1 = 5`
3. Fork: `Duck Bridge` (duck icon) or `Big Hill` (hill icon)
   - Duck Bridge, on 3: `4 + 3 = 7` | `4 - 3 = 1` | `4 + 3 = 8`
   - Big Hill, on 4: `4 + 4 = 8` | `4 - 4 = 0` | `4 + 4 = 9`
4. The Park (Split stop): all riders get off to play, `Swings` or `Slide`. 7 riders (bridge) or 8 (hill).
5. Ice Cream Corner (Ten stop): 7 aboard, 3 empty, 5 kids waiting: `7 + 3 = 10` | `7 + 2 = 10` | `7 + 4 = 10`. Hill: 8 aboard, 2 empty, 4 waiting: `8 + 2 = 10` | `8 + 1 = 10` | `8 + 3 = 10`.
6. School, off 10: `10 - 10 = 0` | `10 - 9 = 0` | `10 - 0 = 0`

Library road (start 4):
1. Bakery, on 2: `4 + 2 = 6` | `4 - 2 = 2` | `4 + 2 = 7`
2. Fire Station, on 1: `6 + 1 = 7` | `6 - 1 = 5` | `6 + 1 = 8`
3. Fork: `Big Street` (tall buildings icon) or `Little Lane` (cottage icon)
   - Big Street, off 1: `7 - 1 = 6` | `7 + 1 = 8` | `7 - 1 = 7`
   - Little Lane, off 2: `7 - 2 = 5` | `7 + 2 = 9` | `7 - 2 = 6`
4. The Library (Split stop): `Story rug` or `Puppet stage`. 6 riders (Big Street) or 5 (Little Lane).
5. Fruit Stand (Ten stop): 6 aboard, 4 empty, 6 waiting: `6 + 4 = 10` | `6 + 3 = 10` | `6 + 5 = 10`. Little Lane: 5 aboard, 5 empty, 7 waiting: `5 + 5 = 10` | `5 + 4 = 10` | `5 + 6 = 10`.
6. School, off 10 (cards as on Park).

Farm road (start 5):
1. Mailbox Corner, off 1: `5 - 1 = 4` | `5 + 1 = 6` | `5 - 1 = 5`
2. Apple Orchard, on 3: `4 + 3 = 7` | `4 - 3 = 1` | `4 + 3 = 8`
3. Fork: `Barn Road` (red barn door icon) or `Pumpkin Patch` (pumpkin icon)
   - Barn Road, off 3: `7 - 3 = 4` | `7 + 3 = 10` | `7 - 3 = 5`
   - Pumpkin Patch, off 1: `7 - 1 = 6` | `7 + 1 = 8` | `7 - 1 = 7`
4. The Farm (Split stop): `Goats` or `Hens`. 4 riders (Barn Road) or 6 (Pumpkin Patch).
5. Corn Stand (Ten stop): Barn Road: 4 aboard, 6 empty, 8 waiting: `4 + 6 = 10` | `4 + 5 = 10` | `4 + 7 = 10`. Pumpkin: 6 aboard, 4 empty, 6 waiting: `6 + 4 = 10` | `6 + 3 = 10` | `6 + 5 = 10`.
6. School, off 10 (cards as on Park).

Card kinds: the right card; the "wrong way" card (the other sign: on became off or off became on); the "miscount" card (total one more, or for take-away the start number, the "forgot to take away" slip). Ten stop wrong cards (Refine round 1: a card picked by its total alone taught nothing, so all three end in 10): "one too few" (`n + (e-1) = 10`) and "one too many" (`n + (e+1) = 10`); the child matches the second number to the new counters. School wrong cards (all three end in 0, same reason): "one rider still on" (`10 - 9 = 0`) and "nobody got off" (`10 - 0 = 0`); the child matches the second number to the empty rings.

**Split stop and Split mode.** A way is recorded as `n = a + b`, a on the left area, b on the right. Ways for n are the n + 1 pairs (n, 0) down to (0, n); each fills the slot of its left count, top slot = n on the left. Turn-around pairs: (a, b) and (b, a) with a not equal to b. In Drive, `Drive on` lights after 2 different ways. Split mode: n from 2 to 10, starting at 7 on the Park areas; each n keeps its own list for the page load.

**Express facts** (25, all within 5): add a + b for a, b from 1 and a + b at most 5 (10 facts: 1+1, 1+2, 1+3, 1+4, 2+1, 2+2, 2+3, 3+1, 3+2, 4+1); take away a - b for 1 to 5 and b from 1 to a (15 facts, 1-1 up to 5-5). A ride is 5 facts drawn without repeats, at least 2 of each kind. On a fact the strip holds a plain solid counters; for "on", b kids wait at the curb; for "off", b kids stand at the open door facing out, and no counter is marked as leaving until the reveal (Refine round 1: leaving rings shown before the answer made take-away "count the yellow ones"). Each fact uses a fresh set of kids. Rides mix kinds at random, 2 or 3 of each.

## Interactions in detail
- Watch step: when a stop opens, the scene slides in, the door opens, and the story line plays while the riders walk on (they slide into the door and vanish) or step off (they appear at the door and walk to the curb), about 2.5 s with a small bob per step (Motion off: they appear at their end spot on the same beat). The cup (on stops) or the counters (off stops) are live from the first frame: a tap during the walk acts at once.
- First stop of a road: the road line and the start-counters line play first, and the riders' walk starts with the story line (not on the road tap), so "{k} kids get on" is heard while they board.
- Tell first (toggle): riders wait at the curb or at the door; the hint and line ask the class to tell what will happen; `Go` starts the walk. Only `Go` is live while riders wait (cup, counters and Done wake with the walk). Off by default.
- Show step, on stops: a tap on the cup (or a drag from it to any empty seat) adds one new counter in the next seat; tapping a new counter takes it back; aboard counters are fixed. The cup greys when no seat is empty. Off stops: the cup is hidden; tapping an aboard counter sends it off (dashed ring stays); tapping the ring brings it back. No running total is shown anywhere: the child counts.
- `Done` checks the change, not the total: exact k new (on) or k gone (off). Too few: "Two kids got on, and you added one. Tap the cup for each kid." Too many: "Two kids got on, and you added three. Tap a blue counter to take one back." Both name `See again`. Done with no change gives the too-few line. The cards appear only after a right Done.
- Tell step: the question and the three cards are read in order (one sequence; any tap cuts it). A card's speaker icon reads that card only. Tapping a card picks it:
  - Right: chime, the right line, ticket to the strip, drive-off (2 s, Motion off: the scene swaps on the same beat). The right line is `whole`: the next stop's story line waits for it.
  - Wrong way: the card greys; for 1.5 s the chart acts out the card (ghost counters leave for a minus card, ghost counters arrive for a plus card) and returns, while its line plays. Then the other two cards are live.
  - Miscount: the card greys; the chart numbers each seat that still holds a rider (solid or new, never a dashed ring), in seat order, while Ms. Rosa counts aloud (one number per 0.6 s), then the miss line.
  - Ten stop and Fill up wrong cards: the card greys; the chart numbers the new (blue) counters in turn while Ms. Rosa counts them, then "{e} kids got on. Try another card."
  - School wrong cards: the card greys; the chart numbers the dashed empty rings in turn while Ms. Rosa counts them, then "Ten kids got off. Try another card."
  - The bus never leaves on a wrong card. Greyed cards stay greyed for that stop. No score anywhere; tickets hold only right sentences.
- Split stop and mode: counters start all on the left area (n = n + 0). Tap a counter to send it to the other area (or drag). The equation updates at once. `Keep it` records the shown way into its slot (slot fills with the equation and dots, chime). A duplicate makes its slot flash; its line plays once per pair. When both turn-around ways of a pair are kept, a curved link joins their slots with its line. When every slot is full, all slots pulse once and the all-ways line plays (whole). In Drive, `Drive on` (gold, bus icon) appears after 2 ways; the riders then walk back aboard and the chart shows n.
- Ten stop: the waiting kids stand at the curb; each cup tap fills the next empty seat and one kid walks aboard. At 10 the cup greys and shows "Full" in code; a further tap plays the full line (once per stop). The kids left over wave (wave pose). `Done` with an empty seat: "There is still an empty seat. Tap the cup to fill it." Then the cards.
- School: Ms. Rosa says everybody off; the child taps all 10 counters. After the right card the end screen opens.
- `Other road`: jumps back to the fork with the chart and tickets as they were before it, so the class can compare where the other road leads. `New road`: back to the three signs, chart cleared.
- Express: the question plays; tiles and `Show me` are live at once. The first tile tap locks the tiles for that fact: right, chime and the yes line; wrong, the tile shakes and the look line (it still shows the answer). Then the riders move (1.5 s), the strip shows the result, the ticket drops in, and the next fact comes 1 s after the line ends. `Show me` reveals without a tile. Keys 0 to 5 tap the tiles. No timer. After 5 facts, `Again` starts a new ride.
- Mode switches hush speech and keep each mode's state (the trip waits where it was). Keyboard: Tab reaches panel controls first, then the cup, seats, Done and cards; Enter or Space taps.
- Edge cases: Next stop never starts while a card line plays except by the drive-off; resizing mid-walk re-lays out without losing counters; a drag dropped outside the chart returns the counter.

## Look
- Accent `--brand` #2b4c7e road-sign navy (header, mode buttons, the trip map line); bus yellow #f5b301 for `Done`, `Keep it`, the counters and the bus; paper #fbf7ec, ink #1d2633, muted #5a6270; new-rider blue #2f6fb3; seat fill #d9dee6; scenes in warm morning light. Different from hundred-hop's green #2f7a4a.
- Contrast (WCAG 2.1, computed): white on brand 8.61:1; brand on paper 8.05:1; ink on paper 14.24:1; muted on paper 5.74:1; ink on bus yellow 8.23:1 (gold buttons); white on new-rider blue 5.19:1; ink on card white 15.25:1; blue counter on seat fill 3.84:1 (non-text, over 3:1). Yellow counters carry a 3 px ink outline, so they read on the light seats.

## Art
One style for all: bright painted children's picture book, warm morning light, clean edges. People go to Gemini with `people: true`; scenes, bus and icons may use local FLUX. Text on signs stays in code over blank painted surfaces.
- bus-closed: "A small yellow school bus with ten seats, side view facing right, door closed, tinted windows, blank yellow side panel"; 16:9; cutout yes; people no; every stop.
- bus-open: the same bus with its front door folded open; 16:9; cutout yes; people no; during boarding.
- 19 stop scenes, 16:10, cutout no, people no, each "<place>, a curb and an empty bus stop sign post with a blank sign in front, warm morning, painted children's picture book": school front with a flagpole and big doors; Maple Street with red maple trees and houses; a duck pond with ducks and reeds; a wooden bridge over a creek; a road up a big grassy hill; a park entrance with a gate; a corner with an ice cream shop with a blank awning; a bakery with bread in the window; a fire station with a red truck in the open bay; a busy street with tall buildings; a little lane with cottages and flowers; a library with wide steps; a fruit stand with crates of apples and oranges; a mailbox on a country corner; an apple orchard; a dirt road by a red barn; a pumpkin patch; a farm gate with a field; a corn stand with ears of corn in baskets. Each sits behind its stop.
- 6 play areas, 4:3, cutout no, people no: swings; a slide; a story rug with pillows; a small puppet stage; a goat pen with two goats; a hen house with hens. Split stop and Split mode tiles.
- 9 sign icons, 1:1, cutout yes, people no: a green tree; a stack of books; a red barn; a duck; a green hill; tall city buildings; a cottage; a red barn door; a pumpkin. Road and fork signs (sign shape and word drawn in code).
- 10 rider kids, each two poses (standing three-quarter facing left, and waving), 3:4, cutout yes, people yes (20 images): a varied group of kindergartners with backpacks: different skin tones and hair (braids, curls, a hijab, a buzz cut, pigtails), one with glasses, one with a hearing aid, one with a leg brace, bright everyday clothes. Shown full body on the curb, fully visible, feet on the curb line. The same 10 serve every route (the ones boarding at a stop are chosen in order so a kid never boards twice in a row without leaving).
- ms-rosa, three faces (smiling and talking, thinking with a hand on her chin, cheering), 1:1, cutout yes, people yes: "a friendly woman school bus driver in her forties in a navy driver's jacket, head and shoulders". Panel portrait (faces follow her lines: talking, a wrong card, a right card) and small in the bus driver's window.
45 images; 23 with people (contact sheet for Cory and the fresh representation check, BASELINE 11). Drawn in code: the seat chart, counters, cup, cards, dots, tickets, trip map, sign shapes and words, the five-seat strip, tiles, the stop name on the blank sign.

## Voice
Bank voice `bright-teacher` (Autonoe): she is Ms. Rosa. Style line: "Say brightly and warmly, like a cheerful school bus driver talking to kindergartners." Different from hundred-hop (hero-coach); no other K math neighbor is specced. `Curio.voice` with `scope: () => state.mode + ':' + state.stopKey`. Numbers are spoken as words. Templates in braces are expanded by the builder over Content; lines.json holds every expansion, with singular forms for 1 ("1 kid gets on", "1 rider").

Drive:
- how, welcome (stale when a road is picked): "Hi! I'm Ms. Rosa. You drive today, and you help me count. Tap a road sign: the park, the library or the farm."
- event, road picked: "The park road! Off we go." / "The library road! Off we go." / "The farm road! Off we go."
- event, start counters shown: "{n} riders are on the bus. I can't see the back seats, so the seat chart shows me."
- event, whole, each stop story (when the walk starts): on: "{Stop}! {k} kids get on the bus." off: "{Stop}! {k} kids get off the bus."
- how, first on stop (stale when Done is right): "Show me on the seat chart. Tap the cup once for each kid who got on. Then tap Done."
- how, first off stop (stale when Done is right): "Show me on the seat chart. Tap a counter once for each kid who got off. Then tap Done."
- how, Tell first on, first time (stale when Go is tapped): "Tell the story first. What will happen? Then tap Go."
- event, Done too few / too many: the two lines in Interactions, with "Tap See again to watch." added. Every time.
- event, cards shown (sequence, cut by any tap): "How many riders now? Tap the number sentence that tells the story." then each card read ("Three plus two equals five.").
- event, whole, right card: "Yes! {sentence}. {c} riders now." then the bus leaves.
- event, wrong way card: on stop: "{sentence}. That means kids got off. But kids got on! Try another card." off stop: "{sentence}. That means kids got on. But kids got off! Try another card."
- event, miscount card: "Let's count." then "One, two, ... {c}." (one number per counter), then "{c} riders. Try another card."
- event, fork: "Two roads! Tap the {iconA} for {RoadA}, or the {iconB} for {RoadB}."
- event, whole, Split stop: "{Place}! {n} riders get off to play. Some go to the {areaA}, and the rest go to the {areaB}."
- how, first Split (stale when Keep it is tapped twice): "Tap a rider counter to send it to the other side. Then tap Keep it."
- event, each kept way: "{n} is {a} and {b}."
- event, duplicate, once per pair: "You found that way already. Try a new way."
- event, turn-around link, once per pair: "{a} and {b}, {b} and {a}. Switch sides, still {n}!"
- how, Drive on shown (stale when Drive on is tapped or all ways are found): "Find more ways, or tap Drive on."
- event, whole, all ways: "You found every way to make {n}. {n+1} ways!"
- event, whole, Ten stop: "{Stop}! Kids are waiting. The bus has ten seats, and {n} are full."
- how, first Ten stop (stale when Done is right): "Tap the cup to fill every empty seat. Then tap Done."
- event, cup tapped when full, once per stop: "Every seat is full!"
- event, Ten stop Done with empty seat: "There is still an empty seat. Tap the cup to fill it."
- event, whole, Ten stop right: "Yes! {n} plus {e} equals ten. The bus is full! {w} kids wait for the next bus."
- event, whole, School: "Back at school! Everybody off. Tap each counter. Then tap Done."
- event, whole, school right: "Yes! Ten minus ten equals zero. The bus is empty. Great driving!"
- event, end screen: "What a trip! Tap Other road to see what changes, or New road."

Split mode:
- how, welcome (stale when a counter or Keep it is tapped): "Riders at the playground! Tap a counter to send it to the other side. Then tap Keep it."
- event, More or Fewer: "{n} riders."
- the kept, duplicate, link and all-ways lines as above.

Express:
- No separate welcome (it was always dropped by the first fact). The first fact's how line: "Listen, say the answer out loud, then tap the number or Show me." then the fact.
- event, each fact: "{a} riders. {b} more get on. How many now?" / "{a} riders. {b} get off. How many now?" The fact's story is also the first sentence of the Express hint, so Read says it again.
- event, right tile: "Yes! {sentence}." Wrong tile: "Look. {sentence}." Show me: "{sentence}."
- event, ride done: "Five express stops! Tap Again for a new ride."

Fill up:
- how, first bus (stale when Done is right): "Fill up the bus! {n} seats are full. Tap the cup to fill every empty seat. Then tap Done."
- event, each later bus: "{n} seats are full."
- the cup-full, empty-seat, cards and wrong-card lines as at the Ten stop; right card: "Yes! {n} plus {e} equals ten. The bus is full!"
- event, ride done: "Five full buses! Tap Again for a new ride."

Read speaks the hint, which always names the current action and control (the how line of the step, or "Tap the number sentence that tells the story." while cards show; in Express the fact's story, then the action).

## Family engine
none

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| K.OA.A.1 to A.5 wording (represent with objects, fingers, drawings, expressions or equations; solve word problems within 10; decompose numbers up to 10 every way and record by drawing or equation; make 10 from 1 to 9; fluently add and subtract within 5) | CCSS Mathematics, Kindergarten, Operations and Algebraic Thinking, corestandards.org/Math/Content/K/OA | Common Core Standards Writing Team (2011), Progressions for the CCSS in Mathematics, K, Counting and Cardinality; K-5, Operations and Algebraic Thinking | yes |
| K students work with add to and take from (result unknown) and put together and take apart (total unknown, both addends unknown) | CCSS Mathematics Glossary, Table 1, with its note on kindergarten | Progressions, K-5 OA (2011), kindergarten section | yes |
| Kindergartners should see equations; writing them is encouraged but not required (why cards are picked, not written) | CCSS Mathematics, K.OA note | Progressions, K-5 OA (2011) | yes |
| Fluency within 5 is the kindergarten fluency expectation | CCSS K.OA.A.5 | Progressions, K-5 OA (2011) | yes |
| Turn-around (commutative) is taught formally in grade 1; Bus Stop only lets K children notice it (teacher notes) | CCSS 1.OA.B.3 | Progressions, K-5 OA (2011), grade 1 | yes |
Backed twice: 5. Cut: 1 (a research claim about ten-frames helping K make ten; not needed on screen, so dropped). The bus's ten seats are story, not a claim.

Checks run (Python, S:/CurioClass-codex-scratch/specs/bus-stop/check.py, 2026-11-05):
- All 6 route paths stay within 0 to 10 at every stop; every right card is true; every wrong-way card is a true sentence with the other sign and a different total; every miscount card is false; no card has a negative or a total over 10. A first draft had Farm at 9 riders minus 5, whose wrong-way card was 9 + 5 = 14, and Library's 2 + 4 whose wrong-way card had to be 4 - 2: both routes were re-numbered.
- Split numbers by path: 7, 8, 6, 5, 4, 6; ways n + 1 (5 to 9); turn-around links 2 to 4; Split mode 2 to 10 gives 3 to 11 slots (fits in two columns).
- Ten stops: empty seats 2 to 6, waiting kids empty + 2 = 4 to 8 (at most 10 rider cutouts in use). Refine round 1 (2026-11-06) changed the Ten stop and School cards so all three share the total (10, or 0 at School) and differ in the second number; every wrong one is false (Ten: n + (e-1) and n + (e+1) are never 10; School: 10 - 9 and 10 - 0 are never 0), no number over 10. Fill up: starts 1 to 9, e = 9 down to 1, waiting e + 1 = 2 to 10 (at most 10 cutouts), wrong second numbers 0 to 10.
- Express: 10 add + 15 take-away facts, largest sum 5.
- Wrong behaviors: Done with 0, k-1, k+1 or 7 counters (on k = 2) fails; only exactly k passes, so mashing the cup never shows cards; Done with nothing fails; Express locks on the first tile, so mashing gives one answer; Split's Keep it without moving records a real way (n + 0), and Drive on needs two different ways; no score exists to game.
- Contrast ratios as in Look.

## Done when
1. Focus: at 1366x768 the stop scene with the bus and the seat chart fill the stage, seats are 84 px, and the cup, Done, See again and the three cards are all above the fold; at 680x425 the chart, Done and cards still show with no scroll and scene text is 10 px or more.
2. All 6 paths (3 roads, 2 forks each) play from school to school with the numbers in Content, and Other road returns to the fork with the chart as it was.
3. Done passes only with exactly the stop's k counters added or removed (try 0, k-1, k+1 and ten cup taps), and no running total shows anywhere.
4. A right card drives on with its ticket; a wrong-way card acts its sign out on the chart; a miscount card counts aloud; the bus never leaves on a wrong card. (K.OA.A.1, A.2)
5. Split: Keep it records "n = a + b" into its slot, a duplicate flashes and its line plays once, both turn-around ways get linked, filling every slot plays the all-ways line, and Drive on appears after two ways. (K.OA.A.3)
6. Ten stop: the cup stops at 10, the extra kids wave, all three cards end in 10, and only "n + e = 10" drives on; a wrong card counts the blue counters. School's cards all end in 0 and a wrong one counts the empty rings. (K.OA.A.4)
7. Express: five facts within 5 per ride, the first tile locks, right and wrong both show the answer, no timer; before the answer no counter is marked as leaving; Read repeats the fact's story. (K.OA.A.5)
8. Tap while it plays: tapping the cup during the boarding walk adds a counter at once; a mode button during the drive-off switches at once and no older line plays after.
9. Pre-reader: every choice (road, fork, cards, tiles, places) is a picture or numerals with dots and is spoken; a child with Sound on can finish a trip without reading.
10. Voice: in five Done-wrong taps the Done line plays five times; the how lines play once each; no line names Done, Drive on or Go while it is hidden.
11. Motion off: riders and bus appear at their end spots on the same beats; no wobble or pulse.
12. No network requests; nothing is stored.
13. Fill up: two rides use every start from 1 to 9; each bus plays as the Ten stop with three cards ending in 10. (K.OA.A.4)

## Open questions
- None for Cory. The idea card's on-screen finger strip is left out: fingers are used in the room ("say the answer out loud" and the class can show fingers), and counters carry K.OA.A.1 on screen. People art (23 images) goes to the contact sheet and the fresh representation check.
- Settled in Refine round 1 (2026-11-06, integrator, by BASELINE rule 2 and "a check must reward the right practice"): Express no longer marks leavers before the answer; Ten stop and School cards share their total; Fill up mode added so K.OA.A.4 covers starts 1 to 9; the first stop's walk waits for its story line; Read in Express repeats the fact.
