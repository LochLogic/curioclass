# Clock Shop

## One idea
In a clockmaker's shop with a big geared clock, a digital clock and a window to the sky, the child drags the long hand around and watches everything move together: one full turn of the long hand moves the short hand from one number to the next, the digital clock counts along, and the window goes from sunrise to lunch to sunset to moon; the long hand snaps at the top (o'clock) and the bottom (half past), and customers come in with orders ("Set it to 7:30", or a digital card the child copies onto the hands, or a clock face whose digital time the child types); at 3:30 a magnifier shows the short hand is not on the 3 but halfway to the 4, and "half past three" suddenly makes sense; at the end a daily strip shows the child's clocks for breakfast, school, lunch and bed, so a first grader learns to tell and write time in hours and half hours using analog and digital clocks, both ways.

## Not like
- kitchen-lab (3, concept): elapsed time to the minute. Here hours and half hours.
- corner-store (2, live): time to five minutes and money. Here first clock reading.
- paperclip-ruler (1, spec): measuring length. Here measuring time.
- bead-slider (1, spec): moving on a number path. Here moving around a dial.

## Who and how
- Grade 1, Math, module "Telling Time". Standards: 1.MD.3 (tell and write time in hours and half-hours using analog and digital clocks).
- Format: sandbox. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- A geared analog clock, a digital clock, the sky window, twelve customer orders (four set-the-hands, four copy-the-digital, four type-the-time), the half-past magnifier, the daily strip. Extra: My day (the child sets times for their own routine and prints it). tool.json `modes: ["Shop", "My day"]`, `minutes: "10-15"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.MD.3 (hours) | Turn the long hand; set o'clock orders | the short hand on a number; :00 | 2 |
| 1.MD.3 (half hours) | Set half-past orders; use the magnifier | the short hand between two numbers; :30 | 3 |
| 1.MD.3 (both ways) | Read a clock face and type the time | the typed digital time | 4 |

## Screens and modes
Header (kit): title "Clock Shop"; `Shop`, `My day`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A warm clockmaker's shop with shelves of clocks, a big geared clock on the counter, a digital clock beside it and a window with morning sky. The clockmaker, an old tortoise, peers over glasses. The welcome is queued (`welcomeAfter: true`): "Welcome to my shop! Drag the long hand around and watch the short hand. Drag the long hand." First hint: "Drag the long hand."

**Turning (focus: the clock).** At 1366x768 the big clock is center with the digital clock and window at the right; at 680x425 the digital clock sits under the face and the window shrinks to a strip. The long hand is a wide, easy grab (at least 56 px). Gears turn behind the face. The long hand snaps to the top and bottom; between, it still moves but the shop rounds to the nearest half hour for orders.

**Orders.** A customer (a goose, a hedgehog, a bear) comes in. Three kinds: "Set it to 7:30" (spoken and written); a digital card to copy onto the hands; a clock face whose time the child types on a keypad (7:30, not 7:3).

**Half past (the aha).** At 3:30 a magnifier slides over: the short hand sits halfway between 3 and 4. The tortoise: "Half past three. The short hand is halfway to four, because half the hour has gone by."

**The end.** A daily strip: breakfast 7:00, school 8:30, lunch 12:00, bed 7:30, each with both clocks. `Print` prints it.

**My day (extra).** The child sets their own times; nothing leaves the device.

## Content
- One geared clock, hours and half hours only, twelve orders, the sky window (sunrise, midday, sunset, moon), all spoken. Customers are animals.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The long hand can be dragged both ways; the short hand follows and can't be dragged alone.
- Keyboard: Tab to the long hand, the keypad, and buttons; arrows move the long hand by half hours; number keys type.
- With Motion off the hands jump to each half hour and the sky changes without fading.

## Look
- Accent `--brand` #7a5310 brass brown (header, the clock rim, buttons); gold #f4c542 (the hand in hand, the magnifier rim); paper #fbf6ec; ink #261a04; muted #5a5245.
- Contrast (WCAG 2.1, computed): white on brand 6.84:1; brand on paper 6.35:1; ink on paper 15.83:1; muted on paper 7.15:1; ink on gold 10.48:1.
- Never color alone: the hour and minute hands differ in length and width and are named.
- Different from this batch (tomato red, notebook navy, ballot violet, circuit green).

## Art
- Local FLUX (`scripts/localart.py`): the clock shop (1, 16:9), the tortoise clockmaker in three poses (peer, point, smile) (3, 1:1), three animal customers (3, 1:1), four sky windows (4, 1:1).
- Drawn in code: the clock face, hands, gears, the digital clock, the magnifier.
About 11 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the tortoise clockmaker; `knowing-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.order + ':' + state.time + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `turn`: "Drag the long hand."
- how `set`: "Drag the long hand to the time."
- how `type`: "Type the time, then tap Enter."
- event, whole, each order.
- event, whole, half past.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
clock (family "clock"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* CLOCK ENGINE: begin */ ... /* end */`: a geared analog clock where the hour hand follows the minute hand (half a degree per minute), a linked digital clock, snapping to chosen steps, and a time keypad; later clock tools reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Set | Spin until it's right | The order checks only on Done; a wrong time shows both clocks side by side. |
| Type | Type random digits | The keypad checks the format and the time; the clock reads itself aloud on a miss. |
| Half past | Put the short hand on the 3 | The short hand can't be moved alone. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `turn`.
2. Order (whole), waits. `set` or `type`.
3. Half past (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.MD.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The hour hand moves continuously, so at half past it sits between numbers, a common confusion | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | Friedman and Laycock (1989), "Children's analog and digital clock knowledge", Child Development | yes |
| Geared clocks where hands move together help children connect the two hands | National Council of Teachers of Mathematics, "Principles and Standards", Pre-K to 2 measurement | Friedman and Laycock (1989), "Children's analog and digital clock knowledge", Child Development | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r8, 2026-11-10): at 3:30 the hour hand is at 105 degrees, between 3 (90) and 4 (120); at 7:30 it is at 225 degrees; one turn of the long hand moves the short hand 30 degrees; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 clock, digital and window; at 680x425 strip.
2. Hour orders are set on the geared clock. (1.MD.3)
3. Half-hour orders are set and the magnifier shows the short hand halfway. (1.MD.3)
4. Clock faces are read and typed as digital times. (1.MD.3)
5. Every card is spoken; every control is 56 px or more.
6. The short hand only moves with the long hand.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
