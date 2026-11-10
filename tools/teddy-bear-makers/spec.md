# Teddy Bear Makers

## One idea
In Mrs. Haddad's small bear workshop the child puts seven step cards in order on an empty line, gives each step its tool or machine and the worker with the right skill, and watches one bear travel down the line while each step adds its cost to a price tag (a wrong order makes a funny bear, like stuffing that falls out of fur that isn't sewn yet); then the child asks Mrs. Haddad questions and answers a visiting kid's questions from their own line, so a first grader learns that making a thing takes steps, tools, skilled people and money, and can explain it in order.

## Not like
- paper-plane-assembly-line (3, concept): splitting work and counting how many planes come out. Here one bear's steps, tools, skills and cost.
- market-day (1, spec, this batch): buying and trading. Here making.
- community-helpers-village (1, spec, this batch): who does what job for a town. Here the steps of one product.
- compass-rose-quest (1, spec, this batch): steps across a map. Here steps in order on a line, each with a cost.
- capsule-from-1965 (1, spec, this batch): reading old sources. Here explaining a process you built.

## Who and how
- Grade 1, Social Studies (Economics), module "Teddy Bear Makers". Standards: D2.Eco.7.K-2 (describe examples of costs of production), D2.Eco.13.K-2 (describe examples of capital goods and human capital), D4.2.K-2 (construct an explanation of an event or process), D4.5.K-2 (ask and answer questions about explanations).
- Driver: teacher on the projector with the class calling the next step, or one child alone; every card, tool, worker and button is spoken (tool.json `driver: "either"`). Controls 56 px or more.
- Three parts: Build the line, Ask Mrs. Haddad, Visitor's questions. tool.json `modes: ["Build the line", "Ask the maker", "Visitor"]`, `minutes: "15-25"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D4.2.K-2 | Put seven step cards in order and run one bear down the line | the line, the bear changing at each step, a funny result for a wrong order | 2, 3 |
| D2.Eco.13.K-2 | Drag the tool or machine and the worker with the right skill to each step | the step slot filling with a tool picture and a worker picture, labeled "Machine" and "Skill" | 4 |
| D2.Eco.7.K-2 | Watch each step add its cost to the price tag | the tag growing to 12 dollars, each cost a picture and a number | 5 |
| D4.5.K-2 | Ask Mrs. Haddad three questions, then answer the visitor's three by tapping the right part of your own line | the question and the lit step that answers it | 6, 7 |

## Screens and modes
Header (kit): title "Teddy Bear Makers"; `Build the line`, `Ask the maker`, `Visitor`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A bright workshop. Mrs. Haddad waves from behind a table piled with seven step cards. An empty line of seven slots runs across the floor, a price tag hangs at its end showing 0 dollars. The welcome is queued (`welcomeAfter: true`): "Welcome to my bear workshop! I need help setting up my line. Which step comes first? Tap a card to hear it." First hint: "Tap a card to hear it. Then drag it to the first slot." The first tap reads that card and cuts the welcome.

**Build the line (focus: the line of slots).** At 1366x768 the line runs across the middle; cards sit above it; tools and workers sit in two trays below (shown after the order is set); the price tag is at the right end. At 680x425 the trays become `Tools` and `Workers` buttons that open a tray.
- Step cards (pictures plus words): Cut the fur; Sew the pieces; Put in the eyes; Stuff the bear; Sew it closed; Check it; Put it in a box.
- The child drags cards into slots in any order and taps `Run a bear`. One bear moves down the line and each step plays. A wrong order plays its funny result and stops there:
  - Stuff before sew: "The stuffing fell right through the pieces!"
  - Eyes before sewing: "Where do the eyes go? There's no face yet!"
  - Eyes after stuff or after closing: "I can't reach inside to lock the eyes now!"
  - Close before stuff: "A flat bear! It's all sewn up with nothing inside."
  - Check before close or box before check: "We can't check a bear that isn't done."
  - Cut not first: "There are no pieces to sew yet!"
  The child moves cards and runs again. A full right run gives a finished bear in its box.
- Then the trays open. For each step the child drags one tool or machine and one worker:
  - Cut the fur: big scissors and a pattern; Omar the cutter (knows how to read a pattern).
  - Sew the pieces: sewing machine; Bea the sewer (trained on the machine).
  - Put in the eyes: safety eyes and an eye press; Bea.
  - Stuff the bear: stuffing machine; Ray the stuffer.
  - Sew it closed: needle and thread; Bea.
  - Check it: pull tester; Mrs. Haddad (knows the safety rules).
  - Put it in a box: boxes and tape; Ray.
  A wrong tool or worker is turned back with a reason ("Ray hasn't learned the sewing machine yet."). Tools and machines get a "Machine or tool" tag; workers' skills get a "Skill" tag. Mrs. Haddad: "Machines and tools help us work. Skills are what people learn to do the work."
- The price tag: each step's run adds its cost with a picture: fur 3 dollars, stuffing 2, eyes 1, workers' pay 4, machines and power 2. Total 12 dollars. Mrs. Haddad: "So one bear costs me 12 dollars to make."
- `Faster?` (after the tag shows 12): the child picks one change: a new stuffing machine, or teaching Ray to sew. Either makes the line run faster on screen, and Mrs. Haddad says why ("A better machine" / "Now two people can sew").

**Ask the maker (focus: Mrs. Haddad and a row of question bubbles).** Six picture question bubbles; the child picks three:
- "Why do you need a machine for stuffing?"
- "How do you learn to sew bears?"
- "Why do the eyes go in before stuffing?"
- "What costs the most?"
- "Why do you check every bear?"
- "Why are they called teddy bears?"
Each answer is spoken and lights the step it is about.

**Visitor (focus: the line and a visiting kid, Theo).** Theo asks three questions in turn. The child answers by tapping the right part of their own line (a step, a tool, a worker or the price tag):
- "What happens right after you sew the pieces?" (Put in the eyes)
- "Who checks the bears?" (Mrs. Haddad)
- "How much does one bear cost to make?" (the price tag)
A right tap: Theo nods and repeats it in his words. A wrong tap: "Hmm, is that right after sewing? Look at your line." After three: Theo says "Now I know how bears are made!" and `Print` prints the line in order with tools, workers and the tag.

## Content
- Seven steps, seven tool or machine pictures, four workers (Omar, Bea, Ray, Mrs. Haddad), five costs summing to 12, six wrong-order results, six maker questions, three visitor questions. All fictional; no bear brand.

## Interactions in detail
- Every tap acts at once; a new line stops the old one; dragging a card during a run stops the run.
- `Run a bear` shows when all seven slots hold cards. The trays and `Faster?` show only after the line is right and after the tag shows 12; the hint names the next step instead.
- Keyboard: Tab to a card, Enter to pick it up, arrow keys to a slot, Enter to drop.
- With Motion off the bear jumps step to step and the funny result shows as a still picture.

## Look
- Accent `--brand` #9d174d workshop raspberry (header, slot frames, the tag string); gold #f4c542 (the lit step, the running bear's ring, the total); paper #fcf0f5; ink #2d0616; muted #6a5059.
- Contrast (WCAG 2.1, computed): white on brand 7.88:1; brand on paper 7.10:1; ink on paper 16.46:1; muted on paper 6.51:1; ink on gold 11.24:1.
- Never color alone: tags carry the words "Machine or tool" and "Skill"; wrong results carry a picture and a line.
- Different from this batch (brick orange, market teal, map navy, capsule slate).

## Art
- People art goes to Gemini with `people: true`: Mrs. Haddad (5 poses: waving, pointing, holding a bear, pulling the tester, thinking; 1:1; cutout yes); Omar, Bea and Ray (3 poses each: working, waiting, smiling; cutout yes); Theo (3 poses: asking, nodding, cheering; cutout yes).
- Local FLUX (`scripts/localart.py`): the workshop (16:9); the bear at each of 8 stages from fur to box (8, 1:1, cutout yes); 6 funny wrong-order bears (6, 1:1); tools and machines (9, 1:1, cutout yes); cost pictures (5).
- Drawn in code: the line and slots, cards, trays, the price tag and its numbers, bubbles.
About 51 images.

## Voice
Two bank voices, both unique in this batch: `lively-host` as Mrs. Haddad and narrator; `easy-coach` as Theo. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.q`, `welcomeAfter: true`.
- how `welcome`: "Welcome to my bear workshop! I need help setting up my line. Which step comes first? Tap a card to hear it."
- event `card`: the card's words.
- how `run` (once): "Tap Run a bear."
- event, whole, each wrong-order result (six lines above).
- event, whole, `line-right`: "A perfect bear! Now give each step its tool and its worker. Drag from the trays."
- event `no-tool`: the reason line for that tool or worker.
- event, whole, `machine-skill`: "Machines and tools help us work. Skills are what people learn to do the work."
- event, whole, `cost`: "So one bear costs me 12 dollars to make."
- event, whole, `faster`: the chosen change's line.
- how `ask`: "Pick a question to ask me."
- event, whole, each answer.
- how `visitor`: "Theo is visiting. Answer his questions by tapping your line."
- event, whole, Theo's questions, his nods and his "Look at your line" line, and "Now I know how bears are made!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the ordered line and its run, the wrong-order rules, the tool and worker matching, the price tag, and the question views.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Order | Try orders at random | 5,040 orders; each run stops at the first wrong pair with a reason, so trial needs the reasons. |
| Tools | Drag everything onto one step | Each slot holds one tool and one worker; wrong ones come back with a reason. |
| Cost | Ignore it | The visitor's third question asks for it. |
| Visitor | Tap every step | The first wrong tap gives the hint; the answer counts only after the hint plays; three questions, three different parts of the line. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued; may be cut). Tap a card: `card`.
2. Seven slots full: `run`. Run: step sounds, then a wrong-order line (whole) or `line-right` (whole).
3. Trays: `no-tool` or a click; all matched: `machine-skill` (whole); tag: `cost` (whole); `Faster?`: `faster` (whole).
4. Ask the maker: `ask`; each bubble: answer (whole).
5. Visitor: `visitor`; Theo's question (whole), waits; the child's tap; nod or hint (whole); after three, the closing line (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Eco.7, D2.Eco.13, D4.2 and D4.5 (K-2) | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Capital goods are tools, machines and buildings used to make goods; human capital is the knowledge and skills people use to work | Federal Reserve Bank of St. Louis, Econ Lowdown "Capital resources" and "Human capital" | Wikipedia, Capital good and Human capital (checked 2026-11-09) | yes |
| The cost of making a product includes materials, labor (pay) and the use of machines and power | Federal Reserve Bank of St. Louis, Econ Lowdown "Costs of production" | Wikipedia, Cost of goods sold (checked 2026-11-09) | yes |
| Toys for young children must not have small parts, like eyes, that pull off; toys are pull-tested | U.S. Consumer Product Safety Commission, small parts rule (16 CFR 1501) | eCFR, 16 CFR 1500.51 (use and abuse tests, tension test) | yes |
| The teddy bear is named after President Theodore Roosevelt (1902) | Wikipedia, Teddy bear (checked 2026-11-09) | National Park Service, Theodore Roosevelt Birthplace, "The Story of the Teddy Bear" | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r2, 2026-11-09): costs 3 + 2 + 1 + 4 + 2 = 12; the seven-step order passes every wrong-order rule and every one of the other 5,039 orders breaks at least one rule, so only one order wins; the three visitor answers sit on three different parts of the line; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 line, cards, trays and tag fit; at 680x425 the trays fold into buttons.
2. Only the one right order runs a whole bear; each wrong order stops with its result. (D4.2.K-2)
3. Each of the six wrong-order results plays with its picture.
4. Each step takes only its tool or machine and its worker, tagged "Machine or tool" and "Skill". (D2.Eco.13.K-2)
5. The price tag adds five costs to 12 dollars. (D2.Eco.7.K-2)
6. Ask the maker answers six questions, three picked. (D4.5.K-2)
7. Theo's three questions are answered by tapping the line. (D4.5.K-2)
8. `Run a bear`, the trays and `Faster?` are never named before they show.
9. Tap while it plays: dragging during a run stops it; no older line plays after a newer one.
10. Motion off: no bear motion; no network requests.

## Open questions
- None for Cory.
