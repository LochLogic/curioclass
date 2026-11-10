# Ten Frame Spillover

## One idea
On a big green leaf the child taps a jar to drop ladybugs one at a time into a ten frame, and at the tenth ladybug the frame glows "a full ten!" while the next ladybug spills onto a second frame, and as they go the screen builds and says "ten and 4 more, fourteen, 10 + 4 = 14"; in break-apart rounds 16 or 17 ladybugs land scattered on the leaf and the child drags ten into the first frame, the rest hop into the second, and the equation writes itself (10 + 7 = 17); a word strip shows that "four-teen" means four and a ten, while eleven and twelve are the odd names, said plainly; at the end a row of ladybug pictures from 11 to 19 each shows one full ten and some more, so a kindergartner learns to compose and decompose the numbers from 11 to 19 into ten ones and some further ones, and to record each with a drawing and an equation such as 10 + 6 = 16.

## Not like
- crayon-boxes (1, concept): tens and ones to 99 as bundles. Here only 11 to 19.
- sheep-count (K, spec): counting one set. Here a teen number as a ten and some more.
- hundred-hop (K, live): saying the counting sequence. Here what a teen number is made of.
- snack-scale (K, spec): which group has more. Here how one group is built.

## Who and how
- Kindergarten, Math, module "Teen Numbers". Standards: K.NBT.1 (compose and decompose numbers from 11 to 19 into ten ones and some further ones, e.g., by using objects or drawings, and record each composition or decomposition by a drawing or equation (e.g., 18 = 10 + 8); understand that these numbers are composed of ten ones and one, two, three, four, five, six, seven, eight, or nine ones).
- Format: sandbox. Driver: one child with a grown-up nearby (tool.json `driver: "student"`). Every card is spoken. Controls 64 px or more.
- Two ten frames, a ladybug jar, nine fill rounds (11 to 19), four break-apart rounds, the word strip. Extra: Tile builder (the child builds the equation from big number tiles; numerals can be hidden so only words are heard). tool.json `modes: ["Leaf", "Tile builder"]`, `minutes: "10-15"`, `grades_label: "Kindergarten"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| K.NBT.1 (compose) | Drop ladybugs past ten | the full frame; the spill; "ten and 4 more" | 2 |
| K.NBT.1 (decompose) | Drag ten of a scattered set into a frame | the rest in frame two; the equation | 3 |
| K.NBT.1 (record) | Read the equation and the word strip | 10 + 4 = 14; "four-teen" | 4 |

## Screens and modes
Header (kit): title "Ten Frame Spillover"; `Leaf`, `Tile builder`; `Read`, `Motion`, `Sound`, `Print`. Controls 64 px or more.

**On load and first tap.** A big leaf in morning light, two empty ten frames drawn on it, a glass jar full of ladybugs. The welcome is queued (`welcomeAfter: true`): "Hello! Let's fill the leaf with ladybugs. Tap the jar to drop a ladybug." First hint: "Tap the jar."

**Filling (focus: the frames).** At 1366x768 the two frames sit side by side with the jar at the left and the equation strip below; at 680x425 the frames stack and the jar is a button under them. Each tap drops one ladybug into the next square and says its number. At ten the frame glows gold: "A full ten!" The eleventh lands in frame two: "Ten and 1 more, eleven." The strip builds 10 + 1 = 11.

**Break apart.** 16 ladybugs land scattered. "Can you put ten in the first frame?" The child drags ladybugs one at a time; after ten, the rest hop into frame two. "Ten and 6 more. Sixteen. 10 + 6 = 16."

**The word strip (the aha).** Fourteen splits into "four" and "teen" with a ten frame under "teen." "Fourteen is four and a ten!" Then eleven and twelve: "These two have odd names. Eleven is ten and 1. Twelve is ten and 2."

**The end.** A row of ladybug leaves from 11 to 19, each a full ten and some more. `Print` prints it.

**Tile builder (extra).** Big tiles 10, +, =, and 1 to 9. The child builds the equation for the leaf; numerals can be hidden so only the words are said.

## Content
- Two frames of ten squares, nine fill rounds (11 to 19), four break-apart rounds (16, 17, 13, 19), the word strip, all spoken. Ladybugs only walk and hop.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A `Take one back` button lifts the last ladybug off.
- Keyboard: Tab to the jar, each ladybug in a scattered set, each frame and the tiles; Enter drops or places.
- With Motion off ladybugs appear in squares and the spill is a jump.

## Look
- Accent `--brand` #2f6b2a leaf green (header, frames, buttons); gold #f4c542 (the full-ten glow, the ladybug in hand); paper #f2f8ef; ink #0e1f0c; muted #4b5a48.
- Contrast (WCAG 2.1, computed): white on brand 6.45:1; brand on paper 5.97:1; ink on paper 15.94:1; muted on paper 6.81:1; ink on gold 10.58:1.
- Never color alone: the full frame also gets the words "full ten" and a ring.
- Different from this batch (bead teal, curtain crimson, river blue, factory orange).

## Art
- Local FLUX (`scripts/localart.py`): the leaf in morning light (1, 16:9), a ladybug in three poses (walk, hop, sit) (3, 1:1), the jar (1, 1:1).
- Drawn in code: frames, the equation strip, the word strip, tiles.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator; `warm-teacher` as the hints and counts. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.count + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `drop`: "Tap the jar."
- how `drag`: "Drag a ladybug into the first frame."
- how `tiles`: "Drag a tile to build the equation."
- event, whole, each count (short, cut off by the next tap).
- event, whole, the full ten.
- event, whole, the word strip.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
ten-frame (family "ten-frame"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* TEN-FRAME ENGINE: begin */ ... /* end */`: a ten frame that fills in order, the spill to a second frame, drag-to-frame with a ten-check, and the equation strip; later ten-frame tools reuse them.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fill | Tap the jar fast | Each tap says its number; the round ends on its target. |
| Break apart | Drag all into frame one | Frame one holds ten; the eleventh hops to frame two. |
| Tiles | Try tiles at random | Only true equations lock; the leaf shows the count. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `drop`; counts.
2. Full ten (whole), waits.
3. `drag`.
4. Word strip (whole), waits. `tiles`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for K.NBT.1 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Ten frames help children see teen numbers as ten and some ones | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
| English teen names (eleven, twelve) hide the ten, which makes them hard | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2009), "Mathematics Learning in Early Childhood" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-10): every number 11 to 19 is 10 and 1 to 9 more; 10 + 4 = 14; 16 and 17 break into 10 + 6 and 10 + 7; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 frames side by side; at 680x425 stacked.
2. Nine fill rounds build 11 to 19 with the spill. (K.NBT.1)
3. Four scattered sets are broken into ten and the rest. (K.NBT.1)
4. Each round shows an equation, and the word strip names the ten. (K.NBT.1)
5. Every card is spoken; every control is 64 px or more.
6. Ladybugs are never hurt; nothing is squashed.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
