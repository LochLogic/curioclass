# Multiplication Dungeon

## One idea
A hero with a lantern explores a friendly pixel-art castle where every door shows a multiplication or division fact (7 x 8, 56 / 7), and the child types the answer to open it; floors follow strategy families (2s, 5s and 10s, then 3s, 4s and 6s, then 7s, 8s and 9s), and a missed fact never ends the run: it comes back a few doors later as a big, sleepy guardian who dozes off when the fact is answered, each time with a strategy hint card (an array split, 7 x 8 = 5 x 8 + 2 x 8; a known neighbor, 7 x 7 + 7; or the matching multiplication for a division), and the gap between returns grows as the fact sticks; a castle map of all 100 products lights a tile for each fact the child has answered on three separate visits, with each division door lighting the same tile as its multiplication, and the child notices that 7 x 8 and 8 x 7 light the same pair, so 100 tiles are really 55 facts to learn; at the end the whole map glows, so a third grader learns to multiply and divide within 100 fluently, using strategies and the link between multiplication and division, toward knowing all products of two one-digit numbers from memory.

## Not like
- fact-rally (2, spec): addition facts on a tennis court with rally repeats. Here times facts with guardians on later floors.
- equal-groups-zoo (3, spec): what multiplication means. Here knowing the facts.
- pattern-painter (3, spec): patterns in the times table. Here recalling each fact.
- area-model-builder (4, concept): splitting big products. Here one-digit facts.

## Who and how
- Grade 3, Math, module "Times Tables Fluency". Standards: 3.OA.7 (fluently multiply and divide within 100, using strategies such as the relationship between multiplication and division or properties of operations; by the end of grade 3, know from memory all products of two one-digit numbers).
- Format: arcade. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three floors of strategy families, about 30 doors per floor, returning guardians with hint cards, the 100-tile product map. Extra: Daily run (a three-minute run with a personal best, kept on the device). tool.json `modes: ["Dungeon", "Daily run"]`, `minutes: "10-20"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.OA.7 (strategies) | Answer a returning guardian after its hint card | the array split or neighbor fact | 2 |
| 3.OA.7 (multiply and divide) | Open division doors with the matching multiplication | the shared tile on the map | 3 |
| 3.OA.7 (from memory) | Answer each fact on three separate visits | the map tile lighting | 4 |

## Screens and modes
Header (kit): title "Multiplication Dungeon"; `Dungeon`, `Daily run`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A pixel-art castle gate at night and a small hero with a lantern. The welcome is queued (`welcomeAfter: true`): "Each door has a fact. Answer it to open the door. Type the answer and tap Open." First hint: "Type the answer, then tap Open."

**Doors (focus: the door).** At 1366x768 the corridor fills the left with the number pad and the mini map right; at 680x425 the map is a tab. A door shows one fact; a right answer swings it open and the hero walks on. No countdown: the door waits as long as needed.

**Guardians.** A missed fact shows its answer, then returns two doors later as a big sleepy guardian (a dragon in slippers, a yawning knight) holding a hint card. Each correct answer pushes its next return farther (2, then 4, then 8 doors). Guardians never fight: they nod off with a snore.

**Floors.** Floor 1: 2s, 5s and 10s. Floor 2: 3s, 4s and 6s. Floor 3: 7s, 8s and 9s. Each floor opens with a strategy card (doubles for 4s, 10s minus one group for 9s).

**The castle map (the aha).** A 10 by 10 product map. A tile lights after three separate right answers. Division doors light the multiplication tile they belong to. When 8 x 7 lights next to 7 x 8 the narrator says: "Same pair, same answer. You don't have 100 facts to learn. You have 55."

**The end.** The glowing map with the facts still to practice listed. `Print` prints the map and the list.

**Daily run (extra).** Three minutes of doors with a personal best kept on the device, said on screen.

## Content
- Facts 1 x 1 to 10 x 10 and their divisions, hint cards for every fact, about 90 doors, ten guardian sprites, all readable with `Read`.
- Guardians are cozy and never hurt; nothing dies.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The number pad and the keyboard both type answers; Enter opens.
- Keyboard: Tab to the answer box, Open, the hint card and the map; arrows move over map tiles, and each tile reads its fact.
- With Motion off doors open at once and the hero appears at the next door.

## Look
- Accent `--brand` #4b2d7f dungeon violet (header, door frames, the map); gold #f4c542 (the lantern, a lit tile); paper #f3f0fa; ink #170c2b; muted #575266.
- Contrast (WCAG 2.1, computed): white on brand 10.60:1; brand on paper 9.42:1; ink on paper 16.60:1; muted on paper 6.65:1; ink on gold 11.49:1.
- Never color alone: lit tiles show the product; facts to practice carry a dot and are listed.
- Different from this batch (tomato red, kitchen-tile blue, highway green, soil brown).

## Art
- Drawn in code: a hand-made pixel set (the gate, three floors of corridor, the hero, ten guardians, doors, the map), made with care as the tool's look.
No generated images; the pixel set is checked against rule 3 like any art.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the castle herald; `playful-friend` as the hero's lantern and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.floor + ':' + state.door + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `door`: "Type the answer, then tap Open."
- how `hint`: "Read the hint card, then type the answer."
- event, whole, each floor's strategy card.
- event, whole, the 55 facts line.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the fact scheduler (returns at 2, 4 and 8 doors), the pixel renderer, the 10 by 10 map with three-visit lighting. Hint cards sit in a marked block `/* FACT HINTS DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Map | Answer one fact many times in a row | A tile lights only after three answers on separate visits with other doors between. |
| Division | Skip division doors | Each floor needs its division doors to open the stairs. |
| Guessing | Type numbers until one works | A wrong answer shows the right one and brings the fact back as a guardian. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Floor 1 strategy card (whole), waits.
2. `door`; `hint`.
3. The 55 facts line (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.OA.7 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Fluency grows from strategies, not memorizing alone | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Baroody (2006), "Why children have difficulties mastering the basic number combinations", Teaching Children Mathematics | yes |
| Spaced returns help recall last | Cepeda and others (2006), "Distributed practice in verbal recall tasks", Psychological Bulletin | Roediger and Karpicke (2006), "Test-enhanced learning", Psychological Science | yes |
| Timed fact tests can raise math anxiety, so doors wait | Boaler (2014), "Research suggests that timed tests cause math anxiety", Teaching Children Mathematics | Ramirez and others (2013), "Math anxiety, working memory, and math achievement in early elementary school", Journal of Cognition and Development | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s12, 2026-11-10): 7 x 8 = 5 x 8 + 2 x 8 = 7 x 7 + 7 = 56; the 10 by 10 map has 100 tiles and 55 different pairs when order does not matter; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 corridor, pad and map; at 680x425 map as a tab.
2. Missed facts return as guardians with a strategy hint, at growing gaps. (3.OA.7)
3. Division doors light the matching multiplication tile. (3.OA.7)
4. A tile lights only after three separate right answers; the map can fill. (3.OA.7)
5. No door has a countdown; the repeat is visibly different from fact-rally's.
6. Nothing is hurt; guardians fall asleep.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: doors open at once; no network requests.

## Open questions
- The idea card flags overlap with fact-rally (default used: missed facts return as guardians on later doors at 2, 4 and 8 door gaps with a hint card and a product map; fact-rally keeps rally-spaced repeats on a court).
