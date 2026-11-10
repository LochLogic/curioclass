# Morning Meeting Board

## One idea
In a bright classroom the class leader of the day, Tavi (made up, labeled "illustration"), stands by the morning board, which has six labeled boxes, Weather, Lunch, Helper, Day, Class and Birthday, each holding a picture sign (a sun, a taco, a smiling helper, "Monday", "Room 4 Owls", a cake with no name yet); the child taps a box to hear its name and what its sign means, learning that a picture can carry information; then the child predicts, dragging each box to "changes by lunch", "changes tomorrow" or "never changes", and slides a time handle to lunch and then to tomorrow to watch the board update: clouds roll in over the sun, the helper's face changes tomorrow, the day turns to "Tuesday", and "Room 4 Owls" stays all year; first graders tell a box's name apart from what is in it today ("The box is Helper; today it holds Maya."), and second graders predict every box, then add a box of their own (pet of the week, library day) and decide whether it will change; at the end the child sees that a box keeps its name while the sign inside it changes, and a few boxes never change at all, so a child in kindergarten to grade 2 learns that symbols carry information and that named values can change or stay the same, the first idea behind variables.

## Not like
- score-keeper (3, live): variables in a game. Here named boxes on a board.
- robot-dance (K, live): a sequence of steps. Here values that change over time.
- feelings-weather-report (Grades K-2, live): feeling words. Here picture signs as data.
- question-jar (K, concept): questions data can answer. Here values with names.

## Who and how
- Grades K-2, Computer Science, module "Signs and Changing Values". Standards: EK-PRO-VD-05, E1-PRO-VD-05, E2-PRO-VD-05 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Symbols that carry information; named values that change or stay the same").
- Format: showdown, solo default (one child makes every prediction). Driver: one student alone (tool.json `driver: "student"`). Every word is spoken; `Read` reads every box. Controls 60 px or more.
- One board with six boxes, three prediction rounds (lunch, tomorrow, next week), one add-a-box round. Extra: Class vote (the class stands for "changes" or sits for "stays" before the handle moves). tool.json `modes: ["Board", "Class vote"]`, `minutes: "10-15"`, `grades_label: "Grades K-2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| EK-PRO-VD-05 | Tap boxes; hear what each sign means | pictures that carry information | 2 |
| E1-PRO-VD-05 | Tell the box name from what is in it | "Helper" holds "Maya" | 3 |
| E2-PRO-VD-05 | Predict changes; add a box | the board updating over time | 4 |

## Screens and modes
Header (kit): title "Morning Meeting Board"; `Board`, `Class vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 60 px or more.

**On load and first tap.** A cheerful classroom wall with the morning board, six labeled boxes, a big clock with a time handle, and Tavi holding a pointer. The welcome is queued (`welcomeAfter: true`): "This is our morning board. Tap a box to hear what it says." First hint: "Tap a box."

**Read the board (focus: the board).** At 1366x768 the board fills the center with the time handle below; at 680x425 the boxes wrap to two rows. Each tap speaks the box name, then its sign ("Weather. The sun means it's sunny.").

**Name and inside (grade 1).** Tavi points: "Is Helper the name or what's inside?" The child taps the label or the picture to answer, for each box.

**Predict.** Three bins appear: "changes by lunch", "changes tomorrow", "never changes". The child drags a copy of each box. Then `Slide time` moves the handle to lunch, to tomorrow, and to next week; boxes that change flip with a card-turn, and predictions are marked right or not with a reason.

**Add a box (grade 2).** The child picks a new box (pet of the week, library day, snack) and its first sign, decides if it will change, and watches next week.

**Name stays, sign changes (the aha).** Tavi: "The box keeps its name. What's inside can change. And some boxes never do."

**The end.** The board with the child's box. `Print` prints a blank board for class.

**Class vote (extra).** Stand or sit votes before each slide.

## Content
- Six boxes and twelve signs, high contrast for projectors, all spoken; the helper names are made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Predictions can be moved until `Slide time`; the handle can go back.
- Keyboard: Tab to boxes, labels and pictures, the bins, the time handle (arrows move it) and add-a-box choices; Enter picks or drops.
- With Motion off boxes change without the card-turn.

## Look
- Accent `--brand` #1f4e9a board blue (header, box frames, buttons); gold #f4c542 (the box in hand, a changed box); paper #eef3fb; ink #081a38; muted #4b5463.
- Contrast (WCAG 2.1, computed): white on brand 8.03:1; brand on paper 7.21:1; ink on paper 15.51:1; muted on paper 6.86:1; ink on gold 10.63:1.
- Never color alone: changed boxes show a small "new" star and are spoken.
- Different from this batch (honey brown, attic rose, street-fair green, bamboo teal).

## Art
- People (illustrated): Tavi and six helper faces, labeled "illustration" (Gemini, `people: true`, 7; cutout yes).
- Local FLUX (`scripts/localart.py`): the classroom wall (1, 16:9), picture signs (12, 1:1).
- Drawn in code: box frames, labels, bins and the clock.
About 20 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as Tavi; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.box + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `read`: "Tap a box."
- how `name`: "Tap the name, or tap what's inside."
- how `predict`: "Drag each box to a bin."
- how `slide`: "Tap Slide time."
- how `add`: "Pick a new box, then pick its sign."
- event, whole, name stays, sign changes.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the board as a list of named values with a change schedule, the time handle, prediction bins, the add-a-box step.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predict | Put every box in one bin | Each box has its own right bin, shown when time slides. |
| Name and inside | Tap the picture every time | Half the questions ask for the name. |
| Add a box | Skip the decision | The new box will not join until it is decided. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `read`.
2. `name`.
3. `predict`; `slide`; `add`.
4. Name stays, sign changes (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| A variable is a named container whose value can change, taught early with concrete labels | CSTA K-12 Computer Science Standards (2017), 1A-AP-09 and its clarification | K-12 Computer Science Framework (2016), Algorithms and Programming, grades K-2 "Variables" | yes |
| Morning meeting routines with a class board are common in K-2 | Responsive Classroom, "The Morning Meeting Book" | Kriete and Davis (2014), "The Morning Meeting Book", 3rd edition, Center for Responsive Schools | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s22, 2026-11-10): six boxes; two change by lunch (weather, lunch), two change tomorrow (helper, day), one changes next week (birthday), one never (class); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 board and clock; at 680x425 boxes in two rows.
2. Every box is read, with its sign's meaning spoken. (EK-PRO-VD-05)
3. Box names are told apart from what they hold. (E1-PRO-VD-05)
4. Changes are predicted and checked over time, and a new box is added and decided. (E2-PRO-VD-05)
5. Signs are high contrast for projectors.
6. `Read` reads every box; every control is 60 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: boxes change at once; no network requests.

## Open questions
None.
