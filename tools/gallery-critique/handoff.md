# Gallery Critique build handoff

## Cold review changes

- Challenge reasons now use a native modal dialog containing the original sentence. It traps focus, supports Escape,
  and returns focus to Challenge or Withdraw challenge. The card's delegated click handler still resolves reasons.
- Failed own pins have their own event line, pointing to Cancel and menu revision. Menu changes show the complete
  sentence immediately in the hint. The voice inventory now includes fixed Read hints, panel claims and replies.
- Finish scrolls the existing Record to the editable role product and focuses it without page scrolling. Opening
  Record during a panel still starts at the transcript. Compact textareas are 110 pixels tall so the payoff fits.
- The Artist emblem was redrawn with built-in imagegen and native transparency. Its manifest uses native_alpha:true
  and cutout:false to preserve its alpha during art.py --rekey. Other active object emblems now use despill:true.
- Audit states include the finished product and an own-pin miss. Review evidence is in Scratch with review prefixes.
- The final audit confirmed Record toolbar overlap. The toolbar is now outside the scrolling Record section, which
  reserves its own 64-pixel action area. Recheck these frames directly; the single full audit predates this repair.
- During pinning the disabled zoom button is hidden, leaving the evidence-status message clear in compact layouts.
- Short landscape Panels put zoom beside a compact two-row wall label. Removing its separate top row gives the
  artwork substantially more height without shrinking controls or omitting the artist, date or medium.
- The challenge dialog describes its quoted sentence to screen readers and includes Read claim, reusing V.read(),
  because native modal focus makes the header's Read control unavailable until the dialog closes.
- No shared engine, specification, other tool, or git history was changed.

Cold review verification: one full audit completed in 1377 seconds with 39 leads; all are dispositioned in Scratch.
Targeted post-repair checks pass all 72 evidence centers and ten Record views, dialog Read with Sound off,
compact art, Finish and print frames. The voice manifest matches 94 fixed texts or segments. All test ports are
closed and host.html is removed. The full audit was not repeated after its confirmed repairs.

Original build record follows. codex-report.md describes that earlier snapshot; codex-review.md records the cold review.

## Structure

- src.html starts from the kit starter, adds theme-912 and the gallery-specific wall, frames, speech cards and record.
- content.json, loaded through the bundler's json token, holds the three work records, 36 claims, 21 image spots,
  element tables, meaning tables and judgment tables. A separate image-token map in src.html is necessary because
  bundle_tool.py substitutes art before it expands JSON. Do not move the three active art tokens into JSON alone.
- Curio.voice owns the narration queue. The tool owns the visible hint, and Read adds the currently selected card.
  Event lines are pinned, missPin, laterRound, wrongLens, struck, missChallenge and recordReady.
- state holds only in-memory work. It is never serialized. The kit may remember the shared Motion preference.
- The Gallery Critique-local Museum adapter is based on the existing sibling adapter in
  tools/art-style-match/lib/museum.min.js, read in full during the build. No shared file was changed.
- Normal painting taps zoom to the tapped point. While pinning, the whole image returns, the eight evidence targets
  appear, and only the active claim's Done/Cancel or the own-claim Done/Cancel can resolve the pin.
- Evidence buttons use a small repulsion layout when image details cluster. A leader and dot retain the exact
  evidence anchor when its numbered ring moves. Resize preserves the same buttons, focus and selected evidence.
- The Gulf Stream boat anchor is inside its visible hull at .58,.62. The Child's Bath floor anchor is on the
  visible floor at .94,.55. These builder-selected coordinates avoid misleading water or obstructed hand targets.
- Support is checked on Done. Selecting two spots succeeds when at least one is supported, as the spec says.
  For own Analyze claims, the element must belong to the chosen first spot and the second spot must differ.
- Rounds lock when advancing. Undo remains available in the current round. Finish locks Judge and opens the record.
- Small layouts page through floor claims. Menus collapse to receipts after an own claim; Add claim reopens them.
  Receipts expose the full sentence in their title and accessible name. Open Record to read all student sentences.
- Record reseeds while its text is unedited. Once edited, the text survives further panel visits. Only an edited
  product triggers the New panel discard confirmation. Printing is never blocked by length checks.

## Open questions resolved

1. The Gulf Stream and race: retain the spec's visible-evidence claims. Do not add the optional curator claim or
   introduce a new historical interpretation. Teacher notes acknowledge the topic without asserting a new source claim.
2. Support tables: use the supplied tables. All listed objects and general regions were visible in the originals;
   no rows or claims were dropped. The tables are explicitly described as bounded teaching judgments in teacher notes.

## Spec and implementation notes

- The missing family document and engine prevent a literal shared-engine import. The existing sibling's adapter
  provides the precedent for a local workaround. It is embedded in src.html to keep this folder within the allowed file list.
- No painted portraits are used. The three legacy portrait assets and prompts are retained untouched as required;
  all active speaker images are the newly generated object emblems. The five generated assets contain no people.
- Museum paintings were already present at long side 1400 pixels. They were inspected against every spot before building.
- The computed longest sentence among all panel-only Curator seed sentences is 14 words, rather than the spec's 16.
  Work totals are 98/101/95 supported words and 45/55/41 Curator seed words, matching the spec. No spec was edited.
- The exact product sentence and counts remain available on Record. Compact menus use accessible names and the
  current option text; the full own sentence appears in the hint while pinning.
- No voice recordings were made. The calm-professor voice manifest is ready; the kit falls back to browser speech.
- The user's stop instruction requires codex-report.md to be written last. Intermediate evidence stays in Scratch.

## Engine changes wanted

- File: kit/art-museum.js (absent). Functions: frame, zoomTo, unzoom, pins, label, pair and dispose.
  Add the shared engine specified by art-style-match, promoting its existing adapter after review.
- Function: pins(frame, spots, opts). Add an explicit selectable mode with autoZoom:false, selection state and onPin,
  so evidence selection can preserve the whole picture and choose up to two targets. Current sibling pins always zooms.
- File: docs/families/art-museum.md (absent). Document those APIs and the 44-pixel pin behavior, including label targets.
  The Gallery Critique build did not create or edit either shared file.

## Evidence

All temporary scripts, shots, contact sheets, Chrome profiles, arithmetic output, the bar-tool bundles and comparison
frames are in _scratch/gallery-critique/. The report names the final audit and any remaining limits.

## Audit closure

The one full audit completed in 1186.7 seconds with 104 leads. Its Motion off, resize recovery, held-click runtime,
five-click repetition and quick-tap checks were clean. All 47 audit frames were inspected.

Repairs explicitly hide closed disclosure content and the content covered by the challenge chooser, give the museum
link a 44-pixel target, name the editable product, keep Print/Back/New panel in a fixed Record toolbar, retain focus
when the compact pager reaches its end, freeze the finished lens, and stabilize utility-button widths.

Additional native hit testing found overlapping Gulf Stream phone centers and a compact Child's Bath center.
Adaptive ring layout and the corrected evidence anchors now pass all 72 center checks across the three paintings
at compact, laptop and phone sizes. Resizing preserves the selected spot and its focus; resizing during zoom also passes.

Each original audit row is answered in Scratch audit-disposition.md. The full audit was not repeated after repairs.
Only affected frames and regression checks were rerun. The Record's long text deliberately scrolls; its action
toolbar stays in view. Requiring the entire product textarea in the initial compact transcript frame was removed
from audit keep regions because a complete transcript and its editor cannot occupy that short viewport together.
