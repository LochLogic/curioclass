# Molecule Forge build handoff

## Source map
src.html holds the bench UI, graph operations, element-labelled isomorphism, local geometry relaxation, canvas rendering, drawers and storage.
material.json and also-known.json pack explicit PubChem atoms, bonds and coordinates. crystals.json contains generated lattice graphs.
art contains forty cropped, coordinated real-material paintings. All are bundled in molecule-forge.html.
Scratch holds reproducible gathering, lattice, packing and validation scripts, raw source records, shots and audit evidence.

## Tricky parts
The focused connected component controls naming and shelf saves; the well may hold several structures. Matching ignores bond order only when every spot is filled.
PubChem coordinate models are not measured geometry. Interior means actual full coordination in the finite sample, rather than an unverified fixed count.
The Manual and field guide are overlays with focus containment. Power controls belong to the instrument.

## Engine changes wanted
None. Shared kit, scripts and other tools were read only.

## Next build considerations
See the final report for exact validation limits and retained approximations. No polish round or commit was started.

## Rebuild and evidence
From the repository root, set CURIO_DRAFT=1 for the local process and run scripts/bundle_tool.py molecule-forge with a 120-second subprocess timeout. This packs the existing data and all forty WebPs without fetching anything.
Scratch/closeout-prep.py demonstrates bounded bundling, JavaScript parsing, independent material checks and focused native-key frames. It uses HTTP 8795 and Chrome 9990, then closes its own processes.
Raw PubChem records are in Scratch/data. prepare.py and gather-extra.py pack the two molecule arrays; final-facts.py applies checked facts and computed descriptions; fix-fallback.py and allene-fallback.py apply the labelled coordinate exceptions. crystals.py generates finite lattice graphs. Crop bounds, originals and crop/pack scripts preserve the image provenance.
validation-manifest.json hashes the final code, data, metadata and bundle. final-native.json, final-controller.json, material-check.txt, closeout-log.txt and audit/audit.md preserve the checks and their limits. The full audit ran once; later corrections have focused checks.
The strict 60 fps stress target remains unmet: graphite has a 16.7 ms median and 33.4 ms p95 at desktop CDP 4x CPU slowdown. No physical Chromebook was tested. Keep this limitation visible in any later review.

## Cold review changes (2026-11-05)
Review evidence uses Chrome 9950/9951 and HTTP 8755, with bounded commands in Scratch/review_run.py.
finish() now settles conformer glides as well as crystal tests, so Motion off and rapid Save retain the labelled geometry.
Undo captures cut/test state; seed-order labels rebuild with keyboard focus restored. Separate new specimens reserve sphere clearance.
Crystal Sticks exposes bonding with smaller atom radii, an oblique first view and a cut plane through the inspected atom with its neighbours exposed.
The Manual includes every field-guide factual summary, named references and source-specific permissions; tool metadata has the same permission boundaries.
No current OpenStax text, third-party source tables or article illustrations were copied. Public-domain molecular arrays and original finite graphs remain bundled.

Final accessibility follow-up: 44-pixel drawer links; atom deletion retains focus and crystal labels name actual controls. Metal Push counts explicitly refer to the unpushed graph, since bending is illustrative. The cold review retains the strict 600-atom cadence limitation; see codex-review.md for measured evidence.

Final scoped checks confirm crystal drags starting on atoms rotate the viewer, and editing a separate component leaves a finished conformer byte-for-byte unchanged. Relaxation is restricted to the edited component.

## Refine repair (2026-11-06)
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
