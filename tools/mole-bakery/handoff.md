# Mole Bakery build handoff

## Structure
src.html starts from the kit starter frame, using kit:curio and theme-912. Styles adapt the painted workbench and controls at real viewport sizes. The inline script contains the reaction table, stoichiometry, transactional week state, rendering and a particle canvas. Curio.voice owns narration; the tool updates its hint synchronously. ART and PANTRY_ART hold all bundle tokens.

## Tricky parts
The bake commits ingredients and payment synchronously, then animates a snapshot. A revision token drops obsolete animation callbacks. No control waits for the oven. Each order can pay only once. Storage is guarded and validated at load; it is convenience storage, not tamper-resistant scoring.

The mass ledger includes vinegar solvent, ethanol that escapes, and secondary soda decomposition. Waste means excess before the oven, so it includes soda subsequently converted into carbonate. R4's three-gas volume is an idealized gas-volume comparison.

## Decisions and open questions
- Keep the spec's fictional Day 4 90 percent gas retention, plainly labeled. Its measured ratio rounds from 89.96 percent.
- Follow the current build brief and use OpenAI image generation rather than the spec's older local FLUX plan. All 14 assets contain no people.
- Mix exact is available in both modes, following the explicit interaction requirement over Test kitchen's earlier wording about a shortcut. It solves only the second ingredient, not the gas target, and logs its chain.
- The spec omits Day 6 payments. Reuse the established product payments: biscuits 20, cake 18, cookies 14.
- Store award and inventory before visual animation so interrupting or reloading cannot duplicate payment. A paid order stays paid when its animation is canceled.
- The brief says to create the report early, but the owner's direct instruction says to stop when it is written. The report is finalized last.
- The named shared molecules engine and family document are absent. Use the restricted local formula adapter pending the shared engine. This is an explicit dependency gap.
- Apply the explicit four-significant-figure rule to moles, even where a worked example prints only three significant figures. Internal calculations keep the unrounded atomic sums.
- Tiny but nonzero wrong bakes receive the mandated half payment. They never pass the full-price gate; the till is a game ledger, not an assessment of independent calculation.

## Sensitivity
No cultural, religious, historical or body-related content. No people appear in generated art. Food taste labels describe the specified model, not instructions to taste laboratory substances.

## Engine changes wanted
- kit/molecules.js, missing file: provide ATOMS, parse, molarMass, tally and SUBSTANCES as described in tools/bond-battle/spec.md. Then replace this tool's restricted local adapter with calls to that shared API and add the listed compound entries. No kit or docs file was changed.

## Next review
Cold review should examine the glass cutout and the visual balance between bowl and oven, keyboard input at compact sizes, gas-retention wording, and the mandated half-price rule for tiny but valid bakes. Build only; no polish round or commits.
