# Number Path Rescue

## One idea
A river runs past a stepping-stone path laid out as a 1 to 120 chart, some stones have washed away and a duck family waits to cross, so the child taps a blank stone and types its number on a big keypad, and each right stone lets the ducks waddle one step closer; later paths start in the middle (count on from 87) and run past 100, where the tool shows "one hundred one" next to 101 so the child never writes 1001; fish baskets hold up to 120 fish in rows of ten, and the child counts and writes how many to buy a new stone; the river rises gently and can be switched off (calm mode is the default for a first try); at the end a tally shows how the chart's patterns (the stone under 46 is 56, one row down is ten more) let the child fill whole columns fast, so a first grader learns to count to 120 starting at any number, to read and write numerals to 120, and to write the numeral for a counted set of objects.

## Not like
- bead-slider (1, spec): adding tens and ones, same family. Here reading and writing numerals.
- hundred-hop (K, live): counting aloud to 100. Here typing numerals to 120.
- place-value-vault (2, concept): numbers to 1000. Here to 120.
- crayon-boxes (1, concept): tens and ones as bundles. Here the chart's order.

## Who and how
- Grade 1, Math, module "Counting to 120". Standards: 1.NBT.1 (count to 120, starting at any number less than 120; in this range, read and write numerals and represent a number of objects with a written numeral).
- Format: race (calm mode first). Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Eight paths (four starting mid-chart, three crossing 100), four fish baskets, the keypad, the pattern tally. Extra: Ghost race (race your own best run; the river is always optional). tool.json `modes: ["Path", "Ghost race"]`, `minutes: "10-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.NBT.1 (count on) | Fill paths that start mid-chart | the ducks moving stone by stone | 2 |
| 1.NBT.1 (read and write to 120) | Type stones past 100 | "one hundred one" next to 101 | 3 |
| 1.NBT.1 (count a set) | Count fish in rows and write how many | the basket; the typed numeral | 4 |

## Screens and modes
Header (kit): title "Number Path Rescue"; `Path`, `Ghost race`; `Read`, `Motion`, `Sound`, `Print`; a `Calm` switch (on at first). Controls 56 px or more.

**On load and first tap.** A riverbank with stepping stones in twelve rows of ten, a few stones missing. A mother duck and four ducklings wait at stone 1. The welcome is queued (`welcomeAfter: true`): "Some stepping stones washed away! Help the ducks get across. Tap a blank stone." First hint: "Tap a blank stone."

**Rebuilding (focus: the path).** At 1366x768 the chart fills the left two thirds with the keypad on the right; at 680x425 the path scrolls by rows and the keypad slides up from the bottom. The child taps a blank stone and types. Right: the stone rises and the ducks move. Wrong: "Look at the stone before it." The stone before glows.

**Past 100.** A path from 96 to 112. At 101 a card shows "one hundred one" beside the digits 1 0 1. If the child types 1001: "That's one thousand one. One hundred one has three digits."

**Fish baskets.** A basket of fish in rows of ten. "How many fish? Type the number to buy a stone." 47 fish: four full rows and seven.

**The pattern (the aha).** A whole column is missing under 46. The child types 56, 66, 76 fast. The tally: "You used the pattern! One row down is ten more."

**The end.** The ducks across the river and the tally. `Print` prints a blank 120 chart.

**Ghost race (extra).** A faint duck shows the child's best run; the river can rise gently or stay still.

## Content
- A 1 to 120 chart in rows of ten, eight paths, four baskets (47, 63, 108, 120), the 101 card, all spoken. The river only rises to the ducks' feet; the ducks always make it.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Calm` turns the river off at any time.
- Keyboard: Tab to blank stones in order, the keypad, the baskets; number keys type; Enter places.
- With Motion off the ducks jump stone to stone and the river is still.

## Look
- Accent `--brand` #1f5f8b river blue (header, stones, keypad); gold #f4c542 (the stone being typed, the pattern column); paper #eef5fa; ink #0a1c2a; muted #4a5764.
- Contrast (WCAG 2.1, computed): white on brand 6.84:1; brand on paper 6.22:1; ink on paper 15.73:1; muted on paper 6.72:1; ink on gold 10.65:1.
- Never color alone: blank stones are dashed; the pattern column gets arrows.
- Different from this batch (leaf green, bead teal, curtain crimson, factory orange).

## Art
- Local FLUX (`scripts/localart.py`): the riverbank (1, 16:9), the duck family in three poses (wait, waddle, cheer) (3, 1:1), a fish basket (1, 1:1).
- Drawn in code: stones and numbers, the keypad, fish rows, the tally.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `hero-coach` as the mother duck; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.path + ':' + state.stone + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `stone`: "Tap a blank stone."
- how `type`: "Type the number, then tap Enter."
- how `fish`: "Count the fish and type how many."
- event, whole, 101.
- event, whole, the pattern.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
number-path (family "number-path"). Uses the shared pieces from the marked block `/* NUMBER-PATH ENGINE: begin */ ... /* end */` as described in bead-slider's spec: the 1 to 120 path in rows of ten and hidden-number views. Tool-only code: blank stones, the keypad, the river, fish baskets.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Stones | Type any number | Only the right numeral places; the stone before glows. |
| Past 100 | Type 1001 | The 101 card explains and asks again. |
| Baskets | Guess | The fish rows count themselves on a wrong answer, and a new basket follows. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `stone`; `type`.
2. 101 (whole), waits.
3. `fish`.
4. Pattern (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.NBT.1 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Writing 1001 for 101 is a common error from writing numbers as they sound | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | Fuson (1990), "Conceptual structures for multiunit numbers", Cognition and Instruction | yes |
| Timed pressure can raise math anxiety in young children, so a calm option helps | Boaler (2014), "Research suggests that timed tests cause math anxiety", Teaching Children Mathematics | Ramirez and others (2013), "Math anxiety, working memory, and math achievement in early elementary school", Journal of Cognition and Development | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-10): twelve rows of ten make 120; the stone under 46 is 56; 101 to 120 is twenty stones; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 chart and keypad; at 680x425 scrolling rows.
2. Paths starting mid-chart are filled by counting on. (1.NBT.1)
3. Paths past 100 are typed correctly. (1.NBT.1)
4. Four baskets are counted and written. (1.NBT.1)
5. Every card is spoken; every control is 56 px or more.
6. Calm is on at first; the ducks always cross.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps and still river; no network requests.

## Open questions
- The idea card flags overlap with hundred-hop (default used: this tool is about reading and typing numerals to 120 on a river chart; hundred-hop keeps counting aloud to 100 on its own path).
