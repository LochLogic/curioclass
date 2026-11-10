# Parachute Teamwork

## One idea
On a bright gym floor a rainbow parachute lies flat with eight cartoon kids around its edge, one of them in a wheelchair holding the edge with both hands, and one empty spot that is the child's; Coach Lulu (made up, labeled "illustration") says "Stand up. You hold this edge," and calls the classic games one at a time, small waves, big waves, the mushroom, popcorn and trading places, and the child copies the arm move at home while the cartoon kids move with the call; the parachute only works when everyone moves together, so when one cartoon kid pulls early the mushroom collapses, and the child picks the fix (wait for "three", say it together) and tries again until the dome rises; in trading places the kids run under one color at a time, and the child cheers for others ("Go, Sam!") and hears the circle cheer back on the child's turn; before the games and after them the child puts a hand on their chest and taps slow, medium or fast, and sees their own heart picture speed up; at the end the parachute flies because the whole group moved together, and moving made the child's heart beat faster and feel good, so a child in kindergarten to grade 2 learns to work together, take turns and follow rules in parachute games, and to notice how moving feels.

## Not like
- animal-moves (Grades K-2, live): copying animal moves alone. Here moving with a group.
- target-toss (Grades K-2, spec): a throwing experiment. Here cooperation and turns.
- friend-moves-practice (K, spec): friend words at play. Here following calls together.
- fridge-goal-chart (K, spec): a health goal at home. Here a group game.

## Who and how
- Grades K-2, Physical Education, module "Cooperative Games". Standards: SHAPE.S3 (develops social skills through movement), SHAPE.S4 (personal skills, benefits of movement, chooses to engage), SHAPE America National PE Standards (2024).
- Format: showdown. Driver: one child alone at home or in class (tool.json `driver: "student"`). Every word is spoken. Controls 60 px or more.
- Five games, the collapse-and-fix moment, trading places with cheers, two heart checks. Extra: Real parachute (the board calls the games, counts each lift and shows whose turn it is). tool.json `modes: ["Play", "Real parachute"]`, `minutes: "10-15"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SHAPE.S3 | Follow the call; fix the early pull; take turns and cheer | the dome rising; turns by color | 2 |
| SHAPE.S4 | Check the heart before and after; say why moving is good | the heart speeding up | 3 |

## Screens and modes
Header (kit): title "Parachute Teamwork"; `Play`, `Real parachute`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** The gym, the parachute, eight kids and the empty spot glowing gold, and Coach Lulu with a whistle. The welcome is queued (`welcomeAfter: true`): "Stand up. You hold this edge. Tap the heart to check it first." First hint: "Tap the heart."

**Heart check.** A big heart button; the child puts a hand on their chest and taps slow, medium or fast (pictures of a turtle, a dog, a rabbit).

**Games (focus: the parachute).** At 1366x768 the parachute fills the view with the call card on top; at 680x425 the call card is a banner. Coach Lulu calls a game; the child taps `Ready` and copies the move; the cartoon kids move with the call.

**Collapse.** In the mushroom one kid lifts early and the dome falls. Two fix cards with pictures: "Wait for three" and "Say it together". The child taps one and the circle tries again.

**Trading places.** Colors are called one at a time; the child taps `Cheer` for each runner, then runs on their color.

**Together (the aha).** Coach Lulu: "We did it together! And feel your heart. Moving makes it go fast."

**The end.** Two heart pictures side by side and a sticker. `Print` prints a parachute game card.

**Real parachute (extra).** Class calls.

## Content
- Every call, card and button is spoken.
- Kids vary in looks, size and ability; the wheelchair user plays every game, including trading places.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Games can be replayed in any order after the first.
- Keyboard: Tab to the heart, Ready, fix cards and Cheer; Enter picks.
- With Motion off the parachute shows still poses for each move.

## Look
- Accent `--brand` #b0233a parachute red (header, buttons); gold #f4c542 (the child's spot, the call in focus); paper #fdf0f2; ink #2e0710; muted #5e4a4f.
- Contrast (WCAG 2.1, computed): white on brand 6.67:1; brand on paper 6.01:1; ink on paper 16.40:1; muted on paper 7.37:1; ink on gold 11.19:1.
- Never color alone: color calls also show a shape on each panel (star, circle, square); hearts carry animal pictures.
- Different from this batch (range sage, fridge blue, playground orange, gym purple).

## Art
- People (illustrated): Coach Lulu and eight kids, labeled "illustration" (Gemini, `people: true`, 9; cutout yes).
- Local FLUX (`scripts/localart.py`): the gym (1, 16:9).
- Drawn in code: the parachute (panels, waves, the dome), heart pictures, cards.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as Coach Lulu; `playful-friend` as the circle's cheers and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.game + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `heart`: "Tap the heart, then tap how fast it feels."
- how `ready`: "Tap Ready and move your arms."
- how `fix`: "Tap a fix card."
- how `cheer`: "Tap Cheer for your friend."
- how `run`: "It's your color. Tap Run."
- event, whole, together.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the parachute animation, calls and timing, the collapse, color turns, heart check records.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Games | Tap Ready early | The move starts on the count, and early taps collapse the dome. |
| Fix | Skip it | The mushroom needs a fix before it rises. |
| Heart | Tap one answer twice | Both checks are shown side by side to compare. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `heart`.
2. `ready`; `fix`.
3. `cheer`; `run`.
4. Together (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SHAPE 2024 S3 and S4 wording | data/standards/shape-pe-2024.txt | data/modules.csv module line | yes |
| Parachute games build cooperation and turn-taking | SHAPE America, PE lesson resources on cooperative games | PE Central, "Parachute activities" lesson ideas | yes |
| Moving raises heart rate, and children 6 and up need 60 minutes a day | U.S. Department of Health and Human Services (2018), Physical Activity Guidelines for Americans, 2nd edition | Centers for Disease Control and Prevention, "Physical Activity Basics" for children | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s26, 2026-11-10): five games and two heart checks fit in about 10 minutes; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 parachute and call card; at 680x425 call as a banner.
2. Five games are played, the collapse fixed, and every turn cheered. (SHAPE.S3)
3. Two heart checks are compared and why moving is good is said. (SHAPE.S4)
4. Every kid, including the wheelchair user, plays every game.
5. Every word is spoken.
6. `Read` reads every card; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still poses; no network requests.

## Open questions
None.
