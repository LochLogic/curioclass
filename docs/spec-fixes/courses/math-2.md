# Spec fixes: math, grade 2

9 tools: 2 rework, 7 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (2), Hand the key step to the student (3), Close the guessable check (5), Add the missing part (8), Add a model or a guide (1), Reach five items that differ (3), Teach the code or drop it (2).

Shape for this course: ../../agents/catalog/shape/math-2.md.

## Marching Band

- Spec: `tools/marching-band/spec.md` . Module: math-2-odd-even-and-arrays. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Write the spec, Hand the key step to the student, Add the missing part.
- **2.OA.C.3** (shown, in Partners mode, plan.md hook): Class calls partner or alone as teacher adds a musician
  - To do: the tool does the "determine" step: the student must do it
  - Parts of the standard the student never does (must add):
    - pair or count by 2s themselves
    - write an equation as a sum of two equal addends (the tool writes it)
- **2.OA.C.4** (shown, in Rows mode, plan.md apply): Set rows and columns; class reads the repeated addition
  - To do: the tool does the "use, write" step: the student must do it
  - Parts of the standard the student never does (must add):
    - find the total by adding themselves
    - write the equation themselves (on whiteboards off the tool)
- The read was unsure about (check these against the spec; the read may be wrong):
  - spec.md holds only voice; used notes.md, plan.md, tool.json and the src.html header
  - driver is teacher, so students do not touch the tool
  - minutes 30 from plan.md; tool.json says 10-15
  - cost_class guessed simple
  - whiteboard exit check is off the tool

## Corner Store

- Spec: `tools/corner-store/spec.md` . Module: math-2-time-and-money. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Write the spec, Hand the key step to the student, Close the guessable check, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Give change: too much or too little feedback says which way, free tries and coins can be taken back
- **2.MD.C.7** (claimed, in tool.json outcome; plan.md): Watches the clock advance 5 minutes per customer
  - To do: nothing the student does matches this code: teach it or drop it
  - To do: the tool does the "tell and write" step: the student must do it
  - Parts of the standard the student never does (must add):
    - tell time
    - write time
    - a.m. and p.m.
    - read analog and digital clocks
- **2.MD.C.8** (practiced, in Count it together; Give change): Count coins paid, count up from price to give change
  - Parts of the standard the student never does (small, add if cheap):
    - write amounts with $ and cent symbols
- The read was unsure about (check these against the spec; the read may be wrong):
  - spec.md holds only the voice spec, so rows come from notes, plan and tool.json
  - time is only watched, class talk question in plan.md is teacher-led
  - cost_class guessed new-engine, family money origin unknown
  - Count it together may do the paid-coin counting for the student

## Jump Line

- Spec: `tools/jump-line/spec.md` . Module: math-2-adding-and-subtracting-to-1000. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a model or a guide, Reach five items that differ.
- Checks a student can pass by guessing:
  - Mental lane taps (choices not stated; Hopper hops once to check, free tries)
- **2.NBT.B.5** (taught, in Jumping; Subtraction): Drag and label jumps to add and subtract within 100
  - Parts of the standard the student never does (small, add if cheap):
    - fluency beyond a drawn jump path
- **2.NBT.B.6** (taught, in Four-number path): Walk four two-digit numbers in one jump path
  - To do: only 3 items: reach five or more that differ
- **2.NBT.B.7** (taught, in Hundreds): Jump across hundreds and break a jump into hundreds, tens, ones
  - Parts of the standard the student never does (must add):
    - relate the strategy to a written method (the strip writes the steps)
    - say that hundreds go with hundreds, tens with tens
- **2.NBT.B.8** (practiced, in Mental lane): Tap 10 more, 10 less, 100 more, 100 less
  - To do: no model or guide: add one
- **2.NBT.B.9** (taught, in Path gallery): Judge three classmate paths, finish 'It works because' from pieces
  - Parts of the standard the student never does (must add):
    - say the reason in own words
    - name the properties of operations
- The read was unsure about (check these against the spec; the read may be wrong):
  - B.5 and B.6 support rated guided from hints only
  - gallery pieces: number of pieces not stated, trial may be cheap
  - mental lane answer format (tap choices) not stated
  - does the tool check the answer of a drawn path? inferred yes from Done when 2

## Fact Rally

- Spec: `tools/fact-rally/spec.md` . Module: math-2-fluency-within-20. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part.
- **2.OA.B.2** (taught, in Rally, Strategy chips, Board): Tap answers to served facts; tap strategy chips
  - Parts of the standard the student never does (must add):
    - use mental strategies on their own (chips and pictures show them; tapping is optional)
- The read was unsure about (check these against the spec; the read may be wrong):
  - items 10 per rally
  - four answer buttons, so guessing is possible but misses return
  - depth taught on the main drill

## Place Value Vault

- Spec: `tools/place-value-vault/spec.md` . Module: math-2-hundreds-tens-and-ones. Stage: spec only. Sort: **small addition**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ, Teach the code or drop it.
- Checks a student can pass by guessing:
  - Compare: two codes and three signs with free retry, trays show the answer
  - Skip-count: tap plus until the dial reaches the target
- **2.NBT.A.1a** (taught, in Bundle lock): Drag ten rods together to snap a flat
  - To do: only 3 items: reach five or more that differ
- **2.NBT.A.1b** (claimed, in Standards line only): Codes run 100 to 999; no lock names round hundreds
  - To do: nothing the student does matches this code: teach it or drop it
  - Parts of the standard the student never does (must add):
    - no lock isolates 100 to 900 as 1 to 9 hundreds
- **2.NBT.A.2** (shown, in Skip-count lock): Tap plus to click the dial to a target; tool says numbers
  - To do: the tool does the "count, skip-count" step: the student must do it
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - count within 1000 one by one
    - say or write the skip-count numbers themselves
- **2.NBT.A.3** (taught, in Word lock): Turn number names and expanded form into dial digits
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - write number names
    - write expanded form
- **2.NBT.A.4** (practiced, in Compare lock): Pick the bigger code and the sign
  - To do: only 3 items: reach five or more that differ
- The module also lists codes this tool does not carry: 2.NBT.A.1b.
- The read was unsure about (check these against the spec; the read may be wrong):
  - 2.NBT.A.1b judged claimed: no lock isolates it
  - items 3 per lock type assumed (three vaults of five locks)
  - unclear whether the student sets 5s, 10s or 100s steps

## Lunch Line Data

- Spec: `tools/lunch-line-data/spec.md` . Module: math-2-line-plots-and-bar-graphs. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Measure: a wrong tap highlights the nearest mark, so the answer is shown after one try
- **2.MD.D.9** (practiced, in Carrot crates): Drag ruler to each carrot, tap the nearest inch
  - Parts of the standard the student never does (must add):
    - repeated measurements of one object
    - make the line plot (the X stacks by itself)
- The read was unsure about (check these against the spec; the read may be wrong):
  - items for D.10 counts 3 polls plus 9 questions
  - question answer format (tap) and number of choices not stated
  - Measure the room mode is optional

## Estimation Station

- Spec: `tools/estimation-station/spec.md` . Module: math-2-rulers-and-units. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Add the missing part, Reach five items that differ.
- **2.MD.A.2** (taught, in Two-unit crate): Measure in one unit, guess then measure the other
  - To do: only 1 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - describe how the two measurements relate to unit size (the tool says it)
- **2.MD.A.4** (taught, in Ribbon crate): Read both ribbons on one tool, type the difference
  - To do: only 1 items: reach five or more that differ
- **2.MD.B.5** (taught, in Order slips): Place piece B on the tape, type the box in the equation
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - write the equation themselves (the tool writes it from the layout)
- **2.MD.B.6** (taught, in Order slips; Placements): Lay pieces from 0 end to end or side by side, read the point or gap
  - To do: only 2 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - represent a single whole number as a point (pieces are given bars)
- The read was unsure about (check these against the spec; the read may be wrong):
  - 2.MD.A.2 and B.5 and A.4 appear once or twice per run so items are low
  - A.2 depth: student measures but the tool states the relation
  - Yard mode is optional so not counted
  - action drill kept; race format

## Garden Grid

- Spec: `tools/garden-grid/spec.md` . Module: math-2-shapes-and-equal-shares. Stage: spec only. Sort: **small addition**.
- Fixes: Add the missing part.
- **2.G.A.1** (taught, in Shape orders): Drag corner posts to build the bed a clue names
  - Parts of the standard the student never does (must add):
    - identify shapes shown to them
    - cube (the bin unfolds, the child does not build or name it)
- **2.G.A.3** (taught, in Fair shares): Draw lines to share a bed among 2, 3 or 4
  - Parts of the standard the student never does (must add):
    - describe shares in words (the tool says them)
    - describe the whole as two halves, three thirds, four fourths
    - the different-shape vote is run by the club, not the child
- The read was unsure about (check these against the spec; the read may be wrong):
  - share size bars let a child nudge lines until bars match, may be trial

## Lost and Found

- Spec: `tools/lost-and-found/spec.md` . Module: math-2-two-step-word-problems. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Answer: type each of the five sticker numbers until a box is ruled out (free tries)
- **2.OA.A.1** (practiced, in A clue, Ruling out): Drag bars, build an equation, type the answer to a clue
  - Parts of the standard the student never does (must add):
    - write the equation themselves (the builder fills it in)
    - put together and take apart situations with both addends unknown
- The read was unsure about (check these against the spec; the read may be wrong):
  - depth practiced: the model is optional and the answer check is beatable
  - put-together and take-apart not named

