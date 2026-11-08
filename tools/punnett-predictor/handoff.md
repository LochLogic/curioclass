# Punnett Predictor build handoff

## Structure
src.html starts from the kit starter. Its own CSS lays out a naturalist's bench without scaling the whole scene. Curio Class kit handles motion, sound and narration. The graphing family Plane draws Converge with log10-transformed horizontal coordinates. Tool-local functions implement exact gamete probabilities, seeded sampling, phenotype classification and chi-square.

State holds separate Cross and Linked broods. The seeded stream belongs to its brood. Model edits clear the affected brood. The animation changes displayed counts only; the final sample is committed immediately. Play owns one cancellable timeout. Mode changes and parent changes stop it synchronously.

Opening female linked meiosis switches from the independent model once and clears that obsolete brood. Reopening the same model preserves its brood. Male-header meiosis explains its identical bv products without exposing the female crossing-over slider.

Converge uses a clip rectangle tied to the currently displayed offspring count during a large batch. Resize rebuilds that rectangle from the same progress state. Desktop controls sit outside the results scroller. On phones Breed, Clear and Test remain in a dock; the main content scrolls above the hint and dock. Explicit actions reveal their requested tray, fit card or meiosis view without taking focus on load.

## Open questions resolved
- Keep meiosis-only scope. No nondisjunction step was added. Notes explicitly limit HS-LS3-2 coverage and point to Protein Factory for mutations.
- Keep the supplied Campbell-style fly counts. The edition was not available to verify. Label them Morgan-style, retain their exact values and document that attribution remains open; do not substitute a different dataset.
- Use painted pea and fly cutouts. All 20 spec assets are generated in this build; none contains people.

## Spec conflicts and decisions
- The spec requests local FLUX, while the build brief and user require the image tool. Used the built-in image tool, with individual prompts and OpenAI credit.
- genetics.js, probability.js and docs/families/genetics.md are absent. Built the specified mechanics locally inside this tool without writing shared files. No protein or creature API was invented.
- A testcross has four female gamete types and one male type. The requested 4 × 4 display repeats bv male headers and labels that repetition. After linkage is enabled, female columns are weighted rather than falsely implying equiprobable cells.
- Female fly headers print their probabilities. Zero-probability columns keep their genotype labels but mute their specimen pictures; they are possibilities of the independent model, not possible offspring at zero recombination.
- Rr × Rr has a 25% chance per displayed box and 50% aggregate Rr probability. Accessible cell labels state both, resolving the spec's ambiguous 'Rr, round, 1 in 2' cell example.
- Four meiotic products need not have different genotypes. Two unlinked genes can orient two ways, but one meiosis uses only one. Both alternatives are shown at line-up; products show one possible orientation.
- Crossing-over slider d is recombinant gamete percentage. A crossover involves two of four chromatids. Text does not equate d with percentage of meioses experiencing an exchange.
- The requested fitYes voice overclaimed that chance explains the result. Wording now says compatible, not proof. fitNo uses rare rather than impossible.
- Motion off preserves the six three-second Play beats. This follows STANDARDS and POLISH timing rules where the spec's phrase 'off with Motion off' could suggest skipping playback time.

## Art review
The two full-wing fly assets were redrawn once because the first magenta key tinted their wings pink. The selected redraws use a green key, neutral wings and the standard pipeline's despill option. First candidates remain in Scratch. All images were inspected, including the finished 240-pixel cutouts.

## Sensitivity
This is organismal inheritance using peas and flies. No human traits or bodies are modeled. Family notes avoid inferring a person's genotype from appearance or presenting one-gene examples as a model for human identity.

## Engine changes wanted
- Missing kit/genetics.js and docs/families/genetics.md: add the spec's Gene, Genotype, gametes, cross, breed, phenotype, chiSquare, Punnett, Meiosis and Skins API when shared code is commissioned. Promote tested mechanics after three real tools need them, per BASELINE rule 13.
- Missing kit/probability.js: a standard seeded Rand and Converge wrapper would remove the local implementation. This build uses its own explicitly documented Mulberry32 stream, so its seed-1 result cannot promise identity with a future family engine.
- No existing shared file was changed.

## Review next
Cold review should inspect phenotype art fidelity, linked-chromatid continuity, compact layouts and voice with the final friendly-dad recordings. This run is Build only.

## Cold review repairs, 2026-11-08
- The tally animation now reveals actual prefix counts and fractions, rather than interpolating the final ratio. Its tray reveal and thousand-event voice follow displayed N. Clear, model edits, repeat Breed and mode changes still cancel synchronously.
- Mendel row selection shows expected dominant count and observed departure, labels bars O/E for grayscale, gives immediate specimen feedback, and uses a fixed recorded-line-ready hint. Try this total stays above the detailed result.
- Short landscape meiosis puts Back/Next/Play and Close in one row, reserving at least 90 pixels for chromosomes. Automatic Play now updates the hint at each step and at the products.
- The 375-pixel Mendel view gives Try this total the existing bottom action dock; all seven trait choices remain visible. Stopping a reveal or changing modes refreshes the status for the actual brood.
- Both vestigial flies were redrawn with neutral edges and explicit curled stubs, using the corresponding normal-wing fly as a reference. A display scale aligns body sizes. Original art is preserved only in Scratch; finished WebP files use art.py --rekey.
- Motion states on screen that its preference stays on device. Fit text now explicitly describes the upper tail under the model.
- Primary Mendel counts were verified through Brown University's MendelWeb mirror. OpenStax 13.1 Figure 13.3 independently confirms all four fly counts, resolving dataset verification without substituting data. The Campbell edition itself remains unchecked.
- No new topic, nondisjunction step, score or mastery gate was added. Shared engine work and full HS-LS3-2 coverage remain outside this tool's authorized scope.
- The single final audit completed with 112 mechanical leads. Confirmed layout issues were repaired: results no longer pass beneath Breed/Seed, phone content has a bounded scroll area, and compact linked-allele labels no longer touch. Phone meiosis keeps Close and the step controls together, with the scientific scene filling the remaining space.
- Repeated taps on the current mode or already-open parent panel preserve narration instead of hushing it. Switching modes and closing still interrupt normally.
- Audit keep regions now identify the requested fit result and the complete Mendel trait table plus action. Supplemental cards and keyboard-inspectable mini-square content remain available by scrolling.
- Targeted post-audit evidence: 12 desktop layout states, 13 phone states, the main voice path, all six cheap routes, four quick-tap regressions and 62 actual-prefix animation frames passed. All resulting frames inspected. Scratch review-final-behavior-receipt.json and review-receipt.json record the final behavior and raw bundle hash.
- Review host.html is absent and ports 8745 / 9940-9947 are closed. Windows denied the CIM process inventory query; the port checks and exact permission error are preserved in Scratch review-cleanup.json.

## Prior build test-process cleanup limitation (historical)
This is the builder's recorded result, not refreshed in the cold review: those ports are outside the review's assigned 9940-9947 and 8745.
Chrome debugging ports 9970 through 9977 are closed and host.html is removed. The local test host on 8775 still responds. Windows denied termination of the exact matched `python -X utf8 -u scripts/drive.py punnett-predictor --host 8775` processes (PIDs 15364, 44808, 35032, 19084 at inspection). No unrelated process was terminated. Scratch native-host-close.json records the matched commands and Access denied results; validation-receipt.json records the live port. This is a runtime permission limitation, not an approval-review rejection.
