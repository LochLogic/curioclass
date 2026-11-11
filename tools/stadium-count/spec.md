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
- Format: explorer. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): the stadium and the zoom stay. Before, the child dragged the slider and watched the digit move. Now each zoom stop is locked until the child types how many seats it will show, and six "ten times" cards follow, two of them using division. In Read and write the crowds now come in all three forms, so the child also writes the numeral, and says each number aloud before hearing it. A compare needs the deciding place tapped before the sign, and a wrong sign costs the pair. The last two headlines are rounded with no number line. The announcer works one crowd first.
- Six zoom levels with a prediction at each, six "ten times" cards, the place-value strip, eight crowd counts to read and write, six real comparisons, six headlines to round, the game program. Extra: Our town (the child looks up their town's population on a teacher-given card and finds how many stadiums it would fill). tool.json `modes: ["Game day", "Our town"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| 4.NBT.1 | recognize that a digit in one place is ten times what it is in the place to its right | the student | Type the next stop's seat count before the zoom unlocks (two passes); answer six "ten times" cards, two as divisions | 10 predictions and 6 cards | the strip shifting only after the prediction | 2 |
| 4.NBT.2 (read and write) | read and write multi-digit numbers as numerals, number names and expanded form | the student | Given one form, write the other two; say the number aloud, then hear it | 8 (3 start as numerals, 3 as names, 2 as expanded form) | the three forms side by side | 3 |
| 4.NBT.2 (compare) | compare two numbers by the digits in each place; record with >, = or < | the student | Tap the first place where the digits differ, then drag the sign | 6 pairs | the digit-by-digit compare | 4 |
| 4.NBT.3 | round multi-digit whole numbers to any place | the student | Round a crowd for each headline, four on a number line and two with no line, to the hundred, thousand, ten thousand and hundred thousand | 6 | the number line under the ticker; the rounded headline | 5 |

## Screens and modes
Header (kit): title "Stadium Count"; `Game day`, `Our town`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** One fan in a seat waving a foam finger, a zoom slider and a place-value strip showing 1. The welcome is queued (`welcomeAfter: true`): "One fan. Zoom out, and every step is ten times as many people. Drag the zoom slider." First hint: "Drag the zoom slider."

**Zoom (focus: the crowd).** At 1366x768 the crowd fills the left with the strip and card right; at 680x425 the strip runs across the bottom. Six stops: seat (1), row (10), section (100), deck (1,000), bowl (10,000), crowd and city (100,000). The first step, seat to row, is shown by the announcer as the model ("One fan. Ten in a row. The 1 slides one place left."). From then on the slider is locked at each stop until the child types how many seats the next stop holds; the crowd is hidden behind a tunnel until the number is in. A right number opens the zoom, the strip slides the 1 one place left and a card says "ten times as many as the step before". A wrong number shows the row count times ten being built, and the child types again. A second pass with 4 seats asks for 40, 400, 4,000, 40,000 and 400,000 the same way.

**Ten times cards.** Six cards after the zoom, each with a number box or a tap: "The 7 in 700 is how many times the 7 in 70?" (10). "5,000 / 500 = ?" (10). "In 33,000, tap the 3 that is worth ten times the other." (the ten-thousands 3). "80,000 is ten times what number?" (8,000). "700 / 70 = ?" (10). "In 4,600 the 6 is worth 600. Type a number where the 6 is worth ten times that." (any number with 6 in the thousands place, such as 6,000). The last card asks the child to finish the sentence "A digit one place to the left is worth __ times as much."

**Read and write.** The announcer does one first as the model: 23,480, "twenty-three thousand, four hundred eighty", 20,000 + 3,000 + 400 + 80. Then eight crowd counts. Three are given as numerals (the child builds the number name from word tiles and the expanded form from place tiles), three as number names (the child types the numeral and builds the expanded form), and two as expanded form (the child types the numeral and builds the name). The form that is given is the only one on screen. For each, the child says the number aloud, then taps `Hear it` and ticks "I said it that way" or "I'll say it again".

**Compare.** Real capacities side by side with the year shown: Michigan Stadium (107,601) and Ohio Stadium (102,780). The child compares from the left: hundred thousands equal, ten thousands equal, thousands 7 > 2. The child taps the first place where the digits differ, then drags `>`, `=` or `<` between the numbers. A wrong place or a wrong sign can be fixed once; a second miss sets the pair aside and it comes back at the end with its two sides swapped. Five more pairs.

**Headlines.** A news ticker: "Crowd of about ___". The child rounds 45,312 to the thousand (45,000) and to the ten thousand (50,000) on a number line, and picks which headline is more honest for each story. Six headlines in all; the last two have no number line and the rounded number is typed.

**Ten times (the aha).** The 4 in 4,000 and the 4 in 400 light up together. Narrator: "Same digit, one place over, ten times the crowd."

**The end.** The game program. `Print` prints it.

**Our town (extra).** A teacher-given population; how many full stadiums.

## Content
- Six zoom levels (crowds drawn with care; faces not identifiable), six real stadium capacities with year and source, one city population, all readable with `Read`.
- Real capacities are official figures from the stadium owners, dated.
- Crowd counts (made up): as numerals 45,312; 70,850; 108,001. As names: nine thousand, four hundred six (9,406); two hundred thirty thousand, seventy-five (230,075); sixty-one thousand, nineteen (61,019). As expanded form: 500,000 + 300 (500,300); 80,000 + 4,000 + 200 + 60 (84,260).
- Headlines: 45,312 to the thousand (45,000); 45,312 to the ten thousand (50,000); 70,850 to the hundred (70,900); 108,001 to the hundred thousand (100,000); with no line, 61,019 to the thousand (61,000) and 84,260 to the ten thousand (80,000).

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
- how `guess`: "Type how many seats the next stop holds."
- how `write`: "Drag place tiles to build the number."
- how `say`: "Say the number out loud. Then tap Hear it."
- how `compare`: "Tap the first place where the digits differ. Then drag a sign."
- event, whole, the announcer's two examples.
- how `round`: "Drag the crowd to the nearest mark, then pick a headline."
- event, whole, ten times.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the zoom levels, the place-value strip, place tiles, the digit-by-digit compare. The rounding line uses `kit/number-line.js` as described in roller-coaster-rounding's spec. Real figures sit in a marked block `/* STADIUMS DATA: begin */ ... /* end */` with sources and years.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Zoom | Drag the slider and watch | Each stop is locked and the crowd hidden until the next count is typed. |
| Ten times cards | Type 10 every time | Three of the six answers are not 10 (a tapped digit, 8,000, a built number). |
| Write | Copy another form on screen; type digits in any order | Only the given form is on screen; the numeral and the expanded form must each match place by place. Zeros inside 108,001, 9,406 and 230,075 catch digit-by-digit copying of the name. |
| Say it | Tick without saying | The tool cannot hear; the tick is a self-check, and the name is also built from tiles, which is checked. |
| Compare | Pick by the first digit only; guess one of three signs | Pairs share their first digits; the deciding place is tapped first, and a second miss sets the pair aside to come back swapped. |
| Round | Always round down; read the nearest mark | Three of six round up; the last two have no line to read. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). The announcer's first step (whole). `guess`; `zoom`.
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
Checks run again for the spec fix (Python, scratchpad s/fx, 2026-11-10): the second pass is 4, 40, 400, 4,000, 40,000, 400,000; 700 / 70 = 10 and 5,000 / 500 = 10; 80,000 / 10 = 8,000; the eight crowd counts match their names and expanded forms; rounding gives 45,000, 50,000, 70,900, 100,000, 61,000 and 80,000, three up and three down.

## Done when
1. Focus and fold: at 1366x768 crowd, strip and card; at 680x425 strip across the bottom.
2. Ten zoom stops over two passes open only after the child types the count, and six "ten times" cards are answered, two as divisions. (4.NBT.1)
3. Eight crowds are written in the two forms not given, with the given form the only one on screen, and each is said aloud. (4.NBT.2)
4. Six pairs are compared by tapping the deciding place and dragging the sign. (4.NBT.2)
5. Six headlines are rounded to the place they need, two with no number line. (4.NBT.3)
6. Real capacities and the city figure show their source and year.
7. Crowds have no identifiable faces and no team logos.
8. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
9. Motion off: zoom jumps between stops; no network requests.

## Open questions
- The idea card flags a data source (default used: official capacities from the University of Michigan and Ohio State athletics sites and the 2020 Census for Green Bay, each shown with its year and checked again before build).
- The idea card flags overlap with zoom-by-tens (default used: whole numbers and crowds here, in stadium blue; zoom-by-tens zooms on a meter stick for decimals).
