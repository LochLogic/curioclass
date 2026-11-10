# Who Wins?

## One idea
On a zoo stage a referee hippo in a striped shirt brings out two animals at a time and asks about one thing at once ("Who is longer?", "Who is taller?", "Who is heavier?"); the child taps a guess, then drags both animals to the start line for longer, stands them on the same floor line for taller, or sets them on a big balance for heavier, and the tool marks the winner while the hippo says it in words ("The crocodile is longer. The zebra is shorter."); in fair-start rounds one animal stands ahead of the line and the hippo asks "Is that fair?" so the child slides it back; in the big switch the crocodile wins longer but the zebra wins taller, and the giraffe wins taller but the elephant wins heavier, so "bigger" needs a word (longer, taller or heavier); finally a "what can we measure?" card shows one animal and the child taps its length, its height and its weight, so a kindergartner learns to describe measurable attributes of objects such as length and weight, and to directly compare two objects with one attribute in common to see which has more of it or less of it.

## Not like
- snack-scale (K, spec): comparing how many. Here comparing how long, tall and heavy.
- paperclip-ruler (1, concept): measuring with units. Here comparing side by side.
- estimation-station (2, spec): rulers and estimates. Here no numbers at all.
- sheep-count (K, spec): counting. Here measuring.

## Who and how
- Kindergarten, Math, module "Longer, Heavier, Bigger". Standards: K.MD.1 (describe measurable attributes of objects, such as length or weight; describe several measurable attributes of a single object), K.MD.2 (directly compare two objects with a measurable attribute in common, to see which object has "more of" or "less of" the attribute, and describe the difference).
- Format: showdown (the hippo narrates so one child can play alone). Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- Six animals, ten face-off rounds (four longer, three taller, three heavier), two fair-start rounds, the big switch, three "what can we measure?" cards. Extra: Thumbs vote (the class votes before each reveal). tool.json `modes: ["Stage", "Thumbs vote"]`, `minutes: "10-15"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.MD.2 | Guess, then line up ends or use the balance | the start line; the floor line; the balance tipping | 2 |
| K.MD.2 (fair start) | Slide an animal back to the line | "Is that fair?"; the fixed line-up | 3 |
| K.MD.1 | Tap length, height and weight on one animal; see different winners | the measure card; the big switch | 4 |

## Screens and modes
Header (kit): title "Who Wins?"; `Stage`, `Thumbs vote`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A bright zoo stage with a curtain, a start line painted on the floor and a big balance at the side. The referee hippo waves a flag. A crocodile and a zebra walk out. The welcome is queued (`welcomeAfter: true`): "Welcome to Who Wins! Who is longer, the crocodile or the zebra? Tap your guess." First hint: "Tap the animal you think is longer."

**A face-off (focus: the two animals).** At 1366x768 the stage fills the screen with the guess buttons below; at 680x425 the animals sit side by side and scale to fit. After the guess, the child drags both to the start line (longer), stands them on the floor line (taller), or drags them onto the balance pans (heavier). A bright edge marks the winner. The hippo says both words: longer and shorter, taller and shorter, heavier and lighter.

**Fair start.** One animal stands a step past the line. "Is that fair?" The child taps No and slides it back. "Now they start at the same place."

**The big switch (the aha).** Crocodile and zebra: the crocodile is longer, the zebra is taller. Giraffe and elephant: the giraffe is taller, the elephant is heavier. The hippo: "Who's bigger? It depends! Bigger how? Longer, taller or heavier?"

**What can we measure?** One animal fills the stage. The child taps three buttons: How long (a tape runs nose to tail), How tall (a tape runs floor to head), How heavy (a scale appears under it).

**The end.** A trophy shelf with each winner and its word. `Print` prints it.

**Thumbs vote (extra).** The class shows thumbs before each reveal.

## Content
- Six animals with true relative sizes (crocodile, zebra, giraffe, elephant, penguin, kangaroo), ten rounds, two fair-start rounds, the big switch, three measure cards, all spoken. No animal is hurt; the balance is gentle.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Animals can be dragged back and forth; the result shows only once both ends are on the line.
- Keyboard: Tab to guess buttons, animals, the line, the balance and measure buttons; Enter picks; arrows move an animal.
- With Motion off animals jump to the line and the balance tips without swinging.

## Look
- Accent `--brand` #a2460f zoo orange (header, the start line, buttons); gold #f4c542 (the winner's edge, the flag); paper #fdf5ef; ink #2a1205; muted #5f5047.
- Contrast (WCAG 2.1, computed): white on brand 6.14:1; brand on paper 5.70:1; ink on paper 16.41:1; muted on paper 7.15:1; ink on gold 10.88:1.
- Never color alone: winners carry a star and the word.
- Different from this batch (meadow green, playground blue, spy purple, robot red).

## Art
- Local FLUX (`scripts/localart.py`): the zoo stage (1, 16:9), the referee hippo in three poses (3, 1:1), six animals side views drawn to true relative size (6, 1:1).
- Drawn in code: lines, the balance, tapes, stars.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the referee hippo; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `guess`: "Tap the animal you think wins."
- how `lineup`: "Drag both animals to the start line."
- how `balance`: "Drag both animals onto the balance."
- how `fair`: "Tap Yes or No."
- event, whole, each result in two words.
- event, whole, the big switch.
- how `measure`: "Tap How long, How tall or How heavy."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the line-up check, the balance, the measure tapes. Animal sizes sit in a marked block `/* WHO-WINS DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Guess | Guess at random | Guesses aren't scored; the check always runs. |
| Line-up | Leave one animal ahead | The result waits until both ends are on the line. |
| Measure | Tap one button | The card needs all three. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `guess`; `lineup`.
2. Result (whole), waits.
3. `fair`; `balance`.
4. Big switch (whole), waits. `measure`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for K.MD.1, K.MD.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Direct comparison needs ends lined up | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
| Crocodile about 4.5 m long; plains zebra about 2.3 m long and 1.3 m at the shoulder | Smithsonian National Zoo, "Crocodiles" and "Plains zebra" | San Diego Zoo Wildlife Alliance, animal fact pages | yes |
| Giraffe about 5 m tall and 1,200 kg; African elephant about 3.2 m at the shoulder and 6,000 kg | Smithsonian National Zoo, "Giraffe" and "African elephant" | San Diego Zoo Wildlife Alliance, animal fact pages | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r6, 2026-11-10): the crocodile is longer than the zebra and the zebra taller; the giraffe is taller than the elephant and the elephant five times heavier; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 stage and buttons; at 680x425 scaled animals.
2. Ten face-offs are checked by lining up or the balance. (K.MD.2)
3. Two fair-start rounds are fixed. (K.MD.2)
4. The big switch and three measure cards name length, height and weight. (K.MD.1)
5. Every card is spoken; every control is 64 px or more.
6. Animal sizes match the cited zoo pages; no animal is hurt.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps and still balance; no network requests.

## Open questions
- The idea card flags a data source (default used: typical adult sizes from the Smithsonian National Zoo and San Diego Zoo Wildlife Alliance, checked before build; pairs chosen so each winner is clear).
