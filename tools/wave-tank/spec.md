# Wave Tank

## One idea
A glass-sided water tank has a paddle at one end, amplitude and frequency sliders, a ruler, a timer and a cork floating halfway; the student wiggles the paddle and measures wavelength, frequency and height, and notices the cork bobs up and down but doesn't travel, so waves carry energy, not water; a wave-energy meter shows energy growing with amplitude (twice as tall carries four times the energy), and the student plots their own data and checks that speed equals frequency times wavelength (2 waves a second that are 0.5 m long move 1 m a second); then the same sliders run a rope and a light beam; next the student drops blocks into each wave's path (a wall, a sponge and a gap for water waves; a mirror, glass, water and black cloth for light; tile and foam for sound) and records whether each wave bounces back, passes through or fades out; at the end a summary table filled from the student's own tests holds what each material does to each wave and how amplitude relates to energy, so an eighth grader learns to use a simple model of waves to describe how amplitude relates to energy, and to describe how waves are reflected, absorbed or transmitted through different materials.

## Not like
- copy-of-a-copy (8, spec): waves carrying a message. Here the wave itself.
- spectrum-explorer (11, spec): the whole range of light. Here light, water and sound meeting materials.
- secret-code-signals (4, spec): patterns that carry codes. Here what makes a wave.
- field-lines (11, live): invisible fields. Here waves you can see and measure.

## Who and how
- Grade 8, Science, module "Waves". Standards: MS-PS4-1 (use mathematical representations to describe a simple model for waves that includes how the amplitude of a wave is related to the energy in a wave), MS-PS4-2 (develop and use a model to describe that waves are reflected, absorbed, or transmitted through various materials).
- Format: sandbox. Driver: one student alone, or a teacher leading the class (tool.json `driver: "either"`). `Read` reads every card. Controls 48 px or more.
- Three wave setups (tank, rope, light beam, plus sound in the block step), two sliders, ruler, timer, cork, energy meter, a data plot, nine material blocks, the summary table. Extra: Free tank (no goals at all). tool.json `modes: ["Tank", "Free tank"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| MS-PS4-1 (model) | Measure wavelength, frequency and height; check speed | the ruler; the timer; the cork | 2 |
| MS-PS4-1 (energy) | Change amplitude and plot energy | the energy meter; the plot | 3 |
| MS-PS4-2 | Put materials in each wave's path and fill the table | reflected, passed or faded waves; the summary table | 4 |

## Screens and modes
Header (kit): title "Wave Tank"; `Tank`, `Free tank`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A long glass tank on a lab bench, a paddle at the left, a cork floating in the middle, a ruler along the glass. The welcome is queued (`welcomeAfter: true`): "Does a wave carry water, or something else? Watch the cork. Tap the paddle." First hint: "Tap the paddle to start the waves."

**Measuring (focus: the tank).** At 1366x768 the tank fills the top with sliders and the data table below; at 680x425 the table is a sheet. The student drags markers to two crests to read the wavelength, taps the timer for ten waves to get frequency, and drags a marker to the crest height for amplitude. The cork bobs in place; a card: "The cork goes up and down, not along. The wave moves energy, not water."

**Energy.** The energy meter grows as amplitude rises. The student logs four runs and taps `Plot`: energy against amplitude curves up. A card: "Twice as tall, ___ times the energy." Then speed: the student fills frequency times wavelength and checks it against a dot timed across the tank.

**Rope and light.** The same sliders run a rope tied to a post and a light beam from a lamp (frequency shown as color with its name).

**Blocks (MS-PS4-2).** The student drags blocks into the path. Water: a wall (bounces back), a sponge (fades out), a gap (passes through and spreads). Light: a mirror (bounces), glass and water (passes through and bends), black cloth (fades out, the cloth warms). Sound: tile (bounces, echo), foam (fades). Each test adds a row to the summary table with reflected, transmitted or absorbed.

**The table (the aha).** Narrator: "Every wave carries energy. Bigger waves carry a lot more. And what a wave hits decides whether that energy bounces, goes through or gets soaked up."

**The end.** The plot and the summary table. `Print` prints them.

**Free tank (extra).** All setups, all blocks, no goals.

## Content
- A wave model (speed set by medium, energy proportional to amplitude squared), three setups, nine blocks with stated behavior, the plot, the summary table. Sound tests show a waveform picture so they work with Sound off.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Markers snap to crests within a few pixels.
- Keyboard: Tab to the paddle, sliders, markers, timer, `Plot`, setups and blocks; arrows move sliders and markers; Enter acts.
- With Motion off waves show as still snapshots with arrows and the cork's path as a line.

## Look
- Accent `--brand` #135d7a wave blue (header, the wave line, the table); gold #f4c542 (markers, the block in hand); paper #eef5f8; ink #071d26; muted #4a5960.
- Contrast (WCAG 2.1, computed): white on brand 7.31:1; brand on paper 6.63:1; ink on paper 15.71:1; muted on paper 6.59:1; ink on gold 10.65:1.
- Never color alone: light frequency shows its color name; table cells carry words.
- Different from this batch (skate purple, storm slate, strawberry red, pond green).

## Art
- Local FLUX (`scripts/localart.py`): the lab bench with the tank (1, 16:9).
- Drawn in code: water, the rope, the light beam, blocks, the cork, markers, plots, the table.
About 1 image.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `upbeat-guide` as the lab guide and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.setup + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `measure`: "Drag the markers to two crests."
- how `time`: "Tap the timer, then tap again after ten waves."
- how `plot`: "Move the amplitude slider, then tap Plot."
- how `block`: "Drag a block into the wave's path."
- event, whole, each block result.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the wave model, markers, blocks, the plot. Block behaviors sit in a marked block `/* WAVE-TANK DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Measuring | Guess values | Markers must sit on crests; the timer reads real taps. |
| Plot | Plot one point | `Plot` needs four amplitudes. |
| Table | Fill rows by guess | Rows fill only from tests run. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `measure`; `time`.
2. `plot`.
3. `block`; block result (whole), waits.
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| NGSS wording for MS-PS4-1, MS-PS4-2 | NGSS Lead States, "Next Generation Science Standards" (2013) | data/standards/ngss-pes.txt | yes |
| Waves carry energy, not matter; water bobs in place | NOAA Ocean Service, "What is a wave?" | The Physics Classroom, "Waves" | yes |
| Speed equals frequency times wavelength | NASA Science, "Anatomy of an electromagnetic wave" | OpenStax, "College Physics 2e", chapter 16 | yes |
| Wave energy is proportional to amplitude squared | OpenStax, "College Physics 2e", chapter 16 | The Physics Classroom, "Energy transport and amplitude" | yes |
| Materials reflect, transmit or absorb light and sound | NASA Science, "Reflected near-infrared waves" and wave behaviors | Acoustical Society of America, "Sound absorption" education page | yes |
Backed twice: 5. Cut: 0.

Checks run (Python, scratchpad r5, 2026-11-10): 2 waves a second at 0.5 m long move 1 m a second; twice the amplitude carries four times the energy; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 tank and table; at 680x425 sheet.
2. Wavelength, frequency and height are measured and speed checked. (MS-PS4-1)
3. Energy is plotted against amplitude from four runs. (MS-PS4-1)
4. Blocks are tested for water, light and sound and the table filled. (MS-PS4-2)
5. Model behavior matches the cited sources.
6. Sound tests work with Sound off.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: snapshots and paths; no network requests.

## Open questions
- Code move: the idea card moves MS-PS4-3 to copy-of-a-copy (default used: this tool teaches MS-PS4-1 and MS-PS4-2).
