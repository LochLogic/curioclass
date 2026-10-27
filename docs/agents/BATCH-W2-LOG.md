# Wave 2 spec log

Rules: `docs/agents/BATCH-W2.md`. 58 specs in six groups (9-12 math, CTE, computer science), one agent per group, at
most three at once beside the wave 1 art agent. Wave 3 (9-12 science) follows, then one joint review.

## Agent reports

### math-alg (12, done)

- Rename proposed: unit-detective to "Unit Sense" (spec written to the old folder with `Renamed from:`).
- Family engines: algebra-tiles (kit/algebra-tiles.js: Poly, TileMat, Frame), described in full in
  algebra-tile-studio for expression-garden (6) and expression-match (7). balance (kit/balance.js: Frac,
  Balance.moves and solutions, Beam skins), described in full in equation-golf for snack-scale (K), balance-the-beam
  (1) and balance-puzzle (6); the build confirms each hole's par by breadth-first search. graphing used unchanged by
  intersection-quest, graph-story-lab and launch-pad. data-desk: which-model-wins asks for computed columns,
  chart.curve and a row filter on fit.
- Agent notes: intersection-quest's accent #ffe14d is close to hole-hunter's #ffe45c (grade 12); neighbors.py
  crashes on the cp1252 console when output has a theta (run with PYTHONIOENCODING=utf-8).

Open questions:
- [algebra-tile-studio] A-SSE.B.3c and A-SSE.B.4 on the module are not covered. Leave them, or place them elsewhere?
- [equation-golf] Quadratic solving (A-REI.B.4) is left to launch-pad, letter coefficients to model-my-world. OK?
- [unit-detective] Take "Unit Sense", or keep "Unit Detective"?
- [correlation-guessing-game] S-ID.A is touched only through box plots on each axis. Enough, or add a one-variable
  round?
- [work-rate-crew] True extraneous roots come from the audit's practice-sheet equations, not the jobs. Is a practice
  sheet OK inside a role play, or drop the audit and teach only "doesn't fit the story" roots?

### cte (9, done)

- Renames proposed: scam-shield to "Covered: Insurance Claims" (takes the overlap note's insurance reshape; settles
  the clash with phishing-spotter); startup-tycoon to "Startup Booth" ("Startup Tycoon" is the name of several games).
- Family engines: money written out in full in paycheck-decoder (2026 brackets, FICA, PLACES, loanPay, statement,
  grow, rng), used by compound-interest-head-start, the-credit-card-diaries, Covered and Startup Booth. careers from
  the career-cluster-explorer spec; path-planner adds a `p25` field, hospital-shift adds 9 healthcare careers.
- For the spec check: paycheck-decoder's accent #ffe14d is the same as intersection-quest's.

Open questions:
- [paycheck-decoder] Annualized withholding enough, or the full IRS Pub 15-T tables?
- [compound-interest-head-start] Keep the "A stops at 26" what-if? Saver A only wins above about 6.58%, higher than
  savings rates.
- [the-credit-card-diaries] Wording of the landlord ending and the report OK? Is "medical collections under $500"
  stable enough to teach?
- [scam-shield] Title "Covered: Insurance Claims" OK? Made-up insurer quotes OK?
- [path-planner] Military path framed right? Add `p25` to the shared careers.json?
- [hospital-shift] Add the 9 new roles to the shared careers builder? Do the privacy and oxygen scenes need a parent
  check?
- [interview-simulator] Is the small Resume lines mode enough, or a resume tool later? Is the optional, unsaved "Say
  it your way" text box OK?
- [startup-tycoon] "Startup Booth" OK? Best prices earn $15 to $20 an hour before taxes: too rosy? Add a valuation
  line ($1,000 for 20% means a $5,000 valuation)?
- [prototype-lab] Keep the 0.30 N tip target (a classroom simplification; at 1 N only Brief A's 110 and 120 mm bases
  pass)? Printer-time limit on by default?

### math-pre (14, done)

- Rename proposed: cone-slicer to "Conic Focus Finder" (the overlap note's reshape: strings and pins, no cone).
- Family engines: none new. function-family-reunion builds on kit/graphing.js; the others use Plane for plotting.
  identity-proof-race uses its own lap format (exact expressions, checked numerically at build).
- Accents moved off the algebra group's: flight-planner #3aa8ff, hole-hunter #fff533, optimization-workshop #2ff0b0,
  slope-field-garden #52f05a; identity-proof-race moved to hero-coach / #ff5cf0. Nine voices are shared with the
  algebra group (the bank has 23 kept voices for 26 math tools).

Open questions:
- [fire-lookout-triangles] The fire finder history line leaves the instrument unnamed (no source found). Leave it, or
  add the Osborne Firefinder later?
- [flight-planner] Magnetic variation left out (said on screen). OK, or add one plan with variation?
- [image-transformer] The 3x3 color filter is the only 3x3 work for A-REI.C.9. Enough?
- [polar-rose-studio] "Download PNG" saves a file to the student's device. OK, or only the on-device gallery?
- [cone-slicer] Agree with "Conic Focus Finder" and the reshape (no cone, no slicing)?
- [zoom-to-the-limit] Add F-IF.B.6 to its module (now AP-PRECALC.U1 only)?
- [speedometer] Implicit differentiation (AP-CALC.U3) not covered. Leave out, or another tool later?
- [optimization-workshop] Local linearity and L'Hospital's rule (AP-CALC.U4) not covered. Where should they live?
- [solid-spinner] U8 average value (8.1) and motion along a line (8.2 to 8.3) not taught here. Another tool, or a mode
  here? The shell method is left out on purpose (not in the AP CED). Agree?
- [slope-field-garden] Euler's method and logistic models are BC only; kept and marked BC on screen. Agree?
- [identity-proof-race] F-TF.B.5 and AP-PRECALC.U3 parts 3.1 to 3.8 and 3.13 to 3.15 are not taught here. Keep the
  module's codes, or narrow them? Fake cards (Race only) might feel like trickery. OK?

### math-geo (9, done)

- Renames proposed: proof-blocks to "Proof Tower" ("Proof Blocks" is a PrairieLearn tool); slice-it to "Slice and
  Stack" ("Slice It!" is a mobile game).
- Family engines, each in full: coordinate in coordinate-proof-lab (kit/coordinate.js on Plane: Frac, Rad, Coord,
  CoordPlane, RuleTable) for two-rule-race and sea-search-grid (5); probability in medical-test-paradox
  (kit/probability.js: seeded Rand, Frac, Trials, Tally, Converge, Population grid, TwoWay, Tree) for carnival-odds
  (7) and game-show-strategist (12); transformations in rigid-motion-twins (kit/transformations.js on Plane: Motion,
  classify, matches, symmetries, animate, MoveBar) for dance-floor-moves (8).
- Voices shared only with grade 12 math (hero-coach, big-sister, soft-breath, gentle-storyteller, gravel-ranger).
  coordinate-proof-lab moved off jade (#00e0a0, too close to optimization-workshop) to #ffc400.
- Unconfirmed fact, kept off screen: the exact doctor-survey figure in Gigerenzer 2007; the C1 card says only that
  doctors did better with counts.

Open questions:
- [proof-blocks] Keep "Proof Tower"? Levels open in order, or all open from the start?
- [ramp-and-roof] OK to use the ADA rules as the class standard for home ramps?
- [slice-it] Keep "Slice and Stack"?
- [packaging-challenge] The Shelf has real can sizes and no brands. Good, or add an invented cereal-style box?
- [coordinate-proof-lab] Trapezoid uses the exclusive definition. Keep, or inclusive? G-GPE.A.2 (parabola) left to
  Conic Focus Finder: OK? Move the exact Frac into kit/curio.js as Curio.Frac, shared by balance, coordinate and
  probability? Voice is hs-narrator (the only unused kept voices are K-2 teachers): OK?
- [medical-test-paradox] S-CP.B.8 (+) appears only in the tree view and B.9 (+) counting is not taught: keep the
  module's codes? Case C1 uses a real screening example's numbers, credited without naming the disease: OK?

### math-stat (6, done)

- No renames.
- Family engines: probability (game-show-strategist matches medical-test-paradox's API; asks for path-dependent Tree
  branches with given() and Converge with up to 3 series and running means). sampling (sample-machine lifts
  poll-workshop's engine into kit/sampling.js unchanged, adds hopper, draw, stat.*, repeat, theory; jellybean-jar can
  reuse it). data-desk (data-desk-distributions asks for median-of-halves quartiles as the documented rule, settable
  bins, chart.mark evidence marks, a log10 x axis and a normal curve overlay).
- Builder notes: the World Bank pull for desks 3 and 4 is re-pulled at build by the rule in the spec (check n and
  medians); the statehood years need confirming against an admission-date table.

Open questions:
- [design-the-study] Is an energy-drink study OK for school (adult volunteers, an AAP note; fallback is music versus
  silence)? S-IC.B.4 and the sampling half of AP-STAT.U3 left to poll-workshop: OK?
- [design-the-study, courtroom-statistics, data-desk-distributions] Light themes instead of the dark 9-12 theme. OK?
- [courtroom-statistics] For proportions the test's band and the AP (Wald) interval differ slightly. Show both, or
  only the AP interval with a note?
- [fair-dice-investigation] A board game cafe instead of a casino: OK? The independence test is only in help text:
  enough for AP-STAT.U8?
- [data-desk-distributions] AP-STAT.U2 covered only by desk 4: add a two-way table desk? Desk 1 includes recent
  presidents (Trump 70, Biden 78): fine?
- [game-show-strategist] Add the two engine additions to the probability family? Briefcases is modeled on a known TV
  format with no name, logo or catchphrase: OK?
- [sample-machine] Sampling distributions of a difference (AP U5) not covered. Add a two-hopper mode?

### cs-hs (8, done)

- No renames.
- Family engines: catalog-column-rules uses data-desk and asks for `t.validate(dictionary)` (engine and
  docs/families/data-desk.md in the same change); Seattle Public Library checkout data pulled at build by
  scripts/spl_checkouts.py. computing-team-stories adds 11 careers to careers.json through scripts/careers_data.py.

Open questions:
- [emerging-tech-pitch] The "late buses" brief became "Town meetings" so it doesn't repeat sprint-board's bus app:
  OK? No free-text box (students pitch out loud): add an unsaved one, or keep it out?
- [cloud-through-time] Company names off screen, towns and ENIAC/UNIVAC named: right line? The Dalles water figures
  come from newspaper coverage: keep, or show only that the records were released after a lawsuit?
- [dice-in-the-chatbot] Debate claim 8 says real large language models also sample their next words: OK, or stay
  inside what the lab measures? Students can type 60-character messages, never saved: keep, or chips only?
- [pull-request-review] Case 1 uses GPL-3.0 code in an MIT project: GPL, or a snippet with no license at all?
- [sprint-board] Built for one shared laptop; one per student would need syncing, which the no-network rule rules out.
  OK?
- [coin-cell-greenhouse] Made-up board sized like real parts: OK, or a real chip's numbers in Sources only? Blocks,
  not typed code: add a typed text view?
- [catalog-column-rules] Add `t.validate` to the shared data-desk engine in this tool's build? Rule-break counts
  known only after the build-time pull: OK?
- [computing-team-stories] Add 11 careers to the shared careers.json (hospital-shift asks the same)? Team 3 has a
  tribal nation's water manager and team 4 a copy editor named Ivy Two Rivers: should a Native educator review those
  portrayals before build?
