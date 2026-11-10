# Paperclip Ruler

## One idea
In a cartoon classroom with a lab notebook, the child measures things by dragging same-size units end to end (paperclips for a pencil, cubes for a book, shoes for a table) and writes the count, while a helper named Milo (made up, labeled "illustration") measures too and sometimes leaves gaps or lets units overlap, so the child spots the mistake and fixes it (a pencil Milo calls 5 paperclips with gaps is really 6); in order rounds the child lines up scissors, a crayon and a glue stick from longest to shortest and then says which is longer than which without moving them twice; in string rounds the bookshelf and the door can't be moved side by side, so the child stretches a string along one and carries it to the other; in the shoe round Milo's big shoes and a small shoe measure the same table as 9 and 12, and the notebook shows both, so a first grader learns to order three objects by length, to compare two lengths using a third object, and to measure length as a count of same-size units laid end to end with no gaps or overlaps.

## Not like
- who-wins (K, spec): direct comparison, side by side. Here units and a go-between string.
- estimation-station (2, spec): rulers and standard units. Here everyday units first.
- tile-the-floor (3, concept): covering a floor for area. Here length only.
- pizza-party (1, spec): equal shares of a whole. Here equal units along a length.

## Who and how
- Grade 1, Math, module "Measuring Length". Standards: 1.MD.1 (order three objects by length; compare the lengths of two objects indirectly by using a third object), 1.MD.2 (express the length of an object as a whole number of length units, by laying multiple copies of a shorter object (the length unit) end to end; understand that the length measurement of an object is the number of same-size length units that span it with no gaps or overlaps).
- Format: lab. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Ten objects, three units (paperclips, cubes, shoes), six measure rounds, four Milo-mistake rounds, three order rounds, two string rounds, the shoe round. Extra: Real clips (a printable card for measuring real things with real paperclips). tool.json `modes: ["Lab", "Real clips"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.MD.2 | Lay units end to end and count | units snapping; the count in the notebook | 2 |
| 1.MD.2 (gaps and overlaps) | Fix Milo's gaps, overlaps and mixed shoes | gaps glowing; two counts for one table | 3 |
| 1.MD.1 | Order three objects; compare with a string | the line-up; the string carried across | 4 |

## Screens and modes
Header (kit): title "Paperclip Ruler"; `Lab`, `Real clips`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A sunny classroom, a desk with a pencil, a box of paperclips and an open lab notebook. Milo waves with a magnifier. The welcome is queued (`welcomeAfter: true`): "Hi, I'm Milo! Let's measure the pencil with paperclips. Drag paperclips end to end along the pencil." First hint: "Drag a paperclip to the end of the pencil."

**Measuring (focus: the object).** At 1366x768 the object lies across the desk with units in a tray below and the notebook at the right; at 680x425 the notebook is a tab. Units snap end to end when close. When the units reach the end, the child taps the count: "6 paperclips long." The notebook writes it.

**Milo's mistakes.** Milo measures a crayon with gaps between clips. "Milo says 5. Is that right?" The child taps the gap; it glows; the child closes the gaps and gets 6. Another time the clips overlap.

**Order rounds (1.MD.1).** Scissors, a crayon and a glue stick. The child drags them into order from longest to shortest on a line, then answers "Is the scissors longer than the crayon?"

**String rounds (1.MD.1).** The bookshelf and the door are across the room. The child drags a string along the shelf, cuts it, carries it to the door. "The string is longer than the shelf... and shorter than the door!"

**The shoe round (the aha).** Milo measures the table with his big shoes: 9. The child uses a small shoe: 12. The notebook shows both: "Same table, different shoes. Only same-size units make counts you can trust."

**The end.** The lab notebook with every measurement. `Print` prints it and a measuring card.

**Real clips (extra).** A printable list of classroom things to measure with real paperclips.

## Content
- Ten classroom objects with true relative lengths, three units, four Milo mistakes, three order rounds, two string rounds, all spoken. Milo is never laughed at; mistakes are "lab puzzles".

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Units can be dragged off and back at any time.
- Keyboard: Tab to the tray, the object, gaps, the string and the count buttons; Enter places; arrows nudge a unit.
- With Motion off units jump into place and the string appears stretched.

## Look
- Accent `--brand` #26457a notebook navy (header, the notebook, buttons); gold #f4c542 (gaps and overlaps, the unit in hand); paper #f0f3f9; ink #0b1427; muted #4b5466.
- Contrast (WCAG 2.1, computed): white on brand 9.48:1; brand on paper 8.53:1; ink on paper 16.52:1; muted on paper 6.85:1; ink on gold 11.29:1.
- Never color alone: gaps show a dashed outline and the word "gap".
- Different from this batch (tomato red, ballot violet, circuit green, brass brown).

## Art
- People (illustrated): Milo, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the classroom (1, 16:9), ten objects from above (10, 1:1).
- Drawn in code: paperclips, cubes, shoes, the string, the notebook.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Milo; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.object + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `lay`: "Drag a unit to the end of the last one."
- how `count`: "Tap the number of units."
- how `fix`: "Tap a gap or an overlap."
- how `order`: "Drag them from longest to shortest."
- how `string`: "Drag the string along the shelf."
- event, whole, the shoe round.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: unit snapping, gap and overlap checks, the string, the notebook. Objects sit in a marked block `/* PAPERCLIP-RULER DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Measure | Tap any count | The units count aloud and the right count glows. |
| Gaps | Ignore Milo's gaps | The notebook won't take a count with gaps. |
| Order | Drag at random | The line checks each pair and points to the first wrong one. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `lay`; `count`.
2. `fix`.
3. `order`; `string`.
4. Shoe round (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.MD.1, 1.MD.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Gaps, overlaps and mixed units are the common early measuring errors | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | Clements and Sarama, "Learning and Teaching Early Math" (2014) | yes |
| Comparing with a third object (transitivity) belongs in grade 1 | Common Core Standards Writing Team (2012), "Progressions for the CCSS, K-5 Geometric Measurement" | National Council of Teachers of Mathematics, "Principles and Standards", Pre-K to 2 measurement | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r8, 2026-11-10): a 108 unit table is 12 small shoes of 9 and 9 big shoes of 12; an 18 unit pencil is 6 clips of 3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 desk, tray and notebook; at 680x425 notebook tab.
2. Six objects are measured end to end with same-size units. (1.MD.2)
3. Four Milo mistakes and the shoe round are fixed and explained. (1.MD.2)
4. Three order rounds and two string rounds are done. (1.MD.1)
5. Every card is spoken; every control is 56 px or more.
6. Milo is labeled illustration and never mocked.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: jumps; no network requests.

## Open questions
None.
