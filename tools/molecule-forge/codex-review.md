# Codex review: molecule-forge

## Played

Cold grade-7/adult walkthrough preceded reading the builder report, handoff, notes or source. Oxygen to water, separate H2, methane/shelf, Sticks/Spheres, drag/keys, diamond/salt tests, cut and unrestricted guide/Manual.
More than ten minutes of exploratory states and real held input; an agent assessment, not a child usability study. Strong tactile kit, immediate chemistry, no game layer.

## Findings fixed

- Blocker, general, src.html: Motion off discarded the conformer glide and left about 105 degrees labelled as the PubChem water model. finish() now settles the exact target; rapid Save also settles it.
- Blocker, general, seed bonds: order changed but its label stayed single. Order is in the UI signature; keyboard focus survives each update.
- Should fix, general, Undo: restoring a salt specimen lost its fracture/test state while keeping the fracture result. History now retains cut and test state.
- Should fix, general, first two minutes: new specimens could intersect in Spheres. Placement uses sphere radii and clear space; default view framing contains the specimen.
- Should fix, general, phone crystal: model crossed the inspector. Inspector sits below the model, with separate space above the tray.
- Should fix, general, sources: blanket permissions obscured ESA, DuPont, museum and article rights. Named per-page references and source-specific rights are now in Manual, guide and metadata. No restricted prose, figures or data tables copied.
- Should fix, general, metadata: repaired corrupted hook text and added the missing description.
- Should fix, general, keyboard atoms: Delete dropped focus onto the body and Crystal atom labels offered a nonexistent melt action. Focus now follows the remaining selected atom, or returns to the well when empty; crystal labels name the actual bracket controls.
- Should fix, general, audit: named source links could be 30 to 43 pixels wide. All drawer links now have a 44-pixel minimum width and height.
- Should fix, general, metal Push: bending is illustrative and does not recompute atomic slip contacts. Inspector and readout now identify neighbour counts as the unpushed pattern, with the limitation stated in Manual.
- Should fix, general, crystal drag: starting a drag on a crystal atom selected it instead of turning the viewer. Crystal dragging now rotates from both atoms and empty well; Forge atom editing is retained.
- Should fix, general, finished shapes: relaxation of a new separate component could alter an existing matched conformer. Relaxation now applies only to the edited component, keeping finished numerical geometry intact.
- Polish, general, flattest moment: axial crystal views hid coordination in a dense disk. Oblique first views, open Sticks spacing and a cut through the inspected atom expose its bonded neighbours.

## Findings left

Should fix, general: strict unbroken 60 fps was not met. At desktop 4x slowdown, 600-atom cadence median 16.7 ms, p95 33.3 ms (9 missed frames/149 intervals); 40-atom p95 16.8 ms (4 misses). Profile-guided cached geometry, baked sprites and simpler crystal paths improved median delivery from 19.2 to 16.8 ms. No physical Chromebook was tested. Bounded optimization did not eliminate missed frames; this remains an explicit FAIL of the strict cadence item.

## Break it

No score, goal, level, quiz, completion gate or collectible book exists. Atom counts and open spots describe the actual selected graph.
Independent controller reconstruction and identity checks: 287 checks, zero failures; all 32 hand-built molecules, 72 recognized graphs, aromatic alternatives and unknown H5N3.
Independent numerical pass: 478 checks, zero failures; explicit valence/formula arrays, finite coordinates, crystal budgets/equal bond distances, inside coordination and 1-mm salt estimate.
40-atom cap, 30-step Undo, empty well, every atom, zoom 50/300 percent, triple-carbon rejection, all seven Push/Current outcomes and resize mid-action: no exceptions or locked controls.
Targeted checks confirm seed text/focus, salt Undo, completed calm/saved water geometry, separate specimens, native crystal drag and unchanged finished geometry while another component is edited. Shelf limit/reload and blocked storage also pass.

## Voice walk

Held taps, 2-second pace: H, H, Read, Crystal, Na, Cl, Grow, Push, Current, Read, Sound off, Read.
Heard: first-run hint once; water readout; salt/no-current readout; the same Read with Sound off. No automatic names or result narration.
Curiosity brief's "then only when Read is pressed" takes precedence over the spec's automatic names/test lines. No per-mode lesson narration added.
Hint expected/spoken 1/1; requested Read expected/spoken 3/3. Browser speech fallback, no recorded knowing-guide clips. Runtime allLines matches voice/lines.json.

## Facts checked

All checks 2026-11-05; raw build source records are retained. [Every graph/fact URL and permission](../../_scratch/molecule-forge/review-material.json); [478 numerical/source checks](../../_scratch/molecule-forge/review-data-results.json).

- 72 numerical graphs: NIH PubChem PUG REST, public-domain federal records; independent formula, valence and bond counts. Only atom/bond/coordinate arrays, not contributor annotations.
- Computed conformers: https://pubchem.ncbi.nlm.nih.gov/docs/pubchem3d confirms computational models, not measured structures. H2/silane/allene reference models stay explicitly labelled.
- Geometry: OpenStax Chemistry 2e 2019 chapter 7, CC BY 4.0, versus NIST CCCBDB water/ammonia/methane experiment records. Computed water 103.9799 degrees stays distinct from experimental 104.4776.
- Licence: https://ic.arc.losrios.edu/~paynem/textbook_os_2e/chemistry_2e_intro.pdf explicitly says 2019 CC BY 4.0. Current OpenStax web preface instead says CC BY-NC-SA; it was used only to cross-check facts.
- Seven lattices and qualitative material tests: own finite graphs, OpenStax 2019 chapter 10; covalent/metal/ionic/network distinctions cross-checked against current chapters 10.5, 10.6 and 18.3. No simulated strengths or current magnitudes.
- Radii/colours/spacings: named Cordero 2008, Bondi 1964, Shannon 1976, CRC 97th edition and Jmol references. Publisher rights retained; only specified factual constants, no copied tables or code. Direct publisher access was partly blocked.
- Sun/hydrogen: NASA Cosmicopia and Radio JOVE Sun introduction. Water/71 percent: USGS Water Science School and NASA Aqua. US government factual references; no images copied.
- H2S odour: OSHA overview and CDC/NIOSH hydrogen sulfide. Hydrazine/thrusters: NASA Cassini Engine and ESA Euclid fuelled for launch. ESA text remains copyrighted; fact independently summarized.
- Urea/1828: Wöhler original via ChemTeam, ACS Urea. Original is public domain; translation/ACS rights retained, no excerpts used.
- Ethanol/78 C: PubChem 702 and CDC/NIOSH Ethyl alcohol (173 F converts to 78.33 C). Dimethyl ether/-24.8 C: PubChem 8254 and EPA-hosted DuPont report. Submitter report is not claimed public domain.
- Glycine/67P/2016: ESA Rosetta article and Altwegg et al., Science Advances, e1600285, CC BY-NC. Only the independently summarized historical fact, no restricted paper data/prose.
- Benzene/Faraday/1825: Royal Institution sample and Science Museum Group collection co12946; museum factual fields CC0, descriptions CC BY 4.0, Royal Institution copyright retained.
- Caffeine/coffee/tea: FDA Spilling the Beans plus PubChem 2519; no dosage or advice. Twenty-two other page facts are structural counts independently recomputed from the packed graphs.

## Sensitivity

An isolated stomach illustration is neutral anatomy; no treatment, chemical-handling instructions, cultural generalizations or people pictures. Reviewers can check that context, alongside the source-rights distinctions.

## Flattest moment left

Invalid seed combinations still answer mostly in a short result line. The crystal inspection, formerly the flattest moment, now exposes the actual coordination without adding a game.

## Short test

- Kid opens it unassigned: PASS, two taps change the waiting oxygen into water; another pair makes a separate specimen.
- Adult plays for fun: PASS, isomers, rings, unfamiliar filled graphs and seven lattice patterns support independent questions.
- Real material is the interface: PASS, the editable graph, computed coordinates and generated lattice are the working surface; qualitative tests are labelled as such.
- Works without score/finish: PASS, every guide page is open and no action unlocks or ends anything.
Fresh comparison: [Molecule Forge beside Elements Inspector](../../_scratch/molecule-forge/review-frames/review-frame-comparison.png).

## Graphics

All forty existing paintings, 39 audit frames and the review frames inspected in contact sheets and individual views, with all required dimensions opened individually. Coherent material style, no placeholders or people. Kept all art; changed the working crystal rendering, not the paintings. Bundle 1,145,511 bytes (about 1.14 MB), including all forty paintings; the 2 MB goal is met.

## Audit

The single final audit completed with exit 0 inside its 40-minute limit: [audit.md](../../_scratch/molecule-forge/review-audit/audit.md), 229 raw leads. The small source-link targets were confirmed and fixed, then measured at 680 and 1366: 54 Manual links and two guide links meet 44 by 44 pixels.
Other leads are intentional canvas/control overlap, a dismissed first-run hint, inert bench regions behind modal drawers, scrolling reference citations, or padded title rectangles without glyph collision. Three resized-atom leads compared labels changed by the accessibility fix; final native resize of all seven materials confirms no exceptions or locked controls.
The audit includes an earlier bundle; final changes received targeted rechecks, not a second full audit. One concurrent phone replay collided with its local host and was discarded; the final phone replay ran after host release.

## Left open

Unattended choices follow the Curiosity brief: keep the sodium page, no built-here marks, no lesson narration, no teacher-plan takeover claim. No kit changes or commits. Initial brief-reading shell batches lacked explicit subprocess deadlines; all later commands used the bounded runner.
