# Remainder Loop

## One idea
On a clean board the child divides 1 by 7 the long way, one step at a time, and every remainder drops onto a loop of numbered stops from 0 to 6 that sits beside the division; the remainders come 1, 3, 2, 6, 4, 5 and then 1 again, and the moment a remainder lands on a stop already lit the loop closes, the digits 142857 start over, and the bar goes over the repeat, so 1/7 = 0.142857 repeating; the child tries more fractions and predicts first: 1/8 lands on 0 after three steps, so 0.125 ends; 5/12 gives remainders 5, 2, 8, 8, so 0.41666... repeats only the 6; 3/11 gives 0.2727...; for each one the child marks "ends" or "repeats" and the length of the repeat; then the question turns: dividing by 7 has only seven possible remainders, 0 to 6, so within seven steps a remainder must be 0 (the decimal ends) or come back (the decimal repeats), and the child writes that reason for any denominator; a final sort guesses which fractions end from their denominators before dividing, and the loop confirms; at the end the child sees that every fraction's decimal ends or repeats because there are only so many remainders, so a seventh grader learns to convert a rational number to a decimal using long division and to know that its decimal form terminates in 0s or eventually repeats.

## Not like
- hot-air-and-sandbags (7, spec): operations with signed numbers. Here decimal forms of fractions.
- square-root-hunt (8, concept): irrational numbers that never repeat. Here rationals that must.
- zoom-by-tens (5, spec): decimal place value. Here why decimals end or repeat.
- camp-cook-share-out (5, spec): fractions as division with pictures. Here division digit by digit.

## Who and how
- Grade 7, Math, module "Terminating and Repeating Decimals". Standards: 7.NS.2d (convert a rational number to a decimal using long division; know that the decimal form of a rational number terminates in 0s or eventually repeats).
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twelve fractions to divide, the remainder loop, the reason builder, eight denominator guesses. Extra: Class chart (the class collects repeat lengths for 1/2 to 1/20 on the projector). tool.json `modes: ["Lab", "Class chart"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.NS.2d (long division) | Divide step by step; place each remainder | the loop lighting stop by stop | 2 |
| 7.NS.2d (ends or repeats) | Mark ends or repeats and the repeat length | 0.125; 0.142857 repeating; 0.41666... | 3 |
| 7.NS.2d (why) | Build the reason; predict from denominators | only so many remainders | 4 |

## Screens and modes
Header (kit): title "Remainder Loop"; `Lab`, `Class chart`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A dark-green board with 7 into 1.000000 set up in long division, and beside it a ring of seven stops numbered 0 to 6. The welcome is queued (`welcomeAfter: true`): "Watch the remainders. How many sevens in ten? Type the next digit." First hint: "Type the next digit."

**Divide (focus: the division).** At 1366x768 the division is on the left with the loop right and the decimal growing on top; at 680x425 the loop is a tab. Each step: the child types the digit, then the remainder; the remainder lights its stop and an arrow joins it to the last one. When a lit stop is hit again, the loop glows, the repeating digits are marked, and a bar appears over them.

**More fractions.** Cards: 1/8, 5/12, 3/11, 1/3, 2/9, 7/20, 1/6, 4/15, 5/16, 1/13, 3/40. Before dividing, the child guesses "ends" or "repeats". Each has its own loop with stops 0 to d - 1.

**Why.** A reason builder with blocks ("there are only", "possible remainders", "so within", "steps", "a remainder must be 0 or come back"). The child builds the reason and applies it to 1/97 without dividing (at most 96 steps before it repeats).

**Guess from the bottom.** Eight denominators; the child sorts which will end. The loop checks each one. A hint card notes the ones that end have only 2s and 5s as factors, after the sort, not before.

**Only so many (the aha).** Narrator: "There are only so many remainders. Sooner or later you hit zero, or you come back around."

**The end.** The fraction log with bars. `Print` prints it.

**Class chart (extra).** Repeat lengths for 1/2 to 1/20.

## Content
- Twelve fractions, proper and improper, positive and negative (-3/8 = -0.375), all readable with `Read`.
- The loop never shows more than 40 stops; larger denominators are reasoned about, not divided.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Digits can be retyped until the step is checked.
- Keyboard: Tab to the digit box, the remainder box, the loop (arrows move between stops), cards and reason blocks; Enter checks a step.
- With Motion off arrows and the glow appear at once.

## Look
- Accent `--brand` #44388a loop indigo (header, the loop, buttons); gold #f4c542 (the digit in hand, the closing stop); paper #f2f0f9; ink #140f2e; muted #52505e.
- Contrast (WCAG 2.1, computed): white on brand 9.64:1; brand on paper 8.54:1; ink on paper 16.36:1; muted on paper 6.97:1; ink on gold 11.35:1.
- Never color alone: lit stops carry a dot and their step number; the repeat has a bar.
- Different from this batch (blueprint blue, reef green, case-file brown, factory red).

## Art
- Drawn in code: the board, the division, the loop and the decimal, because the remainders are the picture.
No generated images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator; `clear-teacher` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.card + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `digit`: "Type the next digit."
- how `remainder`: "Type the remainder."
- how `guess`: "Tap Ends or Repeats first."
- how `reason`: "Drag blocks to build the reason."
- how `sort`: "Drag the denominator to Ends or Repeats."
- event, whole, only so many.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: step-by-step long division with integer remainders, the remainder loop, repeat detection, the reason builder. The division and repeat detector sit in a marked block `/* REMAINDER ENGINE: begin */ ... /* end */` so square-root-hunt can reuse it for its repeating-decimal part.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Steps | Type digits from a calculator | Each remainder is typed and checked too. |
| Ends or repeats | Guess | Guesses are logged, and the loop shows the answer step by step. |
| Reason | Pick blocks at random | The reason is checked against its parts and applied to 1/97. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `digit`; `remainder`.
2. `guess`.
3. `reason`; `sort`.
4. Only so many (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.NS.2d | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The pigeonhole argument: finitely many remainders force ending or repeating | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 The Number System" | Niven (1961), "Numbers: Rational and Irrational", Mathematical Association of America | yes |
| A fraction in lowest terms ends exactly when its denominator has no prime factors but 2 and 5 | Niven (1961), "Numbers: Rational and Irrational", Mathematical Association of America | Hardy and Wright, "An Introduction to the Theory of Numbers", chapter 9 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s20, 2026-11-10): 1/7 gives remainders 1, 3, 2, 6, 4, 5 and digits 142857, then remainder 1 again; 1/8 gives 125 and remainder 0; 5/12 gives 416 with remainder 8 repeating; 3/11 gives 27 with remainder 3 repeating; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 division, loop and decimal; at 680x425 loop as a tab.
2. Twelve fractions are divided step by step with each remainder placed. (7.NS.2d)
3. Each decimal is marked ends or repeats with its repeat. (7.NS.2d)
4. The reason is built and applied, and denominators are sorted then checked. (7.NS.2d)
5. The REMAINDER ENGINE block is marked for reuse.
6. `Read` reads every card and step; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: arrows appear at once; no network requests.

## Open questions
None.
