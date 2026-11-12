# Codex report: mole-bakery

## Built

- Grade 10 Test kitchen and six-day Bakery, in one offline HTML file.
- All five reactions, live grams-to-moles calculations, limiting rows, secondary soda decomposition, taste, ideal gas volume and complete mass accounts.
- Four painted products, 14 generated illustrations, particle pairing and gas bubbles, an oven bake, pantry purchases, receipts, saved week and ledger.
- Transactional bakes spend stock and award coins once before animation. Input, reaction changes and modes interrupt immediately.
- Source: src.html. Playable bundle: mole-bakery.html. Metadata remains tool.draft.json with stage built.
- No commits, deployment or polish round. The report was written last to honor the owner's stop instruction.

## Numbers check

Evidence: ../../_scratch/mole-bakery/check_math.py, numbers.json and check-results.json.

- All 33 functional checks passed. All five equations conserve each element.
- 1,250 mass-balance cases: largest discrepancy 5.684341886080802e-14 g.
- Default R1: 0.04999643 mol gas, 2.20029 g CO2, 1,223.16 mL; before and after 13.61 g.
- R1 at 6.00 / 9.41 g: tartar limits; R5 adds 0.01070859 mol CO2; total 0.06071488 mol, soapy.
- R2 target vinegar: 72.0624 g before rounding. 5.04 / 72.06 g gives clean 0.0600 mol.
- Day 3: three separate 1.88 g batches use 5.64 g tartar and leave 0.36 g. Exact combined 0.030 mol would use 5.645289 g.
- Day 4: 9.01 g glucose theoretically makes 4.40197484 g CO2; 3.96 g is 89.9596%, displayed 90.0%.
- Day 5: exact ammonia requirement 2.37165 g. 2.37 g passes; 7.11 g produces 0.269812 mol and fails rise.
- Day 6: 3.36 + 2.52 g soda leaves 2.12 g. Completed test week: 154 coins after 11 coins of necessary purchases.
- Avogadro dot conversion: 0.001 mol = 6.02214076e20 particles. PV/nRT gives 24.4654037 L/mol; specified math uses 24.465.
- NH4HCO3 sums to 79.055, displayed explicitly as 79.06. Internal calculations retain unrounded sums.
- Four significant figures are used for moles, even where a spec example uses three.

## Facts checked

| Student-facing fact | Named source and check |
|---|---|
| Grams divided by molar mass gives moles; coefficients set mole ratios | [OpenStax Chemistry 2e 4.3](https://openstax.org/books/chemistry-2e/pages/4-3-reaction-stoichiometry); independent recipe calculations above |
| The reactant with the smallest stoichiometric capacity limits product | [OpenStax Chemistry 2e 4.4](https://openstax.org/books/chemistry-2e/pages/4-4-reaction-yields); both ingredient capacities appear in the rows |
| Actual divided by theoretical yield gives percent yield | Same OpenStax 4.4; fictional proof-box data are labeled on screen |
| Avogadro constant and particle key | [NIST SP 330](https://www.nist.gov/pml/special-publication-330/sp-330-section-2); exact constant and rounded keys recomputed |
| Gas volume at 25 degrees Celsius and one atmosphere | NIST CODATA gas constant and ideal gas law; recomputed 24.465 L/mol |
| Formula masses and the soda/carbonate and ammonium bicarbonate reactions | PubChem CIDs 516892, 23681127, 176, 5793 and [14013](https://pubchem.ncbi.nlm.nih.gov/compound/ammonium_bicarbonate), as cited in spec.md; formulas and sums checked locally. Full PubChem pages hit a browser challenge; indexed primary-source entries supported ammonium bicarbonate's mass and decomposition |
| Vinegar acidity is labeled per 100 mL | [FDA CPG 525.825](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/cpg-sec-525825-vinegar-definitions-adulteration-vinegar-eels); the tool explicitly states its approximate 5 g acid per 100 g model |
| Yeast fermentation gives ethanol and carbon dioxide | [OpenStax Biology 2e 7.5](https://openstax.org/books/biology-2e/pages/7-5-metabolism-without-oxygen); R3 atom and mass balances checked |
| Gas escape does not destroy mass | NGSS HS-PS1-7 and balanced equations; product accounts include vinegar water, ethanol, carbonate and gases |
| Sour/soapy/clean threshold, prices, payments, day inventories and 90% retention | Explicit fictional/model rules from the spec, not universal food-quality or yeast-efficiency claims. Notes distinguish these assumptions |

R4's volume is an ideal gas equivalent for its three hot-oven gases. Notes explain the room-temperature water-vapor limitation. Bread results distinguish 3.96 g kept from 4.40 g made. Vinegar leftovers are labeled acetic acid, not whole vinegar.

## Break it

Evidence: checks.js, cheat-checks.js, check-results.json and cheat-results-final.json in Scratch. The additional cheat matrix passed 10 of 10 checks.

- Repeated Bake, including ten immediate presses: no duplicate payment or stock consumption.
- Interrupting a paid animation: the receipt remains committed; no refund or second award.
- Zero, negative, infinity and beyond-stock entries: refused or unable to earn payment. Day 3 refuses more than 6.00 g, then refuses a fourth 1.88 g batch.
- Wrong gas with clean taste, right gas with sour taste, and extra soda gas with soapy taste: never full payment.
- Cookies at three times the intended gas: half price, never a pass.
- Decline then Bake: no payment. Buy until the till empties: no negative balance. Closed supplier: no purchase.
- A 1,001-value soda sweep accepted only chemically valid target-and-taste mixes.
- Mix exact at zero cannot pay. With a positive first amount it fills only the second amount and prints the calculation chain.
- Reload preserved the completed six-day ledger. New week reset inventory, orders, day and till.
- Important limit: the mandated half-price rule still rewards a tiny nonzero failed bake. It cannot earn full price or repeat the same order, but coins are not evidence of mastery.
- Live forecasts and Mix exact intentionally scaffold calculation. This is an exploratory model, not an independent-answer assessment; tuning a valid recipe remains possible under the spec.

## Voice walk

Curio.voice, scope by mode; playful-friend / Laomedeia, kept bank entry. Twelve manifest lines, no recordings generated, as instructed. Browser speech is the current fallback.

- Held main path at two-second gaps: wKitchen, baked, wBakery, then Read of the current Bakery hint. Both mode welcomes started.
- Side path: day5, half. A separate held mode-entry fixture heard day3.
- Three paid orders at a two-second action pace: paid started three times; till 45 from 30.
- Two failed orders: half started twice; till 35. The newer result cuts stale speech, so the last result completes.
- Five held bakes at two-second gaps after the audit fix: five baked starts, zero lost events.
- Two taps on the selected Bakery mode at 0.7-second gaps: one welcome, no cut.
- Read stops speech and reads the current hint. Stale queued limiting tips drop on a newer mix, remain unmarked, and may trigger again.
- Files: voice-main.json, voice-side-fixed.json, voice-day3.json, paid-voice.json, half-voice.json, voice-five-bakes.json and voice-same-mode.json in Scratch.

## Feel check

Student walk used held clicks, keyboard input, real slider dragging and an automated full week, not a classroom trial.

- Best moment: the cookie order pays in full at 2.37 g while the tempting threefold batch visibly misses the rise band. The warm oven, detailed food and receipt give the numbers a place.
- Flat moment 1: repeated baking queued a long spoken result. Replaced it with the short Bake ready cue and immediate current-result speech.
- Flat moment 2: discovering a closed Day 6 supplier without preparation felt arbitrary. Day 5 now warns the student to stock up.
- Early oven enlargement overlapped the recipe and squeezed the bowl. Container-relative bounds now keep it inside the workbench; glass retains its aspect ratio.
- Compared both bar tools. Scratch bar-comparison.png places this tool beside Beat Lab. The finished scene has painted depth, glass, brushed steel, food texture, warm directional light and distinct particle shapes; it does not look plain beside the bar.
- Bakery's bowl is small in the shortest four-order preview. The order board remains dominant there; see the layout limitation below.

## Done when

1. PASS: ready R1 recipe, clean taste, correct gas and 13.61 g balance. check-results.json and final-particles.png.
2. PASS: 6.00 / 9.41 g gives tartar limiting, secondary gas and soapy taste. Functional and cheat matrices.
3. PASS: vinegar solution factor and 5.04 / 72.06 g result. Functional matrix and vinegar-cake.png.
4. PASS: Day 3 stock refusal, three full payments and fourth refusal at 0.36 g. Functional matrix and paid-three-orders.png.
5. PASS: fictional 90.0% yield, correct 9.01 g bread result, made versus kept labels. final-bread.png.
6. PASS: 2.37 g passes; 7.11 g fails. cookies-correct.png and cookies-overrise.png.
7. PASS: Day 6 leaves 2.12 g soda; ledger has six limiting-ingredient records; reload and New week checked.
8. PARTIAL: bowl and rows lead in Test kitchen, oven leads during Bake, Bakery board and bowl are central. Bakery uses board above bowl rather than the requested side-by-side arrangement, particularly to keep four orders readable.
9. PASS: mid-bake input cancels immediately. Revision guard tested; resize audit reports no exception or stuck control.
10. PASS after fixes: once-only how lines, repeated result events and live-action hints. Audit plus focused held-click logs above.
11. PASS for primary controls: every required size, 375 px host, keyboard and real range drag; all 14 images load, no people, clean final console, no external resource URLs or em dashes. Secondary details and phone purchases require scrolling.

## Wave lessons

- Hint and voice: PASS. Hints update synchronously; Read uses the current hint. Kit handles heard state and stale queues. Rapid-event loss fixed and retested.
- Focus and layout: PASS for controls. No focus on load, static numeric controls, order buttons retained under the pointer, preventScroll for deliberate test focus. Mix exact log moved below day actions so those controls stay put.
- Sizes: PASS for required primary controls. Final compact day buttons bottom 410 px at 680x425; phone ingredients bottom 759.75 and day buttons bottom 808.75 in an 812 px iframe.
- No giveaways: LIMITED BY SPEC. There is no hidden-answer quiz. Live mole capacities and forecasts permit tuning; valid chemistry and finite order consumption determine payment.
- Honest numbers: PASS. Fictional yield, ideal gas reference conditions, vinegar approximation and game coins are identified. All product mass is accounted for.
- Standards: PARTIAL dependency. HS-PS1-7 is enacted through equations and mass accounts, but the named molecules engine is absent. Local adapter is documented rather than changing kit.
- Motion off: PASS. No infinite animation remains; the specified instant bake is used. Steam stops.
- Short choices: PASS for the four order cards and reaction picker. Supplemental mass details scroll; phone purchasing is farther down the page, not a clipped subset of orders.
- Resize mid-animation: PASS. Audit stress checks found no exception or permanently disabled control.
- Welcome put off late: PASS. welcomeAfter is not used. First-action welcome omission follows BASELINE rule 16; premise remains in hint and Read.
- Unknown stays unknown: PASS. No hidden diagnoses or undiscovered state are presented as known; ready food art illustrates the selected product.
- One look, one meaning: PASS. Reactants have distinct shape and color; gas uses rings. Gray/cream carbonate replaces excess soda during heating.
- Badge truth: PASS. Limiting row, taste, rise and paid/half status come from the same calculation.
- Hint changes back: PASS. Mode, recipe, order, edit, result and reset all update it immediately.
- No answer by copying words: NOT A DIAGNOSIS QUIZ. Names do not encode a separate correct choice; numerical forecasts are explicit scaffolding.

## Audit leads

One full audit completed, 28 leads: ../../_scratch/mole-bakery/audit/audit.md. It was not rerun; fixes received focused checks.

- Default 680, 800, 1000 and 1280 widths, Bakery 1280/1366, cookie 680, and duplicated bakery-board states: Follow every gram is below the panel fold. Retained as supplemental product accounting, not an answer option; weighing and Bake stay visible.
- Phone summary and five Buy buttons below the fold, including duplicated Bakery states: retained in the vertically scrolling page. Primary order, grams, scale, Bake and day actions fit. This remains a secondary-control scrolling limitation.
- Hidden reaction-water row overlapping the privacy note at 1920 and 760: fixed with explicit closed-details display:none. Final probe returned zero client rectangles for every hidden row.
- First Bake / Mix exact omit welcome: intentional under BASELINE rule 16. Current hint and Read preserve the instructions; no delayed welcome is queued.
- New week changed nothing on an already fresh week: added a visible reset confirmation and tone.
- Mix exact shifted day controls: moved its calculation log below them; final 680 px frame keeps day actions in view.
- Long Bake event lost in five rapid presses: short cue plus current-event replacement; final five-of-five log passes.
- Repeated selected-mode presses cut welcomes: same-mode selection now preserves state and speech. Focused quick-tap log has no cut.
- Other movement in the walk: mode changes are expected; Sound's kit label changes header widths. No primary weighing control rebuilt under the pointer.
- Resize stage: clean, no exceptions or stuck controls. Motion-off stage: clean. Final drive batches: zero console errors or warnings.

## Frames looked at

- All game PNGs in bar-frames, first-frames, layout-frames, sizes-frames, check-frames, voice-frames, voice-fix-frames, focused-frames, cheat-frames, final-frames and pay-voice-frames.
- All 26 audit PNGs, using contact sheets plus full-size inspection of key and omitted sheet-edge frames.
- Art sheet for all 14 finished cutouts/backdrop and their in-tool placements. Bar comparison viewed.
- All evidence lives under ../../_scratch/mole-bakery/. Early frames preserve the failures; final-frames and pay-voice-frames show the corrected build.

## Art made

Fourteen built-in OpenAI image-tool illustrations, full prompts in art/prompts.json, drawn_by codex on every asset, people false on all fourteen. Raw PNGs retained in art/raw. All finished assets processed through art.py --rekey; no paid generation script ran.

Art 431,976 bytes, about 432 KB / 422 KiB. Recorded voice 0 KB. Final bundle about 687 KB / 671 KiB, comfortably below the 2 MB goal. No redraws were needed; glass transparency and material detail were inspected.

Contrast: brand on panel 5.22:1; on the baseline section background 4.95:1; brand ink on brand 5.57:1; main text on panel 14.70:1.

## Art still to paint

None. No people assets were requested or generated.

## Engine changes wanted

kit/molecules.js is missing, confirmed again at closeout. Provide ATOMS, parse, molarMass, tally and SUBSTANCES as specified in bond-battle, then replace the restricted local adapter and register the listed compounds. No kit or family-document change was made.

## Left open

- Missing shared molecules engine; full-engine integration cannot be verified in this checkout.
- Bakery board-above-bowl layout differs from the requested side-by-side layout; the bowl is small in the shortest four-order preview.
- Supplemental mass disclosure and phone purchases scroll. Core controls fit without scrolling.
- The required half-price fallback rewards tiny valid failed batches. Forecasts allow recipe tuning. Neither the saved till nor full payment proves independent calculation.
- Day 6 payments were unspecified: reused established product payments 20, 18 and 14. Fictional Day 4 yield retained, as the open question leans toward it. Both decisions are in handoff.md.
- Recorded bank narration remains absent because Build explicitly prohibited recording. Browser fallback is functional.
- Procedural deviation: the bar instruction caused ignored snowy-mail-route and beat-lab bundles to be regenerated outside the requested write folders. Their source was not edited. Initial read-only commands also preceded the hard-timeout wrapper; subsequent build/check commands used hard limits.
- Final host.html removed. All test ports 8785 and 9980 through 9987 were closed at closeout. No commits or polish round.
