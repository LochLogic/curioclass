# Batch note: spec wave 3, 9-12 science (2026-10-27)

Cory asked for a smaller spec wave 3 right after wave 2: every remaining 9-12 science tool, 32 in four groups. Wave 2
(9-12 math, CTE and computer science, `docs/agents/BATCH-W2.md`) is specced first; this wave is written against it,
and both get one joint review at the end, since 9-12 math and science overlap the most (modeling, rates, data
fitting, physics math).

The overlap pass is done and Cory decided every cluster (`docs/agents/overlap/choices.json`); accepted fixes are
already in `data/concepts/*.txt`. Fixes left for the spec are in the per-tool notes below. Six science concepts were
extended in the gap fill so their new NGSS codes are honest (`docs/agents/gapfill/core/notes.md`): energy-accountant
and feedback-loop-builder are in this wave, so build that clause into the spec.

Already live, not in this wave: elements-inspector (elements family), collision-lab (forces), and the grade 11 batch
(outbreak-model, island and others). Read them as the closest references.

## How this wave runs

Spec agents each take one group below and write every spec in it. At most three run at once. Then the integrating
session runs the spec check over the wave (`python scripts/spec_sheet.py docs/agents/BATCH-W3.md`) and the joint
review with wave 2.

## Rules for this wave (on top of SPEC.md and STANDARDS.md)

The wave 1 rules apply unchanged (`docs/agents/BATCH-W1.md`, "Rules for this wave"); read that section first. The
wave 2 additions on standards, exact math, real numbers, families and look and voice across 9-12 apply too
(`docs/agents/BATCH-W2.md`). On top of them:

- **Check the math wave.** Before writing, read the wave 2 specs that sit near yours (`python scripts/spec_sheet.py
  docs/agents/BATCH-W2.md` lists them all; `scripts/neighbors.py <id>` shows the nearest). Where a math tool and
  your tool model the same thing (projectiles, rates, growth and decay, data fitting, accumulation), make the
  science tool about the science (the mechanism, the evidence, the system) and say how it differs in "Not like".
- **Science facts.** Every constant, rate and data set has a dated source in "Sources": NIST, NASA, NOAA, USGS, EPA,
  NIH, PubChem, the NGSS evidence statements, or a named textbook or paper. Models say what they leave out.
- **Lab safety.** Virtual labs only. No instructions for a hazardous home experiment; any real-world procedure
  shown follows standard school lab safety (goggles, ventilation, an adult), sourced.
- **Climate and environment** are factual and calm: real data, clear uncertainty, choices with trade-offs, no doom
  framing and no political sides.
- **Families.** cells, ecosystem, genetics, molecules, particles and forces have lower-grade siblings that are not
  specced yet (forces has the live collision-lab: match it). The sibling in this wave describes the shared engine in
  full in "Family engine", written so the lower grades can reuse it, and names them. astronomy's two tools are both
  here: share one engine.

## Groups and per-tool notes

### Science: biology (`sci-bio`, 9)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| body-thermostat | Body Thermostat | 9 | simulator | - |
| energy-accountant | Energy Accountant | 9 | data | - |
| tree-of-life | Tree of Life | 9 | explorer | - |
| reserve-designer | Reserve Designer | 9 | builder | - |
| membrane-gatekeeper | Membrane Gatekeeper | 9 | arcade | cells |
| mitosis-mixer | Mitosis Mixer | 9 | sort | cells |
| carrying-capacity | Carrying Capacity | 9 | simulator | ecosystem |
| protein-factory | Protein Factory | 9 | puzzle | genetics |
| punnett-predictor | Punnett Predictor | 9 | simulator | genetics |

- **energy-accountant:** The overlap pass added standards to its module; the concept above already covers them (Wave 1. Its carbon and energy ledger already models photosynthesis and respiration; HS-LS2-5 is the carbon cycle across the spheres and has no module).

### Science: chemistry (`sci-chem`, 8)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| equation-balancer | Equation Balancer | 10 | puzzle | - |
| mole-bakery | Mole Bakery | 10 | tycoon | - |
| hand-warmer-lab | Hand Warmer Lab | 10 | lab | - |
| equilibrium-seesaw | Equilibrium Seesaw | 10 | simulator | - |
| ph-mystery-liquids | pH Mystery Liquids | 10 | mystery | - |
| half-life-dice | Half-Life Dice | 10 | simulator | - |
| bond-battle | Bond Battle | 10 | cards | molecules |
| gas-law-lab | Gas Law Lab | 10 | lab | particles |

- **ph-mystery-liquids:** Topic line under the title on the tool page: "acids, bases and pH". Renamed by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: One of four 9-12 mysteries and one of twelve 'Detective' titles; identifying unknowns by pH is real lab work, so the case frame stays.

### Science: earth and space, physics (`sci-earth-phys`, 10)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| feedback-loop-builder | Feedback Loop Builder | 9 | builder | - |
| water-shapes-earth | Water Shapes Earth | 9 | lab | - |
| climate-dashboard | Climate Dashboard | 9 | data | - |
| lake-commons | Island Economy | 9 | tycoon | - |
| star-life-story | Star Life Story | 9 | timeline | astronomy |
| orbit-lab | Orbit Lab | 9 | simulator | astronomy |
| zipline-energy | Zipline Energy | 11 | builder | - |
| spectrum-explorer | Spectrum Explorer | 11 | explorer | - |
| hot-meets-cold | Hot Meets Cold | 11 | simulator | - |
| curling-stones | Curling Stones | 11 | simulator | forces |

- **island-economy:** Topic line under the title on the tool page: "resources and sustainability". Overlap note (left for you to settle in the spec): One of four islands in 9-12; matches trade-island on action and setting. Suggested fix (reshape): "Lake Commons": Manage a lake town's fish, forest and water over generations, through good years and flood years; sustainable use keeps the town going and overuse brings collapse. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

- **zipline-energy:** Topic line under the title on the tool page: "conservation of energy with friction, roller coaster physics". Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: A coaster track in grade 11 beside the live rollercoaster-polynomials, with a near-identical title.

- **hot-meets-cold:** New in the gap fill (docs/agents/gapfill/core/notes.md).

- **curling-stones:** Topic line under the title on the tool page: "Newton's second law, F = ma". Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: One of three space simulators in 9-12 (with launch-pad, wave 1, and orbit-lab). Family: stays in forces.

### Science: environmental (`sci-env`, 5)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| biome-atlas | Biome Atlas | 12 | map | - |
| population-dashboard | Population Dashboard | 12 | data | - |
| grid-operator | Grid Operator | 12 | tycoon | - |
| up-the-watershed | Watershed Detective | 12 | mystery | - |
| design-challenge-studio | Design Challenge Studio | 12 | builder | - |

- **population-dashboard:** Kept as written in the overlap pass (One of 12 data-format tools in 9-12; its standards are also on island-economy and carrying-capacity).

- **grid-operator:** Topic line under the title on the tool page: "energy sources, cost, reliability and emissions". Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: Manages a city like the live community-project-planner; the title is also the Power Grid board game.

- **watershed-detective:** Topic line under the title on the tool page: "watershed pollution and solutions". Overlap note (left for you to settle in the spec): One of twelve 'Detective' titles. Suggested fix (rename): "Upstream". Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

