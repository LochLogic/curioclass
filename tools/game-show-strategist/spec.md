# Game Show Strategist

## One idea
Every game show decision is a bet with a computable value. You play four made-up shows by gut, then go to the Strategy
lab where your strategy plays 10,000 games and its running average settles onto an exact expected value, then open
Why and see that number come out of a tree or a table. The twist that sticks: change the host's rule and the best
strategy changes too.

## Not like
- carnival-odds (gr 7, probability family): long-run frequency of simple chance games. Here decisions with stakes, expected value as the score, conditional probability and the binomial and geometric models.
- medical-test-paradox (gr 10, probability family): conditional probability in a screening test, with icons. Here conditional probability in a host's rule, and expected value of strategies.
- courtroom-statistics and fair-dice-investigation (gr 12, same group): inference from data. Here no data to judge: the models are known and the question is what to do.
- sample-machine (gr 12, same group): simulates statistics of samples. Here simulates strategies.

## Who and how
- Grade 12, Statistics, Math: statistics. Students drive, alone or in pairs; a teacher can project the Three Doors. 20 to 40 minutes.
- Topic line: "probability, expected value and strategy".
- Standards (module): AP-STAT.U4; S-CP.A; S-MD.A; S-MD.B.
- CCSS clusters: Three Doors and Why trees serve S-CP.A (A.2 independence, A.3 and A.5 conditional probability).
  Push Your Luck and Lucky Guess serve S-MD.A (A.1 to A.4: random variables, their distributions and expected values).
  Briefcases and the Strategy lab serve S-MD.B (B.5 to B.7: weigh strategies by expected value and analyze decisions).
- AP-STAT.U4 (Probability, Random Variables, and Probability Distributions): conditional probability, expected value
  and spread of a random variable, the binomial (Lucky Guess) and geometric (Push Your Luck) models.
- tool.json: driver "students or teacher", minutes "20-40", modes ["Play", "Strategy lab", "Why"], grades_label "Grade 12".

## Screens and modes
Header: title, subtitle "What's it worth, on average?" Modes `Play` (opens first), `Strategy lab`, `Why`. Show picker:
four show cards (`Three Doors`, `Briefcases`, `Push Your Luck`, `Lucky Guess`), each with a thumbnail cut from that
show's art. Kit buttons.
Stage: the studio (art: studio-stage) with the current show's set on it. Panel: the decision buttons, then a running
tally of your own winnings and play count.
Sets (all painted cutouts placed in code over the studio; numbers, amounts and words on them are drawn in code):
- Three Doors: three door-closed cutouts (ten, smaller, on Ten doors) with the door number on the blank panel. An
  opened door swaps to door-open with the prize cutout (prize-car or prize-goat) inside.
- Briefcases: ten briefcase-closed cutouts in two rows of five with the case number on the blank tag; an opened case
  swaps to briefcase-open with its dollar amount on the blank card. Your kept case sits apart on a spotlit spot. A
  board of the ten amounts (code) greys each one out as it is revealed. The banker-phone cutout rings (a small shake)
  when an offer comes; the offer is in code beside it.
- Push Your Luck: the wheel's six equal sectors are drawn in code (exact wedges, "$100" on five and "Bust" on one)
  inside the wheel-rim cutout, with a pointer in code at the top. The bank so far shows under it.
- Lucky Guess: the quiz-podium cutout with the question and the four choices on its blank screen in code.

### Play
Focus: the set, center stage and largest (doors, the case wall, the wheel or the podium); the panel holds only the
decision buttons and the tally. One game at a time, the real decisions, no hints. Buttons per show:
- Three Doors: tap a door (or `Door 1` to `Door 3` buttons), then `Stick` or `Switch`; `Next game`. Host rule picker
  in the panel: `Classic`, `Random host`, `Ten doors`, `Devious host`.
- Briefcases: tap a case to keep, then tap cases to open (the count left this round is shown); at each offer `Deal`
  or `No deal`; `Next game`.
- Push Your Luck: `Spin` and `Stop`; `Next game`.
- Lucky Guess: round picker `Plain`, `Penalty`, `Scenario` (Content); per question `A` to `D` and, in Penalty and
  Scenario, `Skip`; `Next game` after question 10.
After each game: what you won and your average so far. A small line "Exact expected value of what you just did"
appears only after 10 games (so the student gets a gut feel first).

### Strategy lab
Focus: the running-average chart, center stage and largest; the winnings bars under it; the strategy list and the
readouts in the panel; the set shrinks to its show card.
Pick up to 3 strategies for the current show (from a list, with settings such as a threshold). `Play 10,000 games`
runs them on the same random stream; a running-average chart draws each line settling toward its exact EV (dashed);
bars show the distribution of winnings (theory as outlines, simulation as fill). Readouts per strategy: average, exact
EV, SD of winnings, median, chance of $100 or less.

### Why
Focus: the tree or table for the current show, center stage and largest.
The exact math for the current show: a probability tree (Three Doors, any variant), a table of paths (Briefcases), an
EV table by stopping point (Push Your Luck), the binomial table and EV per guess (Lucky Guess). Every node and cell is
an exact fraction where it can be, then a decimal.

## Content
All shows are made up; no real show names, hosts or logos.
1. Three Doors (a car behind one door, goats behind two). Host rule variants (picker in the panel):
   - Classic: host knows, always opens a goat door you didn't pick, always offers a switch. Stick 1/3, switch 2/3.
   - Random host: host opens one of the other two at random; a third of rounds the car is shown (round spoiled). Given
     a goat was shown: stick 1/2, switch 1/2.
   - Ten doors: host opens 8 goat doors. Stick 1/10, switch 9/10.
   - Devious host: host offers a switch only if you picked the car. Always switch wins 0; always stick 1/3.
2. Briefcases: 10 cases holding $1, $5, $10, $50, $100, $500, $1,000, $5,000, $10,000, $50,000 (mean $6,666.60). You
   keep one; open 3, 2, 2, then 1 other cases; after each round the banker offers 40%, 60%, 80%, 90% of the mean of
   the unopened cases (yours included), rounded half up to the dollar. 151,200 equally likely paths (your case, then
   which cases open in each round), so every strategy's EV is exact by enumeration.
   - Never deal: EV $6,666.60, median $300, P(≤ $100) 0.5, P(≥ $5,000) 0.3.
   - Deal at offer 1: $2,666.60. Offer 2: $4,000.00. Offer 3: $5,333.23. Offer 4: $6,000.00.
   - Take the first offer of at least $1,000: $2,803.91; $2,000: $2,909.07; $3,000: $3,034.79; $5,000: $4,359.92;
     $10,000: $5,592.49.
   - The lesson: never dealing has the highest EV, and also a 50% chance of $100 or less. Why shows both, and the
     student writes which they'd pick and why (risk is a real reason; EV is not the only one).
3. Push Your Luck: a wheel with six equal sectors, one is Bust. Each safe spin adds $100; stop any time and keep it;
   Bust loses it all. EV of planning to stop after k spins = 100k(5/6)^k: k = 1 to 10: 83.33, 138.89, 173.61, 192.90,
   200.94, 200.94, 195.36, 186.05, 174.43, 161.51. Best: stop at $500 or $600 (tie). Spins until bust: geometric with
   p = 1/6, mean 6.
4. Lucky Guess: a 10-question quiz, 4 choices each, on topics you can't know (made-up trivia about a made-up town).
   - Plain round, pure guessing: correct count is binomial(10, 1/4): P(0..8) 0.0563, 0.1877, 0.2816, 0.2503, 0.1460,
     0.0584, 0.0162, 0.0031, 0.0004; P(≥ 5) 0.0781; P(≥ 6) 0.0197; mean 2.5; SD 1.369.
   - Penalty round (+1 right, -1/3 wrong, 0 skip): EV of a guess with 4, 3, 2, 1 choices left = 0, 1/9, 1/3, 1.
   - Scenario round: you know 4 answers; on 2 questions you can rule out 2 choices, on 2 you can rule out 1, on 2 you
     know nothing (the ruled-out choices are greyed on the podium). Guess on everything: EV 4 + 2(1/3) + 2(1/9) = 4.889.
     Skip every unknown: 4.

## Interactions in detail
- All randomness from the engine's seeded `Rand` (`?seed=n` for tests); the Strategy lab runs strategies on the same
  stream so differences are not luck of the stream.
- Exact values: fractions for Doors and Lucky Guess; Briefcases EVs by enumerating the 151,200 paths once on opening
  Why or the lab (in batches with a progress bar, under a second), not hard-coded; Push Your Luck from the formula.
- Random host in the lab: spoiled rounds (the car shown) are counted and reported ("spoiled: 3,342 of 10,000") but left
  out of the averages, so the lines settle on the given-a-goat values 1/2 and 1/2. Devious host: when no switch is
  offered, the player keeps the first pick.
- Running average plotted every 100 games; dashed line at the exact EV; the readout shows simulation minus exact.
- Short animations never block: a door opens in 0.5 s, a case in 0.4 s, a spin lands in at most 1.5 s, the phone
  shakes for 0.6 s. Each result is decided when the button is pressed; any tap during an animation (another door,
  `Stop`, `Deal`, `Next game`, a show card) finishes it at once and then acts. With Motion off there are no animations.
- `Play 10,000 games` computes at once and draws the lines and bars over 2 s; changing a strategy, its setting, the
  host rule or the show during the draw cancels it and shows the new state at once.
- Play history and the best average per show saved on device (localStorage `curio-gss-play`, try/catch) with `Clear`.
- Keyboard: doors 1 to 3 (or 0 to 9 on Ten doors), D for Deal and N for No deal, Space to spin, S to stop, A to D and K
  (Skip) on the quiz.
- `window.__tool = {state, setMode, seed(n), show(k), variant(v), play(choice), lab(strategies, n), exact(strategy)}`.

## Look
Dark studio: stage paper `#120c24` (deep violet, the studio art is dimmed toward it), panels from kit/theme-912.css.
Accent `--brand #39ff6e` (jackpot green: running lines, the Deal button, winning door outline), `--brand-ink #10161f`.
Other strategy series `#ffb3f0` and `#7cc8ff`, each line also dashed or dotted differently. Numbers on doors, tags and
cards are #10161f on the blank cream or white surfaces of the art (15.8:1 on #f4efe2); prizes also show as text.
Contrast (computed): brand on panel 12.94:1, on sections 12.26:1, on the studio 14.23:1; brand-ink on brand 13.58:1;
`#ffb3f0` on panel 10.68:1; `#7cc8ff` on panel 9.53:1. Minimal celebration: a win shows the amount, no confetti, no sirens.

## Art
Local FLUX (`scripts/localart.py`), no people (the host and the banker are never shown: the doors open by themselves
and the banker is a ringing phone). One style: glossy, brightly lit painted illustration of a TV studio, purple and
gold.
- studio-stage: "An empty television game show stage with a glossy deep purple floor, curved arches lined with round
  warm bulb lights, soft spotlights from above, painted illustration"; 16:9; cutout no; people no; the stage background
  in every mode, dimmed under the charts and tables.
- door-closed: "A tall closed stage door painted deep red, set in a carved gold frame, with a round brass knob and a
  smooth blank cream panel in the upper middle, front view, painted illustration, plain white background"; 9:16;
  cutout yes; people no; the Three Doors set (3 or 10), the number written in code on the cream panel.
- door-open: "A tall carved gold door frame with a deep red door swung open inward, a softly lit empty alcove with a
  purple floor behind it, front view, painted illustration, plain white background"; 9:16; cutout yes; people no; an
  opened door, with the prize cutout placed inside.
- prize-car: "A shiny compact car painted bright green, three-quarter front view, studio lighting, painted
  illustration, plain white background"; 4:3; cutout yes; people no; the prize behind a winning door.
- prize-goat: "A friendly white goat with small curved horns standing and looking at the viewer, studio lighting,
  painted illustration, plain white background"; 1:1; cutout yes; people no; behind every other door.
- briefcase-closed: "A silver aluminum briefcase standing upright, front view, with a plain blank cream tag hanging
  from the handle, studio lighting, painted illustration, plain white background"; 4:3; cutout yes; people no; the ten
  cases, numbers in code on the tag.
- briefcase-open: "An open silver aluminum briefcase seen from the front with its lid up and a blank cream card
  standing inside, studio lighting, painted illustration, plain white background"; 4:3; cutout yes; people no; an
  opened case, the dollar amount in code on the card.
- banker-phone: "An old-fashioned glossy black desk telephone with a coiled cord on a small round wooden side table,
  warm spotlight, painted illustration, plain white background"; 1:1; cutout yes; people no; the banker's offers.
- wheel-rim: "A polished brass ring with round warm bulb lights evenly spaced around it and an empty open center, front
  view, painted illustration, plain white background"; 1:1; cutout yes; people no; the frame of the Push Your Luck
  wheel; it turns with the sectors drawn in code inside it.
- quiz-podium: "A game show contestant podium with a glossy royal blue front and gold trim, a blank dark screen on its
  slanted top, front view, studio lighting, painted illustration, plain white background"; 3:4; cutout yes; people no;
  the Lucky Guess set, the question and choices drawn in code on the screen.
Wheel sectors, the amounts board, charts, bars, trees, tables and preview.svg are drawn in code: they are diagrams,
charts and labels, and the sectors must be exact.

## Voice
Bank voice `lively-host` (Sadachbia), style "Say with lively energy, like a friendly game show host who is quietly
rooting for you." Changed from hero-coach, which identity-proof-race (same group, batch R05) also used. Every bank
voice is already used by some math 9-12 neighbor; lively-host's only one is work-rate-crew (gr 11, a painting-company
dispatcher). `Curio.voice`, `scope: () => state.mode + ':' + state.show`. Readouts and tables are read on screen;
Read speaks the hint.
- wPlay (how, Play welcome; stale on the first decision): "Pick a show card. Play a few rounds on gut feel first, then we'll check the math."
- doors (how, first Three Doors game; stale once a door is picked): "Tap a door. When another one opens, press Stick or Switch."
- cases (how, first Briefcases game; stale once a case is kept): "Tap a case to keep. Then open cases, and when the phone rings, press Deal or No deal."
- wheel (how, first Push Your Luck game; stale on the first spin): "Press Spin to add a hundred dollars, or Stop to keep what you have."
- quiz (how, first Lucky Guess game; stale on the first answer): "Tap A, B, C or D. In the penalty rounds you can press Skip instead."
- tenGames (event, 10th game of a show; stale on a show change): "Ten games in. Now look at the exact value of what you did."
- wLab (how, Strategy lab welcome; stale once a run starts): "Choose up to three strategies, then press Play 10,000 games. Watch the lines settle."
- devious (event, Devious host chosen; stale on a variant change): "New host, new rules. Play a few rounds and see if switching still pays."
- briefcase (event, first Never deal result in the lab; stale on a show change): "Highest average, and half the time a hundred dollars or less. Your call."
- wWhy (how, Why welcome; stale on a show change): "Here's where the numbers come from. Read each branch left to right and multiply along the way."

## Family engine
probability (`kit/probability.js`), as described in full in tools/medical-test-paradox/spec.md; this tool matches
that API and adds nothing that breaks it.
- Uses: `Rand(seed)` (mulberry32; `.next()`, `.int(a, b)`, `.pick`, `.shuffle`, `.bern(p)`), `Frac` for exact
  probabilities (2/3, 9/10, 1/9), `Trials(fn, n, {rand, batch: 500, onBatch})` for the Strategy lab, `Tally` for
  wins per strategy, `Converge` for the running averages, `Tree` for the Why trees.
- Kept in this tool, as the family page says (expected value stays here): EV tables, the Briefcases enumeration,
  the binomial and geometric tables, the winnings bars.
- Asks the engine for two additions (into the engine and its description in the same change, existing calls kept
  working): (1) `Tree` branches given as functions of the path so far, so the host's choice can depend on the
  player's pick, plus `tree.given(event, condition)` returning a `Frac` (for "given a goat was shown"); (2)
  `Converge` with up to 3 series and a `mode: 'mean'` option, so it can draw running mean winnings, not only
  running relative frequency.
- The sampling engine's `rng` is the same mulberry32, so a seed means the same stream in both families.

## Sources
- S-CP.A, S-MD.A, S-MD.B: Common Core State Standards for Mathematics, Conditional Probability and Using Probability to Make Decisions, https://www.thecorestandards.org/Math/Content/HSS/CP/ and https://www.thecorestandards.org/Math/Content/HSS/MD/
- AP-STAT.U4: College Board, AP Statistics Course and Exam Description, https://apcentral.collegeboard.org/courses/ap-statistics
- Conditional probability, expected value, binomial and geometric distributions: OpenStax, Introductory Statistics 2e, chapters 3 and 4, https://openstax.org/books/introductory-statistics-2e/pages/4-introduction
- The three doors problem and how the host's rule changes the answer: OpenIntro Statistics 4e, chapter 3 "Probability", https://www.openintro.org/book/os/
- mulberry32: a public-domain 32-bit PRNG (Tommy Ettinger), the same function used in the sampling engine (poll-workshop).
- All shows are made up.
- Checks run (Python, exact fractions, 2026-10-29): Briefcases enumerated over all 151,200 paths with offers rounded
  half up: never deal 6,666.60, median 300, P(≤ $100) 0.5, P(≥ $5,000) 0.3; deal at offers 1 to 4: 2,666.60,
  4,000.00, 5,333.23, 6,000.00; first offer of at least $1,000, $2,000, $3,000, $5,000, $10,000: 2,803.91, 2,909.07,
  3,034.79, 4,359.92, 5,592.49 (all match). Worst cases: the lowest offer ever made is $95 at offer 1 and $3 at offer
  4; the chance of $100 or less is 0.008 dealing at offer 1 and 0.222 at offer 4. Random host by exact enumeration:
  spoiled 1/3, given a goat stick 1/2 and switch 1/2. Push Your Luck 100k(5/6)^k for k = 1 to 10 matches the list, with
  k = 5 and 6 tied at 200.94. Binomial(10, 1/4) table, P(≥ 5) 0.0781, P(≥ 6) 0.0197, SD 1.369 match; penalty EVs 0,
  1/9, 1/3, 1; scenario 44/9 = 4.889. Lab band in Done when 2: the spread of a 10,000-game switch rate is 0.0047, so
  ±0.02 is over four spreads wide.

## Done when
1. Three Doors Why tree: classic switch 2/3; random host given a goat shown 1/2; ten doors 9/10; devious host switch 0.
2. Strategy lab, 10,000 classic games with always switch: average win rate within 0.02 of 2/3; with Random host the
   spoiled rounds are reported and left out, and both lines settle near 1/2.
3. Briefcases exact EVs: never deal 6,666.60; deal at offer 3 5,333.23; first offer at least $3,000 gives 3,034.79.
4. Push Your Luck EV table matches the Content list; stopping at 5 and 6 tie at 200.94.
5. Lucky Guess table: P(≥ 5) 0.0781; scenario EVs 4.889 and 4.
6. Focus: at 1366x768 and 1000x625 the set (Play), the running-average chart (Strategy lab) and the tree or table
   (Why) are each the largest thing on the stage.
7. Tap while it plays: during a door opening, a wheel spin or the 2 s lab draw, `Stop`, `Next game`, a strategy change
   or a show card acts at once, and the results stay exact.
8. Same seed, same results; `Clear` empties saved play.
9. How-to lines spoken once each in five actions; "Ten games in" and the devious line each time their event happens;
   no line names a control that is not on screen.
10. Every size in STANDARDS.md keeps the set and the decision buttons visible without page scrolling; keyboard only
    works; ten painted images, no people; console clean, no network.

## Open questions
- [game-show-strategist] This tool asks the probability engine (defined in medical-test-paradox's spec) for path-dependent `Tree` branches with `given()`, and multi-series running means in `Converge`. OK to add them to the family?
- [game-show-strategist] Briefcases is modeled on a well-known TV format, with no name, logo or catchphrase. OK?
- [game-show-strategist] Voice moved to lively-host (identity-proof-race keeps hero-coach); it still shares lively-host with work-rate-crew (gr 11), because every bank voice suited to grade 12 is taken by some neighbor. OK?
