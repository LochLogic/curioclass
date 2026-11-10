# Crash Test Lab

## One idea
On a long test track two carts sit beside a stack of bricks, fan units and a tiny seat holding an egg; at the push bench the student first plans a fair test on a card (what to change, what to keep the same, what to measure), then adds fans (more push), bricks (more mass) or a felt strip (friction) and measures how fast the cart's speed changes, and a results table shows the pattern (twice the push gives twice the change; twice the mass gives half); at the crash bench two carts with force meters on both bumpers collide head-on or one catches the other, and both meters always show the same peak in opposite directions, even a heavy cart against a light one, while the light cart's motion changes more; then the design task asks for a bumper (spring, foam, clay or a crumple box, within a weight and length limit) that keeps the egg from cracking in the standard crash, tested and changed until it works, and the student sees that a good bumper spreads the push over more time; at the end a design card holds the student's bumper and its evidence, so an eighth grader learns to apply Newton's third law to design a solution to a collision problem, and to plan an investigation showing that a change in motion depends on the sum of forces and the mass.

## Not like
- collision-lab (11, live): momentum and impulse in numbers, same family. Here force pairs and fair tests, no momentum math.
- tug-of-war-arena (3, spec): balanced and unbalanced forces, same family. Here how mass changes the effect of a force.
- curling-stones (11, spec): force, mass and friction in equations. Here planning tests and designing a bumper.
- bowling-lab (4, spec): energy in collisions. Here forces in collisions.

## Who and how
- Grade 8, Science, module "Forces and Motion". Standards: MS-PS2-1 (apply Newton's third law to design a solution to a problem involving the motion of two colliding objects), MS-PS2-2 (plan an investigation to provide evidence that the change in an object's motion depends on the sum of the forces on the object and the mass of the object).
- Format: lab. Driver: one student alone, or pairs (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- The push bench with a plan card, up to three fans, up to three bricks, a felt strip, the results table; the crash bench with two meters, two crash types; four bumper materials, a weight limit and a length limit, up to eight tests. Extra: Real crash tests (how crash test dummies and crumple zones work). tool.json `modes: ["Track", "Real crash tests"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS2-2 | Plan a fair test, change push, mass or friction, record speed change | the plan card; the results table | 2 |
| MS-PS2-1 (force pairs) | Crash carts of different masses and read both meters | two equal peaks in opposite directions | 3 |
| MS-PS2-1 (design) | Build and test a bumper until the egg survives | the meter's peak; the egg; the test log | 4 |

## Screens and modes
Header (kit): title "Crash Test Lab"; `Track`, `Real crash tests`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright test hall with a long track, two carts, a brick stack, fans and a tiny seat with an egg, safety stripes on the floor. The welcome is queued (`welcomeAfter: true`): "Every good crash test starts with a plan. Pick one thing to change. Tap the plan card." First hint: "Tap the plan card."

**Push bench (focus: the cart).** At 1366x768 the track runs across the top with the table below; at 680x425 the track scrolls and the table is a sheet. The plan card has three blanks: I will change ___, keep the same ___, measure ___. Then the student adds fans, bricks or felt and taps `Go`. A speed gauge shows how fast speed changes. The table fills; the student taps the pattern: more push, faster change; more mass, slower change. If a plan changes two things, the row is marked "not fair" with a reason.

**Crash bench (focus: the meters).** Two carts, a bumper meter on each. Head-on or catch-up, any brick counts. After each crash both meters show the same peak (for a 1 kg cart and a 3 kg cart, both read 30 newtons), and the speed changes show the light cart's change is three times the heavy cart's. A card: "Who pushed harder? Neither."

**Design task.** The egg rides the front cart into a wall at a set speed. The student builds a bumper from spring, foam, clay or a crumple box within 200 grams and 10 cm. Each test shows the peak force and how long the push lasted; above the crack line the egg cracks (drawn as a small crack, no mess). A bumper that makes the push last 5 times longer cuts the peak about 5 times.

**The design card (the aha).** "My bumper is ___. The peak dropped from ___ to ___ because ___." Narrator: "In a crash, the forces always come in equal pairs. You can't stop that. You can only spread the push out over more time."

**The end.** The plan, the table, the crash readings and the design card. `Print` prints them.

**Real crash tests (extra).** How crumple zones, airbags and test dummies spread out a crash, from NHTSA and IIHS public pages.

## Content
- A stated cart model with friction, fans of set push, bricks of 1 kg, force meters, four bumper materials with stated stiffness and crush behavior, the crack line, the design card.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The plan card must be filled before the first `Go`.
- Keyboard: Tab to the plan, fans, bricks, felt, `Go`, crash type, bumper parts and the log; Enter acts.
- With Motion off carts jump to before and after and meters show peaks only.

## Look
- Accent `--brand` #b03a0f safety orange (header, meters, the plan card); gold #f4c542 (the part in hand, the peak marker); paper #fdf4ee; ink #2b0f05; muted #604f46.
- Contrast (WCAG 2.1, computed): white on brand 6.07:1; brand on paper 5.60:1; ink on paper 16.49:1; muted on paper 7.16:1; ink on gold 11.01:1.
- Never color alone: meters carry numbers and arrows; fair and not-fair rows carry words.
- Different from this batch (radio navy, orchid, bone tan, town green).

## Art
- Local FLUX (`scripts/localart.py`): the test hall (1, 16:9), a crash test dummy in a car for the extra (1, 16:9).
- Drawn in code: the track, carts, fans, bricks, meters, bumpers, the egg, the table.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as the test engineer; `lively-host` as the crash announcer and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.bench + ':' + state.test + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `plan`: "Fill in the plan card."
- how `go`: "Add fans, bricks or felt, then tap Go."
- how `crash`: "Pick a crash type, then tap Crash."
- event, whole, the equal-peaks card.
- how `bumper`: "Drag parts onto the bumper, then tap Test."
- event, whole, each test result.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
forces. Copies collision-lab's `/* FORCES ENGINE: begin */ ... /* FORCES ENGINE: end */` block unchanged and adds a fan push, friction strip and a bumper spring-damper step, so the block can move to `kit/forces.js` for the whole family. No momentum is shown on screen.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Plan | Change everything at once | The row is marked not fair and doesn't count. |
| Crash | Assume the heavy cart pushes harder | The meters show equal peaks; the card asks again. |
| Design | Stack every material | The weight and length limits refuse it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `plan`; `go`.
2. `crash`; equal-peaks card (whole), waits.
3. `bumper`; test result (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-PS2-1, MS-PS2-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Newton's third law: forces between two objects are equal and opposite | NASA Glenn Research Center, "Newton's Third Law" | The Physics Classroom, "Newton's Third Law" | yes |
| Acceleration grows with net force and shrinks with mass | NASA Glenn Research Center, "Newton's Second Law" | OpenStax, "College Physics 2e", chapter 4 | yes |
| Crumple zones and airbags lower peak force by lengthening the collision time | National Highway Traffic Safety Administration, "Air bags" | Insurance Institute for Highway Safety, "How crash tests work" | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r4, 2026-11-10): a 2 N push on 1 kg gives 2 m/s per second and on 2 kg gives 1; equal 30 N peaks change a 1 kg cart's speed three times as much as a 3 kg cart's; spreading the push over 0.1 s instead of 0.02 s cuts the peak by 5; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 track and table; at 680x425 scrolling track and sheet.
2. A fair test plan is made and push, mass and friction are tested. (MS-PS2-2)
3. Crashes of unequal carts show equal and opposite peaks. (MS-PS2-1)
4. A bumper within limits keeps the egg safe and the design card explains why. (MS-PS2-1)
5. No momentum math appears.
6. The egg cracks as a small drawn crack only.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: before and after and peaks only; no network requests.

## Open questions
- Overlap risk with collision-lab (default used: this tool stays with force pairs and fair tests, no momentum math; collision-lab keeps momentum and impulse).
