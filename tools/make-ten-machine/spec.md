# Make Ten Machine

## One idea
In a bright toy factory, facts roll in on a conveyor as trays of counters in two ten frames, and the child uses machine attachments to turn a hard fact into an easy one before tapping the answer: for 8 + 5 the child slides 2 counters across to fill the 8 to ten, the tray now reads 10 + 3 and 13 is easy; each level unlocks one attachment (the Flipper turns 3 + 9 into 9 + 3, the Grouper adds the pair that makes ten first in 4 + 6 + 3, Break ten turns 13 - 4 into 13 - 3 - 1, the Doubles mirror shows 6 + 7 as 6 + 6 + 1, and Think addition turns 12 - 8 into 8 + ? = 12 and shows the four-fact family card); at the end the same fact solved three ways comes out of the machine as one answer, and the machine shows the child's fastest route, so a first grader learns to use properties of operations (order and grouping) as strategies, to see subtraction as an unknown-addend problem, to add and subtract within 20 with strategies such as counting on, making ten, breaking ten and doubles, and to add and subtract within 10 fluently.

## Not like
- fact-rally (2, concept): speed recall of facts. Here building strategies step by step with counters.
- balance-the-beam (1, concept): what the equal sign means. Here how to make a fact easy.
- story-replay (1, spec): choosing a sentence for a story. Here solving bare facts.
- ten-frame-spillover (K, spec): teen numbers as ten and some more. Here using ten to add.

## Who and how
- Grade 1, Math, module "Fact Strategies". Standards: 1.OA.3 (apply properties of operations as strategies to add and subtract; e.g., if 8 + 3 = 11 is known, then 3 + 8 = 11 is also known; to add 2 + 6 + 4, the second two numbers can be added to make a ten), 1.OA.4 (understand subtraction as an unknown-addend problem), 1.OA.5 (relate counting to addition and subtraction), 1.OA.6 (add and subtract within 20, demonstrating fluency for addition and subtraction within 10; use strategies such as counting on; making ten; decomposing a number leading to a ten; using the relationship between addition and subtraction; and creating equivalent but easier or known sums).
- Format: puzzle. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Two ten frames on each tray, five attachments over five levels, 30 facts within 20, the fact family card, the three-ways finale. Extra: Quick lane (facts within 10 only, no timer). tool.json `modes: ["Factory", "Quick lane"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.OA.3 | Use the Flipper and the Grouper | 3 + 9 becoming 9 + 3; the ten made first | 2 |
| 1.OA.4 | Use Think addition | 12 - 8 as 8 + ? = 12; the fact family card | 3 |
| 1.OA.5, 1.OA.6 | Make ten, break ten, doubles, counting on; the quick lane | counters sliding; the new easy fact | 4 |

## Screens and modes
Header (kit): title "Make Ten Machine"; `Factory`, `Quick lane`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A toy factory with a conveyor, one big lever and a foreman bear in a hard hat. A tray with 8 and 5 counters rolls in. The welcome is queued (`welcomeAfter: true`): "Welcome to the factory! Hard facts come in. We make them easy. Slide counters to fill the first frame." First hint: "Drag a counter into the first frame."

**A tray (focus: the frames).** At 1366x768 the tray sits center with attachments along the top and answer buttons below; at 680x425 the attachments become a row of icons. After the slide, the label changes: 8 + 5 becomes 10 + 3. Three answer buttons; the right one sends the tray off with a toot.

**Attachments.** Level by level: the Flipper (tap to swap the frames), the Grouper (pick which two of three to add first), Break ten (13 - 4: take 3 to reach ten, then 1 more), the Doubles mirror (6 + 7 shows 6 + 6 and one extra), Think addition (12 - 8 shows 8 + ? = 12 and the counters fill up to 12). The fact family card shows 4 + 8, 8 + 4, 12 - 8, 12 - 4.

**Three ways (the aha).** 6 + 7 comes in. The child solves it with make ten, then doubles, then counting on. Three trays, one answer, 13. The foreman: "Three ways, one answer! Your fastest way was doubles."

**The end.** The machine's board with each attachment the child used. `Print` prints a strategy card.

**Quick lane (extra).** Facts within 10 roll by with no timer.

## Content
- 30 facts within 20 sorted by strategy, five attachments, fact family cards, the three-ways finale, all spoken. The machine never breaks or explodes; a wrong answer just sends the tray around again.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Counters can be slid back before answering.
- Keyboard: Tab to counters, attachments and answers; arrows move a counter; Enter picks.
- With Motion off the conveyor steps instead of rolling and counters jump.

## Look
- Accent `--brand` #9a4300 factory orange (header, the conveyor frame, buttons); gold #f4c542 (the counter in hand, the full ten); paper #fdf4ec; ink #2a1300; muted #5e5046.
- Contrast (WCAG 2.1, computed): white on brand 6.61:1; brand on paper 6.08:1; ink on paper 16.22:1; muted on paper 7.13:1; ink on gold 10.84:1.
- Never color alone: the two addends use filled and ringed counters, not two colors.
- Different from this batch (leaf green, bead teal, curtain crimson, river blue).

## Art
- Local FLUX (`scripts/localart.py`): the toy factory (1, 16:9), the foreman bear in three poses (point, cheer, think) (3, 1:1), five attachment icons (5, 1:1).
- Drawn in code: trays, ten frames, counters, cards.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `friendly-dad` as the foreman bear; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.fact + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `slide`: "Drag a counter to make ten."
- how `tool`: "Tap the attachment to change the fact."
- how `answer`: "Tap the answer."
- event, whole, each new attachment.
- event, whole, three ways.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: trays, attachments, fact family cards. It may reuse the ten frame drawing from `/* TEN-FRAME ENGINE: begin */ ... /* end */` as described in ten-frame-spillover's spec. Facts sit in a marked block `/* MAKE-TEN DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Answer | Tap answers until one works | A wrong tray loops back with the attachment glowing. |
| Attachment | Skip it and count all | Allowed, but levels unlock only after the attachment is used. |
| Three ways | Use one way three times | Each tray locks the way used before. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `slide`; `answer`.
2. New attachment (whole), waits. `tool`.
3. Three ways (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.OA.3 to 1.OA.6 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Make ten, doubles and think addition are the main derived-fact strategies in grade 1 | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Baroody (2006), "Why children have difficulties mastering the basic number combinations", Teaching Children Mathematics | yes |
| Building strategies leads to fluency better than timed drill alone | National Research Council (2001), "Adding It Up" | Baroody (2006), "Why children have difficulties mastering the basic number combinations", Teaching Children Mathematics | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-10): 8 + 5 = 10 + 3 = 13; 3 + 9 = 9 + 3 = 12; 4 + 6 + 3 = 13; 13 - 4 = 13 - 3 - 1 = 9; 6 + 7 = 6 + 6 + 1 = 13; 12 - 8 = 4 and its family of four; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 tray and attachments; at 680x425 icon row.
2. The Flipper and the Grouper are used on real facts. (1.OA.3)
3. Think addition solves subtraction and fact family cards show four facts. (1.OA.4)
4. Make ten, break ten, doubles and counting on solve 30 facts, and the quick lane covers facts within 10. (1.OA.5, 1.OA.6)
5. Every card is spoken; every control is 56 px or more.
6. No timer anywhere; the machine never breaks.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: steps and jumps; no network requests.

## Open questions
- The idea card flags overlap with fact-rally (default used: this tool builds each strategy step by step with counters and no timer; fact-rally keeps speed).
