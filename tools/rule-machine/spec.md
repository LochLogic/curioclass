# Rule Machine

## One idea
In a cozy workshop stands a ticker-tape machine with two dials, Start and Rule, and a small robot helper named Cog, and the child sets a start and a rule ("Start at 1, add 3"), then, before pulling the lever, predicts a feature the rule never mentions from a short menu (will the numbers be odd, even or both? will 100 appear?), and the tape prints 1, 4, 7, 10, 13 while Cog highlights the feature (odd, even, odd, even) and asks why; the child builds a reason from cards ("odd + 3 is even, and even + 3 is odd"); a second machine grows shape patterns from a rule ("start with 3 tiles, add a row of 2") and the child predicts the 10th shape (21 tiles) before it prints; mystery tapes from Cog hide the start and rule, and the child finds both; at the end the child sees that the rule says "add 3" but never says "take turns odd and even", because that feature comes from the start and the rule together, so a fourth grader learns to generate number and shape patterns that follow a given rule and to identify and explain features of the pattern that the rule does not state.

## Not like
- function-machine-factory (8, concept): input-output functions. Here patterns from a start and a rule.
- pattern-painter (3, spec): patterns in the times table. Here patterns a rule makes.
- two-rule-race (5, concept): two patterns on a grid. Here one pattern and its hidden features.
- growth-spurt (4, spec): comparing two amounts. Here sequences.

## Who and how
- Grade 4, Math, module "Number Patterns". Standards: 4.OA.5 (generate a number or shape pattern that follows a given rule; identify apparent features of the pattern that were not explicit in the rule itself; for example, given the rule "Add 3" and the starting number 1, generate terms in the resulting sequence and observe that the terms appear to alternate between odd and even numbers; explain informally why the numbers will continue to alternate in this way).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight number tapes, four shape tapes, six mystery tapes, the prediction menu, reason cards. Extra: Tape for a friend (the child makes a tape with a hidden start and rule and passes the device). tool.json `modes: ["Workshop", "Tape for a friend"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.OA.5 (generate) | Set Start and Rule and pull the lever; predict the 10th shape | the tape printing; tiles growing | 2 |
| 4.OA.5 (features) | Predict a hidden feature before printing | Cog's highlights on the tape | 3 |
| 4.OA.5 (explain) | Build a reason from cards; crack mystery tapes | the reason card; the found rule | 4 |

## Screens and modes
Header (kit): title "Rule Machine"; `Workshop`, `Tape for a friend`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A workshop bench, the ticker-tape machine with Start and Rule dials, a lever and Cog. The welcome is queued (`welcomeAfter: true`): "Start at 1. Rule: add 3. Before you pull the lever, guess: will the numbers be odd, even or both? Tap a guess." First hint: "Tap a guess."

**Number tapes (focus: the tape).** At 1366x768 the machine fills the left with the tape running across the bottom and the reason cards right; at 680x425 the cards are a sheet. The tape prints 12 terms. Cog highlights the feature that was predicted. Eight tapes, each with a feature to predict: odd and even (add 3 from 1), all even (add 4 from 2), will 100 appear (add 3 from 1: yes, as term 34; add 4 from 2: no, it jumps from 98 to 102), ones digits that repeat (add 5 from 3: 3, 8, 3, 8).

**Reasons.** For each, the child drags cards to build why: "odd + 3 is even", "even + 3 is odd", "adding 4 to an even number keeps it even", "every term is 2 more than a number in the 4s count, and 100 is in the 4s count, so 100 is skipped". The cards are short and true; wrong cards are there too.

**Shape tapes.** A rule grows a tile shape (start with 3 tiles, add 2 each step). The child predicts the 10th shape (21 tiles) and says whether any shape will have an even number of tiles.

**Mystery tapes.** Cog prints 5, 9, 13, 17 with dials covered; the child sets the dials to match.

**Hidden features (the aha).** Cog: "My rule said add 3. It never said odd, even, odd, even. That came from where we started." The child tries start 2, add 3 and sees the turn-taking start with even.

**The end.** The tapes with features and reasons. `Print` prints them.

**Tape for a friend (extra).** Hide a start and rule; pass the device.

## Content
- Rules of add 2 to add 9 and multiply by 2 for two tapes, starts from 0 to 10, four shape rules, six mystery tapes, all readable with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Dials turn by one; the lever prints at once if Motion is off.
- Keyboard: Tab to dials, the prediction menu, the lever, reason cards and the tape; arrows turn a dial; Enter pulls the lever.
- With Motion off the tape appears printed in full.

## Look
- Accent `--brand` #8a4a1c workshop copper (header, the machine, buttons); gold #f4c542 (the highlighted feature, the card in hand); paper #fbf3ec; ink #2a1608; muted #5e554d.
- Contrast (WCAG 2.1, computed): white on brand 6.82:1; brand on paper 6.22:1; ink on paper 15.73:1; muted on paper 6.64:1; ink on gold 10.61:1.
- Never color alone: highlighted terms carry a mark and a word (odd, even).
- Different from this batch (greenhouse green, stadium blue, test-kitchen pink, sieve purple).

## Art
- Local FLUX (`scripts/localart.py`): the workshop (1, 16:9), the machine (1, 4:3), Cog in three poses (3, 1:1).
- Drawn in code: the tape, dials, tiles and cards.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as Cog; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.tape + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `predict`: "Tap a guess before you pull the lever."
- how `lever`: "Pull the lever."
- how `reason`: "Drag cards to build the reason."
- how `mystery`: "Turn the dials to match the tape."
- event, whole, hidden features.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None for this tool (the catalog lists family "function-machine"). This tool doesn't use the function-machine engine described in undo-machine's spec, since a start-and-rule sequence is not an input-output machine. Tool-only code: the sequence printer, feature tests (parity, a target value, repeating last digits), shape growth.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Predictions | Always guess "both" | The score counts only predictions made before printing, and some tapes are all even. |
| Reasons | Drag any cards | Cards are checked against the tape's start and rule. |
| Mystery | Turn dials at random | The machine prints the child's tape beside Cog's so the difference shows. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `predict`; `lever`.
2. `reason`.
3. `mystery`.
4. Hidden features (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.OA.5 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Grade 4 patterns are about features a rule implies, not finding a function rule | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 3 to 5 algebra | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad s14, 2026-11-10): start 1, add 3 alternates odd and even and reaches 100 as term 34; start 2, add 4 stays even and skips from 98 to 102; 3 tiles plus 2 each step gives 21 tiles at the 10th shape; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 machine, tape and cards; at 680x425 cards as a sheet.
2. Eight number tapes and four shape tapes are generated from a rule. (4.OA.5)
3. A hidden feature is predicted before each print. (4.OA.5)
4. Reasons are built and six mystery tapes are cracked. (4.OA.5)
5. `Read` reads every card; every control is 48 px or more.
6. The tool does not ask for in-out rules (that stays in function-machine-factory).
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: tapes print in full at once; no network requests.

## Open questions
- The idea card changes the mechanic and flags overlap with the function-machine family (default used: start-and-rule patterns with predicted hidden features; in-out rule guessing stays with function-machine-factory; this tool does not use the function-machine engine).
