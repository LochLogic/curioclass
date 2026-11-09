# Microscope Bench build handoff

`src.html` contains the physical instrument, canvas renderer, input handling, preparation controls, Manual and local sketchbook. `material.json` is the source catalog, asset sampling and physical slide arrangement, embedded through the bundler's JSON token. `art/*.webp` are licensed photographic crops, individually inlined. `kit:curio` supplies shared Motion, Sound and Read behaviour only. Rebundle with `CURIO_DRAFT=1` and `python scripts/bundle_tool.py microscope-bench`.

The photographic source files, bounded download scripts, PDF extraction, accepted crop list and Chrome WebP packer are under `_scratch/microscope-bench/`. `curate2.py`, `pack2.py`, `catalog2.py` reproduce the photographic package. The raw source hashes, crop coordinates, resampling, original and packed µm/pixel, scale evidence, credit and licence are recorded in `art/manifest.json`. Never infer camera scale from objective power alone. `codex-report-1.md` is retained unchanged.

The mounted photograph is never repainted. Source contrast and sampling limit what can be seen. The pond is an explicit assemblage; only a photographed ciliate follows a computed swimming path. The colony switches/blends nine real registered focal planes. Other focus and preparation effects are bounded optical models. Finite source coverage is visible in the glass locator.

`window.__tool` exposes state, material, decoded photos and instrument functions for verification. Test helpers use Chrome 9980–9987, muted audio, and an isolated local host on 8785. The build makes no shared-engine edits, commits or branch operations or publishing actions. Its own sketchbook adapter remains necessary because this checkout's kit has no save/load API.

Deferred material: defensibly scaled salt/sugar/feather and methylene-blue cheek preparation; recorded ciliary motion and resolved hair cuticle detail; broader contiguous biological fields. These are absent from the tray rather than fabricated or presented as empty placeholders. A physical Chromebook benchmark remains distinct from CPU-throttled desktop testing.

## Cold review repairs

The field guide now refuses identification through a fully closed iris and dismisses an observation when an optical control or stage motion changes its view. Sand is labelled as source reflected light on the instrument. Photographic credits are regenerated from the canonical source catalog, preserving author spelling, the measured 64-pixel low-power bar and DOI/journal attribution.

Calibration is a nonmodal sheet beside the eyepiece, with live stage movement available. Opening another drawer or changing the objective closes it; Escape closes it too. Its own button toggles it. Keep the scales visible when changing this layout. Review checks use Chrome 9950 and 9953; the single audit uses 9951 and host 8755. Evidence is in Scratch under review-*.

Close-to-stage workflows use `closeToView` and a transient `focusAfterClose` destination. Keep that destination in the dialog's close listener: restoring its ordinary trigger there would steal focus after keyboard selection and make Enter reopen the tray instead of mounting the specimen. Preparation actions also refresh the status from the current mount. Eyepiece source labels are inset far enough to stay inside the circular clip at small previews.

## Sensitivity

Human hair, cheek cells and a published malaria blood sample are shown at microscopic scale. Retain the sample's documented disease context without inferring a student's health, ancestry or identity. No patient image or clinical diagnosis is presented. Source authors' names and diacritics must remain accurate.

## Claude Refine fix passes, 2026-11-06

Round 1 is preserved in polish-1.md. Round 2 preserves its instrument repairs and adds two distinct transmitted-light ciliates from Kodama et al. Figure 1a. The pond has six unique cutouts, each placed once. No repeated biological stamps remain. The extra cultures are an explicit assemblage, with original source scales and transparent annotation masks.

The new cheek field is Daliasalloum's CC BY 4.0 methylene-blue photograph. Nuclei are visible. Its 0.22 um/pixel scale is explicitly inferred from a roughly 250-pixel cell edge and a 55 um reference, cross-checked with Prasad et al. and Romeo et al. The on-instrument caption says SCALE APPROXIMATE. Use the measured-bar blood fields for precision micrometry. Source-glass removal changes alpha only; no RGB colour is invented.

Defocus now downsamples and reconstructs an optical layer instead of applying a software Gaussian filter on every pan. The logarithmic field-scaled focus response and hair depth gradient remain. Final proxy timing and unresolved gate items are in polish.md; no physical Chromebook benchmark is claimed.

Reproduce packing with Scratch r2_material.py, r2_metadata.py, r2_trim.py, r2_cheek_mask.py and r2_handoff.py, in that order, r2_licences.py, then bundle. Use the retained raw files and r2-gather.json. r2-cuts.json and art/manifest.json record the crops, masks, licences, scale inference and hashes. Chrome 9920-9927 and host 8725 belong to this fix session.

Still open: broad contiguous blood, root and onion fields; high-power wing hairs and leaf detail; colour iodine with defensible scale. The broader CC0 root candidates returned 403/429 and the origin copy returned 410. The colour iodine candidate has an uncalibrated reticle, not a physical scale. These were left unchanged rather than assigned invented dimensions. The curriculum map and omitted tray topics remain unchanged, following the brief's settled scope.

Current OpenStax reference labels were corrected to CC BY-NC-SA 4.0 after checking its 2026 page footer. No OpenStax text or images are reproduced; the photo assets remain PD or CC BY.

## Engine changes wanted

None. No shared-engine changes, commits, outreach, upload or publication. The incomplete real-material blocker still prevents claiming a fresh short-test pass.
