# Contraption Workshop

## One idea
A neighbor's job card asks for a wake-up machine that rings a bell across the workshop, and the student reads it to set the criteria (the bell rings, in under 10 seconds) and the limits (a $20 parts budget, the space on one wall), then builds a silly chain machine from a priced parts shelf where every link changes energy from one form to another (a battery runs a motor, a motor winds a string, a lamp shines on a solar cell, a solar cell runs a buzzer, a falling weight pulls a pin, a buzzer shakes a cup that tips a marble); test runs play in slow motion with an energy view that tags each link (stored, motion, electric, light, sound, heat) and shows energy traveling along wires, across a gap as light and through the air as sound, and a failed link glows with a broken mark; the student then runs fair tests on one link at a time (change only the ramp angle), sketches a second full design, compares the two on cost, time and how often they work, and refines the better one; at the end the finished machine replays with a labeled energy path from battery to bell next to the student's test log, so a fourth grader learns to design, test and refine a device that converts energy, sees energy carried by electric current, light, sound and heat, and practices defining a problem, comparing solutions and fair testing.

## Not like
- bowling-lab (4, spec): speed and energy in one collision. Here energy changing form along a chain.
- magnet-maze (3, spec): magnetic forces. Here many forms of energy.
- vibration-station (1, spec): one sound or light device. Here a chain of transfers.
- zipline-energy (11, spec): energy math on a line. Here building and testing.

## Who and how
- Grade 4, Science and Engineering, module "Energy Conversion Devices". Standards: 4-PS3-4 (apply scientific ideas to design, test, and refine a device that converts energy from one form to another), 4-PS3-2 (make observations to provide evidence that energy can be transferred from place to place by sound, light, heat, and electric currents; moved here from bowling-lab), 3-5-ETS1-1 (define a simple design problem reflecting a need or a want that includes specified criteria for success and constraints on materials, time, or cost), 3-5-ETS1-2 (generate and compare multiple possible solutions to a problem based on how well each is likely to meet the criteria and constraints of the problem), 3-5-ETS1-3 (plan and carry out fair tests in which variables are controlled and failure points are considered to identify aspects of a model or prototype that can be improved).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- The job card, twelve priced parts, the energy view with six tags, slow-motion test runs, the fair test bench, two designs side by side, the test log. Extra: Machine code (share a code so a friend can load the machine and beat it). tool.json `modes: ["Workshop", "Machine code"]`, `minutes: "30-40"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3-5-ETS1-1 | Set criteria and limits from the job card | the filled job card | 2 |
| 4-PS3-4 | Build a chain whose links change energy form and run it | the machine; the energy tags | 3 |
| 4-PS3-2 | Watch energy travel by wire, light, sound and heat between links | the energy view | 3 |
| 3-5-ETS1-3 | Change one link at a time and find the failure point | the fair test bench; the log | 4 |
| 3-5-ETS1-2 | Compare two full designs on cost, time and reliability | the side-by-side table | 5 |

## Screens and modes
Header (kit): title "Contraption Workshop"; `Workshop`, `Machine code`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A workshop wall, a bell on the far side, a parts shelf with price tags and a job card from a neighbor. The welcome is queued (`welcomeAfter: true`): "Your neighbor needs a wake-up machine. Read the job card first. What must it do, and what are the limits? Tap the job card." First hint: "Tap the job card."

**Define (3-5-ETS1-1).** The job card has blanks. The student picks criteria (the bell rings; under 10 seconds; works three runs out of three) and limits ($20 budget, one wall, no water). The card locks when both are set.

**Build (focus: the wall).** At 1366x768 the wall fills the left with the shelf and budget right; at 680x425 the shelf is a sheet. Twelve parts with prices: battery, wires, switch, motor, lamp, solar cell, buzzer, cup, marble and ramp, string and pulley, weight, spring. Parts snap to the wall and connect by wire, string or a gap.

**Test runs (4-PS3-4, 4-PS3-2).** `Run` plays the chain in slow motion. The energy view tags each link (stored, motion, electric, light, sound, heat) and draws energy moving: along wires, as a beam across a gap, as rings of sound to a cup, as a faint glow of heat at the motor. A failed link shows a broken mark and a reason ("the lamp is too far from the solar cell").

**Fair tests (3-5-ETS1-3).** The bench takes one link and lets the student change one setting (lamp distance, ramp angle, weight size) while the rest stay locked. A table logs each try. The weak point gets fixed.

**Two designs (3-5-ETS1-2).** A second wall lets the student sketch a different chain. A side-by-side table compares cost, time and runs that worked out of three. The student picks the better design and refines it.

**The replay (the aha).** The finished machine replays with a labeled energy path from battery to bell next to the test log. Narrator: "Energy didn't disappear. It changed form at every link and traveled all the way to the bell."

**The end.** The job card, the energy path and the test log. `Print` prints them.

**Machine code (extra).** A short code loads a machine for a friend to beat on cost or time.

## Content
- Twelve parts with prices and stated behavior, the energy tags, the fair test bench, the comparison table, the job card.
- Batteries, lamps and buzzers are shown as safe classroom parts; no wall outlets.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Parts can be moved between runs; the budget updates at once.
- Keyboard: Tab to the shelf, wall spots, connectors, `Run` and the bench; arrow keys move the held part; Enter places.
- With Motion off runs show each link's before and after picture with its tag.

## Look
- Accent `--brand` #126b6b workshop teal (header, the budget, the energy path); gold #f4c542 (the part in hand, energy moving); paper #eef7f7; ink #062222; muted #4c5b5b.
- Contrast (WCAG 2.1, computed): white on brand 6.29:1; brand on paper 5.77:1; ink on paper 15.31:1; muted on paper 6.53:1; ink on gold 10.25:1.
- Never color alone: energy tags carry words and icons; a failed link carries a broken mark and a reason.
- Different from this batch (civic blue, canyon rust, dusk purple, moss green).

## Art
- Local FLUX (`scripts/localart.py`): the workshop wall (1, 16:9), the neighbor's job card scene (1, 4:3).
- Drawn in code: all twelve parts, wires, strings, the energy view, the bench and tables.
About 2 images.

## Voice
Two bank voices, each unique in this batch: `playful-friend` as the neighbor; `clear-teacher` as the shop guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `define`: "Pick what the machine must do and its limits."
- how `build`: "Drag a part to the wall."
- how `run`: "Tap Run."
- event, whole, a failed link's reason.
- how `test`: "Change one setting, then tap Test."
- how `compare`: "Build a second design to compare."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: parts, connections, the chain runner, the energy view, the fair test bench.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Define | Skip the job card | `Run` stays off until criteria and limits are set. |
| Build | Wire the battery straight to the bell | The job card asks for at least four links that change energy form. |
| Fair test | Change two things at once | The bench locks all but one setting. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `define`; `build`.
2. `run`; failed link (whole), waits.
3. `test`; `compare`.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for 4-PS3-4, 4-PS3-2 and 3-5-ETS1-1 to 3 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Forms of energy and how they change (stored, motion, electric, light, sound, heat) | U.S. Energy Information Administration, "Energy Kids: Forms of energy" | NASA Glenn Research Center, "Energy" | yes |
| Solar cells change light to electricity; motors change electricity to motion | National Renewable Energy Laboratory, "Solar photovoltaic basics" | U.S. Department of Energy, "How does solar work" | yes |
| Fair tests change one variable at a time | NGSS Appendix I, "Engineering Design" | National Science Teaching Association, "Fair test" guidance | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad r29, 2026-11-09): twelve parts; six energy tags; three runs of three for reliability; a four-link chain priced at battery 4, motor 5, lamp 3, solar cell 6 dollars is 18 dollars and fits the 20 dollar budget; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 wall and shelf; at 680x425 sheet.
2. Criteria and limits are set from the job card before any run. (3-5-ETS1-1)
3. A chain of at least four energy-changing links runs, with energy shown moving by wire, light, sound and heat. (4-PS3-4, 4-PS3-2)
4. A failure point is found by changing one setting at a time. (3-5-ETS1-3)
5. Two designs are compared on cost, time and reliability. (3-5-ETS1-2)
6. Only safe classroom parts are shown.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: before and after pictures; no network requests.

## Open questions
None.
