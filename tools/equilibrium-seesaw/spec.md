# Equilibrium Seesaw

## One idea
Equilibrium is not a reaction that stopped: it is two reactions running at the same rate. A sealed syringe of
brown NO2 and colorless N2O4 sits on a seesaw that weighs "splitting per second" against "pairing per second". Heat
it, squeeze it or add gas, and the seesaw tips toward the faster side, then settles level again at new amounts,
which is the shift students can see as a change in color.

## Not like
- equation-golf (gr 9, math): a balance beam weighs equal expressions. Here the beam weighs two reaction rates, and level means equal rates, not equal amounts.
- gas-law-lab (gr 10, same group): one gas that never changes. Here the molecules change into each other, so squeezing changes more than pressure.
- hand-warmer-lab (gr 10, same group): energy in and out of one reaction that runs to the end. Here the reaction runs both ways at once, and temperature changes the balance point.
- carrying-capacity (gr 9, biology): a population levels off. Here the level comes from two opposite reactions, and you can measure both.

## Who and how
- Grade 10, Chemistry, Reaction Rates and Equilibrium. Students drive. 20 to 35 minutes.
- Topic line: "reaction rates and chemical equilibrium".
- Standards (module): HS-PS1-5 (temperature and concentration change reaction rates: the two pans and the collision
  view), HS-PS1-6 (change conditions to get more product at equilibrium: Design mode and the ammonia plant).
- tool.json: driver "students", minutes "20-35", modes ["Syringe", "Design"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "Level means equal speed, not equal amounts." Modes `Syringe` (opens first), `Design`. Kit
buttons.
Stage, left: a glass syringe seen from the side, gas drawn as moving particles (NO2 single brown dots, N2O4 linked
pale pairs), behind a tint whose brownness follows [NO2]. Stage, right: the seesaw. Left pan "splitting per second"
(N2O4 → 2 NO2), right pan "pairing per second" (2 NO2 → N2O4); pan weights are the two rates, drawn as stacks of
blocks with numbers. Below: an amounts bar (moles of NO2 and N2O4) and a strip chart of both rates over time.

### Syringe (explore)
Controls: bath `Ice 0 °C`, `Room 25 °C`, `Warm 50 °C`, `Hot 80 °C`; plunger `25 mL`, `50 mL`, `100 mL`; `Add NO2`
and `Add N2O4` (0.0005 mol each press); `Add argon` (0.0010 mol, a gas that takes no part); `Reset` (0.0020 mol
N2O4 at 25 °C, 50 mL, settled). Any change applies at once, the seesaw tips, then it settles over about 4 seconds
(instant with Motion off).
A readout card: temperature, volume, mol NO2, mol N2O4, percent of molecules that are NO2, [NO2] in mol/L, total
pressure in kPa, and the word `level` or which side is faster.
`Collision view` (toggle): slows the picture, highlights NO2 pairs that bump and join, and counts bumps per second
in the picture next to the right pan, so students see why squeezing (more crowding) speeds pairing.

### Design
Three challenge cards, done in any order, each checked by the model (Content). Progress saved on this device
(localStorage `curio-equilibrium-seesaw`, try/catch), `Clear` resets.
- D1 Brown signal: a warning sign needs [NO2] of at least 0.040 mol/L, using the least heating. Pick bath and volume.
- D2 Keep it pale: at least 90 percent of the molecules must be N2O4.
- D3 The ammonia plant: N2 + 3 H2 ⇌ 2 NH3, about −92 kJ per 2 NH3. Four choices (temperature, pressure,
  catalyst, removing ammonia), each picked from two options with a reason, then the card shows what real plants do.

## Content
Reaction: N2O4 ⇌ 2 NO2, ΔH +57.12 kJ, ΔS +175.70 J/K (from NIST WebBook data: NO2 ΔfH 33.10 kJ/mol, S° 240.04 J/mol K;
N2O4 ΔfH 9.08, S° 304.38). OpenStax 13.3 gives +57.20 kJ (shown in Sources only). NO2 is a brown gas, N2O4 is
colorless (PubChem).
Kp (standard 1 bar) = exp(−(ΔH − TΔS)/RT): 0 °C 0.01797, 25 °C 0.1481, 50 °C 0.8803, 80 °C 5.357.
Amounts are solved exactly: with N = mol N2O4 + ½ mol NO2 and y = mol NO2, y² RT = Kp V P° (N − y/2), the positive
root. Starting load 0.0020 mol N2O4.
Settled amounts (mol NO2, percent of molecules NO2, total kPa, [NO2] mol/L):
- 50 mL: 0 °C 0.000272, 12.7, 97.0, 0.00543; 25 °C 0.000702, 29.9, 116.6, 0.01404; 50 °C 0.001446, 53.1, 146.3,
  0.02893; 80 °C 0.002562, 78.1, 192.7, 0.05123.
- 25 mL: 0 °C 0.000194, 9.3, 190.5, 0.00776; 25 °C 0.000510, 22.6, 223.6, 0.02042; 50 °C 0.001091, 42.9, 273.6,
  0.04366; 80 °C 0.002088, 68.6, 357.5, 0.08353.
- 100 mL: 0 °C 0.000379, 17.3, 49.7, 0.00379; 25 °C 0.000954, 38.5, 61.4, 0.00954; 50 °C 0.001869, 63.7, 78.8,
  0.01869; 80 °C 0.003008, 85.8, 102.9, 0.03008.
Additions at 25 °C, 50 mL, from the settled start: add 0.0005 NO2 → settles at NO2 0.000748, N2O4 0.001876; add
0.0005 N2O4 → NO2 0.000793, N2O4 0.002104. Add argon: total pressure rises, both partial pressures stay, no shift.
Rate model: pairing rate per liter = kr [NO2]², splitting rate = kf [N2O4], with kf = Kc × kr so level always
matches Kp. kr is held fixed (a model choice, said in the help); kf scales with temperature by Kc: ×0.1325 at 0 °C,
×5.485 at 50 °C, ×30.55 at 80 °C. Kc at 25 °C = 0.00597 mol/L. Pan numbers are relative, 100 = each rate at the
25 °C, 50 mL start.
- Squeeze 50 → 25 mL: right after, splitting 200, pairing 400 (tips to pairing); settles level at 211.6. [NO2] jumps
  to 0.02807 then falls to 0.02042: darker, then partly fades, still darker than the 0.01404 start.
- Heat to 80 °C: right after, splitting 3,055, pairing 100; settles level at 1,332.
- Cool to 0 °C: right after, splitting 13.2, pairing 100; settles level at 15.0.
Time: real NO2 pairing settles in far less than a second; the tool slows it so the tip is visible (said in help).
Design answers:
- D1: 25 mL at 50 °C gives 0.04366 (passes, least heating). 50 mL at 50 °C (0.02893) fails; 25 mL or 50 mL at
  80 °C pass but use more heat (the card says "passes, but a cooler bath would do").
- D2: 25 mL at 0 °C, 90.7 percent N2O4 (passes); 50 mL at 0 °C is 87.3 percent (fails).
- D3 (OpenStax 13.3): temperature: lower gives more ammonia at equilibrium but slows both directions, so plants
  compromise at 400 to 500 °C; pressure: 4 gas molecules become 2, so high pressure favors ammonia, plants run 150
  to 250 atm; catalyst: speeds both directions equally, same amounts, sooner; ammonia is removed as it forms, so the
  forward direction keeps winning.
Safety line (help): "NO2 is toxic. Real NO2 syringes are a teacher demonstration behind a fume hood. This lab is
virtual."

## Interactions in detail
- Settling runs the rate equations forward in model time (step 1/60 s, kr chosen so 95 percent of the change happens
  in 4 seconds at 25 °C, 50 mL) and the final state is snapped to the exact root.
- `Add` buttons stop at 0.0050 mol total N2O4-equivalent ("The syringe is full").
- Seesaw angle = clamp(atan of (splitting − pairing) / (splitting + pairing)), at most 20 degrees; `level` shows
  when the rates are within 1 percent.
- Design cards check the settled state only; a card shows the readouts that decided it.
- Keyboard: every control is a button group (arrows move within the group). Screen readers get the readout card as
  a live region updated when the system settles, not every frame.
- `window.__tool = {state, setMode, bath(tC), volume(mL), add(species, mol), settle(), rates(), card(id, answer)}`.

## Look
Accent `--brand #c0b959` (brass, like an old balance), `--brand-ink #10141a`. Gas tint from `#f4e9d8` alpha 0 (no NO2)
to `#8a4a1c` alpha 0.85 at [NO2] 0.16 mol/L (the most a full syringe reaches: 0.0050 mol, 25 mL, 80 °C gives
0.151), linear in [NO2]. Baths: ice `#8fd3ff`, room `--ink`, warm `#f2b880`,
hot `#ff8a5c`. Pans: splitting blocks `#d39a64`, pairing blocks `#9fb7d9`, each with its label (not color alone).
Contrast (computed): brand on panel 8.51:1, on --sec-bg 8.06:1, brand-ink on brand 9.08:1.

## Art
None. Syringe, baths, seesaw and particles are drawn in code.

## Voice
Bank voice `gentle-storyteller` (unhurried, like the seesaw settling). No 9-12 science tool uses it. `Curio.voice`, scope = mode.
- wSyringe (how, Syringe welcome): "Pick a bath or move the plunger, then watch which pan drops."
- levelTip (how, first time the seesaw settles after a change): "Level again. The speeds match now, but the amounts moved."
- squeezeTip (how, first squeeze): "Crowded molecules bump more, so pairing speeds up first."
- wDesign (how, Design welcome): "Pick a card. Set the bath and the plunger, then press Check."
- pass (event, a card passes; stale when the next card opens): "That design works. The numbers on the card show why."

## Family engine
particles (`kit/particles.js`), described in full in gas-law-lab's spec. Family none here; it uses `Box` with two
species (NO2 mass 46.01, N2O4 92.01) and asks the engine for one addition: `react({pair: ['NO2', 'N2O4'], split:
['N2O4', 'NO2']})`, which joins two NO2 that touch and splits N2O4 at a set rate, with `steer(id, count)` nudging the
picture's counts toward the model's (1 dot = 0.00001 mol). Readouts never come from the picture.

## Sources
- HS-PS1-5, HS-PS1-6: NGSS Lead States (2013), Next Generation Science Standards, https://www.nextgenscience.org/
- NO2 and N2O4 enthalpy of formation and entropy: NIST Chemistry WebBook, SRD 69 (gas phase thermochemistry, from JANAF tables), https://webbook.nist.gov/chemistry/ (checked 2026-10-27).
- Equilibrium, Le Chatelier's principle, the NO2/N2O4 example (+57.20 kJ), the Haber process conditions and catalyst: OpenStax, Chemistry 2e, 13.2 "Equilibrium Constants" and 13.3 "Shifting Equilibria: Le Chatelier's Principle", https://openstax.org/books/chemistry-2e/pages/13-3-shifting-equilibria-le-chateliers-principle
- Reaction rates and concentration, temperature: OpenStax, Chemistry 2e, 12.2 "Factors Affecting Reaction Rates".
- Colors (NO2 reddish brown, N2O4 colorless): PubChem, nitrogen dioxide CID 3032552 and dinitrogen tetroxide CID 25352, https://pubchem.ncbi.nlm.nih.gov/
- Gas constant: NIST CODATA 2018.
- Every amount, Kp and rate recomputed in Python (2026-10-27).

## Done when
1. Reset shows 0.000702 mol NO2, 29.9 percent, 116.6 kPa, [NO2] 0.01404, seesaw level.
2. Squeeze to 25 mL: pans read 200 and 400 at once, then level at 211.6; [NO2] reads 0.02807 then settles at 0.02042, and the tint follows.
3. Hot 80 °C at 50 mL settles at 0.002562 mol NO2 and 78.1 percent; Ice 0 °C at 50 mL settles at 0.000272.
4. Add argon leaves both amounts unchanged and the seesaw level; total pressure rises.
5. Add NO2 settles at 0.000748 and 0.001876; the cap stops adds at 0.0050 mol.
6. D1 passes at 25 mL and 50 °C and fails at 50 mL and 50 °C; D2 passes at 25 mL and 0 °C only; D3 shows the real plant ranges after four answers.
7. Motion off snaps to the settled state; progress survives a reload; `Clear` resets.
8. Every size in STANDARDS.md keeps the syringe, the seesaw and the controls visible; keyboard-only works; console clean, no network.

## Open questions
- Holding the pairing rate constant while splitting carries all the temperature change is a model choice that keeps level matched to Kp. OK as is, or show both rates rising with temperature?
- D3 uses only OpenStax's qualitative plant conditions, no ammonia amounts. Enough for HS-PS1-6, or add a numeric ammonia mode later (needs a sourced Kp table)?
