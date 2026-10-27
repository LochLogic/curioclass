# Batch note: spec wave 2, 9-12 math, CTE and computer science (2026-10-27)

Cory asked for spec wave 2 (`docs/agents/SCALE-PLAN.md` step 3): every remaining 9-12 math tool, the 9-12 CTE
pathways and personal finance tools, and the 9-12 computer science tools added by the gap fill. 58 tools in six
groups. It ends at the spec check and a joint review with wave 3 (9-12 science, `docs/agents/BATCH-W3.md`), which is
specced right after this wave and checked against it. Builds, art and voice come later.

The overlap pass is done and Cory decided every cluster (`docs/agents/overlap/choices.json`); accepted fixes are
already in `data/concepts/*.txt`, so `scripts/neighbors.py` shows the current titles and concepts. Fixes left for the
spec are in the per-tool notes below: settle them in your spec. Tools added by the gap fill point to their staging
notes (`docs/agents/gapfill/<domain>/notes.md`), which say what each new tool is for and which codes it carries.

Already live, not in this wave: first-apartment-budget and market-time-machine (money family), poll-workshop
(sampling), rollercoaster-polynomials (graphing), and the grade 11 batch. Read them as the closest references.

## How this wave runs

Spec agents each take one group below and write every spec in it, so the group's tools differ from each other by
design. At most three spec agents run at once. Then the integrating session runs the spec check over the wave
(`python scripts/spec_sheet.py docs/agents/BATCH-W2.md`).

## Rules for this wave (on top of SPEC.md and STANDARDS.md)

The wave 1 rules apply unchanged (`docs/agents/BATCH-W1.md`, "Rules for this wave"): one spec per tool with exactly
the SPEC.md sections, topic lines, title changes written to the old folder with `Renamed from:`, trademark checks,
families, voice (`Curio.voice`, every line marked `how` or `event`), look, art, no network or accounts or stored
student data, 9-12 works like the real thing, facts with sources, plain words, no em dashes, "Curio Class" never
"Curio" alone. Read that section first. On top of it:

- **Standards.** The `- Standards` line names exactly the codes on the tool's module in `data/modules.csv`. If the
  tool cannot honestly teach one, say so in Open questions; do not drop it silently. If it clearly teaches one more,
  name it and say so in Open questions.
- **Math is exact.** Every formula, worked answer, generated problem and checker must be right for every input the
  tool allows, including edge cases (zero, negatives, no solution, infinitely many, undefined, rounding). Say in
  "Interactions in detail" how answers are checked (exact fractions, tolerance, equivalent forms) and in "Done when"
  give worked cases the verify agent can recompute. Name the CCSS cluster each mode serves.
- **Real numbers.** Real-world data (prices, rates, tax brackets, physical constants, census or market figures) gets
  a dated source in "Sources" and a "data as of" line on screen. Money: IRS, SSA, BLS, CFPB, FDIC, the Federal
  Reserve, Census. Careers: the BLS Occupational Outlook Handbook and O*NET. No real bank, card, insurer, employer or
  app brands; scam and phishing examples are made up.
- **Families.** graphing (`docs/families/graphing.md`, engine `kit/graphing.js`, built) and data-desk
  (`docs/families/data-desk.md`) have family docs: use them and say which parts you use. money and careers have live
  or specced siblings (first-apartment-budget, market-time-machine, career-cluster-explorer, career-match-quiz):
  read them and match their engine. For the other families (algebra-tiles, balance, coordinate, probability,
  transformations, sampling) the lower-grade siblings are not specced yet: the sibling in this wave describes the
  shared engine in full in "Family engine", written so the lower grades can reuse it, and names them.
- **Look and voice across 9-12.** 9-12 has 18 live tools and wave 1 added 28 specs. `python scripts/spec_sheet.py
  docs/agents/BATCH-W1.md` lists their voices and accents: keep yours different from any 9-12 neighbor in the same
  subject, not only inside your group.
- **Finance and careers are calm and practical.** No shaming about debt or spending, no promises of returns. Past
  returns are labeled as past. Tax and benefit figures name the year.
- **CS tools run entirely in the page.** A chatbot, a cloud or a code review is simulated with made-up content; no
  model, API or network call.

## Groups and per-tool notes

### Math: algebra 1 and 2 (`math-alg`, 12)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| exponent-rule-builder | Exponent Rule Builder | 9 | puzzle | - |
| unit-sense | Unit Detective | 9 | mystery | - |
| polynomials-as-numbers | Polynomials as Numbers | 9 | builder | - |
| model-my-world | Model My World | 9 | builder | - |
| correlation-guessing-game | Correlation Guessing Game | 9 | arcade | - |
| algebra-tile-studio | Algebra Tile Studio | 9 | sandbox | algebra-tiles |
| equation-golf | Equation Golf | 9 | puzzle | balance |
| which-model-wins | Which Model Wins? | 9 | data | data-desk |
| intersection-quest | Intersection Quest | 9 | race | graphing |
| graph-story-lab | Graph Story Lab | 9 | explorer | graphing |
| launch-pad | Launch Pad | 9 | simulator | graphing |
| work-rate-crew | Work Rate Crew | 11 | roleplay | - |

- **unit-detective:** Topic line under the title on the tool page: "units and dimensional analysis". Overlap note (left for you to settle in the spec): One of twelve 'Detective' titles. Suggested fix (rename): "Unit Sense". Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

- **polynomials-as-numbers:** Topic line under the title on the tool page: "adding and multiplying polynomials". Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: The same rectangle area model as algebra-tile-studio in grade 9, and one of eight 'Garden' titles. Family: Leaves algebra-tiles on purpose: its grade 9 sibling Algebra Tile Studio owns the area model.

### Math: geometry (`math-geo`, 9)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| proof-tower | Proof Blocks | 10 | puzzle | - |
| shadow-measure | Shadow Measure | 10 | lab | - |
| ramp-and-roof | Ramp and Roof | 10 | builder | - |
| circle-theorem-explorer | Circle Theorem Explorer | 10 | explorer | - |
| slice-and-stack | Slice It | 10 | explorer | - |
| packaging-challenge | Packaging Challenge | 10 | builder | - |
| coordinate-proof-lab | Coordinate Proof Lab | 10 | sandbox | coordinate |
| medical-test-paradox | Medical Test Paradox | 10 | simulator | probability |
| rigid-motion-twins | Rigid Motion Twins | 10 | puzzle | transformations |

- **rigid-motion-twins:** Topic line under the title on the tool page: "rigid motions and congruence". Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: A second golf course in 9-12 math beside equation-golf; 'Transformation Golf' is also a Desmos activity. Family: stays in transformations.

### Math: precalculus and calculus (`math-pre`, 14)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| identity-proof-race | Identity Proof Race | 12 | race | - |
| flight-planner | Flight Planner | 12 | simulator | - |
| image-transformer | Image Transformer | 12 | studio | - |
| polar-rose-studio | Polar Rose Studio | 12 | studio | - |
| conic-focus-finder | Cone Slicer | 12 | explorer | - |
| zoom-to-the-limit | Zoom to the Limit | 12 | explorer | - |
| fire-lookout-triangles | Fire Lookout Triangles | 12 | map | - |
| function-family-reunion | Function Family Reunion | 12 | explorer | graphing |
| hole-hunter | Hole Hunter | 12 | puzzle | - |
| speedometer | Speedometer | 12 | simulator | - |
| optimization-workshop | Optimization Workshop | 12 | builder | - |
| rain-gauge | Rain Gauge | 12 | simulator | - |
| solid-spinner | Solid Spinner | 12 | explorer | - |
| slope-field-garden | Slope Field Garden | 12 | sandbox | - |

- **cone-slicer:** Topic line under the title on the tool page: "conic sections". Overlap note (left for you to settle in the spec): One of three slice-or-spin-a-solid explorers in 9-12 math (with slice-it and solid-spinner). Suggested fix (reshape): "Conic Focus Finder": Drag a point so its distances to two foci (or to a focus and a line) follow one rule, and watch an ellipse, a hyperbola or a parabola appear; then find each one's equation. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title.

- **fire-lookout-triangles:** New in the gap fill (docs/agents/gapfill/core/notes.md).

- **speedometer:** Spec note from the overlap pass: lead with the derivative as rate; graph matching belongs to the live motion-graph-match.

### Math: statistics (`math-stat`, 6)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| design-the-study | Design the Study | 12 | story | - |
| courtroom-statistics | Courtroom Statistics | 12 | roleplay | - |
| fair-dice-investigation | Fair Dice Investigation | 12 | mystery | - |
| data-desk-distributions | Data Desk: Distributions | 12 | data | data-desk |
| game-show-strategist | Game Show Strategist | 12 | simulator | probability |
| sample-machine | Sample Machine | 12 | simulator | sampling |

- **design-the-study:** Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: Shares S-IC.B and the newsroom setting with the live poll-workshop, which already covers sampling, wording and bias.

- **courtroom-statistics:** Kept as written in the overlap pass (Kept: 'the null is innocent until proven guilty' is the standard teaching frame; the alternative would repeat fair-dice-investigation. Call closed).

### CTE: pathways and personal finance (`cte`, 9)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| interview-simulator | Interview Simulator | 9-12 | roleplay | - |
| startup-booth | Startup Tycoon | 9-12 | tycoon | - |
| prototype-lab | Prototype Lab | 9-12 | lab | - |
| path-planner | Path Planner | 9-12 | builder | careers |
| hospital-shift | Hospital Shift | 9-12 | story | careers |
| paycheck-decoder | Paycheck Decoder | 9-12 | explorer | money |
| compound-interest-head-start | Compound Interest Head Start | 9-12 | simulator | money |
| the-credit-card-diaries | The Credit Card Diaries | 9-12 | story | money |
| covered-insurance-claims | Scam Shield | 9-12 | escape | money |

- **prototype-lab:** Spec note from the overlap pass: iterate one product; breaking down a global problem belongs to design-challenge-studio.

- **compound-interest-head-start:** Topic line under the title on the tool page: "saving and compound interest". Reshaped by the overlap pass (Cory accepted; the title and concept above are the new ones). The clash it fixed: Grows savings over decades like the live savings-plan and market-time-machine. Family: Stays in money, and compound interest is back at the core (the pass had moved it to emergency funds).

- **scam-shield:** Topic line under the title on the tool page: "insurance, deductibles and scam texts". Overlap note (left for you to settle in the spec): An escape room on scams beside capture-the-flag; a 'year of surprises' would repeat Rainy Day Fund. Suggested fix (reshape): "Covered": Compare three insurance quotes side by side; a slider trades the monthly premium against the deductible, and a claim calculator shows who pays what for a stolen bike or a fender bender. A last round sorts real insurer messages from fake 'claim refund' texts. Take it, or solve the clash another way and say how in "Not like". Keep the topic word in the title. Family: stays in money.

### Computer science 9-12 (`cs-hs`, 8)

| Id | Title | Grade | Format | Family |
|---|---|---|---|---|
| emerging-tech-pitch | Emerging Tech Pitch | 9-12 | studio | - |
| cloud-through-time | Cloud Through Time | 9-12 | timeline | - |
| dice-in-the-chatbot | Dice in the Chatbot | 9-12 | lab | - |
| pull-request-review | Pull Request Review | 9-12 | mystery | - |
| sprint-board | Sprint Board | 9-12 | builder | - |
| computing-team-stories | Computing Team Stories | 9-12 | explorer | - |
| coin-cell-greenhouse | Coin Cell Greenhouse | 9-12 | simulator | - |
| catalog-column-rules | Catalog Column Rules | 9-12 | data | data-desk |

- **emerging-tech-pitch:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

- **cloud-through-time:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

- **dice-in-the-chatbot:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

- **pull-request-review:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

- **sprint-board:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

- **computing-team-stories:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

- **coin-cell-greenhouse:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

- **catalog-column-rules:** New in the gap fill (docs/agents/gapfill/cs/notes.md).

