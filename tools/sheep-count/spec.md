# Sheep Count

## One idea
On a green hill beside an empty pen, Farmer Bo (made up, labeled "illustration") rings a bell and sheep trot in one at a time; the child taps each sheep once as it comes in and it wears the child's number on a tag and bleats, a sheep tapped twice says "Baa, I'm already counted!", and when the gate shuts Bo asks "How many?" and the child picks the last number said from a row of cards; rounds grow from a few sheep in a line to sheep in a circle (the first sheep tapped wears the bell, so you know where you started) to scattered sheep (counted ones sit down), up to 20 in a line and 10 scattered, and then Bo turns it around: "Put 7 sheep in the pen"; at the barn the door closes on 8 sheep, they shuffle inside, the door opens and there are still 8, then one more sheep hops in over a low step and the child can say 9 without counting again, so a kindergartner learns to count to tell the number of objects: one number for each thing, the last number says how many, the count stays the same however things are arranged, each next number is one more, and to count out a given number of things up to 20.

## Not like
- hundred-hop (K, live): saying the counting words to 100. Here each word matches one sheep.
- ten-frame-spillover (K, concept): teen numbers as ten and some more. Here counting one set.
- toy-box-sort (K, spec): sorting first, counting second. Here counting only.
- snack-scale (K, spec): comparing two groups. Here how many in one group.

## Who and how
- Kindergarten, Math, module "How Many?". Standards: K.CC.4 (understand the relationship between numbers and quantities; connect counting to cardinality: (a) say the number names in order, pairing each object with one and only one number name; (b) understand that the last number name said tells the number of objects counted, regardless of arrangement or order; (c) understand that each successive number name refers to a quantity that is one larger), K.CC.5 (count to answer "how many?" questions about as many as 20 things arranged in a line, a rectangular array, or a circle, or as many as 10 things in a scattered configuration; given a number from 1 to 20, count out that many objects).
- Format: showdown (Bo plays the teacher so one child can run every round alone). Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- Twelve rounds (lines, an array, circles, scattered, count-out), two barn rounds, the one-more step. Extra: Class showdown (the class gives thumbs up or down on "still 8?" before the door opens). tool.json `modes: ["Hill", "Class showdown"]`, `minutes: "10-15"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.CC.4a, K.CC.4b | Tap each sheep once, then pick the last number | number tags; "already counted"; the How many card | 2 |
| K.CC.5 | Count lines, an array, circles and scattered sheep, then count out a number | each arrangement; the bell sheep; sitting sheep | 3 |
| K.CC.4b, K.CC.4c | Barn rounds and one more | the door opening on the same count; the one-more sheep | 4 |

## Screens and modes
Header (kit): title "Sheep Count"; `Hill`, `Class showdown`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A green hill with a wooden pen and an open gate. Farmer Bo stands by the gate with a bell. The welcome is queued (`welcomeAfter: true`): "Hello, friend! My sheep are coming home. Tap each sheep one time as it comes in. Tap Start." First hint: "Tap Start."

**Counting (focus: the sheep).** At 1366x768 the hill fills the screen with the number cards along the bottom; at 680x425 the pen is centered and the cards are one row. Each sheep is at least 64 px. Tapping a sheep hangs a tag with the next number and says it aloud. A second tap: "Baa, I'm already counted!" When the gate shuts: "How many sheep?" The child taps a number card. Wrong card: "Let's look at the last tag." The last tag glows.

**Arrangements.** Line rounds (up to 20), an array (rows in the pen), circle rounds (the first sheep tapped gets the bell), scattered rounds (up to 10; counted sheep sit down).

**Count out.** Bo holds up a card: "Put 7 sheep in the pen." The child taps sheep on the hill to send them in one at a time; Bo checks.

**The barn (the aha).** Bo walks 8 sheep into the barn. The door closes; little bleats and shuffles inside. "How many now?" The door opens: the sheep are mixed up, still 8 tags. Then one more sheep hops in over a low step. "Now how many?" The child picks 9. Bo: "One more than 8 is 9. You didn't even have to count!"

**The end.** A picture of the pen with the child's best count. `Print` prints a counting page.

**Class showdown (extra).** The class votes before each barn door opens.

## Content
- Sheep in five arrangements, number tags 1 to 20, number cards 1 to 20, two barn rounds, count-out targets, all spoken. Sheep are never hurt; no wolves.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A tap on a sheep never waits for a voice line.
- Keyboard: Tab to `Start`, each sheep in arrival order, and the number cards; Enter taps.
- With Motion off sheep appear in place instead of trotting.

## Look
- Accent `--brand` #3f6b1f meadow green (header, tags, buttons); gold #f4c542 (the bell, the last tag); paper #f3f8ee; ink #12200a; muted #4e5a47.
- Contrast (WCAG 2.1, computed): white on brand 6.30:1; brand on paper 5.84:1; ink on paper 15.75:1; muted on paper 6.77:1; ink on gold 10.44:1.
- Never color alone: tags carry numbers; the bell sheep wears a bell.
- Different from this batch (zoo orange, playground blue, spy purple, robot red).

## Art
- People (illustrated): Farmer Bo, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the hill and pen (1, 16:9), the barn inside (1, 16:9), a sheep in three poses (walk, stand, sit) (3, 1:1).
- Drawn in code: tags, cards, the bell.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as Farmer Bo; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.count + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `tap`: "Tap the next sheep."
- how `howmany`: "Tap the number card for how many."
- how `countout`: "Tap sheep to send them in."
- event, whole, each number as a sheep is tapped (short, cut off by the next tap).
- event, whole, the barn door.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: arrivals, tags, arrangements, the barn. Rounds sit in a marked block `/* SHEEP-COUNT DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tapping | Tap one sheep many times | "Already counted"; the tag doesn't change. |
| How many | Tap cards until one works | The last tag glows; the round repeats with a new count. |
| Barn | Recount every time | Allowed; Bo still shows that the number didn't change. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `tap`; numbers as tapped.
2. `howmany`.
3. `countout`.
4. Barn door (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for K.CC.4 and K.CC.5 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| One-to-one, cardinality, conservation of number and one-more are the core counting ideas | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K, Counting and Cardinality" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
| A start marker helps children count circles; scattered sets are harder | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K, Counting and Cardinality" | National Research Council (2009), "Mathematics Learning in Early Childhood" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r6, 2026-11-10): 8 sheep stay 8 after the barn; one more than 8 is 9; lines go to 20, scattered to 10; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 hill and cards; at 680x425 one row of cards.
2. Each sheep takes one tag and the last number answers how many. (K.CC.4)
3. Lines to 20, an array, circles and scattered sets to 10 are counted, and a number is counted out. (K.CC.5)
4. Barn rounds keep the count; one more gives the next number. (K.CC.4)
5. Every card is spoken; every control is 64 px or more.
6. Farmer Bo is labeled illustration; no animal is hurt.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: sheep appear in place; no network requests.

## Open questions
None.
