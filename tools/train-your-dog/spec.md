# Train Your Dog

## One idea
On adoption day the student takes home Biscuit, a shelter dog (made up and animated), with a clicker, a treat jar and a goals board, and trains her through five lessons: classical conditioning (the leash comes out before every walk until Biscuit wags at the leash alone, then extinction when the leash appears without walks, and spontaneous recovery a day later), operant conditioning (reward a sit, remove attention when she jumps up), four reinforcement schedules (fixed and variable, ratio and interval) on the same behavior with a live chart of response rate that shows why variable schedules resist extinction, shaping a new trick one small step at a time, and observational learning when a puppy watches Biscuit; the student predicts each curve before the run, and each lesson closes with a human example (a phone buzz, a slot machine, a fear after a dog bite, a younger sibling copying a skateboard trick); at the end the student writes a "why it worked" report using the right terms, and reads why reward-based training works better than punishment for dogs and people, so a twelfth grader learns classical, operant and observational learning, reinforcement schedules, extinction and shaping, and ties each to human behavior.

## Not like
- brain-explorer (12, spec): the brain's biology. Here learning from experience.
- one-life-many-stages (12, spec): development across a lifetime. Here learning in days.
- illusion-lab (12, spec): perception and memory. Here conditioning.
- go-along (12, concept): social pressure. Here rewards and signals.

## Who and how
- Grade 12, Psychology, module "Learning and Development". Standards: APA.Development and Learning (APA National Standards for High School Psychology Curricula, the learning half: classical and operant conditioning, schedules of reinforcement, extinction, shaping and observational learning; the lifespan half is taught in one-life-many-stages).
- Format: creature. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Five lessons with predictions and live charts, five human examples, the report. Extra: Predict first (the class predicts each curve together before each run and votes). tool.json `modes: ["Training", "Predict first"]`, `minutes: "30-40"`, `grades_label: "Grade 12"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| APA.Development and Learning (classical) | Pair the leash with walks, then present the leash alone, then stop pairing | Biscuit's wag to the leash rising, extinguishing and recovering on the chart | 2 |
| APA.Development and Learning (operant, schedules) | Choose a consequence and a schedule, predict the curve, run it, then stop rewards | response rate under four schedules and their extinction curves | 3 |
| APA.Development and Learning (shaping, observational) | Reward closer and closer steps to a trick; let the puppy watch | the shaping ladder; the puppy copying | 4 |
| APA.Development and Learning (human links) | Match each lesson's terms to a human example and write the report | the human example cards; the report with terms | 5 |

## Screens and modes
Header (kit): title "Train Your Dog"; `Training`, `Predict first`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A living room on adoption day. Biscuit, a medium brown shelter dog, sits by the door. On the table: a clicker, a treat jar, a leash and a goals board (wag at the leash, sit, stop jumping, a spin, a puppy who learns by watching). The welcome is queued (`welcomeAfter: true`): "Biscuit is home. She doesn't know any of your signals yet. You'll teach her, and you'll see learning happen on a chart. Tap the leash." First hint: "Tap the leash."

**Lessons (focus: Biscuit and the chart).** At 1366x768 Biscuit fills the left with the chart and controls right; at 680x425 the chart is a sheet. Each run takes about twenty seconds; the model's rules are stated on a card.
1. Classical: the leash (neutral, then conditioned stimulus) before each walk (unconditioned stimulus) brings a wag (conditioned response); then leash only (extinction); then a day later a small wag returns (spontaneous recovery). Human link: the stomach that growls at a lunch bell.
2. Operant: a treat after a sit (positive reinforcement); turning away when she jumps (negative punishment, removing attention). Human link: a phone buzz that keeps you checking.
3. Schedules: the same sit under fixed ratio, variable ratio, fixed interval and variable interval; the student predicts each curve first. Variable ratio gives the highest steady rate and lasts longest when rewards stop; fixed interval shows the scallop. Human link: a slot machine.
4. Shaping: reward a look, then a turn of the head, then a half turn, then a full spin. Human link: a coach praising each step closer to a clean free throw.
5. Observational: a neighbor's puppy watches Biscuit sit for a treat, then tries it. Human link: a younger sibling copying a skateboard trick; Bandura's Bobo doll study (1961).
- A fear lesson is told, not trained: a child bitten once fears all dogs (classical conditioning of fear), with a note on Watson and Rayner's 1920 "Little Albert" study and why it would not be allowed today.

**The report (the aha).** "Biscuit learned to ___ through ___. The schedule that lasted longest was ___ because ___. A person learns the same way when ___." Then the evidence card: veterinary behavior groups recommend reward-based training, and studies find it works at least as well as punishment with fewer stress signs. Narrator: "You didn't change Biscuit. You changed what happened after she acted."

**The end.** Biscuit's charts, the predictions beside the results, and the report. `Print` prints them.

**Predict first (extra).** The class predicts each curve and votes before each run.

## Content
- Biscuit and the puppy are made up and labeled; the learning model's rules (acquisition, extinction, recovery, schedule rates) are stated and match published patterns; five human examples; the evidence card.
- No punishment beyond removing attention is ever offered as a choice.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each run waits for a prediction; the chart draws as the run plays.
- Keyboard: Tab to tools, the schedule picker, the prediction and the chart; Space clicks the clicker; Enter runs.
- With Motion off Biscuit changes pose without animating and the chart draws all at once.

## Look
- Accent `--brand` #8f3f0f biscuit brown (header, the clicker, the chart); gold #f4c542 (the treat, the current run); paper #fbf3ee; ink #26100a; muted #5f554f.
- Contrast (WCAG 2.1, computed): white on brand 7.28:1; brand on paper 6.64:1; ink on paper 16.50:1; muted on paper 6.61:1; ink on gold 11.12:1.
- Never color alone: chart lines carry labels and markers; schedules carry names.
- Different from this batch (lifespan rose, chart navy, Fed green, trait indigo).

## Art
- Illustrated Biscuit with poses (sit, wag, jump, spin, lie down) and the puppy (Gemini, 2 characters with pose sheets; cutout yes).
- Local FLUX (`scripts/localart.py`): the living room (1, 16:9), a park path (1, 16:9).
- Drawn in code: the charts, the clicker, the shaping ladder.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as the trainer friend and hints; `easy-coach` as the explainer of each term and human example. `Curio.voice` with `scope: () => state.mode + ':' + state.lesson + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `predict`: "Draw your prediction on the chart."
- how `run`: "Press Run and watch Biscuit."
- event, whole, each run's result.
- event, whole, each human example.
- how `report`: "Write why it worked, with the terms."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the dog with poses, the learning model, live charts, the shaping ladder, the report.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Draw a flat line every time | Predictions aren't scored, but the report asks why the student's guess differed. |
| Schedules | Run only one | The report needs the schedule that lasted longest, which needs all four. |
| Report | Skip the terms | The report checks for at least four terms used correctly. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `predict`; `run`; result (whole).
2. Human example (whole), waits.
3. The next lesson.
4. `report`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| APA.Development and Learning wording | APA, "National Standards for High School Psychology Curricula" (2022) | data/modules/social-studies.txt | yes |
| Classical conditioning, extinction and spontaneous recovery | Pavlov, "Conditioned Reflexes" (Oxford, 1927) | Bouton, "Learning and Behavior" (Sinauer, 2016) | yes |
| Schedules: variable ratio highest and most resistant to extinction; fixed-interval scallop | Ferster and Skinner, "Schedules of Reinforcement" (Appleton, 1957) | Domjan, "The Principles of Learning and Behavior" (7th ed., 2015) | yes |
| Observational learning (Bobo doll, 1961) | Bandura, Ross and Ross, Journal of Abnormal and Social Psychology (1961) | APA, "Bandura" biography | yes |
| "Little Albert" (1920) and its ethics | Watson and Rayner, Journal of Experimental Psychology (1920) | Harris, American Psychologist (1979) | yes |
| Reward-based training recommended; punishment linked to stress signs | American Veterinary Society of Animal Behavior, position statement (2021) | China, Mills and Cooper, Frontiers in Veterinary Science (2020) | yes |
| Variable reinforcement in slot machines and phone checking | Domjan (2015) | Schüll, "Addiction by Design" (Princeton, 2012) | yes |
Backed twice: 7. Cut: 0.

Checks run (Python, scratchpad r23, 2026-11-09): four schedules, two ratio and two interval, two fixed and two variable; five lessons each have a human example; a twenty-second run at 10 frames a second is 200 points; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 Biscuit and chart; at 680x425 sheet.
2. The classical lesson shows acquisition, extinction and recovery. (APA.Development and Learning)
3. Four schedules run with predictions and extinction curves. (APA.Development and Learning)
4. Shaping and observational learning both run. (APA.Development and Learning)
5. The report uses four terms correctly with a human example. (APA.Development and Learning)
6. No punishment beyond removing attention is offered.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still poses; no network requests.

## Open questions
None.
