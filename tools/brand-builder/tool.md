# Brand Builder: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: brand-builder

#### Built

Built Brief, Design, Test and Sheet as one offline HTML file, with six clients and an own-business form.
The editor has 24 filled/line symbols, five containers, monograms, scale/rotation, name controls, colors, lockups and history.
Eight raster/contrast tests explain failures and jump to the relevant design control. Brands and fit notes stay local.
The sheet contains three lockups, clear space, minimum size, color ratios, typography and the student's evidence.
No git commits, shared-engine edits or polish round. The report draft began in Scratch after the first bundle.

#### Numbers check

Python recomputation of the five Look pairs: 5.1093, 5.4839, 16.5065, 7.1580 and 6.5743, matching the spec's rounding.
All eight palette mids exceed 3:1 on white; the lowest is 4.473:1. See `_scratch/brand-builder/numbers.json`.
Independent 8x shapes give circle 0.9839, filled star 0.9336, Thin ring 0.0000, Regular ring 0.8153, Heavy ring 0.9313.
Thin ring first passes at 32 px. The separately drawn fine wheat differs from the spec: 0.0000 and 104 px, rather than 0.40 and 48 px.
Exact reference paths are absent from the spec, so its illustrative raster scores cannot be reproduced bit for bit.
The tool computes its actual SVGs, never inserts reference scores. Final Thin/Heavy star setups break/hold as intended.
Final heart masks give 2 colored regions to 1 ink region at each surface's print scale; line repair gives 1 to 1.
Color masks isolate painted coverage, avoiding color classification of antialias fringes. A final all-eight run took about 24 ms.
At 3.5:1, a large name with its tagline off passes; enabling the small tagline breaks. Gray and crop thresholds are labeled tool choices.

#### Feel check

Best moment: the two-color heart becomes a single ink shape, then a heavier line repairs print and small-size behavior while leaving an icon-coverage tradeoff.
Flattest moment 1: the first one-color failure was mostly words. Added a colored/single-ink comparison with the merged region outlined.
Flattest moment 2: small swatches felt cramped. Replaced them with a full, keyboard-usable palette dialog; the brand changes immediately.
The same identity lands on five textured photos; later clients prioritize different constraints, and the sheet records the designer's choices.
Compared with Beat Lab and Snowy Mail Route. `_scratch/brand-builder/feel-comparison.jpg` places the finished wall beside Beat Lab.
The quiet studio finish follows this spec; the photographs and crisp enlarged pixels carry the visual detail.

#### Done when

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

#### Wave lessons

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

#### Audit leads

One complete audit finished with **210 raw leads**. Original report and 113 frames are preserved in `_scratch/brand-builder/audit`.
Every bullet and the held-click table are answered in `_scratch/brand-builder/audit-disposition.md` (218 bullet rows, including clean results).
Fixed: undersized mode/Read/arrows, 9 px CLIENT label, unnamed inputs, compact Brief utilities, small dialog repair buttons, focus loss, moving history, and repeated-tap speech cuts.
Fixed: phone header/footer workspace bounds, visible phone Print, minimum-size inline wrapping, correct own-dialog setup and current hints.
Fixed after numerical inspection: per-surface ink masks, color fringe artifacts, monogram-only rotation, correct sign font-size threshold, and all eight repair focus targets.
Intentional: a floating caption's box overlaps its padded field outline; values do not collide with it. Native modal dialogs cover and block their background.
Intentional: Print opens native UI, so its headless DOM does not change. A real one-page print proof verifies the action.
Open: phone lists scroll, as described above. The full audit was not repeated; only affected controls, layouts and numerical paths were rechecked.

#### Frames looked at

Every required size and mode: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and a 375x812 iframe.
Viewed the full run, all 113 audit frames in contact sheets, both bar frames, student/print frames, grayscale, Motion off, keyboard, dialogs and long-name extremes.
Viewed focused fixes in post-frames, mask-frames, ui-frames, route-frames and post-phone. Latest phone Design has artboard bottom 391 and controls bottom 751 in an 812 px viewport.
All final focused browser runs reported zero console errors, warnings or exceptions. Sound as the first held tap leaves the voice log empty.

#### Art made

Two new images and one image edit with the built-in image tool: phone, studio still life and the cleaned van. Three original photos remain unchanged.
Six WebP images total: **307.1 KiB**. Final offline bundle: **662760 bytes / 647.2 KiB**, below 2 MB.
Van redrawn once to remove the background plaque; every finished WebP was inspected at final size. Prompts, provenance and logo zones are in art/prompts.json.

#### Art still to paint

None. No people, faces or body parts were generated. No audio was recorded; the 25-line hs-narrator catalog uses browser speech fallback.

#### Engine changes wanted

None. Shared kit and audit code were left untouched.

#### Left open

- Supply local SIL OFL latin-subset WOFF2 files for Montserrat, Quicksand, Playfair Display, Arvo, Bebas Neue and Pacifico, then enable their real weights.
- Resolve the literal no-scroll requirement against the explicitly required large one-column phone wall. The build uses the latter and keeps actions visible.
- Cold review is still pending. This is a built draft, with no claim of a clean full audit after fixes.
- All owned Chrome processes and servers are closed; host.html is removed. Open-question choices are recorded in handoff.md: storefront sign for Willowmere, and Print retained.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: brand-builder

#### Played

Cold Grade 10 solo play before builder notes/source: chose a client, explored every section, tested, inspected failures,
used Fix in Design, undo/redo, own business and Sheet. Projection check and two bar tools followed. Strong studio identity.

#### Findings fixed

- **Blocker, general, Design:** six specified fonts were unavailable. Embedded ten local WOFF2 weights; all eight faces and 14 weights load offline.
- **Should fix, general, Name:** single-weight faces offered synthetic Bold; Bebas lowercase overrode its capitals-only rule. Corrected both.
- **Blocker, general, rendering/tests:** enlarged marks could paint outside the test's 100-unit window. Lockups now use the same mark window as tests.
- **Should fix, general, Mark:** monogram-only scale/rotation did nothing. Monograms now share the mark transform.
- **Should fix, general, Test:** stale details could open after a mode change, and pending rows kept old verdicts. Added revision/mode guards and Testing feedback.
- **Should fix, general, Design/voice:** repeated section taps rebuilt controls; queued how-to lines could outlive their section. Kept controls/focus and scoped validity.
- **Should fix, general, Test:** kraft contrast-only failures showed a false merged-region diagram. Draw that evidence only for an actual merge.
- **Should fix, general, Sheet:** clear-space box measured renderer padding. It now follows painted bounds, with the stated 25% margin.
- **Should fix, general, typography:** tagline width and small-name notes used rough guesses. Measure the font and both dimensions of each print zone.
- **Should fix, general, typography:** the audit found script descenders sharing the tagline's line box. Reserve the real font descent/ascent and enough lockup height.
- **Should fix, general, own business:** long unbroken names/evidence could spill from the sheet. Added wrapping and a titled compact phone heading.
- **Should fix, general, voice:** Sound on could not recover an unheard all-hold introduction. The welcome now follows the all-hold state.
- **Should fix, general, layouts:** phone client choices were hidden and a long failure could clip the repair action. All six choices fit; detail art leaves action room.
- **Should fix, general, notes/hints:** a container was proposed as an internal-color repair. Corrected the notes and passing-detail/all-hold hints.
- **Polish, general, Test:** flattest proof was the tiny phone icon. Kept its photograph and added an enlarged view of the exact icon.
- **Polish, general, graphics:** redrew the soft, flat kraft bag with paper fibers, folded gussets and directional light. Preserved the other five images.

#### Findings left

- **Should fix (spec conflict), general:** the required one-column phone Test wall scrolls; eight large photographs cannot also all fit without scrolling. Kept the explicit layout.
- **Should fix (spec rule), general:** any container passes the van test. Preserved the prescribed rule and labeled its shortcut as insufficient for WCAG compliance.

#### Flattest moment left

The brief-fit form remains the quietest step. Its notes become the student's own evidence on the sheet.

#### Graphics

Six finished images inspected, one redrawn, none missing; no people in these product mockups. Art 339.4 KiB; offline bundle 953.4 KiB.
Bag redrawn with the built-in imagegen tool; asset `art/bb-bag.webp`, full prompt `art/prompts.json`.
Phone proof enlarged; original studio palette, large artboard, textured surfaces and grayscale-safe verdict icons preserved.
Compared current Beat Lab and Snowy Mail Route frames at 1366x768 without modifying either tool.

#### Audit

One final audit completed inside 40 minutes, Chrome 9941 and host 8745: 117 raw leads, 145 frames viewed.
Seven script-spacing rows fixed; 100 caption/modal/form rows intentional; eight skipped welcomes and two no-op flags explained.
Repeated/rapid taps, keyboard paths and resize stress finished with no runtime exceptions or stranded disabled controls.
Eleven scoped post-audit frames passed with no console errors; script/tagline gap is positive at all eight sizes.
Sound recovery and maximum custom text passed. The complete audit predates these final repairs; no second full audit.
Evidence under `_scratch/brand-builder/`: `review-audit/audit.md`, `review-audit-disposition.md`, `review-frames/`, and voice/numerical JSON logs.
Independent checks: 16/16 passing/breaking test cases; all six client priorities; undo/redo; fast changes end on the final revision.
Motion off, grayscale and keyboard checks passed. All six client choices remain visible, including maximum custom text.
Five contrast pairs recomputed: 5.1093, 5.4839, 16.5065, 7.1580, 6.5743. No unresolved art tokens or tool network loads.

| Voice line | Kind | Expected | Spoken |
|---|---|---:|---:|
| nameHow, five repeated taps at 2 seconds | how | 1 | 1 |
| broke-sign, five new failures | event | 5 | 5 |
| allHold, entry plus five repairs | event | 6 | 6 |

Read interrupted speech and worked with Sound off and inside a modal. First stage/key welcomed; first Read only read; first Sound stayed silent.
The 26-line catalog matches allLines. A long voice probe exceeded the driver's 60-second evaluation cap; one smaller retry passed.

#### Left open

Recorded narration is not supplied: browser speech remains, as the no-recording build rule requires.
No classroom test. The spec's no-scroll contradiction and van-container shortcut remain documented in handoff.md.
All owned Chrome processes and servers closed; host.html removed. No git commits. The final audience-copy correction only shortens text.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Brand Builder build handoff

#### Structure

`src.html` starts from the kit starter and includes the 9-12 kit theme, overridden with the spec's light studio palette.
CSS lays out the studio at real available sizes. Content tables, SVG rendering, edit history, raster tests, dialogs,
mode renderers and Curio.voice wiring follow in that order. `window.__tool` exposes state and test hooks.
`tool.draft.json` remains a built draft. No commits or polish round were made.

#### Art and placement

The storefront and shirt FLUX photos remain unchanged. The van photo was edited with OpenAI gpt-image to remove a tiny
background plaque. Two new OpenAI gpt-image photos were made during the build: phone and studio. Cold review redrew the bag.
The studio still life introduces Brief; the other five photos receive the actual SVG identity.
`art/prompts.json` preserves the original asset records and records percentage logo zones. Raw new PNGs are under `art/raw`.
The prior van WebP is preserved in Scratch, and its source is retained in the van asset's previous_source field.
The generated phone screen is at x31%, y16%, width38%, height61%. Photos and overlays share an SVG coordinate system.
Browser tab, circle crop, newspaper, symbols and lockups are drawn in code.

#### Tests and assumptions

Tests rasterize the same SVG that students edit. The 256 px and 16 px alpha masks use a half-coverage threshold and
bilinear enlargement for intersection over union. The minimum-size search checks 16 through 256 px in 8 px steps.
No passing size through 256 is reported as such. The source's illustrative reference scores are not hardcoded.
Contrast uses WCAG relative luminance; gray conversions preserve luminance. The phone coverage excludes its background.
The avatar raster includes text and embedded fonts. One-color masks isolate each original ink color's painted coverage, then count connected
regions in the union, with 8-neighbor contact at each surface's actual simulated mark-grid print width.
Transparent holes are negative space; deliberately painted white regions count as colors.
This is a raster approximation of subpixel merging, rather than a physical ink-spread model.
Latest-change guards combine a 150 ms debounce, revision number and run token.

#### Local storage and focus

Each brief is saved in `brand-builder-brands` with try/catch. No network requests or cross-device transfer.
Own-business fields and fit notes are escaped on rendering. Reset and Clear all ask first.
Mode controls persist in the DOM; editing does not rebuild the source control. Dialogs restore focus without scrolling.
Symbol and palette grids are dialogs so every choice has a usable target even in the smallest preview.
The compact Brief view exposes own-business and clear controls in the panel; the phone header stays visible while scrolling.
History is pinned across desktop panel sections. Same-mode/client taps are idempotent so they do not cut narration.
Surface dialogs expose Read inside the native modal; short previews keep the photo, explanation and repair action side by side.
Undo and redo preserve a focusable endpoint using aria-disabled after the last available step.

#### Open questions resolved

- Willowmere uses the storefront sign. No scrubs surface was added, matching the spec's current leaning.
- Print sheet stays as a design deliverable. It does not transfer a brand between devices.

#### Cold review changes (2026-11-03)

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

#### Spec limitations

The missing-font limitation in the builder's original report is resolved by the cold review using local files.
No fonts or other assets were downloaded.
The spec's claim that a font is not a real brand is interpreted as avoiding proprietary brand typefaces: the named
open-source font families are real typefaces by design.
Name cap-height and script-capitals notes are implemented with the restored typefaces.

The literal no-scroll requirement for the entire Test wall at 375 px conflicts with eight large tiles in one column.
The phone wall scrolls vertically, with persistent mode controls. At 680 px, four tiles and arrows are visible together.
The van's automatic container exception is prescribed by the spec, even for a low-contrast container; it should be
reconsidered in the spec rather than silently changed in this review. No physical readability guarantee is made.

#### Engine changes wanted

None requested at this point. No kit, docs or shared scripts were changed.

#### Verification evidence

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

#### Cold review verification

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

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-04)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-04)
- 2026-11-25: handoff.md folded in (last changed 2026-11-04)
