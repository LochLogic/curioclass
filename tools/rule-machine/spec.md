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
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the machine, Cog and the tapes stay. Before, the tape printed every term, reasons were only built from cards, and mystery tapes could be tuned by watching the child's tape print beside Cog's. Now the machine prints three terms and the child types the next five; after the cards the child writes the reason in their own words beside a guide; a wrong card build costs the tape; and on mystery tapes the child types the start, the rule and the next two terms before anything prints. Cog works one tape first. The Content list now names every tape.
- Eight number tapes, four shape tapes, six mystery tapes, the prediction menu, reason cards. Extra: Tape for a friend (the child makes a tape with a hidden start and rule and passes the device). tool.json `modes: ["Workshop", "Tape for a friend"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.
- Change note (hooks, 2026-11-11): Added the three hooks: two tapes on your own with the end screen by part, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. The words rule, pattern, term, odd, even and feature each show on Cog's tape the first time they are used. The reason line offers a frame the child may take or leave: "It will keep going because __."

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.OA.5 (generate) | generate a number or shape pattern that follows a given rule | the student | Set Start and Rule, read three printed terms, type the next five; build the next two shapes and type the 10th shape's tile count | 8 number tapes and 4 shape tapes | the child's typed terms on the tape; tiles the child placed | 2 |
| 4.OA.5 (features) | identify features of the pattern that the rule did not state | the student | Predict the feature before the tape is finished, then mark it on the tape | 12 | Cog's highlights only after the child's marks | 3 |
| 4.OA.5 (explain) | explain informally why the feature will continue | the student | Build the reason from cards, then write it in your own words and check it against the guide | 8 | the reason card and the child's own line | 4 |

## Screens and modes
Header (kit): title "Rule Machine"; `Workshop`, `Tape for a friend`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A workshop bench, the ticker-tape machine with Start and Rule dials, a lever and Cog. The welcome is queued (`welcomeAfter: true`): "Start at 1. Rule: add 3. Before you pull the lever, guess: will the numbers be odd, even or both? Tap a guess." First hint: "Tap a guess."

**Cog goes first (the model).** Cog runs one tape alone: start 2, add 2. Cog guesses "all even", prints three terms, writes the next five by hand, marks the feature and says why: "Even plus 2 is even, so it can never turn odd." It cannot be skipped and `Cog's tape` reopens it.

**Number tapes (focus: the tape).** At 1366x768 the machine fills the left with the tape running across the bottom and the reason cards right; at 680x425 the cards are a sheet. The child predicts, pulls the lever, and the machine prints three terms and stops. The child types terms 4 to 8 into empty boxes on the tape; each is checked when all five are in, and a wrong box is marked once. Then the last four print. The child marks the feature on the tape (taps every odd term, or the repeating ones digits, or types the term number where 100 lands), and only then does Cog highlight it. Eight tapes, each with a feature to predict: odd and even (add 3 from 1), all even (add 4 from 2), will 100 appear (add 3 from 1: yes, as term 34; add 4 from 2: no, it jumps from 98 to 102), ones digits that repeat (add 5 from 3: 3, 8, 3, 8).

**Reasons.** For each, the child drags cards to build why: "odd + 3 is even", "even + 3 is odd", "adding 4 to an even number keeps it even", "every term is 2 more than a number in the 4s count, and 100 is in the 4s count, so 100 is skipped". The cards are short and true; wrong cards are there too, six cards in all for each tape with two needed. A wrong build is shown false on the tape with one counterexample; a second wrong build ends the tape and the same feature returns later with a new start. After a right build the child writes the reason in a one-line box, "Why will it keep going?", beside Cog's model line and a three-box guide: says what the rule adds; says what that does to odd or even, or to the ones digit; says why it can never change. The tool cannot mark the words, so the guide and the model do that job, and the line prints with the tape.

**Shape tapes.** A rule grows a tile shape (start with 3 tiles, add 2 each step). The machine builds three shapes; the child builds the next two by placing tiles, types the tile count of the 10th shape in a number box (21), and answers the feature question by typing or tapping (will any shape have an even number of tiles? no).

**Mystery tapes.** Cog prints 5, 9, 13, 17 with dials covered and the lever locked. The child types the start, the rule (a sign and a number) and the next two terms (21, 25) in boxes. Only then does the machine print the child's tape under Cog's. Two tries; after the second miss Cog uncovers the dials and a new mystery tape takes its place.

**Hidden features (the aha).** Cog: "My rule said add 3. It never said odd, even, odd, even. That came from where we started." The child tries start 2, add 3 and sees the turn-taking start with even.

**The end.** The tapes with features and reasons. `Print` prints them.

**Tape for a friend (extra).** Hide a start and rule; pass the device.
**On your own.** Four items with Cog quiet: no highlights, no reason cards, no hints (two tapes, each with a generate part and a feature part), one answer each. Nothing is marked until all are in.

**Results strip (on the end screen).** For the teacher: for each part of 4.OA.5 (generate; find a feature and explain it), how many of its items on your own were right, in numbers and words, with each item missed and the answer the child gave. It prints with the rest.

## Content
- All readable with `Read`. Each tape prints 12 terms.
- Number tapes (start, rule, feature): (1) 1, add 3: odd and even take turns. (2) 2, add 4: all even. (3) 1, add 3: will 100 appear? Yes, as term 34. (4) 2, add 4: will 100 appear? No, it jumps from 98 to 102. (5) 3, add 5: ones digits go 3, 8, 3, 8. (6) 5, add 10: the ones digit is always 5. (7) 1, multiply by 2: every term after the first is even. (8) 4, add 6: all even, and the ones digits repeat every five terms (4, 0, 6, 2, 8).
- Shape tapes (start, rule, 10th shape, feature): 3 tiles, add 2: 21, never even. 1 tile, add 3: 28, odd and even take turns. 4 tiles, add 4: 40, always a multiple of 4. 2 tiles, add 5: 47, ones digits go 2, 7.
- Mystery tapes (shown terms; start and rule; next two): 5, 9, 13, 17 (5, add 4; 21, 25). 2, 9, 16, 23 (2, add 7; 30, 37). 10, 13, 16, 19 (10, add 3; 22, 25). 3, 6, 12, 24 (3, multiply by 2; 48, 96). 0, 8, 16, 24 (0, add 8; 32, 40). 7, 12, 17, 22 (7, add 5; 27, 32).
- Prediction menu for each tape: four choices that fit the question (for odd and even: all odd, all even, take turns, no pattern).
- On your own, with what each common wrong answer means:
  - Generate: "Start at 4. Add 7." After 4, 11, 18 type the next five (25, 32, 39, 46, 53). "Start at 3. Add 6." After 3, 9, 15 type the next five (21, 27, 33, 39, 45). One wrong term with the rest following from it means a counting slip; terms that go up by a different amount mean the rule was not held.
  - Feature and why: on the first tape, "What do you notice that the rule did not say? Will it keep going? Why?" (Even and odd take turns, because adding an odd number flips even to odd and back.) On the second, every term is odd, and every term is a multiple of 3 (an odd start plus an even number stays odd; a multiple of 3 plus 6 is still a multiple of 3). "They are all odd" on the first tape means the child looked at only some terms; a reason that only repeats the rule means the feature is seen but not yet explained.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Dials turn by one; the lever prints at once if Motion is off.
- Keyboard: Tab to dials, the prediction menu, the lever, reason cards and the tape; arrows turn a dial; Enter pulls the lever.
- With Motion off the tape appears printed in full.
- Access: every action works by tap and by keyboard. Dials turn by tap or arrow key; tiles and reason cards can be dragged, or picked with a tap and placed with a tap. The child's marks on the tape are rings and the words odd or even, never color alone. Motion can be paused.
- On your own: one answer each, no feedback until the fourth is in.

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
- how `terms`: "Type the next five numbers on the tape."
- how `mark`: "Tap the numbers that show the pattern."
- how `reason`: "Drag two cards to build the reason."
- how `words`: "Now say why in your own words."
- how `mystery`: "Type the start, the rule and the next two numbers."
- event, whole, Cog's tape.
- event, whole, hidden features.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.
- how `own`: "Four more on your own. No hints this time."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None for this tool (the catalog lists family "function-machine"). This tool doesn't use the function-machine engine described in undo-machine's spec, since a start-and-rule sequence is not an input-output machine. Tool-only code: the sequence printer, feature tests (parity, a target value, repeating last digits), shape growth.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Terms | Wait for the tape to print | The machine stops after three terms; the child types five. |
| Predictions | Always pick the same choice | Four choices, and the right one changes from tape to tape; only predictions made before the stop count. A wrong prediction is not a fail, it is what the tape then tests. |
| Feature marks | Tap every term | Marks are checked as a set; extra taps fail it. |
| Reasons | Try card pairs until one sticks | Six cards make fifteen pairs; the second wrong build ends the tape and brings a new start. |
| Own words | Tick the boxes on an empty line | The ticks open only when the line has words; the line prints. |
| Mystery | Tune the dials against Cog's tape | The dials are covered and nothing prints until start, rule and two next terms are typed; two tries, then a new tape. |
| Shapes | Count tiles on a drawn 10th shape | Only five shapes are ever drawn; the 10th is typed. |
| On your own | Retry until right; lean on the hints | One answer each, no hints or models, and nothing is marked until all are in. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: Cog's tape (whole), then `welcome` (queued). `predict`; `lever`; `terms`; `mark`.
2. `reason`; `words`.
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
Checks run again for the spec fix (Python, scratchpad s/fx, 2026-11-10): all eight number tapes generated to 12 terms and each stated feature tested on them (and to 40 terms for the 100 questions); 10th shapes 21, 28, 40 and 47 and their features; the six mystery tapes' next two terms; six cards give 15 pairs.
Checks run for the items on your own (Python, 2026-11-11): 4 + 7 steps: 25, 32, 39, 46, 53; 3 + 6 steps: 21, 27, 33, 39, 45, all odd and all multiples of 3.

## Done when
1. Focus and fold: at 1366x768 machine, tape and cards; at 680x425 cards as a sheet.
2. Eight number tapes and four shape tapes: the child types terms 4 to 8 or builds the next two shapes, and types the 10th shape's count. (4.OA.5)
3. A hidden feature is predicted before each tape is finished and then marked on the tape by the child. (4.OA.5)
4. Eight reasons are built from cards and then written in the child's own words against the guide; six mystery tapes are cracked by typing start, rule and two terms before any print. (4.OA.5)
5. Cog's tape plays first and can be reopened.
6. `Read` reads every card; every control is 48 px or more.
7. The tool does not ask for in-out rules (that stays in function-machine-factory).
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: tapes print in full at once; no network requests.
10. Four items on your own run with no model or hint, one answer each; the end screen shows the result by code and the items missed. (4.OA.5)
11. Every spoken instruction is also on screen, and each key word shows with a picture or example at first use.
12. Every action works by keyboard as well as tap, drags have a tap way, nothing is shown by color alone, and motion can be paused.

## Open questions
- The idea card changes the mechanic and flags overlap with the function-machine family (default used: start-and-rule patterns with predicted hidden features; in-out rule guessing stays with function-machine-factory; this tool does not use the function-machine engine).
