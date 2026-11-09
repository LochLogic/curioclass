# Equation Balancer handoff

## Layout and code
`src.html` is a readable standalone source built from the kit starter. The shared kit and Grade 9-12 theme precede the tool styles. Content and masses are embedded constants; the three modes share the same coefficient cards and ledgers. ART tokens are declared once and reused for menu thumbnails and story cards.

The local chemistry block provides parse, tally, compare, molarMass, ATOMS, SUBSTANCES and molecule drawings. Integer thousandths make the two mass totals exact before display rounding. Parsing supports parentheses and dot hydrates. The ledger always tests elements before optional whole-group display. Coefficient edits update immediately; copies only animate their visual arrival.

`window.__tool` exposes the specified state, setMode, load, set, ledger and predict API, along with pure chemistry helpers and voice logs. `load` uses IDs L1-1 through L5-5 and P1 through P10. `predict(n, choice)` accepts the original zero-based choice index or formula text. Browser evidence and the independent SymPy check are in `_scratch/equation-balancer/`.

## Spec decisions and contradictions
- Open question: retain the recommended ion-charge Predict scope for HS-PS1-2. Do not add new-fuel combustion prediction.
- The build brief's OpenAI image tool overrides the older local-FLUX art instruction. All 25 images are newly generated, with people=false.
- The shared `kit/molecules.js` and its family document do not exist. They cannot be added under the authorized write boundary. The required counting functionality is local; it can be replaced when the shared engine exists.
- PubChem CID 61745 confirms magnesium peroxide, MgO2. The lookup calls it a different compound instead of the spec's false unstable-substance claim. Ordinary neutral H3 and sodium/chloride charge wording are qualified to avoid absolute claims about every possible chemical condition.
- The peroxide story describes decomposition, preserving the cotton-pad image without treating a cut as wound-care instruction.
- Emergency oxygen generators use chlorate chemistry, commonly sodium chlorate. The potassium chlorate story describes the reaction type rather than claiming all pictured aircraft equipment contains KClO3.
- Small molecules have bonds; generic atom inventories do not invent geometries or bonds for complex species. This is an explicit gap against the absent engine's full structural drawing request.
- A small choice set with feedback is instructional, not an assessment. Predict saves no score or mastery claim. Levels checks mean balanced in lowest terms; the specified already-balanced equations earn their truthful check on entry.

## Engine changes wanted
`kit/molecules.js`: supply the API specified in bond-battle/spec.md, with complete formula parsing, shared ATOMS masses/colors and reliable SUBSTANCES coordinates, bonds and ionic polyatomic clusters for every Content formula. Add `docs/families/molecules.md`. Replace this tool's local chemistry block only after parity checks against all 35 equations.

## Sensitivity
No people, cultural content or body depictions. Respiration is a symbolic cell-chemistry context. A reviewer should check that the peroxide image and teacher-demo sodium example are never read as instructions to perform hazardous reactions or treat wounds.

## Next review
This is Build only. See codex-report.md for observed checks and limits. Do not infer review approval, deployment or recorded-voice completion from stage=built.

## Final build evidence and limits
The bundle is 1,585,898 bytes, including 1,110,134 bytes of generated WebP art and no recorded audio. `_scratch/equation-balancer/final-verification.json` records source and bundle hashes, 21 passing evidence checks, and closed tool-owned ports. There are 143 passing functional assertions and an independent exact arithmetic check of all 35 equations.

The one full audit finished with 40 leads. Its frames are a pre-fix snapshot. Targeted final frames and JSON measurements verify the affected fixes; the full audit was not repeated. The audit could not enter its phone iframe, so all three modes were checked separately in the 375x812 host. This is not a claim that the final full audit is clean.

The phone keeps the trays, steppers and ledgers together; secondary equation navigation and story pictures require scrolling. Up to eight copies are drawn, with smaller models in compact layouts; larger counts use a multiplier. The dot display caps at 24 while numeric counts stay exact. Per-element gram detail is suppressed on compact screens, with total grams retained. These counting models are not laboratory or molecular dynamics simulations.

The odd-oxygen hint appears only for the first fuel count in the two relevant combustion cases, when the recommended plus button is enabled. At the cap it gives ordinary adjustment guidance. P8's teacher-demo safety text remains in the visible hint after Reset.

Predict rotates choices and gives no saved score or mastery mark. Its required retries still allow a student to enumerate choices. Do not use correct-choice feedback as evidence of independent product prediction. Quick repeated mode or Reset taps can interrupt narration; the visible hint and Read remain available. At the required two-second pace, all three mode introductions were heard and both balance events repeated.
