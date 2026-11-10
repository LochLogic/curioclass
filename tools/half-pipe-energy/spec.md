# Half-Pipe Energy

## One idea
A skater stands at the top of a half-pipe beside a pen to redraw the ramp, mass and height sliders, a speed meter, a height marker and three live energy bars (kinetic, potential, thermal); the student drops the skater and watches the bars trade places as height turns into speed and back, with friction on by default so each pass ends a little lower and the thermal bar grows (friction can be switched off to see the ideal case); a data drawer logs each run, and the student graphs kinetic energy against mass (twice the mass, twice the energy) and against speed (twice the speed, four times the energy), changes the drop height to see how much more energy is stored the higher the skater starts (a 50 kg skater 3 m up stores about 1,470 joules), then drags a brake pad onto the ramp and stops the skater, watching the kinetic bar drain into the thermal bar while a heat view shows the wheels and pad glowing warm; at the end a claim card holds the student's graphs and the brake test, so an eighth grader learns how kinetic energy relates to mass and speed, how stored energy changes with distance from Earth, and that when kinetic energy changes, energy is transferred to or from the object.

## Not like
- zipline-energy (11, spec): friction and brakes in numbers and equations. Here bar charts and proportional graphs only.
- bowling-lab (4, spec): faster means more energy. Here how much more.
- crash-test-lab (8, spec): forces in collisions. Here energy trading forms.
- curling-stones (11, spec): forces on ice. Here energy on a ramp.

## Who and how
- Grade 8, Science, module "Kinetic and Potential Energy". Standards: MS-PS3-1 (construct and interpret graphical displays of data to describe the relationships of kinetic energy to the mass of an object and to the speed of an object), MS-PS3-2 (develop a model to describe that when the arrangement of objects interacting at a distance changes, different amounts of potential energy are stored in the system), MS-PS3-5 (construct, use, and present arguments to support the claim that when the kinetic energy of an object changes, energy is transferred to or from the object).
- Format: simulator. Driver: one student alone, or a teacher leading the class (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- One skater, the ramp pen, mass (30 to 90 kg) and height (1 to 5 m) sliders, three bars, the friction switch, the data drawer, two graphs, the brake pad with a heat view, the claim card. Extra: Free ramp (draw any ramp, no goals). tool.json `modes: ["Half-pipe", "Free ramp"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS3-1 | Log runs and graph kinetic energy against mass and against speed | the data drawer; two graphs | 2 |
| MS-PS3-2 | Change drop height and compare stored energy | the potential bar; the height marker | 3 |
| MS-PS3-5 | Run friction and brake tests and argue where the energy went | the thermal bar; the heat view; the claim card | 4 |

## Screens and modes
Header (kit): title "Half-Pipe Energy"; `Half-pipe`, `Free ramp`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A skate park at sunset, a smooth half-pipe, a skater in a helmet (illustrated, labeled "illustration") balanced at the top. Three empty bars on the right. The welcome is queued (`welcomeAfter: true`): "Where does a skater's speed come from, and where does it go? Tap Drop." First hint: "Tap Drop."

**Runs (focus: the skater and bars).** At 1366x768 the ramp fills the left with the bars and meters right; at 680x425 the bars sit in a strip above the ramp. The skater rolls; potential falls as kinetic rises; the total line stays level. Friction on: each pass is lower and thermal grows. The data drawer logs mass, height, top speed and top kinetic energy each run.

**Graphs (MS-PS3-1).** The student taps `Graph` and plots kinetic energy against mass (same height) and against speed (different heights). The first is a straight line; the second curves up. A card: "Twice the speed gave ___ times the energy."

**Height (MS-PS3-2).** The student moves the height slider; the potential bar at the start grows with height. A card: "The skater and Earth pull on each other. Farther apart means more energy stored."

**Brake test (MS-PS3-5).** The student drags a brake pad onto the flat; the skater stops; the kinetic bar empties into thermal; the heat view shows warm wheels and pad. Friction off: the skater rolls forever and thermal stays empty.

**The claim card (the aha).** "When the skater slowed, the energy went ___. My evidence: ___." Narrator: "Height stores energy, speed carries it, and when the skater slows down, the energy doesn't vanish. It warms the wheels and the ramp."

**The end.** Graphs, the brake test and the claim. `Print` prints them.

**Free ramp (extra).** Draw any ramp; bars still run.

## Content
- A stated ramp model with gravity 9.8, rolling friction, a brake, three bars with a total line, the data drawer, two graphs, the claim card. Units in joules, meters, kilograms, meters per second.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Sliders are locked during a run and free between runs.
- Keyboard: Tab to `Drop`, sliders, friction, the pen, `Graph`, the brake and the card; arrows move sliders; Enter acts.
- With Motion off the skater jumps between top, middle and bottom stills and bars update at each.

## Look
- Accent `--brand` #5b2a86 skate purple (header, the total line, sliders); gold #f4c542 (kinetic bar edge, the brake in hand); paper #f6f1fa; ink #1b0c28; muted #574e5f.
- Contrast (WCAG 2.1, computed): white on brand 9.90:1; brand on paper 8.91:1; ink on paper 16.71:1; muted on paper 7.10:1; ink on gold 11.43:1.
- Never color alone: bars carry names and numbers; the heat view carries a temperature scale.
- Different from this batch (storm slate, strawberry red, wave blue, pond green).

## Art
- People (illustrated): the skater, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the skate park at sunset (1, 16:9).
- Drawn in code: the ramp, bars, meters, graphs, the brake, the heat view.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as the skater; `bright-teacher` as the science guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `drop`: "Tap Drop."
- how `slider`: "Move the mass or height slider, then tap Drop."
- how `graph`: "Tap Graph, then tap a run to plot it."
- how `brake`: "Drag the brake pad onto the ramp."
- event, whole, the brake result.
- how `claim`: "Fill in the claim card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the ramp model, bars, graphs, the heat view. Model constants sit in a marked block `/* HALF-PIPE DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Graphs | Plot one run | Each graph needs four runs that vary only one thing. |
| Height | Skip the slider | The height card asks to compare two starts. |
| Claim | "It disappeared" | The card needs the thermal bar or the heat view as evidence. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `drop`; `slider`.
2. `graph`.
3. `brake`; brake result (whole), waits.
4. `claim`.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-PS3-1, MS-PS3-2, MS-PS3-5 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Kinetic energy is half the mass times speed squared | NASA Glenn Research Center, "Kinetic energy" | OpenStax, "College Physics 2e", chapter 7 | yes |
| Gravitational potential energy is mass times g times height | NASA Glenn Research Center, "Potential energy" | The Physics Classroom, "Potential energy" | yes |
| Friction turns kinetic energy into thermal energy | U.S. Energy Information Administration, "Forms of energy" | OpenStax, "College Physics 2e", chapter 7 | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r5, 2026-11-10): a 50 kg skater 3 m up stores about 1,470 joules and reaches about 7.67 m/s with no friction; twice the speed gives four times the kinetic energy and twice the mass gives twice; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 ramp and bars; at 680x425 strip.
2. Kinetic energy is graphed against mass and against speed from the student's runs. (MS-PS3-1)
3. Drop heights are compared for stored energy. (MS-PS3-2)
4. The brake test and claim show energy moving out as heat. (MS-PS3-5)
5. The total line stays level within 1 percent in every run.
6. No equations beyond the two cards; bar charts and graphs only.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: three stills per run; no network requests.

## Open questions
- Overlap risk with zipline-energy (default used: this tool stays with bar charts and proportional graphs; zipline-energy keeps friction and brakes in numbers).
