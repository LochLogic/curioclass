# Spec fixes: math, grade 4

13 tools: 1 rework, 10 small addition, 2 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (1), Hand the key step to the student (4), Close the guessable check (6), Add the missing part (11), Add a model or a guide (2), Reach five items that differ (4).

## Fraction Wall Duel  [FIXED]

- Spec: `tools/fraction-wall-duel/spec.md` . Module: math-4-equivalent-fractions-and-comparing. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Note: 2026-11-10 rework: child splits, writes equal fractions and the why sentence on blank cards; drags the sign, carries out the reason, writes own reason line; wrong tries cost the round; traps need the same-whole sentence

- Checks a student can pass by guessing:
  - reason buttons: three choices, a wrong reason is shown false and counted, but no cost for a wrong try is stated
- **4.NF.A.1** (shown, in A round; Steals): Pick same-pieces reason; wall renames the fractions
  - To do: the tool does the "explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain why in words (the split shows it, nothing is said)
    - write equivalent fractions (cards are supplied)
    - state the n x a over n x b rule
- **4.NF.A.2** (taught, in A round; Later decks; Rule book): Play the bigger card; pick the reason the wall shows
  - Parts of the standard the student never does (must add):
    - record the comparison with >, = or <
    - justify in their own words (reason is chosen from three buttons)
    - say why the wholes differ on trap cards (the rule book voids the round)
- The read was unsure about (check these against the spec; the read may be wrong):
  - 4.NF.A.1 rated shown: the steal-split (student taps Split, bars must line up) is the only student step and happens only if the student chooses an equal card, so it is not guaranteed on the path
  - A.1 items 0 because steal count is not stated
  - engine is built first by this tool, so new-engine
  - 36 rounds from three decks of twelve

## Recipe Scaler  [FIXED]

- Spec: `tools/recipe-scaler/spec.md` . Module: math-4-adding-and-multiplying-fractions. Stage: spec only. Sort: **small addition**.
- Fixes: Write the spec, Hand the key step to the student, Add the missing part, Add a model or a guide, Reach five items that differ.
- Note: 2026-11-10 child writes every equation (strip no longer writes); Lou models first; five or more rounds per code; story problems and all amounts listed

- **4.NF.B.3** (taught, in Building): Tap scoops to fill a cup; sum strip counts unit fractions
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - write the sum themselves (the strip writes it)
- **4.NF.B.3a** (taught, in Pour and take away): Drag a flour bag in; take sugar away
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - say why the wholes must match
- **4.NF.B.3b** (taught, in Building; split step): Fill the same amount a second way
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - record each decomposition by an equation themselves (the strip writes it)
    - justify the decomposition in words
- **4.NF.B.3c** (shown, in Pour and take away): Pour two mixed amounts; watch fourths regroup
  - To do: the tool does the "add" step: the student must do it
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - replace mixed numbers with equivalent fractions themselves
    - use properties of operations or the add-subtract relation
- **4.NF.B.3d** (practiced, in Pour and take away; word problems follow): Solve kitchen word problems on adding fractions
  - To do: no model or guide: add one
  - Parts of the standard the student never does (small, add if cheap):
    - write an equation for the problem
    - draw a visual fraction model themselves
- **4.NF.B.4** (taught, in Scaling): Add batches; scoops pile into cups
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - write the product as a single fraction themselves in all cases
- **4.NF.B.4a** (taught, in Building): Fill 3/4 as 3 scoops of 1/4
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - record 5/4 = 5 x (1/4) themselves (the strip writes it)
- **4.NF.B.4b** (taught, in Scaling): Scale 6 x 2/3 as 12 scoops of 1/3
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - state n x (a/b) = (n x a)/b in general
    - explain the step in words
- **4.NF.B.4c** (taught, in Scaling; test bake): Answer batch questions; place 5 x 3/8 between wholes
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - write an equation for the problem
    - draw a visual fraction model themselves
- The read was unsure about (check these against the spec; the read may be wrong):
  - bare stems 4.NF.B.3 and 4.NF.B.4 kept as entries because the packet and spec print them
  - how a second way is made with one-size scoops (3/8 = 1/8 + 2/8) is not stated
  - kitchen word problems in 4.NF.B.3d get one sentence only; support and check guessed
  - 3c rated shown because the pour regroups on screen and the total is typed from it
  - fraction-food engine is described in pizza-party spec; may not exist, so sibling is a guess

## Road Trip Logbook  [FIXED]

- Spec: `tools/road-trip-logbook/spec.md` . Module: math-4-adding-and-subtracting-multi-digit-numbers. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part.
- Note: 2026-11-10 added sibling's worked sum, per-column feedback, and a twelve-problem Trip ledger to six digits for fluency

- **4.NBT.B.4** (taught, in Estimate; Columns; Miles left; Check): Estimate, then add and subtract in columns with regrouping
  - Parts of the standard the student never does (must add):
    - fluency (no speed or repeated-practice measure; about ten problems)
- The module also lists codes this tool does not carry: 4.NBT.B.5, 4.NBT.B.6.
- The read was unsure about (check these against the spec; the read may be wrong):
  - whether each column box gets its own right-or-wrong feedback is not stated
  - numbers stay at 3 to 4 digits; the standard names no upper limit
  - station chosen because the tool practices the algorithm more than it teaches why it works

## Skate Park Angles  [FIXED]

- Spec: `tools/skate-park-angles/spec.md` . Module: math-4-angles-and-line-plots. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Hand the key step to the student, Add the missing part, Reach five items that differ.
- Note: 2026-11-10 built tool, spec only: Spin jobs 7 to 11 added (sixths and twelfths, one-degree turns answered, student writes the equation); line plot scale choice not added

- **4.MD.B.4** (taught, in Jump Log): Read each jump on the pole; tap its dot on the plot
  - Parts of the standard the student never does (small, add if cheap):
    - choose the scale or draw the axis (axis is given)
    - use halves and quarters as the data unit (data is eighths only)
- **4.MD.C.5a** (taught, in Spin Deck Explore; Spin jobs 1 to 3): Drag the board around the dial; fraction of a turn to degrees
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - say in words why a one-degree angle is 1/360 of a circle
- **4.MD.C.5b** (shown, in Spin Deck readout): Drag or arrow the dial; read the one-degree count
  - To do: the tool does the "understand" step: the student must do it
  - Parts of the standard the student never does (must add):
    - state that n one-degree angles make n degrees
    - answer any question on it
- **4.MD.C.7** (taught, in Spin jobs 4 to 6; Ramp job 3; Add a spin): Type the unknown angle in 90 + 45 = ? style jobs
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - write the equation themselves (the strip is given with a box for the unknown)
- The module also lists codes this tool does not carry: 4.MD.C.5.
- The read was unsure about (check these against the spec; the read may be wrong):
  - built tool; src.html not read
  - 4.MD.C.5 stem is not named in the spec so it is listed as untaught and not given an entry
  - 5b rated shown: arrow stepping and the one-degree count line show it, but no job checks it though the Standards map cites Spin job 3
  - jump log items 43 = 34 dots plus 9 questions
  - ongoing because progress saves on the device and Park fills over sittings; spec says 20 to 40 minutes

## Money and Meters  [FIXED]

- Spec: `tools/money-and-meters/spec.md` . Module: math-4-decimals. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ.
- Note: 2026-11-10 panel labels hidden in challenge rounds; child writes hundredths form, sums, decimals and fractions on a blank tag; compares need the sign, both amounts built, and a reason line; six sums

- **4.NF.C.5** (taught, in Adding): Build 3/10 + 4/100 with coins; dimes trade to pennies
  - To do: only 4 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write the equivalent fraction and the sum themselves (written under each panel)
- **4.NF.C.6** (taught, in Linked panels; Placing): Drag dots to place 0.7 and 0.07 on the line
  - Parts of the standard the student never does (must add):
    - write the decimal or fraction themselves (shown under each panel)
- **4.NF.C.7** (taught, in Compare; Same whole): Pick a sign and a panel as proof
  - Parts of the standard the student never does (must add):
    - justify in their own words (a proof panel is picked, not explained)
- The read was unsure about (check these against the spec; the read may be wrong):
  - compare: three signs and four proof panels with unstated retry limits; spec says a sign needs a proof panel that shows it
  - C.5 key step rated shared: the student chooses coins, the panels do the 10-to-100 renaming
  - the 8 free rounds are not counted in items

## Egg Carton Factory  [FIXED]

- Spec: `tools/egg-carton-factory/spec.md` . Module: math-4-factors-and-multiples. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part.
- Note: 2026-11-10 built tool, spec only: Rush shift 5 "From the shelf" added so the student answers on "a multiple of each of its factors"

- **4.OA.B.4** (taught, in Pack Station; Fill Line; Rush Orders): Re-deal eggs into rows; find every carton; sort primes
  - Parts of the standard the student never does (must add):
    - recognize a number is a multiple of each of its factors (the seal card states it, nothing asks it)
- The read was unsure about (check these against the spec; the read may be wrong):
  - one entry for 4.OA.B.4 because the spec maps four parts to one code; each part rated together
  - built tool; src.html not read
  - Rush is a mode button, not forced; counted on_path because Pack Station seals feed the same factor work

## Quilt Block Studio  [FIXED]

- Spec: `tools/quilt-block-studio/spec.md` . Module: math-4-lines-angles-and-symmetry. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a model or a guide.
- Note: 2026-11-10 child drags name tags and finds lines and angles in Mae's block; scrap bin is now four yes-or-no sorts with proof marks and a mending pile; Mae models first

- Checks a student can pass by guessing:
  - scrap bin: twelve pieces, three labels, a wrong placement bounces back with the missing feature named and tries look free
- **4.G.A.1** (taught, in Drafting): Draft six tasks with point, segment, ray, line tools
  - Parts of the standard the student never does (must add):
    - name the lines and angles themselves (the kit names and tags them)
- **4.G.A.2** (practiced, in Scrap bin): Drag twelve scraps onto feature labels
  - To do: no model or guide: add one
  - Parts of the standard the student never does (must add):
    - classify by absence of a feature (all three labels name a feature present)
    - perpendicular lines as a sorting feature
    - angles of a specified size other than right
- The read was unsure about (check these against the spec; the read may be wrong):
  - A.2 rated practiced because its only check is the bounce-back, which is listed as beatable
  - flags are real national flags (cultural content) but only drawn shapes; not marked sensitive
  - mirror mode item count not stated and not counted

## Area Model Builder  [FIXED]

- Spec: `tools/area-model-builder/spec.md` . Module: math-4-multi-digit-multiplication-and-division. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part.
- Note: 2026-11-10 child types every equation (strip no longer fills) and writes how it worked on seven rectangles; guide models 12 x 13 and 852 by 4; all products and quotients listed

- **4.NBT.B.5** (taught, in Slicing; Two slicings): Drag cuts at place-value breaks; type each partial product
  - Parts of the standard the student never does (must add):
    - explain the calculation in words
    - write the full equation themselves (the strip fills; Match the slicing is an optional extra)
- **4.NBT.B.6** (taught, in Division): Drag chunks onto the missing side; type the remainder
  - Parts of the standard the student never does (must add):
    - explain the calculation in words
    - write the division equation themselves (the strip writes 857 = 4 x 214 + 1)
- The module also lists codes this tool does not carry: 4.NBT.B.4.
- The read was unsure about (check these against the spec; the read may be wrong):
  - area engine is described in tile-the-floor spec; unclear it exists as code, so sibling is a guess
  - the first division example (852 by 4) is worked for the student

## Growth Spurt  [FIXED]

- Spec: `tools/growth-spurt/spec.md` . Module: math-4-multiplicative-comparison. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ.
- Note: 2026-11-10 read-both-ways cards; child builds the strip; three division problems; tray answers typed on two sets, no choices; four orders on the main path; wrong kind costs the problem

- Checks a student can pass by guessing:
  - tray picker: three answers (9, 8, 2) matched to three questions; spec only says each question checks its own use, no stated cost for wrong tries
- **4.OA.A.1** (taught, in Growing; Standards map 4.OA.1): Grow the bean in times-as mode; write 24 = 3 x 8
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - read a given multiplication equation as a comparison in both directions (35 = 5 x 7 as 5 times as many as 7 and 7 times as many as 5)
- **4.OA.A.2** (taught, in Which one?): Tap Multiply or Add, then solve with a letter
  - Parts of the standard the student never does (must add):
    - divide to solve a comparison problem
    - draw the model themselves (the strip diagram redraws on its own)
- **4.OA.A.3** (taught, in Tray jobs; Orders): Pick the remainder answer each tray question wants; write order equation
  - Parts of the standard the student never does (must add):
    - subtract or divide inside a multistep order (the shown order is multiply then add)
    - decide for themselves how to use a remainder (three given answers are matched to three questions)
- The read was unsure about (check these against the spec; the read may be wrong):
  - 4.OA.A.1 check not stated, guessed tool-rule from 'written as multiplication equations'
  - tray picker retry limits not stated
  - Orders (extra mode) has longer orders, not counted in items

## Rule Machine  [FIXED]

- Spec: `tools/rule-machine/spec.md` . Module: math-4-number-patterns. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Note: 2026-11-10 child types terms 4 to 8 and writes the reason in own words; wrong card build costs the tape; mystery tapes typed before any print; all tapes listed

- Checks a student can pass by guessing:
  - mystery tapes: few dials and the child's tape prints beside Cog's, so the gap guides tuning
  - reason cards: wrong cards are mixed with true ones; spec says checked but not whether tries are limited
- **4.OA.C.5** (taught, in Number tapes; Reasons; Shape tapes; Mystery tapes): Set start and rule; predict feature; build reason from cards
  - Parts of the standard the student never does (must add):
    - write out the terms themselves (the tape prints them)
    - explain in their own words (reasons are built from supplied cards)
- The read was unsure about (check these against the spec; the read may be wrong):
  - items counts 8 number, 4 shape and 6 mystery tapes
  - shape-pattern prediction (21 tiles) answer format not stated
  - Tape for a friend (extra) not counted

## Stadium Count  [FIXED]

- Spec: `tools/stadium-count/spec.md` . Module: math-4-place-value-to-a-million. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Note: 2026-11-10 zoom stops locked until the count is typed; six ten-times cards; crowds given in all three forms and said aloud; compare taps the deciding place, wrong sign costs; two headlines with no line

- Checks a student can pass by guessing:
  - compare sign: three signs to tap, spec does not say tries are limited
- **4.NBT.A.1** (shown, in Zoom; Ten times): Drag the zoom slider; watch the digit slide left
  - To do: the tool does the "recognize" step: the student must do it
  - Parts of the standard the student never does (small, add if cheap):
    - use division to show it (700 / 70 = 10)
    - state the ten-times relation themselves
- **4.NBT.A.2** (taught, in Read and write; Compare): Type number names, build expanded form, tap compare sign
  - Parts of the standard the student never does (must add):
    - write the numeral from a name or expanded form (numeral is given)
    - read the number aloud (Read speaks it)
- **4.NBT.A.3** (taught, in Headlines): Drag crowd to nearest mark; pick the honest headline
  - Parts of the standard the student never does (small, add if cheap):
    - round without the number line (marks do the work)
- The read was unsure about (check these against the spec; the read may be wrong):
  - 4.NBT.A.1 is rated shown because the student drags the slider but never predicts or answers; the 4-seat second pass is also watching
  - whether the numeral is given or typed in Read and write is not stated
  - places rounded to are only the thousand and ten thousand in the example

## Community Plot Planner  [FIXED]

- Spec: `tools/community-plot-planner/spec.md` . Module: math-4-area-and-perimeter-formulas. Stage: spec only. Sort: **fine**.
- Fixes: Close the guessable check.
- Note: 2026-11-10 sorted fine; small: two tries on the missing side then a spare note; child works out the other measure from both sides for each plot

- Checks a student can pass by guessing:
  - missing-side number box after the squares fade: typed number, retry limits not stated
- **4.MD.A.3** (taught, in Area plots; Fence plots; Formula cards; The lot): Lay squares or fence; write the equation for the missing side
  - Parts of the standard the student never does (small, add if cheap):
    - find the area or perimeter when both sides are given (every note gives one side and a total)
- The module also lists codes this tool does not carry: 4.MD.A.1, 4.MD.A.2.
- The read was unsure about (check these against the spec; the read may be wrong):
  - area engine is described in tile-the-floor spec; sibling is a guess
  - only the last area plot is unaided once the cards fade, so the unaided count is small

## Unit Ladder  [FIXED]

- Spec: `tools/unit-ladder/spec.md` . Module: math-4-measurement-conversions. Stage: spec only. Sort: **fine**.
- Fixes: none found; confirm at final review.
- Note: 2026-11-10 sorted fine, nothing to fix; spec not changed (no role line added; confirm at final review)

- The module also lists codes this tool does not carry: 4.MD.A.3.
- The read was unsure about (check these against the spec; the read may be wrong):
  - items 80 assumes all eight unit sets are climbed (Done when says so); a student may pick fewer
  - the track marker placement may not be checked for accuracy, only required before the answer box opens
  - 4.MD.A.3 moved to community-plot-planner per the spec

