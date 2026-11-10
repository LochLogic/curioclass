# Mystery Powders

## One idea
In the back room of a school bakery, the labels have fallen off five jars of white powder (salt, sugar, baking soda, cornstarch and plaster) and a sixth jar holds a mystery mix, and Ana the baker (illustrated) needs them sorted before the bake sale; the student runs tests on each powder with a hand lens, water, vinegar, iodine, a magnet and a conductivity tester, and logs each result in a property table (crystal shape, dissolves or not, fizzes with vinegar, turns blue-black with iodine, gets warm and hard with water, makes salt water that conducts), and each test uses a little of each sample so planning matters; for every mix the student decides "just mixed" or "something new" from the evidence (gas bubbles, a color change, heat, a hard new solid) and tries to get the starting materials back (salt from evaporated salt water, yes; dry plaster from hardened plaster, no); at the end the student names each jar and the two ingredients in the mystery mix, citing tests from the table, and the bake sale goes on, so a fifth grader learns to identify materials by their properties, and to test whether mixing substances makes a new substance.

## Not like
- particle-zoom (5, spec): what all matter is made of. Here telling substances apart.
- melt-or-not (2, live): changes that can be undone. Here evidence of a new substance.
- bond-battle (10, spec): why substances bond. Here what they do in tests.
- magnet-maze (3, spec): one property, magnetism. Here many properties at once.

## Who and how
- Grade 5, Science, module "Properties and Mixtures". Standards: 5-PS1-3 (make observations and measurements to identify materials based on their properties), 5-PS1-4 (conduct an investigation to determine whether the mixing of two or more substances results in new substances).
- Format: mystery. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five known powders and a mystery mix, six tests, a sample budget, the property table, the "just mixed or something new" check, the get-it-back test, the case notebook. Extra: Lab partners (two students split the tests and share one table). tool.json `modes: ["Bakery", "Lab partners"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 5-PS1-3 | Run six tests on five powders and fill the property table | the test tray; the table | 2 |
| 5-PS1-4 | Decide "just mixed" or "something new" from evidence and try to get the starting materials back | the evidence card; the get-it-back result | 3 |
| 5-PS1-3 (identify) | Name each jar and the mystery mix's ingredients from the table | the case notebook | 4 |

## Screens and modes
Header (kit): title "Mystery Powders"; `Bakery`, `Lab partners`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bakery back room with five unlabeled jars marked A to E, a sixth jar marked "?", a test tray and a case notebook. Ana (illustration) stands at the door. A safety card shows first: "Never taste lab samples. Iodine and plaster are not food." The welcome is queued (`welcomeAfter: true`): "The labels fell off! Help me sort these before the bake sale. Pick a jar, then pick a test." First hint: "Tap jar A."

**Testing (focus: the tray).** At 1366x768 the tray fills the left with the table right; at 680x425 the table is a sheet. Six tests:
1. Hand lens: salt shows tiny cubes; sugar shows clear crystals of a different shape; the others look like fine powder.
2. Water: salt and sugar dissolve; baking soda partly dissolves; cornstarch makes a cloudy mix that settles; plaster gets warm and starts to harden.
3. Vinegar: baking soda fizzes.
4. Iodine: cornstarch turns blue-black.
5. Magnet: none are pulled (a result too).
6. Conductivity tester in the water mix: salt water lights the bulb; sugar water does not.
Each sample starts with ten scoops, and each test uses one. The table fills with the student's results.

**Just mixed or something new (5-PS1-4).** For each mix, an evidence card asks: bubbles of gas? a color change? heat? a hard new solid? The student picks "just mixed" or "something new". Then a get-it-back test: evaporate salt water and salt crystals return; hardened plaster stays hard; the gas from fizzing is gone.

**The mystery mix.** Jar "?" fizzes with vinegar and turns blue-black with iodine: baking soda and cornstarch. The student names both from the table.

**The case notebook (the aha).** Each jar named with the tests that proved it. Narrator: "Every substance has its own set of properties, like a fingerprint. And when something new forms, the evidence shows it: gas, heat, a color change or a new solid."

**The end.** The notebook and table, and a bake sale scene. `Print` prints them.

**Lab partners (extra).** Two students split the tests and share one table.

## Content
- Five powders with true test results, six tests, the sample budget, evidence cards, get-it-back tests, the mystery mix, the notebook.
- The safety card shows first and again before iodine and plaster.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A test can be redone if scoops remain.
- Keyboard: Tab to jars, tests, the table, evidence cards and the notebook; Enter runs a test.
- With Motion off results appear without fizzing or color fades.

## Look
- Accent `--brand` #9b2f5a bakery rose (header, the notebook, jar labels); gold #f4c542 (the jar in use, a new result); paper #fcf0f5; ink #2c0b19; muted #5f5158.
- Contrast (WCAG 2.1, computed): white on brand 7.12:1; brand on paper 6.42:1; ink on paper 16.19:1; muted on paper 6.75:1; ink on gold 11.05:1.
- Never color alone: the iodine result carries the words "blue-black"; the bulb carries "on" or "off"; results carry words.
- Different from this batch (globe blue, tea amber, river green, night indigo).

## Art
- People (illustrated): Ana the baker, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the back room (1, 16:9), the bake sale (1, 16:9), lens close-ups of five powders (5, 1:1).
- Drawn in code: the tray, test reactions, the table, cards, the notebook.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `warm-teacher` as Ana; `knowing-guide` as the lab guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.jar + ':' + state.test + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `test`: "Pick a jar, then tap a test."
- event, whole, each test result.
- how `evidence`: "Pick just mixed or something new."
- how `getback`: "Tap Get it back to try."
- how `name`: "Name each jar in the notebook."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the test tray, result rules, the sample budget, evidence cards, the notebook.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Naming | Guess names | Each name needs at least one test from the table cited. |
| Tests | Run every test on every jar | The ten-scoop budget runs out on the mystery mix. |
| Evidence | Always pick "something new" | Each pick checks against the evidence card. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: safety card; `welcome` (queued). `test`; result (whole), waits.
2. `evidence`; `getback`.
3. `name`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 5-PS1-3, 5-PS1-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Test results for salt, sugar, baking soda and cornstarch (dissolving, vinegar, iodine) | American Chemical Society, "Inquiry in Action", identifying an unknown powder | Royal Society of Chemistry, "Identifying white powders" | yes |
| Plaster of Paris warms and hardens when mixed with water | U.S. Geological Survey, "Gypsum" mineral commodity summary | American Chemical Society, "ChemMatters", plaster | yes |
| Salt water conducts electricity; sugar water does not | U.S. Geological Survey, Water Science School, "Conductivity" | American Chemical Society, "Middle School Chemistry", ions in solution | yes |
| Evidence of a new substance: gas, color change, heat, new solid | American Chemical Society, "Middle School Chemistry", chapter 6 | NGSS Appendix E, progressions for PS1 | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r30, 2026-11-09): five powders and six tests is thirty table cells; ten scoops for five jars plus the mystery jar is sixty scoops; the mystery mix has two ingredients; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 tray and table; at 680x425 sheet.
2. Six tests on five powders fill the table with true results. (5-PS1-3)
3. Mixes are judged "just mixed" or "something new" from evidence, with get-it-back tests. (5-PS1-4)
4. Each jar and the mystery mix's ingredients are named with tests cited. (5-PS1-3)
5. The safety card shows first and before iodine and plaster.
6. Ana is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no fizzing animation; no network requests.

## Open questions
None.
