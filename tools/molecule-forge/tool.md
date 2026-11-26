# Molecule Forge: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: molecule-forge (Curiosity No. 12)

#### Built

Full-screen molecular model kit and crystal specimen viewer, with the engraved plate, lower-left Manual, and Motion, Sound and Read on the instrument power panel.
Forge has nine atoms, explicit bonding spots, single/double/triple bonds, rings, 3D rotation, relative space-filling spheres, a turntable, 30-edit Undo and a twelve-specimen local shelf.
Crystal has seven generated lattice graphs, growth, an interior cut, an atom-number inspector, and qualitative Push and Current tests. The field guide has all 39 pages, open in any order.
The final offline bundle is **1,110,569 bytes**, about **1.11 MB**, below the 2 MB goal. No commit, deployment or polish round. Shared files and spec.md were read only; the existing spec diff was left intact.
All authoring, sources, scripts, profiles and evidence are inside the two authorized directories. The report was staged in Scratch and copied here last to honor the explicit stop instruction.

#### The real material

- **Molecular graphs:** 32 guide entries and 40 additional names, complete explicit hydrogen/bond arrays from [PubChem PUG REST](https://pubchem.ncbi.nlm.nih.gov/rest/pug/). Public-domain numerical molecular records; fetched 2026-11-05. No sampling. Raw JSON is in `_scratch/molecule-forge/data/`; per-entry URLs are packed in material.json.
- **Coordinates:** 30 supplied 3D computed conformers in the illustrated molecular guide, not measured structures. The fetched hydrogen and silane records only supplied 2D coordinates: H2 uses the specified 74 pm reference model, and SiH4 uses a labelled ideal tetrahedron with an estimated 142 pm Si-H distance. No flat 2D silane masquerades as a 3D conformer. Of the forty additional names, 39 supplied 3D records; allene uses a labelled ideal model with perpendicular terminal planes, derived from the chapter 8 bonding rules.
- **Valence and geometry:** independently written code following OpenStax Chemistry 2e, 7.6 and chapter 8. The [2019 licence page](https://ic.arc.losrios.edu/~paynem/textbook_os_2e/chemistry_2e_intro.pdf) states CC BY 4.0; original chapter 7, 8 and 10 PDFs were preserved. Authors: Flowers, Theopold, Langley and Robinson, Rice University. The current web edition instead lists CC BY-NC-SA, so current prose and illustrations were not copied.
- **Crystal data:** our own finite graph generators using the specified diamond/tetrahedral, honeycomb AB, rock-salt, FCC, BCC and bridged-silica rules. Counts: diamond 525, graphite 600, silicon 525, salt 392, copper 561, sodium 559, silica 147 Si + 220 O. [OpenStax 2019 chapter 10](https://ic.arc.losrios.edu/~paynem/textbook_os_2e/openstax_2e_ch10.pdf), CC BY 4.0, and the named CRC 97th-edition lattice parameters supply factual structure/spacings. No source figures or proprietary tables were reproduced.
- **Radii and colours:** prescribed factual values from Cordero 2008, Bondi 1964, Shannon 1976, CRC and [Jmol CPK](https://jmol.sourceforge.net/jscolors/). Covalent radius estimates carry a `~` label; they are distinguished from lengths in stored conformers. Salt uses ionic sphere radii.
- **Context facts:** retained only checked short facts, in original wording, with linked sources on each guide page. Sources include NASA, USGS, OSHA/NIOSH, ESA, Wöhler's public-domain 1828 text, Royal Institution, Science Museum, PubChem, EPA and FDA. Scientific facts were paraphrased; outside prose, photographs and annotated data tables were not republished. `fact-provenance.json` records each claim, URL, date and disposition. Other anecdotes were replaced by independently computed atom/bond counts.
- **Art:** generated for this build with OpenAI gpt-image. Forty final paintings, no people, with two object-specific redraws. Atomic geometry, crystal patterns, bonds, pegs, protractor, contacts and battery are drawn in code, never painted into a dataset image.

Gathering used bounded requests, stayed below the 45-minute active gathering allowance, and retained raw downloads plus packing scripts. The final tool makes no automatic network requests.

#### Break the instrument

- 85 independent material checks pass: valence, Hill formulas, explicit atom counts, bonds, geometry, coordination, equal nearest-neighbour distances and graph budgets.
- 183 original controller checks and 54 deeper checks pass. All 32 molecules were reconstructed one atom at a time through the editing controller, including ring closures. All 72 records match their names. Both aromatic drawings of benzene, vanillin and aspirin match after their six ring bond orders are actually swapped.
- Water takes two H additions; two more produce a separate H2 without disturbing the water's identity. Forty atoms is enforced; Undo stops after 30 edits. A filled H5N3 invention stays outside the guide.
- Every seed and no-grow category was exercised, plus a triple-carbon seed. The latter is explicitly rejected rather than silently becoming diamond. H/Cl/ion seed contacts do not acquire extra covalent bond orders.
- All seven Push and Current results were exercised. Salt growth uses the actual highest-occupied-neighbour rule; silica reveals bridging oxygens with its silicon shells; graphite begins with its double-bond seed. Views reframe as the actual shells arrive. A tap/key ends growth or a test in the same frame. Salt's cross-cut charge-product sum was independently recomputed: approximately -4.4748 at rest and +3.4267 after one spacing, in the model's relative units. No invented force or current value is displayed.
- Native keyboard input closed a three-carbon ring, then filled it to recognized cyclopropane. The extra formaldehyde card and automatic guide selection of the current Ethanol model passed. The labelled allene model has independently checked perpendicular terminal planes. Focused closeout run: zero browser exceptions.
- Salt fracture updates the actual graph to 90 fully coordinated interior ions, then Current restores the original 150.
- Whole-pixel, timing-jittered real mouse drags attached H to oxygen and placed another H separately in the empty well. Real keyboard input alone built water and grew 392-ion salt.
- Shelf data survives reload; blocked storage continues playing with one readout notice. Extreme zoom, empty well, rapid edits, full shelf logic, atom-number bounds, switching back from a high crystal atom index, and mid-action resize were checked.
- Final native controller/drag run: 54 checks, no browser exceptions and no HTTP/HTTPS requests. A document-targeted synthetic-key guard error found during testing was fixed and the full native test rerun.

#### Voice walk

Knowing-guide is the declared voice; this build uses the kit's browser-speech fallback and synthesized effects, with no audio recordings.
Held clicks at two-second intervals produce the first-run hint once. Further additions and material tests do not automatically narrate. Read speaks the current formula, identity, spots, selected atom/angle and result. Opening a drawer first does not speak an instruction naming its inert tray.
The controlling Curiosity brief's “then only when Read is pressed” wins over the spec's automatic molecule-name and test-result narration. This conflict was stated before building. Sound off and Read were exercised; the audit's repeated and quick-tap voice checks finished cleanly.

#### Short test

Build-side exploration used the unread first encounter and more than ten minutes of manually chosen instrument states, visual inspection and automated interaction sequences. This is an agent assessment through grade-7 and adult lenses, not a study with children.

| Question | Assessment |
|---|---|
| Would a kid open it unassigned? | PASS: the waiting oxygen has visible attachment ports, and two taps immediately change its shape and name. |
| Would an adult play for fun? | PASS: isomers, unfamiliar filled graphs, resonance drawings, caffeine and different lattice coordination invite independent investigations. |
| Is the real thing the interface? | PASS: the atom graph and the generated lattice are the working surface. Pictures are only field-guide context. |
| Does it work without a score or finish? | PASS: nothing unlocks, collects a mark or ends the session. |

Best moment: filling water, then watching another pair of hydrogens become their own specimen. Adult depth: the same carbon becomes a four-connected network or three-connected sheets, and the test responses follow that distinction.
Frame comparison: [Molecule Forge beside Elements Inspector](../../_scratch/molecule-forge/frame-comparison.png). Beat Lab, Elements Inspector, Span and Spire and Pocket Universe were opened and inspected; their sources and family marks informed this build.

#### Lesson creep check

The requested whole-word scan of src.html and the voice lines finds no score, points, level, goal, sticker, badge, correct, wrong, try again, complete or well done. No em dash in the tool source. Capacity and atom readouts are physical budgets, not progress targets.

#### Done when

| Spec item | Result and evidence |
|---|---|
| 1. Unread first two minutes | PASS: native water path and separate H2, saved in final-native.json and frames. |
| 2. All names, isomers, resonance and inventions | PASS: 32 atom-by-atom assemblies, 72 recognitions, three genuinely swapped ring patterns, formaldehyde and unknown H5N3. |
| 3. Orders, angles and formulas | PASS: independent geometry checks, native water angle 103.9799°, single/double/triple changes and canonical Hill order. Guide headings retain conventional formulas. |
| 4. Seven seeds and neighbour counts | PASS: exact budgets and adjacency checks; inside coordination 4, 3, 6, 12, 8 and Si 4. “Inside” is actual full coordination, not the illustrative hard-coded 87. |
| 5. Material tests and interruption | PASS: all fourteen outcomes and same-frame completion checks. Push/Current remain qualitative as disclosed. |
| 6. Open reference guide | PASS: 39 selectable pages; no locked pages, totals or found marks. |
| 7. Well and controls at required sizes | PASS: full size sweep and targeted corrections, including the 375×812 iframe. |
| 8. Performance and keyboard | FAIL for a strict unbroken 60 fps: 4× CPU, 1366×768, median 16.7 ms for both stress cases; graphite p95 33.4 ms, forge p95 16.8 ms. Keyboard water and salt pass. Desktop CDP slowdown is an emulation, not a physical Chromebook certification. |
| 9. Shelf and blocked storage | PASS: reload and blocked-storage tests preserved in runtime.json. |
| 10. No game layer | PASS: source/voice scan and visual inspection. |
| 11. Short test, comparison, runtime, offline | PASS with the assessment limits above; final native run has zero exceptions/HTTP requests and a side-by-side frame. |

#### Audit leads

The single required audit finished with exit 0 and 231 raw leads. It is preserved in Scratch and is **not presented as a zero-lead audit**.
Most leads are intentional: a full-size canvas lies behind its controls and readouts; the first-run hint intentionally disappears; a modal drawer makes the covered bench inert; reference books scroll; the one-time hint is not a per-mode welcome.
Actual fixes: the phone engraving was shortened, fixed H bonds became readouts rather than inert buttons, compact diagrams moved clear of bond readouts, source links gained 44 px targets, guide Turn/Load stay outside the scrolling body, and the mid-height tray uses a 3×3 layout with 44+ px targets.
The audit's resize lead involving a hydrogen bond control is resolved by removing that non-steppable button. Drawer title/Close boxes shared bounding rectangles without text collision; the guide title now reserves space for Close.
The full audit was not rerun. All affected areas received targeted post-fix frames and input tests. The held-click main-control walk, Motion-off check, repeated-click checks and quick-tap checks finished without runtime/focus errors.

#### Frames looked at

All required sizes, both bench positions, storage/keyboard/drag paths, Motion off, grayscale spheres, caffeine, salt cuts, guide and Manual. The 29 audit frames were inspected in four contact sheets. Early failed syntax frames were inspected, fixed and superseded.
Additional final frames confirm the compact well, phone salt and turntable, conventional guide labels, analytic silane, reachable guide actions and corrected art. Every final painting was inspected in the WebP contact sheet and the two replacement originals.

#### Art made

40 final WebP pictures, 557,506 bytes in total, plus the code-drawn working surface. One 5×8 atlas and two corrected-object redraws. Actual tile edges were measured and inset to remove adjacent-picture strips. Raw paintings, crop bounds, source atlas and scripts are preserved.
`art.py --rekey` was attempted but this Python lacks NumPy/Pillow. Native image cropping plus Chrome canvas produced the WebP assets without installing software or changing shared scripts.

#### Engine changes wanted

None. The graph, geometry and lattice code stays local to this tool. The shared kit supplies settings and voice behavior.

#### Left open

- Unattended choices follow the brief: no built-here guide marks; keep the sodium metal page; no automatic names or test narration after the first hint.
- The brief's verification rule superseded unconfirmed contextual anecdotes. Twenty-two molecule pages currently use computed structural descriptions; the full 39-page illustrated guide and all molecular graphs remain present. The exact FDA coffee range was not retained without a second independent check, although caffeine's coffee/tea context remains.
- PubChem supplied no 3D records for H2 or silane in this gathering. Their explicitly labelled analytic/reference models, and allene’s perpendicular-plane model, are intentional fallbacks. Stored conformers are computed, not advertised as measured.
- Finite specimens expose their actual graph boundaries. Graphite's 150-atom sheet crop admits a matching on all 600 atoms, and diamond has 363 fully coordinated atoms; these actual counts replace unverified illustrative interior/matching counts in the old prose.
- This build does not supply a teacher plan or establish the anchor lesson-card takeover. It is the requested Curiosity instrument.
- The strict 600-atom frame-budget target remains open: median cadence is about 60 fps, with occasional 33.4 ms frames at 4× slowdown. Several bounded optimizations were made; the brief’s single-issue time limit ends further optimization in this build. Hardware performance still merits a physical school Chromebook run. Browser narration uses available system voices rather than a newly recorded knowing-guide clip bank.

All Chrome and host processes started for this build were closed. No tools/molecule-forge/host.html was created. Evidence, source records and replay scripts remain in `_scratch/molecule-forge/`.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: molecule-forge

#### Played

Cold grade-7/adult walkthrough preceded reading the builder report, handoff, notes or source. Oxygen to water, separate H2, methane/shelf, Sticks/Spheres, drag/keys, diamond/salt tests, cut and unrestricted guide/Manual.
More than ten minutes of exploratory states and real held input; an agent assessment, not a child usability study. Strong tactile kit, immediate chemistry, no game layer.

#### Findings fixed

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

#### Findings left

Should fix, general: strict unbroken 60 fps was not met. At desktop 4x slowdown, 600-atom cadence median 16.7 ms, p95 33.3 ms (9 missed frames/149 intervals); 40-atom p95 16.8 ms (4 misses). Profile-guided cached geometry, baked sprites and simpler crystal paths improved median delivery from 19.2 to 16.8 ms. No physical Chromebook was tested. Bounded optimization did not eliminate missed frames; this remains an explicit FAIL of the strict cadence item.

#### Break it

No score, goal, level, quiz, completion gate or collectible book exists. Atom counts and open spots describe the actual selected graph.
Independent controller reconstruction and identity checks: 287 checks, zero failures; all 32 hand-built molecules, 72 recognized graphs, aromatic alternatives and unknown H5N3.
Independent numerical pass: 478 checks, zero failures; explicit valence/formula arrays, finite coordinates, crystal budgets/equal bond distances, inside coordination and 1-mm salt estimate.
40-atom cap, 30-step Undo, empty well, every atom, zoom 50/300 percent, triple-carbon rejection, all seven Push/Current outcomes and resize mid-action: no exceptions or locked controls.
Targeted checks confirm seed text/focus, salt Undo, completed calm/saved water geometry, separate specimens, native crystal drag and unchanged finished geometry while another component is edited. Shelf limit/reload and blocked storage also pass.

#### Voice walk

Held taps, 2-second pace: H, H, Read, Crystal, Na, Cl, Grow, Push, Current, Read, Sound off, Read.
Heard: first-run hint once; water readout; salt/no-current readout; the same Read with Sound off. No automatic names or result narration.
Curiosity brief's "then only when Read is pressed" takes precedence over the spec's automatic names/test lines. No per-mode lesson narration added.
Hint expected/spoken 1/1; requested Read expected/spoken 3/3. Browser speech fallback, no recorded knowing-guide clips. Runtime allLines matches voice/lines.json.

#### Facts checked

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

#### Sensitivity

An isolated stomach illustration is neutral anatomy; no treatment, chemical-handling instructions, cultural generalizations or people pictures. Reviewers can check that context, alongside the source-rights distinctions.

#### Flattest moment left

Invalid seed combinations still answer mostly in a short result line. The crystal inspection, formerly the flattest moment, now exposes the actual coordination without adding a game.

#### Short test

- Kid opens it unassigned: PASS, two taps change the waiting oxygen into water; another pair makes a separate specimen.
- Adult plays for fun: PASS, isomers, rings, unfamiliar filled graphs and seven lattice patterns support independent questions.
- Real material is the interface: PASS, the editable graph, computed coordinates and generated lattice are the working surface; qualitative tests are labelled as such.
- Works without score/finish: PASS, every guide page is open and no action unlocks or ends anything.
Fresh comparison: [Molecule Forge beside Elements Inspector](../../_scratch/molecule-forge/review-frames/review-frame-comparison.png).

#### Graphics

All forty existing paintings, 39 audit frames and the review frames inspected in contact sheets and individual views, with all required dimensions opened individually. Coherent material style, no placeholders or people. Kept all art; changed the working crystal rendering, not the paintings. Bundle 1,145,511 bytes (about 1.14 MB), including all forty paintings; the 2 MB goal is met.

#### Audit

The single final audit completed with exit 0 inside its 40-minute limit: [audit.md](../../_scratch/molecule-forge/review-audit/audit.md), 229 raw leads. The small source-link targets were confirmed and fixed, then measured at 680 and 1366: 54 Manual links and two guide links meet 44 by 44 pixels.
Other leads are intentional canvas/control overlap, a dismissed first-run hint, inert bench regions behind modal drawers, scrolling reference citations, or padded title rectangles without glyph collision. Three resized-atom leads compared labels changed by the accessibility fix; final native resize of all seven materials confirms no exceptions or locked controls.
The audit includes an earlier bundle; final changes received targeted rechecks, not a second full audit. One concurrent phone replay collided with its local host and was discarded; the final phone replay ran after host release.

#### Left open

Unattended choices follow the Curiosity brief: keep the sodium page, no built-here marks, no lesson narration, no teacher-plan takeover claim. No kit changes or commits. Initial brief-reading shell batches lacked explicit subprocess deadlines; all later commands used the bounded runner.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 2 (general 0, family 2), should fix 17 (general 8, family 9), polish accepted 16

### Refine: molecule-forge

Merged from refine/teaching.md, refine/play.md, refine/craft.md (no sensitivity.md; all three lenses found nothing
cultural, Native or hard history). Judged as a Curiosity (No. 12) against docs/agents/CODEX-CURIOSITY.md and BASELINE.
Frame roots: Teaching `S:/CurioClass-codex-scratch/molecule-forge/teaching/frames/`, Play
`S:/CurioClass-codex-scratch/molecule-forge/play/` (f1 to f4), Craft `S:/CurioClass-codex-scratch/molecule-forge/craft/`,
shared audit `S:/CurioClass-codex-scratch/molecule-forge/audit-r1/`.
Integrator spot-checks: src.html:376-380 and 726 (bond label), 574-582 (no-grow lines), 497-501 (crystal seed add),
1218-1222 (hint), 688 (Spheres aria-pressed), and the `fact` field of material.json (22 of 32 start "In this model").
All confirmed as the lenses describe.

#### Blocker
1. **Bond labels state lengths the model on screen contradicts.** src.html:726 (bond button text) and `length()` at
   src.html:376; Forge, any matched molecule. The visible label is always the radius-sum estimate with a bare "~", even
   after the molecule has glided to its stored PubChem conformer. H2 reads "H single · ~62 pm" while the drawn model is
   74 pm (and the Manual says 74). Benzene, vanillin and aspirin ring bonds read "single ~152" and "double ~132" while
   every ring bond in the model is 139 pm, so the readout teaches the alternating-length misconception the real
   structure disproves. Others more than 5 percent off: O2 115 vs 123, H2O2 O-O 132 vs 145, formic acid C-O 142 vs 135,
   urea and caffeine C-N 147 vs 137 to 139 (14 bond types over 5 percent in Teaching's `dev` measurement, shots2.json).
   Seen: teaching/frames/h2-label.png. Only the aria-label says "radius estimate". A meter that misleads when its
   assumption fails is a blocker (REFINE.md). Fixed looks like: once a structure matches, every bond label shows the
   stored model's distance ("139 pm, model"); while building (no match), the label says "estimate" on screen, not just
   "~", and the aria-label matches. For aromatic rings the order button may still step (it is how the student draws
   either Kekule pattern), but the length shown is the model's equal 139 pm; add one Manual line that benzene's ring
   bonds are all the same length, which is why both drawings name the same molecule. (family:curiosity)
2. **Silicon seeds are told they close into a molecule when the real substance is a giant network.** src.html:579-581,
   Crystal, `noGrow()`. Si + C gets "This closes into a molecule. Grow carbon alone, or two carbons." (play/f2/c11);
   silicon carbide is a real diamond-pattern covalent network, so the line is false. The last fallback ("Two of these
   close up into a small molecule") is equally untrue for other silicon pairs such as Si + N (silicon nitride is also a
   network). Weighed under the misleading-readout rule: the message's assumption (anything that is not one of the seven
   seeds closes into a molecule) fails here and the readout states a falsehood about a real material, so it is a
   blocker. Fixed looks like: any seed this forge does not grow gets an honest line that does not claim what it would
   make in nature when that claim is wrong, e.g. for Si + C "Silicon carbide is a real giant network, like diamond, but
   this forge does not grow it. Try carbon or silicon alone." Keep the C + O line (CO2 really is a molecule). Do not add
   silicon carbide as a crystal (that is a spec change, see open questions). (family:curiosity)

#### Should fix
1. **The closing moment is flat (visual part).** src.html:453-465 `edited()`; Forge. The spec's first-two-minutes
   payoff is a thin cyan ring pulsing out from the molecule and the Field guide tab lighting with the name ("Water").
   The build plays a tone and glides; the only visible change is the strip name, and the Field guide button never
   changes. Seen: play/f1/p02, audit state-water-1366x768.png. Fixed: a single cyan (#5fd4ff) ring pulse on first close
   of each molecule this visit (Motion off: a brief static ring, no animation), and the Field guide tab shows the name
   for a few seconds (and opens on that page if tapped then). The spoken name is deferred (see Settled calls). (family:curiosity)
2. **The first-run hint hides on the wrong tap and is spoken after the student already acted (merged Play SF2, Craft
   F3, Play nit 2).** src.html:1218-1222. Any click anywhere hides the hint and queues the voice line: tapping the red
   oxygen in the well adds nothing but removes the only instruction (play/f4/h01); so does Motion (f4/h02). When the
   first tap does add an H, the voice then says "Tap an atom to snap it on." after it has already snapped on
   (craft/v-firstH.png, craft/voice1.py first_H log, audit one-click rows 1 to 9). The keyboard path (T, 2, G) never
   hides it, leaving the Forge hint over a grown diamond (play/f4/h03). Fixed: hide the hint when the first atom is
   actually added (tap, drag or key, either mode); skip the spoken hint (unmarked, so it can still play later) when the
   first action added an atom, and speak it once only when the first action was something else; word it "Tap an atom
   in the tray to snap it on." (the oxygen is an atom too), updating voice/lines.json and `allLines()` to match.
   (general; Craft tagged it family:curiosity)
3. **22 of 32 molecule pages and all 7 crystal pages show placeholder facts.** material.json `fact`; crystal pages
   built at src.html:1076 (`fact:c.pattern`). Oxygen, Nitrogen, Ammonia, Methane, CO2, Acetone, Propane, Butane,
   Vanillin, Aspirin and 12 more read "In this model: 2 O. 1 double bond."; crystals say only "Every inside atom touches
   4 neighbours." The spec lists a real fact for each page and says they are kept unchanged; the Manual's "Field guide
   facts" repeats the placeholders. Seen: teaching/frames/guide-oxygen.png, guide-diamond.png. Fixed: restore the
   spec's facts (spec.md "Real material and sources") with each page's named source, checked against a second source;
   drop only a fact that truly fails a second source, and say so in notes.md. Crystal pages get both the pattern line
   and the spec's use fact (Mohs 10, pencil lead, chips, quartz and sand, most wire, cut with a knife). (family:curiosity)
4. **A lone atom and its molecule carry the same name.** src.html:709. The opening oxygen reads "Oxygen", identical to
   the O2 page "Oxygen · O2"; a lone H reads "Hydrogen", and so does H2. Atom versus molecule is the anchor idea
   (MS-PS1-1). Seen: teaching/frames/guide-oxygen.png; checks.json `loneH`, `h2`. Fixed: "oxygen atom" / "hydrogen atom"
   for a single atom; the guide name only for a matched molecule. (family:curiosity)
5. **O=Si=O settles bent at about 165 degrees against the groups rule it teaches.** relax() src.html:748; Forge,
   Things to do 7. CO2 glides to 180 (matched) but O=Si=O stops at 165 (Motion on) or 153 (Motion off), and the
   readout says "about 165°" for a shape the Manual calls straight. Any unmatched two-group centre does the same.
   Seen: Teaching `osio-motion` shot, checks.json `osio`. Fixed: relaxation reaches the ideal angle for two-group
   centres (or snaps to it when settled); the same check for 120 and 109.5 targets. (family:curiosity)
6. **The outer-electron link (HS-PS1-1) is claimed but never shown.** Atom table src.html:287 (`ve` defined, never
   displayed). Nothing on screen connects spots to outer electrons. Fixed (inside the spec, which carries valence
   electrons in its atom table): one more part in the selected-atom readout, e.g. "O · 6 outer electrons · 2 spots ·
   2 filled · 2 lone pairs", and the same count in the tray ball's label. Dropping HS-PS1-1 instead would be a spec
   change. (general)
7. **The Manual reads at about grade 14.** src.html:238-276. "element-labelled connections", "computed PubChem
   conformer", "The extra recognized allene record also supplied only a 2D diagram ... two perpendicular pi bonds",
   "cristobalite-like network", "appreciable current", "not an atomic slip solver". Fixed: plain sentences for a grade 6
   to 10 reader ("Hydrogen and silane use a textbook shape instead of a PubChem one"), keeping every honesty point;
   build detail moves to notes.md. (general)
8. **"Things people have found" has 4 of the spec's 9 entries (Teaching polish 7, Play SF8).** src.html:272-273.
   Missing: lone pairs squeeze the angle (109.5, 107, 104.5); 78 °C against -24.8 °C; 92 legal C/N/O structures, 56
   unnamed; the pencil; salt cracks while copper bends; CO2 small but SiO2 giant; silicon a semiconductor; Wöhler 1828.
   Fixed: restore all nine as short separate entries, each with its source as in the spec. (family:curiosity)
9. **A stray tray tap in Crystal silently wipes the grown crystal.** src.html:499-501. With a one-atom seed, any tray
   tap adds to the seed and sets `crystal=null`; after diamond, one tap on H leaves "C · H, Seed plate" and an empty
   bench (play/f2/c15). Undo is hidden in Crystal (src.html:687), so only Ctrl+Z restores it, and Grow then refuses.
   Fixed: show Undo in Crystal too, and keep the grown specimen on the bench until the seed actually changes into a
   new growable seed or Clear seed is pressed. (general)
10. **Push outcomes look alike, so the comparison does not land.** src.html:878-883. Copper "bends" and graphite
    "slides" both draw as the top half shifted sideways (play/f2/c07, c08); diamond's push goes out and back
    (`65*sin`), so its end state looks untouched while the strip says "64 bonds cross this cut and none let go"
    (f2/c05). Fixed: distinct end shapes for crack (gap), bend (rows roll and the block stays whole and bowed), slide
    (sheets offset cleanly) and hold (nothing moves), and the bonds crossing the cut highlighted at the end so the
    student can count the bonds that hold (Things to do 9). A tap mid-test still shows the end state the same frame.
    (family:curiosity)
11. **Copper and sodium metal drop to 35 fps at 4x slowdown while turning.** draw() src.html:835-982, Crystal. Copper
    (561 atoms, 2,820 bonds) 34.5 fps, sodium (559, 1,728 bonds) 35 fps with Show on or dragging; graphite (600) passes.
    Done when 8 fails. Seen: craft/perf3.py. Fixed: 60 fps at 4x for both (e.g. batch bond strokes by colour, skip
    hidden back bonds, or cache the bond list per frame). (family:curiosity)
12. **At the 680x425 preview the model is a tiny dot in a corner (Play SF9, Craft F5).** src.html:866-872 (`cx=w*.78`
    when short) and the max-height:690px layout. The lone oxygen is about 35 px across, water about 70, caffeine about
    130 px pushed into the right corner with the hint over its lower edge; the tool page's first impression is a box
    and text. Seen: audit size-680x425.png, state-water-680x425.png, state-water-800x500.png, play/f2/n05. Fixed: in
    short windows frame the model larger and nearer the well's centre of the free area, and keep the hint clear of it.
    (general)
13. **Read leaves out the hint and is not shaped for speech (Play SF10, Craft F6).** readText() src.html:745-747. On
    the first screen Read speaks the readout but not the hint, so a non-reader never hears what to do (CODEX-CURIOSITY:
    the hint is spoken once, then when Read is pressed). The text is screen glyphs: "C₈H₁₀N₄O₂", middle dots, "°", a
    doubled period ("Straight model.. Si"), capitals. The angle is only read with exactly two neighbours. Seen:
    craft/voice1.py, play/f3/d04, audit row 12. Fixed: build a spoken string ("C 8, H 10, N 4, O 2. Caffeine. All spots
    full. Selected: oxygen, 2 bonds, about 104 degrees."), include the hint while it is showing, and include the
    angle whenever the selected atom has one. (general)
14. **Spheres / Sticks button reports the wrong state to a screen reader.** src.html:688. The label flips to the other
    mode and aria-pressed flips too, so with spheres showing it announces "Sticks, toggle button, pressed". Fixed: one
    fixed label "Spheres" with aria-pressed, or (with Polish 8, a real two-position switch) a switch that
    announces its current position. (general)
15. **Na plus Cl in Forge contradicts itself.** src.html:709. The strip reads "ClNa · NOT IN THIS GUIDE" while the
    result line says "Na⁺ Cl⁻ · an ion pair. Grow salt in Crystal." and the guide has a Salt page (play/f3/d03). Fixed:
    the strip name reads "Ion pair" (or "salt, as one ion pair"), never NOT IN THIS GUIDE for this special card.
    (family:curiosity)
16. **Other no-grow messages do not match the seed (Play SF7, Craft polish 11).** src.html:574-582. Na + Na gets "These
    do not build a crystal in this forge. Try one atom of each alone." though Na alone grows sodium metal (play/f2/c10);
    a single H, O, N, S or Cl gets "Two of these close up into a small molecule" with one atom on the plate (f2/c12).
    Fixed: each line names what to try for that seed (Na + Na: "Sodium metal grows from one sodium atom."; one H, O,
    N, S or Cl: "Hydrogen pairs into a small molecule. Nothing to grow." with the element named). Blocker 2 covers the
    silicon lines. (family:curiosity)
17. **Words do not match the state: plurals and case.** src.html:670, 685, 706, 1047, selectedInfo. "1 SPOTS OPEN"
    (play/f1/p01, craft/v-firstH.png), "1 lone pairs" (f1/p06), tray labels "Hydrogen · 1 spots", "Sodium · 0 spots",
    "Bench switch: forge", "Na · sodium" lower case beside capitalised atoms, also-known names lower case in the strip
    ("formaldehyde", f3/d06). Fixed: singular for 1, and the capitalisation used everywhere else. (general)

#### Polish accepted
1. **Drags show the snap.** src.html:1000-1010, 1053-1064. Dragging a tray ball or model atom draws nothing until
   release (play/f3/d01, d02). Draw a ball following the pointer, light the target peg, and stretch the would-be bond.
2. **A second structure does not shrink the first.** A stray atom is parked 300+ pm away and the view reframes, so
   water drops from about 110 px to 55 px (play/f1/p02 vs p03, p04). Park new structures closer or frame the one in
   focus.
3. **NOT IN THIS GUIDE only once a structure is closed.** After the first tap the strip reads "HO · NOT IN THIS GUIDE"
   (play/f1/p01), which sounds like "wrong" mid-build. Leave the name blank while spots are open; keep NOT IN THIS
   GUIDE for closed inventions (f1/p10, Done when 2).
4. **Current reads at projector distance.** The battery's left wire runs through the specimen and flow, a little and
   none look alike (play/f2/c06). Wires stop at the faces; a brighter carrier stream for flow, a sparse one for a
   little, none for none.
5. **The empty seed plate says what to do.** play/f2/c01: a bare ellipse, Grow disabled. Engrave "TAP AN ATOM, THEN
   GROW" on the stand (a first-run style line on the instrument, gone once a seed is on it).
6. **The inspected crystal atom is visible after Grow.** Atom 1's cyan ring is lost among 525 balls (play/f2/c03,
   audit state-salt-1366x768.png). Start inspection on an atom near the viewer.
7. **Manual find on isomers by tap order.** C, O, C taps always make ethanol (play/f1/p08); O, C, H, H, H, C makes
   dimethyl ether. Add a short find: "The order you tap decides which isomer you get."
8. **Instrument controls.** src.html:17-22, 199, 209-217. The bench switch, Sticks / Spheres, Show and Cut open are flat
   web buttons. A two-position slide switch for Forge / Crystal and Sticks / Spheres, and lit keys for Show and Cut
   open, keyboard operable and announcing their value (CODEX-CURIOSITY "Real controls"; spec "slide the bench switch").
9. **Sound per outcome.** src.html:592, 623, 633. Push plays one sound for five outcomes; Current one blip. Use the
   spec's palette: crack, bend ring, hold clink, slide swish, current hum or one spark (tones, not voice).
10. **Tab order: bench controls before model atoms.** src.html:203. 18 Tabs from Hydrogen to Undo with 3 atoms, about
    55 with 40 (craft/kb.py). Move `#atomkeys` after the controls in the DOM / tab order.
11. **Field guide at short heights.** src.html:97, 104. At 680x425 the page is all picture; name, fact and sources are
    below an unmarked scroll (audit state-guide-680x425.png, state-guide-1366x768.png). Cap the picture height in short
    windows or put name and fact above it.
12. **Test line in plain words.** src.html:630. "No current. No mobile carriers in this model." becomes "No current.
    Nothing here can move to carry charge."
13. **Crystal counts name what they count.** Salt reads "392 ATOMS" (they are ions); silica "83 INSIDE" counts only
    Si though inside O atoms are inside too (checks.json `crys`). "392 IONS"; count every inside atom.
14. **Live region writes only on change.** src.html:205, 711, 889. The polite `#readout` is rewritten every frame
    during Grow and every sync.
15. **Canvas font fallback.** src.html:962, 966. `'11px Consolas'` and `'15px Consolas'` gain `, monospace`
    (Chromebooks have no Consolas).
16. **OpenStax links go to openstax.org.** The Manual's OpenStax links point at a personal college mirror
    (ic.arc.losrios.edu/~paynem). Link the openstax.org book sections instead and state the licence shown there.

#### Settled calls
- **Spoken lines deferred (BASELINE 18).** The spec's molecule name on first close ("Water.") and the Push / Current
  result lines are not fix items this round; Curiosity voice is one collective Forge effort. Note for that pass: queue
  the name from `edited()` (src.html:453-465) on the first close of each molecule this visit, and the result line from
  `push()` / `current()` (src.html:610-634); both are event lines. Codex does not record or add them now. The visual
  close (Should fix 1) is in scope. The existing hint line's timing (Should fix 2) and Read (Should fix 13) are fixes
  to behaviour already built, so they are in scope.
- **Silicon carbide: blocker, not should fix.** Play asked Teaching to weigh it; Teaching did not see it. Settled under
  the misleading-readout rule (REFINE.md): a no-grow line that states a false fact about a real material is a blocker.
  The fix is honest wording, not a new crystal.
- **Manual finds: should fix, not polish.** Teaching called it polish, Play should fix. A month of depth is one of the
  Curiosity qualities and the spec lists all nine; settled as should fix.
- **Plurals: should fix, not nit.** Teaching and Craft called them nits, Play should fix. "1 SPOTS OPEN" is on screen
  after the very first tap; words must match the state.
- **First-run hint tag.** Play tagged it general, Craft family:curiosity; kept as general (any tool's hint can do this).
- **Illustration credit stays.** Craft asked whether the Manual's "Illustrations generated with OpenAI gpt-image"
  credit breaks BASELINE 15. It is the source credit CODEX-BUILD.md:128-129 requires, not marketing copy; keep it.
- **Do not change:** the no-score, no-goal, no-"found" field guide (all lenses passed it); the full-screen well (all
  audit "overlap #stage" rows are noise); modal drawers making the bench inert; Hill order on the strip (see open
  questions); the Na+ Cl- ion pair, O=Si=O, O3 ring and Cu-Cu special cards and their honesty lines.

#### To the spec's open questions
- **Hill order against familiar formulas.** The strip shows H3N, ClH, ClNa, O2Si while guide pages say NH3, HCl, NaCl,
  SiO2 (checks.json `nh3`, `nacl`; play/f3/d05). The spec and Done when 3 fix Hill order; showing the conventional
  formula when the guide knows the molecule would change the spec. Lean: conventional formula on the strip for known
  molecules, Hill for inventions, with the Manual's Hill note kept.
- **Silicon carbide as an eighth crystal (Si + C seed, diamond pattern)?** Would add a page and a growth rule. Lean: no
  for now; the honest no-grow line (Blocker 2) is enough.

#### Not taken
- match() stall of about 100 ms at 40 atoms under 4x slowdown (Craft nit 14): a rare edit, fix not clearly cheap.
- Top of a grown crystal under the bench buttons at 760x900 (Craft nit 16): minor; re-look after the framing fix in
  Should fix 12.
- Hint wraps to a lone "on." at 375 (Play nit 3): the new wording in Should fix 2 changes the line; re-look then.
- prompts.json stub descriptions (Craft nit 17): not student-facing.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: molecule-forge (Curiosity No. 12), round 1

Cold Craft lens, 2026-11-06. Judged against CODEX-CURIOSITY.md, VISION "Curiosities: the second shape", STANDARDS
and BASELINE. Bundle looked at: `tools/molecule-forge/molecule-forge.html` (1,145,511 bytes). My scripts, frames and
Chrome profile: `S:/CurioClass-codex-scratch/molecule-forge/craft/` (perf.py, perf3.py, voice1.py, kb.py, kb2.py,
cut2.py). Shared audit: `S:/CurioClass-codex-scratch/molecule-forge/audit-r1/`.

#### What passed (checked, not findings)

- Contract: one file, 1.15 MB (under the 2 MB goal). Network log over a full session (forge, all crystals, grow, push,
  guide): one request, the file itself; the 40 pictures are inline. No console errors or exceptions in any of my runs
  or the audit's.
- Look rules: the well fills the screen at every size; no header, card, pills, score, goal, level or finish anywhere;
  field guide is a plain index with no counts or "found" marks. Maker's plate reads
  `Curio Class Curiosities · No. 12 · Molecule Forge` beside `Manual`, lower-left, at every size including 375.
  Motion, Sound and Read sit on their own power panel. Readouts are monospace with units (pm, degrees, atoms).
- Lesson creep search (score, points, level, goal, sticker, badge, correct, wrong, try again, complete, well done)
  over src.html, material.json, crystals.json: no hits.
- Keyboard: Tab reaches the tray, Enter on Hydrogen twice builds water (H2O, Water); T, 8, 6, G grows salt (392 ATOMS ·
  150 INSIDE); X cuts, P pushes; B opens the guide with focus on Close, Escape closes it and returns focus. Drawers trap
  Tab. Focus ring visible on tray and atom-focus buttons (`craft/kb-atomfocus.png`).
- Motion off: pegs stop wobbling but stay as pegs (not colour only), Show stands still and the 30-degree turn buttons
  remain; audit "Motion off: clean".
- Cut open works (`craft/salt-cut-compare.png`: 178 of 392 front atoms removed around the inspected ion).
- Art: 40 `art:` tokens (mf-0 to mf-39), 40 prompts.json entries, all `people: false`; contact sheet
  (`craft/art-sheet.png`) shows no people, faces or hands.
- Words: no em dashes in src.html, notes.md, lines.json, tool.draft.json or the JSON data; "Curio Class" never alone;
  classroom-safe; privacy stated ("Shelf stays on this device" in the footer, "Never leaves this device" on the shelf).
- 60 fps at 4x CPU slowdown (rAF frame intervals, Motion on, 1366x768): idle, 40 atoms relaxing, 40 atoms on Show,
  graphite 600 atoms, diamond 525, salt 392, silica 367, grow and push animations all hold about 60 fps. Two do not:
  see finding 1.

#### Findings

1. **Copper and sodium metal drop to 35 fps at 4x slowdown while turning.** Where: `draw()`, src.html:835-982,
   Crystal mode. What: with Show on (or dragging), copper (561 atoms, 2,820 bonds) runs 34.5 fps, median frame 33.3 ms;
   sodium metal (559 atoms, 1,728 bonds) 35 fps. Both are 60 fps at 1x and 2x. Spec Done when 8 asks 600 crystal atoms
   at 60 fps at 4x; graphite (600) passes, the two metals do not. How: `craft/perf3.py`, rAF intervals over 4 s at
   CPU throttle 1, 2 and 4. Level: **should fix**. Tag: family:curiosity.

2. **The spec's spoken lines are missing: no molecule name on first close and no Crystal test result.** Where:
   src.html:328-329 (`L` holds only the hint), 453-465 (`edited()`), 610-634 (`push()`, `current()`). What: spec Voice says
   "only a molecule's name when it first closes this visit ('Water.') and a Crystal test's result line". Neither is ever
   queued; the only line is the first-run hint. So the moment the spec builds the first two minutes around (water bends
   and names itself) is silent, and a non-reader never hears what Push or Current found. How: `craft/voice1.py`, five
   held H taps 2.5 s apart (water then H2 close): log holds only the hint; Push, Current, Push, Current, Push on salt:
   log empty. Level: **should fix**. Tag: family:curiosity.

3. **The first-run hint is spoken after the student has already done it.** Where: src.html:1217-1222. What: the hint
   is queued on the first click anywhere, including a tap on a tray atom. A first tap on Hydrogen snaps H onto oxygen,
   hides the on-screen hint, then the voice says "Tap an atom to snap it on." The line no longer matches the screen
   (STANDARDS, Voice behavior). It should be skipped (unmarked) when the first tap added an atom, and spoken only when
   the first action was something else (a drag on the stage, Motion). How: `craft/voice1.py` first_H (log: spoken,
   2 atoms, hint hidden; frame `craft/v-firstH.png`), audit "One held click" rows 1 to 9 show the same. Level:
   **should fix**. Tag: family:curiosity.

4. **Spheres / Sticks button reports the wrong state to a screen reader.** Where: src.html:688. What: the button's
   label flips to the other mode ("Spheres" then "Sticks") while `aria-pressed` also flips, so with spheres showing a
   screen reader hears "Sticks, toggle button, pressed": Sticks is not on. Either keep one fixed label ("Spheres") with
   aria-pressed, or keep the flipping label and drop aria-pressed. How: code read, confirmed by the sync() logic and
   the 1366 frames (label "Sticks" while spheres show). Level: **should fix**. Tag: general.

5. **At the 680x425 preview the model is a 35 px dot in a corner.** Where: src.html:866-872 (short-window framing,
   `cx = w*.78`) and the max-height:690px layout. What: tray, title and selection text fill the left two thirds of the
   well, and the oxygen with its pegs is drawn about 35 px across at the lower right; water is about 70 px. The well is
   the largest thing (Done when 7 passes on the letter), but the subject is not: the site's tool-page preview shows a
   wooden box and some text. 800x500 is only a little better. How: audit `size-680x425.png`,
   `state-water-680x425.png`, `state-water-800x500.png`. Level: **should fix**. Tag: general.

6. **Read never says what to do, and what it says is not shaped for speech.** Where: src.html:745-747 (`readText`).
   What: (a) on the first screen, while the hint is showing, Read speaks "O. Oxygen. 2 SPOTS OPEN. O · Oxygen 2 spots ·
   0 filled · 2 lone pairs." and leaves out the hint, so a student who cannot read never hears "Tap an atom"
   (CODEX-CURIOSITY: the hint is spoken once, then when Read is pressed). (b) the text is the screen's glyphs: Unicode
   subscripts ("C₈H₁₀N₄O₂"), middle dots, "°", a doubled period ("Straight model.. Si"), "O · O · O · O", newlines. A
   speech engine may read subscripts as "subscript eight" or skip them. Build a spoken string instead ("C 8 H 10 N 4
   O 2, caffeine, all spots full. Selected: oxygen, 2 bonds, about 104 degrees."). How: `craft/voice1.py` reads (water,
   caffeine, pushed silica) and read_soundoff; audit row 12. Level: **should fix**. Tag: general.

7. **The controls are web buttons, not instrument controls.** Where: src.html:17-22, 199, 209-217. What: the look asks
   for toggle switches, faders, lit pads; the spec says "slide the bench switch to Crystal". The bench switch is a
   button showing the current mode with a small grey square; Spheres, Show and Cut open are the same flat buttons as
   Undo and Save. A real two-position slide switch for Forge / Crystal and for Sticks / Spheres, and a lit key for Show
   and Cut, would read as a modelling bench. How: every frame, e.g. audit `size-1366x768.png`. Level: **polish**.
   Tag: family:curiosity.

8. **Sound is thinner than the spec's palette.** Where: src.html:592, 623, 633. What: spec lists crack, bend ring,
   hold clink, slide swish, current hum or one spark. Push plays one sawtooth for salt and the same 360 Hz sine for
   copper, graphite, diamond, silicon and silica; Current is one 120 Hz or 900 Hz blip. Better: one distinct sound per
   outcome so the result is heard as well as read. How: code read. Level: **polish**. Tag: family:curiosity.

9. **Tab order puts every model atom before the bench controls.** Where: src.html:203 (`#atomkeys` inside the well,
   before `#controls`). What: from Hydrogen it took 18 Tab presses to reach Undo with 3 atoms in the well; with 40 atoms
   it is about 55. STANDARDS: panel controls before long lists of map items. How: `craft/kb.py`. Level: **polish**.
   Tag: general.

10. **Field guide at short heights shows only the picture.** Where: src.html:97, 104 (`.guide-body`, 4:3 image at full
   width). What: at 680x425 the guide body is all painting; the page name, fact and its sources (USGS, NASA links) are
   below a scroll with no sign there is more. At 1366x768 the source links are also just below the fold. Put name and
   fact above the picture, or cap the picture height in short windows. How: audit `state-guide-680x425.png`,
   `state-guide-1366x768.png`. Level: **polish**. Tag: general.

11. **No-grow message says "Two of these" for one atom.** Where: src.html:581. What: a single H, O, N, S or Cl on the
   seed plate gives "Two of these close up into a small molecule. Nothing left to grow." Words do not match the plate.
   How: code read (`crystalRule` returns nothing for one H; falls through to the last line). Level: **polish**.
   Tag: general.

12. **Singular/plural and case slips.** Where: src.html:670 ("1 spots"), 706 ("1 SPOTS OPEN"), 1047 (tray labels
   "Hydrogen · 1 spots", "Sodium · 0 spots"), 685 ("Bench switch: forge" lower case). How: `craft/v-firstH.png`
   (readout "1 SPOTS OPEN"), kb.py focus labels. Level: **nit**. Tag: general.

13. **The live region churns during growth.** Where: src.html:205 (`#readout aria-live="polite"`), 889 (counts rewritten
   every frame while growing) and 711 (every sync rewrites all four fields even when unchanged). A screen reader may
   re-announce the strip many times per Grow. Write only on change. How: code read. Level: **nit**. Tag: general.

14. **A tap at 40 atoms stalls about 100 ms at 4x.** Where: `match()`, src.html:417-426 (isomorphism tried against all
   72 entries on every edit). One melt plus add at 40 atoms took 101.5 ms at 4x slowdown. How: `craft/perf2.py`.
   Level: **nit**. Tag: family:curiosity.

15. **Canvas text names Consolas only.** Where: src.html:962, 966 (`'11px Consolas'`, `'15px Consolas'`). Chromebooks
   have no Consolas, so "SEED PLATE" and the battery's "+ −" fall back to the default sans. Add `, monospace`. Level:
   **nit**. Tag: general.

16. **At 760x900 the top of a grown crystal draws under the bench buttons.** How: audit
   `state-salt-fracture-760x900.png` (the upper half's corner sits behind "Crystal" / "Field guide"). Level: **nit**.
   Tag: general.

17. **For the integrator, not judged here:** the Manual's OpenStax links go to a personal college mirror
   (ic.arc.losrios.edu/~paynem) instead of openstax.org, and its note that the current OpenStax site lists CC BY-NC-SA
   should be checked (Teaching lens territory). The illustrations credit names a company and links openai.com
   (src.html:1241); BASELINE rule 15 says public copy names no companies, so decide whether a credit line counts.
   prompts.json entries are stubs ("Hydrogen: sun, real object or place") that do not record what was drawn. Level:
   **nit**. Tag: general.

Nothing cultural, Native or hard-history here; no sensitivity review needed from this lens.

#### Standard voice check

Sound on, Motion on, held clicks (0.12 s), 1366x768, fresh page per run (`craft/voice1.py`).

| line | kind | expected | spoken |
|---|---|---|---|
| "Tap an atom to snap it on." | how | once, and only while it still fits | once in five taps; but after an atom tap it plays when the atom has already snapped on (finding 3) |
| molecule name on first close ("Water.", "Hydrogen.") | event (spec) | once per molecule per visit | 0 of 2 (finding 2) |
| Push result, salt, x3 | event (spec) | 3 | 0 |
| Current result, salt, x2 | event (spec) | 2 | 0 |
| bond step x5 (C-C) | none | 0 | 0 |
| Read, Sound off | read | speaks the readout | spoke it (finding 6 on content) |

First-tap timing: stage tap gives the hint; tray atom tap gives the hint late and stale; key "1" first gives nothing
(fine); Sound first nothing; Read first the readout only (audit). Stale lines and order: with one line there is
nothing to go stale across mode switches; mode switch and drawers call `V.hush()`. `allLines()` and
voice/lines.json agree word for word on the one line.

#### Audit pilot

- Leads confirmed: guide "choices cut short by a scroll panel" (USGS, NASA links below the fold), real but minor
  (finding 10). The held-click table's spoken column also shows finding 3, though the audit did not flag it.
- Leads wrong: all of the roughly 200 "overlap: #stage / ..." rows (the stage is the full-screen well; every control
  sits on it by design); "keep region hidden" for #readout, #controls, #tray in the guide and manual states (modal
  drawers make main inert and cover it on purpose); "hint out of view" in every state (the hint hides after the first
  action, as the Curiosity brief asks); guide "button.close / h2 overlap" (the h2 box has 80 px right padding, no text
  collides).
- What it missed: missing name and result lines (2), metals at 35 fps under 4x slowdown (1), inverted aria-pressed
  on Spheres/Sticks (4), the 35 px model in the 680x425 preview (5), Read content and speech shape (6), Tab order
  through 40 atom stops (9), the one-atom no-grow wording (11).

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: molecule-forge (Curiosity No. 12), round 1

Cold lens, 2026-11-06. Played twice: as a grade 7 student alone at home, and as a teacher projecting at 1366x768.
Bundle `tools/molecule-forge/molecule-forge.html` as built. Own frames in
`S:/CurioClass-codex-scratch/molecule-forge/play/f1` to `f4` (drive.py, held clicks, port 9451; 375 wide through the
iframe host on 8875). Shared audit cited from `S:/CurioClass-codex-scratch/molecule-forge/audit-r1`.

**Counts: 0 blocker, 10 should fix, 7 polish, 4 nit.**

#### Short test (Curiosity)

- **Would a kid open it unassigned?** Yes. Two taps on H and water bends and names itself (f1/p02); a carbon and Grow
  builds a 525-atom diamond shell by shell (f2/c02, c03). Real reactions with nothing read.
- **Would an adult play with it for fun?** Yes. Loading caffeine and turning it (f1/p12), closing a ring by drag
  (f3/d01: cyclopropane, "about 60°"), O=Si=O getting its special card (f3/d05) and 40 recognised extra graphs give
  real depth.
- **Is the real thing the interface?** Yes. The model is the only working surface; readouts are live formulas, angles
  and neighbour counts.
- **Does it work with no finish line?** Yes. No score, goal, level, count or "found" marks; the lesson-creep word
  search on src.html hits only the Manual heading "Things people have found". The field guide lists all 39 pages.

Passes all four. The flaws below are about the moments between taps, not the shape.

#### Should fix

1. **The closing moment is flat.** Forge, `src.html:453-465` (`edited()`). The spec's payoff for the first two
   minutes is a cyan ring pulsing out, the guide tab lighting with the name, and the name spoken ("Water."). The build
   plays a three-note tone and glides to the conformer; the only visible change is the readout name. No ring, the
   Field guide button never changes, and no name is spoken (`voice/lines.json` holds only the hint; no `V.say`
   anywhere). Crystal test results are not spoken either. Seen on f1/p02 and audit state-water-1366x768.png; source
   check. The spoken name can wait for the shared voice pass (BASELINE 18), but the ring and the lit guide tab are
   visual and should land now. Tag: family:curiosity.
2. **The one hint vanishes on the wrong tap and is spoken stale.** `src.html:1217-1222`: any click anywhere (except
   Read and Sound) hides the hint. Tapping the red oxygen in the well, the most obvious "atom" on screen, adds nothing
   and removes the only instruction (f4/h01: hint hidden, 1 atom); so does Motion (f4/h02). When the first tap *does*
   add H, the voice then says "Tap an atom to snap it on." after the student already did it (f1/p01 voice log; audit
   one-click rows 1 to 9). Better: hide the hint on the first atom actually added; speak it only when the first gesture
   did not add one; word it "Tap an atom in the tray to snap it on." since the oxygen is an atom too. Tag: general.
3. **A stray tray tap in Crystal silently wipes the grown crystal.** `src.html:499-501`: with a one-atom seed, any
   tray tap adds to the seed and sets `crystal=null`. After growing diamond, one tap on H leaves "C · H, Seed plate"
   and an empty bench (f2/c15). The Undo button is hidden in Crystal (`src.html:687`), so only Ctrl+Z gets the diamond
   back, and Grow now refuses ("This closes into a molecule"). Show Undo in Crystal too, or keep the grown specimen
   until Clear seed. Tag: general.
4. **Push outcomes look alike, so the comparison does not land.** Crystal, `src.html:878-883`. Copper "bends" and
   graphite "slides" both draw as the top half translated sideways (f2/c07, f2/c08); the copper frame reads as a
   shear with long stretched bonds, not a bend. Diamond's push goes out and back (`65*sin`), so the end state (and a
   tap mid-test) looks untouched while the strip says "64 bonds cross this cut and none let go" (f2/c05); the spec's
   "count the bonds that hold" has nothing to count. Highlight the crossing bonds at the end, and give bend, slide and
   crack distinct end shapes. Tag: family:curiosity.
5. **Plurals do not match counts.** "1 SPOTS OPEN" (f1/p04, f1/p01), "1 lone pairs" (f1/p06 ammonia), tray labels
   "Hydrogen · 1 spots", "Sodium · 0 spots" (audit control names). `src.html:670, 706, 1047`. POLISH "Words match the
   state". Tag: general.
6. **Na plus Cl in Forge contradicts itself.** The strip reads "ClNa · NOT IN THIS GUIDE" while the result line says
   "Na⁺ Cl⁻ · an ion pair. Grow salt in Crystal." and the guide has a Salt page under NaCl (f3/d03; `src.html:709`).
   Show "Ion pair" (or "Salt, as one ion pair") and NaCl. Tag: family:curiosity.
7. **No-grow messages fail the cheap sweep.** `src.html:574-582`. Na + Na is refused with "These do not build a
   crystal in this forge. Try one atom of each alone." although Na alone grows sodium metal and Cu + Cu grows copper
   (f2/c10). Si + C is told "This closes into a molecule. Grow carbon alone, or two carbons." (f2/c11); silicon carbide
   is a real diamond-pattern network, so this line is untrue (the Teaching lens should weigh it against the Curiosity
   rule on readouts that lie). A single S, H or O seed gets "Two of these close up into a small molecule" (f2/c12).
   Tag: family:curiosity.
8. **"Things people have found" was cut to four sentences.** Manual, `src.html:272-273`. The spec lists nine short
   finds with sources (lone pairs squeeze the angle 109.5 / 107 / 104.5; 78 °C against -24.8 °C; 92 legal C/N/O
   structures with 56 unnamed; the pencil; crack against bend; CO2 against SiO2; silicon warm; Wöhler 1828). This is
   the month-of-use depth a Curiosity is judged on, and the 92/56 one invites inventing. Restore them as short
   separate entries. Tag: family:curiosity.
9. **The 16:10 preview shows a tiny model.** At 680x425 caffeine is drawn about 130 px wide, pushed into the right
   corner (`src.html:867-868`, `cx=w*.78` when short), smaller than the tray, with the hint text over its lower edge
   (f2/n05; audit size-680x425.png for the lone oxygen). The preview beside "Play full screen" is the tool page's first
   impression. Tag: general.
10. **Read speaks what a voice will misread.** `readText()` (`src.html:745-747`) sends "C₈H₁₀N₄O₂. Caffeine. ALL
    SPOTS FULL. O · Oxygen 2 spots · 2 filled..." (f3/d04; audit row 12 for oxygen). Subscript digits, middle dots
    and capitals in a projected class are a garble; the spec also asks Read for the angle, which is only included when
    the selected atom has two neighbours. Spell formulas out ("C 8, H 10, N 4, O 2") and say "all spots full".
    Tag: general.

#### Polish

1. **Drags give no feedback until release.** `src.html:1000-1010, 1053-1064`. Dragging a tray ball or a model atom
   draws nothing: no ghost ball, no lit peg, no stretched bond; the result just appears on release (f3/d01, f3/d02
   worked, but blind). A model kit is all about the snap; a ball following the pointer and the target peg lighting
   would make ring closing discoverable.
2. **A second structure shrinks the first.** A lone atom is placed 300+ pm away and the view reframes to both, so
   water drops from about 110 px to 55 px wide in a mostly empty well (f1/p02 against f1/p03, f1/p04). Frame the
   structure in focus, or park the stray atom closer.
3. **"NOT IN THIS GUIDE" mid-build.** After the very first tap the strip reads "HO · NOT IN THIS GUIDE"
   (f1/p01): to a student building water it sounds like "wrong". Leave the name blank (or "BUILDING") until every spot
   is full; keep NOT IN THIS GUIDE for closed inventions, where it is a good moment (f1/p10).
4. **Current barely shows.** The battery's left wire is drawn straight through the specimen (f2/c06), and flow (14
   small dots), "a little" (3) and none are hard to tell apart at projector distance. A brighter carrier stream and
   wires that stop at the faces would let "a sea, a little, none" read without the strip.
5. **The empty seed plate is a bare ellipse with no next step.** f2/c01: "SEED PLATE · EMPTY", Grow disabled, nothing
   on the plate says to tap an atom. The spec wants a small specimen stand; an engraved "TAP AN ATOM, THEN GROW" on
   it would name the action without breaking the Curiosity rules. Tag: family:curiosity.
6. **The inspected crystal atom is buried.** After Grow, atom 1 sits in the middle and its cyan ring is lost among
   525 balls (f2/c03, audit state-salt-1366x768.png) until Cut open. Start inspection on an atom near the viewer, or
   auto-cut briefly on the first tap.
7. **Ether by taps.** C, O, C taps always make ethanol (f1/p08) because the next atom joins the most open spot. O, C,
   H, H, H, C does make dimethyl ether. A Manual find ("the order you tap decides which isomer you get") turns this
   into a discovery instead of a dead end.

#### Nit

1. Also-known names show lower case in the strip ("formaldehyde", f3/d06) beside "Water", "Ethanol".
2. Keyboard path T, 2, G leaves the Forge hint "Tap an atom to snap it on." on screen over the grown diamond
   (f4/h03); the hint only hides on a click.
3. At 375 wide the hint wraps to a lone "on." (f2/n01).
4. Silica-style formulas read "O₂Si" in the strip and "SiO₂" in the guide (f3/d05); the Manual explains Hill order,
   but a student comparing the two sees a mismatch.

#### Checked and fine

First screen at every size (audit size-*.png), water and H2 by taps (f1/p02 to p04), methane about 109° and ammonia
about 106° after the glide (f1/p05, p06), CO2 at 180° (f1/p09), 40-atom cap message (f1/p11), caffeine and benzene
loads (f1/p12, p14; f3/d07), Spheres (f1/p13), all seven crystals grow to their stated counts, salt cracks with a gap
and 5 neighbours at the face (audit state-salt-fracture), graphite and silica messages (f2/c08, c09), Show with Motion
off keeps the 30° buttons (f3/d07), 375 Forge and Crystal layouts (f2/n01 to n04). Frame times during Crystal Show at
1x: median 16.7 ms (f4/h04; Craft owns the 4x check).

#### Audit pilot

- **Leads confirmed:** the "spoken" column showing the hint after an atom tap (rows 1 to 9) is the stale-hint problem
  in should fix 2.
- **Leads wrong (noise):** every "overlap #stage / ..." row at every size (the well is a full-screen canvas with the
  tray, power panel and readouts laid over it by design); "hint out of view" in every state (the hint hides after the
  first click by design); guide "Close / h2" overlap (the Close button sits beside the heading, no overlap on
  state-guide-1366x768.png); "keep region hidden" for the guide and Manual (modal drawers make the bench inert);
  "choices cut short" for the USGS and NASA links (source links further down a scrolling page, not choices).
- **Missed:** the flat closing moment, plurals, the crystal wiped by a stray tap, look-alike Push outcomes, the Na Cl
  readout contradiction, wrong no-grow messages, the cut Manual finds, the tiny 680x425 model and the Read text.
  None of these are mechanical-layout leads.

Nothing here is cultural, Native or hard history; no sensitivity review needed from this lens.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: molecule-forge (Curiosity No. 12), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and VISION.md "Curiosities: the second shape", not lesson norms.
Scratch: `S:/CurioClass-codex-scratch/molecule-forge/teaching/` (frames in `frames/`, rule checks in `checks.js` and
`checks.json`, run headless on the built bundle, port 9441).

Counts: 1 blocker, 5 should fix, 4 polish, 3 nits.

#### Findings

##### 1. Bond labels state lengths the model on screen contradicts (blocker, family:curiosity)
- Where: src.html:726 (bond button text), length() at src.html:376; Forge, any matched molecule.
- What: the visible label is the radius-sum estimate ("H single · ~62 pm") even after the molecule has glided to its
  stored conformer. The estimate's assumption fails exactly where students look: H2 reads ~62 pm while the model is
  drawn at 74 pm (the Manual itself says 74). Benzene, vanillin and aspirin ring bonds read "single ~152" and "double
  ~132" while every ring bond in the model is 139 pm, so the readout teaches the alternating-length misconception the
  real structure disproves. Others more than 5 percent off: O2 115 vs 123, H2O2 O-O 132 vs 145, formic acid C-O 142 vs
  135, urea and caffeine C-N 147 vs 137-139. Only the aria-label and a Manual paragraph say "radius estimate"; the
  visible text just says "~".
- How seen: frames/h2-label.png (label "H single · ~62 pm" beside the drawn H2); `dev` shot in shots2.json measured
  every guide bond against its label (14 bond types over 5 percent).
- Better: once a structure matches, label the stored model's length ("139 pm, model"); keep the radius estimate only
  while building and say "estimate" on screen.

##### 2. Most field guide facts are gone; 22 of 32 molecule pages and all 7 crystal pages restate the model (should fix, family:curiosity)
- Where: material.json `fact`; crystal pages built at src.html:1076 (`fact:c.pattern`).
- What: 22 molecule pages read "In this model: 2 O. 1 double bond." (Oxygen, Nitrogen, Ammonia, Methane, CO2, Acetone,
  Propane, Butane, Vanillin, Aspirin and 12 more). The crystal pages say only "Every inside atom touches 4 neighbours."
  The spec lists a real fact for each (21 percent of the air, 78 percent nitrogen, dry ice at -78 °C, fertilizer,
  Mohs 10, pencil lead, chips, quartz and sand, most wire, sodium cut with a knife) and says they are kept unchanged.
  The guide is meant to be read "like a book"; with these it answers nothing the strip did not already say, and the
  crystal pages lose the structure-to-use link that HS-PS2-6 rides on. The Manual's "Field guide facts" list repeats the
  same 22 placeholders as facts.
- How seen: frames/guide-oxygen.png, frames/guide-diamond.png; a count over material.json (22 of 32 start "In this model").
- Better: restore the spec facts, each with its named source (most are NASA, USGS, EIA, EPA, NIST-level facts that are
  easy to double-source); drop only the ones that truly fail a second source.

##### 3. The outer-electron link (HS-PS1-1) is claimed but never shown (should fix, general)
- Where: spec Map "outer electrons set the bonding spots"; notes.md "Good to know"; atom table src.html:287 (`ve` is
  defined but never displayed).
- What: the student sees spots, filled and lone pairs, never the valence electron count, so nothing they can do or
  see connects spots to outer electrons or the periodic table. Rule 2 binds only the anchor (MS-PS1-1, taught well),
  but the "also reaches" claim is not true as built.
- How seen: grep of src.html (`.ve` unused); selection readout in frames/water and h2-label.
- Better: one more line in the selected-atom readout ("6 outer electrons · needs 2 more · 2 spots"), and on the tray
  ball's label; or drop HS-PS1-1 from the spec and notes.

##### 4. A lone atom and its molecule carry the same name (should fix, family:curiosity)
- Where: src.html:709.
- What: the opening oxygen atom reads "Oxygen", identical to the O2 page "Oxygen · O2"; a lone H reads "Hydrogen",
  and so does H2 one tap later. Atom versus molecule is the core idea of the anchor (MS-PS1-1), and the strip blurs it
  at the very first screen.
- How seen: frames/guide-oxygen.png (strip "O / Oxygen" beside page "Oxygen · O2 · 2 atoms"); checks.json `loneH`
  and `h2` both name "Hydrogen".
- Better: "oxygen atom" / "hydrogen atom" for a single atom; the guide name only for a matched molecule.

##### 5. O=Si=O settles bent, at about 165 degrees, against the groups rule it teaches (should fix, family:curiosity)
- Where: relax() at src.html:748; Forge, Things to do 7.
- What: CO2 glides to 180 (matched), but O=Si=O, which has the same two groups at the centre and no match to glide to,
  stops at 165 degrees with Motion on (153 with Motion off). Things to do 2 and 7 invite exactly this comparison, and
  the readout then says "about 165°" for a shape the Manual says is straight. Any unmatched two-group centre will do
  the same.
- How seen: `osio-motion` shot (3 s settle, angle 165.4); checks.json `osio` (calm, 153 degrees).
- Better: let relaxation reach its 180 target for two-group centres (or snap to the ideal angle when settled).

##### 6. The Manual is written for an engineer, not a grade 6 to 10 reader (should fix, general)
- Where: src.html:238-276 (Manual).
- What: "element-labelled connections", "computed PubChem conformer", "Two records had no supplied 3D model", "The extra
  recognized allene record also supplied only a 2D diagram ... two perpendicular pi bonds", "cristobalite-like
  network", "appreciable current", "not an atomic slip solver". These are build notes. The honesty content is right;
  the reading level is about grade 14.
- How seen: read in the Manual drawer and in src.
- Better: plain sentences ("Hydrogen and silane use a textbook shape instead of a PubChem one"), with build detail moved
  to notes.md.

##### 7. "Things people have found" has 4 of the spec's 9 entries (polish, family:curiosity)
- Where: src.html:272.
- What: missing: lone pairs squeeze the angle (109.5, 107, 104.5), the two boiling points, 56 of 92 small structures
  unnamed, salt cracks while copper bends, CO2 small but SiO2 giant, silicon a semiconductor, Wöhler 1828. These are the
  month-of-use depth the Manual is meant to hold, read after finding them.
- How seen: Manual drawer text against spec "The Manual".
- Better: add them back, each with its source.

##### 8. Hill formulas on the strip differ from the guide headings for familiar molecules (polish, general)
- Where: strip formula, hill() at src.html:368.
- What: ammonia reads H3N, hydrogen chloride ClH, the ion pair ClNa, while the guide page says NH3 and HCl and the
  crystal says NaCl. Correct Hill order and the Manual explains it, but a 7th grader comparing strip and page sees two
  formulas for one substance.
- How seen: checks.json `nh3` ("H₃N" / "Ammonia"), `nacl` ("ClNa").
- Better: show the conventional formula on the strip when the guide knows the molecule, Hill order otherwise.

##### 9. Crystal test results are never spoken (polish, family:curiosity)
- Where: voice/lines.json has only the hint; src.html:328.
- What: the spec's Voice says a molecule's name is spoken on first close and each Crystal test's result line too. The
  Push and Current lines ("Like charges met and pushed apart. Salt splits along flat faces.") are the HS-PS2-6 moment;
  they are only heard via Read. (Craft will judge the voice list itself.)
- How seen: grep of V.say / lines.json.

##### 10. On-screen words above grade in the test lines (polish, general)
- Where: src.html:630.
- What: "No current. No mobile carriers in this model." for diamond and silica. "Nothing can move to carry charge" says
  the same thing to a 7th grader.

##### 11. Plural slips (nit, general)
- src.html:670 and 706: "1 lone pairs", "1 SPOTS OPEN", tray labels "1 spots". checks.json `nh3`, `loneH`.

##### 12. Salt and silica counts use "ATOMS" and a partial "INSIDE" (nit, family:curiosity)
- Salt reads "392 ATOMS" (they are ions, as the spec says); silica reads "83 INSIDE", counting only Si, while inside O
  atoms also sit fully inside. checks.json `crys`.

##### 13. "Na · sodium" is lower case where every other atom is capitalised (nit, general)
- src.html selectedInfo; checks.json `nacl`.

#### What passed (tested)
- Done when 1: two H on the waiting O make water, "ALL SPOTS FULL", named, "about 104°"; two more H make H2, named.
- Done when 2: every one of the 32 guide molecules matches its own page (no cross-match, butane and isobutane apart,
  ethanol and dimethyl ether apart); formaldehyde shows the also-known card; H2N-NH-NH2 reads NOT IN THIS GUIDE;
  bond orders ignored once spots fill (benzene's two drawings).
- Done when 3: angles after the glide 109 (CH4), 106 (NH3), 104 (H2O), CO2 180; Hill order as specified.
- Done when 4: all 7 seeds grow to the stated counts (525, 525, 600, 392, 561, 559, 147 Si + 220 O); inside neighbour
  counts 4, 4, 3, 6, 12, 8, Si 4, all inside atoms; no-grow messages for C#C, C-O, O, Cl, H.
- Done when 5 (outcomes): salt splits, metals bend, graphite slides, diamond, silicon and silica hold (bond counts
  from the sample); current: metals and graphite flow, silicon a little, salt and the networks none.
- Done when 6 and 10: guide index lists all 39, no counts, locks or found marks; no score, goal, level or finish anywhere.
- Special cards: O=Si=O, O3 ring, Na+ Cl- ion pair, Cu-Cu all show their honesty lines.
- No giveaway risk: there is no predict or quiz mode. No cultural, Native or hard-history content; no sensitive topic
  needing a rule 8 note. Support at home ideas (pencil, salt and copper wire, a tiled floor) are doable tonight.

#### Facts spot-checked (second source: recomputation and standard reference values)
1. Salt grain 1 mm across about 4.5 x 10^19 ions: 2.165 g/cm3 x 1 mm3 / 58.44 g/mol x 6.022e23 x 2 = 4.46e19. OK.
2. Water bend 104.5 degrees. OK. 3. Quartz Si-O-Si about 144 degrees. OK.
4. Cu-Cu 255.6 pm (fcc a = 361.5 pm / sqrt 2). OK. 5. Graphite sheets 335 pm apart. OK.
6. Neighbours: diamond 4, graphite 3, rock salt 6, fcc copper 12, bcc sodium 8. OK.
7. Ethanol boils about 78 °C; dimethyl ether about -24.8 °C. OK.
8. Wöhler urea 1828; Faraday benzene 1825; Rosetta glycine at 67P, published 2016. OK.
9. Water covers about 71 percent of Earth's surface (USGS). OK.
10. Cordero covalent radii H 31, C 76, N 71, O 66, S 105, Cl 102, Si 111; Bondi vdW radii and Jmol colours as listed. OK.
11. Salt 8 x 7 x 7 = 392; silica 147 + 220 = 367. OK.
No fact on screen was wrong; the problems are the missing facts (finding 2) and the bond labels (finding 1).

#### Frames looked at
Mine: frames/h2-label.png, guide-oxygen.png, guide-diamond.png, plus the scripted readouts in checks.json and the
shots2.json results (bond deviations, O=Si=O settle, silica readout). Audit: audit.md rows only; its clean rows
(Motion off, resize mid-action, held clicks) are cited, not re-shot.

#### Audit pilot
- Leads confirmed: none that bear on teaching.
- Leads wrong (noise): all "overlap: #stage / ..." rows (the canvas is full screen by design); "keep region hidden" for
  #readout, #controls and #tray in the guide and manual states (modal drawers, expected); "hint out of view" in every
  state (the hint correctly goes after the first action); "choices cut short" in the guide (two source links below the
  fold of a scrolling page, fine).
- Missed (outside its reach): bond labels contradicting the drawn model, the placeholder guide facts, atom and molecule
  sharing one name, O=Si=O settling bent, the unshown valence electrons, Manual reading level.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: molecule-forge (Codex fix, round 1)

Repair in `S:\CurioClass-codex`, 2026-11-06. Only this tool and `_scratch/molecule-forge/` were written.
`refine.md` and `refine/` were not edited. No commits, branch changes, engine changes, registrations or uploads.
The pre-existing spec working-tree difference was left alone. Chrome: 9920, 9922, 9923, 9924; final audit: 9921. Host: 8725.
Evidence paths below are relative to `_scratch/molecule-forge/`. All FIXED claims have observed DOM numbers, frames or logged events.

#### Blocker

1. **FIXED. Bond lengths.** Reproduced H2 62 vs 74 pm, benzene 132/152 vs 139 pm, O2 115 vs 123 pm and peroxide 132 vs 145 pm in `before-bonds.json` and its frame. Labels now use the mapped stored coordinates on a match and say “model”; unfinished bonds visibly say “estimate”. `fix-verification.json` checks **972 directed bond readouts across all 72 recognized graphs: zero failures**. `after-bonds.json` gives the same examples after repair. The Manual explains benzene's equal ring bonds and both Kekule drawings.
2. **FIXED. Silicon no-grow falsehood.** Reproduced Si+C and Si+N false molecule claims in `before-seeds.json`. The fallback now states only which seeds this instrument supports, making no claim that unsupported silicon substances are molecules. `after-seeds.json` and the 90 seed cases in `fix-verification.json` prove the new wording. No eighth crystal was added.

#### Should fix

1. **FIXED. Visual close.** One cyan ring per first closure of each molecule per visit; a static ring with Motion off. The guide key lights with the molecule name for 4.5 seconds and retains the corresponding page while lit. `fix-after-frames/after-close.png`, `fix-native-frames/calm-close.png`, `close-guide-page.json` and its final frame. New spoken names remain deferred.
2. **FIXED. Hint timing and meaning.** Before: Motion erased the hint; first H spoke the instruction after adding H; T,2,G left the hint over diamond. `before-hint-oxygen.json`, `before-hint-firstH.json`, `before-keyhint.json`. After: only a successful atom add hides it, including tap, drag and keys in either mode. First add speaks no hint; another first action speaks the revised tray-specific hint once and leaves it visible. `fix-verification.json`: voice-water has no how line, voice-other has exactly one, keyboard and tray-drag hide the hint. Manifest equals `allLines()`. A held Guide, Load path also hides the hint with **zero late voice entries** (`load-hint.json`).
3. **FIXED with documented narrower facts.** Reproduced 22 composition placeholders and the seven pattern-only crystal pages. All **32 molecule and seven crystal pages now contain real context facts**, named references and permission boundaries; no “In this model:” facts remain. `fix-fact-sources.json`, `fix-verification.json` metadata, final Oxygen and Diamond guide frames. Main use facts are restored. Unconfirmed or changing clauses are omitted explicitly in notes: the exact US ammonia percentage, current CO2 ppm, vinegar minimum, caffeine range, Latin etymology and a global “most wire” share. These were not replaced by model-count placeholders.
4. **FIXED. Atom versus molecule.** Opening strip now says “Oxygen atom”; single H says “Hydrogen atom”, while matched molecules keep their guide names. `before-atom-voice-view-ion.json`, `fix-verification.json` read/keyboard data, default and water frames.
5. **FIXED. Two-group shape.** Reproduced O=Si=O at 165.53° in Motion on. Angular relaxation removes the near-straight spring stall and turns whole acyclic branches at a straight centre. `fix-verification.json`: Motion on/off angles respectively **179.9996/179.9994°, 120/120°, 109.5/109.5°** for linear, flat and tetrahedral examples. `after-angle.json` and frame. An extra branched-end model exposed the same stall at 166.54°; the whole-branch repair reaches **179.9995° on and 179.9949° calm**, with before/after JSON and frames under `fix-nonleaf-*`. Cycles are not rotated as one branch.
6. **FIXED. Outer electrons.** Selected atom readout and every tray label include the outer-electron count, with spot and lone-pair counts retained. The first-H record explicitly reads O, six outer electrons, two spots, one filled. `after-hint-firstH.json`, final default frames and native read strings.
7. **FIXED. Plain Manual.** Reproduced the listed technical phrases, then rewrote the instructions while retaining shape fallbacks, finite edges, charge/stereo limits, straight silica and qualitative test limits. Build details moved to notes. The listed phrases are absent. Our approximate readability estimator did **not** reproduce the review's grade-14 number: it measures 7.67 before and 3.81 after, with sentence length **11.45 to 8.76 words**. Treat that as a comparison, not a validated reading grade. `fix-localcheck.json`, `fix-layout-frames/manual-final.png`.
8. **FIXED. Nine finds.** All nine are separate Manual entries, with source links or an explicit local computation. `fix-verification.json`: nine list entries. Independent exhaustive enumeration confirms **92 legal structures, 36 named, 56 unnamed**. The isomer boiling points, pencil, material tests, CO2/SiO2, semiconductor and Wöhler finds are present.
9. **FIXED. Stray seed edits.** Reproduced diamond disappearing after H and hidden Undo. Preserve the specimen until a different supported seed or Clear seed; Undo is visible in Crystal. The native check repeats this for **diamond+H, sodium+H, copper+O and silicon+Cl**, all retained and all undone to the original seed. `before-seeds.json`, `fix-verification.json`, audit state `preserved-specimen`.
10. **FIXED. Distinct Push shapes.** Salt leaves a gap; metal rows bow continuously; graphite sheets offset; held networks keep their geometry. All bonds counted across a held cut receive an orange inspection overlay after the spheres, including **64 for diamond** and **26 for silica**. Finishing mid-test uses the identical end-state transform. `fix-before-frames/before-push-*.png`, `fix-seal2-frames/final-push-Diamond.png`, `final-push-Copper.png`, and the seven crystal Push frames.
11. **NOT FIXED. Strict 60 fps at 4× CPU slowdown.** Reproduced in the isolated 1366×768 measurement: copper **29.58 fps**, sodium **30.11 fps**. Culling hidden back bonds while keeping inspected and cut bonds improved them to **41.18 and 46.41 fps**; graphite reached **60.00 fps**. Both metal runs still have a 33.4 ms p95. `fix-perf-before.json`, `fix-perf-after.json`, bounded script `fix-measure.py`. A larger renderer change remains open; no 60 fps claim and no physical Chromebook claim.
12. **FIXED. Preview framing.** Reproduced all named examples at 680×425 and water at 800×500. Short windows now reserve a clear model area and fit the actual projected bounds. At 680, lone O grows **33.6 to 103.3 px**; water **82.7 to 175.7 px**; caffeine **115.9 to 139.9 px**. The hint sits clear to the left. Final default/caffeine/water frames and JSON, native 800 frames. Phone is additionally checked in a real 375×812 iframe.
13. **FIXED. Read.** Native initial Read includes the visible hint. Formula tokens are spoken as “C 8, H 10, N 4, O 2”, glyph punctuation is expanded and doubled periods removed. Every selected centre with an angle is included, even with three or four neighbours; methane's four-bond centre reads about 109 degrees. Crystal formulas use raw symbols too. `fix-verification.json` read-state/read-hint/voice-water; `read-silica.json`.
14. **FIXED. View state.** Fixed “Sticks / Spheres” switch label, current-position accessible name and `aria-checked`. `final-sound-switch-counts.json` observes Spheres/true then Sticks/false, without inverted announcements.
15. **FIXED. Ion pair name.** Na+Cl reads “Ion pair”, while Hill-order ClNa and the ion-pair honesty card stay intact. Before/after ion records and `fix-verification.json` read-state.
16. **FIXED. Other no-grow lines.** Na+Na explicitly requests one sodium atom; lone H/O/N/S/Cl name their element and state this forge's limit. Other unsupported pairs give a supported next seed, without a false generic claim. `before-seeds.json`, `after-seeds.json`, all 90 native seed records.
17. **FIXED. Grammar and case.** “1 SPOT OPEN”, “1 spot”, “1 lone pair”, “1 outer electron” and “1 neighbour”; capitalized bench state, Sodium/Copper and also-known strip names. `after-hint-firstH.json`, `final-sound-switch-counts.json`, final Push/default frames. Hill order remains unchanged.

#### Polish accepted

1. **FIXED. Drag snap.** Pointer-following ball, target ring and stretched bond for tray and model drags. Real held native mid-drag frames: `fix-native-frames/tray-drag-mid.png` and `model-drag-mid.png`; tray release adds one bond and hides the hint.
2. **FIXED. Stable second structure.** New structures park closer; the camera frames the focused component. Native water radius before and after adding a separate H then refocusing water is **90.5578 px in both cases** (`water-stability`).
3. **FIXED. Unknown only when closed.** The first HO build has a blank name and one spot open; closed unknown structures retain NOT IN THIS GUIDE. The 92-graph run distinguishes the 56 unnamed closed structures. First-H before/after records.
4. **FIXED. Current contrast.** Leads route around the specimen and stop at its faces. Flow has 38 bright carriers, silicon three, insulators zero. `fix-crystal-frames/current-Copper.png`, `current-Silicon.png`, `current-Diamond.png` were inspected at 1366×768.
5. **FIXED. Empty seed instruction.** Stand engraving says “TAP AN ATOM, THEN GROW” only while empty. Seed and populated specimen states checked in the audit and the 90 seed native run; `fix-final-leads-frames/empty-seed680.png` proves the engraving is visible at 680×425 too.
6. **FIXED. Visible inspected atom.** Grow selects a front-facing atom using view depth. The cyan ring is visible at the front after Grow, including the native keyboard salt and final crystal frames.
7. **FIXED. Isomer tap order.** Added the exact short find about the order of taps deciding the isomer, beside the ethanol/ether comparison; native metadata observes all nine finds.
8. **FIXED. Instrument controls.** Sliding metal handles on the two-position bench/view switches, lit Show/Cut keys, native keyboard support and current-value ARIA. Final bench/phone frames and switch-state numbers.
9. **FIXED. Outcome tones.** Native event capture distinguishes salt crack (140 Hz sawtooth), bend ring (440/660), sheet swish (230/120 triangle) and hold clink (1200/1700). Current uses a longer metal hum, shorter silicon tone, or one spark. `final-sound-switch-counts.json`; Chrome remains muted as required.
10. **FIXED. Tab order.** Atom focus controls moved after the bench controls in the DOM; native `atomkeysAfterControls: true` holds regardless of atom count. Keyboard alone builds water and grows salt.
11. **FIXED. Short guide.** At 680×425 the name moves from y=513.5 to **146**, fact from y=577.9 to **201.4–240.6**. `before-guide680.json`, `final-guide680-final.json`, matching frames.
12. **FIXED. Plain test line.** Diamond Current reads “No current. Nothing here can move to carry charge.” Native result and inspected full-size frame.
13. **FIXED. Counts.** Salt says **392 IONS**; silica says **367 ATOMS · 303 INSIDE**, comprising 83 fully coordinated Si and all 220 fully coordinated O. Final crystal JSON and the raw degree calculation in `insideCount()`.
14. **FIXED. Live-region changes.** Text writes use a value comparison; Grow writes only a changed shell count. Native observation of three identical syncs reports **zero readout mutations**.
15. **FIXED. Font fallback.** Both canvas Consolas declarations now include monospace; both seed engraving and battery appear in inspected frames.
16. **FIXED. OpenStax links.** **Zero personal-mirror links in the Manual**. Official book-section URLs, archived 2019 CC BY 4.0 and current CC BY-NC-SA 4.0 clearly distinguished. No current OpenStax prose or images republished.

#### Settled calls

- Applied all calls: spoken close names and Push/Current results remain deferred to the collective voice pass; existing hint/Read behavior repaired now.
- The silicon fix is honest wording, not a new material. Nine finds and plurals are treated as should-fix items.
- Required generated-illustration credit remains. No checklist, “found” marks, goal, score, quiz, forced finish or kit header was added.
- Full-screen well, inert modal drawers, Hill order, special cards and source art are retained. Open questions were not implemented.

#### Cheats tried

- There is no score or check to pass. Tried all 90 one/two-atom seed combinations, including unsupported Si pairs and Na+Na; unsupported recipes stay unsupported without false claims.
- Tried the seed-wipe pattern in four material families; every specimen survived and Undo restored its original seed.
- Exercised every matched graph's directed bond readout, then an unmatched oxygen pair; no silent radius estimate is presented as a model distance.
- Recomputed every legal one-to-three C/N/O graph independently, including all unnamed examples; no novelty or “wrong” claim appears.
- Native keyboard, held taps, real drags, both Motion states, view toggles, angle targets and repeated identical syncs all retain valid state.

#### Voice walk

- At a held-click, two-second pace: H, H, Read produces no late how line, then one Read of water, filled spots and the selected oxygen's angle.
- Side path: Motion speaks the tray hint once and leaves it visible; Read speaks that current hint again. Adding H hides it. Keyboard and drag adds also hide it.
- The log records playback requests in muted Chrome, including Read cutting the how line by request. No new recording was made.
- `voice/lines.json` equals `allLines()`: one fixed line, “Tap an atom in the tray to snap it on.” Dynamic Read is separate.

#### The real material

- Retained PubChem explicit graphs and stored coordinates: 32 illustrated plus 40 also-known entries, fetched 2026-11-05, federal numerical records public domain; all bundled. No new conformer data sampled.
- Retained original finite lattice arrays: seven materials, original generated graphs checked by coordination and counts. Referenced OpenStax 2019 CC BY 4.0 and CRC factual constants; no copied tables or images.
- Restored contextual facts: **all 39 page-specific facts, URLs, permission boundaries, check date (2026-11-06) and sampling description** are in `fix-fact-sources.json`, the in-tool Manual, guide pages and `tool.draft.json`.
- Online material was used only for fact checks and original short summaries. Government raw responses and their actual fetch failures/rights exclusions are preserved under `data/fix-facts/` and `fix-fetch-manifest.json`. No fetched outside prose, art or restrictive annotation dataset enters the bundle. Some browser-readable sources return 403 to a download; that is recorded, not treated as retrieved data.
- OpenStax official current licence was checked at https://openstax.org/books/chemistry-2e/pages/preface. The current web edition is CC BY-NC-SA 4.0; the prior archived reference is CC BY 4.0. Link labels explicitly distinguish them.
- The two biological isomers' boiling points, original named fact sources, radii, Jmol colours and all 40 illustrations retain their credit boundaries. No data or topic was added outside the brief.

#### Engine changes wanted

None. The performance gap is in the tool renderer, not a request to change the shared kit.

#### Audit

The required audit ran **once**, within its 2400-second limit, with the full walk and resize stress enabled: `fix-audit/audit.md`. It completed with **255 mechanical leads**. It was started before the last scoped corrections, so its original snapshots intentionally retain the failures below; this is not a claim of a clean final audit or an exit PASS.

- **Short seed exception: FIXED.** Three state groups hit a null frame-index lookup in short Crystal windows. Reproduced by the audit, corrected the Forge-only index assumption, then re-shot the C=C seed at **680×425 and 800×500**, both with zero errors. `fix-seed-check-frames/`, `fix-final-leads-frames/`, `seed-680.json`, `seed-800.json`.
- **Phone inspector obstruction: FIXED.** The retained specimen's seed-bond label covered the ATOM input in salt, fractured salt and the preserved-specimen state. Grown specimens now hide the ungrown seed control. Final 375×812 recheck reports **9 of 9 inspector sample points visible**, no seed label and scroll width **375**; `phone-salt-inspector.json` and `fix-phone-ready-frames/phone-salt-inspector.png`. The first targeted phone retry collided with the audit's own host and failed to load its child; that failed artifact is retained, and the successful retry ran only after the audit's server closed. The Scratch host runner now refuses an occupied port.
- **218 canvas/control overlap rows:** the full-screen canvas is the viewing well behind the controls, as explicitly settled in Refine. These are expected compositing, not clipped controls. All 43 audit frames were inspected through four indexed contact sheets and the affected phone frame at full size.
- **Hidden hint and hidden main keep regions:** intended after a real atom add or while a modal drawer makes the bench inert. Native logs and frames verify those states. No welcome, goal or extra instruction panel was added to satisfy this lesson-shaped lead.
- **Guide Close/header/label boxes:** padded block rectangles intersect, but the actual title and label glyphs do not run under Close in either named frame. The guide's name and fact remain visible at 680×425.
- **Two source links below the guide fold:** citations in a scrollable reference page, not hidden play choices. Turn, Load, the name and the fact remain in view; sources remain reachable by scrolling and keyboard.
- **Quick bench toggle cuts the one hint:** expected `V.hush()` on a mode change, allowed by BASELINE 16. The hint stays visible until an atom is added, and Read repeats it. No automatic replay loop was added. Five held clicks and the other quick-tap rows are clean.
- **Resize and calm:** completed clean, no exceptions or stuck disabled controls. `fix-audit-triage.json` groups every reported lead. Original audit output was not rewritten.


#### Frames and checks

- Before: `fix-before-frames/` (all 16 frames inspected), plus stored numbers. After: `fix-after-frames/`, `fix-layout-frames/`, `fix-crystal-frames/`, `fix-native-frames/`, `fix-last-frames/`, `fix-seal-frames/`, `fix-seal2-frames/`, `fix-final-leads-frames/`, `fix-phone-ready-frames/` and `fix-nonleaf-after-frames/`.
- Early intermediate frames exposed an undersized preview tray, weak hold highlights and five-pixel phone overflow; these were corrected and targeted frames repeated. Superseded frames are evidence, not claimed final layouts.
- All seven STANDARDS desktop sizes, both modes at 1366×768, 680×425 and 800×500 previews, Motion off, native keys and a hosted 375×812 iframe were covered. Phone scroll width is now **375**, matching its viewport.
- The local check finds zero lesson-creep words in src.html and zero em dashes in changed public source/notes/voice/metadata. Report words such as “score” describe the excluded lesson conventions only.
- Final bundle: about **1110 KB**. The native instrument run has **zero console exceptions and zero external network requests**. A parent-host favicon 404 in an earlier run is distinct from the offline bundle and was corrected in the Scratch server before the final check.
- All browser and server processes started by these bounded drivers are closed by their driver cleanup. The final resource check confirms every owned debug and host port is closed (`fix-resource-check.json`).

#### Left open

- Should fix 11 remains open: copper and sodium do not meet strict 60 fps at 4× slowdown. Done when 8 therefore remains FAIL; no exit-pass claim is made.
- The full audit was not repeated after its focused corrections and the broader branch-angle check. The preserved audit contains resolved leads; the next integrator should audit the final bundle afresh, as planned by the handoff.
- The session was unattended. Where wording or layout needed a choice, the Curiosity brief and Refine's stated lean won. Deferred spoken events and spec open questions remain for their designated pass.

#### Instrument comparison

The repaired bench retains the instrument density, direct controls and live readouts seen in the Beat Lab reference. The object remains the interface, the guide remains freely browsable, and play has no assigned path or finish. This repair did not rerun three review lenses or claim a new independent ten-minute short-test verdict.

| Molecule Forge | Reference: Beat Lab |
|---|---|
| ![Molecule Forge](../../_scratch/molecule-forge/fix-native-frames/water-native.png) | ![Beat Lab](../../_scratch/molecule-forge/fix-seal2-frames/reference-beat-lab.png) |

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Molecule Forge build handoff

#### Source map
src.html holds the bench UI, graph operations, element-labelled isomorphism, local geometry relaxation, canvas rendering, drawers and storage.
material.json and also-known.json pack explicit PubChem atoms, bonds and coordinates. crystals.json contains generated lattice graphs.
art contains forty cropped, coordinated real-material paintings. All are bundled in molecule-forge.html.
Scratch holds reproducible gathering, lattice, packing and validation scripts, raw source records, shots and audit evidence.

#### Tricky parts
The focused connected component controls naming and shelf saves; the well may hold several structures. Matching ignores bond order only when every spot is filled.
PubChem coordinate models are not measured geometry. Interior means actual full coordination in the finite sample, rather than an unverified fixed count.
The Manual and field guide are overlays with focus containment. Power controls belong to the instrument.

#### Engine changes wanted
None. Shared kit, scripts and other tools were read only.

#### Next build considerations
See the final report for exact validation limits and retained approximations. No polish round or commit was started.

#### Rebuild and evidence
From the repository root, set CURIO_DRAFT=1 for the local process and run scripts/bundle_tool.py molecule-forge with a 120-second subprocess timeout. This packs the existing data and all forty WebPs without fetching anything.
Scratch/closeout-prep.py demonstrates bounded bundling, JavaScript parsing, independent material checks and focused native-key frames. It uses HTTP 8795 and Chrome 9990, then closes its own processes.
Raw PubChem records are in Scratch/data. prepare.py and gather-extra.py pack the two molecule arrays; final-facts.py applies checked facts and computed descriptions; fix-fallback.py and allene-fallback.py apply the labelled coordinate exceptions. crystals.py generates finite lattice graphs. Crop bounds, originals and crop/pack scripts preserve the image provenance.
validation-manifest.json hashes the final code, data, metadata and bundle. final-native.json, final-controller.json, material-check.txt, closeout-log.txt and audit/audit.md preserve the checks and their limits. The full audit ran once; later corrections have focused checks.
The strict 60 fps stress target remains unmet: graphite has a 16.7 ms median and 33.4 ms p95 at desktop CDP 4x CPU slowdown. No physical Chromebook was tested. Keep this limitation visible in any later review.

#### Cold review changes (2026-11-05)
Review evidence uses Chrome 9950/9951 and HTTP 8755, with bounded commands in Scratch/review_run.py.
finish() now settles conformer glides as well as crystal tests, so Motion off and rapid Save retain the labelled geometry.
Undo captures cut/test state; seed-order labels rebuild with keyboard focus restored. Separate new specimens reserve sphere clearance.
Crystal Sticks exposes bonding with smaller atom radii, an oblique first view and a cut plane through the inspected atom with its neighbours exposed.
The Manual includes every field-guide factual summary, named references and source-specific permissions; tool metadata has the same permission boundaries.
No current OpenStax text, third-party source tables or article illustrations were copied. Public-domain molecular arrays and original finite graphs remain bundled.

Final accessibility follow-up: 44-pixel drawer links; atom deletion retains focus and crystal labels name actual controls. Metal Push counts explicitly refer to the unpushed graph, since bending is illustrative. The cold review retains the strict 600-atom cadence limitation; see codex-review.md for measured evidence.

Final scoped checks confirm crystal drags starting on atoms rotate the viewer, and editing a separate component leaves a finished conformer byte-for-byte unchanged. Relaxation is restricted to the edited component.

#### Refine repair (2026-11-06)
The current repair and its exact item dispositions are in polish.md. Before/after frames, native interaction logs,
all 972 directed bond-label checks, the 92-graph enumeration, source manifests and bounded driver scripts are in
`_scratch/molecule-forge/fix-*`. This repair used Chrome 9920 to 9924 and host 8725. Run from S:/CurioClass-codex.

Matched bond labels now measure the mapped stored model; unfinished bonds explicitly say estimate.
Terminal-branch angular relaxation reaches 180, 120 and 109.5 degrees with Motion on or off.
At a straight centre with branched ends, the entire acyclic branch turns together; cached adjacency avoids repeated
searches. A separate check improved the Si3H4 model's central angle from 166.54 to 179.9995 degrees (179.9949 calm).
Branches containing the reference neighbour are cycles and are not rotated as one piece.
The camera fits the focused component, with a separate projected-bounds fit for short previews.
Undo is visible in Crystal, unsupported seed edits preserve the specimen, and new supported seeds replace it.
Push uses a continuous metal bow, sheet offsets, a salt gap, and a visible held-bond inspection overlay.
The guide's 39 contextual facts, page-specific references, rights boundaries and nine Manual finds are restored,
with narrower facts where a second source did not confirm a clause. See notes.md and fix-fact-sources.json.
Read constructs speech from formula tokens and includes the hint while visible. The manifest remains one fixed line.
Spoken molecule-close and test-result events remain deferred by the Refine settled calls.

Strict 60 fps remains open. At 1366x768 and CDP 4x slowdown, copper improved from 29.58 to 41.18 fps and sodium
from 30.11 to 46.41 fps; graphite measured 60.00 fps. No physical Chromebook was tested. The retained back-bond
culling preserves selected and cut bonds. Do not describe the performance requirement as passed.
The final mechanical audit runs once at fix-audit, with a 2400-second limit, debug 9921 and host 8725.
That audit completed with 255 mechanical leads. Its short-seed null-index error and phone seed-label overlap were
repaired with focused follow-ups; the original audit frames are preserved. See polish.md for the complete triage.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
