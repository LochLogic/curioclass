# Expression Escape

## One idea
After closing time the child is locked inside a clockmaker's cluttered workshop, and a note from the clockmaker, Mr. Okafor (made up, labeled "illustration"), says his locks open for anyone who reads his numbers right; grouping locks show an expression and a code (3 + 5 x 2 - 1 and the code 15), and the child drags parentheses (later brackets and braces) until the expression makes the code ((3 + 5) x 2 - 1 = 15), while every wrong placement shows its own value so the child sees what the grouping changed; writing locks play a voice note from Mr. Okafor ("add 8 and 7, then double it") that must be built from tiles as 2 x (8 + 7); reading locks show two drawers, 3 x (18,932 + 921) and 18,932 + 921, and ask which holds three times as many gears, with no calculator and no scratch pad, so the child explains it from the structure; each opened lock gives a gear, and the last door's clock needs every gear to chime; at the end the child sees that grouping symbols change the order of work and that an expression tells a story before it is worked out, so a fifth grader learns to use parentheses, brackets and braces in expressions and evaluate them, and to write simple expressions from words and interpret them without evaluating.

## Not like
- rule-machine (4, spec): number patterns. Here the order of operations.
- expression-garden (6, concept): expressions with letters. Here numbers and grouping.
- expression-match (7, concept): equivalent linear expressions. Here evaluating and reading structure.
- clock-shop (1, spec): telling time with a clock. Here clocks are just the setting.

## Who and how
- Grade 5, Math, module "Expressions and Order of Operations". Standards: 5.OA.1 (use parentheses, brackets, or braces in numerical expressions, and evaluate expressions with these symbols), 5.OA.2 (write simple expressions that record calculations with numbers, and interpret numerical expressions without evaluating them; for example, express the calculation "add 8 and 7, then multiply by 2" as 2 x (8 + 7); recognize that 3 x (18932 + 921) is three times as large as 18932 + 921, without having to calculate the indicated sum or product).
- Format: escape. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three rooms, eight grouping locks, six writing locks, six reading locks, the gear clock. Extra: Team escape (a shared timer and three roles: reader, builder, checker). tool.json `modes: ["Workshop", "Team escape"]`, `minutes: "20-30"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5.OA.1 | Place grouping symbols to make the code; evaluate | each placement's own value | 2 |
| 5.OA.2 (write) | Build an expression from a spoken note | 2 x (8 + 7) in tiles | 3 |
| 5.OA.2 (interpret) | Compare two drawers without computing | the reason card | 4 |

## Screens and modes
Header (kit): title "Expression Escape"; `Workshop`, `Team escape`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A dim clock workshop full of ticking clocks, a locked door, a workbench and a note pinned to it. The welcome is queued (`welcomeAfter: true`): "My locks open for anyone who reads my numbers right. The first dial says 3 + 5 x 2 - 1, and the code is 15. Drag a pair of parentheses onto the dial." First hint: "Drag parentheses onto the dial."

**Grouping locks (focus: the dial).** At 1366x768 the lock fills the middle with the gear tray and the note right; at 680x425 the note is a sheet. The child drags grouping symbols; the dial shows the value of what's there, worked step by step (inside first, then times and divide, then plus and minus). 3 + 5 x 2 - 1 is 12; (3 + 5) x 2 - 1 is 15: open. Later locks use brackets and braces (2 x [3 + (4 x 5)] = 46).

**Writing locks.** A voice note plays; the child builds it from number, sign and grouping tiles. Six notes, from "add 8 and 7, then double it" to "take 4 from 20, then split it into 2 equal parts".

**Reading locks.** Two drawers labeled with expressions. "Which drawer holds three times as many gears?" The child picks a drawer and a reason card ("the same sum, times 3"). No scratch pad and no number pad here.

**The clock (the aha).** The last clock needs every gear. As it chimes Mr. Okafor's note ends: "The symbols tell you the order. And you can read an expression's story before you work it out."

**The end.** The lock log. `Print` prints it.

**Team escape (extra).** A shared timer and three roles.

## Content
- Twenty locks with whole numbers, all readable with `Read`; grouping symbols are parentheses, brackets and braces.
- The workshop is cozy, not scary; the door just needs the code.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Symbols can be moved or removed until the lock is tried.
- Keyboard: Tab to symbol tiles, gaps in the expression, number tiles, drawers and reason cards; Enter places or tries.
- With Motion off locks open at once.

## Look
- Accent `--brand` #6e4b16 clockmaker brass (header, lock faces, buttons); gold #f4c542 (the symbol in hand, an opened lock); paper #f9f4ea; ink #241806; muted #5b554b.
- Contrast (WCAG 2.1, computed): white on brand 7.83:1; brand on paper 7.15:1; ink on paper 15.85:1; muted on paper 6.73:1; ink on gold 10.69:1.
- Never color alone: opened locks show an open shackle and the word "open".
- Different from this batch (campfire red, lab teal, cart blue, garden moss).

## Art
- People (illustrated): Mr. Okafor in a framed photo, labeled "illustration" (Gemini, `people: true`, 1; cutout no).
- Local FLUX (`scripts/localart.py`): three workshop rooms (3, 16:9), the drawers (1, 4:3), the great clock (1, 1:1).
- Drawn in code: dials, tiles, the gear tray.
About 6 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as Mr. Okafor's notes; `knowing-guide` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.room + ':' + state.lock + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `group`: "Drag parentheses onto the dial."
- how `try`: "Tap Try to test the lock."
- how `build`: "Drag tiles to build the note."
- how `read`: "Pick a drawer and a reason."
- event, whole, the clock.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: an expression parser and step-by-step evaluator, the grouping placer, the tile builder, the drawer pairs.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Grouping | Try every placement | Each try shows its value, and locks count tries; later locks have many placements. |
| Writing | Build any expression with the right value | The note's order must match, so 2 x (8 + 7) passes and 30 alone does not. |
| Reading | Compute on paper | The reason card is needed; a computed answer without one doesn't open it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `group`; `try`.
2. `build`.
3. `read`.
4. The clock (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 5.OA.1, 5.OA.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Order of operations is a convention for reading expressions | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Expressions and Equations" | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | yes |
| Reading structure without computing builds algebra readiness | Kieran (2007), "Learning and teaching algebra at the middle school through college levels", Second Handbook of Research on Mathematics Teaching and Learning | Blanton and Kaput (2005), "Characterizing a classroom practice that promotes algebraic reasoning", Journal for Research in Mathematics Education | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s15, 2026-11-10): 3 + 5 x 2 - 1 = 12 and (3 + 5) x 2 - 1 = 15; 2 x (8 + 7) = 30; 2 x [3 + (4 x 5)] = 46; 18,932 + 921 = 19,853 and 3 x 19,853 = 59,559; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 lock, tray and note; at 680x425 note as a sheet.
2. Eight grouping locks are opened with parentheses, brackets or braces. (5.OA.1)
3. Six spoken notes are built as expressions. (5.OA.2)
4. Six reading locks are opened with a reason, without computing. (5.OA.2)
5. `Read` reads every card; every control is 48 px or more.
6. Mr. Okafor is labeled illustration; the workshop is not scary.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: locks open at once; no network requests.

## Open questions
None.
