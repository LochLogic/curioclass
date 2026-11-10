# Intersection Angles

## One idea
A busy intersection is seen from above, and the crossing guard, Mr. Osei (made up, labeled "illustration"), needs every angle marked on the new crosswalk plan from one angle the surveyor measured, 62 degrees; the child finds the angle straight across the street as its vertical partner (62), the angle beside it as supplementary (180 - 62 = 118), and the corner where a sidewalk ramp meets a right-angle curb as complementary (90 - 62 = 28), and for each one writes and solves an equation rather than just typing a number; later levels hide the numbers in expressions: a rail crossing's scissor gates make vertical angles of 2x and x + 30, so 2x = x + 30 and x = 30, giving 60 degrees; two adjacent angles along a straight curb are 3x and x + 20, so 3x + x + 20 = 180 and the angles are 120 and 60; a bike lane splits a right angle into 2x and 3x, so 5x = 90 and the parts are 36 and 54; each solved angle unlocks the next, and the plan fills in until every angle at the intersection is labeled from that first 62; at the end the child sees that a few angle facts and an equation reach every angle, so a seventh grader learns to use supplementary, complementary, vertical and adjacent angles to write and solve simple equations for an unknown angle in a figure.

## Not like
- big-wheel-small-wheel (7, concept): circles. Here angles between lines.
- clay-cutting-bench (7, concept): slicing solids. Here angles in a plane.
- balance-puzzle (6, spec): one-step equations on a scale. Here equations from angle facts.
- transformation-dock (8, concept): moving figures. Here angles where lines cross.

## Who and how
- Grade 7, Math, module "Angle Relationships". Standards: 7.G.5 (use facts about supplementary, complementary, vertical, and adjacent angles in a multi-step problem to write and solve simple equations for an unknown angle in a figure).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Four intersections (a crossroads, a rail crossing, a five-way corner, a bike-lane junction), eighteen angles to find, the angle-fact cards. Extra: Teacher plan (the teacher picks the given angle and the hidden ones). tool.json `modes: ["Crosswalk plan", "Teacher plan"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.G.5 (facts) | Pick the fact that links two angles | vertical, adjacent, supplementary, complementary marks | 2 |
| 7.G.5 (equations) | Write and solve the equation | 2x = x + 30; 3x + x + 20 = 180 | 3 |
| 7.G.5 (multi-step) | Chain facts across the intersection | the plan filling in from one angle | 4 |

## Screens and modes
Header (kit): title "Intersection Angles"; `Crosswalk plan`, `Teacher plan`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** An intersection from above with crossing streets, painted crosswalks, a curb ramp, and Mr. Osei with a stop sign. One angle is labeled 62 degrees. The welcome is queued (`welcomeAfter: true`): "I need the angle straight across the street. Tap it." First hint: "Tap the angle across from 62."

**Find an angle (focus: the plan).** At 1366x768 the plan fills the left with the fact cards and equation box right; at 680x425 the cards are a sheet. The child taps an unknown angle, then a known one, then the fact card that links them (vertical, adjacent and supplementary, complementary). The equation box fills with the fact's form (a + 62 = 180) and the child solves it step by step. A wrong fact shows a counterexample overlay (the two angles drawn with their real sizes).

**Expression levels.** Angles are labeled with expressions. The child writes the equation from the fact (vertical: 2x = x + 30), solves for x, then substitutes to get each angle.

**Chains.** Some angles need two facts in a row (vertical, then supplementary). The plan draws the chain as arrows.

**From one angle (the aha).** The whole plan is labeled. Mr. Osei: "One measurement and a few facts, and every corner is known."

**The end.** The labeled plan. `Print` prints it.

**Teacher plan (extra).** The teacher picks the given and hidden angles.

## Content
- Eighteen angles in four figures, whole-degree answers, all readable with `Read`.
- Lines are exact; the street picture is a backdrop only.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Facts and equations can be changed until `Check`.
- Keyboard: Tab to angles on the plan, fact cards, the equation box and Check; Enter picks or checks.
- With Motion off overlays and arrows appear at once.

## Look
- Accent `--brand` #3d4a5c asphalt slate (header, plan lines, buttons); gold #f4c542 (the angle in hand, a solved angle); paper #f0f2f5; ink #0e141d; muted #535860.
- Contrast (WCAG 2.1, computed): white on brand 9.00:1; brand on paper 8.03:1; ink on paper 16.48:1; muted on paper 6.38:1; ink on gold 11.36:1.
- Never color alone: right angles carry a square mark; each fact card has an icon and a name.
- Different from this batch (beaker violet, bike-path blue, clay sienna, card-table green).

## Art
- People (illustrated): Mr. Osei, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): four intersections from above (4, 16:9).
- Drawn in code: every line, arc and angle label over the scenes, so angles are exact.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as Mr. Osei; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.figure + ':' + state.angle + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `pick`: "Tap an unknown angle, then a known one."
- how `fact`: "Tap the fact that links them."
- how `solve`: "Type the next step of the equation."
- how `chain`: "Find a known angle one step away."
- event, whole, from one angle.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: exact line and angle drawing, fact checking, the equation box with step checks, chains.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Facts | Guess 180 minus every angle | Vertical and complementary pairs fail it. |
| Expressions | Type the angle without x | The equation and x are checked first. |
| Reading off the picture | Measure by eye | Expression angles are drawn to scale only after they are solved. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `pick`; `fact`.
2. `solve`.
3. `chain`.
4. From one angle (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.G.5 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Vertical angles are equal; a straight angle is 180 degrees; a right angle is 90 | Euclid, "Elements", Book I, Proposition 15 and definitions | Common Core Standards Writing Team (2012), "Progressions for the CCSS, 7-8 Geometry" | yes |
| Writing equations from angle facts links geometry and algebra | Common Core Standards Writing Team (2012), "Progressions for the CCSS, 7-8 Geometry" | National Council of Teachers of Mathematics (2000), "Principles and Standards for School Mathematics", grades 6-8 geometry | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s18, 2026-11-10): 180 - 62 = 118 and 90 - 62 = 28; 2x = x + 30 gives x = 30 and 60 degrees; 3x + x + 20 = 180 gives 120 and 60; 2x + 3x = 90 gives 36 and 54; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 plan and cards; at 680x425 cards as a sheet.
2. Each angle is linked to a known one by a named fact. (7.G.5)
3. Expression angles are found by writing and solving an equation. (7.G.5)
4. Four intersections are fully labeled through chains of facts. (7.G.5)
5. Unsolved expression angles are not drawn to scale.
6. `Read` reads every card and angle; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: overlays appear at once; no network requests.

## Open questions
None.
