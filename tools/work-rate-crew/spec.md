# Work Rate Crew

## One idea
You run the schedule board for a small house-painting company: each call is a job with a deadline, and the only
way to know whether two crews together beat the clock is to add their rates (a house per 4 hours plus a house per
6 hours), never their times, so the wall on screen fills with both crews' paint at once and the rational equation
you write predicts the exact moment it is done; the back office then audits worksheets where a "solution" makes a
denominator zero.

## Not like
- savings-plan (gr 11, tycoon): money building over time by sequences. Here rates combine, and the unknown sits in a denominator.
- undo-machine (gr 11, puzzle): inverse functions as machines. Here equations with rational expressions, solved and checked for extraneous roots.
- outbreak-model (gr 11, simulator): exponential growth and logs. Here fixed rates and reciprocal sums.
- hole-hunter (gr 12, puzzle): finds holes and asymptotes on graphs. Here the asymptote shows up once, in the quote sheet, as "never faster than the fastest crew alone".
- model-my-world (gr 9): writes linear and exponential rules. Here every rule is a sum of reciprocals.
- courtroom-statistics (gr 12, roleplay): the other math role play; argues a claim. Here a dispatcher's job board, no argument.

## Who and how
- Grade 11, Algebra 2, Rational Expressions and Equations. Students drive. 20 to 40 minutes.
- Topic line: "rational equations, combined work rates and extraneous solutions".
- Standards (module): A-APR.D (D.6 rewriting a rational expression as q(x) + r(x)/b(x); D.7 adding rational expressions), A-REI.A.2 (solving rational equations in one variable, with extraneous solutions).
- CCSS clusters: Calls serve A-REI.A.2 and A-APR.D.7 (1/a + 1/b = (a + b)/ab); the Quote sheet serves A-APR.D.6; the Office audit serves A-REI.A.2 (extraneous solutions).
- tool.json: driver "students", minutes "20-40", modes ["Calls", "Quote sheet", "Office audit"], grades_label "Grade 11".

## Screens and modes
Header: title, subtitle "Add the rates, not the hours." Modes `Calls` (opens first), `Quote sheet`, `Office
audit`. Kit buttons.
Layout: left the schedule board (crew cards and the call card); center the wall (the painted house front, art:
wrc-house, standing on its street, art: wrc-street, that fills with paint); right the work panel. Under 900 px tall
the wall shrinks but stays the widest column, beside the board; at 760 wide the order is call card, work panel,
wall, crew cards.

Crew cards (made-up people and prices, labeled "made-up company"): Ana's crew, 4 hours a house, $90 an hour;
Ben's crew, 6 hours a house, $50 an hour; Cy's crew, 12 hours a house, $30 an hour. Each card shows its rate as a
fraction ("1/4 house per hour") and the crew's gear as its picture (art: wrc-gear-*: Ana a paint roller and tray,
Ben a bucket of brushes, Cy a stepladder; Dee's crew in call 3 a paint can, the sprayer crew in call 5 a paint
sprayer). Crew members stay names only, no portraits.

### Calls
Focus: the wall, center stage and the largest thing on screen; during Paint each crew's band grows from its side.
Five calls in order (Content). Each call card states the job and the question. Work panel steps:
1. `Rate sum`: tap crew cards to assign them; the tool writes the rate sum ("1/4 + 1/6") and the student types it as
   one fraction (5/12) in a box; checked exactly.
2. `Equation`: for calls with an unknown, the student builds the equation from tiles (the rates, t, x, =, 1) or types
   it; the tool checks it by testing sample values against the target equation.
3. `Solve`: type the answer; for calls with two roots, type both, then mark each `Fits` or `Doesn't fit` with a
   reason picker ("negative time", "makes a denominator zero", "fits").
4. `Paint`: the wall fills in real time (one second per hour, Motion off: a progress bar), each crew's color from its
   side; it stops at the student's time, or when the wall is full, and shows the fraction of the wall painted.
   Exactly 1 means done. Every run lasts at most 4 s (the slowest pair here, Ben and Cy, takes 4 hours). During a
   run every control stays live: a crew card, the call picker, a mode tab or `Paint` again stops it and acts at once.
Finished calls saved on this device (localStorage `curio-work-rate-crew`, try/catch) with `Clear board`.

### Quote sheet
Focus: the graph of T(x), center of the sheet, with the slider directly under it; the rewrite boxes sit above.
Ana's crew teams with a new crew that takes x hours alone. The sheet shows T(x) = 1/(1/4 + 1/x) = 4x/(x + 4) and asks
the student to rewrite it as 4 − 16/(x + 4) (fill the boxes in q + r/(x + 4)). Then a plane (graphing kit) draws T(x)
for x from 0 to 60 with the line T = 4 dashed; a slider sets x and the readout shows T(x). The card asks: "Can any
partner get the job under 2 hours?" (yes, any x below 4: T(x) < 2 when x < 4) and "Can any partner make it take 4
hours or more?" (no: 16/(x + 4) > 0, so T < 4 always). A one-line note explains that the remainder form shows both
at a glance.

### Office audit
Focus: the worksheet, a sheet of painted paper (art: wrc-paper) with the work in code, center and large; the verdict
buttons under it.
Four worksheets from a new hire. Each shows an equation and the hire's work ending in an answer. The student marks
each answer `Valid` or `Extraneous`, and for extraneous names the denominator that becomes zero. Substituting is a
button (`Check in the original`) that shows each denominator's value.

## Content
Calls:
1. Average myth. "Ana and Ben will paint the Lee house together. The office guessed 5 hours, the average of 4 and 6.
   How long will it really take?" 1/4 + 1/6 = 5/12, t = 12/5 = 2.4 h (2 h 24 min). The wall is full at 2.4 h; if the
   student paints for 5 hours it stops full and the readout says "In 5 hours they could paint 2 1/12 houses."
2. Deadline. "The Park house must be done in 3 hours. Which pairs make it, and which pair is cheapest?" Ana + Ben 2.4 h
   (yes, $336), Ana + Cy exactly 3 h (yes, $360), Ben + Cy 4 h (no). All three: 2 h ($340). Cheapest that makes it:
   Ana + Ben.
3. New hire. "Ana's crew and Dee's new crew painted a house in 3 hours. How long would Dee's crew take alone?"
   1/4 + 1/x = 1/3, x = 12.
4. Late start. "Ana starts at 8:00; Ben's crew joins at 9:00. When is the house done?" t/4 + (t − 1)/6 = 1, t = 14/5 =
   2.8 h after 8:00, done at 10:48.
5. Sprayer. "A crew with a paint sprayer paints a house 2 hours faster than a brush crew. Together they took 2.4 hours.
   How long does each take alone?" 1/x + 1/(x − 2) = 5/12, 5x² − 34x + 24 = 0, x = 6 or 0.8. x = 0.8 gives the
   sprayer −1.2 h (doesn't fit). Brush 6 h, sprayer 4 h.
Office audit (the hire's practice worksheet, not a job; labeled "practice sheet"):
1. x/(x − 3) = 3/(x − 3) + 2. Work gives x = 3. Extraneous (x − 3 = 0). No solution.
2. 1/(x − 2) + 1/(x + 2) = 4/(x² − 4). Work gives x = 2. Extraneous (x − 2 = 0). No solution.
3. x/(x − 1) = 1/(x − 1) + 2x. Work gives 2x² − 3x + 1 = 0, x = 1/2 or 1. x = 1/2 valid; x = 1 extraneous.
4. 2/(x + 1) + 1 = 6/(x + 1). Work gives x = 3. Valid.

## Interactions in detail
- All arithmetic exact with fractions; times shown as fractions, decimals and hours and minutes (12/5 h = 2.4 h =
  2 h 24 min).
- Equation checking: the student's equation is parsed (no eval) and compared with the target by testing five
  sample values away from any zero denominator; equivalent forms pass (1/4 + 1/6 = 1/t, 5t/12 = 1, t(1/4 + 1/6) = 1).
- Typed answers: fractions, decimals within 0.01 of the exact value, or "2 h 24 min".
- Reason picker for roots: right only when the reason matches (negative time for call 5's 0.8, a zero denominator in
  the audit).
- Quote sheet: the rewrite boxes q and r check exactly (4 and −16); the slider runs x from 0.5 to 60 in steps of 0.5.
- Wall fill: painted fraction = sum over crews of (hours worked ÷ crew's hours per house), capped at 1 on the wall
  (the readout shows the uncapped number), drawn as colored bands meeting, laid over the house picture with a
  multiply blend and clipped to the cutout so the siding grain shows through the paint.
- Keyboard: crew cards and tiles are buttons; slider with arrow keys; Enter submits a box.
- `window.__tool = {state, setMode, call(n), assign(crews), answer(text), audit(n, verdict)}`.

## Look
Accent `--brand #b8e0a0` (fresh sage paint), `--brand-ink #10200a`. Board `#1b2430` like a whiteboard with cards;
the house is painted in pale weathered gray white so the crew colors read on it: Ana `#ffd166`, Ben `#5aa9ff`, Cy
`#ff8a8a` (Dee and the sprayer crew reuse Ben's and Cy's slots in their calls), each band also labeled with the
crew's name on a dark pill (never color only). Office audit sheets on the legal pad image (the work sits on a `#f3efe4` paper card laid over it)
with dark text `#1b1b1b` (contrast 14.99:1). Contrast
(computed): brand on panel 11.71:1, on --sec-bg 11.10:1, brand-ink on brand 11.52:1. Minimal celebration: a done
call shows "Job done" on the card.

## Art
Local FLUX (`scripts/localart.py`), no people anywhere. 8 images. One style: friendly flat painted illustration,
late afternoon light.
- wrc-street: a quiet residential street in late afternoon, a strip of green lawn and sidewalk across the bottom,
  leafy trees and soft sky, an empty lot in the middle, flat painted illustration; 16:9; cutout no; people no;
  backdrop behind the house in the wall column.
- wrc-house: the front of a two-story wooden house with plain weathered pale gray white clapboard siding, four
  windows with dark frames, a front door and a small porch, straight-on view, flat painted illustration, plain
  white background; 4:3; cutout yes; people no; the wall that fills with paint, centered on the lawn.
- wrc-gear-roller, wrc-gear-brushes, wrc-gear-ladder, wrc-gear-can, wrc-gear-sprayer (kit of five, one shared
  prompt): {a paint roller resting in a paint tray | a metal bucket holding three paintbrushes | a wooden stepladder
  | a closed paint can with a plain blank label | a handheld paint sprayer with a coiled hose}, three quarter view,
  soft light, flat painted illustration, plain white background; 1:1; cutout yes; people no; the crew card pictures,
  about 64 px, all at the same size.
- wrc-paper: a single page of a yellow legal pad seen straight down, faint blue lines and a red margin line, soft
  even light, blank page; 3:4; cutout no; people no; the Office audit worksheet, with the work in code.
Drawn in code: the paint bands, the schedule board and cards' text, tiles, the Quote sheet plane, every label and
equation, preview.svg.

## Voice
Bank voice `lively-host` (Sadachbia), style "lively and friendly, like the dispatcher at a busy painting company
calling out the day's jobs". Changed from `news-reader`, which design-the-study (a math neighbor) also uses; not used
by any other neighbor or spec in this batch. `Curio.voice`, `scope: () => state.mode + ':' + state.call`. Call cards,
worksheets and notes are read on screen; Read speaks the hint.
- wCalls (how, Calls welcome; stale when a crew is first assigned): "Calls are on the board. Tap crew cards to put them on the job, then type their rate sum as one fraction."
- rate (how, first Rate sum step; stale when the sum is right): "Add the rates, not the hours. Each card says what part of a house that crew paints in an hour. Type the total in the box."
- done (event, a call's wall reaches exactly 1; stale on call change): "Job done, right on time."
- fit (how, first call with two roots; stale when both are marked): "Two roots. Mark each one Fits or Doesn't fit, and pick a reason."
- wQuote (how, Quote sheet welcome; stale when both boxes are right): "Fill the two boxes to write the time as 4 minus something. Then drag the x slider."
- wAudit (how, Office audit welcome; stale on the first verdict): "Tap Check in the original, then mark the answer Valid or Extraneous."
- extra (event, an extraneous answer caught; stale on the next sheet): "Caught it. That value breaks the equation."

## Family engine
none (uses `kit/graphing.js` only for the Quote sheet plot: Plane, g.fn, g.label, g.trace, with no new engine
features).

## Sources
- A-APR.D and A-REI.A.2: Common Core State Standards for Mathematics, High School Algebra, https://www.thecorestandards.org/Math/Content/HSA/APR/ and https://www.thecorestandards.org/Math/Content/HSA/REI/
- Work problems with rational equations: OpenStax, Intermediate Algebra 2e, 7.5 "Solve Applications with Rational Equations", https://openstax.org/books/intermediate-algebra-2e/pages/7-5-solve-applications-with-rational-equations
- Extraneous solutions of rational equations: OpenStax, Intermediate Algebra 2e, 7.4 "Solve Rational Equations", https://openstax.org/books/intermediate-algebra-2e/pages/7-4-solve-rational-equations
- Crews, names, hours and prices are made up and labeled so on screen.
- Every call and audit answer recomputed with exact fractions in Python (2026-10-27): 12/5, 12, 14/5, 6 and 4/5, 1/2.
- Checks run (Python, fractions and sympy, 2026-10-29): call 1 rate 5/12, time 12/5, 5 hours paints 25/12; call 2
  Ana + Ben 12/5 h $336, Ana + Cy 3 h $360, Ben + Cy 4 h, all three 2 h $340; call 3 x = 12; call 4 t = 14/5; call 5
  roots 4/5 and 6. Quote sheet: 4x/(x + 4) − (4 − 16/(x + 4)) simplifies to 0; T(12) = 3; T < 2 exactly when
  0 < x < 4; T(0.5) = 4/9 and T(60) = 15/4, under 4 across the slider. Audit: sympy finds no solution for sheets 1
  and 2, only 1/2 for sheet 3, and 3 for sheet 4. Longest paint run 4 s. Nothing failed; no rule changed. The draft
  said the wall shows 5 hours painting 2 1/12 houses, but the wall caps at 1, so the readout now says it.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Call 1: the rate sum accepts 5/12 and the time 12/5 (also 2.4 and "2 h 24 min"); typing 5 is refused; the wall at 2.4 h shows exactly 1.
2. Call 2: Ana + Cy is exactly 3 h and counts as making the deadline; Ana + Ben is cheapest at $336; Ben + Cy fails.
3. Call 4: t/4 + (t − 1)/6 = 1 and its equivalents pass; 14/5 and 10:48 are accepted.
4. Call 5: roots 6 and 4/5; 4/5 needs the reason "negative time" (sprayer −1.2 h).
5. Quote sheet: boxes accept 4 and −16; T(12) = 3 on the readout; the dashed line at 4 is never crossed.
6. Audit sheets 1 and 2 are extraneous with the right denominator named; sheet 3 needs x = 1/2 valid and x = 1 extraneous; sheet 4 is valid.
7. Focus: at 1366x768 and 1000x625 the house wall is the largest thing in Calls, the T(x) graph on the Quote sheet,
   the worksheet in the audit.
8. Tap while it plays: during Paint, a crew card, the call picker and a mode tab act at once and the wall shows the
   new state.
9. The paint bands show the siding through them and each band carries its crew's name.
10. Board progress survives a reload; `Clear board` works; every size in STANDARDS.md keeps the call card, the work panel and the wall visible; keyboard only works; console clean, no network.

## Open questions
- Work problems rarely produce a true extraneous root (a zero denominator); they produce roots that don't fit the story (negative time). So the Office audit uses practice-sheet equations, not jobs, to teach real extraneous solutions. Is a practice sheet inside a role play acceptable, or should the audit be dropped and extraneous roots taught only as "doesn't fit"?
