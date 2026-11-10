# Bowling Lab

## One idea
A school hallway holds a bowling lane with a ramp, height marks at 25, 50 and 100 centimeters, a light gate near the bottom and a triangle of ten pins, and the student predicts which height will knock down the most pins, rolls the ball, and reads the light gate's speed while a table logs speed, pins down and how far the farthest pin slid; after several rolls the student graphs speed against pins and distance and finds that a faster ball moves pins farther and knocks down more, so it carries more energy; then before each collision the student picks what will change (the ball slows, pins speed up, a crash sound, a tiny warmth on a heat camera) and checks; a heavy and a light ball at the same speed show that mass matters too; at the end an explanation card built from the student's own data says that faster means more energy, and that in a collision energy moves from the ball into the pins, sound and heat, so a fourth grader learns to use evidence to relate an object's speed to its energy, and to ask questions and predict how energy changes when objects collide.

## Not like
- contraption-workshop (4, concept): energy changing form in a device. Here speed and collisions.
- collision-lab (11, live): momentum math. Here what you can see and measure.
- push-the-pumpkin (K, spec): push size. Here speed and energy.
- tug-of-war-arena (3, spec): balanced forces. Here moving energy.

## Who and how
- Grade 4, Science, module "Energy and Motion". Standards: 4-PS3-1 (use evidence to construct an explanation relating the speed of an object to the energy of that object), 4-PS3-3 (ask questions and predict outcomes about the changes in energy that occur when objects collide).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three heights, two balls, the light gate, the roll table, two graphs, four collision questions per roll, the heat camera, the explanation card. Extra: Class predict (the class votes on each roll's pins). tool.json `modes: ["Lane", "Class predict"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4-PS3-1 | Roll from three heights, log speed, pins and distance, and graph them | the light gate; the table; the graphs | 2 |
| 4-PS3-3 | Pick what will change before each collision, then check | the collision question card; the heat camera | 3 |
| 4-PS3-1 (explain) | Build an explanation card from the graphs | the card | 4 |

## Screens and modes
Header (kit): title "Bowling Lab"; `Lane`, `Class predict`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A school hallway bowling lane with a ramp, three height marks, a light gate and ten pins. The welcome is queued (`welcomeAfter: true`): "Which height will knock down the most pins? Predict first. Tap a height mark." First hint: "Tap a height mark on the ramp."

**Rolling (focus: the lane).** At 1366x768 the lane fills the left with the table and graphs right; at 680x425 the table is a sheet. The student picks a height and a ball, predicts pins down, and taps `Roll`. The ball passes the light gate, which shows its speed in meters per second. The table logs height, ball, speed, pins down and how far the farthest pin slid. Pins reset after each roll. The model uses a solid rolling ball on a smooth ramp; a note says real lanes add friction.

**Graphs.** After at least three rolls, two graphs fill: speed against pins down, and speed against farthest slide. Both rise together.

**Collision questions (4-PS3-3).** Before each roll, four question cards: Will the ball slow down? Will the pins speed up? Will there be a sound? Will anything get warmer? The student picks yes or no for each, then checks. A heat camera view shows a tiny warm spot where ball meets pins, with the temperature change written in words ("a tiny bit warmer"). A heavy and a light ball at the same height show the heavier one moves pins farther.

**The explanation (the aha).** A card built from the student's own data: "When the ball was faster, ___. So a faster ball has more ___. In the crash, energy went into ___, ___ and ___." Narrator: "Speed is a clue to energy. And energy doesn't disappear in a crash. It moves into the pins, the sound and a little heat."

**The end.** The table, both graphs and the card. `Print` prints them.

**Class predict (extra).** The class votes on pins down before each roll.

## Content
- Three ramp heights, two balls (light and heavy), the light gate, the roll model with a stated rule, four collision questions, the heat camera, the explanation card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each roll waits for a prediction; any roll can be repeated.
- Keyboard: Tab to heights, balls, the prediction, `Roll`, the table, the graphs and the cards; Enter rolls.
- With Motion off the ball jumps to the pins and pins show their end positions.

## Look
- Accent `--brand` #4a3a8c lane indigo (header, the table, graph lines); gold #f4c542 (the chosen height, the light gate beam); paper #f3f1fa; ink #150f2e; muted #57536a.
- Contrast (WCAG 2.1, computed): white on brand 9.23:1; brand on paper 8.25:1; ink on paper 16.47:1; muted on paper 6.59:1; ink on gold 11.33:1.
- Never color alone: graph points carry labels; the heat camera carries words; yes and no carry marks.
- Different from this batch (magnet red, collar green, postcard orange, ocean navy).

## Art
- Local FLUX (`scripts/localart.py`): the school hallway lane (1, 16:9), the pins close-up (1, 4:3).
- Drawn in code: the ramp, ball, light gate, pins in motion, the table, graphs, the heat camera.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the lane announcer; `firm-captain` as the lab lead and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.roll + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `predict`: "Tap how many pins you think will fall."
- how `questions`: "Tap yes or no on each card."
- how `roll`: "Tap Roll."
- event, whole, each roll's result.
- how `explain`: "Finish the card using your graphs."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the ramp and roll model, the light gate, pin scatter, the table and graphs, the heat camera.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Graphs | Roll from one height only | The graphs need all three heights. |
| Questions | Skip them | `Roll` stays off until all four cards are answered. |
| Card | Fill any words | Each blank checks against the student's own table. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `predict`; `questions`; `roll`.
2. Result (whole), waits.
3. `explain`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 4-PS3-1, 4-PS3-3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| A faster object has more kinetic energy; energy grows with mass and with speed squared | NASA Glenn Research Center, "Kinetic Energy" | The Physics Classroom, "Kinetic Energy" | yes |
| A rolling solid ball's speed at the bottom of a ramp is about the square root of 10/7 times g times h | OpenStax, "University Physics Volume 1", rolling motion | The Physics Classroom, "Rolling and energy" | yes |
| In collisions some energy becomes sound and heat | OpenStax, "College Physics", inelastic collisions | U.S. Department of Energy, "Energy transformations" (Energy Kids) | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r28, 2026-11-09): a solid ball rolling down 25, 50 and 100 centimeters reaches about 1.87, 2.65 and 3.74 meters per second; doubling the height multiplies the speed by about 1.41; doubling the speed gives four times the energy; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 lane and table; at 680x425 sheet.
2. Rolls from three heights log speed, pins and distance and fill two graphs. (4-PS3-1)
3. Four collision questions are predicted and checked before each roll. (4-PS3-3)
4. The explanation card is built from the student's own data. (4-PS3-1)
5. The model's rule and left-out friction are stated.
6. Heavy and light balls are compared at the same height.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: end positions only; no network requests.

## Open questions
- The idea card moves 4-PS3-2 out of this tool to contraption-workshop (default used: this tool teaches 4-PS3-1 and 4-PS3-3 only; contraption-workshop carries 4-PS3-2).
