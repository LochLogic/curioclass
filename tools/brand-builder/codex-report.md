# Codex report: brand-builder

## Built

Built Brief, Design, Test and Sheet as one offline HTML file, with six clients and an own-business form.
The editor has 24 filled/line symbols, five containers, monograms, scale/rotation, name controls, colors, lockups and history.
Eight raster/contrast tests explain failures and jump to the relevant design control. Brands and fit notes stay local.
The sheet contains three lockups, clear space, minimum size, color ratios, typography and the student's evidence.
No git commits, shared-engine edits or polish round. The report draft began in Scratch after the first bundle.

## Numbers check

Python recomputation of the five Look pairs: 5.1093, 5.4839, 16.5065, 7.1580 and 6.5743, matching the spec's rounding.
All eight palette mids exceed 3:1 on white; the lowest is 4.473:1. See `_scratch/brand-builder/numbers.json`.
Independent 8x shapes give circle 0.9839, filled star 0.9336, Thin ring 0.0000, Regular ring 0.8153, Heavy ring 0.9313.
Thin ring first passes at 32 px. The separately drawn fine wheat differs from the spec: 0.0000 and 104 px, rather than 0.40 and 48 px.
Exact reference paths are absent from the spec, so its illustrative raster scores cannot be reproduced bit for bit.
The tool computes its actual SVGs, never inserts reference scores. Final Thin/Heavy star setups break/hold as intended.
Final heart masks give 2 colored regions to 1 ink region at each surface's print scale; line repair gives 1 to 1.
Color masks isolate painted coverage, avoiding color classification of antialias fringes. A final all-eight run took about 24 ms.
At 3.5:1, a large name with its tagline off passes; enabling the small tagline breaks. Gray and crop thresholds are labeled tool choices.

## Feel check

Best moment: the two-color heart becomes a single ink shape, then a heavier line repairs print and small-size behavior while leaving an icon-coverage tradeoff.
Flattest moment 1: the first one-color failure was mostly words. Added a colored/single-ink comparison with the merged region outlined.
Flattest moment 2: small swatches felt cramped. Replaced them with a full, keyboard-usable palette dialog; the brand changes immediately.
The same identity lands on five textured photos; later clients prioritize different constraints, and the sheet records the designer's choices.
Compared with Beat Lab and Snowy Mail Route. `_scratch/brand-builder/feel-comparison.jpg` places the finished wall beside Beat Lab.
The quiet studio finish follows this spec; the photographs and crisp enlarged pixels carry the visual detail.

## Done when

1. **FAIL:** controls, all 48 symbol/style renders, undo/redo and embedded fonts work, but only Instrument Sans and Fraunces are available. Six required families are missing locally.
2. **PASS:** five independent WCAG pairs match; ratios show one decimal. Palette mids were separately checked.
3. **PASS:** passing and breaking setups exist for all eight tests. Functional matrix plus final isolated-mask and sign-threshold probes are in Scratch.
4. **PASS:** all six client surfaces are first and outlined; every repair route and selected color role is verified in `fix-routes.json`.
5. **PASS:** SVG overlays stay in the recorded photo zones. All six finished images were inspected; the van's tiny plaque was removed with the image tool.
6. **PASS:** at 1366x768 the identity dominates Design; the 4x2 Test wall fills the stage's main area, with the client's tile first.
7. **PASS:** 25 fast changes end at matching state/test revisions, with the last scale value. Token and revision guards reject stale work.
8. **PASS:** sheet minimum size uses the same raster test; clear space uses 25% of measured mark height. A native print proof is one page, black-on-white friendly.
9. **PASS:** exact saved-brand reload, per-client saves, own text and confirmed Clear all were checked; no network requests from the tool.
10. **FAIL:** exact-name searches found no matching client business; both bundled fonts carry SIL OFL URLs. Six specified font files remain unavailable and unverified locally.
11. **FAIL, literal reading:** Design controls fit all required sizes; compact Test has four tiles and arrows. The required large one-column phone wall and client list scroll, so the entire wall cannot also be visible without scrolling.
12. **PASS:** five changes produce one how-to welcome; newly broken sign events speak twice across two failures. Stale queued events have revision guards. First-card and quick-repeat welcome fixes were checked with held clicks.

## Wave lessons

- **Hint and voice PASS:** immediate contextual hints, modal Read, correct close/reset hints, Curio.voice heard checks, separate event lines and idempotent repeated taps. Catalog matches allLines (25 lines).
- **Focus and layout PASS:** source controls survive edits; history stays fixed across sections; transitions and reset retain useful focus. Floating labels reserve a separate caption band.
- **Sizes FAIL for the literal all-content phone rule:** main actions, 44 px buttons, artboard and active Design controls fit; long phone content scrolls in a reserved workspace.
- **No giveaways PASS:** no hidden-answer quiz or automated personality score. Students supply evidence for brief fit.
- **Honest numbers PASS:** reproduction cutoffs and kraft-color assumptions are stated; silhouette and ink-region values come from rendered geometry.
- **Standards PASS:** students develop to a brief, evaluate surfaces, revise and record evidence before a partner critique.
- **Motion off PASS:** no infinite animations; no pacing shortcuts. The complete audit's calm check is clean.
- **Short choices FAIL for the full phone client list:** all symbols and swatches fit their dialogs and compact Brief utilities stay visible. The large phone client chooser remains scrollable.
- **Resize mid-action PASS:** complete audit found no exceptions or stranded disabled controls.
- **First-tap welcome PASS:** card selection speaks Start this brand, own business speaks its form action, and Test gets an actual welcome entry.
- **Unknown shown as unknown PASS:** pending test rows say Testing, not Holds up. Brief fit begins Not yet with empty evidence.
- **One look, one meaning PASS:** ticks and crosses accompany words, and the static key is labeled Test key.
- **Badge truth PASS:** saved ticks reflect stored brands; test badges reflect computed results; brief fit is explicitly the student's judgment.
- **Hint changes back PASS:** closing any dialog restores the current mode/section hint; direct Read checks confirm it.
- **No answer by word copying PASS:** client words are design constraints requiring a choice and evidence, not an answer-card matching exercise.

## Audit leads

One complete audit finished with **210 raw leads**. Original report and 113 frames are preserved in `_scratch/brand-builder/audit`.
Every bullet and the held-click table are answered in `_scratch/brand-builder/audit-disposition.md` (218 bullet rows, including clean results).
Fixed: undersized mode/Read/arrows, 9 px CLIENT label, unnamed inputs, compact Brief utilities, small dialog repair buttons, focus loss, moving history, and repeated-tap speech cuts.
Fixed: phone header/footer workspace bounds, visible phone Print, minimum-size inline wrapping, correct own-dialog setup and current hints.
Fixed after numerical inspection: per-surface ink masks, color fringe artifacts, monogram-only rotation, correct sign font-size threshold, and all eight repair focus targets.
Intentional: a floating caption's box overlaps its padded field outline; values do not collide with it. Native modal dialogs cover and block their background.
Intentional: Print opens native UI, so its headless DOM does not change. A real one-page print proof verifies the action.
Open: phone lists scroll, as described above. The full audit was not repeated; only affected controls, layouts and numerical paths were rechecked.

## Frames looked at

Every required size and mode: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a 375x812 iframe.
Viewed the full run, all 113 audit frames in contact sheets, both bar frames, student/print frames, grayscale, Motion off, keyboard, dialogs and long-name extremes.
Viewed focused fixes in post-frames, mask-frames, ui-frames, route-frames and post-phone. Latest phone Design has artboard bottom 391 and controls bottom 751 in an 812 px viewport.
All final focused browser runs reported zero console errors, warnings or exceptions. Sound as the first held tap leaves the voice log empty.

## Art made

Two new images and one image edit with the built-in image tool: phone, studio still life and the cleaned van. Three original photos remain unchanged.
Six WebP images total: **307.1 KiB**. Final offline bundle: **662760 bytes / 647.2 KiB**, below 2 MB.
Van redrawn once to remove the background plaque; every finished WebP was inspected at final size. Prompts, provenance and logo zones are in art/prompts.json.

## Art still to paint

None. No people, faces or body parts were generated. No audio was recorded; the 25-line hs-narrator catalog uses browser speech fallback.

## Engine changes wanted

None. Shared kit and audit code were left untouched.

## Left open

- Supply local SIL OFL latin-subset WOFF2 files for Montserrat, Quicksand, Playfair Display, Arvo, Bebas Neue and Pacifico, then enable their real weights.
- Resolve the literal no-scroll requirement against the explicitly required large one-column phone wall. The build uses the latter and keeps actions visible.
- Cold review is still pending. This is a built draft, with no claim of a clean full audit after fixes.
- All owned Chrome processes and servers are closed; host.html is removed. Open-question choices are recorded in handoff.md: storefront sign for Willowmere, and Print retained.
