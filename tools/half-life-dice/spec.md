# Half-Life Dice

## One idea
No single nucleus can be predicted, but a crowd of them can: roll a thousand dice where a 1 means "decayed", and the
crowd halves on a steady schedule even though each die never remembers how long it has waited. Students then look
inside the nucleus to see what a decay changes, compare its energy with chemistry, fission and fusion, and use the
halving clock to date real and made-up samples with carbon-14.

## Not like
- fair-dice-investigation (gr 12, statistics): tests whether dice are fair. Here the dice are fair on purpose and stand in for nuclei; the result is a decay curve and a half-life.
- outbreak-model (gr 11, math): exponential growth of cases. Here exponential decay of nuclei, with the half-life read off a graph and used as a clock.
- dice-in-the-chatbot (gr 9-12, computer science): random sampling of words. Here randomness is the nucleus's, and its rule never changes with age.
- star-life-story (gr 9, earth and space): fusion powers a star's life. Here one fusion and one fission are balanced as nuclear equations and their energy compared per event.

## Who and how
- Grade 10, Chemistry, Nuclear Chemistry. Students drive. 25 to 40 minutes.
- Topic line: "radioactive decay, half-life, fission and fusion".
- Standards (module): HS-PS1-8 (models of changes in the nucleus and the energy released in fission, fusion and
  decay: the Nucleus mode and its energy ladder; Roll and Dating lab model decay over time).
- tool.json: driver "students", minutes "25-40", modes ["Roll", "Nucleus", "Dating lab"], grades_label "Grade 10".

## Screens and modes
Header: title, subtitle "A crowd keeps time. One nucleus never does." Modes `Roll` (opens first), `Nucleus`,
`Dating lab`. Kit buttons.

### Roll
Stage: a tray of 1,000 dice in a 40 × 25 grid (each a small square with its face), a graph of undecayed count
against roll number, and a die picker: `Coin`, `d4`, `d6`, `d8`, `d10`, `d12`, `d20`. Rule card: "Every die that
shows 1 (tails for the coin) has decayed. Decayed dice turn gray and leave the next roll."
- `Roll once`, `Roll to 10`, `Reset`. The graph adds a point per roll; a dashed line shows the expected curve,
  1000 × (1 − p)^n, with `Show expected` on by default.
- `Mark a half-life`: the student drags a horizontal line to 500 and reads the roll number where the curve crosses;
  the card compares it with the exact half-life (Content).
- Tracked die: `Track one` gives one live die a ring. After every roll the card shows "Rolls survived: 7. Chance it
  decays next roll: 1 in 6", the same at every age. If it decays, `Track one` picks another.
- `Average 20 runs`: runs 20 seeded trays to 10 rolls and plots the mean, which hugs the expected curve.
Seeded random (a small mulberry32 generator in the tool); `New seed` changes it.

### Nucleus
Stage: before and after nuclei drawn as packed protons (`#ff8f6b`) and neutrons (`#9fb3c8`), with counts, and the
nuclear equation underneath with mass number on top and charge (atomic number) below each symbol.
Cards (pick one): decays N1 to N5, then fission F1 and fusion F2 (Content). In each, one product is blank: the
student sets its mass number and atomic number with steppers; the element symbol fills in from the atomic number
(elements-inspector's table); `Check` confirms both sums match. After checking, the change is named ("a neutron
became a proton and an electron left") and the energy appears on the ladder.
Energy ladder (a log scale bar, one rung per event): burning one methane molecule 9.23 eV; carbon-14 decay 156 keV;
D-T fusion 17.6 MeV; uranium-235 fission about 200 MeV. A ratio line: "One fission gives about 22 million times the
energy of one methane molecule burning."

### Dating lab
A sample shelf; each sample has a count of carbon-14 decays per minute per gram of carbon (dpm/g). A Geiger counter counts for a set time; its clicks follow the count (about one click per 20 counted
decays) and play only when `Counter clicks` is on (off by default; the header Sound stays as the kit sets it). The halving ruler: 13.6 at the left, halving at each
5,730-year tick. Students read the age from the ruler first (`Estimate`), then press `Calculate` to see the exact
age by t = (5730 ÷ ln 2) × ln(13.6 ÷ A). Samples (Content). `Counting noise` (off by default): counts over 100
minutes from 1 g follow Poisson noise (seeded) and the age shows a ± range from the square root of the count; `Count again` draws the
next count from the same seeded stream and lists the counts so far.
Progress (cards checked, samples dated) saved on this device (localStorage `curio-half-life-dice`, try/catch), `Clear`
resets.

## Content
Dice: p = 1/sides (coin 1/2). Half-life in rolls = ln 2 ÷ (−ln(1 − p)): coin 1.000, d4 2.409, d6 3.802, d8 5.191,
d10 6.579, d12 7.966, d20 13.513. Expected left of 1,000 after 10 rolls: coin 1.0, d4 56.3, d6 161.5, d8 263.1, d10
348.7, d12 418.9, d20 598.7.
Nucleus cards (half-lives from NNDC NuDat):
- N1 Carbon-14, beta: ¹⁴₆C → ¹⁴₇N + ⁰₋₁e. Half-life 5,730 years (OpenStax; NNDC lists 5,700 ± 30).
- N2 Uranium-238, alpha: ²³⁸₉₂U → ²³⁴₉₀Th + ⁴₂He.
- N3 Iodine-131, beta (thyroid treatment): ¹³¹₅₃I → ¹³¹₅₄Xe + ⁰₋₁e. Half-life 8.02 days.
- N4 Cobalt-60, beta then gamma (radiation therapy): ⁶⁰₂₇Co → ⁶⁰₂₈Ni + ⁰₋₁e, then a gamma ray (no change in mass
  number or charge). Half-life 5.27 years.
- N5 Fluorine-18, positron (PET scans): ¹⁸₉F → ¹⁸₈O + ⁰₊₁e. Half-life 110 minutes.
- F1 Fission: ²³⁵₉₂U + ¹₀n → ¹⁴¹₅₆Ba + ⁹²₃₆Kr + 3 ¹₀n, about 200 MeV.
- F2 Fusion: ²₁H + ³₁H → ⁴₂He + ¹₀n, 17.6 MeV. Per nucleon: fusion 3.52 MeV, fission 0.85 MeV.
Energy ladder: methane combustion 890.6 kJ/mol ÷ Avogadro = 9.23 eV per molecule; carbon-14 decay energy 156 keV
(NNDC); ratio fission to methane 2.2 × 10⁷.
Dating (living carbon 13.6 dpm/g, half-life 5,730 years, OpenStax 21.3):
- Dead Sea Scrolls fragment (OpenStax example), 10.8 dpm/g: 1,906 years.
- Seeds from Tutankhamun's tomb (OpenStax example), 9.07 dpm/g: 3,349 years.
- Made-up samples, labeled "practice sample": fresh leaf 13.6, 0 years; hearth charcoal 6.8, 5,730; cave charcoal 3.4,
  11,460; mammoth bone 0.85, 22,920; deep core wood 0.02, 53,916, which the card flags "too old to date well"
  (OpenStax: carbon dating is accurate to about 30,000 years and reasonable to about 50,000).
- Counting noise example: cave charcoal, 340 counts in 100 minutes, ±18, gives 11,020 to 11,920 years.

## Interactions in detail
- Each roll draws one random face per live die from the seeded generator; the tray animates faces for 0.4 s (Motion
  off: no animation, faces shown).
- `Mark a half-life` moves the line in 25-nucleus steps and accepts it at 500; the card reads the tray's own crossing
  to the half roll against the exact value ("Your tray: 3.5 rolls. Exact for a d6: 3.80.") and, when they differ by
  more than 0.5 rolls, says one tray scatters and points to Average 20 runs. Before any roll it asks for a roll first.
  (Integrator, 2026-10-29: the old rule, accept within 0.5 rolls of exact, refused correct lines on a noisy tray.)
- Roll once continues to the graph's last roll for every die, so a d20 tray (half-life 13.5 rolls) can cross 500.
- Nucleus steppers range A 0 to 240, Z −1 to 94; `Check` reports which sum is off ("Mass numbers: 14 = 14. Charges:
  6 ≠ 8.") without giving the answer.
- Dating: `Estimate` takes a number from the ruler drag; within 10 percent of the exact age gets "Close"; then
  `Calculate` shows the steps.
- Keyboard: dice tray is one image with a live text summary ("640 left after 2 rolls"); every control is a button or
  stepper.
- `window.__tool = {state, setMode, die(kind), roll(n), seed(s), card(id), setProduct(A, Z), check(), sample(id), noise(on)}`.

## Look
Accent `--brand #97c059` (lab-glow green), `--brand-ink #10141a`. Dice: live `#e8edf3` faces with dark pips, decayed
`#4a5160` (and a small x, so not color alone), tracked die ringed in accent. Graph on Plane colors: observed accent,
expected dashed `--ink` at 60 percent. Nucleons: protons `#ff8f6b`, neutrons `#9fb3c8`, each with a legend word.
Contrast (computed): brand on panel 8.24:1, on --sec-bg 7.81:1, brand-ink on brand 8.79:1.

## Art
None. Dice, nuclei, counter and ruler are drawn in code.

## Voice
Bank voice `curious-librarian` (keeper of old scrolls and seeds, curious about their age). No 9-12 science tool
uses it. `Curio.voice`,
scope = mode.
- wRoll (how, Roll welcome): "Pick a die, then press Roll once. Every 1 is a decay."
- trackTip (how, first Track one): "Watch the ringed die. Its chance stays the same, no matter how long it lasts."
- wNucleus (how, Nucleus welcome): "Pick a card. Set the missing mass number and charge, then press Check."
- wDating (how, Dating lab welcome): "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate."
- tooOld (event, the deep core sample is dated; stale on the next sample): "That one's past the clock's range. Too little carbon-14 left."

## Family engine
None. Uses `kit/graphing.js` (Plane, g.point, g.fn for the expected curve) and its own seeded generator; the
element symbols come from a copy of elements-inspector's ELEMENTS table (symbol and name by atomic number only).

## Sources
- HS-PS1-8: NGSS Lead States (2013), Next Generation Science Standards, https://www.nextgenscience.org/
- Radioactive decay, half-life, carbon-14 dating (13.6 dpm/g, 5,730 years, Dead Sea Scrolls and Tutankhamun examples, the 30,000 and 50,000 year limits), nuclear equations: OpenStax, Chemistry 2e, 21.3 "Radioactive Decay", https://openstax.org/books/chemistry-2e/pages/21-3-radioactive-decay
- Fission of uranium-235 and D-T fusion reactions: OpenStax, Chemistry 2e, 21.4 "Transmutation and Nuclear Energy", https://openstax.org/books/chemistry-2e/pages/21-4-transmutation-and-nuclear-energy. Energies: D-T fusion 17.59 MeV, OpenStax College Physics 2e, 32.5 "Fusion", https://openstax.org/books/college-physics-2e/pages/32-5-fusion; average U-235 fission 200 MeV, 32.6 "Fission", https://openstax.org/books/college-physics-2e/pages/32-6-fission (checked by the integrator 2026-10-29).
- Half-lives (C-14 5,700 ± 30 y, I-131 8.02 d, Co-60 5.27 y, F-18 109.8 min) and C-14 decay energy 156 keV: National Nuclear Data Center, NuDat 3, Brookhaven National Laboratory, https://www.nndc.bnl.gov/nudat3/ (checked 2026-10-27).
- Methane combustion 890.6 kJ/mol: OpenStax, Chemistry 2e, 5.3 "Enthalpy" (standard enthalpies of combustion table).
- Avogadro constant and the electronvolt: NIST CODATA 2018, https://physics.nist.gov/cuu/Constants/
- Dice half-lives, expected counts, ages and the noise range recomputed in Python (2026-10-27).

## Done when
1. d6 tray: `Show expected` gives 161.5 at roll 10; `Average 20 runs` lands within 15 of it at every roll.
2. The card's exact half-lives match Content for all seven dice; a line at 500 is accepted and the card gives the tray's crossing and the exact value.
3. The tracked die's card always says the same chance at every age.
4. N1 to N5, F1 and F2 accept only the right product and report which sum is off otherwise.
5. The energy ladder shows the four rungs and the 22 million ratio.
6. Dating: 10.8 gives 1,906 years, 9.07 gives 3,349, 0.85 gives 22,920; the 0.02 sample shows the too-old flag; with noise on, the cave charcoal's ± range is the square root of its count (±18 at 340 counts).
7. Same seed, same tray every time; progress survives a reload; `Clear` resets; Motion off shows faces without animation.
8. Every size in STANDARDS.md keeps the tray, the graph and the buttons visible; keyboard-only works; console clean, no network.

## Open questions
- The dating ages use OpenStax's 5,730-year half-life while NNDC now lists 5,700 ± 30. Keep 5,730 (matches the textbook and its examples), or switch to 5,700?
