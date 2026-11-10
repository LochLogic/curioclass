# Carnival Odds

## One idea
At a school carnival the organizer, Ms. Adeyemi (made up, labeled "illustration"), pins a fairness inspector badge on the child because parents say the dice game never pays out, and five booths wait on the midway (a four-color spinner, a two-dice toss, a duck pond with 3 gold ducks among 20, a two-coin flip and a ring toss), with prizes in tickets only; likelihood rounds place each booth's chance on a 0 to 1 line (impossible, unlikely, even, likely, certain) before any play; run rounds play a booth 10 times, then 100, then 10,000 at the press of a button, and a relative-frequency line wobbles and then settles near the model, so the child predicts about 50 sevens in 300 tosses of two dice; model rounds build a probability model (equal chances for a fair spinner, 3/20 for a gold duck), compare it with runs, and explain a mismatch (one spinner is bent and lands on red far too often, so it is rigged); compound rounds find two dice summing to 7 (6 of 36, so 1/6), two coins both heads (1/4) and a spinner then a coin (1/8) with organized lists, tables and trees, each checked by simulation; in the design round the child builds a simulation for a question (if 40% of donors have type O blood, how often are exactly 4 of 10 donors type O? about 25% of the time) and a fair booth for next year; at the end the child sees that a few plays can fool you, many plays settle near the model, and a model can catch a cheat, so a seventh grader learns probability as a number from 0 to 1, long-run relative frequency, probability models, and compound events with lists, tables, trees and simulations.

## Not like
- jellybean-jar (7, concept): sampling a population, same grade. Here chance events.
- game-show-strategist (12, spec): expected value and decisions. Here probabilities and fairness.
- medical-test-paradox (10, spec): conditional probability, same engine. Here simple and compound events.
- question-lab (6, spec): describing data from a survey. Here data from chance.

## Who and how
- Grade 7, Math, module "Probability". Standards: 7.SP.5 (understand that the probability of a chance event is a number between 0 and 1 that expresses the likelihood of the event occurring; larger numbers indicate greater likelihood; a probability near 0 indicates an unlikely event, a probability around 1/2 indicates an event that is neither unlikely nor likely, and a probability near 1 indicates a likely event), 7.SP.6 (approximate the probability of a chance event by collecting data on the chance process that produces it and observing its long-run relative frequency, and predict the approximate relative frequency given the probability), 7.SP.7 (develop a probability model and use it to find probabilities of events; compare probabilities from a model to observed frequencies; if the agreement is not good, explain possible sources of the discrepancy: a. uniform models; b. models from observed frequencies), 7.SP.8 (find probabilities of compound events using organized lists, tables, tree diagrams, and simulation; represent sample spaces; identify the outcomes in the sample space which compose the event; design and use a simulation to generate frequencies for compound events).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five booths, one rigged spinner, six compound questions, the simulation designer, the booth designer. Extra: Class pool (the class pools runs on the projector). tool.json `modes: ["Midway", "Class pool"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.SP.5 | Place each booth's chance on the 0 to 1 line | booths along the line with words | 2 |
| 7.SP.6 | Run booths 10, 100, 10,000 times; predict | the frequency line settling | 2 |
| 7.SP.7 | Build models; compare with runs; catch the rigged spinner | model against result bars | 3 |
| 7.SP.8 | List, table, tree; design a simulation | 6 of 36; the tree to 1/8; the donor simulation | 4 |

## Screens and modes
Header (kit): title "Carnival Odds"; `Midway`, `Class pool`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A school carnival midway at dusk with five booths and string lights, a ticket counter, and Ms. Adeyemi holding a clipboard and a badge. The welcome is queued (`welcomeAfter: true`): "Parents say the dice game never pays. Before we play, where does each booth's chance go? Drag the spinner booth onto the line." First hint: "Drag a booth onto the chance line."

**Chance line (focus: the line).** At 1366x768 the midway fills the top with the 0 to 1 line below and the inspector notebook right; at 680x425 the notebook is a tab. Booth icons drop on the line; words sit under it.

**Run rounds.** At a booth the child taps `Play 10`, `Play 100` or `Play 10,000`. A converging line shows the running share of wins against a dashed model line. Before 300 plays of the dice, the child types a prediction.

**Models.** The child builds a model table for each booth (outcomes and probabilities that add to 1). Bars compare model and results. The bent spinner shows red far above 1/4 after 10,000 spins; the child picks an explanation and writes it in the notebook.

**Compound.** Two dice: a 6 by 6 table lights the sums of 7. Two coins: an organized list. Spinner then coin: a tree with products at the leaves. Each is checked by a simulation run.

**Design.** The child picks a tool to simulate donors (a spinner with 40% shaded, or random digits 0 to 3 for type O), runs 1,000 groups of 10, and reads how often exactly 4 are type O. Then the child designs a fair booth, sets its prize in tickets, and tests it.

**Many plays (the aha).** Ms. Adeyemi: "Ten plays can fool you. Ten thousand settle near the model. And the model catches the cheat."

**The end.** The inspector report. `Print` prints it.

**Class pool (extra).** Runs pooled on the projector.

## Content
- Five booths, prizes in tickets (never money), no betting words; all readable with `Read`.
- The type O figure is a stated assumption ("suppose 40%"), not a claim about real donors.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Model tables can be edited until `Compare`; runs can be stopped.
- Keyboard: Tab to booths, the line (arrows move by 0.05), Play buttons, table cells, tree branches and the designer; Enter places or plays.
- With Motion off runs finish at once and the line draws in full.

## Look
- Accent `--brand` #a3262b midway red (header, booth awnings, buttons); gold #f4c542 (the booth in hand, a win); paper #fbeff0; ink #2c0a0b; muted #5f4f50.
- Contrast (WCAG 2.1, computed): white on brand 7.32:1; brand on paper 6.52:1; ink on paper 16.19:1; muted on paper 6.88:1; ink on gold 11.18:1.
- Never color alone: spinner sections carry letters (R, B, Y, G); model and result bars are labeled.
- Different from this batch (signal orange, balloon sky blue, diner teal, licorice purple).

## Art
- People (illustrated): Ms. Adeyemi and visitors, labeled "illustration" (Gemini, `people: true`, 3; cutout yes).
- Local FLUX (`scripts/localart.py`): the midway (1, 16:9), five booths (5, 1:1).
- Drawn in code: spinners, dice, ducks, coins, the chance line, tables, trees, the converging line.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `upbeat-guide` as Ms. Adeyemi; `news-reader` as the inspector report and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.booth + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `place`: "Drag a booth onto the chance line."
- how `play`: "Tap Play 10 to start."
- how `predict`: "Type your prediction, then tap Play."
- how `model`: "Fill in the model table."
- how `compound`: "Tap the outcomes that make the event."
- how `design`: "Pick a tool for the simulation."
- event, whole, many plays.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
probability (`kit/probability.js`), as described in medical-test-paradox's spec. Uses `Rand(seed)` for repeatable runs, `Trials` in batches, `Tally`, `Converge` with `logX: true` for 10 to 10,000 plays, `TwoWay` for the dice table and `Tree` with `show: 'probs'`, and `Frac` for exact models. Tool-only code: booths, the chance line, the rigged spinner, the simulation and booth designers.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Wait for the run | Play stays off until a prediction is typed. |
| Rigged spinner | Blame bad luck | After 10,000 spins only the "bent spinner" reason passes. |
| Compound | Add the chances | 1/2 + 1/2 for two heads is caught; the list shows 1/4. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `place`; `play`; `predict`.
2. `model`.
3. `compound`; `design`.
4. Many plays (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.SP.5 to 7.SP.8 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Small samples mislead; relative frequency settles in the long run | American Statistical Association, "GAISE II" (2020) | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Statistics and Probability" | yes |
| Students often add probabilities of independent events | Konold (1989), "Informal conceptions of probability", Cognition and Instruction | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Statistics and Probability" | yes |
Backed twice: 3. Cut: 0.

Sensitivity: prizes are tickets, never money; no betting framing anywhere.

Checks run (Python, scratchpad s19, 2026-11-10): 6 of 36 dice pairs sum to 7, so 1/6, and 300 x 1/6 = 50; two heads 1/2 x 1/2 = 1/4; spinner of 4 then coin 1/8; a gold duck 3/20; exactly 4 of 10 at 0.4 is C(10, 4) x 0.4^4 x 0.6^6, about 0.25; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 midway, line and notebook; at 680x425 notebook as a tab.
2. Five booths are placed on the 0 to 1 line and run with predictions. (7.SP.5, 7.SP.6)
3. Models are built, compared with runs, and the rigged spinner is explained. (7.SP.7)
4. Compound events are found with lists, tables, trees and a designed simulation. (7.SP.8)
5. Prizes are tickets; no money or betting words.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: runs finish at once; no network requests.

## Open questions
None.
