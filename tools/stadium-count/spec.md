# Stadium Count

## One idea
It's game day, and the view starts on one fan in one seat with a zoom slider and a place-value strip, and each zoom step out holds ten times as many people (one seat, a row of 10, a section of 100, a deck of 1,000, a stadium bowl of 10,000, then a sold-out crowd and a city around it of 100,000), while the strip slides the digit one place left so the child sees the 4 in 4,000 is worth ten times the 4 in 400; the child reads crowd counts in numerals, words and expanded form (45,312 = 40,000 + 5,000 + 300 + 10 + 2), compares two real stadiums' official capacities digit by digit with >, = or < (Michigan Stadium at 107,601 against Ohio Stadium at 102,780), and finds that a city like Green Bay has about as many people as one big stadium holds; a sports news ticker rounds the crowd ("about 45,000 fans", "about 50,000") and the child rounds to the place each headline needs and sees how the story changes; at the end the child's game program lists every crowd in four forms, so a fourth grader learns that a digit is worth ten times what it is worth one place to its right, to read, write and compare multi-digit numbers to a million, and to round them to any place.

## Not like
- zoom-by-tens (5, concept): place value to thousandths on a meter stick. Here whole numbers up to a million in crowds.
- size-of-everything (7-9, live): scientific notation. Here place value.
- place-value-vault (2, spec): numbers to 1,000. Here to a million.
- road-trip-logbook (4, spec): using place value to regroup. Here reading, comparing and rounding.

## Who and how
- Grade 4, Math, module "Place Value to a Million". Standards: 4.NBT.1 (recognize that in a multi-digit whole number, a digit in one place represents ten times what it represents in the place to its right), 4.NBT.2 (read and write multi-digit whole numbers using base-ten numerals, number names, and expanded form; compare two multi-digit numbers based on meanings of the digits in each place, using >, =, and < symbols to record the results of comparisons), 4.NBT.3 (use place value understanding to round multi-digit whole numbers to any place).
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six zoom levels, the place-value strip, eight crowd counts to read and write, six real comparisons, six headlines to round, the game program. Extra: Our town (the child looks up their town's population on a teacher-given card and finds how many stadiums it would fill). tool.json `modes: ["Game day", "Our town"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.NBT.1 | Zoom out a step and watch the digit move | ten times as many seats; the strip shifting | 2 |
| 4.NBT.2 | Write crowds in three forms; compare two capacities | expanded form; the digit-by-digit compare | 3 |
| 4.NBT.3 | Round a crowd for each headline | the number line under the ticker; the rounded headline | 4 |

## Screens and modes
Header (kit): title "Stadium Count"; `Game day`, `Our town`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** One fan in a seat waving a foam finger, a zoom slider and a place-value strip showing 1. The welcome is queued (`welcomeAfter: true`): "One fan. Zoom out, and every step is ten times as many people. Drag the zoom slider." First hint: "Drag the zoom slider."

**Zoom (focus: the crowd).** At 1366x768 the crowd fills the left with the strip and card right; at 680x425 the strip runs across the bottom. Six stops: seat (1), row (10), section (100), deck (1,000), bowl (10,000), crowd and city (100,000). At each stop the strip slides the 1 one place left and a card says "ten times as many as the step before". A second pass with 4 seats shows 4, 40, 400, 4,000.

**Read and write.** Eight crowd counts (45,312, 70,850, 108,001 and others). The child types the number name and builds the expanded form from place tiles.

**Compare.** Real capacities side by side with the year shown: Michigan Stadium (107,601) and Ohio Stadium (102,780). The child compares from the left: hundred thousands equal, ten thousands equal, thousands 7 > 2. Five more pairs.

**Headlines.** A news ticker: "Crowd of about ___". The child rounds 45,312 to the thousand (45,000) and to the ten thousand (50,000) on a number line, and picks which headline is more honest for each story.

**Ten times (the aha).** The 4 in 4,000 and the 4 in 400 light up together. Narrator: "Same digit, one place over, ten times the crowd."

**The end.** The game program. `Print` prints it.

**Our town (extra).** A teacher-given population; how many full stadiums.

## Content
- Six zoom levels (crowds drawn with care; faces not identifiable), eight made-up crowd counts, six real stadium capacities with year and source, one city population, all readable with `Read`.
- Real capacities are official figures from the stadium owners, dated.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The zoom slider snaps to six stops; arrows step it.
- Keyboard: Tab to the slider, the strip, place tiles, sign buttons and the ticker; Enter checks.
- With Motion off zoom jumps between stops.

## Look
- Accent `--brand` #1e4a8a stadium blue (header, the strip, buttons); gold #f4c542 (the moving digit, the foam finger); paper #eef3fa; ink #081a33; muted #4e5767.
- Contrast (WCAG 2.1, computed): white on brand 8.74:1; brand on paper 7.84:1; ink on paper 15.62:1; muted on paper 6.53:1; ink on gold 10.71:1.
- Never color alone: the moving digit is outlined and named ("4 thousands").
- Different from this batch (greenhouse green, workshop copper, test-kitchen pink, sieve purple).

## Art
- Local FLUX (`scripts/localart.py`): six zoom scenes from one seat to a city (6, 16:9), crowds drawn with care and no team logos.
- Drawn in code: the place-value strip, tiles, the ticker and number line.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the stadium announcer; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.zoom + ':' + state.round + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `zoom`: "Drag the zoom slider to the next stop."
- how `write`: "Drag place tiles to build the number."
- how `compare`: "Tap the sign that's true."
- how `round`: "Drag the crowd to the nearest mark, then pick a headline."
- event, whole, ten times.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the zoom levels, the place-value strip, place tiles, the digit-by-digit compare. The rounding line uses `kit/number-line.js` as described in roller-coaster-rounding's spec. Real figures sit in a marked block `/* STADIUMS DATA: begin */ ... /* end */` with sources and years.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Compare | Pick by the first digit only | Pairs share their first digits, so the compare goes place by place. |
| Write | Type digits in any order | Expanded form must match each place. |
| Round | Always round down | Headlines include numbers that round up. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `zoom`.
2. `write`; `compare`.
3. `round`.
4. Ten times (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.NBT.1, 4.NBT.2, 4.NBT.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Michigan Stadium capacity 107,601 | University of Michigan Athletics, "Michigan Stadium" | University of Michigan Bentley Historical Library, "Michigan Stadium" history | yes |
| Ohio Stadium capacity 102,780 | Ohio State University Athletics, "Ohio Stadium" | Ohio State University Libraries, "Ohio Stadium" history | yes |
| Green Bay, Wisconsin, population 107,395 in the 2020 Census | U.S. Census Bureau, "QuickFacts: Green Bay city, Wisconsin" | U.S. Census Bureau, 2020 Census Redistricting Data (P.L. 94-171) | yes |
| A digit is worth ten times the same digit one place right | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2001), "Adding It Up: Helping Children Learn Mathematics" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad s14, 2026-11-10): six zoom stops are 1, 10, 100, 1,000, 10,000 and 100,000; 4,000 is 10 times 400; 45,312 = 40,000 + 5,000 + 300 + 10 + 2, rounding to 45,000 and 50,000; 107,601 > 102,780; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 crowd, strip and card; at 680x425 strip across the bottom.
2. Six zoom steps show each place worth ten times the one to its right. (4.NBT.1)
3. Eight crowds are written three ways; six pairs are compared digit by digit. (4.NBT.2)
4. Six headlines are rounded to the place they need. (4.NBT.3)
5. Real capacities and the city figure show their source and year.
6. Crowds have no identifiable faces and no team logos.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: zoom jumps between stops; no network requests.

## Open questions
- The idea card flags a data source (default used: official capacities from the University of Michigan and Ohio State athletics sites and the 2020 Census for Green Bay, each shown with its year and checked again before build).
- The idea card flags overlap with zoom-by-tens (default used: whole numbers and crowds here, in stadium blue; zoom-by-tens zooms on a meter stick for decimals).
