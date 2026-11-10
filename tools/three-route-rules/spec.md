# Three Route Rules

## One idea
A walking app called StepMap (made up) can pick routes by three rules, fastest, fewest street crossings, or no stairs, and its designer, Lena (made up, labeled "illustration"), asks the child to test them on one town map with four travelers going to the school, the library and the park: a kid walking to school, a wheelchair user, a parent with a stroller and a jogger; the child picks a rule, each traveler's route draws on the map with a trip card (minutes, crossings, stairs and a face), and the trouble shows at once: fastest sends the wheelchair user to a staircase shortcut she cannot use, fewest crossings makes the jogger's run long and dull, and no stairs helps the stroller and the wheelchair but turns the kid's 12-minute walk into 18 minutes; a score sheet of 3 rules by 4 travelers fills with helped, OK and let down; then the child writes a combined rule ("no stairs, then fastest") from condition blocks, tests it on all four, and explains the trade-off that is still left; at the end the child sees that no rule is neutral, each one picks who comes first, and the people who make the app choose that, so a student in grades 3 to 5 learns that different algorithms for the same job help or hurt different people.

## Not like
- line-leader-picker (Grades K-2, spec): turn rules for a class. Here route rules for a town.
- algorithm-audit (Grades 6-8, spec): bias in a scoring formula. Here trade-offs between simple rules.
- biased-bot (4, spec): unfair training data. Here unfair rules written by people.
- code-tracer (4, live): tracing values in code. Here comparing what rules do to people.

## Who and how
- Grades 3-5, Computer Science, module "Algorithms That Help Some More". Standards: E3-ALG-IM-03, E4-ALG-IM-03, E5-ALG-IM-03 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Different algorithms for the same job help or hurt different people").
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- One town map, four travelers, three rules, the score sheet, a rule builder with five condition blocks, two extra maps. Extra: Town meeting (the class votes on which rule the app should use, on the projector). tool.json `modes: ["Test rules", "Town meeting"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-ALG-IM-03 | Run each rule; read each traveler's trip | routes and faces | 2 |
| E4-ALG-IM-03 | Fill and explain the score sheet | 3 by 4 grid of helped and let down | 3 |
| E5-ALG-IM-03 | Build a combined rule; test it; name the trade-off | a better sheet, still not perfect | 4 |

## Screens and modes
Header (kit): title "Three Route Rules"; `Test rules`, `Town meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A colorful town map with a school, a library, a park, a hill with a staircase shortcut, four travelers at their homes, three rule buttons, and Lena with a phone. The welcome is queued (`welcomeAfter: true`): "Same town, three rules. Who does each one help? Tap Fastest to try it." First hint: "Tap Fastest."

**Run a rule (focus: the map).** At 1366x768 the map fills the left with trip cards right; at 680x425 the cards are a tab. Routes draw one by one with a dot walking; each card shows minutes, crossings, stairs and a face. A stair on a wheelchair route shows a stop sign and "can't use this route".

**Score sheet.** After each rule the child marks each traveler helped, OK or let down. The sheet asks one "why" per row.

**Make a rule.** Condition blocks: no stairs, fastest, fewest crossings, wide sidewalks, shade. The child stacks two or three in order ("first no stairs, then fastest") and runs it on all four.

**New towns.** Two more maps (a riverside town with a bridge, a city with an elevator) test the child's rule.

**Rules pick who comes first (the aha).** Lena: "No rule is neutral. Every rule picks who comes first, and people like us choose it."

**The end.** The score sheets and the child's rule. `Print` prints them.

**Town meeting (extra).** Class vote.

## Content
- Four travelers labeled "illustration"; minutes and crossings fixed per map.
- The wheelchair user is shown as capable and busy, not as a problem; her trip is let down by the rule, not by her.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Rules can be run again; blocks can be reordered until `Test it`.
- Keyboard: Tab to rule buttons, the map (arrows move between travelers), trip cards, score cells and blocks (arrows reorder); Enter runs or marks.
- With Motion off routes appear at once.

## Look
- Accent `--brand` #2f5d8a map blue (header, routes, buttons); gold #f4c542 (the traveler in focus, the chosen rule); paper #eef3f8; ink #0a1a2b; muted #4c5560.
- Contrast (WCAG 2.1, computed): white on brand 6.88:1; brand on paper 6.16:1; ink on paper 15.73:1; muted on paper 6.78:1; ink on gold 10.80:1.
- Never color alone: each route has its traveler's icon and a dash pattern; sheet cells say helped, OK or let down.
- Different from this batch (relay purple, museum brown, workday green, council red).

## Art
- People (illustrated): Lena and four travelers, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): a town map backdrop for each of three towns (3, 16:9).
- Drawn in code: routes, stairs, crossings, trip cards and the score sheet.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as Lena; `news-reader` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.town + ':' + state.rule + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `rule`: "Tap a rule button."
- how `mark`: "Tap helped, OK or let down for each traveler."
- how `why`: "Tap the reason."
- how `build`: "Drag blocks to build your rule, then tap Test it."
- event, whole, rules pick who comes first.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: a small street graph per town with edge costs (minutes, crossing, stairs, shade, width), lexicographic route search for stacked rules, trip cards, the score sheet.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Score sheet | Mark everyone helped | Each mark is checked against the trip card. |
| Why | Tap any reason | Each row has one matching reason. |
| Own rule | Stack every block | The child must still name who is let down. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `rule`.
2. `mark`; `why`.
3. `build`.
4. Rules pick who comes first (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Stairs block wheelchair routes, and accessible routes need curb ramps and no steps | U.S. Access Board, ADA Accessibility Guidelines, accessible routes | U.S. Department of Justice, "2010 ADA Standards for Accessible Design" | yes |
| Algorithm design choices can favor some groups over others | K-12 Computer Science Framework (2016), Impacts of Computing | CSTA K-12 Computer Science Standards (2017), 1B-IC-18 and 1B-IC-19 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s23, 2026-11-10): the kid's no-stairs route is 18 minutes against 12, 6 more; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and cards; at 680x425 cards as a tab.
2. Three rules are run for four travelers with trips read. (E3-ALG-IM-03)
3. The score sheet is filled and explained. (E4-ALG-IM-03)
4. A combined rule is built, tested on three towns, and its trade-off named. (E5-ALG-IM-03)
5. The wheelchair user is shown as capable; travelers labeled illustration.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: routes appear at once; no network requests.

## Open questions
None.
