# Zoom by Tens

## One idea
On a nature table a magnifier hangs over a meter stick and a tray of small real things (a pencil, an acorn, a ladybug, a grain of rice, a grain of sand); the child lays an item on the stick and zooms in, and each zoom spreads ten new marks between the old ones, so the pencil reads 0.2 m, then 0.18 m, then 0.175 m, and the length gains one digit per zoom; a place-value chart beside the stick shows each digit worth 10 times the one to its right and 1/10 of the one to its left; slide rounds line up 10, 100 and 1,000 rice grains (0.07 m, 0.7 m, 7 m), so the length is multiplied by 10, 10^2 and 10^3 and the decimal point slides one place per zero, then divides back down; compare rounds set the ladybug (0.008 m) beside the rice grain (0.007 m) and ask which of 0.25 and 0.205 is longer; round rounds zoom out to round a length to the nearest hundredth or tenth (0.175 m to 0.18 m, then 0.2 m); name-it rounds write 0.175 in expanded form and in words; at the end the child sees that every place is ten of the place to its right, so multiplying by 10 just moves every digit one place, so a fifth grader learns place value of decimals to thousandths, powers of ten with exponents, and reading, writing, comparing and rounding decimals.

## Not like
- size-of-everything (Grades 7-9, live): scientific notation across the universe. Here one meter stick and thousandths.
- money-and-meters (4, spec): tenths and hundredths as money and centimeters. Here thousandths and powers of ten.
- stadium-count (4, spec): whole-number place value with crowds. Here decimal places below one.
- roller-coaster-rounding (3, spec): rounding whole numbers to 10 and 100. Here rounding decimals to any place.

## Who and how
- Grade 5, Math, module "Powers of Ten and Decimals". Standards: 5.NBT.1 (recognize that in a multi-digit number, a digit in one place represents 10 times as much as it represents in the place to its right and 1/10 of what it represents in the place to its left), 5.NBT.2 (explain patterns in the number of zeros of the product when multiplying a number by powers of 10, and explain patterns in the placement of the decimal point when a decimal is multiplied or divided by a power of 10; use whole-number exponents to denote powers of 10), 5.NBT.3 (read, write, and compare decimals to thousandths: a. read and write decimals to thousandths using base-ten numerals, number names, and expanded form; b. compare two decimals to thousandths based on meanings of the digits in each place, using >, =, and < symbols to record the results of comparisons), 5.NBT.4 (use place value understanding to round decimals to any place).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six objects with sourced sample lengths, three zoom levels, six slide rounds, six compare rounds, six round rounds, four name-it rounds. Extra: My ruler (the child measures a real object at home and enters it; it stays on the device). tool.json `modes: ["Nature table", "My ruler"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.NBT.1 | Zoom in and read each new digit | ten new marks; the place-value chart | 2 |
| 5.NBT.2 | Line up 10, 100, 1,000 grains; divide back | the point sliding; 10^1, 10^2, 10^3 | 3 |
| 5.NBT.3 | Compare lengths; write expanded form and words | items side by side; 0.175 in three forms | 4 |
| 5.NBT.4 | Zoom out to round | the nearest mark lighting up | 4 |

## Screens and modes
Header (kit): title "Zoom by Tens"; `Nature table`, `My ruler`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A sunny nature table, a brass magnifier over a meter stick, and a tray with a pencil, an acorn, a feather, a ladybug, a grain of rice and a grain of sand. The welcome is queued (`welcomeAfter: true`): "Everything here fits on one meter stick. Drag the pencil onto the stick, then tap Zoom in." First hint: "Drag the pencil onto the stick."

**Zoom (focus: the stick).** At 1366x768 the stick runs across the middle with the magnifier window above and the place-value chart right; at 680x425 the chart is a tab. Each `Zoom in` fills the window with ten new marks between two old ones and adds a column to the chart (tenths, hundredths, thousandths). The child types the reading at each level: 0.2, 0.18, 0.175. The chart's arrows read "10 times" leftward and "1/10 of" rightward.

**Slide rounds.** 10 rice grains in a row, then 100, then 1,000 (the 1,000 row runs off the table onto the floor). The child types each length; the chart writes 0.007 x 10^1 = 0.07 and the decimal point slides one place per zero. Then the rounds run backward: 7 m / 10^3 = 0.007 m.

**Compare rounds.** Two items or two cards side by side: the ladybug and the rice grain (0.008 against 0.007), 0.25 against 0.205. The child picks >, = or <, and the chart lines the digits up by place.

**Round rounds.** The child taps `Zoom out` until the stick shows hundredths, and the nearest mark lights: 0.175 rounds to 0.18. One more zoom out: 0.2.

**Name it.** The child builds 0.175 from tiles as 1 x 1/10 + 7 x 1/100 + 5 x 1/1000 and writes it in words ("one hundred seventy-five thousandths").

**Every place (the aha).** All three zoom windows stack. Narrator: "Each place is ten of the place to its right. Times ten just moves every digit one place over."

**The end.** The measurement log. `Print` prints it.

**My ruler (extra).** The child types a length measured at home; it is placed on the stick and zoomed like the others.

## Content
- Six items with sample lengths labeled "about": pencil 0.175 m, feather 0.150 m, acorn 0.025 m, ladybug 0.008 m, rice grain 0.007 m, sand grain 0.0005 m (shown only as "less than one thousandth"). The pencil, feather and acorn are typical sizes; the three small items are sourced. All readable with `Read`.
- Lengths stay within thousandths in the rounds; the sand grain shows where the stick runs out of marks.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Readings can be retyped until `Check`.
- Keyboard: Tab to tray items, the stick, Zoom in, Zoom out, the chart, comparison signs and tiles; Enter places or checks; plus and minus keys zoom.
- With Motion off each zoom level appears at once.

## Look
- Accent `--brand` #3b3f8f magnifier indigo (header, the chart, buttons); gold #f4c542 (the item in hand, the lit mark); paper #f0f1fa; ink #0d0f2b; muted #50525f.
- Contrast (WCAG 2.1, computed): white on brand 9.16:1; brand on paper 8.14:1; ink on paper 16.66:1; muted on paper 6.88:1; ink on gold 11.53:1.
- Never color alone: the lit mark carries its number; comparisons show the sign and words.
- Different from this batch (chart sea blue, sprout green, sign red, cardboard umber).

## Art
- Local FLUX (`scripts/localart.py`): the nature table (1, 16:9), six items (6, 1:1), the magnifier (1, 1:1).
- Drawn in code: the meter stick and every mark, the zoom window, the place-value chart, tiles.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as the narrator; `bright-teacher` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.zoom + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `zoom`: "Tap Zoom in."
- how `read`: "Type the length you see."
- how `slide`: "Type the length of the whole row."
- how `compare`: "Tap the sign that fits."
- how `round`: "Tap Zoom out to round."
- event, whole, every place.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: exact decimals kept as integer thousandths (no floating point), the zoom window, the place-value chart, slide rounds. Lengths sit in a marked block `/* LENGTHS DATA: begin */ ... /* end */` with sources.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Readings | Type any long decimal | Each level checks its own digit count (0.2, 0.18, 0.175). |
| Slides | Add a zero every time | 0.007 x 10 is checked as 0.07, not 0.0070 shown as new. |
| Compare | Pick the longer numeral | 0.25 against 0.205 is built to catch it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `zoom`; `read`.
2. `slide`.
3. `compare`; `round`.
4. Every place (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.NBT.1 to 5.NBT.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| A long-grain rice kernel is about 7 mm | USDA Federal Grain Inspection Service, "Rice Inspection Handbook" (long grain at least 6.6 mm) | USA Rice Federation, "Rice Varieties" | yes |
| A seven-spot ladybug is about 7 to 8 mm | University of Minnesota Extension, "Multicolored Asian lady beetles and other lady beetles" | Penn State Extension, "Lady Beetles" | yes |
| Medium sand grains are 0.25 to 0.5 mm | USGS, "Wentworth grain size chart" | Wentworth (1922), "A scale of grade and class terms for clastic sediments", Journal of Geology | yes |
| Decimal place value extends whole-number place value | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s16, 2026-11-10): 0.175 rounds to 0.18 and 0.2 (half up, exact decimals); 0.007 x 10, 10^2, 10^3 = 0.07, 0.7, 7; 7 / 10^3 = 0.007; 0.25 > 0.205 and 0.008 > 0.007; 1/10 + 7/100 + 5/1000 = 175/1000; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 stick, window and chart; at 680x425 chart as a tab.
2. Three zoom levels are read for each item, and the chart shows 10 times and 1/10 of. (5.NBT.1)
3. Six slide rounds multiply and divide by powers of ten written as exponents. (5.NBT.2)
4. Comparisons, expanded form, words and rounding are done to thousandths. (5.NBT.3, 5.NBT.4)
5. Lengths are labeled "about" and come from the marked data block with sources.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: zoom levels appear at once; no network requests.

## Open questions
- The idea card flags a data source (default used: sample lengths labeled "about", from USDA, extension and USGS sources, kept in a marked data block).
- The idea card flags overlap with size-of-everything (default used: one meter stick down to thousandths; no cosmic zoom, which stays with size-of-everything).
