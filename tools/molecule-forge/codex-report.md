# Codex report: molecule-forge (Curiosity No. 12)

## Built

Full-screen molecular model kit and crystal specimen viewer, with the engraved plate, lower-left Manual, and Motion, Sound and Read on the instrument power panel.
Forge has nine atoms, explicit bonding spots, single/double/triple bonds, rings, 3D rotation, relative space-filling spheres, a turntable, 30-edit Undo and a twelve-specimen local shelf.
Crystal has seven generated lattice graphs, growth, an interior cut, an atom-number inspector, and qualitative Push and Current tests. The field guide has all 39 pages, open in any order.
The final offline bundle is **1,110,569 bytes**, about **1.11 MB**, below the 2 MB goal. No commit, deployment or polish round. Shared files and spec.md were read only; the existing spec diff was left intact.
All authoring, sources, scripts, profiles and evidence are inside the two authorized directories. The report was staged in Scratch and copied here last to honor the explicit stop instruction.

## The real material

- **Molecular graphs:** 32 guide entries and 40 additional names, complete explicit hydrogen/bond arrays from [PubChem PUG REST](https://pubchem.ncbi.nlm.nih.gov/rest/pug/). Public-domain numerical molecular records; fetched 2026-11-05. No sampling. Raw JSON is in `_scratch/molecule-forge/data/`; per-entry URLs are packed in material.json.
- **Coordinates:** 30 supplied 3D computed conformers in the illustrated molecular guide, not measured structures. The fetched hydrogen and silane records only supplied 2D coordinates: H2 uses the specified 74 pm reference model, and SiH4 uses a labelled ideal tetrahedron with an estimated 142 pm Si-H distance. No flat 2D silane masquerades as a 3D conformer. Of the forty additional names, 39 supplied 3D records; allene uses a labelled ideal model with perpendicular terminal planes, derived from the chapter 8 bonding rules.
- **Valence and geometry:** independently written code following OpenStax Chemistry 2e, 7.6 and chapter 8. The [2019 licence page](https://ic.arc.losrios.edu/~paynem/textbook_os_2e/chemistry_2e_intro.pdf) states CC BY 4.0; original chapter 7, 8 and 10 PDFs were preserved. Authors: Flowers, Theopold, Langley and Robinson, Rice University. The current web edition instead lists CC BY-NC-SA, so current prose and illustrations were not copied.
- **Crystal data:** our own finite graph generators using the specified diamond/tetrahedral, honeycomb AB, rock-salt, FCC, BCC and bridged-silica rules. Counts: diamond 525, graphite 600, silicon 525, salt 392, copper 561, sodium 559, silica 147 Si + 220 O. [OpenStax 2019 chapter 10](https://ic.arc.losrios.edu/~paynem/textbook_os_2e/openstax_2e_ch10.pdf), CC BY 4.0, and the named CRC 97th-edition lattice parameters supply factual structure/spacings. No source figures or proprietary tables were reproduced.
- **Radii and colours:** prescribed factual values from Cordero 2008, Bondi 1964, Shannon 1976, CRC and [Jmol CPK](https://jmol.sourceforge.net/jscolors/). Covalent radius estimates carry a `~` label; they are distinguished from lengths in stored conformers. Salt uses ionic sphere radii.
- **Context facts:** retained only checked short facts, in original wording, with linked sources on each guide page. Sources include NASA, USGS, OSHA/NIOSH, ESA, Wöhler's public-domain 1828 text, Royal Institution, Science Museum, PubChem, EPA and FDA. Scientific facts were paraphrased; outside prose, photographs and annotated data tables were not republished. `fact-provenance.json` records each claim, URL, date and disposition. Other anecdotes were replaced by independently computed atom/bond counts.
- **Art:** generated for this build with OpenAI gpt-image. Forty final paintings, no people, with two object-specific redraws. Atomic geometry, crystal patterns, bonds, pegs, protractor, contacts and battery are drawn in code, never painted into a dataset image.

Gathering used bounded requests, stayed below the 45-minute active gathering allowance, and retained raw downloads plus packing scripts. The final tool makes no automatic network requests.

## Break the instrument

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

## Voice walk

Knowing-guide is the declared voice; this build uses the kit's browser-speech fallback and synthesized effects, with no audio recordings.
Held clicks at two-second intervals produce the first-run hint once. Further additions and material tests do not automatically narrate. Read speaks the current formula, identity, spots, selected atom/angle and result. Opening a drawer first does not speak an instruction naming its inert tray.
The controlling Curiosity brief's “then only when Read is pressed” wins over the spec's automatic molecule-name and test-result narration. This conflict was stated before building. Sound off and Read were exercised; the audit's repeated and quick-tap voice checks finished cleanly.

## Short test

Build-side exploration used the unread first encounter and more than ten minutes of manually chosen instrument states, visual inspection and automated interaction sequences. This is an agent assessment through grade-7 and adult lenses, not a study with children.

| Question | Assessment |
|---|---|
| Would a kid open it unassigned? | PASS: the waiting oxygen has visible attachment ports, and two taps immediately change its shape and name. |
| Would an adult play for fun? | PASS: isomers, unfamiliar filled graphs, resonance drawings, caffeine and different lattice coordination invite independent investigations. |
| Is the real thing the interface? | PASS: the atom graph and the generated lattice are the working surface. Pictures are only field-guide context. |
| Does it work without a score or finish? | PASS: nothing unlocks, collects a mark or ends the session. |

Best moment: filling water, then watching another pair of hydrogens become their own specimen. Adult depth: the same carbon becomes a four-connected network or three-connected sheets, and the test responses follow that distinction.
Frame comparison: [Molecule Forge beside Elements Inspector](../../_scratch/molecule-forge/frame-comparison.png). Beat Lab, Elements Inspector, Span and Spire and Pocket Universe were opened and inspected; their sources and family marks informed this build.

## Lesson creep check

The requested whole-word scan of src.html and the voice lines finds no score, points, level, goal, sticker, badge, correct, wrong, try again, complete or well done. No em dash in the tool source. Capacity and atom readouts are physical budgets, not progress targets.

## Done when

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

## Audit leads

The single required audit finished with exit 0 and 231 raw leads. It is preserved in Scratch and is **not presented as a zero-lead audit**.
Most leads are intentional: a full-size canvas lies behind its controls and readouts; the first-run hint intentionally disappears; a modal drawer makes the covered bench inert; reference books scroll; the one-time hint is not a per-mode welcome.
Actual fixes: the phone engraving was shortened, fixed H bonds became readouts rather than inert buttons, compact diagrams moved clear of bond readouts, source links gained 44 px targets, guide Turn/Load stay outside the scrolling body, and the mid-height tray uses a 3×3 layout with 44+ px targets.
The audit's resize lead involving a hydrogen bond control is resolved by removing that non-steppable button. Drawer title/Close boxes shared bounding rectangles without text collision; the guide title now reserves space for Close.
The full audit was not rerun. All affected areas received targeted post-fix frames and input tests. The held-click main-control walk, Motion-off check, repeated-click checks and quick-tap checks finished without runtime/focus errors.

## Frames looked at

All required sizes, both bench positions, storage/keyboard/drag paths, Motion off, grayscale spheres, caffeine, salt cuts, guide and Manual. The 29 audit frames were inspected in four contact sheets. Early failed syntax frames were inspected, fixed and superseded.
Additional final frames confirm the compact well, phone salt and turntable, conventional guide labels, analytic silane, reachable guide actions and corrected art. Every final painting was inspected in the WebP contact sheet and the two replacement originals.

## Art made

40 final WebP pictures, 557,506 bytes in total, plus the code-drawn working surface. One 5×8 atlas and two corrected-object redraws. Actual tile edges were measured and inset to remove adjacent-picture strips. Raw paintings, crop bounds, source atlas and scripts are preserved.
`art.py --rekey` was attempted but this Python lacks NumPy/Pillow. Native image cropping plus Chrome canvas produced the WebP assets without installing software or changing shared scripts.

## Engine changes wanted

None. The graph, geometry and lattice code stays local to this tool. The shared kit supplies settings and voice behavior.

## Left open

- Unattended choices follow the brief: no built-here guide marks; keep the sodium metal page; no automatic names or test narration after the first hint.
- The brief's verification rule superseded unconfirmed contextual anecdotes. Twenty-two molecule pages currently use computed structural descriptions; the full 39-page illustrated guide and all molecular graphs remain present. The exact FDA coffee range was not retained without a second independent check, although caffeine's coffee/tea context remains.
- PubChem supplied no 3D records for H2 or silane in this gathering. Their explicitly labelled analytic/reference models, and allene’s perpendicular-plane model, are intentional fallbacks. Stored conformers are computed, not advertised as measured.
- Finite specimens expose their actual graph boundaries. Graphite's 150-atom sheet crop admits a matching on all 600 atoms, and diamond has 363 fully coordinated atoms; these actual counts replace unverified illustrative interior/matching counts in the old prose.
- This build does not supply a teacher plan or establish the anchor lesson-card takeover. It is the requested Curiosity instrument.
- The strict 600-atom frame-budget target remains open: median cadence is about 60 fps, with occasional 33.4 ms frames at 4× slowdown. Several bounded optimizations were made; the brief’s single-issue time limit ends further optimization in this build. Hardware performance still merits a physical school Chromebook run. Browser narration uses available system voices rather than a newly recorded knowing-guide clip bank.

All Chrome and host processes started for this build were closed. No tools/molecule-forge/host.html was created. Evidence, source records and replay scripts remain in `_scratch/molecule-forge/`.
