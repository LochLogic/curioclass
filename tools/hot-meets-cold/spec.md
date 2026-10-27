# Hot Meets Cold

## One idea
Drop a hot metal block into a cup of cold water, predict where the two temperatures meet, then zoom into the wall
between them: jiggling particles pass energy both ways, but more goes from hot to cold every time, so the temperatures
always meet in between and no setting you try makes the heat flow back.

## Not like
- slope-field-garden (gr 12 math, wave 2), cooling cocoa: the differential equation dT/dt = −k(T − 20) and its
  slope field. Here the physics: two objects, energy conserved between them, heat capacity deciding where they meet,
  and particles explaining why heat only flows one way.
- hand-warmer-lab (gr 10 chemistry, this wave): energy released by a reaction, measured as a temperature rise. Here no
  reaction: energy moves from one object to another and the total stays fixed.
- gas-law-lab (gr 10 chemistry, particles family): pressure, volume and temperature of a gas. Here particles only
  trade energy across a wall; no gas laws.
- body-thermostat (gr 9 biology): feedback that holds body temperature. Here no control loop; equilibrium just
  happens.
- zipline-energy (this group): energy changing form (height, motion, heat from friction). Here thermal energy moving
  between objects.

## Who and how
Grade 11, physics (Heat and Thermal Equilibrium). Students drive, 20 to 35 minutes. Explore first: Cup opens with an
aluminum block at 100 °C over 200 g of water at 20 °C, ready to drop.
Standards: HS-PS3-4.
tool.json: driver "students", minutes "20-35", modes ["Cup", "Particles", "Dare"].

## Screens and modes
Header (kit, 9-12 theme): "Hot Meets Cold", small line "Heat flows one way." Modes `Cup`, `Particles`, `Dare`; kit
`Motion`, `Sound`, `Read`.

Panel (Cup and Dare): Block material buttons (Aluminum, Copper, Iron, Lead, Gold, Silver, Granite, Glass), Block
mass (50 to 500 g, step 5, default 200), Block temperature (0 to 100 °C, step 1, default 100), Water mass (100 to 500
g, step 10, default 200), Water temperature (5 to 80 °C, step 1, default 20). Readout of each heat capacity: "block
C = m × c = 180 J/°C", "water C = 837 J/°C".

### Cup (explore, default)
Stage: a foam cup (calorimeter) with a lid, a thermometer in the water, the block hanging above on a string with its
own thermometer probe, a lab clock. Under it, a temperature against time plot (0 to 300 s) with the block line and the
water line.
- `Predict` box "Final temperature (°C)" (optional) and `Drop` (Space). The block drops in; both lines move toward
  each other and level off; the clock runs 10 lab seconds per real second (`x1` toggle for real time).
- Energy ledger under the plot, live: "block gave ... J", "water got ... J", "total ... J" (always equal while the lid
  is on). After the run: "Your prediction 35, final 34.16 °C."
- `Lid off` toggle: the cup now leaks to a 22 °C room; the ledger adds "room got ... J" and the final temperature
  drifts toward 22 over minutes. Note: "Lid on is a closed system."
- `Again` lifts the block out and restores the start temperatures; `Lab book` adds the run to a table (material,
  masses, start temperatures, prediction, final, energy moved) with `Copy table`.

### Particles
Stage: a box split by a thin wall, block particles on the left, water particles on the right, each particle a dot that
jiggles faster and glows hotter with more energy. Under it, three bars: "energy passed hot to cold", "energy passed
cold to hot", "net"; and a plot of each side's average energy (shown as a temperature) over time.
- Particle count `12`, `60`, `300` (default 60). The split between sides follows the two heat capacities, so the
  meeting point matches Cup.
- `Start` (Space), `Pause`, `Restart`; `Slow` toggle (one exchange per frame, the pair flashes).
- Strip under the bars: "Energy goes both ways. More goes from hot to cold." With 12 particles a note may appear: "For
  a moment the cold side got ahead. With 7 million billion billion particles in a real cup, you would never see it."

### Dare
Cards D1 to D5 (Content), each asking for a setting. The student sets the panel, presses `Drop` and the card checks.
D3 is a dare that cannot be won; after three tries it opens the explanation.

## Content
Model: final temperature T_f = (C_b T_b + C_w T_w) / (C_b + C_w), C = mass × specific heat. Energy moved Q = C_b (T_b
− T_f). Exchange while running: power P = hA (T_b − T_w) with hA = 5 W/°C (lab setting), so the gap closes with rate
hA (1/C_b + 1/C_w). Lid off adds a leak from the water to a 22 °C room at 0.5 W/°C (lab setting). Ranges keep the water
liquid (no boiling, no ice). Left out (said on screen): the cup's own heat capacity, evaporation, the string.

Specific heats (J/kg·°C, OpenStax College Physics 2e, Table 14.1): aluminum 900, copper 387, iron 452, lead 128, gold
129, silver 235, granite 840, glass 840, water 4186.

Check values (200 g block at 100 °C into 200 g water at 20 °C unless stated):
| Case | Final (°C) | Energy moved (J) | Time constant (s) |
|---|---|---|---|
| Aluminum | 34.16 | 11,852 | 29.6 (99 percent by 136 s) |
| Copper | 26.77 | 5,668 | 14.2 |
| Iron | 27.80 | 6,527 | 16.3 |
| Lead | 22.37 | 1,987 | 5.0 |
| Gold | 22.39 | 2,002 | 5.0 |
| Silver | 24.25 | 3,560 | 8.9 |
| Granite or glass | 33.37 | 11,194 | 28.0 |
| 300 g granite | 38.51 | 15,496 | 38.7 |
| 200 g aluminum at 0 °C into 60 °C water | 49.38 | 8,889 into the block | 29.6 |
| 465 g aluminum, 100 g water | 60.00 | 16,742 | 41.9 |
| 50 g copper, 500 g water | 20.73 | 1,534 | 3.8 |
| block and water both 40 °C | 40.00 | 0 | none |

Particles: a kinetic exchange model. Each particle holds an energy in kelvin units; a step picks a random pair (two in
the block, two in the water, or one on each side of the wall at a lower rate) and splits their total at a random
fraction. Sides' particle counts N_b = max(3, round(N × C_b / (C_b + C_w))). The average energy of each side is shown
as its temperature. Over time every particle averages the same energy, which is why both sides meet. A real 200 g of
water holds about 6.7 × 10^24 molecules (200 g / 18.015 g/mol × 6.022 × 10^23).

Dare cards:
- D1 "Meet in the middle": aluminum at 100 °C, 100 g water at 20 °C. Make the final 60.00 °C. Answer 465 g
  (equal heat capacities, 418.5 and 418.6 J/°C; 460 g gives 59.78 and 470 g gives 60.21).
- D2 "Five degrees": copper at 100 °C, 500 g water at 20 °C. Smallest block that warms the water at least 5 °C. Answer
  365 g (25.06 °C; 360 g gives 24.99).
- D3 "Uphill heat" (cannot be won): make the water end hotter than the block started, or the block end colder than the
  water started. Explanation after three tries: the final always lies between the two starting temperatures.
- D4 "No flow": find a setting where no energy moves. Answer: equal starting temperatures.
- D5 "Best warmer": 200 g blocks at 100 °C into 200 g water at 20 °C. Which material warms the water most? Aluminum
  (34.16 °C), because its specific heat is highest.

## Interactions in detail
- Cup integrates the two-object exchange exactly (closed form exponential for lid on; small steps, 0.05 lab seconds,
  for lid off) and the final number shown is the closed form value to 2 decimals.
- Prediction is optional; a typed value within 0.5 °C reads "close"; outside it reads the gap, never "wrong".
- Slider changes during a run stop the run and reset; `Drop` is disabled while the block is in the water.
- Particles: 60 exchanges per frame at normal speed; the wall pair rate is one tenth of the inside rate so each side
  mixes before it trades. Seeded random (`Restart` reseeds). Bars count only wall exchanges. Block particles start at
  the block temperature and water particles at the water temperature (in kelvin), all equal within a side.
- Few particles jiggle a lot (a side's average swings by about 1 / √N of itself), so the plot shows each side's
  average smoothed over the last 3 s as a bold line, with the raw average as a faint line. The panel shows the
  particle model's own meeting point, the count-weighted average (60 particles at the default: 11 block and 49 water,
  34.67 °C against Cup's 34.16; 300 particles: 53 and 247, 34.13 °C; 12 particles: 3 and 9, 40.00 °C), with the note
  "rounded to whole particles".
- Extremes: block and water at equal temperatures give flat lines and "No energy moves: they are already in balance."
- Sound: a soft fizz at the drop, a ticking clock while running; off with Sound.
- Keyboard: Space = Drop or Start, R = Again or Restart, material buttons in Tab order, arrows on sliders.
- Layout by real stage pixels: wide (cup beside plot), compact, stack (375 wide: plot under the cup, ledger folds).
- Mode change: `Curio.stop()`, `V.hush()`. Lab book and passed dares per device (localStorage `curio-hot-meets-cold`,
  try/catch), `Clear lab book`.

## Look
Accent (`--brand`) #ff8f5e, ember orange: 7.70:1 on --panel #141b25, 7.30:1 on --sec-bg #18202b; --brand-ink #10161f
on it 8.08:1. Group siblings are far from it (curling #ff7a8f is the closest at ΔE 34); nearest 9-12 accents are in
other subjects (captain-s-log #ff8f6b, undo-machine #e98a4c).
Scene: lab bench #2a2f36, foam cup #e9e4da with a shadow #b8b2a6, water #4f8fd0 at 70 percent, metal blocks in their
own colors (aluminum #b8c0c8, copper #c8784a, iron #6c7078, lead #7a8088, gold #d8b440, silver #d0d4d8, granite
#8a8580 flecked, glass #bfe0e8 at 60 percent). Particle glow from blue #5aa9ff (cold) to the accent (hot). Block line
`--gr-4`, water line `--gr-1`.

## Art
none: drawn in code (cup, blocks, thermometers, particles, plots, preview.svg).

## Voice
`clear-teacher` (Iapetus), style "Say clearly and kindly, like a patient physics teacher at the lab bench." No 9-12
science tool uses it. `Curio.voice`, `scope: () => state.mode`.
- cup (how, Cup welcome): "Guess where the two temperatures will meet, then press Drop."
- ledger (how, first run ends): "Look at the ledger. What the block gave, the water got."
- balance (event, equal start temperatures dropped; stale on any slider change): "Already in balance. Nothing moves."
- particles (how, Particles welcome): "Press Start. Watch the bars: energy crosses both ways."
- backward (event, first moment the cold side gets ahead with 12 particles; stale on Restart): "There, the cold side got ahead for a moment. Keep watching."
- dare (how, Dare welcome): "Each card asks for a setting. One of them cannot be done."
- uphill (event, D3 explanation opens; stale on a new card): "The meeting point is always in between. Heat does not run uphill on its own."

## Family engine
none. Plots use `kit/graphing.js` `Plane` if present (`g.fn` for the closed form curves, `g.trace` for the particle
averages); otherwise the tool's own SVG.

## Sources
- Specific heats: OpenStax, College Physics 2e (2022), Table 14.1,
  https://openstax.org/books/college-physics-2e/pages/14-2-temperature-change-and-heat-capacity
- Heat transfer to equilibrium, conservation of energy in calorimetry, the second law: OpenStax, College Physics 2e,
  14.4 "Heat Transfer Methods" and 15.3 "Introduction to the Second Law of Thermodynamics".
- Kinetic exchange model of energy sharing: Dragulescu and Yakovenko 2000, "Statistical mechanics of money", European
  Physical Journal B 17:723 (random pairwise splits give an exponential, Boltzmann-like distribution).
- Avogadro constant 6.02214076 × 10^23 per mol: NIST, https://physics.nist.gov/cgi-bin/cuu/Value?na ; water molar
  mass 18.015 g/mol: PubChem, https://pubchem.ncbi.nlm.nih.gov/compound/Water
- NGSS HS-PS3-4 evidence statement (closed system, uniform final temperature), https://www.nextgenscience.org/
- hA and the room leak are lab settings; every check value computed in Python (2026-10-27).

## Done when
1. Default drop ends at 34.16 °C with "block gave 11,852 J", "water got 11,852 J"; the lines reach 99 percent of the
   way by 136 lab seconds.
2. Copper ends at 26.77, lead at 22.37, 300 g granite at 38.51.
3. 200 g aluminum at 0 °C into 60 °C water ends at 49.38 °C with energy moving into the block.
4. Equal start temperatures: flat lines, 0 J, the balance line spoken.
5. Lid off: the final drifts below 34.16 toward 22 °C and the ledger shows "room got" energy.
6. Particles with 60: the "hot to cold" bar always ends larger than "cold to hot"; after 60 s both smoothed averages
   sit within 3 °C of the panel's meeting point (34.67 °C at the default).
7. D1 accepts 465 g (60.00 °C); D2 accepts 365 g and rejects 360 g; D3 cannot be passed and explains after three tries.
8. How-to lines once each; event lines as listed.
9. Cup, plot and ledger visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the 680x425
   preview; no network, no images, no em dashes.

## Open questions
- [hot-meets-cold] With 12 particles the cold side can briefly get ahead, which looks like heat flowing back. The spec
  shows it and explains it as a small-number effect (the concept says "no setting ever makes the heat flow back"). Keep
  that honesty note, or lock Particles to 60 and 300 so it never shows?
