# Stop-Motion Clay Shoot build handoff

## Structure
`src.html` starts from the kit starter structure. The style block lays out an animation light box and a compact control desk. The script holds content, saved state, common frame rendering, pixel differences, Rough cut, Studio, Premiere, input, and voice. `window.__tool` exposes the model and functional hooks for reproducible checks.

Frames contain set name, character coordinates and poses, props, camera offset, light multiplier and hand layer. The 100-unit coordinate system is independent of viewport size. Bumps accumulate in the saved camera offset. Check and Play consume the same saved records. A difference image subtracts actual rendered RGB pixels and maps change magnitude to lime on near black.

Rough-cut camera repair realigns all later images, including an inserted halfway pose. Light and hand repairs remove their planted problems. The missing pose must lie within 1.1 units of the midpoint and leave both movement gaps within the figure's threshold. Studio insertion uses the same test; a very large gap may need reshooting because one midpoint cannot make both halves small enough.

Wrong cause guesses close the cards and require stepping away and back before another guess. Cards rotate positions by frame and attempt. Progress records film repairs, not diagnostic mastery. Empty, single-frame and entirely still shoots cannot earn the clean-shoot message. At least one intentional pose, figure or prop change is required, alongside the continuity rules.

Studio step navigation is persistent DOM, and title-board selection updates existing controls. The compact pose bar moves into the viewer at heights up to 700 pixels, with full labels available in tooltips. Plan uses storyboard cards over the set. The irrelevant Plan frame counter is hidden. Redundant onward buttons are hidden in favor of the persistent step controls. Start over remains in Rough cut and clears work in every mode.

The set choice applies to the whole film. It changes each saved frame's set name, keeping the backdrop consistent rather than silently permitting a mid-film scenery jump. Thumbnail images are cached, and the strip follows the current photograph without scrolling the page.

## Spec decisions and conflicts
- No open questions were listed. Unattended choices follow the supplied examples.
- The enumerated Art section contains 21 assets, though its total says 20. All 21 are generated and used.
- The explicit durations win: on twos is 6 captured frames per second; on ones is 12. The spec's production terminology is inconsistent with conventional 24-fps playback. Teacher notes explain it.
- The hand trigger is 1.5 seconds. Its fix text is adjusted from one second to one and a half seconds to match the actual rule.
- CODEX-BUILD requests an early report, but the user's stronger instruction says to stop when it is written. The report is created only after the checks.
- BUILD's older no-art instructions and the spec's FLUX suggestion are superseded by the user's explicit instruction to generate artwork with the image tool.
- Images use magenta keys, including green subjects, and record `people: false`. The only hand is a gray code silhouette. No generated people.
- The bar tools were bundled as CODEX-BUILD asked, before recognizing that generated outputs also fall outside the user's write boundary. No source files in other tools were edited. Their ignored bundles were regenerated; this is a recorded process deviation.

## Voice
Curio.voice owns the queue and once-only how lines. The tool changes hints synchronously. `voice/lines.json` prepares firm-captain / Alnilam. No audio recordings were made. Browser voices determine the actual spoken timbre until the owner records the lines.

## Sensitivity
Friendly fictional clay animals, original toy scenery and a generic filming-hand silhouette. No cultural, religious, historical or human-body teaching content. No people images require a contact review.

## Engine changes wanted
None. No shared kit or engine changes were made.

## Next review
Use the report and Scratch evidence for cold review. Reviewers should pay particular attention to the spec's timing vocabulary, compact-panel scrolling, the quality of the generated pose set, and the difference between a clean technical check and a compelling animated story. This run is Build only, with no commit or polish round.

The one mechanical audit was interrupted by the session restart. Its saved partial report contains 30 leads. Completed targeted checks address its layout findings; the full automated walk and remaining state/resize coverage are still open for the cold reviewer. The full audit was not restarted, following the one-audit build instruction.

## Cold review repairs
Premiere now always projects the full-color film, even after Check leaves Finder on. Current-state speech interrupts stale queued hints;
the twelfth-frame Check instruction stays on screen until used. Wren's in-between instructions name the selected figure.
Props have keyboard positioning on their existing buttons. The technical result explicitly states its four checked dimensions;
it does not certify prop continuity or story quality. Equivalent prop arrays no longer count as animation merely because their order changed.
Setup's existing painting now shows the selected window/blinds, tripod tape and remote. The wooden title slab was redrawn with native alpha.
Its manifest uses cutout:false to preserve that alpha through the required art.py rekey resize, rather than keying an already transparent PNG.
The source timing remains the spec's 6 unique pictures per second on twos; conventional production terminology remains a spec issue.
The rough-cut retry can still be guessed by cycling causes after stepping away and back. A separate evidence or transfer gate would change
the prescribed interaction; this is left explicit for the spec owner rather than adding a new quiz during review.

Teaching repair tips now use once-only how narration. Wren selection has its own current-figure shooting hint.
Scene labels describe the pixels actually shown, including Setup and live posing with Finder selected.

## Cold audit disposition
The single review audit used debugging port 9961, host 8765 and a 2,400-second process limit. It exited before the first
frame with ConnectionResetError, WinError 64, during the CDP WebSocket handshake. It wrote no audit.md and was not retried.
The review's independent screenshots, 13 functional assertions, reload comparison, complete default voice path and side
voice/keyboard checks are in Scratch's review-* artifacts. These do not establish completion of the automated resize,
every-control or all-state-at-all-size walk. All assigned ports were closed and host.html was removed before reporting.
