# Tug of War Arena

## One idea
On field day a rope lies across the grass with a flag at the middle line, and a bench holds pullers of different strengths, kids and grown-ups (made up), each with a force number and an arrow; the student drags pullers onto each side, predicts whether the flag will stay still, move left or move right, and runs the pull while the arrows add up on a force bar: equal pulls hold the flag still, unequal pulls move it toward the stronger side and it speeds up; challenges ask the student to balance three pullers against two, to add one puller to win by a little, and to put a box on the rope with a push on one side and a pull on the other; then at a playground pattern station, the student gives a swing one push and a marble in a bowl one roll, records where each is at every tick on a strip chart, sees the back-and-forth repeat, and predicts where each will be at a future tick before playing it; at the end a claim card holds what the student found, so a third grader learns the effects of balanced and unbalanced forces on an object's motion, and that a pattern in motion can be used to predict future motion.

## Not like
- push-the-pumpkin (K, spec): one push's size and direction. Here forces added on both sides.
- crash-test-lab (8, concept): mass and collisions, same family. Here balance and patterns.
- magnet-maze (3, concept): forces at a distance. Here pulls by touch.
- bowling-lab (4, concept): energy in collisions. Here forces at rest and in motion.

## Who and how
- Grade 3, Science, module "Balanced and Unbalanced Forces". Standards: 3-PS2-1 (plan and conduct an investigation to provide evidence of the effects of balanced and unbalanced forces on the motion of an object), 3-PS2-2 (make observations and/or measurements of an object's motion to provide evidence that a pattern can be used to predict future motion).
- Format: simulator. Driver: one student alone, or the class predicting together (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- The rope with eight pullers, five challenges, the box challenge, the pattern station with two objects, the claim card. Extra: Class predict (the class votes left, still or right before each run). tool.json `modes: ["Arena", "Class predict"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-PS2-1 (balanced) | Make equal pulls, predict, run | the flag holding still; equal arrows | 2 |
| 3-PS2-1 (unbalanced) | Make unequal pulls and change one side at a time | the flag moving toward the bigger force and speeding up | 3 |
| 3-PS2-2 | Record a swing and a rolling marble at each tick and predict a future position | the strip chart; the predicted and real positions | 4 |

## Screens and modes
Header (kit): title "Tug of War Arena"; `Arena`, `Class predict`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A field day rope on the grass with a red flag over a white middle line. A bench of eight pullers, each with a number (10 to 40) and an arrow as long as its number. The welcome is queued (`welcomeAfter: true`): "Make the flag stay right over the line. Drag pullers onto each side." First hint: "Drag a puller to the left side of the rope."

**The rope (focus: the flag and arrows).** At 1366x768 the rope fills the middle with the bench below and the force bar above; at 680x425 the bench scrolls sideways. After pullers are placed, a prediction card (stays, moves left, moves right), then `Pull`. The force bar adds each side's arrows; the flag holds still when they match and moves toward the bigger side when they don't, speeding up as it goes. A note says the model leaves out slipping and tiring.

**Challenges.** Five: (1) balance one against one, (2) balance three on the left against two on the right, (3) add one puller so the right wins by a little, (4) change only the right side and predict, (5) a box on the rope with a push on one side and a pull on the other. Each change is one thing at a time, and the notebook records what changed and what happened.

**Pattern station (3-PS2-2).** A playground swing and a marble in a bowl. One push or roll, then a tick clock. The student taps the position at each tick on a strip chart (far left, middle, far right). After two swings back and forth, the pattern repeats; the student predicts the position at tick 12 and plays it to check. A note says swings slow down slowly because of air and friction.

**The claim card (the aha).** "When the pulls are equal, the flag ___. When one side pulls harder, the flag ___. A swing's motion repeats, so I can predict ___." Narrator: "Forces that cancel out don't change motion. Forces that don't cancel change it. And patterns let you see the future."

**The end.** The notebook, the strip chart and the claim card. `Print` prints them.

**Class predict (extra).** The class votes before each run.

## Content
- Eight pullers (varied kids and adults, made up, labeled "illustration") with force numbers; the force bar; five challenges; the box; two pattern objects with stated motion rules; the claim card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each run waits for a prediction; pullers can be swapped between runs.
- Keyboard: Tab to the bench, rope sides, the prediction, `Pull` and the strip chart; Enter places.
- With Motion off the flag jumps to its end position and the swing shows tick stills.

## Look
- Accent `--brand` #1d4f91 team blue (header, arrows, the force bar); gold #f4c542 (the puller in hand, the prediction); paper #eff4fb; ink #091a33; muted #4f5868.
- Contrast (WCAG 2.1, computed): white on brand 8.14:1; brand on paper 7.37:1; ink on paper 15.74:1; muted on paper 6.49:1; ink on gold 10.70:1.
- Never color alone: arrows carry numbers and length; strip chart marks carry positions in words.
- Different from this batch (clay pot, sandstone, wheel violet, winter teal).

## Art
- People (illustrated) for eight pullers of varied ages and looks, labeled "illustration" (Gemini, `people: true`, 8; cutout yes).
- Local FLUX (`scripts/localart.py`): the field day lawn (1, 16:9), the playground (1, 16:9).
- Drawn in code: the rope, flag, arrows, force bar, the box, the swing and bowl, the strip chart.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the field day announcer; `hero-coach` as the coach and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.challenge + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `place`: "Drag a puller to a side."
- how `predict`: "Tap stays, left or right."
- event, whole, each run's result.
- how `tick`: "Tap where it is at this tick."
- how `future`: "Tap where it will be at tick 12."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
forces. Copies collision-lab's `/* FORCES ENGINE: begin */ ... /* FORCES ENGINE: end */` block unchanged and adds net force along one line and a simple pendulum step, so the block can move to `kit/forces.js` for the whole family.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Always pick "stays" | Predictions aren't scored, but the claim card asks why the flag moved. |
| Challenges | Pile everyone on one side | Each challenge has a goal (balance, win by a little) that a pile-up fails. |
| Pattern | Guess tick 12 | The guess is checked against the played position and the chart pattern. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `place`; `predict`.
2. Result (whole), waits.
3. `tick`; `future`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 3-PS2-1, 3-PS2-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Balanced forces don't change motion; unbalanced forces do | NASA Glenn Research Center, "Newton's Laws of Motion" | The Physics Classroom, "Balanced and Unbalanced Forces" | yes |
| A swing's period depends on its length and repeats | NASA Glenn Research Center, "Pendulum" | The Physics Classroom, "Pendulum Motion" | yes |
| Friction and air slowly reduce a swing's motion | The Physics Classroom, "Pendulum Motion" | OpenStax, "College Physics", damped oscillations | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r27, 2026-11-09): three pullers of 20 balance two of 30 at 60 each; a 2-meter swing takes about 2.84 seconds per full swing; the right side wins by 10 when a 10 is added to a balanced rope; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 rope, bench and bar; at 680x425 scrolling bench.
2. Equal pulls hold the flag still after a prediction. (3-PS2-1)
3. Unequal pulls move the flag toward the bigger force across five challenges. (3-PS2-1)
4. A swing and a marble are recorded and a future position predicted and checked. (3-PS2-2)
5. Pullers are varied in age and look and labeled illustration.
6. The model's left-out effects are stated.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: end positions only; no network requests.

## Open questions
None.
