# Living Earth build handoff

## Structure
The first build's spherical geometry, great-circle sections, station intersection, input handling, drum and family marks remain in src.html. The second build adds a WebGL material surface with a bounded canvas fallback, full M5.5 catalogue, geography, city search, model plate readouts and Rewind. material.json is the only data file and is embedded by bundle_tool.py.

## Reproduce the real material
All second-build raw downloads are in _scratch/living-earth/data/build2/ with source URL, date, checksum and download duration beside them. build2_fetch.py and the sources/more/taup/spotcheck batch scripts retrieve them with limits. build2_plates.py resolves the original GPML and finite rotation circuit. build2_pack.py produces the compressed material and code-shaded relief PNG. The final texture conversion is build2_texture72.py, texture72.html and build2-texture72.json, using Chrome at WebP quality 0.72; its saved data URL is data/build2/texture-webp.json. Run pack again to embed that result. The packer preserves this cached texture when present. build2_patch.py preserves the first source and assembles build2_renderer.js and build2_instruments.js with its substitutions. Editing src.html directly is fine; do not re-run assembly afterward without carrying edits back to its Scratch inputs.

## Numerical conventions
Spherical Earth radius 6371 km. Dates are UTC days; the selected year includes its whole calendar year. Catalogue playback progresses continuously; Motion off updates in year steps. Local pin history is independent of current filters. Quake depths stay true in sections; ETOPO surface relief alone is x20.
TauP-calculated iasp91 times replace the first build's uncalibrated shell table. PREM paths replace its iasp91 paths. They are numerical model outputs, not bundled software. Stations remain a surface-focus idealization with synthetic traces and shallow real catalogue epicentres.
Merdith finite rotations are recursively composed relative to plate 000, sampled each 5 Ma, then slerped in the browser. Present plate polygons are simplified resolved topologies. Some small polygons reference absent archive features; those places remain unknown. The manifest records every omitted reference and join. The model's motion frame and hotspot exclusion must remain visible.

## Sensitivity
Real earthquakes are presented as observations, without tolls, gore, disaster photography or ratings. A local event count is not hazard guidance. No location or student data is transmitted.

## Validation
Second-build evidence is prefixed build2 in Scratch. build2-numbers-final.json has 38 numerical probes; data/build2/spot-checks.json has ten fresh ComCat checks. build2-performance-final contains the 4x CPU pointer profile and playback measurement. build2-explore records two ten-minute builder walks. build2-audit/audit.md is the single full audit, with build2-audit-triage.json recording its dispositions. build2-after-audit and build2-verified-targets contain the affected layout follow-ups. build2-keyboard-last-retry contains the last native keyboard inspection. build2-final-manifest.json freezes hashes, sizes and evidence paths. codex-report.md records results and limitations; codex-report-1.md is preserved unchanged.

## Engine changes wanted
Log only, not implemented: `kit/curio.js`, `showMotion()`, could offer plain `Motion` and `Motion off` text without the emoji for engraved instrument panels. This is the Refine's deferred shared-kit request. Kit, scripts, docs and other tools were not edited; no commits or deployment were made.

## Cold review changes, 2026-11-05
The review preserves the scientific pack and renderer. Station Clear and marker edits now remove stale labels and revealed records, and clearing during a pointer drag is guarded. The trace has a five-minute ruler and a taller compact layout. Phone panels retain an unobscured globe, working Close controls and readable measurement plots.
Read expands section, station and wave units into sentences, announces out-of-filter selections and stops on instrument switches. Keyboard centre placement keeps the result announcement. A new Wave source waits for Fire. The canvas fallback now honors Relief off.
Independent evidence uses the review-* and cold-* prefixes in Scratch: ten fresh ComCat checks, primary licence responses, numerical before/after probes, native range endpoints, voice logs, size frames and performance. The existing build2 evidence is historical builder evidence. Do not rerun build2 assembly over the reviewed source.

City search ranks an exact town name before partial matches: Lima now selects Lima rather than the earlier substring match Quelimane. Accent folding and the limited offline gazetteer remain.

Rewind fossil regions now have a solid Glossopteris outline and dashed Mesosaurus outline, with the latter drawn above broad regions. This retains the existing schematic data while adding a non-colour key.

## Refine fixes, round 1, 2026-11-05
The original `material.json` pack is unchanged. Present-day motion now removes the surface-area-weighted shared rotation from the original 0-5 Ma angular velocities. `_scratch/living-earth/fix_nnr.js` reproduces the correction by integrating `(I - r r^T) omega` over a cosine-weighted 5 degree grid of the model's own polygons, covering 99.811 percent of the sphere. `fix-independent-numbers.json` independently checks all five cities against the Refine's ITRF2014 comparison, with maximum errors 0.28 cm/year and 5.45 degrees. This is still a model average, not GPS. EDGE MOTION is the normal component of relative motion at the nearest plate edge; the shared rotation cancels in that difference. Rewind still uses the original finite rotations. Do not rerun the older source assembly over these changes.

Stations keeps independent P/S placement flags and separate trace handles; S starts at the end of the 26-minute ruler. No inferred circle or intersection uses an unplaced marker. Catalog records dock above the active instrument; offsets remain measurements with no fit verdict. The sea-floor profile has its own strip and scale derived from its actual sampled range; its vertical exaggeration is exactly twenty relative to horizontal kilometres. Quake axes remain 1:1. Wave's ring, shadow arc and readouts use the bundled direct-branch edges (P 98, S 99, far-side P 140 degrees) and a 1560 second window. The Manual explains the difference from the usual 104 degree textbook shadow and the omitted diffraction.

Volcanoes are one WebGL triangle point layer, with one batched canvas path as the fallback. Immutable shader locations and motion-arrow vectors are cached. The same paired 4x CPU benchmark at 1366x768 changes the volcano median frame interval from 33.4 ms to 16.7 ms. Occasional slower frames remain; a sustained 60 fps hardware claim is not established. The NNR arrows are drawn above the quake layer at several sites near each large plate's edge.

The first native Play speaks only `Drag to spin.`; the first drag speaks only `Press play.`; an instrument switch stays silent. Both lines have validity checks and match `voice/lines.json`. Read uses plain speech. Compact layouts retain names, depth labels and a 40 px drum; phone evidence uses a 375x812 iframe on host port 8715. Rewind now plays both directions, and calm Wave advances by whole minutes at the same pace as full motion. The family maker's plate, Manual drawer and power panel remain; there is no lesson flow, score, goal or finish.

All fix scripts, before/after frames, native-input probes, source metadata and the final audit are under `_scratch/living-earth/` with the `fix-` prefix. `polish.md` is the item-by-item disposition. `refine.md` and its review folder were not changed.
