# Particle Party

## One idea
A sealed jar of ice at minus 20 degrees Celsius sits on a stand with a burner knob and a freezer knob, a particle zoom window and an empty temperature graph; before each run the student sketches the graph they expect, then turns the burner and watches: particles jiggle faster in place and the temperature climbs, at 0 degrees the line goes flat while particles break out of their places and slide past each other, then climbs again, and at 100 degrees goes flat again as particles fly apart into a gas, and the flat parts last longer than the student expects (melting 1 gram of ice takes as much energy as heating that water 80 degrees, and boiling takes over five times the energy of heating from 0 to 100); then the freezer runs it all backward; iron (melts near 1,538 degrees) and nitrogen (boils near minus 196) show the same shape at very different temperatures; at the end the student's sketch sits next to the real graph with one sentence about what temperature measures and where the energy goes on the flat parts, so a seventh grader learns to develop a model that predicts and describes changes in particle motion, temperature and state of a pure substance when thermal energy is added or removed.

## Not like
- particle-zoom (5, spec): dissolving and air as particles, same family. Here heating, cooling and states.
- gas-law-lab (10, spec): pressure and volume of a gas. Here the whole path from solid to gas.
- hot-meets-cold (11, spec): heat flowing between two objects. Here one substance changing state.
- reaction-kitchen (7, spec): new substances forming. Here the same substance changing state.

## Who and how
- Grade 7, Science, module "States of Matter". Standard: MS-PS1-4 (develop a model that predicts and describes changes in particle motion, temperature, and state of a pure substance when thermal energy is added or removed).
- Format: simulator. Driver: one student alone, or a teacher leading the class (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- Three pure substances (water, iron, nitrogen), the burner and freezer knobs, the particle window, the sketch tool, the live graph, the sentence card. Extra: Mystery substance (the plateaus identify it, from a list of five). tool.json `modes: ["Jar", "Mystery substance"]`, `minutes: "20-30"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS1-4 (predict) | Sketch the expected graph before each run | the sketch layer | 2 |
| MS-PS1-4 (motion and temperature) | Heat and cool, watch particles and the graph together | the particle window; the climbing and flat graph | 3 |
| MS-PS1-4 (state) | Compare three substances and explain the flat parts | three graphs; the sentence card | 4 |

## Screens and modes
Header (kit): title "Particle Party"; `Jar`, `Mystery substance`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A glass jar of ice on a lab stand, frost on the outside, a thermometer reading minus 20. A round zoom window shows particles locked in a neat pattern, shivering. The welcome is queued (`welcomeAfter: true`): "What happens to the tiny particles when you heat ice? First, guess. Draw the line you think the thermometer will make." First hint: "Drag on the graph to draw your guess."

**The jar (focus: the window and graph).** At 1366x768 the jar is left, the zoom window center and the graph right; at 680x425 the jar and window share the top and the graph is below. The student draws a guess, then turns the burner knob (low, medium, high). Particles speed up; the graph line climbs. At 0 degrees the line stays flat while particles break their pattern; a label "melting" sits on the flat part with the note "energy going into breaking particles loose". At 100 degrees flat again, "boiling", particles fly apart and the jar's vent opens.

**Backward.** The freezer knob runs it in reverse: condensing at 100, freezing at 0, flat both times while energy leaves.

**Other substances.** Iron in a crucible melts near 1,538 degrees; nitrogen in a flask boils near minus 196. Same shape, different temperatures; the graph rescales with a note.

**Sketch and real (the aha).** The student's sketch beside the real line. A sentence card: "Temperature tells me ___. On the flat parts the energy ___." Narrator: "Temperature is how fast particles move on average. On the flat parts, the energy goes into moving them apart instead."

**The end.** The sketches, real graphs and the sentence. `Print` prints them.

**Mystery substance (extra).** A jar of something unnamed; read its melting and boiling plateaus and pick it from five.

## Content
- Melting and boiling points and a simple energy model (heat to raise each state, heat to change state) for water, iron and nitrogen; five mystery substances with their points; the sentence card.
- A note: "The particles in the window are a picture. Real particles are far smaller and far more."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The knob can be turned up, down or off at any point; the graph pauses with it.
- Keyboard: Tab to the sketch, knobs, substance picker and card; arrows draw and turn knobs; Enter confirms.
- With Motion off particles show one still frame per state and the graph draws in steps.

## Look
- Accent `--brand` #3a3f9a indigo (header, the real line, the knobs); gold #f4c542 (the flat parts, the student's sketch); paper #f2f2fb; ink #0f1030; muted #50516a.
- Contrast (WCAG 2.1, computed): white on brand 8.91:1; brand on paper 8.00:1; ink on paper 16.59:1; muted on paper 6.92:1; ink on gold 11.35:1.
- Never color alone: sketch and real lines differ in dash and carry labels; states carry words.
- Different from this batch (spruce, prairie amber, signal magenta, factory teal).

## Art
- Local FLUX (`scripts/localart.py`): the jar on the stand (1, 1:1), the iron crucible (1, 1:1), the nitrogen flask (1, 1:1).
- Drawn in code: particles, the graph, knobs, the thermometer.
About 3 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the party host; `clear-teacher` as the lab guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.substance + ':' + state.phase + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sketch`: "Drag on the graph to draw your guess."
- how `heat`: "Turn the burner knob up."
- event, whole, each flat part.
- how `cool`: "Turn the freezer knob."
- how `substance`: "Tap iron or nitrogen to try another."
- how `write`: "Fill in the sentence card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
particles (`kit/particles.js`, inlined after `kit:curio`), as described in gas-law-lab's spec. Uses `Box` with `attract` for the solid, temperature-scaled speeds, wall `hits(side)` for the gas, and `still()` for Motion off; the picture is labeled "in the picture".

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sketch | Skip the sketch | `Start` waits for a sketch. |
| Graph | Turn the knob to high | The flat parts still appear; the card asks about them. |
| Sentence | Write "it melts" | The card needs both what temperature tells and where the energy goes. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sketch`; `heat`.
2. Flat part (whole), waits.
3. `cool`; `substance`.
4. `write`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-PS1-4 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Water melts at 0 C and boils at 100 C at sea level | NIST Chemistry WebBook, "Water" | U.S. Geological Survey, "Water properties" | yes |
| Heat to melt ice 334 J/g; to warm water 4.18 J/g per degree; to boil 2,260 J/g | OpenStax, "College Physics 2e", chapter 14 | NIST Chemistry WebBook, "Water" | yes |
| Iron melts near 1,538 C; nitrogen boils near minus 196 C | Royal Society of Chemistry, Periodic Table, iron and nitrogen | NIST Chemistry WebBook | yes |
| Temperature relates to the average motion of particles | American Chemical Society, "Middle School Chemistry", chapter 1 | OpenStax, "Chemistry 2e", chapter 9 | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r3, 2026-11-10): melting takes as much energy as warming water 80 degrees; boiling takes 5.4 times the energy of warming from 0 to 100; iron's melting and nitrogen's boiling are 1,734 degrees apart; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 jar, window and graph; at 680x425 stacked.
2. A sketch is drawn before each run. (MS-PS1-4)
3. Heating and cooling show particle motion with climbing and flat parts. (MS-PS1-4)
4. Three substances are compared and the sentence explains the flat parts. (MS-PS1-4)
5. Points and energy values match the cited tables.
6. The picture note shows.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still frames and stepped graph; no network requests.

## Open questions
None.
