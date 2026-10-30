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
`Motion`, `Sound`, `Read` (Sound starts on as the kit sets it).

Panel (Cup and Dare): Block material buttons, each with its painted block (Aluminum, Copper, Iron, Lead, Gold, Silver,
Granite, Glass), Block mass (50 to 500 g, step 5, default 200), Block temperature (0 to 100 °C, step 1, default 100),
Water mass (100 to 500 g, step 10, default 200), Water temperature (5 to 80 °C, step 1, default 20). Readout of each
heat capacity: "block C = m × c = 180 J/°C", "water C = 837 J/°C".

### Cup (explore, default)
Focus: the temperature plot, the largest thing, centre right; the cup scene sits at its left at about two thirds of
its width, so the student sees the two lines meet while the thermometers move.
Stage: the painted lab table (hmc-bench) with the painted foam cup (hmc-cup) and its lid (hmc-lid), a painted
thermometer in the water, the painted block hanging above on a string (code line) with its own painted thermometer,
and the painted lab timer (hmc-timer). Thermometer columns, the timer's hands and all numbers are drawn in code.
Beside it, a temperature against time plot (0 to 300 s) with the block line and the water line.
- `Predict` box "Final temperature (°C)" (optional) and `Drop` (Space). The block drops in; both lines move toward
  each other and level off; the clock runs 10 lab seconds per real second, so a run takes 30 s (`x1` toggle for real
  time, 5 minutes, for classes timing with a real clock).
- While the block is in, the cup's front fades to 35 percent so the block and the code-drawn water show inside.
- Energy ledger under the plot, live: "block gave ... J", "water got ... J", "total ... J" (always equal while the lid
  is on). After the run: "Your prediction 35, final 34.16 °C."
- `Lid off` toggle: the lid lifts off; the cup now leaks to a 22 °C room; the ledger adds "room got ... J" and the
  final temperature drifts toward 22 over minutes. Note: "Lid on is a closed system."
- `Again` lifts the block out and restores the start temperatures; `Lab book` adds the run to a table (material,
  masses, start temperatures, prediction, final, energy moved) with `Copy table`.

### Particles
Focus: the particle box, the largest thing, centred; the bars and the plot sit under it.
Stage: a box split by a thin wall, block particles on the left, water particles on the right, each particle a dot that
jiggles faster and glows hotter with more energy. Under it, three bars: "energy passed hot to cold", "energy passed
cold to hot", "net"; and a plot of each side's average energy (shown as a temperature) over time.
- Particle count `12`, `60`, `300` (default 60). The split between sides follows the two heat capacities, so the
  meeting point matches Cup.
- `Start` (Space), `Pause`, `Restart`; `Slow` toggle (one exchange per frame, the pair flashes).
- Strip under the bars: "Energy goes both ways. More goes from hot to cold." With 12 particles a note may appear: "For
  a moment the cold side got ahead. With 7 million billion billion particles in a real cup, you would never see it."

### Dare
Focus: the dare card at the top of the stage and the cup scene under it, as in Cup.
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
- Controls stay live during a run: a slider or material change stops the run at once and resets to the new start
  (the block lifts out in the same frame); `Lid off` and `x1` act on the next frame without a reset. `Drop` is
  disabled while the block is in the water, so no line names it then.
- Particles: 60 exchanges per frame at normal speed; the wall pair rate is one tenth of the inside rate so each side
  mixes before it trades. Seeded random (`Restart` reseeds). Bars count only wall exchanges. Block particles start at
  the block temperature and water particles at the water temperature (in kelvin), all equal within a side. Particles
  run until `Pause`; a count change or `Slow` acts at once (a count change restarts with the new count).
- Few particles jiggle a lot (a side's average swings by about 1 / √N of itself), so the plot shows each side's
  average smoothed over the last 3 s as a bold line, with the raw average as a faint line. The panel shows the
  particle model's own meeting point, the count-weighted average (60 particles at the default: 11 block and 49 water,
  34.67 °C against Cup's 34.16; 300 particles: 53 and 247, 34.13 °C; 12 particles: 3 and 9, 40.00 °C), with the note
  "rounded to whole particles".
- Painted blocks: one cutout per material; drawn at a size that grows with the cube root of the block's mass (the
  same rule for every material), from 50 g at 40 px to 500 g at 86 px on a 1366x768 stage.
- Extremes: block and water at equal temperatures give flat lines and "No energy moves: they are already in balance."
- Sound: a soft fizz at the drop, a ticking clock while running; off with Sound.
- Keyboard: Space = Drop or Start, R = Again or Restart, material buttons in Tab order, arrows on sliders.
- Layout by real stage pixels: wide (cup beside plot), compact, stack (375 wide: plot under the cup, ledger folds).
- Mode change: `Curio.stop()`, `V.hush()`. Lab book and passed dares per device (localStorage `curio-hot-meets-cold`,
  try/catch), `Clear lab book`.

## Look
Accent (`--brand`) #ff8f5e, ember orange: 7.70:1 on --panel #141b25, 7.30:1 on --sec-bg #18202b; --brand-ink #10161f
on it 8.08:1. Group siblings are far from it (curling #ff7a8f is the closest at ΔE 34; circuit-builder moved off
copper to stay clear of it); nearest 9-12 accents are in other subjects (captain-s-log #ff8f6b, undo-machine #e98a4c).
Scene: the painted maple table and warm window light (the only warm wooden bench in this batch). Code colors on top:
water #4f8fd0 at 70 percent, thermometer column #e0442c. Particle glow from blue #5aa9ff (cold) to the accent (hot).
Block line `--gr-4`, water line `--gr-1`.

## Art
Local FLUX (`scripts/localart.py`). No people anywhere. 13 images.
- hmc-bench: a pale maple wood lab table seen from the front at eye level, a tall window with warm afternoon light
  behind it, a softly blurred pegboard wall; 16:9; cutout no; people no; the Cup and Dare backdrop.
- hmc-cup: a plain white foam cup, side view, soft studio light, on a plain white background; 3:4; cutout yes; people
  no; the calorimeter (its front fades while the block is in).
- hmc-lid: a plain white plastic cup lid with a small round hole in the middle, side view, on a plain white
  background; 4:1; cutout yes; people no; sits on the cup, lifts off with Lid off.
- hmc-thermo: a slim glass lab thermometer with a red bulb and a smooth unmarked stem, upright, on a plain white
  background; 9:16; cutout yes; people no; used twice (water and block), the column and scale drawn in code.
- hmc-timer: a round white lab timer clock with a plain blank face and a chrome rim, front view, on a plain white
  background; 1:1; cutout yes; people no; the lab clock, hands in code.
- Block kit (one shared prompt line, each a separate cutout, 1:1, people no): "a single solid cube of one material
  with a small steel hook on top, three-quarter view, studio light, on a plain white background", pieces:
  hmc-aluminum (brushed silver aluminum), hmc-copper (polished reddish copper), hmc-iron (dark gray cast iron, lightly
  rough), hmc-lead (dull blue-gray lead), hmc-gold (gleaming yellow gold), hmc-silver (bright polished silver),
  hmc-granite (speckled pink, black and gray granite), hmc-glass (a clear glass cube catching the light). Sizing rule
  in Interactions; on the material buttons each fits the same 40 px box.
Drawn in code: water, thermometer columns and scales, timer hands, the string, plots, ledger, the whole Particles
mode (box, wall, dots, bars), preview.svg.

## Voice
`clear-teacher` (Iapetus), style "Say clearly and kindly, like a patient physics teacher at the lab bench." No grade
10 or 11 science neighbor or batch sibling uses it; feedback-loop-builder (grade 9) does. `Curio.voice`,
`scope: () => state.mode`. Hints change at once on every mode or state change; lines queue with a `valid` check.
- cup (how; Cup welcome; stale once Drop is pressed): "Type your guess in Predict if you like, then press Drop."
- ledger (how; first run ends; stale on Again): "Look at the ledger. What the block gave, the water got."
- balance (event; a drop with equal start temperatures; stale on any slider change): "Already in balance. Nothing
  moves."
- particles (how; Particles welcome; stale once Start is pressed): "Press Start. Watch the bars: energy crosses both
  ways."
- backward (event; first moment the cold side gets ahead with 12 particles; stale on Restart): "There, the cold side
  got ahead for a moment. Keep watching."
- dare (how; Dare welcome; stale once a card is checked): "Set the panel to match the card, then press Drop. One card
  cannot be done."
- uphill (event; D3 explanation opens; stale on a new card): "The meeting point is always in between. Heat does not
  run uphill on its own."

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
- hA and the room leak are lab settings.
- Number checks (Python, 2026-10-29): every row of the check table matched (finals, energies and time constants);
  99 percent by 136.3 lab s; D1 465 g gives 60.00 (460 g 59.78, 470 g 60.21); D2 360 g 24.99 and 365 g 25.06; particle
  splits 3/9, 11/49, 53/247 with meeting points 40.00, 34.67, 34.13; 6.69 × 10^24 molecules. Worst cases: hottest
  possible final 54.22 °C (500 g aluminum, 100 g water at 5 °C) and a block colder than the water (0 °C lead into
  80 °C water) both stay between the start temperatures, as D3 needs. Lid off: the two time constants are 29.5 and
  2,041 lab s; at 300 lab s the water reads 32.64 °C (1.5 °C under the lid-on 34.16), so the drift shows in a 30 s
  run. No values changed.

## Done when
1. Default drop ends at 34.16 °C with "block gave 11,852 J", "water got 11,852 J"; the lines reach 99 percent of the
   way by 136 lab seconds; the run takes about 30 s.
2. Copper ends at 26.77, lead at 22.37, 300 g granite at 38.51.
3. 200 g aluminum at 0 °C into 60 °C water ends at 49.38 °C with energy moving into the block.
4. Equal start temperatures: flat lines, 0 J, the balance line spoken each time.
5. Lid off: the lid lifts, the final drifts below 34.16 toward 22 °C and the ledger shows "room got" energy.
6. Particles with 60: the "hot to cold" bar always ends larger than "cold to hot"; after 60 s both smoothed averages
   sit within 3 °C of the panel's meeting point (34.67 °C at the default).
7. D1 accepts 465 g (60.00 °C); D2 accepts 365 g and rejects 360 g; D3 cannot be passed and explains after three tries.
8. Focus: the plot is the largest thing in Cup and the particle box in Particles, at 1366x768 and in the 680x425
   preview.
9. A tap while a run plays: moving a slider stops it and resets in the same frame; in Particles, Pause stops the next
   frame and a count change restarts at once.
10. How-to lines once each per load, then hint only; event lines each time; no line names Drop while it is disabled.
11. All 13 images load, none shows a person; the block's size grows with mass and its button picture matches.
12. Cup, plot and ledger visible at 1366x768; stacked at 760 and 375 wide; labels at least 10 px in the 680x425
    preview; no network, no em dashes.

## Open questions
- [hot-meets-cold] With 12 particles the cold side can briefly get ahead, which looks like heat flowing back. The spec
  shows it and explains it as a small-number effect (the concept says "no setting ever makes the heat flow back"). Keep
  that honesty note, or lock Particles to 60 and 300 so it never shows?
