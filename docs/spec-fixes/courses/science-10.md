# Spec fixes: science, grade 10

9 tools: 4 rework, 5 small addition, 0 fine. How to use this file: ../README.md. When a spec is fixed, add a line to ../done.txt.

Kinds of fix in this course: Write the spec (1), Hand the key step to the student (4), Close the guessable check (7), Add the missing part (9), Add a check (1), Reach five items that differ (2), Sensitivity read (1).

## Elements Inspector

- Spec: `tools/elements-inspector/(no spec.md yet)` . Module: science-10-atomic-structure-and-the-periodic-table. Stage: LIVE (the code changes after the spec). Sort: **rework**.
- Fixes: Write the spec, Hand the key step to the student, Add the missing part.
- **HS-PS1-1** (shown, in Atom side panel, family filter): Spin the atom, count outer electrons, highlight an element family
  - To do: the tool does the "predict" step: the student must do it
  - Parts of the standard the student never does (must add):
    - use the periodic table as a model to predict relative properties
    - predict from outermost-electron patterns (student never predicts)
    - compare elements by pattern
- The read was unsure about (check these against the spec; the read may be wrong):
  - no spec on file: read notes.md, tool.json and grepped the html only
  - standard wording from memory of NGSS, packet prints none
  - tool.json says Grades 6-12 while the module is grade 10
  - talk prompt 'two elements in the same column' is in notes only, so not counted as a student action
  - grade_split one-path guessed

## Bond Battle

- Spec: `tools/bond-battle/spec.md` . Module: science-10-bonding-and-intermolecular-forces. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Battle: 'ionic or high-bp wins' heuristic plus free retries beats the 70 percent rival without reading the force
  - Jobs: 19-substance book, pass or fail shown with the number, free tries, one or two answers per job
- **HS-PS1-3** (explored, in Bench, Battle): Build substances, pin them, slide Heat; lock one in and see which boils first
  - To do: see-why code, fine here; the unit must add: Student states which of two substances has stronger forces and why before the heat climbs, then explains the result from the bulk property.
  - Parts of the standard the student never does (must add):
    - plan the investigation (hand and recipe book set the cases)
    - infer strength of forces in own words (a Why card gives it)
    - electrical forces named as such
- **HS-PS2-6** (shown, in Jobs): Pick a substance for each job card and read the structure reason
  - To do: the tool does the "communicate" step: the student must do it
  - Parts of the standard the student never does (must add):
    - communicate why structure matters (the tool states the reason, not the student)
    - designed material beyond five jobs
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - action changed from match to build: main activity is building substances
  - cost_class new-engine: spec says molecules engine has no family doc yet
  - PS1-3 explored because lock-in is an implied prediction; could be practiced
  - use station guessed from 15-35 minutes

## Gas Law Lab

- Spec: `tools/gas-law-lab/spec.md` . Module: science-10-gases-and-kinetic-theory. Stage: built (the code changes after the spec). Sort: **rework**.
- Fixes: Hand the key step to the student, Add the missing part.
- **HS-PS3-2** (shown, in Bench energy bars): Heat a weighted piston and read the particle-motion and weights-lifted bars
  - To do: the tool does the "develop and use models" step: the student must do it
  - Parts of the standard the student never does (must add):
    - develop a model (bars are made by the tool)
    - energy tied to relative position of particles (ideal gas has none)
    - account for energy in own words or numbers
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - tool's main path (gas laws, absolute zero fit) maps to no listed standard; only the energy bars touch HS-PS3-2 (spec open question)
  - PS3-2 energy bars appear in Bench, not in the guided Absolute zero steps
  - cost_class new-engine: this tool founded the particles engine

## Equilibrium Seesaw

- Spec: `tools/equilibrium-seesaw/spec.md` . Module: science-10-reaction-rates-and-equilibrium. Stage: spec only. Sort: **rework**.
- Fixes: Hand the key step to the student, Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - Design D1 and D2: 4 baths by 3 volumes, free Check, numbers shown on the card, so the passing setting is found by trying
  - D3: two options per choice, four choices
- **HS-PS1-5** (shown, in Syringe, Collision view): Change bath, plunger or add gas; watch the seesaw tip
  - To do: the tool does the "apply principles to explain" step: the student must do it
  - Parts of the standard the student never does (must add):
    - explain the effect on rate in own words (no prompt asks for it)
    - effect on a one-way reaction (system is an equilibrium)
    - temperature raises both rates (pairing rate held fixed in model)
- **HS-PS1-6** (practiced, in Design D1 to D3): Pick bath and volume for a goal; choose ammonia plant conditions
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (small, add if cheap):
    - refine an existing design (student specifies fresh settings)
    - amounts of ammonia (qualitative only)
- The module also lists codes this tool does not carry: HS-PS1-5.
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - PS1-5 shown: no prediction required before a change, voice hint only says watch which pan drops
  - cost_class sibling: particles engine built with gas-law-lab, needs one new method (react)
  - module has two codes; PS1-5 never explained by student

## pH Mystery Liquids

- Spec: `tools/ph-mystery-liquids/spec.md` . Module: science-10-acids-bases-and-solutions. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Reach five items that differ.
- Checks a student can pass by guessing:
  - C1: Check labels marks each label right or wrong and wrong ones can be moved and rechecked, so six labels can be found by elimination (notes admit this)
  - C2 and C3 explanation: three choices, one right
- **HS-PS1-2** (practiced, in Cases C1 to C3): Run tests to label six bottles; compare two acids; neutralize a spill
  - To do: only 3 items: reach five or more that differ
  - Parts of the standard the student never does (must add):
    - construct and revise an explanation in own words (explanation picked from three)
    - outermost electron states
    - periodic trends
    - predict the outcome of a reaction
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - notes.md says the tool does not teach the outer-electron explanation HS-PS1-2 requires
  - items 3 counts cases, not tests
  - use lesson from 25-40 minutes

## Equation Balancer

- Spec: `tools/equation-balancer/spec.md` . Module: science-10-chemical-reactions-and-equations. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Levels: ledger says which side is short by how many, coefficients 1 to 30, free tries, so balancing can be found by nudging
  - Predict: 3 choices per product and wrong picks get the charge reason, so trial beats thinking
- **HS-PS1-2** (practiced, in Predict P1 to P10): Pick each product formula from three charge-based choices, then balance
  - Parts of the standard the student never does (must add):
    - construct and revise an explanation (explanation comes from the tool after a wrong pick)
    - outermost electron states (strip gives ion charges by group only)
    - reaction types beyond metal plus nonmetal, metal in water, metal plus acid
- **HS-PS1-7** (practiced, in Workbench, Levels, atom and mass ledgers): Set coefficients until atom and mass ledgers match
  - Parts of the standard the student never does (must add):
    - support the claim that mass is conserved (student reads ledgers the tool computes)
    - calculate the masses themselves
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - PS1-7 held at practiced because ledger feedback gives direction (beatable); could argue taught
  - items for PS1-7 counts 25 level equations
  - cost_class new-engine: molecules engine not yet built

## Hand Warmer Lab

- Spec: `tools/hand-warmer-lab/spec.md` . Module: science-10-energy-in-reactions. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Add a check.
- Checks a student can pass by guessing:
  - Trail orders: 3 to 4 accepted salts per order, a pass band of 1.0 C, and the card says how far off, so trial finds the grams
  - T4: iron and a reason chosen from three, one right
  - T3: Can't be done goes live after two NaCl pops and passes when pressed
- **HS-PS1-4** (practiced, in Bond ledger; Pack bench): Click bonds to break and form; read net kJ; run reaction backward
  - To do: no check: add one where thinking is cheaper than guessing
  - Parts of the standard the student never does (must add):
    - develop the model (ledger and staircase are supplied, student fills them)
    - choose bond energies or reactions
    - dissolving is a physical change, not a reaction
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - PS1-4 practiced because Bond ledger has no right-wrong check; Break all and Form all let the tool do it
  - Pack bench dissolving is a physical change (spec open question)
  - cost_class new-engine: molecules engine adds clickable bonds

## Half-Life Dice

- Spec: `tools/half-life-dice/spec.md` . Module: science-10-nuclear-chemistry. Stage: built (the code changes after the spec). Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part, Sensitivity read.
- Checks a student can pass by guessing:
  - Nucleus Check prints both sums ('Mass numbers: 14 = 14. Charges: 6 not 8'), so a stepper can be moved until both match
  - Dating lab: Estimate within 10 percent just earns 'Close', no gate
- **HS-PS1-8** (practiced, in Nucleus, Roll, Dating lab): Set missing mass number and charge for decay, fission, fusion; roll dice; date samples
  - Parts of the standard the student never does (must add):
    - energy released in fission, fusion, decay (ladder shown after Check, student does not work it out)
    - develop the model (drawings and equations supplied)
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - flag sensitive: N3 to N5 mention cancer care and thyroid treatment (notes ask for care)
  - depth practiced because the only check is beatable and energy is shown
  - module is single code so untaught list empty

## Mole Bakery

- Spec: `tools/mole-bakery/spec.md` . Module: science-10-stoichiometry-and-the-mole. Stage: spec only. Sort: **small addition**.
- Fixes: Close the guessable check, Add the missing part.
- Checks a student can pass by guessing:
  - Mix exact fills the other ingredient to match moles and, in Bakery, prints the whole gram-to-mole chain, so orders can be passed without the calculation
  - Each ingredient row shows its own 'makes' gas live, so the target can be matched by reading rows and sliding grams
- **HS-PS1-7** (practiced, in Test kitchen, Bakery, mass check): Set grams per ingredient using moles and mole ratio to hit the order
  - Parts of the standard the student never does (must add):
    - support the claim that atoms and mass are conserved (mass check is tool-made)
    - atoms counted before and after
    - write or explain the conservation claim
- The read was unsure about (check these against the spec; the read may be wrong):
  - standard wording from memory of NGSS, packet prints none
  - depth practiced because Mix exact makes the only check beatable
  - conservation of mass is a tool-made check, so the module's main idea here is stoichiometry
  - items 11 counted from Bakery orders by day

