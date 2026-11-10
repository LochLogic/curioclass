# Money and Meters

## One idea
At the ribbon counter of a school craft fair, one amount lives in four linked panels at once (dimes and pennies, a meter stick marked in tenths and hundredths, a 10 by 10 grid, and a number line from 0 to 1), so when the child changes any one (adds a penny, drags the ribbon's end, shades a square) the other three follow, with the fraction and decimal written under each, and 0.5, 0.50, 5/10 and 50/100 land on the same place; challenge rounds ask the child to make 3/10 + 4/100 with coins only (30/100 + 4/100 = 34/100 = 0.34), to place 0.7 and 0.07 on the number line, and to settle a claim from Ana (made up, labeled "illustration") that 0.45 is bigger than 0.5 because 45 is bigger than 5, which the meter stick settles; a same-whole round sets 0.3 of a meter of ribbon beside 0.3 of a dollar, and the clerk explains why the counter refuses to compare amounts of different wholes; at the end the child sees that tenths and hundredths are the same pieces in coins, centimeters and squares, and that more digits does not mean bigger, so a fourth grader learns to rewrite tenths as hundredths and add them, to write and place decimals to hundredths, and to compare two decimals with <, = or > and a reason.

## Not like
- zoom-by-tens (5, concept): place value to thousandths. Here tenths and hundredths in four views.
- stadium-count (4, concept): whole-number place value. Here decimals.
- corner-store (2, live): counting coins and making change. Here coins as tenths and hundredths of a dollar.
- fraction-trail (3, spec): fractions on a number line. Here decimals linked to fractions.

## Who and how
- Grade 4, Math, module "Decimals". Standards: 4.NF.5 (express a fraction with denominator 10 as an equivalent fraction with denominator 100, and use this technique to add two fractions with respective denominators 10 and 100), 4.NF.6 (use decimal notation for fractions with denominators 10 or 100; locate these decimals on a number line diagram), 4.NF.7 (compare two decimals to hundredths by reasoning about their size; recognize that comparisons are valid only when the two decimals refer to the same whole; record the results of comparisons with the symbols >, =, or <, and justify the conclusions, e.g., by using a visual model).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Four linked panels, eight free rounds, four adding rounds, six placing rounds, six compare rounds including Ana's claim, the same-whole round. Extra: Hidden panel (a projector view with one panel covered so the class predicts it). tool.json `modes: ["Ribbon counter", "Hidden panel"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.NF.5 | Make 3/10 + 4/100 with coins and the grid | 3 dimes become 30 pennies' worth; 34/100 | 2 |
| 4.NF.6 | Change one panel; place decimals on the line | all four panels moving; the dot at 0.07 | 3 |
| 4.NF.7 | Compare with a sign and a panel as proof; the same-whole round | the meter stick; the clerk's refusal | 4 |

## Screens and modes
Header (kit): title "Money and Meters"; `Ribbon counter`, `Hidden panel`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A craft-fair ribbon counter with four panels. A ribbon 0.3 m long lies on the meter stick; the other panels already show 3 dimes, 3 shaded grid columns and a dot at 0.3. The welcome is queued (`welcomeAfter: true`): "One amount, four ways to see it. Change any panel and watch the others. Drag the ribbon's end." First hint: "Drag the ribbon's end."

**Linked panels (focus: the panel in use).** At 1366x768 the four panels sit in a 2 by 2 grid with the challenge card below; at 680x425 one panel shows at a time with tabs and a strip of the other three as thumbnails. Under each panel: the fraction (34/100) and decimal (0.34). Adding a penny moves the ribbon 1 cm, shades one square and nudges the dot.

**Adding.** "Make 3/10 + 4/100 with coins only." Dimes trade for ten pennies' worth on the grid: 30/100 + 4/100 = 34/100.

**Placing.** The child drags dots for 0.7 and 0.07; the meter stick shows 70 cm and 7 cm.

**Compare.** Pairs with a sign to pick and a panel to pick as proof. Ana's claim: "0.45 is bigger than 0.5 because 45 is bigger than 5." The child lays both ribbons on the meter stick: 45 cm is shorter than 50 cm.

**Same whole (the aha).** 0.3 of a meter of ribbon and 0.3 of a dollar. The counter shows "Can't compare" and the clerk says: "They're both three tenths, but of different wholes. Compare only when the whole is the same."

**The end.** A receipt listing every amount in four forms. `Print` prints it.

**Hidden panel (extra).** One panel is covered and the class predicts it.

## Content
- Amounts from 0.01 to 1.00 in coins, centimeters, grid squares and line positions; dimes and pennies drawn plainly; all readable with `Read`.
- Coins are drawn in a plain style, not copied from real coin designs.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Any panel can drive; the others follow at once.
- Keyboard: Tab to each panel, the sign buttons and the proof picker; arrows change the amount by 0.01 (with Shift, 0.1); Enter checks.
- With Motion off the panels change without sliding.

## Look
- Accent `--brand` #8e2463 craft-fair plum (header, panel frames, buttons); gold #f4c542 (the panel in use, a matched amount); paper #fbeff5; ink #2b0a1c; muted #5e5058.
- Contrast (WCAG 2.1, computed): white on brand 8.13:1; brand on paper 7.27:1; ink on paper 16.14:1; muted on paper 6.79:1; ink on gold 11.10:1.
- Never color alone: every panel shows its fraction and decimal in words and numbers.
- Different from this batch (brick orange, quilt navy, track teal, workbench olive).

## Art
- People (illustrated): Ana and the clerk, labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Local FLUX (`scripts/localart.py`): the craft-fair counter (1, 16:9).
- Drawn in code: coins, the meter stick, the grid, the number line, ribbons.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the clerk; `upbeat-guide` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.panel + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `change`: "Change any panel: drag, tap a coin or shade a square."
- how `add`: "Make it with coins only."
- how `place`: "Drag the dot to the number."
- how `compare`: "Pick a sign, then pick a panel to prove it."
- event, whole, same whole.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the linked amount (kept in hundredths as a whole number) and four panel views; the number line uses `kit/number-line.js` as described in roller-coaster-rounding's spec.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Compare | Pick a sign at random | A sign needs a panel picked as proof, and the panel must show it. |
| Adding | Type 0.34 | Coins only: the dimes must be on the counter. |
| Same whole | Compare anyway | The counter asks what each amount is part of. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `change`.
2. `add`; `place`.
3. `compare`.
4. Same whole (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.NF.5, 4.NF.6, 4.NF.7 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| A dime is 1/10 of a dollar and a penny 1/100 | U.S. Mint, "Circulating coins" | Coinage Act of 1792, section 9 (the disme as one tenth and the cent as one hundredth of a dollar) | yes |
| "Longer is larger" is a common decimal mistake | Resnick and others (1989), "Conceptual bases of arithmetic errors: the case of decimal fractions", Journal for Research in Mathematics Education | Steinle and Stacey (2004), "A longitudinal study of students' understanding of decimal notation", PME proceedings | yes |
| Decimals are taught as fractions with denominators 10 and 100 | Common Core Standards Writing Team (2013), "Progressions for the CCSS, 3-5 Number and Operations, Fractions" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s13, 2026-11-10): 3/10 + 4/100 = 34/100 = 0.34; 0.5 = 0.50 = 5/10 = 50/100; 0.45 < 0.5; 0.07 < 0.7; 0.3 m is 30 cm; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 four panels; at 680x425 tabs and thumbnails.
2. Tenths are rewritten as hundredths and added with coins and the grid. (4.NF.5)
3. Changing any panel moves the others; decimals are placed on the line. (4.NF.6)
4. Six compares are made with a sign and a proof panel; the same-whole round refuses. (4.NF.7)
5. `Read` reads every card; every control is 48 px or more.
6. Ana and the clerk are labeled illustration; coins are plain drawings.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: panels change without sliding; no network requests.

## Open questions
None.
