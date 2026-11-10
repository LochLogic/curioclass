# Adventure Outline Cards

## One idea
On a corkboard with a stack of blank index cards and a story starter, "A fox wants to cross the river before dark", the storyteller, Nana Wren (made up, labeled "illustration"), asks the child to plan a choose-your-own-adventure as an algorithm before any of it is written: third graders write numbered steps with one event that starts it ("when the sun sets, start at card 1") and send a reader token down the path to the end; fourth graders add a repeat ("knock on the door until someone answers") and an if-then fork ("if the bridge is out, go to card 7"), and the token walks every branch; fifth graders redraw the outline as a card diagram with arrows and a coin counter that changes along the way ("if coins are 3 or more, buy the boat ride"); `Test every path` runs the token down each route and lights cards red where it gets stuck, a fork that points to a card 7 that does not exist, a repeat that never stops because nobody ever answers, a counter that can never reach 3 because only 2 coins exist on that path, and the child fixes each one and tests again; at the end the outline is an algorithm, and testing every path before writing a single line of code catches the bugs, so a student in grades 3 to 5 learns to plan an algorithm with events, loops, choices and variables, in words and in diagrams.

## Not like
- chore-flowcharts (Grades 6-8, spec): flowcharts into pseudocode. Here card outlines for a story.
- traffic-light-coder (3, spec): if-then rules in code. Here planning before code.
- inside-the-keypress (3, concept): hardware and software. Here algorithms on paper.
- team-code-relay (3, spec): combining code. Here planning one algorithm.

## Who and how
- Grades 3-5, Computer Science, module "Plan It Before You Code It". Standards: E3-ALG-PS-01, E4-ALG-PS-01, E5-ALG-PS-01 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Write and draw algorithms with events, loops, choices and variables").
- Format: builder (changed from story; the story is the content, not the play). Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three story starters, one level per grade, the token tester, a card diagram view for grade 5. Extra: Story swap (a partner tests the child's outline on the same device). tool.json `modes: ["Corkboard", "Story swap"]`, `minutes: "25-35"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-ALG-PS-01 | Write ordered steps with an event; test | the token reaching the end | 2 |
| E4-ALG-PS-01 | Add a loop and a fork; test each branch | the token on two paths | 3 |
| E5-ALG-PS-01 | Draw the diagram with a coin counter; fix stuck paths | red cards turning green | 4 |

## Screens and modes
Header (kit): title "Adventure Outline Cards"; `Corkboard`, `Story swap`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A cork wall with pins, a stack of index cards, a story starter card, and Nana Wren in a reading chair. The welcome is queued (`welcomeAfter: true`): "Plan the story before you write it. Tap the stack to pin your first card." First hint: "Tap the stack."

**Steps (focus: the board).** At 1366x768 the board fills the view with a card editor below; at 680x425 the editor is a sheet. Each card has a number, a step line (pick from story phrases or type), and a "next" field. One event card starts the story.

**Repeat and fork (grade 4).** Repeat cards ("do ... until ...") and fork cards ("if ..., go to card ..., else go to card ...").

**Diagram (grade 5).** `Diagram view` turns the cards into boxes and arrows; a coin counter card adds or subtracts and a fork can test it.

**Test every path.** The token, a little paper fox, walks every route; stuck cards turn red with a reason ("card 7 doesn't exist", "this repeat never stops", "coins never reach 3"). The child fixes and re-tests.

**Plan first (the aha).** Nana Wren: "Your outline is an algorithm. Test every path before you write, and the bugs show up early."

**The end.** The finished outline and the story it makes. `Print` prints the cards.

**Story swap (extra).** A partner tests it.

## Content
- Three starters (the fox and the river, a robot lost in a library, a kid planting a garden), story phrases for each, all readable with `Read`.
- Typed card text stays on the device.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be edited, renumbered and unpinned until `Test every path`, and after.
- Keyboard: Tab to the stack, cards (arrows move them on the board), card fields, Diagram view and the test button; Enter pins or tests.
- With Motion off the token jumps card to card.

## Look
- Accent `--brand` #5b4a8a corkboard violet (header, card frames, buttons); gold #f4c542 (the card in hand, the token); paper #f3f1f9; ink #18122e; muted #53505e.
- Contrast (WCAG 2.1, computed): white on brand 7.52:1; brand on paper 6.72:1; ink on paper 16.11:1; muted on paper 7.01:1; ink on gold 11.08:1.
- Never color alone: stuck cards show an X and a reason; good cards show a check.
- Different from this batch (circuit blue, kitchen-table rust, ramp green, helper teal).

## Art
- People (illustrated): Nana Wren, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the corkboard (1, 16:9), story art for three starters (3, 4:3).
- Drawn in code: cards, arrows, the token and the coin counter.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as Nana Wren; `easy-coach` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pin`: "Tap the stack to pin a card."
- how `write`: "Pick a step and set what comes next."
- how `fork`: "Pick the if, then pick both cards."
- how `test`: "Tap Test every path."
- how `fix`: "Tap a red card to fix it."
- event, whole, plan first.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: card graph with events, repeats, forks and one counter; an all-paths walker with a step limit to catch endless loops; the diagram view.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Steps | One card pointing to the end | Each level needs its parts (event, loop, fork, counter). |
| Branches | Test one path | The test walks every path. |
| Counter | Set coins to 99 | The counter starts at 0 and changes only on cards. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pin`; `write`.
2. `fork`.
3. `test`; `fix`.
4. Plan first (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Planning algorithms with events, loops, conditionals and variables before coding | CSTA K-12 Computer Science Standards (2017), 1B-AP-08, 1B-AP-09 and 1B-AP-10 | K-12 Computer Science Framework (2016), Algorithms and Programming, grades 3-5 | yes |
| Testing all paths finds errors early | CSTA K-12 Computer Science Standards (2017), 1B-AP-15 | Code.org CS Fundamentals, debugging and planning lessons | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s24, 2026-11-10): the seeded coin path has 2 coins, so "3 or more" can never be met; the walker stops at 50 steps to call a loop endless; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 board and editor; at 680x425 editor as a sheet.
2. A step plan with an event is tested to the end. (E3-ALG-PS-01)
3. A loop and a fork are added and every branch is tested. (E4-ALG-PS-01)
4. The diagram with a counter is fixed until every path finishes. (E5-ALG-PS-01)
5. Typed text stays on the device.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: the token jumps; no network requests.

## Open questions
- Format change from story to builder, as the idea card proposes (default used: builder).
