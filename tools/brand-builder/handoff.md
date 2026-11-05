# Brand Builder build handoff

## Structure

`src.html` starts from the kit starter and includes the 9-12 kit theme, overridden with the spec's light studio palette.
CSS lays out the studio at real available sizes. Content tables, SVG rendering, edit history, raster tests, dialogs,
mode renderers and Curio.voice wiring follow in that order. `window.__tool` exposes state and test hooks.
`tool.draft.json` remains a built draft. No commits or polish round were made.

## Art and placement

The storefront and shirt FLUX photos remain unchanged. The van photo was edited with OpenAI gpt-image to remove a tiny
background plaque. Two new OpenAI gpt-image photos were made during the build: phone and studio. Cold review redrew the bag.
The studio still life introduces Brief; the other five photos receive the actual SVG identity.
`art/prompts.json` preserves the original asset records and records percentage logo zones. Raw new PNGs are under `art/raw`.
The prior van WebP is preserved in Scratch, and its source is retained in the van asset's previous_source field.
The generated phone screen is at x31%, y16%, width38%, height61%. Photos and overlays share an SVG coordinate system.
Browser tab, circle crop, newspaper, symbols and lockups are drawn in code.

## Tests and assumptions

Tests rasterize the same SVG that students edit. The 256 px and 16 px alpha masks use a half-coverage threshold and
bilinear enlargement for intersection over union. The minimum-size search checks 16 through 256 px in 8 px steps.
No passing size through 256 is reported as such. The source's illustrative reference scores are not hardcoded.
Contrast uses WCAG relative luminance; gray conversions preserve luminance. The phone coverage excludes its background.
The avatar raster includes text and embedded fonts. One-color masks isolate each original ink color's painted coverage, then count connected
regions in the union, with 8-neighbor contact at each surface's actual simulated mark-grid print width.
Transparent holes are negative space; deliberately painted white regions count as colors.
This is a raster approximation of subpixel merging, rather than a physical ink-spread model.
Latest-change guards combine a 150 ms debounce, revision number and run token.

## Local storage and focus

Each brief is saved in `brand-builder-brands` with try/catch. No network requests or cross-device transfer.
Own-business fields and fit notes are escaped on rendering. Reset and Clear all ask first.
Mode controls persist in the DOM; editing does not rebuild the source control. Dialogs restore focus without scrolling.
Symbol and palette grids are dialogs so every choice has a usable target even in the smallest preview.
The compact Brief view exposes own-business and clear controls in the panel; the phone header stays visible while scrolling.
History is pinned across desktop panel sections. Same-mode/client taps are idempotent so they do not cut narration.
Surface dialogs expose Read inside the native modal; short previews keep the photo, explanation and repair action side by side.
Undo and redo preserve a focusable endpoint using aria-disabled after the last available step.

## Open questions resolved

- Willowmere uses the storefront sign. No scrubs surface was added, matching the spec's current leaning.
- Print sheet stays as a design deliverable. It does not transfer a brand between devices.

## Cold review changes (2026-11-03)

All eight fonts now work offline. The six missing families were already installed at
`C:/Users/Cory/AppData/Local/Microsoft/Windows/Fonts`; ten TTF weights were converted to embedded Latin WOFF2 subsets.
The installed font metadata identifies SIL OFL 1.1 for five families. Arvo's matching copyright and OFL are confirmed at
https://github.com/google/fonts/blob/main/ofl/arvo/OFL.txt. Copyright notices and source links are embedded in src.html.
Bebas Neue and Pacifico expose only their real Regular weight. Bebas Neue always renders capitals, including with lowercase selected.
Font loading completes before raster tests; both supported weights are preloaded for the main editor's measurement.

The paper bag was redrawn with the built-in imagegen tool. Its raw PNG is `art/raw/bb-bag.png`; prompt and provenance
are in prompts.json. The other five images are preserved. The phone proof now keeps the photo and shows an enlarged
view of the same 60 px app icon. Product-only scenes remain appropriate; no people are present.

Monogram-only marks now respond to the mark transform. Lockups use the same clipped 100-unit mark window as raster tests.
Tagline measurement uses the real embedded font. Clear space is measured from actual painted lockup bounds.
Pending tests show Testing; details refuse stale revisions and mode switches. A color-only kraft failure no longer
shows a false merged-region illustration. Passing details and the all-hold wall restore the matching hint.
Repeated section taps keep controls and focus in place; queued section how-to lines must still fit the active section.

On phones all six client choices and both Brief utilities fit together. Compact cards show name, words and constraint;
the selected client's complete description and audience remain in the panel. Desktop cards and studio hero retain their finish.
Surface detail art is sized to leave the repair action visible alongside the evidence.
The final audit exposed overlapping script-font and tagline line boxes. Name descent and tagline ascent now determine
their spacing, with lockup height enlarged when needed. Long own-business names and evidence wrap in the sheet.
Sound on can recover the all-hold welcome if it was skipped while muted; event results still speak on every new result.

## Spec limitations

The missing-font limitation in the builder's original report is resolved by the cold review using local files.
No fonts or other assets were downloaded.
The spec's claim that a font is not a real brand is interpreted as avoiding proprietary brand typefaces: the named
open-source font families are real typefaces by design.
Name cap-height and script-capitals notes are implemented with the restored typefaces.

The literal no-scroll requirement for the entire Test wall at 375 px conflicts with eight large tiles in one column.
The phone wall scrolls vertically, with persistent mode controls. At 680 px, four tiles and arrows are visible together.
The van's automatic container exception is prescribed by the spec, even for a low-contrast container; it should be
reconsidered in the spec rather than silently changed in this review. No physical readability guarantee is made.

## Engine changes wanted

None requested at this point. No kit, docs or shared scripts were changed.

## Verification evidence

All commands, profiles, bar copies, frames, numerical checks and audit output are in `_scratch/brand-builder`.
`functional-results.json` records a passing and breaking setup for all eight tests, latest-change behavior,
all six brief-to-tile mappings, symbol rendering, undo/redo and actual font loading.
The final report records the remaining verification results and limitations.

The final audit is preserved in Scratch, including all 113 frames and its original 210-lead report.
`audit-disposition.md` answers every bullet and the held-click table. Floating-caption outlines and modal background
occlusion are intentional; actual target, focus, repeated-tap narration and compact-dialog issues were fixed.
`last-results.json` supersedes preliminary one-color counts in earlier probe files. It records the corrected heart's
two colored regions merging to one, the line repair, large-name/tagline contrast thresholds and an all-eight-hold setup.
`fix-routes.json` checks every repair route, including selected Ink/Primary/Secondary roles and the avatar's Mark only button.
`post-phone/results.json` verifies modal Read, restored hints, a persistent header, visible Print, and artboard/control bounds.

## Cold review verification

One complete review audit finished within its 40-minute cap: `_scratch/brand-builder/review-audit/audit.md`.
All 145 frames were viewed. The 117 raw leads consist of 100 intentional caption/modal/form rows, seven font-spacing
rows repaired as one typography issue, eight correctly skipped first-tap welcomes, and two expected no-change controls.
`_scratch/brand-builder/review-audit-disposition.md` answers every row and the control walk. Repeated taps, quick taps,
keyboard paths and resize stress completed with no runtime exceptions or stranded disabled controls.

The full audit precedes the last font-spacing, Sound-recovery and long-text repairs. Eleven scoped post-audit frames
passed with zero console errors. Script/tagline bounds are separate at all eight required sizes, Sound on recovers the
unheard all-hold line, the 60-character custom title and 160-character evidence wrap, and all phone Brief utilities fit.
Only affected states were reshot; no second full audit was run. The final audience-copy correction only shortens text.

Independent review evidence: `review-numbers.json`, `numeric-after.json`, `verify-results.json`, voice JSON logs,
`post-script-*.json`, `post-sound.json`, `post-long-sheet.json` and `post-long-phone.json` under Scratch.
Browser narration remains a disclosed limitation. The no-scroll/one-column conflict and van container shortcut remain spec questions.
All owned Chrome processes and the host server are closed; `tools/brand-builder/host.html` is removed. No commits.
