# Crayon Boxes

## One idea
Over one school week the child runs the supply closet with Mr. Okafor the custodian (made up, labeled "illustration"): on Monday a heap of loose crayons gets packed into boxes of ten, each box closing with a click at ten, and the shelf label updates as "3 boxes and 4 loose, 34"; each day orders arrive ("Table 2 needs 46") and the child sends whole boxes and loose crayons, opening a box into ten loose ones when needed; Wednesday is "a box and some more" day (11 to 19) and Thursday is full-box day (30 is 3 boxes and 0 loose); on Friday two classrooms' shelves sit side by side (52 and 47), and the child compares boxes first, then loose, and picks the sign >, = or <, finding that 52 wins because it has more boxes even though 7 loose is more than 2, so a first grader learns that the two digits of a two-digit number stand for tens and ones, that 10 is a bundle of ten ones, that 11 to 19 are a ten and some ones, that 10, 20, 30 up to 90 are tens with no ones, and to compare two two-digit numbers by their tens and ones, writing the result with >, = and <.

## Not like
- ten-frame-spillover (K, spec): teen numbers only, as ladybugs in frames. Here tens and ones to 99.
- place-value-vault (2, spec): hundreds, same family. Here tens and ones.
- bead-slider (1, spec): adding with tens and ones. Here what the digits mean and comparing.
- snack-scale (K, spec): more and less by matching. Here comparing by place value.

## Who and how
- Grade 1, Math, module "Tens and Ones". Standards: 1.NBT.2 (understand that the two digits of a two-digit number represent amounts of tens and ones; understand the following as special cases: (a) 10 can be thought of as a bundle of ten ones, called a "ten"; (b) the numbers from 11 to 19 are composed of a ten and one, two, three, four, five, six, seven, eight, or nine ones; (c) the numbers 10, 20, 30, 40, 50, 60, 70, 80, 90 refer to one, two, three, four, five, six, seven, eight, or nine tens (and 0 ones)), 1.NBT.3 (compare two two-digit numbers based on meanings of the tens and ones digits, recording the results of comparisons with the symbols >, =, and <).
- Format: tycoon (a five-day week, no money, no losing). Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Five days, twelve orders, a box-opening tool, two special days, four Friday compares. Extra: Teacher orders (the teacher types custom orders). tool.json `modes: ["Closet", "Teacher orders"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.NBT.2a, 1.NBT.2b | Pack loose crayons into boxes of ten; fill teen orders | a box closing at ten; "a box and 4 more" | 2 |
| 1.NBT.2, 1.NBT.2c | Fill orders as boxes and loose; full-box day | the shelf label; 30 as 3 boxes and 0 loose | 3 |
| 1.NBT.3 | Compare two shelves, boxes first | the two shelves; the sign | 4 |

## Screens and modes
Header (kit): title "Crayon Boxes"; `Closet`, `Teacher orders`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A cozy supply closet, a heap of loose crayons on the table, a stack of empty boxes that each hold ten, and Mr. Okafor with a clipboard. The welcome is queued (`welcomeAfter: true`): "Morning! It's Monday, and these crayons are a mess. Let's pack them in boxes of ten. Drag a crayon into a box." First hint: "Drag a crayon into a box."

**Packing (focus: the table).** At 1366x768 the heap is center, boxes at the left, the shelf and its label at the right; at 680x425 the shelf is a strip along the top. Each crayon slides into a slot; at ten the lid clicks shut. The shelf label reads boxes and loose with the number: "3 boxes and 4 loose. 34."

**Orders.** A note slides under the door: "Table 2 needs 46." The child drags boxes and loose crayons into the order tray. If there aren't enough loose, `Open a box` breaks one into ten loose.

**Special days.** Wednesday: "a box and some more" orders from 11 to 19. Thursday: full-box orders (30, 50, 90) with no loose crayons.

**Friday check (the aha).** Two classroom shelves side by side: 52 and 47. "Which has more? Look at the boxes first." Five boxes beat four. The child picks >, = or <. Mr. Okafor: "7 loose is more than 2, but boxes count first. 52 is more than 47."

**The end.** The week's log. `Print` prints a packing page.

**Teacher orders (extra).** The teacher types orders; nothing leaves the device.

## Content
- Crayons in many colors, boxes of ten, twelve orders, two special days, four compares (52 vs 47, 38 vs 83, 60 vs 59, 24 vs 24), all spoken. Nothing breaks; no money.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Open a box` and `Undo` work at any time.
- Keyboard: Tab to the heap, boxes, the order tray, `Open a box` and the sign buttons; Enter picks up and drops; B sends a box, L sends a loose crayon.
- With Motion off crayons jump into slots and lids shut without swinging.

## Look
- Accent `--brand` #1d5c7a closet blue (header, the shelf label, buttons); gold #f4c542 (a closed box, the crayon in hand); paper #eef5f8; ink #081c26; muted #485760.
- Contrast (WCAG 2.1, computed): white on brand 7.33:1; brand on paper 6.65:1; ink on paper 15.82:1; muted on paper 6.79:1; ink on gold 10.72:1.
- Never color alone: boxes show ten slots and the word "ten"; crayon colors carry no meaning.
- Different from this batch (gym red, park green, court orange, vault indigo).

## Art
- People (illustrated): Mr. Okafor, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the supply closet (1, 16:9), two classroom shelves (1, 16:9).
- Drawn in code: crayons, boxes, the label, the order tray, signs.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as Mr. Okafor; `warm-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.day + ':' + state.order + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pack`: "Drag a crayon into a box."
- how `order`: "Drag boxes and loose crayons into the tray."
- how `open`: "Tap Open a box for ten loose ones."
- how `compare`: "Tap the sign that fits."
- event, whole, each box closing (short).
- event, whole, Friday check.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
base-ten (family "base-ten"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* BASE-TEN ENGINE: begin */ ... /* end */`: bundles of ten that close and open, a units-and-tens label that reads digits and words, and a compare-by-place view; place-value-vault reuses them and adds hundreds.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Orders | Send only loose crayons | Allowed, but the tray counts slowly and Mr. Okafor asks for boxes next order. |
| Compare | Pick a sign at random | The shelves line up boxes and loose to show which is more. |
| Full box | Send 3 loose for 30 | The label reads 3, not 30. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pack`.
2. `order`; `open`.
3. Special days.
4. Friday check (whole), waits. `compare`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.NBT.2, 1.NBT.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Bundling ten ones into a ten is the base of place value | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | Fuson (1990), "Conceptual structures for multiunit numbers", Cognition and Instruction | yes |
| Comparing two-digit numbers by tens first | Common Core Standards Writing Team (2015), "Progressions for the CCSS, K-5 Number and Operations in Base Ten" | National Research Council (2001), "Adding It Up" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-10): 34 is 3 tens and 4; 46 is 4 tens and 6; 30 is 3 tens and 0; 52 beats 47 on tens though its ones are smaller; every teen has one ten; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 heap, boxes and shelf; at 680x425 shelf strip.
2. Crayons are packed into tens and teen orders are filled. (1.NBT.2)
3. Twelve orders go out as boxes and loose, including full-box day. (1.NBT.2)
4. Four Friday compares use >, = and <. (1.NBT.3)
5. Every card is spoken; every control is 56 px or more.
6. Mr. Okafor is labeled illustration; no money or losing.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
