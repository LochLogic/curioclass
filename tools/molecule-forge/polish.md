# Polish: molecule-forge (Codex fix, round 1)

Repair in `S:\CurioClass-codex`, 2026-11-06. Only this tool and `_scratch/molecule-forge/` were written.
`refine.md` and `refine/` were not edited. No commits, branch changes, engine changes, registrations or uploads.
The pre-existing spec working-tree difference was left alone. Chrome: 9920, 9922, 9923, 9924; final audit: 9921. Host: 8725.
Evidence paths below are relative to `_scratch/molecule-forge/`. All FIXED claims have observed DOM numbers, frames or logged events.

## Blocker

1. **FIXED. Bond lengths.** Reproduced H2 62 vs 74 pm, benzene 132/152 vs 139 pm, O2 115 vs 123 pm and peroxide 132 vs 145 pm in `before-bonds.json` and its frame. Labels now use the mapped stored coordinates on a match and say “model”; unfinished bonds visibly say “estimate”. `fix-verification.json` checks **972 directed bond readouts across all 72 recognized graphs: zero failures**. `after-bonds.json` gives the same examples after repair. The Manual explains benzene's equal ring bonds and both Kekule drawings.
2. **FIXED. Silicon no-grow falsehood.** Reproduced Si+C and Si+N false molecule claims in `before-seeds.json`. The fallback now states only which seeds this instrument supports, making no claim that unsupported silicon substances are molecules. `after-seeds.json` and the 90 seed cases in `fix-verification.json` prove the new wording. No eighth crystal was added.

## Should fix

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

## Polish accepted

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

## Settled calls

- Applied all calls: spoken close names and Push/Current results remain deferred to the collective voice pass; existing hint/Read behavior repaired now.
- The silicon fix is honest wording, not a new material. Nine finds and plurals are treated as should-fix items.
- Required generated-illustration credit remains. No checklist, “found” marks, goal, score, quiz, forced finish or kit header was added.
- Full-screen well, inert modal drawers, Hill order, special cards and source art are retained. Open questions were not implemented.

## Cheats tried

- There is no score or check to pass. Tried all 90 one/two-atom seed combinations, including unsupported Si pairs and Na+Na; unsupported recipes stay unsupported without false claims.
- Tried the seed-wipe pattern in four material families; every specimen survived and Undo restored its original seed.
- Exercised every matched graph's directed bond readout, then an unmatched oxygen pair; no silent radius estimate is presented as a model distance.
- Recomputed every legal one-to-three C/N/O graph independently, including all unnamed examples; no novelty or “wrong” claim appears.
- Native keyboard, held taps, real drags, both Motion states, view toggles, angle targets and repeated identical syncs all retain valid state.

## Voice walk

- At a held-click, two-second pace: H, H, Read produces no late how line, then one Read of water, filled spots and the selected oxygen's angle.
- Side path: Motion speaks the tray hint once and leaves it visible; Read speaks that current hint again. Adding H hides it. Keyboard and drag adds also hide it.
- The log records playback requests in muted Chrome, including Read cutting the how line by request. No new recording was made.
- `voice/lines.json` equals `allLines()`: one fixed line, “Tap an atom in the tray to snap it on.” Dynamic Read is separate.

## The real material

- Retained PubChem explicit graphs and stored coordinates: 32 illustrated plus 40 also-known entries, fetched 2026-11-05, federal numerical records public domain; all bundled. No new conformer data sampled.
- Retained original finite lattice arrays: seven materials, original generated graphs checked by coordination and counts. Referenced OpenStax 2019 CC BY 4.0 and CRC factual constants; no copied tables or images.
- Restored contextual facts: **all 39 page-specific facts, URLs, permission boundaries, check date (2026-11-06) and sampling description** are in `fix-fact-sources.json`, the in-tool Manual, guide pages and `tool.draft.json`.
- Online material was used only for fact checks and original short summaries. Government raw responses and their actual fetch failures/rights exclusions are preserved under `data/fix-facts/` and `fix-fetch-manifest.json`. No fetched outside prose, art or restrictive annotation dataset enters the bundle. Some browser-readable sources return 403 to a download; that is recorded, not treated as retrieved data.
- OpenStax official current licence was checked at https://openstax.org/books/chemistry-2e/pages/preface. The current web edition is CC BY-NC-SA 4.0; the prior archived reference is CC BY 4.0. Link labels explicitly distinguish them.
- The two biological isomers' boiling points, original named fact sources, radii, Jmol colours and all 40 illustrations retain their credit boundaries. No data or topic was added outside the brief.

## Engine changes wanted

None. The performance gap is in the tool renderer, not a request to change the shared kit.

## Audit

The required audit ran **once**, within its 2400-second limit, with the full walk and resize stress enabled: `fix-audit/audit.md`. It completed with **255 mechanical leads**. It was started before the last scoped corrections, so its original snapshots intentionally retain the failures below; this is not a claim of a clean final audit or an exit PASS.

- **Short seed exception: FIXED.** Three state groups hit a null frame-index lookup in short Crystal windows. Reproduced by the audit, corrected the Forge-only index assumption, then re-shot the C=C seed at **680×425 and 800×500**, both with zero errors. `fix-seed-check-frames/`, `fix-final-leads-frames/`, `seed-680.json`, `seed-800.json`.
- **Phone inspector obstruction: FIXED.** The retained specimen's seed-bond label covered the ATOM input in salt, fractured salt and the preserved-specimen state. Grown specimens now hide the ungrown seed control. Final 375×812 recheck reports **9 of 9 inspector sample points visible**, no seed label and scroll width **375**; `phone-salt-inspector.json` and `fix-phone-ready-frames/phone-salt-inspector.png`. The first targeted phone retry collided with the audit's own host and failed to load its child; that failed artifact is retained, and the successful retry ran only after the audit's server closed. The Scratch host runner now refuses an occupied port.
- **218 canvas/control overlap rows:** the full-screen canvas is the viewing well behind the controls, as explicitly settled in Refine. These are expected compositing, not clipped controls. All 43 audit frames were inspected through four indexed contact sheets and the affected phone frame at full size.
- **Hidden hint and hidden main keep regions:** intended after a real atom add or while a modal drawer makes the bench inert. Native logs and frames verify those states. No welcome, goal or extra instruction panel was added to satisfy this lesson-shaped lead.
- **Guide Close/header/label boxes:** padded block rectangles intersect, but the actual title and label glyphs do not run under Close in either named frame. The guide's name and fact remain visible at 680×425.
- **Two source links below the guide fold:** citations in a scrollable reference page, not hidden play choices. Turn, Load, the name and the fact remain in view; sources remain reachable by scrolling and keyboard.
- **Quick bench toggle cuts the one hint:** expected `V.hush()` on a mode change, allowed by BASELINE 16. The hint stays visible until an atom is added, and Read repeats it. No automatic replay loop was added. Five held clicks and the other quick-tap rows are clean.
- **Resize and calm:** completed clean, no exceptions or stuck disabled controls. `fix-audit-triage.json` groups every reported lead. Original audit output was not rewritten.


## Frames and checks

- Before: `fix-before-frames/` (all 16 frames inspected), plus stored numbers. After: `fix-after-frames/`, `fix-layout-frames/`, `fix-crystal-frames/`, `fix-native-frames/`, `fix-last-frames/`, `fix-seal-frames/`, `fix-seal2-frames/`, `fix-final-leads-frames/`, `fix-phone-ready-frames/` and `fix-nonleaf-after-frames/`.
- Early intermediate frames exposed an undersized preview tray, weak hold highlights and five-pixel phone overflow; these were corrected and targeted frames repeated. Superseded frames are evidence, not claimed final layouts.
- All seven STANDARDS desktop sizes, both modes at 1366×768, 680×425 and 800×500 previews, Motion off, native keys and a hosted 375×812 iframe were covered. Phone scroll width is now **375**, matching its viewport.
- The local check finds zero lesson-creep words in src.html and zero em dashes in changed public source/notes/voice/metadata. Report words such as “score” describe the excluded lesson conventions only.
- Final bundle: about **1110 KB**. The native instrument run has **zero console exceptions and zero external network requests**. A parent-host favicon 404 in an earlier run is distinct from the offline bundle and was corrected in the Scratch server before the final check.
- All browser and server processes started by these bounded drivers are closed by their driver cleanup. The final resource check confirms every owned debug and host port is closed (`fix-resource-check.json`).

## Left open

- Should fix 11 remains open: copper and sodium do not meet strict 60 fps at 4× slowdown. Done when 8 therefore remains FAIL; no exit-pass claim is made.
- The full audit was not repeated after its focused corrections and the broader branch-angle check. The preserved audit contains resolved leads; the next integrator should audit the final bundle afresh, as planned by the handoff.
- The session was unattended. Where wording or layout needed a choice, the Curiosity brief and Refine's stated lean won. Deferred spoken events and spec open questions remain for their designated pass.

## Instrument comparison

The repaired bench retains the instrument density, direct controls and live readouts seen in the Beat Lab reference. The object remains the interface, the guide remains freely browsable, and play has no assigned path or finish. This repair did not rerun three review lenses or claim a new independent ten-minute short-test verdict.

| Molecule Forge | Reference: Beat Lab |
|---|---|
| ![Molecule Forge](../../_scratch/molecule-forge/fix-native-frames/water-native.png) | ![Beat Lab](../../_scratch/molecule-forge/fix-seal2-frames/reference-beat-lab.png) |
