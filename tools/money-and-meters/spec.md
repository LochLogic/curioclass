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
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the four linked panels stay. Before, the fraction and decimal were printed under every panel, so the child never wrote one, and a compare was a sign plus a picked panel. Now every challenge round hides the printed labels and gives the child a blank tag to write; adding goes from four rounds to six, with the hundredths form and the sum both written by the child; compares need the child to build both amounts in the proof panel and write a reason line; a wrong sign costs the pair. The clerk writes one tag first as the model.
- Four linked panels, eight free rounds, the clerk's worked tag, six adding rounds, ten tag-and-place rounds, six compare rounds including Ana's claim, two same-whole rounds. Extra: Hidden panel (a projector view with one panel covered so the class predicts it). tool.json `modes: ["Ribbon counter", "Hidden panel"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NF.5 | express a tenths fraction as hundredths; use this to add tenths and hundredths | the student | Write 3/10 = __/100 on the tag, then write the sum; coins and grid confirm after | 6 (one sum reaches 1; one starts with the hundredths) | dimes trading to pennies only after the tag is written | 2 |
| 4.NF.6 | use decimal notation for fractions with denominators 10 or 100; locate decimals on a number line | the student | Write the decimal for a fraction, the fraction for a decimal, and drag a dot to a decimal on a line with no labels but 0 and 1 | 10 (4 decimals written, 2 fractions written, 4 dots placed) | the blank tag; the line; the other panels after the check | 3 |
| 4.NF.7 | compare two decimals to hundredths by reasoning about size; same whole only; record with >, = or <; justify with a model | the student | Drag the sign, build both amounts in a panel of your choice, write one reason line and check it against the guide; finish the same-whole sentence | 6 pairs and 2 same-whole rounds | the child's two ribbons or grids side by side | 4, 5 |

## Screens and modes
Header (kit): title "Money and Meters"; `Ribbon counter`, `Hidden panel`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A craft-fair ribbon counter with four panels. A ribbon 0.3 m long lies on the meter stick; the other panels already show 3 dimes, 3 shaded grid columns and a dot at 0.3. The welcome is queued (`welcomeAfter: true`): "One amount, four ways to see it. Change any panel and watch the others. Drag the ribbon's end." First hint: "Drag the ribbon's end."

**Linked panels (focus: the panel in use).** At 1366x768 the four panels sit in a 2 by 2 grid with the challenge card below; at 680x425 one panel shows at a time with tabs and a strip of the other three as thumbnails. Under each panel: the fraction (34/100) and decimal (0.34). Adding a penny moves the ribbon 1 cm, shades one square and nudges the dot.

**The clerk writes a tag (the model).** After the free rounds the clerk takes a ribbon of 3 tenths of a meter and writes its price tag while saying each step: "3 tenths. Each tenth is 10 hundredths, so 30 hundredths. As a decimal, 0.30, which is the same as 0.3." The tag reads 3/10 = 30/100 = 0.3. It cannot be skipped and `Clerk's tag` reopens it.

**Challenge rounds hide the labels.** From here on the fraction and decimal under each panel are covered by a blank tag until the child's answer is checked. Free play keeps them on show.

**Adding.** "A customer wants 3/10 of a meter and 4/100 of a meter more." The child writes on the tag, in typed boxes: 3/10 = __/100, then __/100 + 4/100 = __/100. `Check` then lets the coins run: three dimes trade for thirty pennies' worth on the grid and four more squares shade, landing on the typed sum or missing it. A miss can be fixed once; a second miss shows the trade slowly and the round returns later with new numbers.

**Tags and dots.** Ten rounds. Four give a fraction and ask for the decimal on the tag; two give a decimal and ask for the fraction; four ask the child to drag a dot to a decimal on a number line marked only at 0 and 1, with ten unlabeled ticks, which zooms into one tenth when the dot is held still so hundredths can be placed. A dot within half a hundredth passes. After each check the meter stick, coins and grid show the amount (0.07 is 7 cm, 7 pennies, 7 squares).

**Compare.** Each pair shows two decimals as plain numbers. The child (1) drags `>`, `=` or `<` between them, (2) picks a panel and builds both amounts in it by hand (two ribbons on the meter stick, two coin piles, two grids or two dots), and (3) writes a reason line beside a three-box guide: says what each decimal is in tenths or hundredths; uses the picture; says which is more. The clerk's model line stays in view: "0.5 is 50 hundredths and 0.45 is 45 hundredths, so 0.5 is more. The ribbons show it." Then the sign is judged. A wrong sign can be changed once after the build; a second miss sends the pair to the end of the list with new numbers. Ana's claim is one of the six: "0.45 is bigger than 0.5 because 45 is bigger than 5." The child lays both ribbons: 45 cm is shorter than 50 cm.

**Same whole (the aha).** Two rounds. 0.3 of a meter of ribbon against 0.3 of a dollar, then 0.5 of a small spool against 0.5 of a big spool. No sign fits: the child taps `Cannot compare` and finishes "They are both __ , but of different __ ." A sign dragged in is refused and the clerk says: "They're both three tenths, but of different wholes. Compare only when the whole is the same."

**The end.** A receipt listing every amount in four forms. `Print` prints it.

**Hidden panel (extra).** One panel is covered and the class predicts it.

## Content
- Amounts from 0.01 to 1.00 in coins, centimeters, grid squares and line positions; dimes and pennies drawn plainly, not copied from real coin designs; all readable with `Read`.
- Adding rounds: 3/10 + 4/100 = 34/100; 5/10 + 7/100 = 57/100; 2/10 + 15/100 = 35/100; 26/100 + 4/10 = 66/100; 1/10 + 9/100 = 19/100; 6/10 + 40/100 = 100/100 = 1.
- Tags: 7/10 as 0.7; 7/100 as 0.07; 62/100 as 0.62; 40/100 as 0.40 or 0.4; 0.9 as 9/10 (or 90/100); 0.05 as 5/100. Dots: 0.7, 0.07, 0.62, 0.35.
- Compare pairs: 0.45 < 0.5 (Ana's claim); 0.07 < 0.7; 0.3 = 0.30; 0.62 > 0.26; 0.8 > 0.75; 0.09 < 0.1.
- Same whole: 0.3 m and 0.3 of a dollar; 0.5 of a 2 m spool and 0.5 of a 10 m spool.

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
- how `add`: "Type the hundredths on the tag, then the sum."
- how `tag`: "Write it on the blank tag."
- how `place`: "Drag the dot to the number, then tap Check."
- how `compare`: "Drag a sign between them. Then build both in one panel."
- how `why`: "Write your reason, then check the guide."
- event, whole, the clerk's tag.
- event, whole, same whole.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the linked amount (kept in hundredths as a whole number) and four panel views; the number line uses `kit/number-line.js` as described in roller-coaster-rounding's spec.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Read the label under a panel | Labels are covered in every challenge round until the check. |
| Adding | Type 0.34; add tops and bottoms (7/110) | The tag asks for the hundredths form first and the sum as hundredths; 7/110 fails and the coins show why. A second miss brings new numbers. |
| Dots | Slide until it turns green | Nothing changes color while dragging; the dot is judged only on `Check`, twice at most. |
| Compare | Guess one of three signs; read the longer ribbon first | The sign goes in before the build; one change is allowed after it, then the pair returns with new numbers. The child builds the ribbons, so reading them is doing the reasoning. |
| Reason line | Tick the boxes on an empty line | The ticks open only when the line has words; the line is printed on the receipt. |
| Same whole | Compare anyway | A sign is refused and the sentence must be finished. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `change`.
2. The clerk's tag (whole). `add`; `tag`; `place`.
3. `compare`; `why`.
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
Checks run again for the spec fix (Python `fractions` and `decimal`, scratchpad s/fx, 2026-11-10): the six sums (34, 57, 35, 66, 19 and 100 hundredths); the six tags; the six compare signs; add-tops-and-bottoms slips (7/110, 12/110, 17/110, 30/110, 10/110, 46/110) never equal a right sum.

## Done when
1. Focus and fold: at 1366x768 four panels; at 680x425 tabs and thumbnails.
2. Six sums: the child writes the hundredths form and the sum before the coins move. (4.NF.5)
3. Ten tag-and-dot rounds with the panel labels covered: decimals and fractions are written and four dots placed. (4.NF.6)
4. Six compares: the sign is dragged in, both amounts are built by the child in one panel, and a reason line is written and checked against the guide. (4.NF.7)
5. Two same-whole rounds refuse a sign and need the sentence finished. (4.NF.7)
6. The clerk's tag plays before the challenge rounds and can be reopened; changing any panel in free play moves the others.
7. `Read` reads every card; every control is 48 px or more.
8. Ana and the clerk are labeled illustration; coins are plain drawings.
9. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
10. Motion off: panels change without sliding; no network requests.

## Open questions
None.
